# -*- coding: utf-8 -*-
"""
Module: visualize_eda.py
Mục đích: Phân tích khám phá dữ liệu (EDA) và xuất các biểu đồ trực quan hóa dữ liệu sạch
Thuộc quy trình: Bước 4 (Vẽ biểu đồ EDA phân tích dữ liệu) - Dự án Phân tích quan điểm ứng dụng di động (Nhóm 12)
Thực hiện: Lưu Thị Khánh Ly (luuthily34-lab)
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Cấu hình font và phong cách hiển thị học thuật
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme(style="whitegrid", palette="muted")

def generate_eda_visualizations(data_path: str, output_dir: str):
    print(f"[*] Đang nạp dữ liệu sạch từ: {data_path}")
    df = pd.read_csv(data_path)
    os.makedirs(output_dir, exist_ok=True)
    print(f"[+] Tổng số dòng dữ liệu: {len(df):,} mẫu")

    # Bảng màu chuẩn
    colors = {
        'Tiêu cực': '#e74c3c',   # Đỏ cam
        'Tích cực': '#2ecc71',   # Xanh lá
        'Trung tính': '#3498db'  # Xanh dương
    }

    # -------------------------------------------------------------
    # 1. Biểu đồ phân bố cảm xúc tổng thể (Donut + Bar Chart)
    # -------------------------------------------------------------
    print("[*] Đang xuất Biểu đồ 1: Phân bố nhãn cảm xúc...")
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
    ax1.set_title("Tỷ lệ phân bố nhãn cảm xúc tổng thể", fontsize=14, weight='bold', pad=15)

    # Bar Chart
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=ax2, palette=palette_list, hue=sentiment_counts.index, legend=False)
    for i, v in enumerate(sentiment_counts.values):
        ax2.text(i, v + 150, f"{v:,} ({sentiment_percent.values[i]:.1f}%)", ha='center', fontsize=11, weight='bold')
    ax2.set_title("Số lượng mẫu theo từng lớp cảm xúc", fontsize=14, weight='bold', pad=15)
    ax2.set_ylabel("Số lượng đánh giá", fontsize=12)
    ax2.set_xlabel("Lớp nhãn cảm xúc", fontsize=12)

    plt.tight_layout()
    fig1_path = os.path.join(output_dir, "eda_sentiment_distribution.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"[v] Đã lưu: {fig1_path}")

    # -------------------------------------------------------------
    # 2. Biểu đồ phân bố số lượng đánh giá theo 8 ứng dụng
    # -------------------------------------------------------------
    print("[*] Đang xuất Biểu đồ 2: Số lượng đánh giá theo từng ứng dụng...")
    fig, ax = plt.subplots(figsize=(12, 6))
    app_counts = df['app_name'].value_counts()
    sns.barplot(x=app_counts.values, y=app_counts.index, ax=ax, palette="Blues_r", hue=app_counts.index, legend=False)
    for i, v in enumerate(app_counts.values):
        ax.text(v + 30, i, f"{v:,} ({v/len(df)*100:.1f}%)", va='center', fontsize=10, weight='bold')
    ax.set_title("Số lượng đánh giá thu thập theo từng ứng dụng (8 Apps)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Số lượng mẫu", fontsize=12)
    ax.set_ylabel("Tên ứng dụng", fontsize=12)

    plt.tight_layout()
    fig2_path = os.path.join(output_dir, "eda_reviews_per_app.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"[v] Đã lưu: {fig2_path}")

    # -------------------------------------------------------------
    # 3. Biểu đồ phân bố cảm xúc theo từng ứng dụng (Stacked Bar Chart)
    # -------------------------------------------------------------
    print("[*] Đang xuất Biểu đồ 3: Tỷ lệ cảm xúc theo từng ứng dụng...")
    app_sentiment = pd.crosstab(df['app_name'], df['sentiment'], normalize='index') * 100
    # Đảm bảo thứ tự cột
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
    ax.set_title("Tỷ lệ phân bố cảm xúc chi tiết theo từng ứng dụng (%)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Tỷ lệ phần trăm (%)", fontsize=12)
    ax.set_ylabel("Ứng dụng", fontsize=12)
    ax.legend(title="Lớp cảm xúc", loc='lower right', frameon=True)

    # Hiển thị text phần trăm trên bar
    for c in ax.containers:
        ax.bar_label(c, fmt='%.1f%%', label_type='center', color='white', weight='bold', fontsize=9)

    plt.tight_layout()
    fig3_path = os.path.join(output_dir, "eda_sentiment_by_app.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"[v] Đã lưu: {fig3_path}")

    # -------------------------------------------------------------
    # 4. Biểu đồ phân phối độ dài từ vựng (Word Count Distribution)
    # -------------------------------------------------------------
    print("[*] Đang xuất Biểu đồ 4: Phân phối độ dài từ vựng...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Boxplot
    sns.boxplot(x='sentiment', y='word_count', data=df, ax=ax1, palette=palette_list, hue='sentiment', legend=False, showfliers=False)
    ax1.set_title("Độ dài văn bản (Số từ) theo từng nhãn cảm xúc", fontsize=13, weight='bold')
    ax1.set_xlabel("Nhãn cảm xúc", fontsize=11)
    ax1.set_ylabel("Số lượng từ (Word Count)", fontsize=11)

    # Histogram + KDE
    sns.histplot(df['word_count'], bins=40, kde=True, ax=ax2, color='#184C78', binrange=(1, 80))
    ax2.set_title("Phân bố số lượng từ vựng của phản hồi người dùng", fontsize=13, weight='bold')
    ax2.set_xlabel("Số lượng từ trong mỗi đánh giá", fontsize=11)
    ax2.set_ylabel("Tần suất xuất hiện", fontsize=11)

    plt.tight_layout()
    fig4_path = os.path.join(output_dir, "eda_word_length_distribution.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"[v] Đã lưu: {fig4_path}")

    # -------------------------------------------------------------
    # 5. Tổng hợp Dashboard EDA Overview (2x2)
    # -------------------------------------------------------------
    print("[*] Đang xuất Biểu đồ 5: Dashboard EDA Tổng Quan 2x2...")
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
    axs[0, 0].set_title("(A) Phân bố 3 lớp nhãn cảm xúc", fontsize=13, weight='bold')

    # [0, 1] App counts
    sns.barplot(x=app_counts.values, y=app_counts.index, ax=axs[0, 1], palette="Blues_r", hue=app_counts.index, legend=False)
    axs[0, 1].set_title("(B) Khối lượng dữ liệu theo 8 ứng dụng", fontsize=13, weight='bold')
    axs[0, 1].set_xlabel("Số mẫu")

    # [1, 0] Platform distribution
    platform_counts = df['platform'].value_counts()
    sns.barplot(x=platform_counts.index, y=platform_counts.values, ax=axs[1, 0], palette=["#27ae60", "#2980b9"], hue=platform_counts.index, legend=False)
    for i, v in enumerate(platform_counts.values):
        axs[1, 0].text(i, v + 100, f"{v:,} ({v/len(df)*100:.1f}%)", ha='center', weight='bold')
    axs[1, 0].set_title("(C) So sánh dữ liệu Google Play vs App Store", fontsize=13, weight='bold')
    axs[1, 0].set_ylabel("Số lượng đánh giá")

    # [1, 1] Word count distribution
    sns.histplot(df['word_count'], bins=35, kde=True, ax=axs[1, 1], color='#8e44ad', binrange=(1, 70))
    axs[1, 1].set_title("(D) Phân phối độ dài từ vựng (Word Count)", fontsize=13, weight='bold')
    axs[1, 1].set_xlabel("Số lượng từ trong mỗi đánh giá")
    axs[1, 1].set_ylabel("Tần suất")

    plt.tight_layout()
    fig5_path = os.path.join(output_dir, "eda_overview.png")
    plt.savefig(fig5_path, dpi=300)
    plt.close()
    print(f"[v] Đã lưu: {fig5_path}")
    print("[*] Hoàn thành xuất toàn bộ 5 biểu đồ EDA chất lượng cao thành công 100%!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "app_reviews_cleaned.csv")
    out_dir = os.path.join(base_dir, "reports", "figures")
    generate_eda_visualizations(data_file, out_dir)
