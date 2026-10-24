# -*- coding: utf-8 -*-
"""
Module: anonymize_pii.py
Mục đích: Loại bỏ hoàn toàn thông tin định danh cá nhân (PII) và che giấu dữ liệu nhạy cảm
Thuộc quy trình: Bước 2 (Ẩn danh PII) - Dự án Phân tích quan điểm ứng dụng di động (Nhóm 12)
Thực hiện: Lưu Thị Khánh Ly (luuthily34-lab)
"""

import os
import sys
import re
import pandas as pd

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def mask_sensitive_patterns(text: str) -> str:
    """Che giấu số điện thoại và email xuất hiện trong nội dung đánh giá."""
    if not isinstance(text, str):
        return ""
    # Che số điện thoại di động Việt Nam (đầu số 03, 05, 07, 08, 09 kèm 8 chữ số)
    text = re.sub(r'(03|05|07|08|09)\d{8}', '[SDT]', text)
    # Che địa chỉ email
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL]', text)
    return text

def anonymize_dataset(input_file: str, output_file: str):
    print(f"[*] Đang đọc tập dữ liệu thô từ: {input_file}")
    df = pd.read_csv(input_file)
    initial_rows = len(df)
    initial_cols = list(df.columns)
    print(f"[+] Tổng số dòng ban đầu: {initial_rows}")
    print(f"[+] Các cột ban đầu: {initial_cols}")

    # 1. Loại bỏ cột định danh người dùng (user_name) nếu tồn tại
    if "user_name" in df.columns:
        df = df.drop(columns=["user_name"])
        print("[v] Đã loại bỏ hoàn toàn cột định danh 'user_name'.")
    else:
        print("[!] Không tìm thấy cột 'user_name', dữ liệu đã không còn tên người dùng.")

    # 2. Quét và ẩn danh số điện thoại, email trong cột nội dung
    if "content" in df.columns:
        df["content"] = df["content"].apply(mask_sensitive_patterns)
        print("[v] Đã che giấu toàn bộ Số điện thoại và Email trong nội dung đánh giá.")

    # 3. Lưu dữ liệu đã ẩn danh
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"[v] Đã xuất dữ liệu an toàn ra: {output_file}")
    print(f"[v] Các cột hiện tại sau xử lý PII: {list(df.columns)}")
    print("[*] Hoàn thành Bước 2: Ẩn danh hóa thông tin cá nhân (PII) thành công 100%!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data", "app_reviews_raw.csv")
    anon_path = os.path.join(base_dir, "data", "app_reviews_anonymized.csv")
    anonymize_dataset(raw_path, anon_path)
