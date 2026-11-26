# -*- coding: utf-8 -*-
"""
Module: chapter2_expanded.py
Comprehensive Chapter 2 for Machine Learning Project Report (ICTU 2026).
Word budget: ~5,500 words. Full mathematical rigor and formal proofs.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from .helpers import (
    add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_math_block, add_callout,
    add_code_snippet, add_image_with_caption, set_cell_background, set_cell_margins
)

def add_chapter2(doc):
    add_heading_1(doc, "CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ CƠ SỞ TOÁN HỌC CÁC MÔ HÌNH")

    # -------------------------------------------------------------
    # 2.1. TIỀN XỬ LÝ DỮ LIỆU ĐA TẦNG
    # -------------------------------------------------------------
    add_heading_2(doc, "2.1. Quy trình Tiền xử lý dữ liệu văn bản tiếng Việt đa tầng")
    add_body_p(doc, "Dữ liệu văn bản thô thu thập từ phản hồi người dùng trên các kho ứng dụng (App Store, Google Play) chứa đựng vô số nhiễu: lỗi chính tả, teencode, icon cảm xúc phức tạp, thông tin nhạy cảm và cách diễn đạt phi cấu trúc. Để chuẩn bị cho việc trích xuất đặc trưng toán học, nhóm đã xây dựng một đường ống tiền xử lý đa tầng (Multi-stage Preprocessing Pipeline) bao gồm 4 bước kỹ thuật nghiêm ngặt:")

    add_heading_3(doc, "2.1.1. Chuẩn hóa mã ký tự Unicode và Ẩn danh thông tin cá nhân (PII)")
    add_body_p(doc, "Tiếng Việt có hai dạng biểu diễn ký tự có dấu phổ biến: Unicode dựng sẵn (NFC - Normalization Form C) và Unicode tổ hợp (NFD - Normalization Form D). Ví dụ, ký tự \"ế\" trong NFC được lưu trữ bằng 1 code point duy nhất (U+1E7F), trong khi trong NFD được tạo thành từ 3 code point ghép lại: ký tự gốc \"e\" (U+0065) + dấu nón \"^\" (U+0302) + dấu sắc \"/\" (U+0301). Nếu không quy chuẩn, hai từ nhìn giống hệt nhau sẽ bị máy tính coi là hai từ hoàn toàn khác biệt, gây bùng nổ số chiều từ vựng một cách giả tạo. Nhóm áp dụng hàm `unicodedata.normalize('NFC', text)` đưa toàn bộ văn bản về dạng dựng sẵn đồng nhất.")
    add_body_p(doc, "Đồng thời, để tuân thủ quy định bảo mật dữ liệu người dùng (Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân), toàn bộ các thông tin định danh cá nhân (Personally Identifiable Information - PII) như số điện thoại (ví dụ: 098xxxxxxx), địa chỉ email (ví dụ: user@gmail.com), số tài khoản ngân hàng và các đường dẫn URL đều được phát hiện bằng biểu thức chính quy (Regex) và thay thế bằng các token đặc biệt tương ứng: `[PHONE]`, `[EMAIL]`, `[URL]` trước khi đưa vào mô hình.")

    add_heading_3(doc, "2.1.2. Xây dựng từ điển Teencode và Chuẩn hóa từ lóng công nghệ")
    add_body_p(doc, "Giới trẻ và người dùng di động tại Việt Nam có xu hướng sử dụng ngôn ngữ viết tắt (Teencode) rất dày đặc. Nhóm đã khảo sát thực tế trên tập dữ liệu cào và đúc kết một từ điển chuẩn hóa Teencode gồm 50 quy tắc phổ biến nhất được phân loại thành các nhóm ngữ nghĩa:")

    t_teen = doc.add_table(rows=26, cols=4)
    t_teen.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_t = [Inches(1.5), Inches(1.5), Inches(1.5), Inches(1.5)]
    headers_t = ["Từ gốc (Teencode)", "Dạng chuẩn hóa", "Từ gốc (Teencode)", "Dạng chuẩn hóa"]

    hdr_tn = t_teen.rows[0]
    for j, h in enumerate(headers_t):
        c = hdr_tn.cells[j]
        c.width = w_t[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 70, 70, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    teencode_pairs = [
        ("k / ko / kh / hok / hem", "không", "đc / dc / dk / duoc", "được"),
        ("app / áp / ứng dụng", "ứng_dụng", "acc / tk / nick", "tài_khoản"),
        ("chán / tệ / dở / cùi", "kém", "nhanh / mượt / xịn", "tốt"),
        ("lag / đơ / giật / treo", "chậm", "ship / giao hàng", "vận_chuyển"),
        ("r / rùi / ròi", "rồi", "cx / cũng", "cũng"),
        ("ms / mới", "mới", "h / hnay / hn", "hôm_nay"),
        ("mik / mk / mình", "mình", "ng / ngta / ngừi", "người"),
        ("nv / cskh / tổng đài", "nhân_viên", "bill / hóa đơn", "hóa_đơn"),
        ("otp / mã otp", "mã_xác_thực", "scan / quét mặt", "sinh_trắc_học"),
        ("voucher / mã giảm giá", "khuyến_mãi", "hoàn tiền / hoàn xu", "hoàn_tiền"),
        ("bực / cáu / tức", "thất_vọng", "ok / oki / okee", "hài_lòng"),
        ("update / cập nhật", "cập_nhật", "login / đăng nhập", "đăng_nhập"),
        ("crash / văng / sập", "lỗi_ứng_dụng", "pass / mk / mật khẩu", "mật_khẩu"),
        ("sp / shop / ng bán", "người_bán", "feed / bài viết", "bài_đăng"),
        ("cmt / cmt dạo", "bình_luận", "tt / thanh toán", "thanh_toán"),
        ("ck / chuyển khoản", "chuyển_tiền", "nạp / rút", "giao_dịch"),
        ("đắt / mắc / chát", "giá_cao", "rẻ / bèo / hời", "giá_tốt"),
        ("tệ hại / tệ bạc", "rất_tệ", "tuyệt vời / đỉnh", "rất_tốt"),
        ("phí ship / tiền ship", "phí_vận_chuyển", "driver / shipper", "tài_xế"),
        ("quá lâu / chờ mòn mỏi", "rất_lâu", "nhiệt tình / chu đáo", "tận_tâm"),
        ("quét căn cước / cccd", "sinh_trắc_học", "lừa đảo / scam", "gian_lận"),
        ("khóa acc / ban nick", "khóa_tài_khoản", "trừ tiền / mất tiền", "lỗi_trừ_tiền"),
        ("quảng cáo / qc", "quảng_cáo", "thông báo / noti", "thông_báo"),
        ("gỡ app / xóa app", "xóa_ứng_dụng", "chăm sóc / sp", "hỗ_trợ_khách_hàng"),
        ("bảo mật / an toàn", "bảo_mật", "tiện lợi / dễ dùng", "tiện_lợi")
    ]

    for i, row in enumerate(teencode_pairs):
        r_el = t_teen.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_t[j]
            set_cell_margins(c, 40, 40, 40, 40)
            if i % 2 == 1:
                set_cell_background(c, "F9FBFD")
            p = c.paragraphs[0]
            if j in [0, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
                r.font.bold = True
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.0)

    add_body_p(doc, "\nBảng 2.1: Từ điển 50 quy tắc Teencode và chuẩn hóa từ lóng công nghệ của Nhóm 12")

    add_heading_3(doc, "2.1.3. Thuật toán phân tách từ ghép tiếng Việt (Word Segmentation)")
    add_body_p(doc, "Không giống như tiếng Anh vốn có ranh giới từ được phân tách rõ ràng bằng dấu khoảng trắng, trong tiếng Việt, khoảng trắng vừa đóng vai trò là ranh giới giữa các từ đơn, vừa là ranh giới giữa các âm tiết cấu thành từ ghép. Nếu tách từ thuần túy bằng khoảng trắng (Whitespace Tokenizer), cụm từ \"ngân hàng số\" sẽ bị chẻ nhỏ thành 3 từ đơn \"ngân\", \"hàng\", \"số\" - làm mất hoàn toàn ngữ nghĩa của thực thể nghiệp vụ.")
    add_body_p(doc, "Nhóm sử dụng thư viện `underthesea` áp dụng mô hình Trường ngẫu nhiên có điều kiện tuyến tính (Linear-chain Conditional Random Fields - CRF) kết hợp giải thuật quy hoạch động Viterbi để gán nhãn chuỗi theo định dạng IOB (Inside-Outside-Beginning). Xét chuỗi quan sát âm tiết x = (x_1, x_2, ..., x_T) và chuỗi nhãn ranh giới từ y = (y_1, y_2, ..., y_T) với y_t ∈ {B, I, O}. Xác suất có điều kiện của chuỗi nhãn y khi biết chuỗi âm tiết x được định nghĩa:")
    add_math_block(doc, "P(y | x) = (1 / Z(x)) exp( ∑_{t=1}^T ∑_{k=1}^K λ_k f_k(y_{t-1}, y_t, x, t) )", "2.1")
    add_body_p(doc, "Trong đó: f_k là các hàm đặc trưng trích xuất từ ngữ cảnh (tiền tố, hậu tố, từ điển từ ghép); λ_k là trọng số học được từ dữ liệu huấn luyện; và Z(x) là hàm phân phối chuẩn hóa tổng xác suất về 1:")
    add_math_block(doc, "Z(x) = ∑_{y'} exp( ∑_{t=1}^T ∑_{k=1}^K λ_k f_k(y'_{t-1}, y'_t, x, t) )", "2.2")
    add_body_p(doc, "Để tìm chuỗi nhãn tối ưu y* có xác suất lớn nhất mà không phải duyệt qua toàn bộ số lượng chuỗi nhãn hàm mũ (|Y|^T), giải thuật quy hoạch động Viterbi được sử dụng với độ phức tạp tính toán O(T · |Y|²):")
    add_math_block(doc, "y* = argmax_{y} P(y | x) = argmax_{y} ∑_{t=1}^T ∑_{k=1}^K λ_k f_k(y_{t-1}, y_t, x, t)", "2.3")
    add_body_p(doc, "Kết quả phân tách được liên kết bằng ký tự gạch dưới (Ví dụ: \"chuyển_tiền\", \"sinh_trắc_học\", \"ứng_dụng\", \"hài_lòng\"), giúp bảo toàn nguyên vẹn ngữ nghĩa đơn vị từ ghép trong các giai đoạn xử lý tiếp theo.")

    # -------------------------------------------------------------
    # 2.2. XÂY DỰNG KHÔNG GIAN ĐẶC TRƯNG TF-IDF N-GRAM
    # -------------------------------------------------------------
    add_heading_2(doc, "2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm")
    add_body_p(doc, "Để các thuật toán học máy có thể tính toán trên dữ liệu văn bản tự nhiên, ta cần chuyển đổi các chuỗi ký tự thành các vector số thực trong không gian Euclide. Phương pháp TF-IDF (Term Frequency - Inverse Document Frequency) kết hợp N-gram là kỹ thuật biểu diễn kinh điển nhưng đặc biệt hiệu quả, đánh giá tầm quan trọng của một từ vựng dựa trên tần suất xuất hiện cục bộ trong văn bản và độ hiếm gặp trên toàn bộ kho ngữ liệu.")

    add_heading_3(doc, "2.2.1. Tần suất từ (Term Frequency - TF) và Sublinear TF Scaling")
    add_body_p(doc, "Tần suất từ thô (Raw Term Frequency) tf(t, d) đếm số lần từ t xuất hiện trong văn bản d. Tuy nhiên, nếu một từ xuất hiện 20 lần trong một phản hồi thì tầm quan trọng của nó không thể cao gấp 20 lần so với một phản hồi chỉ chứa từ đó 1 lần. Để tránh hiện tượng các từ lặp lại nhiều lần lấn át các từ khác, nhóm áp dụng kỹ thuật hàm logarit dưới tuyến tính (Sublinear TF Scaling):")
    add_math_block(doc, "tf_{sublinear}(t, d) = 1 + ln(tf(t, d))  khi tf(t, d) > 0;  ngược lại bằng 0", "2.4")

    add_heading_3(doc, "2.2.2. Nghịch đảo tần suất văn bản (Inverse Document Frequency - IDF)")
    add_body_p(doc, "Độ đo IDF phản ánh mức độ cung cấp thông tin đặc trưng của từ t trên toàn bộ tập dữ liệu D. Những từ xuất hiện ở hầu hết mọi bài đánh giá (như \"và\", \"thì\", \"là\", \"app\") mang lại rất ít giá trị phân lớp, trong khi những từ đặc trưng xuất hiện có chọn lọc (như \"quẹt thẻ\", \"nguội tanh\", \"sinh_trắc_học\") lại mang lượng thông tin rất cao. Nhóm sử dụng công thức Smooth IDF có bổ sung số hạng làm mịn 1 ở cả tử số và mẫu số để triệt tiêu lỗi chia cho 0:")
    add_math_block(doc, "idf(t, D) = ln( (|D| + 1) / (df(t, D) + 1) ) + 1", "2.5")
    add_body_p(doc, "Trong đó: |D| là tổng số văn bản trong tập huấn luyện (|D| = 10.437); df(t, D) là tần suất văn bản (Document Frequency), tức số lượng văn bản chứa từ t.")

    add_heading_3(doc, "2.2.3. Khai thác n-gram (1, 2) và Chuẩn hóa Euclidean L2-norm")
    add_body_p(doc, "Nếu chỉ sử dụng các từ đơn lẻ (Unigram - 1-gram), mô hình sẽ hoàn toàn mù mờ trước ngữ cảnh phủ định hoặc tăng cường cảm xúc. Ví dụ: câu \"không tốt\" sẽ bị bóc tách thành \"không\" và \"tốt\" - dẫn tới việc mô hình nhận diện nhầm là cảm xúc tích cực do sự xuất hiện của từ \"tốt\". Nhóm thiết lập cấu hình N-gram dải rộng `ngram_range=(1, 2)` bao gồm cả từ đơn và cặp từ liền kề (Bigram - 2-gram), kết hợp tham số lọc `min_df=2` (loại bỏ từ hiếm chỉ xuất hiện 1 lần) và `max_df=0.9` (loại bỏ từ dừng xuất hiện trên 90% số câu).")
    add_body_p(doc, "Giá trị trọng số đặc trưng thô của từ t trong văn bản d là tích của hai thành phần:")
    add_math_block(doc, "w_{thô}(t, d) = tf_{sublinear}(t, d) × idf(t, D)", "2.6")
    add_body_p(doc, "Do độ dài của các phản hồi người dùng rất chênh lệch (từ 2 từ đến hơn 100 từ), các văn bản dài sẽ có tổng trọng số lớn hơn văn bản ngắn. Để loại bỏ ảnh hưởng của độ dài văn bản, toàn bộ vector đặc trưng x_d được chiếu lên mặt cầu đơn vị bằng chuẩn Euclid L2-norm:")
    add_math_block(doc, "x_d = ( w_{thô}(t_1, d) / ||w_d||₂ ,  w_{thô}(t_2, d) / ||w_d||₂ ,  ...,  w_{thô}(t_V, d) / ||w_d||₂ )^T", "2.7")
    add_body_p(doc, "Trong đó: ||w_d||₂ = √( ∑_{j=1}^V w_{thô}(t_j, d)² ). Sau chuẩn hóa, mọi vector văn bản đều có độ dài hình học bằng đúng 1: ||x_d||₂ = 1, nằm trong không gian Hilbert số chiều d = 24.619 chiều.")

    # -------------------------------------------------------------
    # 2.3. CƠ SỞ TOÁN HỌC BỘ PHÂN LOẠI NAIVE BAYES
    # -------------------------------------------------------------
    add_heading_2(doc, "2.3. Cơ sở toán học Bộ phân loại Naive Bayes")
    add_body_p(doc, "Bộ phân loại Naive Bayes là một trong những giải thuật phân lớp xác suất thống kê cơ bản và kinh điển nhất. Cho vector đặc trưng văn bản x = (x_1, x_2, ..., x_d) và tập các lớp mục tiêu C = {Tích cực, Tiêu cực}. Theo Định lý Bayes, xác suất hậu nghiệm (Posterior Probability) của lớp c khi quan sát văn bản x là:")
    add_math_block(doc, "P(y = c | x) = [ P(y = c) · P(x | y = c) ] / P(x)", "2.8")
    
    add_body_p(doc, "Trong đó, mẫu số P(x) = ∑_{c' ∈ C} P(y = c') P(x | y = c') là hằng số chuẩn hóa không phụ thuộc vào lớp c. Do đó, bài toán phân lớp quy về việc tìm lớp c cực đại hóa xác suất đồng thời (Maximum A Posteriori - MAP):")
    add_math_block(doc, "c* = argmax_{c ∈ C} P(y = c) · P(x | y = c)", "2.9")
    
    add_body_p(doc, "Giả định cốt lõi của Naive Bayes (\"thơ ngây\") là: khi biết trước nhãn lớp c, sự xuất hiện của các từ đặc trưng x_j là hoàn toàn độc lập với nhau (Conditional Independence Assumption):")
    add_math_block(doc, "P(x | y = c) = ∏_{j=1}^d P(x_j | y = c)", "2.10")
    
    add_body_p(doc, "Trong mô hình Multinomial Naive Bayes (MNB), xác suất của từ j trong lớp c được ước lượng từ tần suất xuất hiện trong tập huấn luyện. Nếu một từ t_j chưa từng xuất hiện trong các bài đánh giá của lớp c, xác suất cực đại hợp lý MLE sẽ bằng 0: P(t_j | c) = 0. Do công thức (2.10) là một tích các thừa số, một giá trị 0 duy nhất sẽ kéo toàn bộ tích về 0, làm mô hình hoàn toàn bất lực. Để giải quyết triệt để vấn đề này, kỹ thuật làm mịn Laplace Smoothing (hay cộng 1 - Additive Smoothing với tham số α = 1.0) được áp dụng:")
    add_math_block(doc, "P̂(t_j | y = c) = [ N_{cj} + α ] / [ ∑_{k=1}^d N_{ck} + α · d ]", "2.11")
    add_body_p(doc, "Trong đó: N_{cj} là tổng trọng số của từ j trong toàn bộ các văn bản thuộc lớp c; d = 24.619 là tổng kích thước không gian từ vựng. Để tránh hiện tượng tràn số dưới (Numerical Underflow) do nhân liên tiếp hàng nghìn xác suất cực nhỏ, ta chuyển phép toán sang không gian Logarit tự nhiên:")
    add_math_block(doc, "c* = argmax_{c ∈ C} [ ln P(y = c) + ∑_{j=1}^d x_j · ln P̂(t_j | y = c) ]", "2.12")
    add_body_p(doc, "Hạn chế chí mạng của Naive Bayes: Giả định độc lập điều kiện hoàn toàn trái ngược với thực tế ngôn ngữ tự nhiên, nơi các từ vựng luôn có mối liên kết cú pháp và ngữ nghĩa chặt chẽ (ví dụ: 'không' và 'được'). Do đó, MNB có xu hướng ước lượng xác suất hậu nghiệm bị lệch quá mức về hai cực 0 hoặc 1.")

    # -------------------------------------------------------------
    # 2.4. CƠ SỞ TOÁN HỌC HỒI QUY LOGISTIC VÀ ĐIỀU CHUẨN L2
    # -------------------------------------------------------------
    add_heading_2(doc, "2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2")
    add_body_p(doc, "Hồi quy Logistic (Logistic Regression) là mô hình phân loại tuyến tính xác suất thuộc lớp mô hình phân biệt (Discriminative Models). Mô hình mô hình hóa trực tiếp xác suất hậu nghiệm P(y = 1 | x) thông qua hàm kích hoạt phi tuyến Sigmoid (Logistic Function):")
    add_math_block(doc, "σ(z) = 1 / (1 + e^{-z})", "2.13")
    add_body_p(doc, "Với z = w^T x + b, trong đó w ∈ R^d là vector trọng số và b ∈ R là hệ số định kiến. Hàm Sigmoid có các tính chất giải tích tuyệt vời: miền giá trị nằm hoàn toàn trong khoảng mở (0, 1), đồ thị hình chữ S đối xứng qua tâm (0, 0.5), và đạo hàm bậc nhất có dạng đóng cực kỳ thanh lịch: σ'(z) = σ(z)(1 - σ(z)).")
    
    add_body_p(doc, "Giả sử biến mục tiêu nhị phân y_i ∈ {0, 1} tuân theo phân bố Bernoulli với xác suất p_i = P(y_i = 1 | x_i) = σ(w^T x_i + b). Hàm hợp lý (Likelihood Function) trên toàn bộ tập dữ liệu huấn luyện N mẫu độc lập là:")
    add_math_block(doc, "L(w, b) = ∏_{i=1}^N p_i^{y_i} (1 - p_i)^{1 - y_i}", "2.14")
    
    add_body_p(doc, "Lấy logarit tự nhiên và đổi dấu để chuyển từ bài toán cực đại hóa hàm hợp lý sang bài toán cực tiểu hóa hàm mất mát mất mát chéo nhị phân (Binary Cross-Entropy Loss hay Log-Loss), kết hợp số hạng điều chuẩn L2:")
    add_math_block(doc, "J(w, b) = - (1/N) ∑_{i=1}^N [ y_i ln p_i + (1 - y_i) ln(1 - p_i) ] + (1 / 2C) ||w||₂²", "2.15")
    
    add_body_p(doc, "Để tìm nghiệm tối ưu w*, ta tính vector Gradient bậc một và ma trận đạo hàm riêng bậc hai Hessian:")
    add_math_block(doc, "∇_w J = (1/N) ∑_{i=1}^N (p_i - y_i) x_i + (1/C) w", "2.16")
    add_math_block(doc, "H_w = ∇_w² J = (1/N) ∑_{i=1}^N p_i (1 - p_i) x_i x_i^T + (1/C) I_d", "2.17")
    add_body_p(doc, "Vì 0 < p_i < 1 nên p_i(1 - p_i) > 0, ma trận x_i x_i^T là ma trận nửa xác định dương, và số hạng điều chuẩn (1/C)I_d là xác định dương. Do đó, ma trận Hessian H_w luôn là ma trận đối xứng xác định dương (Positive Definite) trên toàn bộ không gian tham số. Điều này chứng minh rằng hàm mất mát J(w, b) là hàm lồi ngặt (Strictly Convex) và chỉ có duy nhất một điểm cực tiểu toàn cục (Global Minimum), hoàn toàn không bị kẹt ở các điểm cực tiểu địa phương. Thư viện Scikit-learn sử dụng giải thuật tối ưu hóa bậc hai tựa Newton L-BFGS (Limited-memory BFGS) xấp xỉ ma trận nghịch đảo Hessian H^{-1} để cập nhật nghiệm với tốc độ hội tụ siêu tuyến tính.")

    # -------------------------------------------------------------
    # 2.5. CƠ SỞ TOÁN HỌC MÁY VECTOR HỖ TRỢ - SVM (LINEARSVC)
    # -------------------------------------------------------------
    add_heading_2(doc, "2.5. Cơ sở toán học Máy vector hỗ trợ (LinearSVC)")
    add_body_p(doc, "Máy vector hỗ trợ (Support Vector Machines - SVM) do Vladimir Vapnik và Corinna Cortes phát minh là một trong những thuật toán học máy có nền tảng toán học đại số và hình học vững chắc nhất. Thay vì tối thiểu hóa sai số kinh nghiệm thông thường (Empirical Risk Minimization), SVM tối thiểu hóa sai số cấu trúc (Structural Risk Minimization) nhằm tìm kiếm một siêu phẳng phân tách có khoảng cách lề (Margin) rộng nhất đối với các điểm dữ liệu của cả hai lớp.")

    add_body_p(doc, "Cho tập dữ liệu D = {(x_i, y_i)}_{i=1}^N với x_i ∈ R^d và y_i ∈ {-1, +1}. Siêu phẳng phân cách tuyến tính được định nghĩa:")
    add_math_block(doc, "w^T x + b = 0", "2.18")
    add_body_p(doc, "Khoảng cách hình học từ điểm x_i bất kỳ tới siêu phẳng là γ_i = [ y_i(w^T x_i + b) ] / ||w||₂. Bài toán tối ưu hóa lề cực đại mềm (Soft-Margin SVM) cho phép một số điểm dữ liệu nằm trong vùng lề hoặc bị phân loại sai thông qua các biến bù trượt sai số ξ_i ≥ 0 (Slack Variables). Bài toán quy hoạch toàn phương nguyên thủy (Primal Quadratic Programming):")
    add_math_block(doc, "min_{w, b, ξ}  (1/2) ||w||₂² + C ∑_{i=1}^N ξ_i", "2.19")
    add_math_block(doc, "thỏa mãn ràng buộc:  y_i(w^T x_i + b) ≥ 1 - ξ_i   và   ξ_i ≥ 0,  ∀i = 1, ..., N", "2.20")

    add_body_p(doc, "Để giải bài toán có ràng buộc trên, ta thiết lập hàm nhân tử Lagrange (Lagrangian Function) với các nhân tử α_i ≥ 0 và r_i ≥ 0:")
    add_math_block(doc, "L(w, b, ξ, α, r) = (1/2) ||w||₂² + C ∑_{i=1}^N ξ_i - ∑_{i=1}^N α_i [ y_i(w^T x_i + b) - 1 + ξ_i ] - ∑_{i=1}^N r_i ξ_i", "2.21")
    
    add_body_p(doc, "Lấy đạo hàm riêng theo các biến nguyên thủy và cho bằng 0:")
    add_math_block(doc, "∂L/∂w = 0  =>  w = ∑_{i=1}^N α_i y_i x_i", "2.22")
    add_math_block(doc, "∂L/∂b = 0  =>  ∑_{i=1}^N α_i y_i = 0", "2.23")
    add_math_block(doc, "∂L/∂ξ_i = 0  =>  C - α_i - r_i = 0  =>  α_i ≤ C  (do r_i ≥ 0)", "2.24")

    add_body_p(doc, "Thế các kết quả trên ngược lại hàm Lagrange, ta thu được bài toán đối ngẫu Lagrange (Dual Problem):")
    add_math_block(doc, "max_{α}  ∑_{i=1}^N α_i - (1/2) ∑_{i=1}^N ∑_{j=1}^N α_i α_j y_i y_j (x_i^T x_j)", "2.25")
    add_math_block(doc, "thỏa mãn:  0 ≤ α_i ≤ C,  ∀i = 1, ..., N   và   ∑_{i=1}^N α_i y_i = 0", "2.26")

    add_body_p(doc, "Theo định lý Karush-Kuhn-Tucker (KKT), tại điểm nghiệm tối ưu, các điều kiện bù triệt tiêu (Complementary Slackness) phải được thỏa mãn đồng thời:\n"
                  "1. α_i = 0: Điểm x_i nằm ngoài khoảng lề (y_i(w^T x_i + b) > 1), phân loại đúng hoàn hảo, không ảnh hưởng tới siêu phẳng.\n"
                  "2. 0 < α_i < C: Điểm x_i nằm chính xác trên biên lề (y_i(w^T x_i + b) = 1, ξ_i = 0). Đây là các Vector Hỗ trợ (Support Vectors) mấu chốt quyết định vị trí siêu phẳng.\n"
                  "3. α_i = C: Điểm x_i nằm trong lề hoặc bị phân loại sai (ξ_i > 0).")

    add_body_p(doc, "Trong thư viện `LinearSVC` (dựa trên giải thuật LIBLINEAR chuyên dụng cho bài toán tuyến tính số chiều lớn), mô hình sử dụng hàm mất mát bình phương bản lề Squared Hinge Loss: L₂(z) = [max(0, 1 - z)]². Hàm này khả vi liên tục bậc nhất, cho phép giải thuật hạ dốc tọa độ (Coordinate Descent) cập nhật nghiệm từng chiều một cách đóng kín (Closed-form update) với tốc độ hội tụ siêu nhanh, vượt trội hoàn toàn so với việc giải bài toán đối ngẫu bậc hai thông thường.")

    # -------------------------------------------------------------
    # 2.6. CƠ SỞ TOÁN HỌC RỪNG NGẪU NHIÊN - RANDOM FOREST
    # -------------------------------------------------------------
    add_heading_2(doc, "2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên (Random Forest)")
    add_body_p(doc, "Rừng ngẫu nhiên (Random Forest - RF) do Leo Breiman đề xuất là phương pháp học kết hợp (Ensemble Learning) hoạt động dựa trên nguyên lý Đóng bao (Bootstrap Aggregating - Bagging). Mô hình xây dựng một tập hợp gồm B cây quyết định độc lập {T_1, T_2, ..., T_B}.")

    add_body_p(doc, "Tại mỗi nút phân nhánh của cây quyết định, giải thuật tìm kiếm điểm chia cắt tối ưu dựa trên độ đo vẩn đục Gini Impurity:")
    add_math_block(doc, "Gini(m) = 1 - ∑_{k=1}^K p_{mk}²", "2.27")
    add_body_p(doc, "Trong đó p_{mk} là tỷ lệ các mẫu thuộc lớp k tại nút m. Mức giảm độ vẩn đục (Gini Gain) khi chia nút m thành hai nút con m_L và m_R được tối đa hóa:")
    add_math_block(doc, "ΔGini = Gini(m) - (N_L / N_m) Gini(m_L) - (N_R / N_m) Gini(m_R)", "2.28")

    add_body_p(doc, "Nguyên lý giảm phương sai của Bagging: Giả sử ta có B cây quyết định dự đoán f̂_b(x) với phương sai mỗi cây là σ² và hệ số tương quan cặp giữa các cây là ρ. Phương sai của mô hình trung bình kết hợp f̄(x) = (1/B) ∑_{b=1}^B f̂_b(x) là:")
    add_math_block(doc, "Var(f̄(x)) = ρ σ² + [ (1 - ρ) / B ] σ²", "2.29")
    add_body_p(doc, "Khi số lượng cây B tăng lên rất lớn (B -> ∞), số hạng thứ hai triệt tiêu về 0, và phương sai của rừng chỉ phụ thuộc vào số hạng ρσ². Để giảm thiểu hệ số tương quan ρ giữa các cây, Random Forest áp dụng hai cơ chế ngẫu nhiên hóa kép:\n"
                  "• Lấy mẫu có hoàn lại (Bootstrap Sampling): Mỗi cây được huấn luyện trên một tập con dữ liệu ngẫu nhiên gồm N mẫu chọn có hoàn lại từ tập huấn luyện gốc. Khoảng 36.8% mẫu không bao giờ được chọn vào tập huấn luyện của cây (gọi là tập Out-of-Bag - OOB), được dùng để đánh giá sai số nội tại không thiên lệch.\n"
                  "• Lấy mẫu ngẫu nhiên không gian đặc trưng (Feature Subsampling): Tại mỗi bước phân nhánh, thay vì xét toàn bộ d đặc trưng, cây chỉ chọn ngẫu nhiên m = √d đặc trưng để tìm điểm chia cắt tốt nhất.")

    add_body_p(doc, "Tại sao Random Forest bị giảm hiệu năng trên dữ liệu văn bản thưa? Trong không gian văn bản d = 24.619 chiều, phần lớn các chiều đặc trưng chứa giá trị 0 (độ thưa > 99%). Khi lấy ngẫu nhiên m = √24.619 ≈ 157 đặc trưng tại mỗi nút, xác suất rất cao là cả 157 đặc trưng này đều mang giá trị 0 trên mẫu dữ liệu đang xét, dẫn tới việc cây phân nhánh dựa trên các đặc trưng không mang thông tin, làm suy giảm hiệu năng tổng thể của mô hình so với các mô hình tuyến tính.")

    # -------------------------------------------------------------
    # 2.7. PHƯƠNG PHÁP LUẬN JOINT ABSA
    # -------------------------------------------------------------
    add_heading_2(doc, "2.7. Phương pháp luận Phân tích quan điểm theo khía cạnh (Joint ABSA)")
    add_body_p(doc, "Một đóng góp sáng tạo then chốt của đồ án là xây dựng hệ sinh thái Phân tích quan điểm đa diện kết hợp (Joint Aspect-Based Sentiment Analysis). Thay vì chỉ phân loại cảm xúc tổng quát, mô hình thực hiện giải quyết đồng thời bài toán dự đoán cảm xúc y_{sent} ∈ {Tích cực, Tiêu cực} và phân loại khía cạnh nghiệp vụ y_{asp} ∈ {7 khía cạnh tiêu chuẩn}.")

    add_body_p(doc, "7 khía cạnh nghiệp vụ được chuẩn hóa dựa trên bộ tiêu chuẩn công nghiệp quốc tế ISO/IEC 25010 về Chất lượng sản phẩm phần mềm:\n"
                  "1. `Hieu_nang_UI_UX`: Tốc độ tải, độ mượt mà giao diện, tính dễ sử dụng, độ phản hồi nút bấm.\n"
                  "2. `Dich_vu_Va_CSKH`: Chất lượng hỗ trợ giải đáp khiếu nại của nhân viên tổng đài, thái độ phục vụ.\n"
                  "3. `Bao_mat_Va_Tai_khoan`: Vấn đề đăng nhập, xác thực sinh trắc học khuôn mặt CCCD, mã OTP, khóa/mở tài khoản.\n"
                  "4. `Giao_dich_Thanh_toan_Gia_ca`: Tính năng chuyển khoản, nạp/rút tiền, cước phí giao dịch, biến động số dư.\n"
                  "5. `Van_chuyen_Giao_nhan`: Tốc độ giao đồ ăn/hàng hóa, thái độ tài xế shipper, hủy đơn, đồ ăn nguội.\n"
                  "6. `Chuong_trinh_Khuyen_mai`: Mã giảm giá, voucher freeship, tích lũy điểm thưởng, chương trình quà tặng.\n"
                  "7. `Tinh_nang_Noi_dung`: Chất lượng nội dung video (TikTok), thuật toán gợi ý, công cụ sáng tạo nội dung.")

    add_body_p(doc, "Kiến trúc Joint ABSA hoạt động dưới dạng hai bộ phân loại LinearSVC độc lập được huấn luyện song song trên cùng một không gian biểu diễn đặc trưng vector TF-IDF x_d:")
    add_math_block(doc, "ŷ_{sent} = sign( w_{sent}^T x_d + b_{sent} )", "2.30")
    add_math_block(doc, "ŷ_{asp} = argmax_{k ∈ {1,...,7}} ( w_{asp, k}^T x_d + b_{asp, k} )", "2.31")
    add_body_p(doc, "Cơ chế song song hóa này đảm bảo thời gian suy luận (Inference Latency) cho cả hai nhiệm vụ chỉ tốn chưa đầy 0.3 ms trên mỗi mẫu văn bản.")

    # -------------------------------------------------------------
    # 2.8. HỆ THỐNG ĐỘ ĐO ĐÁNH GIÁ HIỆU NĂNG MÔ HÌNH
    # -------------------------------------------------------------
    add_heading_2(doc, "2.8. Các độ đo đánh giá hiệu năng mô hình (Evaluation Metrics)")
    add_body_p(doc, "Để đánh giá toàn diện và khách quan hiệu năng của các mô hình trên tập kiểm thử độc lập (Test Set), nhóm sử dụng Ma trận nhầm lẫn (Confusion Matrix) và 4 độ đo chuẩn mực quốc tế:")

    add_body_p(doc, "1. Độ chính xác tổng thể (Accuracy): Tỷ lệ các mẫu được dự đoán đúng trên tổng số mẫu kiểm thử:")
    add_math_block(doc, "Accuracy = (TP + TN) / (TP + TN + FP + FN)", "2.32")

    add_body_p(doc, "2. Độ chuẩn xác (Precision): Đo lường trong số các mẫu được mô hình dự đoán là Tích cực, có bao nhiêu mẫu thực sự là Tích cực:")
    add_math_block(doc, "Precision = TP / (TP + FP)", "2.33")

    add_body_p(doc, "3. Độ bao phủ (Recall / Sensitivity): Đo lường trong số toàn bộ các mẫu thực tế là Tích cực, mô hình đã tìm ra được bao nhiêu mẫu:")
    add_math_block(doc, "Recall = TP / (TP + FN)", "2.34")

    add_body_p(doc, "4. Điểm F1 trung bình điều hòa (F1-Score): Trung bình điều hòa giữa Precision và Recall, phản ánh sự cân bằng giữa hai mục tiêu:")
    add_math_block(doc, "F1 = 2 · (Precision · Recall) / (Precision + Recall)", "2.35")

    add_body_p(doc, "Tại sao Macro F1 là tiêu chuẩn vàng trên dữ liệu mất cân bằng? Trong thực tế dữ liệu đánh giá ứng dụng di động, số lượng mẫu Tiêu cực và Tích cực thường chênh lệch nhau đáng kể (phản hồi tiêu cực chiếm đa số khi app bị lỗi). Điểm Accuracy thông thường có thể tạo ra ảo tưởng về hiệu năng cao khi mô hình chỉ cần đoán nhãn đa số. Nhóm ưu tiên sử dụng Macro-averaged F1 - tính toán điểm F1 độc lập cho từng lớp rồi lấy trung bình số học không trọng số:")
    add_math_block(doc, "Macro F1 = (1 / |C|) ∑_{c ∈ C} F1_c", "2.36")
    add_body_p(doc, "Macro F1 coi trọng bình đẳng tất cả các lớp, bắt buộc mô hình phải học tốt cả lớp chiếm số lượng ít lẫn lớp chiếm số lượng nhiều, đảm bảo tính công bằng và tin cậy tuyệt đối trong việc xếp hạng các thuật toán.")

    
    # -------------------------------------------------------------
    # 2.9. PHÂN TÍCH TOÁN HỌC KHÔNG GIAN HILBERT VÀ LỌC ĐẶC TRƯNG
    # -------------------------------------------------------------
    add_heading_2(doc, "2.9. Phân tích toán học chuyên sâu về Không gian đặc trưng Hilbert và Giảm chiều")
    add_body_p(doc, "Trong bài toán xử lý ngôn ngữ tự nhiên, không gian vector từ vựng ban đầu V chứa toàn bộ các từ ghép đơn và đôi xuất hiện trong tập huấn luyện. Với kích thước ban đầu lên tới hơn 45.000 cụm từ, ma trận dữ liệu chứa rất nhiều nhiễu do các từ hiếm (xuất hiện 1 lần do gõ sai chính tả) hoặc các từ quá phổ biến (xuất hiện ở hầu hết mọi câu). Nhóm áp dụng kỹ thuật lọc tần suất biên:")
    add_math_block(doc, "V_{lọc} = { t ∈ V | min_df ≤ df(t) ≤ max_df × |D| }", "2.37")
    add_body_p(doc, "Trong đó: min_df = 2 loại bỏ toàn bộ các từ đơn lẻ chỉ xuất hiện duy nhất 1 lần (Outlier / Typo), và max_df = 0.9 loại bỏ các từ dừng xuất hiện trong hơn 90% số văn bản. Kỹ thuật này đã giảm số chiều đặc trưng từ 45.210 xuống còn đúng d = 24.619 chiều, đồng thời nâng cao mật độ thông tin hữu ích của ma trận biểu diễn CSR.")

    # -------------------------------------------------------------
    # 2.10. CƠ SỞ ĐẠI SỐ TUYẾN TÍNH CỦA SIÊU PHẲNG PHÂN TÁCH SVM
    # -------------------------------------------------------------
    add_heading_2(doc, "2.10. Cơ sở đại số tuyến tính của Phân tách siêu phẳng trong SVM")
    add_body_p(doc, "Để hiểu rõ tại sao LinearSVC đạt hiệu năng áp đảo, ta phân tích hình học không gian Hilbert R^d với d = 24.619. Cho tập điểm dữ liệu D = {(x_i, y_i)}_{i=1}^N với y_i ∈ {-1, +1}. Siêu phẳng phân cách được định nghĩa bởi phương trình:")
    add_math_block(doc, "H = { x ∈ R^d | w^T x + b = 0 }", "2.38")
    add_body_p(doc, "Vecto pháp tuyến w vuông góc với siêu phẳng H và quyết định hướng phân tách. Khoảng cách vuông góc từ điểm x_i bất kỳ tới siêu phẳng H là:")
    add_math_block(doc, "γ_i = [ y_i (w^T x_i + b) ] / ||w||₂", "2.39")
    add_body_p(doc, "Khoảng cách lề hình học (Geometric Margin) của toàn bộ tập dữ liệu là khoảng cách từ siêu phẳng tới điểm dữ liệu gần nó nhất: γ = min_i γ_i. Để siêu phẳng nằm chính xác ở vị trí cân bằng và cách xa hai lớp nhất, bài toán tối ưu hóa lề cực đại yêu cầu cực đại hóa γ:")
    add_math_block(doc, "max_{w, b} γ  thỏa mãn: [ y_i (w^T x_i + b) ] / ||w||₂ ≥ γ,  ∀i = 1, ..., N", "2.40")
    add_body_p(doc, "Bằng cách chuẩn hóa thang đo lề hàm số (Functional Margin) sao cho min_i y_i (w^T x_i + b) = 1, bài toán trên tương đương với:")
    add_math_block(doc, "max_{w, b} (1 / ||w||₂)  <=>  min_{w, b} (1/2) ||w||₂²   thỏa mãn: y_i (w^T x_i + b) ≥ 1,  ∀i = 1, ..., N", "2.41")

    add_body_p(doc, "Khi tồn tại nhiễu hoặc dữ liệu không thể phân tách tuyến tính hoàn hảo (Linearly Inseparable), việc đưa vào các biến bù trượt sai số ξ_i ≥ 0 (Slack Variables) dẫn tới bài toán tối ưu hóa biên mềm Soft-Margin SVM. Tại nghiệm tối ưu, theo điều kiện KKT (Karush-Kuhn-Tucker), các điểm dữ liệu được phân thành 3 nhóm rõ rệt:\n"
                  "1. Điểm nằm ngoài khoảng lề (Non-Support Vectors): y_i (w^T x_i + b) > 1 => α_i = 0. Các điểm này không đóng góp vào vector trọng số w và không ảnh hưởng tới vị trí siêu phẳng.\n"
                  "2. Điểm nằm đúng trên biên lề (Margin Support Vectors): y_i (w^T x_i + b) = 1 và ξ_i = 0 => 0 < α_i < C. Đây là các điểm mấu chốt quyết định chính xác vị trí siêu phẳng phân tách.\n"
                  "3. Điểm nằm trong khoảng lề hoặc bị phân loại sai (Non-margin Support Vectors): y_i (w^T x_i + b) < 1 và ξ_i > 0 => α_i = C. Đây là các mẫu khó hoặc mẫu nhiễu được kiểm soát bởi siêu tham số phạt C.")

    # -------------------------------------------------------------
    # 2.11. SO SÁNH GIỮA HINGE LOSS VÀ SQUARED HINGE LOSS
    # -------------------------------------------------------------
    add_heading_2(doc, "2.11. So sánh lý thuyết giữa hàm Hinge Loss và Squared Hinge Loss")
    add_body_p(doc, "Trong bài toán SVM chuẩn, hàm mất mát bản lề Hinge Loss cổ điển có dạng L_1(z) = max(0, 1 - z). Tuy nhiên, hàm L_1 không có đạo hàm tại điểm z = 1 (điểm gập), đòi hỏi phải sử dụng các giải thuật tối ưu dưới đạo hàm (Subgradient Optimization) có tốc độ hội tụ chậm.")
    add_body_p(doc, "Trong thư viện LinearSVC của Scikit-learn (dựa trên LIBLINEAR), hàm mất mát bình phương bản lề Squared Hinge Loss L_2(z) = [max(0, 1 - z)]² được sử dụng. Hàm L_2(z) khả vi liên tục bậc nhất trên toàn bộ miền xác định với đạo hàm:")
    add_math_block(doc, "L'_2(z) = -2 (1 - z)  khi z < 1;  ngược lại bằng 0", "2.42")
    add_body_p(doc, "Tính chất khả vi liên tục này cho phép giải thuật hạ dốc tọa độ (Coordinate Descent) cập nhật từng biến trọng số w_j một cách đóng kín (Closed-form update) cực kỳ nhanh chóng, giúp LinearSVC huấn luyện toàn bộ 10.437 mẫu trên 24.619 chiều chỉ trong 0.0577 giây, nhanh gấp 3 lần so với Logistic Regression và nhanh gấp 11 lần so với Random Forest.")

    doc.add_page_break()
