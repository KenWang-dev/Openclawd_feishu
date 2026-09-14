#!/bin/bash
# 监控 OpenClaw Issue #46840 和 #46832 直到关闭

REPO="openclaw/openclaw"
TOKEN="REDACTED_TOKENRnpkcandt1M0eZcGyaXy6lc4x1HL6D0dxnTL"
ISSUES=("46840" "46832")
LOG_FILE="/root/.openclaw/workspace/issue-monitor.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M')] $1" | tee -a $LOG_FILE
}

notify_ken() {
    local issue_num=$1
    local title=$2
    local comment=$3
    local url="https://github.com/$REPO/issues/$issue_num"
    
    # 发送飞书通知
    curl -s -X POST "https://api.openclaude.ai/extensions/feishu/message" \
      -H "Content-Type: application/json" \
      -d "{
        \"action\": \"send\",
        \"target\": \"ou_d81ad689104f8c660a5834c10740aea8\",
        \"message\": \"🔔 Issue #$issue_num 有新进展！\\n\\n**$title**\\n\\n$comment\\n\\n查看: $url\"
      }"
}

for ISSUE_NUM in "${ISSUES[@]}"; do
    log "检查 Issue #$ISSUE_NUM..."
    
    # 获取 issue 状态
    ISSUE_DATA=$(curl -s "https://api.github.com/repos/$REPO/issues/$ISSUE_NUM" \
      -H "Authorization: token $TOKEN" \
      -H "Accept: application/vnd.github.v3+json")
    
    STATE=$(echo "$ISSUE_DATA" | python3 -c "import json,sys; print(json.load(sys.stdin).get('state', 'unknown'))")
    TITLE=$(echo "$ISSUE_DATA" | python3 -c "import json,sys; print(json.load(sys.stdin).get('title', '')[:50])")
    LAST_COMMENT_COUNT=$(cat /root/.openclaw/workspace/issue-${ISSUE_NUM}-comments 2>/dev/null || echo "0")
    CURRENT_COMMENT_COUNT=$(curl -s "https://api.github.com/repos/$REPO/issues/$ISSUE_NUM/comments" \
      -H "Authorization: token $TOKEN" \
      -H "Accept: application/vnd.github.v3+json" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))")
    
    log "Issue #$ISSUE_NUM: state=$STATE, comments=$CURRENT_COMMENT_COUNT"
    
    # 检查是否有新评论
    if [ "$CURRENT_COMMENT_COUNT" -gt "$LAST_COMMENT_COUNT" ] && [ "$LAST_COMMENT_COUNT" -gt 0 ]; then
        log "Issue #$ISSUE_NUM 有新评论！"
        
        # 获取最新评论
        LATEST_COMMENT=$(curl -s "https://api.github.com/repos/$REPO/issues/$ISSUE_NUM/comments?per_page=1" \
          -H "Authorization: token $TOKEN" \
          -H "Accept: application/vnd.github.v3+json" | python3 -c "
import json,sys
comments = json.load(sys.stdin)
if comments:
    c = comments[0]
    print(f\"用户 @{c['user']['login']} 评论: {c['body'][:150]}...\")
")
        
        notify_ken "$ISSUE_NUM" "$TITLE" "$LATEST_COMMENT"
    fi
    
    # 更新评论数
    echo "$CURRENT_COMMENT_COUNT" > /root/.openclaw/workspace/issue-${ISSUE_NUM}-comments
    
    # 如果已关闭，记录并通知
    if [ "$STATE" = "closed" ]; then
        CLOSED_BEFORE=$(cat /root/.openclaw/workspace/issue-${ISSUE_NUM}-closed 2>/dev/null || echo "no")
        if [ "$CLOSED_BEFORE" = "no" ]; then
            log "🎉 Issue #$ISSUE_NUM 已关闭！"
            echo "yes" > /root/.openclaw/workspace/issue-${ISSUE_NUM}-closed
            notify_ken "$ISSUE_NUM" "$TITLE" "✅ Issue 已关闭！任务完成。"
        fi
    fi
done

# 检查是否所有 issue 都已关闭
ALL_CLOSED=true
for ISSUE_NUM in "${ISSUES[@]}"; do
    CLOSED=$(cat /root/.openclaw/workspace/issue-${ISSUE_NUM}-closed 2>/dev/null || echo "no")
    if [ "$CLOSED" = "no" ]; then
        ALL_CLOSED=false
        break
    fi
done

if [ "$ALL_CLOSED" = true ]; then
    log "🎉 所有监控的 Issue 都已关闭！"
    # 通知 Ken 任务完成
    curl -s -X POST "https://api.openclaude.ai/extensions/feishu/message" \
      -H "Content-Type: application/json" \
      -d '{
        "action": "send",
        "target": "ou_d81ad689104f8c660a5834c10740aea8",
        "message": "🎉 所有监控的 Issue 都已关闭！任务完成！\n\n- #46840 gateway stop/start\n- #46832 voice-call EADDRINUSE"
      }'
fi
