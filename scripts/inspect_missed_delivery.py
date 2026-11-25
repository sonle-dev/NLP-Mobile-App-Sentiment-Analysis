import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')
hn = df[df['aspect_category'] == 'Hieu_nang_Va_Loi_App']

delivery_kws = ['ship', 'giao', 'đơn', 'hàng', 'tài xế', 'món', 'quán', 'bác tài', 'cuốc', 'đón', 'rước', 'xe']
has_del = hn[hn['content'].str.lower().apply(lambda x: any(k in x for k in delivery_kws))]

print("=== 20 MAU GIAO HANG / DON HANG BI BI LOT VAO HIEU NANG ===")
for idx, r in has_del.head(20).iterrows():
    print(f"- [{r['app_name']} | {r['rating']}*]: {r['content']}")
