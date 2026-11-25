import sys
sys.path.append('d:/HocMayPrJ')
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
from scripts.build_comprehensive_7_aspects import classify_7_aspects

# Load test.csv
df_test = pd.read_csv('d:/HocMayPrJ/data/test.csv')

screenshot_indices = [0, 3, 4, 7, 9, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33]

print("=== SO SANH TRUOC VA SAU KHI PHAN LOAI 7 ASPECT TREN CAC DONG ANH EXCEL ===")
for idx in screenshot_indices:
    r = df_test.iloc[idx]
    new_asp = classify_7_aspects(r['content'], r['app_name'])
    print(f"Dong {idx+2}: [{r['app_name']}] | Content: {r['content'][:60]}...")
    print(f"   Cu: {r['aspect_category']}")
    print(f"   Moi: {new_asp}")
    print("-" * 60)
