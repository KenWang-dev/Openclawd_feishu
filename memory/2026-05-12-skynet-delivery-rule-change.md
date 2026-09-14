# 天网监控投递规则变更

**日期：** 2026-05-12
**变更：** 子 agent 不再直接发送飞书消息给用户

## 背景
cron 子 agent 执行天网监控任务时，直接调用 message tool 发送飞书消息，导致：
1. 发送失败时静默降级，用户收不到报告
2. 主会话补发机制导致重复/分段消息
3. 用户在飞书聊天里收到多条分片消息

## 新规则
1. **子 agent 职责**：只做数据搜索 + 报告生成 + 本地存档 + 飞书知识库存档
2. **主 agent 职责**：收到 cron 完成通知后，审核报告内容，由主 agent 统一发送给用户
3. **投递方式**：主 agent 精简摘要后用 message tool 发一条飞书消息

## 执行操作
已修改 27 个任务配置文件（`skynet-monitor/references/tasks/` 下所有 .md）：
- 移除所有 `message({ action: "send", channel: "feishu", ... })` 代码
- 替换为警告文案：`⚠️ 子 agent 不得直接调用 message tool 发送飞书消息`
