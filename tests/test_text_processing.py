import re
import pytest

TEENCODE_DICT = {
    "ko": "không",
    "k": "không",
    "khong": "không",
    "dc": "được",
    "đc": "được",
    "rat": "rất",
    "tốt": "tốt",
    "oke": "tốt",
    "ok": "tốt",
    "lag": "chậm",
    "đơ": "chậm"
}

def clean_vietnamese_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    # Replace teencode
    words = text.split()
    words = [TEENCODE_DICT.get(w, w) for w in words]
    text = " ".join(words)
    # Remove digits
    text = re.sub(r"\d+", " ", text)
    # Remove special chars and punctuation
    text = re.sub(r"[^\w\sàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def test_lowercase_conversion():
    raw = "Ứng Dụng Rất Tuyệt Vời"
    cleaned = clean_vietnamese_text(raw)
    assert cleaned == "ứng dụng rất tuyệt vời"

def test_teencode_standardization():
    raw = "app k dùng dc rat lag"
    cleaned = clean_vietnamese_text(raw)
    assert "không" in cleaned
    assert "được" in cleaned
    assert "rất" in cleaned
    assert "chậm" in cleaned

def test_special_characters_removal():
    raw = "Shopee tệ quá!!! 😡😡😡 Đơ suốt ngày... $$$ 123"
    cleaned = clean_vietnamese_text(raw)
    assert "!" not in cleaned
    assert "$" not in cleaned
    assert "123" not in cleaned
