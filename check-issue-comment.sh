#!/bin/bash
# 检查 OpenClaw issue #46840 是否有新评论

ISSUE_NUM="46840"
REPO="openclaw/openclaw"
TOKEN="${GITHUB_TOKEN:-$(gh auth token)}"
LOG_FILE="/root/.openclaw/workspace/issue-comment-check.log"

# 获取最新评论数
COMMENT_COUNT=$(curl -s "https://api.github.com/repos/$REPO/issues/$ISSUE_NUM/comments" \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))")

TODAY=$(date '+%Y-%m-%d')
LAST_CHECK=$(cat /root/.openclaw/workspace/issue-46840-last-check 2>/dev/null)
LAST_COUNT=$(cat /root/.openclaw/workspace/issue-46840-count 2>/dev/null)

echo "[$TODAY] 检查: 当前评论数=$COMMENT_COUNT, 上次记录=$LAST_COUNT" >> $LOG_FILE

if [ "$LAST_COUNT" != "$COMMENT_COUNT" ] && [ -n "$LAST_COUNT" ]; then
    # 有新评论
    NEW_COMMENTS=$((COMMENT_COUNT - LAST_COUNT))
    echo "发现新评论！"
    
    # 获取最新评论内容
    curl -s "https://api.github.com/repos/$REPO/issues/$ISSUE_NUM/comments?per_page=1" \
      -H "Authorization: token $TOKEN" \
      -H "Accept: application/vnd.github.v3+json" | python3 -c "
import json,sys
comments = json.load(sys.stdin)
if comments:
    c = comments[0]
    print(f\"用户: {c['user']['login']}\")
    print(f\"内容: {c['body'][:200]}\")
"
    
    # 发送通知给 Ken（通过飞书）
    curl -s -X POST "https://api.openclaude.ai/extensions/feishu/message" \
      -H "Content-Type: application/json" \
      -d '{
        "action": "send",
        "target": "ou_d81ad689104f8c660a5834c10740aea8",
        "message": "🔔 OpenClaw Issue #46840 有新评论！\n\n'${NEW_COMMENTS}' 条新评论，请查看: https://github.com/openclaw/openclaw/issues/46840"
      }'
fi

# 更新记录
echo "$COMMENT_COUNT" > /root/.openclaw/workspace/issue-46840-count
echo "$TODAY" > /root/.openclaw/workspace/issue-46840-last-check
