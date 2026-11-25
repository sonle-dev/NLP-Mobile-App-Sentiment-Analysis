import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

# Test regex without false positive triggers (avoid ngan hang, giao dien, don gian, xem)
van_chuyen_patterns = [
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
    r'\btới đón\b', r'\bchờ tài xế\b', r'\btìm tài xế\b', r'\btài xế hủy\b', r'\blấy đồ ăn\b'
]

bao_mat_patterns = [
    r'\bsinh trắc\b', r'\bsinh trắc học\b', r'\bsth\b', r'\bnfc\b', r'\bquét nfc\b',
    r'\bcccd\b', r'\bvneid\b', r'\bcăn cước\b', r'\bkhuôn mặt\b', r'\bface id\b', r'\bfaceid\b',
    r'\bvân tay\b', r'\bđăng nhập\b', r'\bdang nhap\b', r'\blogin\b', r'\bmật khẩu\b',
    r'\bmat khau\b', r'\bpass\b', r'\bpassword\b', r'\bquên mật khẩu\b', r'\bđổi mật khẩu\b',
    r'\botp\b', r'\bmã otp\b', r'\bsmart otp\b', r'\bsoft otp\b', r'\bxác thực\b',
    r'\bđịnh danh\b', r'\bekyc\b', r'\bkhóa tài khoản\b', r'\bkhóa nick\b', r'\bkhóa app\b',
    r'\bbị khóa\b', r'\bmất tài khoản\b', r'\bmất nick\b', r'\bbị hack\b', r'\bhack nick\b',
    r'\blấy lại tài khoản\b', r'\bvô hiệu hóa\b', r'\blừa đảo\b', r'\bchiếm đoạt\b', r'\bbảo mật\b'
]

giao_dich_patterns = [
    r'\bchuyển tiền\b', r'\bchuyen tien\b', r'\bchuyển khoản\b', r'\bchuyen khoan\b',
    r'\bnạp tiền\b', r'\bnap tien\b', r'\brút tiền\b', r'\brut tien\b', r'\bthanh toán\b',
    r'\bthanh toan\b', r'\bhoá đơn\b', r'\btrừ tiền\b', r'\btru tien\b', r'\bmất tiền\b',
    r'\bmat tien\b', r'\bhoàn tiền\b', r'\bhoan tien\b', r'\bphí dịch vụ\b', r'\btính phí\b',
    r'\bthu phí\b', r'\btrừ phí\b', r'\bphí thường niên\b', r'\bphí duy trì\b', r'\bphí chuyển\b',
    r'\btăng giá\b', r'\bcước phí\b', r'\bgiá đắt\b', r'\bđắt đỏ\b', r'\bkhuyến mãi\b',
    r'\bvoucher\b', r'\bmã giảm giá\b', r'\bshopee xu\b', r'\bhoàn xu\b', r'\bđiểm thưởng\b',
    r'\bsố tài khoản\b', r'\bstk\b', r'\bthẻ atm\b', r'\bnuốt thẻ\b', r'\bquét qr\b',
    r'\bqr code\b', r'\bví điện tử\b', r'\bnapas\b', r'\bliên ngân hàng\b', r'\blãi suất\b',
    r'\bbiến động số dư\b', r'\bsố dư\b', r'\bnuốt tiền\b', r'\btiền gửi\b', r'\bbắn tiền\b',
    r'\bchuyển nhanh\b'
]

cskh_patterns = [
    r'\btổng đài\b', r'\btong dai\b', r'\bhotline\b', r'\bnhân viên\b', r'\bnhan vien\b',
    r'\bcskh\b', r'\bchăm sóc khách hàng\b', r'\bthái độ nhân viên\b', r'\bchi nhánh\b',
    r'\bphòng giao dịch\b', r'\bpgd\b', r'\bgiải quyết khiếu nại\b', r'\bkhiếu nại\b',
    r'\bkhieu nai\b', r'\bphản hồi\b', r'\btư vấn viên\b', r'\bchăm sóc khách\b',
    r'\bnhân viên hỗ trợ\b', r'\bliên hệ tổng đài\b', r'\bthái độ phục vụ\b', r'\bhỗ trợ khách hàng\b'
]

hieu_nang_patterns = [
    r'\bvăng app\b', r'\bvăng ra\b', r'\btreo máy\b', r'\bđơ máy\b', r'\bđen màn hình\b',
    r'\btrắng màn hình\b', r'\bkhông vào được\b', r'\bkhong vao duoc\b', r'\bkhông mở được\b',
    r'\bmở không lên\b', r'\blỗi ứng dụng\b', r'\blỗi app\b', r'\bloi app\b', r'\bnóng máy\b',
    r'\bhao pin\b', r'\btốn pin\b', r'\bcập nhật lỗi\b', r'\bbản cập nhật tệ\b', r'\bload video\b',
    r'\bmạng yếu\b', r'\bkết nối thất bại\b', r'\bapp rác\b', r'\bnhư rác\b', r'\bxóa app\b',
    r'\bgỡ cài đặt\b', r'\blag\b', r'\bgiật\b', r'\bđơ\b', r'\bvăng\b', r'\btreo\b',
    r'\bchậm\b', r'\bload lâu\b', r'\btải lâu\b', r'\bcập nhật\b', r'\bupdate\b',
    r'\bphiên bản\b', r'\bgiao diện\b', r'\bmượt\b', r'\bmượt mà\b', r'\bdễ dùng\b',
    r'\bkhó dùng\b', r'\brối mắt\b', r'\bnâng cấp\b', r'\btối ưu\b', r'\bnặng máy\b',
    r'\bbug\b', r'\bcrash\b'
]

compiled = {
    'Van_chuyen_Giao_nhan': re.compile('|'.join(van_chuyen_patterns), re.IGNORECASE),
    'Bao_mat_Va_Tai_khoan': re.compile('|'.join(bao_mat_patterns), re.IGNORECASE),
    'Giao_dich_Thanh_toan_Gia_ca': re.compile('|'.join(giao_dich_patterns), re.IGNORECASE),
    'Dich_vu_Va_CSKH': re.compile('|'.join(cskh_patterns), re.IGNORECASE),
    'Hieu_nang_Va_Loi_App': re.compile('|'.join(hieu_nang_patterns), re.IGNORECASE)
}

# Test priority classification
def classify_refined(text, app_name):
    t = str(text)
    scores = {}
    for asp, pat in compiled.items():
        matches = pat.findall(t)
        scores[asp] = len(matches)
        
    # Domain prior
    if app_name in ['ShopeeFood', 'Grab', 'Shopee']:
        scores['Van_chuyen_Giao_nhan'] *= 2
    elif app_name in ['Agribank', 'MB Bank', 'MoMo', 'ZaloPay']:
        scores['Giao_dich_Thanh_toan_Gia_ca'] *= 2
        scores['Bao_mat_Va_Tai_khoan'] *= 2
        
    # If tie between business operational aspects and Hieu_nang, prioritize business operational aspect
    max_score = max(scores.values())
    if max_score > 0:
        candidates = [asp for asp, s in scores.items() if s == max_score]
        # Prefer specific business domain over general performance
        for preferred in ['Van_chuyen_Giao_nhan', 'Bao_mat_Va_Tai_khoan', 'Giao_dich_Thanh_toan_Gia_ca', 'Dich_vu_Va_CSKH']:
            if preferred in candidates:
                return preferred
        return candidates[0]
        
    return 'Hieu_nang_Va_Loi_App'

df['aspect_v2'] = [classify_refined(r['content'], r['app_name']) for _, r in df.iterrows()]
print("=== PHAN BO ASPECT V2 SAU KHI TRIET TIEU FALSE POSITIVES ===")
print(df['aspect_v2'].value_counts())

print("\n=== THEO TUNG UNG DUNG (V2) ===")
for app in df['app_name'].unique():
    print(f"\n[{app}]:")
    print(df[df['app_name'] == app]['aspect_v2'].value_counts())
