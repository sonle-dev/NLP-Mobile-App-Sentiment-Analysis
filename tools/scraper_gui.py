# -*- coding: utf-8 -*-
"""
================================================================================
CONG CU CAO DU LIEU DA NANG (WEB & APP SCRAPER) - GIAO DIEN TKINTER
================================================================================
Mo ta:
  Ung dung cao du lieu do hoa (GUI) hoan chinh, truc quan, ho tro:
  1. Google Play Store Reviews (ho tro cao hang nghin ban ghi, phan trang)
  2. Apple App Store Reviews (qua iTunes RSS/Customer Reviews API)
  3. Trang web tin tuc / bai viet co ban (Requests + BeautifulSoup)

Tinh nang chinh:
  - Chon thu muc luu linh hoat bang hop thoai Browse.
  - Tu dong tach Package Name / App ID tu duong dan URL.
  - Tuy chon so luong ban ghi (1000, 3000, 5000+ ban ghi), quoc gia, sap xep, loc sao.
  - Tu dong lam sach du lieu (loai bo rong, loc trung, format ngay gio, phan loai cam xuc).
  - Xuat ra file Excel (.xlsx) hoac CSV (UTF-8-sig chong loi font tieng Viet).
  - Thanh tien trinh (Progress Bar), Nhat ky (Log Console) va nut mo thu muc truc tiep.
  - Chay tren da luong (Multi-threading) khong gay do/treo giao dien.
================================================================================
"""

import os
import re
import sys
import time
import queue
import threading
from datetime import datetime
import urllib.parse

# Giao dien Tkinter
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# Xu ly du lieu & Web Scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Google Play Scraper
try:
    from google_play_scraper import reviews as gp_reviews, Sort as gp_Sort
    HAS_GOOGLE_PLAY = True
except ImportError:
    HAS_GOOGLE_PLAY = False


# ==============================================================================
# 1. CAC HAM TIEN ICH TRICH XUAT & XU LY DU LIEU
# ==============================================================================

def extract_google_play_id(input_str: str) -> str:
    """
    Trich xuat App Package Name tu chuoi nhap vao.
    Ho tro ca dang ID truc tiep (vd: com.shopee.vn) hoac Link URL day du:
    https://play.google.com/store/apps/details?id=com.shopee.vn&hl=vi
    """
    input_str = input_str.strip()
    if not input_str:
        return ""
    # Neu la URL
    if "play.google.com" in input_str:
        parsed = urllib.parse.urlparse(input_str)
        query = urllib.parse.parse_qs(parsed.query)
        if "id" in query and query["id"]:
            return query["id"][0]
    # Neu la chuoi package name thong thuong (vd: com.zing.zalo)
    match = re.search(r'[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)+', input_str)
    if match:
        return match.group(0)
    return input_str


def extract_app_store_id(input_str: str) -> tuple:
    """
    Trich xuat App ID va ma quoc gia (neu co) tu chuoi nhap vao cua Apple App Store.
    Ho tro dang so (vd: 959841449) hoac Link URL:
    https://apps.apple.com/vn/app/10-10-shopee-thuong-hieu/id959841449?l=vi
    Tra ve: (app_id, country_code)
    """
    input_str = input_str.strip()
    if not input_str:
        return "", ""

    country = ""
    # Trich xuat ma quoc gia trong URL (vd: /vn/app/ hoac /us/app/)
    match_country = re.search(r'apple\.com/([a-zA-Z]{2})/', input_str)
    if match_country:
        country = match_country.group(1).lower()

    # Neu dan link co chua id123456789
    match_id = re.search(r'id(\d+)', input_str)
    if match_id:
        return match_id.group(1), country

    # Neu nguoi dung nhap truc tiep day so ID (vd: 959841449)
    digits = re.findall(r'\d+', input_str)
    if digits:
        return digits[0], country

    return input_str, country


def clean_text(text: str) -> str:
    """Lam sach chuoi van ban: chuan hoa khoang trang, loai bo ky tu la."""
    if not text or not isinstance(text, str):
        return ""
    # Thay the nhieu dau cach/xuong dong lien tiep bang 1 dau cach gon gang
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()


def categorize_sentiment(rating: int) -> str:
    """Gan nhan cam xuc so bo dua tren so sao rating."""
    try:
        r = int(rating)
        if r >= 4:
            return "Tích cực (Positive)"
        elif r == 3:
            return "Trung tính (Neutral)"
        else:
            return "Tiêu cực (Negative)"
    except Exception:
        return "Không xác định"


# ==============================================================================
# 2. CAC HAM CAO DU LIEU (SCRAPING ENGINES)
# ==============================================================================

def scrape_google_play_reviews(
    app_id: str,
    target_count: int,
    country: str,
    lang: str,
    sort_type: str,
    filter_score: int,
    stop_event: threading.Event,
    log_queue: queue.Queue,
    progress_queue: queue.Queue
) -> pd.DataFrame:
    """
    Cao danh gia tu Google Play Store theo lo (batch) va phan trang tu dong.
    """
    if not HAS_GOOGLE_PLAY:
        raise ImportError("Chưa cài đặt thư viện 'google-play-scraper'. Vui lòng chạy: pip install google-play-scraper")

    log_queue.put(f"[Google Play] Bắt đầu cào app: '{app_id}' (Mục tiêu: {target_count:,} bản ghi)...")
    
    # Xac dinh kieu sap xep
    sort_enum = gp_Sort.NEWEST if sort_type == "newest" else gp_Sort.MOST_RELEVANT

    all_reviews = []
    continuation_token = None
    batch_size = 200  # Google Play API ho tro tot nhat o khoang 100-200 moi batch
    consecutive_empty = 0

    while len(all_reviews) < target_count and not stop_event.is_set():
        needed = min(batch_size, target_count - len(all_reviews))
        try:
            results, continuation_token = gp_reviews(
                app_id,
                lang=lang,
                country=country,
                sort=sort_enum,
                count=needed,
                filter_score_with=filter_score if filter_score > 0 else None,
                continuation_token=continuation_token
            )
        except Exception as e:
            log_queue.put(f"[Lỗi API Google Play] {str(e)}")
            break

        if not results:
            consecutive_empty += 1
            if consecutive_empty >= 2:
                log_queue.put("[Google Play] Không còn đánh giá nào mới hơn từ Store.")
                break
            time.sleep(1)
            continue
        else:
            consecutive_empty = 0

        # Luu du lieu tu batch
        for r in results:
            content = clean_text(r.get('content', ''))
            score = r.get('score', 0)
            created_at = r.get('at', None)
            created_str = created_at.strftime('%Y-%m-%d %H:%M:%S') if isinstance(created_at, datetime) else str(created_at or '')

            all_reviews.append({
                'review_id': r.get('reviewId', ''),
                'user_name': r.get('userName', 'Ẩn danh'),
                'rating': score,
                'sentiment': categorize_sentiment(score),
                'content': content,
                'thumbs_up': r.get('thumbsUpCount', 0),
                'review_date': created_str,
                'app_version': r.get('reviewCreatedVersion', '') or r.get('appVersion', ''),
                'reply_content': clean_text(r.get('replyContent', '')),
                'replied_at': str(r.get('repliedAt', '') or ''),
                'source': 'Google Play Store'
            })

        current_count = len(all_reviews)
        progress_queue.put((current_count, target_count))
        log_queue.put(f"[Google Play] Đã thu thập: {current_count:,}/{target_count:,} bản ghi...")

        # Neu khong con token tiep theo thi da het toan bo review
        if not continuation_token:
            log_queue.put("[Google Play] Đã tải hết toàn bộ đánh giá có sẵn trên Store.")
            break

        # Gian cach nhe tranh spam rate limit
        time.sleep(0.3)

    if stop_event.is_set():
        log_queue.put("[Cảnh báo] Quá trình cào đã được người dùng dừng lại.")

    df = pd.DataFrame(all_reviews)
    return df


def scrape_app_store_reviews(
    app_id: str,
    target_count: int,
    country: str,
    filter_score: int,
    stop_event: threading.Event,
    log_queue: queue.Queue,
    progress_queue: queue.Queue
) -> pd.DataFrame:
    """
    Cao danh gia tu Apple App Store su dung Catalog Web API hien dai (ho tro phan trang khong gioi han)
    ket hop tra cuu thong tin ung dung qua iTunes Lookup API.
    """
    log_queue.put(f"[Apple App Store] Đang kiểm tra App ID: '{app_id}' tại khu vực '{country.upper()}'...")

    # 1. Tra cuu ten va nha phat trien ung dung tren Store
    app_name = f"App ID {app_id}"
    seller_name = ""
    try:
        lookup_url = f"https://itunes.apple.com/lookup?id={app_id}&country={country}"
        r_lookup = requests.get(lookup_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if r_lookup.status_code == 200:
            lookup_data = r_lookup.json()
            if lookup_data.get('resultCount', 0) > 0:
                res = lookup_data['results'][0]
                app_name = res.get('trackName', app_name)
                seller_name = res.get('sellerName', '')
                log_queue.put(f"[Apple App Store] ✅ Đã tìm thấy: '{app_name}' (Phát triển: {seller_name})")
            else:
                # Thu tim o khu vuc 'us' xem co phai do nguoi dung chon nham khu vuc
                r_us = requests.get(f"https://itunes.apple.com/lookup?id={app_id}&country=us", headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
                if r_us.status_code == 200 and r_us.json().get('resultCount', 0) > 0:
                    res_us = r_us.json()['results'][0]
                    app_name = res_us.get('trackName', app_name)
                    log_queue.put(f"[Gợi ý] Ứng dụng '{app_name}' được tìm thấy tại App Store US, đang tự động chuyển khu vực sang US...")
                    country = 'us'
                else:
                    log_queue.put(f"[Cảnh báo] Không tìm thấy ứng dụng với ID '{app_id}'. Hãy đảm bảo bạn dán đúng link từ App Store (ví dụ: https://apps.apple.com/vn/app/.../id{app_id})")
    except Exception as e:
        log_queue.put(f"[Apple App Store] Ghi chú tra cứu: {e}")

    log_queue.put(f"[Apple App Store] Bắt đầu cào đánh giá: '{app_name}' (Mục tiêu: {target_count:,} bản ghi)...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Origin': 'https://apps.apple.com',
        'Referer': f'https://apps.apple.com/{country}/app/id{app_id}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    all_reviews = []
    offset = 0
    batch_size = 20
    consecutive_empty = 0
    retry_429 = 0

    # 2. Thu thap du lieu qua Catalog API (Modern Web API cua Apple App Store)
    while len(all_reviews) < target_count and not stop_event.is_set():
        url = f"https://apps.apple.com/api/apps/v1/catalog/{country}/apps/{app_id}/reviews"
        params = {
            'platform': 'web',
            'additionalPlatforms': 'appletv,ipad,iphone,mac',
            'limit': batch_size,
            'offset': offset
        }

        try:
            resp = requests.get(url, headers=headers, params=params, timeout=12)
            if resp.status_code == 429:
                retry_429 += 1
                if retry_429 > 3:
                    log_queue.put("[Apple App Store] Máy chủ Apple giới hạn tốc độ. Đang tiếp tục chuyển sang kênh dự phòng...")
                    break
                log_queue.put("[Apple App Store] Đang tạm nghỉ 2 giây theo yêu cầu của Store để tránh giới hạn tốc độ...")
                time.sleep(2)
                continue
            else:
                retry_429 = 0

            if resp.status_code == 404:
                log_queue.put(f"[Apple App Store] HTTP 404: Không tìm thấy trang đánh giá của App '{app_id}' tại '{country}'.")
                break
            if resp.status_code != 200:
                log_queue.put(f"[Apple App Store] Lỗi tải dữ liệu offset {offset} (HTTP {resp.status_code}).")
                break

            data = resp.json()
            items = data.get('data', [])

            if not items:
                consecutive_empty += 1
                if consecutive_empty >= 2:
                    log_queue.put("[Apple App Store] Đã đến trang cuối cùng của đánh giá trên Store.")
                    break
                time.sleep(1)
                continue
            else:
                consecutive_empty = 0

            for item in items:
                attr = item.get('attributes', {})
                rating = int(attr.get('rating', 0))

                if filter_score > 0 and rating != filter_score:
                    continue

                r_id = item.get('id', '')
                author = attr.get('userName', 'Người dùng Apple')
                title = clean_text(attr.get('title', ''))
                body = clean_text(attr.get('review', ''))
                full_content = f"{title}. {body}".strip(" .") if title else body
                date_str = str(attr.get('date', '')).replace('T', ' ').replace('Z', '')

                # Phan hoi tu nha phat trien
                dev_resp = attr.get('developerResponse', {})
                reply_body = clean_text(dev_resp.get('body', '')) if dev_resp else ''
                reply_date = str(dev_resp.get('modified', '')).replace('T', ' ').replace('Z', '') if dev_resp else ''

                all_reviews.append({
                    'review_id': r_id,
                    'user_name': author,
                    'rating': rating,
                    'sentiment': categorize_sentiment(rating),
                    'content': full_content,
                    'thumbs_up': 0,
                    'review_date': date_str,
                    'app_version': '',
                    'reply_content': reply_body,
                    'replied_at': reply_date,
                    'source': f'Apple App Store ({country.upper()})'
                })

                if len(all_reviews) >= target_count:
                    break

            offset += len(items)
            current_count = len(all_reviews)
            progress_queue.put((current_count, target_count))
            log_queue.put(f"[Apple App Store] Đã thu thập: {current_count:,}/{target_count:,} bản ghi...")

            # Neu khong con link next
            if not data.get('next'):
                log_queue.put("[Apple App Store] Đã tải hết toàn bộ đánh giá có sẵn trên Store.")
                break

            time.sleep(0.2)

        except Exception as e:
            log_queue.put(f"[Lỗi Apple App Store] {str(e)}")
            break

    # 3. Phuong thuc du phong qua XML RSS neu Catalog API chua lay duoc ban ghi nao
    if not all_reviews and not stop_event.is_set():
        log_queue.put("[Apple App Store] Đang thử phương thức kết nối dự phòng (RSS Feed)...")
        try:
            xml_url = f"https://itunes.apple.com/{country}/rss/customerreviews/id={app_id}/xml"
            xml_resp = requests.get(xml_url, headers={'User-Agent': 'iTunes/12.11.3 (Windows; Microsoft Windows 10 x64)'}, timeout=10)
            if xml_resp.status_code == 200:
                soup = BeautifulSoup(xml_resp.content, 'xml')
                for e in soup.find_all('entry'):
                    r_tag = e.find('im:rating')
                    if not r_tag:
                        continue
                    rating = int(r_tag.text.strip())
                    if filter_score > 0 and rating != filter_score:
                        continue
                    title = clean_text(e.find('title').text if e.find('title') else '')
                    content = clean_text(e.find('content').text if e.find('content') else '')
                    full_content = f"{title}. {content}".strip(" .") if title else content
                    author = e.find('author').find('name').text if e.find('author') and e.find('author').find('name') else 'Người dùng Apple'
                    all_reviews.append({
                        'review_id': e.find('id').text if e.find('id') else '',
                        'user_name': author,
                        'rating': rating,
                        'sentiment': categorize_sentiment(rating),
                        'content': full_content,
                        'thumbs_up': 0,
                        'review_date': e.find('updated').text.replace('T', ' ').replace('Z', '') if e.find('updated') else '',
                        'app_version': e.find('im:version').text if e.find('im:version') else '',
                        'reply_content': '',
                        'replied_at': '',
                        'source': f'Apple App Store RSS ({country.upper()})'
                    })
                    if len(all_reviews) >= target_count:
                        break
                if all_reviews:
                    progress_queue.put((len(all_reviews), target_count))
                    log_queue.put(f"[Apple App Store RSS] Đã thu thập: {len(all_reviews):,} bản ghi từ kênh dự phòng.")
        except Exception as ex_rss:
            log_queue.put(f"[Lỗi RSS dự phòng] {ex_rss}")

    if stop_event.is_set():
        log_queue.put("[Cảnh báo] Quá trình cào đã được dừng lại.")

    return pd.DataFrame(all_reviews)


def scrape_generic_website(
    url: str,
    target_count: int,
    stop_event: threading.Event,
    log_queue: queue.Queue,
    progress_queue: queue.Queue
) -> pd.DataFrame:
    """
    Cao bai viet, tieu de, doan van va lien ket tu mot trang web thong thuong.
    """
    log_queue.put(f"[Web Scraper] Bắt đầu cào trang: '{url}'...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.encoding = resp.apparent_encoding or 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
    except Exception as e:
        log_queue.put(f"[Lỗi truy cập Web] {str(e)}")
        return pd.DataFrame()

    items = []
    # 1. Tim cac tieu de h1, h2, h3 va the bai viet
    headings = soup.find_all(['h1', 'h2', 'h3', 'p', 'article', 'li'])
    log_queue.put(f"[Web Scraper] Đã phân tích DOM, tìm thấy {len(headings):,} thẻ nội dung.")

    seen_texts = set()
    for tag in headings:
        if stop_event.is_set():
            break
        text = clean_text(tag.get_text())
        # Bo qua chuoi qua ngan (< 25 ky tu) hoac trung lap
        if len(text) < 25 or text in seen_texts:
            continue
        seen_texts.add(text)

        link = ""
        a_tag = tag.find('a') if tag.name != 'a' else tag
        if a_tag and a_tag.get('href'):
            link = urllib.parse.urljoin(url, a_tag.get('href'))

        items.append({
            'review_id': f"web_{len(items)+1}",
            'user_name': tag.name.upper(),
            'rating': 5,
            'sentiment': 'Thông tin web',
            'content': text,
            'thumbs_up': 0,
            'review_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'app_version': link,
            'reply_content': '',
            'replied_at': '',
            'source': f"Web: {urllib.parse.urlparse(url).netloc}"
        })

        if len(items) % 50 == 0:
            progress_queue.put((len(items), target_count))
            log_queue.put(f"[Web Scraper] Đã thu thập {len(items):,} khối nội dung...")

        if len(items) >= target_count:
            break

    progress_queue.put((len(items), target_count))
    log_queue.put(f"[Web Scraper] Hoàn thành cào {len(items):,} dòng dữ liệu từ web.")
    return pd.DataFrame(items)


# ==============================================================================
# 3. HAM LAM SACH VA LUU DU LIEU
# ==============================================================================

def clean_and_process_dataframe(df: pd.DataFrame, log_queue: queue.Queue) -> pd.DataFrame:
    """
    Lam sach du lieu tho:
    - Loai bo hang rong, null
    - Loc trung theo review_id hoac noi dung
    - Chuan hoa kieu du lieu rating va ngay thang
    """
    if df.empty:
        return df

    initial_len = len(df)

    # 1. Loai bo cac dong co noi dung rong
    df['content'] = df['content'].astype(str).str.strip()
    df = df[df['content'].str.len() > 0].copy()

    # 2. Xoa cac ban ghi trung lap (neu co review_id hoac trung 100% noi dung)
    if 'review_id' in df.columns:
        df.drop_duplicates(subset=['review_id'], keep='first', inplace=True)
    df.drop_duplicates(subset=['content'], keep='first', inplace=True)

    # 3. Chuan hoa cot rating
    if 'rating' in df.columns:
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0).astype(int)

    cleaned_len = len(df)
    removed = initial_len - cleaned_len
    if removed > 0:
        log_queue.put(f"[Làm sạch] Đã lọc bỏ {removed:,} bản ghi rác/trùng lặp. Còn lại {cleaned_len:,} bản ghi chuẩn.")
    else:
        log_queue.put(f"[Làm sạch] Dữ liệu hoàn toàn sạch sẽ ({cleaned_len:,} bản ghi hợp lệ).")

    # Thong ke phan bo so sao truc quan
    if 'rating' in df.columns and cleaned_len > 0:
        counts = df['rating'].value_counts().to_dict()
        log_queue.put("[Thống kê số sao thu thập]:")
        for star in [5, 4, 3, 2, 1]:
            cnt = counts.get(star, 0)
            pct = (cnt / cleaned_len) * 100
            log_queue.put(f"   ⭐ {star} sao: {cnt:,} dòng ({pct:.1f}%)")

    return df


def export_dataframe(
    df: pd.DataFrame,
    save_dir: str,
    base_name: str,
    export_format: str,
    log_queue: queue.Queue
) -> list:
    """
    Xuat DataFrame ra file .csv (UTF-8-sig chong loi font Excel) hoac .xlsx
    """
    saved_files = []
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_base = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', base_name)[:60]

    # Xuat Excel (.xlsx)
    if export_format in ["xlsx", "both"]:
        file_path_xlsx = os.path.join(save_dir, f"{clean_base}_{timestamp}.xlsx")
        try:
            with pd.ExcelWriter(file_path_xlsx, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Data_Scraped')
            saved_files.append(file_path_xlsx)
            log_queue.put(f"[Xuất file] Đã tạo file Excel: {file_path_xlsx}")
        except Exception as e:
            log_queue.put(f"[Lỗi xuất Excel] {str(e)}. Tự động chuyển hướng sang CSV...")
            export_format = "csv"

    # Xuat CSV (UTF-8 co BOM chong loi tieng Viet tren Microsoft Excel)
    if export_format in ["csv", "both"]:
        file_path_csv = os.path.join(save_dir, f"{clean_base}_{timestamp}.csv")
        try:
            df.to_csv(file_path_csv, index=False, encoding='utf-8-sig')
            saved_files.append(file_path_csv)
            log_queue.put(f"[Xuất file] Đã tạo file CSV (UTF-8-sig): {file_path_csv}")
        except Exception as e:
            log_queue.put(f"[Lỗi xuất CSV] {str(e)}")

    return saved_files


# ==============================================================================
# 4. GIAO DIEN DO HOA NGUOI DUNG (TKINTER GUI)
# ==============================================================================

class ScraperGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Cong Cu Cao Du Lieu Da Nang (Google Play, App Store & Web) - GUI")
        self.root.geometry("960x780")
        self.root.minsize(860, 680)

        # Hang doi giao tiep giua luong cao du lieu va giao dien GUI
        self.log_queue = queue.Queue()
        self.progress_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.scraping_thread = None
        self.last_saved_dir = os.path.abspath(os.getcwd())

        # Thiet lap phong cach giao dien (Theme)
        self.setup_styles()

        # Xay dung cac thanh phan giao dien
        self.create_widgets()

        # Bat dau vong lap kiem tra hang doi nhat ky
        self.root.after(100, self.process_queues)

    def setup_styles(self):
        """Cau hinh mau sac, phong chu va kieu dang ttk truc quan, hien dai."""
        self.style = ttk.Style()
        try:
            self.style.theme_use('clam')
        except Exception:
            pass

        # Mau sac chu dao
        self.COLOR_BG = "#f8fafc"          # Nen xam nhat hien dai
        self.COLOR_CARD = "#ffffff"        # Nen card trang
        self.COLOR_PRIMARY = "#2563eb"     # Xanh duong dam
        self.COLOR_SUCCESS = "#16a34a"     # Xanh la cay thanh cong
        self.COLOR_DANGER = "#dc2626"      # Do huy
        self.COLOR_TEXT = "#0f172a"        # Chu den xam dam
        self.COLOR_MUTED = "#64748b"       # Chu phu mau xam

        self.root.configure(bg=self.COLOR_BG)

        # Style chung cho Label, Frame
        self.style.configure(".", background=self.COLOR_BG, foreground=self.COLOR_TEXT, font=("Segoe UI", 10))
        self.style.configure("Card.TFrame", background=self.COLOR_CARD, relief="groove")
        self.style.configure("Header.TLabel", font=("Segoe UI", 15, "bold"), foreground="#1e3a8a", background=self.COLOR_BG)
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 9), foreground=self.COLOR_MUTED, background=self.COLOR_BG)
        self.style.configure("Section.TLabel", font=("Segoe UI", 10, "bold"), foreground="#1e293b", background=self.COLOR_CARD)
        
        # Style cho cac nut bam
        self.style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background=self.COLOR_PRIMARY, foreground="#ffffff")
        self.style.map("Primary.TButton", background=[('active', '#1d4ed8'), ('disabled', '#94a3b8')])

        self.style.configure("Danger.TButton", font=("Segoe UI", 10, "bold"), background=self.COLOR_DANGER, foreground="#ffffff")
        self.style.map("Danger.TButton", background=[('active', '#b91c1c'), ('disabled', '#cbd5e1')])

        self.style.configure("Success.TButton", font=("Segoe UI", 10, "bold"), background=self.COLOR_SUCCESS, foreground="#ffffff")
        self.style.map("Success.TButton", background=[('active', '#15803d')])

    def create_widgets(self):
        """Khoi tao toan bo cac phan tu tren cua so ung dung."""
        # --- 1. TIEU DE UNG DUNG ---
        header_frame = ttk.Frame(self.root, padding="15 10 15 5")
        header_frame.pack(fill="x")

        title_lbl = ttk.Label(
            header_frame,
            text="🚀 CÔNG CỤ CÀO DỮ LIỆU ĐA NĂNG (WEB & APP REVIEWS)",
            style="Header.TLabel"
        )
        title_lbl.pack(anchor="w")

        sub_lbl = ttk.Label(
            header_frame,
            text="Thu thập hàng ngàn đánh giá từ Google Play Store, App Store hoặc nội dung website. Tự động làm sạch & xuất Excel / CSV chuẩn Tiếng Việt.",
            style="SubHeader.TLabel"
        )
        sub_lbl.pack(anchor="w", pady=(2, 0))

        # --- 2. CARD CAU HINH DAU VAO ---
        input_card = ttk.Frame(self.root, padding=15, style="Card.TFrame")
        input_card.pack(fill="x", padx=15, pady=8)

        # Dong 1: Chon Nguon du lieu
        row1 = ttk.Frame(input_card, style="Card.TFrame")
        row1.pack(fill="x", pady=4)
        
        ttk.Label(row1, text="Nguồn dữ liệu:", style="Section.TLabel", width=18).pack(side="left")
        self.source_var = tk.StringVar(value="google_play")
        
        rb1 = ttk.Radiobutton(
            row1, text="Google Play Store", value="google_play",
            variable=self.source_var, command=self.on_source_change
        )
        rb1.pack(side="left", padx=10)
        
        rb2 = ttk.Radiobutton(
            row1, text="Apple App Store", value="app_store",
            variable=self.source_var, command=self.on_source_change
        )
        rb2.pack(side="left", padx=10)

        rb3 = ttk.Radiobutton(
            row1, text="Trang Web thông thường (URL)", value="web",
            variable=self.source_var, command=self.on_source_change
        )
        rb3.pack(side="left", padx=10)

        # Dong 2: Nhap Link hoac App ID
        row2 = ttk.Frame(input_card, style="Card.TFrame")
        row2.pack(fill="x", pady=6)

        self.lbl_target = ttk.Label(row2, text="Package Name / Link:", style="Section.TLabel", width=18)
        self.lbl_target.pack(side="left")

        self.target_entry = ttk.Entry(row2, font=("Segoe UI", 10))
        self.target_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.target_entry.insert(0, "com.shopee.vn")

        # Nut vi du nhanh
        self.btn_example = ttk.Button(row2, text="Mẫu thử", command=self.fill_example, width=9)
        self.btn_example.pack(side="right")

        self.lbl_hint = ttk.Label(
            input_card,
            text="Gợi ý: Nhập Package Name (ví dụ: com.shopee.vn, com.zing.zalo) hoặc dán link Google Play đầy đủ.",
            font=("Segoe UI", 8, "italic"), foreground=self.COLOR_MUTED, background=self.COLOR_CARD
        )
        self.lbl_hint.pack(anchor="w", padx=(145, 0), pady=(0, 6))

        # Dong 3: So luong ban ghi, Quoc gia, Sap xep, Loc sao
        row3 = ttk.Frame(input_card, style="Card.TFrame")
        row3.pack(fill="x", pady=6)

        # So luong
        ttk.Label(row3, text="Số lượng:", style="Section.TLabel", width=10).pack(side="left")
        self.count_combobox = ttk.Combobox(
            row3, values=["500", "1000", "2000", "3000", "5000", "10000", "20000"],
            width=8, font=("Segoe UI", 10)
        )
        self.count_combobox.set("1000")
        self.count_combobox.pack(side="left", padx=(0, 15))

        # Quoc gia
        ttk.Label(row3, text="Quốc gia:", style="Section.TLabel").pack(side="left")
        self.country_combobox = ttk.Combobox(
            row3, values=["vn (Việt Nam)", "us (Hoa Kỳ)", "kr (Hàn Quốc)", "jp (Nhật Bản)", "sg (Singapore)"],
            width=13, state="readonly", font=("Segoe UI", 9)
        )
        self.country_combobox.set("vn (Việt Nam)")
        self.country_combobox.pack(side="left", padx=(5, 15))

        # Sap xep
        ttk.Label(row3, text="Sắp xếp:", style="Section.TLabel").pack(side="left")
        self.sort_combobox = ttk.Combobox(
            row3, values=["Mới nhất (Newest)", "Liên quan nhất (Most Relevant)"],
            width=18, state="readonly", font=("Segoe UI", 9)
        )
        self.sort_combobox.set("Mới nhất (Newest)")
        self.sort_combobox.pack(side="left", padx=(5, 15))

        # Loc sao
        ttk.Label(row3, text="Lọc số sao:", style="Section.TLabel").pack(side="left")
        self.star_combobox = ttk.Combobox(
            row3, values=[
                "Tất cả (1 - 5 sao)",
                "Chỉ 1 sao (Rất tệ)",
                "Chỉ 2 sao",
                "Chỉ 3 sao",
                "Chỉ 4 sao",
                "Chỉ 5 sao (Tốt)"
            ],
            width=17, state="readonly", font=("Segoe UI", 9)
        )
        self.star_combobox.set("Tất cả (1 - 5 sao)")
        self.star_combobox.pack(side="left", padx=5)

        # Dong 4: Thu muc luu ket qua & Dinh dang xuat
        row4 = ttk.Frame(input_card, style="Card.TFrame")
        row4.pack(fill="x", pady=6)

        ttk.Label(row4, text="Thư mục lưu:", style="Section.TLabel", width=18).pack(side="left")
        self.save_dir_entry = ttk.Entry(row4, font=("Segoe UI", 10))
        self.save_dir_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.save_dir_entry.insert(0, self.last_saved_dir)

        btn_browse = ttk.Button(row4, text="📁 Chọn thư mục...", command=self.browse_folder)
        btn_browse.pack(side="left", padx=(0, 15))

        # Dinh dang file
        ttk.Label(row4, text="Định dạng:", style="Section.TLabel").pack(side="left")
        self.format_combobox = ttk.Combobox(
            row4, values=["Excel (.xlsx)", "CSV (UTF-8-sig)", "Cả hai (.xlsx & .csv)"],
            width=18, state="readonly", font=("Segoe UI", 9)
        )
        self.format_combobox.set("Excel (.xlsx)")
        self.format_combobox.pack(side="left", padx=5)

        # --- 3. KHU VUC DIEU KHIEN & TIEN TRINH ---
        action_frame = ttk.Frame(self.root, padding="15 5 15 5")
        action_frame.pack(fill="x")

        self.btn_start = ttk.Button(
            action_frame, text="▶ BẮT ĐẦU CÀO DỮ LIỆU",
            style="Primary.TButton", command=self.start_scraping
        )
        self.btn_start.pack(side="left", ipadx=12, ipady=4, padx=(0, 10))

        self.btn_stop = ttk.Button(
            action_frame, text="⏹ DỪNG LẠI",
            style="Danger.TButton", command=self.stop_scraping, state="disabled"
        )
        self.btn_stop.pack(side="left", ipadx=8, ipady=4, padx=(0, 10))

        self.btn_open_folder = ttk.Button(
            action_frame, text="📂 MỞ THƯ MỤC LƯU",
            command=self.open_output_folder
        )
        self.btn_open_folder.pack(side="left", ipadx=8, ipady=4)

        # Nhan trang thai tom tat
        self.status_lbl = ttk.Label(action_frame, text="Sẵn sàng thực hiện.", font=("Segoe UI", 9, "bold"), foreground="#0369a1")
        self.status_lbl.pack(side="right", padx=10)

        # Thanh tien trinh
        progress_frame = ttk.Frame(self.root, padding="15 4 15 6")
        progress_frame.pack(fill="x")

        self.progress_bar = ttk.Progressbar(progress_frame, mode="determinate")
        self.progress_bar.pack(fill="x")

        # --- 4. NHAT KY HOAT DONG (LOG CONSOLE) ---
        log_frame = ttk.LabelFrame(self.root, text=" 📜 Nhật ký hoạt động & Trạng thái chi tiết ", padding=8)
        log_frame.pack(fill="both", expand=True, padx=15, pady=(4, 15))

        self.log_text = ScrolledText(
            log_frame, wrap="word", font=("Consolas", 9),
            bg="#1e1e1e", fg="#e2e8f0", insertbackground="#ffffff"
        )
        self.log_text.pack(fill="both", expand=True)

        # Ghi log chao mung ban dau
        self.log(f"[{datetime.now().strftime('%H:%M:%S')}] Công cụ đã sẵn sàng. Nhập thông tin và bấm 'BẮT ĐẦU CÀO DỮ LIỆU'...")

    # ==========================================================================
    # CAC SU KIEN TUONG TAC GIAO DIEN
    # ==========================================================================

    def on_source_change(self):
        """Thay doi nhan va goi y khi nguoi dung chuyen nguon du lieu."""
        src = self.source_var.get()
        if src == "google_play":
            self.lbl_target.config(text="Package Name / Link:")
            self.lbl_hint.config(text="Gợi ý: Nhập Package Name (ví dụ: com.shopee.vn, com.spotify.music) hoặc dán link Google Play.")
            self.star_combobox.config(state="readonly")
        elif src == "app_store":
            self.lbl_target.config(text="App ID / Link:")
            self.lbl_hint.config(text="Gợi ý: Dán thẳng link App Store (vd: https://apps.apple.com/vn/app/.../id959841449) hoặc nhập ID (vd: 959841449 cho Shopee).")
            self.star_combobox.config(state="readonly")
        else:
            self.lbl_target.config(text="Đường dẫn Web (URL):")
            self.lbl_hint.config(text="Gợi ý: Dán URL bài viết hoặc chuyên mục (ví dụ: https://vnexpress.net/thoi-su).")
            self.star_combobox.config(state="disabled")

    def fill_example(self):
        """Dien du lieu mau nhanh de nguoi dung thu nghiem ngay."""
        src = self.source_var.get()
        if src == "google_play":
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, "com.shopee.vn")
            self.count_combobox.set("1000")
        elif src == "app_store":
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, "https://apps.apple.com/vn/app/10-10-shopee-thương-hiệu/id959841449")
            self.count_combobox.set("1000")
        else:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, "https://vnexpress.net/thoi-su")
            self.count_combobox.set("500")

    def browse_folder(self):
        """Mo hop thoai chon thu muc luu tru."""
        chosen = filedialog.askdirectory(initialdir=self.save_dir_entry.get().strip() or os.getcwd())
        if chosen:
            self.save_dir_entry.delete(0, tk.END)
            self.save_dir_entry.insert(0, chosen)
            self.last_saved_dir = chosen

    def open_output_folder(self):
        """Mo thu muc luu tru tren Windows Explorer."""
        target_dir = self.save_dir_entry.get().strip() or os.getcwd()
        if os.path.exists(target_dir):
            try:
                os.startfile(target_dir)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể mở thư mục: {e}")
        else:
            messagebox.showwarning("Cảnh báo", "Thư mục chưa tồn tại trên máy tính!")

    def log(self, message: str):
        """Them dong chu vao man hinh console."""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def process_queues(self):
        """Lang nghe hang doi tu luong cao du lieu de cap nhat UI muot ma."""
        # 1. Cap nhat Log
        while not self.log_queue.empty():
            try:
                msg = self.log_queue.get_nowait()
                self.log(msg)
            except queue.Empty:
                break

        # 2. Cap nhat Progress Bar
        while not self.progress_queue.empty():
            try:
                current, total = self.progress_queue.get_nowait()
                if total > 0:
                    percent = min(100.0, (current / total) * 100)
                    self.progress_bar['value'] = percent
                    self.status_lbl.config(text=f"Đang cào: {current:,}/{total:,} ({percent:.1f}%)")
            except queue.Empty:
                break

        self.root.after(100, self.process_queues)

    # ==========================================================================
    # QUAN LY TIEN TRINH CAO DU LIEU (THREADING & CONTROLLER)
    # ==========================================================================

    def start_scraping(self):
        """Khoi dong luong cao du lieu."""
        raw_target = self.target_entry.get().strip()
        if not raw_target:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Link, Package Name hoặc App ID!")
            return

        # Kiem tra so luong
        try:
            target_count = int(self.count_combobox.get().replace(",", "").replace(".", "").strip())
            if target_count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Lỗi số lượng", "Số lượng bản ghi phải là một số nguyên dương (ví dụ: 1000)!")
            return

        save_dir = self.save_dir_entry.get().strip() or os.getcwd()

        # Xac dinh dinh dang xuat
        fmt_choice = self.format_combobox.get()
        if "Excel" in fmt_choice:
            export_format = "xlsx"
        elif "CSV" in fmt_choice:
            export_format = "csv"
        else:
            export_format = "both"

        # Lay thong so loc sao
        star_str = self.star_combobox.get().strip()
        filter_star = 0
        if "Tất cả" in star_str:
            filter_star = 0  # 0 nghia la cao tat ca cac muc sao tu 1 den 5 sao
        else:
            match_star = re.search(r'(\d+)\s*sao', star_str)
            if match_star:
                filter_star = int(match_star.group(1))

        # Lay kieu sap xep
        sort_choice = self.sort_combobox.get()
        sort_type = "most_relevant" if "Liên quan" in sort_choice else "newest"

        # Lay thong so quoc gia
        country_code = self.country_combobox.get().split()[0].strip()

        # Thiet lap trang thai giao dien khi dang chay
        self.stop_event.clear()
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        self.progress_bar['value'] = 0
        self.status_lbl.config(text="Đang kết nối & cào dữ liệu...", foreground=self.COLOR_PRIMARY)

        # Chay trong luong rieng de tranh lam do ung dung Tkinter
        self.scraping_thread = threading.Thread(
            target=self._worker_scrape,
            args=(
                self.source_var.get(),
                raw_target,
                target_count,
                country_code,
                filter_star,
                sort_type,
                save_dir,
                export_format
            ),
            daemon=True
        )
        self.scraping_thread.start()

    def stop_scraping(self):
        """Gui tin hieu dung cao du lieu."""
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn dừng quá trình cào? Dữ liệu đã cào được sẽ vẫn được lưu lại."):
            self.stop_event.set()
            self.log_queue.put("[Yêu cầu dừng] Đang lưu lại các dữ liệu đã thu thập được...")
            self.btn_stop.config(state="disabled")

    def _worker_scrape(
        self,
        source_type: str,
        raw_target: str,
        target_count: int,
        country: str,
        filter_star: int,
        sort_type: str,
        save_dir: str,
        export_format: str
    ):
        """Ham thuc thi trong luong nen (Background Worker Thread)."""
        start_time = time.time()
        base_name = "scraped_data"

        try:
            # 1. Thu thap du lieu theo nguon
            if source_type == "google_play":
                app_id = extract_google_play_id(raw_target)
                base_name = f"google_play_{app_id}"
                df = scrape_google_play_reviews(
                    app_id=app_id,
                    target_count=target_count,
                    country=country,
                    lang='vi' if country == 'vn' else 'en',
                    sort_type=sort_type,
                    filter_score=filter_star,
                    stop_event=self.stop_event,
                    log_queue=self.log_queue,
                    progress_queue=self.progress_queue
                )

            elif source_type == "app_store":
                app_id, detected_country = extract_app_store_id(raw_target)
                actual_country = detected_country if detected_country else country
                base_name = f"app_store_{app_id}"
                df = scrape_app_store_reviews(
                    app_id=app_id,
                    target_count=target_count,
                    country=actual_country,
                    filter_score=filter_star,
                    stop_event=self.stop_event,
                    log_queue=self.log_queue,
                    progress_queue=self.progress_queue
                )

            else:  # Trang Web thong thuong
                url = raw_target if raw_target.startswith("http") else f"https://{raw_target}"
                domain = urllib.parse.urlparse(url).netloc
                base_name = f"web_{domain}"
                df = scrape_generic_website(
                    url=url,
                    target_count=target_count,
                    stop_event=self.stop_event,
                    log_queue=self.log_queue,
                    progress_queue=self.progress_queue
                )

            # 2. Xu ly & Lam sach du lieu
            if df.empty:
                self.log_queue.put("[Cảnh báo] Không tìm thấy dữ liệu nào phù hợp với yêu cầu.")
                self.root.after(0, lambda: messagebox.showwarning("Kết quả rỗng", "Không tìm thấy dữ liệu nào. Vui lòng kiểm tra lại Link/ID hoặc kết nối mạng!"))
            else:
                df = clean_and_process_dataframe(df, self.log_queue)
                
                # 3. Xuat file ket qua
                saved_files = export_dataframe(df, save_dir, base_name, export_format, self.log_queue)

                elapsed = round(time.time() - start_time, 2)
                success_msg = f"ĐÃ HOÀN THÀNH!\n- Thu thập: {len(df):,} bản ghi\n- Thời gian: {elapsed} giây\n- Thư mục lưu: {save_dir}"
                self.log_queue.put("=" * 60)
                self.log_queue.put(f"[Thành công] {success_msg.replace(chr(10), ' | ')}")
                self.log_queue.put("=" * 60)

                # Hien thi popup thong bao thanh cong
                self.root.after(0, lambda: messagebox.showinfo("Cào dữ liệu thành công!", success_msg))

        except Exception as e:
            self.log_queue.put(f"[Lỗi ngoại lệ] {str(e)}")
            self.root.after(0, lambda err=str(e): messagebox.showerror("Lỗi thực thi", f"Đã xảy ra lỗi:\n{err}"))

        finally:
            # Khoi phuc trang thai nut bam tren giao dien
            self.root.after(0, self._reset_ui_after_scraping)

    def _reset_ui_after_scraping(self):
        """Khoi phuc trang thai giao dien sau khi luong cao hoan tat."""
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled")
        self.status_lbl.config(text="Đã hoàn thành công việc.", foreground=self.COLOR_SUCCESS)
        self.progress_bar['value'] = 100


# ==============================================================================
# 5. DIEM KHOI CHAY CHUONG TRINH (MAIN ENTRY)
# ==============================================================================

def main():
    # Ho tro hien thi sac net tren man hinh do phan giai cao (High DPI) cua Windows
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    root = tk.Tk()
    app = ScraperGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
