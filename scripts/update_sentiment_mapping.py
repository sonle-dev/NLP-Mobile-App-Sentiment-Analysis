import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pandas as pd

def map_sentiment_vn(r):
    try:
        return 'Tiêu cực' if int(r) in [1, 2, 3] else 'Tích cực'
    except Exception:
        return 'Tiêu cực'

data_files = [
    'd:/HocMayPrJ/data/app_reviews_raw.csv',
    'd:/HocMayPrJ/data/app_reviews.csv',
    'd:/HocMayPrJ/data/app_reviews_anonymized.csv',
    'd:/HocMayPrJ/Nhom_12/Code_va_Data_Nhom12/data/app_reviews_raw.csv',
    'd:/HocMayPrJ/Nhom_12/Code_va_Data_Nhom12/data/app_reviews.csv',
    'd:/HocMayPrJ/Nhom_12/Code_va_Data_Nhom12/data/app_reviews_anonymized.csv',
]

for fpath in data_files:
    if os.path.exists(fpath):
        df = pd.read_csv(fpath)
        df['sentiment'] = df['rating'].apply(map_sentiment_vn)
        df.to_csv(fpath, index=False, encoding='utf-8-sig')
        counts = df['sentiment'].value_counts().to_dict()
        print(f"Updated {fpath}: {counts}")

# Also update tools/scraper_gui.py
scraper_path = 'd:/HocMayPrJ/tools/scraper_gui.py'
if os.path.exists(scraper_path):
    with open(scraper_path, 'r', encoding='utf-8') as f:
        scraper_code = f.read()
    
    old_target = """def categorize_sentiment(rating: int) -> str:
    \"\"\"Gan nhan cam xuc so bo dua tren so sao rating.\"\"\"
    try:
        r = int(rating)
        if r >= 4:
            return \"Tich cuc (Positive)\"
        elif r == 3:
            return \"Trung tinh (Neutral)\"
        else:
            return \"Tieu cuc (Negative)\""""
    
    new_replacement = """def categorize_sentiment(rating: int) -> str:
    \"\"\"Gan nhan cam xuc so bo dua tren so sao rating: 1, 2, 3 sao la Tieu cuc; 4, 5 sao la Tich cuc.\"\"\"
    try:
        r = int(rating)
        if r >= 4:
            return \"Tich cuc (Positive)\"
        else:
            return \"Tieu cuc (Negative)\""""
    
    if old_target in scraper_code:
        scraper_code = scraper_code.replace(old_target, new_replacement)
        with open(scraper_path, 'w', encoding='utf-8') as f:
            f.write(scraper_code)
        print("Updated tools/scraper_gui.py categorize_sentiment successfully!")
