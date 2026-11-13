import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import pandas as pd
from underthesea import word_tokenize

print("=== BAT DAU PIPELINE LLM & ASPECT RULE-BASED LABELING ===")

# 1. Doc du lieu da lam sach
data_path = 'd:/HocMayPrJ/data/app_reviews_cleaned.csv'
df = pd.read_csv(data_path)
print(f"Tong so mau: {len(df)}")

# 2. Xay dung tu dien tu khoa chinh xac cho 4 nhom Aspect (Khia canh)
aspect_keywords = {
    'Hieu_nang_UI_UX': [
        'lag', 'giật', 'giat', 'đơ', 'do', 'văng', 'vang', 'treo', 'chậm', 'cham',
        'load', 'tải', 'tai', 'cập nhật', 'cap nhat', 'update', 'phiên bản', 'phien ban',
        'giao diện', 'giao dien', 'màu sắc', 'mau sac', 'font', 'chữ', 'chu',
        'khó dùng', 'kho dung', 'rối mắt', 'roi mat', 'mượt', 'muot', 'mượt mà', 'muot ma',
        'tiện ích', 'tien ich', 'dễ dùng', 'de dung', 'thao tác', 'thao tac', 'app như rác',
        'nâng cấp', 'nang cap', 'tối ưu', 'toi uu', 'bộ nhớ', 'bo nho', 'nặng máy', 'nang may'
    ],
    'Giao_dich_Thanh_toan': [
        'chuyển tiền', 'chuyen tien', 'ck', 'chuyển khoản', 'chuyen khoan', 'giao dịch', 'giao dich',
        'nạp tiền', 'nap tien', 'rút tiền', 'rut tien', 'thanh toán', 'thanh toan', 'tiền', 'tien',
        'trừ tiền', 'tru tien', 'mất tiền', 'mat tien', 'hoàn tiền', 'hoan tien', 'phí', 'phi',
        'biến động số dư', 'bien dong so du', 'thông báo số dư', 'stk', '[stk]', 'tài khoản nguồn',
        'thẻ', 'the', 'nuốt thẻ', 'nuot the', 'atm', 'quét qr', 'quet qr', 'qr', 'ví', 'vi',
        'chuyển nhanh', 'chuyen nhanh', 'napas', 'liên ngân hàng', 'lien ngan hang', 'lãi suất', 'lai suat'
    ],
    'Bao_mat_Tai_khoan': [
        'đăng nhập', 'dang nhap', 'login', 'mật khẩu', 'mat khau', 'pass', 'password',
        'otp', 'mã otp', 'ma otp', 'smart otp', 'sinh trắc học', 'sinh trac hoc', 'vneid',
        'căn cước', 'can cuoc', 'cccd', 'khuôn mặt', 'khuon mat', 'face id', 'faceid',
        'vân tay', 'van tay', 'khóa tài khoản', 'khoa tai khoan', 'khóa app', 'khoa app',
        'bị khóa', 'bi khoa', 'bảo mật', 'bao mat', 'lừa đảo', 'lua dao', 'chiếm đoạt', 'chiem doat',
        'xác thực', 'xac thuc', 'định danh', 'dinh danh', 'quên mật khẩu', 'quen mat khau'
    ],
    'Dich_vu_CSKH': [
        'tổng đài', 'tong dai', 'hotline', 'nhân viên', 'nhan vien', 'cskh', 'chăm sóc', 'cham soc',
        'hỗ trợ', 'ho tro', 'support', 'phục vụ', 'phuc vu', 'thái độ', 'thai do', 'chi nhánh', 'chi nhanh',
        'phòng giao dịch', 'pgd', 'giải quyết', 'giai quyet', 'khiếu nại', 'khieu nai', 'phản hồi', 'phan hoi',
        'khuyến mãi', 'khuyen mai', 'voucher', 'xu', 'mã giảm giá', 'ma giam gia', 'quà', 'qua', 'ưu đãi', 'uu dai'
    ]
}

def extract_aspect(text: str) -> str:
    text_lower = str(text).lower()
    scores = {}
    for aspect, kws in aspect_keywords.items():
        score = sum(1 for kw in kws if re.search(r'\b' + re.escape(kw) + r'\b', text_lower))
        scores[aspect] = score
    
    max_score = max(scores.values())
    if max_score > 0:
        for aspect, score in scores.items():
            if score == max_score:
                return aspect
    return 'Hieu_nang_UI_UX'  # Mac dinh ve trai nghiem app neu khong chua tu khoa dac thu

# 3. Tu dien tu khoa cam xuc manh de phat hien nghich nhan (Cham biem / Danh 5 sao che)
strong_negative_kws = [
    'lừa đảo', 'lua dao', 'quá tệ', 'qua te', 'như rác', 'nhu rac', 'bực mình', 'buc minh',
    'bực bội', 'buc boi', 'tồi tệ', 'toi te', 'rác rưởi', 'rac ruoi', 'thất vọng', 'that vong',
    'chán nản', 'chan nan', 'vứt đi', 'vut di', 'tẩy chay', 'tay chay', 'khốn nạn', 'chó chết',
    'ăn cướp', 'an cuop', 'mất dạy', 'mat day', 'chết tiệt', 'chet tiet', 'lỗi tùm lum', 'loi tum lum',
    'không dùng được', 'khong dung duoc', 'không vào được', 'khong vao duoc', 'lỗi liên tục', 'loi lien tuc',
    'lừa đảo trắng trợn', 'app lừa', 'trừ tiền vô lý', 'bị trừ tiền mà không nhận'
]

strong_positive_kws = [
    'rất tuyệt vời', 'rat tuyet voi', 'quá tuyệt vời', 'qua tuyet voi', 'quá tốt', 'qua tot',
    'cực kỳ hài lòng', 'cuc ky hai long', 'rất mượt mà', 'rat muot ma', 'xuất sắc', 'xuat sac',
    'trên cả tuyệt vời', 'dịch vụ tuyệt vời', 'ưng ý', 'ung y', '10 điểm', '10 diem', '5 sao tuyệt đối',
    'rất tiện lợi', 'rat tien loi', 'yêu thích ứng dụng', 'cảm ơn agribank', 'cảm ơn ngân hàng',
    'dùng rất thích', 'dung rat thich', 'quá đỉnh', 'qua dinh', 'tiện ích tuyệt vời'
]

# 4. Ham gop xep nhan Sentiment ket hop: Rating + Tu khoa cam xuc manh (Rule-based & LLM logic)
# Quy uoc mac dinh: 1, 2, 3 sao la Tieu cuc (0); 4, 5 sao la Tich cuc (1)
# Dieu chinh:
# - Neu 4, 5 sao ma chua tu khoa chui/che nang (tam ly cham 5 sao de len top) -> Chuyen sang Tieu cuc (0)
# - Neu 1, 2, 3 sao ma thuc su la khen tuyet doi khong he co tu phan nan -> Chuyen sang Tich cuc (1)
def assign_refined_sentiment(rating: int, content: str) -> tuple[int, str, str]:
    text_lower = str(content).lower()
    r = int(rating)
    
    has_strong_neg = any(kw in text_lower for kw in strong_negative_kws)
    has_strong_pos = any(kw in text_lower for kw in strong_positive_kws)
    
    # Kiem tra truong hop 4, 5 sao nhung chui tham te
    if r in [4, 5] and has_strong_neg and not has_strong_pos:
        return 0, 'Tieu cuc', 'Nghich_nhan_5sao_che'
    
    # Kiem tra truong hop 1, 2 sao nhung khen het loi (khong he co chu khong/loi)
    if r in [1, 2] and has_strong_pos and not any(k in text_lower for k in ['không', 'khong', 'chưa', 'chua', 'lỗi', 'loi', 'tệ', 'te']):
        return 1, 'Tich cuc', 'Nghich_nhan_1sao_khen'
    
    # Mac dinh theo quy tac cua nguoi dung: 1, 2, 3 sao = Tieu cuc; 4, 5 sao = Tich cuc
    if r in [1, 2, 3]:
        return 0, 'Tieu cuc', 'Chuan_1_3_sao'
    else:
        return 1, 'Tich cuc', 'Chuan_4_5_sao'

# 5. Ap dung gan nhan Aspect va Sentiment
print("Dang phan tich khia canh (Aspect) va chuan hoa nhan cam xuc...")
aspects = []
sentiments = []
labels = []
label_types = []

for idx, row in df.iterrows():
    asp = extract_aspect(row['content'])
    lbl, sent, ltype = assign_refined_sentiment(row['rating'], row['content'])
    aspects.append(asp)
    sentiments.append(sent)
    labels.append(lbl)
    label_types.append(ltype)

df['aspect_category'] = aspects
df['sentiment'] = sentiments
df['label'] = labels
df['label_audit_type'] = label_types

# 6. Ap dung tach tu tieng Viet (Word Segmentation) qua underthesea de phuc vu spaCy pipeline
print("Dang tach tu tieng Viet chuan (Word Segmentation) cho cot cleaned_content...")
def segment_vietnamese(text: str) -> str:
    try:
        return word_tokenize(str(text), format='text')
    except Exception:
        return str(text)

df['segmented_content'] = df['cleaned_content'].apply(segment_vietnamese)

print("\n=== THONG KE PHAN PHOI KHIA CANH (ASPECT CATEGORIES) ===")
print(df['aspect_category'].value_counts())

print("\n=== THONG KE PHAN PHOI NHAN CAM XUC (REFINED SENTIMENT) ===")
print(df['sentiment'].value_counts())

print("\n=== SO LUONG MAU NGHICH NHAN DA DUOC PHAT HIEN & XU LY ===")
print(df['label_audit_type'].value_counts())

# 7. Luu ra cac file CSV va Excel
print("\nDang luu du lieu vao cac thu muc data/ va Nhom_12/...")
df.to_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')
df.to_csv('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')

try:
    df.to_excel('d:/HocMayPrJ/data/app_reviews_cleaned.xlsx', index=False)
    df.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx', index=False)
    df.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_sach_tieng_viet.xlsx', index=False)
except Exception as e:
    print("Canh bao luu Excel (co the file dang mo):", e)

print("=== HOAN THANH XU LY DU LIEU CO SO ===")
