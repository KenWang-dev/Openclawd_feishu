# Claude Code 从入门到精通自学手册

> **版本**: 2026年5月 | **基于**: Claude Code v2.x | **原则**: 第一性原理 × 帕累托法则 × MECE × 金字塔原理

---

## 引言：为什么 Claude Code 值得系统学习

Claude Code 不是一个"更聪明的 Copilot"。它是 Anthropic 推出的**终端级 AI 工程代理**——能读取你的代码库、执行命令、编辑文件、运行测试、自主完成从规划到实现的全流程。

**数据说话**：
- 2026年初，Claude Code 已占全球 GitHub 提交的 **4%**
- Spotify 工程师自 2025年12月起不再手动写代码
- Anthropic 内部每位工程师每天产出 **10-30 个 PR**

**核心定位**：Claude Code 是 Agent，不是 Chat。它理解你的整个代码库，而非只看到你粘贴的那几行。

---

## 第一部分：快速上手（Day 1）

### 1.1 安装与环境准备

**前置条件**：
- Node.js ≥ 18
- 终端环境（macOS/Linux/WSL）

```bash
# 全局安装
npm install -g @anthropic-ai/claude-code

# 首次启动（自动引导登录）
claude

# 验证安装
claude --version
```

**IDE 集成**（可选但推荐）：
- VS Code 扩展：在扩展市场搜索 "Claude Code" 安装
- 支持在编辑器内直接交互，无需切换终端

### 1.2 账户与订阅

| 方案 | 价格 | 适合人群 |
|------|------|----------|
| Free | $0 / 有每日用量限制 | 体验评估 |
| Pro | $20/月 | 个人开发者 |
| Max | $100/月或$200/月 | 重度用户 |
| Team | $30/人/月 | 团队协作 |
| Enterprise | 定制 | 企业级合规 |

> **💡 帕累托提示**：Pro 方案覆盖 80% 的个人使用场景，Max 适合全量依赖 Claude Code 工作的用户。

### 1.3 第一次对话：建立心智模型

在项目目录下启动 `claude`，输入你的第一条指令：

```
> /init
```

这会自动分析项目结构并生成 `CLAUDE.md`——Claude Code 的核心配置文件。

**关键心智转变**：
- ❌ 旧方式："我来写代码，你帮我审查"
- ✅ 新方式："我要什么效果，你来实现，我来验证"

---

## 第二部分：核心能力掌握（Day 1-3）

### 2.1 CLAUDE.md：你的项目宪法

CLAUDE.md 是 Claude Code 每次会话自动读取的配置文件。它决定了 Claude 如何理解你的项目。

**该写什么 vs 不该写什么**：

| ✅ 必须写 | ❌ 不要写 |
|-----------|-----------|
| 特殊的构建命令（Claude 猜不到的） | 语言默认规范（Claude 已经知道） |
| 项目特有的代码风格 | "写干净的代码"（废话） |
| 测试运行方式 | 详细的 API 文档（放链接即可） |
| Git 分支命名规则 | 文件级别的代码描述 |
| 已知的坑/非直觉行为 | 频繁变动的内容 |

**实战示例**：

```markdown
# CLAUDE.md
# 构建与测试
- 运行测试：pnpm test（不是 npm test）
- 单个测试：pnpm test -- path/to/file.test.ts
- 类型检查：pnpm typecheck

# 代码风格
- 使用 ES Modules（import/export），禁止 CommonJS
- 优先解构导入
- 中文注释，英文代码

# 架构约定
- API 路由在 src/routes/
- 数据模型在 src/models/
- 工具函数在 src/utils/
- 禁止直接操作 DOM，使用 React 组件

# 工作流
- 改完代码先跑类型检查
- commit 前确保测试通过
- PR 标题格式：feat/fix/refactor: 描述
```

**进阶技巧**：用 `@` 导入其他文件

```markdown
# 引用 README 了解项目全貌
@README.md

# 引用 Git 工作流规范
@docs/git-conventions.md
```

> **⚠️ 常见错误**：CLAUDE.md 太长。每多一行，Claude 就可能忽略一行。保持精简，只写"去掉会让 Claude 犯错"的内容。

### 2.2 四阶段工作流（最核心的方法论）

这是官方推荐的工作模式，也是 Boris Cherny（Claude Code 之父）的日常实践：

```
探索(Plan Mode) → 规划(Plan Mode) → 实现(Edit Mode) → 提交(Git)
```

**Phase 1：探索**
```
> 进入 Plan Mode
> 读取 src/auth/ 目录，理解我们的登录和会话管理机制
```
Claude 只读不写，回答你的问题。

**Phase 2：规划**
```
> 我要加 Google OAuth。哪些文件需要改？会话流程是什么？列一个计划。
```
按 `Ctrl+G` 可在编辑器中直接修改计划。

**Phase 3：实现**
```
> 按 Plan 实现 OAuth 流程。为回调处理器写测试，运行测试套件，修复所有失败。
```
切换到 Edit Mode，Claude 开始写代码。

**Phase 4：提交**
```
> commit 并开 PR
```

> **💡 何时跳过规划**：改动范围明确且很小（修 typo、加一行日志），直接做。如果你能用一句话描述 diff，就不需要规划。

### 2.3 Prompt 纪律：输入决定输出

| 低效 Prompt | 高效 Prompt |
|-------------|-------------|
| "修复登录 bug" | "用户报告登录后 session 超时会失败。检查 src/auth/ 的认证流程，特别是 token 刷新。写一个失败的测试复现问题，然后修复。" |
| "加个日历组件" | "看 src/components/ 下现有组件的实现模式，参照 DatePicker 组件的风格实现日历组件。支持月份选择和年份翻页。不用外部库。" |
| "写测试" | "为 foo.py 写测试，覆盖用户登出的边界情况。不要用 mock。" |

**提供验证手段**（这是最高杠杆的做法）：
- 给测试用例
- 给期望输出
- 给 UI 截图让 Claude 对比
- 让 Claude 运行测试自我验证

### 2.4 上下文管理：最稀缺的资源

**核心约束**：Claude 的上下文窗口会快速填满，性能随填充度下降。

**管理策略**：

1. **用 `@` 引用文件**而非在 prompt 中描述路径
2. **用管道传数据**：`cat error.log | claude`
3. **用 Subagent 做大量搜索**（详见第三部分）
4. **用 /compact 手动压缩上下文**
5. **监控上下文使用**：配置自定义状态栏

```json
// .claude/settings.json
{
  "statusLine": {
    "command": "echo \"$CLAUDE_CONTEXT_USAGE% context used | $CLAUDE_TOTAL_TOKENS tokens\""
  }
}
```

---

## 第三部分：进阶能力（Week 1-2）

### 3.1 Hooks：确定性系统控制

Hooks 是在特定生命周期事件触发的**确定性脚本**。与 prompt 不同，hooks 不会"理解偏差"——它要么执行，要么不执行。

**5 种 Hook 类型**：

| 类型 | 作用 | 典型场景 |
|------|------|----------|
| command | Shell 脚本 | 阻止危险命令 |
| http | HTTP POST 请求 | 集中策略控制 |
| mcp_tool | MCP 服务器工具 | 调用外部安全扫描器 |
| prompt | 单轮 LLM 评估 | 语义判断"这是不是密钥？" |
| agent | 子代理多步验证 | 复杂多步校验 |

**25 个生命周期事件（按使用频率排序）**：

**可阻塞事件（能阻止执行）**：
- `UserPromptSubmit` — 提交 prompt 前
- `PreToolUse` — 工具执行前（**最重要的安全检查点**）
- `PermissionRequest` — 权限请求时
- `Stop / SubagentStop` — 任务完成时
- `PreCompact` — 上下文压缩前

**信息性事件（仅记录/通知）**：
- `SessionStart / SessionEnd` — 会话生命周期
- `PostToolUse / PostToolUseFailure` — 工具执行后
- `SubagentStart` — 子代理启动

**退出码含义**：
- `0` = 成功
- `2` = 阻塞错误（stderr 反馈给 Claude，操作被阻止）
- `1` 或其他 = 非阻塞错误（首行 stderr 显示，继续执行）

**实战：阻止 rm -rf**

```bash
#!/bin/bash
# .claude/hooks/block-dangerous.sh
COMMAND=$(jq -r '.tool_input.command')
if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked"
    }
  }'
  exit 2
fi
exit 0
```

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash(rm *)",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/block-dangerous.sh"
      }]
    }]
  }
}
```

**实战：文件修改后自动运行 lint**

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "npx eslint $FILE_PATH --fix"
      }]
    }]
  }
}
```

### 3.2 Subagents：并行隔离的工作单元

Subagents 是独立上下文窗口中运行的 AI 实例。它的冗长输出（文件搜索、日志等）不会污染主会话——只有摘要返回。

**3 个内置 Subagent**：

| 名称 | 模型 | 工具权限 | 用途 |
|------|------|----------|------|
| Explore | Haiku | 只读 | 快速代码库搜索和分析 |
| Plan | 继承 | 只读 | 为 Plan Mode 做研究 |
| General-purpose | 继承 | 全部 | 复杂多步任务 |

**何时用 Subagent vs 主会话**：

| 场景 | 用 Subagent | 用主会话 |
|------|-------------|----------|
| 输出很冗长 | ✅ | ❌ |
| 需要工具限制（如只读审查） | ✅ | ❌ |
| 并行研究独立主题 | ✅ | ❌ |
| 需要频繁来回迭代 | ❌ | ✅ |
| 多阶段共享大量上下文 | ❌ | ✅ |

**创建自定义 Subagent**：

```markdown
<!-- .claude/agents/code-reviewer.md -->
---
name: code-reviewer
description: 高级代码审查专家。在修改代码后主动审查质量、安全性和可维护性。
tools: Read, Grep, Glob, Bash
disallowedTools: Write, Edit
model: sonnet
---

你是一名高级代码审查员。

审查清单：
1. 代码清晰可读
2. 函数和变量命名良好
3. 无重复代码
4. 错误处理完备
5. 无暴露的密钥或 API Key
6. 输入验证已实现
7. 测试覆盖充分

按优先级组织反馈：
- 严重问题（必须修复）
- 警告（应该修复）
- 建议（可以改进）
```

**调用方式**：
```
> 让 code-reviewer 审查认证模块的修改
> @code-reviewer (agent) 检查最近的 git diff
```

### 3.3 Skills：可复用的工作流封装

Skills 把重复使用的 prompt 模板打包成可调用的命令。

**Skills vs CLAUDE.md 的区别**：

| 维度 | CLAUDE.md | Skills |
|------|-----------|--------|
| 加载时机 | 每次会话自动加载 | 仅在被调用时加载 |
| 适合 | 项目约定、永久上下文 | 流程、规范、工作流 |
| 成本 | 始终占用上下文 | 用时才占用 |

**创建 Skill**：

```bash
mkdir -p ~/.claude/skills/secure-review
```

```markdown
<!-- ~/.claude/skills/secure-review/SKILL.md -->
---
name: secure-review
description: 安全聚焦的代码审查。在审查认证、授权或数据处理代码时使用。
context: fork
agent: Explore
disable-model-invocation: true
---

执行安全聚焦的代码审查：

1. 检查硬编码的密钥、API Key 或凭证
2. 验证输入验证和净化
3. 审查认证和授权逻辑
4. 检查 SQL 注入、XSS 和注入漏洞
5. 验证错误处理不泄露敏感信息

按严重级别报告发现，附具体文件引用。
```

**调用**：`/secure-review` 或 Claude 根据描述自动调用。

**动态上下文注入**：用 `!` 语法在加载时执行命令

```markdown
## PR 上下文
- PR diff: !`gh pr diff`
- PR 评论: !`gh pr view --comments`
- 变更文件: !`gh pr diff --name-only`
```

### 3.4 MCP：连接外部工具世界

MCP（Model Context Protocol）让 Claude Code 能操作你项目外部的工具和服务。

**配置方式**（`.mcp.json`）：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-notion"],
      "env": {
        "NOTION_API_KEY": "your-key"
      }
    }
  }
}
```

**高价值 MCP 连接**（帕累托 Top 5）：

| MCP Server | 连接服务 | 核心价值 |
|------------|----------|----------|
| @anthropic-ai/mcp-github | GitHub | 直接操作 Issue/PR/Code |
| @anthropic-ai/mcp-notion | Notion | 读写项目文档 |
| @anthropic-ai/mcp-slack | Slack | 消息和频道管理 |
| sentry-mcp | Sentry | 错误追踪分析 |
| @anthropic-ai/mcp-google-drive | Google Drive | 文档操作 |

**实战示例**：
```
> 查看 Sentry 中最近的 10 个错误，分析哪些与我的最新提交相关
> 从 Notion 中拉取所有未完成 action items，按负责人汇总
> 为 JIRA issue ENG-4521 实现功能并创建 GitHub PR
```

---

## 第四部分：高级工作流（Week 2-4）

### 4.1 Git Worktrees：并行开发不冲突

Git Worktrees 让你同时在多个分支上运行 Claude Code，互不干扰。

```
> 进入 worktree 功能
> EnterWorktree: feature/auth
# Claude 自动创建新 worktree 并切换

> EnterWorktree: feature/dashboard
# 在另一个终端中运行，独立上下文
```

**子代理隔离**：在 subagent 配置中设置 `isolation: worktree`

### 4.2 自主循环（Autonomous Loops）

**安全条件**：
- ✅ 有明确的成功标准（测试通过、lint 通过）
- ✅ 变更范围有限
- ✅ 有版本控制兜底（随时可回滚）
- ❌ 不确定的范围或没有验证手段的任务

```bash
# 让 Claude 自主循环直到所有测试通过
> /loop "运行测试套件，修复所有失败，直到全部通过"

# 让 Claude 自主重构
> /loop "重构 utils.ts，确保每个函数有测试，最终测试全绿"
```

### 4.3 Auto Mode：消除权限弹窗

按 `Shift+Tab` 或启动时 `--permission-mode auto`，Claude 在合理范围内自主决策，减少手动确认。

**适合场景**：
- 你完全信任的项目
- 有完善的 Hook 做安全网
- 快速原型开发

### 4.4 Claude Code on the Web

通过 `claude.ai/code` 在浏览器中使用 Claude Code，适合没有本地环境的场景。

### 4.5 Agent Teams（实验性）

多人协作的 Agent 团队，每个 Agent 扮演不同角色，通过结构化协议协调。

```bash
CLAUDE_CODE_ENABLE_AGENT_TEAMS=1 claude
```

### 4.6 Chrome 扩展

让 Claude Code 在浏览器中测试 UI 变更，自动截图对比：

```
> 安装 Chrome 扩展后，打开你的应用页面
> [截图] 实现这个设计。完成后截图对比差异
```

---

## 第五部分：实战案例（边学边练）

### 案例 1：从零搭建一个 TODO 应用（Day 1）

```
> 在当前目录创建一个 React + TypeScript TODO 应用
> 用 Plan Mode 先规划项目结构
> 包含：添加/删除/完成 TODO、本地存储持久化、筛选功能
> 实现后运行开发服务器验证
```

**学习重点**：体验四阶段工作流、理解 CLAUDE.md 的价值。

### 案例 2：重构遗留代码（Day 3）

```
> 读取 src/legacy/ 目录的代码
> 分析代码质量问题，给出重构计划
> 按计划逐步重构，每一步都运行测试确保不破坏功能
```

**学习重点**：Plan Mode 的真正价值、上下文管理。

### 案例 3：构建 CI/CD Pipeline（Week 1）

```
> 为这个项目创建 GitHub Actions workflow
> 包含：lint、test、build、deploy 三个 job
> PR 触发时只跑 lint 和 test
> main 分支 push 时完整部署
```

**学习重点**：Subagent 并行研究、Hook 自动化。

### 案例 4：集成 MCP 打造全流程工作台（Week 2）

```
> 配置 MCP 连接 GitHub + Notion + Sentry
> 实现工作流：从 Notion 获取需求 → 在 GitHub 创建 Issue → 完成后自动更新 Notion 状态
```

**学习重点**：MCP 配置和调试、跨服务自动化。

---

## 第六部分：常见陷阱与避坑指南

### 6.1 新手 Top 10 错误

| # | 错误 | 正确做法 |
|---|------|----------|
| 1 | 一次性给太大的任务 | 拆成小步骤，逐步验证 |
| 2 | 不给验证标准 | 始终提供测试/期望输出 |
| 3 | CLAUDE.md 太长 | 只写必要规则，定期精简 |
| 4 | 不用 Plan Mode | 不确定时先规划再动手 |
| 5 | 让 Claude "随便改" | 明确指定文件、范围、风格 |
| 6 | 忽略上下文窗口 | 监控使用率，及时 /compact |
| 7 | 不审查 Claude 的代码 | 每次提交前都要读一遍 |
| 8 | 一上来就全自主模式 | 先手动模式建立信任 |
| 9 | 不写 Hook 安全网 | 至少配 PreToolUse 阻止危险操作 |
| 10 | 不用版本控制 | 每次 Claude 操作前确保有 git 状态 |

### 6.2 过时内容标注

以下功能/模式在 2026 年已不推荐：

- ❌ **CLAUDE.md 中放长文档** → 改用 Skills 按需加载
- ❌ **不用 /init 而手写 CLAUDE.md** → 让 Claude 分析项目后生成
- ❌ **纯 chat 模式使用** → 用 Agent 模式（默认）
- ❌ **不用 Git Worktree 并行开发** → 这是 2026 年标准做法

---

## 第七部分：学习路线图（8 周计划）

| 周次 | 主题 | 目标 |
|------|------|------|
| **Week 1** | 安装配置 + 基础操作 | 能独立用 Claude Code 完成小功能开发 |
| **Week 2** | CLAUDE.md + 四阶段工作流 | 建立规范工作流程，Prompt 纪律 |
| **Week 3** | Plan Mode 深度实践 | 复杂功能先规划再实现 |
| **Week 4** | Hooks 基础 | 配置安全网和自动化检查 |
| **Week 5** | Subagents | 并行任务隔离，自定义代理 |
| **Week 6** | Skills + MCP | 封装工作流，连接外部工具 |
| **Week 7** | Git Worktrees + Auto Mode | 并行开发，高级工作流 |
| **Week 8** | 综合实战 | 端到端项目：从需求到部署 |

---

## 附录

### A. 常用命令速查

| 命令 | 说明 |
|------|------|
| `claude` | 启动交互式会话 |
| `claude "prompt"` | 非交互式执行 |
| `/init` | 生成 CLAUDE.md |
| `/compact` | 压缩上下文 |
| `/plan` | 切换到 Plan Mode |
| `/clear` | 清空对话历史 |
| `/cost` | 查看当前会话 token 消耗 |
| `/permissions` | 管理权限设置 |
| `/skills` | 查看可用 Skills |
| `/model` | 切换模型 |
| `cat file | claude` | 管道输入 |

### B. 配置文件层级

| 文件 | 作用域 | 用途 |
|------|--------|------|
| `~/.claude/settings.json` | 全局 | 个人偏好 |
| `~/.claude/skills/` | 全局 | 个人 Skills |
| `~/.claude/agents/` | 全局 | 个人 Subagents |
| `.claude/settings.json` | 项目 | 团队共享配置 |
| `.claude/settings.local.json` | 项目 | 个人本地配置（不入 git） |
| `CLAUDE.md` | 项目 | 项目约定 |
| `.claude/rules/` | 项目 | 规则文件 |

### C. 推荐学习资源

| 资源 | 类型 | 链接 |
|------|------|------|
| 官方文档 | 官方 | code.claude.com/docs |
| freeCodeCamp Handbook | 完整教程 | freecodecamp.org/news/claude-code-handbook |
| Boris Cherny 工作流 | 最佳实践 | twitter.com/bcherny |
| 菜鸟教程 | 中文入门 | runoob.com/claude-code |
| shanraisshan/best-practice | GitHub 精华 | github.com/shanraisshan/claude-code-best-practice |

---

> **本手册基于 2026 年 5 月公开资料整理。Claude Code 更新频繁，建议关注官方文档获取最新特性。**
>
> 整理方法：第一性原理（理解 Agent 本质）→ 帕累托法则（20% 功能覆盖 80% 价值）→ MECE（不重不漏分类）→ 金字塔原理（结论先行、逐层展开）
