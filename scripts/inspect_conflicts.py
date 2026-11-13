import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

neg_kw = 'quá tệ|qua te|lừa đảo|lua dao|như rác|nhu rac|bực mình|buc minh|lỗi|loi|treo|đơ|văng|vang|khóa|khoa|không đăng nhập|khong dang nhap|chậm|cham|kém|kem|chán|chan|tồi tệ|toi te|mất tiền|mat tien|trừ tiền|tru tien|nuốt thẻ|nuot the'
praise_kw = 'tuyệt vời|tuyet voi|rất tốt|rat tot|mượt mà|muot ma|cực tốt|cuc tot|quá tốt|qua tot|hài lòng|hai long|dễ dùng|de dung|5 sao|nam sao|yêu thích|yeu thich|tuyệt|tuyet|xuất sắc|xuat sac'

high_stars_complaint = df[(df['rating'].isin([4, 5])) & (df['content'].str.contains(neg_kw, case=False, na=False))]
print("=== 5 MAU 4-5 SAO NHUNG CO TU KHOA LOI / PHAN NAN ===")
for idx, row in high_stars_complaint.head(5).iterrows():
    print(f"[{row['rating']} sao] - {row['content'][:110]}...")

low_stars_praise = df[(df['rating'].isin([1, 2, 3])) & (df['content'].str.contains(praise_kw, case=False, na=False))]
print("\n=== 5 MAU 1-3 SAO NHUNG CO TU KHOA KHEN ===")
for idx, row in low_stars_praise.head(5).iterrows():
    print(f"[{row['rating']} sao] - {row['content'][:110]}...")
