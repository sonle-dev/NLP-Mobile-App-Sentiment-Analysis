import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

df_test = pd.read_csv('d:/HocMayPrJ/data/test.csv')

screenshot_indices = [0, 3, 4, 7, 9, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33]

print("=== KIEM TRA CAC DONG TRONG TEST.CSV SAU KHI NANG CAP 7 ASPECT ===")
for idx in screenshot_indices:
    r = df_test.iloc[idx]
    print(f"Dong {idx+2}: [{r['app_name']} | {r['rating']}*] -> {r['aspect_category']}")
    print(f"   Content: {r['content'][:70]}...")
    print("-" * 65)

# Also save Nhom_12/test_updated_7aspects.xlsx
try:
    df_test.to_excel('d:/HocMayPrJ/Nhom_12/test_updated_7aspects.xlsx', index=False)
    print("Da luu Nhom_12/test_updated_7aspects.xlsx thanh cong!")
except Exception as e:
    print("Loi:", e)
