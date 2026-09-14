#!/bin/bash
# 监控 Claude Code 接入 GLM 报 400 [1210] 的修复情况
# 由 cron 调用，结果存 log；修复确认后由 heartbeat/AI 通知 Ken
LOG=/root/.openclaw/workspace/cc-glm-1210-monitor.log

echo "=== $(date '+%F %T') 检查 ===" >> "$LOG"

# 1. cc-switch issue #7236 状态（是否关闭/有修复回复）
ISSUE=$(curl -s "https://api.github.com/repos/farion1231/cc-switch/issues/7236" | jq -r '"state=\(.state) comments=\(.comments) updated=\(.updated_at)"')
echo "issue7236: $ISSUE" >> "$LOG"

# 2. Claude Code 最新版本
LATEST=$(npm view @anthropic-ai/claude-code version 2>/dev/null)
echo "latest_cc=$LATEST" >> "$LOG"

# 3. 搜索是否已有修复确认
FIX=$(curl -s "https://api.search.brave.com" >/dev/null 2>&1; echo "manual")
echo "note: 人工确认社区修复情况（web_search: claude code 1210 fixed）" >> "$LOG"
echo >> "$LOG"
