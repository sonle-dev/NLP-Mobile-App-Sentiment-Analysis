# -*- coding: utf-8 -*-
"""
Module: train_models.py
Muc dich: Huan luyen, toi uu va danh gia cac mo hinh hoc may phan loai quan diem (NLP-01)
Thuoc quy trinh: Buoc 5 & 6 (Huan luyen & Danh gia mo hinh) - Nhom 12
Thuc hien: Le Hong Son (sonle-dev) - Truong nhom & Nguyen Thanh Tung
"""

import os
import sys
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix
)

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Cau hinh giao dien bieu do
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme(style="whitegrid", palette="muted")


def load_and_prepare_data(file_path: str):
    """Doc du lieu sach va phan chia thanh tap nhan nhi phan (0: Tieu cuc, 1: Tich cuc)."""
    print(f"[*] Dang doc du lieu tu: {file_path}")
    df = pd.read_csv(file_path)

    # Chon cot van ban da lam sach
    text_col = 'cleaned_content' if 'cleaned_content' in df.columns else 'content'
    df = df.dropna(subset=[text_col, 'sentiment']).copy()

    # Chuan hoa chuoi nhan
    sentiment_map = {
        'Tieu cuc': 0, 'Tiêu cực': 0,
        'Tich cuc': 1, 'Tích cực': 1
    }
    df_binary = df[df['sentiment'].isin(sentiment_map.keys())].copy()
    df_binary['label'] = df_binary['sentiment'].map(sentiment_map)

    X = df_binary[text_col].astype(str)
    y = df_binary['label'].astype(int)

    print(f"[+] Tong so mau phan loai nhi phan: {len(df_binary)}")
    print(f"    - So mau Tieu cuc (0): {sum(y == 0)} ({sum(y == 0) / len(y) * 100:.1f}%)")
    print(f"    - So mau Tich cuc (1): {sum(y == 1)} ({sum(y == 1) / len(y) * 100:.1f}%)")

    # Phan chia phan tang: 70% Train, 15% Validation, 15% Test
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=0.15, stratify=y, random_state=42
    )
    # 0.1765 * 0.85 ~ 0.15
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=0.1765, stratify=y_train_val, random_state=42
    )

    print(f"[+] Phan chia du lieu phan tang (Stratified Splitting):")
    print(f"    - Tap Train (70%):      {len(X_train)} mau")
    print(f"    - Tap Validation (15%): {len(X_val)} mau")
    print(f"    - Tap Test (15%):       {len(X_test)} mau")

    return X_train, X_val, X_test, y_train, y_val, y_test


def build_feature_extractor(X_train, X_val, X_test):
    """Trich xuat dac trung TF-IDF voi Unigrams va Bigrams, chuan hoa L2 norm."""
    print("\n[*] Dang thiet lap bo trich xuat dac trung TF-IDF (Unigrams + Bigrams)...")
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.9,
        sublinear_tf=True,
        norm='l2'
    )
    # Tuan thu nghiem ngat phong chong ro ri du lieu (Data Leakage): Chi fit tren Train
    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)
    X_test_vec = vectorizer.transform(X_test)

    print(f"[+] So luong dac trung tu vung (Vocabulary size): {len(vectorizer.vocabulary_)} tu/cum tu")
    print(f"    - Kich thuoc ma tran Train: {X_train_vec.shape}")
    print(f"    - Kich thuoc ma tran Val:   {X_val_vec.shape}")
    print(f"    - Kich thuoc ma tran Test:  {X_test_vec.shape}")

    return vectorizer, X_train_vec, X_val_vec, X_test_vec


def train_and_evaluate_models(X_train_vec, y_train, X_val_vec, y_val, X_test_vec, y_test):
    """Huan luyen 3 mo hinh (MultinomialNB, Logistic Regression, LinearSVC) va danh gia."""
    models = {
        'Multinomial Naive Bayes': MultinomialNB(alpha=1.0),
        'Logistic Regression': LogisticRegression(
            class_weight='balanced', max_iter=1000, random_state=42, C=1.0
        ),
        'Linear SVC': LinearSVC(
            class_weight='balanced', random_state=42, C=1.0, max_iter=2000
        )
    }

    results = []
    trained_models = {}

    print("\n" + "=" * 80)
    print("TIEN HANH HUAN LUYEN VA DANH GIA TREN TAP VALIDATION VA TAP TEST")
    print("=" * 80)

    for name, model in models.items():
        print(f"\n[*] Dang huan luyen: {name}...")
        model.fit(X_train_vec, y_train)
        trained_models[name] = model

        # Du doan tren tap Validation
        y_val_pred = model.predict(X_val_vec)
        val_acc = accuracy_score(y_val, y_val_pred)
        val_p = precision_score(y_val, y_val_pred, average='macro', zero_division=0)
        val_r = recall_score(y_val, y_val_pred, average='macro', zero_division=0)
        val_f1 = f1_score(y_val, y_val_pred, average='macro', zero_division=0)

        # Du doan tren tap Test
        y_test_pred = model.predict(X_test_vec)
        test_acc = accuracy_score(y_test, y_test_pred)
        test_p = precision_score(y_test, y_test_pred, average='macro', zero_division=0)
        test_r = recall_score(y_test, y_test_pred, average='macro', zero_division=0)
        test_f1 = f1_score(y_test, y_test_pred, average='macro', zero_division=0)

        results.append({
            'Mo hinh': name,
            'Val_Accuracy': val_acc,
            'Val_Precision': val_p,
            'Val_Recall': val_r,
            'Val_Macro_F1': val_f1,
            'Test_Accuracy': test_acc,
            'Test_Precision': test_p,
            'Test_Recall': test_r,
            'Test_Macro_F1': test_f1,
            'y_test_pred': y_test_pred
        })

        print(f"    [Val]  Accuracy: {val_acc:.4f} | Precision: {val_p:.4f} | Recall: {val_r:.4f} | Macro F1: {val_f1:.4f}")
        print(f"    [Test] Accuracy: {test_acc:.4f} | Precision: {test_p:.4f} | Recall: {test_r:.4f} | Macro F1: {test_f1:.4f}")

    df_results = pd.DataFrame(results)
    return trained_models, df_results


def export_evaluation_visualizations(df_results, trained_models, vectorizer, X_test, y_test, output_dir: str):
    """Xuat cac bieu do so sanh, ma tran nham lan va dac trung quan trong nhat."""
    os.makedirs(output_dir, exist_ok=True)

    # 1. Bieu do so sanh hieu nang cac mo hinh
    fig, ax = plt.subplots(figsize=(10, 6))
    metrics = ['Test_Accuracy', 'Test_Precision', 'Test_Recall', 'Test_Macro_F1']
    metric_names = ['Accuracy', 'Precision', 'Recall', 'Macro F1']

    x = np.arange(len(df_results))
    width = 0.2

    for i, (m, label) in enumerate(zip(metrics, metric_names)):
        bars = ax.bar(x + i * width, df_results[m], width, label=label)
        for b in bars:
            h = b.get_height()
            ax.annotate(f'{h:.3f}', xy=(b.get_x() + b.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

    ax.set_title('So sanh hieu nang cac mo hinh hoc may tren tap Test', fontsize=13, fontweight='bold')
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(df_results['Mo hinh'], fontweight='bold')
    ax.set_ylabel('Diem so danh gia (0.0 - 1.0)')
    ax.set_ylim(0.7, 1.0)
    ax.legend(loc='lower right')
    plt.tight_layout()
    comp_path = os.path.join(output_dir, 'model_comparison.png')
    plt.savefig(comp_path, dpi=300)
    plt.close()
    print(f"[v] Da xuat bieu do so sanh mo hinh tai: {comp_path}")

    # 2. Xac dinh mo hinh xuat sac nhat dua tren Test_Macro_F1
    best_row = df_results.loc[df_results['Test_Macro_F1'].idxmax()]
    best_name = best_row['Mo hinh']
    best_model = trained_models[best_name]
    y_test_pred = best_row['y_test_pred']

    print(f"\n[★] MO HINH TOT NHAT: {best_name} (Test Macro F1 = {best_row['Test_Macro_F1']:.4f})")

    # 3. Ma tran nham lan (Confusion Matrix)
    cm = confusion_matrix(y_test, y_test_pred)
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues', cbar=False,
        xticklabels=['Tiêu cực (0)', 'Tích cực (1)'],
        yticklabels=['Tiêu cực (0)', 'Tích cực (1)'],
        ax=ax, annot_kws={'fontsize': 13, 'fontweight': 'bold'}
    )
    ax.set_title(f'Ma tran nham lan - {best_name}\n(Tap Test: {len(y_test)} mau)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Nhan du doan (Predicted Label)', fontweight='bold')
    ax.set_ylabel('Nhan thuc te (True Label)', fontweight='bold')
    plt.tight_layout()
    cm_path = os.path.join(output_dir, 'confusion_matrix_best_model.png')
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"[v] Da xuat ma tran nham lan tai: {cm_path}")

    # 4. Trac xuat dac trung tu vung quan trong (Feature Importance)
    feature_names = np.array(vectorizer.get_feature_names_out())
    if hasattr(best_model, 'coef_'):
        coef = best_model.coef_[0]
        top_neg_idx = np.argsort(coef)[:15]
        top_pos_idx = np.argsort(coef)[-15:][::-1]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Top tu khoa Tieu cuc (trong so am lon nhat)
        ax1.barh(feature_names[top_neg_idx][::-1], -coef[top_neg_idx][::-1], color='#e74c3c')
        ax1.set_title('Top 15 tu khoa dac trung TIÊU CỰC manh nhat', fontsize=11, fontweight='bold')
        ax1.set_xlabel('Do lon trong so mo hinh')

        # Top tu khoa Tich cuc (trong so duong lon nhat)
        ax2.barh(feature_names[top_pos_idx][::-1], coef[top_pos_idx][::-1], color='#2ecc71')
        ax2.set_title('Top 15 tu khoa dac trung TÍCH CỰC manh nhat', fontsize=11, fontweight='bold')
        ax2.set_xlabel('Do lon trong so mo hinh')

        plt.tight_layout()
        feat_path = os.path.join(output_dir, 'top_features.png')
        plt.savefig(feat_path, dpi=300)
        plt.close()
        print(f"[v] Da xuat bieu do dac trung quan trong tai: {feat_path}")

    # 5. Phan tich sai so (Error Analysis) - Top mau du doan sai
    errors = pd.DataFrame({
        'content': X_test.values,
        'true_label': y_test.values,
        'pred_label': y_test_pred
    })
    errors_df = errors[errors['true_label'] != errors['pred_label']]
    print(f"\n[!] Tong so mau du doan sai tren tap Test: {len(errors_df)} / {len(y_test)} ({len(errors_df)/len(y_test)*100:.2f}%)")

    return best_name, best_model, df_results


def save_trained_artifacts(best_model, vectorizer, output_dirs):
    """Luu mo hinh va bo vector hoa de phuc vu Web Demo va kiem tra."""
    for d in output_dirs:
        os.makedirs(d, exist_ok=True)
        joblib.dump(best_model, os.path.join(d, 'best_sentiment_model.joblib'))
        joblib.dump(vectorizer, os.path.join(d, 'tfidf_vectorizer.joblib'))
        print(f"[v] Da luu model va vectorizer tai: {d}")


def main():
    base_dir = r"d:\HocMayPrJ"
    data_path = os.path.join(base_dir, "Nhom_12", "Code_va_Data_Nhom12", "data", "app_reviews_cleaned.csv")
    if not os.path.exists(data_path):
        data_path = os.path.join(base_dir, "data", "app_reviews_cleaned.csv")

    fig_dir = os.path.join(base_dir, "reports", "figures")
    fig_dir2 = os.path.join(base_dir, "Nhom_12", "Code_va_Data_Nhom12", "figures")
    model_dirs = [
        os.path.join(base_dir, "models"),
        os.path.join(base_dir, "Nhom_12", "Code_va_Data_Nhom12", "models")
    ]

    # Quy trinh 4 buoc
    X_train, X_val, X_test, y_train, y_val, y_test = load_and_prepare_data(data_path)
    vectorizer, X_train_vec, X_val_vec, X_test_vec = build_feature_extractor(X_train, X_val, X_test)
    trained_models, df_results = train_and_evaluate_models(
        X_train_vec, y_train, X_val_vec, y_val, X_test_vec, y_test
    )
    best_name, best_model, df_results = export_evaluation_visualizations(
        df_results, trained_models, vectorizer, X_test, y_test, fig_dir
    )
    export_evaluation_visualizations(
        df_results, trained_models, vectorizer, X_test, y_test, fig_dir2
    )
    save_trained_artifacts(best_model, vectorizer, model_dirs)

    print("\n" + "=" * 80)
    print("HOAN THANH XUAT SAC QUY TRINH HUAN LUYEN VA DANH GIA MO HINH!")
    print("=" * 80)


if __name__ == '__main__':
    main()
