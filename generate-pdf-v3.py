import markdown
import re

md_path = '/root/.openclaw/workspace/ai-quality-inspection-report-2026.md'
css_path = '/root/.openclaw/workspace/ai-quality-inspection-report-v2.css'
out_path = '/root/.openclaw/workspace/ai-quality-inspection-report-2026-v3.pdf'

with open(md_path, 'r') as f:
    md_content = f.read()

with open(css_path, 'r') as f:
    base_css = f.read()

extra_css = """
/* ===== 封面页 ===== */
.cover-page {
  page-break-after: always;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  text-align: center;
}
.cover-content { margin-top: 15vh; }
.cover-page h1 {
  font-size: 28pt; color: #1b2a4a; border: none;
  border-bottom: 4px solid #c4a35a; padding-bottom: 16px;
  margin-bottom: 20px; letter-spacing: 4px;
}
.cover-page h2 {
  font-size: 15pt; color: #4a5568; border: none; padding: 0;
  text-align: center; margin-top: 10px; margin-bottom: 40px; font-weight: normal;
}
.cover-meta { margin-top: 60px; font-size: 11pt; color: #666; line-height: 2.4; }
.cover-meta p { margin: 4px 0; }
.cover-meta strong { color: #444; }
.toc { font-size: 12pt; line-height: 2.4; padding: 16px 24px; background: #f9fafb; border-radius: 6px; margin: 16px 0; }
.toc p { margin: 3px 0; }
.toc-item { margin: 6px 0; font-weight: 600; color: #1b2a4a; }
.toc-sub { margin: 2px 0 2px 2em; color: #4a5568; font-weight: 400; }
body > h1:first-of-type { page-break-before: avoid; }
body > h1 { page-break-before: always; }
"""

full_css = base_css + "\n" + extra_css

cover_html = """
<div class="cover-page">
  <div class="cover-content">
    <h1>电子制造业AI质检全景研究报告</h1>
    <h2>基于第一性原理的深度调研与最佳实践分析</h2>
    <div class="cover-meta">
      <p><strong>编制日期</strong>　2026年6月26日</p>
      <p><strong>研究范围</strong>　全球电子制造业AI质检技术现状（截至2026年6月）</p>
      <p><strong>分析框架</strong>　MECE分类法 · 帕累托法则 · 金字塔原理</p>
      <p><strong>应用视角</strong>　IQC → SPI → 炉前AOI → 炉后AOI → AXI → FCT/ICT</p>
    </div>
  </div>
</div>
"""

# Strip the existing cover div from markdown
md_body = re.sub(r'<div class="cover">.*?</div>\s*', '', md_content, flags=re.DOTALL)
md_body = re.sub(r'^##\s+基于第一性原理.*?\n\n', '', md_body, flags=re.MULTILINE)
md_body = re.sub(r'<div class="meta">.*?</div>\s*', '', md_body, flags=re.DOTALL)

extensions = ['tables', 'fenced_code', 'toc', 'codehilite']
html_body = markdown.markdown(md_body.strip(), extensions=extensions)

# Fix list item spacing
html_body = html_body.replace('<li>', '<li style="margin:5px 0; line-height:1.9;">')
# Fix code blocks
html_body = re.sub(
    r'<pre><code(.*?)>',
    r'<pre style="white-space:pre-wrap; word-wrap:break-word;"><code\1>',
    html_body
)

full_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>电子制造业AI质检全景研究报告</title>
<style>
""" + full_css + """
</style>
</head>
<body>
""" + cover_html + html_body + """
</body>
</html>"""

from weasyprint import HTML
HTML(string=full_html).write_pdf(out_path)
print('PDF v3 generated successfully')
