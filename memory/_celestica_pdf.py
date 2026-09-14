import markdown
from weasyprint import HTML

def md_to_pdf(md_path, css_path, output_path, title=""):
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()
    extensions = ['tables', 'fenced_code', 'toc']
    html_body = markdown.markdown(md, extensions=extensions)
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    custom_css = """
    @page { size: A4; margin: 2cm 1.8cm; @bottom-center { content: "第 " counter(page) " 页 / 共 " counter(pages) " 页"; font-size: 8pt; color: #888; } }
    body { font-family: "Noto Sans CJK SC", sans-serif; font-size: 9.5pt; line-height: 1.7; }
    h1 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 18pt; color: #1a1a2e; border-bottom: 3px solid #2c3e50; padding-bottom: 8px; margin-top: 30px; page-break-before: avoid; }
    h2 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 13pt; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px; margin-top: 22px; page-break-before: avoid; }
    h3 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 11pt; color: #34495e; margin-top: 16px; page-break-before: avoid; }
    table { font-family: "Noto Sans CJK SC", sans-serif; font-size: 8.5pt; width: 100%; border-collapse: collapse; margin: 8px 0; }
    th { font-family: "Noto Sans CJK SC", sans-serif; background: #2c3e50; color: white; padding: 5px 7px; text-align: left; font-size: 8pt; }
    td { font-family: "Noto Sans CJK SC", sans-serif; padding: 4px 7px; border-bottom: 1px solid #ddd; font-size: 8pt; }
    tr:nth-child(even) { background: #f8f9fa; }
    tr { page-break-inside: avoid; }
    blockquote { border-left: 4px solid #3498db; padding: 8px 12px; background: #f0f7ff; margin: 8px 0; font-size: 8.5pt; }
    p { orphans: 3; widows: 3; margin: 5px 0; }
    strong { color: #2c3e50; }
    """
    full_html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>{title}</title><style>{css}{custom_css}</style></head><body>{html_body}</body></html>"""
    HTML(string=full_html).write_pdf(output_path)
    print(f"PDF generated: {output_path}")

if __name__ == '__main__':
    md_to_pdf('/root/.openclaw/workspace/memory/celestica-research-2026-06.md', '/root/.openclaw/workspace/skills/pdf-styles/templates/business-report.css', '/root/.openclaw/workspace/memory/Celestica天弘科技调研报告-2026-06-25.pdf', 'Celestica天弘科技调研报告')
