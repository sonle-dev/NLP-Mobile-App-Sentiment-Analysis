# -*- coding: utf-8 -*-
"""
Module: clean_reviews.py
Muc dich: Loc du lieu trung lap (duplicate), xu ly ky tu trang, loai bo spam va chuan hoa van ban so bo
Thuoc quy trinh: Buoc 3 (Lam sach so bo) - Du an Phan tich quan diem ung dung di dong (Nhom 12)
Thuc hien: Le Hong Son (sonle-dev) - Truong nhom
"""

import os
import sys
import re
import pandas as pd

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def basic_clean_text(text: str) -> str:
    """Loai bo ky tu xuong dong du thua va chuan hoa khoang trang co ban."""
    if not isinstance(text, str):
        return ""
    # Chuyen doi tab, newline thanh khoang trang don
    text = re.sub(r'[\r\n\t]+', ' ', text)
    # Loai bo khoang trang lien tiep
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def run_preliminary_cleaning(input_file: str, output_file: str):
    print(f"[*] Dang nap du lieu da an danh tu: {input_file}")
    df = pd.read_csv(input_file)
    n_original = len(df)
    print(f"[+] Tong so ban ghi dau vao: {n_original:,} dong")

    # 1. Loai bo cac ban ghi rong noi dung
    df = df.dropna(subset=['content'])
    df['content'] = df['content'].astype(str).apply(basic_clean_text)
    df = df[df['content'].str.len() > 1]
    n_after_na = len(df)
    print(f"[v] Loai bo {n_original - n_after_na:,} ban ghi rong hoac ky tu don le.")

    # 2. Loai bo cac ban ghi trung lap (Duplicates) dua tren noi dung danh gia
    n_before_dedup = len(df)
    df = df.drop_duplicates(subset=['content'], keep='first')
    n_duplicates = n_before_dedup - len(df)
    print(f"[v] Da phat hien va loai bo: {n_duplicates:,} danh gia trung lap noi dung (Spam duplicate).")

    # 3. Tinh toan do dai tu vung (Word count)
    df['word_count'] = df['content'].apply(lambda x: len(x.split()))

    # 4. Luu tru tap du lieu sach dat chuan
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"[v] Da xuat tap du lieu sach ra: {output_file}")
    print(f"[+] Tong so ban ghi dat chuan dua vao huan luyen: {len(df):,} mau")
    print(f"[+] Phan bo cam xuc: \n{df['sentiment'].value_counts(normalize=True).round(3) * 100}%")
    print("[*] Hoan thanh Buoc 3: Lam sach so bo du lieu thanh cong!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    anon_path = os.path.join(base_dir, "data", "app_reviews_anonymized.csv")
    cleaned_path = os.path.join(base_dir, "data", "app_reviews_cleaned.csv")
    run_preliminary_cleaning(anon_path, cleaned_path)
