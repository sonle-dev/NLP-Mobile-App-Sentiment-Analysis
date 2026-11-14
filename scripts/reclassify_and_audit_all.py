import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import pandas as pd
from sklearn.model_selection import train_test_split

print("=== BAT DAU TOAN DIEN PHAN LOAI ASPECT & KIEM TOAN SENTIMENT ===")

# 1. Doc du lieu goc da lam sach
data_path = 'd:/HocMayPrJ/data/app_reviews_cleaned.csv'
df = pd.read_csv(data_path)
print(f"Tong so ban ghi: {len(df)}")

# 2. Tu dien teencode / chuan hoa tu ngu
teencode_pairs = [
    (re.compile(r'\bnguoij tanh\b', re.IGNORECASE), 'nguội tanh'),
    (re.compile(r'\bnguoi tanh\b', re.IGNORECASE), 'nguội tanh'),
    (re.compile(r'\bshiper\b', re.IGNORECASE), 'shipper'),
    (re.compile(r'\bsiper\b', re.IGNORECASE), 'shipper'),
    (re.compile(r'\btx\b', re.IGNORECASE), 'tài xế'),
    (re.compile(r'\bbác tài\b', re.IGNORECASE), 'tài xế'),
    (re.compile(r'\bđh\b', re.IGNORECASE), 'đơn hàng'),
    (re.compile(r'\bdh\b', re.IGNORECASE), 'đơn hàng'),
    (re.compile(r'\bnv\b', re.IGNORECASE), 'nhân viên'),
    (re.compile(r'\btk\b', re.IGNORECASE), 'tài khoản'),
    (re.compile(r'\bacc\b', re.IGNORECASE), 'tài khoản'),
    (re.compile(r'\bmk\b', re.IGNORECASE), 'mật khẩu'),
    (re.compile(r'\bpass\b', re.IGNORECASE), 'mật khẩu'),
    (re.compile(r'\bck\b', re.IGNORECASE), 'chuyển khoản'),
    (re.compile(r'\bstk\b', re.IGNORECASE), 'số tài khoản'),
    (re.compile(r'\bmgg\b', re.IGNORECASE), 'mã giảm giá'),
    (re.compile(r'\bkm\b', re.IGNORECASE), 'khuyến mãi'),
    (re.compile(r'\bvoucher\b', re.IGNORECASE), 'voucher')
]

# 3. 5 Nhom Aspect chuyen sau
aspect_definitions = {
    'Van_chuyen_Giao_nhan': [
        'giao hàng lâu', 'giao hàng chậm', 'giao trễ', 'giao nhanh', 'giao chậm',
        'giao hàng', 'giao hang', 'giao đồ', 'giao do', 'giao muộn', 'giao cơm', 'giao nước',
        'tiền ship', 'phí ship', 'đơn hàng', 'don hang', 'hủy đơn', 'huy don', 'bị hủy đơn',
        'bom hàng', 'bom hang', 'tài xế hủy', 'chờ tài xế', 'tìm tài xế', 'tài xế tới',
        'tài xế', 'tai xe', 'bác tài', 'bac tai', 'cuốc xe', 'cuoc xe', 'đặt xe', 'dat xe',
        'bắt xe', 'bat xe', 'chuyến xe', 'chuyen xe', 'chuyến đi', 'chuyen di', 'quán ăn',
        'quan an', 'đặt món', 'dat mon', 'giao món', 'nguội tanh', 'nguoi tanh', 'đổ vỡ',
        'hàng vỡ', 'hàng hỏng', 'kiện hàng', 'bưu tá', 'buu ta', 'vận chuyển', 'van chuyen',
        'lấy hàng', 'lay hang', 'trả hàng', 'tra hang', 'hoàn hàng', 'hoan hang', 'nhận hàng',
        'giao nhầm', 'giao thiếu', 'đóng gói', 'dong goi', 'nhận đơn', 'lấy món', 'trà sữa',
        'ship', 'shipper', 'quán', 'đồ ăn', 'do an', 'món ăn', 'mon an', 'thức ăn', 'thuc an',
        'đặt giao', 'giao đến', 'chở', 'tới rước', 'điểm đón', 'giao', 'đơn', 'hàng giao', 'cuốc'
    ],
    'Giao_dich_Thanh_toan_Gia_ca': [
        'chuyển tiền', 'chuyen tien', 'chuyển khoản', 'chuyen khoan', 'nạp tiền', 'nap tien',
        'rút tiền', 'rut tien', 'thanh toán', 'thanh toan', 'trừ tiền', 'tru tien', 'mất tiền',
        'mat tien', 'hoàn tiền', 'hoan tien', 'phí dịch vụ', 'phi dich vu', 'tăng giá',
        'cước phí', 'giá đắt', 'gia dat', 'đắt đỏ', 'dat do', 'mã giảm giá', 'ma giam gia',
        'mã giảm', 'shopee xu', 'hoàn xu', 'điểm thưởng', 'số tài khoản', 'thẻ atm', 'nuốt thẻ',
        'quét qr', 'quet qr', 'qr code', 'ví điện tử', 'napas', 'liên ngân hàng', 'thu phí',
        'trừ phí', 'nuốt tiền', 'tiền gửi', 'biến động số dư', 'bắn tiền', 'chuyển nhanh', 'tiền nong',
        'voucher', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'uu dai', 'xu', 'tiền', 'phí', 'giá',
        'cước', 'stk', 'atm', 'lãi suất', 'hoàn trả', 'hoàn tiền', 'thẻ tín dụng'
    ],
    'Bao_mat_Va_Tai_khoan': [
        'đăng nhập', 'dang nhap', 'login', 'mật khẩu', 'mat khau', 'quên mật khẩu', 'đổi mật khẩu',
        'mã otp', 'smart otp', 'sinh trắc học', 'sinh trac hoc', 'vneid', 'căn cước', 'can cuoc',
        'cccd', 'khuôn mặt', 'khuon mat', 'face id', 'faceid', 'vân tay', 'van tay', 'khóa tài khoản',
        'khoa tai khoan', 'khóa nick', 'khoa nick', 'khóa app', 'bị khóa', 'bi khoa', 'bảo mật',
        'bao mat', 'lừa đảo', 'lua dao', 'chiếm đoạt', 'xác thực', 'xac thuc', 'định danh', 'dinh danh',
        'ekyc', 'mất tài khoản', 'mất nick', 'bị hack', 'hack nick', 'lấy lại tài khoản', 'vô hiệu hóa',
        'quên pass', 'khóa vĩnh viễn', 'xác minh danh tính', 'mật mã', 'tài khoản', 'tai khoan',
        'nick', 'pass', 'password', 'hack'
    ],
    'Dich_vu_Va_CSKH': [
        'tổng đài', 'tong dai', 'hotline', 'chăm sóc khách hàng', 'cskh', 'thái độ nhân viên',
        'chi nhánh', 'chi nhanh', 'phòng giao dịch', 'pgd', 'giải quyết khiếu nại', 'khiếu nại',
        'khieu nai', 'phản hồi', 'phan hoi', 'tư vấn viên', 'chăm sóc khách', 'nhân viên hỗ trợ',
        'liên hệ tổng đài', 'thái độ tệ', 'không ai giải quyết', 'nhân viên cskh', 'nhân viên',
        'nhan vien', 'hỗ trợ', 'ho tro', 'support', 'phục vụ', 'phuc vu', 'thái độ', 'tư vấn'
    ],
    'Hieu_nang_Va_Loi_App': [
        'văng app', 'vang app', 'văng ra', 'treo máy', 'đơ máy', 'đen màn hình', 'trắng màn hình',
        'không vào được', 'khong vao duoc', 'không mở được', 'khong mo duoc', 'mở không lên',
        'lỗi ứng dụng', 'lỗi app', 'loi app', 'nóng máy', 'nong may', 'hao pin', 'tốn pin',
        'cập nhật lỗi', 'cap nhat loi', 'bản cập nhật tệ', 'load video', 'mạng yếu', 'kết nối thất bại',
        'app rác', 'như rác', 'nhu rac', 'xóa app', 'xoa app', 'gỡ cài đặt', 'go cai dat',
        'lag', 'giật', 'giat', 'đơ', 'văng', 'vang', 'treo', 'chậm', 'cham', 'load', 'tải lâu',
        'cập nhật', 'cap nhat', 'update', 'phiên bản', 'giao diện', 'mượt', 'mượt mà', 'dễ dùng',
        'khó dùng', 'rối mắt', 'nâng cấp', 'tối ưu', 'nặng máy', 'bug', 'crash', 'lỗi', 'loi'
    ]
}

compiled_aspects = {}
for asp, kws in aspect_definitions.items():
    sorted_kws = sorted(kws, key=lambda x: len(x), reverse=True)
    pat = re.compile(r'\b(' + '|'.join(re.escape(k) for k in sorted_kws) + r')\b', re.IGNORECASE)
    compiled_aspects[asp] = pat

def classify_aspect(text, app_name):
    t = str(text)
    for p, r in teencode_pairs:
        t = p.sub(r, t)
        
    counts = {}
    for asp, pat in compiled_aspects.items():
        matches = pat.findall(t)
        counts[asp] = len(matches)
        
    # App-specific weighting
    if app_name in ['ShopeeFood', 'Grab', 'Shopee']:
        counts['Van_chuyen_Giao_nhan'] = int(counts['Van_chuyen_Giao_nhan'] * 1.5)
    elif app_name in ['Agribank', 'MB Bank', 'MoMo', 'ZaloPay']:
        counts['Giao_dich_Thanh_toan_Gia_ca'] = int(counts['Giao_dich_Thanh_toan_Gia_ca'] * 1.5)
        
    max_c = max(counts.values())
    if max_c > 0:
        for asp, c in counts.items():
            if c == max_c:
                return asp
    return 'Hieu_nang_Va_Loi_App'

# 4. Kiem toan nhan Sentiment (1, 2, 3 sao = Tieu cuc; 4, 5 sao = Tich cuc + Loc nghich nhan)
strong_negative_kws = [
    'lừa đảo', 'lua dao', 'quá tệ', 'qua te', 'như rác', 'nhu rac', 'bực mình', 'buc minh',
    'bực bội', 'buc boi', 'tồi tệ', 'toi te', 'rác rưởi', 'rac ruoi', 'thất vọng', 'that vong',
    'chán nản', 'chan nan', 'vứt đi', 'vut di', 'tẩy chay', 'tay chay', 'khốn nạn', 'chó chết',
    'ăn cướp', 'an cuop', 'mất dạy', 'mat day', 'chết tiệt', 'chet tiet', 'lỗi tùm lum', 'loi tum lum',
    'không dùng được', 'khong dung duoc', 'không vào được', 'khong vao duoc', 'lỗi liên tục', 'loi lien tuc',
    'lừa đảo trắng trợn', 'app lừa', 'trừ tiền vô lý', 'bị trừ tiền mà không nhận', 'quá chán', 'như hạch'
]

strong_positive_kws = [
    'rất tuyệt vời', 'rat tuyet voi', 'quá tuyệt vời', 'qua tuyet voi', 'quá tốt', 'qua tot',
    'cực kỳ hài lòng', 'cuc ky hai long', 'rất mượt mà', 'rat muot ma', 'xuất sắc', 'xuat sac',
    'trên cả tuyệt vời', 'dịch vụ tuyệt vời', 'ưng ý', 'ung y', '10 điểm', '10 diem', '5 sao tuyệt đối',
    'rất tiện lợi', 'rat tien loi', 'yêu thích ứng dụng', 'cảm ơn agribank', 'cảm ơn ngân hàng',
    'dùng rất thích', 'dung rat thich', 'quá đỉnh', 'qua dinh', 'tiện ích tuyệt vời', 'rất ưng ý'
]

def audit_sentiment(rating, text):
    t_lower = str(text).lower()
    r = int(rating)
    has_neg = any(kw in t_lower for kw in strong_negative_kws)
    has_pos = any(kw in t_lower for kw in strong_positive_kws)
    
    # 4, 5 sao nhung chui nang
    if r in [4, 5] and has_neg and not has_pos:
        return 0, 'Tieu cuc', 'Nghich_nhan_5sao_che'
        
    # 1, 2, 3 sao nhung khen tuyet doi
    if r in [1, 2, 3] and has_pos and not any(k in t_lower for k in ['không', 'khong', 'chưa', 'chua', 'lỗi', 'loi', 'tệ', 'te', 'nhưng', 'nhung']):
        return 1, 'Tich cuc', 'Nghich_nhan_1sao_khen'
        
    if r in [1, 2, 3]:
        return 0, 'Tieu cuc', 'Chuan_1_3_sao'
    else:
        return 1, 'Tich cuc', 'Chuan_4_5_sao'

# 5. Thuc thi gan nhan
print("Dang thuc hien gan nhan toan bo 14.910 dong...")
new_aspects = []
new_sentiments = []
new_labels = []
new_audit_types = []

for idx, row in df.iterrows():
    asp = classify_aspect(row['content'], row['app_name'])
    lbl, sent, atype = audit_sentiment(row['rating'], row['content'])
    new_aspects.append(asp)
    new_sentiments.append(sent)
    new_labels.append(lbl)
    new_audit_types.append(atype)

df['aspect_category'] = new_aspects
df['sentiment'] = new_sentiments
df['label'] = new_labels
df['label_audit_type'] = new_audit_types

print("\n=== THONG KE PHAN PHOI ASPECT MOI ===")
print(df['aspect_category'].value_counts())

print("\n=== THONG KE PHAN PHOI SENTIMENT MOI ===")
print(df['sentiment'].value_counts())

print("\n=== THONG KE LOAI KIEM TOAN NHAN ===")
print(df['label_audit_type'].value_counts())

# Kiem tra rieng Row 72
row_72 = df[df['review_id'] == '14543589745']
print("\n=== KIEM TRA ROW 72 (ShopeeFood Giao hang lau...) ===")
print("Review ID:", row_72['review_id'].values[0])
print("App:", row_72['app_name'].values[0])
print("Rating:", row_72['rating'].values[0])
print("Content:", row_72['content'].values[0])
print("Aspect:", row_72['aspect_category'].values[0])
print("Sentiment:", row_72['sentiment'].values[0])
print("Label:", row_72['label'].values[0])

# 6. Luu tap du lieu sach moi
print("\nDang luu du lieu sach cap nhat...")
df.to_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')
df.to_csv('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')

try:
    df.to_excel('d:/HocMayPrJ/data/app_reviews_cleaned.xlsx', index=False)
    print("Da luu data/app_reviews_cleaned.xlsx")
except Exception as e:
    print("Warning Excel data:", e)

try:
    df.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx', index=False)
    print("Da luu Nhom_12/app_reviews_cleaned.xlsx")
except Exception as e:
    print("Warning Excel Nhom_12:", e)

# 7. Chia lai tap Train / Val / Test (70 / 15 / 15) phan tang theo label
print("\nDang phan chia Stratified Split 70 / 15 / 15...")
train_df, temp_df = train_test_split(df, test_size=0.30, random_state=42, stratify=df['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42, stratify=temp_df['label'])

print(f"Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")

# Luu tap train / val / test
for name, dset in [('train', train_df), ('val', val_df), ('test', test_df)]:
    dset.to_csv(f'd:/HocMayPrJ/data/{name}.csv', index=False, encoding='utf-8-sig')
    dset.to_csv(f'd:/HocMayPrJ/Nhom_12/{name}.csv', index=False, encoding='utf-8-sig')
    try:
        dset.to_excel(f'd:/HocMayPrJ/data/{name}.xlsx', index=False)
        dset.to_excel(f'd:/HocMayPrJ/Nhom_12/{name}.xlsx', index=False)
    except Exception as e:
        print(f"Warning Excel {name}:", e)

print("HOAN THANH CAP NHAT DU LIEU TOAN HE THONG!")
