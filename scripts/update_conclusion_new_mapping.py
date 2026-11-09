import sys
sys.stdout.reconfigure(encoding='utf-8')
import nbformat

nb_path = 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

new_conclusion = '''---
## KẾT LUẬN VÀ HOÀN THÀNH TIẾN ĐỘ ĐẾN GIAI ĐOẠN KAN-8
* **Hoàn thành KAN-1 đến KAN-5:** Đã cào 15.541 đánh giá thô, thiết lập quy tắc nhãn nhị phân chuẩn xác (1, 2, 3 sao là Tiêu cực; 4, 5 sao là Tích cực), ẩn danh 100% PII, làm sạch trùng lặp còn 14.910 dòng sạch, trực quan hóa EDA và phân tích ngưỡng ngoại lai IQR (60 từ).
* **Hoàn thành KAN-6:** Xây dựng Pipeline TF-IDF Unigram + Bigram với chuẩn hóa L2-norm trên 24.432 đặc trưng từ vựng tiếng Việt có dấu chuẩn xác, phân tầng dữ liệu 70/15/15 (Train: 10.437, Val: 2.236, Test: 2.237) chống rò rỉ (Data Leakage).
* **Hoàn thành KAN-7:** Huấn luyện thành công 3 thuật toán học máy phân loại văn bản: Multinomial Naive Bayes, Logistic Regression và Linear Support Vector Classifier (Linear SVC).
* **Hoàn thành KAN-8 (MỐC CHỐT HIỆN TẠI):** Sử dụng tập kiểm thử độc lập (Test Set gồm 2.237 mẫu) để chấm điểm và so sánh toàn diện:
  - **Mô hình tối ưu nhất:** `Linear SVC` kết hợp trọng số `class_weight='balanced'` đạt **Accuracy 90.39%**, **Macro Recall 88.36%**, **Macro F1 88.54%** (theo sát là `Logistic Regression` đạt **Accuracy 90.30%** và **Macro F1 88.44%**).
  - Xử lý triệt để bài toán mất cân bằng dữ liệu giữa nhãn Tiêu cực (69.8%) và Tích cực (30.2%).
* **Tiến độ dự án:** Nghiệm thu hoàn tất toàn bộ các yêu cầu từ KAN-1 đến KAN-8 theo đúng kế hoạch đề ra.'''

nb.cells[-1].source = new_conclusion

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Updated conclusion!')
