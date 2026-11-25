import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

df_test = pd.read_csv('d:/HocMayPrJ/data/test.csv')

indices = [0, 3, 4, 7, 9, 15, 16, 21, 22, 23, 25, 27, 33]
for idx in indices:
    r = df_test.iloc[idx]
    print(f"Excel Row {idx+2}: [{r['app_name']} | {r['rating']}* | {r['aspect_category']}]")
    print(f"   Raw Content: {r['content']}")
    print(f"   Cleaned Content: {r['cleaned_content']}")
    print("-" * 70)
