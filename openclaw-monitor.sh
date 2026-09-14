#!/bin/bash
# OpenClaw 动态监控脚本
# ⚠️ 只监控过去 24 小时的信息！

echo "🦞 OpenClaw 动态监控 - $(date '+%Y-%m-%d %H:%M:%S')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 检查是否有过去 24 小时内的重大更新
# 使用 freshness=pd (past day) 搜索

# 1. GitHub 最近 24 小时提交
echo "📦 检查 GitHub 最近提交..."
COMMITS_24H=$(curl -s "https://api.github.com/repos/openclaw/openclaw/commits?since=$(date -d '24 hours ago' -Iseconds)" 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d))" 2>/dev/null || echo "0")
echo "  过去24小时提交: $COMMITS_24H"

# 2. 版本发布（检查最近 7 天）
echo "📝 检查版本发布..."
RELEASE=$(curl -s "https://api.github.com/repos/openclaw/openclaw/releases?per_page=5" 2>/dev/null | python3 -c "
import json,sys,datetime
d=json.load(sys.stdin)
now = datetime.datetime.now()
for r in d:
    date = r['published_at'][:10]
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    if (now - dt).days <= 1:
        print(f\"{r['tag_name']}|{date}\")
" 2>/dev/null)

if [ -n "$RELEASE" ]; then
    echo "  最新发布: $RELEASE"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 监控完成"
echo "请使用 web_search freshness=pd 搜索具体内容"
