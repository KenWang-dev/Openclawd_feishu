import markdown
from weasyprint import HTML

def md_to_pdf(md_path, css_path, output_path, title=""):
    """Markdown -> HTML -> PDF"""
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()
    
    # Markdown to HTML
    extensions = ['tables', 'fenced_code', 'toc']
    html_body = markdown.markdown(md, extensions=extensions)
    
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Add custom overrides for better Chinese formatting
    custom_css = """
    @page { 
        size: A4; 
        margin: 2cm 1.8cm;
        @bottom-center {
            content: "第 " counter(page) " 页 / 共 " counter(pages) " 页";
            font-size: 9pt;
            color: #888;
        }
    }
    body { font-family: "Noto Sans CJK SC", "Noto Sans CJK TC", "Microsoft YaHei", sans-serif; }
    h1 { font-family: "Noto Sans CJK SC", sans-serif; page-break-before: avoid; }
    h2 { font-family: "Noto Sans CJK SC", sans-serif; page-break-before: avoid; border-bottom: 2px solid #2c3e50; padding-bottom: 8px; margin-top: 28px; }
    h3 { font-family: "Noto Sans CJK SC", sans-serif; page-break-before: avoid; }
    h4 { font-family: "Noto Sans CJK SC", sans-serif; page-break-before: avoid; }
    table { font-family: "Noto Sans CJK SC", sans-serif; }
    th { font-family: "Noto Sans CJK SC", sans-serif; }
    td { font-family: "Noto Sans CJK SC", sans-serif; }
    blockquote { border-left: 4px solid #3498db; padding: 10px 15px; background: #f8f9fa; margin: 15px 0; }
    blockquote p { margin: 5px 0; }
    /* Make table rows not split */
    table tr { page-break-inside: avoid; }
    /* Avoid orphan lines */
    p { orphans: 3; widows: 3; }
    /* Better code block style */
    code { background: #f0f0f0; padding: 2px 4px; border-radius: 3px; font-size: 0.9em; }
    /* Cover page effect */
    h1:first-of-type { font-size: 24pt; margin-top: 60px; margin-bottom: 10px; }
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
        md_path='/root/.openclaw/workspace/memory/aoi-ai-research-2025-06.md',
        css_path='/root/.openclaw/workspace/skills/pdf-styles/templates/business-report.css',
        output_path='/root/.openclaw/workspace/memory/AI+AOI深度调研报告-2025-06.pdf',
        title='AI+AOI深度调研报告'
    )
