import sys
sys.stdout.reconfigure(encoding='utf-8')
import shutil
import zipfile
import os

print("=== DONG BO CAC THU MUC VA PACKAGE ZIP ===")

# Copy files from root to Nhom_12
shutil.copy('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'd:/HocMayPrJ/Nhom_12/du_an_hoc_may_nhom_12.ipynb')
shutil.copy('d:/HocMayPrJ/data/app_reviews_cleaned.csv', 'd:/HocMayPrJ/Nhom_12/app_reviews_cleaned.csv')
shutil.copy('d:/HocMayPrJ/data/train.csv', 'd:/HocMayPrJ/Nhom_12/train.csv')
shutil.copy('d:/HocMayPrJ/data/val.csv', 'd:/HocMayPrJ/Nhom_12/val.csv')
shutil.copy('d:/HocMayPrJ/data/test.csv', 'd:/HocMayPrJ/Nhom_12/test.csv')

# Package into Nhom_12/Nhom12.zip
zip_path = 'd:/HocMayPrJ/Nhom_12/Nhom12.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk('d:/HocMayPrJ/data'):
        for file in files:
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, 'd:/HocMayPrJ')
            z.write(full_p, rel_p)
    z.write('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'du_an_hoc_may_nhom_12.ipynb')
    z.write('d:/HocMayPrJ/reports/BAO_CAO_KIEM_TOAN_DU_LIEU_VA_MINH_CHUNG.md', 'reports/BAO_CAO_KIEM_TOAN_DU_LIEU_VA_MINH_CHUNG.md')
    z.write('d:/HocMayPrJ/README.md', 'README.md')
    z.write('d:/HocMayPrJ/requirements.txt', 'requirements.txt')

print("Dong bo va nen zip thanh cong!")
