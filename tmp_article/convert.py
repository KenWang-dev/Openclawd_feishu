#!/usr/bin/env python3
"""
Convert Twitter/X article blocks to PDF via HTML.
1:1 faithful reproduction of the original article.
"""
import json
import os
import re
from pathlib import Path

# ─── Step 1: Load JSON and extract blocks ───────────────────────────────
with open('tweet.json', 'r') as f:
    data = json.load(f)

blocks = data['tweet']['article']['content']['blocks']
entity_map = data['tweet']['article']['content']['entityMap']

# Build entity lookup: key -> entity data
entity_lookup = {}
for item in entity_map:
    if isinstance(item, dict) and 'key' in item:
        entity_lookup[item['key']] = item['value']

# ─── Step 2: Convert blocks to Markdown ───────────────────────────────────
def apply_inline_styles(text, inline_style_ranges):
    """Apply inline styles (Bold, Italic, Strikethrough) to text."""
    if not inline_style_ranges:
        return text
    
    # Build list of (start, end, open_tag, close_tag)
    tags = {
        'BOLD': ('**', '**'),
        'ITALIC': ('*', '*'),
        'STRIKETHROUGH': ('~~', '~~'),
        'UNDERLINE': ('<u>', '</u>'),
        'CODE': ('`', '`'),
    }
    
    # Sort ranges by offset descending to avoid index shifting
    sorted_ranges = sorted(inline_style_ranges, key=lambda x: x['offset'], reverse=True)
    
    chars = list(text)
    for r in sorted_ranges:
        style = r['style']
        offset = r['offset']
        length = r['length']
        
        if style in tags:
            open_tag, close_tag = tags[style]
            # Insert close tag first (after the styled text)
            end_pos = offset + length
            if end_pos <= len(chars):
                chars.insert(end_pos, close_tag)
            chars.insert(offset, open_tag)
    
    return ''.join(chars)


def block_to_markdown(block, index):
    """Convert a single block to markdown text."""
    btype = block['type']
    text = block.get('text', '')
    styles = block.get('inlineStyleRanges', [])
    entities = block.get('entityRanges', [])
    
    # Apply inline styles
    text = apply_inline_styles(text, styles)
    
    # Handle atomic blocks (dividers, images)
    if btype == 'atomic':
        if entities:
            # Find entity
            ent = entities[0]
            key = str(ent['key'])
            if key in entity_lookup:
                ent_val = entity_lookup[key]
                ent_type = ent_val.get('type', '')
                if ent_type == 'DIVIDER':
                    return '\n\n---\n\n'
                elif ent_type == 'IMAGE':
                    src = ent_val.get('data', {}).get('src', '')
                    if src:
                        return f'\n\n![image]({src})\n\n'
                elif ent_type == 'TWEMOJI':
                    # Render emoji URL as-is or skip
                    return ''
        return '\n\n---\n\n'
    
    if not text.strip() and btype not in ('header-one', 'header-two'):
        return ''
    
    # Map block types to markdown
    if btype == 'header-one':
        return f'\n\n# {text}\n\n'
    elif btype == 'header-two':
        return f'\n\n## {text}\n\n'
    elif btype == 'header-three':
        return f'\n\n### {text}\n\n'
    elif btype == 'blockquote':
        # Handle [!important] and ## headers inside blockquotes
        if text.strip() == '[!important]':
            return ''
        if text.startswith('## '):
            return f'\n> **{text[3:].strip()}**\n'
        # Multi-line blockquote
        lines = text.split('\n')
        quoted = '\n'.join(f'> {line}' for line in lines)
        return f'\n{quoted}\n'
    elif btype == 'unordered-list-item':
        return f'- {text}\n'
    elif btype == 'ordered-list-item':
        return f'1. {text}\n'  # We'll fix numbering later
    elif btype == 'code-block':
        return f'\n```\n{text}\n```\n'
    else:
        # unstyled or other
        if text.strip() == '>' or text.strip() == '':
            return ''
        return f'\n{text}\n'

# Track ordered list state
def blocks_to_markdown(blocks):
    """Convert all blocks to markdown, handling ordered list numbering."""
    md_lines = []
    ordered_counter = 0
    prev_was_ordered = False
    
    for i, block in enumerate(blocks):
        btype = block['type']
        
        if btype == 'ordered-list-item':
            ordered_counter += 1
            text = block.get('text', '')
            styles = block.get('inlineStyleRanges', [])
            text = apply_inline_styles(text, styles)
            md_lines.append(f'{ordered_counter}. {text}')
            prev_was_ordered = True
        elif btype == 'unordered-list-item':
            ordered_counter = 0
            text = block.get('text', '')
            styles = block.get('inlineStyleRanges', [])
            text = apply_inline_styles(text, styles)
            md_lines.append(f'- {text}')
            prev_was_ordered = False
        elif btype == 'atomic':
            ordered_counter = 0
            md = block_to_markdown(block, i)
            md_lines.append(md)
            prev_was_ordered = False
        else:
            if prev_was_ordered and btype != 'ordered-list-item':
                ordered_counter = 0
            md = block_to_markdown(block, i)
            md_lines.append(md)
            prev_was_ordered = False
    
    return '\n'.join(md_lines)


markdown_content = blocks_to_markdown(blocks)

# Prepend article title as main heading and cover image
title = data['tweet']['article']['title']
full_markdown = f"""# {title}

![封面](cover.jpg)

{markdown_content}
"""

# Save markdown for reference
with open('article.md', 'w') as f:
    f.write(full_markdown)

print(f"Markdown generated: {len(full_markdown)} chars, {len(blocks)} blocks")
print(f"First 200 chars:\n{full_markdown[:200]}")
print(f"\nLast 200 chars:\n{full_markdown[-200:]}")

# ─── Step 3: Convert to HTML with CSS ──────────────────────────────────
import markdown2

# Use markdown2 with extras
html_body = markdown2.markdown(
    full_markdown, 
    extras=['tables', 'fenced-code-blocks', 'strike', 'cuddled-lists']
)

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
@page {{
    size: A4;
    margin: 2cm 2.5cm;
}}

body {{
    font-family: 'Noto Sans CJK SC', 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
    font-size: 11pt;
    line-height: 1.9;
    color: #1a1a1a;
    text-align: justify;
}}

/* Cover image */
img {{
    max-width: 100%;
    height: auto;
    display: block;
    margin: 20px auto;
    border-radius: 4px;
}}

/* Main title */
h1 {{
    font-size: 22pt;
    font-weight: bold;
    color: #111;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 10px;
    page-break-after: avoid;
}}

/* Sub-title (header-two used for section intro lines) */
h2 {{
    font-size: 15pt;
    font-weight: bold;
    color: #222;
    margin-top: 28px;
    margin-bottom: 12px;
    padding-bottom: 6px;
    border-bottom: 1px solid #ddd;
    page-break-after: avoid;
}}

h3 {{
    font-size: 13pt;
    font-weight: bold;
    color: #333;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
}}

/* Paragraphs */
p {{
    margin: 0 0 10px 0;
    text-indent: 0;
    orphans: 3;
    widows: 3;
}}

/* Blockquotes */
blockquote {{
    margin: 12px 0 12px 20px;
    padding: 4px 16px;
    border-left: 3px solid #666;
    color: #333;
    background: #f9f9f9;
    font-style: normal;
}}

blockquote p {{
    margin: 4px 0;
}}

/* Bold blockquote labels */
blockquote strong:first-child {{
    /* Keep the emphasis on labels like "体感", "补充" etc. */
}}

/* Lists */
ul, ol {{
    margin: 8px 0 12px 20px;
    padding-left: 16px;
}}

li {{
    margin: 4px 0;
    line-height: 1.8;
}}

/* Horizontal rules (dividers) */
hr {{
    border: none;
    border-top: 1px solid #ccc;
    margin: 24px auto;
    width: 60%;
}}

/* Inline styles */
strong, b {{
    font-weight: bold;
    color: #111;
}}

em, i {{
    font-style: italic;
}}

del, s {{
    text-decoration: line-through;
    color: #888;
}}

u {{
    text-decoration: underline;
}}

code {{
    font-family: 'Noto Sans Mono CJK SC', 'Consolas', monospace;
    font-size: 10pt;
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 3px;
}}

/* Page breaks before major chapters */
h1 {{
    page-break-before: auto;
}}

/* First h1 (title) - no page break */
h1:first-of-type {{
    page-break-before: avoid;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

with open('article.html', 'w') as f:
    f.write(html_full)

print(f"\nHTML generated: {len(html_full)} chars")

# ─── Step 4: Convert to PDF with weasyprint ──────────────────────────────
from weasyprint import HTML

output_path = '/root/.openclaw/workspace/output/构架师教程-神话时代.pdf'

HTML(filename='article.html', base_url='.').write_pdf(output_path)

size = os.path.getsize(output_path)
print(f"\nPDF generated: {output_path}")
print(f"PDF size: {size / 1024:.1f} KB")
print("Done!")
