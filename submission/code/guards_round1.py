"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("Không có chính sách hiệu lực: cần người xác minh")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action["tool"]
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if order is None or order["customer_id"] != ctx.ticket["customer_id"]:
        return Verdict.escalate("Không xác minh được chủ đơn")
    if action.get("ticket_id") != ctx.ticket["ticket_id"]:
        return Verdict.escalate("Lệnh ghi không khớp ticket")
    if tool != "notify_carrier" and action.get("order_id") != order["order_id"]:
        return Verdict.escalate("Lệnh ghi không khớp đơn")
    if not order.get("parcels"):
        return Verdict.escalate("Thiếu tracking kiện hàng")
    pid = ctx.ticket.get("parcel_id")
    if pid and not any(p["parcel_id"] == pid for p in order["parcels"]):
        return Verdict.escalate("Kiện yêu cầu không thuộc đơn")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("Không có chính sách hiệu lực")
    delay = H.db_delay_days(parcel, ctx.as_of)
    limits = ctx.tools.ops_limits()

    # G1: money and authority come from DB/policy, never the customer's text.
    if tool == "issue_refund":
        if parcel.get("delay_cause") is None and delay > 0:
            return Verdict.escalate("Thiếu nguyên nhân trễ: xác minh trước hoàn")
        entitlement = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        if paid >= entitlement or entitlement <= 0:
            return Verdict.deny("DB/chính sách không có quyền lợi còn phải hoàn")
        amount = entitlement - paid
        approval_id = action.get("approval_id")
        approved = False
        if approval_id:
            approved = any(
                a.get("status") == "valid"
                and a.get("expires_at", "") >= ctx.as_of
                and a.get("max_vnd", 0) >= amount
                and bool(a.get("approver_id"))
                and (not ctx.gates.get("operations", {}).get("approver_id")
                     or a["approver_id"] == ctx.gates["operations"]["approver_id"])
                for a in ctx.tools.lookup_approvals(
                    approval_id=approval_id, ticket_id=ctx.ticket["ticket_id"],
                    order_id=order["order_id"], customer_id=order["customer_id"])
            )
            if not approved:
                return Verdict.escalate("Phê duyệt sai phạm vi, hết hạn hoặc vượt hạn mức")
        customer_total = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(
            customer_id=order["customer_id"]) if not r.get("approval_id"))
        if not approved and (amount > policy["auto_limit_vnd"] or customer_total + amount >
                             limits["max_auto_refund_per_customer_per_day_vnd"]):
            return Verdict.escalate("Vượt hạn mức tự động: cần Hạnh duyệt")
        if not approved and ctx.tools.auto_refund_today_vnd() + amount > limits["daily_auto_refund_budget_vnd"]:
            return Verdict.escalate("Vượt ngân sách Finance trong ngày")
        if any(action.get(k) != v for k, v in {
                "amount_vnd": amount, "payer": "LOGIX", "basis": "policy"}.items()):
            return Verdict.modify("Quyền lợi từ DB/chính sách, không theo lời khai",
                                  amount_vnd=amount, payer="LOGIX", basis="policy")

    # G2: strike the actual parcel/carrier only when the recorded cause supports it.
    elif tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("Tracking/chính sách không đủ căn cứ ghi lỗi hãng")
        if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
            return Verdict.deny("Kiện đã được ghi lỗi; không ghi lặp")
        if len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limits["max_auto_strikes_per_carrier_per_day"]:
            return Verdict.escalate("Từ lỗi thứ ba của hãng trong ngày: Hạnh xác minh")
        changes = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                   "driver_id": parcel.get("driver_id"), "delay_days": delay}
        if any(action.get(k) != v for k, v in changes.items()):
            return Verdict.modify("Ghi lỗi đúng tracking của kiện", **changes)

    # G3: reconstruct an allowlisted notice from facts, including nested PII removal.
    elif tool == "notify_carrier":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("Không có căn cứ thông báo lỗi hãng")
        payload = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                   "district": order["recipient"]["district"], "delay_days": delay}
        return Verdict.modify("Chỉ gửi dữ liệu nghiệp vụ; bỏ nội dung tự do và liên hệ người nhận",
                              carrier_id=parcel["carrier_id"], payload=payload)
    return Verdict.allow()
