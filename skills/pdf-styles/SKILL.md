---
name: pdf-styles
description: Markdown/HTML 转 PDF 的专业排版引擎。根据文档类型自动选择最佳 CSS 模板，支持 10+ 种场景风格。触发词：生成PDF、做PDF、PDF排版、文档排版、转PDF、make PDF、PDF report、PDF styles。
---

# PDF 专业排版引擎

将 Markdown 转为精美 PDF，根据文档内容自动匹配最佳排版风格。

## 工作流程

1. **分析文档类型** — 判断内容属于哪种场景（见下方场景表）
2. **选择 CSS 模板** — 从模板库中加载对应风格
3. **Markdown → HTML** — 用 Python markdown 库转换（支持 tables/fenced_code/toc 扩展）
4. **注入 CSS** — 将 HTML 包裹在带完整样式的 HTML 壳中
5. **生成 PDF** — 用 WeasyPrint 输出
6. **发送给用户** — 通过飞书云盘上传并发送文件

## 场景与模板匹配

根据文档内容特征，自动推荐最合适的 CSS 风格：

| 场景 | 模板名 | 特征 | 典型用途 |
|------|--------|------|----------|
| 技术手册 | `tech-manual` | 深蓝色系、暗色代码块、红色强调 | 技术文档、API文档、编程教程 |
| 商务报告 | `business-report` | 灰色系、简洁专业、图表友好 | 行业报告、竞品分析、市场调研 |
| 学术论文 | `academic` | 衬线字体、严格排版、脚注支持 | 研究报告、白皮书、论文 |
| 简报/决策 | `executive-brief` | 大标题、留白多、数据突出 | 管理简报、决策摘要、周报 |
| 知识图谱 | `knowledge-map` | 思维导图式、节点连接、层次清晰 | 知识整理、学习笔记、概念图 |
| 产品手册 | `product-doc` | 清新配色、图文混排、步骤式 | 产品说明、用户手册、SOP |
| 数据报告 | `data-report` | 数据表格突出、图表区域、指标卡片 | 数据分析、运营报告、监控报告 |
| 个人简历 | `resume` | 双栏、紧凑、专业照片区 | CV、简历、作品集 |
| 合同/法律 | `legal` | 严肃衬线体、严格编号、红头风格 | 合同、协议、法律文件 |
| 新闻/文章 | `article` | 宽松行距、大号引文、阅读舒适 | 公众号文章、博客长文、新闻稿 |
| 创意/设计 | `creative` | 大胆配色、非对称布局、视觉冲击 | 创意提案、品牌手册、设计稿 |
| 课件/培训 | `training` | 步骤高亮、练习区、知识卡片 | 培训材料、课程课件、工作坊 |

## 模板文件位置

所有 CSS 模板存放在同一目录下的 `templates/` 子目录中：
- `templates/tech-manual.css`
- `templates/business-report.css`
- `templates/academic.css`
- `templates/executive-brief.css`
- `templates/knowledge-map.css`
- `templates/product-doc.css`
- `templates/data-report.css`
- `templates/resume.css`
- `templates/legal.css`
- `templates/article.css`
- `templates/creative.css`
- `templates/training.css`

## 使用方式

### 自动模式（推荐）
将 Markdown 文件交给 AI，说明用途即可。AI 自动判断场景并选择模板：
```
帮我把这份竞品分析转成 PDF，要商务风格
```

### 手动指定模板
```
用 tech-manual 模板把这份文档转 PDF
```

### 自定义调整
```
转 PDF，用商务风格但要把主色换成绿色
```

## 生成脚本模板

```python
import markdown
from weasyprint import HTML

def md_to_pdf(md_path, css_path, output_path, title=""):
    """Markdown → HTML → PDF"""
    with open(md_path, 'r') as f:
        md = f.read()
    
    # Markdown to HTML
    extensions = ['tables', 'fenced_code', 'toc', 'codehilite']
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
```

## 发送给用户（重要！）

**绝对不允许发送服务器内部路径。** 正确流程：
1. 将 PDF 上传到飞书云盘：`lark-cli drive +upload --file <本地路径> --name <文件名>`
2. 用 `message` 工具发送文件附件给用户

## 字体要求

确保服务器已安装中文字体：
```bash
# 检查字体
fc-list | grep -i "cjk\|chinese\|noto"
# 安装（如缺失）
yum install -y google-noto-cjk-fonts google-noto-emoji-color-fonts
```

## 输出规格

| 参数 | 默认值 |
|------|--------|
| 页面大小 | A4 |
| 边距 | 2cm（上下左右） |
| 字号 | 正文 11pt |
| 行距 | 1.8 |
| 最大页数 | 无限制 |
| 文件格式 | PDF |
