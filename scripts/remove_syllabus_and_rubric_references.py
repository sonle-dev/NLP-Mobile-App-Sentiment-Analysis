# -*- coding: utf-8 -*-
"""
Script: remove_syllabus_and_rubric_references.py
Removes all informal syllabus citations, page numbers ("Mục 1.7 tr. 33"),
chapter tags ("Chương X GT Học máy"), rubric points ("- 1.5 đ"),
and replaces them with pure, formal academic scientific prose.
"""

import re

def clean_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Cleaned {filepath}")

# 1. Frontmatter replacements
frontmatter_replacements = [
    # Table of contents titles
    ("(Chương 1 GT Học máy ICTU)", ""),
    ("(Chương 2 GT Học máy ICTU)", ""),
    ("(Chương 6 GT Học máy ICTU)", ""),
    ("(Chương 9 GT Học máy ICTU)", ""),
    ("(Chương 10 GT Học máy ICTU)", ""),
    ("(Chương 8 & 14 GT Học máy ICTU)", ""),
    ("(Mục 1 Tiêu chí chấm - 1.5 đ)", ""),
    ("(Mục 2 Tiêu chí chấm - 1.5 đ)", ""),
    ("(Mục 3 Tiêu chí chấm - 1.0 đ)", ""),
    ("(Mục 4 Tiêu chí chấm - 1.5 đ)", ""),
    ("(Mục 5 Tiêu chí chấm - 1.5 đ)", ""),
    ("(Mục 6 Tiêu chí chấm - 1.0 đ)", ""),
    ("Máy vector hỗ trợ - LinearSVC (Chương 10 GT Học máy ICTU)", "Máy vector hỗ trợ - LinearSVC"),
    ("Mô hình Rừng ngẫu nhiên (Chương 8 & 14 GT Học máy ICTU)", "Mô hình Rừng ngẫu nhiên (Random Forest)"),
]

# 2. Chapter 1 replacements
chapter1_replacements = [
    (
        "Theo định nghĩa kinh điển của Tom Mitchell (1997) được tái khẳng định trong Chương 1 Giáo trình Học máy ICTU (năm 2026, tr. 11 - 15) của các tác giả TS. Trần Quang Quý, TS. Ngô Hữu Huy, TS. Nguyễn Đức Bình và TS. Nguyễn Tuấn Anh: \"Một chương trình máy tính",
        "Theo định nghĩa kinh điển của Tom Mitchell (1997): \"Một chương trình máy tính"
    ),
    (
        'add_heading_2(doc, "1.2. Quy trình thực hiện dự án học máy tiêu chuẩn (Chương 1 GT Học máy ICTU)")',
        'add_heading_2(doc, "1.2. Quy trình thực hiện dự án học máy tiêu chuẩn")'
    ),
    (
        "Theo Chương 1 Giáo trình Học máy ICTU (năm 2026, tr. 16 - 22), quy trình phát triển một dự án học máy trong môi trường công nghiệp không phải là một chuỗi hành động ngẫu nhiên mà là một chu trình kỹ thuật 7 bước lặp khép kín (Iterative Engineering Pipeline).",
        "Trong môi trường công nghiệp và nghiên cứu ứng dụng, quy trình phát triển một dự án học máy là một chu trình kỹ thuật 7 bước lặp khép kín (Iterative Engineering Pipeline)."
    ),
    (
        "Theo Mục 1.7 (tr. 33 - 35) của Giáo trình Học máy ICTU, sự đánh đổi giữa Thiên lệch (Bias) và Phương sai (Variance) là nguyên lý trung tâm chi phối khả năng tổng quát hóa của mọi mô hình học máy.",
        "Trong lý thuyết học máy thống kê (Statistical Learning Theory), sự đánh đổi giữa Thiên lệch (Bias) và Phương sai (Variance) là nguyên lý toán học trung tâm chi phối khả năng tổng quát hóa của mọi mô hình học máy."
    )
]

# 3. Chapter 2 replacements
chapter2_replacements = [
    (
        'add_heading_2(doc, "2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm (Chương 2 GT Học máy ICTU)")',
        'add_heading_2(doc, "2.2. Xây dựng không gian đặc trưng bằng TF-IDF và Chuẩn hóa L2-norm")'
    ),
    (
        "Theo Chương 2 Giáo trình Học máy ICTU (năm 2026, tr. 45 - 52), để các thuật toán học máy có thể tính toán trên dữ liệu văn bản, ta cần chuyển đổi",
        "Để các thuật toán học máy có thể tính toán trên dữ liệu văn bản tự nhiên, ta cần chuyển đổi"
    ),
    (
        'add_heading_2(doc, "2.3. Cơ sở toán học Bộ phân loại Naive Bayes (Chương 6 GT Học máy ICTU)")',
        'add_heading_2(doc, "2.3. Cơ sở toán học Bộ phân loại Naive Bayes")'
    ),
    (
        "Theo Chương 6 Giáo trình Học máy ICTU (năm 2026, tr. 142 - 156), bộ phân loại Naive Bayes là",
        "Bộ phân loại Naive Bayes là"
    ),
    (
        'add_heading_2(doc, "2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2 (Chương 9 GT Học máy ICTU)")',
        'add_heading_2(doc, "2.4. Cơ sở toán học Hồi quy Logistic và Điều chuẩn L2")'
    ),
    (
        "Theo Chương 9 Giáo trình Học máy ICTU (năm 2026, tr. 215 - 230), Hồi quy Logistic (Logistic Regression) là",
        "Hồi quy Logistic (Logistic Regression) là"
    ),
    (
        'add_heading_2(doc, "2.5. Cơ sở toán học Máy vector hỗ trợ - SVM (Chương 10 GT Học máy ICTU)")',
        'add_heading_2(doc, "2.5. Cơ sở toán học Máy vector hỗ trợ (LinearSVC)")'
    ),
    (
        "Theo Chương 10 Giáo trình Học máy ICTU (năm 2026, tr. 245 - 268), Máy vector hỗ trợ (Support Vector Machines - SVM) do",
        "Máy vector hỗ trợ (Support Vector Machines - SVM) do"
    ),
    (
        'add_heading_2(doc, "2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên - Random Forest (Chương 8 & 14 GT Học máy ICTU)")',
        'add_heading_2(doc, "2.6. Cơ sở toán học Mô hình Rừng ngẫu nhiên (Random Forest)")'
    ),
    (
        "Theo Chương 8 và Chương 14 Giáo trình Học máy ICTU (năm 2026, tr. 190 - 212 & 335 - 350), Rừng ngẫu nhiên (Random Forest - RF) do",
        "Rừng ngẫu nhiên (Random Forest - RF) do"
    )
]

# 4. Chapter 3 replacements
chapter3_replacements = [
    (
        'add_heading_2(doc, "3.1. Thu thập, phân tích và trực quan hóa dữ liệu EDA (Mục 1 Tiêu chí chấm - 1.5 đ)")',
        'add_heading_2(doc, "3.1. Thu thập, phân tích và trực quan hóa dữ liệu (EDA)")'
    ),
    (
        "Tuân thủ chặt chẽ Mục 1 trong Barem Tiêu chí chấm (1.5 điểm), nhóm đã thực hiện thu thập dữ liệu tự động",
        "Trong giai đoạn đầu của dự án, nhóm đã thực hiện thu thập dữ liệu tự động"
    ),
    (
        'add_heading_2(doc, "3.2. Tiền xử lý dữ liệu và Khử nhiễu nghịch nhãn (Mục 2 Tiêu chí chấm - 1.5 đ)")',
        'add_heading_2(doc, "3.2. Tiền xử lý dữ liệu và Khử nhiễu nghịch nhãn")'
    ),
    (
        'add_heading_2(doc, "3.3. Huấn luyện mô hình học máy (Mục 3 Tiêu chí chấm - 1.0 đ)")',
        'add_heading_2(doc, "3.3. Huấn luyện các mô hình phân lớp học máy")'
    ),
    (
        "Tuân thủ Mục 3 Tiêu chí chấm (1.0 điểm), nhóm tiến hành phân chia tập dữ liệu",
        "Sau khi hoàn thành tiền xử lý, nhóm tiến hành phân chia tập dữ liệu"
    ),
    (
        'add_heading_2(doc, "3.4. Tìm mô hình tốt nhất & Tinh chỉnh siêu tham số (Mục 4 Tiêu chí chấm - 1.5 đ)")',
        'add_heading_2(doc, "3.4. Tìm mô hình tốt nhất và Tinh chỉnh siêu tham số")'
    ),
    (
        "Để tìm kiếm cấu hình tối ưu và lựa chọn mô hình tốt nhất theo Mục 4 Tiêu chí chấm (1.5 điểm), nhóm thiết lập quy trình kiểm định chéo",
        "Để tìm kiếm cấu hình tham số tối ưu và lựa chọn mô hình có khả năng tổng quát hóa cao nhất, nhóm thiết lập quy trình kiểm định chéo"
    ),
    (
        "TRỤ CỘT 4: KIỂM ĐỊNH ĐỘC LẬP NGHIÊM NGẶT TRÊN UNSEEN TEST SET THEO GIÁO TRÌNH ICTU.",
        "TRỤ CỘT 4: KIỂM ĐỊNH ĐỘC LẬP NGHIÊM NGẶT TRÊN UNSEEN TEST SET THEO NGUYÊN TẮC CÁCH LY DỮ LIỆU."
    ),
    (
        'add_heading_2(doc, "3.6. Đánh giá và Phân tích lỗi - Error Analysis (Mục 5 Tiêu chí chấm - 1.5 đ)")',
        'add_heading_2(doc, "3.6. Đánh giá chi tiết và Phân tích lỗi (Error Analysis)")'
    ),
    (
        "Tuân thủ chặt chẽ Mục 5 Tiêu chí chấm (1.5 điểm), việc đánh giá một hệ thống học máy",
        "Trong kỹ thuật học máy thực nghiệm, việc đánh giá một hệ thống không dừng lại ở các con số thống kê tổng quát,"
    ),
    (
        'add_heading_2(doc, "3.7. Dự đoán trên dữ liệu mới và Triển khai hệ thống (Mục 6 Tiêu chí chấm - 1.0 đ)")',
        'add_heading_2(doc, "3.7. Dự đoán trên dữ liệu mới và Triển khai hệ thống")'
    ),
    (
        "Tuân thủ Mục 6 Tiêu chí chấm (1.0 điểm), toàn bộ các mô hình tối ưu",
        "Sau khi hoàn thành đánh giá thực nghiệm, toàn bộ các mô hình tối ưu"
    )
]

# 5. Chapter 4 replacements
chapter4_replacements = [
    (
        "định lý phân rã sai số Bias-Variance, và kỹ thuật điều chuẩn L2 bám sát Chương 1, 2, 6, 8, 9, 10, 14 của Giáo trình Học máy ICTU (2026).",
        "định lý phân rã sai số Bias-Variance, và kỹ thuật điều chuẩn L2."
    )
]

# Execute replacements
clean_file('scripts/report_modules/frontmatter_expanded.py', frontmatter_replacements)
clean_file('scripts/report_modules/chapter1_expanded.py', chapter1_replacements)
clean_file('scripts/report_modules/chapter2_expanded.py', chapter2_replacements)
clean_file('scripts/report_modules/chapter3_expanded.py', chapter3_replacements)
clean_file('scripts/report_modules/chapter4_expanded.py', chapter4_replacements)

# Also clean the legacy files just in case
clean_file('scripts/report_modules/chapter1.py', chapter1_replacements)
clean_file('scripts/report_modules/chapter2.py', chapter2_replacements)
clean_file('scripts/report_modules/chapter3.py', chapter3_replacements)
clean_file('scripts/report_modules/chapter4.py', chapter4_replacements)
