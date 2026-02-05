#!/bin/bash
# 自动备份脚本 - 每天凌晨 3 点执行

cd /root/.openclaw/workspace

# 添加所有相关文件
git add IDENTITY.md USER.md MEMORY.md SOUL.md inspiration.md
git add TODO.md TODOS.md TOOLS.md Claude.md 短视频制作方法.md

# 检查是否有变更
if git diff --cached --quiet; then
    echo "无变更，跳过备份"
    exit 0
fi

# 提交变更
DATE=$(date +"%Y-%m-%d %H:%M:%S")
git commit -m "自动备份：$DATE

- 备份核心记忆文件
- 备份个人文档

触发方式：定时任务（每天凌晨 3:00）"

# 推送到 GitHub
git push origin master

echo "备份完成：$DATE"
