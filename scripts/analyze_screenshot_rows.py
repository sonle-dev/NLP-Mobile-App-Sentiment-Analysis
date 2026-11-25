import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import pandas as pd

# Load test.csv
df_test = pd.read_csv('d:/HocMayPrJ/data/test.csv')

# Let's inspect the exact rows from the user's screenshot
screenshot_indices = [0, 3, 4, 7, 9, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33]

print("=== CAC DONG TRONG ANH NGUOI DUNG VA PHAN TICH ===")
for idx in screenshot_indices:
    r = df_test.iloc[idx]
    print(f"Dong {idx+2}: [{r['app_name']} | {r['rating']}*]")
    print(f"  Noi dung: {r['content']}")
    print(f"  Aspect hien tai: {r['aspect_category']}")
    print("-" * 50)
