# 📱 Phân Tích Quan Điểm Phản Hồi Của Người Dùng Về Ứng Dụng Di Động
> **Học phần**: Học máy (Machine Learning) --- Khoa Công nghệ Thông tin, Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU)  
> **Giảng viên hướng dẫn**: ThS. Hà Thị Thanh  
> **Nhóm thực hiện**: **Nhóm 12**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Tiến_độ-Bước_1:_Thu_thập_dữ_liệu_(Hoàn_thành)-brightgreen.svg)]()
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-black.svg)](https://peps.python.org/pep-0008/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 👥 Danh Sách Thành Viên & Phân Công Nhiệm Vụ (Nhóm 12)

Dự án được quản lý và phân công công việc tuần tự theo quy trình 11 bước chuẩn:

| STT | Họ và Tên | Mã Sinh Viên | GitHub Account | Vai Trò | Trách Nhiệm Kỹ Thuật Chính |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | **Lê Hồng Sơn** | `DTC235200647` | [@sonle-dev](https://github.com/sonle-dev) | **Trưởng nhóm** | Quản trị dự án, thiết kế kiến trúc hệ thống, xây dựng pipeline tiền xử lý văn bản tiếng Việt & trích xuất đặc trưng TF-IDF, huấn luyện các mô hình Machine Learning. |
| 2 | **Lưu Thị Khánh Ly** | `DTC235200483` | [@luuthily34-lab](https://github.com/luuthily34-lab) | **Thành viên** | Lập trình công cụ thu thập dữ liệu đa luồng (`scraper_gui.py`), xử lý bảo mật và ẩn danh hóa thông tin cá nhân (PII), trực quan hóa dữ liệu khám phá (EDA). |
| 3 | **Ngô Thị Sinh** | `DTC235200645` | [@sinhnt-dev](https://github.com/sinhnt-dev) | **Thành viên** | Thiết kế thang đo đánh giá mô hình (Precision, Recall, Macro F1), xây dựng kịch bản kiểm thử tự động, phân tích ma trận nhầm lẫn (Confusion Matrix) và mổ xẻ lỗi sai (Error Analysis). |
| 4 | **Nguyễn Thanh Tùng** | `DTC235200811` | [@NguyenThanhTung812](https://github.com/NguyenThanhTung812) | **Thành viên** | Đối soát chuẩn đầu ra, xây dựng ứng dụng Web Demo tương tác người dùng (Streamlit), thiết lập quy trình tự động hóa kiểm thử mã nguồn (CI/CD). |

---

## 📌 Báo Cáo Tiến Độ Dự Án: Bước 1 --- Thu Thập Dữ Liệu Thực Tế

### 1. Mục tiêu và Phạm vi thu thập
Nhóm tiến hành khảo sát và thu thập dữ liệu đánh giá thực tế của người dùng từ hai nền tảng phân phối ứng dụng lớn nhất hiện nay là **Google Play Store** và **Apple App Store**. Dữ liệu tập trung vào 8 ứng dụng di động phổ biến tại Việt Nam thuộc 4 lĩnh vực trọng yếu:
* **Thương mại điện tử**: Shopee, TikTok Shop
* **Ví điện tử & Thanh toán số**: MoMo, ZaloPay
* **Ngân hàng số**: MB Bank, Agribank E-Mobile Banking
* **Dịch vụ tiện ích (Giao đồ ăn & Di chuyển)**: Grab, ShopeeFood

### 2. Công cụ cào dữ liệu tự động (`tools/scraper_gui.py`)
Nhóm đã chủ động phát triển công cụ phần mềm thu thập dữ liệu với các đặc tả kỹ thuật:
* **Giao diện đồ họa (GUI)**: Lập trình bằng Python `tkinter`, hỗ trợ nhập liên kết trực tiếp từ trình duyệt hoặc mã gói ứng dụng (Package ID / Apple ID).
* **Kiến trúc xử lý đa luồng**: Sử dụng `threading.Thread` kết hợp hàng đợi `queue.Queue` để phân tách hoàn toàn giữa luồng giao diện người dùng và luồng cào ngầm, ngăn chặn tình trạng ứng dụng bị treo (Not Responding) khi kéo lượng dữ liệu lớn.
* **Cơ chế thu thập**: Tích hợp module `google-play-scraper` và giao tiếp qua iTunes RSS API của Apple.
* **Quy tắc phân nhãn sơ bộ**: Tự động ánh xạ số sao đánh giá (Star Rating) sang nhãn cảm xúc theo tiêu chuẩn 3 lớp:
  * $1 - 2\bigstar \rightarrow$ **Tiêu cực (Negative)**
  * $3\bigstar \rightarrow$ **Trung tính (Neutral)**
  * $4 - 5\bigstar \rightarrow$ **Tích cực (Positive)**

### 3. Kết quả dữ liệu thô ban đầu (`data/app_reviews_raw.csv`)
* **Tổng số bản ghi thu thập**: **15.541 đánh giá**.
* **Định dạng cấu trúc**: Bảng dữ liệu bao gồm các trường thông tin: `review_id`, `user_name`, `app_name`, `platform`, `rating`, `sentiment`, `content`, `thumbs_up`, `review_date`.
* **Kế hoạch giai đoạn tiếp theo (Bước 2)**: Chuyển giao dữ liệu cho module xử lý bảo mật để ẩn danh hóa hoàn toàn thông tin định danh cá nhân (PII - loại bỏ tên người dùng, che số điện thoại và email).

---

## 🗂 Cấu Trúc Mã Nguồn Hiện Tại (Mốc Bước 1)

```text
NLP-Mobile-App-Sentiment-Analysis/
├── data/
│   └── app_reviews_raw.csv           # 15.541 đánh giá thô thu thập từ Google Play & App Store
├── tools/                            # Công cụ thu thập dữ liệu do nhóm tự phát triển
│   ├── scraper_gui.py                # Mã nguồn công cụ cào dữ liệu đa luồng (Tkinter)
│   └── run.bat                       # Kịch bản khởi chạy nhanh công cụ
├── requirements.txt                  # Danh mục thư viện phụ thuộc
├── .gitignore                        # Cấu hình loại trừ các tệp tạm thời và môi trường
└── README.md                         # Tài liệu thuyết minh dự án và tiến độ kỹ thuật
```

---

## ⚙️ Hướng Dẫn Cài Đặt & Vận Hành

### 1. Thiết lập môi trường thực thi
```bash
# Sao chép kho lưu trữ về máy cục bộ
git clone https://github.com/sonle-dev/NLP-Mobile-App-Sentiment-Analysis.git
cd NLP-Mobile-App-Sentiment-Analysis

# Khởi tạo và kích hoạt môi trường ảo Python
python -m venv .venv
# Trên hệ điều hành Windows:
.venv\Scripts\activate

# Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt
```

### 2. Vận hành công cụ cào dữ liệu
```bash
python tools/scraper_gui.py
# Hoặc nhấp đúp tệp tools/run.bat
```

---

## 🔄 Quy Trình Phát Triển & Kiểm Soát Phiên Bản (Git Workflow)

Dự án áp dụng mô hình phân nhánh tính năng (**Feature Branching Workflow**) và quy trình đánh giá chéo mã nguồn (**Peer Review**) nhằm đảm bảo tính toàn vẹn dữ liệu:

1. **Phân nhánh tính năng (Branching)**: Mỗi nhiệm vụ độc lập được phát triển trên một nhánh riêng biệt, không chỉnh sửa trực tiếp trên nhánh `main`:
   ```bash
   git checkout -b feature/<ten_tinh_nang>
   ```
2. **Quy chuẩn thông điệp Commit (Conventional Commits)**:
   * `[Thu-thap] feat: Cập nhật giao diện cào dữ liệu App Store`
   * `[Bao-mat] feat: Xử lý ẩn danh thông tin cá nhân PII`
   * `[Tien-xu-ly] feat: Chuẩn hóa từ điển viết tắt teencode tiếng Việt`
   * `[Kiem-thu] test: Xây dựng ca kiểm thử hồi quy tính toàn vẹn dữ liệu`
3. **Yêu cầu hợp nhất (Pull Request - PR) & Duyệt chéo (Review)**:
   * Các nhánh tính năng khi hoàn thành phải gửi Pull Request.
   * Ít nhất một thành viên khác trong nhóm kiểm thử, thẩm định chất lượng mã nguồn và chấp thuận (Approve) trước khi hợp nhất vào nhánh `main`.
