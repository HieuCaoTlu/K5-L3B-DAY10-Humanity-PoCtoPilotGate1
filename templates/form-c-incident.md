# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-Humanity-PoCtoPilotGate1 · **Thẻ đã bốc:** S3 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S3-prepared-20261119-162914-5516f2` | S3 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0,6667 (CI [0,4167; 0,9167]) | 0,6667 | 0đ · 0 · 0 | 41,7% | Cổng vòng 1 chặn hết hoàn sai (900.000đ về 0) và lỗi oan (35 về 0), nhưng còn 4/12 ticket sai (S3-20, 21, 42, 43) và ROI 0,3 < 0,5. |
| 2 | `R-S3-after-20261119-163028-6da223` | S3 · after | ticket thiếu nguyên nhân trễ vẫn hoàn cho khách (bỏ chuyển người), không ghi lỗi hãng | 0,8333 (CI [0,5833; 1,0]) | 0,8333 | 0đ · 0 · 0 | 25% | S3-20, 21 về đúng; còn S3-42, 43. Chi phí 6.055đ vẫn > 6.000đ. |
| 3 | `R-S3-after-20261119-163043-d40733` | S3 · after | hãng chạm trần lỗi trong ngày thì chặn riêng lệnh ghi lỗi (deny), không chuyển cả ticket | 1,0 (CI [1,0; 1,0]) | 1,0 | 0đ · 0 · 0 | 8,3% | Hết ticket hỏng. Chi phí 4.405đ, ROI 1,27, hết vượt trần. |
| 4 | `R-base-after-20261119-163102-817d2f` | base · after | (kiểm không regression; code đã có thêm 2 monitor) | 1,0 (CI [1,0; 1,0]) | 1,0 | 0đ · 0 · 0 | 22,7% | Bộ nền không hỏng ca nào. Monitor mới đo 0,0 trên bộ nền. |
| 5 | `R-S3-after-20261119-163101-817d2f` | S3 · after | thêm 2 monitor (`cause_missing_rate`, `fault_write_blocked_rate`) | 1,0 | 1,0 | 0đ · 0 · 0 | 8,3% | Chỉ thêm đo, không đổi hành vi. Cả hai monitor sáng đèn trên thẻ (0,1667 và 0,3333). |
| 6 | `R-S3-grade-20261119-163112-817d2f` | S3 · base/prepared/after | (grade cuối, ba mốc: base `R-S3-before-20261119-163113-817d2f`, prepared `R-S3-prepared-20261119-163113-817d2f`, after `R-S3-after-20261119-163113-817d2f`) | 1,0 | 1,0 | 0đ · 0 · 0 | 8,3% | `PASS-VISIBLE`: 5 mục kiểm đạt, mục 4 (bài ẩn) do team chấm chạy. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S3-grade-20261119-162914-5516f2` · base: `R-S3-before-20261119-162914-5516f2` · prepared: `R-S3-prepared-20261119-162914-5516f2` (chạy trước khi sửa bất cứ thứ gì. Lần grade đầu tiên báo `1 integrity ❌` do Git trên Windows đổi dòng LF thành CRLF, không phải do bài; đã ghi lại 23 file khóa về đúng LF rồi chạy lại)
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): trên gói sự cố, tiền hoàn sai 900.000đ về 0 (S3-04: 180.000đ vượt hạn mức tự động mới 100.000đ, nhãn là chuyển người); lỗi hãng ghi oan 35 về 0 (S3-01 đến S3-05: trễ do bão FORCE_MAJEURE vẫn bị ghi lỗi); pass_rate 0,25 lên 0,6667; ticket hỏng từ 9 xuống 4. Nguyên nhân đỡ được: `pre_guard` ghim chính sách theo ngày hiệu lực (REFUND-v4) và `carrier_at_fault` chỉ ghi lỗi khi nguyên nhân thuộc `fault_causes`.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: có. Ở mốc prepared trên gói sự cố: ROI 0,3 < 0,5 và chi phí 7.688đ > 6.000đ (đã ký), cùng pass_rate 0,6667 < 0,97 và pass_k 0,6667 < 0,95. Nguyên nhân của hai dòng tiền không nằm ở tiền máy (tiền LLM lớn nhất 771đ < 1.500đ) mà ở tỉ lệ chuyển người 41,7% (mỗi ca chuyển tốn 10.000đ công).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chủ yếu **kỹ thuật** (dữ liệu đổi mà hệ thống chưa đổi theo: concept drift và dữ liệu thiếu), kéo theo **pháp lý và kinh doanh** (hãng bị phạt oan 120.000đ/lỗi, trái phụ lục hợp đồng) và **vận hành** (ca chuyển người dồn).
- Có nằm trong các lý do bàn đã viết không? **Không nằm trực tiếp.** B6 có 5 lý do: tin lời khai, chi phí, hàng chờ, dữ liệu gửi hãng, tracking sai từ nguồn. Lý do gần nhất là "tracking sai từ nguồn" nhưng nói về tracking ghi sai, không nói về luật nghiệp vụ đổi theo ngày hay tracking để trống. Vì sao cả bàn không nghĩ tới: bộ nền chỉ có một phiên bản chính sách hiệu lực (v3) nên cả bàn coi chính sách là hằng số; B3 chỉ ghi "chính sách đổi" chung chung và chưa biến thành cổng hay chỉ số. Cổng vòng 1 vẫn đỡ được phần lớn (pass_rate 0,25 lên 0,6667) nhờ `pre_guard` ghim theo ngày, nhưng đó là hệ quả của thiết kế chung chứ không phải bàn đã lường trước sự cố này.
- Lý do còn thiếu, thêm bây giờ (bút khác màu):

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Chính sách đã đổi ngày 01/12 nhưng hệ thống vẫn chạy luật cũ vì cờ `index_active` do batch cập nhật chậm | Kỹ thuật | `data/world.json` → `policies`: REFUND-v3 `index_active: true`, REFUND-v4 `index_active: false` dù hiệu lực từ 2026-12-01; trace `S3-02@11` (base): `policy REFUND-v3 pinned: false`, `as_of` 2026-12-02 |
| Tracking đã để trống nguyên nhân trễ và hệ thống mặc định về một phía mà không ai chọn | Kỹ thuật, pháp lý | `S3-20@11`, `S3-21@11`: `cause_recorded: false`, `delay_cause: null` |
| Hãng chạm trần lỗi trong ngày làm cả ticket chuyển người dù khoản hoàn đã ghi, dồn việc cho người duyệt | Con người và vận hành | `S3-42@11`: sổ cái 47.400đ nhưng `status escalated`; `ops_limits.max_auto_strikes_per_carrier_per_day = 2` |
| Hãng bị phạt oan mà không ai bên LogiX xác nhận, đối tác ký phụ lục rồi vẫn bị phạt | Kinh doanh, pháp lý | Tin nhắn trên thẻ; `carriers`: MKD phạt 120.000đ/lỗi, đình chỉ sau 5 lỗi/7 ngày; base: 35 lỗi oan |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `hãng Mekong Delta Ship (MKD) và tài xế bị phạt 120.000đ/lỗi (cả DNB 80.000đ/lỗi); khách trễ 2 ngày bị từ chối hoàn` · đo bằng gì `wrongful_carrier_faults (lỗi hãng oan), wrongful_refund_vnd (tiền hoàn sai), under_refund_vnd (hoàn thiếu cho khách), pass_rate` · bao nhiêu ở mốc base `35 lỗi hãng oan, 900.000đ hoàn sai, 667.000đ hoàn thiếu, pass_rate 0,25 (60 lượt chạy)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S3-01@11` (base): tracking `cause: FORCE_MAJEURE` (bão số 9), `policy REFUND-v3 pinned: false`; sổ lỗi hãng có `MKD / O-2301-P1 / TX-MKD-07 / delay 4`; nhãn đúng là không ghi lỗi hãng (`faults: []`) | Hãng MKD và tài xế `TX-MKD-07` chịu phạt 120.000đ; khách không thấy gì sai; không ai trong LogiX nhận ra | cao | **chìm** |
| 2 | `S3-02@11` (base): tracking trễ 2 ngày do CARRIER, `proposal amount_vnd: 0`, `basis policy` theo v3 (cần từ 3 ngày); nhãn đúng là hoàn 18.000đ và ghi lỗi GHSH | Khách bị từ chối hoàn trong khi thông báo chính sách mới nói từ 2 ngày là được hoàn | cao | ngữ cảnh |
| 3 | `S3-20@11` (base): `cause_recorded: false`, `delay_cause: null` mà vẫn `file_carrier_fault` cho MKD (`delay 3`); nhãn đúng là hoàn 22.000đ và **không** ghi lỗi. Ở mốc prepared cổng vòng 1 chặn nhầm ngược lại: `gate escalate "Thiếu nguyên nhân trễ"`, khách mất khoản hoàn | Base: hãng MKD chịu oan. Prepared: khách bị từ chối, người duyệt nhận thêm ca | cao | **chìm** (base), giới hạn hệ thống (prepared) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | không (ticket không khai số ngày; `trust_claim: false`) | không | không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✔ (bản chính sách dùng là bản cũ, dữ liệu "phiên bản hiệu lực" lỗi thời) | ✔ (cùng gốc: ngưỡng 3 ngày của v3 thay vì 2 ngày của v4) | ✔ (`delay_cause` trống) |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | ✔ (hai nơi cùng nói phiên bản nào hiệu lực: ngày `effective_from/to` và cờ `index_active`) | ✔ (cùng gốc) | không |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | không | không | không |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Điều phối MKD đã ký phụ lục: trễ do bão thì không ghi lỗi hãng; mỗi lỗi oan là 120.000đ và gần đủ 5 lỗi/7 ngày để bị đình chỉ | Thông báo chính sách mới ghi từ 2 ngày là được hoàn; CSKH thấy trợ lý từ chối | Base: hãng bị ghi lỗi khi tracking chưa có nguyên nhân. Prepared: khách đủ điều kiện nhưng bị chặn hoàn |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Khác (cổng chặn): ghim chính sách theo ngày và chỉ ghi lỗi hãng khi nguyên nhân thuộc `fault_causes` | Khác (cổng chặn): ghim v4 thì ngưỡng 2 ngày áp dụng ngay | Phản hồi: hoàn cho khách theo quyền lợi từ DB; không ghi lỗi hãng khi thiếu nguyên nhân; để vết cho người xác minh |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Lỗi hãng không được ghi; nếu hãng khiếu nại, NV-OANH đối soát theo tracking và nguyên nhân | Khách được hoàn đúng 18.000đ và trả lời ngay | Khách được hoàn tự động; ca thiếu nguyên nhân được NV-OANH rà trong đối soát tuần để bổ sung `delay_cause` |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `fault_write_blocked_rate` | `escalation_rate` (có sẵn) và `fault_write_blocked_rate` | `cause_missing_rate` |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `policies[].effective_from` / `effective_to` | Nguồn sự thật (B3 ghi "hiệu lực/chế độ chính sách" là trường then chốt) | Xác nhận: đây là nguồn sự thật về phiên bản đang hiệu lực, so với `as_of` (2026-12-02 nên REFUND-v4) | `pre_guard` ghim theo ngày nên dùng v4: ngưỡng 2 ngày, hạn mức tự động 100.000đ, FORCE_MAJEURE không còn ghi lỗi hãng |
| `policies[].index_active` | **Chưa hỏi** (không có trong B3) | **Bản sao** do batch cập nhật, chậm: v3 vẫn `true`, v4 `false` dù đã hiệu lực từ 01/12 | Nếu tin cờ này thì dùng v3: ghi lỗi hãng khi bão (35 lỗi oan), từ chối khách trễ 2 ngày, hoàn 180.000đ vượt hạn mức mới (900.000đ hoàn sai) |
| `parcels[].delay_cause` | Nguồn sự thật, **chưa hỏi "nếu trống thì nghiêng về phía ai"** | Có thể trống (S3-20, S3-21: `cause_recorded: false`) | Base nghiêng về hãng chịu thiệt (ghi lỗi oan); vòng 1 nghiêng về khách chịu thiệt (chặn hoàn). Cách đúng: hoàn cho khách, không ghi lỗi hãng |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault` (kèm `issue_refund` ở dòng 1, 2 và 4)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `policies` (phiên bản hiệu lực) | INVALID | `S3-01` đến `S3-05`: phiên bản v3 hết hiệu lực từ 2026-12-01 nhưng cờ `index_active` còn `true` | Hãng bị ghi lỗi khi bão (MKD, 120.000đ/lỗi); khách trễ 2 ngày bị từ chối; hoàn 180.000đ vượt hạn mức mới | Vòng 1: `pre_guard` ghim theo ngày hiệu lực (đã đỡ) | Giữ `pre_guard`; theo dõi bằng `fault_write_blocked_rate` khi chặn tăng sau ngày đổi chính sách. Tầng: chặn |
| `parcels[].delay_cause` | INCOMPLETE | `S3-20@11`, `S3-21@11`: `delay_cause: null`, `cause_recorded: false` | Base: hãng ghi oan. Vòng 1: khách bị chặn hoàn | Vòng 1: `carrier_at_fault` chặn ghi lỗi (đỡ); nhưng `issue_refund` cũng `escalate` (chặn nhầm khách) | Hoàn theo quyền lợi từ DB khi thiếu nguyên nhân; không ghi lỗi hãng; monitor `cause_missing_rate`. Tầng: chặn + phát hiện |
| Số lỗi đã ghi cho hãng trong ngày (`fault_rows`) | WRONG | `S3-42@11`, `S3-43@11`: MKD đã có 2 lỗi (S3-40, S3-41) nên lỗi thứ 3 chạm trần; cổng vòng 1 `escalate` sau khi `issue_refund` đã ghi sổ (47.400đ) nên `status` thành `escalated` trong khi tiền đã hoàn. **Nhánh bàn chưa thấy trên trace lúc viết HAZOP vòng 1** | Khách C-06, C-08 nhận hoàn nhưng ticket báo chuyển người (không nhất quán); người duyệt nhận thêm ca; ROI 0,3 | Vòng 1: `escalate` trong `write_gate` nhánh `file_carrier_fault` (chính nó gây lỗi) | Đổi thành `deny` riêng lệnh ghi lỗi, để vết `fault_deferred_strike_cap`, theo dõi bằng `fault_write_blocked_rate`. Tầng: giới hạn thiệt hại |
| `auto_limit_vnd` của chính sách | INVALID | `S3-04`: hoàn 180.000đ, v3 cho tự động (≤ 200.000đ), v4 chỉ ≤ 100.000đ; nhãn là chuyển người | LogiX hoàn vượt hạn mức mới; 900.000đ hoàn sai ở base (5 seed) | Vòng 1: hạn mức đọc từ chính sách ghim theo ngày (đã đỡ) | Giữ cổng hạn mức trong `write_gate` nhánh `issue_refund`. Tầng: chặn |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **Lệnh ghi lỗi hãng chỉ được thực hiện khi, theo phiên bản chính sách có hiệu lực vào ngày hôm nay, số ngày trễ theo tracking ≥ `min_days_fee` VÀ `delay_cause` đã được ghi VÀ thuộc `fault_causes` của phiên bản đó (REFUND-v4: chỉ `CARRIER`, không `FORCE_MAJEURE`); và số lỗi tự ghi cho một hãng trong ngày không quá 2.** Nếu vi phạm: hãng bị phạt oan (35 lỗi ở base).

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `pre_guard` (ghim chính sách theo ngày qua `H.effective_policy`) và `write_gate` nhánh `file_carrier_fault` (`H.carrier_at_fault`, đếm `fault_rows` theo hãng); trong report đọc `wrongful_carrier_faults` (phải bằng 0) và monitor `fault_write_blocked_rate`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): **Kho và hãng luôn nhập đủ `delay_cause` vào tracking, và bảng `policies` luôn được cập nhật đúng và đúng ngày khi chính sách đổi.**

Vì sao có thể sai: `delay_cause` do người ở kho và hãng nhập, có thể nhập muộn hoặc bỏ trống (S3-20, S3-21); cờ `index_active` do batch đêm cập nhật và đã chậm đúng ngày đổi chính sách (v4 hiệu lực 01/12 nhưng cờ vẫn `false`). Phần mềm không kiểm soát được hai việc này.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S3-before-20261119-162914-5516f2` và `R-S3-prepared-20261119-162914-5516f2`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: hãng MKD bị ghi lỗi và phạt oan (120.000đ/lỗi) và khách trễ 2 ngày bị từ chối hoàn
        (cho ai: hãng, tài xế, khách; đo bằng: wrongful_carrier_faults, under_refund_vnd; base 35 lỗi, 667.000đ)
 └─ HOẶC
 ├─ [1] Hệ thống chạy luật cũ REFUND-v3 sau ngày 01/12              tầng: data
 │ └─ vì: cờ index_active (bản sao, batch cập nhật chậm) báo v3 còn hiệu lực   bằng chứng: S3-01@11, S3-02@11 (policy v3 pinned false)
 ├─ [2] Ghi lỗi hãng khi tracking chưa có nguyên nhân trễ            tầng: đầu vào / data
 │ └─ vì: delay_cause trống, hệ thống mặc định nghiêng về hãng chịu thiệt     bằng chứng: S3-20@11, S3-21@11 (cause_recorded false)
 ├─ [3] Chạm trần lỗi hãng trong ngày: cổng chuyển cả ticket sau khi hoàn đã ghi   tầng: hành động / vận hành
 │ └─ vì: write_gate dùng escalate thay vì deny riêng lệnh ghi lỗi    bằng chứng: S3-42@11, S3-43@11 (prepared: sổ cái có hoàn nhưng status escalated; escalation 41,7%, ROI 0,3)
 └─ [4] Không có chỉ số nào cho thấy lỗi hãng bị chặn hoặc tracking thiếu    tầng: vận hành
   └─ vì: monitors.py chỉ có escalation_rate    bằng chứng: grade lần đầu, mục 6 monitor ❌ ("metric mới: CHƯA CÓ")
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Phiên bản chính sách dùng phải là bản có `effective_from ≤ ngày hôm nay ≤ effective_to`, không dựa vào `index_active` | Giả định sai: "bảng `policies` và cờ `index_active` luôn được cập nhật đúng ngày đổi chính sách" |
| [2] | Chỉ ghi lỗi hãng khi `delay_cause` đã ghi và thuộc `fault_causes`; thiếu nguyên nhân thì không phạt hãng và không từ chối khách | Giả định sai: "kho và hãng luôn nhập đủ `delay_cause`" |
| [3] | Chạm trần lỗi trong ngày thì chặn riêng lệnh ghi lỗi hãng; khoản hoàn đã ghi vẫn giữ và trạng thái ticket phải nhất quán với sổ cái | Giả định sai: "người duyệt luôn kịp nhận ca chuyển" (1 người, 6 ca/giờ) |
| [4] | Mỗi lệnh ghi bị chặn phải để lại một chỉ số đo được cho người vận hành | Giả định sai: "nếu có chuyện, người trực sẽ tự nhìn thấy" |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Luật cũ v3 còn chạy sau 01/12 | `pre_guard`: `H.effective_policy(lookup_policies(), ctx.as_of)` và `Verdict.allow(policy_id=...)` (đã có từ vòng 1, không sửa thêm) | chặn | **NGĂN** nhánh "đọc nhầm phiên bản", miễn là bảng `policies` có đủ phiên bản và `as_of` đúng; còn hở nếu bảng thiếu bản mới | `R-S3-prepared-20261119-162914-5516f2` (đã đỡ ở mốc prepared) |
| [2] | Ghi lỗi hãng và/hoặc chặn hoàn khi thiếu `delay_cause` | `write_gate` nhánh `issue_refund`: bỏ `escalate` khi `delay_cause` trống, hoàn theo `entitlement_vnd` và ghi `ctx.log("cause_missing_refund_kept")`; nhánh `file_carrier_fault` giữ `carrier_at_fault` (thiếu nguyên nhân thì `deny`) | chặn | **NGĂN** việc ghi oan hãng (không có nguyên nhân thì không ghi). Chỉ **GIẢM** rủi ro hoàn nhầm: ca `CUSTOMER_ABSENT` chưa được ghi vẫn có thể được hoàn (tối đa phí ship, ≤ 24.000đ ở S3) | `R-S3-after-20261119-163028-6da223` (S3-20, S3-21 về đúng) |
| [3] | Chạm trần lỗi hãng làm cả ticket chuyển người | `write_gate` nhánh `file_carrier_fault`: đổi `escalate` thành `deny` + `ctx.log("fault_deferred_strike_cap")` | giới hạn thiệt hại | **NGĂN** việc tự ghi lỗi hãng thứ ba trong ngày. Chỉ **GIẢM** khả năng người xác minh: `deny` không tạo ca trong hàng chờ nên Hạnh chỉ thấy qua nhật ký và monitor | `R-S3-after-20261119-163043-d40733` (S3-42, S3-43 về đúng; ROI 0,3 lên 1,27) |
| [4] | Không có chỉ số theo dõi | `monitors.py`: thêm `cause_missing_rate` và `fault_write_blocked_rate`, đăng ký vào `MONITORS` | phát hiện | **GIẢM** (chỉ phát hiện, không chặn gì) | `R-S3-after-20261119-163101-817d2f`; kiểm bộ nền `R-base-after-20261119-163102-817d2f` |

**Không sửa `config/operating_gates.json`.** Nguyên nhân là logic và dữ liệu, không phải con số: ROI 0,3 và chi phí 7.688đ ở mốc prepared đến từ 41,7% ticket bị chuyển người (mỗi ca 10.000đ công), nên hết chuyển nhầm thì tự về ROI 1,27 và 4.405đ. Mỗi lần chạy chỉ đổi một thứ (xem `--note` ở C0). Không sửa nhắm vào ID ticket hay câu chữ: cả ba chỗ sửa đọc nguồn sự thật (tracking, chính sách, sổ lỗi).

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | (1) `cause_missing_rate` · (2) `fault_write_blocked_rate` |
| **Bước / hành vi được đo** | (1) Bước tra tracking: kiện trễ mà chưa có nguyên nhân. (2) Bước ghi lỗi hãng: lệnh `file_carrier_fault` bị cổng chặn |
| **Thước đo** (một câu, có đơn vị) | (1) Tỉ lệ các lần tra tracking có `cause_recorded = false`, đơn vị: %. (2) Tỉ lệ ticket có lệnh ghi lỗi hãng bị cổng chặn (`deny` hoặc `escalate`), đơn vị: % ticket |
| **Dữ liệu** (trường nào của trial, không có nhãn) | (1) sự kiện `tracking` trong `trial["events"]`, trường `cause_recorded`. (2) sự kiện `gate` có `tool = file_carrier_fault` và `action` là `deny` hoặc `escalate`. Không cần nhãn đúng/sai |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | (1) số sự kiện `tracking` có `cause_recorded = false` / số sự kiện `tracking`; mẫu số 0 thì trả 0. (2) số ticket có ít nhất một sự kiện `gate` chặn lỗi hãng / tổng số ticket trong cửa sổ; một ticket chỉ đếm một lần |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ 24 giờ, soát lúc đóng ca. **Đã đề xuất (chưa có dữ liệu thật để kiểm):** (1) VÀNG ≥ 5%: NV-OANH hỏi kho/hãng bổ sung nguyên nhân; ĐỎ ≥ 15% hoặc hãng nào có ≥ 3 ca trống trong ngày: NV-TUNG xem lại có tắt `file_carrier_fault` không. (2) VÀNG > 10%: NV-HANH xem nhật ký `fault_deferred_strike_cap`; ĐỎ > 25% hoặc một hãng chạm trần 2 lần trong ngày: NV-TUNG và NV-HANH xác minh với hãng |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | (1) Không thấy nguyên nhân bị ghi SAI (có điền nhưng điền nhầm). (2) Không phân biệt chặn đúng với chặn nhầm; không thấy lỗi hãng đáng ghi mà chưa bị đưa vào hàng đợi |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | (1) bộ nền 0,0 · thẻ 0,1667. (2) bộ nền 0,0 · thẻ 0,3333 (mốc after, report `grade` cuối `R-S3-grade-20261119-163112-817d2f`; mục `6 monitor ✅`) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S3-after-20261119-163113-817d2f`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Hãng MKD bị ghi lỗi và phạt oan; khách trễ 2 ngày bị từ chối hoàn
 └─ HOẶC
 ├─ [1] Hệ thống chạy luật cũ v3 sau 01/12 VÀ [pre_guard ghim theo ngày hỏng]
 ├─ [2] Ghi lỗi hãng khi thiếu nguyên nhân trễ VÀ [carrier_at_fault trong write_gate hỏng]
 ├─ [3] Chạm trần lỗi hãng làm khách mất hoàn VÀ [deny riêng lệnh ghi lỗi hỏng]
 └─ [4] Không thấy lỗi hãng bị chặn VÀ [monitor fault_write_blocked_rate / cause_missing_rate không báo]  (còn hở: chỉ phát hiện)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `pre_guard` (`H.effective_policy`) | chặn | **Ngăn**: không đọc `index_active` | Hở nếu bảng `policies` thiếu bản v4 hoặc `as_of` sai |
| [2] | `write_gate` nhánh `file_carrier_fault` (`H.carrier_at_fault`); `issue_refund` không chặn khi thiếu nguyên nhân | chặn | **Ngăn** ghi oan hãng. **Giảm** rủi ro hoàn nhầm cho ca `CUSTOMER_ABSENT` chưa ghi | Hở khi nguyên nhân bị ghi SAI (có điền nhưng điền nhầm) và khi ca hoàn nhầm cho khách vắng nhà |
| [3] | `write_gate` nhánh `file_carrier_fault` (`deny` + `ctx.log`) | giới hạn thiệt hại | **Ngăn** tự ghi lỗi thứ ba; **giảm** việc đưa ca tới người xác minh | Hở: ca lỗi thứ ba không vào hàng chờ của Hạnh, chỉ thấy qua nhật ký và monitor |
| [4] | `monitors.py`: `fault_write_blocked_rate`, `cause_missing_rate` | phát hiện | **Giảm** (chỉ phát hiện, không chặn) | Hở: ngưỡng báo động mới đã được đề xuất, chưa đo trên dữ liệu thật |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tracking thiếu hoặc ghi sai `delay_cause`: hoàn nhầm cho ca khách vắng nhà chưa ghi, hoặc phạt hãng sai nguyên nhân | Trung bình | Tiền nhỏ mỗi ca (phí ship ≤ 24.000đ ở S3) nhưng hãng chịu phạt 120.000đ/lỗi, MKD bị đình chỉ sau 5 lỗi/7 ngày | Phạm Kiều Oanh / NV-OANH | `cause_missing_rate` ≥ 5% trong 24 giờ | NV-OANH rà đối soát tuần, bổ sung nguyên nhân cùng kho và hãng; kiểm mẫu 10% quyết định tự động | Cần đo tỉ lệ `delay_cause` trống thật trước Bước đánh giá 2; có thể buộc thu hẹp phạm vi theo hãng | MEASURE |
| Chính sách đổi mà bảng `policies` hoặc ngày hiệu lực không được cập nhật kịp | Cao (v4 vừa đổi, v3 hết ngày 30/11) | Hoàn sai và phạt oan hàng loạt trong vài giờ đầu sau ngày đổi | Lê Thanh Tùng / NV-TUNG | `escalation_rate` và `fault_write_blocked_rate` tăng đột ngột trong 48 giờ sau ngày đổi | Checklist đổi chính sách: xác nhận `effective_from` và hạn mức trước hiệu lực 3 ngày; chạy `lab10.grade` trên gói ticket mới | Quyết định mở rộng pilot phải chờ qua một lần đổi chính sách thật | MANAGE |
| Ca lỗi hãng thứ ba trong ngày bị `deny` mà không ai nhận | Trung bình | Hãng không bị phạt oan nhưng lỗi đáng ghi bị bỏ sót; quan hệ với hãng và kế toán đối soát lệch | Trần Thị Hạnh / NV-HANH | `fault_write_blocked_rate` > 10% trong 24 giờ | NV-HANH xem nhật ký `fault_deferred_strike_cap` đầu mỗi ca, xác minh với hãng | Cần thêm hàng chờ riêng cho ca này trước khi tăng phạm vi | GOVERN |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 2 (Dữ liệu) | Chưa (đã có phương án, chưa xác nhận trên tracking thật) | S3: `delay_cause` trống ở S3-20, S3-21; `cause_missing_rate` 0,1667 trên thẻ, 0,0 trên bộ nền (`R-S3-grade-20261119-163112-817d2f`) | Lê Thanh Tùng / NV-TUNG |
| 4 (Quyền hạn) | Xong cổng; Chưa diễn tập vận hành thật | `deny` riêng lệnh ghi lỗi khi chạm trần (`R-S3-after-20261119-163043-d40733`); ca lỗi thứ ba chưa vào hàng chờ của người duyệt | Trần Thị Hạnh / NV-HANH |
| 6 (Chi phí) | Xong ở bộ nền và gói sự cố | Gói sự cố after: 4.405đ/ticket, ROI 1,27; bộ nền after: 4.456đ, ROI 1,24 (`R-S3-grade-20261119-163112-817d2f`, `R-base-after-20261119-163102-817d2f`) | Phạm Kiều Oanh / NV-OANH |
| 8 (Con người/pháp lý) | Xong kiểm thử trên mock; Chưa tín hiệu production | Lỗi hãng oan 35 về 0 trên gói sự cố; còn cần log phản đối của hãng ngoài lab | Phạm Kiều Oanh / NV-OANH |
| 9 (Quyết định) | Chưa (chờ C12) | Quyết định v2 viết ở C12 | Cao Trung Hiếu / 2A202603993 |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Hàng "Lỗi oan/PII" (`wrongful_carrier_faults`) chỉ nhìn được sau khi có nhãn, còn production không có nhãn. Lẽ ra phải có tín hiệu "nguyên nhân trễ trống" và "lệnh ghi lỗi bị chặn". Chưa có; nay đã thêm `cause_missing_rate` và `fault_write_blocked_rate` |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm 2 hàng vào Runbook 2: `cause_missing_rate` (VÀNG ≥ 5%, ĐỎ ≥ 15%) và `fault_write_blocked_rate` (VÀNG > 10%, ĐỎ > 25%). Hai ngưỡng này đã được đề xuất, chưa có dữ liệu thật. Không đổi ngưỡng đã ký |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Không đổi số người trực (1 người, 6 ca/giờ; chuyển người còn 8,3% trên thẻ nên vẫn kham được). Thêm việc cho NV-HANH: đầu mỗi ca xem nhật ký `fault_deferred_strike_cap`; thêm việc cho NV-OANH: rà ca thiếu nguyên nhân khi đối soát tuần |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Không đổi phạm vi và `operating_gates.json`. Thêm quy trình: trước ngày chính sách đổi, NV-TUNG xác nhận phiên bản hiệu lực và hạn mức trong `policies` trước 3 ngày và chạy lại `lab10.grade` trên gói ticket mới |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-OANH báo điều phối Mekong Delta Ship (và DNB) trong 24 giờ: các lỗi oan đã ghi theo luật cũ sẽ được xóa và đối soát lại; NV-HANH báo CSKH các khách trễ 2 ngày từng bị từ chối sẽ được hoàn bù |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có dữ liệu cá nhân rời hệ thống trong sự cố này (`pii_leaks` bằng 0 ở cả ba mốc). Thông báo gửi hãng chỉ gồm `order_id`, `parcel_id`, `district`, `delay_days` |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ qua phản hồi của người: điều phối MKD và ghi chú CSKH. Số máy đo (`wrongful_carrier_faults`) cần nhãn nên không có trong production. Chưa có: kênh phản đối của hãng có log, và tỉ lệ `delay_cause` trống thật |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp **3** lần trong một giờ thì: ngay cả khi dồn cả 22 ticket của bộ nền vào một giờ thì chỉ cần duyệt khoảng 2 ca (tỉ lệ chuyển người 8,3% trên gói sự cố) đến 5 ca (22,7% trên bộ nền), vẫn dưới công suất 6 ca/giờ nên chưa cần thêm người; nếu ≥ 4 ca chờ cùng lúc thì NV-HANH gọi người dự phòng (30.000đ/ca) và NV-TUNG xem `queue_wait_max_min`.
2. Nếu nhà cung cấp LLM lỗi quá **10** phút thì: mọi ticket mới chuyển người duyệt, không để trợ lý tự hoàn khi chưa xác nhận được; NV-TUNG tắt `issue_refund` tự động nếu chuyển người vượt 6 ca/giờ.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: NV-HANH giữ ca đó, đối chiếu `decision_note` với tracking và chính sách hiệu lực; nếu trợ lý sai thì NV-TUNG ghi vào Risk register và tắt đúng thao tác ghi liên quan (không tắt cả trợ lý).

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
