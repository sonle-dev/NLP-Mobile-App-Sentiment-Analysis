import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
from sklearn.model_selection import train_test_split

print("=== BAT DAU CAP NHAT DU_AN_HOC_MAY_NHOM_12.IPYNB ===")
nb_path = 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

# 1. Update Cell 0: Header with Aspect & LLM/spaCy mention
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
*Quy trình kỹ thuật hoàn chỉnh tích hợp mô hình phân tích khía cạnh (Aspect-based) và chuẩn hóa nhãn theo yêu cầu:*
1. **Phần I (KAN-1 -> KAN-5):** Thu thập dữ liệu thô, Thống kê mô tả, Ẩn danh PII, Khử nhiễu nghịch nhãn (Sarcasm/5 sao chê), Phân loại khía cạnh (Aspect: Hiệu năng UI/UX, Giao dịch, Bảo mật, CSKH), Trực quan hóa EDA & Tiền xử lý tách từ tiếng Việt chuẩn.
2. **Phần II (KAN-6 -> KAN-8):** Phân chia phân tầng 70/15/15, Trích xuất đặc trưng TF-IDF trên từ ghép tiếng Việt, Huấn luyện 3 mô hình học máy và Đánh giá so sánh chi tiết trên tập kiểm thử độc lập (Test Set)."""

# 2. Update Cell 5: Descriptive stats & New Audit & Aspect Summary
nb.cells[5].source = """# 1. Khai bao tong quan ve kich thuoc va kieu du lieu
print(f"Kich thuoc tap du lieu (So dong, So cot): {df.shape}\\n")
print("=== THONG TIN KIEU DU LIEU CAC COT (info) ===")
df.info()

# 2. Bang thong ke mo ta bien dinh luong (rating, thumbs_up)
print("\\n=== BANG THONG KE MO TA BIEN DINH LUONG (describe) ===")
display(df.describe().T)

# 2b. Bang tong hop chi tiet so luong comment theo tung muc sao (1 - 5 sao)
print("\\n=== BANG TONG HOP SO LUONG COMMENT THEO TUNG MUC SAO (1 - 5 SAO) ===")
rating_counts = df['rating'].value_counts().reindex([1, 2, 3, 4, 5])
rating_summary = pd.DataFrame({
    'Thang_danh_gia': ['1 sao (Rat te)', '2 sao (Te)', '3 sao (Trung tinh)', '4 sao (Tot)', '5 sao (Tuyet voi)'],
    'So_sao': [1, 2, 3, 4, 5],
    'So_luong_comment': rating_counts.values,
    'Ty_le_phan_tram': [f"{v / len(df) * 100:.2f}%" for v in rating_counts.values]
})
display(rating_summary)

# 2c. Bang chi tiet so sao theo tung ung dung
print("\\n=== BANG THONG KE SO SAO CHI TIET THEO TUNG UNG DUNG ===")
app_rating_crosstab = pd.crosstab(df['app_name'], df['rating'], margins=True, margins_name='Tong_comment')
app_rating_crosstab.columns = ['1 sao', '2 sao', '3 sao', '4 sao', '5 sao', 'Tong_comment']
display(app_rating_crosstab)

# 3. Kiem tra so luong gia tri thieu (Missing values)
print("\\n=== KIEM TRA GIA TRI CON THIEU ===")
print(df.isnull().sum())

# 4. Kiem tra so luong ban ghi trung lap noi dung
num_duplicates = df['content'].duplicated().sum()
print(f"\\nSo luong ban ghi trung lap noi dung: {num_duplicates} ({num_duplicates / len(df) * 100:.2f}%)")

# 5. Kiem tra va phan tich gia tri ngoai lai (Outlier Detection)
print("\\n=== KIEM TRA VA PHAN TICH GIA TRI NGOAI LAI (OUTLIERS) ===")
df['word_count'] = df['content'].apply(lambda x: len(str(x).split()))
q1 = float(df['word_count'].quantile(0.25))
q3 = float(df['word_count'].quantile(0.75))
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
outliers_length = df[df['word_count'] > upper_bound]

print(f"a. Do dai cau (IQR): Q1 = {q1:.1f}, Q3 = {q3:.1f}, IQR = {iqr:.1f} -> Nguong tren: {upper_bound:.1f} tu")
print(f"   - So luong cau dai ngoai lai (> {upper_bound:.1f} tu): {len(outliers_length)} mau ({len(outliers_length) / len(df) * 100:.2f}%)")
print(f"   - Do dai cau dai nhat (Max words): {df['word_count'].max()} tu")

# b. Phat hien rating ngoai doan quy uoc [1, 5]
outliers_rating = df[~df['rating'].isin([1, 2, 3, 4, 5])]
print(f"b. So luong rating bat thuong ngoai doan [1, 5]: len(outliers_rating) = {len(outliers_rating)} mau (Du lieu chuan)")

# c. Phat hien mau nghich nhan / di biet ngu nghia
praise_kw = 'tuyet voi|rat tot|muot ma|cuc tot|tuyệt vời|rất tốt|mượt'
neg_kw = 'qua te|lua dao|nhu rac|buc minh|loi|quá tệ|lừa đảo|bực mình|lỗi'
suspicious_1star = df[(df['rating'].isin([1, 2, 3])) & (df['content'].str.contains(praise_kw, case=False, na=False))]
suspicious_5star = df[(df['rating'].isin([4, 5])) & (df['content'].str.contains(neg_kw, case=False, na=False))]

print(f"c. Phat hien mau nghich nhan / di biet ngu nghia truoc khi loc LLM/Rule-based:")
print(f"   - Danh gia 1-3 sao nhung chua tu khen (cham biem, mia mai): {len(suspicious_1star)} mau")
print(f"   - Danh gia 4-5 sao nhung keu loi / phan nan (tam ly cham 5 sao de len top): {len(suspicious_5star)} mau")
"""

# 3. Update Cell 7: EDA Plot (Show 4 Subplots: App, Rating, Sentiment, Aspect Breakdown!)
nb.cells[7].source = """# Khoi tao luoi 2x2 bieu do truc quan toan dien
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Phan phoi so luong phan hoi theo tung ung dung
app_counts = df['app_name'].value_counts()
sns.barplot(
    x=app_counts.values, y=app_counts.index, ax=axes[0, 0],
    hue=app_counts.index, palette='Blues_r', legend=False
)
axes[0, 0].set_title('1. Phan phoi so luong phan hoi theo ung dung', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('So luong phan hoi')
axes[0, 0].set_ylabel('Ung dung')

# 2. Phan phoi diem so danh gia (Rating: 1 - 5 sao)
rating_order = [1, 2, 3, 4, 5]
rating_counts_list = df['rating'].value_counts().reindex(rating_order)
sns.barplot(
    x=rating_counts_list.index, y=rating_counts_list.values, ax=axes[0, 1],
    hue=rating_counts_list.index, palette='Purples', legend=False
)
axes[0, 1].set_title('2. Phan phoi diem so danh gia (Rating: 1 - 5 sao)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('So sao danh gia')
axes[0, 1].set_ylabel('Tan suat (So luong)')
for i, v in enumerate(rating_counts_list.values):
    axes[0, 1].text(i, v + 120, f"{v}\\n({v / len(df) * 100:.1f}%)", ha='center', fontweight='bold', fontsize=10)

# 3. Phan phoi nhan quan diem (Sentiment: 1-3 sao Tieu cuc vs 4-5 sao Tich cuc)
sentiment_order = ['Tieu cuc', 'Tich cuc']
sentiment_counts = df['sentiment'].value_counts().reindex(sentiment_order)
sns.barplot(
    x=sentiment_counts.index, y=sentiment_counts.values, ax=axes[1, 0],
    hue=sentiment_counts.index, palette=['#e74c3c', '#2ecc71'], legend=False
)
axes[1, 0].set_title('3. Phan phoi nhan quan diem (Sentiment)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Nhan quan diem')
axes[1, 0].set_ylabel('So luong')
for i, v in enumerate(sentiment_counts.values):
    axes[1, 0].text(i, v + 120, f"{v}\\n({v / len(df) * 100:.1f}%)", ha='center', fontweight='bold', fontsize=11)

# 4. Phan phoi do dai cau phan hoi (so tu) theo nhan quan diem
sns.boxplot(
    data=df, x='sentiment', y='word_count', order=sentiment_order, ax=axes[1, 1],
    hue='sentiment', palette=['#e74c3c', '#2ecc71'], legend=False, showfliers=False
)
axes[1, 1].set_title('4. Do dai phan hoi theo quan diem (showfliers=False)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Nhan quan diem')
axes[1, 1].set_ylabel('So tu trong phan hoi')

plt.tight_layout()
os.makedirs('reports/figures', exist_ok=True)
plt.savefig('reports/figures/eda_overview.png', dpi=300)
plt.show()
"""

# 4. Update Cell 9: Text preprocessing with Tokenization & Aspect extraction & Label audit!
nb.cells[9].source = """import re
import os
import pandas as pd
from underthesea import word_tokenize

# 1. Doc du lieu sach da duoc tinh chinh boi pipeline LLM & Aspect Analysis
clean_data_path = 'data/app_reviews_cleaned.csv' if os.path.exists('data/app_reviews_cleaned.csv') else '../data/app_reviews_cleaned.csv'
df_clean = pd.read_csv(clean_data_path)

print(f"So luong ban ghi hop le sau khi lam sach va loc nhan: {len(df_clean)}")
print("\\n=== 5 DONG DU LIEU MAU KET HOP KHIA CANH (ASPECT) VA TACH TU TIENG VIET ===")
display(df_clean[['content', 'segmented_content', 'sentiment', 'aspect_category', 'label_audit_type']].head())

print("\\n=== THONG KE PHAN PHOI KHIA CANH (ASPECTS) ===")
display(df_clean['aspect_category'].value_counts().to_frame(name='So_luong_comment'))

print("\\n=== THONG KE PHAN LOAI KIEM DUYET NHAN (LABEL AUDIT) ===")
display(df_clean['label_audit_type'].value_counts().to_frame(name='So_luong_mau'))
"""

# 5. Update Cell 13: Loading clean data for Modeling (reads segmented_content)
nb.cells[13].source = """import os, sys, joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# Doc tep du lieu da tien xu ly sach
data_path = 'data/app_reviews_cleaned.csv'
if not os.path.exists(data_path):
    data_path = '../data/app_reviews_cleaned.csv'
df = pd.read_csv(data_path)
print(f"=== NAP THANH CONG DU LIEU: {data_path} ===")
print(f"Tong so mau sach: {len(df)}")
"""

# 6. Update Cell 15: Stratified split using segmented_content
nb.cells[15].source = """# 1. Chuan hoa nhan nhi phan (1, 2, 3 sao -> 0, 4, 5 sao -> 1, da duoc loc boi LLM/Rule-based)
sentiment_map = {
    'Tieu cuc': 0, 'Tiêu cực': 0,
    'Tich cuc': 1, 'Tích cực': 1
}
df_binary = df[df['sentiment'].isin(sentiment_map.keys())].copy()
df_binary['label'] = df_binary['sentiment'].map(sentiment_map)

# 2. Su dung van ban da tach tu tieng Viet chuan (segmented_content)
X = df_binary['segmented_content'].fillna(df_binary['cleaned_content']).fillna('')
y = df_binary['label']

# Chia 70% Train va 30% Temp
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# Chia 30% Temp thanh 15% Val va 15% Test
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

print("=== KET QUA PHAN CHIA TAP DU LIEU (STRATIFIED SPLIT 70 / 15 / 15) ===")
print(f"Tong so mau nhi phan: {len(df_binary)}")
print(f"Tap Train      (70%): {len(X_train)} mau (Tieu cuc: {sum(y_train==0)}, Tich cuc: {sum(y_train==1)})")
print(f"Tap Validation (15%): {len(X_val)} mau (Tieu cuc: {sum(y_val==0)}, Tich cuc: {sum(y_val==1)})")
print(f"Tap Test       (15%): {len(X_test)} mau (Tieu cuc: {sum(y_test==0)}, Tich cuc: {sum(y_test==1)})")
"""

# 7. Update Cell 17: TF-IDF vectorizer configuration
nb.cells[17].source = """# Thiet lap bo vector hoa TF-IDF tren tu ghep tieng Viet
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),  # Unigram va Bigram tren tu ghep (vd: ung_dung, chuyen_tien)
    min_df=2,            # Loai bo tu xuat hien duoi 2 lan
    max_df=0.9,          # Loai bo tu qua pho bien tren 90%
    sublinear_tf=True,   # Ap dung log(1 + tf)
    norm='l2'            # Chuan hoa vector ve do dai don vi 1
)

# Fit tren tap Train, transform sang Val va Test
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)
X_test_vec = vectorizer.transform(X_test)

print(f"So luong dac trung tu vung (Vocabulary size): {len(vectorizer.vocabulary_)} dac trung")
print(f"Kich thuoc ma tran Train: {X_train_vec.shape}")
print(f"Kich thuoc ma tran Val:   {X_val_vec.shape}")
print(f"Kich thuoc ma tran Test:  {X_test_vec.shape}")
"""

# 8. Update Cell 21: Final Evaluation & Bar Chart
nb.cells[21].source = """# 1. Bieu do cot so sanh 4 chi so tren tap Test (KAN-8)
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

# Save notebook
with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

# Execute notebook to render all outputs
print("Dang thuc thi ExecutePreprocessor tren toan bo notebook...")
os.chdir('d:/HocMayPrJ')
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': 'd:/HocMayPrJ'}})

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("=== THUC THI DU_AN_HOC_MAY_NHOM_12.IPYNB THANH CONG 100%! ===")

# 9. Split and export Train, Val, Test datasets (CSV and Excel)
print("Dang xuat 3 tap Train, Val, Test va dong bo file Excel...")
sentiment_map = {'Tieu cuc': 0, 'Tiêu cực': 0, 'Tich cuc': 1, 'Tích cực': 1}
df_b = df_clean[df_clean['sentiment'].isin(sentiment_map.keys())].copy()
df_b['label'] = df_b['sentiment'].map(sentiment_map)

train_df, temp_df = train_test_split(df_b, test_size=0.30, random_state=42, stratify=df_b['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42, stratify=temp_df['label'])

for base in ['d:/HocMayPrJ/data', 'd:/HocMayPrJ/Nhom_12']:
    train_df.to_csv(f'{base}/train.csv', index=False, encoding='utf-8-sig')
    val_df.to_csv(f'{base}/val.csv', index=False, encoding='utf-8-sig')
    test_df.to_csv(f'{base}/test.csv', index=False, encoding='utf-8-sig')

try:
    train_df.to_excel('d:/HocMayPrJ/Nhom_12/train.xlsx', index=False)
    val_df.to_excel('d:/HocMayPrJ/Nhom_12/val.xlsx', index=False)
    test_df.to_excel('d:/HocMayPrJ/Nhom_12/test.xlsx', index=False)
    df_clean.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_sach_tieng_viet.xlsx', index=False)
    df_clean.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx', index=False)
    df_clean.to_excel('d:/HocMayPrJ/data/app_reviews_cleaned.xlsx', index=False)
except Exception as e:
    print("Canh bao ghi Excel (co the file dang mo):", e)

print("=== TOAN BO PIPELINE DU LIEU DA HOAN TAT! ===")
