# BÁO CÁO KIỂM TOÁN DỮ LIỆU VÀ MINH CHỨNG LÀM SẠCH (DATA AUDIT & EVIDENCE REPORT)
**Dự án:** Phân tích quan điểm phản hồi của người dùng về ứng dụng di động (NLP-01)  
**Nhóm thực hiện:** Nhóm 12  
**Thời gian rà soát:** 14/11/2026  
**Quy mô dữ liệu sạch:** 14.910 bản ghi  

---

## 1. BẢNG TỔNG QUAN TÍNH TOÀN VẸN VÀ ĐỘ SẠCH DỮ LIỆU

| Chỉ số kiểm tra | Kết quả kiểm toán | Đánh giá kỹ thuật |
| :--- | :---: | :--- |
| **Tổng số bản ghi hợp lệ** | **14.910 dòng** | Đã loại bỏ 631 bản ghi rỗng / spam trùng lặp hoàn toàn. |
| **Giá trị khuyết thiếu (Missing/Null)** | **0 ô (0%)** | $100\%$ các trường thuộc tính đều đầy đủ, không có dữ liệu khuyết. |
| **Trùng lặp nội dung (Duplication)** | **0 dòng (0%)** | Áp dụng thuật toán băm SHA-256 để khử sạch bản ghi trùng khớp nội dung. |
| **Bảo mật dữ liệu cá nhân (PII Leakage)** | **0 vi phạm (0%)** | Tuân thủ Nghị định 13/2023/NĐ-CP: Ẩn danh $100\%$ tên người dùng, SĐT `[SDT]`, STK `[STK]`, email `[EMAIL]`. |
| **Dị biệt số sao (Rating Outliers)** | **0 mẫu (0%)** | Toàn bộ rating nằm nghiêm ngặt trong khoảng $[1, 5]$. |

---

## 2. MINH CHỨNG KHỬ NHIỄU NGHỊCH NHÃN (LABEL AUDIT EVIDENCE)

### A. Quy tắc cốt lõi:
* **1, 2, 3 sao** $\rightarrow$ **Tiêu cực (Nhãn 0)**.
* **4, 5 sao** $\rightarrow$ **Tích cực (Nhãn 1)**.

### B. Minh chứng xử lý trường hợp: Chấm 4-5 sao nhưng nội dung CHỬI BỚI / LỖI THẬM TỆ
* **Tổng số mẫu được hệ thống phát hiện và tự động sửa sang Tiêu cực (0):** **46 mẫu**.
* **3 mẫu đối chứng thực tế từ tập dữ liệu:**

1. **Mẫu 1 (Rating: 5 sao):**
   * *Nội dung gốc:* `"Ứng dụng quá tệ. Ứng dụng quá tệ so với các ứng dụng của các ngân hàng khác. Bày ra mọi cách để khách hàng cài thêm ứng dụng để thu tiền; trong khi chất lượng quá tệ"`
   * *Xử lý:* Hệ thống phát hiện từ khóa tiêu cực mạnh `quá tệ`, tự động chuyển sang **`sentiment: Tieu cuc` (nhãn 0)**, gắn cờ `Nghich_nhan_5sao_che`.
2. **Mẫu 2 (Rating: 4 sao):**
   * *Nội dung gốc:* `"quá tệ. Cực kỳ tệ chuyển khoản cứ bị lỗi không nhận được tiền thu phí thàng tháng cũng cực kì cao nói chung là app tệ nhất..."`
   * *Xử lý:* Phát hiện từ khóa `cực kỳ tệ`, `lỗi không nhận được tiền`, chuyển sang **`sentiment: Tieu cuc` (nhãn 0)**.
3. **Mẫu 3 (Rating: 5 sao):**
   * *Nội dung gốc:* `"App không dùng được trên iphone. Không vào được app từ iphone..."`
   * *Xử lý:* Phát hiện từ khóa `không dùng được`, `không vào được`, chuyển sang **`sentiment: Tieu cuc` (nhãn 0)**.

### C. Minh chứng xử lý trường hợp: Chấm 1-2 sao nhưng KHEN NGỢI HẾT LỜI (Bấm nhầm)
* **Tổng số mẫu được hệ thống phát hiện và tự động sửa sang Tích cực (1):** **2 mẫu**.
* **Mẫu đối chứng thực tế:**
  * *Rating gốc:* 1 sao.
  * *Nội dung gốc:* `"rất hữu ích lãi cao và chỉ phí thấp quá tuyệt vời đánh dùng trong lâu dài 🌹💗"`
  * *Xử lý:* Người dùng viết lời khen tuyệt đối (`rất hữu ích`, `quá tuyệt vời`), không có bất kỳ từ phàn nàn nào. Hệ thống chuyển sang **`sentiment: Tich cuc` (nhãn 1)**, gắn cờ `Nghich_nhan_1sao_khen`.

---

## 3. MINH CHỨNG PHÂN LOẠI 4 KHÍA CẠNH NGHIỆP VỤ (ASPECT EXTRACTION EVIDENCE)

| Nhóm Aspect | Số lượng | Tỷ lệ | Ví dụ minh chứng thực tế trích xuất từ dữ liệu |
| :--- | :---: | :---: | :--- |
| **`Hieu_nang_UI_UX`** | $9.935$ | $66.6\%$ | *"Người dùng Agribank. Ứng dụng thật tiện ích và tuyệt vời với tất cả mọi người. Mình cảm thấy hài lòng..."* (từ khóa: `tiện ích`, `mượt mà`, `lag`, `treo`) |
| **`Giao_dich_Thanh_toan`** | $3.097$ | $20.8\%$ | *"Mục thông báo biến động số dư trong app cũng ổn mà, bấm vào 1 phát là tra được lịch sử chuyển khoản..."* (từ khóa: `chuyển tiền`, `số dư`, `nạp rút`, `phí`) |
| **`Dich_vu_CSKH`** | $1.304$ | $8.7\%$ | *"Tệ. Người lớn mở tài khoản tại chi nhánh không biết gì nhân viên gài mua số tài khoản hết hơn 550k..."* (từ khóa: `nhân viên`, `chi nhánh`, `tổng đài`, `khiếu nại`) |
| **`Bao_mat_Tai_khoan`** | $574$ | $3.9\%$ | *"muốn chuyển khoản mà đợi 30p vẫn không thấy gửi mã otp về, xác thực sinh trắc học thì báo lỗi..."* (từ khóa: `mã otp`, `đăng nhập`, `sinh trắc học`, `khóa`) |

---

## 4. DANH MỤC TỆP LƯU TRỮ VÀ DẪN CHỨNG TRÊN HỆ THỐNG

1. **Tệp dữ liệu sạch toàn diện (Đầy đủ 14 cột dẫn chứng):**
   * Excel: [`data/app_reviews_cleaned.xlsx`](file:///d:/HocMayPrJ/data/app_reviews_cleaned.xlsx)
   * Excel (bản sao thư mục nộp bài): [`Nhom_12/app_reviews_cleaned.xlsx`](file:///d:/HocMayPrJ/Nhom_12/app_reviews_cleaned.xlsx)
   * CSV: [`data/app_reviews_cleaned.csv`](file:///d:/HocMayPrJ/data/app_reviews_cleaned.csv)
2. **Bộ 3 tệp dữ liệu đã phân chia độc lập (Train / Val / Test):**
   * Tập Train (70% - 10.437 mẫu): [`Nhom_12/train.xlsx`](file:///d:/HocMayPrJ/Nhom_12/train.xlsx) & [`Nhom_12/train.csv`](file:///d:/HocMayPrJ/Nhom_12/train.csv)
   * Tập Val (15% - 2.236 mẫu): [`Nhom_12/val.xlsx`](file:///d:/HocMayPrJ/Nhom_12/val.xlsx) & [`Nhom_12/val.csv`](file:///d:/HocMayPrJ/Nhom_12/val.csv)
   * Tập Test (15% - 2.237 mẫu): [`Nhom_12/test.xlsx`](file:///d:/HocMayPrJ/Nhom_12/test.xlsx) & [`Nhom_12/test.csv`](file:///d:/HocMayPrJ/Nhom_12/test.csv)
3. **Mã nguồn Notebook chạy kiểm thử thực tế:**
   * Notebook: [`Nhom_12/du_an_hoc_may_nhom_12.ipynb`](file:///d:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb) (Cell 9 in bảng đối soát nhãn, Cell 21 in bảng Classification Report đạt F1 $88.74\%$).
4. **Kho lưu trữ mã nguồn:**
   * GitHub Repository: `https://github.com/sonle-dev/NLP-Mobile-App-Sentiment-Analysis.git` (Commit `c04e7c0`).
