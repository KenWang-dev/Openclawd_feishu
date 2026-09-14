---
name: eli5
description: 用大白话+可视化 HTML 页面解释任何概念。触发词：eli5、简单解释、画个图解释、可视化解释、explain like i'm 5、用图解释。
---

# eli5

Explain like I'm someone who knows nothing about this topic, using a single self-contained HTML page with big pictures (CSS/SVG diagrams, illustrations via Unicode/emoji art, or described imagery) and very few words.

## Instructions

1. Parse the user's topic from their message (the part after `/eli5`, or the whole message if no slash command was used).
2. Generate a complete, self-contained HTML page that explains the topic visually.

### HTML Requirements

- **Single file**, no external dependencies (inline all CSS and JS)
- **Dark background** (#1a1a2e or similar) with light text for readability
- **Big, bold headings** — use 2-3em font size for section titles
- **CSS-only diagrams** — use flexbox, grid, borders, colors, shapes (border-radius, clip-path) to create visual representations of concepts
- **Emoji as icons** — use large emoji (2-4rem) to represent components/actors
- **Minimal text** — aim for 3-5 short sentences per section, never more than a short paragraph
- **Arrow/flow indicators** — use CSS arrows (border tricks) or Unicode arrows (→ ↓ ↔) to show relationships
- **Color coding** — use consistent colors for related concepts
- **Responsive** — should work on mobile screens
- **Chinese text** — since the user is Chinese, write all explanatory text in Chinese

### Structure

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ELI5: [topic]</title>
  <style>
    /* Full inline styles */
  </style>
</head>
<body>
  <!-- Visual explanation -->
</body>
</html>
```

### Content Guidelines

- Start with the **simplest possible analogy** (everyday life if possible)
- Use 3-5 visual "slides" / sections maximum
- Each section: one big visual + one short sentence
- End with a one-line "TL;DR" summary
- No jargon, no technical terms unless absolutely necessary (and if so, explain them immediately)
- Make it feel like a children's picture book, not a textbook

3. Save the HTML to a file in the workspace, then use the `canvas` tool to present it.

### Output

- Write the HTML to `/root/.openclaw/workspace/eli5-output.html`
- Use `canvas` action=`present` with `url` pointing to the file to display it
- Tell the user the topic has been visualized

Topic: $ARGUMENTS
