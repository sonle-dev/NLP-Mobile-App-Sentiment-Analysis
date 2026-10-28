# -*- coding: utf-8 -*-
"""
Module: visualize_eda.py
Muc dich: Phan tich kham pha du lieu (EDA) va xuat cac bieu do truc quan hoa du lieu sach
Thuoc quy trinh: Buoc 4 (Ve bieu do EDA phan tich du lieu) - Du an Phan tich quan diem ung dung di dong (Nhom 12)
Thuc hien: Luu Thi Khanh Ly (luuthily34-lab)
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Cau hinh font va phong cach hien thi hoc thuat
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme(style="whitegrid", palette="muted")

def generate_eda_visualizations(data_path: str, output_dir: str):
    print(f"[*] Dang nap du lieu sach tu: {data_path}")
    df = pd.read_csv(data_path)
    os.makedirs(output_dir, exist_ok=True)
    print(f"[+] Tong so dong du lieu: {len(df):,} mau")

    # Bang mau chuan
    colors = {
        'Tiêu cực': '#e74c3c',   # Do cam
        'Tích cực': '#2ecc71',   # Xanh la
        'Trung tính': '#3498db'  # Xanh duong
    }

    # -------------------------------------------------------------
    # 1. Bieu do phan bo cam xuc tong the (Donut + Bar Chart)
    # -------------------------------------------------------------
    print("[*] Dang xuat Bieu do 1: Phan bo nhan cam xuc...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    sentiment_counts = df['sentiment'].value_counts()
    sentiment_percent = df['sentiment'].value_counts(normalize=True) * 100

    # Donut Chart
    palette_list = [colors.get(x, '#95a5a6') for x in sentiment_counts.index]
    wedges, texts, autotexts = ax1.pie(
        sentiment_counts, 
        labels=sentiment_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=palette_list,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2),
        textprops=dict(size=12, weight='bold')
    )
    ax1.set_title("Ty le phan bo nhan cam xuc tong the", fontsize=14, weight='bold', pad=15)

    # Bar Chart
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=ax2, palette=palette_list, hue=sentiment_counts.index, legend=False)
    for i, v in enumerate(sentiment_counts.values):
        ax2.text(i, v + 150, f"{v:,} ({sentiment_percent.values[i]:.1f}%)", ha='center', fontsize=11, weight='bold')
    ax2.set_title("So luong mau theo tung lop cam xuc", fontsize=14, weight='bold', pad=15)
    ax2.set_ylabel("So luong danh gia", fontsize=12)
    ax2.set_xlabel("Lop nhan cam xuc", fontsize=12)

    plt.tight_layout()
    fig1_path = os.path.join(output_dir, "eda_sentiment_distribution.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"[v] Da luu: {fig1_path}")

    # -------------------------------------------------------------
    # 2. Bieu do phan bo so luong danh gia theo 8 ung dung
    # -------------------------------------------------------------
    print("[*] Dang xuat Bieu do 2: So luong danh gia theo tung ung dung...")
    fig, ax = plt.subplots(figsize=(12, 6))
    app_counts = df['app_name'].value_counts()
    sns.barplot(x=app_counts.values, y=app_counts.index, ax=ax, palette="Blues_r", hue=app_counts.index, legend=False)
    for i, v in enumerate(app_counts.values):
        ax.text(v + 30, i, f"{v:,} ({v/len(df)*100:.1f}%)", va='center', fontsize=10, weight='bold')
    ax.set_title("So luong danh gia thu thap theo tung ung dung (8 Apps)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("So luong mau", fontsize=12)
    ax.set_ylabel("Ten ung dung", fontsize=12)

    plt.tight_layout()
    fig2_path = os.path.join(output_dir, "eda_reviews_per_app.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"[v] Da luu: {fig2_path}")

    # -------------------------------------------------------------
    # 3. Bieu do phan bo cam xuc theo tung ung dung (Stacked Bar Chart)
    # -------------------------------------------------------------
    print("[*] Dang xuat Bieu do 3: Ty le cam xuc theo tung ung dung...")
    app_sentiment = pd.crosstab(df['app_name'], df['sentiment'], normalize='index') * 100
    # Dam bao thu tu cot
    order_cols = [c for c in ['Tiêu cực', 'Trung tính', 'Tích cực'] if c in app_sentiment.columns]
    app_sentiment = app_sentiment[order_cols]

    fig, ax = plt.subplots(figsize=(12, 7))
    app_sentiment.plot(
        kind='barh', 
        stacked=True, 
        color=[colors[c] for c in order_cols], 
        ax=ax, 
        edgecolor='white', 
        linewidth=1.2
    )
    ax.set_title("Ty le phan bo cam xuc chi tiet theo tung ung dung (%)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Ty le phan tram (%)", fontsize=12)
    ax.set_ylabel("Ung dung", fontsize=12)
    ax.legend(title="Lớp cảm xúc", loc='lower right', frameon=True)

    # Hien thi text phan tram tren bar
    for c in ax.containers:
        ax.bar_label(c, fmt='%.1f%%', label_type='center', color='white', weight='bold', fontsize=9)

    plt.tight_layout()
    fig3_path = os.path.join(output_dir, "eda_sentiment_by_app.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"[v] Da luu: {fig3_path}")

    # -------------------------------------------------------------
    # 4. Bieu do phan phoi do dai tu vung (Word Count Distribution)
    # -------------------------------------------------------------
    print("[*] Dang xuat Bieu do 4: Phan phoi do dai tu vung...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Boxplot
    sns.boxplot(x='sentiment', y='word_count', data=df, ax=ax1, palette=palette_list, hue='sentiment', legend=False, showfliers=False)
    ax1.set_title("Do dai van ban (So tu) theo tung nhan cam xuc", fontsize=13, weight='bold')
    ax1.set_xlabel("Nhan cam xuc", fontsize=11)
    ax1.set_ylabel("So luong tu (Word Count)", fontsize=11)

    # Histogram + KDE
    sns.histplot(df['word_count'], bins=40, kde=True, ax=ax2, color='#184C78', binrange=(1, 80))
    ax2.set_title("Phan bo so luong tu vung cua phan hoi nguoi dung", fontsize=13, weight='bold')
    ax2.set_xlabel("So luong tu trong moi danh gia", fontsize=11)
    ax2.set_ylabel("Tan suat xuat hien", fontsize=11)

    plt.tight_layout()
    fig4_path = os.path.join(output_dir, "eda_word_length_distribution.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"[v] Da luu: {fig4_path}")

    # -------------------------------------------------------------
    # 5. Tong hop Dashboard EDA Overview (2x2)
    # -------------------------------------------------------------
    print("[*] Dang xuat Bieu do 5: Dashboard EDA Tong Quan 2x2...")
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))

    # [0, 0] Donut chart
    axs[0, 0].pie(
        sentiment_counts, 
        labels=sentiment_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=palette_list,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2),
        textprops=dict(size=11, weight='bold')
    )
    axs[0, 0].set_title("(A) Phan bo 3 lop nhan cam xuc", fontsize=13, weight='bold')

    # [0, 1] App counts
    sns.barplot(x=app_counts.values, y=app_counts.index, ax=axs[0, 1], palette="Blues_r", hue=app_counts.index, legend=False)
    axs[0, 1].set_title("(B) Khoi luong du lieu theo 8 ung dung", fontsize=13, weight='bold')
    axs[0, 1].set_xlabel("So mau")

    # [1, 0] Platform distribution
    platform_counts = df['platform'].value_counts()
    sns.barplot(x=platform_counts.index, y=platform_counts.values, ax=axs[1, 0], palette=["#27ae60", "#2980b9"], hue=platform_counts.index, legend=False)
    for i, v in enumerate(platform_counts.values):
        axs[1, 0].text(i, v + 100, f"{v:,} ({v/len(df)*100:.1f}%)", ha='center', weight='bold')
    axs[1, 0].set_title("(C) So sanh du lieu Google Play vs App Store", fontsize=13, weight='bold')
    axs[1, 0].set_ylabel("So luong danh gia")

    # [1, 1] Word count distribution
    sns.histplot(df['word_count'], bins=35, kde=True, ax=axs[1, 1], color='#8e44ad', binrange=(1, 70))
    axs[1, 1].set_title("(D) Phan phoi do dai tu vung (Word Count)", fontsize=13, weight='bold')
    axs[1, 1].set_xlabel("So luong tu trong moi danh gia")
    axs[1, 1].set_ylabel("Tan suat")

    plt.tight_layout()
    fig5_path = os.path.join(output_dir, "eda_overview.png")
    plt.savefig(fig5_path, dpi=300)
    plt.close()
    print(f"[v] Da luu: {fig5_path}")
    print("[*] Hoan thanh xuat toan bo 5 bieu do EDA chat luong cao thanh cong 100%!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "app_reviews_cleaned.csv")
    out_dir = os.path.join(base_dir, "reports", "figures")
    generate_eda_visualizations(data_file, out_dir)
