import sys
sys.stdout.reconfigure(encoding='utf-8')
import json

with open('d:/HocMayPrJ/du_an_hoc_may_nhom_12.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for idx in [16, 17, 18, 19, 20]:
    cell = nb['cells'][idx]
    print(f"=== CELL {idx} ({cell['cell_type']}) ===")
    print(''.join(cell['source'])[:500])
    print("---------------------------------------------")
