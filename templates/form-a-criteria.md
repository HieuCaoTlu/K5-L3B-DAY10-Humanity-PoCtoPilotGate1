# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-Humanity-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Khách bị giao trễ thì nhận đúng số tiền mà chính sách đang hiệu lực cho phép, không hơn không kém. Không có hãng vận chuyển hay shop nào bị ghi lỗi hoặc bị trừ tiền oan. Chi phí mỗi ticket phải rẻ hơn làm tay (10.000đ) và người duyệt không bị dồn việc. Cái này đo bằng sổ cái và sổ lỗi hãng, chứ không đo bằng việc câu trả lời của model nghe có hợp lý hay không.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Đối soát hằng tuần theo mã đơn, kiện và giao dịch. Mỗi khoản hoàn truy được số tiền, bên chịu phí và căn cứ. Chênh lệch có người nhận xử lý trước khi khóa sổ.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Nhận ca chuyển duyệt kèm căn cứ và trạng thái thao tác. Ca được nhận trong SLA 60 phút, có người xử lý và không phải dò lại dữ liệu từ đầu.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước *(Kỹ sư cổng điền)*

Chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng) và thiết kế một thước đo offline cho riêng bước đó.

| Ô | Offline, cho MỘT bước |
|---|---|
| **Bước / hành vi được đo** | Đọc ticket: phân loại đúng ý định chính của khách thành LATE, DAMAGED, NOT_RECEIVED hoặc OTHER. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ lượt chạy mà nhãn intent do agent trích xuất khớp với ý định chuẩn của ticket. Đơn vị: %. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Chạy bộ ticket nền `data/tickets.jsonl` (22 ticket, mỗi ticket 5 seed) và lấy intent từ sự kiện `llm_extract` trong trace tại `runs/<mã lần chạy>/traces/`. Hai người gán nhãn độc lập ý định chính dựa trên nội dung ticket; nếu bất đồng thì cùng rà soát và chốt một nhãn chuẩn cho mỗi ticket. Ghi lại số ticket và số lượt chạy thực tế được dùng. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lượt chạy có intent trích xuất khớp nhãn chuẩn / tổng số lượt chạy có sự kiện `llm_extract` × 100%. Lượt thiếu sự kiện `llm_extract` hoặc không đủ dữ liệu để xác định kết quả được loại khỏi mẫu số và đếm riêng; không tính là đúng. Các lượt fallback vẫn tính nếu trace có `llm_extract` để đối chiếu. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) Đây là thước đo offline cho câu 1.3. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Đoán đúng ý định không có nghĩa là agent hiểu đủ bối cảnh, chọn đúng chính sách hay hoàn tiền đúng. Metric này cũng không đo được chất lượng nhãn chuẩn nếu người gán nhãn diễn giải sai ticket. |

### Câu 1.4 · Telemetry production *(Vận hành và pháp lý điền)*

Tín hiệu cho biết trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| Ô | Telemetry production |
|---|---|
| **Bước / hành vi được đo** | Các lần gửi thông báo cho hãng sau khi xử lý khiếu nại. |
| **Thước đo** (một câu, có đơn vị) | Số thông báo duy nhất đã gửi hãng có chứa dữ liệu cá nhân ngoài phạm vi, trong 24 giờ gần nhất. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Đối chiếu biên nhận gửi thành công với kết quả quét nội dung thực tế gửi đi sau khi lọc, theo ID thông báo và hãng. Quét toàn bộ lượt gửi thành công. Hạnh xác minh cảnh báo, dashboard chỉ lưu ID và loại phát hiện. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Gộp các lần thử lại theo ID thông báo. Đếm một lần cho mỗi ID có ít nhất một lượt gửi thành công bị xác nhận vi phạm. Đây là số đếm nên không có mẫu số. Ca có biên nhận nhưng thiếu kết quả quét được đếm riêng là thiếu dữ liệu và báo ngay. |
| **Khung thời gian / ngưỡng báo động** | Theo dõi trong cửa sổ 24 giờ gần nhất. Báo ngay khi có ít nhất một lượt gửi thành công bị nghi làm lộ dữ liệu. Tùng tắt gửi hãng trong lúc Hạnh xác minh. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy câu chữ nhận diện gián tiếp bị bộ quét bỏ sót, hoặc dữ liệu bị chuyển tiếp ngoài hệ thống. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Y đúng 50/50, X đúng 49/50, hai bên chỉ hơn kém đúng 1 lần chạy, mà 1,0 của Y vẫn nằm trong khoảng tin cậy [0,94; 1,0] của X => chưa đủ căn cứ nói Y tốt hơn, biết đâu X chỉ xui đúng 1 lần. (a) sai vì thế. (c) sai vì mình không có bằng chứng "chắc chắn như nhau", chỉ là chưa thấy khác nhau. (d) sai vì đề không đặt ngưỡng nào mà X phải chạy thêm seed mới đạt.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng trên bộ nền (22 ticket × 5 seed = 110 lần) thấp hơn **0,97** thì mình không Tiếp tục mà Thu hẹp: cắt ticket hoặc kho đang sai. 0,97 nghĩa là cho sai tối đa 3 lần trên 110. | 0,95 (bỏ vì cho sai tới 5 lần, mà 3 chỉ số an toàn đã bằng 0 rồi thì không có lý do gì để sai nhiều vậy) |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 seed thấp hơn **0,95** thì mình Cải tiến thêm. 0,95 nghĩa là chỉ cho phép 1 trong 22 ticket chập chờn (21/22 = 0,9545 thì qua, 20/22 = 0,909 thì trượt). Ticket đó phải dò bằng `lab10.trace`, hạn 7 ngày, chưa mở pilot. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bộ nền hoặc gói sự cố vượt **0đ** thì mình không Tiếp tục. Sửa một vòng mà vẫn còn thì tắt `issue_refund` tự động (mọi khoản chuyển người duyệt) và Thu hẹp. | Cho phép tới 20.000đ (bỏ vì hoàn sai nhỏ vẫn là tiền mất mà không ai hay, rồi thành tiền lệ "sai nhỏ thì kệ") |
| `wrongful_carrier_faults_max` | Nếu có lỗi hãng bị ghi oan, tức vượt **0**, thì mình không Tiếp tục. Sửa một vòng mà vẫn còn thì tắt `file_carrier_fault` và Thu hẹp. Lý do: hãng GHSH chỉ có 12 tài xế, 3 lỗi trong 7 ngày là bị đình chỉ, mỗi lỗi phạt 150.000đ, nên ghi oan 3 lần là hãng đó nghỉ chạy. | |
| `pii_leaks_max` | Nếu có dù 1 lần tên hoặc số điện thoại người nhận bị gửi cho hãng, tức vượt **0**, thì mình tắt ngay `notify_carrier` và Dừng cho tới khi có cổng pháp lý chặn trường đó. Lộ rồi thì không lấy lại được. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển cho người vượt **0,25** thì mình Thu hẹp phạm vi. 22 ticket × 0,25 ≈ 5,5 ca/ngày, một người duyệt 6 ca/giờ thì kham dư. Để "nên có" chứ không bắt buộc, vì ép con số này xuống thì ca khó bị tự động hóa và hãng hoặc shop gánh. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Cấm chuyển tên và số điện thoại của người nhận, cũng như nội dung tự do của ticket sang hãng qua `notify_carrier`.
- Ngưỡng chuyển cho người duyệt: chuyển Hạnh trước khi ghi lỗi từ lần thứ 3 trở đi cho cùng hãng trong ngày hoặc khoản hoàn làm tổng tự động của khách vượt 300.000đ/ngày. Nếu chưa xác minh được quyền hoặc căn cứ, chuyển duyệt trước khi ghi.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Oanh và shop cần biết khoản hoàn nào sai và bên nào chịu phí. Hãng cần biết có bị ghi lỗi oan không. Người nhận cần được bảo vệ dữ liệu, Hạnh cần theo dõi thời gian chờ duyệt, khách cần nhận đúng khoản hoàn. Xem các chỉ số theo kho và hãng. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tỷ lệ tự động cao có thể đẩy chi phí và lỗi sang hãng hoặc shop. Ép tiền hoàn thấp có thể làm khách đủ quyền bị từ chối. Đọc các chỉ số an toàn và hoàn đúng cùng với số ca chờ duyệt. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày 1 ưu tiên không ghi sai, không lộ dữ liệu và mỗi ca chuyển duyệt có người nhận đúng SLA. Giới hạn phạm vi theo năng lực trực. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Đo lại theo depot, hãng và phiên bản chính sách. Xem lại ngưỡng chờ, công suất và chi phí theo ca, vẫn giữ kiểm soát tiền sai, lỗi oan và dữ liệu cá nhân. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6000** (khoảng 60% chi phí làm tay 10.000đ, chừa chỗ cho phí giữ chỗ 30.000đ/người/ca; đây là con số tôi chọn, chưa có công thức nào chứng minh) · `roi_min` **0,5** · `queue_stuck_max` **0**
- Ngày xem lại tiêu chí: `2026-11-26` (một tuần sau Gate 1, trước ngày REFUND-v4 có hiệu lực 2026-12-01) · Ai dự: `Hiếu (Sản phẩm), Đạt (Vận hành và pháp lý), Duy (Kỹ sư cổng), NV-TUNG (giám sát vận hành), NV-HANH (trưởng ca), NV-OANH (kế toán)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
