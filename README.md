# 📱 Phan Tich Quan Diem Phan Hoi Cua Nguoi Dung Ve Ung Dung Di Dong
> **Hoc phan**: Hoc may (Machine Learning) --- Khoa Cong nghe Thong tin, Truong Dai hoc Cong nghe Thong tin va Truyen thong (ICTU)  
> **Giang vien huong dan**: ThS. Ha Thi Thanh  
> **Nhom thuc hien**: **Nhom 12**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Tien_do-Buoc_1:_Thu_thap_du_lieu_(Hoan_thanh)-brightgreen.svg)]()
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-black.svg)](https://peps.python.org/pep-0008/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 👥 Danh Sach Thanh Vien & Phan Cong Nhiem Vu (Nhom 12)

Du an duoc quan ly va phan cong cong viec tuan tu theo quy trinh 11 buoc chuan:

| STT | Ho va Ten | Ma Sinh Vien | GitHub Account | Vai Tro | Trach Nhiem Ky Thuat Chinh |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | **Le Hong Son** | `DTC235200647` | [@sonle-dev](https://github.com/sonle-dev) | **Truong nhom** | Quan tri du an, thiet ke kien truc he thong, xay dung pipeline tien xu ly van ban tieng Viet & trich xuat dac trung TF-IDF, huan luyen cac mo hinh Machine Learning. |
| 2 | **Luu Thi Khanh Ly** | `DTC235200483` | [@luuthily34-lab](https://github.com/luuthily34-lab) | **Thanh vien** | Lap trinh cong cu thu thap du lieu da luong (`scraper_gui.py`), xu ly bao mat va an danh hoa thong tin ca nhan (PII), truc quan hoa du lieu kham pha (EDA). |
| 3 | **Ngo Thi Sinh** | `DTC235200645` | [@sinhnt-dev](https://github.com/sinhnt-dev) | **Thanh vien** | Thiet ke thang do danh gia mo hinh (Precision, Recall, Macro F1), xay dung kich ban kiem thu tu dong, phan tich ma tran nham lan (Confusion Matrix) va mo xe loi sai (Error Analysis). |
| 4 | **Nguyen Thanh Tung** | `DTC235200811` | [@NguyenThanhTung812](https://github.com/NguyenThanhTung812) | **Thanh vien** | Doi soat chuan dau ra, xay dung ung dung Web Demo tuong tac nguoi dung (Streamlit), thiet lap quy trinh tu dong hoa kiem thu ma nguon (CI/CD). |

---

## 📌 Bao Cao Tien Do Du An: Buoc 1 --- Thu Thap Du Lieu Thuc Te

### 1. Muc tieu va Pham vi thu thap
Nhom tien hanh khao sat va thu thap du lieu danh gia thuc te cua nguoi dung tu hai nen tang phan phoi ung dung lon nhat hien nay la **Google Play Store** va **Apple App Store**. Du lieu tap trung vao 8 ung dung di dong pho bien tai Viet Nam thuoc 4 linh vuc trong yeu:
* **Thuong mai dien tu**: Shopee, TikTok Shop
* **Vi dien tu & Thanh toan so**: MoMo, ZaloPay
* **Ngan hang so**: MB Bank, Agribank E-Mobile Banking
* **Dich vu tien ich (Giao do an & Di chuyen)**: Grab, ShopeeFood

### 2. Cong cu cao du lieu tu dong (`tools/scraper_gui.py`)
Nhom da chu dong phat trien cong cu phan mem thu thap du lieu voi cac dac ta ky thuat:
* **Giao dien do hoa (GUI)**: Lap trinh bang Python `tkinter`, ho tro nhap lien ket truc tiep tu trinh duyet hoac ma goi ung dung (Package ID / Apple ID).
* **Kien truc xu ly da luong**: Su dung `threading.Thread` ket hop hang doi `queue.Queue` de phan tach hoan toan giua luong giao dien nguoi dung va luong cao ngam, ngan chan tinh trang ung dung bi treo (Not Responding) khi keo luong du lieu lon.
* **Co che thu thap**: Tich hop module `google-play-scraper` va giao tiep qua iTunes RSS API cua Apple.
* **Quy tac phan nhan so bo**: Tu dong anh xa so sao danh gia (Star Rating) sang nhan cam xuc theo tieu chuan 3 lop:
  * $1 - 2\bigstar \rightarrow$ **Tieu cuc (Negative)**
  * $3\bigstar \rightarrow$ **Trung tinh (Neutral)**
  * $4 - 5\bigstar \rightarrow$ **Tich cuc (Positive)**

### 3. Ket qua du lieu tho ban dau (`data/app_reviews_raw.csv`)
* **Tong so ban ghi thu thap**: **15.541 danh gia**.
* **Dinh dang cau truc**: Bang du lieu bao gom cac truong thong tin: `review_id`, `user_name`, `app_name`, `platform`, `rating`, `sentiment`, `content`, `thumbs_up`, `review_date`.
* **Ke hoach giai doan tiep theo (Buoc 2)**: Chuyen giao du lieu cho module xu ly bao mat de an danh hoa hoan toan thong tin dinh danh ca nhan (PII - loai bo ten nguoi dung, che so dien thoai va email).

---

## 🗂 Cau Truc Ma Nguon Hien Tai (Moc Buoc 1)

```text
NLP-Mobile-App-Sentiment-Analysis/
├── data/
│   └── app_reviews_raw.csv           # 15.541 danh gia tho thu thap tu Google Play & App Store
├── tools/                            # Cong cu thu thap du lieu do nhom tu phat trien
│   ├── scraper_gui.py                # Ma nguon cong cu cao du lieu da luong (Tkinter)
│   └── run.bat                       # Kich ban khoi chay nhanh cong cu
├── requirements.txt                  # Danh muc thu vien phu thuoc
├── .gitignore                        # Cau hinh loai tru cac tep tam thoi va moi truong
└── README.md                         # Tai lieu thuyet minh du an va tien do ky thuat
```

---

## ⚙️ Huong Dan Cai Dat & Van Hanh

### 1. Thiet lap moi truong thuc thi
```bash
# Sao chep kho luu tru ve may cuc bo
git clone https://github.com/sonle-dev/NLP-Mobile-App-Sentiment-Analysis.git
cd NLP-Mobile-App-Sentiment-Analysis

# Khoi tao va kich hoat moi truong ao Python
python -m venv .venv
# Tren he dieu hanh Windows:
.venv\Scripts\activate

# Cai dat cac thu vien phu thuoc
pip install -r requirements.txt
```

### 2. Van hanh cong cu cao du lieu
```bash
python tools/scraper_gui.py
# Hoac nhap dup tep tools/run.bat
```

---

## 🔄 Quy Trinh Phat Trien & Kiem Soat Phien Ban (Git Workflow)

Du an ap dung mo hinh phan nhanh tinh nang (**Feature Branching Workflow**) va quy trinh danh gia cheo ma nguon (**Peer Review**) nham dam bao tinh toan ven du lieu:

1. **Phan nhanh tinh nang (Branching)**: Moi nhiem vu doc lap duoc phat trien tren mot nhanh rieng biet, khong chinh sua truc tiep tren nhanh `main`:
   ```bash
   git checkout -b feature/<ten_tinh_nang>
   ```
2. **Quy chuan thong diep Commit (Conventional Commits)**:
   * `[Thu-thap] feat: Cap nhat giao dien cao du lieu App Store`
   * `[Bao-mat] feat: Xu ly an danh thong tin ca nhan PII`
   * `[Tien-xu-ly] feat: Chuan hoa tu dien viet tat teencode tieng Viet`
   * `[Kiem-thu] test: Xay dung ca kiem thu hoi quy tinh toan ven du lieu`
3. **Yeu cau hop nhat (Pull Request - PR) & Duyet cheo (Review)**:
   * Cac nhanh tinh nang khi hoan thanh phai gui Pull Request.
   * It nhat mot thanh vien khac trong nhom kiem thu, tham dinh chat luong ma nguon va chap thuan (Approve) truoc khi hop nhat vao nhanh `main`.
