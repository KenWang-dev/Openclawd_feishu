# OpenClaw 动态监控 - 2026年5月13日 (08:00 GMT+8)

## GitHub Releases

### v2026.5.8 (Pre-release, 5/12)
- Codex harness: auth-profile-backed media tools (image_generate) 兼容修复
- memory-wiki: admin scope 权限修复 (#80897, #80904)
- Control UI: 子 agent 会话在 session picker 中嵌套显示为 └─ 前缀 (#78623)
- Auto-reply: 模型后端失败时显示可见错误 (#80917)
- Agents/exec: 跳过子 agent 完成时的冗余心跳唤醒 (#66749)
- Provider streams: Azure Responses 流 bounded 诊断 (#80927)
- Cron: 新增 `openclaw cron get` 按 ID 查询单个 cron 任务 (#75117)
- **重大新功能**: per-sender tool policies — 按发送者身份限制危险工具 (#66933)
- Gateway/OpenAI HTTP: 支持 max_completion_tokens/max_tokens 透传
- Models/OpenAI CLI: `openclaw models auth login --provider openai` 默认启动 ChatGPT 账号登录
- ACP: 暴露 Gateway session lineage metadata (#73458)
- iMessage: BlueBubbles 切换路径文档化 (#80706)
- Fal: GPT Image 2 / Nano Banana 2 编辑路由支持
- Control UI: 白屏恢复面板 (#44107)

### v2026.5.7 (5/10)
- WhatsApp: LID forward mappings 修复 (#67378)
- WhatsApp: MEDIA 指令带 caption 不再发送空消息 (#78770)
- Codex/approvals: 原生 PermissionRequest hook 默认不安装，allow-always 记忆

### v2026.5.5 (5/5)
- Doctor/Codex OAuth: 修复 #78407
- Telegram: polling watchdog 绑定 getUpdates liveness (#78422)
- Subagents: archiveAfterMinutes 配置化

## 当前安装版本
- **本地**: v2026.2.25（落后 4 个版本）

## 🔥 业界重大新闻

### 【Hermes Agent v0.13.0 "Tenacity" 发布，多家媒体称"正在碾压 OpenClaw"】
- 事实：Nous Research 的 Hermes Agent 发布 v0.13.0，864 commits / 295 contributors / 一周内
- 是什么：自改进 AI agent，内置学习循环，默认开启数据脱敏
- 安全：修复 8 个 P0 安全漏洞（包括 Discord 跨服消息、WhatsApp 陌生人拒绝、TOCTOU 等）
- 竞争态势：eWeek、The Neuron Daily、MarkTechPost 均报道"用户从 OpenClaw 迁移到 Hermes"
- Reddit 民调声称约 30% OpenClaw 用户已切换
- CVE-2026-7113: Hermes v0.8.0 webhooks 缺少认证（CVSS 5.6 Medium）

### 【HN 热帖："OpenClaw had a rough week"】（2天前）
- 讨论 OpenClaw 供应链安全担忧（大量未审查 npm 依赖）
- 多位用户表示已迁移到 Hermes Agent 或 picoclaw
- 正面声音：家庭自动化、日历管理、语音控制等实际使用场景
- 一位前重度用户分享 7 个深度使用场景（智能家居、聊天监控、车源查找、日程规划等）

### 【WireClaw — OpenClaw 移植到 ESP32】
- r/Arduino_AI 热帖：WiFi MCU 上的 OpenClaw
- ESP32 & Pico W 支持，80KB RAM 运行
- 物联网 agent 赛道新玩家

### 【r/OpenAI: "OpenClaw is trending down"】
- 帖子声称 OpenClaw 走向衰落
- 社区纠正：OpenClaw 是开源项目，未被 OpenAI 收购

## 趋势分析
- OpenClaw 生态竞争加剧：Hermes Agent 自改进特性、picoclaw 轻量化、WireClaw 物联网化
- 安全与供应链成为焦点议题（HN 帖子 + SecurityScorecard 报告）
- 本地版本严重落后（v2026.2.25 vs v2026.5.8），建议尽快升级
