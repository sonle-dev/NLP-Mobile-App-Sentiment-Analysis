# -*- coding: utf-8 -*-
"""
================================================================================
CÔNG CỤ CÀO DỮ LIỆU ĐA NĂNG (WEB & APP SCRAPER) - GIAO DIỆN TKINTER
================================================================================
Mô tả:
  Ứng dụng cào dữ liệu đồ họa (GUI) hoàn chỉnh, trực quan, hỗ trợ:
  1. Google Play Store Reviews (hỗ trợ cào hàng nghìn bản ghi, phân trang)
  2. Apple App Store Reviews (qua iTunes RSS/Customer Reviews API)
  3. Trang web tin tức / bài viết cơ bản (Requests + BeautifulSoup)

Tính năng chính:
  - Chọn thư mục lưu linh hoạt bằng hộp thoại Browse.
  - Tự động tách Package Name / App ID từ đường dẫn URL.
  - Tùy chọn số lượng bản ghi (1000, 3000, 5000+ bản ghi), quốc gia, sắp xếp, lọc sao.
  - Tự động làm sạch dữ liệu (loại bỏ rỗng, lọc trùng, format ngày giờ, phân loại cảm xúc).
  - Xuất ra file Excel (.xlsx) hoặc CSV (UTF-8-sig chống lỗi font tiếng Việt).
  - Thanh tiến trình (Progress Bar), Nhật ký (Log Console) và nút mở thư mục trực tiếp.
  - Chạy trên đa luồng (Multi-threading) không gây đơ/treo giao diện.
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

# Giao diện Tkinter
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# Xử lý dữ liệu & Web Scraping
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
# 1. CÁC HÀM TIỆN ÍCH TRÍCH XUẤT & XỬ LÝ DỮ LIỆU
# ==============================================================================

def extract_google_play_id(input_str: str) -> str:
    """
    Trích xuất App Package Name từ chuỗi nhập vào.
    Hỗ trợ cả dạng ID trực tiếp (vd: com.shopee.vn) hoặc Link URL đầy đủ:
    https://play.google.com/store/apps/details?id=com.shopee.vn&hl=vi
    """
    input_str = input_str.strip()
    if not input_str:
        return ""
    # Nếu là URL
    if "play.google.com" in input_str:
        parsed = urllib.parse.urlparse(input_str)
        query = urllib.parse.parse_qs(parsed.query)
        if "id" in query and query["id"]:
            return query["id"][0]
    # Nếu là chuỗi package name thông thường (vd: com.zing.zalo)
    match = re.search(r'[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)+', input_str)
    if match:
        return match.group(0)
    return input_str


def extract_app_store_id(input_str: str) -> tuple:
    """
    Trích xuất App ID và mã quốc gia (nếu có) từ chuỗi nhập vào của Apple App Store.
    Hỗ trợ dạng số (vd: 959841449) hoặc Link URL:
    https://apps.apple.com/vn/app/10-10-shopee-thương-hiệu/id959841449?l=vi
    Trả về: (app_id, country_code)
    """
    input_str = input_str.strip()
    if not input_str:
        return "", ""

    country = ""
    # Trích xuất mã quốc gia trong URL (vd: /vn/app/ hoặc /us/app/)
    match_country = re.search(r'apple\.com/([a-zA-Z]{2})/', input_str)
    if match_country:
        country = match_country.group(1).lower()

    # Nếu dán link có chứa id123456789
    match_id = re.search(r'id(\d+)', input_str)
    if match_id:
        return match_id.group(1), country

    # Nếu người dùng nhập trực tiếp dãy số ID (vd: 959841449)
    digits = re.findall(r'\d+', input_str)
    if digits:
        return digits[0], country

    return input_str, country


def clean_text(text: str) -> str:
    """Làm sạch chuỗi văn bản: chuẩn hóa khoảng trắng, loại bỏ ký tự lạ."""
    if not text or not isinstance(text, str):
        return ""
    # Thay thế nhiều dấu cách/xuống dòng liên tiếp bằng 1 dấu cách gọn gàng
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()


def categorize_sentiment(rating: int) -> str:
    """Gán nhãn cảm xúc sơ bộ dựa trên số sao rating."""
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
# 2. CÁC HÀM CÀO DỮ LIỆU (SCRAPING ENGINES)
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
    Cào đánh giá từ Google Play Store theo lô (batch) và phân trang tự động.
    """
    if not HAS_GOOGLE_PLAY:
        raise ImportError("Chưa cài đặt thư viện 'google-play-scraper'. Vui lòng chạy: pip install google-play-scraper")

    log_queue.put(f"[Google Play] Bắt đầu cào app: '{app_id}' (Mục tiêu: {target_count:,} bản ghi)...")
    
    # Xác định kiểu sắp xếp
    sort_enum = gp_Sort.NEWEST if sort_type == "newest" else gp_Sort.MOST_RELEVANT

    all_reviews = []
    continuation_token = None
    batch_size = 200  # Google Play API hỗ trợ tốt nhất ở khoảng 100-200 mỗi batch
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

        # Lưu dữ liệu từ batch
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

        # Nếu không còn token tiếp theo thì đã hết toàn bộ review
        if not continuation_token:
            log_queue.put("[Google Play] Đã tải hết toàn bộ đánh giá có sẵn trên Store.")
            break

        # Giãn cách nhẹ tránh spam rate limit
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
    Cào đánh giá từ Apple App Store sử dụng Catalog Web API hiện đại (hỗ trợ phân trang không giới hạn)
    kết hợp tra cứu thông tin ứng dụng qua iTunes Lookup API.
    """
    log_queue.put(f"[Apple App Store] Đang kiểm tra App ID: '{app_id}' tại khu vực '{country.upper()}'...")

    # 1. Tra cứu tên và nhà phát triển ứng dụng trên Store
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
                # Thử tìm ở khu vực 'us' xem có phải do người dùng chọn nhầm khu vực
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

    # 2. Thu thập dữ liệu qua Catalog API (Modern Web API của Apple App Store)
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

                # Phản hồi từ nhà phát triển
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

            # Nếu không còn link next
            if not data.get('next'):
                log_queue.put("[Apple App Store] Đã tải hết toàn bộ đánh giá có sẵn trên Store.")
                break

            time.sleep(0.2)

        except Exception as e:
            log_queue.put(f"[Lỗi Apple App Store] {str(e)}")
            break

    # 3. Phương thức dự phòng qua XML RSS nếu Catalog API chưa lấy được bản ghi nào
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
    Cào bài viết, tiêu đề, đoạn văn và liên kết từ một trang web thông thường.
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
    # 1. Tìm các tiêu đề h1, h2, h3 và thẻ bài viết
    headings = soup.find_all(['h1', 'h2', 'h3', 'p', 'article', 'li'])
    log_queue.put(f"[Web Scraper] Đã phân tích DOM, tìm thấy {len(headings):,} thẻ nội dung.")

    seen_texts = set()
    for tag in headings:
        if stop_event.is_set():
            break
        text = clean_text(tag.get_text())
        # Bỏ qua chuỗi quá ngắn (< 25 ký tự) hoặc trùng lặp
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
# 3. HÀM LÀM SẠCH VÀ LƯU DỮ LIỆU
# ==============================================================================

def clean_and_process_dataframe(df: pd.DataFrame, log_queue: queue.Queue) -> pd.DataFrame:
    """
    Làm sạch dữ liệu thô:
    - Loại bỏ hàng rỗng, null
    - Lọc trùng theo review_id hoặc nội dung
    - Chuẩn hóa kiểu dữ liệu rating và ngày tháng
    """
    if df.empty:
        return df

    initial_len = len(df)

    # 1. Loại bỏ các dòng có nội dung rỗng
    df['content'] = df['content'].astype(str).str.strip()
    df = df[df['content'].str.len() > 0].copy()

    # 2. Xóa các bản ghi trùng lặp (nếu có review_id hoặc trùng 100% nội dung)
    if 'review_id' in df.columns:
        df.drop_duplicates(subset=['review_id'], keep='first', inplace=True)
    df.drop_duplicates(subset=['content'], keep='first', inplace=True)

    # 3. Chuẩn hóa cột rating
    if 'rating' in df.columns:
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0).astype(int)

    cleaned_len = len(df)
    removed = initial_len - cleaned_len
    if removed > 0:
        log_queue.put(f"[Làm sạch] Đã lọc bỏ {removed:,} bản ghi rác/trùng lặp. Còn lại {cleaned_len:,} bản ghi chuẩn.")
    else:
        log_queue.put(f"[Làm sạch] Dữ liệu hoàn toàn sạch sẽ ({cleaned_len:,} bản ghi hợp lệ).")

    # Thống kê phân bố số sao trực quan
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
    Xuất DataFrame ra file .csv (UTF-8-sig chống lỗi font Excel) hoặc .xlsx
    """
    saved_files = []
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_base = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', base_name)[:60]

    # Xuất Excel (.xlsx)
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

    # Xuất CSV (UTF-8 có BOM chống lỗi tiếng Việt trên Microsoft Excel)
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
# 4. GIAO DIỆN ĐỒ HỌA NGƯỜI DÙNG (TKINTER GUI)
# ==============================================================================

class ScraperGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Công Cụ Cào Dữ Liệu Đa Năng (Google Play, App Store & Web) - GUI")
        self.root.geometry("960x780")
        self.root.minsize(860, 680)

        # Hàng đợi giao tiếp giữa luồng cào dữ liệu và giao diện GUI
        self.log_queue = queue.Queue()
        self.progress_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.scraping_thread = None
        self.last_saved_dir = os.path.abspath(os.getcwd())

        # Thiết lập phong cách giao diện (Theme)
        self.setup_styles()

        # Xây dựng các thành phần giao diện
        self.create_widgets()

        # Bắt đầu vòng lặp kiểm tra hàng đợi nhật ký
        self.root.after(100, self.process_queues)

    def setup_styles(self):
        """Cấu hình màu sắc, phông chữ và kiểu dáng ttk trực quan, hiện đại."""
        self.style = ttk.Style()
        try:
            self.style.theme_use('clam')
        except Exception:
            pass

        # Màu sắc chủ đạo
        self.COLOR_BG = "#f8fafc"          # Nền xám nhạt hiện đại
        self.COLOR_CARD = "#ffffff"        # Nền card trắng
        self.COLOR_PRIMARY = "#2563eb"     # Xanh dương đậm
        self.COLOR_SUCCESS = "#16a34a"     # Xanh lá cây thành công
        self.COLOR_DANGER = "#dc2626"      # Đỏ hủy
        self.COLOR_TEXT = "#0f172a"        # Chữ đen xám đậm
        self.COLOR_MUTED = "#64748b"       # Chữ phụ màu xám

        self.root.configure(bg=self.COLOR_BG)

        # Style chung cho Label, Frame
        self.style.configure(".", background=self.COLOR_BG, foreground=self.COLOR_TEXT, font=("Segoe UI", 10))
        self.style.configure("Card.TFrame", background=self.COLOR_CARD, relief="groove")
        self.style.configure("Header.TLabel", font=("Segoe UI", 15, "bold"), foreground="#1e3a8a", background=self.COLOR_BG)
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 9), foreground=self.COLOR_MUTED, background=self.COLOR_BG)
        self.style.configure("Section.TLabel", font=("Segoe UI", 10, "bold"), foreground="#1e293b", background=self.COLOR_CARD)
        
        # Style cho các nút bấm
        self.style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background=self.COLOR_PRIMARY, foreground="#ffffff")
        self.style.map("Primary.TButton", background=[('active', '#1d4ed8'), ('disabled', '#94a3b8')])

        self.style.configure("Danger.TButton", font=("Segoe UI", 10, "bold"), background=self.COLOR_DANGER, foreground="#ffffff")
        self.style.map("Danger.TButton", background=[('active', '#b91c1c'), ('disabled', '#cbd5e1')])

        self.style.configure("Success.TButton", font=("Segoe UI", 10, "bold"), background=self.COLOR_SUCCESS, foreground="#ffffff")
        self.style.map("Success.TButton", background=[('active', '#15803d')])

    def create_widgets(self):
        """Khởi tạo toàn bộ các phần tử trên cửa sổ ứng dụng."""
        # --- 1. TIÊU ĐỀ ỨNG DỤNG ---
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

        # --- 2. CARD CẤU HÌNH ĐẦU VÀO ---
        input_card = ttk.Frame(self.root, padding=15, style="Card.TFrame")
        input_card.pack(fill="x", padx=15, pady=8)

        # Dòng 1: Chọn Nguồn dữ liệu
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

        # Dòng 2: Nhập Link hoặc App ID
        row2 = ttk.Frame(input_card, style="Card.TFrame")
        row2.pack(fill="x", pady=6)

        self.lbl_target = ttk.Label(row2, text="Package Name / Link:", style="Section.TLabel", width=18)
        self.lbl_target.pack(side="left")

        self.target_entry = ttk.Entry(row2, font=("Segoe UI", 10))
        self.target_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.target_entry.insert(0, "com.shopee.vn")

        # Nút ví dụ nhanh
        self.btn_example = ttk.Button(row2, text="Mẫu thử", command=self.fill_example, width=9)
        self.btn_example.pack(side="right")

        self.lbl_hint = ttk.Label(
            input_card,
            text="Gợi ý: Nhập Package Name (ví dụ: com.shopee.vn, com.zing.zalo) hoặc dán link Google Play đầy đủ.",
            font=("Segoe UI", 8, "italic"), foreground=self.COLOR_MUTED, background=self.COLOR_CARD
        )
        self.lbl_hint.pack(anchor="w", padx=(145, 0), pady=(0, 6))

        # Dòng 3: Số lượng bản ghi, Quốc gia, Sắp xếp, Lọc sao
        row3 = ttk.Frame(input_card, style="Card.TFrame")
        row3.pack(fill="x", pady=6)

        # Số lượng
        ttk.Label(row3, text="Số lượng:", style="Section.TLabel", width=10).pack(side="left")
        self.count_combobox = ttk.Combobox(
            row3, values=["500", "1000", "2000", "3000", "5000", "10000", "20000"],
            width=8, font=("Segoe UI", 10)
        )
        self.count_combobox.set("1000")
        self.count_combobox.pack(side="left", padx=(0, 15))

        # Quốc gia
        ttk.Label(row3, text="Quốc gia:", style="Section.TLabel").pack(side="left")
        self.country_combobox = ttk.Combobox(
            row3, values=["vn (Việt Nam)", "us (Hoa Kỳ)", "kr (Hàn Quốc)", "jp (Nhật Bản)", "sg (Singapore)"],
            width=13, state="readonly", font=("Segoe UI", 9)
        )
        self.country_combobox.set("vn (Việt Nam)")
        self.country_combobox.pack(side="left", padx=(5, 15))

        # Sắp xếp
        ttk.Label(row3, text="Sắp xếp:", style="Section.TLabel").pack(side="left")
        self.sort_combobox = ttk.Combobox(
            row3, values=["Mới nhất (Newest)", "Liên quan nhất (Most Relevant)"],
            width=18, state="readonly", font=("Segoe UI", 9)
        )
        self.sort_combobox.set("Mới nhất (Newest)")
        self.sort_combobox.pack(side="left", padx=(5, 15))

        # Lọc sao
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

        # Dòng 4: Thư mục lưu kết quả & Định dạng xuất
        row4 = ttk.Frame(input_card, style="Card.TFrame")
        row4.pack(fill="x", pady=6)

        ttk.Label(row4, text="Thư mục lưu:", style="Section.TLabel", width=18).pack(side="left")
        self.save_dir_entry = ttk.Entry(row4, font=("Segoe UI", 10))
        self.save_dir_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.save_dir_entry.insert(0, self.last_saved_dir)

        btn_browse = ttk.Button(row4, text="📁 Chọn thư mục...", command=self.browse_folder)
        btn_browse.pack(side="left", padx=(0, 15))

        # Định dạng file
        ttk.Label(row4, text="Định dạng:", style="Section.TLabel").pack(side="left")
        self.format_combobox = ttk.Combobox(
            row4, values=["Excel (.xlsx)", "CSV (UTF-8-sig)", "Cả hai (.xlsx & .csv)"],
            width=18, state="readonly", font=("Segoe UI", 9)
        )
        self.format_combobox.set("Excel (.xlsx)")
        self.format_combobox.pack(side="left", padx=5)

        # --- 3. KHU VỰC ĐIỀU KHIỂN & TIẾN TRÌNH ---
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

        # Nhãn trạng thái tóm tắt
        self.status_lbl = ttk.Label(action_frame, text="Sẵn sàng thực hiện.", font=("Segoe UI", 9, "bold"), foreground="#0369a1")
        self.status_lbl.pack(side="right", padx=10)

        # Thanh tiến trình
        progress_frame = ttk.Frame(self.root, padding="15 4 15 6")
        progress_frame.pack(fill="x")

        self.progress_bar = ttk.Progressbar(progress_frame, mode="determinate")
        self.progress_bar.pack(fill="x")

        # --- 4. NHẬT KÝ HOẠT ĐỘNG (LOG CONSOLE) ---
        log_frame = ttk.LabelFrame(self.root, text=" 📜 Nhật ký hoạt động & Trạng thái chi tiết ", padding=8)
        log_frame.pack(fill="both", expand=True, padx=15, pady=(4, 15))

        self.log_text = ScrolledText(
            log_frame, wrap="word", font=("Consolas", 9),
            bg="#1e1e1e", fg="#e2e8f0", insertbackground="#ffffff"
        )
        self.log_text.pack(fill="both", expand=True)

        # Ghi log chào mừng ban đầu
        self.log(f"[{datetime.now().strftime('%H:%M:%S')}] Công cụ đã sẵn sàng. Nhập thông tin và bấm 'BẮT ĐẦU CÀO DỮ LIỆU'...")

    # ==========================================================================
    # CÁC SỰ KIỆN TƯƠNG TÁC GIAO DIỆN
    # ==========================================================================

    def on_source_change(self):
        """Thay đổi nhãn và gợi ý khi người dùng chuyển nguồn dữ liệu."""
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
        """Điền dữ liệu mẫu nhanh để người dùng thử nghiệm ngay."""
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
        """Mở hộp thoại chọn thư mục lưu trữ."""
        chosen = filedialog.askdirectory(initialdir=self.save_dir_entry.get().strip() or os.getcwd())
        if chosen:
            self.save_dir_entry.delete(0, tk.END)
            self.save_dir_entry.insert(0, chosen)
            self.last_saved_dir = chosen

    def open_output_folder(self):
        """Mở thư mục lưu trữ trên Windows Explorer."""
        target_dir = self.save_dir_entry.get().strip() or os.getcwd()
        if os.path.exists(target_dir):
            try:
                os.startfile(target_dir)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể mở thư mục: {e}")
        else:
            messagebox.showwarning("Cảnh báo", "Thư mục chưa tồn tại trên máy tính!")

    def log(self, message: str):
        """Thêm dòng chữ vào màn hình console."""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def process_queues(self):
        """Lắng nghe hàng đợi từ luồng cào dữ liệu để cập nhật UI mượt mà."""
        # 1. Cập nhật Log
        while not self.log_queue.empty():
            try:
                msg = self.log_queue.get_nowait()
                self.log(msg)
            except queue.Empty:
                break

        # 2. Cập nhật Progress Bar
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
    # QUẢN LÝ TIẾN TRÌNH CÀO DỮ LIỆU (THREADING & CONTROLLER)
    # ==========================================================================

    def start_scraping(self):
        """Khởi động luồng cào dữ liệu."""
        raw_target = self.target_entry.get().strip()
        if not raw_target:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Link, Package Name hoặc App ID!")
            return

        # Kiểm tra số lượng
        try:
            target_count = int(self.count_combobox.get().replace(",", "").replace(".", "").strip())
            if target_count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Lỗi số lượng", "Số lượng bản ghi phải là một số nguyên dương (ví dụ: 1000)!")
            return

        save_dir = self.save_dir_entry.get().strip() or os.getcwd()

        # Xác định định dạng xuất
        fmt_choice = self.format_combobox.get()
        if "Excel" in fmt_choice:
            export_format = "xlsx"
        elif "CSV" in fmt_choice:
            export_format = "csv"
        else:
            export_format = "both"

        # Lấy thông số lọc sao
        star_str = self.star_combobox.get().strip()
        filter_star = 0
        if "Tất cả" in star_str:
            filter_star = 0  # 0 nghĩa là cào tất cả các mức sao từ 1 đến 5 sao
        else:
            match_star = re.search(r'(\d+)\s*sao', star_str)
            if match_star:
                filter_star = int(match_star.group(1))

        # Lấy kiểu sắp xếp
        sort_choice = self.sort_combobox.get()
        sort_type = "most_relevant" if "Liên quan" in sort_choice else "newest"

        # Lấy thông số quốc gia
        country_code = self.country_combobox.get().split()[0].strip()

        # Thiết lập trạng thái giao diện khi đang chạy
        self.stop_event.clear()
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        self.progress_bar['value'] = 0
        self.status_lbl.config(text="Đang kết nối & cào dữ liệu...", foreground=self.COLOR_PRIMARY)

        # Chạy trong luồng riêng để tránh làm đơ ứng dụng Tkinter
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
        """Gửi tín hiệu dừng cào dữ liệu."""
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
        """Hàm thực thi trong luồng nền (Background Worker Thread)."""
        start_time = time.time()
        base_name = "scraped_data"

        try:
            # 1. Thu thập dữ liệu theo nguồn
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

            else:  # Trang Web thông thường
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

            # 2. Xử lý & Làm sạch dữ liệu
            if df.empty:
                self.log_queue.put("[Cảnh báo] Không tìm thấy dữ liệu nào phù hợp với yêu cầu.")
                self.root.after(0, lambda: messagebox.showwarning("Kết quả rỗng", "Không tìm thấy dữ liệu nào. Vui lòng kiểm tra lại Link/ID hoặc kết nối mạng!"))
            else:
                df = clean_and_process_dataframe(df, self.log_queue)
                
                # 3. Xuất file kết quả
                saved_files = export_dataframe(df, save_dir, base_name, export_format, self.log_queue)

                elapsed = round(time.time() - start_time, 2)
                success_msg = f"ĐÃ HOÀN THÀNH!\n- Thu thập: {len(df):,} bản ghi\n- Thời gian: {elapsed} giây\n- Thư mục lưu: {save_dir}"
                self.log_queue.put("=" * 60)
                self.log_queue.put(f"[Thành công] {success_msg.replace(chr(10), ' | ')}")
                self.log_queue.put("=" * 60)

                # Hiển thị popup thông báo thành công
                self.root.after(0, lambda: messagebox.showinfo("Cào dữ liệu thành công!", success_msg))

        except Exception as e:
            self.log_queue.put(f"[Lỗi ngoại lệ] {str(e)}")
            self.root.after(0, lambda err=str(e): messagebox.showerror("Lỗi thực thi", f"Đã xảy ra lỗi:\n{err}"))

        finally:
            # Khôi phục trạng thái nút bấm trên giao diện
            self.root.after(0, self._reset_ui_after_scraping)

    def _reset_ui_after_scraping(self):
        """Khôi phục trạng thái giao diện sau khi luồng cào hoàn tất."""
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled")
        self.status_lbl.config(text="Đã hoàn thành công việc.", foreground=self.COLOR_SUCCESS)
        self.progress_bar['value'] = 100


# ==============================================================================
# 5. ĐIỂM KHỞI CHẠY CHƯƠNG TRÌNH (MAIN ENTRY)
# ==============================================================================

def main():
    # Hỗ trợ hiển thị sắc nét trên màn hình độ phân giải cao (High DPI) của Windows
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
