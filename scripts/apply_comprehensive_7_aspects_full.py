import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import pandas as pd
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from sklearn.model_selection import train_test_split

print("=== BAT DAU NANG CAP TOAN BO DU LIEU SANG HE THONG 7 ASPECT TOAN DIEN ===")

data_path = 'd:/HocMayPrJ/data/app_reviews_cleaned.csv'
df = pd.read_csv(data_path)
print(f"Tong so mau: {len(df)}")

teencode_pairs = [
    (re.compile(r'\bnguoij tanh\b', re.IGNORECASE), 'nguội tanh'),
    (re.compile(r'\bnguoi tanh\b', re.IGNORECASE), 'nguội tanh'),
    (re.compile(r'\bshiper\b', re.IGNORECASE), 'shipper'),
    (re.compile(r'\bsiper\b', re.IGNORECASE), 'shipper'),
    (re.compile(r'\bship\b', re.IGNORECASE), 'ship'),
    (re.compile(r'\btx\b', re.IGNORECASE), 'tài xế'),
    (re.compile(r'\bbác tài\b', re.IGNORECASE), 'tài xế'),
    (re.compile(r'\bđh\b', re.IGNORECASE), 'đơn hàng'),
    (re.compile(r'\bdh\b', re.IGNORECASE), 'đơn hàng'),
    (re.compile(r'\bnv\b', re.IGNORECASE), 'nhân viên'),
    (re.compile(r'\bck\b', re.IGNORECASE), 'chuyển khoản'),
    (re.compile(r'\bstk\b', re.IGNORECASE), 'số tài khoản'),
    (re.compile(r'\bmgg\b', re.IGNORECASE), 'mã giảm giá'),
    (re.compile(r'\bkm\b', re.IGNORECASE), 'khuyến mãi'),
    (re.compile(r'\bvoucher\b', re.IGNORECASE), 'voucher'),
    (re.compile(r'\bqc\b', re.IGNORECASE), 'quảng cáo')
]

# 1. Bao mat, Tai khoan & Chinh sach kiem duyet
patterns_bao_mat = [
    r'\bsinh trắc\b', r'\bsinh trắc học\b', r'\bsth\b', r'\bnfc\b', r'\bquét nfc\b',
    r'\bcccd\b', r'\bquét cccd\b', r'\bvneid\b', r'\bcăn cước\b', r'\bkhuôn mặt\b',
    r'\bface id\b', r'\bfaceid\b', r'\bvân tay\b', r'\bđăng nhập\b', r'\bdang nhap\b',
    r'\blogin\b', r'\bmật khẩu\b', r'\bmat khau\b', r'\bquên mật khẩu\b', r'\bđổi mật khẩu\b',
    r'\bquên pass\b', r'\botp\b', r'\bmã otp\b', r'\bsmart otp\b', r'\bsoft otp\b',
    r'\bxác thực\b', r'\bđịnh danh\b', r'\bekyc\b', r'\bkhóa tài khoản\b', r'\bkhóa nick\b',
    r'\bkhóa app\b', r'\bbị khóa\b', r'\bmất tài khoản\b', r'\bmất nick\b', r'\bbị hack\b',
    r'\bhack nick\b', r'\blấy lại tài khoản\b', r'\bvô hiệu hóa\b', r'\blừa đảo\b',
    r'\bchiếm đoạt\b', r'\bbảo mật\b', r'\bcảnh cáo\b', r'\bcảnh báo\b', r'\bvi phạm\b',
    r'\btiêu chuẩn cộng đồng\b', r'\bcấm đăng\b', r'\bkhóa đăng\b', r'\bđăng ký\b',
    r'\btên mail\b', r'\bemail không hợp lệ\b', r'\bmail ko hợp lệ\b'
]

# 2. Giao dich, Thanh toan, Vi tien & Uu dai
patterns_giao_dich = [
    r'\bchuyển tiền\b', r'\bchuyen tien\b', r'\bchuyển khoản\b', r'\bchuyen khoan\b',
    r'\bnạp tiền\b', r'\bnap tien\b', r'\brút tiền\b', r'\brut tien\b', r'\bthanh toán\b',
    r'\bthanh toan\b', r'\bhoá đơn\b', r'\bhóa đơn\b', r'\btrừ tiền\b', r'\btru tien\b',
    r'\bmất tiền\b', r'\bmat tien\b', r'\bhoàn tiền\b', r'\bhoan tien\b', r'\bphí dịch vụ\b',
    r'\btính phí\b', r'\bthu phí\b', r'\btrừ phí\b', r'\bphí thường niên\b', r'\bphí duy trì\b',
    r'\bphí chuyển\b', r'\btăng giá\b', r'\bcước phí\b', r'\bgiá đắt\b', r'\bđắt đỏ\b',
    r'\bbào tiền\b', r'\bbào tiền khách\b', r'\bkhuyến mãi\b', r'\bvoucher\b', r'\bmã giảm giá\b',
    r'\bshopee xu\b', r'\bhoàn xu\b', r'\bđiểm thưởng\b', r'\bsố tài khoản\b', r'\bstk\b',
    r'\bthẻ atm\b', r'\bnuốt thẻ\b', r'\bquét qr\b', r'\bqr code\b', r'\bví điện tử\b',
    r'\bnapas\b', r'\bliên ngân hàng\b', r'\blãi suất\b', r'\bbiến động số dư\b', r'\bsố dư\b',
    r'\bnuốt tiền\b', r'\btiền gửi\b', r'\bbắn tiền\b', r'\bchuyển nhanh\b', r'\btiền trong ví\b',
    r'\blỗi chuyển tiền\b', r'\blỗi chuyển khoản\b', r'\blỗi nạp tiền\b', r'\blỗi thanh toán\b',
    r'\btrùm deal\b', r'\bmua deal\b'
]

# 3. Van chuyen, Giao nhan, Dat xe & Do an
patterns_van_chuyen = [
    r'\bgiao hàng\b', r'\bgiao hang\b', r'\bshipper\b', r'\bshiper\b', r'\bsiper\b',
    r'\bship\b', r'\btiền ship\b', r'\bphí ship\b', r'\bgiao đồ\b', r'\bgiao do\b',
    r'\bgiao lâu\b', r'\bgiao chậm\b', r'\bgiao trễ\b', r'\bgiao nhanh\b', r'\bgiao muộn\b',
    r'\bgiao món\b', r'\bgiao cơm\b', r'\bgiao nước\b', r'\bđơn hàng\b', r'\bdon hang\b',
    r'\bhủy đơn\b', r'\bhuy don\b', r'\bbom hàng\b', r'\bbom hang\b', r'\btài xế\b',
    r'\btai xe\b', r'\bbác tài\b', r'\bbac tai\b', r'\bcuốc xe\b', r'\bcuoc xe\b',
    r'\bđặt xe\b', r'\bdat xe\b', r'\bbắt xe\b', r'\bchuyến xe\b', r'\bchuyến đi\b',
    r'\bquán ăn\b', r'\bđặt món\b', r'\bnguội tanh\b', r'\bnguoij tanh\b', r'\bđồ ăn\b',
    r'\bmón ăn\b', r'\bthức ăn\b', r'\bđổ vỡ\b', r'\bhàng vỡ\b', r'\bhàng hỏng\b',
    r'\bkiện hàng\b', r'\bbưu tá\b', r'\bvận chuyển\b', r'\blấy hàng\b', r'\btrả hàng\b',
    r'\bhoàn hàng\b', r'\bnhận hàng\b', r'\bgiao nhầm\b', r'\bgiao thiếu\b', r'\bđóng gói\b',
    r'\bnhận đơn\b', r'\blấy món\b', r'\btrà sữa\b', r'\bchở khách\b', r'\bđiểm đón\b',
    r'\btới đón\b', r'\bchờ tài xế\b', r'\btìm tài xế\b', r'\btài xế hủy\b', r'\blấy đồ ăn\b',
    r'\bkhông có xe\b', r'\bko có xe\b', r'\bkhông có xe nào\b', r'\bko có xe nào\b',
    r'\bđơn vận chuyển\b', r'\bđơn ghép\b', r'\bchậm đơn\b'
]

# 4. Dich vu khach hang, Hotline & Telesale
patterns_cskh = [
    r'\btổng đài\b', r'\btong dai\b', r'\bhotline\b', r'\bnhân viên\b', r'\bnhan vien\b',
    r'\bcskh\b', r'\bchăm sóc khách hàng\b', r'\bthái độ nhân viên\b', r'\bchi nhánh\b',
    r'\bphòng giao dịch\b', r'\bpgd\b', r'\bgiải quyết khiếu nại\b', r'\bkhiếu nại\b',
    r'\bkhieu nai\b', r'\bphản hồi\b', r'\btư vấn viên\b', r'\bchăm sóc khách\b',
    r'\bnhân viên hỗ trợ\b', r'\bliên hệ tổng đài\b', r'\bthái độ phục vụ\b', r'\bhỗ trợ khách hàng\b',
    r'\bgọi điện\b', r'\bgọi đòi nợ\b', r'\bnhắc nợ\b', r'\bgọi làm phiền\b', r'\bgọi lên đến\b',
    r'\bgọi trc\b', r'\bgọi trước\b', r'\bchưa đến hạn tt mà gọi\b'
]

# 5. Quang cao, Popup & Thong bao lam phien
patterns_quang_cao = [
    r'\bquảng cáo\b', r'\bquang cao\b', r'\bquản cáo\b', r'\bnhiều quảng cáo\b', r'\bchèn quảng cáo\b',
    r'\bthông báo rác\b', r'\bthông báo nhiều\b', r'\bpopup\b', r'\bpop up\b',
    r'\bbắt đánh giá\b', r'\bbắt chấm điểm\b', r'\bđòi đánh giá\b', r'\bask for rating\b',
    r'\basking for rating\b', r'\basking for ratings\b', r'\bstop asking\b', r'\bgây phiền toái\b'
]

# 6. Hieu nang, Loi ky thuat & Giao dien UI/UX
patterns_hieu_nang = [
    r'\bvăng app\b', r'\bvăng ra\b', r'\btreo máy\b', r'\bđơ máy\b', r'\bđen màn hình\b',
    r'\btrắng màn hình\b', r'\bkhông vào được\b', r'\bkhong vao duoc\b', r'\bkhông mở được\b',
    r'\bmở không lên\b', r'\blỗi ứng dụng\b', r'\blỗi app\b', r'\bloi app\b', r'\bnóng máy\b',
    r'\bhao pin\b', r'\btốn pin\b', r'\bcập nhật lỗi\b', r'\bbản cập nhật tệ\b', r'\bload video\b',
    r'\bmạng yếu\b', r'\bkết nối thất bại\b', r'\bapp rác\b', r'\bxóa app\b', r'\bgỡ cài đặt\b',
    r'\blag\b', r'\bgiật\b', r'\bđơ\b', r'\bvăng\b', r'\btreo\b', r'\bchậm\b', r'\bload lâu\b',
    r'\btải lâu\b', r'\bcập nhật\b', r'\bupdate\b', r'\bphiên bản\b', r'\bgiao diện\b',
    r'\bbug\b', r'\bcrash\b', r'\bmàu đỏ làm nền\b', r'\bmàu xanh xấu\b', r'\bđổi màu nền\b',
    r'\bgiao diện xấu\b'
]

compiled_aspects = {
    'Bao_mat_Va_Xac_thuc': re.compile('|'.join(patterns_bao_mat), re.IGNORECASE),
    'Giao_dich_Thanh_toan': re.compile('|'.join(patterns_giao_dich), re.IGNORECASE),
    'Van_chuyen_Va_Dat_xe': re.compile('|'.join(patterns_van_chuyen), re.IGNORECASE),
    'Dich_vu_Va_CSKH': re.compile('|'.join(patterns_cskh), re.IGNORECASE),
    'Quang_cao_Va_Thong_bao': re.compile('|'.join(patterns_quang_cao), re.IGNORECASE),
    'Hieu_nang_Va_Loi_Ky_thuat': re.compile('|'.join(patterns_hieu_nang), re.IGNORECASE)
}

def classify_7_aspects(text, app_name):
    t = str(text)
    for p, r in teencode_pairs:
        t = p.sub(r, t)
        
    counts = {}
    for asp, pat in compiled_aspects.items():
        matches = pat.findall(t)
        counts[asp] = len(matches)
        
    # Uu tien nghiep vu dac thu
    priority_groups = ['Bao_mat_Va_Xac_thuc', 'Giao_dich_Thanh_toan', 'Van_chuyen_Va_Dat_xe', 'Dich_vu_Va_CSKH', 'Quang_cao_Va_Thong_bao']
    active_priorities = [a for a in priority_groups if counts[a] > 0]
    
    if active_priorities:
        max_priority_count = max(counts[a] for a in active_priorities)
        top_candidates = [a for a in active_priorities if counts[a] == max_priority_count]
        
        # Logic chuyen biet theo app
        if app_name in ['Grab', 'ShopeeFood'] and 'Van_chuyen_Va_Dat_xe' in top_candidates:
            return 'Van_chuyen_Va_Dat_xe'
        if app_name in ['Agribank', 'MB Bank', 'MoMo', 'ZaloPay']:
            if 'Giao_dich_Thanh_toan' in top_candidates and counts['Van_chuyen_Va_Dat_xe'] == 0:
                return 'Giao_dich_Thanh_toan'
            if 'Bao_mat_Va_Xac_thuc' in top_candidates:
                return 'Bao_mat_Va_Xac_thuc'
        return top_candidates[0]

    # Loi ky thuat thuan tuy
    if counts['Hieu_nang_Va_Loi_Ky_thuat'] > 0:
        return 'Hieu_nang_Va_Loi_Ky_thuat'
        
    # Trai nghiem tong the (Khen / Che chung / Meme / Fandom)
    return 'Trai_nghiem_Tong_the'

# Gan nhan 7 Aspect
print("Dang thuc hien gan nhan toan bo 14.910 mau...")
df['aspect_category'] = [classify_7_aspects(r['content'], r['app_name']) for _, r in df.iterrows()]

print("\n=== KET QUA PHAN BO 7 KHIA CANH MOI ===")
print(df['aspect_category'].value_counts())

# Luu file csv
df.to_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')
df.to_csv('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')

# Phân chia phân tầng 70 / 15 / 15
print("\nDang phan chia Stratified Split 70 / 15 / 15...")
train_df, temp_df = train_test_split(df, test_size=0.30, random_state=42, stratify=df['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42, stratify=temp_df['label'])

for base in ['d:/HocMayPrJ/data', 'd:/HocMayPrJ/Nhom_12']:
    train_df.to_csv(f'{base}/train.csv', index=False, encoding='utf-8-sig')
    val_df.to_csv(f'{base}/val.csv', index=False, encoding='utf-8-sig')
    test_df.to_csv(f'{base}/test.csv', index=False, encoding='utf-8-sig')

try:
    df.to_excel('d:/HocMayPrJ/data/app_reviews_cleaned.xlsx', index=False)
    train_df.to_excel('d:/HocMayPrJ/data/train.xlsx', index=False)
    val_df.to_excel('d:/HocMayPrJ/data/val.xlsx', index=False)
    test_df.to_excel('d:/HocMayPrJ/data/test.xlsx', index=False)
    df.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx', index=False)
    val_df.to_excel('d:/HocMayPrJ/Nhom_12/val.xlsx', index=False)
    test_df.to_excel('d:/HocMayPrJ/Nhom_12/test.xlsx', index=False)
    train_df.to_excel('d:/HocMayPrJ/Nhom_12/train.xlsx', index=False)
    print("Da luu toan bo file Excel!")
except Exception as e:
    print("Ghi chu file Excel (neu co file dang mo):", e)

print("=== HOAN TAT DONG BO DU LIEU 7 ASPECT ===")
