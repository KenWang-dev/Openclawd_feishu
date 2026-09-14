#!/usr/bin/env python3
"""Generate PDF report from Markdown using markdown + weasyprint."""

import markdown
from weasyprint import HTML, CSS
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILE = os.path.join(BASE_DIR, "odm-inventory-turnover-report.md")
CSS_FILE = "/root/.openclaw/workspace/skills/pdf-styles/templates/business-report.css"
PDF_FILE = os.path.join(BASE_DIR, "手机ODM行业存货周转效率提升报告.pdf")

# Read markdown content
with open(MD_FILE, "r", encoding="utf-8") as f:
    md_content = f.read()

# Read CSS
if os.path.exists(CSS_FILE):
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        css_content = f.read()
else:
    print(f"WARNING: CSS file not found at {CSS_FILE}, using inline styles.")
    css_content = ""

# Convert markdown to HTML with extensions
html_body = markdown.markdown(
    md_content,
    extensions=["tables", "fenced_code", "toc", "sane_lists"],
)

# Build full HTML document with CSS
full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <style>
{css_content}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

# Additional inline CSS for print quality
extra_css = CSS(string="""
@page {
    size: A4;
    margin: 2cm 2.5cm;
    @bottom-center {
        content: "第 " counter(page) " 页";
        font-size: 9pt;
        color: #999;
    }
}

/* Page break before major chapters */
h2 {
    page-break-before: auto;
}

/* Avoid breaking inside tables */
table, figure {
    page-break-inside: avoid;
}

/* Avoid orphan headers */
h2, h3 {
    page-break-after: avoid;
}

/* First h1 is cover - give it more space */
h1:first-of-type {
    page-break-after: always;
}

/* Cover page subtitle styling */
h1:first-of-type + p {
    text-align: center;
    font-size: 14pt;
    color: #666;
}

/* Blockquote styling for key findings */
blockquote {
    border-left: 4px solid #c4a35a;
    margin: 14px 0;
    padding: 10px 18px;
    background: #faf8f5;
    font-style: italic;
    font-size: 10.5pt;
}

/* Code blocks */
pre {
    background: #f5f5f5;
    color: #333;
    padding: 14px;
    border-radius: 4px;
    font-size: 9pt;
    border: 1px solid #e0e0e0;
}

pre code {
    background: none;
    color: inherit;
}

/* Table refinement */
table {
    font-size: 10pt;
    width: 100%;
}

th {
    font-size: 9.5pt;
}

/* HR separator */
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 20px 0;
}

/* Print-friendly link styling */
a {
    color: #1b2a4a;
    text-decoration: none;
}

/* Avoid blank pages after cover */
h1:first-of-type + hr + blockquote + hr + h2 {
    page-break-before: always;
}
""")

# Generate PDF
print(f"Generating PDF from {MD_FILE}...")
print(f"CSS: {CSS_FILE}")

HTML(string=full_html).write_pdf(
    PDF_FILE,
    stylesheets=[extra_css],
)

print(f"PDF generated: {PDF_FILE}")
print(f"File size: {os.path.getsize(PDF_FILE) / 1024:.1f} KB")
