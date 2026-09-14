# HEARTBEAT.md

当收到以下特定 systemEvent 时，执行对应操作：

## ⏰ 每天例行检查（每天 4:00）

当收到包含"⏰ 每天例行检查"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/check-daily.sh`
2. 捕获脚本输出
3. 如果发现问题（退出码=1），通过飞书发送报告给 Ken（ou_a7195bd3e0508f0e0d09f19ff12a8811）
4. 使用 `message` 工具，action=send, channel=feishu, target=ou_a7195bd3e0508f0e0d09f19ff12a8811
5. 报告格式：显示检查结果 + 自动修复情况

> ⚠️ **已知问题**：cron-event 频道中使用 message 工具时，target 参数会被默认设置为 "heartbeat"，导致飞书发送失败。问题原因待查，目前记录到 memory 并在主会话中手动处理。

## ⏰ 每周中度检查（每周日 4:00）

当收到包含"⏰ 每周中度检查"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/check-weekly.sh`
2. 捕获脚本输出
3. 无论成功与否，都通过飞书发送报告给 Ken
4. 使用 `message` 工具，action=send, channel=feishu, target=ou_a7195bd3e0508f0e0d09f19ff12a8811
5. 报告格式：完整摘要 + 问题列表 + 修复建议

## ⏰ 每月大度检查（每月1日 4:00）

当收到包含"⏰ 每月大度检查"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/check-monthly.sh`
2. 捕获脚本输出
3. 无论成功与否，都通过飞书发送详细报告给 Ken
4. 使用 `message` 工具，action=send, channel=feishu, target=ou_a7195bd3e0508f0e0d09f19ff12a8811
5. 报告格式：完整审计报告 + 趋势分析 + 改进建议

## ⏰ 天气报告（每天 7:35）

当收到包含"⏰ 天气报告"或"天气提醒任务"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/weather-notify.sh`
2. 捕获脚本输出
3. 通过飞书发送给 Ken（ou_a7195bd3e0508f0e0d09f19ff12a8811）
4. 使用 `message` 工具，action=send, channel=feishu, target=ou_a7195bd3e0508f0e0d09f19ff12a8811

脚本输出的格式已经很好，直接发送即可。

## 📋 每日备份通知（每天 8:00）

当收到包含"📋 每日备份通知"或"备份完成通知"的消息时：

1. 检查 GitHub 最新提交时间
2. 通过飞书发送美化的备份通知给 Ken

格式示例：
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 每日备份通知
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 凌晨 3:00 已完成 GitHub 自动备份

📦 备份内容：
• IDENTITY.md（我的身份）
• MEMORY.md（长期记忆）
• SOUL.md（灵魂准则）
• inspiration.md（灵感汇总）

🔗 仓库：https://github.com/KenWang-dev/Openclawd_feishu

✅ 所有记忆安全保存
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

祝你有美好的一天！🪭
```

## ⏰ SSH 防护检查（每 5 分钟）

当收到包含"⏰ SSH 防护检查"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/ssh-protect.sh`
2. 捕获脚本输出
3. 如果有新封禁的 IP，记录到日志

---

# 其他时间

如果没有收到上述特定消息，回复：HEARTBEAT_OK

## 📋 待办清单检查（每天 1 次）

在没有特定任务时，可选择性检查待办清单：

1. 读取 `pending-tasks.md`
2. 检查是否有待处理事项
3. 如有重要待办，可提醒 Ken
