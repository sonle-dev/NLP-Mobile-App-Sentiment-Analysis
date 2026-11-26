# -*- coding: utf-8 -*-
"""
Module: chapter1_expanded.py
Comprehensive Chapter 1 for Machine Learning Project Report (ICTU 2026).
Word budget: ~4,200 words.
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

def add_chapter1(doc):
    add_heading_1(doc, "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN BÀI TOÁN")

    # -------------------------------------------------------------
    # 1.1. KHÁI QUÁT VỀ HỌC MÁY VÀ XỬ LÝ NGÔN NGỮ TỰ NHIÊN (NLP)
    # -------------------------------------------------------------
    add_heading_2(doc, "1.1. Khái quát về Học máy và Xử lý ngôn ngữ tự nhiên (NLP)")
    
    add_heading_3(doc, "1.1.1. Khái niệm và phân loại các phương pháp học máy")
    add_body_p(doc, "Theo định nghĩa kinh điển của Tom Mitchell (1997): \"Một chương trình máy tính được coi là học từ kinh nghiệm E (Experience) đối với một lớp nhiệm vụ T (Task) và độ đo hiệu năng P (Performance), nếu hiệu năng của nó đối với các nhiệm vụ trong T, được đo bởi P, cải thiện cùng với kinh nghiệm E\". Trong kỷ nguyên dữ liệu lớn (Big Data), học máy đóng vai trò là động lực cốt lõi cho phép hệ thống tự động trích xuất các quy luật tiềm ẩn từ dữ liệu quá khứ mà không cần lập trình các quy tắc logic thủ công tường minh.")
    
    add_body_p(doc, "Căn cứ vào phương thức phản hồi của dữ liệu môi trường và bản chất của kinh nghiệm E, học máy được phân chia thành 4 phân nhánh chính:\n"
                  "1. Học có giám sát (Supervised Learning): Tập dữ liệu huấn luyện bao gồm các cặp đầu vào - đầu ra mong muốn D = {(x_i, y_i)}_{i=1}^N. Mục tiêu là xấp xỉ hàm ánh xạ f: X -> Y sao cho cực tiểu hóa hàm mất mát (Loss Function) trên dữ liệu chưa từng quan sát. Bài toán phân loại cảm xúc (Sentiment Analysis) và phân loại khía cạnh (Aspect Classification) trong đồ án này thuộc lớp bài toán học có giám sát với nhãn cảm xúc rời rạc y ∈ {Tích cực, Tiêu cực}.\n"
                  "2. Học không giám sát (Unsupervised Learning): Dữ liệu chỉ chứa các quan sát đầu vào x_i mà không có nhãn chỉ dẫn y_i. Thuật toán tự khám phá cấu trúc nội tại, phân cụm dữ liệu (Clustering như K-Means, DBSCAN) hoặc giảm số chiều không gian (Dimensionality Reduction như PCA, t-SNE).\n"
                  "3. Học bán giám sát (Semi-supervised Learning): Kết hợp lượng nhỏ dữ liệu có gán nhãn với lượng lớn dữ liệu phi nhãn nhằm giảm thiểu chi phí gán nhãn thủ công tốn kém.\n"
                  "4. Học tăng cường (Reinforcement Learning): Tác tử (Agent) tương tác trực tiếp với môi trường thông qua các hành động, nhận tín hiệu thưởng/phạt (Reward/Penalty) và học chính sách hành động tối ưu để cực đại hóa phần thưởng tích lũy lâu dài.")

    add_heading_3(doc, "1.1.2. Vị trí của Xử lý ngôn ngữ tự nhiên trong hệ thống thông tin số")
    add_body_p(doc, "Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP) là một nhánh liên ngành then chốt nằm tại giao điểm giữa Trí tuệ nhân tạo (AI), Khoa học máy tính và Ngôn ngữ học tính toán. Mục tiêu tối thượng của NLP là thu hẹp khoảng cách giao tiếp giữa tư duy ngôn ngữ tự nhiên của con người và hệ thống tính toán nhị phân của máy tính. Trong bối cảnh hơn 85% dữ liệu số sinh ra trên không gian mạng hiện nay tồn tại dưới dạng văn bản phi cấu trúc (Unstructured Text) - bao gồm bài viết mạng xã hội, bình luận đánh giá ứng dụng, email khách hàng, tin nhắn phản hồi - các kỹ thuật NLP truyền thống và học máy văn bản đóng vai trò là chiếc cầu nối chuyển hóa các chuỗi ký tự tự do thành thông tin có cấu trúc phục vụ phân tích nghiệp vụ và ra quyết định kinh doanh.")

    add_heading_3(doc, "1.1.3. Khái niệm bài toán Phân tích quan điểm (Sentiment Analysis)")
    add_body_p(doc, "Phân tích quan điểm (Sentiment Analysis - SA), hay còn gọi là Khai phá quan điểm (Opinion Mining), là lĩnh vực nghiên cứu chuyên sâu của NLP nhằm phân tích các ý kiến, cảm xúc, đánh giá và thái độ của người viết đối với một thực thể cụ thể (sản phẩm, dịch vụ, con người, sự kiện hoặc chủ đề). Theo Bing Liu (2012), một quan điểm (Opinion) đầy đủ được biểu diễn hình thức dưới dạng một bộ ngũ (Quintupel):")
    add_math_block(doc, "o = (e_j, a_{jk}, s_{ijkl}, h_i, t_l)", "1.1")
    add_body_p(doc, "Trong đó: e_j là thực thể mục tiêu (Target Entity); a_{jk} là khía cạnh/thuộc tính của thực thể (Aspect / Attribute); s_{ijkl} là sắc thái cảm xúc (Sentiment Value: Tích cực, Tiêu cực, hoặc Trung tính); h_i là người nắm giữ quan điểm (Opinion Holder); và t_l là thời điểm quan điểm được phát biểu (Time Stamp).")

    add_body_p(doc, "Trong thực tế công nghiệp, bài toán Phân tích quan điểm được chia thành 3 cấp độ chi tiết chính:\n"
                  "• Cấp độ toàn văn bản (Document Level): Xác định sắc thái cảm xúc chung cho toàn bộ một tài liệu hay bài đánh giá. Giả định rằng toàn bộ văn bản chỉ bày tỏ một quan điểm đồng nhất về một đối tượng duy nhất.\n"
                  "• Cấp độ câu (Sentence Level): Phân tích từng câu độc lập xem câu đó là câu cảm xúc (Subjective Sentence) hay câu thông tin sự thật (Objective Sentence), và nếu có cảm xúc thì là tích cực hay tiêu cực.\n"
                  "• Cấp độ khía cạnh (Aspect-Based Sentiment Analysis - ABSA): Đây là cấp độ phân tích hạt mịn và có giá trị nghiệp vụ cao nhất. Một đánh giá người dùng thường khen mặt này nhưng chê mặt khác (Ví dụ: \"Giao diện app MB Bank rất đẹp nhưng tính năng sinh trắc học quét CCCD bị lỗi hoài\"). ABSA bóc tách chính xác từng khía cạnh nghiệp vụ cụ thể để gán nhãn cảm xúc tương ứng, cung cấp dữ liệu hành động trực tiếp cho đội ngũ phát triển sản phẩm.")

    add_heading_3(doc, "1.1.4. So sánh đối sánh các trường phái tiếp cận trong NLP")
    add_body_p(doc, "Trong lịch sử phát triển của NLP, đã có 5 trường phái tiếp cận chính được áp dụng cho bài toán phân loại quan điểm văn bản. Nhóm 12 tổng hợp và đối sánh chi tiết 5 trường phái này qua Bảng 1.1 dưới đây:")

    t_school = doc.add_table(rows=6, cols=6)
    t_school.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_sch = [Inches(1.0), Inches(1.0), Inches(1.1), Inches(1.0), Inches(1.1), Inches(1.0)]
    headers_sch = ["Trường phái", "Nguyên lý cốt lõi", "Ưu điểm nổi bật", "Hạn chế chí mạng", "Độ trễ suy luận", "Chi phí triển khai"]

    hdr_s = t_school.rows[0]
    for j, h in enumerate(headers_sch):
        c = hdr_s.cells[j]
        c.width = w_sch[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 70, 70, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_sch = [
        ("1. Dựa trên luật (Rule-Based)", "Xây dựng các mẫu ngữ pháp Regex và luật if-else thủ công.", "Không cần dữ liệu huấn luyện, giải thích được 100%.", "Dễ sụp đổ khi gặp từ lóng, teencode, cấu trúc câu tự do.", "Siêu nhanh (< 0.1 ms)", "Rất cao (bảo trì thủ công)"),
        ("2. Dựa trên từ điển (Lexicon-Based)", "Tra cứu điểm cảm xúc từ các từ điển định sẵn (SentiWordNet).", "Dễ cài đặt, không đòi hỏi huấn luyện mô hình phức tạp.", "Không nắm bắt được ngữ cảnh (Ví dụ: 'rất không tốt').", "Rất nhanh (< 0.2 ms)", "Thấp"),
        ("3. Học máy cổ điển (Classical ML)\n[ĐỀ TÀI LỰA CHỌN]", "Biểu diễn vector TF-IDF N-gram kết hợp mô hình Linear SVM, Logistic Regression.", "Độ chính xác cao (F1 > 90%), tốc độ suy luận cực nhanh (< 0.3 ms), kích thước mô hình siêu nhẹ (< 10 MB), không cần GPU.", "Cần kỹ thuật trích chọn đặc trưng (Feature Engineering) chỉn chu.", "Siêu nhanh (< 0.3 ms/mẫu)", "Cực kỳ thấp (chạy tốt trên CPU 5$)"),
        ("4. Học sâu tuần tự (RNN / LSTM)", "Mạng nơ-ron hồi quy xử lý chuỗi ký tự và từ vựng tuần tự.", "Học được phụ thuộc ngữ cảnh chuỗi trong khoảng cách ngắn.", "Thời gian huấn luyện lâu, dễ bị biến mất gradient (Vanishing Gradient).", "Trung bình (~15-30 ms)", "Trung bình (cần GPU nhẹ)"),
        ("5. Transformers tiền huấn luyện (PhoBERT/LLM)", "Cơ chế Self-Attention học ngữ cảnh hai chiều sâu rộng.", "Độ chính xác rất cao, hiểu được ngữ cảnh phức tạp.", "Rất nặng (500MB - 14GB), độ trễ cao (50-200ms), chi phí vận hành đắt đỏ, khó triển khai edge.", "Chậm (50 - 500 ms)", "Rất cao (đòi hỏi GPU chuyên dụng)")
    ]

    for i, row in enumerate(data_sch):
        r_el = t_school.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_sch[j]
            set_cell_margins(c, 50, 50, 50, 50)
            if i % 2 == 1:
                set_cell_background(c, "F9FBFD")
            p = c.paragraphs[0]
            if j in [0, 4, 5]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.0)
            if j == 0 and "ĐỀ TÀI LỰA CHỌN" in val:
                r.font.bold = True

    add_body_p(doc, "\nBảng 1.1: So sánh đối chuẩn toàn diện 5 trường phái công nghệ trong Xử lý ngôn ngữ tự nhiên")

    # -------------------------------------------------------------
    # 1.2. QUY TRÌNH THỰC HIỆN DỰ ÁN HỌC MÁY TIÊU CHUẨN
    # -------------------------------------------------------------
    add_heading_2(doc, "1.2. Quy trình thực hiện dự án học máy tiêu chuẩn")
    add_body_p(doc, "Trong môi trường công nghiệp và nghiên cứu ứng dụng, quy trình phát triển một dự án học máy là một chu trình kỹ thuật 7 bước lặp khép kín (Iterative Engineering Pipeline). Nhóm 12 đã tuân thủ nghiêm ngặt chuẩn mực này để đảm bảo tính tái lập (Reproducibility) và độ tin cậy khoa học của toàn bộ kết quả thực nghiệm.")

    t_7steps = doc.add_table(rows=8, cols=5)
    t_7steps.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_7s = [Inches(0.6), Inches(1.3), Inches(1.4), Inches(1.8), Inches(1.1)]
    headers_7s = ["Bước", "Tên giai đoạn", "Dữ liệu đầu vào", "Nội dung kỹ thuật thực hiện", "Sản phẩm đầu ra"]

    hdr_7 = t_7steps.rows[0]
    for j, h in enumerate(headers_7s):
        c = hdr_7.cells[j]
        c.width = w_7s[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 70, 70, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_7s = [
        ("B1", "Xác định bài toán & Thu thập dữ liệu", "Phản hồi người dùng trên Google Play & App Store", "Sử dụng công cụ cào tự động 15.541 đánh giá thô của 8 ứng dụng di động", "Tập dữ liệu thô app_reviews.csv"),
        ("B2", "Khám phá & Trực quan hóa dữ liệu EDA", "Tập dữ liệu thô 15.541 dòng", "Phân tích rating, độ dài từ, phân bố cảm xúc và khía cạnh trên biểu đồ", "Báo cáo thống kê mô tả & Báo cáo EDA"),
        ("B3", "Tiền xử lý & Xây dựng đặc trưng", "Văn bản thô, teencode, lỗi chính tả", "Chuẩn hóa Unicode, xử lý teencode, khử nhiễu nghịch nhãn, tách từ ghép underthesea, TF-IDF", "Tập dữ liệu sạch 14.910 mẫu & Ma trận TF-IDF"),
        ("B4", "Huấn luyện các mô hình phân lớp", "Ma trận TF-IDF tập Train (10.437 mẫu)", "Cài đặt và huấn luyện 4 mô hình: MultinomialNB, Logistic Regression, LinearSVC, Random Forest", "4 mô hình đã được fit tham số trọng số"),
        ("B5", "Tối ưu siêu tham số & Chọn mô hình", "Tập Train & Validation (2.236 mẫu)", "Chạy GridSearchCV 5-fold tối ưu tham số C, loss; đối chuẩn định lượng trên tập Test", "Mô hình tốt nhất LinearSVC (F1: 90.38%)"),
        ("B6", "Đánh giá mô hình & Phân tích lỗi", "Tập Test độc lập (2.237 mẫu)", "Vẽ ma trận nhầm lẫn (Confusion Matrix), mổ xẻ nguyên nhân sai lệch 20 ca mẫu FP và FN", "Báo cáo ma trận nhầm lẫn & Bảng mổ xẻ lỗi"),
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
            r.font.size = Pt(8.0)

    add_body_p(doc, "\nBảng 1.2: Chi tiết các giai đoạn triển khai trong Quy trình 7 bước dự án học máy của Nhóm 12")

    # -------------------------------------------------------------
    # 1.3. SỰ ĐÁNH ĐỔI GIỮA THIÊN LỆCH VÀ PHƯƠNG SAI (BIAS - VARIANCE)
    # -------------------------------------------------------------
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
                  "• E_D[2(f̄(x) - f̂(x))ε] = 2 E_D[(f̄(x) - f̂(x))] E[ε] = 0\n"
                  "• E_D[2(f(x) - f̄(x))(f̄(x) - f̂(x))] = 2(f(x) - f̄(x)) E_D[f̄(x) - f̂(x)] = 2(f(x) - f̄(x))(f̄(x) - f̄(x)) = 0")
    
    add_body_p(doc, "Như vậy, ta thu được kết quả phân rã toán học hoàn chỉnh:")
    add_math_block(doc, "E_D[(y - f̂(x))²] = (f(x) - f̄(x))² + E_D[(f̂(x) - f̄(x))²] + σ² = Bias²(f̂(x)) + Var(f̂(x)) + σ²", "1.5")

    add_heading_3(doc, "1.3.2. Ý nghĩa của kỹ thuật điều chuẩn L2 trong kiểm soát phương sai")
    add_body_p(doc, "Trong bài toán xử lý ngôn ngữ tự nhiên với không gian đặc trưng TF-IDF N-gram có số chiều rất lớn (d = 24.619 chiều trong đồ án này), mô hình có xu hướng rất nhạy cảm với các biến động ngẫu nhiên của tập huấn luyện, dẫn tới phương sai (Variance) tăng vọt và gây ra hiện tượng quá khớp (Overfitting). Để kiểm soát phương sai, kỹ thuật điều chuẩn L2 (Ridge Regularization / L2-Penalty) được áp dụng vào hàm mục tiêu:")
    add_math_block(doc, "J(w) = Loss(y, Xw) + (1 / 2C) ||w||₂²", "1.6")
    add_body_p(doc, "Tham số phạt C > 0 đóng vai trò điều tiết sự đánh đổi: Khi C quá lớn, mô hình ít bị phạt độ lớn trọng số w, cố gắng khớp từng điểm dữ liệu kể cả nhiễu => Bias thấp nhưng Variance cao (Overfitting). Ngược lại, khi C quá nhỏ, lực ép w về 0 quá mạnh, mô hình trở nên quá đơn giản => Variance thấp nhưng Bias cao (Underfitting). Thực nghiệm tại Mục 3.4 chứng minh việc tinh chỉnh C = 2.0 đã đạt điểm cân bằng vàng giữa Bias và Variance, mang lại hiệu năng kiểm thử cao nhất trên tập Test độc lập.")

    # -------------------------------------------------------------
    # 1.4. BỐI CẢNH KINH TẾ SỐ VÀ TÍNH CẤP THIẾT CỦA ĐỀ TÀI
    # -------------------------------------------------------------
    add_heading_2(doc, "1.4. Bối cảnh kinh tế số và Tính cấp thiết của đề tài tại Việt Nam")
    add_body_p(doc, "Trong giai đoạn 2024 - 2026, nền kinh tế số Việt Nam chứng kiến sự bùng nổ vượt bậc với tốc độ tăng trưởng hàng năm đạt trên 20%. Hàng chục triệu người dân sử dụng điện thoại thông minh để thực hiện các giao dịch thiết yếu hàng ngày thông qua 4 trụ cột ứng dụng di động công nghệ hàng đầu:\n"
                  "1. Ngân hàng số (Digital Banking): MB Bank, Agribank - nơi người dùng thực hiện thanh toán, chuyển khoản, xác thực sinh trắc học căn cước công dân (CCCD) gắn chip theo Quyết định 2345/QĐ-NHNN của Ngân hàng Nhà nước.\n"
                  "2. Ví điện tử và Cổng thanh toán (Fintech E-Wallets): MoMo, ZaloPay - hệ sinh thái tài chính tiêu dùng, thanh toán hóa đơn điện nước, nạp tiền điện thoại và tích lũy đầu tư.\n"
                  "3. Thương mại điện tử và Dịch vụ giao vận theo yêu cầu (E-Commerce & Food Delivery): Shopee, ShopeeFood, Grab - phục vụ nhu cầu mua sắm trực tuyến, đặt đồ ăn và gọi xe công nghệ hàng ngày.\n"
                  "4. Mạng xã hội và Giải trí video ngắn (Social Media): TikTok - nền tảng sáng tạo nội dung và giải trí số tích hợp tính năng thương mại điện tử TikTok Shop.")

    add_body_p(doc, "Mỗi ngày, các nền tảng này tiếp nhận hàng chục nghìn phản hồi, đánh giá (Reviews) từ người dùng trên kho ứng dụng Google Play Store và Apple App Store. Đây là kho tàng thông tin vô giá phản ánh trực tiếp trải nghiệm khách hàng (Voice of Customer - VoC). Tuy nhiên, việc đọc và phân loại thủ công bằng sức người là hoàn toàn bất khả thi do khối lượng khổng lồ. Do đó, việc xây dựng một hệ thống học máy thông minh, có khả năng tự động phân tích quan điểm đa diện (Joint ABSA), bóc tách chính xác cảm xúc gắn liền với từng khía cạnh kỹ thuật/nghiệp vụ cụ thể với tốc độ tính toán thời gian thực là nhu cầu vô cùng cấp thiết, mang lại giá trị thực tiễn và kinh tế to lớn.")

    # -------------------------------------------------------------
    # 1.5. THÁCH THỨC ĐẶC THÙ TRONG XỬ LÝ NGÔN NGỮ TIẾNG VIỆT
    # -------------------------------------------------------------
    add_heading_2(doc, "1.5. Thách thức đặc thù trong xử lý ngôn ngữ tự nhiên Tiếng Việt")
    add_body_p(doc, "Tiếng Việt là một ngôn ngữ đơn lập (Isolating Language) không biến đổi hình thái từ, sở hữu những đặc trưng ngữ pháp và thói quen giao tiếp đời thường vô cùng phức tạp, đặc biệt là trong các bình luận trực tuyến của thế hệ trẻ (Gen Z). Đề tài xác định 6 thách thức kỹ thuật lớn nhất:")

    t_chal = doc.add_table(rows=7, cols=3)
    t_chal.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_ch = [Inches(1.2), Inches(2.3), Inches(2.7)]
    headers_ch = ["Thách thức", "Biểu hiện cụ thể trong dữ liệu", "Giải pháp kỹ thuật của Nhóm 12"]

    hdr_c = t_chal.rows[0]
    for j, h in enumerate(headers_ch):
        c = hdr_c.cells[j]
        c.width = w_ch[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 70, 70, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.0)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_ch = [
        ("1. Từ ghép & Cấu trúc đa âm tiết", "Từ vựng tiếng Việt cấu tạo từ nhiều âm tiết đơn lẻ. Dấu khoảng trắng vừa là ranh giới từ vừa là ranh giới âm tiết ('ngân hàng' vs 'ngân' + 'hàng').", "Sử dụng giải thuật quy hoạch động Viterbi kết hợp mô hình CRF của thư viện underthesea để phân tách từ ghép chính xác."),
        ("2. Teencode & Từ lóng công nghệ", "Người dùng viết tắt vô độ: 'k'/'ko'/'hông' -> 'không', 'đc' -> 'được', 'app'/'áp' -> 'ứng dụng', 'lag'/'đơ'/'giật' -> 'chậm lag'.", "Xây dựng Từ điển chuẩn hóa Teencode 50 quy tắc tự động ánh xạ về dạng chuẩn mực tiếng Việt."),
        ("3. Lỗi gõ bàn phím Telex/VNI", "Gõ thừa ký tự hoặc sai dấu thanh: 'nguoii', 'duwowcj', 'khoos', 'yeu caau'.", "Module tiền xử lý Regular Expression quét và khôi phục ký tự nguyên bản theo bộ gõ Unicode chuẩn NFC."),
        ("4. Nghịch nhãn cảm xúc (Rating Sarcasm)", "Chấm 1 sao nhưng ghi 'App tuyệt vời lắm ạ :))', hoặc chấm 5 sao nhưng chê 'Đợi đồ ăn 1 tiếng nguội tanh'.", "Thiết kế Bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit) dựa trên ma trận mâu thuẫn sao và từ điển ngữ nghĩa."),
        ("5. Phủ định kép & Đảo ngữ", "Cụm từ phủ định làm đảo ngược cảm xúc: 'không phải là không tốt', 'chẳng chê vào đâu được'.", "Khai thác không gian đặc trưng N-gram (1, 2) bảo toàn trọn vẹn cụm từ ghép cặp cảm xúc ('không_tốt', 'rất_mượt')."),
        ("6. Ngôn ngữ pha trộn (Code-switching)", "Trộn lẫn tiếng Anh và tiếng Việt: 'app lag vcl, crash liên tục khi scan face'.", "Bổ sung các thuật ngữ kỹ thuật tiếng Anh phổ biến vào bộ từ điển dừng và từ điển đặc trưng miền ứng dụng.")
    ]

    for i, row in enumerate(data_ch):
        r_el = t_chal.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_ch[j]
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

    add_body_p(doc, "\nBảng 1.3: Tổng hợp các thách thức ngôn ngữ tiếng Việt và giải pháp kỹ thuật tương ứng của Đề tài")

    # -------------------------------------------------------------
    # 1.6. TỔNG QUAN CÁC NGHIÊN CỨU LIÊN QUAN
    # -------------------------------------------------------------
    add_heading_2(doc, "1.6. Tổng quan các nghiên cứu liên quan trên thế giới và tại Việt Nam")
    add_body_p(doc, "Nghiên cứu về phân tích quan điểm văn bản đã trải qua hơn hai thập kỷ phát triển mạnh mẽ. Trên thế giới, nghiên cứu nền tảng của Pang và Lee (2002) tại Đại học Cornell đã đặt viên gạch đầu tiên khi chứng minh rằng các thuật toán học máy cổ điển (Naive Bayes, Maximum Entropy, SVM) vượt trội hoàn toàn so với các phương pháp dựa trên từ điển luật truyền thống trong việc phân loại đánh giá phim ảnh. Joachims (1998) đã chứng minh bằng lý thuyết đại số rằng SVM là mô hình tối ưu tuyệt đối cho dữ liệu văn bản nhờ khả năng chống lại hiện tượng quá khớp trong không gian vector thưa có số chiều cực lớn.")

    add_body_p(doc, "Về phân tích quan điểm theo khía cạnh (ABSA), chuỗi hội thảo quốc tế SemEval (2014, 2015, 2016) do Pontiki và các cộng sự khởi xướng đã định hình các chuẩn mực đánh giá cho bài toán phát hiện khía cạnh và phân loại cảm xúc tương ứng trong các miền nhà hàng, khách sạn và thiết bị điện tử gia dụng.")

    add_body_p(doc, "Tại Việt Nam, các nghiên cứu tiêu biểu bao gồm bộ ngữ liệu UIT-VSFC (Vietnamese Students' Feedback Corpus) của Nguyen et al. (2018) tại Trường ĐH Công nghệ Thông tin - ĐHQG TP.HCM dành cho phân tích phản hồi sinh viên; các chiến dịch đánh giá xử lý ngôn ngữ tiếng Việt VLSP (Vietnamese Language and Speech Processing) qua các năm 2016, 2018; và mô hình ngôn ngữ PhoBERT của VinAI Research (Nguyen & Nguyen, 2020). Tuy nhiên, hầu hết các nghiên cứu này chủ yếu tập trung vào dữ liệu chuẩn ngữ pháp (học đường, báo chí) hoặc sử dụng các mô hình học sâu kích thước lớn khó triển khai trong thực tế sản xuất thời gian thực. Đề tài của Nhóm 12 giải quyết triệt để khoảng trống này bằng cách tập trung vào phản hồi ứng dụng di động thực tế, xử lý teencode và tối ưu hóa giải pháp học máy siêu nhẹ với độ trễ < 0.3 ms/mẫu.")

    # -------------------------------------------------------------
    # 1.7. CÁC ĐIỂM ĐỔI MỚI SÁNG TẠO CỦA ĐỀ TÀI
    # -------------------------------------------------------------
    add_heading_2(doc, "1.7. Các điểm đổi mới sáng tạo và giải pháp công nghệ vượt trội của Đề tài")
    add_callout(doc, [
        "1. Hệ thống Phân tích quan điểm đa diện (Joint ABSA) 7 khía cạnh nghiệp vụ: Chuẩn hóa phân loại phản hồi theo tiêu chuẩn công nghiệp ISO/IEC 25010, phân tách rạch ròi giữa cảm xúc chung và khía cạnh chức năng chuyên biệt.",
        "2. Bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit): Phát hiện và chuẩn hóa tự động hơn 1.240 mẫu mâu thuẫn giữa số sao đánh giá và nội dung bình luận thực tế, nâng độ tin cậy của tập dữ liệu lên mức tiệm cận nhãn vàng (Gold Standard).",
        "3. Tối ưu hóa suy luận siêu nhẹ thời gian thực (Ultra-low Latency Inference): Mô hình LinearSVC kết hợp TF-IDF N-gram chỉ mất 0.28 ms để phân loại 1 phản hồi trên CPU thông thường, kích thước tệp mô hình chỉ 8.4 MB, dễ dàng nhúng vào ứng dụng di động hoặc máy chủ biên.",
        "4. Sẵn sàng tích hợp dịch vụ sản xuất (Production-Ready Architecture): Đóng gói toàn bộ pipeline thành dịch vụ Microservice RESTful API bằng FastAPI và Giao diện Dashboard tương tác trực quan bằng Streamlit."
    ], "4 ĐIỂM ĐỔI MỚI SÁNG TẠO VÀ CÔNG NGHỆ VƯỢT TRỘI CỦA ĐỒ ÁN:")

    doc.add_page_break()
