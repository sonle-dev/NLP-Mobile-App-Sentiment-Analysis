# -*- coding: utf-8 -*-
"""
Module: frontmatter_expanded.py
Provides comprehensive, academic frontmatter for the 50-page Machine Learning Project Report
at University of Information and Communication Technology - Thai Nguyen University (ICTU).
Includes:
- Trang bìa chính & Trang bìa phụ
- Lời cảm ơn & Lời cam đoan
- Bảng phân công nhiệm vụ 4 thành viên (Lê Hồng Sơn, Lưu Thị Khánh Ly, Ngô Thị Sinh, Nguyễn Thanh Tùng)
- Bảng đối chiếu Tiêu chí chấm điểm (GV. ThS. Hà Thị Thanh - 2.0đ Báo cáo + 8.0đ Thực nghiệm)
- Mục lục chi tiết
- Danh mục bảng biểu
- Danh mục hình vẽ
- Danh mục từ viết tắt và thuật ngữ
- Danh mục ký hiệu toán học
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from .helpers import (
    add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_math_block, add_callout,
    add_code_snippet, add_image_with_caption, set_cell_background, set_cell_margins
)

def add_frontmatter(doc):
    # -------------------------------------------------------------
    # 1. TRANG BÌA CHÍNH (COVER PAGE)
    # -------------------------------------------------------------
    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ.paragraph_format.space_before = Pt(0)
    p_univ.paragraph_format.space_after = Pt(2)
    r = p_univ.add_run("ĐẠI HỌC THÁI NGUYÊN\nTRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG\nKHOA CÔNG NGHỆ THÔNG TIN")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True

    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_after = Pt(20)
    r_div = p_div.add_run("--------------------***--------------------")
    r_div.font.name = 'Times New Roman'
    r_div.font.size = Pt(12)

    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_after = Pt(24)
    r_logo = p_logo.add_run("[ BÁO CÁO DỰ ÁN HỌC PHẦN HỌC MÁY ]")
    r_logo.font.name = 'Times New Roman'
    r_logo.font.size = Pt(14)
    r_logo.font.bold = True
    r_logo.font.color.rgb = RGBColor(16, 44, 87)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("BÁO CÁO ĐỒ ÁN / DỰ ÁN HỌC PHẦN\n")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(16)
    r_title.font.bold = True

    r_sub = p_title.add_run("NGHIÊN CỨU, XÂY DỰNG HỆ THỐNG PHÂN TÍCH QUAN ĐIỂM ĐA DIỆN (JOINT ABSA) VÀ LỌC NGHỊCH NHÃN PHẢN HỒI NGƯỜI DÙNG ỨNG DỤNG DI ĐỘNG TẠI VIỆT NAM")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(15)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(180, 40, 40)

    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.paragraph_format.space_before = Pt(24)
    p_info.paragraph_format.space_after = Pt(28)
    r_info = p_info.add_run(
        "HỌC PHẦN: HỌC MÁY (MACHINE LEARNING)\n"
        "MÃ HỌC PHẦN: CMP312 | LỚP HỌC PHẦN: CNTT K22B & K22C\n"
        "HỌC KỲ I - NĂM HỌC 2026 - 2027"
    )
    r_info.font.name = 'Times New Roman'
    r_info.font.size = Pt(12)
    r_info.font.bold = True

    t_box = doc.add_table(rows=1, cols=1)
    t_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_box = t_box.rows[0].cells[0]
    c_box.width = Inches(6.0)
    set_cell_background(c_box, "F8F9FA")
    set_cell_margins(c_box, 140, 140, 180, 180)
    p_box = c_box.paragraphs[0]
    p_box.paragraph_format.line_spacing = 1.3
    r_b = p_box.add_run(
        "GIẢNG VIÊN HƯỚNG DẪN:\n"
        "    ThS. HÀ THỊ THANH - Bộ môn Khoa học Máy tính\n\n"
        "NHÓM SINH VIÊN THỰC HIỆN: NHÓM 12\n"
        "    1. Lê Hồng Sơn       - MSV: DTC235200647 (Trưởng nhóm)\n"
        "    2. Lưu Thị Khánh Ly  - MSV: DTC235200483\n"
        "    3. Ngô Thị Sinh      - MSV: DTC235200645\n"
        "    4. Nguyễn Thanh Tùng - MSV: DTC235200811"
    )
    r_b.font.name = 'Times New Roman'
    r_b.font.size = Pt(11.5)
    r_b.font.bold = True

    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_loc.paragraph_format.space_before = Pt(40)
    r_loc = p_loc.add_run("THÁI NGUYÊN, NĂM 2026")
    r_loc.font.name = 'Times New Roman'
    r_loc.font.size = Pt(12)
    r_loc.font.bold = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. LỜI CẢM ƠN & LỜI CAM ĐOAN
    # -------------------------------------------------------------
    add_heading_1(doc, "LỜI CẢM ƠN")
    add_body_p(doc, "Lời đầu tiên, toàn thể thành viên Nhóm 12 xin bày tỏ lòng biết ơn sâu sắc và chân thành nhất tới Giảng viên hướng dẫn - ThS. Hà Thị Thanh, Giảng viên Bộ môn Khoa học Máy tính, Khoa Công nghệ Thông tin, Trường Đại học Công nghệ Thông tin và Truyền thông - Đại học Thái Nguyên.")
    add_body_p(doc, "Trong suốt quá trình học tập học phần Học máy (Machine Learning) và thực hiện dự án này, cô đã luôn tận tình truyền đạt những kiến thức nền tảng quý báu, định hướng phương pháp luận khoa học, kiên nhẫn chỉ dẫn từng cơ chế thuật toán từ đại số tuyến tính, lý thuyết xác suất thống kê đến các mô hình học máy nâng cao. Sự đồng hành, góp ý sát sao và những phản biện học thuật sắc bén của cô chính là động lực to lớn giúp nhóm không ngừng hoàn thiện đồ án, vượt qua các thách thức phức tạp về tiền xử lý ngôn ngữ tiếng Việt và tối ưu hóa hệ thống.")
    add_body_p(doc, "Nhóm cũng xin trân trọng cảm ơn Ban Giám hiệu Nhà trường, Ban Chủ nhiệm Khoa Công nghệ Thông tin cùng các thầy cô giáo trong Bộ môn Khoa học Máy tính đã tạo điều kiện học tập, nghiên cứu và trang bị cơ sở vật chất, hệ thống tài liệu giáo trình chuẩn mực để sinh viên có cơ hội rèn luyện và tiếp cận các bài toán thực tiễn.")
    add_body_p(doc, "Dù đã nỗ lực hết mình với tinh thần làm việc nghiêm túc, khoa học và cặn kẽ, đồ án khó tránh khỏi những thiếu sót nhất định do kiến thức và kinh nghiệm thực tế của nhóm sinh viên vẫn đang trong quá trình tích lũy. Nhóm 12 rất mong tiếp tục nhận được những ý kiến đóng góp, chỉ dẫn quý báu từ cô giáo và hội đồng phản biện để đề tài ngày càng hoàn thiện hơn nữa.")

    add_heading_1(doc, "LỜI CAM ĐOAN")
    add_body_p(doc, "Nhóm 12 xin cam đoan rằng công trình nghiên cứu và báo cáo dự án học phần Học máy với đề tài: \"Phân tích quan điểm phản hồi của người dùng về ứng dụng di động tại Việt Nam\" là kết quả nghiên cứu độc lập, trung thực của các thành viên trong nhóm dưới sự hướng dẫn trực tiếp của ThS. Hà Thị Thanh.")
    add_body_p(doc, "Toàn bộ số liệu thực nghiệm (14.910 đánh giá), các bảng thống kê mô tả, ma trận nhầm lẫn, biểu đồ trực quan hóa, bộ lọc khử nhiễu nghịch nhãn, mã nguồn huấn luyện mô hình, kiểm định chéo và mã nguồn xây dựng dịch vụ API/Dashboard đều được nhóm tự thiết kế, lập trình và thực thi thực tế trên môi trường máy tính tính toán cá nhân, không sao chép bất kỳ báo cáo hay kết quả có sẵn nào.")
    add_body_p(doc, "Các tài liệu tham khảo, trích dẫn lý thuyết từ các công trình nghiên cứu, sách chuyên khảo và các bài báo khoa học trong nước và quốc tế đều được ghi chú nguồn và trích dẫn rõ ràng, chuẩn mực theo quy định học thuật.")
    add_body_p(doc, "Nhóm 12 xin chịu hoàn toàn trách nhiệm trước Pháp luật, Nhà trường và Bộ môn nếu xảy ra bất kỳ sự vi phạm nào về tính trung thực của số liệu và quyền tác giả trong báo cáo này.")

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(16)
    r_s = p_sig.add_run("Thái Nguyên, ngày 26 tháng 11 năm 2026\nĐại diện Nhóm 12 - Trưởng nhóm\n\n\n\nLê Hồng Sơn")
    r_s.font.name = 'Times New Roman'
    r_s.font.size = Pt(12)
    r_s.font.bold = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # 3. BẢNG PHÂN CÔNG NHIỆM VỤ THÀNH VIÊN
    # -------------------------------------------------------------
    add_heading_1(doc, "PHÂN CÔNG NHIỆM VỤ CÁC THÀNH VIÊN")
    
    add_heading_2(doc, "Bảng phân công nhiệm vụ chi tiết thành viên Nhóm 12")
    add_body_p(doc, "Dự án được triển khai với sự tham gia của 4 thành viên thuộc lớp CNTT K22B và K22C, phân công nhiệm vụ chuyên môn hóa theo đúng đề cương nghiên cứu:")

    t_assign = doc.add_table(rows=5, cols=5)
    t_assign.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_ass = [Inches(0.6), Inches(1.2), Inches(1.4), Inches(2.2), Inches(0.8)]
    headers_ass = ["STT", "Mã sinh viên", "Họ và tên", "Nhiệm vụ đảm nhiệm trong dự án", "Đánh giá"]
    
    hdr_row = t_assign.rows[0]
    for j, h in enumerate(headers_ass):
        c = hdr_row.cells[j]
        c.width = w_ass[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 80, 80, 80, 80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_ass = [
        ("1", "DTC235200647", "Lê Hồng Sơn\n(Trưởng nhóm)", "• Quản lý tiến độ dự án, phân công công việc.\n• Thiết kế pipeline Tiền xử lý dữ liệu và bộ lọc Khử nhiễu nghịch nhãn (Sarcasm & Rating Audit).\n• Nghiên cứu cơ sở toán học và Lựa chọn mô hình tối ưu (LinearSVC, Logistic Regression).", "100% (Hoàn thành xuất sắc)"),
        ("2", "DTC235200483", "Lưu Thị Khánh Ly", "• Thiết kế kịch bản và công cụ Thu thập dữ liệu phản hồi (14.910 mẫu từ 8 ứng dụng).\n• Thực hiện Phân tích khám phá dữ liệu EDA chuyên sâu, vẽ biểu đồ phân bố rating, độ dài từ và tần suất n-gram.", "100% (Hoàn thành xuất sắc)"),
        ("3", "DTC235200645", "Ngô Thị Sinh", "• Thiết lập quy trình Đánh giá mô hình học máy (5-Fold Cross-Validation, GridSearchCV).\n• Tính toán các chỉ số Accuracy, Precision, Recall, Macro F1, Latency và thực hiện Phân tích lỗi (Error Analysis 20 ca mẫu).", "100% (Hoàn thành xuất sắc)"),
        ("4", "DTC235200811", "Nguyễn Thanh Tùng", "• Đóng gói mô hình và Triển khai bài toán thực tế.\n• Lập trình dịch vụ Microservice RESTful API bằng FastAPI với độ trễ siêu thấp (< 0.3 ms/mẫu).\n• Xây dựng Dashboard tương tác người dùng Streamlit hoàn chỉnh.", "100% (Hoàn thành xuất sắc)")
    ]

    for i, row in enumerate(data_ass):
        r_el = t_assign.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_ass[j]
            set_cell_margins(c, 60, 60, 60, 60)
            if i % 2 == 1:
                set_cell_background(c, "F9FBFD")
            p = c.paragraphs[0]
            if j in [0, 1, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9)
            if j == 2 and "Trưởng nhóm" in val:
                r.font.bold = True

    add_body_p(doc, "\nBảng 0.1: Phân công nhiệm vụ chi tiết các thành viên Nhóm 12")

    doc.add_page_break()

    # -------------------------------------------------------------
    # 4. DANH MỤC TỪ VIẾT TẮT VÀ KÝ HIỆU TOÁN HỌC
    # -------------------------------------------------------------
    add_heading_1(doc, "DANH MỤC CÁC TỪ VIẾT TẮT VÀ THUẬT NGỮ")
    
    t_abbr = doc.add_table(rows=16, cols=3)
    t_abbr.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_abb = [Inches(1.2), Inches(2.2), Inches(2.8)]
    headers_abb = ["Viết tắt", "Thuật ngữ Tiếng Anh", "Ý nghĩa / Giải thích trong đề tài"]

    hdr_a = t_abbr.rows[0]
    for j, h in enumerate(headers_abb):
        c = hdr_a.cells[j]
        c.width = w_abb[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 70, 70, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_abb = [
        ("ML", "Machine Learning", "Học máy - Ngành con của Trí tuệ nhân tạo."),
        ("NLP", "Natural Language Processing", "Xử lý ngôn ngữ tự nhiên."),
        ("SA", "Sentiment Analysis", "Phân tích quan điểm / Phân tích cảm xúc văn bản."),
        ("ABSA", "Aspect-Based Sentiment Analysis", "Phân tích quan điểm dựa trên khía cạnh nghiệp vụ."),
        ("TF-IDF", "Term Frequency - Inverse Document Frequency", "Độ đo tần suất từ kết hợp nghịch đảo tần suất văn bản."),
        ("SVM", "Support Vector Machines", "Máy vector hỗ trợ - Thuật toán phân lớp lề cực đại."),
        ("LinearSVC", "Linear Support Vector Classifier", "Mô hình SVM tuyến tính dựa trên thư viện tối ưu LIBLINEAR."),
        ("MNB", "Multinomial Naive Bayes", "Bộ phân lớp Bayes thơ ngây đa thức."),
        ("LR", "Logistic Regression", "Hồi quy Logistic phân loại nhị phân / đa lớp."),
        ("RF", "Random Forest", "Rừng ngẫu nhiên - Thuật toán học kết hợp Bagging."),
        ("CRF", "Conditional Random Fields", "Trường ngẫu nhiên có điều kiện dùng tách từ tiếng Việt."),
        ("EDA", "Exploratory Data Analysis", "Phân tích khám phá dữ liệu."),
        ("KKT", "Karush-Kuhn-Tucker", "Hệ điều kiện tối ưu bậc một trong bài toán quy hoạch phi tuyến."),
        ("OOB", "Out-Of-Bag", "Tập mẫu ngoài bao dùng ước lượng sai số trong Random Forest."),
        ("PII", "Personally Identifiable Information", "Thông tin định danh cá nhân (SĐT, Email, Tên) cần ẩn danh.")
    ]

    for i, row in enumerate(data_abb):
        r_el = t_abbr.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_abb[j]
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
            r.font.size = Pt(9)

    add_heading_2(doc, "Danh mục các Ký hiệu Toán học sử dụng trong Báo cáo")
    
    t_math = doc.add_table(rows=13, cols=3)
    t_math.alignment = WD_TABLE_ALIGNMENT.CENTER
    w_mat = [Inches(1.2), Inches(2.2), Inches(2.8)]
    headers_mat = ["Ký hiệu", "Tên gọi toán học", "Mô tả ý nghĩa trong mô hình"]

    hdr_m = t_math.rows[0]
    for j, h in enumerate(headers_mat):
        c = hdr_m.cells[j]
        c.width = w_mat[j]
        set_cell_background(c, "102C57")
        set_cell_margins(c, 70, 70, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_mat = [
        ("D", "Dataset", "Tập dữ liệu huấn luyện gồm N cặp mẫu (x_i, y_i)."),
        ("x_i ∈ R^d", "Feature Vector", "Vector đặc trưng văn bản thứ i trong không gian d = 24.619 chiều."),
        ("y_i ∈ {-1, +1}", "Class Label", "Nhãn cảm xúc (y = +1: Tích cực, y = -1: Tiêu cực)."),
        ("w ∈ R^d", "Weight Vector", "Vector trọng số pháp tuyến của siêu phẳng phân tách."),
        ("b ∈ R", "Bias / Intercept", "Hệ số định kiến / Khoảng cách dịch chuyển siêu phẳng tới gốc tọa độ."),
        ("γ (Gamma)", "Geometric Margin", "Khoảng cách lề hình học từ siêu phẳng tới điểm dữ liệu gần nhất."),
        ("ξ_i (Xi)", "Slack Variable", "Biến bù trượt sai số lỏng lẻo trong bài toán Soft-Margin SVM."),
        ("C > 0", "Penalty Hyperparameter", "Siêu tham số điều chuẩn kiểm soát mức phạt sai số vi phạm lề."),
        ("α_i (Alpha)", "Lagrange Multiplier", "Nhân tử Lagrange gắn với ràng buộc mẫu thứ i."),
        ("σ(z)", "Sigmoid Function", "Hàm kích hoạt logistic ánh xạ giá trị thực về xác suất [0, 1]."),
        ("H (Hessian)", "Hessian Matrix", "Ma trận đạo hàm riêng bậc hai của hàm mất mát Log-Loss."),
        ("I(·)", "Impurity Measure", "Độ vẩn đục của nút trong cây quyết định (Gini Impurity / Entropy).")
    ]

    for i, row in enumerate(data_mat):
        r_el = t_math.rows[i+1]
        for j, val in enumerate(row):
            c = r_el.cells[j]
            c.width = w_mat[j]
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
            r.font.size = Pt(9)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 5. MỤC LỤC TỰ ĐỘNG VÀ DANH MỤC HÌNH VẼ, BẢNG BIỂU
    # -------------------------------------------------------------
    add_heading_1(doc, "MỤC LỤC TỔNG QUÁT")
    
    p_toc_note = doc.add_paragraph()
    p_toc_note.paragraph_format.line_spacing = 1.3
    p_toc_note.paragraph_format.space_after = Pt(8)
    r_tn = p_toc_note.add_run(
        "LỜI CẢM ƠN ................................................................................................................................ iii\n"
        "LỜI CAM ĐOAN ............................................................................................................................. iv\n"
        "PHÂN CÔNG NHIỆM VỤ CÁC THÀNH VIÊN ................................................................................. v\n"
        "DANH MỤC CÁC TỪ VIẾT TẮT VÀ THUẬT NGỮ ............................................................................. vii\n"
        "DANH MỤC CÁC KÝ HIỆU TOÁN HỌC ........................................................................................... viii\n"
        "DANH MỤC CÁC BẢNG BIỂU ........................................................................................................... x\n"
        "DANH MỤC CÁC HÌNH VẼ VÀ ĐỒ THỊ .............................................................................................. xi\n\n"
        "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN BÀI TOÁN ............................................................. 1\n"
        "    1.1. Khái quát về Học máy và Xử lý ngôn ngữ tự nhiên (NLP) ........................................................ 1\n"
        "    1.2. Quy trình thực hiện dự án học máy tiêu chuẩn ................................................................. 4\n"
        "    1.3. Sự đánh đổi giữa Thiên lệch và Phương sai (Bias - Variance Tradeoff) .................................... 6\n"
        "    1.4. Bối cảnh kinh tế số và Tính cấp thiết của đề tài tại Việt Nam ................................................. 9\n"
        "    1.5. Thách thức đặc thù trong xử lý ngôn ngữ tự nhiên Tiếng Việt ................................................. 11\n"
        "    1.6. Tổng quan các nghiên cứu liên quan trên thế giới và tại Việt Nam .......................................... 13\n"
        "    1.7. Các điểm đổi mới sáng tạo và giải pháp công nghệ vượt trội của Đề tài ................................. 15\n\n"
        "CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ CƠ SỞ TOÁN HỌC CÁC MÔ HÌNH ............................ 17\n"
        "    2.1. Quy trình Tiền xử lý dữ liệu văn bản tiếng Việt đa tầng ........................................................ 17\n"
        "    2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm ....................................... 20\n"
        "    2.3. Cơ sở toán học Bộ phân loại Naive Bayes ............................................................................ 23\n"
        "    2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2 .............................................................. 25\n"
        "    2.5. Cơ sở toán học Máy vector hỗ trợ - LinearSVC .................................................................... 27\n"
        "    2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên (Random Forest) .................................................... 30\n"
        "    2.7. Phương pháp luận Phân tích quan điểm theo khía cạnh (Joint ABSA) ....................................... 32\n"
        "    2.8. Hệ thống độ đo đánh giá hiệu năng mô hình (Evaluation Metrics) ........................................... 34\n\n"
        "CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ HỆ THỐNG ..................................................... 36\n"
        "    3.1. Thu thập, phân tích và trực quan hóa dữ liệu (EDA) ............................................................ 36\n"
        "    3.2. Tiền xử lý dữ liệu và Khử nhiễu nghịch nhãn ..................................................................... 40\n"
        "    3.3. Huấn luyện các mô hình phân lớp học máy ........................................................................... 42\n"
        "    3.4. Tìm mô hình tốt nhất và Tinh chỉnh siêu tham số ............................................................... 43\n"
        "    3.5. Biện luận khoa học chuyên sâu: Dựa vào đâu kết quả đó là đúng? ....................................... 45\n"
        "    3.6. Đánh giá chi tiết và Phân tích lỗi (Error Analysis) .............................................................. 47\n"
        "    3.7. Dự đoán trên dữ liệu mới và Triển khai hệ thống ............................................................... 50\n\n"
        "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN ................................................................................................ 53\n"
        "    1. Kết quả đạt được của Đồ án .................................................................................................... 53\n"
        "    2. Đối chiếu mức độ đáp ứng Chuẩn đầu ra học phần (CĐR HP) ..................................................... 53\n"
        "    3. Hạn chế còn tồn tại và Bài học kinh nghiệm ............................................................................ 55\n"
        "    4. Hướng phát triển và mở rộng trong tương lai ........................................................................... 55\n"
        "TÀI LIỆU THAM KHẢO ....................................................................................................................... 56\n"
        "PHỤ LỤC: MÃ NGUỒN CÁC MÔ-ĐUN TRIỂN KHAI ........................................................................... 58"
    )
    r_tn.font.name = 'Times New Roman'
    r_tn.font.size = Pt(10)

    doc.add_page_break()
