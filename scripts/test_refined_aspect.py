import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import pandas as pd
import time

t0 = time.time()
df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

# Precompile teencode patterns
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

# Build compiled regex for each aspect category
aspect_definitions = {
    'Van_chuyen_Giao_nhan': [
        'giao hàng', 'giao hang', 'giao đồ', 'giao do', 'giao hàng lâu', 'giao hàng chậm',
        'tiền ship', 'phí ship', 'giao trễ', 'giao nhanh', 'giao chậm', 'đơn hàng', 'don hang',
        'hủy đơn', 'huy don', 'bị hủy đơn', 'bom hàng', 'bom hang', 'tài xế', 'tai xe',
        'bác tài', 'bac tai', 'tài xế hủy', 'cuốc xe', 'cuoc xe', 'đặt xe', 'dat xe',
        'bắt xe', 'bat xe', 'chuyến xe', 'chuyen xe', 'chuyến đi', 'chuyen di', 'quán ăn',
        'quan an', 'đặt món', 'dat mon', 'giao món', 'nguội tanh', 'nguoi tanh', 'đổ vỡ',
        'do vo', 'hàng vỡ', 'hàng hỏng', 'kiện hàng', 'bưu tá', 'buu ta', 'vận chuyển',
        'van chuyen', 'lấy hàng', 'lay hang', 'trả hàng', 'tra hang', 'hoàn hàng', 'hoan hang',
        'giao nhầm', 'giao thiếu', 'đóng gói', 'dong goi', 'chờ tài xế', 'tìm tài xế', 'nhận đơn',
        'lấy món', 'giao cơm', 'giao nước', 'trà sữa', 'giao tận nơi', 'lâu tới', 'không nhận đơn',
        'ship', 'shipper', 'quán', 'đồ ăn', 'do an', 'món ăn', 'mon an', 'thức ăn', 'thuc an',
        'đặt giao', 'nhận hàng', 'giao đến', 'chở', 'tới rước', 'điểm đón', 'tài xế tới',
        'giao', 'đơn', 'hàng giao', 'cuốc'
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

# Precompile patterns for fast matching
compiled_patterns = {}
for asp, kws in aspect_definitions.items():
    # Sort keywords by length descending to match longest phrases first
    sorted_kws = sorted(kws, key=lambda x: len(x), reverse=True)
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in sorted_kws) + r')\b', re.IGNORECASE)
    compiled_patterns[asp] = pattern

def classify_fast(text, app_name):
    t = str(text)
    for p, r in teencode_pairs:
        t = p.sub(r, t)
        
    counts = {}
    for asp, pat in compiled_patterns.items():
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

df['refined_aspect'] = [classify_fast(r['content'], r['app_name']) for _, r in df.iterrows()]
print(f"Executed in {time.time() - t0:.2f} seconds!")

print("\n=== PHAN PHOI ASPECT MOI ===")
print(df['refined_aspect'].value_counts())

print("\n=== THEO TUNG UNG DUNG ===")
for app in df['app_name'].unique():
    print(f"\n[{app}]:")
    print(df[df['app_name'] == app]['refined_aspect'].value_counts())

row_72 = df[df['review_id'] == '14543589745']
print("\n=== ROW 72 TRONG ANH NGUOI DUNG ===")
print("Review ID:", row_72['review_id'].values[0])
print("App:", row_72['app_name'].values[0])
print("Rating:", row_72['rating'].values[0])
print("Content:", row_72['content'].values[0])
print("Cu: Hieu_nang_UI_UX -> Moi:", row_72['refined_aspect'].values[0])
