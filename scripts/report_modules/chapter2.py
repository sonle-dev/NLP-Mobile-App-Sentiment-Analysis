# -*- coding: utf-8 -*-
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
    
    add_heading_2(doc, "2.1. Quy trình Tiền xử lý dữ liệu văn bản tiếng Việt đa tầng")
    add_body_p(doc, "Chất lượng của dữ liệu đầu vào quyết định trực tiếp giới hạn trên (Upper bound) về độ chính xác của mọi mô hình học máy theo nguyên lý 'Garbage In, Garbage Out'. Nhóm 12 đã thiết kế một pipeline tiền xử lý dữ liệu khép kín gồm 6 công đoạn nghiêm ngặt:")

    add_heading_3(doc, "2.1.1. Chuẩn hóa mã ký tự Unicode và Ẩn danh thông tin cá nhân (PII)")
    add_body_p(doc, "Trong môi trường tiếng Việt, tồn tại hai bảng mã Unicode song song: Unicode Dựng sẵn (NFC - Precomposed) và Unicode Tổ hợp (NFD - Decomposed). Cùng một từ 'tiền', ở dạng dựng sẵn là 1 ký tự duy nhất, nhưng ở dạng tổ hợp là sự kết hợp của ký tự gốc 'e' và các dấu thanh rời rạc. Nếu không quy chuẩn, thuật toán sẽ coi đây là hai từ hoàn toàn khác nhau. Nhóm sử dụng thư viện `unicodedata` để ép toàn bộ văn bản về chuẩn NFC.")
    add_body_p(doc, "Đồng thời, nhằm tuân thủ nghiêm ngặt các quy định về bảo vệ quyền riêng tư người dùng (Personally Identifiable Information - PII), toàn bộ các thông tin nhạy cảm như tên người dùng, số điện thoại (ví dụ: '0912345678' -> '<SDT>'), số tài khoản ngân hàng, liên kết URL và địa chỉ email đều được lọc và ẩn danh hoàn toàn thông qua các biểu thức chính quy (Regular Expressions).")

    add_heading_3(doc, "2.1.2. Xây dựng từ điển Teencode và Chuẩn hóa từ lóng công nghệ")
    add_body_p(doc, "Nhóm đã biên soạn một từ điển quy chuẩn gồm hơn 50 quy tắc teencode và tiếng lóng công nghệ / tài chính phổ biến nhất trên các kho ứng dụng di động tại Việt Nam:")

    # Table 2.1 Teencode dictionary
    t_slang = doc.add_table(rows=11, cols=4)
    t_slang.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_slang.autofit = False
    hdrs_sl = ["Nhóm ngôn ngữ", "Từ lóng / Teencode gốc", "Dạng chuẩn hóa tiếng Việt", "Mục đích ngữ nghĩa"]
    w_sl = [Inches(1.5), Inches(1.8), Inches(1.8), Inches(1.4)]
    for j, h in enumerate(hdrs_sl):
        c = t_slang.rows[0].cells[j]
        c.width = w_sl[j]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 70, 70, 50, 50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_sl = [
        ("Phủ định", "ko, k, hok, hem, hong, koo", "không", "Khôi phục từ phủ định chuẩn xác"),
        ("Được / Khả năng", "dc, đc, dcc, dk, dx", "được", "Đồng nhất từ chỉ sự thành công"),
        ("Giao dịch ngân hàng", "ck, chuyen khoan, bank, ckhoan", "chuyển khoản", "Quy về khái niệm thanh toán cốt lõi"),
        ("Tài khoản", "tk, acc, acount, tkk", "tài khoản", "Đồng nhất thực thể định danh"),
        ("Ứng dụng", "app, ứng dụngg, ap, phần mềm", "ứng dụng", "Chuẩn hóa danh từ đối tượng"),
        ("Chê bai cực đoan", "nhu cc, nhu cl, nhu hach, app lo", "rất tệ hại", "Làm rõ sắc thái tiêu cực mạnh"),
        ("Lỗi kỹ thuật", "lag, giật lag, laggg, đơ, treo", "giật lag đơ máy", "Nhận diện khía cạnh hiệu năng"),
        ("Giao vận chuyển", "shipper, ship, xíp, ship hàng", "giao hàng", "Nhận diện khía cạnh vận chuyển"),
        ("Căn cước công dân", "cccd, cmnd, can cuoc, định danh", "căn cước công dân", "Nhận diện khía cạnh bảo mật"),
        ("Thời gian trễ", "delay, tre gio, cham tre, ngam gio", "chậm trễ", "Khôi phục sắc thái phàn nàn thời gian")
    ]

    for i, row in enumerate(data_sl):
        r_el = t_slang.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_sl[j]
            set_cell_margins(c, 50, 50, 50, 50)
            if i % 2 == 1:
                set_cell_background(c, "F9FBFD")
            p = c.paragraphs[0]
            if j == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(val)
                r.font.bold = True
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)

    add_body_p(doc, "\nBảng 2.1: Bảng đối chiếu các nhóm quy tắc Teencode và từ lóng công nghệ được chuẩn hóa")

    add_heading_3(doc, "2.1.3. Thuật toán phân tách từ ghép tiếng Việt (Word Segmentation)")
    add_body_p(doc, "Khác với tiếng Anh nơi các từ đơn được phân cách rõ ràng bằng dấu cách, tiếng Việt sử dụng từ ghép đa âm tiết làm đơn vị ngữ nghĩa cơ bản. Nhóm tích hợp công cụ xử lý ngôn ngữ tự nhiên `underthesea` áp dụng mô hình Trường ngẫu nhiên có điều kiện (Conditional Random Fields - CRF) kết hợp thuật toán Viterbi để xác định ranh giới từ ghép chính xác. Các âm tiết thuộc cùng một từ được liên kết bằng dấu gạch dưới (ví dụ: 'chuyển_tiền_nhanh', 'nhân_viên_thân_thiện', 'lỗi_kết_nối', 'quét_mã_qr').")

    add_heading_2(doc, "2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm (Chương 2 GT Học máy ICTU)")
    add_body_p(doc, "Theo Chương 2 (Các kỹ thuật xây dựng đặc trưng, Mục 2.3 và 2.4, tr. 40 - 58) của Giáo trình Học máy ICTU, mô hình học máy chỉ có thể tiếp nhận đầu vào là các vector số học trong không gian nhiều chiều. Kỹ thuật TF-IDF (Term Frequency - Inverse Document Frequency) là phương pháp gán trọng số cho từng từ ghép phản ánh chính xác mức độ quan trọng của từ đó trong văn bản.")

    add_heading_3(doc, "2.2.1. Tần suất từ (Term Frequency - TF) và Sublinear TF Scaling")
    add_body_p(doc, "Tần suất xuất hiện thô của từ ghép t trong văn bản d được định nghĩa:")
    add_math_block(doc, "TF_{raw}(t, d) = f(t, d) / ∑_{t' ∈ d} f(t', d)", "2.1")
    add_body_p(doc, "Tuy nhiên, trong các đánh giá bức xúc của người dùng, một từ chê bai như 'lỗi' có thể xuất hiện lặp lại 10 lần, nhưng mức độ tiêu cực của văn bản đó không tăng gấp 10 lần so với văn bản xuất hiện 1 lần. Do đó, nhóm áp dụng kỹ thuật nén phi tuyến Sublinear TF Scaling (Mục 2.3, tr. 48):")
    add_math_block(doc, "TF_{sublinear}(t, d) = 1 + log(TF_{raw}(t, d))  khi TF > 0;  ngược lại bằng 0", "2.2")

    add_heading_3(doc, "2.2.2. Nghịch đảo tần suất văn bản (Inverse Document Frequency - IDF)")
    add_body_p(doc, "Để giảm bớt tầm quan trọng của các từ xuất hiện phổ biến trong hầu hết mọi văn bản (như 'ứng dụng', 'này', 'là') và tăng trọng số cho các từ mang tính phân biệt cao (như 'treo_tiền', 'mượt_mà', 'trừ_phí_vô_lý'), giá trị IDF được tính theo công thức mượt (Smooth IDF):")
    add_math_block(doc, "IDF(t, D) = log [ (1 + |D|) / (1 + df(t)) ] + 1", "2.3")
    add_body_p(doc, "Trong đó: |D| là tổng số văn bản trong tập huấn luyện (10.437 mẫu), và df(t) là số lượng văn bản có chứa từ ghép t.")

    add_heading_3(doc, "2.2.3. Khai thác n-gram (1, 2) và Chuẩn hóa Euclidean L2-norm")
    add_body_p(doc, "Nhóm kết hợp Unigrams (từ đơn) và Bigrams (cặp hai từ đi liền kề). Việc bổ sung Bigrams có ý nghĩa sống còn trong NLP tiếng Việt để bảo toàn các cấu trúc đảo nghĩa hoặc bổ nghĩa, ví dụ: 'không_thể_chuyển_tiền', 'rất_hài_lòng', 'quá_chậm'.")
    add_body_p(doc, "Theo Mục 2.4 (Chuẩn hóa vector đặc trưng, tr. 54), vector đặc trưng x_i sau khi tính toán TF-IDF được chuẩn hóa theo chuẩn Euclidean L2-norm:")
    add_math_block(doc, "x_{norm} = x / ||x||₂ = x / √(∑_{j=1}^d x_j²)", "2.4")
    add_body_p(doc, "Chuẩn hóa L2-norm đảm bảo rằng mọi vector biểu diễn văn bản đều nằm trên mặt cầu đơn vị trong không gian R^d, triệt tiêu hoàn toàn sự sai lệch do độ dài văn bản ngắn (2 từ) hay dài (hàng trăm từ).")

    add_heading_2(doc, "2.3. Cơ sở toán học Bộ phân loại Naive Bayes (Chương 6 GT Học máy ICTU)")
    add_body_p(doc, "Multinomial Naive Bayes (MNB) được trình bày chi tiết tại Chương 6 (Bộ phân loại Naive Bayes, tr. 104 - 118) của Giáo trình Học máy. Đây là mô hình phân loại dựa trên xác suất hậu nghiệm (Posterior Probability) kết hợp định lý Bayes:")
    add_math_block(doc, "P(y | x) = [ P(y) × P(x | y) ] / P(x)", "2.5")
    
    add_body_p(doc, "Giả định cốt lõi của Naive Bayes: Các đặc trưng từ x_1, x_2, ..., x_d độc lập có điều kiện với nhau khi biết trước nhãn lớp y. Do đó:")
    add_math_block(doc, "P(x | y) = ∏_{j=1}^d P(x_j | y)", "2.6")

    add_body_p(doc, "Ước lượng tham số hợp lý cực đại (MLE) kết hợp tiền nghiệm Dirichlet (Laplace Smoothing) với hệ số α = 0.5 nhằm tránh xác suất bằng 0 khi gặp từ vựng mới:")
    add_math_block(doc, "P(w_j | y) = [ N_{y, j} + α ] / [ N_y + α × |V| ]", "2.7")

    add_body_p(doc, "Quy tắc quyết định tối ưu Bayes (Bayes Decision Rule) trong không gian log-likelihood:")
    add_math_block(doc, "ŷ = argmax_{y ∈ {0, 1}} [ log P(y) + ∑_{j=1}^d x_j log P(w_j | y) ]", "2.8")

    add_heading_2(doc, "2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2 (Chương 9 GT Học máy ICTU)")
    add_body_p(doc, "Chương 9 (Hồi quy Logistic, tr. 154 - 169) trình bày mô hình phân loại nhị phân dựa trên hàm kích hoạt Sigmoid:")
    add_math_block(doc, "P(y = 1 | x; w, b) = σ(w^T x + b) = 1 / [ 1 + e^{-(w^T x + b)} ]", "2.9")
    add_math_block(doc, "P(y = 0 | x; w, b) = 1 - σ(w^T x + b) = e^{-(w^T x + b)} / [ 1 + e^{-(w^T x + b)} ]", "2.10")

    add_body_p(doc, "Hàm mất mát Binary Cross-Entropy (Negative Log-Likelihood) kết hợp số hạng điều chuẩn L2 (Weight Decay):")
    add_math_block(doc, "J(w, b) = - (1/N) ∑_{i=1}^N [ y_i log σ(w^T x_i + b) + (1 - y_i) log(1 - σ(w^T x_i + b)) ] + (1 / 2C) ||w||₂²", "2.11")

    add_body_p(doc, "Vecto Gradient của hàm mất mát đối với vector trọng số w được tính bằng:")
    add_math_block(doc, "∇_w J(w, b) = (1/N) X^T (σ(Xw + b) - y) + (1/C) w", "2.12")
    add_body_p(doc, "Ma trận Hessian đạo hàm bậc hai H = ∇²_w J(w) = (1/N) X^T D X + (1/C) I (với D là ma trận đường chéo D_ii = σ_i(1 - σ_i) > 0) luôn là ma trận nửa xác định dương, chứng minh rằng hàm mất mát là lồi nghiêm ngặt (Strictly Convex) và đảm bảo thuật toán L-BFGS luôn hội tụ tới nghiệm tối ưu toàn cục duy nhất.")

    add_heading_2(doc, "2.5. Cơ sở toán học Máy vector hỗ trợ - SVM (Chương 10 GT Học máy ICTU)")
    add_body_p(doc, "Chương 10 (Máy vector hỗ trợ - SVM, tr. 170 - 181) của Giáo trình Học máy là nền tảng lý thuyết cốt lõi của đề tài. Mục tiêu của SVM là tìm một siêu phẳng phân tách tuyến tính w^T x + b = 0 sao cho khoảng cách lề hình học (Geometric Margin) giữa hai lớp là lớn nhất.")

    add_body_p(doc, "Bài toán tối ưu hóa biên mềm (Soft-Margin SVM) dạng gốc (Primal Formulation):")
    add_math_block(doc, "min_{w, b, ξ}  (1/2) ||w||₂² + C ∑_{i=1}^N ξ_i", "2.13")
    add_math_block(doc, "thỏa mãn điều kiện: y_i (w^T x_i + b) ≥ 1 - ξ_i,  với ξ_i ≥ 0,  ∀i = 1, ..., N", "2.14")

    add_body_p(doc, "Thiết lập hàm Lagrange với các nhân tử Lagrange α_i ≥ 0 và r_i ≥ 0:")
    add_math_block(doc, "L(w, b, ξ, α, r) = (1/2) ||w||₂² + C ∑ ξ_i - ∑ α_i [ y_i (w^T x_i + b) - 1 + ξ_i ] - ∑ r_i ξ_i", "2.15")

    add_body_p(doc, "Các điều kiện Karush-Kuhn-Tucker (KKT) tại điểm tối ưu:\n"
                  "1. Đạo hàm theo w triệt tiêu: ∂L/∂w = w - ∑ α_i y_i x_i = 0  =>  w = ∑_{i=1}^N α_i y_i x_i\n"
                  "2. Đạo hàm theo b triệt tiêu: ∂L/∂b = - ∑ α_i y_i = 0\n"
                  "3. Đạo hàm theo ξ_i: C - α_i - r_i = 0  =>  0 ≤ α_i ≤ C\n"
                  "4. Điều kiện bù trượt (Complementary Slackness): α_i [ y_i (w^T x_i + b) - 1 + ξ_i ] = 0 và r_i ξ_i = 0")

    add_body_p(doc, "Bài toán đối ngẫu Lagrange (Dual Problem) tương đương:")
    add_math_block(doc, "max_{α}  ∑_{i=1}^N α_i - (1/2) ∑_{i=1}^N ∑_{j=1}^N α_i α_j y_i y_j x_i^T x_j   s.t. 0 ≤ α_i ≤ C và ∑ α_i y_i = 0", "2.16")

    add_body_p(doc, "Trong LinearSVC, hàm mất mát bình phương bản lề (Squared Hinge Loss) được áp dụng trực tiếp:")
    add_math_block(doc, "min_{w}  (1/2) ||w||₂² + C ∑_{i=1}^N [ max(0, 1 - y_i (w^T x_i + b)) ]²", "2.17")
    add_body_p(doc, "Hàm mục tiêu này khả vi liên tục bậc nhất, cho phép giải thuật hạ dốc tọa độ kép (Dual Coordinate Descent) trong LIBLINEAR hội tụ với độ phức tạp thời gian O(N × d) tuyến tính theo số mẫu và số chiều đặc trưng, hoàn toàn vượt trội so với các thuật toán QP bậc ba O(N³).")

    add_heading_2(doc, "2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên - Random Forest (Chương 8 & 14 GT Học máy ICTU)")
    add_body_p(doc, "Được trình bày tại Chương 8 (Cây quyết định, tr. 132 - 153) và Chương 14 (Dự án học máy tiêu biểu, tr. 248 - 254), Rừng ngẫu nhiên (Random Forest) là thuật toán học kết hợp (Ensemble Learning) dựa trên kỹ thuật đóng bao (Bagging - Bootstrap Aggregating).")

    add_body_p(doc, "Tiêu chí phân chia nút dựa trên độ vẩn đục Gini Impurity (Gini Index):")
    add_math_block(doc, "Gini(D) = 1 - ∑_{c=0}^1 p_c²", "2.18")
    add_body_p(doc, "Độ lợi thông tin (Information Gain) khi phân chia tập D thành D_L và D_R theo thuộc tính j và ngưỡng θ:")
    add_math_block(doc, "ΔGini(D, j, θ) = Gini(D) - ( |D_L|/|D| × Gini(D_L) + |D_R|/|D| × Gini(D_R) )", "2.19")

    add_heading_2(doc, "2.7. Phương pháp luận Phân tích quan điểm theo khía cạnh (Joint ABSA)")
    add_body_p(doc, "Nhóm xây dựng kiến trúc phân loại song hành đa nhiệm. Thay vì chỉ đưa ra nhãn nhị phân, hệ thống tiếp nhận văn bản d_i và ánh xạ đồng thời vào hai không gian đích: y_i^(sent) ∈ {0, 1} và y_i^(asp) ∈ {A_1, A_2, ..., A_7}. Cả hai mô hình đều chia sẻ chung một không gian biểu diễn đặc trưng TF-IDF chuẩn hóa, giúp tối ưu hóa bộ nhớ và thời gian tính toán.")

    add_heading_2(doc, "2.8. Các độ đo đánh giá hiệu năng mô hình (Evaluation Metrics)")
    add_body_p(doc, "Các công thức đo lường chuẩn mực gồm:")
    add_math_block(doc, "Accuracy = (TP + TN) / (TP + TN + FP + FN)", "2.20")
    add_math_block(doc, "Precision = TP / (TP + FP),    Recall = TP / (TP + FN)", "2.21")
    add_math_block(doc, "F1_{class} = 2 × (Precision × Recall) / (Precision + Recall)", "2.22")
    add_math_block(doc, "Macro F1 = (1/K) ∑_{k=1}^K F1_k,    Weighted F1 = ∑_{k=1}^K (N_k / N) × F1_k", "2.23")

    doc.add_page_break()
    return doc
