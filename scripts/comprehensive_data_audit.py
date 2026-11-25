import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

print("=== 1. TONG QUAN DU LIEU HIEN TAI ===")
print(f"Tong so dong: {len(df)}")
print(f"So ung dung: {df['app_name'].nunique()} ({list(df['app_name'].unique())})")

print("\n=== 2. THONG KE DO DAI (WORD COUNT) ===")
print(df['word_count'].describe())

print("\n=== 3. CAC DANG DU LIEU CAN XU LY TOAN DIEN ===")

# a. Review cuc ngan (<= 2 tu)
short_df = df[df['word_count'] <= 2]
print(f"a. Review sieu ngan (<= 2 tu): {len(short_df)} mau")

# b. Review spam / ky tu dac biet / vo nghia
def has_noise(text):
    t = str(text).strip()
    # Chi co so hoac ky tu khong phai chu cai
    if not re.search(r'[a-zA-Zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', t):
        return True
    # Ky tu lap >= 4 lan
    if re.search(r'(.)\1{4,}', t):
        return True
    return False

noisy_df = df[df['content'].apply(has_noise)]
print(f"b. Review chua ky tu lap di thuong / ky tu rac: {len(noisy_df)} mau")

# c. Teencode tien te / so luong bi bien dang (vd: 11k, 50k, 100k, 1tr)
money_samples = df[df['content'].str.contains(r'\b\d+\s*(?:k|vnđ|vnd|đ|tr|triệu)\b', case=False, na=False)]
print(f"c. Review chua so tien / tien te (k, tr, vnd, đ): {len(money_samples)} mau")

# d. Teencode mk (mat khau vs minh)
mk_samples = df[df['content'].str.contains(r'\bmk\b', case=False, na=False)]
print(f"d. Review chua chu 'mk' (can phan biet mat khau vs minh): {len(mk_samples)} mau")

# e. Teencode tk (tai khoan)
tk_samples = df[df['content'].str.contains(r'\btk\b', case=False, na=False)]
print(f"e. Review chua chu 'tk' (tai khoan): {len(tk_samples)} mau")

# f. Ty le phan bo Aspect hien tai
print("\nf. Phan bo 5 Aspect hien tai:")
print(df['aspect_category'].value_counts())

# g. Ty le phan bo Sentiment
print("\ng. Phan bo Sentiment hien tai:")
print(df['sentiment'].value_counts())
print("\nLoai kiem toan sentiment:")
print(df['label_audit_type'].value_counts())
