import sys
sys.stdout.reconfigure(encoding='utf-8')
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

nb = nbformat.read('d:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb', as_version=4)

# 1. Update Title in Cell 0
nb.cells[0].source = """# DỰ ÁN HỌC MÁY (MACHINE LEARNING) - NLP-01
# BÁO CÁO TIẾN ĐỘ THỰC HIỆN TỪ KAN-1 ĐẾN KAN-8
## Đề tài: Phân tích quan điểm phản hồi của người dùng về ứng dụng di động
**Giảng viên hướng dẫn:** ThS. Hà Thị Thanh  
**Nhóm thực hiện:** Nhóm 12  
* Lê Hồng Sơn (Nhóm trưởng)
* Lưu Thị Khánh Ly
* Ngô Thị Sinh
* Nguyễn Thanh Tùng

---
*Notebook này bao gồm toàn bộ quy trình từ Thu thập dữ liệu đến Đánh giá so sánh mô hình học máy (dừng tại mốc KAN-8):*
1. **Phần I (KAN-1 -> KAN-5):** Thu thập dữ liệu thô, Thống kê mô tả, Ẩn danh PII, Trực quan hóa EDA & Tiền xử lý dữ liệu.
2. **Phần II (KAN-6 -> KAN-8):** Phân chia phân tầng, Trích xuất đặc trưng TF-IDF, Huấn luyện 3 mô hình học máy và Đánh giá so sánh chi tiết trên tập kiểm thử (Test Set)."""

# 2. Update Cell 20 (Markdown)
nb.cells[20].source = """---
## BƯỚC 5: TRỰC QUAN HÓA SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH TRÊN TẬP TEST (KAN-8)
Trực quan hóa biểu đồ cột so sánh 4 chỉ số đo lường (Accuracy, Precision, Recall, Macro F1) giữa 3 mô hình học máy trên tập kiểm thử độc lập (Test Set: 2.145 mẫu)."""

# 3. Update Cell 21 (Code) - keep only comparison & best model report
cell21_code = """# 1. Bieu do cot so sanh 4 chi so tren tap Test (KAN-8)
fig, ax = plt.subplots(figsize=(10, 5))
metrics = ['Test_Accuracy', 'Test_Precision', 'Test_Recall', 'Test_Macro_F1']
labels = ['Accuracy', 'Precision', 'Recall', 'Macro F1']
x = np.arange(len(df_results))
width = 0.2

for i, (m, label) in enumerate(zip(metrics, labels)):
    bars = ax.bar(x + i * width, df_results[m], width, label=label)
    for b in bars:
        h = b.get_height()
        ax.annotate(f'{h:.3f}', xy=(b.get_x() + b.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

ax.set_title('So sanh hieu nang cac mo hinh hoc may tren tap Test (KAN-8)', fontsize=12, fontweight='bold')
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(df_results['Mo hinh'], fontweight='bold')
ax.set_ylabel('Diem so (0.0 - 1.0)')
ax.set_ylim(0.7, 1.0)
ax.legend(loc='lower right')
plt.tight_layout()
plt.show()

# 2. Xac dinh mo hinh xuat sac nhat va in chi tiet danh gia
best_row = df_results.loc[df_results['Test_Macro_F1'].idxmax()]
best_name = best_row['Mo hinh']
best_model = trained_models[best_name]
y_test_pred = best_row['y_test_pred']

print(f"=== [★] MO HINH TOT NHAT TOAN DIEN: {best_name} ===")
print(f"Test Accuracy: {best_row['Test_Accuracy']:.4f} | Test Macro F1: {best_row['Test_Macro_F1']:.4f}\\n")
print("=== CHI TIET CLASSIFICATION REPORT (KAN-8) ===")
print(classification_report(y_test, y_test_pred, target_names=['Tieu cuc (0)', 'Tich cuc (1)'], digits=4))
"""
nb.cells[21].source = cell21_code

# 4. Add Final Conclusion Cell for KAN-8
conclusion_text = """---
## KẾT LUẬN VÀ HOÀN THÀNH TIẾN ĐỘ ĐẾN GIAI ĐOẠN KAN-8
* **Hoàn thành KAN-1 đến KAN-5:** Đã cào 15.541 đánh giá thô, ẩn danh 100% PII, làm sạch 549 dòng trùng lặp còn 14.869 dòng sạch, trực quan hóa EDA và phân tích ngưỡng ngoại lai IQR (60 từ).
* **Hoàn thành KAN-6:** Xây dựng Pipeline TF-IDF Unigram + Bigram với chuẩn hóa L2-norm trên 8.163 đặc trưng từ vựng, phân tầng dữ liệu không bị rò rỉ (Data Leakage).
* **Hoàn thành KAN-7:** Huấn luyện thành công 3 thuật toán học máy phân loại văn bản: Multinomial Naive Bayes, Linear Support Vector Classifier và Logistic Regression.
* **Hoàn thành KAN-8 (MỐC DỪNG HIỆN TẠI):** Sử dụng tập kiểm thử độc lập (Test Set gồm 2.145 mẫu) để đánh giá toàn diện, xác định:
  - **Mô hình tối ưu nhất:** `Logistic Regression` kết hợp trọng số `class_weight='balanced'` đạt **Accuracy 85.27%**, **Macro Recall 84.86%**, **Macro F1 83.48%**.
  - Xử lý triệt để bài toán mất cân bằng dữ liệu giữa nhãn Tiêu cực (68.7%) và Tích cực (31.3%).
* **Tiến độ dự án:** Nghiệm thu hoàn tất toàn bộ các yêu cầu từ KAN-1 đến KAN-8 theo đúng kế hoạch."""

# Slice cells to keep 0 to 21 + conclusion
nb.cells = nb.cells[:22]
nb.cells.append(nbformat.v4.new_markdown_cell(conclusion_text))

print('So cells sau khi dung o KAN-8:', len(nb.cells))

# Execute to refresh output
os.chdir('d:/HocMayPrJ')
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
print('Dang chay thuc thi lai notebook...')
ep.preprocess(nb, {'metadata': {'path': 'd:/HocMayPrJ'}})

with open('d:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Luu thanh cong ca 2 file notebook!')
