import sys
sys.stdout.reconfigure(encoding='utf-8')
import nbformat

nb_path = 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

new_conclusion = '''---
## KẾT LUẬN VÀ HOÀN THÀNH TIẾN ĐỘ ĐẾN GIAI ĐOẠN KAN-8
* **Hoàn thành KAN-1 đến KAN-5:** Đã cào 15.541 đánh giá thô, thiết lập quy tắc nhãn nhị phân chuẩn xác (1, 2, 3 sao là Tiêu cực; 4, 5 sao là Tích cực), ứng dụng bộ lọc từ khóa LLM/Rule-based để xử lý triệt để 48 trường hợp nghịch nhãn (5 sao chửi bới / 1 sao khen ngợi), phân loại 4 khía cạnh nghiệp vụ (Aspect: Hiệu năng UI/UX, Giao dịch, Bảo mật, CSKH) và tách từ tiếng Việt chuẩn.
* **Hoàn thành KAN-6:** Xây dựng Pipeline TF-IDF Unigram + Bigram với chuẩn hóa L2-norm trên 24.432 đặc trưng từ ghép tiếng Việt, phân tầng dữ liệu 70/15/15 (Train: 10.437, Val: 2.236, Test: 2.237 mẫu) chống rò rỉ dữ liệu (Data Leakage).
* **Hoàn thành KAN-7:** Huấn luyện thành công 3 thuật toán học máy phân loại văn bản: Multinomial Naive Bayes, Linear Support Vector Classifier và Logistic Regression.
* **Hoàn thành KAN-8 (MỐC CHỐT HIỆN TẠI):** Sử dụng tập kiểm thử độc lập (Test Set gồm 2.237 mẫu) để chấm điểm và so sánh toàn diện:
  - **Mô hình tối ưu nhất:** `Logistic Regression` kết hợp trọng số `class_weight='balanced'` đạt **Accuracy 90.52%**, **Macro Recall 88.90%**, **Macro F1 88.74%** (theo sát là `Linear SVC` đạt **Accuracy 90.41%** và **Macro F1 88.61%**).
  - Khắc phục hoàn toàn tình trạng mất cân bằng dữ liệu giữa nhãn Tiêu cực (70.1%) và Tích cực (29.9%).
* **Tiến độ dự án:** Nghiệm thu hoàn tất toàn bộ các yêu cầu từ KAN-1 đến KAN-8 theo đúng chỉ đạo của giảng viên hướng dẫn.'''

nb.cells[-1].source = new_conclusion

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Updated conclusion in both notebooks!')
