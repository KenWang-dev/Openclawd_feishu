#!/bin/bash
# Claude Code 动态监控脚本
# 监控过去 24 小时内的 Claude Code 动态

echo "🦊 Claude Code 动态监控 - $(date '+%Y-%m-%d %H:%M:%S')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. 检查 GitHub 最新版本
echo "📦 检查版本发布..."
VERSION=$(curl -s "https://api.github.com/repos/anthropics/claude-code/releases/latest" 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(f\"{d.get('tag_name','N/A')}|{d.get('published_at','N/A')[:10]}\")" 2>/dev/null || echo "N/A")
echo "  最新版本: $VERSION"

# 2. 检查 GitHub stars
echo "⭐ 检查 GitHub 热度..."
STARS=$(curl -s "https://api.github.com/repos/anthropics/claude-code" 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stargazers_count','N/A'))" 2>/dev/null || echo "N/A")
echo "  Stars: $STARS"

# 3. 检查 Release Notes (最新更新)
echo "📝 检查 Release Notes..."
curl -s "https://releasebot.io/updates/anthropic/claude-code" 2>/dev/null | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    if isinstance(d, list) and len(d) > 0:
        print(f\"  最新更新: {d[0].get('title','N/A')[:50]}\")
        print(f\"  时间: {d[0].get('date','N/A')}\")
except: pass
" 2>/dev/null || echo "  无法获取"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 监控完成"
echo "请使用 web_search freshness=pd 搜索具体内容"
