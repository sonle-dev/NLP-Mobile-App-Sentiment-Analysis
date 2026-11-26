# -*- coding: utf-8 -*-
"""
Exports docx report to Markdown format.
"""
import docx

def docx_to_md(docx_path, md_path):
    doc = docx.Document(docx_path)
    lines = []
    
    for element in doc.element.body:
        if element.tag.endswith('p'):
            p = docx.text.paragraph.Paragraph(element, doc)
            text = p.text.strip()
            if not text:
                continue
            style_name = p.style.name if p.style else ""
            if "Heading 1" in style_name:
                lines.append(f"\n# {text}\n")
            elif "Heading 2" in style_name:
                lines.append(f"\n## {text}\n")
            elif "Heading 3" in style_name:
                lines.append(f"\n### {text}\n")
            else:
                lines.append(f"{text}\n")
        elif element.tag.endswith('tbl'):
            table = docx.table.Table(element, doc)
            if not table.rows:
                continue
            # Header
            header_cells = [c.text.strip().replace('\n', ' ') for c in table.rows[0].cells]
            lines.append("\n| " + " | ".join(header_cells) + " |")
            lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
            # Rows
            for row in table.rows[1:]:
                row_cells = [c.text.strip().replace('\n', '<br>') for c in row.cells]
                lines.append("| " + " | ".join(row_cells) + " |")
            lines.append("\n")
            
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"[✓] Exported {docx_path} to {md_path}")

if __name__ == '__main__':
    docx_to_md("reports/BAO_CAO_DU_AN_HOC_MAY_NHOM_12.docx", "reports/BAO_CAO_DU_AN_HOC_MAY_NHOM_12.md")
    docx_to_md("reports/BAO_CAO_DU_AN_HOC_MAY_NHOM_12.docx", "Nhom_12/BAO_CAO_DU_AN_HOC_MAY_NHOM_12.md")
