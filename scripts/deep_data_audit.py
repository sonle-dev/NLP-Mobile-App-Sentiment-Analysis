import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import pandas as pd

df = pd.read_csv('d:/HocMayPrJ/data/app_reviews_cleaned.csv')

print("=== 1. KIEM TRA CAC PHAN HOI NGAN (<= 2 TU) ===")
short_reviews = df[df['word_count'] <= 2]
print(f"So luong phan hoi <= 2 tu: {len(short_reviews)}")
print(short_reviews['content'].value_counts().head(20))

print("\n=== 2. KIEM TRA CAC PHAN HOI VO NGHIA / SPAM / KY TU RAC ===")
# Tim cac comment chi gom chu cai lap lai, ky tu dac biet, hoac khong chua nguyen am tieng Viet hop le
def is_gibberish(text):
    t = str(text).strip().lower()
    # Toan ky tu lap lai >= 3 lan (vd: aaaaa, zzzzz, ddd)
    if re.search(r'(.)\1{3,}', t):
        return True
    # Khong co chu cai nao (chi so hoac dau)
    if not re.search(r'[a-zA-Zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', t):
        return True
    # Qua ngan va chua chuoi vo nghia
    if len(t) <= 3 and t in ['asdf', 'ghjk', 'qwerty', 'zzz', 'xxx', 'ccc', 'bbb', 'aaa']:
        return True
    return False

gibberish = df[df['content'].apply(is_gibberish)]
print(f"So luong comment co dau hieu spam / ky tu lap vo nghia: {len(gibberish)}")
print("Mau 10 comment spam:")
for idx, r in gibberish.head(10).iterrows():
    print(f"- [{r['app_name']} | {r['rating']}*]: {r['content']}")

print("\n=== 3. KIEM TRA CAC COMMENT TRONG HIEU_NANG_VA_LOI_APP NHUNG CHUA TU KHOA NGHIEP VU ===")
# Kiem tra xem trong 7.412 mau cua Hieu_nang_Va_Loi_App con bi sot tu khoa nghiep vu nao khong
delivery_kws = ['ship', 'giao', 'đơn', 'hàng', 'tài xế', 'món', 'quán', 'bác tài', 'cuốc', 'đón', 'rước', 'xe']
trans_kws = ['tiền', 'chuyển', 'nạp', 'rút', 'phí', 'giá', 'cước', 'xu', 'voucher', 'mã giảm', 'thẻ', 'stk', 'ngân hàng', 'thanh toán']
sec_kws = ['đăng nhập', 'mật khẩu', 'otp', 'khóa', 'bảo mật', 'lừa đảo', 'cccd', 'vneid', 'sinh trắc', 'face id', 'vân tay', 'nick', 'tài khoản']
cskh_kws = ['tổng đài', 'nhân viên', 'hỗ trợ', 'cskh', 'thái độ', 'khiếu nại', 'hotline', 'phục vụ']

hn = df[df['aspect_category'] == 'Hieu_nang_Va_Loi_App']
has_del = hn[hn['content'].str.lower().apply(lambda x: any(k in x for k in delivery_kws))]
has_trans = hn[hn['content'].str.lower().apply(lambda x: any(k in x for k in trans_kws))]
has_sec = hn[hn['content'].str.lower().apply(lambda x: any(k in x for k in sec_kws))]
has_cskh = hn[hn['content'].str.lower().apply(lambda x: any(k in x for k in cskh_kws))]

print(f"Tong mau trong Hieu_nang_Va_Loi_App: {len(hn)}")
print(f"- Chua tu lien quan van chuyen/don hang: {len(has_del)}")
print(f"- Chua tu lien quan giao dich/tien/phi: {len(has_trans)}")
print(f"- Chua tu lien quan bao mat/tai khoan: {len(has_sec)}")
print(f"- Chua tu lien quan CSKH/nhan vien: {len(has_cskh)}")
