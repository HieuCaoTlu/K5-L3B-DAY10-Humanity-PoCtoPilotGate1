# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Humanity
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Humanity-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): 

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Cao Trung Hiếu | 2A202603993 | Sản phẩm và kinh doanh | ✔ |
|   2 | Cao Phạm Thành Đạt | 2A202603970 | Vận hành và pháp lý |             |
|   3 | Đặng Quang Duy | 2A202603984 | Kỹ sư cổng |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

### CP3 · Đo, rủi ro, cổng vòng 1, quyết định v1 (Phiếu B)

**Đã xong:** chạy base (mã `R-base-before-20261119-150403-bde05c`), chạy `gate`, trace `T-002@55`, điền B0 dòng 1, B1 và B2. Kết quả: hoàn sai 20.000đ và 1 lỗi hãng oan (VNX), cả hai do **một** ticket `T-002@55` (agent tin số ngày khách khai là 5, trong khi tracking ghi 2). `runs/` không được push, nên Duy đọc kết quả trong Phiếu B (B0, B1, B2) chứ không đọc từ thư mục `runs/`.

**Duy** (cổng và bằng chứng)
- ⏳ Chờ pre-mortem (cả nhóm) để biết 2–3 lý do nào thành cổng.
- [ ] Viết 2–3 cổng trong `pre_guard` và `write_gate` (câu 2.6, B7.1). Bắt đầu từ lỗi thật ở B2: số ngày khách khai bị tin hơn DB (hoàn sai), lỗi hãng ghi theo số khai (ghi oan), và `customer_note` bị gửi cho hãng.
- [ ] Câu 2.7 (hai bước tránh rò rỉ dữ liệu) và câu 2.8 (một tính chất cần kiểm và hai ticket hiểm chạy bằng `--adhoc`).
- ⏳ Chờ Hiếu điền xong mục `business` và Đạt điền xong mục `operations` / `legal`, vì cổng đọc các con số này.
- [ ] Chạy `eval --stage after` và `unittest`: không được có ca nào hỏng thêm so với base.
- [ ] Khi test xanh và cổng xong: chạy `python -m lab10.checkpoint` (**chỉ một lần**), rồi `eval --stage prepared` và `gate`.
- ➜ Mở khoá cho Hiếu: Hiếu cần ba mã lần chạy này để viết quyết định v1.

**Đạt** (HAZOP, checklist và config làm được ngay, không cần chờ eval)
- [ ] HAZOP vòng 1 (câu 2.4, B4): ít nhất 3 dòng, trong đó ít nhất 2 dòng ngoài kỹ thuật. Có thể dùng lỗi thật ở B2 làm dòng ví dụ.
- [ ] Checklist go-live 9 nhóm (B5): mỗi dòng một người phụ trách có tên thật trong `world.json`.
- [ ] Mục `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và mục `legal` trong `config/operating_gates.json`.
- [ ] Runbook phần 1–3 và mục "Giờ cao điểm" (B7.5, B7.6): các con số phải khớp với `operations`.
- ➜ Mở khoá cho Duy: Duy cần `operations.pic` không còn trống mới qua mốc được.

**Hiếu**
- [ ] Câu 2.3 (B3): bản đồ dữ liệu của trợ lý và một ví dụ drift.
- [ ] Câu 2.9 (B7.4): điền mục `business` trong `operating_gates.json` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`), mỗi số một câu lý do lấy từ `world.json`. Gợi ý từ base: trần hoàn hiện còn `null`, ngày nhiều nhất trợ lý tự hoàn 155.000đ, ngân sách tự động của Finance 2.000.000đ/ngày.
- ➜ Mở khoá cho Duy: như trên.
- ⏳ Chờ Duy chạy xong `prepared` và `gate`.
- [ ] Viết quyết định v1 ở B8 (một quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho hoặc hãng có số xấu nhất, ngày quyết định lại). Từ base: kho xấu nhất **HCM**, hãng xấu nhất **VNX**. Commit và push.

**Cả ba cùng làm**
- [ ] Pre-mortem bốn lăng kính (câu 2.5, B6), đánh dấu 2–3 lý do sẽ thành cổng. Điều kiện đã đủ: base và `T-002@55` đã có, không phải chờ gì thêm.

### CP4 · Sự cố (Phiếu C). Mọi việc ở đây chờ thẻ được phát.

**Hiếu** (mở đường cho cả nhóm)
- ⏳ Chờ Lab Coach báo số thẻ.
- [ ] Chạy ba lệnh nhận thẻ, ghi `Thẻ đã bốc:` ở đầu Phiếu C và ở mục "Thông tin nhóm" phía trên, chạy `python -m lab10.grade --incident Sx`, rồi push để Đạt và Duy kéo về.
- ➜ Mở khoá cho Duy và Đạt: cả hai chưa làm được gì ở CP4 khi chưa có thẻ.
- [ ] C0, C5 (specification và giả định môi trường).
- [ ] Sửa mục `business` nếu nguyên nhân sự cố là tiền hoặc phạm vi.

**Duy**
- ⏳ Chờ Hiếu push thẻ và kết quả `grade` đầu tiên.
- [ ] C2: dò ít nhất hai ticket hỏng theo hai kiểu khác nhau bằng `trace`.
- [ ] C6: fault tree trước khi sửa.
- [ ] Sửa `guards.py` nếu nguyên nhân là kỹ thuật. Thêm ít nhất một chỉ số theo dõi mới trong `lab10/monitors.py` (C8).
- ⏳ Chờ Hiếu và Đạt sửa xong phần config của họ (nếu có), để chạy bản đo cuối cùng cho "đổi MỘT thứ mỗi lần".
- [ ] Chạy `eval --suite Sx --stage after`, `eval --suite base --stage after` và `grade`.
- ➜ Mở khoá cho Hiếu: Hiếu cần kết quả này để viết quyết định v2.

**Đạt**
- ⏳ Chờ Hiếu push thẻ.
- [ ] C3 (phần riêng theo thẻ đã bốc), C4 (HAZOP của thẻ, không ghi đè HAZOP vòng 1).
- [ ] Sửa `operations` / `legal` nếu nguyên nhân sự cố là con người hoặc pháp lý.
- ⏳ Chờ Duy chạy xong bản đo cuối để biết còn rủi ro nào.
- [ ] C9 (fault tree sau khi sửa), C10 (ít nhất 1 dòng risk register), C11 (cập nhật checklist và runbook phần 4–5).

**Cả ba cùng làm**
- [ ] C1: cổng vòng 1 đỡ được gì, đối chiếu với pre-mortem bằng bút khác màu.
- [ ] C7: bảng sửa, ghi rõ mỗi chỗ sửa là **giảm** hay **ngăn** tác hại.

### CP5 · Quyết định v2, demo, nộp

**Hiếu**
- ⏳ Chờ Duy chạy xong bản đo cuối và Đạt xong C9–C11.
- [ ] Điền C12 (cột v2, mục "Chỉ ở v2", ba dòng bắt buộc). Chọn "Tiếp tục" khi report còn vượt trần là quyết định không đạt.
- ➜ Mở khoá cho Đạt: Đạt chép ba dòng từ C12 sang `submission.json`.

**Đạt**
- ⏳ Chờ Hiếu xong C12.
- [ ] Điền `submission/submission.json` (`incident`, `decision_v1`, `decision_v2`, ba dòng `three_lines` chép từ C12). Hai trường `team` và `members` đã điền sẵn.
- ➜ Mở khoá cho Duy: Duy chạy lệnh 7 sau khi file này xong.

**Duy**
- ⏳ Chờ Đạt xong `submission.json` và mọi phiếu đã điền.
- [ ] Chạy `python -m lab10.check_submission --collect`, sửa từng dòng `[THIẾU]` rồi chạy lại cho tới khi thấy `ĐỦ THÀNH PHẦN`.
- [ ] Sau demo: trả mọi con số đã đổi thử về bản v2, chạy lại `grade` và lệnh 7.

**Hiếu (cuối cùng)**
- ⏳ Chờ Duy báo `ĐỦ THÀNH PHẦN`.
- [ ] Push bài nộp cuối, gửi link repo cho team chấm.

**Cả ba**
- [ ] Viết mục cá nhân của mình bên dưới (phần việc, đóng góp, bằng chứng, exit ticket, ghi rõ nếu đã dùng AI cho phần nào).
- [ ] **Mỗi người** tự nộp link repo trên LMS bằng tài khoản của mình. Ai không nộp thì không có bài.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## CaoTrungHieu-2A202603993

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## CaoPhamThanhDat-2A202603970

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DangQuangDuy-2A202603984

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
