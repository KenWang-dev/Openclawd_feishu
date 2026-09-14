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
    @page { 
        size: A4;
        margin: 1.5cm 1.5cm;
        @bottom-center {
            content: "第 " counter(page) " 页 / 共 " counter(pages) " 页";
            font-size: 8pt;
            color: #888;
        }
    }
    body { font-family: "Noto Sans CJK SC", "Noto Sans CJK TC", sans-serif; font-size: 9.5pt; line-height: 1.6; }
    h1 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 20pt; color: #1a1a2e; border-bottom: 3px solid #2c3e50; padding-bottom: 10px; margin-top: 30px; page-break-before: avoid; }
    h2 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 14pt; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 6px; margin-top: 24px; page-break-before: avoid; }
    h3 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 12pt; color: #34495e; margin-top: 18px; page-break-before: avoid; }
    h4 { font-family: "Noto Sans CJK SC", sans-serif; font-size: 10.5pt; color: #555; margin-top: 14px; page-break-before: avoid; }
    table { font-family: "Noto Sans CJK SC", sans-serif; font-size: 8.5pt; width: 100%; border-collapse: collapse; margin: 10px 0; }
    th { font-family: "Noto Sans CJK SC", sans-serif; background: #2c3e50; color: white; padding: 6px 8px; text-align: left; font-weight: bold; font-size: 8.5pt; }
    td { font-family: "Noto Sans CJK SC", sans-serif; padding: 5px 8px; border-bottom: 1px solid #ddd; font-size: 8pt; }
    tr:nth-child(even) { background: #f8f9fa; }
    tr { page-break-inside: avoid; }
    blockquote { border-left: 4px solid #3498db; padding: 8px 12px; background: #f0f7ff; margin: 10px 0; font-size: 9pt; }
    p { orphans: 3; widows: 3; margin: 6px 0; }
    code { background: #f0f0f0; padding: 2px 4px; border-radius: 3px; font-size: 8.5pt; }
    strong { color: #2c3e50; }
    hr { border: none; border-top: 1px solid #ddd; margin: 15px 0; }
    """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{css}
{custom_css}
</style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    HTML(string=full_html).write_pdf(output_path)
    print(f"PDF generated: {output_path}")

if __name__ == '__main__':
    md_to_pdf(
        md_path='/root/.openclaw/workspace/memory/phone-roadmap-visual-report.md',
        css_path='/root/.openclaw/workspace/skills/pdf-styles/templates/business-report.css',
        output_path='/root/.openclaw/workspace/memory/全球手机产品迭代路线图-2026-06-25.pdf',
        title='全球手机产品迭代路线图 2026'
    )
