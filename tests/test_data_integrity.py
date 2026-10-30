import os
import pandas as pd
import pytest

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "app_reviews_cleaned.csv")

def test_dataset_exists():
    assert os.path.exists(DATA_PATH), f"Tập dữ liệu đã làm sạch không tồn tại tại {DATA_PATH}"

def test_pii_removed():
    """Kiểm tra tuân thủ đạo đức dữ liệu: Cột user_name tuyệt đối không được có trong file sạch."""
    df = pd.read_csv(DATA_PATH)
    assert "user_name" not in df.columns, "Lỗi bảo mật PII: Vẫn còn cột user_name trong tập dữ liệu!"

def test_labels_validity():
    """Kiểm tra tính hợp lệ của nhãn cảm xúc (Tiêu cực, Tích cực, Trung tính)."""
    df = pd.read_csv(DATA_PATH)
    valid_labels = {"Tiêu cực", "Trung tính", "Tích cực", "negative", "neutral", "positive"}
    actual_labels = set(df["sentiment"].dropna().unique())
    assert actual_labels.issubset(valid_labels), f"Nhãn không hợp lệ phát hiện: {actual_labels - valid_labels}"

def test_no_empty_reviews():
    """Kiểm tra không có đánh giá nào bị rỗng nội dung sau khi làm sạch."""
    df = pd.read_csv(DATA_PATH)
    content_col = "cleaned_content" if "cleaned_content" in df.columns else "clean_content"
    null_count = df[content_col].isnull().sum()
    assert null_count == 0, f"Có {null_count} bản ghi có nội dung văn bản bị rỗng!"

def test_dataset_size():
    """Kiểm tra quy mô dữ liệu đạt chuẩn yêu cầu giảng viên (> 10.000 mẫu)."""
    df = pd.read_csv(DATA_PATH)
    assert len(df) >= 10000, f"Dung lượng dữ liệu quá nhỏ ({len(df)} mẫu), yêu cầu tối thiểu 10.000 mẫu!"
