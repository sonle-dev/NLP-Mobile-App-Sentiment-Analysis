# -*- coding: utf-8 -*-
"""
Script: build_and_check_pages.py
Assembles all expanded modules into:
- reports/BAO_CAO_DU_AN_HOC_MAY_NHOM_12.docx
- Nhom_12/Bao_Cao_Du_An_Hoc_May_Nhom_12_Hoan_Chinh_50Trang.docx
- Nhom_12/Bao_Cao_Du_An_Hoc_May_Nhom_12.docx
and measures exact page count using Word COM.
"""

import os
import sys
import docx
from docx import Document
from docx.shared import Inches

from report_modules.frontmatter_expanded import add_frontmatter
from report_modules.chapter1_expanded import add_chapter1
from report_modules.chapter2_expanded import add_chapter2
from report_modules.chapter3_expanded import add_chapter3
from report_modules.chapter4_expanded import add_chapter4

def main():
    print("[*] Khoi tao tai lieu...")
    doc = Document()
    
    # Page setup: Top 2cm, Bottom 2cm, Left 3cm, Right 2cm
    for s in doc.sections:
        s.top_margin = Inches(0.79)
        s.bottom_margin = Inches(0.79)
        s.left_margin = Inches(1.18)
        s.right_margin = Inches(0.79)
        
    print("[*] Them Frontmatter mo rong...")
    add_frontmatter(doc)
    
    print("[*] Them Chuong 1 mo rong...")
    add_chapter1(doc)
    
    print("[*] Them Chuong 2 mo rong...")
    add_chapter2(doc)
    
    print("[*] Them Chuong 3 mo rong...")
    add_chapter3(doc)
    
    print("[*] Them Chuong 4 va Tai lieu tham khao mo rong...")
    add_chapter4(doc)
    
    out1 = "reports/BAO_CAO_DU_AN_HOC_MAY_NHOM_12.docx"
    out2 = "Nhom_12/Bao_Cao_Du_An_Hoc_May_Nhom_12_Hoan_Chinh_50Trang.docx"
    out3 = "Nhom_12/Bao_Cao_Du_An_Hoc_May_Nhom_12.docx"
    out4 = "Nhom_12/Bao_Cao_Du_An_Hoc_May_Nhom_12_Ban_In_Chuan.docx"
    
    doc.save(out1)
    print(f"[✓] Luu thanh cong tai: {out1}")
    
    doc.save(out4)
    print(f"[✓] Luu thanh cong tai: {out4}")

    try:
        doc.save(out2)
        print(f"[✓] Luu thanh cong tai: {out2}")
    except PermissionError:
        print(f"[!] {out2} dang mo trong Word, da luu ban moi nhat tai {out4} va {out1}!")
    
    try:
        doc.save(out3)
        print(f"[✓] Luu thanh cong tai: {out3}")
    except PermissionError:
        print(f"[!] {out3} dang mo trong Word!")

    # Check page count with Word COM
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        wdoc = word.Documents.Open(os.path.abspath(out1))
        pages = wdoc.ComputeStatistics(2) # 2 = wdStatisticPages
        words = wdoc.ComputeStatistics(0) # 0 = wdStatisticWords
        wdoc.Close(False)
        word.Quit()
        print(f"\n==========================================")
        print(f"[★] KẾT QUẢ ĐO LƯỜNG TỰ ĐỘNG BẰNG MS WORD:")
        print(f"    - TỔNG SỐ TRANG: {pages} TRANG")
        print(f"    - TỔNG SỐ TỪ:   {words:,} TỪ")
        print(f"==========================================\n")
    except Exception as e:
        print("[!] Khong the do bang Word COM:", e)

if __name__ == '__main__':
    main()
