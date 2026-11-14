import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

# 1. 5-star complaints fixed
fixed_5stars = df[df['label_audit_type'] == 'Nghich_nhan_5sao_che']
print(f"Tong so mau 4-5 sao chui/loi da sua sang Tieu cuc: {len(fixed_5stars)}")
print("\n=== MINH CHUNG: 3 MAU 5 SAO CHUI DA SUA SANG TIEU CUC (0) ===")
for idx, r in fixed_5stars.head(3).iterrows():
    print(f"- [Rating: {r['rating']} sao] -> Sentiment moi: {r['sentiment']} (label={r['label']}) | Aspect: {r['aspect_category']}")
    print(f"  Noi dung goc: \"{r['content'][:120]}...\"\n")

# 2. 1-star praise fixed
fixed_1stars = df[df['label_audit_type'] == 'Nghich_nhan_1sao_khen']
print(f"Tong so mau 1-2 sao khen da sua sang Tich cuc: {len(fixed_1stars)}")
print("\n=== MINH CHUNG: MAU 1 SAO KHEN DA SUA SANG TICH CUC (1) ===")
for idx, r in fixed_1stars.iterrows():
    print(f"- [Rating: {r['rating']} sao] -> Sentiment moi: {r['sentiment']} (label={r['label']}) | Aspect: {r['aspect_category']}")
    print(f"  Noi dung goc: \"{r['content'][:120]}...\"\n")

# 3. Aspects proof
print("=== MINH CHUNG 4 KHIA CANH (ASPECTS) ===")
for asp in ['Hieu_nang_UI_UX', 'Giao_dich_Thanh_toan', 'Bao_mat_Tai_khoan', 'Dich_vu_CSKH']:
    sample = df[df['aspect_category'] == asp].iloc[0]
    print(f"- Khia canh: {asp}")
    print(f"  Noi dung: \"{sample['content'][:100]}...\"\n")
