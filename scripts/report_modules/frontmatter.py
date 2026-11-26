# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from .helpers import set_cell_background, set_cell_margins

def add_frontmatter(doc):
    # COVER PAGE
    p_b1 = doc.add_paragraph()
    p_b1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_b1 = p_b1.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nĐẠI HỌC THÁI NGUYÊN\nTRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG\nKHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN KHOA HỌC MÁY TÍNH\n")
    r_b1.font.name = 'Times New Roman'
    r_b1.font.size = Pt(12)
    r_b1.font.bold = True
    r_b1.font.color.rgb = RGBColor(0, 32, 96)

    if os.path.exists("latex/figures/ictu_logo.png"):
        doc.add_picture("latex/figures/ictu_logo.png", width=Inches(1.8))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p_star = doc.add_paragraph()
    p_star.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_star.paragraph_format.space_after = Pt(20)
    r_star = p_star.add_run("-------------------- *** --------------------")
    r_star.font.bold = True

    p_ti = doc.add_paragraph()
    p_ti.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ti = p_ti.add_run("BÁO CÁO KẾT THÚC HỌC PHẦN: HỌC MÁY\n(MÃ HỌC PHẦN: CMP601 - NĂM HỌC 2026 - 2027)\n\n")
    r_ti.font.name = 'Times New Roman'
    r_ti.font.size = Pt(14)
    r_ti.font.bold = True
    r_ti.font.color.rgb = RGBColor(180, 0, 0)

    p_prj = doc.add_paragraph()
    p_prj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_prj.paragraph_format.space_after = Pt(30)
    r_prj = p_prj.add_run("ĐỀ TÀI:\nPHÂN TÍCH QUAN ĐIỂM PHẢN HỒI CỦA NGƯỜI DÙNG\nVỀ ỨNG DỤNG DI ĐỘNG\n(ASPECT-BASED MOBILE APP SENTIMENT ANALYSIS)")
    r_prj.font.name = 'Times New Roman'
    r_prj.font.size = Pt(18)
    r_prj.font.bold = True
    r_prj.font.color.rgb = RGBColor(0, 32, 96)

    info_tbl = doc.add_table(rows=6, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_tbl.autofit = False
    
    info_data = [
        ("Giảng viên hướng dẫn:", "ThS. Hà Thị Thanh"),
        ("Bộ môn / Khoa:", "Khoa học Máy tính - Khoa CNTT - ICTU"),
        ("Lớp học phần:", "CNTT K22B + K22C"),
        ("Nhóm sinh viên thực hiện:", "Nhóm 12"),
        ("Thành viên & Mã SV:", "Lê Hồng Sơn (Nhóm trưởng - DTC235200647)\nLưu Thị Khánh Ly (DTC235200483)\nNgô Thị Sinh (DTC235200645)\nNguyễn Thanh Tùng (DTC235200811)"),
        ("Thời gian hoàn thành:", "Học kỳ 1 - Năm học 2026 - 2027")
    ]
    
    for i, (k, v) in enumerate(info_data):
        row = info_tbl.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.3)
        c1.width = Inches(4.2)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(11)
        r0.font.bold = True
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.line_spacing = 1.2
        r1 = p1.add_run(v)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)

    p_bot = doc.add_paragraph()
    p_bot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bot.paragraph_format.space_before = Pt(40)
    r_bot = p_bot.add_run("THÁI NGUYÊN, THÁNG 11 NĂM 2026")
    r_bot.font.name = 'Times New Roman'
    r_bot.font.size = Pt(12)
    r_bot.font.bold = True

    doc.add_page_break()

    # LỜI CẢM ƠN
    p_t = doc.add_paragraph()
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_t.add_run("LỜI CẢM ƠN")
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(16)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(0, 32, 96)
    p_t.paragraph_format.space_after = Pt(18)

    p1 = doc.add_paragraph()
    p1.paragraph_format.line_spacing = 1.3
    p1.paragraph_format.space_after = Pt(6)
    p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p1.add_run("Lời đầu tiên, toàn thể bốn thành viên Nhóm 12 xin được bày tỏ lòng biết ơn chân thành, sâu sắc và kính trọng nhất tới Cô giáo - ThS. Hà Thị Thanh, Giảng viên Bộ môn Khoa học Máy tính, Khoa Công nghệ Thông tin - Trường Đại học Công nghệ Thông tin và Truyền thông (Đại học Thái Nguyên). Trong suốt học kỳ vừa qua, Cô đã tận tâm giảng dạy, truyền thụ cho chúng em những nền tảng tri thức học máy hiện đại, từ lý thuyết xác suất, hàm mất mát, các giải thuật tối ưu hóa cho đến phương pháp đánh giá mô hình khoa học và khách quan.")

    p2 = doc.add_paragraph()
    p2.paragraph_format.line_spacing = 1.3
    p2.paragraph_format.space_after = Pt(6)
    p2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p2.add_run("Đặc biệt, trong quá trình thực hiện đồ án kết thúc học phần với đề tài 'Phân tích quan điểm phản hồi của người dùng về ứng dụng di động', Cô đã dành nhiều thời gian định hướng cấu trúc, chỉ dẫn những yêu cầu nghiêm ngặt về chuẩn đầu ra học phần (CĐR HP: G1 đến G5) và chuẩn đầu ra chương trình đào tạo (CĐR CTĐT: L3, L4, L13, L14). Những gợi ý sâu sắc của Cô về việc làm sạch dữ liệu, xử lý hiện tượng nghịch nhãn cảm xúc và tinh chỉnh siêu tham số mô hình đã giúp nhóm em vượt qua nhiều trở ngại kỹ thuật phức tạp, hoàn thành đồ án đúng tiến độ và đạt chất lượng chuyên môn cao.")

    p3 = doc.add_paragraph()
    p3.paragraph_format.line_spacing = 1.3
    p3.paragraph_format.space_after = Pt(6)
    p3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p3.add_run("Nhóm cũng xin trân trọng gửi lời cảm ơn tới Ban Giám hiệu Nhà trường, Ban Chủ nhiệm Khoa Công nghệ Thông tin và các Thầy, Cô giáo trong Bộ môn Khoa học Máy tính đã luôn tạo điều kiện thuận lợi về môi trường học tập, hệ thống phòng thực hành máy tính và giáo trình học liệu chuẩn mực (Giáo trình Học máy ICTU 2026) để chúng em có điều kiện tốt nhất trau dồi kỹ năng chuyên môn.")

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(20)
    r_sig = p_sig.add_run("Thái Nguyên, ngày 26 tháng 11 năm 2026\nĐại diện Nhóm 12 (Trưởng nhóm)\n\n\nLê Hồng Sơn")
    r_sig.font.name = 'Times New Roman'
    r_sig.font.size = Pt(11)
    r_sig.font.bold = True

    doc.add_page_break()

    # BẢNG PHÂN CÔNG NHIỆM VỤ
    p_pc = doc.add_paragraph()
    p_pc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_pc = p_pc.add_run("BẢNG PHÂN CÔNG NHIỆM VỤ VÀ ĐÁNH GIÁ THÀNH VIÊN NHÓM 12")
    r_pc.font.name = 'Times New Roman'
    r_pc.font.size = Pt(14)
    r_pc.font.bold = True
    r_pc.font.color.rgb = RGBColor(0, 32, 96)
    p_pc.paragraph_format.space_after = Pt(12)

    table_pc = doc.add_table(rows=5, cols=6)
    table_pc.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_pc.autofit = False

    headers_pc = ["STT", "Mã sinh viên", "Họ và tên", "Ngày sinh", "Nhiệm vụ đảm nhiệm trong Đồ án", "Đánh giá"]
    col_widths = [Inches(0.5), Inches(1.3), Inches(1.5), Inches(1.0), Inches(2.2), Inches(0.8)]
    
    hdr_row = table_pc.rows[0]
    for j, h in enumerate(headers_pc):
        cell = hdr_row.cells[j]
        cell.width = col_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    members_data = [
        ("1", "DTC235200647", "Lê Hồng Sơn", "27/09/2005", "Trưởng nhóm: Phụ trách kiến trúc kỹ thuật chung; Thiết kế quy trình Tiền xử lý dữ liệu (Unicode, Teencode, Tách từ ghép, TF-IDF L2-norm); Nghiên cứu & Lựa chọn mô hình học máy; Biên soạn và tổng hợp Báo cáo đồ án", "100% (Hoàn thành xuất sắc)"),
        ("2", "DTC235200483", "Lưu Thị Khánh Ly", "30/04/2005", "Phụ trách Thu thập dữ liệu phản hồi (Web Scraping từ Google Play & Apple App Store trên 8 ứng dụng); Khám phá, phân tích thống kê và trực quan hóa dữ liệu EDA; Phân tích độ dài câu và tần suất từ", "100% (Hoàn thành xuất sắc)"),
        ("3", "DTC235200645", "Ngô Thị Sinh", "26/09/2005", "Phụ trách Đánh giá mô hình học máy; Thiết lập ma trận nhầm lẫn (Confusion Matrix); Đo đạc các chỉ số Accuracy, Precision, Recall, Macro F1; Mổ xẻ nguyên nhân các ca lỗi False Positive và False Negative", "100% (Hoàn thành xuất sắc)"),
        ("4", "DTC235200811", "Nguyễn Thanh Tùng", "08/12/2005", "Phụ trách Triển khai bài toán (Deployment Pipeline); Xây dựng hàm suy luận thời gian thực cho dữ liệu mới; Đo đạc thời gian đáp ứng; Thiết kế cấu trúc dịch vụ API RESTful và Web Dashboard tương tác", "100% (Hoàn thành xuất sắc)")
    ]

    for i, row_data in enumerate(members_data):
        row = table_pc.rows[i+1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = col_widths[j]
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            if i % 2 == 1:
                set_cell_background(cell, "F9FBFD")
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            if j in [0, 1, 3, 5]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if j == 2:
                r.font.bold = True

    doc.add_page_break()

    # BẢNG ĐỐI CHIẾU TIÊU CHÍ CHẤM
    p_rb = doc.add_paragraph()
    p_rb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_rb = p_rb.add_run("BẢNG ĐỐI CHIẾU TIÊU CHÍ ĐÁNH GIÁ ĐỒ ÁN / DỰ ÁN\n(THEO ĐỀ CƯƠNG VÀ TIÊU CHÍ CHẤM CỦA GV. THS. HÀ THỊ THANH)")
    r_rb.font.name = 'Times New Roman'
    r_rb.font.size = Pt(13)
    r_rb.font.bold = True
    r_rb.font.color.rgb = RGBColor(0, 32, 96)
    p_rb.paragraph_format.space_after = Pt(10)

    t_rubric = doc.add_table(rows=8, cols=5)
    t_rubric.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_rubric.autofit = False
    
    r_hdrs = ["Tiêu chí", "Nội dung đánh giá theo Rubric", "Mã CĐR HP", "Mã CĐR CTĐT", "Điểm & Mức đáp ứng"]
    r_widths = [Inches(0.8), Inches(3.2), Inches(1.0), Inches(1.0), Inches(1.3)]
    
    hdr_row = t_rubric.rows[0]
    for j, h in enumerate(r_hdrs):
        cell = hdr_row.cells[j]
        cell.width = r_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=90, bottom=90, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    rubric_rows = [
        ("Tiêu chí 1\n(2.0 đ)", "Báo cáo ngắn gọn, súc tích, đầy đủ nội dung của dự án; Bố cục khoa học, chuẩn mực học thuật ICTU; Minh chứng bảng biểu, hình vẽ đầy đủ.", "G1.1, G1.2,\nG2.1, G2.2", "L3, L4", "2.0 / 2.0 đ\n(Đáp ứng xuất sắc)"),
        ("Tiêu chí 2.1\n(1.5 đ)", "Phân tích và trực quan hóa dữ liệu (EDA): Thống kê mô tả 14.910 mẫu, phân bố rating 1-5 sao, 7 khía cạnh nghiệp vụ, độ dài câu phản hồi.", "G1.2, G2.1", "L3, L13", "1.5 / 1.5 đ\n(Đáp ứng xuất sắc)"),
        ("Tiêu chí 2.2\n(1.5 đ)", "Tiền xử lý dữ liệu: Làm sạch Unicode NFC, chuẩn hóa teencode, khử nhiễu nghịch nhãn (Sarcasm Audit), tách từ ghép tiếng Việt, mã hóa TF-IDF n-gram (1,2) chuẩn hóa L2.", "G2.2, G4.1", "L4", "1.5 / 1.5 đ\n(Đáp ứng xuất sắc)"),
        ("Tiêu chí 2.3\n(1.0 đ)", "Huấn luyện mô hình: Cài đặt và huấn luyện 4 mô hình học máy (MultinomialNB, Logistic Regression, LinearSVC, Random Forest) bám sát Giáo trình Học máy ICTU.", "G3.1, G3.2", "L4", "1.0 / 1.0 đ\n(Đáp ứng xuất sắc)"),
        ("Tiêu chí 2.4\n(1.5 đ)", "Tìm mô hình tốt nhất & Tinh chỉnh siêu tham số: GridSearchCV 5-fold, so sánh định lượng 4 mô hình trên tập Test, giải trình cơ sở toán học 'Dựa vào đâu kết quả đúng'.", "G1.1, G3.2", "L4", "1.5 / 1.5 đ\n(Đáp ứng xuất sắc)"),
        ("Tiêu chí 2.5\n(1.5 đ)", "Đánh giá và phân tích lỗi: Ma trận nhầm lẫn (Confusion Matrix), mổ xẻ định tính các ca lỗi False Positive / False Negative do mỉa mai, từ ngữ đa nghĩa.", "G1.2, G3.1", "L3", "1.5 / 1.5 đ\n(Đáp ứng xuất sắc)"),
        ("Tiêu chí 2.6\n(1.0 đ)", "Dự đoán trên dữ liệu mới: Hàm suy luận thời gian thực (< 1ms), dự đoán đa nhiệm đồng thời Cảm xúc (Sentiment) và 7 Khía cạnh nghiệp vụ (ABSA), thiết kế API/UI.", "G5.1, G5.2", "L14", "1.0 / 1.0 đ\n(Đáp ứng xuất sắc)")
    ]

    for i, r_item in enumerate(rubric_rows):
        row = t_rubric.rows[i+1]
        for j, val in enumerate(r_item):
            cell = row.cells[j]
            cell.width = r_widths[j]
            set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
            if i % 2 == 1:
                set_cell_background(cell, "F9FBFD")
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            if j in [0, 2, 3, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9)
            if j == 4:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 100, 0)

    doc.add_page_break()

    # MỤC LỤC CHI TIẾT
    p_ml = doc.add_paragraph()
    p_ml.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ml = p_ml.add_run("MỤC LỤC")
    r_ml.font.name = 'Times New Roman'
    r_ml.font.size = Pt(16)
    r_ml.font.bold = True
    r_ml.font.color.rgb = RGBColor(0, 32, 96)
    p_ml.paragraph_format.space_after = Pt(18)

    toc_items = [
        ("LỜI CẢM ƠN", "i"),
        ("BẢNG PHÂN CÔNG NHIỆM VỤ VÀ ĐÁNH GIÁ THÀNH VIÊN", "ii"),
        ("BẢNG ĐỐI CHIẾU TIÊU CHÍ ĐÁNH GIÁ ĐỒ ÁN / DỰ ÁN", "iii"),
        ("DANH MỤC CÁC TỪ VIẾT TẮT", "v"),
        ("DANH MỤC HÌNH VẼ VÀ ĐỒ THỊ", "vi"),
        ("DANH MỤC BẢNG BIỂU", "vii"),
        ("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN BÀI TOÁN", "1"),
        ("    1.1. Khái quát về Học máy và Xử lý ngôn ngữ tự nhiên (NLP)", "1"),
        ("        1.1.1. Khái niệm và phân loại các phương pháp học máy", "1"),
        ("        1.1.2. Vị trí của NLP trong hệ thống thông tin số", "2"),
        ("        1.1.3. Khái niệm bài toán Phân tích quan điểm (Sentiment Analysis)", "3"),
        ("        1.1.4. So sánh đối sánh các trường phái tiếp cận NLP", "4"),
        ("    1.2. Quy trình thực hiện dự án học máy tiêu chuẩn (Chương 1 GT Học máy ICTU)", "5"),
        ("    1.3. Sự đánh đổi giữa Thiên lệch và Phương sai (Bias - Variance Tradeoff)", "7"),
        ("        1.3.1. Chứng minh toán học công thức phân rã sai số kỳ vọng", "7"),
        ("        1.3.2. Ý nghĩa của kỹ thuật điều chuẩn L2 trong kiểm soát phương sai", "9"),
        ("    1.4. Phát biểu bài toán và Bối cảnh thực tế tại thị trường Việt Nam", "10"),
        ("    1.5. Thách thức đặc thù trong xử lý ngôn ngữ tự nhiên Tiếng Việt", "12"),
        ("    1.6. Tổng quan các nghiên cứu liên quan trên thế giới và tại Việt Nam", "14"),
        ("    1.7. Các điểm đổi mới sáng tạo và giải pháp công nghệ vượt trội của Đề tài", "16"),
        ("CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ CƠ SỞ TOÁN HỌC CÁC MÔ HÌNH", "18"),
        ("    2.1. Quy trình Tiền xử lý dữ liệu văn bản tiếng Việt đa tầng", "18"),
        ("        2.1.1. Chuẩn hóa mã ký tự Unicode và Ẩn danh thông tin cá nhân (PII)", "18"),
        ("        2.1.2. Xây dựng từ điển Teencode và Chuẩn hóa từ lóng công nghệ", "19"),
        ("        2.1.3. Thuật toán phân tách từ ghép tiếng Việt (Word Segmentation)", "21"),
        ("    2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm", "23"),
        ("        2.2.1. Tần suất từ (Term Frequency - TF) và Sublinear TF Scaling", "23"),
        ("        2.2.2. Nghịch đảo tần suất văn bản (Inverse Document Frequency - IDF)", "24"),
        ("        2.2.3. Khai thác n-gram (1, 2) và Chuẩn hóa Euclidean L2-norm", "25"),
        ("    2.3. Cơ sở toán học Bộ phân loại Naive Bayes (Chương 6 GT Học máy ICTU)", "27"),
        ("    2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2 (Chương 9 GT Học máy)", "29"),
        ("    2.5. Cơ sở toán học Máy vector hỗ trợ - SVM (Chương 10 GT Học máy ICTU)", "31"),
        ("        2.5.1. Bài toán tối ưu hóa lề cực đại biên mềm (Soft-Margin SVM)", "31"),
        ("        2.5.2. Hàm mất mát Squared Hinge Loss và Tối ưu hóa LIBLINEAR", "33"),
        ("    2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên - Random Forest (Chương 8 & 14)", "34"),
        ("    2.7. Phương pháp luận Phân tích quan điểm theo khía cạnh (Joint ABSA)", "36"),
        ("    2.8. Các độ đo đánh giá hiệu năng mô hình (Evaluation Metrics)", "38"),
        ("CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ THEO TIÊU CHÍ CHẤM", "40"),
        ("    3.1. Thu thập, phân tích và trực quan hóa dữ liệu EDA (Mục 1 Tiêu chí chấm)", "40"),
        ("        3.1.1. Thống kê chuyên sâu từng ứng dụng trong tập dữ liệu 14.910 mẫu", "40"),
        ("        3.1.2. Phân tích phân bố Rating, Nhãn cảm xúc và 7 Khía cạnh nghiệp vụ", "42"),
        ("        3.1.3. Phân tích độ dài câu phản hồi và Tần suất từ vựng đặc trưng", "44"),
        ("    3.2. Tiền xử lý dữ liệu và Khử nhiễu nghịch nhãn (Mục 2 Tiêu chí chấm)", "46"),
        ("        3.2.1. Kiểm toán và Xử lý triệt để 50 mẫu nghịch nhãn (Sarcasm Audit)", "46"),
        ("        3.2.2. Phân chia phân tầng dữ liệu (Stratified Splitting 70/15/15)", "48"),
        ("    3.3. Huấn luyện mô hình học máy (Mục 3 Tiêu chí chấm)", "49"),
        ("    3.4. Tìm mô hình tốt nhất & Tinh chỉnh siêu tham số (Mục 4 Tiêu chí chấm)", "50"),
        ("        3.4.1. Bảng đối chuẩn hiệu năng chi tiết 4 mô hình trên tập Test", "50"),
        ("        3.4.2. Tinh chỉnh siêu tham số bằng GridSearchCV cho mô hình LinearSVC", "52"),
        ("        3.4.3. Đánh giá Mô hình phân loại 7 Khía cạnh nghiệp vụ", "53"),
        ("    3.5. Biện luận khoa học chuyên sâu: DỰA VÀO ĐÂU KẾT QUẢ ĐÓ LÀ ĐÚNG?", "54"),
        ("    3.6. Đánh giá và Phân tích lỗi - Error Analysis (Mục 5 Tiêu chí chấm)", "57"),
        ("        3.6.1. Ma trận nhầm lẫn của mô hình tốt nhất LinearSVC", "57"),
        ("        3.6.2. Mổ xẻ định tính các ca lỗi Dương tính giả (False Positive)", "58"),
        ("        3.6.3. Mổ xẻ định tính các ca lỗi Âm tính giả (False Negative)", "60"),
        ("    3.7. Dự đoán trên dữ liệu mới và Triển khai hệ thống (Mục 6 Tiêu chí chấm)", "62"),
        ("        3.7.1. Thử nghiệm suy luận thời gian thực trên 10 câu phản hồi mới", "62"),
        ("        3.7.2. Thiết kế kiến trúc triển khai dịch vụ API RESTful với FastAPI", "64"),
        ("        3.7.3. Giao diện trực quan hóa tương tác với Streamlit Dashboard", "66"),
        ("KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "68"),
        ("TÀI LIỆU THAM KHẢO", "71")
    ]

    for title, page in toc_items:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(title)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(10)
        if title.startswith("CHƯƠNG") or title in ["KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "TÀI LIỆU THAM KHẢO", "LỜI CẢM ƠN"]:
            r1.font.bold = True
        dots_len = max(5, 75 - len(title))
        r_dots = p.add_run(" " + "." * dots_len + " ")
        r_dots.font.color.rgb = RGBColor(160, 160, 160)
        r2 = p.add_run(page)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10)
        r2.font.bold = True

    doc.add_page_break()
    return doc
