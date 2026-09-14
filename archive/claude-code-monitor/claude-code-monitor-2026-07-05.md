# 🦊 Claude Code 动态监控 - 2026年7月5日

## 📦 重磅更新：Claude Sonnet 5 成为默认模型

### Claude Sonnet 5（v2.1.197+）
- **事实**：Claude Sonnet 5 现在是 Claude Code 默认模型，原生 1M token 上下文窗口，促销价 $2/$10 per Mtok（截至 8月31日）
- **是什么**：Anthropic 推出了下一代旗舰模型，显著提升代码理解、生成和多文件上下文处理能力
- **洞察**：这是本周最大更新。1M 上下文对大型代码库来说是质变——可以一次性加载整个项目。促销期成本降低 50%，建议近期高强度使用

## 📦 Claude Code 最近多个版本关键更新

### v2.1.201（最新，7月3日）
- Claude Sonnet 5 会话不再使用 mid-conversation system role for harness reminders

### v2.1.200
- **事实**：权限模式默认改为 "Manual"，AskUserQuestion 不再自动继续
- **是什么**：提升安全性，防止 Claude 自动执行危险操作
- **洞察**：如果你习惯自动执行模式，需要在 /config 中重新配置

### v2.1.199
- **事实**：堆叠 slash 技能调用支持（/skill-a /skill-b 可同时加载最多5个技能）
- **事实**：Claude in Chrome 正式 GA
- **事实**：子代理（subagents）默认后台运行
- **是什么**：多技能编排能力增强，Chrome 版本成熟可用
- **洞察**：子代理后台运行是大改进——之前要等子代理完成才能继续，现在可以并行工作

### v2.1.198
- **事实**：Gateway 新增 Claude Platform on AWS (anthropicAws) 作为上游 provider
- **事实**：后台代理完成任务后自动 commit、push 并创建 draft PR
- **是什么**：AWS 生态集成加深，自动化工作流更完整
- **洞察**：如果你用 AWS，现在可以直接从 Claude Code 调用 AWS 托管的 Claude

### v2.1.197（Sonnet 5 首发）
- **事实**：Claude Sonnet 5 成为默认模型，1M 上下文，促销定价
- **事实**：新增组织默认模型设置、可点击文件附件、MCP 安全加固
- **是什么**：企业级管理能力和安全性增强
- **洞察**：管理员可以在组织控制台设置默认模型，对团队统一管理很实用

## 📦 其他值得关注的更新
- **Streaming idle watchdog** 默认开启：5 分钟无事件自动重试
- **Claude in Microsoft Foundry** 正式 GA
- **Trusted Devices** 功能：Team/Enterprise 远程控制前需验证设备
- **Fable 5 和 Mythos 5 恢复访问**
- **Claude Tag**：团队协作新功能
- **Claude Code 访问权限扩展到 Team plan Standard seats**

## 🔧 竞品动态

### Cursor
- **事实**：新增 Premium 席位（$120/seat/月，5x 用量），6月25日推出 Design Mode（视觉提示直接操作代理），6月29日推出 iOS 版 Cursor
- **是什么**：Cursor 正在向全平台扩展（桌面+iOS），并推出高用量企业定价
- **洞察**：iOS 版意味着移动端代码审查/轻量编辑成为可能，值得关注

### Windsurf / Devin
- **事实**：Cognition 已将 Windsurf 并入 Devin Desktop，windsurf.com/pricing 重定向到 devin.ai/pricing
- **是什么**：Windsurf 作为独立产品已终结，整合进 Devin 生态
- **洞察**：Coding IDE 市场正在整合，独立工具越来越难存活

### ZCode by Z.ai（新入局者）
- **事实**：7月初发布，基于 GLM-5.2 模型的免费 Agentic Coding IDE，支持 Win/Mac/Linux
- **是什么**：中国 AI 厂商进入 coding IDE 市场，以免费策略差异化竞争
- **洞察**：免费策略对价格敏感的独立开发者有吸引力，但模型能力和生态积累还需要时间验证

## 💬 用户反馈趋势
- 权限模式改默认 Manual 引发部分用户不满（习惯自动执行的用户需要重新配置）
- 后台代理稳定性大幅改善（大量 daemon crash、stale lock 相关 bug 修复）
- 子代理默认后台运行获得广泛好评
- 1M 上下文窗口被期待已久，用户反馈积极

---

*监控时间：2026-07-05 09:30 CST*
*下次检查：2026-07-06 09:30 CST*
