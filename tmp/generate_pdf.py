import markdown
from weasyprint import HTML

def md_to_pdf(md_path, css_path, output_path, title=""):
    with open(md_path, 'r') as f:
        md = f.read()
    
    extensions = ['tables', 'fenced_code', 'toc']
    html_body = markdown.markdown(md, extensions=extensions)
    
    with open(css_path, 'r') as f:
        css = f.read()
    
    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{css}
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
        '/root/.openclaw/workspace/tmp/claude-code-expertise.md',
        '/root/.openclaw/workspace/skills/pdf-styles/templates/academic.css',
        '/root/.openclaw/workspace/tmp/claude-code-expertise.pdf',
        '代理式编程与专业技能的持续回报'
    )
