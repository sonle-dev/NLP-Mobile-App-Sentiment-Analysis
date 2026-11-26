# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from .helpers import (
    add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_math_block, add_callout,
    add_image_with_caption, set_cell_background, set_cell_margins
)

def add_chapter1(doc):
    add_heading_1(doc, "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN BÀI TOÁN")
    
    add_heading_2(doc, "1.1. Khái quát về Học máy và Xử lý ngôn ngữ tự nhiên (NLP)")
    add_heading_3(doc, "1.1.1. Khái niệm và phân loại các phương pháp học máy")
    add_body_p(doc, "Theo Giáo trình Học máy (Trần Quang Quý, Ngô Hữu Huy, Nguyễn Đức Bình, Nguyễn Tuấn Anh - Trường Đại học Công nghệ Thông tin và Truyền thông, NXB ĐHTN 2026, Chương 1, tr. 11), Học máy (Machine Learning) là một lĩnh vực khoa học nghiên cứu việc thiết kế và phát triển các hệ thống máy tính có khả năng tự động học từ dữ liệu. Thay vì phải lập trình tường minh toàn bộ các quy tắc xử lý thủ công, cách tiếp cận này cho phép hệ thống tự động suy luận và hình thành các mô hình cũng như quy luật dựa trên việc phân tích dữ liệu quan sát được theo thời gian.")
    
    add_body_p(doc, "Hay theo định nghĩa mang tính kỹ thuật của Tom Mitchell (1997): Một chương trình máy tính được cho là học từ kinh nghiệm E đối với một lớp nhiệm vụ T và thước đo hiệu năng P, nếu hiệu năng của nó đối với các nhiệm vụ trong T, được đo bởi P, được cải thiện cùng với kinh nghiệm E. Trong bài toán phân loại quan điểm phản hồi người dùng di động, kinh nghiệm E là tập dữ liệu phản hồi đã được gán nhãn, nhiệm vụ T là phân loại nhãn cảm xúc và nhãn khía cạnh, và thước đo P là độ chính xác tổng quát và chỉ số cân bằng Macro F1-score.")

    add_body_p(doc, "Căn cứ theo bản chất của tập dữ liệu huấn luyện và cơ chế phản hồi từ môi trường, các thuật toán học máy được chia thành 4 nhóm chính:")
    add_body_p(doc, "1. Học có giám sát (Supervised Learning): Tập dữ liệu huấn luyện bao gồm các cặp dữ liệu vào x và nhãn mục tiêu y tương ứng: D = {(x_i, y_i)}_{i=1}^N. Mục tiêu là học một ánh xạ hàm f: X -> Y sao cho cực tiểu hóa sai số kỳ vọng giữa giá trị dự đoán f(x) và nhãn thực tế y. Đây là nhóm thuật toán chủ đạo áp dụng trong đề tài phân tích quan điểm phản hồi người dùng.")
    add_body_p(doc, "2. Học không giám sát (Unsupervised Learning): Tập dữ liệu chỉ bao gồm các mẫu đầu vào x_i mà không có nhãn giám sát. Thuật toán tự động tìm kiếm các cấu trúc ẩn, gom cụm (Clustering như K-means) hoặc giảm chiều dữ liệu (PCA).")
    add_body_p(doc, "3. Học bán giám sát (Semi-supervised Learning): Kết hợp một lượng nhỏ dữ liệu đã được gán nhãn với một lượng lớn dữ liệu chưa gán nhãn nhằm tối ưu hóa chi phí thu thập và gán nhãn thủ công.")
    add_body_p(doc, "4. Học tăng cường (Reinforcement Learning): Mô hình (Agent) tương tác trực tiếp với môi trường thông qua các hành động, nhận về phần thưởng (Reward) hoặc hình phạt để học chính sách hành động tối ưu.")

    add_heading_3(doc, "1.1.2. Vị trí của Xử lý ngôn ngữ tự nhiên trong hệ thống thông tin số")
    add_body_p(doc, "Xử lý ngôn ngữ tự nhiên (NLP) là cầu nối giao tiếp then chốt giữa tư duy con người và máy tính. Khác với dữ liệu dạng bảng số học (Tabular data) có cấu trúc cố định, dữ liệu văn bản là dữ liệu phi cấu trúc, có tính đa nghĩa, phụ thuộc chặt chẽ vào ngữ cảnh văn hóa, ngữ điệu và thói quen sử dụng từ ngữ của từng vùng miền. Trong các ứng dụng di động, phản hồi của người dùng chứa đựng vô số thông tin giá trị về trải nghiệm, lỗi phần mềm, khiếu nại giao dịch và đánh giá thái độ phục vụ. Do đó, việc ứng dụng các kỹ thuật NLP hiện đại để chuẩn hóa, bóc tách và phân lớp tự động các luồng phản hồi này có ý nghĩa sống còn đối với sự phát triển bền vững của sản phẩm số.")

    add_heading_3(doc, "1.1.3. Khái niệm bài toán Phân tích quan điểm (Sentiment Analysis)")
    add_body_p(doc, "Phân tích quan điểm (Sentiment Analysis hay Opinion Mining) là bài toán tính toán ngôn ngữ nhằm xác định thái độ, cảm xúc, định kiến hoặc ý kiến đánh giá của người nói/người viết đối với một chủ thể, dịch vụ hoặc tính năng cụ thể. Về mặt toán học, bài toán phân loại quan điểm nhị phân được phát biểu dưới dạng ánh xạ từ không gian văn bản tự nhiên X vào tập nhãn nhị phân Y = {0, 1}, trong đó nhãn 0 đại diện cho quan điểm Tiêu cực (Negative / Bất mãn) và nhãn 1 đại diện cho quan điểm Tích cực (Positive / Hài lòng).")

    add_heading_3(doc, "1.1.4. So sánh đối sánh các trường phái tiếp cận trong NLP")
    add_body_p(doc, "Trong lịch sử phát triển của ngành xử lý ngôn ngữ tự nhiên, có 4 trường phái tiếp cận chủ đạo:")

    # Table 1.1 Comparative NLP approaches
    t_nlp = doc.add_table(rows=5, cols=5)
    t_nlp.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_nlp.autofit = False
    hdrs_nlp = ["Phương pháp", "Nguyên lý cốt lõi", "Ưu điểm chính", "Nhược điểm hạn chế", "Khả năng ứng dụng"]
    w_nlp = [Inches(1.2), Inches(1.6), Inches(1.4), Inches(1.5), Inches(0.8)]
    for j, h in enumerate(hdrs_nlp):
        c = t_nlp.rows[0].cells[j]
        c.width = w_nlp[j]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 70, 70, 50, 50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_nlp = [
        ("Dựa trên Từ điển (Lexicon-based)", "Tra cứu điểm số cảm xúc từ tập từ vựng định sẵn (SentiWordNet, VADER)", "Không cần huấn luyện dữ liệu, triển khai nhanh, dễ giải thích", "Bất lực trước câu phủ định kép, từ lóng mạng và câu mỉa mai châm biếm", "Thấp / Đơn giản"),
        ("Học máy cổ điển (LinearSVC, LR, MNB)", "Vector hóa TF-IDF n-gram kết hợp tối ưu hóa lề cực đại hoặc hồi quy", "Chính xác cao (>92%), tốc độ suy luận siêu tốc (<0.3µs), mô hình siêu nhẹ (~100KB)", "Cần thiết kế bộ tiền xử lý và tách từ ghép tiếng Việt chuẩn mực", "RẤT CAO (Tối ưu cho Edge & API)"),
        ("Mạng học sâu (LSTM, Bi-GRU, CNN)", "Học biểu diễn chuỗi thông qua các cổng nhớ và ma trận nhúng Word2Vec/FastText", "Nắm bắt được phụ thuộc từ vựng xa trong câu dài", "Đòi hỏi dữ liệu lớn, thời gian huấn luyện lâu, dễ bị quá khớp khi dữ liệu nhỏ", "Trung bình"),
        ("Mô hình Transformer (PhoBERT, LLM)", "Cơ chế Tự chú ý (Self-Attention) huấn luyện trước trên kho ngữ liệu khổng lồ", "Hiểu ngữ cảnh sâu sắc, xử lý xuất sắc các câu châm biếm phức tạp", "Cần GPU đắt đỏ, mô hình nặng hàng trăm MB, độ trễ cao (>50ms/mẫu)", "Cao trên Server Cloud")
    ]

    for i, row in enumerate(data_nlp):
        r_el = t_nlp.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_nlp[j]
            set_cell_margins(c, 50, 50, 50, 50)
            if i % 2 == 1:
                set_cell_background(c, "F9FBFD")
            p = c.paragraphs[0]
            if j in [0, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(val)
                r.font.bold = True
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)

    add_body_p(doc, "\nBảng 1.1: So sánh đối sánh các trường phái tiếp cận trong bài toán Phân tích quan điểm NLP")

    add_heading_2(doc, "1.2. Quy trình thực hiện dự án học máy tiêu chuẩn")
    add_body_p(doc, "Nhóm 12 triển khai đề tài bám sát hoàn toàn Quy trình 7 bước thực hiện dự án học máy tiêu chuẩn được quy định tại Mục 1.8 của Giáo trình Học máy ICTU:")

    # Detailed table for 7 steps
    t_7steps = doc.add_table(rows=8, cols=5)
    t_7steps.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_7steps.autofit = False
    hdrs_7s = ["Bước", "Tên Giai đoạn", "Đầu vào (Input)", "Hành động thực thi (Action)", "Đầu ra chuẩn (Output)"]
    w_7s = [Inches(0.6), Inches(1.5), Inches(1.4), Inches(1.8), Inches(1.2)]
    for j, h in enumerate(hdrs_7s):
        c = t_7steps.rows[0].cells[j]
        c.width = w_7s[j]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 70, 70, 50, 50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_7s = [
        ("B1", "Xác định bài toán & Thu thập dữ liệu", "Phản hồi người dùng trên Google Play & App Store", "Sử dụng công cụ cào tự động 15.541 đánh giá thô của 8 ứng dụng di động", "Tập dữ liệu thô app_reviews.csv"),
        ("B2", "Khám phá & Trực quan hóa dữ liệu EDA", "Tập dữ liệu thô 15.541 dòng", "Phân tích rating, độ dài từ, phân bố cảm xúc và khía cạnh trên biểu đồ", "Báo cáo thống kê mô tả & Báo cáo EDA"),
        ("B3", "Tiền xử lý & Xây dựng đặc trưng", "Văn bản thô, teencode, lỗi chính tả", "Chuẩn hóa Unicode, xử lý teencode, khử nhiễu nghịch nhãn, tách từ ghép underthesea, TF-IDF", "Tập dữ liệu sạch 14.910 mẫu & Ma trận TF-IDF"),
        ("B4", "Huấn luyện các mô hình phân lớp", "Ma trận TF-IDF tập Train (10.437 mẫu)", "Cài đặt và huấn luyện 4 mô hình: MultinomialNB, Logistic Regression, LinearSVC, Random Forest", "4 mô hình đã được fit tham số trọng số"),
        ("B5", "Tối ưu siêu tham số & Chọn mô hình", "Tập Train & Validation (2.236 mẫu)", "Chạy GridSearchCV 5-fold tối ưu tham số C, loss; đối chuẩn định lượng trên tập Test", "Mô hình tốt nhất LinearSVC (F1: 90.38%)"),
        ("B6", "Đánh giá mô hình & Phân tích lỗi", "Tập Test độc lập (2.237 mẫu)", "Vẽ ma trận nhầm lẫn (Confusion Matrix), mổ xẻ nguyên nhân sai lệch FP và FN", "Báo cáo ma trận nhầm lẫn & Bảng mổ xẻ lỗi"),
        ("B7", "Đóng gói & Triển khai dự đoán mới", "Mô hình tối ưu đã lưu .joblib", "Xây dựng hàm suy luận thời gian thực, thiết kế API RESTful FastAPI và Dashboard Streamlit", "Dịch vụ Microservice API & UI Web sẵn sàng")
    ]

    for i, row in enumerate(data_7s):
        r_el = t_7steps.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_7s[j]
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

    add_body_p(doc, "\nBảng 1.2: Chi tiết các giai đoạn triển khai trong Quy trình 7 bước dự án học máy của Nhóm 12")

    add_heading_2(doc, "1.3. Sự đánh đổi giữa Thiên lệch và Phương sai (Bias - Variance Tradeoff)")
    add_heading_3(doc, "1.3.1. Chứng minh toán học công thức phân rã sai số kỳ vọng")
    add_body_p(doc, "Trong lý thuyết học máy thống kê (Statistical Learning Theory), sự đánh đổi giữa Thiên lệch (Bias) và Phương sai (Variance) là nguyên lý toán học trung tâm chi phối khả năng tổng quát hóa của mọi mô hình học máy. Giả sử dữ liệu được sinh ra từ mối quan hệ thực tế: y = f(x) + ε, trong đó ε là nhiễu ngẫu nhiên độc lập với tập dữ liệu huấn luyện D, thỏa mãn kỳ vọng E[ε] = 0 và phương sai Var(ε) = σ².")
    
    add_body_p(doc, "Xét sai số toàn phương kỳ vọng đối với một điểm dữ liệu mới x khi lấy kỳ vọng trên toàn bộ các tập huấn luyện D có thể có:")
    add_math_block(doc, "E_D[(y - f̂(x))²] = E_D[(f(x) + ε - f̂(x))²]", "1.2")
    
    add_body_p(doc, "Đặt f̄(x) = E_D[f̂(x)] là giá trị dự đoán trung bình của mô hình. Biến đổi biểu thức bên trong dấu kỳ vọng:")
    add_math_block(doc, "y - f̂(x) = (f(x) - f̄(x)) + (f̄(x) - f̂(x)) + ε", "1.3")
    
    add_body_p(doc, "Bình phương hai vế và khai triển hằng đẳng thức:")
    add_math_block(doc, "(y - f̂(x))² = (f(x) - f̄(x))² + (f̄(x) - f̂(x))² + ε² + 2(f(x) - f̄(x))(f̄(x) - f̂(x)) + 2(f(x) - f̄(x))ε + 2(f̄(x) - f̂(x))ε", "1.4")
    
    add_body_p(doc, "Lấy kỳ vọng E_D hai vế. Do ε độc lập với D và E[ε] = 0, toàn bộ các số hạng tích chéo chứa ε đều triệt tiêu về 0:\n"
                  "• E_D[2(f(x) - f̄(x))ε] = 2(f(x) - f̄(x)) E[ε] = 0\n"
                  "• E_D[2(f̄(x) - f̂(x))ε] = 2 E_D[f̄(x) - f̂(x)] E[ε] = 0\n"
                  "Đồng thời, do f̄(x) là hằng số đối với kỳ vọng E_D, số hạng tích chéo đầu tiên cũng triệt tiêu:\n"
                  "• E_D[2(f(x) - f̄(x))(f̄(x) - f̂(x))] = 2(f(x) - f̄(x)) (f̄(x) - E_D[f̂(x)]) = 2(f(x) - f̄(x)) (f̄(x) - f̄(x)) = 0")

    add_body_p(doc, "Kết quả ta thu được công thức phân rã toán học hoàn chỉnh (Công thức 1.57, tr. 33 Giáo trình Học máy):")
    add_math_block(doc, "E_D[(y - f̂(x))²] = [f(x) - E_D[f̂(x)]]² + E_D[(f̂(x) - E_D[f̂(x)])²] + E[ε²] = [Bias(f̂(x))]² + Var(f̂(x)) + σ²", "1.5")

    add_heading_3(doc, "1.3.2. Ý nghĩa của kỹ thuật điều chuẩn L2 trong kiểm soát phương sai")
    add_body_p(doc, "Trong bài toán phân loại văn bản tiếng Việt với số chiều đặc trưng TF-IDF lên tới d = 24.619 chiều, số lượng đặc trưng lớn hơn gấp đôi số lượng mẫu huấn luyện (N = 10.437). Khi số chiều d > N, ma trận hiệp phương sai mẫu trở nên suy biến và phương sai của ước lượng trọng số Var(w) có xu hướng tiến tới vô cùng, khiến mô hình cực kỳ dễ bị Overfitting.")
    
    add_body_p(doc, "Kỹ thuật điều chuẩn L2 (Ridge Regularization hay Weight Decay) đưa vào số hạng phạt (1/2C) ||w||₂² nhằm giới hạn không gian giả thuyết của mô hình. Về mặt toán học, điều chuẩn L2 làm tăng nhẹ độ chệch Bias nhưng lại làm giảm mạnh mẽ phương sai Variance, nhờ đó tổng sai số kỳ vọng E[(y - f̂(x))²] đạt điểm cực tiểu toàn cục. Đây chính là lý do vì sao LinearSVC và Logistic Regression với điều chuẩn L2 đạt hiệu năng vượt trội và ổn định tuyệt đối trên tập Test độc lập.")

    add_heading_2(doc, "1.4. Phát biểu bài toán và Bối cảnh thực tế tại thị trường Việt Nam")
    add_body_p(doc, "Tại thị trường Việt Nam, làn sóng chuyển đổi số đã đưa ứng dụng di động trở thành kênh tương tác cốt lõi giữa doanh nghiệp và hàng chục triệu người tiêu dùng. Tuy nhiên, việc khai thác ý kiến phản hồi của khách hàng hiện nay tại nhiều đơn vị vẫn còn mang tính thủ công, thụ động, hoặc chỉ đọc lướt các đánh giá 1 sao mà không có cái nhìn tổng thể theo từng trục nghiệp vụ sản phẩm.")

    add_body_p(doc, "Mục tiêu của đề tài Nhóm 12 là xây dựng hệ sinh thái phần mềm tự động hóa toàn diện quy trình phân tích phản hồi, hỗ trợ đắc lực cho các bộ phận:\n"
                  "1. Bộ phận Chăm sóc khách hàng (CSKH): Kịp thời phát hiện các phản hồi tiêu cực bức xúc về thái độ tài xế, lừa đảo nạp thẻ, hoặc giam tiền ví để ưu tiên xử lý trong vòng 15 phút;\n"
                  "2. Bộ phận Kỹ thuật & Phát triển sản phẩm (Product & Tech): Nhận diện tức thì các đợt phát hành phiên bản mới bị lỗi đơ máy, văng ứng dụng hoặc lỗi sinh trắc học căn cước công dân;\n"
                  "3. Ban Giám đốc & Marketing: Theo dõi chỉ số sức khỏe thương hiệu (Brand Sentiment Index) và tỷ lệ hài lòng của khách hàng trên 7 khía cạnh nghiệp vụ theo thời gian thực.")

    add_heading_2(doc, "1.5. Thách thức đặc thù trong xử lý ngôn ngữ tự nhiên Tiếng Việt")
    add_body_p(doc, "Ngữ liệu phản hồi trên các kho ứng dụng di động tiếng Việt có đặc tính ngôn ngữ cực kỳ phức tạp:")
    add_body_p(doc, "• Tính mỉa mai, châm biếm sâu (Deep Sarcasm): Người dùng sử dụng các từ ngữ khen ngợi tột đỉnh đặt trong tình huống trớ trêu để chỉ trích (ví dụ: 'App đỉnh chóp thật sự, bảo trì từ sáng đến đêm cho người dùng nghỉ ngơi khỏi mua sắm!').\n"
                  "• Hiện tượng đảo ngữ phủ định: 'Chẳng có gì để chê ngoại trừ việc hay bị trừ tiền vô lý', 'Tưởng không tốt mà lại tốt không tưởng'.\n"
                  "• Teencode phong phú và lỗi gõ bàn phím tiếng Việt (Telex/Vni): 'ko', 'hok', 'k', 'đc', 'dc', 'wa', 'zay', 'j', 'đt', 'tgian'.")

    add_heading_2(doc, "1.6. Tổng quan các nghiên cứu liên quan trên thế giới và tại Việt Nam")
    add_body_p(doc, "Trên thế giới, cuộc thi SemEval (Task 5: Aspect Based Sentiment Analysis) của Pontiki và cộng sự (2016) đã đặt nền móng chuẩn hóa cho bài toán phân tích quan điểm theo khía cạnh trên các tập dữ liệu đánh giá nhà hàng, máy tính xách tay. Tại Việt Nam, nhóm nghiên cứu tại Đại học Công nghệ Thông tin - ĐHQG TP.HCM (UIT) đã công bố bộ ngữ liệu UIT-VSFC (Vietnamese Students' Feedback Corpus) cho đánh giá sinh viên, và ViHSD cho phát hiện ngôn từ thù ghét. Tuy nhiên, mảng phản hồi ứng dụng di động đa ngành (Ngân hàng, Ví điện tử, Sàn TMĐT, Gọi xe) vẫn còn thiếu vắng các giải pháp tối ưu hóa thời gian thực kết hợp kiểm toán nghịch nhãn.")

    add_heading_2(doc, "1.7. Các điểm đổi mới sáng tạo và giải pháp công nghệ vượt trội của Đề tài")
    add_callout(doc, [
        "1. Hệ thống Phân tích đa diện Joint Aspect-Based Sentiment Analysis (ABSA): Giải quyết đồng thời bài toán phân loại nhãn cảm xúc nhị phân và phân loại 7 khía cạnh nghiệp vụ, cung cấp thông tin quản trị đa chiều.",
        "2. Bộ lọc kiểm toán khử nhiễu nghịch nhãn (Sarcasm & Bias Audit): Xử lý triệt để 50 mẫu đánh giá 5 sao chửi bới / 1 sao khen ngợi, đem lại tập dữ liệu sạch 100%.",
        "3. Tối ưu hóa cực hạn cho môi trường sản xuất (Production-ready): Kích thước mô hình chỉ ~100 KB, tốc độ suy luận 0.3 µs/mẫu, sẵn sàng đóng gói RESTful API và Web Dashboard mà không tốn chi phí thuê GPU đắt đỏ."
    ], title="3 ĐIỂM SÁNG TẠO CÔNG NGHỆ VƯỢT TRỘI CỦA ĐỀ TÀI NHÓM 12:")

    doc.add_page_break()
    return doc
