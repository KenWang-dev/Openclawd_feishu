#!/usr/bin/env python3
"""Generate PDF from the Karpathy-Anthropic analysis markdown using academic template."""

import markdown
from weasyprint import HTML, CSS

MD_PATH = "/root/.openclaw/workspace/output/karpathy-anthropic-analysis.md"
CSS_PATH = "/root/.openclaw/workspace/skills/pdf-styles/templates/academic.css"
OUTPUT_PATH = "/root/.openclaw/workspace/output/Karpathy加入Anthropic-深度分析.pdf"

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md = f.read()

extensions = ['tables', 'fenced_code', 'toc']
html_body = markdown.markdown(md, extensions=extensions)

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# Add a cover page style and metadata section styling
extra_css = """
h1 { page-break-before: auto; }
h2 { page-break-after: avoid; }
table { page-break-inside: avoid; }
blockquote { page-break-inside: avoid; }
strong { color: #000; }
/* Emphasis for key conclusions */
p > strong:first-child { display: block; margin-bottom: 4px; }
"""

full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Karpathy 加入 Anthropic：第一性原理深度分析</title>
<style>
{css}
{extra_css}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=full_html).write_pdf(OUTPUT_PATH)
print(f"PDF generated: {OUTPUT_PATH}")
