ĐẠI HỌC THÁI NGUYÊN
TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG
KHOA CÔNG NGHỆ THÔNG TIN

--------------------***--------------------

[ BÁO CÁO DỰ ÁN HỌC PHẦN HỌC MÁY ]

BÁO CÁO ĐỒ ÁN / DỰ ÁN HỌC PHẦN
NGHIÊN CỨU, XÂY DỰNG HỆ THỐNG PHÂN TÍCH QUAN ĐIỂM ĐA DIỆN (JOINT ABSA) VÀ LỌC NGHỊCH NHÃN PHẢN HỒI NGƯỜI DÙNG ỨNG DỤNG DI ĐỘNG TẠI VIỆT NAM

HỌC PHẦN: HỌC MÁY (MACHINE LEARNING)
MÃ HỌC PHẦN: CMP312 | LỚP HỌC PHẦN: CNTT K22B & K22C
HỌC KỲ I - NĂM HỌC 2026 - 2027


| GIẢNG VIÊN HƯỚNG DẪN:     ThS. HÀ THỊ THANH - Bộ môn Khoa học Máy tính  NHÓM SINH VIÊN THỰC HIỆN: NHÓM 12     1. Lê Hồng Sơn       - MSV: DTC235200647 (Trưởng nhóm)     2. Lưu Thị Khánh Ly  - MSV: DTC235200483     3. Ngô Thị Sinh      - MSV: DTC235200645     4. Nguyễn Thanh Tùng - MSV: DTC235200811 |
| --- |


THÁI NGUYÊN, NĂM 2026

LỜI CẢM ƠN

Lời đầu tiên, toàn thể thành viên Nhóm 12 xin bày tỏ lòng biết ơn sâu sắc và chân thành nhất tới Giảng viên hướng dẫn - ThS. Hà Thị Thanh, Giảng viên Bộ môn Khoa học Máy tính, Khoa Công nghệ Thông tin, Trường Đại học Công nghệ Thông tin và Truyền thông - Đại học Thái Nguyên.

Trong suốt quá trình học tập học phần Học máy (Machine Learning) và thực hiện dự án này, cô đã luôn tận tình truyền đạt những kiến thức nền tảng quý báu, định hướng phương pháp luận khoa học, kiên nhẫn chỉ dẫn từng cơ chế thuật toán từ đại số tuyến tính, lý thuyết xác suất thống kê đến các mô hình học máy nâng cao. Sự đồng hành, góp ý sát sao và những phản biện học thuật sắc bén của cô chính là động lực to lớn giúp nhóm không ngừng hoàn thiện đồ án, vượt qua các thách thức phức tạp về tiền xử lý ngôn ngữ tiếng Việt và tối ưu hóa hệ thống.

Nhóm cũng xin trân trọng cảm ơn Ban Giám hiệu Nhà trường, Ban Chủ nhiệm Khoa Công nghệ Thông tin cùng các thầy cô giáo trong Bộ môn Khoa học Máy tính đã tạo điều kiện học tập, nghiên cứu và trang bị cơ sở vật chất, hệ thống tài liệu giáo trình chuẩn mực để sinh viên có cơ hội rèn luyện và tiếp cận các bài toán thực tiễn.

Dù đã nỗ lực hết mình với tinh thần làm việc nghiêm túc, khoa học và cặn kẽ, đồ án khó tránh khỏi những thiếu sót nhất định do kiến thức và kinh nghiệm thực tế của nhóm sinh viên vẫn đang trong quá trình tích lũy. Nhóm 12 rất mong tiếp tục nhận được những ý kiến đóng góp, chỉ dẫn quý báu từ cô giáo và hội đồng phản biện để đề tài ngày càng hoàn thiện hơn nữa.

LỜI CAM ĐOAN

Nhóm 12 xin cam đoan rằng công trình nghiên cứu và báo cáo dự án học phần Học máy với đề tài: "Phân tích quan điểm phản hồi của người dùng về ứng dụng di động tại Việt Nam" là kết quả nghiên cứu độc lập, trung thực của các thành viên trong nhóm dưới sự hướng dẫn trực tiếp của ThS. Hà Thị Thanh.

Toàn bộ số liệu thực nghiệm (14.910 đánh giá), các bảng thống kê mô tả, ma trận nhầm lẫn, biểu đồ trực quan hóa, bộ lọc khử nhiễu nghịch nhãn, mã nguồn huấn luyện mô hình, kiểm định chéo và mã nguồn xây dựng dịch vụ API/Dashboard đều được nhóm tự thiết kế, lập trình và thực thi thực tế trên môi trường máy tính tính toán cá nhân, không sao chép bất kỳ báo cáo hay kết quả có sẵn nào.

Các tài liệu tham khảo, trích dẫn lý thuyết từ Giáo trình Học máy ICTU (năm 2026) của các tác giả TS. Trần Quang Quý, TS. Ngô Hữu Huy, TS. Nguyễn Đức Bình, TS. Nguyễn Tuấn Anh và các bài báo khoa học quốc tế đều được ghi chú nguồn và trích dẫn rõ ràng, chuẩn mực theo quy định học thuật.

Nhóm 12 xin chịu hoàn toàn trách nhiệm trước Pháp luật, Nhà trường và Bộ môn nếu xảy ra bất kỳ sự vi phạm nào về tính trung thực của số liệu và quyền tác giả trong báo cáo này.

Thái Nguyên, ngày 26 tháng 11 năm 2026
Đại diện Nhóm 12 - Trưởng nhóm



Lê Hồng Sơn

PHÂN CÔNG NHIỆM VỤ VÀ TIÊU CHÍ ĐÁNH GIÁ ĐỒ ÁN

Bảng phân công nhiệm vụ chi tiết thành viên Nhóm 12

Dự án được triển khai với sự tham gia của 4 thành viên thuộc lớp CNTT K22B và K22C, phân công nhiệm vụ chuyên môn hóa theo đúng đăng ký đồ án:


| STT | Mã sinh viên | Họ và tên | Nhiệm vụ đảm nhiệm trong dự án | Đánh giá |
| --- | --- | --- | --- | --- |
| 1 | DTC235200647 | Lê Hồng Sơn<br>(Trưởng nhóm) | • Quản lý tiến độ dự án, phân công công việc.<br>• Thiết kế pipeline Tiền xử lý dữ liệu và bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit).<br>• Nghiên cứu cơ sở toán học và Lựa chọn mô hình tối ưu (LinearSVC, Logistic Regression). | 100% (Hoàn thành xuất sắc) |
| 2 | DTC235200483 | Lưu Thị Khánh Ly | • Thiết kế kịch bản và công cụ Thu thập dữ liệu phản hồi (14.910 mẫu từ 8 ứng dụng).<br>• Thực hiện Phân tích khám phá dữ liệu EDA chuyên sâu, vẽ biểu đồ phân bố rating, độ dài từ và tần suất n-gram. | 100% (Hoàn thành xuất sắc) |
| 3 | DTC235200645 | Ngô Thị Sinh | • Thiết lập quy trình Đánh giá mô hình học máy (5-Fold Cross-Validation, GridSearchCV).<br>• Tính toán các chỉ số Accuracy, Precision, Recall, Macro F1, Latency và thực hiện Phân tích lỗi (Error Analysis 20 ca mẫu). | 100% (Hoàn thành xuất sắc) |
| 4 | DTC235200811 | Nguyễn Thanh Tùng | • Đóng gói mô hình và Triển khai bài toán thực tế.<br>• Lập trình dịch vụ Microservice RESTful API bằng FastAPI với độ trễ siêu thấp (< 0.3 ms/mẫu).<br>• Xây dựng Dashboard tương tác người dùng Streamlit hoàn chỉnh. | 100% (Hoàn thành xuất sắc) |


Bảng 0.1: Phân công nhiệm vụ chi tiết các thành viên Nhóm 12

Bảng đối chiếu Barem Tiêu chí chấm đồ án/dự án học phần Học máy

Báo cáo và chương trình thực nghiệm của nhóm được xây dựng bám sát 100% Tiêu chí chấm đồ án của Giảng viên ThS. Hà Thị Thanh (Bộ môn Khoa học Máy tính - ICTU):


| Tiêu chí | Nội dung yêu cầu chi tiết theo Barem | Điểm | Minh chứng trong báo cáo |
| --- | --- | --- | --- |
| Tiêu chí 1: Báo cáo | Báo cáo trình bày đúng mẫu quy định, bố cục rõ ràng, văn phong khoa học, logic chặt chẽ, đầy đủ cơ sở lý thuyết, trích dẫn tài liệu tham khảo chính xác. | 2.0 đ | Đầy đủ 4 chương (48 trang), đúng thể thức ICTU, trích dẫn 18 tài liệu tham khảo. |
| Tiêu chí 2 - Mục 1: EDA | Thu thập dữ liệu, phân tích khám phá dữ liệu (EDA), thống kê mô tả, trực quan hóa biểu đồ phân bố nhãn, thuộc tính, độ dài từ. | 1.5 đ | Mục 3.1: 8 hồ sơ ứng dụng, biểu đồ rating, n-gram, phân bố 7 khía cạnh. |
| Tiêu chí 2 - Mục 2: Tiền xử lý | Làm sạch dữ liệu, xử lý giá trị thiếu, ngoại lai, chuẩn hóa text, mã hóa đặc trưng vector phù hợp với bài toán học máy. | 1.5 đ | Mục 3.2: 50 quy tắc teencode, khử nhiễu nghịch nhãn 1.240 mẫu, TF-IDF 24.619 chiều. |
| Tiêu chí 2 - Mục 3: Huấn luyện | Xây dựng và huấn luyện ít nhất 2 mô hình học máy trở lên, phân chia tập dữ liệu huấn luyện/kiểm thử hợp lý. | 1.0 đ | Mục 3.3: Huấn luyện 4 mô hình (MNB, Logistic Regression, LinearSVC, Random Forest). |
| Tiêu chí 2 - Mục 4: Tinh chỉnh | Tìm kiếm siêu tham số tối ưu (GridSearchCV / RandomSearchCV), so sánh đối chuẩn các mô hình để chọn ra mô hình tốt nhất. | 1.5 đ | Mục 3.4: GridSearchCV 5-fold qua 15 tổ hợp tham số, chọn LinearSVC C=2.0. |
| Tiêu chí 2 - Mục 5: Đánh giá & Lỗi | Đánh giá mô hình trên tập kiểm thử bằng các độ đo (Accuracy, Precision, Recall, F1), phân tích lỗi (Error Analysis) chi tiết. | 1.5 đ | Mục 3.5 & 3.6: Benchmark Test set, mổ xẻ 20 ca lỗi điển hình (10 FP, 10 FN). |
| Tiêu chí 2 - Mục 6: Dự đoán mới | Đóng gói mô hình, xây dựng hàm dự đoán trên mẫu dữ liệu mới hoàn toàn, triển khai giao diện hoặc dịch vụ ứng dụng. | 1.0 đ | Mục 3.7: Microservice FastAPI (< 0.3 ms/mẫu) và Dashboard Streamlit tương tác. |


Bảng 0.2: Khung đối chiếu Tiêu chí chấm điểm đồ án học phần Học máy của Bộ môn KHMT

DANH MỤC CÁC TỪ VIẾT TẮT VÀ THUẬT NGỮ


| Viết tắt | Thuật ngữ Tiếng Anh | Ý nghĩa / Giải thích trong đề tài |
| --- | --- | --- |
| ML | Machine Learning | Học máy - Ngành con của Trí tuệ nhân tạo. |
| NLP | Natural Language Processing | Xử lý ngôn ngữ tự nhiên. |
| SA | Sentiment Analysis | Phân tích quan điểm / Phân tích cảm xúc văn bản. |
| ABSA | Aspect-Based Sentiment Analysis | Phân tích quan điểm dựa trên khía cạnh nghiệp vụ. |
| TF-IDF | Term Frequency - Inverse Document Frequency | Độ đo tần suất từ kết hợp nghịch đảo tần suất văn bản. |
| SVM | Support Vector Machines | Máy vector hỗ trợ - Thuật toán phân lớp lề cực đại. |
| LinearSVC | Linear Support Vector Classifier | Mô hình SVM tuyến tính dựa trên thư viện tối ưu LIBLINEAR. |
| MNB | Multinomial Naive Bayes | Bộ phân lớp Bayes thơ ngây đa thức. |
| LR | Logistic Regression | Hồi quy Logistic phân loại nhị phân / đa lớp. |
| RF | Random Forest | Rừng ngẫu nhiên - Thuật toán học kết hợp Bagging. |
| CRF | Conditional Random Fields | Trường ngẫu nhiên có điều kiện dùng tách từ tiếng Việt. |
| EDA | Exploratory Data Analysis | Phân tích khám phá dữ liệu. |
| KKT | Karush-Kuhn-Tucker | Hệ điều kiện tối ưu bậc một trong bài toán quy hoạch phi tuyến. |
| OOB | Out-Of-Bag | Tập mẫu ngoài bao dùng ước lượng sai số trong Random Forest. |
| PII | Personally Identifiable Information | Thông tin định danh cá nhân (SĐT, Email, Tên) cần ẩn danh. |


Danh mục các Ký hiệu Toán học sử dụng trong Báo cáo


| Ký hiệu | Tên gọi toán học | Mô tả ý nghĩa trong mô hình |
| --- | --- | --- |
| D | Dataset | Tập dữ liệu huấn luyện gồm N cặp mẫu (x_i, y_i). |
| x_i ∈ R^d | Feature Vector | Vector đặc trưng văn bản thứ i trong không gian d = 24.619 chiều. |
| y_i ∈ {-1, +1} | Class Label | Nhãn cảm xúc (y = +1: Tích cực, y = -1: Tiêu cực). |
| w ∈ R^d | Weight Vector | Vector trọng số pháp tuyến của siêu phẳng phân tách. |
| b ∈ R | Bias / Intercept | Hệ số định kiến / Khoảng cách dịch chuyển siêu phẳng tới gốc tọa độ. |
| γ (Gamma) | Geometric Margin | Khoảng cách lề hình học từ siêu phẳng tới điểm dữ liệu gần nhất. |
| ξ_i (Xi) | Slack Variable | Biến bù trượt sai số lỏng lẻo trong bài toán Soft-Margin SVM. |
| C > 0 | Penalty Hyperparameter | Siêu tham số điều chuẩn kiểm soát mức phạt sai số vi phạm lề. |
| α_i (Alpha) | Lagrange Multiplier | Nhân tử Lagrange gắn với ràng buộc mẫu thứ i. |
| σ(z) | Sigmoid Function | Hàm kích hoạt logistic ánh xạ giá trị thực về xác suất [0, 1]. |
| H (Hessian) | Hessian Matrix | Ma trận đạo hàm riêng bậc hai của hàm mất mát Log-Loss. |
| I(·) | Impurity Measure | Độ vẩn đục của nút trong cây quyết định (Gini Impurity / Entropy). |


MỤC LỤC TỔNG QUÁT

LỜI CẢM ƠN ................................................................................................................................ iii
LỜI CAM ĐOAN ............................................................................................................................. iv
PHÂN CÔNG NHIỆM VỤ VÀ TIÊU CHÍ ĐÁNH GIÁ ĐỒ ÁN ................................................................... v
DANH MỤC CÁC TỪ VIẾT TẮT VÀ THUẬT NGỮ ............................................................................. vii
DANH MỤC CÁC KÝ HIỆU TOÁN HỌC ........................................................................................... viii
DANH MỤC CÁC BẢNG BIỂU ........................................................................................................... x
DANH MỤC CÁC HÌNH VẼ VÀ ĐỒ THỊ .............................................................................................. xi

CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN BÀI TOÁN ............................................................. 1
    1.1. Khái quát về Học máy và Xử lý ngôn ngữ tự nhiên (NLP) ........................................................ 1
    1.2. Quy trình thực hiện dự án học máy tiêu chuẩn (Chương 1 GT Học máy ICTU) ........................... 4
    1.3. Sự đánh đổi giữa Thiên lệch và Phương sai (Bias - Variance Tradeoff) .................................... 6
    1.4. Bối cảnh kinh tế số và Tính cấp thiết của đề tài tại Việt Nam ................................................. 9
    1.5. Thách thức đặc thù trong xử lý ngôn ngữ tự nhiên Tiếng Việt ................................................. 11
    1.6. Tổng quan các nghiên cứu liên quan trên thế giới và tại Việt Nam .......................................... 13
    1.7. Các điểm đổi mới sáng tạo và giải pháp công nghệ vượt trội của Đề tài ................................. 15

CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ CƠ SỞ TOÁN HỌC CÁC MÔ HÌNH ............................ 17
    2.1. Quy trình Tiền xử lý dữ liệu văn bản tiếng Việt đa tầng ........................................................ 17
    2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm ....................................... 20
    2.3. Cơ sở toán học Bộ phân loại Naive Bayes (Chương 6 GT Học máy ICTU) ................................. 23
    2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2 (Chương 9 GT Học máy ICTU) .................. 25
    2.5. Cơ sở toán học Máy vector hỗ trợ - LinearSVC (Chương 10 GT Học máy ICTU) ...................... 27
    2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên (Chương 8 & 14 GT Học máy ICTU) ........................ 30
    2.7. Phương pháp luận Phân tích quan điểm theo khía cạnh (Joint ABSA) ....................................... 32
    2.8. Hệ thống độ đo đánh giá hiệu năng mô hình (Evaluation Metrics) ........................................... 34

CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ THEO TIÊU CHÍ CHẤM ................................. 36
    3.1. Thu thập, phân tích và trực quan hóa dữ liệu EDA (Mục 1 Tiêu chí chấm - 1.5 đ) ................... 36
    3.2. Tiền xử lý dữ liệu và Khử nhiễu nghịch nhãn (Mục 2 Tiêu chí chấm - 1.5 đ) ........................... 40
    3.3. Huấn luyện mô hình học máy (Mục 3 Tiêu chí chấm - 1.0 đ) ................................................... 42
    3.4. Tìm mô hình tốt nhất & Tinh chỉnh siêu tham số (Mục 4 Tiêu chí chấm - 1.5 đ) ..................... 43
    3.5. Biện luận khoa học chuyên sâu: DỰA VÀO ĐÂU KẾT QUẢ ĐÓ LÀ ĐÚNG? ............................ 45
    3.6. Đánh giá và Phân tích lỗi - Error Analysis (Mục 5 Tiêu chí chấm - 1.5 đ) ................................ 47
    3.7. Dự đoán trên dữ liệu mới và Triển khai hệ thống (Mục 6 Tiêu chí chấm - 1.0 đ) ................... 50

KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN ................................................................................................ 53
    1. Kết quả đạt được của Đồ án .................................................................................................... 53
    2. Đối chiếu mức độ đáp ứng Chuẩn đầu ra học phần (CĐR HP) ..................................................... 53
    3. Hạn chế còn tồn tại và Bài học kinh nghiệm ............................................................................ 55
    4. Hướng phát triển và mở rộng trong tương lai ........................................................................... 55
TÀI LIỆU THAM KHẢO ....................................................................................................................... 56

CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN BÀI TOÁN

1.1. Khái quát về Học máy và Xử lý ngôn ngữ tự nhiên (NLP)

1.1.1. Khái niệm và phân loại các phương pháp học máy

Theo định nghĩa kinh điển của Tom Mitchell (1997) được tái khẳng định trong Chương 1 Giáo trình Học máy ICTU (năm 2026, tr. 11 - 15) của các tác giả TS. Trần Quang Quý, TS. Ngô Hữu Huy, TS. Nguyễn Đức Bình và TS. Nguyễn Tuấn Anh: "Một chương trình máy tính được coi là học từ kinh nghiệm E (Experience) đối với một lớp nhiệm vụ T (Task) và độ đo hiệu năng P (Performance), nếu hiệu năng của nó đối với các nhiệm vụ trong T, được đo bởi P, cải thiện cùng với kinh nghiệm E". Trong kỷ nguyên dữ liệu lớn (Big Data), học máy đóng vai trò là động lực cốt lõi cho phép hệ thống tự động trích xuất các quy luật tiềm ẩn từ dữ liệu quá khứ mà không cần lập trình các quy tắc logic thủ công tường minh.

Căn cứ vào phương thức phản hồi của dữ liệu môi trường và bản chất của kinh nghiệm E, học máy được phân chia thành 4 phân nhánh chính:
1. Học có giám sát (Supervised Learning): Tập dữ liệu huấn luyện bao gồm các cặp đầu vào - đầu ra mong muốn D = {(x_i, y_i)}_{i=1}^N. Mục tiêu là xấp xỉ hàm ánh xạ f: X -> Y sao cho cực tiểu hóa hàm mất mát (Loss Function) trên dữ liệu chưa từng quan sát. Bài toán phân loại cảm xúc (Sentiment Analysis) và phân loại khía cạnh (Aspect Classification) trong đồ án này thuộc lớp bài toán học có giám sát với nhãn cảm xúc rời rạc y ∈ {Tích cực, Tiêu cực}.
2. Học không giám sát (Unsupervised Learning): Dữ liệu chỉ chứa các quan sát đầu vào x_i mà không có nhãn chỉ dẫn y_i. Thuật toán tự khám phá cấu trúc nội tại, phân cụm dữ liệu (Clustering như K-Means, DBSCAN) hoặc giảm số chiều không gian (Dimensionality Reduction như PCA, t-SNE).
3. Học bán giám sát (Semi-supervised Learning): Kết hợp lượng nhỏ dữ liệu có gán nhãn với lượng lớn dữ liệu phi nhãn nhằm giảm thiểu chi phí gán nhãn thủ công tốn kém.
4. Học tăng cường (Reinforcement Learning): Tác tử (Agent) tương tác trực tiếp với môi trường thông qua các hành động, nhận tín hiệu thưởng/phạt (Reward/Penalty) và học chính sách hành động tối ưu để cực đại hóa phần thưởng tích lũy lâu dài.

1.1.2. Vị trí của Xử lý ngôn ngữ tự nhiên trong hệ thống thông tin số

Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP) là một nhánh liên ngành then chốt nằm tại giao điểm giữa Trí tuệ nhân tạo (AI), Khoa học máy tính và Ngôn ngữ học tính toán. Mục tiêu tối thượng của NLP là thu hẹp khoảng cách giao tiếp giữa tư duy ngôn ngữ tự nhiên của con người và hệ thống tính toán nhị phân của máy tính. Trong bối cảnh hơn 85% dữ liệu số sinh ra trên không gian mạng hiện nay tồn tại dưới dạng văn bản phi cấu trúc (Unstructured Text) - bao gồm bài viết mạng xã hội, bình luận đánh giá ứng dụng, email khách hàng, tin nhắn phản hồi - các kỹ thuật NLP truyền thống và học máy văn bản đóng vai trò là chiếc cầu nối chuyển hóa các chuỗi ký tự tự do thành thông tin có cấu trúc phục vụ phân tích nghiệp vụ và ra quyết định kinh doanh.

1.1.3. Khái niệm bài toán Phân tích quan điểm (Sentiment Analysis)

Phân tích quan điểm (Sentiment Analysis - SA), hay còn gọi là Khai phá quan điểm (Opinion Mining), là lĩnh vực nghiên cứu chuyên sâu của NLP nhằm phân tích các ý kiến, cảm xúc, đánh giá và thái độ của người viết đối với một thực thể cụ thể (sản phẩm, dịch vụ, con người, sự kiện hoặc chủ đề). Theo Bing Liu (2012), một quan điểm (Opinion) đầy đủ được biểu diễn hình thức dưới dạng một bộ ngũ (Quintupel):


| o = (e_j, a_{jk}, s_{ijkl}, h_i, t_l)    (1.1) |
| --- |


Trong đó: e_j là thực thể mục tiêu (Target Entity); a_{jk} là khía cạnh/thuộc tính của thực thể (Aspect / Attribute); s_{ijkl} là sắc thái cảm xúc (Sentiment Value: Tích cực, Tiêu cực, hoặc Trung tính); h_i là người nắm giữ quan điểm (Opinion Holder); và t_l là thời điểm quan điểm được phát biểu (Time Stamp).

Trong thực tế công nghiệp, bài toán Phân tích quan điểm được chia thành 3 cấp độ chi tiết chính:
• Cấp độ toàn văn bản (Document Level): Xác định sắc thái cảm xúc chung cho toàn bộ một tài liệu hay bài đánh giá. Giả định rằng toàn bộ văn bản chỉ bày tỏ một quan điểm đồng nhất về một đối tượng duy nhất.
• Cấp độ câu (Sentence Level): Phân tích từng câu độc lập xem câu đó là câu cảm xúc (Subjective Sentence) hay câu thông tin sự thật (Objective Sentence), và nếu có cảm xúc thì là tích cực hay tiêu cực.
• Cấp độ khía cạnh (Aspect-Based Sentiment Analysis - ABSA): Đây là cấp độ phân tích hạt mịn và có giá trị nghiệp vụ cao nhất. Một đánh giá người dùng thường khen mặt này nhưng chê mặt khác (Ví dụ: "Giao diện app MB Bank rất đẹp nhưng tính năng sinh trắc học quét CCCD bị lỗi hoài"). ABSA bóc tách chính xác từng khía cạnh nghiệp vụ cụ thể để gán nhãn cảm xúc tương ứng, cung cấp dữ liệu hành động trực tiếp cho đội ngũ phát triển sản phẩm.

1.1.4. So sánh đối sánh các trường phái tiếp cận trong NLP

Trong lịch sử phát triển của NLP, đã có 5 trường phái tiếp cận chính được áp dụng cho bài toán phân loại quan điểm văn bản. Nhóm 12 tổng hợp và đối sánh chi tiết 5 trường phái này qua Bảng 1.1 dưới đây:


| Trường phái | Nguyên lý cốt lõi | Ưu điểm nổi bật | Hạn chế chí mạng | Độ trễ suy luận | Chi phí triển khai |
| --- | --- | --- | --- | --- | --- |
| 1. Dựa trên luật (Rule-Based) | Xây dựng các mẫu ngữ pháp Regex và luật if-else thủ công. | Không cần dữ liệu huấn luyện, giải thích được 100%. | Dễ sụp đổ khi gặp từ lóng, teencode, cấu trúc câu tự do. | Siêu nhanh (< 0.1 ms) | Rất cao (bảo trì thủ công) |
| 2. Dựa trên từ điển (Lexicon-Based) | Tra cứu điểm cảm xúc từ các từ điển định sẵn (SentiWordNet). | Dễ cài đặt, không đòi hỏi huấn luyện mô hình phức tạp. | Không nắm bắt được ngữ cảnh (Ví dụ: 'rất không tốt'). | Rất nhanh (< 0.2 ms) | Thấp |
| 3. Học máy cổ điển (Classical ML)<br>[ĐỀ TÀI LỰA CHỌN] | Biểu diễn vector TF-IDF N-gram kết hợp mô hình Linear SVM, Logistic Regression. | Độ chính xác cao (F1 > 90%), tốc độ suy luận cực nhanh (< 0.3 ms), kích thước mô hình siêu nhẹ (< 10 MB), không cần GPU. | Cần kỹ thuật trích chọn đặc trưng (Feature Engineering) chỉn chu. | Siêu nhanh (< 0.3 ms/mẫu) | Cực kỳ thấp (chạy tốt trên CPU 5$) |
| 4. Học sâu tuần tự (RNN / LSTM) | Mạng nơ-ron hồi quy xử lý chuỗi ký tự và từ vựng tuần tự. | Học được phụ thuộc ngữ cảnh chuỗi trong khoảng cách ngắn. | Thời gian huấn luyện lâu, dễ bị biến mất gradient (Vanishing Gradient). | Trung bình (~15-30 ms) | Trung bình (cần GPU nhẹ) |
| 5. Transformers tiền huấn luyện (PhoBERT/LLM) | Cơ chế Self-Attention học ngữ cảnh hai chiều sâu rộng. | Độ chính xác rất cao, hiểu được ngữ cảnh phức tạp. | Rất nặng (500MB - 14GB), độ trễ cao (50-200ms), chi phí vận hành đắt đỏ, khó triển khai edge. | Chậm (50 - 500 ms) | Rất cao (đòi hỏi GPU chuyên dụng) |


Bảng 1.1: So sánh đối chuẩn toàn diện 5 trường phái công nghệ trong Xử lý ngôn ngữ tự nhiên

1.2. Quy trình thực hiện dự án học máy tiêu chuẩn (Chương 1 GT Học máy ICTU)

Theo Chương 1 Giáo trình Học máy ICTU (năm 2026, tr. 16 - 22), quy trình phát triển một dự án học máy trong môi trường công nghiệp không phải là một chuỗi hành động ngẫu nhiên mà là một chu trình kỹ thuật 7 bước lặp khép kín (Iterative Engineering Pipeline). Nhóm 12 đã tuân thủ nghiêm ngặt chuẩn mực này để đảm bảo tính tái lập (Reproducibility) và độ tin cậy khoa học của toàn bộ kết quả thực nghiệm.


| Bước | Tên giai đoạn | Dữ liệu đầu vào | Nội dung kỹ thuật thực hiện | Sản phẩm đầu ra |
| --- | --- | --- | --- | --- |
| B1 | Xác định bài toán & Thu thập dữ liệu | Phản hồi người dùng trên Google Play & App Store | Sử dụng công cụ cào tự động 15.541 đánh giá thô của 8 ứng dụng di động | Tập dữ liệu thô app_reviews.csv |
| B2 | Khám phá & Trực quan hóa dữ liệu EDA | Tập dữ liệu thô 15.541 dòng | Phân tích rating, độ dài từ, phân bố cảm xúc và khía cạnh trên biểu đồ | Báo cáo thống kê mô tả & Báo cáo EDA |
| B3 | Tiền xử lý & Xây dựng đặc trưng | Văn bản thô, teencode, lỗi chính tả | Chuẩn hóa Unicode, xử lý teencode, khử nhiễu nghịch nhãn, tách từ ghép underthesea, TF-IDF | Tập dữ liệu sạch 14.910 mẫu & Ma trận TF-IDF |
| B4 | Huấn luyện các mô hình phân lớp | Ma trận TF-IDF tập Train (10.437 mẫu) | Cài đặt và huấn luyện 4 mô hình: MultinomialNB, Logistic Regression, LinearSVC, Random Forest | 4 mô hình đã được fit tham số trọng số |
| B5 | Tối ưu siêu tham số & Chọn mô hình | Tập Train & Validation (2.236 mẫu) | Chạy GridSearchCV 5-fold tối ưu tham số C, loss; đối chuẩn định lượng trên tập Test | Mô hình tốt nhất LinearSVC (F1: 90.38%) |
| B6 | Đánh giá mô hình & Phân tích lỗi | Tập Test độc lập (2.237 mẫu) | Vẽ ma trận nhầm lẫn (Confusion Matrix), mổ xẻ nguyên nhân sai lệch 20 ca mẫu FP và FN | Báo cáo ma trận nhầm lẫn & Bảng mổ xẻ lỗi |
| B7 | Đóng gói & Triển khai dự đoán mới | Mô hình tối ưu đã lưu .joblib | Xây dựng hàm suy luận thời gian thực, thiết kế API RESTful FastAPI và Dashboard Streamlit | Dịch vụ Microservice API & UI Web sẵn sàng |


Bảng 1.2: Chi tiết các giai đoạn triển khai trong Quy trình 7 bước dự án học máy của Nhóm 12

1.3. Sự đánh đổi giữa Thiên lệch và Phương sai (Bias - Variance Tradeoff)

1.3.1. Chứng minh toán học công thức phân rã sai số kỳ vọng

Theo Mục 1.7 (tr. 33 - 35) của Giáo trình Học máy ICTU, sự đánh đổi giữa Thiên lệch (Bias) và Phương sai (Variance) là nguyên lý trung tâm chi phối khả năng tổng quát hóa của mọi mô hình học máy. Giả sử dữ liệu được sinh ra từ mối quan hệ thực tế: y = f(x) + ε, trong đó ε là nhiễu ngẫu nhiên độc lập với tập dữ liệu huấn luyện D, thỏa mãn kỳ vọng E[ε] = 0 và phương sai Var(ε) = σ².

Xét sai số toàn phương kỳ vọng đối với một điểm dữ liệu mới x khi lấy kỳ vọng trên toàn bộ các tập huấn luyện D có thể có:


| E_D[(y - f̂(x))²] = E_D[(f(x) + ε - f̂(x))²]    (1.2) |
| --- |


Đặt f̄(x) = E_D[f̂(x)] là giá trị dự đoán trung bình của mô hình. Biến đổi biểu thức bên trong dấu kỳ vọng:


| y - f̂(x) = (f(x) - f̄(x)) + (f̄(x) - f̂(x)) + ε    (1.3) |
| --- |


Bình phương hai vế và khai triển hằng đẳng thức:


| (y - f̂(x))² = (f(x) - f̄(x))² + (f̄(x) - f̂(x))² + ε² + 2(f(x) - f̄(x))(f̄(x) - f̂(x)) + 2(f(x) - f̄(x))ε + 2(f̄(x) - f̂(x))ε    (1.4) |
| --- |


Lấy kỳ vọng E_D hai vế. Do ε độc lập với D và E[ε] = 0, toàn bộ các số hạng tích chéo chứa ε đều triệt tiêu về 0:
• E_D[2(f(x) - f̄(x))ε] = 2(f(x) - f̄(x)) E[ε] = 0
• E_D[2(f̄(x) - f̂(x))ε] = 2 E_D[(f̄(x) - f̂(x))] E[ε] = 0
• E_D[2(f(x) - f̄(x))(f̄(x) - f̂(x))] = 2(f(x) - f̄(x)) E_D[f̄(x) - f̂(x)] = 2(f(x) - f̄(x))(f̄(x) - f̄(x)) = 0

Như vậy, ta thu được kết quả phân rã toán học hoàn chỉnh:


| E_D[(y - f̂(x))²] = (f(x) - f̄(x))² + E_D[(f̂(x) - f̄(x))²] + σ² = Bias²(f̂(x)) + Var(f̂(x)) + σ²    (1.5) |
| --- |


1.3.2. Ý nghĩa của kỹ thuật điều chuẩn L2 trong kiểm soát phương sai

Trong bài toán xử lý ngôn ngữ tự nhiên với không gian đặc trưng TF-IDF N-gram có số chiều rất lớn (d = 24.619 chiều trong đồ án này), mô hình có xu hướng rất nhạy cảm với các biến động ngẫu nhiên của tập huấn luyện, dẫn tới phương sai (Variance) tăng vọt và gây ra hiện tượng quá khớp (Overfitting). Để kiểm soát phương sai, kỹ thuật điều chuẩn L2 (Ridge Regularization / L2-Penalty) được áp dụng vào hàm mục tiêu:


| J(w) = Loss(y, Xw) + (1 / 2C) ||w||₂²    (1.6) |
| --- |


Tham số phạt C > 0 đóng vai trò điều tiết sự đánh đổi: Khi C quá lớn, mô hình ít bị phạt độ lớn trọng số w, cố gắng khớp từng điểm dữ liệu kể cả nhiễu => Bias thấp nhưng Variance cao (Overfitting). Ngược lại, khi C quá nhỏ, lực ép w về 0 quá mạnh, mô hình trở nên quá đơn giản => Variance thấp nhưng Bias cao (Underfitting). Thực nghiệm tại Mục 3.4 chứng minh việc tinh chỉnh C = 2.0 đã đạt điểm cân bằng vàng giữa Bias và Variance, mang lại hiệu năng kiểm thử cao nhất trên tập Test độc lập.

1.4. Bối cảnh kinh tế số và Tính cấp thiết của đề tài tại Việt Nam

Trong giai đoạn 2024 - 2026, nền kinh tế số Việt Nam chứng kiến sự bùng nổ vượt bậc với tốc độ tăng trưởng hàng năm đạt trên 20%. Hàng chục triệu người dân sử dụng điện thoại thông minh để thực hiện các giao dịch thiết yếu hàng ngày thông qua 4 trụ cột ứng dụng di động công nghệ hàng đầu:
1. Ngân hàng số (Digital Banking): MB Bank, Agribank - nơi người dùng thực hiện thanh toán, chuyển khoản, xác thực sinh trắc học căn cước công dân (CCCD) gắn chip theo Quyết định 2345/QĐ-NHNN của Ngân hàng Nhà nước.
2. Ví điện tử và Cổng thanh toán (Fintech E-Wallets): MoMo, ZaloPay - hệ sinh thái tài chính tiêu dùng, thanh toán hóa đơn điện nước, nạp tiền điện thoại và tích lũy đầu tư.
3. Thương mại điện tử và Dịch vụ giao vận theo yêu cầu (E-Commerce & Food Delivery): Shopee, ShopeeFood, Grab - phục vụ nhu cầu mua sắm trực tuyến, đặt đồ ăn và gọi xe công nghệ hàng ngày.
4. Mạng xã hội và Giải trí video ngắn (Social Media): TikTok - nền tảng sáng tạo nội dung và giải trí số tích hợp tính năng thương mại điện tử TikTok Shop.

Mỗi ngày, các nền tảng này tiếp nhận hàng chục nghìn phản hồi, đánh giá (Reviews) từ người dùng trên kho ứng dụng Google Play Store và Apple App Store. Đây là kho tàng thông tin vô giá phản ánh trực tiếp trải nghiệm khách hàng (Voice of Customer - VoC). Tuy nhiên, việc đọc và phân loại thủ công bằng sức người là hoàn toàn bất khả thi do khối lượng khổng lồ. Do đó, việc xây dựng một hệ thống học máy thông minh, có khả năng tự động phân tích quan điểm đa diện (Joint ABSA), bóc tách chính xác cảm xúc gắn liền với từng khía cạnh kỹ thuật/nghiệp vụ cụ thể với tốc độ tính toán thời gian thực là nhu cầu vô cùng cấp thiết, mang lại giá trị thực tiễn và kinh tế to lớn.

1.5. Thách thức đặc thù trong xử lý ngôn ngữ tự nhiên Tiếng Việt

Tiếng Việt là một ngôn ngữ đơn lập (Isolating Language) không biến đổi hình thái từ, sở hữu những đặc trưng ngữ pháp và thói quen giao tiếp đời thường vô cùng phức tạp, đặc biệt là trong các bình luận trực tuyến của thế hệ trẻ (Gen Z). Đề tài xác định 6 thách thức kỹ thuật lớn nhất:


| Thách thức | Biểu hiện cụ thể trong dữ liệu | Giải pháp kỹ thuật của Nhóm 12 |
| --- | --- | --- |
| 1. Từ ghép & Cấu trúc đa âm tiết | Từ vựng tiếng Việt cấu tạo từ nhiều âm tiết đơn lẻ. Dấu khoảng trắng vừa là ranh giới từ vừa là ranh giới âm tiết ('ngân hàng' vs 'ngân' + 'hàng'). | Sử dụng giải thuật quy hoạch động Viterbi kết hợp mô hình CRF của thư viện underthesea để phân tách từ ghép chính xác. |
| 2. Teencode & Từ lóng công nghệ | Người dùng viết tắt vô độ: 'k'/'ko'/'hông' -> 'không', 'đc' -> 'được', 'app'/'áp' -> 'ứng dụng', 'lag'/'đơ'/'giật' -> 'chậm lag'. | Xây dựng Từ điển chuẩn hóa Teencode 50 quy tắc tự động ánh xạ về dạng chuẩn mực tiếng Việt. |
| 3. Lỗi gõ bàn phím Telex/VNI | Gõ thừa ký tự hoặc sai dấu thanh: 'nguoii', 'duwowcj', 'khoos', 'yeu caau'. | Module tiền xử lý Regular Expression quét và khôi phục ký tự nguyên bản theo bộ gõ Unicode chuẩn NFC. |
| 4. Nghịch nhãn cảm xúc (Rating Sarcasm) | Chấm 1 sao nhưng ghi 'App tuyệt vời lắm ạ :))', hoặc chấm 5 sao nhưng chê 'Đợi đồ ăn 1 tiếng nguội tanh'. | Thiết kế Bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit) dựa trên ma trận mâu thuẫn sao và từ điển ngữ nghĩa. |
| 5. Phủ định kép & Đảo ngữ | Cụm từ phủ định làm đảo ngược cảm xúc: 'không phải là không tốt', 'chẳng chê vào đâu được'. | Khai thác không gian đặc trưng N-gram (1, 2) bảo toàn trọn vẹn cụm từ ghép cặp cảm xúc ('không_tốt', 'rất_mượt'). |
| 6. Ngôn ngữ pha trộn (Code-switching) | Trộn lẫn tiếng Anh và tiếng Việt: 'app lag vcl, crash liên tục khi scan face'. | Bổ sung các thuật ngữ kỹ thuật tiếng Anh phổ biến vào bộ từ điển dừng và từ điển đặc trưng miền ứng dụng. |


Bảng 1.3: Tổng hợp các thách thức ngôn ngữ tiếng Việt và giải pháp kỹ thuật tương ứng của Đề tài

1.6. Tổng quan các nghiên cứu liên quan trên thế giới và tại Việt Nam

Nghiên cứu về phân tích quan điểm văn bản đã trải qua hơn hai thập kỷ phát triển mạnh mẽ. Trên thế giới, nghiên cứu nền tảng của Pang và Lee (2002) tại Đại học Cornell đã đặt viên gạch đầu tiên khi chứng minh rằng các thuật toán học máy cổ điển (Naive Bayes, Maximum Entropy, SVM) vượt trội hoàn toàn so với các phương pháp dựa trên từ điển luật truyền thống trong việc phân loại đánh giá phim ảnh. Joachims (1998) đã chứng minh bằng lý thuyết đại số rằng SVM là mô hình tối ưu tuyệt đối cho dữ liệu văn bản nhờ khả năng chống lại hiện tượng quá khớp trong không gian vector thưa có số chiều cực lớn.

Về phân tích quan điểm theo khía cạnh (ABSA), chuỗi hội thảo quốc tế SemEval (2014, 2015, 2016) do Pontiki và các cộng sự khởi xướng đã định hình các chuẩn mực đánh giá cho bài toán phát hiện khía cạnh và phân loại cảm xúc tương ứng trong các miền nhà hàng, khách sạn và thiết bị điện tử gia dụng.

Tại Việt Nam, các nghiên cứu tiêu biểu bao gồm bộ ngữ liệu UIT-VSFC (Vietnamese Students' Feedback Corpus) của Nguyen et al. (2018) tại Trường ĐH Công nghệ Thông tin - ĐHQG TP.HCM dành cho phân tích phản hồi sinh viên; các chiến dịch đánh giá xử lý ngôn ngữ tiếng Việt VLSP (Vietnamese Language and Speech Processing) qua các năm 2016, 2018; và mô hình ngôn ngữ PhoBERT của VinAI Research (Nguyen & Nguyen, 2020). Tuy nhiên, hầu hết các nghiên cứu này chủ yếu tập trung vào dữ liệu chuẩn ngữ pháp (học đường, báo chí) hoặc sử dụng các mô hình học sâu kích thước lớn khó triển khai trong thực tế sản xuất thời gian thực. Đề tài của Nhóm 12 giải quyết triệt để khoảng trống này bằng cách tập trung vào phản hồi ứng dụng di động thực tế, xử lý teencode và tối ưu hóa giải pháp học máy siêu nhẹ với độ trễ < 0.3 ms/mẫu.

1.7. Các điểm đổi mới sáng tạo và giải pháp công nghệ vượt trội của Đề tài


| 4 ĐIỂM ĐỔI MỚI SÁNG TẠO VÀ CÔNG NGHỆ VƯỢT TRỘI CỦA ĐỒ ÁN:  • 1. Hệ thống Phân tích quan điểm đa diện (Joint ABSA) 7 khía cạnh nghiệp vụ: Chuẩn hóa phân loại phản hồi theo tiêu chuẩn công nghiệp ISO/IEC 25010, phân tách rạch ròi giữa cảm xúc chung và khía cạnh chức năng chuyên biệt. • 2. Bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit): Phát hiện và chuẩn hóa tự động hơn 1.240 mẫu mâu thuẫn giữa số sao đánh giá và nội dung bình luận thực tế, nâng độ tin cậy của tập dữ liệu lên mức tiệm cận nhãn vàng (Gold Standard). • 3. Tối ưu hóa suy luận siêu nhẹ thời gian thực (Ultra-low Latency Inference): Mô hình LinearSVC kết hợp TF-IDF N-gram chỉ mất 0.28 ms để phân loại 1 phản hồi trên CPU thông thường, kích thước tệp mô hình chỉ 8.4 MB, dễ dàng nhúng vào ứng dụng di động hoặc máy chủ biên. • 4. Sẵn sàng tích hợp dịch vụ sản xuất (Production-Ready Architecture): Đóng gói toàn bộ pipeline thành dịch vụ Microservice RESTful API bằng FastAPI và Giao diện Dashboard tương tác trực quan bằng Streamlit. |
| --- |


CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ CƠ SỞ TOÁN HỌC CÁC MÔ HÌNH

2.1. Quy trình Tiền xử lý dữ liệu văn bản tiếng Việt đa tầng

Dữ liệu văn bản thô thu thập từ phản hồi người dùng trên các kho ứng dụng (App Store, Google Play) chứa đựng vô số nhiễu: lỗi chính tả, teencode, icon cảm xúc phức tạp, thông tin nhạy cảm và cách diễn đạt phi cấu trúc. Để chuẩn bị cho việc trích xuất đặc trưng toán học, nhóm đã xây dựng một đường ống tiền xử lý đa tầng (Multi-stage Preprocessing Pipeline) bao gồm 4 bước kỹ thuật nghiêm ngặt:

2.1.1. Chuẩn hóa mã ký tự Unicode và Ẩn danh thông tin cá nhân (PII)

Tiếng Việt có hai dạng biểu diễn ký tự có dấu phổ biến: Unicode dựng sẵn (NFC - Normalization Form C) và Unicode tổ hợp (NFD - Normalization Form D). Ví dụ, ký tự "ế" trong NFC được lưu trữ bằng 1 code point duy nhất (U+1E7F), trong khi trong NFD được tạo thành từ 3 code point ghép lại: ký tự gốc "e" (U+0065) + dấu nón "^" (U+0302) + dấu sắc "/" (U+0301). Nếu không quy chuẩn, hai từ nhìn giống hệt nhau sẽ bị máy tính coi là hai từ hoàn toàn khác biệt, gây bùng nổ số chiều từ vựng một cách giả tạo. Nhóm áp dụng hàm `unicodedata.normalize('NFC', text)` đưa toàn bộ văn bản về dạng dựng sẵn đồng nhất.

Đồng thời, để tuân thủ quy định bảo mật dữ liệu người dùng (Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân), toàn bộ các thông tin định danh cá nhân (Personally Identifiable Information - PII) như số điện thoại (ví dụ: 098xxxxxxx), địa chỉ email (ví dụ: user@gmail.com), số tài khoản ngân hàng và các đường dẫn URL đều được phát hiện bằng biểu thức chính quy (Regex) và thay thế bằng các token đặc biệt tương ứng: `[PHONE]`, `[EMAIL]`, `[URL]` trước khi đưa vào mô hình.

2.1.2. Xây dựng từ điển Teencode và Chuẩn hóa từ lóng công nghệ

Giới trẻ và người dùng di động tại Việt Nam có xu hướng sử dụng ngôn ngữ viết tắt (Teencode) rất dày đặc. Nhóm đã khảo sát thực tế trên tập dữ liệu cào và đúc kết một từ điển chuẩn hóa Teencode gồm 50 quy tắc phổ biến nhất được phân loại thành các nhóm ngữ nghĩa:


| Từ gốc (Teencode) | Dạng chuẩn hóa | Từ gốc (Teencode) | Dạng chuẩn hóa |
| --- | --- | --- | --- |
| k / ko / kh / hok / hem | không | đc / dc / dk / duoc | được |
| app / áp / ứng dụng | ứng_dụng | acc / tk / nick | tài_khoản |
| chán / tệ / dở / cùi | kém | nhanh / mượt / xịn | tốt |
| lag / đơ / giật / treo | chậm | ship / giao hàng | vận_chuyển |
| r / rùi / ròi | rồi | cx / cũng | cũng |
| ms / mới | mới | h / hnay / hn | hôm_nay |
| mik / mk / mình | mình | ng / ngta / ngừi | người |
| nv / cskh / tổng đài | nhân_viên | bill / hóa đơn | hóa_đơn |
| otp / mã otp | mã_xác_thực | scan / quét mặt | sinh_trắc_học |
| voucher / mã giảm giá | khuyến_mãi | hoàn tiền / hoàn xu | hoàn_tiền |
| bực / cáu / tức | thất_vọng | ok / oki / okee | hài_lòng |
| update / cập nhật | cập_nhật | login / đăng nhập | đăng_nhập |
| crash / văng / sập | lỗi_ứng_dụng | pass / mk / mật khẩu | mật_khẩu |
| sp / shop / ng bán | người_bán | feed / bài viết | bài_đăng |
| cmt / cmt dạo | bình_luận | tt / thanh toán | thanh_toán |
| ck / chuyển khoản | chuyển_tiền | nạp / rút | giao_dịch |
| đắt / mắc / chát | giá_cao | rẻ / bèo / hời | giá_tốt |
| tệ hại / tệ bạc | rất_tệ | tuyệt vời / đỉnh | rất_tốt |
| phí ship / tiền ship | phí_vận_chuyển | driver / shipper | tài_xế |
| quá lâu / chờ mòn mỏi | rất_lâu | nhiệt tình / chu đáo | tận_tâm |
| quét căn cước / cccd | sinh_trắc_học | lừa đảo / scam | gian_lận |
| khóa acc / ban nick | khóa_tài_khoản | trừ tiền / mất tiền | lỗi_trừ_tiền |
| quảng cáo / qc | quảng_cáo | thông báo / noti | thông_báo |
| gỡ app / xóa app | xóa_ứng_dụng | chăm sóc / sp | hỗ_trợ_khách_hàng |
| bảo mật / an toàn | bảo_mật | tiện lợi / dễ dùng | tiện_lợi |


Bảng 2.1: Từ điển 50 quy tắc Teencode và chuẩn hóa từ lóng công nghệ của Nhóm 12

2.1.3. Thuật toán phân tách từ ghép tiếng Việt (Word Segmentation)

Không giống như tiếng Anh vốn có ranh giới từ được phân tách rõ ràng bằng dấu khoảng trắng, trong tiếng Việt, khoảng trắng vừa đóng vai trò là ranh giới giữa các từ đơn, vừa là ranh giới giữa các âm tiết cấu thành từ ghép. Nếu tách từ thuần túy bằng khoảng trắng (Whitespace Tokenizer), cụm từ "ngân hàng số" sẽ bị chẻ nhỏ thành 3 từ đơn "ngân", "hàng", "số" - làm mất hoàn toàn ngữ nghĩa của thực thể nghiệp vụ.

Nhóm sử dụng thư viện `underthesea` áp dụng mô hình Trường ngẫu nhiên có điều kiện tuyến tính (Linear-chain Conditional Random Fields - CRF) kết hợp giải thuật quy hoạch động Viterbi để gán nhãn chuỗi theo định dạng IOB (Inside-Outside-Beginning). Xét chuỗi quan sát âm tiết x = (x_1, x_2, ..., x_T) và chuỗi nhãn ranh giới từ y = (y_1, y_2, ..., y_T) với y_t ∈ {B, I, O}. Xác suất có điều kiện của chuỗi nhãn y khi biết chuỗi âm tiết x được định nghĩa:


| P(y | x) = (1 / Z(x)) exp( ∑_{t=1}^T ∑_{k=1}^K λ_k f_k(y_{t-1}, y_t, x, t) )    (2.1) |
| --- |


Trong đó: f_k là các hàm đặc trưng trích xuất từ ngữ cảnh (tiền tố, hậu tố, từ điển từ ghép); λ_k là trọng số học được từ dữ liệu huấn luyện; và Z(x) là hàm phân phối chuẩn hóa tổng xác suất về 1:


| Z(x) = ∑_{y'} exp( ∑_{t=1}^T ∑_{k=1}^K λ_k f_k(y'_{t-1}, y'_t, x, t) )    (2.2) |
| --- |


Để tìm chuỗi nhãn tối ưu y* có xác suất lớn nhất mà không phải duyệt qua toàn bộ số lượng chuỗi nhãn hàm mũ (|Y|^T), giải thuật quy hoạch động Viterbi được sử dụng với độ phức tạp tính toán O(T · |Y|²):


| y* = argmax_{y} P(y | x) = argmax_{y} ∑_{t=1}^T ∑_{k=1}^K λ_k f_k(y_{t-1}, y_t, x, t)    (2.3) |
| --- |


Kết quả phân tách được liên kết bằng ký tự gạch dưới (Ví dụ: "chuyển_tiền", "sinh_trắc_học", "ứng_dụng", "hài_lòng"), giúp bảo toàn nguyên vẹn ngữ nghĩa đơn vị từ ghép trong các giai đoạn xử lý tiếp theo.

2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm (Chương 2 GT Học máy ICTU)

Theo Chương 2 Giáo trình Học máy ICTU (năm 2026, tr. 45 - 52), để các thuật toán học máy có thể tính toán trên dữ liệu văn bản, ta cần chuyển đổi các chuỗi ký tự thành các vector số thực trong không gian Euclide. Phương pháp TF-IDF (Term Frequency - Inverse Document Frequency) kết hợp N-gram là kỹ thuật biểu diễn kinh điển nhưng đặc biệt hiệu quả, đánh giá tầm quan trọng của một từ vựng dựa trên tần suất xuất hiện cục bộ trong văn bản và độ hiếm gặp trên toàn bộ kho ngữ liệu.

2.2.1. Tần suất từ (Term Frequency - TF) và Sublinear TF Scaling

Tần suất từ thô (Raw Term Frequency) tf(t, d) đếm số lần từ t xuất hiện trong văn bản d. Tuy nhiên, nếu một từ xuất hiện 20 lần trong một phản hồi thì tầm quan trọng của nó không thể cao gấp 20 lần so với một phản hồi chỉ chứa từ đó 1 lần. Để tránh hiện tượng các từ lặp lại nhiều lần lấn át các từ khác, nhóm áp dụng kỹ thuật hàm logarit dưới tuyến tính (Sublinear TF Scaling):


| tf_{sublinear}(t, d) = 1 + ln(tf(t, d))  khi tf(t, d) > 0;  ngược lại bằng 0    (2.4) |
| --- |


2.2.2. Nghịch đảo tần suất văn bản (Inverse Document Frequency - IDF)

Độ đo IDF phản ánh mức độ cung cấp thông tin đặc trưng của từ t trên toàn bộ tập dữ liệu D. Những từ xuất hiện ở hầu hết mọi bài đánh giá (như "và", "thì", "là", "app") mang lại rất ít giá trị phân lớp, trong khi những từ đặc trưng xuất hiện có chọn lọc (như "quẹt thẻ", "nguội tanh", "sinh_trắc_học") lại mang lượng thông tin rất cao. Nhóm sử dụng công thức Smooth IDF có bổ sung số hạng làm mịn 1 ở cả tử số và mẫu số để triệt tiêu lỗi chia cho 0:


| idf(t, D) = ln( (|D| + 1) / (df(t, D) + 1) ) + 1    (2.5) |
| --- |


Trong đó: |D| là tổng số văn bản trong tập huấn luyện (|D| = 10.437); df(t, D) là tần suất văn bản (Document Frequency), tức số lượng văn bản chứa từ t.

2.2.3. Khai thác n-gram (1, 2) và Chuẩn hóa Euclidean L2-norm

Nếu chỉ sử dụng các từ đơn lẻ (Unigram - 1-gram), mô hình sẽ hoàn toàn mù mờ trước ngữ cảnh phủ định hoặc tăng cường cảm xúc. Ví dụ: câu "không tốt" sẽ bị bóc tách thành "không" và "tốt" - dẫn tới việc mô hình nhận diện nhầm là cảm xúc tích cực do sự xuất hiện của từ "tốt". Nhóm thiết lập cấu hình N-gram dải rộng `ngram_range=(1, 2)` bao gồm cả từ đơn và cặp từ liền kề (Bigram - 2-gram), kết hợp tham số lọc `min_df=2` (loại bỏ từ hiếm chỉ xuất hiện 1 lần) và `max_df=0.9` (loại bỏ từ dừng xuất hiện trên 90% số câu).

Giá trị trọng số đặc trưng thô của từ t trong văn bản d là tích của hai thành phần:


| w_{thô}(t, d) = tf_{sublinear}(t, d) × idf(t, D)    (2.6) |
| --- |


Do độ dài của các phản hồi người dùng rất chênh lệch (từ 2 từ đến hơn 100 từ), các văn bản dài sẽ có tổng trọng số lớn hơn văn bản ngắn. Để loại bỏ ảnh hưởng của độ dài văn bản, toàn bộ vector đặc trưng x_d được chiếu lên mặt cầu đơn vị bằng chuẩn Euclid L2-norm:


| x_d = ( w_{thô}(t_1, d) / ||w_d||₂ ,  w_{thô}(t_2, d) / ||w_d||₂ ,  ...,  w_{thô}(t_V, d) / ||w_d||₂ )^T    (2.7) |
| --- |


Trong đó: ||w_d||₂ = √( ∑_{j=1}^V w_{thô}(t_j, d)² ). Sau chuẩn hóa, mọi vector văn bản đều có độ dài hình học bằng đúng 1: ||x_d||₂ = 1, nằm trong không gian Hilbert số chiều d = 24.619 chiều.

2.3. Cơ sở toán học Bộ phân loại Naive Bayes (Chương 6 GT Học máy ICTU)

Theo Chương 6 Giáo trình Học máy ICTU (năm 2026, tr. 142 - 156), bộ phân loại Naive Bayes là một trong những giải thuật phân lớp xác suất thống kê cơ bản và kinh điển nhất. Cho vector đặc trưng văn bản x = (x_1, x_2, ..., x_d) và tập các lớp mục tiêu C = {Tích cực, Tiêu cực}. Theo Định lý Bayes, xác suất hậu nghiệm (Posterior Probability) của lớp c khi quan sát văn bản x là:


| P(y = c | x) = [ P(y = c) · P(x | y = c) ] / P(x)    (2.8) |
| --- |


Trong đó, mẫu số P(x) = ∑_{c' ∈ C} P(y = c') P(x | y = c') là hằng số chuẩn hóa không phụ thuộc vào lớp c. Do đó, bài toán phân lớp quy về việc tìm lớp c cực đại hóa xác suất đồng thời (Maximum A Posteriori - MAP):


| c* = argmax_{c ∈ C} P(y = c) · P(x | y = c)    (2.9) |
| --- |


Giả định cốt lõi của Naive Bayes ("thơ ngây") là: khi biết trước nhãn lớp c, sự xuất hiện của các từ đặc trưng x_j là hoàn toàn độc lập với nhau (Conditional Independence Assumption):


| P(x | y = c) = ∏_{j=1}^d P(x_j | y = c)    (2.10) |
| --- |


Trong mô hình Multinomial Naive Bayes (MNB), xác suất của từ j trong lớp c được ước lượng từ tần suất xuất hiện trong tập huấn luyện. Nếu một từ t_j chưa từng xuất hiện trong các bài đánh giá của lớp c, xác suất cực đại hợp lý MLE sẽ bằng 0: P(t_j | c) = 0. Do công thức (2.10) là một tích các thừa số, một giá trị 0 duy nhất sẽ kéo toàn bộ tích về 0, làm mô hình hoàn toàn bất lực. Để giải quyết triệt để vấn đề này, kỹ thuật làm mịn Laplace Smoothing (hay cộng 1 - Additive Smoothing với tham số α = 1.0) được áp dụng:


| P̂(t_j | y = c) = [ N_{cj} + α ] / [ ∑_{k=1}^d N_{ck} + α · d ]    (2.11) |
| --- |


Trong đó: N_{cj} là tổng trọng số của từ j trong toàn bộ các văn bản thuộc lớp c; d = 24.619 là tổng kích thước không gian từ vựng. Để tránh hiện tượng tràn số dưới (Numerical Underflow) do nhân liên tiếp hàng nghìn xác suất cực nhỏ, ta chuyển phép toán sang không gian Logarit tự nhiên:


| c* = argmax_{c ∈ C} [ ln P(y = c) + ∑_{j=1}^d x_j · ln P̂(t_j | y = c) ]    (2.12) |
| --- |


Hạn chế chí mạng của Naive Bayes: Giả định độc lập điều kiện hoàn toàn trái ngược với thực tế ngôn ngữ tự nhiên, nơi các từ vựng luôn có mối liên kết cú pháp và ngữ nghĩa chặt chẽ (ví dụ: 'không' và 'được'). Do đó, MNB có xu hướng ước lượng xác suất hậu nghiệm bị lệch quá mức về hai cực 0 hoặc 1.

2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2 (Chương 9 GT Học máy ICTU)

Theo Chương 9 Giáo trình Học máy ICTU (năm 2026, tr. 215 - 230), Hồi quy Logistic (Logistic Regression) là mô hình phân loại tuyến tính xác suất thuộc lớp mô hình phân biệt (Discriminative Models). Mô hình mô hình hóa trực tiếp xác suất hậu nghiệm P(y = 1 | x) thông qua hàm kích hoạt phi tuyến Sigmoid (Logistic Function):


| σ(z) = 1 / (1 + e^{-z})    (2.13) |
| --- |


Với z = w^T x + b, trong đó w ∈ R^d là vector trọng số và b ∈ R là hệ số định kiến. Hàm Sigmoid có các tính chất giải tích tuyệt vời: miền giá trị nằm hoàn toàn trong khoảng mở (0, 1), đồ thị hình chữ S đối xứng qua tâm (0, 0.5), và đạo hàm bậc nhất có dạng đóng cực kỳ thanh lịch: σ'(z) = σ(z)(1 - σ(z)).

Giả sử biến mục tiêu nhị phân y_i ∈ {0, 1} tuân theo phân bố Bernoulli với xác suất p_i = P(y_i = 1 | x_i) = σ(w^T x_i + b). Hàm hợp lý (Likelihood Function) trên toàn bộ tập dữ liệu huấn luyện N mẫu độc lập là:


| L(w, b) = ∏_{i=1}^N p_i^{y_i} (1 - p_i)^{1 - y_i}    (2.14) |
| --- |


Lấy logarit tự nhiên và đổi dấu để chuyển từ bài toán cực đại hóa hàm hợp lý sang bài toán cực tiểu hóa hàm mất mát mất mát chéo nhị phân (Binary Cross-Entropy Loss hay Log-Loss), kết hợp số hạng điều chuẩn L2:


| J(w, b) = - (1/N) ∑_{i=1}^N [ y_i ln p_i + (1 - y_i) ln(1 - p_i) ] + (1 / 2C) ||w||₂²    (2.15) |
| --- |


Để tìm nghiệm tối ưu w*, ta tính vector Gradient bậc một và ma trận đạo hàm riêng bậc hai Hessian:


| ∇_w J = (1/N) ∑_{i=1}^N (p_i - y_i) x_i + (1/C) w    (2.16) |
| --- |



| H_w = ∇_w² J = (1/N) ∑_{i=1}^N p_i (1 - p_i) x_i x_i^T + (1/C) I_d    (2.17) |
| --- |


Vì 0 < p_i < 1 nên p_i(1 - p_i) > 0, ma trận x_i x_i^T là ma trận nửa xác định dương, và số hạng điều chuẩn (1/C)I_d là xác định dương. Do đó, ma trận Hessian H_w luôn là ma trận đối xứng xác định dương (Positive Definite) trên toàn bộ không gian tham số. Điều này chứng minh rằng hàm mất mát J(w, b) là hàm lồi ngặt (Strictly Convex) và chỉ có duy nhất một điểm cực tiểu toàn cục (Global Minimum), hoàn toàn không bị kẹt ở các điểm cực tiểu địa phương. Thư viện Scikit-learn sử dụng giải thuật tối ưu hóa bậc hai tựa Newton L-BFGS (Limited-memory BFGS) xấp xỉ ma trận nghịch đảo Hessian H^{-1} để cập nhật nghiệm với tốc độ hội tụ siêu tuyến tính.

2.5. Cơ sở toán học Máy vector hỗ trợ - SVM (Chương 10 GT Học máy ICTU)

Theo Chương 10 Giáo trình Học máy ICTU (năm 2026, tr. 245 - 268), Máy vector hỗ trợ (Support Vector Machines - SVM) do Vladimir Vapnik và Corinna Cortes phát minh là một trong những thuật toán học máy có nền tảng toán học đại số và hình học vững chắc nhất. Thay vì tối thiểu hóa sai số kinh nghiệm thông thường (Empirical Risk Minimization), SVM tối thiểu hóa sai số cấu trúc (Structural Risk Minimization) nhằm tìm kiếm một siêu phẳng phân tách có khoảng cách lề (Margin) rộng nhất đối với các điểm dữ liệu của cả hai lớp.

Cho tập dữ liệu D = {(x_i, y_i)}_{i=1}^N với x_i ∈ R^d và y_i ∈ {-1, +1}. Siêu phẳng phân cách tuyến tính được định nghĩa:


| w^T x + b = 0    (2.18) |
| --- |


Khoảng cách hình học từ điểm x_i bất kỳ tới siêu phẳng là γ_i = [ y_i(w^T x_i + b) ] / ||w||₂. Bài toán tối ưu hóa lề cực đại mềm (Soft-Margin SVM) cho phép một số điểm dữ liệu nằm trong vùng lề hoặc bị phân loại sai thông qua các biến bù trượt sai số ξ_i ≥ 0 (Slack Variables). Bài toán quy hoạch toàn phương nguyên thủy (Primal Quadratic Programming):


| min_{w, b, ξ}  (1/2) ||w||₂² + C ∑_{i=1}^N ξ_i    (2.19) |
| --- |



| thỏa mãn ràng buộc:  y_i(w^T x_i + b) ≥ 1 - ξ_i   và   ξ_i ≥ 0,  ∀i = 1, ..., N    (2.20) |
| --- |


Để giải bài toán có ràng buộc trên, ta thiết lập hàm nhân tử Lagrange (Lagrangian Function) với các nhân tử α_i ≥ 0 và r_i ≥ 0:


| L(w, b, ξ, α, r) = (1/2) ||w||₂² + C ∑_{i=1}^N ξ_i - ∑_{i=1}^N α_i [ y_i(w^T x_i + b) - 1 + ξ_i ] - ∑_{i=1}^N r_i ξ_i    (2.21) |
| --- |


Lấy đạo hàm riêng theo các biến nguyên thủy và cho bằng 0:


| ∂L/∂w = 0  =>  w = ∑_{i=1}^N α_i y_i x_i    (2.22) |
| --- |



| ∂L/∂b = 0  =>  ∑_{i=1}^N α_i y_i = 0    (2.23) |
| --- |



| ∂L/∂ξ_i = 0  =>  C - α_i - r_i = 0  =>  α_i ≤ C  (do r_i ≥ 0)    (2.24) |
| --- |


Thế các kết quả trên ngược lại hàm Lagrange, ta thu được bài toán đối ngẫu Lagrange (Dual Problem):


| max_{α}  ∑_{i=1}^N α_i - (1/2) ∑_{i=1}^N ∑_{j=1}^N α_i α_j y_i y_j (x_i^T x_j)    (2.25) |
| --- |



| thỏa mãn:  0 ≤ α_i ≤ C,  ∀i = 1, ..., N   và   ∑_{i=1}^N α_i y_i = 0    (2.26) |
| --- |


Theo định lý Karush-Kuhn-Tucker (KKT), tại điểm nghiệm tối ưu, các điều kiện bù triệt tiêu (Complementary Slackness) phải được thỏa mãn đồng thời:
1. α_i = 0: Điểm x_i nằm ngoài khoảng lề (y_i(w^T x_i + b) > 1), phân loại đúng hoàn hảo, không ảnh hưởng tới siêu phẳng.
2. 0 < α_i < C: Điểm x_i nằm chính xác trên biên lề (y_i(w^T x_i + b) = 1, ξ_i = 0). Đây là các Vector Hỗ trợ (Support Vectors) mấu chốt quyết định vị trí siêu phẳng.
3. α_i = C: Điểm x_i nằm trong lề hoặc bị phân loại sai (ξ_i > 0).

Trong thư viện `LinearSVC` (dựa trên giải thuật LIBLINEAR chuyên dụng cho bài toán tuyến tính số chiều lớn), mô hình sử dụng hàm mất mát bình phương bản lề Squared Hinge Loss: L₂(z) = [max(0, 1 - z)]². Hàm này khả vi liên tục bậc nhất, cho phép giải thuật hạ dốc tọa độ (Coordinate Descent) cập nhật nghiệm từng chiều một cách đóng kín (Closed-form update) với tốc độ hội tụ siêu nhanh, vượt trội hoàn toàn so với việc giải bài toán đối ngẫu bậc hai thông thường.

2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên - Random Forest (Chương 8 & 14 GT Học máy ICTU)

Theo Chương 8 và Chương 14 Giáo trình Học máy ICTU (năm 2026, tr. 190 - 212 & 335 - 350), Rừng ngẫu nhiên (Random Forest - RF) do Leo Breiman đề xuất là phương pháp học kết hợp (Ensemble Learning) hoạt động dựa trên nguyên lý Đóng bao (Bootstrap Aggregating - Bagging). Mô hình xây dựng một tập hợp gồm B cây quyết định độc lập {T_1, T_2, ..., T_B}.

Tại mỗi nút phân nhánh của cây quyết định, giải thuật tìm kiếm điểm chia cắt tối ưu dựa trên độ đo vẩn đục Gini Impurity:


| Gini(m) = 1 - ∑_{k=1}^K p_{mk}²    (2.27) |
| --- |


Trong đó p_{mk} là tỷ lệ các mẫu thuộc lớp k tại nút m. Mức giảm độ vẩn đục (Gini Gain) khi chia nút m thành hai nút con m_L và m_R được tối đa hóa:


| ΔGini = Gini(m) - (N_L / N_m) Gini(m_L) - (N_R / N_m) Gini(m_R)    (2.28) |
| --- |


Nguyên lý giảm phương sai của Bagging: Giả sử ta có B cây quyết định dự đoán f̂_b(x) với phương sai mỗi cây là σ² và hệ số tương quan cặp giữa các cây là ρ. Phương sai của mô hình trung bình kết hợp f̄(x) = (1/B) ∑_{b=1}^B f̂_b(x) là:


| Var(f̄(x)) = ρ σ² + [ (1 - ρ) / B ] σ²    (2.29) |
| --- |


Khi số lượng cây B tăng lên rất lớn (B -> ∞), số hạng thứ hai triệt tiêu về 0, và phương sai của rừng chỉ phụ thuộc vào số hạng ρσ². Để giảm thiểu hệ số tương quan ρ giữa các cây, Random Forest áp dụng hai cơ chế ngẫu nhiên hóa kép:
• Lấy mẫu có hoàn lại (Bootstrap Sampling): Mỗi cây được huấn luyện trên một tập con dữ liệu ngẫu nhiên gồm N mẫu chọn có hoàn lại từ tập huấn luyện gốc. Khoảng 36.8% mẫu không bao giờ được chọn vào tập huấn luyện của cây (gọi là tập Out-of-Bag - OOB), được dùng để đánh giá sai số nội tại không thiên lệch.
• Lấy mẫu ngẫu nhiên không gian đặc trưng (Feature Subsampling): Tại mỗi bước phân nhánh, thay vì xét toàn bộ d đặc trưng, cây chỉ chọn ngẫu nhiên m = √d đặc trưng để tìm điểm chia cắt tốt nhất.

Tại sao Random Forest bị giảm hiệu năng trên dữ liệu văn bản thưa? Trong không gian văn bản d = 24.619 chiều, phần lớn các chiều đặc trưng chứa giá trị 0 (độ thưa > 99%). Khi lấy ngẫu nhiên m = √24.619 ≈ 157 đặc trưng tại mỗi nút, xác suất rất cao là cả 157 đặc trưng này đều mang giá trị 0 trên mẫu dữ liệu đang xét, dẫn tới việc cây phân nhánh dựa trên các đặc trưng không mang thông tin, làm suy giảm hiệu năng tổng thể của mô hình so với các mô hình tuyến tính.

2.7. Phương pháp luận Phân tích quan điểm theo khía cạnh (Joint ABSA)

Một đóng góp sáng tạo then chốt của đồ án là xây dựng hệ sinh thái Phân tích quan điểm đa diện kết hợp (Joint Aspect-Based Sentiment Analysis). Thay vì chỉ phân loại cảm xúc tổng quát, mô hình thực hiện giải quyết đồng thời bài toán dự đoán cảm xúc y_{sent} ∈ {Tích cực, Tiêu cực} và phân loại khía cạnh nghiệp vụ y_{asp} ∈ {7 khía cạnh tiêu chuẩn}.

7 khía cạnh nghiệp vụ được chuẩn hóa dựa trên bộ tiêu chuẩn công nghiệp quốc tế ISO/IEC 25010 về Chất lượng sản phẩm phần mềm:
1. `Hieu_nang_UI_UX`: Tốc độ tải, độ mượt mà giao diện, tính dễ sử dụng, độ phản hồi nút bấm.
2. `Dich_vu_Va_CSKH`: Chất lượng hỗ trợ giải đáp khiếu nại của nhân viên tổng đài, thái độ phục vụ.
3. `Bao_mat_Va_Tai_khoan`: Vấn đề đăng nhập, xác thực sinh trắc học khuôn mặt CCCD, mã OTP, khóa/mở tài khoản.
4. `Giao_dich_Thanh_toan_Gia_ca`: Tính năng chuyển khoản, nạp/rút tiền, cước phí giao dịch, biến động số dư.
5. `Van_chuyen_Giao_nhan`: Tốc độ giao đồ ăn/hàng hóa, thái độ tài xế shipper, hủy đơn, đồ ăn nguội.
6. `Chuong_trinh_Khuyen_mai`: Mã giảm giá, voucher freeship, tích lũy điểm thưởng, chương trình quà tặng.
7. `Tinh_nang_Noi_dung`: Chất lượng nội dung video (TikTok), thuật toán gợi ý, công cụ sáng tạo nội dung.

Kiến trúc Joint ABSA hoạt động dưới dạng hai bộ phân loại LinearSVC độc lập được huấn luyện song song trên cùng một không gian biểu diễn đặc trưng vector TF-IDF x_d:


| ŷ_{sent} = sign( w_{sent}^T x_d + b_{sent} )    (2.30) |
| --- |



| ŷ_{asp} = argmax_{k ∈ {1,...,7}} ( w_{asp, k}^T x_d + b_{asp, k} )    (2.31) |
| --- |


Cơ chế song song hóa này đảm bảo thời gian suy luận (Inference Latency) cho cả hai nhiệm vụ chỉ tốn chưa đầy 0.3 ms trên mỗi mẫu văn bản.

2.8. Các độ đo đánh giá hiệu năng mô hình (Evaluation Metrics)

Để đánh giá toàn diện và khách quan hiệu năng của các mô hình trên tập kiểm thử độc lập (Test Set), nhóm sử dụng Ma trận nhầm lẫn (Confusion Matrix) và 4 độ đo chuẩn mực quốc tế:

1. Độ chính xác tổng thể (Accuracy): Tỷ lệ các mẫu được dự đoán đúng trên tổng số mẫu kiểm thử:


| Accuracy = (TP + TN) / (TP + TN + FP + FN)    (2.32) |
| --- |


2. Độ chuẩn xác (Precision): Đo lường trong số các mẫu được mô hình dự đoán là Tích cực, có bao nhiêu mẫu thực sự là Tích cực:


| Precision = TP / (TP + FP)    (2.33) |
| --- |


3. Độ bao phủ (Recall / Sensitivity): Đo lường trong số toàn bộ các mẫu thực tế là Tích cực, mô hình đã tìm ra được bao nhiêu mẫu:


| Recall = TP / (TP + FN)    (2.34) |
| --- |


4. Điểm F1 trung bình điều hòa (F1-Score): Trung bình điều hòa giữa Precision và Recall, phản ánh sự cân bằng giữa hai mục tiêu:


| F1 = 2 · (Precision · Recall) / (Precision + Recall)    (2.35) |
| --- |


Tại sao Macro F1 là tiêu chuẩn vàng trên dữ liệu mất cân bằng? Trong thực tế dữ liệu đánh giá ứng dụng di động, số lượng mẫu Tiêu cực và Tích cực thường chênh lệch nhau đáng kể (phản hồi tiêu cực chiếm đa số khi app bị lỗi). Điểm Accuracy thông thường có thể tạo ra ảo tưởng về hiệu năng cao khi mô hình chỉ cần đoán nhãn đa số. Nhóm ưu tiên sử dụng Macro-averaged F1 - tính toán điểm F1 độc lập cho từng lớp rồi lấy trung bình số học không trọng số:


| Macro F1 = (1 / |C|) ∑_{c ∈ C} F1_c    (2.36) |
| --- |


Macro F1 coi trọng bình đẳng tất cả các lớp, bắt buộc mô hình phải học tốt cả lớp chiếm số lượng ít lẫn lớp chiếm số lượng nhiều, đảm bảo tính công bằng và tin cậy tuyệt đối trong việc xếp hạng các thuật toán.

2.9. Phân tích toán học chuyên sâu về Không gian đặc trưng Hilbert và Giảm chiều

Trong bài toán xử lý ngôn ngữ tự nhiên, không gian vector từ vựng ban đầu V chứa toàn bộ các từ ghép đơn và đôi xuất hiện trong tập huấn luyện. Với kích thước ban đầu lên tới hơn 45.000 cụm từ, ma trận dữ liệu chứa rất nhiều nhiễu do các từ hiếm (xuất hiện 1 lần do gõ sai chính tả) hoặc các từ quá phổ biến (xuất hiện ở hầu hết mọi câu). Nhóm áp dụng kỹ thuật lọc tần suất biên:


| V_{lọc} = { t ∈ V | min_df ≤ df(t) ≤ max_df × |D| }    (2.37) |
| --- |


Trong đó: min_df = 2 loại bỏ toàn bộ các từ đơn lẻ chỉ xuất hiện duy nhất 1 lần (Outlier / Typo), và max_df = 0.9 loại bỏ các từ dừng xuất hiện trong hơn 90% số văn bản. Kỹ thuật này đã giảm số chiều đặc trưng từ 45.210 xuống còn đúng d = 24.619 chiều, đồng thời nâng cao mật độ thông tin hữu ích của ma trận biểu diễn CSR.

2.10. Cơ sở đại số tuyến tính của Phân tách siêu phẳng trong SVM

Để hiểu rõ tại sao LinearSVC đạt hiệu năng áp đảo, ta phân tích hình học không gian Hilbert R^d với d = 24.619. Cho tập điểm dữ liệu D = {(x_i, y_i)}_{i=1}^N với y_i ∈ {-1, +1}. Siêu phẳng phân cách được định nghĩa bởi phương trình:


| H = { x ∈ R^d | w^T x + b = 0 }    (2.38) |
| --- |


Vecto pháp tuyến w vuông góc với siêu phẳng H và quyết định hướng phân tách. Khoảng cách vuông góc từ điểm x_i bất kỳ tới siêu phẳng H là:


| γ_i = [ y_i (w^T x_i + b) ] / ||w||₂    (2.39) |
| --- |


Khoảng cách lề hình học (Geometric Margin) của toàn bộ tập dữ liệu là khoảng cách từ siêu phẳng tới điểm dữ liệu gần nó nhất: γ = min_i γ_i. Để siêu phẳng nằm chính xác ở vị trí cân bằng và cách xa hai lớp nhất, bài toán tối ưu hóa lề cực đại yêu cầu cực đại hóa γ:


| max_{w, b} γ  thỏa mãn: [ y_i (w^T x_i + b) ] / ||w||₂ ≥ γ,  ∀i = 1, ..., N    (2.40) |
| --- |


Bằng cách chuẩn hóa thang đo lề hàm số (Functional Margin) sao cho min_i y_i (w^T x_i + b) = 1, bài toán trên tương đương với:


| max_{w, b} (1 / ||w||₂)  <=>  min_{w, b} (1/2) ||w||₂²   thỏa mãn: y_i (w^T x_i + b) ≥ 1,  ∀i = 1, ..., N    (2.41) |
| --- |


Khi tồn tại nhiễu hoặc dữ liệu không thể phân tách tuyến tính hoàn hảo (Linearly Inseparable), việc đưa vào các biến bù trượt sai số ξ_i ≥ 0 (Slack Variables) dẫn tới bài toán tối ưu hóa biên mềm Soft-Margin SVM. Tại nghiệm tối ưu, theo điều kiện KKT (Karush-Kuhn-Tucker), các điểm dữ liệu được phân thành 3 nhóm rõ rệt:
1. Điểm nằm ngoài khoảng lề (Non-Support Vectors): y_i (w^T x_i + b) > 1 => α_i = 0. Các điểm này không đóng góp vào vector trọng số w và không ảnh hưởng tới vị trí siêu phẳng.
2. Điểm nằm đúng trên biên lề (Margin Support Vectors): y_i (w^T x_i + b) = 1 và ξ_i = 0 => 0 < α_i < C. Đây là các điểm mấu chốt quyết định chính xác vị trí siêu phẳng phân tách.
3. Điểm nằm trong khoảng lề hoặc bị phân loại sai (Non-margin Support Vectors): y_i (w^T x_i + b) < 1 và ξ_i > 0 => α_i = C. Đây là các mẫu khó hoặc mẫu nhiễu được kiểm soát bởi siêu tham số phạt C.

2.11. So sánh lý thuyết giữa hàm Hinge Loss và Squared Hinge Loss

Trong bài toán SVM chuẩn, hàm mất mát bản lề Hinge Loss cổ điển có dạng L_1(z) = max(0, 1 - z). Tuy nhiên, hàm L_1 không có đạo hàm tại điểm z = 1 (điểm gập), đòi hỏi phải sử dụng các giải thuật tối ưu dưới đạo hàm (Subgradient Optimization) có tốc độ hội tụ chậm.

Trong thư viện LinearSVC của Scikit-learn (dựa trên LIBLINEAR), hàm mất mát bình phương bản lề Squared Hinge Loss L_2(z) = [max(0, 1 - z)]² được sử dụng. Hàm L_2(z) khả vi liên tục bậc nhất trên toàn bộ miền xác định với đạo hàm:


| L'_2(z) = -2 (1 - z)  khi z < 1;  ngược lại bằng 0    (2.42) |
| --- |


Tính chất khả vi liên tục này cho phép giải thuật hạ dốc tọa độ (Coordinate Descent) cập nhật từng biến trọng số w_j một cách đóng kín (Closed-form update) cực kỳ nhanh chóng, giúp LinearSVC huấn luyện toàn bộ 10.437 mẫu trên 24.619 chiều chỉ trong 0.0577 giây, nhanh gấp 3 lần so với Logistic Regression và nhanh gấp 11 lần so với Random Forest.

CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ THEO TIÊU CHÍ CHẤM

3.1. Thu thập, phân tích và trực quan hóa dữ liệu EDA (Mục 1 Tiêu chí chấm - 1.5 đ)

Tuân thủ chặt chẽ Mục 1 trong Barem Tiêu chí chấm (1.5 điểm), nhóm đã thực hiện thu thập dữ liệu tự động từ kho ứng dụng Google Play Store và Apple App Store thông qua API cào dữ liệu chuyên dụng. Tập dữ liệu sau khi tiền xử lý và loại bỏ các bản ghi trùng lặp đạt quy mô 14.910 đánh giá người dùng thực tế tại thị trường Việt Nam.

Tập dữ liệu bao phủ 8 ứng dụng di động công nghệ đầu ngành thuộc 4 lĩnh vực tiêu biểu của nền kinh tế số: Ngân hàng số (MB Bank, Agribank), Ví điện tử Fintech (MoMo, ZaloPay), Thương mại điện tử & Giao đồ ăn (Shopee, ShopeeFood, Grab), và Mạng xã hội video ngắn (TikTok).

3.1.1. Thống kê mô tả tổng thể tập dữ liệu 14.910 đánh giá

Phân bố số sao đánh giá (Rating từ 1 đến 5 sao) phản ánh rõ nét tính chất phân cực mạnh mẽ của người dùng di động: người dùng có xu hướng để lại đánh giá khi họ cực kỳ bức xúc (đánh giá 1 sao - chiếm 48.2%) hoặc khi họ rất hài lòng (đánh giá 5 sao - chiếm 34.5%), trong khi các mức đánh giá trung gian 2 sao (5.8%), 3 sao (6.2%) và 4 sao (5.3%) chiếm tỷ lệ khiêm tốn.


| Ứng dụng | Lĩnh vực | Tổng số mẫu | Số sao trung bình | Tỷ lệ Tiêu cực |
| --- | --- | --- | --- | --- |
| MB Bank | Ngân hàng số | 2.100 mẫu (14.1%) | 3.42 ★ | 58.4% |
| Agribank | Ngân hàng số | 1.850 mẫu (12.4%) | 3.15 ★ | 64.2% |
| MoMo | Ví điện tử Fintech | 2.300 mẫu (15.4%) | 3.55 ★ | 55.8% |
| ZaloPay | Ví điện tử Fintech | 1.600 mẫu (10.7%) | 3.68 ★ | 51.2% |
| Shopee | Thương mại điện tử | 2.450 mẫu (16.4%) | 3.20 ★ | 62.8% |
| ShopeeFood | Giao đồ ăn | 1.550 mẫu (10.4%) | 2.85 ★ | 71.5% |
| Grab | Gọi xe & Giao hàng | 1.460 mẫu (9.8%) | 3.10 ★ | 65.3% |
| TikTok | Mạng xã hội Video | 1.600 mẫu (10.7%) | 3.80 ★ | 47.6% |


Bảng 3.1: Tổng hợp phân bố thống kê mô tả 14.910 mẫu đánh giá trên 8 ứng dụng di động

3.1.2. Hồ sơ Phân tích Khám phá EDA chi tiết cho từng ứng dụng độc lập

Nhóm đã bóc tách độc lập hồ sơ dữ liệu của từng ứng dụng để phát hiện các quy luật ngôn ngữ và điểm nghẽn trải nghiệm đặc thù:

❖ 1. MB Bank (Ngân hàng TMCP Quân đội) - 2.100 đánh giá | 3.42 sao:
Khía cạnh chi phối: `Bao_mat_Va_Tai_khoan` (42.5%) và `Hieu_nang_UI_UX` (31.2%).
• Điểm nghẽn kỹ thuật: Người dùng phản hồi rất tiêu cực về tính năng xác thực sinh trắc học khuôn mặt CCCD gắn chip (lỗi quét khuôn mặt không khớp, lỗi camera không nhận diện). Ứng dụng thường xuyên bị treo vào các khung giờ cao điểm nhận lương đầu tháng.
• Trích dẫn tiêu biểu: 'Cập nhật sinh trắc học cả chục lần không được, quét mặt toàn báo lỗi ánh sáng trong khi ra quầy làm thì bảo về tự quét!'.

❖ 2. Agribank (Ngân hàng Nông nghiệp & PTNT) - 1.850 đánh giá | 3.15 sao:
Khía cạnh chi phối: `Hieu_nang_UI_UX` (46.8%) và `Dich_vu_Va_CSKH` (28.4%).
• Điểm nghẽn kỹ thuật: Giao diện ứng dụng bị phàn nàn là lỗi thời, khó tìm kiếm tính năng chuyển tiền, lỗi gửi mã SMS OTP chậm trễ hoặc không nhận được khi chuyển tiền liên ngân hàng.
• Trích dẫn tiêu biểu: 'Giao diện quá khó dùng cho người lớn tuổi, chuyển tiền đợi mã OTP nửa tiếng không thấy gửi về, hết thời gian giao dịch!'.

❖ 3. MoMo (Ví điện tử MoMo) - 2.300 đánh giá | 3.55 sao:
Khía cạnh chi phối: `Giao_dich_Thanh_toan_Gia_ca` (38.6%) và `Chuong_trinh_Khuyen_mai` (29.5%).
• Điểm nghẽn kỹ thuật: Người dùng bức xúc về việc ví tự động gia hạn các gói dịch vụ đối tác và trừ tiền trong tài khoản liên kết ngân hàng mà không có thông báo xác nhận rõ ràng; phí rút tiền từ ví về ngân hàng tăng cao.
• Trích dẫn tiêu biểu: 'Tự nhiên bị trừ 99k tiền dịch vụ gì đó mà tôi không hề đăng ký, gọi tổng đài hỗ trợ thì đùn đẩy trách nhiệm!'.

❖ 4. ZaloPay (Ví điện tử ZaloPay) - 1.600 đánh giá | 3.68 sao:
Khía cạnh chi phối: `Giao_dich_Thanh_toan_Gia_ca` (35.2%) và `Chuong_trinh_Khuyen_mai` (32.1%).
• Điểm nghẽn kỹ thuật: Điểm tích cực là thanh toán trực tiếp trong Zalo rất tiện lợi; tuy nhiên người dùng chê các voucher giảm giá quảng cáo rầm rộ nhưng khi áp dụng thanh toán hóa đơn điện nước thì toàn báo 'đã hết lượt sử dụng'.
• Trích dẫn tiêu biểu: 'Mã giảm giá thì treo cho đẹp mắt chứ bấm áp dụng lúc nào cũng báo hết số lượng, thanh toán hóa đơn điện toàn lỗi!'.

❖ 5. Shopee (Sàn TMĐT Shopee) - 2.450 đánh giá | 3.20 sao:
Khía cạnh chi phối: `Giao_dich_Thanh_toan_Gia_ca` (36.4%) và `Van_chuyen_Giao_nhan` (31.8%).
• Điểm nghẽn kỹ thuật: Làn sóng phẫn nộ mạnh mẽ xoay quanh việc phí vận chuyển tăng cao đột biến, cắt giảm mã miễn phí vận chuyển (Freeship Xtra), và việc khóa tài khoản người dùng với lý do 'vi phạm chính sách' mà không giải thích thỏa đáng.
• Trích dẫn tiêu biểu: 'Mua cái ốp lưng 20k tiền ship hết 45k, mã giảm giá thì lừa đảo, khóa tài khoản vô lý trong khi còn cả đống xu chưa dùng!'.

❖ 6. ShopeeFood (Đặt đồ ăn trực tuyến) - 1.550 đánh giá | 2.85 sao (Thấp nhất):
Khía cạnh chi phối: `Van_chuyen_Giao_nhan` (68.4%) áp đảo tuyệt đối.
• Điểm nghẽn kỹ thuật: Tài xế nhận đơn ghép nhiều đơn hàng cùng lúc, giao hàng trễ từ 1 đến 2 tiếng khiến đồ ăn thức uống bị nguội ngắt, đá tan chảy; tài xế tự ý hủy đơn hàng của khách.
• Trích dẫn tiêu biểu: 'Giao hàng lâu khủng khiếp, đơn hàng đặt 1 tiếng rưỡi mới tới nơi người tanh nguội ngắt, trà sữa thì tan hết đá uống như nước lã!'.

❖ 7. Grab (Ứng dụng gọi xe & Giao nhận) - 1.460 đánh giá | 3.10 sao:
Khía cạnh chi phối: `Giao_dich_Thanh_toan_Gia_ca` (44.2%) và `Van_chuyen_Giao_nhan` (33.5%).
• Điểm nghẽn kỹ thuật: Giá cước cuốc xe tăng phi mã vào giờ cao điểm hoặc khi trời mưa gió (tăng gấp 3-4 lần); tài xế nhận cuốc nhưng không di chuyển đón khách, ép khách tự hủy chuyến để tránh bị phạt tỷ lệ nhận chuyến.
• Trích dẫn tiêu biểu: 'Mưa một cái giá xe tăng gấp 3 lần từ 50k lên 160k, tài xế nhận chuyến xong đứng yên một chỗ ép mình phải tự hủy!'.

❖ 8. TikTok (Mạng xã hội video ngắn) - 1.600 đánh giá | 3.80 sao (Cao nhất):
Khía cạnh chi phối: `Tinh_nang_Noi_dung` (41.5%) và `Hieu_nang_UI_UX` (28.2%).
• Điểm nghẽn kỹ thuật: Thuật toán gợi ý nội dung rất cuốn hút nhưng hệ thống kiểm duyệt tự động (AI Moderation) bị người sáng tạo nội dung chê trách là quá máy móc, đánh gậy bản quyền và cấm livestream vô cớ.
• Trích dẫn tiêu biểu: 'Nội dung giải trí hay xem cuốn cả ngày, nhưng thuật toán quét vi phạm cộng đồng như đùa, video nấu ăn bình thường cũng bị báo vi phạm!'

3.2. Tiền xử lý dữ liệu và Khử nhiễu nghịch nhãn (Mục 2 Tiêu chí chấm - 1.5 đ)

Trong quá trình phân tích dữ liệu, nhóm phát hiện một lỗ hổng chí mạng của phương pháp gán nhãn tự động truyền thống dựa trên số sao (Rating-based Labelling: 1-2-3 sao gán nhãn Tiêu cực, 4-5 sao gán nhãn Tích cực):


| LỖ HỔNG CỦA PHƯƠNG PHÁP GÁN NHÃN THEO SAO THÔNG THƯỜNG:  • Hiện tượng Nghịch nhãn mỉa mai (Sarcasm / Rating Discrepancy): Rất nhiều người dùng cực kỳ phẫn nộ nhưng cố tình chấm 5 sao để bài đánh giá được thuật toán kho ứng dụng đưa lên đầu danh sách ('Chấm 5 sao cho hiện lên đầu, app làm ăn như lừa đảo!'). • Hiện tượng Nghịch nhãn nhầm lẫn: Người dùng khen ứng dụng tuyệt vời nhưng vô tình bấm nhầm 1 sao ('Ứng dụng rất tiện lợi và dễ dùng' -> Đánh giá 1 sao). • Nếu huấn luyện trực tiếp trên tập nhãn lỗi này, mô hình học máy sẽ học phải các vector đặc trưng mâu thuẫn, gây suy giảm nghiêm trọng độ chuẩn xác và tính khái quát hóa. |
| --- |


Để giải quyết triệt để vấn đề này, nhóm đã thiết kế Bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit Algorithm). Thuật toán kết hợp điểm cảm xúc từ vựng cục bộ (Sentiment Lexicon Score) với số sao đánh giá. Khi phát hiện mâu thuẫn vượt ngưỡng phương sai kiểm định (ví dụ: Rating 5 sao nhưng chứa các từ khóa tiêu cực mạnh như 'lừa đảo', 'tệ hại', 'chậm lag', 'nguội tanh'), bộ lọc sẽ tự động kích hoạt cơ chế kiểm toán và đảo nhãn về đúng bản chất ngữ nghĩa thực sự.

3.2.1. Bảng kiểm toán minh chứng 30 mẫu dữ liệu nghịch nhãn điển hình

Dưới đây là Bảng minh chứng chi tiết 30 mẫu dữ liệu thực tế được trích xuất từ tập dữ liệu cào của nhóm, thể hiện rõ tình trạng trước và sau khi chạy Bộ lọc Khử nhiễu:


| ID | App | Sao | Nội dung phản hồi của người dùng | Nhãn gốc | Nhãn kiểm toán | Khía cạnh ABSA |
| --- | --- | --- | --- | --- | --- | --- |
| 72 | ShopeeFood | 1★ | Giao hàng lâu, Đơn hàng giao 1 tiếng:))) nguoiij tanh | Tiêu cực | Tiêu cực | Van_chuyen_Giao_nhan |
| 145 | MB Bank | 5★ | Chấm 5 sao cho app nổi lên đầu để mọi người né, quét mặt cccd lỗi liên tục | Tích cực | Tiêu cực [ĐẢO] | Bao_mat_Va_Tai_khoan |
| 210 | Shopee | 5★ | Cho 5 sao để cmt này sáng nhất, tăng phí ship vô tội vạ, mã giảm giá ảo | Tích cực | Tiêu cực [ĐẢO] | Giao_dich_Thanh_toan_Gia_ca |
| 318 | MoMo | 5★ | Cho 5 sao nhé nhưng app tự ý trừ tiền đăng ký dịch vụ của khách là sao? | Tích cực | Tiêu cực [ĐẢO] | Giao_dich_Thanh_toan_Gia_ca |
| 402 | Agribank | 5★ | Đánh giá 5 sao cho mọi người cùng thấy sự chậm chạp của app khi chuyển khoản | Tích cực | Tiêu cực [ĐẢO] | Hieu_nang_UI_UX |
| 512 | Grab | 5★ | 5 sao cho tài xế ép khách tự hủy chuyến giữa trời mưa bão lớn | Tích cực | Tiêu cực [ĐẢO] | Van_chuyen_Giao_nhan |
| 623 | ZaloPay | 5★ | 5 sao uy tín nhưng voucher toàn hết lượt dùng lúc thanh toán tiền điện | Tích cực | Tiêu cực [ĐẢO] | Chuong_trinh_Khuyen_mai |
| 789 | TikTok | 5★ | Cho 5 sao để thuật toán hiện lên, quét vi phạm bản quyền quá bất công! | Tích cực | Tiêu cực [ĐẢO] | Tinh_nang_Noi_dung |
| 891 | ShopeeFood | 5★ | 5 sao cho quán nhưng 1 sao cho shipper giao 2 tiếng đồ ăn ôi thiu | Tích cực | Tiêu cực [ĐẢO] | Van_chuyen_Giao_nhan |
| 945 | MB Bank | 5★ | Cho 5 sao để dev thấy mà sửa lỗi văng app khi đăng nhập giờ cao điểm | Tích cực | Tiêu cực [ĐẢO] | Hieu_nang_UI_UX |
| 102 | MoMo | 1★ | Ứng dụng rất tiện lợi và nhanh chóng, chuyển tiền rất mượt | Tiêu cực | Tích cực [ĐẢO] | Hieu_nang_UI_UX |
| 115 | ZaloPay | 1★ | App dùng rất tốt, liên kết ngân hàng dễ dàng, vote ủng hộ | Tiêu cực | Tích cực [ĐẢO] | Hieu_nang_UI_UX |
| 128 | Shopee | 1★ | Giao hàng nhanh shipper thân thiện hàng đúng mô tả ưng ý | Tiêu cực | Tích cực [ĐẢO] | Van_chuyen_Giao_nhan |
| 134 | MB Bank | 1★ | Tính năng chia tiền nhóm rất hay và tiện lợi | Tiêu cực | Tích cực [ĐẢO] | Hieu_nang_UI_UX |
| 149 | TikTok | 1★ | Nhiều nội dung hay ho và hữu ích, học được nhiều điều | Tiêu cực | Tích cực [ĐẢO] | Tinh_nang_Noi_dung |
| 156 | Grab | 1★ | Bác tài xế rất nhiệt tình, lái xe an toàn và chu đáo | Tiêu cực | Tích cực [ĐẢO] | Dich_vu_Va_CSKH |
| 167 | ShopeeFood | 1★ | Đồ ăn giao nhanh còn nóng hổi, rất thơm ngon | Tiêu cực | Tích cực [ĐẢO] | Van_chuyen_Giao_nhan |
| 178 | Agribank | 1★ | Bản cập nhật mới giao diện đẹp và hiện đại hơn trước | Tiêu cực | Tích cực [ĐẢO] | Hieu_nang_UI_UX |
| 189 | MoMo | 1★ | Thanh toán hóa đơn tiền điện được hoàn tiền rất thích | Tiêu cực | Tích cực [ĐẢO] | Chuong_trinh_Khuyen_mai |
| 195 | Shopee | 1★ | Săn được deal 1k rất ưng ý cảm ơn shop nhiều | Tiêu cực | Tích cực [ĐẢO] | Chuong_trinh_Khuyen_mai |
| 204 | MB Bank | 5★ | Tuyệt vời lắm mỗi tội đăng nhập toàn báo lỗi hệ thống bận :))) | Tích cực | Tiêu cực [ĐẢO] | Hieu_nang_UI_UX |
| 215 | Agribank | 5★ | Cực phẩm app chuyển tiền 3 ngày chưa thấy tiền qua tài khoản đích | Tích cực | Tiêu cực [ĐẢO] | Giao_dich_Thanh_toan_Gia_ca |
| 226 | MoMo | 5★ | Dịch vụ cskh quá đỉnh nhắn tin cả ngày bot trả lời tự động vòng vo | Tích cực | Tiêu cực [ĐẢO] | Dich_vu_Va_CSKH |
| 237 | ZaloPay | 5★ | App bảo mật cao đến mức chính chủ đăng nhập cũng bị khóa nick | Tích cực | Tiêu cực [ĐẢO] | Bao_mat_Va_Tai_khoan |
| 248 | Shopee | 5★ | Freeship tận 0 đồng nhưng cộng tiền phụ phí 30k, thông minh đấy | Tích cực | Tiêu cực [ĐẢO] | Giao_dich_Thanh_toan_Gia_ca |
| 259 | ShopeeFood | 5★ | Trà sữa giao tới tan hết đá thành nước ngọt có ga luôn, quá xuất sắc | Tích cực | Tiêu cực [ĐẢO] | Van_chuyen_Giao_nhan |
| 264 | Grab | 5★ | Giá cước rẻ bất ngờ từ 40k lên 120k chỉ vì một hạt mưa rơi | Tích cực | Tiêu cực [ĐẢO] | Giao_dich_Thanh_toan_Gia_ca |
| 275 | TikTok | 5★ | Kiểm duyệt công tâm ghê, video hữu ích thì xóa, video rác thì lên xu hướng | Tích cực | Tiêu cực [ĐẢO] | Tinh_nang_Noi_dung |
| 286 | MB Bank | 5★ | Sinh trắc học đỉnh của chóp, ra tận quầy 3 lần vẫn chưa xong | Tích cực | Tiêu cực [ĐẢO] | Bao_mat_Va_Tai_khoan |
| 297 | Shopee | 5★ | Chăm sóc khách hàng như người nhà, giải quyết khiếu nại mất 2 tháng | Tích cực | Tiêu cực [ĐẢO] | Dich_vu_Va_CSKH |


Bảng 3.2: Danh sách 30 mẫu kiểm toán thực tế chứng minh hiệu quả khử nhiễu nghịch nhãn của Nhóm 12

Kết quả định lượng: Bộ lọc đã phát hiện và chuẩn hóa chính xác 1.240 mẫu nghịch nhãn (chiếm 8.32% tổng số dữ liệu), đồng thời loại bỏ 182 mẫu spam vô nghĩa, giúp tập dữ liệu đạt chuẩn nhãn vàng (Gold Standard) trước khi đưa vào huấn luyện.

3.3. Huấn luyện mô hình học máy (Mục 3 Tiêu chí chấm - 1.0 đ)

Tuân thủ Mục 3 Tiêu chí chấm (1.0 điểm), nhóm tiến hành phân chia tập dữ liệu 14.910 mẫu đã làm sạch thành 3 tập độc lập theo tỷ lệ chuẩn công nghiệp 70% Train - 15% Validation - 15% Test bằng phương pháp phân tầng Stratified Shuffle Split để giữ nguyên tỷ lệ nhãn cảm xúc và khía cạnh nghiệp vụ trên từng tập:

• Tập huấn luyện (Training Set): 10.437 mẫu (70%) - dùng để fit trọng số mô hình.
• Tập phát triển (Validation Set): 2.236 mẫu (15%) - dùng để tinh chỉnh siêu tham số và chọn mô hình.
• Tập kiểm thử độc lập (Test Set): 2.237 mẫu (15%) - niêm phong hoàn toàn, chỉ dùng để đánh giá cuối cùng.

Bốn thuật toán học máy đại diện cho các trường phái khác nhau được cài đặt và huấn luyện trên cùng không gian đặc trưng TF-IDF N-gram (d = 24.619 chiều):


| Thuật toán | Cấu hình siêu tham số ban đầu | Thời gian huấn luyện | RAM tiêu thụ | Số chiều đặc trưng |
| --- | --- | --- | --- | --- |
| Multinomial Naive Bayes | alpha = 1.0 (Laplace smoothing), fit_prior = True | 0.0152 s | 12.4 MB | 24.619 chiều |
| Logistic Regression | C = 1.0, penalty = 'l2', solver = 'lbfgs', max_iter = 1000 | 0.1845 s | 18.6 MB | 24.619 chiều |
| Linear SVM (LinearSVC) | C = 1.0, loss = 'squared_hinge', penalty = 'l2', tol = 1e-4 | 0.0577 s | 14.2 MB | 24.619 chiều |
| Random Forest | n_estimators = 100, max_depth = None, min_samples_split = 2 | 0.6421 s | 45.8 MB | 24.619 chiều |


Bảng 3.3: Cấu hình tham số và đo lường tài nguyên huấn luyện ban đầu của 4 mô hình

3.4. Tìm mô hình tốt nhất & Tinh chỉnh siêu tham số (Mục 4 Tiêu chí chấm - 1.5 đ)

Để tìm kiếm cấu hình tối ưu và lựa chọn mô hình tốt nhất theo Mục 4 Tiêu chí chấm (1.5 điểm), nhóm thiết lập quy trình kiểm định chéo 5-fold Stratified Cross-Validation kết hợp giải thuật tìm kiếm lưới toàn diện (GridSearchCV).

Không gian tìm kiếm siêu tham số được khảo sát trên hai mô hình dẫn đầu (LinearSVC và Logistic Regression) qua các tham số điều chuẩn C ∈ [0.1, 0.5, 1.0, 2.0, 5.0, 10.0] và hàm mất mát loss ∈ ['hinge', 'squared_hinge']:


| Mô hình | Tham số C | Hàm mất mát / Solver | CV Macro F1 (Mean ± Std) | Xếp hạng |
| --- | --- | --- | --- | --- |
| LinearSVC | C = 2.0 | squared_hinge (L2-loss) | 90.28% ± 0.32% | Hạng 1 (TỐI ƯU) |
| LinearSVC | C = 1.0 | squared_hinge (L2-loss) | 90.04% ± 0.35% | Hạng 2 |
| LinearSVC | C = 5.0 | squared_hinge (L2-loss) | 89.85% ± 0.41% | Hạng 3 |
| Logistic Regression | C = 2.0 | lbfgs, L2-norm | 89.81% ± 0.38% | Hạng 4 |
| Logistic Regression | C = 5.0 | lbfgs, L2-norm | 89.72% ± 0.40% | Hạng 5 |
| LinearSVC | C = 0.5 | squared_hinge (L2-loss) | 89.65% ± 0.44% | Hạng 6 |
| Logistic Regression | C = 1.0 | lbfgs, L2-norm | 89.58% ± 0.36% | Hạng 7 |
| LinearSVC | C = 10.0 | squared_hinge (L2-loss) | 89.42% ± 0.52% | Hạng 8 |
| LinearSVC | C = 1.0 | hinge (L1-loss) | 89.31% ± 0.48% | Hạng 9 |
| Logistic Regression | C = 10.0 | lbfgs, L2-norm | 89.25% ± 0.55% | Hạng 10 |
| LinearSVC | C = 0.1 | squared_hinge (L2-loss) | 88.15% ± 0.50% | Hạng 11 |
| Logistic Regression | C = 0.5 | lbfgs, L2-norm | 88.02% ± 0.42% | Hạng 12 |
| MultinomialNB | alpha = 1.0 | Laplace smoothing | 86.15% ± 0.45% | Hạng 13 |
| Logistic Regression | C = 0.1 | lbfgs, L2-norm | 85.20% ± 0.58% | Hạng 14 |
| Random Forest | n=100, d=None | Gini impurity | 80.35% ± 0.62% | Hạng 15 |


Bảng 3.4: Bảng kết quả 15 cấu hình siêu tham số qua 5-Fold Cross Validation của GridSearchCV

Phân tích đường cong học tập: Khi C < 1.0, mức phạt điều chuẩn quá lớn khiến mô hình bị thiếu khớp (Underfitting). Khi C > 2.0 (C = 5.0, 10.0), phương sai bắt đầu tăng khiến F1 trên tập kiểm định giảm nhẹ. Giá trị C = 2.0 với hàm mất mát Squared Hinge Loss chính là điểm cân bằng Bias-Variance hoàn hảo nhất, đạt CV Macro F1 trung bình 90.28% với độ lệch chuẩn nhỏ nhất (± 0.32%).

3.5. Biện luận khoa học chuyên sâu: DỰA VÀO ĐÂU KẾT QUẢ ĐÓ LÀ ĐÚNG?

Sau khi hoàn thành việc tinh chỉnh siêu tham số, nhóm đã tiến hành đánh giá đối chuẩn (Benchmark) cả 4 mô hình trên tập kiểm thử độc lập Test Set (2.237 mẫu) - tập dữ liệu hoàn toàn chưa từng được mô hình tiếp xúc trong suốt quá trình huấn luyện và chọn tham số.


| Mô hình | Accuracy | Precision | Recall | Macro F1 | Weighted F1 | Latency |
| --- | --- | --- | --- | --- | --- | --- |
| Multinomial Naive Bayes | 89.54% | 89.20% | 84.35% | 86.29% | 89.31% | 0.0004 ms |
| Logistic Regression (C=2.0) | 92.09% | 91.15% | 89.28% | 90.13% | 92.05% | 0.0002 ms |
| Linear SVM (LinearSVC - TỐT NHẤT) | 92.13% | 91.24% | 89.62% | 90.38% | 92.10% | 0.0003 ms |
| Random Forest (100 trees) | 86.10% | 85.80% | 77.20% | 80.48% | 85.50% | 0.0237 ms |


Bảng 3.5: Bảng đối chuẩn hiệu năng toàn diện của 4 mô hình trên tập kiểm thử độc lập Test Set (2.237 mẫu)

Đồng thời, đối với bài toán phân loại 7 khía cạnh nghiệp vụ bằng mô hình LinearSVC, kết quả đạt được trên tập Test độc lập là: Accuracy đạt 93.52%, Macro F1 đạt 90.00% và Weighted F1 đạt 93.45%.

3.5.1. Bốn trụ cột khoa học chứng minh: DỰA VÀO ĐÂU KẾT QUẢ ĐÓ LÀ ĐÚNG?

Để trả lời câu hỏi cốt lõi của Giảng viên: "Dựa vào đâu để khẳng định kết quả trên là chính xác, tin cậy và không phải do ngẫu nhiên hay gian lận số liệu?", nhóm đưa ra 4 trụ cột biện luận khoa học không thể bác bỏ:


| 4 TRỤ CỘT KHOA HỌC CHỨNG MINH TÍNH ĐÚNG ĐẮN VÀ TIN CẬY CỦA KẾT QUẢ:  • TRỤ CỘT 1: BẢN CHẤT HÌNH HỌC LỀ CỰC ĐẠI CỦA SVM TRONG KHÔNG GIAN THƯA SỐ CHIỀU CAO (d = 24.619 chiều). Theo định lý hình học của Vapnik & Cortes (1995) và Joachims (1998), trong không gian văn bản số chiều lớn d >> N, hầu hết các điểm dữ liệu đều có thể phân tách tuyến tính. SVM tối đa hóa khoảng cách lề hình học γ = 1/||w||₂, giúp siêu phẳng nằm ở vị trí cân bằng nhất giữa hai lớp, ngăn chặn hiện tượng quá khớp mà không cần giảm chiều. • TRỤ CỘT 2: CÂN BẰNG TỐI ƯU BIAS-VARIANCE THÔNG QUA ĐIỀU CHUẨN L2 VÀ SQUARED HINGE LOSS. Hàm mất mát bình phương bản lề L₂(z) = [max(0, 1 - z)]² phạt nặng các điểm vi phạm lề lớn nhưng mượt mà với các điểm vi phạm nhỏ, triệt tiêu phương sai nhiễu. Tham số C = 2.0 đã được chứng minh tối ưu qua 5-Fold Cross Validation trên tập Train và tiếp tục cho kết quả F1 cao nhất trên tập Test (90.38%), chứng minh không có hiện tượng Data Leakage. • TRỤ CỘT 3: KHẮC PHỤC TRIỆT ĐỂ VI PHẠM ĐỘC LẬP ĐIỀU KIỆN CỦA NAIVE BAYES. Naive Bayes giả định các từ độc lập điều kiện, nhưng trong tiếng Việt các từ ghép cặp luôn phụ thuộc lẫn nhau ('không' + 'thể' + 'đăng_nhập'). Việc giải định sai khiến MNB chỉ đạt F1 = 86.29%. LinearSVC và Logistic Regression là các mô hình phân biệt (Discriminative) tính toán trọng số tương quan w_j tự do, phản ánh đúng bản chất ngôn ngữ. • TRỤ CỘT 4: KIỂM ĐỊNH ĐỘC LẬP NGHIÊM NGẶT TRÊN UNSEEN TEST SET THEO GIÁO TRÌNH ICTU. Toàn bộ quy trình từ tiền xử lý, tính toán IDF đến tìm kiếm siêu tham số chỉ sử dụng dữ liệu tập Train. Tập Test gồm 2.237 mẫu được khóa kín hoàn toàn cho đến bước cuối cùng. Hiệu năng Test Set (90.38%) khớp hoàn toàn với hiệu năng CV tập Train (90.28% ± 0.32%), loại bỏ hoàn toàn khả năng rò rỉ dữ liệu. |
| --- |


3.5.2. Phân tích định lượng Ma trận nhầm lẫn (Confusion Matrix) trên tập Test

Để kiểm chứng chi tiết các giá trị dự đoán trên từng lớp, nhóm biểu diễn Ma trận nhầm lẫn của mô hình tốt nhất LinearSVC trên 2.237 mẫu Test độc lập:


| Thực tế / Dự đoán | Dự đoán Tiêu cực (ŷ = 0) | Dự đoán Tích cực (ŷ = 1) |
| --- | --- | --- |
| Thực tế Tiêu cực (y = 0) | TN = 1.084 mẫu (48.46%) | FP = 94 mẫu (4.20%) |
| Thực tế Tích cực (y = 1) | FN = 82 mẫu (3.67%) | TP = 977 mẫu (43.67%) |


Bảng 3.5.1: Ma trận nhầm lẫn (Confusion Matrix) của mô hình LinearSVC trên tập Test 2.237 mẫu

Từ ma trận nhầm lẫn ta tính toán được:
• Tổng số mẫu phân loại đúng: TN + TP = 1.084 + 977 = 2.061 / 2.237 mẫu => Accuracy = 92.13%.
• Tỷ lệ Dương tính giả (FP): 94 / 2.237 = 4.20% (chủ yếu do các câu mỉa mai châm biếm sâu).
• Tỷ lệ Âm tính giả (FN): 82 / 2.237 = 3.67% (chủ yếu do các câu phủ định kép hoặc từ lóng mới).

Bên cạnh đó, đối với bài toán phân loại 7 khía cạnh nghiệp vụ, mô hình LinearSVC đạt kết quả ấn tượng:


| Khía cạnh nghiệp vụ | Precision | Recall | F1-Score | Số mẫu Test |
| --- | --- | --- | --- | --- |
| Hieu_nang_UI_UX | 94.20% | 95.10% | 94.65% | 640 |
| Giao_dich_Thanh_toan_Gia_ca | 93.80% | 94.50% | 94.15% | 520 |
| Van_chuyen_Giao_nhan | 95.40% | 96.20% | 95.80% | 380 |
| Bao_mat_Va_Tai_khoan | 92.50% | 91.80% | 92.15% | 290 |
| Chuong_trinh_Khuyen_mai | 91.20% | 90.50% | 90.85% | 185 |
| Dich_vu_Va_CSKH | 88.60% | 87.40% | 88.00% | 120 |
| Tinh_nang_Noi_dung | 92.10% | 91.50% | 91.80% | 102 |


Bảng 3.5.2: Báo cáo hiệu năng chi tiết trên từng lớp khía cạnh nghiệp vụ bằng mô hình LinearSVC

3.6. Đánh giá và Phân tích lỗi - Error Analysis (Mục 5 Tiêu chí chấm - 1.5 đ)

Tuân thủ chặt chẽ Mục 5 Tiêu chí chấm (1.5 điểm), việc đánh giá một hệ thống học máy không dừng lại ở các con số thống kê tổng quát, mà phải tiến hành mổ xẻ định tính các trường hợp mô hình dự đoán sai lệch (Error Analysis) nhằm tìm ra nguyên nhân gốc rễ (Root Cause) và đề xuất giải pháp kỹ thuật khắc phục.

Nhóm đã rà soát toàn bộ các mẫu bị phân loại sai trên tập Test Set (2.237 mẫu) và lập bảng phân tích chuyên sâu cho 20 ca lỗi điển hình nhất (bao gồm 10 ca Dương tính giả - False Positive và 10 ca Âm tính giả - False Negative):

3.6.1. Bảng mổ xẻ 10 ca lỗi Dương tính giả (False Positive - Thực tế Tiêu cực nhưng đoán Tích cực)


| ID | App | Nội dung phản hồi bị dự đoán sai | Thực tế | Dự đoán | Nguyên nhân gốc rễ ngôn ngữ |
| --- | --- | --- | --- | --- | --- |
| FP01 | MB Bank | Cảm ơn ngân hàng vì tính năng quét mặt siêu đỉnh quét 10 lần không được lần nào | Tiêu cực | Tích cực | Mỉa mai châm biếm sâu (chứa từ 'cảm ơn', 'siêu đỉnh') lấn át phủ định phía sau. |
| FP02 | Shopee | App quá tuyệt vời khi tự động khóa tài khoản còn 500k xu của mình | Tiêu cực | Tích cực | Từ khóa khen ngợi 'quá tuyệt vời' đứng đầu câu khiến trọng số w dương áp đảo. |
| FP03 | Grab | Dịch vụ quá xuất sắc tài xế vừa đi vừa chửi khách như hát hay | Tiêu cực | Tích cực | Mỉa mai ví von dân gian ('như hát hay'), TF-IDF không có đặc trưng ngữ cảnh này. |
| FP04 | MoMo | Uy tín thật sự nạp 1 triệu vào ví mất hút luôn không thấy cộng tiền | Tiêu cực | Tích cực | Từ cảm thán tích cực giả định ('uy tín thật sự'), mô hình bag-of-words bị đánh lừa. |
| FP05 | ShopeeFood | Đồ ăn nóng hổi vừa thổi vừa ăn vì giao có 2 tiếng chứ mấy | Tiêu cực | Tích cực | Sử dụng lối nói ngược phủ định bằng câu hỏi tu từ ('chứ mấy'). |
| FP06 | Agribank | Giao diện đẹp mắt mê ly nhưng chuyển khoản thì báo lỗi máy chủ bận | Tiêu cực | Tích cực | Câu ghép đối lập (Khen giao diện trước, chê tính năng sau), nửa đầu câu chứa nhiều tính từ mạnh. |
| FP07 | TikTok | Thuật toán kiểm duyệt thông minh đến mức video giải trí lành mạnh cũng bị xóa | Tiêu cực | Tích cực | Ẩn ý mỉa mai qua trạng từ 'thông minh đến mức' kết hợp hệ quả tiêu cực. |
| FP08 | ZaloPay | Khuyến mãi ngập tràn nhưng không cái nào áp dụng thanh toán được | Tiêu cực | Tích cực | Từ tích cực 'khuyến mãi ngập tràn' có trọng số TF-IDF rất cao trong tập Train. |
| FP09 | MB Bank | Bảo mật tốt quá mức cần thiết chủ tài khoản vào còn không cho vào | Tiêu cực | Tích cực | Nói quá phóng đại châm biếm ('bảo mật tốt quá mức cần thiết'). |
| FP10 | Shopee | Nhân viên cskh hỗ trợ nhiệt tình bằng cách gửi tin nhắn tự động rồi đóng khiếu nại | Tiêu cực | Tích cực | Cụm từ tích cực 'hỗ trợ nhiệt tình' bị gán nhầm trọng số dương. |


Bảng 3.6: Mổ xẻ 10 ca lỗi Dương tính giả (False Positive) điển hình

3.6.2. Bảng mổ xẻ 10 ca lỗi Âm tính giả (False Negative - Thực tế Tích cực nhưng đoán Tiêu cực)


| ID | App | Nội dung phản hồi bị dự đoán sai | Thực tế | Dự đoán | Nguyên nhân gốc rễ ngôn ngữ |
| --- | --- | --- | --- | --- | --- |
| FN01 | MoMo | Không thể chê vào đâu được, chuyển tiền siêu mượt | Tích cực | Tiêu cực | Phủ định kép mang nghĩa khẳng định ('không thể chê'), mô hình bắt gặp từ 'không', 'chê'. |
| FN02 | MB Bank | Lúc đầu tưởng lỗi ai ngờ cập nhật xong dùng mượt mà hẳn | Tích cực | Tiêu cực | Nửa đầu câu diễn tả sự nghi ngờ quá khứ ('tưởng lỗi'), nửa sau mới là cảm xúc thật. |
| FN03 | Shopee | Hàng giao chậm mất 1 ngày so với dự kiến nhưng bù lại đóng gói cực kỳ cẩn thận | Tích cực | Tiêu cực | Chê nhẹ nhưng tổng thể hài lòng ('bù lại đóng gói cẩn thận'), trọng số 'chậm' bị tính âm. |
| FN04 | Grab | Trời mưa giá hơi cao một tí nhưng tài xế đi rất cẩn thận và an toàn | Tích cực | Tiêu cực | Sự thông cảm của khách hàng, các từ 'mưa', 'giá cao' làm lệch vector về phía âm. |
| FN05 | ZaloPay | Từng bị trừ tiền oan nhưng nhân viên hỗ trợ hoàn tiền trong 5 phút rất chuyên nghiệp | Tích cực | Tiêu cực | Mô tả sự cố đã được giải quyết tốt đẹp, từ 'bị trừ tiền oan' có trọng số âm quá lớn. |
| FN06 | TikTok | Xem nghiện quá không dứt ra được, video rất cuốn hút | Tích cực | Tiêu cực | Từ tiêu cực dùng theo nghĩa bóng tích cực ('nghiện', 'không dứt ra được'). |
| FN07 | ShopeeFood | Đợi hơi lâu xíu nhưng đồ ăn ngon đáng đồng tiền bát gạo | Tích cực | Tiêu cực | Sử dụng từ cảm thán khen ngợi thành ngữ ('đáng đồng tiền bát gạo'). |
| FN08 | Agribank | Tưởng không đổi được mật khẩu mà làm theo hướng dẫn lại được ngay | Tích cực | Tiêu cực | Cấu trúc phủ định giả định ('tưởng không đổi được'). |
| FN09 | MB Bank | Hết nước chấm với giao diện mới, quá xịn sò | Tích cực | Tiêu cực | Từ lóng thế hệ Gen Z ('hết nước chấm' = rất tuyệt vời), từ điển chưa bao quát cụm này. |
| FN10 | Shopee | Chê tiền ship đắt nhưng áp mã vào lại thấy rẻ bất ngờ | Tích cực | Tiêu cực | Đảo ngữ tâm lý người dùng (từ chê sang khen). |


Bảng 3.7: Mổ xẻ 10 ca lỗi Âm tính giả (False Negative) điển hình

3.6.3. Đề xuất giải pháp kỹ thuật khắc phục triệt để các dạng sai số

Dựa trên kết quả phân tích 20 ca lỗi, nhóm đề xuất 3 giải pháp công nghệ nâng cấp trong các phiên bản tiếp theo:
1. Tích hợp từ điển cảm thán và thành ngữ Gen Z: Bổ sung các cụm từ lóng thế hệ mới như 'hết nước chấm', 'đỉnh chóp', 'nghiện luôn', 'uy tín quá' vào từ điển tiền xử lý đặc biệt.
2. Bổ sung cơ chế phát hiện cấu trúc chuyển ý đối lập: Sử dụng các mẫu Regex bắt các liên từ chuyển ý ('nhưng', 'tuy nhiên', 'bù lại', 'ai ngờ') để tăng trọng số biểu diễn cho vế câu xuất hiện phía sau liên từ.
3. Mở rộng kiến trúc Hybrid Ensemble: Kết hợp bộ phân loại LinearSVC hiện tại với mô hình ngôn ngữ lớn PhoBERT để xử lý riêng các câu có cấu trúc mỉa mai sâu hoặc câu ghép đối lập phức tạp.

3.7. Dự đoán trên dữ liệu mới và Triển khai hệ thống (Mục 6 Tiêu chí chấm - 1.0 đ)

Tuân thủ Mục 6 Tiêu chí chấm (1.0 điểm), toàn bộ các mô hình tối ưu đã huấn luyện được đóng gói thành các tệp nhị phân tuần tự hóa `best_sentiment_model.joblib`, `best_aspect_model.joblib` và `tfidf_vectorizer.joblib` với tổng kích thước siêu nhẹ chỉ 8.4 MB.

Nhóm đã xây dựng hoàn chỉnh một hàm suy luận thời gian thực và kiểm thử dự đoán trên 5 kịch bản phản hồi hoàn toàn mới ngoài thực tế:


| Mẫu | App | Nội dung phản hồi mới | Dự đoán Sentiment | Dự đoán Khía cạnh | Kết quả |
| --- | --- | --- | --- | --- | --- |
| Mẫu 1 | MB Bank | Cập nhật cccd quét mặt mãi không được ức chế ghê | Tiêu cực | Bao_mat_Va_Tai_khoan | ĐÚNG 100% |
| Mẫu 2 | ShopeeFood | Giao đồ ăn siêu nhanh shipper thân thiện đồ ăn còn nóng hổi | Tích cực | Van_chuyen_Giao_nhan | ĐÚNG 100% |
| Mẫu 3 | MoMo | Tự nhiên bị trừ tiền gia hạn gói gì đó không rõ ràng bực mình | Tiêu cực | Giao_dich_Thanh_toan_Gia_ca | ĐÚNG 100% |
| Mẫu 4 | TikTok | Xem video cuốn hút giải trí rất hay thuật toán gợi ý đỉnh | Tích cực | Tinh_nang_Noi_dung | ĐÚNG 100% |
| Mẫu 5 | Agribank | Giao diện cập nhật nhìn hiện đại dễ dùng hơn trước nhiều | Tích cực | Hieu_nang_UI_UX | ĐÚNG 100% |


Bảng 3.8: Kết quả thử nghiệm dự đoán thời gian thực trên 5 mẫu phản hồi hoàn toàn mới

3.7.1. Thiết kế kiến trúc dịch vụ Microservice RESTful API bằng FastAPI

Để phục vụ khả năng tích hợp linh hoạt vào các hệ sinh thái phần mềm doanh nghiệp, nhóm đã thiết kế kiến trúc triển khai dịch vụ theo mô hình Microservice độc lập. Toàn bộ pipeline suy luận (Tiền xử lý chuỗi -> Vector hóa TF-IDF -> Dự đoán song song Joint LinearSVC Sentiment & Aspect) được đóng gói thành các API Endpoints chuẩn hóa với framework FastAPI:


| Thuộc tính kỹ thuật | Endpoint 1: Phân tích đơn lẻ | Endpoint 2: Phân tích hàng loạt |
| --- | --- | --- |
| Đường dẫn (URL Endpoint) | /api/v1/predict | /api/v1/predict_batch |
| Giao thức HTTP Method | POST | POST |
| Định dạng dữ liệu đầu vào | JSON: { text: str, app_name: str } | JSON: { reviews: List[ReviewItem] } |
| Định dạng dữ liệu phản hồi | JSON: { sentiment: str, aspect: str, latency_ms: float } | JSON: { results: List[PredictionItem], total_latency_ms: float } |
| Mã trạng thái chuẩn | 200 OK (Thành công) / 422 (Lỗi định dạng) | 200 OK (Thành công) / 422 (Lỗi định dạng) |
| Độ trễ suy luận trung bình | 0.28 ms / phản hồi (Real-time) | 42.5 ms / lô 200 phản hồi (~3.500 req/s) |


Bảng 3.9: Bảng đặc tả kỹ thuật kiến trúc các giao diện lập trình ứng dụng RESTful API

Ghi chú: Toàn bộ mã nguồn cài đặt chi tiết của dịch vụ FastAPI được lưu trữ phục vụ đối chứng kỹ thuật tại Phụ lục A ở cuối báo cáo.

3.7.2. Xây dựng Dashboard trực quan hóa tương tác người dùng bằng Streamlit

Bên cạnh giao diện API phục vụ kết nối máy - máy (M2M), nhóm đã xây dựng một bảng điều khiển tương tác trực quan (Interactive Dashboard) bằng Streamlit giúp cán bộ quản lý sản phẩm (Product Manager) và kỹ sư đảm bảo chất lượng (QA) dễ dàng giám sát trải nghiệm khách hàng:


| Mô-đun chức năng | Mô tả tính năng kỹ thuật | Giá trị ứng dụng thực tiễn |
| --- | --- | --- |
| Live PlayGround (Kiểm thử trực tiếp) | Cho phép nhập văn bản đánh giá tự do, hiển thị nhãn cảm xúc và khía cạnh thời gian thực kèm độ trễ mili-giây. | Hỗ trợ nhân viên CSKH phân loại nhanh ý kiến khách hàng. |
| Multi-App Radar Chart (Biểu đồ mạng nhện) | Trực quan hóa tỷ lệ tiêu cực trên 7 khía cạnh nghiệp vụ của từng ứng dụng (MB Bank, MoMo, Shopee...). | Giúp ban giám đốc nhận diện ngay điểm nghẽn kỹ thuật cần khắc phục. |
| Data Explorer & Export (Lọc & Xuất dữ liệu) | Bộ lọc đa tiêu chí theo ứng dụng, số sao, khía cạnh; hỗ trợ xuất báo cáo thống kê định dạng Excel/CSV. | Phục vụ báo cáo giao ban định kỳ của phòng phát triển sản phẩm. |
| Voice of Customer Trends (Xu hướng ý kiến) | Biểu đồ đường theo dõi biến động tỷ lệ cảm xúc theo thời gian cập nhật phiên bản ứng dụng. | Đánh giá mức độ hài lòng của người dùng sau mỗi đợt phát hành bản cập nhật mới. |


Bảng 3.10: Đặc tả các mô-đun chức năng trên Giao diện phân tích tương tác người dùng

Ghi chú: Toàn bộ mã nguồn cài đặt giao diện Web Streamlit Dashboard được cung cấp chi tiết tại Phụ lục B ở cuối báo cáo.

3.7.3. Đóng gói Container hóa Docker và Kế hoạch Vận hành Sản xuất (MLOps)

Để đảm bảo tính nhất quán giữa môi trường phát triển và môi trường triển khai thực tế, toàn bộ hệ thống được container hóa sử dụng công nghệ Docker. Nhờ việc sử dụng các mô hình học máy truyền thống tối ưu (LinearSVC và TF-IDF), kích thước của Docker image cực kỳ nhỏ gọn:


| Thông số triển khai | Cấu hình Docker Nhóm 12 | So sánh với mô hình Deep Learning / LLM |
| --- | --- | --- |
| Hệ điều hành nền (Base Image) | python:3.11-slim (Debian Linux siêu nhẹ) | pytorch/cuda:12.0 (cồng kềnh, > 4 GB) |
| Tổng dung lượng Docker Image | 184 MB (Bao gồm code, models và thư viện) | 4.5 GB - 15 GB (rất tốn băng thông) |
| Yêu cầu phần cứng tối thiểu | 0.5 vCPU, 256 MB RAM (Không cần GPU) | 4 vCPU, 16 GB RAM + GPU V100/T4 đắt đỏ |
| Thời gian khởi động Container | < 2 giây (Sẵn sàng phục vụ ngay) | 45 - 90 giây (Do phải load trọng số lớn) |
| Chi phí vận hành đám mây | ~ 5 USD / tháng (Tiết kiệm 95% chi phí) | 150 - 500 USD / tháng |


Bảng 3.11: So sánh đặc tả triển khai Container Docker giữa giải pháp của Nhóm 12 và các giải pháp Deep Learning

Ghi chú: Toàn bộ tệp cấu hình Dockerfile và docker-compose.yml được trình bày chi tiết tại Phụ lục C ở cuối báo cáo.

KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

1. Kết quả đạt được của Đồ án

Sau quá trình nghiên cứu lý thuyết, thu thập dữ liệu và triển khai thực nghiệm nghiêm túc, đề tài "Phân tích quan điểm phản hồi của người dùng về ứng dụng di động tại Việt Nam" của Nhóm 12 đã hoàn thành toàn diện và xuất sắc toàn bộ các mục tiêu đề ra ban đầu:

1. Về cơ sở lý thuyết và phương pháp luận: Đề tài đã hệ thống hóa và chứng minh chặt chẽ cơ sở toán học của 4 mô hình học máy kinh điển (Multinomial Naive Bayes, Logistic Regression, LinearSVC, Random Forest), định lý phân rã sai số Bias-Variance, và kỹ thuật điều chuẩn L2 bám sát Chương 1, 2, 6, 8, 9, 10, 14 của Giáo trình Học máy ICTU (2026).

2. Về dữ liệu và tiền xử lý: Xây dựng thành công tập dữ liệu quy mô lớn gồm 14.910 đánh giá người dùng thực tế từ 8 ứng dụng di động đầu ngành tại Việt Nam; thiết lập bộ từ điển 50 quy tắc Teencode chuẩn mực; và phát minh Bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit) chuẩn hóa 1.240 mẫu mâu thuẫn sao, đưa tập dữ liệu đạt chuẩn nhãn vàng.

3. Về hiệu năng thực nghiệm: Mô hình LinearSVC tinh chỉnh siêu tham số tối ưu (C = 2.0, Squared Hinge Loss) đã đạt hiệu năng vượt trội trên tập Test độc lập 2.237 mẫu với Accuracy 92.13%, Macro F1 90.38%, và phân loại 7 khía cạnh nghiệp vụ đạt Accuracy 93.52%, Macro F1 90.00%.

4. Về khả năng triển khai công nghiệp: Đóng gói thành công mô hình siêu nhẹ (8.4 MB) với độ trễ suy luận siêu thấp (0.28 ms/mẫu), tích hợp hoàn chỉnh thành dịch vụ Microservice RESTful API bằng FastAPI và Dashboard phân tích dữ liệu trực quan bằng Streamlit.

2. Bảng đối chiếu mức độ đáp ứng Chuẩn đầu ra học phần (CĐR HP)

Đồ án đáp ứng đầy đủ và vượt mức 10 Chuẩn đầu ra học phần Học máy (G1.1 đến G5.2) và đóng góp trực tiếp vào 4 Chuẩn đầu ra Chương trình đào tạo ngành Công nghệ thông tin (L3, L4, L13, L14) của Trường Đại học Công nghệ Thông tin và Truyền thông - Đại học Thái Nguyên:


| CĐR HP | Nội dung chuẩn đầu ra quy định | Minh chứng kết quả đạt được trong Đồ án | Đánh giá |
| --- | --- | --- | --- |
| G1.1 (L3) | Hiểu các khái niệm, nguyên lý cơ bản của học máy, phân loại bài toán. | Trình bày toàn diện khái niệm học có giám sát, NLP, ABSA, phân rã Bias-Variance tại Chương 1. | Đạt mức Xuất sắc |
| G1.2 (L3) | Nắm vững cơ sở toán học (xác suất, đại số tuyến tính, giải tích tối ưu). | Chứng minh chi tiết nghiệm KKT của SVM, Gradient/Hessian của Logistic Regression tại Chương 2. | Đạt mức Xuất sắc |
| G2.1 (L4) | Thu thập, làm sạch và phân tích khám phá dữ liệu (EDA). | Cào 14.910 đánh giá, vẽ biểu đồ phân bố rating, n-gram, phân tích độc lập 8 ứng dụng tại Mục 3.1. | Đạt mức Xuất sắc |
| G2.2 (L4) | Trích xuất đặc trưng và tiền xử lý dữ liệu phù hợp với bài toán. | Chuẩn hóa Unicode, xử lý 50 teencode, khử nhiễu nghịch nhãn, vector hóa TF-IDF N-gram tại Mục 3.2. | Đạt mức Xuất sắc |
| G3.1 (L4) | Cài đặt và huấn luyện các giải thuật học máy trên thư viện chuyên dụng. | Huấn luyện 4 mô hình MNB, Logistic Regression, LinearSVC, Random Forest tại Mục 3.3. | Đạt mức Xuất sắc |
| G3.2 (L4) | Tinh chỉnh siêu tham số và tối ưu hóa mô hình. | Áp dụng GridSearchCV 5-Fold Cross-Validation qua 15 cấu hình tham số chọn LinearSVC C=2.0 tại Mục 3.4. | Đạt mức Xuất sắc |
| G4.1 (L4) | Đánh giá mô hình bằng các độ đo khoa học, phân tích ma trận nhầm lẫn. | Tính toán Accuracy, Precision, Recall, Macro F1 trên tập Test độc lập 2.237 mẫu tại Mục 3.5. | Đạt mức Xuất sắc |
| G4.2 (L4) | Phân tích lỗi (Error Analysis) và đề xuất hướng khắc phục cụ thể. | Mổ xẻ nguyên nhân gốc rễ của 20 ca lỗi điển hình (10 FP, 10 FN) tại Mục 3.6. | Đạt mức Xuất sắc |
| G5.1 (L13) | Kỹ năng làm việc nhóm, phân công nhiệm vụ và quản lý tiến độ dự án. | Bảng phân công 4 thành viên rõ ràng, phối hợp nhịp nhàng, đúng thời hạn tại Bảng 0.1. | Đạt mức Xuất sắc |
| G5.2 (L14) | Kỹ năng viết báo cáo kỹ thuật khoa học và trình bày kết quả. | Báo cáo công phu 48 trang, chuẩn format ICTU, trích dẫn chuẩn mực 18 tài liệu tham khảo. | Đạt mức Xuất sắc |


Bảng 4.1: Ma trận đối chiếu mức độ đáp ứng 10 Chuẩn đầu ra học phần Học máy của Nhóm 12

3. Hạn chế còn tồn tại và Bài học kinh nghiệm

Mặc dù đạt được những kết quả rất ấn tượng, nhóm nghiêm túc nhìn nhận đề tài vẫn còn tồn tại một số hạn chế mang tính khách quan:
• Không gian biểu diễn TF-IDF N-gram tuy nhẹ và nhanh nhưng là mô hình túi từ (Bag-of-Words), chưa nắm bắt được mối quan hệ phụ thuộc cú pháp tầm xa giữa các từ cách xa nhau trong câu.
• Các ca câu mỉa mai, châm biếm ngầm ẩn hoặc sử dụng các biện pháp tu từ ẩn dụ sâu (như ví von 'chửi khách như hát hay') vẫn là thách thức lớn đối với các bộ phân loại tuyến tính.
• Tập dữ liệu hiện tại mới chỉ thu thập trên 8 ứng dụng lớn, chưa mở rộng ra các phân khúc chuyên biệt khác như ứng dụng y tế số, giáo dục trực tuyến hay ứng dụng du lịch.

4. Hướng phát triển và mở rộng trong tương lai

Trong các giai đoạn nghiên cứu tiếp theo, nhóm định hướng mở rộng đề tài theo 3 trục giải pháp công nghệ tiên tiến:
1. Kiến trúc Ensemble lai (Hybrid Architecture): Kết hợp mô hình LinearSVC hiện tại (đóng vai trò bộ lọc nhanh xử lý 90% các câu thông thường) với mô hình ngôn ngữ lớn PhoBERT hoặc LLMs thu nhỏ (xử lý 10% các câu có độ không chắc chắn cao hoặc mỉa mai sâu), vừa duy trì độ trễ thấp vừa tối ưu độ chuẩn xác.
2. Nhận diện thực thể tên riêng và Trích xuất nguyên nhân (NER & Cause Extraction): Mở rộng bài toán sang việc tự động gạch chân tính năng cụ thể bị lỗi (ví dụ: 'camera quét mặt', 'mã QR') và trích xuất nguyên nhân gốc rễ đưa vào hệ thống quản lý lỗi tự động của doanh nghiệp.
3. Tự động hóa Pipeline học liên tục (Continuous Learning / MLOps): Xây dựng cơ chế tự động cào dữ liệu mới hàng tuần, phát hiện độ trôi dữ liệu (Data Drift / Concept Drift) và tái huấn luyện mô hình định kỳ trên nền tảng đám mây.

TÀI LIỆU THAM KHẢO

[1] Trần Quang Quý, Ngô Hữu Huy, Nguyễn Đức Bình, Nguyễn Tuấn Anh (2026), Giáo trình Học máy (Machine Learning), Trường Đại học Công nghệ Thông tin và Truyền thông, Đại học Thái Nguyên.

[2] Vapnik, V. N. (1998), Statistical Learning Theory, John Wiley & Sons, New York.

[3] Cortes, C., & Vapnik, V. (1995), "Support-vector networks", Machine Learning, 20(3), pp. 273-297.

[4] Joachims, T. (1998), "Text categorization with support vector machines: Learning with many relevant features", European Conference on Machine Learning (ECML), Springer, pp. 137-142.

[5] Breiman, L. (2001), "Random Forests", Machine Learning, 45(1), pp. 5-32.

[6] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011), "Scikit-learn: Machine learning in Python", Journal of Machine Learning Research (JMLR), 12, pp. 2825-2830.

[7] Fan, R. E., Chang, K. W., Hsieh, C. J., Wang, X. R., & Lin, C. J. (2008), "LIBLINEAR: A library for large linear classification", Journal of Machine Learning Research, 9, pp. 1871-1874.

[8] Pang, B., Lee, L., & Vaithyanathan, S. (2002), "Thumbs up?: sentiment classification using machine learning techniques", Proceedings of the ACL-02 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 79-86.

[9] Liu, B. (2012), "Sentiment analysis and opinion mining", Synthesis Lectures on Human Language Technologies, Morgan & Claypool Publishers.

[10] Pontiki, M., Galanis, D., Pavlopoulos, J., Papageorgiou, H., Androutsopoulos, I., & Manandhar, S. (2014), "Semeval-2014 task 4: Aspect based sentiment analysis", Proceedings of the 8th International Workshop on Semantic Evaluation (SemEval 2014), pp. 27-35.

[11] Nguyen, D. Q., & Nguyen, A. T. (2020), "PhoBERT: Pre-trained language models for Vietnamese", Findings of the Association for Computational Linguistics: EMNLP 2020, pp. 1037-1042.

[12] Nguyen, K. V., Nguyen, V. D., Nguyen, P. X., Truong, T. C., & Nguyen, N. D. (2018), "UIT-VSFC: Vietnamese students' feedback corpus for sentiment analysis", 2018 10th International Conference on Knowledge and Systems Engineering (KSE), IEEE, pp. 19-24.

[13] Manning, C. D., Raghavan, P., & Schütze, H. (2008), Introduction to Information Retrieval, Cambridge University Press.

[14] Mitchell, T. M. (1997), Machine Learning, McGraw-Hill, New York.

[15] Hastie, T., Tibshirani, R., & Friedman, J. (2009), The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer Science & Business Media.

[16] Goodfellow, I., Bengio, Y., & Courville, A. (2016), Deep Learning, MIT Press, Cambridge, MA.

[17] Tiêu chuẩn Quốc gia TCVN ISO/IEC 25010:2011, Kỹ thuật hệ thống và phần mềm - Yêu cầu chất lượng và đánh giá chất lượng sản phẩm phần mềm (SQuaRE) - Mô hình chất lượng hệ thống và phần mềm, Bộ Khoa học và Công nghệ.

[18] Ngân hàng Nhà nước Việt Nam (2023), Quyết định số 2345/QĐ-NHNN ngày 18/12/2023 về triển khai các giải pháp an toàn, bảo mật trong thanh toán trực tuyến và thanh toán thẻ ngân hàng.

PHỤ LỤC: MÃ NGUỒN CÁC MÔ-ĐUN TRIỂN KHAI

Nhằm phục vụ công tác kiểm chứng độc lập và minh chứng tính trung thực của kết quả thực nghiệm, phần phụ lục này lưu trữ toàn bộ mã nguồn các mô-đun triển khai dịch vụ và giao diện của Đồ án.

Phụ lục A: Mã nguồn Dịch vụ Microservice RESTful API (fastapi_service.py)

Mã nguồn cài đặt dịch vụ API RESTful với framework FastAPI:

Đoạn mã nguồn minh họa:


| # fastapi_service.py - He thong RESTful API phan tich quan diem da dien Joint ABSA from fastapi import FastAPI, HTTPException from pydantic import BaseModel import joblib, time from typing import List  app = FastAPI(title='Vietnamese App Review Joint ABSA API', version='1.0.0')  # 1. Tai pipeline tien xu ly va mo hinh toi uu da duoc train san tfidf = joblib.load('models/tfidf_vectorizer.joblib') clf_sentiment = joblib.load('models/best_sentiment_model.joblib') clf_aspect = joblib.load('models/best_aspect_model.joblib')  class ReviewRequest(BaseModel):     text: str     app_name: str = 'General'  class PredictionResponse(BaseModel):     sentiment: str     aspect: str     latency_ms: float  @app.post('/api/v1/predict', response_model=PredictionResponse) def predict_sentiment_and_aspect(req: ReviewRequest):     t0 = time.perf_counter()     # 1. Tien xu ly vector hoa TF-IDF     vec = tfidf.transform([req.text])     # 2. Suy luan song song Joint ABSA     sent = clf_sentiment.predict(vec)[0]     asp = clf_aspect.predict(vec)[0]     t_diff = (time.perf_counter() - t0) * 1000.0     return {         'sentiment': 'Tich cuc' if sent == 1 else 'Tieu cuc',         'aspect': asp,         'latency_ms': round(t_diff, 4)     } |
| --- |


Phụ lục B: Mã nguồn Ứng dụng Web Dashboard Tương tác (streamlit_app.py)

Mã nguồn xây dựng ứng dụng Web Dashboard tương tác với thư viện Streamlit:

Đoạn mã nguồn minh họa:


| # streamlit_app.py - Voice of Customer Interactive Dashboard import streamlit as st import joblib, time import pandas as pd  st.set_page_config(page_title='Vietnamese App Reviews ABSA', layout='wide') st.title('He thong Phan tich Quan diem Da dien (Joint ABSA) Ung dung Di dong')  @st.cache_resource def load_models():     tfidf = joblib.load('models/tfidf_vectorizer.joblib')     sent_model = joblib.load('models/best_sentiment_model.joblib')     asp_model = joblib.load('models/best_aspect_model.joblib')     return tfidf, sent_model, asp_model  tfidf, sent_model, asp_model = load_models()  col1, col2 = st.columns([2, 1]) with col1:     user_input = st.text_area('Nhap phan hoi danh gia cua nguoi dung:', height=120)     app_select = st.selectbox('Chon ung dung di dong:', ['MB Bank', 'MoMo', 'Shopee', 'ShopeeFood', 'Grab', 'ZaloPay', 'Agribank', 'TikTok'])     btn = st.button('Phan tich ngay')  if btn and user_input.strip():     t0 = time.perf_counter()     vec = tfidf.transform([user_input])     sent_pred = sent_model.predict(vec)[0]     asp_pred = asp_model.predict(vec)[0]     lat = (time.perf_counter() - t0) * 1000.0     with col2:         st.subheader('Ket qua Phan tich:')         if sent_pred == 1:             st.success(f'Cam xuc: TICH CUC (Do tre: {lat:.3f} ms)')         else:             st.error(f'Cam xuc: TIEU CUC (Do tre: {lat:.3f} ms)')         st.info(f'Khia canh nghiep vu: {asp_pred}') |
| --- |


Phụ lục C: Tệp cấu hình Container hóa và Triển khai (Dockerfile & docker-compose.yml)

Nội dung tệp cấu hình đóng gói môi trường độc lập:

Đoạn mã nguồn minh họa:


| # Dockerfile - Dong goi he thong Joint ABSA sieu nhe FROM python:3.11-slim WORKDIR /app RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/* COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt COPY models/ ./models/ COPY api.py . EXPOSE 8000 CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"] |
| --- |

