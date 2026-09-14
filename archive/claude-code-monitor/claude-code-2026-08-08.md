# Claude Code 动态监控存档 | 2026年8月8日

## 最新版本: v2.1.224 (Aug 7, 2026) + v2.1.225 (Aug 8)

### 📦 重大新功能

**1. Self-Hosted Environments (v2.1.224)**
- 事实: `claude self-hosted-runner` 命令，允许将自己的机器/容器作为 Claude Code web/mobile/desktop 的运行环境（Team & Enterprise）
- 是什么: 解决企业数据不出域的安全需求，推理仍发Anthropic但执行环境自主可控
- 洞察: 对有合规要求的组织是关键功能，但推理仍走云端

**2. Cross-Session SendMessage (v2.1.224)**
- 事实: Claude Code 会话之间可以互发消息，支持 ListAgents 发现，跨机器（macOS/Linux）
- 是什么: 多Agent协作的基础设施，类似OpenClaw的sessions_send
- 洞察: 这是Agent编排的重要能力，长任务可以拆分到多个session协作

**3. Archive Plugin Source (v2.1.224)**
- 事实: 从HTTPS zip安装插件，支持SHA-256 pinning，无需git/npm
- 是什么: 离线/受限环境下安装插件的能力
- 洞察: 配合self-hosted runner，形成完整的企业离线部署方案

**4. VSCode Focus View (v2.1.221)**
- 事实: Ctrl+Alt+F 切换，隐藏工具活动只展示摘要+运行指示器
- 是什么: 减少信息过载，让用户聚焦结果而非过程
- 洞察: 对非技术用户友好的改进

**5. Claude Opus 5 (v2.1.219, Jul 24)**
- 事实: claude-opus-5 成为默认Opus模型，1M上下文，fast mode $10/$50 per Mtok
- 是什么: 更强的模型+更大的上下文窗口+更低的fast mode价格
- 洞察: 性价比显著提升

### 🔒 安全修复重点

- v2.1.224: 沙箱 deny trailing slash 可被绕过（Linux/macOS）已修复
- v2.1.223: Bash权限绕过（隐藏命令）、权限对话框隐藏（tab/unicode padding）、workflow动态import逃逸沙箱
- v2.1.222: worktree隔离可运行破坏性git命令
- v2.1.221: zsh [[ ]] 中的隐藏命令执行
- v2.1.225: Gateway spend-limit支持，self-hosted-runner注册失败修复

### 🔧 竞品动态

**Windsurf → Devin Desktop**: Cognition于6月2日将Windsurf更名为Devin Desktop，价格不变（Free/$20/$200）

**NxCode排名**: Claude Code #1, Cursor #2, GitHub Copilot #4

**定价对比**: Copilot Pro $10/mo, Claude Code Pro $20/mo ($17 annual), Cursor Pro $20/mo

### 💡 趋势洞察

1. Claude Code 正在从"单会话编码助手"向"多Agent协作平台"演进（SendMessage + self-hosted + 200 subagent cap removed）
2. 安全加固是本轮更新的主题——连续4个版本修复沙箱/权限绕过问题
3. Team/Enterprise 功能差异化加速（self-hosted runner, cross-session messaging）
4. VSCode Focus View 说明 Anthropic 在争取非专业开发者用户
