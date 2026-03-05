#!/bin/bash
# Karpathy Digest 自动执行脚本
# 每天 7:35 运行

cd /root/.openclaw/workspace/ai-daily-digest

export OPENAI_API_KEY="sk-MaotlYGe8iI54E3JJpECfK0aTk6gTQvt0NQ9aalnZ1GMvglp"
export OPENAI_API_BASE="https://aiberm.com/v1"
export OPENAI_MODEL="gemini-3-flash-preview"

# 运行 digest
npx -y bun scripts/digest.ts --hours 48 --top-n 10 --lang zh --output ./output/digest.md

# 提取关键内容并发送（这里只输出文件路径，后续通过 agent 发送）
echo "DONE: /root/.openclaw/workspace/ai-daily-digest/output/digest.md"
