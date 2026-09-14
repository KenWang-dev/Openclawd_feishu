import markdown
from weasyprint import HTML

md_path = "/root/.openclaw/workspace/codex-report-translation.md"
css_path = "/root/.openclaw/workspace/skills/pdf-styles/templates/business-report.css"
output_path = "/root/.openclaw/workspace/codex-report-CN.pdf"

with open(md_path, 'r', encoding='utf-8') as f:
    md = f.read()

extensions = ['tables', 'fenced_code', 'toc']
html_body = markdown.markdown(md, extensions=extensions)

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>知识工作的下一个时代</title>
<style>
{css}
@page {{
    size: A4;
    margin: 2cm;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=full_html).write_pdf(output_path)
print(f"PDF generated: {output_path}")
