# -*- coding: utf-8 -*-
"""
Enrichment additions for Chapter 1, Chapter 2, and Chapter 3
"""

# Let's write the enrichment module that adds deep academic content to chapter 2 and 3
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from .helpers import (
    add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_math_block, add_callout,
    add_code_snippet, add_image_with_caption, set_cell_background, set_cell_margins
)

def add_chapter2_deep_math(doc):
    add_heading_2(doc, "2.9. Phân tích toán học chuyên sâu về Không gian đặc trưng và Giảm chiều")
    add_body_p(doc, "Trong bài toán xử lý ngôn ngữ tự nhiên, không gian vector từ vựng ban đầu V chứa toàn bộ các từ ghép đơn và đôi xuất hiện trong tập huấn luyện. Với kích thước ban đầu lên tới hơn 45.000 cụm từ, ma trận dữ liệu chứa rất nhiều nhiễu do các từ hiếm (xuất hiện 1 lần do gõ sai chính tả) hoặc các từ quá phổ biến (xuất hiện ở hầu hết mọi câu). Nhóm áp dụng kỹ thuật lọc tần suất biên:")
    add_math_block(doc, "V_{lọc} = { t ∈ V | min_df ≤ df(t) ≤ max_df × |D| }", "2.24")
    add_body_p(doc, "Trong đó: min_df = 2 loại bỏ toàn bộ các từ đơn lẻ chỉ xuất hiện duy nhất 1 lần (Outlier / Typo), và max_df = 0.9 loại bỏ các từ dừng xuất hiện trong hơn 90% số văn bản. Kỹ thuật này đã giảm số chiều đặc trưng từ 45.210 xuống còn đúng d = 24.619 chiều, đồng thời nâng cao mật độ thông tin hữu ích của ma trận biểu diễn.")

    add_heading_2(doc, "2.10. Cơ sở đại số tuyến tính của Phân tách siêu phẳng trong SVM")
    add_body_p(doc, "Để hiểu rõ tại sao LinearSVC đạt hiệu năng áp đảo, ta phân tích hình học không gian Hilbert R^d với d = 24.619. Cho tập điểm dữ liệu D = {(x_i, y_i)}_{i=1}^N với y_i ∈ {-1, +1}. Siêu phẳng phân cách được định nghĩa bởi phương trình:")
    add_math_block(doc, "H = { x ∈ R^d | w^T x + b = 0 }", "2.25")
    add_body_p(doc, "Vecto pháp tuyến w vuông góc với siêu phẳng H và quyết định hướng phân tách. Khoảng cách vuông góc từ điểm x_i bất kỳ tới siêu phẳng H là:")
    add_math_block(doc, "γ_i = [ y_i (w^T x_i + b) ] / ||w||₂", "2.26")
    add_body_p(doc, "Khoảng cách lề hình học (Geometric Margin) của toàn bộ tập dữ liệu là khoảng cách từ siêu phẳng tới điểm dữ liệu gần nó nhất: γ = min_i γ_i. Để siêu phẳng nằm chính xác ở vị trí cân bằng và cách xa hai lớp nhất, bài toán tối ưu hóa lề cực đại yêu cầu cực đại hóa γ:")
    add_math_block(doc, "max_{w, b} γ  thỏa mãn: [ y_i (w^T x_i + b) ] / ||w||₂ ≥ γ,  ∀i = 1, ..., N", "2.27")
    add_body_p(doc, "Bằng cách chuẩn hóa thang đo lề hàm số (Functional Margin) sao cho min_i y_i (w^T x_i + b) = 1, bài toán trên tương đương với:")
    add_math_block(doc, "max_{w, b} (1 / ||w||₂)  <=>  min_{w, b} (1/2) ||w||₂²   thỏa mãn: y_i (w^T x_i + b) ≥ 1,  ∀i = 1, ..., N", "2.28")

    add_body_p(doc, "Khi tồn tại nhiễu hoặc dữ liệu không thể phân tách tuyến tính hoàn hảo (Linearly Inseparable), việc đưa vào các biến bù trượt sai số ξ_i ≥ 0 (Slack Variables) dẫn tới bài toán tối ưu hóa biên mềm Soft-Margin SVM (Công thức 2.13). Tại nghiệm tối ưu, theo điều kiện KKT (Karush-Kuhn-Tucker), các điểm dữ liệu được phân thành 3 nhóm rõ rệt:\n"
                  "1. Điểm nằm ngoài khoảng lề (Non-Support Vectors): y_i (w^T x_i + b) > 1 => α_i = 0. Các điểm này không đóng góp vào vector trọng số w và không ảnh hưởng tới vị trí siêu phẳng.\n"
                  "2. Điểm nằm đúng trên biên lề (Margin Support Vectors): y_i (w^T x_i + b) = 1 và ξ_i = 0 => 0 < α_i < C. Đây là các điểm mấu chốt quyết định chính xác vị trí siêu phẳng phân tách.\n"
                  "3. Điểm nằm trong khoảng lề hoặc bị phân loại sai (Non-margin Support Vectors): y_i (w^T x_i + b) < 1 và ξ_i > 0 => α_i = C. Đây là các mẫu khó hoặc mẫu nhiễu được kiểm soát bởi siêu tham số phạt C.")

    add_heading_2(doc, "2.11. So sánh lý thuyết giữa hàm Hinge Loss và Squared Hinge Loss")
    add_body_p(doc, "Trong bài toán SVM chuẩn, hàm mất mát bản lề Hinge Loss cổ điển có dạng L_1(z) = max(0, 1 - z). Tuy nhiên, hàm L_1 không có đạo hàm tại điểm z = 1 (điểm gập), đòi hỏi phải sử dụng các giải thuật tối ưu dưới đạo hàm (Subgradient Optimization) có tốc độ hội tụ chậm.")
    add_body_p(doc, "Trong thư viện `LinearSVC` của Scikit-learn (dựa trên LIBLINEAR), hàm mất mát bình phương bản lề Squared Hinge Loss L_2(z) = [max(0, 1 - z)]² được sử dụng. Hàm L_2(z) khả vi liên tục bậc nhất trên toàn bộ miền xác định với đạo hàm:")
    add_math_block(doc, "L'_2(z) = -2 (1 - z)  khi z < 1;  ngược lại bằng 0", "2.29")
    add_body_p(doc, "Tính chất khả vi liên tục này cho phép giải thuật hạ dốc tọa độ (Coordinate Descent) cập nhật từng biến trọng số w_j một cách đóng kín (Closed-form update) cực kỳ nhanh chóng, giúp LinearSVC huấn luyện toàn bộ 10.437 mẫu trên 24.619 chiều chỉ trong 0.0577 giây, nhanh gấp 3 lần so với Logistic Regression và nhanh gấp 11 lần so với Random Forest.")
