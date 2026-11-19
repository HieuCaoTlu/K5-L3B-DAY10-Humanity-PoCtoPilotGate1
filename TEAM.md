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

## Danh sách việc cần làm (chia theo checkpoint)

Cách đọc: `[ ]` là việc chưa làm, tick `[x]` khi xong. Dòng **⏳ Chờ …** là nút thắt: việc đó chưa làm được cho tới khi người được nêu xong phần của họ. Dòng **➜ Mở khoá cho …** cho biết ai đang đợi mình.

Quy tắc chung: chỉ **Hiếu** push lên GitHub. Đạt và Duy gửi file hoặc patch cho Hiếu. Mỗi file có một chủ: Duy giữ `lab10/guards.py` và `lab10/monitors.py`; Hiếu giữ `config/acceptance_criteria.json` và mục `business`; Đạt giữ mục `operations`, `legal` và `submission/submission.json`. Hiếu và Đạt cùng sửa `config/operating_gates.json` thì sửa lần lượt, không sửa cùng lúc.

### CP1 · Cài đặt (cả ba làm song song, không ai phải chờ ai)

**Đạt và Duy**
- [ ] Clone repo, chạy `python -m unittest discover -s tests` cho tới khi thấy `Ran 13 tests … OK`.
- [x] Đạt: đọc `data/world.json` (mục `staff`, `ops_limits`, `ops_facts`) và `docs/guide.md`. Đã clone và chạy 13 test public, cả 13 đạt.
- [ ] Duy: đọc `lab10/agent.py`, `lab10/tools.py`, `lab10/guards.py` để hiểu trợ lý đang làm gì.

### CP2 · Ký tiêu chí (Phiếu A). Tuyệt đối chưa ai chạy `eval`.

**Duy**
- [ ] Phiếu A câu 1.3: chọn một bước của trợ lý và viết cách đo nó offline (thước đo, dữ liệu, cách tính, điểm mù).
- ➜ Mở khoá cho Hiếu: Hiếu cần câu này xong để chốt ngưỡng.

**Đạt**
- [x] Phiếu A câu 1.2 (mục tiêu nhìn từ chị Oanh và chị Hạnh) và câu 1.4 (cách đo trên production).
- [x] Bốn câu soát và hai câu "ranh giới đầu ra" (không cần chép vào JSON).
- ➜ Mở khoá cho Hiếu: như trên.

**Hiếu**
- [ ] Phiếu A câu 1.1, 1.5, 1.6 (câu tiêu chí "Nếu … thì chúng tôi sẽ …").
- ⏳ Chờ Duy (câu 1.3) và Đạt (câu 1.2, 1.4, các câu soát) xong, để các ngưỡng khớp với cách đo của họ.
- [ ] Điền `config/acceptance_criteria.json` (`team` phải đúng tên repo `K5-L3B-DAY10-Humanity-PoCtoPilotGate1`, `signed_by`, ngưỡng, `stop_condition`, bốn dòng `decision_rule`).
- [ ] Chạy `python -m lab10.criteria sign`, rồi commit và push ngay. Điền A5 (giờ ký, mã commit).
- ➜ Mở khoá cho Duy: chỉ sau bước này Duy mới được chạy `eval`. **Đây là nút thắt lớn nhất của cả bài.**

### CP3 · Đo, rủi ro, cổng vòng 1, quyết định v1 (Phiếu B)

**Duy**
- ⏳ Chờ Hiếu ký xong và push (CP2).
- [ ] Chạy `eval --suite base --stage base`, rồi `gate`, ghi mã lần chạy vào B0 và đọc kết quả (câu 2.1, B1).
- [ ] Chạy `trace --suite base --ticket T-002 --seed 55`, điền bảng soát lỗi (câu 2.2, B2).
- ➜ Mở khoá cho cả nhóm: pre-mortem cần kết quả base này.
- [ ] Sau pre-mortem: viết 2–3 cổng trong `pre_guard` và `write_gate` (câu 2.6, B7.1).
- [ ] Câu 2.7 (hai bước tránh rò rỉ dữ liệu) và câu 2.8 (một tính chất cần kiểm và hai ticket hiểm chạy bằng `--adhoc`).
- ⏳ Chờ Hiếu điền xong mục `business` và Đạt điền xong mục `operations` / `legal`, vì cổng đọc các con số này.
- [ ] Chạy `eval --stage after` và `unittest`: không được có ca nào hỏng thêm so với base.
- [ ] Khi test xanh và cổng xong: chạy `python -m lab10.checkpoint` (**chỉ một lần**), rồi `eval --stage prepared` và `gate`.
- ➜ Mở khoá cho Hiếu: Hiếu cần ba mã lần chạy này để viết quyết định v1.

**Đạt** (HAZOP, checklist và config làm được ngay, không cần chờ eval)
- [x] HAZOP vòng 1 (câu 2.4, B4): ít nhất 3 dòng, trong đó ít nhất 2 dòng ngoài kỹ thuật.
- [x] Checklist go-live 9 nhóm (B5): mỗi dòng một người phụ trách có tên thật trong `world.json`.
- [x] Mục `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và mục `legal` trong `config/operating_gates.json`.
- [x] Runbook phần 1–3 và mục "Giờ cao điểm" (B7.5, B7.6): các con số phải khớp với `operations`.
- ➜ Mở khoá cho Duy: Duy cần `operations.pic` không còn trống mới qua mốc được.

**Hiếu**
- [ ] Câu 2.3 (B3): bản đồ dữ liệu của trợ lý và một ví dụ drift.
- [ ] Câu 2.9 (B7.4): điền mục `business` trong `operating_gates.json` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`), mỗi số một câu lý do lấy từ `world.json`.
- ➜ Mở khoá cho Duy: như trên.
- ⏳ Chờ Duy chạy xong `prepared` và `gate`.
- [ ] Viết quyết định v1 ở B8 (một quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho hoặc hãng có số xấu nhất, ngày quyết định lại). Commit và push.

**Cả ba cùng làm**
- [ ] Pre-mortem bốn lăng kính (câu 2.5, B6), đánh dấu 2–3 lý do sẽ thành cổng. ⏳ Chờ Duy xong base và `T-002@55`.

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

Vận hành và pháp lý. Phiếu A câu 1.2, 1.4, bốn câu soát và hai ranh giới. Phiếu B mục B4, B5, B7.5–B7.6 và hai mục `operations` / `legal`. Tham gia B6 khi có kết quả bộ nền. Các phần C3–C4, C9–C11 và hồ sơ nộp chờ thẻ, bản đo cuối và C12 theo phân công.

### Đóng góp cụ thể

Đặt công suất 6 ca/giờ cho một người duyệt, SLA 60 phút, chỉ định Hạnh duyệt và Tùng giữ công tắc. Phân tích hậu quả ghi lỗi oan theo kiện và loại `customer_note`, `recipient_contact` trước khi gửi hãng. Đã dùng Codex để đọc repo, soạn và kiểm tra Phiếu A, Phiếu B cùng cấu hình được phân công.

### Bằng chứng

13 bài kiểm tra public đạt. Xem Phiếu A mục A1, A2, A4; Phiếu B mục B4, B5, B7.5–B7.6; hai mục `operations` và `legal` trong cấu hình. Phiếu A có commit 562f6b1 (PR #1). Chưa có mã eval vì nhóm chưa ký tiêu chí.

### Exit ticket

Tôi học được rằng tải duyệt là giới hạn của cả luồng. Một người duyệt 6 ca/giờ vẫn có thể bị ùn nếu ca đến dồn. Tôi còn cần đo tải ca chuyển duyệt ở giờ cao điểm để xác nhận ngưỡng gọi dự phòng.

## DangQuangDuy-2A202603984

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
