# 🦊 Claude Code 动态监控 - 2026年7月7日

## 📦 新功能/版本更新

### 【Claude Sonnet 5 — Claude Code 新默认模型】
- **事实**：Sonnet 5 已成为 Claude Code 的默认模型，需更新至 v2.1.197。1M token 原生上下文窗口，128k max output。促销价 $2/$10 per MTok（截至 8月31日），之后恢复 $3/$15。
- **是什么**：Sonnet 5 是 Anthropic 迄今最 "agentic" 的 Sonnet 模型，在编码、agent 任务和知识工作上显著超越 4.6。三大行为变更：adaptive thinking 默认开启、禁止手动设置 sampling parameters（temperature/top_p/top_k）、移除 manual extended thinking。使用新 tokenizer，同样文本比 4.6 多约 30% tokens。
- **洞察**：对我们来说最重要的是 **新 tokenizer**——同样文本 token 数增加 ~30%，意味着成本和上下文容量都会变化。如果你在用 Sonnet 4.6，迁移前需要重新评估 max_tokens 预算和 token 计费。对 OpenClaw 这类重度使用者尤其要注意。

### 【Artifacts — Beta 开放】
- **事实**：Artifacts 功能进入 beta，Team 和 Enterprise 用户可以从 Claude Code CLI 或桌面端生成 live shareable pages，任何浏览器可查看。
- **是什么**：把 session 的输出变成实时可分享的网页，随 session 工作实时更新。适合做 demo、文档展示、结果分享。
- **洞察**：做技术分享或给同事展示代码分析结果时有用。对个人用户暂时没影响。

### 【Dynamic Workflow Size 设置】
- **事实**：`/config` 新增 "Dynamic workflow size" 设置（small/medium/large agent counts），为 workflow 调度的 subagent 数量提供指导性约束。
- **是什么**：从 Week 22 引入的 dynamic workflows 允许 Claude 编排数十到数百个 subagent，现在可以控制规模上限。
- **洞察**：如果在大项目中用 dynamic workflows，可以根据任务复杂度调整，避免资源浪费或 subagent 过多。

## 🌐 社区热点

### 【Claude Fable 5 重新部署 + 出口管制风波】
- **事实**：Fable 5 和 Mythos 5 在 6月9日发布后被美国出口管制暂停（仅 3 天），7月1日 Fable 5 全球重新部署，Mythos 5 部分恢复给约 100 家审核通过的机构。新增网络安全分类器，业界越狱攻击拦截率 >99%。
- **是什么**：这次事件暴露了 AI 模型作为基础设施的脆弱性——政府管制可以瞬间让产品停摆。Anthropic 的新网络安全框架和分类器是对此的回应。
- **洞察**：**对选型有参考意义**：依赖单一模型供应商有地缘政治风险。Fable 5 新增的网络安全 safeguard 可能会影响某些正常 coding 场景（安全分类器误判），需要注意。

### 【SpaceX 600亿美元收购 Cursor（Anysphere）】
- **事实**：SpaceX 正在敲定以约 600 亿美元收购 AI 编程工具 Cursor 母公司 Anysphere 的交易。
- **是什么**：这将是 AI 编码赛道最大收购案，反映大公司对 AI 编程能力的战略重视。
- **洞察**：Cursor 被收购后发展方向可能更偏向 SpaceX/航天工程场景，通用编程体验可能受影响。Claude Code 作为 Anthropic 亲儿子反而可能因此获得更多独立开发者青睐。

## 🔧 竞品动态

### 【Cursor — 新定价 + iOS 公测】
- **事实**：Cursor 新增 Premium 座位档位（5x 用量，$120/seat/月），iOS app 进入公开测试。Composer 2.5 在移动端 7月5日前 75% 折扣。
- **是什么**：针对重度使用 agent 的开发者推出高用量档位，说明 agent 模式的 token 消耗确实很高。
- **洞察**：定价策略的变化说明 AI coding 工具的成本模型正在从 "订阅制" 向 "用量敏感型" 演变。Claude Code 的 pay-as-you-go 模式在这一点上更有弹性。

### 【OpenAI GPT-5.6 驱动 Codex】
- **事实**：OpenAI 的 GPT-5.6 Sol/Terra/Luna 已成为 GitHub Codex 的驱动模型。Claude Code 2026 竞品对比更新至包含此版本。
- **是什么**：OpenAI 持续在 coding agent 赛道加码，模型能力迭代速度很快。
- **洞察**：Sonnet 5 的发布是 Anthropic 对 GPT-5.6 的直接回应。两者在 coding benchmark 上可能非常接近，实际体验需要测试。

## 💬 用户反馈

### 【Background Agent 稳定性改善】
- **事实**：过去几周的 release 大量修复了 background agent 的稳定性问题——包括 daemon 崩溃、stale lock、memory-starved machines、SSH cold-start 等。新增 streaming idle watchdog（默认开启，5分钟无事件自动重试）。
- **是什么**：说明 background agent 是 Claude Code 的重要增长方向，但之前存在大量可靠性问题。
- **洞察**：好消息是修复力度很大。如果你之前遇到过 background session 静默停止的问题，新版本应该好很多。watchdog 机制对长时间运行的任务是重要保障。

### 【Opus 4.7 Fast Mode 即将下线】
- **事实**：Opus 4.7 的 fast mode 将于 7月24日下线，需迁移到 Opus 4.8 fast mode。
- **洞察**：如果你在用 Opus 4.7 fast mode，记得在 7月24日前切换。

---

*数据来源：GitHub Releases、Claude Code Docs What's New、Anthropic Newsroom、Releasebot*
*下次检查：2026年7月8日 09:30*
