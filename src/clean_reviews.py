# -*- coding: utf-8 -*-
"""
Module: clean_reviews.py
Mục đích: Lọc dữ liệu trùng lặp (duplicate), xử lý ký tự trắng, loại bỏ spam và chuẩn hóa văn bản sơ bộ
Thuộc quy trình: Bước 3 (Làm sạch sơ bộ) - Dự án Phân tích quan điểm ứng dụng di động (Nhóm 12)
Thực hiện: Lê Hồng Sơn (sonle-dev) - Trưởng nhóm
"""

import os
import sys
import re
import pandas as pd

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def basic_clean_text(text: str) -> str:
    """Loại bỏ ký tự xuống dòng dư thừa và chuẩn hóa khoảng trắng cơ bản."""
    if not isinstance(text, str):
        return ""
    # Chuyển đổi tab, newline thành khoảng trắng đơn
    text = re.sub(r'[\r\n\t]+', ' ', text)
    # Loại bỏ khoảng trắng liên tiếp
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def run_preliminary_cleaning(input_file: str, output_file: str):
    print(f"[*] Đang nạp dữ liệu đã ẩn danh từ: {input_file}")
    df = pd.read_csv(input_file)
    n_original = len(df)
    print(f"[+] Tổng số bản ghi đầu vào: {n_original:,} dòng")

    # 1. Loại bỏ các bản ghi rỗng nội dung
    df = df.dropna(subset=['content'])
    df['content'] = df['content'].astype(str).apply(basic_clean_text)
    df = df[df['content'].str.len() > 1]
    n_after_na = len(df)
    print(f"[v] Loại bỏ {n_original - n_after_na:,} bản ghi rỗng hoặc ký tự đơn lẻ.")

    # 2. Loại bỏ các bản ghi trùng lặp (Duplicates) dựa trên nội dung đánh giá
    n_before_dedup = len(df)
    df = df.drop_duplicates(subset=['content'], keep='first')
    n_duplicates = n_before_dedup - len(df)
    print(f"[v] Đã phát hiện và loại bỏ: {n_duplicates:,} đánh giá trùng lặp nội dung (Spam duplicate).")

    # 3. Tính toán độ dài từ vựng (Word count)
    df['word_count'] = df['content'].apply(lambda x: len(x.split()))

    # 4. Lưu trữ tập dữ liệu sạch đạt chuẩn
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"[v] Đã xuất tập dữ liệu sạch ra: {output_file}")
    print(f"[+] Tổng số bản ghi đạt chuẩn đưa vào huấn luyện: {len(df):,} mẫu")
    print(f"[+] Phân bố cảm xúc: \n{df['sentiment'].value_counts(normalize=True).round(3) * 100}%")
    print("[*] Hoàn thành Bước 3: Làm sạch sơ bộ dữ liệu thành công!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    anon_path = os.path.join(base_dir, "data", "app_reviews_anonymized.csv")
    cleaned_path = os.path.join(base_dir, "data", "app_reviews_cleaned.csv")
    run_preliminary_cleaning(anon_path, cleaned_path)
