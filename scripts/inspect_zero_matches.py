import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

aspect_rules = {
    'Van_chuyen_Giao_nhan': [
        'giao hàng', 'giao hang', 'ship', 'shipper', 'tiền ship', 'phí ship', 'đơn hàng', 
        'tài xế', 'bác tài', 'cuốc xe', 'đặt xe', 'đồ ăn', 'món ăn', 'quán ăn', 'quán', 
        'đặt món', 'nguội', 'vận chuyển', 'lấy hàng', 'trả hàng', 'hoàn hàng', 'nhận hàng'
    ],
    'Giao_dich_Thanh_toan_Gia_ca': [
        'chuyển tiền', 'chuyển khoản', 'ck', 'nạp tiền', 'rút tiền', 'thanh toán', 
        'trừ tiền', 'mất tiền', 'hoàn tiền', 'voucher', 'mã giảm giá', 'xu', 'stk', 
        'quét qr', 'ví điện tử'
    ],
    'Bao_mat_Va_Tai_khoan': [
        'đăng nhập', 'mật khẩu', 'pass', 'otp', 'sinh trắc học', 'cccd', 'khuôn mặt', 
        'face id', 'vân tay', 'khóa tài khoản', 'khóa nick', 'lừa đảo', 'xác thực'
    ],
    'Dich_vu_Va_CSKH': [
        'tổng đài', 'hotline', 'nhân viên', 'cskh', 'hỗ trợ', 'support', 'phục vụ', 
        'thái độ', 'chi nhánh', 'khiếu nại'
    ],
    'Hieu_nang_Va_Loi_App': [
        'lag', 'giật', 'đơ', 'văng', 'treo', 'chậm', 'load', 'cập nhật', 'update', 
        'giao diện', 'mượt', 'dễ dùng', 'lỗi app', 'bug', 'crash', 'không vào được'
    ]
}

def get_zero_match(text):
    text_l = str(text).lower()
    for asp, kws in aspect_rules.items():
        if any(kw in text_l for kw in kws):
            return False
    return True

zeros = df[df['content'].apply(get_zero_match)]
print(f"Total zero matches: {len(zeros)} / {len(df)}")
print("\nSample 25 zero matches:")
for i, r in zeros.head(25).iterrows():
    print(f"- [{r['app_name']} | {r['rating']}*]: {r['content']}")
