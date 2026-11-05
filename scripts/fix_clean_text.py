import sys
sys.stdout.reconfigure(encoding='utf-8')
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import pandas as pd

# 1. Update du_an_hoc_may_nhom_12.ipynb Cell 9
nb_path = 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

new_cell_9 = """import re

# 1. Tao ban sao du lieu va loai bo ban ghi trung lap noi dung
df_clean = df.drop_duplicates(subset=['content']).copy()
df_clean = df_clean.dropna(subset=['content', 'sentiment'])

# 2. Tu dien chuan hoa viet tat tieng Viet (Teencode) sang tieng Viet chuan
teencode_dict = {
    'k': 'không', 'ko': 'không', 'khong': 'không', 'hok': 'không',
    'dc': 'được', 'đc': 'được', 'duoc': 'được',
    'app': 'ứng dụng', 'ad': 'quản trị viên', 'sp': 'sản phẩm',
    'acc': 'tài khoản', 'fb': 'facebook', 'ib': 'nhắn tin',
    'mik': 'mình', 'mk': 'mình', 'ae': 'anh em', 'mn': 'mọi người',
    'dt': 'điện thoại', 'tot': 'tốt', 'ok': 'tốt', 'oke': 'tốt'
}

# 3. Ham tien xu ly van ban tieng Viet chuan (giu nguyen dau tieng Viet Unicode)
def preprocess_vietnamese_text(text: str) -> str:
    text = str(text).lower()
    
    # Loai bo duong dan URL
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    
    # Loai bo dau cau va ky tu dac biet, GIU NGUYEN chu cai tieng Viet Unicode
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'[\d_]', ' ', text)
    
    # Chuan hoa tu viet tat theo tu dien teencode
    tokens = [teencode_dict.get(word, word) for word in text.split()]
    
    # Ghep lai thanh cau va chuan hoa khoang trang thua
    return ' '.join(tokens).strip()

# 4. Ap dung tien xu ly len toan bo cot noi dung phan hoi
df_clean['cleaned_content'] = df_clean['content'].apply(preprocess_vietnamese_text)

# 5. Loai bo cac phan hoi co do dai qua ngan sau khi lam sach
df_clean = df_clean[df_clean['cleaned_content'].str.len() > 1].reset_index(drop=True)

# 6. Hien thi so sanh 5 mau phan hoi truoc va sau khi tien xu ly
print(f"So luong ban ghi sau khi lam sach: {len(df_clean)} (loai bo {len(df) - len(df_clean)} ban ghi)")
print("\\n=== SO SANH NOI DUNG TRUOC VA SAU TIEN XU LY (CHUAN TIENG VIET) ===")
display(df_clean[['content', 'cleaned_content', 'sentiment']].head())

# 7. Luu tap du lieu da tien xu ly
clean_data_path = 'data/app_reviews_cleaned.csv' if os.path.exists('data') else '../data/app_reviews_cleaned.csv'
df_clean.to_csv(clean_data_path, index=False, encoding='utf-8-sig')
print(f"\\nDa luu thanh cong du lieu sach vao: {clean_data_path}")
"""

nb.cells[9].source = new_cell_9

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

# Also update d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb
with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

# Execute the entire notebook from top to bottom
os.chdir('d:/HocMayPrJ')
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
print('Dang chay lai toan bo notebook voi bo xu ly tien xu ly tieng Viet chuan...')
ep.preprocess(nb, {'metadata': {'path': 'd:/HocMayPrJ'}})

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

# Also export excel
df_saved = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')
df_saved.to_excel('d:/HocMayPrJ/data/app_reviews_cleaned.xlsx', index=False)
df_saved.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx', index=False)
if os.path.exists('d:/HocMayPrJ/Nhom_12/Code_va_Data_Nhom12/data'):
    df_saved.to_excel('d:/HocMayPrJ/Nhom_12/Code_va_Data_Nhom12/data/app_reviews_cleaned.xlsx', index=False)
    df_saved.to_csv('d:/HocMayPrJ/Nhom_12/Code_va_Data_Nhom12/data/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')

print('Hoan thanh cap nhat toan bo notebook va file excel!')
