@echo off
chcp 65001 > nul
title Công Cụ Cào Dữ Liệu Đa Năng
echo ========================================================
echo   DANG KHOI CHAY CONG CU CAO DU LIEU (WEB & APP SCRAPER)
echo ========================================================
python "%~dp0scraper_gui.py"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Co loi xay ra hoac chua cai dat thu vien.
    echo Dang cai dat thu vien tu dong...
    pip install -r "%~dp0requirements.txt"
    python "%~dp0scraper_gui.py"
)
pause
