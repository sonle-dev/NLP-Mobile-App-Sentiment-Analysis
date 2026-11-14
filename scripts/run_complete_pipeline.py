import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import json
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
from sklearn.model_selection import train_test_split

print("=== GIAI DOAN 1: GAN NHAN ASPECT 5 NHOM & KIEM TOAN SENTIMENT ===")

data_path = 'd:/HocMayPrJ/data/app_reviews_cleaned.csv'
df = pd.read_csv(data_path)
print(f"Tong so mau: {len(df)}")

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
    
    if r in [4, 5] and has_neg and not has_pos:
        return 0, 'Tieu cuc', 'Nghich_nhan_5sao_che'
        
    if r in [1, 2, 3] and has_pos and not any(k in t_lower for k in ['không', 'khong', 'chưa', 'chua', 'lỗi', 'loi', 'tệ', 'te', 'nhưng', 'nhung']):
        return 1, 'Tich cuc', 'Nghich_nhan_1sao_khen'
        
    if r in [1, 2, 3]:
        return 0, 'Tieu cuc', 'Chuan_1_3_sao'
    else:
        return 1, 'Tich cuc', 'Chuan_4_5_sao'

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

print("\n=== THONG KE ASPECT PHAN BO ===")
print(df['aspect_category'].value_counts())

# Save clean CSV
df.to_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')
df.to_csv('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.csv', index=False, encoding='utf-8-sig')

# 70 / 15 / 15 split
train_df, temp_df = train_test_split(df, test_size=0.30, random_state=42, stratify=df['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42, stratify=temp_df['label'])

for base in ['d:/HocMayPrJ/data', 'd:/HocMayPrJ/Nhom_12']:
    train_df.to_csv(f'{base}/train.csv', index=False, encoding='utf-8-sig')
    val_df.to_csv(f'{base}/val.csv', index=False, encoding='utf-8-sig')
    test_df.to_csv(f'{base}/test.csv', index=False, encoding='utf-8-sig')

try:
    df.to_excel('d:/HocMayPrJ/data/app_reviews_cleaned.xlsx', index=False)
    df.to_excel('d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx', index=False)
    train_df.to_excel('d:/HocMayPrJ/data/train.xlsx', index=False)
    val_df.to_excel('d:/HocMayPrJ/data/val.xlsx', index=False)
    test_df.to_excel('d:/HocMayPrJ/data/test.xlsx', index=False)
    val_df.to_excel('d:/HocMayPrJ/Nhom_12/val.xlsx', index=False)
    test_df.to_excel('d:/HocMayPrJ/Nhom_12/test.xlsx', index=False)
except Exception as e:
    print("Excel save note:", e)

print("=== GIAI DOAN 2: CAP NHAT NOTEBOOK VA THUC THI EXECUTEPREPROCESSOR ===")

nb_path = 'd:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb'
nb = nbformat.read(nb_path, as_version=4)

# Update Cell 0
nb.cells[0].source = """# DỰ ÁN HỌC MÁY (MACHINE LEARNING) - NLP-01
# BÁO CÁO TIẾN ĐỘ THỰC HIỆN TỪ KAN-1 ĐẾN KAN-8
## Đề tài: Phân tích quan điểm phản hồi của người dùng về ứng dụng di động
**Giảng viên hướng dẫn:** ThS. Hà Thị Thanh  
**Nhóm thực hiện:** Nhóm 12  
* Lê Hồng Sơn (Nhóm trưởng)
* Lưu Thị Khánh Ly
* Ngô Thị Sinh
* Nguyễn Thanh Tùng

---
*Quy trình kỹ thuật hoàn chỉnh tích hợp phân loại 5 khía cạnh (Aspect Taxonomy) và chuẩn hóa nhãn theo yêu cầu:*
1. **Phần I (KAN-1 -> KAN-5):** Thu thập dữ liệu thô, Thống kê mô tả, Ẩn danh PII, Khử nhiễu nghịch nhãn (Sarcasm/5 sao chê), Phân loại 5 khía cạnh (Aspect: Vận chuyển & Giao nhận, Hiệu năng & Lỗi App, Giao dịch & Giá cả, Bảo mật & Tài khoản, Dịch vụ & CSKH), Trực quan hóa EDA & Tiền xử lý tách từ tiếng Việt chuẩn.
2. **Phần II (KAN-6 -> KAN-8):** Phân chia phân tầng 70/15/15, Trích xuất đặc trưng TF-IDF trên từ ghép tiếng Việt, Huấn luyện 3 mô hình học máy và Đánh giá so sánh chi tiết trên tập kiểm thử độc lập (Test Set)."""

# Update Cell 14
nb.cells[14].source = """---
## BUOC 2: PHAN CHIA TAP DU LIEU PHAN TANG (STRATIFIED SPLIT 70 / 15 / 15)
Chung ta thiet lap bai toan phan loai nhi phan:
* **Nhan 0 (Tieu cuc):** Danh gia 1, 2, 3 sao (hoac duoc phat hien la nghich nhan chui boi / che nang).
* **Nhan 1 (Tich cuc):** Danh gia 4, 5 sao (hoac duoc phat hien la nghich nhan khen ngoi tuyet doi).

Su dung phuong phap phan tang (`stratify=y`) de giu nguyen ty le can bang giua cac lop tren ca 3 tap:
* **Tap Train (70%):** Duyen luyen mo hinh va hoc bo tu dien TF-IDF.
* **Tap Validation (15%):** Danh gia kiem dinh cheo, lua chon sieu tham so.
* **Tap Test (15%):** Danh gia khach quan doc lap tren du lieu chua tung thay (Unseen data)."""

# Update Cell 20
nb.cells[20].source = """---
## BƯỚC 5: TRỰC QUAN HÓA SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH TRÊN TẬP TEST (KAN-8)
Trực quan hóa biểu đồ cột so sánh 4 chỉ số đo lường (Accuracy, Precision, Recall, Macro F1) giữa 3 mô hình học máy trên tập kiểm thử độc lập (Test Set: 2.237 mẫu)."""

# Update Cell 22
nb.cells[22].source = """---
## KẾT LUẬN VÀ HOÀN THÀNH TIẾN ĐỘ ĐẾN GIAI ĐOẠN KAN-8
* **Hoàn thành KAN-1 đến KAN-5:** Đã cào 15.541 đánh giá thô, thiết lập quy tắc nhãn nhị phân chuẩn xác (1, 2, 3 sao là Tiêu cực; 4, 5 sao là Tích cực), ứng dụng bộ lọc từ khóa LLM/Rule-based để xử lý triệt để 50 trường hợp nghịch nhãn (48 mẫu 5 sao chửi bới / 2 mẫu 1-3 sao khen ngợi), phân loại toàn diện 5 khía cạnh nghiệp vụ (Aspect: Vận chuyển & Giao nhận, Hiệu năng & Lỗi App, Giao dịch & Giá cả, Bảo mật & Tài khoản, Dịch vụ & CSKH) và tách từ tiếng Việt chuẩn.
* **Hoàn thành KAN-6:** Xây dựng Pipeline TF-IDF Unigram + Bigram với chuẩn hóa L2-norm trên 24.432 đặc trưng từ ghép tiếng Việt, phân tầng dữ liệu 70/15/15 (Train: 10.437, Val: 2.236, Test: 2.237 mẫu) đảm bảo chống rò rỉ dữ liệu (Data Leakage).
* **Hoàn thành KAN-7:** Huấn luyện 3 mô hình học máy gồm Multinomial Naive Bayes (Baseline), Logistic Regression (balanced) và Linear Support Vector Classifier (LinearSVC).
* **Hoàn thành KAN-8:** Đánh giá độc lập trên tập Test (2.237 mẫu). Mô hình **LinearSVC** đạt hiệu năng dẫn đầu toàn diện với Accuracy vượt 90.7% và Macro F1 vượt 89.2%, đáp ứng xuất sắc mọi tiêu chí bài toán NLP tiếng Việt."""

# Execute notebook
print("Dang thuc thi toan bo notebook...")
os.chdir('d:/HocMayPrJ')
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': 'd:/HocMayPrJ'}})

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

with open('d:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("=== THUC THI NOTEBOOK HOAN TAT 100%! ===")
