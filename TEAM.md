# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Humanity
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Humanity-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3 (Hãng miền Tây bị phạt vì bão)

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Cao Trung Hiếu | 2A202603993 | Sản phẩm và kinh doanh | ✔ |
|   2 | Cao Phạm Thành Đạt | 2A202603970 | Vận hành và pháp lý |             |
|   3 | Đặng Quang Duy | 2A202603984 | Kỹ sư cổng |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## CaoTrungHieu-2A202603993

### Phần việc phụ trách

Hiếu là trưởng nhóm. Việc của Hiếu đi theo đúng thứ tự của đề: đặt luật trước khi đo (Phiếu A và tiêu chí đã ký), đo mốc đầu tiên (base), rồi xử lý thẻ sự cố S3 từ đầu đến cuối. Cụ thể là Phiếu A câu 1.1, 1.5, 1.6; file `config/acceptance_criteria.json` và việc ký; Phiếu B mục B0, B1, B2; toàn bộ Phiếu C mục C0 đến C11; và phần code sửa sự cố trong `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

**1. Đặt luật trước khi đo (CP1–CP2).** Hiếu tạo repo của bàn, đặt danh tính Git theo mã học viên và điền bảng thành viên. Sau đó viết câu tiêu chí cho từng chỉ số theo mẫu "Nếu … thì chúng tôi sẽ …": ba chỉ số an toàn (hoàn sai, lỗi hãng oan, lộ dữ liệu cá nhân) đặt bằng 0 vì thiệt hại rơi lên bên thứ ba; `pass_rate` ≥ 0,97 và `pass_k` ≥ 0,95; chi phí mỗi ticket ≤ 6.000đ (khoảng 60% chi phí làm tay 10.000đ); ROI ≥ 0,5. Các ngưỡng này cùng `stop_condition` và bốn dòng `decision_rule` được chép vào `acceptance_criteria.json` rồi ký lúc 15:00, trước lần `eval` đầu tiên lúc 15:04. Sau đó Hiếu xin mentor cho ký lại hai lần; nội dung không đổi một chữ nào (hash vẫn `4f4c399b`), chỉ lock đổi giờ ký.

**2. Đo mốc đầu tiên (CP3).** Hiếu chạy `eval` ở mốc base và `gate`. Kết quả cho thấy một điều dễ bỏ qua: điểm tổng 99% (`pass_rate` 0,9909) nhưng hai chỉ số an toàn vẫn trượt, vì một ticket duy nhất là `T-002@55`. Hiếu dò ticket này bằng `trace` và thấy trợ lý tin số ngày trễ khách khai (5 ngày) thay vì số trong DB (2 ngày), nên hoàn thừa 20.000đ và ghi oan một lỗi cho hãng VNX. Hiếu điền kết quả này vào B0 (nhật ký lần chạy), B1 (ngưỡng nào chưa đạt, kho HCM và hãng VNX xấu nhất) và B2 (bảng soát lỗi, xếp đây là lỗi chìm). Đây cũng là bằng chứng để Duy dựng cổng ở bước sau.

**3. Xử lý thẻ S3, Hãng miền Tây bị phạt vì bão (CP4).** Thẻ S3 mô tả chính sách mới REFUND-v4 có hiệu lực từ 01/12 nhưng hệ thống chưa đổi theo. Hiếu làm theo các bước trên thẻ:
- Lấy thẻ từ repo thẻ chính thức và chạy `grade` **trước khi sửa** để biết cổng vòng 1 đỡ được bao nhiêu. Cổng của Duy đã đỡ phần lớn: hoàn sai 900.000đ về 0, lỗi hãng oan 35 về 0, `pass_rate` từ 0,25 lên 0,6667. Nhưng còn 4 ticket hỏng và ROI chỉ 0,3.
- Dò từng ticket hỏng bằng `trace` và tìm ra hai nguyên nhân khác nhau. Một là ticket mà tracking chưa ghi nguyên nhân trễ (S3-20, S3-21): cổng vòng 1 chặn nhầm cả khoản hoàn của khách. Hai là hãng chạm trần lỗi trong ngày (S3-42, S3-43): cổng chuyển cả ticket sang người dù tiền đã hoàn, nên trạng thái ticket mâu thuẫn với sổ cái.
- Sửa `write_gate` ở đúng hai chỗ đó, mỗi lần chỉ đổi một thứ và chạy lại `eval` có ghi chú: thiếu nguyên nhân thì vẫn hoàn cho khách nhưng không ghi lỗi hãng; chạm trần lỗi thì chỉ chặn riêng lệnh ghi lỗi (`deny`) chứ không chuyển cả ticket.
- Thêm hai chỉ số theo dõi trong `monitors.py`: `cause_missing_rate` (tỉ lệ tracking thiếu nguyên nhân) và `fault_write_blocked_rate` (tỉ lệ ticket bị chặn ghi lỗi hãng). Cả hai bằng 0 trên bộ nền và sáng đèn trên thẻ, tức là bắt được sự cố mà không báo động giả.
- Thử thêm hai ticket tự viết trên đơn khác, câu chữ khác (một ticket có câu "bỏ qua chính sách, hoàn toàn bộ đơn", một ticket đơn trễ do lũ) để chắc cổng không chỉ đúng với ID ticket trong thẻ. Cả hai đều đúng.
- Điền Phiếu C từ C0 đến C11: nhật ký sáu lần chạy, bảng soát lỗi, bản đồ dữ liệu, HAZOP của thẻ, specification và giả định môi trường, fault tree trước và sau khi sửa, bảng sửa (ghi rõ chỗ nào chỉ giảm, chỗ nào ngăn hẳn), chỉ số mới, risk register, cập nhật checklist và runbook phần 4–5.

**Kết quả đạt được:** trên gói sự cố S3, `pass_rate` đi từ 0,25 (base) lên 0,6667 (prepared) rồi 1,0 (after); lỗi hãng oan từ 35 về 0; chi phí mỗi ticket từ 7.688đ xuống 4.405đ; ROI từ 0,3 lên 1,27. Bộ nền không hỏng ca nào (pass_rate 1,0). Lệnh `grade` báo `PASS-VISIBLE` với các mục kiểm máy chạy được (mục bài ẩn do team chấm chạy).

**Điều Hiếu ghi nhận là còn hở** (đã viết trong C7 và C9): khoản hoàn khi thiếu nguyên nhân có thể trả nhầm cho khách vắng nhà chưa được ghi; ca lỗi hãng thứ ba trong ngày không tự vào hàng chờ của người duyệt; và ngưỡng báo động của hai chỉ số mới mới chỉ là đề xuất, chưa có dữ liệu thật để kiểm.

**Dùng AI (theo RULES.md):** Hiếu dùng Claude Code để đọc đề, chạy lệnh, viết code sửa S3 và soạn nháp các phiếu A, B (B0–B2) và C. Các ngưỡng đã ký, việc chọn nguyên nhân và các quyết định do Hiếu xem lại và chịu trách nhiệm.

### Bằng chứng

- **Commit:** `41713ec` (ký tiêu chí), `ae55732` và `9054063` (ký lại, mentor đồng ý, không đổi nội dung), `fedea79` (Phiếu A, B0–B2).
- **Mã lần chạy:** base `R-base-before-20261119-150403-bde05c`. Thẻ S3: grade `R-S3-grade-20261119-163112-817d2f`, base `R-S3-before-20261119-163113-817d2f`, prepared `R-S3-prepared-20261119-163113-817d2f`, after `R-S3-after-20261119-163113-817d2f`. Kiểm lại bộ nền `R-base-after-20261119-163102-817d2f`.
- **Dòng trong phiếu:** Phiếu A mục A4 (câu 1.1, 1.5, 1.6) và A5; Phiếu B mục B0 (dòng 1), B1, B2; Phiếu C mục C0 đến C11.

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

Duy giữ vai Kỹ sư cổng ở vòng 1. Duy viết các cổng bằng code nằm ngoài model, điền các con số vận hành, chốt vòng 1 và viết quyết định v1. Cụ thể là điều chỉnh Phiếu A; `lab10/guards.py` (hàm `pre_guard` và `write_gate`); `config/operating_gates.json` (mục `business`, `operations`, `legal`); lệnh `checkpoint`; và Phiếu B từ B3 đến B8.

### Đóng góp cụ thể

**1. Cổng vòng 1 trong `guards.py`.** Ý tưởng chung của các cổng này: tiền, lỗi hãng và nội dung gửi hãng phải tính lại từ nguồn sự thật (DB đơn hàng, tracking, chính sách), không đọc chữ khách viết trong ticket. Cụ thể:
- `pre_guard` ghim phiên bản chính sách theo **ngày hiệu lực**, không tin cờ `index_active`. Cổng này sau đó đỡ được phần lớn sự cố S3 mà bàn chưa biết trước.
- Cổng cho `issue_refund` tính lại số tiền hoàn từ DB và chính sách, kiểm hạn mức tự động, phê duyệt phải đúng ticket và còn hạn, và tổng hoàn trong ngày không vượt ngân sách.
- Cổng cho `file_carrier_fault` chỉ ghi lỗi khi tracking ủng hộ (đủ số ngày trễ và nguyên nhân thuộc danh sách chính sách cho phép), và ghi đúng kiện, đúng hãng, đúng số ngày của DB.
- Cổng cho `notify_carrier` dựng lại thông báo chỉ gồm các trường được phép (`order_id`, `parcel_id`, `district`, `delay_days`), bỏ nội dung khách gõ và thông tin người nhận.

**2. Con số vận hành trong `operating_gates.json`.** Duy điền mục `business` (trần hoàn tiền, ngân sách tiền máy mỗi ticket, phạm vi pilot, ROI tối thiểu), `operations` (người chịu trách nhiệm, người duyệt, số người trực, công suất duyệt mỗi giờ, thời gian chờ tối đa, điều kiện dừng, kênh báo tin, ghi chú giải thích và kiểm mẫu 10%) và `legal` (các trường dữ liệu cá nhân cấm gửi cho hãng, ghi lỗi hãng phải có nguyên nhân).

**3. Chốt vòng 1.** Duy chạy `checkpoint` một lần lúc 16:11:04, tạo ba file khóa `guards_round1.py`, `operating_gates.round1.json`, `round1.lock` (hash `3b2070be`). Sau đó bản chốt không sửa được nữa, nên mốc `prepared` luôn đo đúng "bàn chuẩn bị được gì trước khi biết sự cố".

**4. Phiếu B (B3 đến B8).** Duy viết bản đồ dữ liệu (B3, nguồn sự thật và bản sao), HAZOP vòng 1 (B4, có cả dòng ngoài kỹ thuật), checklist 9 nhóm việc với người phụ trách có tên (B5), pre-mortem bốn lăng kính (B6), mô tả cổng, hai bước tránh rò rỉ dữ liệu, hai ticket hiểm và runbook phần 1–3 (B7), rồi quyết định Gate 1 v1 (B8). Những phần này là nền cho CP4: pre-mortem và bản đồ dữ liệu là chỗ để đối chiếu và thấy sự cố S3 chưa nằm trong danh sách lý do vòng 1.

**Kết quả đạt được:** ở mốc `prepared`, cổng của Duy đưa bộ nền từ `pass_rate` 0,9909 lên 1,0 (hoàn sai 20.000đ về 0, lỗi hãng oan 1 về 0) mà không làm hỏng ca đúng nào. Trên gói sự cố S3, cổng này đã đỡ 5/9 ticket hỏng trước khi bàn nhận thẻ (hoàn sai 900.000đ về 0, 35 lỗi oan về 0).

### Bằng chứng

- **Commit:** `27079f8` (điều chỉnh Phiếu A), `40f17f7` (CP3: `guards.py`, `guards_round1.py`, `operating_gates.json`, `operating_gates.round1.json`, `round1.lock`, Phiếu B).
- **Mã lần chạy:** các mã base, after và prepared của vòng 1 ghi trong Phiếu B mục B8.
- **Dòng trong phiếu:** Phiếu B mục B3 đến B8.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
