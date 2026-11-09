import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews.csv')

# 1. 1-star with praise words (sarcasm)
sarcasm = df[(df['rating'] == 1) & (df['content'].str.contains('tuyet voi|rat tot|muot ma|cuc tot|tuyệt vời|rất tốt|mượt', case=False, na=False))]
print("=== 3 MAU 1 SAO CHUA TU KHEN (CHAM BIEM / MIA MAI) ===")
for idx, row in sarcasm.head(3).iterrows():
    print(f"- App: {row['app_name']} | Rating: {row['rating']} sao")
    print(f"  Noi dung: \"{row['content']}\"\n")

# 2. 5-star with complaints (tam ly cham 5 sao len top)
reverse_5star = df[(df['rating'] == 5) & (df['content'].str.contains('qua te|lua dao|nhu rac|buc minh|loi|quá tệ|lừa đảo|bực mình|lỗi', case=False, na=False))]
print("=== 3 MAU 5 SAO NHUNG KEU LOI / PHAN NAN ===")
for idx, row in reverse_5star.head(3).iterrows():
    print(f"- App: {row['app_name']} | Rating: {row['rating']} sao")
    print(f"  Noi dung: \"{row['content']}\"\n")
