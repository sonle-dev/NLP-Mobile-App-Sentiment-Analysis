import sys
sys.stdout.reconfigure(encoding='utf-8')
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

nb_path = 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

# 1. Update Cell 5 to add clear summary tables
cell_5_code = """# 1. Khai bao tong quan ve kich thuoc va kieu du lieu
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

# a. Phat hien ngoai lai ve do dai cau theo phuong phap IQR
df['word_count'] = df['content'].apply(lambda x: len(str(x).split()))
q1 = float(df['word_count'].quantile(0.25))
q3 = float(df['word_count'].quantile(0.75))
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
outliers_length = df[df['word_count'] > upper_bound]

print(f"a. Do dai cau (IQR): Q1 = {q1:.1f}, Q3 = {q3:.1f}, IQR = {iqr:.1f} -> Nguong tren (Upper Bound): {upper_bound:.1f} tu")
print(f"   - So luong cau dai ngoai lai (> {upper_bound:.1f} tu): {len(outliers_length)} mau ({len(outliers_length) / len(df) * 100:.2f}%)")
print(f"   - Do dai cau dai nhat (Max words): {df['word_count'].max()} tu")
print(f"   -> Chien luoc xu ly: Khong xoa bo vi chua thong tin loi quan trong; duoc can bang bang chuan hoa L2 Norm trong TF-IDF.")

# b. Phat hien rating ngoai doan quy uoc [1, 5]
outliers_rating = df[~df['rating'].isin([1, 2, 3, 4, 5])]
print(f"b. So luong rating bat thuong ngoai doan [1, 5]: len(outliers_rating) = {len(outliers_rating)} mau (Du lieu chuan)")

# c. Phat hien mau nghich nhan / di biet ngu nghia
suspicious_1star = df[(df['rating'] == 1) & (df['content'].str.contains('tuyet voi|rat tot|muot ma|cuc tot|tuyệt vời|rất tốt|mượt', case=False, na=False))]
suspicious_5star = df[(df['rating'] == 5) & (df['content'].str.contains('qua te|lua dao|nhu rac|buc minh|loi|quá tệ|lừa đảo|bực mình|lỗi', case=False, na=False))]

print(f"c. Phat hien mau nghich nhan / di biet ngu nghia:")
print(f"   - Danh gia 1 sao nhung chua tu khen (cham biem, mia mai): {len(suspicious_1star)} mau")
print(f"   - Danh gia 5 sao nhung keu loi / phan nan (tam ly cham 5 sao de len top): {len(suspicious_5star)} mau")
"""
nb.cells[5].source = cell_5_code

# 2. Update Cell 7 to annotate counts on Biểu đồ 2 (Rating bars)
cell_7_code = """# Khoi tao luoi 2x2 bieu do truc quan
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

# 2. Phan phoi diem so danh gia (Rating: 1 - 5 sao) co chu thich so luong
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

# 3. Phan phoi nhan quan diem (Sentiment)
sentiment_order = ['Tieu cuc', 'Tich cuc', 'Trung tinh']
sentiment_counts = df['sentiment'].value_counts().reindex(sentiment_order)
sns.barplot(
    x=sentiment_counts.index, y=sentiment_counts.values, ax=axes[1, 0],
    hue=sentiment_counts.index, palette=['#e74c3c', '#2ecc71', '#f39c12'], legend=False
)
axes[1, 0].set_title('3. Phan phoi nhan quan diem (Sentiment)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Nhan quan diem')
axes[1, 0].set_ylabel('So luong')
for i, v in enumerate(sentiment_counts.values):
    axes[1, 0].text(i, v + 120, f"{v}\\n({v / len(df) * 100:.1f}%)", ha='center', fontweight='bold')

# 4. Phan phoi do dai cau phan hoi (so tu) theo nhan quan diem
df['word_count'] = df['content'].apply(lambda x: len(str(x).split()))
sns.boxplot(
    data=df, x='sentiment', y='word_count', order=sentiment_order, ax=axes[1, 1],
    hue='sentiment', palette=['#e74c3c', '#2ecc71', '#f39c12'], legend=False, showfliers=False
)
axes[1, 1].set_title('4. Do dai phan hoi theo quan diem (showfliers=False)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Nhan quan diem')
axes[1, 1].set_ylabel('So tu trong phan hoi')

plt.tight_layout()
os.makedirs('reports/figures', exist_ok=True)
plt.savefig('reports/figures/eda_overview.png', dpi=300)
plt.show()
"""
nb.cells[7].source = cell_7_code

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

os.chdir('d:/HocMayPrJ')
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
print('Dang chay ExecutePreprocessor...')
ep.preprocess(nb, {'metadata': {'path': 'd:/HocMayPrJ'}})

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Cap nhat thanh cong ca 2 cell!')
