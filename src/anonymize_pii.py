# -*- coding: utf-8 -*-
"""
Module: anonymize_pii.py
Muc dich: Loai bo hoan toan thong tin dinh danh ca nhan (PII) va che giau du lieu nhay cam
Thuoc quy trinh: Buoc 2 (An danh PII) - Du an Phan tich quan diem ung dung di dong (Nhom 12)
Thuc hien: Luu Thi Khanh Ly (luuthily34-lab)
"""

import os
import sys
import re
import pandas as pd

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def mask_sensitive_patterns(text: str) -> str:
    """Che giau so dien thoai va email xuat hien trong noi dung danh gia."""
    if not isinstance(text, str):
        return ""
    # Che so dien thoai di dong Viet Nam (dau so 03, 05, 07, 08, 09 kem 8 chu so)
    text = re.sub(r'(03|05|07|08|09)\d{8}', '[SDT]', text)
    # Che dia chi email
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL]', text)
    return text

def anonymize_dataset(input_file: str, output_file: str):
    print(f"[*] Dang doc tap du lieu tho tu: {input_file}")
    df = pd.read_csv(input_file)
    initial_rows = len(df)
    initial_cols = list(df.columns)
    print(f"[+] Tong so dong ban dau: {initial_rows}")
    print(f"[+] Cac cot ban dau: {initial_cols}")

    # 1. Loai bo cot dinh danh nguoi dung (user_name) neu ton tai
    if "user_name" in df.columns:
        df = df.drop(columns=["user_name"])
        print("[v] Da loai bo hoan toan cot dinh danh 'user_name'.")
    else:
        print("[!] Khong tim thay cot 'user_name', du lieu da khong con ten nguoi dung.")

    # 2. Quet va an danh so dien thoai, email trong cot noi dung
    if "content" in df.columns:
        df["content"] = df["content"].apply(mask_sensitive_patterns)
        print("[v] Da che giau toan bo So dien thoai va Email trong noi dung danh gia.")

    # 3. Luu du lieu da an danh
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"[v] Da xuat du lieu an toan ra: {output_file}")
    print(f"[v] Cac cot hien tai sau xu ly PII: {list(df.columns)}")
    print("[*] Hoan thanh Buoc 2: An danh hoa thong tin ca nhan (PII) thanh cong 100%!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data", "app_reviews_raw.csv")
    anon_path = os.path.join(base_dir, "data", "app_reviews_anonymized.csv")
    anonymize_dataset(raw_path, anon_path)
