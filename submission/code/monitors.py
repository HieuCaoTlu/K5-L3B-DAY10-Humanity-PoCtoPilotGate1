"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def cause_missing_rate(trials):
    """S3 (dữ liệu THIẾU): trong các ticket có tra tracking, bao nhiêu phần kiện trễ chưa ghi nguyên nhân (delay_cause)?

    Không cần nhãn: đọc thẳng sự kiện `tracking`. Tăng lên nghĩa là kho/hãng nhập tracking thiếu, hệ thống sẽ đứng trước
    lựa chọn mặc định (nghiêng về khách hay về hãng). Điểm mù: không thấy nguyên nhân ghi SAI (có điền nhưng điền nhầm)."""
    seen = missing = 0
    for t in trials:
        for e in t["events"]:
            if e.get("type") == "tracking":
                seen += 1
                missing += e.get("cause_recorded") is False
    return missing / max(1, seen)


def fault_write_blocked_rate(trials):
    """S3 (tác hại lên bên thứ ba): bao nhiêu phần ticket bị cổng chặn lệnh ghi lỗi hãng (thiếu căn cứ, chạm trần lỗi
    trong ngày, sai kiện)? Số này tăng khi chính sách đổi hoặc tracking thiếu. Điểm mù: không phân biệt chặn đúng và chặn nhầm."""
    blocked = sum(
        any(e.get("type") == "gate" and e.get("tool") == "file_carrier_fault" and e.get("action") in ("deny", "escalate")
            for e in t["events"])
        for t in trials)
    return blocked / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "cause_missing_rate": cause_missing_rate,
    "fault_write_blocked_rate": fault_write_blocked_rate,
}
STARTER_MONITORS = ("escalation_rate",)
