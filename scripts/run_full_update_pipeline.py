import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
from sklearn.model_selection import train_test_split

nb_path = 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

# 1. Check and update Cell 3
cell_3_code = """# 1. Khai bao cac thu vien chuan
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata

# Cau hinh kieu hien thi bieu do
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# 2. Doc tep du lieu app_reviews.csv (ho tro tu dong tim duong dan)
candidate_paths = [
    'data/app_reviews.csv',
    'data/app_reviews_raw.csv',
    '../data/app_reviews.csv',
    '../data/app_reviews_raw.csv',
    'app_reviews.csv'
]
data_path = next((p for p in candidate_paths if os.path.exists(p)), None)
if data_path is None:
    raise FileNotFoundError("Khong tim thay tep du lieu trong thu muc data/")
df = pd.read_csv(data_path)

# 3. Chuan hoa nhan sentiment theo quy uoc moi: 1, 2, 3 sao la Tieu cuc, 4, 5 sao la Tich cuc
def assign_sentiment(r):
    try:
        return 'Tieu cuc' if int(r) in [1, 2, 3] else 'Tich cuc'
    except:
        return 'Tieu cuc'

df['sentiment'] = df['rating'].apply(assign_sentiment)

# 4. Hien thi 5 dong dau tien cua bang du lieu
print(f"=== DOC DU LIEU THANH CONG TU: {data_path} ===")
print("=== 5 DONG DAU TIEN CUA DU LIEU ===")
display(df.head())
"""
nb.cells[3].source = cell_3_code

# 2. Update Cell 7 (Plot 3 & 4 with 2 classes: Tieu cuc vs Tich cuc)
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

# 3. Phan phoi nhan quan diem (Sentiment: 1, 2, 3 sao la Tieu cuc; 4, 5 sao la Tich cuc)
sentiment_order = ['Tieu cuc', 'Tich cuc']
sentiment_counts = df['sentiment'].value_counts().reindex(sentiment_order)
sns.barplot(
    x=sentiment_counts.index, y=sentiment_counts.values, ax=axes[1, 0],
    hue=sentiment_counts.index, palette=['#e74c3c', '#2ecc71'], legend=False
)
axes[1, 0].set_title('3. Phan phoi nhan quan diem (Sentiment: 1-3 sao vs 4-5 sao)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Nhan quan diem')
axes[1, 0].set_ylabel('So luong')
for i, v in enumerate(sentiment_counts.values):
    axes[1, 0].text(i, v + 120, f"{v}\\n({v / len(df) * 100:.1f}%)", ha='center', fontweight='bold', fontsize=11)

# 4. Phan phoi do dai cau phan hoi (so tu) theo nhan quan diem
df['word_count'] = df['content'].apply(lambda x: len(str(x).split()))
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
nb.cells[7].source = cell_7_code

# 3. Update Cell 15 (Binary split: All rows included)
cell_15_code = """# 1. Chuan hoa nhan nhi phan (1, 2, 3 sao -> 0, 4, 5 sao -> 1)
sentiment_map = {
    'Tieu cuc': 0, 'Tiêu cực': 0,
    'Tich cuc': 1, 'Tích cực': 1
}
df_binary = df[df['sentiment'].isin(sentiment_map.keys())].copy()
df_binary['label'] = df_binary['sentiment'].map(sentiment_map)

# 2. Phan chia 70% Train, 15% Validation, 15% Test
X = df_binary['cleaned_content'].fillna('')
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
nb.cells[15].source = cell_15_code

# 4. Save and execute notebook
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

print('Executed du_an_hoc_may_nhom_12.ipynb successfully!')

# 5. Export clean datasets, train/val/test splits
df_clean = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')
sentiment_map = {'Tieu cuc': 0, 'Tiêu cực': 0, 'Tich cuc': 1, 'Tích cực': 1}
df_b = df_clean[df_clean['sentiment'].isin(sentiment_map.keys())].copy()
df_b['label'] = df_b['sentiment'].map(sentiment_map)

train_df, temp_df = train_test_split(df_b, test_size=0.30, random_state=42, stratify=df_b['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42, stratify=temp_df['label'])

train_df.to_csv('d:/HocMayPrJ/Nhom_12/train.csv', index=False, encoding='utf-8-sig')
val_df.to_csv('d:/HocMayPrJ/Nhom_12/val.csv', index=False, encoding='utf-8-sig')
test_df.to_csv('d:/HocMayPrJ/Nhom_12/test.csv', index=False, encoding='utf-8-sig')

train_df.to_csv('d:/HocMayPrJ/data/train.csv', index=False, encoding='utf-8-sig')
val_df.to_csv('d:/HocMayPrJ/data/val.csv', index=False, encoding='utf-8-sig')
test_df.to_csv('d:/HocMayPrJ/data/test.csv', index=False, encoding='utf-8-sig')

try:
    train_df.to_excel('d:/HocMayPrJ/Nhom_12/train.xlsx', index=False)
    val_df.to_excel('d:/HocMayPrJ/Nhom_12/val.xlsx', index=False)
    test_df.to_excel('d:/HocMayPrJ/Nhom_12/test.xlsx', index=False)
    df_clean.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_sach_tieng_viet.xlsx', index=False)
except Exception as e:
    print('Excel write warning (file might be open in Excel):', e)

print('Pipeline update complete!')
