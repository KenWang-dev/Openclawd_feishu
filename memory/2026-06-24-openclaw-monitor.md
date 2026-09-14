# OpenClaw 动态监控 - 2026-06-24

## 当前版本
- 本机安装: 2026.2.25（严重落后）
- 最新 stable: 2026.6.8
- 最新 pre-release: 2026.6.9

## 📦 版本更新

### 2026.6.9 (Pre-Release, ~6月19日)
- **事实**: 新 pre-release，含 Telegram 富文本 HTML 输出、独立 npm provider 插件、iOS Watch 控制代理、Codex GPT-5.3 Spark OAuth、全面 agent recovery 重构
- **是什么**: 让 Telegram 消息展示更丰富（表格、列表、引用块）；provider 插件化方便第三方接入；iOS Watch 可控制 agent；Codex 集成更深
- **洞察**: ClawStat.us 评估为 "Skip"（中等风险），有多个 breaking issues，建议观望 2026.6.10 再升级
- **参考**: https://senx.ai/openclaw-news/2026-06-19-openclaw-news

### 2026.6.8 (Stable, ~6月中旬)
- **事实**: 大版本更新，主要改进：
  - Telegram/WhatsApp 富文本投递更可靠
  - Agent recovery 全面强化（account-scoped DM、subagent 暂停、restart abort 等）
  - GLM-5.2 和 Claude Haiku 4.5 模型支持
  - Web search 默认行为更可预测（key-free provider 需显式 opt-in）
  - /usage 和 usage footer 原生渲染
  - UI/移动端优化（WebChat backscroll、session picker、iOS 重连等）
  - 内存和状态恢复更健壮（embedding batch 分割、SQLite NFS 修复等）
- **是什么**: 修复大量 channel 投递和 agent 运行时的稳定性问题，提升多模型路由安全性
- **洞察**: 本机版本落后太多（2.25 → 6.8），差了约 4 个月的更新，应该尽快升级
- **参考**: https://releasebot.io/updates/openclaw

## 🔧 竞品动态

### Hermes Agent (NousResearch)
- **事实**: NousResearch 发布 Hermes Agent，定位 "The agent that grows with you"，支持 `hermes claw migrate` 从 OpenClaw 迁移
- **是什么**: 开源竞品，CLI 风格类似 OpenClaw，支持多 provider、多 channel，主打可扩展性和多 agent
- **洞察**: Reddit r/hermesagent 社区活跃，有人讨论用 Hermes + OpenClaw + Engram 组合方案。值得持续关注但不急于切换

## 💬 社区热点

### AI Agent 安全危机
- **事实**: reco.ai 发文 "OpenClaw: The AI Agent Security Crisis Unfolding Right Now"，讨论 prompt injection 风险
- **是什么**: 本地运行的 agent 连接 LLM 后，通过消息平台的交互可能暴露安全风险
- **洞察**: OpenClaw 2026.6.9 pre-release 中已有相关安全改进，社区在持续关注

### GLM-5.2 争议
- **事实**: Reddit r/codex 讨论 "Are the GLM 5.2 glazers all Chinese bots?"
- **是什么**: GLM-5.2 发布后社区反馈两极分化，有人认为性能出色，有人质疑评价真实性
- **洞察**: OpenClaw 已添加 GLM-5.2 支持，Ken 当前使用 zai/glm-5-turbo，可关注 5.2 是否有显著提升

## ⚠️ 行动建议
1. **紧急**: 升级 OpenClaw 从 2026.2.25 到 2026.6.8 stable（跳过 6.9 pre-release）
2. **关注**: 2026.6.10 beta.2 已在 CI 验证中，预计近期发布
3. **可选**: 关注 Hermes Agent 发展，评估是否有值得借鉴的功能
4. **可选**: GLM-5.2 模型评估，看是否需要切换
