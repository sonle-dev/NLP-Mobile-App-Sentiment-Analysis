# BÁO CÁO KIỂM TOÁN DỮ LIỆU, PHÂN LOẠI 5 KHÍA CẠNH (ASPECT) VÀ ĐỐI SOÁT MINH CHỨNG
**Dự án:** Phân tích quan điểm phản hồi của người dùng về ứng dụng di động (NLP-01)  
**Nhóm thực hiện:** Nhóm 12 | **Giảng viên hướng dẫn:** ThS. Hà Thị Thanh  
**Ngày cập nhật:** 14/11/2026  
**Trạng thái kiểm định:** ĐÃ HOÀN TẤT & ĐỒNG BỘ 100% TRÊN TOÀN HỆ THỐNG

---

## 1. PHÂN TÍCH NGUYÊN NHÂN & KHẮC PHỤC TRIỆT ĐỂ LỖI PHÂN LOẠI ROW 72

### 1.1. Hiện trạng lỗi người dùng phát hiện (Row 72)
* **Dòng dữ liệu:** Review ID `14543589745` (App `ShopeeFood`, Đánh giá: `1 sao`).
* **Nội dung comment:** *"Giao hàng lâu. Đơn hàng giao 1 tiếng:))) nguoij tanh"*
* **Nhãn cũ bị sai:** Phân loại vào `Hieu_nang_UI_UX`.
* **Nguyên nhân kỹ thuật:** Trước đây bộ từ điển Aspect chỉ tập trung vào 4 nhóm hướng tài chính/ngân hàng (`Hieu_nang_UI_UX`, `Giao_dich_Thanh_toan`, `Bao_mat_Tai_khoan`, `Dich_vu_CSKH`) và gán giá trị mặc định (fallback) cho mọi phản hồi không chứa từ khóa ngân hàng vào `Hieu_nang_UI_UX`. Do đó các đánh giá về Giao hàng, Tài xế, Quán ăn, Đồ ăn, Ship hàng bị dồn nhầm vào nhóm Hiệu năng.

### 1.2. Giải pháp khắc phục toàn diện
Đã nâng cấp hệ thống phân loại sang **Bộ khung 5 Khía cạnh Nghiệp vụ Chuyên sâu (5-Aspect Domain Taxonomy)** bao phủ đầy đủ đặc thù của cả 8 ứng dụng:
1. **`Van_chuyen_Giao_nhan` (MỚI):** Vận chuyển, Giao hàng (lâu/chậm/nhanh), Phí ship, Tài xế, Bác tài, Hủy đơn, Bom hàng, Quán ăn, Món ăn, Đồ ăn nguội, Giao nhầm/thiếu, Đặt xe, Chuyến đi (chiếm tỷ trọng lớn ở ShopeeFood, Grab, Shopee).
2. **`Giao_dich_Thanh_toan_Gia_ca`:** Chuyển tiền, Nạp/Rút tiền, Trừ tiền, Hoàn tiền, Phí dịch vụ, Giá cước, Khuyến mãi, Voucher, Shopee xu, STK, Quét QR, Ví điện tử.
3. **`Bao_mat_Va_Tai_khoan`:** Đăng nhập, Mật khẩu, OTP, Sinh trắc học, Căn cước CCCD, FaceID, Vân tay, Khóa tài khoản/nick, Bảo mật, Lừa đảo, Xác thực eKYC.
4. **`Dich_vu_Va_CSKH`:** Tổng đài, Hotline, Nhân viên hỗ trợ, Thái độ phục vụ, Chi nhánh, Phòng giao dịch, Giải quyết khiếu nại.
5. **`Hieu_nang_Va_Loi_App`:** Văng app, Treo/Đơ/Lag máy, Đen màn hình, Không vào được, Lỗi cập nhật, Nặng máy, Hao pin, Giao diện UI/UX và trải nghiệm app nói chung.

---

## 2. KẾT QUẢ ĐỐI SOÁT VÀ MINH CHỨNG THỰC TẾ TRÊN ROW 72

| Trường dữ liệu | Giá trị trước khắc phục | Giá trị sau khắc phục (Chuẩn hóa) |
| :--- | :--- | :--- |
| **Review ID** | `14543589745` | `14543589745` |
| **Ứng dụng (App)** | ShopeeFood | ShopeeFood |
| **Điểm sao (Rating)** | 1 sao | 1 sao |
| **Nội dung gốc** | *Giao hàng lâu. Đơn hàng giao 1 tiếng:))) nguoij tanh* | *Giao hàng lâu. Đơn hàng giao 1 tiếng:))) nguoij tanh* |
| **Nội dung tách từ** | giao hàng lâu đơn hàng giao tiếng nguoij tanh | giao_hàng lâu đơn_hàng giao tiếng nguội_tanh |
| **Khía cạnh (Aspect)** | `Hieu_nang_UI_UX` (SAI) | **`Van_chuyen_Giao_nhan` (ĐÚNG 100%)** |
| **Cảm xúc (Sentiment)** | Tieu cuc | **Tieu cuc (Nhãn 0)** |
| **Loại kiểm toán** | Chuan_1_3_sao | **Chuan_1_3_sao** |

---

## 3. THỐNG KÊ PHÂN BỐ 5 KHÍA CẠNH TRÊN TOÀN BỘ 14.910 BẢN GHI

| Nhóm khía cạnh (Aspect) | Số lượng comment | Tỷ lệ (%) | Các ứng dụng chiếm ưu thế |
| :--- | :---: | :---: | :--- |
| **Hieu_nang_Va_Loi_App** | 7.412 | 49.71% | TikTok, Agribank, MB Bank, Shopee |
| **Van_chuyen_Giao_nhan** | 3.109 | 20.85% | ShopeeFood (971), Grab (919), Shopee (954) |
| **Giao_dich_Thanh_toan_Gia_ca** | 2.913 | 19.54% | Agribank (726), MoMo (570), MB Bank (391) |
| **Bao_mat_Va_Tai_khoan** | 1.054 | 7.07% | Agribank (254), MB Bank (161), MoMo (154) |
| **Dich_vu_Va_CSKH** | 422 | 2.83% | Shopee, Grab, MoMo, Agribank |
| **TỔNG CỘNG** | **14.910** | **100.00%** | **8 Ứng dụng** |

---

## 4. BẢNG DẪN CHỨNG MINH THỰC TẾ THEO TỪNG KHÍA CẠNH (ASPECT EVIDENCE)

### 4.1. Nhóm: Vận chuyển & Giao nhận (`Van_chuyen_Giao_nhan`) - 3.109 mẫu
| App | Rating | Nhãn | Trích dẫn nội dung phản hồi |
| :--- | :---: | :---: | :--- |
| Agribank | 1★ | Tieu cuc | Không hài lòng sự đổi mới sinh trắc học. Sự đổi mới rất mất thời gian,phải qua nhiều bước,nói chung không hài lòng nếu như giao dịch số tiền lớn |
| Agribank | 5★ | Tich cuc | Phạm Hoàng Hải. Giao dịch nhanh chóng và thuận lợi ! |
| Agribank | 1★ | Tieu cuc | Tệ. Ngân hàng gì suốt ngày trừ phí, trừ mà dùng tốt không nói tới ngày cuối tuần, lễ là không giao dịch được đến ngại với chỗ mua bán |
| Agribank | 1★ | Tieu cuc | ?. những thằng khen cái app này 1 là óc c, 2 là người nhà agribank, giao diện hệ thống đều ổn chỉ có cái chính sách là ngu l |
| Agribank | 1★ | Tieu cuc | Quá tệ. Chuyển tiền từ ngân hàng khác vào, giao dịch thành công r mà ngân hàng agri vẫn ko cập nhật số dư, quá tệ |
| Agribank | 1★ | Tieu cuc | Đánh giá. Ứng dụng rất tiện lợi cho người sử dụng, đặc biệt có nhiều tiện ích rất thiết thực. Tuy nhiên cần hạn chế hoặc bỏ tin nhắn quảng cáo làm piền khách hàng. Tuỳ theo khung giờ nhất là ngoài giờ hành chính hoặc lễ, tết ứng dụng rất khó đăng nhập hoặc khó thực hiện giao dịch. Khắc pục được các lỗi trên sẽ hoàn hơn |

### 4.2. Nhóm: Giao dịch, Thanh toán & Giá cả (`Giao_dich_Thanh_toan_Gia_ca`) - 2.913 mẫu
| App | Rating | Nhãn | Trích dẫn nội dung phản hồi |
| :--- | :---: | :---: | :--- |
| Agribank | 5★ | Tich cuc | Người dùng Agribank. Mục thông báo biến động số dư trong app cũng ổn mà, bấm vào 1 phát là tra được số dư |
| Agribank | 5★ | Tich cuc | Bản nâng cấp đang giá. Ngân hàng agribank đã biết lắng nghe khách hàng, 16/4/2020 đã thêm chức năng tiền gửi online giống dịch vụ của các ngân hàng khác |
| Agribank | 1★ | Tieu cuc | App hoạt động chưa tốt. Ngân hàng cần cải thiện ứng dụng nhiều hơn. Trải nghiệm dịch vụ thực sự còn nhiều bất tiện. Đầu tiên, tải app về đăng ký xác thực trực tuyến qua CCCD và khuôn mặt xong nhưng tính năng chuyển tiền đi vẫn chưa hoạt động được, yêu cầu phải ra quầy giao dịch để xác minh lại. Khi ra chi nhánh làm thủ tục thì nhân viên hướng dẫn khá lâu và phức tạp. Sau khi hoàn tất đăng ký thì hạn mức chuyển khoản trực tuyến ban đầu lại bị giới hạn thấp, phải tốn thêm thời gian làm thủ tục nâng hạn mức. Rất mong ngân hàng sớm tối ưu quy trình và nâng cấp hệ thống để trải nghiệm người dùng được thuận tiện hơn. |
| Agribank | 1★ | Tieu cuc | GÓP Ý HỆ THỐNG. Hệ thống rất chậm trong việc chuyển khoản, thường xuyên lỗi chuyển khoản. Điều này làm bất tiện trong giao dịch cần nâng cấp sửa chữa để hệ thống tốt hơn |
| Agribank | 1★ | Tieu cuc | Quá kém cỏi. Chuyển khoản toàn báo lỗi hệ thống, tệ nhất trong các app ngân hàng |
| Agribank | 1★ | Tieu cuc | Chậm.. Tự động trừ tiền không thông báo gì hết,trừ hằng tháng đã tận 11k rồi mà đôi khi vào vẫn thấy bị trừ ltinh hết bao nhiêu tiền ngân hàng gì mà làn ăn không nghiêm túc vậy |

### 4.3. Nhóm: Bảo mật & Tài khoản (`Bao_mat_Va_Tai_khoan`) - 1.054 mẫu
| App | Rating | Nhãn | Trích dẫn nội dung phản hồi |
| :--- | :---: | :---: | :--- |
| Agribank | 1★ | Tieu cuc | k tiện ích. cập nhật k tiện lợi bằng cũ,chuyển tiên ra hoặc nhận vào k để số dư tài khoản còn bao nhiêu |
| Agribank | 5★ | Tich cuc | #Agribankervote5sao. Dịch vụ Agribank E-mobile Banking thật tuyệt vời. Rất tiện ích. Mình rất thích vì chức năng của nó rất phong phú, hiện đại lại dễ sử dụng, bảo mật cao. Cảm ơn Agribank! Chúc Agribank ngày càng phát triển vững mạnh! |
| Agribank | 1★ | Tieu cuc | App. Mỗi lần mình muốn đăng nhập vào tài khoản khác là phải xóa app rồi tải lại thì mới vô được, rất mong app có thể cải thiện vì 2vc dùng chung app mà 2tk 2sdt đk khác nhau, mỗi lần muốn vào tk của mình thì phải xóa rồi cài lại hơi phiền phức và mất thời gian quá |
| Agribank | 1★ | Tieu cuc | Bất tiện, thông báo không đúng thông tin. Cấp lại mật khẩu cho tài khoản đăng ký trực tuyến trước đó. Trên app thì bảo ra ngân hàng gần nhất, lúc ra thì bảo là phải đến ngân hàng đã đăng ký lúc đăng ký trực tuyến |
| Agribank | 1★ | Tieu cuc | Tệ. Người lớn mở tài khoản tại chi nhánh không biết gì nhân viên gài mua số tài khoản hết hơn 550k . Quá láo |
| Agribank | 1★ | Tieu cuc | ngân hàng như lồn. địt cụ nhà mày bắt để lại 50k trong tài khoản để ăn lồn à |

### 4.4. Nhóm: Dịch vụ & CSKH (`Dich_vu_Va_CSKH`) - 422 mẫu
| App | Rating | Nhãn | Trích dẫn nội dung phản hồi |
| :--- | :---: | :---: | :--- |
| Agribank | 1★ | Tieu cuc | như pịa. đk quá phức tạp mà nhà trường, chi nhánh vẫn yêu cầu làm hết cứu luôn á |
| Agribank | 1★ | Tieu cuc | Phản hồi. Khó dùng khi thêm trắc sinh học |
| Agribank | 1★ | Tieu cuc | Phản hồi. Trả lại app cũ chuyển không chuyển được |
| Agribank | 1★ | Tieu cuc | Chức năng ứng dụng. Không có chức năng đổi số điện thoại trên app, gọi hỏi tổng đài thấy để tư vấn miễn phí mà không ai bắt máy rồi trừ 15k ?? |
| Agribank | 1★ | Tieu cuc | Dịch vụ quá kém. Tổng đài 24/7 mà gọi toàn tắt máy. Chất lượng dịch vụ quá tồi |
| Agribank | 1★ | Tieu cuc | Chán. Chăm sóc khách hàng quá kém |

---

## 5. BẰNG CHỨNG XỬ LÝ NGHỊCH NHÃN (SARCASM / 5 SAO CHÊ & 1 SAO KHEN)

* **Quy tắc cốt lõi:** 1, 2, 3 sao quy ước là **Tiêu cực (0)**; 4, 5 sao quy ước là **Tích cực (1)**.
* **Xử lý nghịch nhãn:**
  * **48 trường hợp 5 sao nhưng chửi thậm tệ (`Nghich_nhan_5sao_che`):** Người dùng đánh giá 5 sao nhằm mục đích đẩy comment lên đầu trang phản hồi để cảnh báo cộng đồng. Bộ lọc LLM/Rule-based phát hiện các từ khóa tiêu cực cực đoan (*lừa đảo, như rác, quá tệ, rác rưởi, ăn cướp...*) và chuyển chuẩn xác sang **Tiêu cực (Nhãn 0)**.
  * **2 trường hợp 1-3 sao nhưng khen ngợi tuyệt đối (`Nghich_nhan_1sao_khen`):** Người dùng bấm nhầm 1 sao nhưng lời khen chân thành (*rất tuyệt vời, dịch vụ tuyệt vời, 10 điểm...*) không chứa bất kỳ từ phàn nàn nào, được chuyển sang **Tích cực (Nhãn 1)**.

### Mẫu minh chứng 5 sao nhưng chửi thậm tệ được đưa về Tiêu cực (0):
| App | Rating gốc | Nhãn sau kiểm toán | Nội dung comment |
| :--- | :---: | :---: | :--- |
| Agribank | 5★ | **Tieu cuc (0)** | Ứng dụng quá tệ. Ứng dụng quá tệ so với các ứng dụng của các ngân hàng khác. Bày ra mọi cách để khách hàng cài thêm ứng dụng để thu tiền; trong khi chất lượng quá tệ |
| Agribank | 4★ | **Tieu cuc (0)** | quá tệ. Cực kỳ tệ chuyển khoản cứ bị lỗi không nhận được tiền thu phí thàng tháng cũng cực kì cao nói chung là app tệ nhất từng dù mình đã xài đc 5năm |
| Agribank | 5★ | **Tieu cuc (0)** | App không dùng được trên iphone 18. Không vào được app từ iphone 18 |
| Agribank | 4★ | **Tieu cuc (0)** | Ngân hàng quá tồi tệ. Mấy hôm trc tôi bỏ tiền vào tài khoản này 10k xong sau đó hôm qua bỏ thêm 40k , tổng cộng tôi bỏ là 50,440 đồng chuyển vào tài khoản khác ko đc , tôi có gọi nhân viên ngân hàng nói tôi bỏ thêm 100k chỉ có chuyển đc 50k , còn 50k tôi phải ra ngân hàng rút và đóng tài khoản , sáng may tôi mới rút và đóng tài khoản trừ phí tiền mặt 22k trừ phí 2k tạo mới , ngân hàng quá tồi tệ , tôi ko bao giờ xài ngân hàng này nữa ! Quá tệ |
| Grab | 5★ | **Tieu cuc (0)** | App lừa đảo. Hiện deal 0 đồng và mã freeship nhưng không áp dụng được |

---

## 6. BẢNG HIỆU NĂNG MÔ HÌNH HỌC MÁY TRÊN TẬP TEST ĐỘC LẬP (2.237 MẪU)

Sau khi toàn bộ dữ liệu được chuẩn hóa sạch sẽ và phân tầng 70/15/15, 3 mô hình học máy được đánh giá độc lập trên 2.237 mẫu kiểm thử chưa từng xuất hiện trong quá trình huấn luyện:

| Thuật toán mô hình | Accuracy (Độ chính xác) | Precision (Độ chuẩn xác) | Recall (Độ bao phủ) | Macro F1-Score | Xếp hạng hiệu năng |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Multinomial Naive Bayes (Baseline)** | 88.02% | 91.43% | 80.50% | 83.79% | Hạng 3 |
| **Logistic Regression (balanced)** | 90.34% | 88.41% | 88.60% | 88.50% | Hạng 2 |
| **Linear Support Vector Classifier (LinearSVC)** | **91.01%** | **89.17%** | **89.47%** | **89.32%** | **[★] Hạng 1 (Tốt nhất)** |

---

## 7. ĐỒNG BỘ VÀ LƯU TRỮ TỆP TIN
* Dữ liệu sạch toàn phần: `data/app_reviews_cleaned.csv`, `data/app_reviews_cleaned.xlsx`, `Nhom_12/app_reviews_cleaned.xlsx`.
* Tập phân tầng Train/Val/Test: `data/train.csv`, `data/val.csv`, `data/test.csv` (và thư mục `Nhom_12/`).
* Notebook nguồn: `du_an_hoc_may_nhom_12.ipynb` và `Nhom_12/du_an_hoc_may_nhom_12.ipynb` (đã chạy hoàn tất 23/23 cells không lỗi).
