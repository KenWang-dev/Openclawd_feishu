# Claude Code 从入门到精通自学手册

> 📅 更新时间：2026年5月  
> 📊 数据点：截至2026年2月，Claude Code 已占全球 GitHub 公开提交的 4%（约13.5万次/天），Anthropic 自身 90% 的代码由 AI 编写  
> 🔗 主要参考：[Claude Code 官方文档](https://code.claude.com/docs/en/overview)、[freeCodeCamp 手册](https://www.freecodecamp.org/news/claude-code-handbook/)、[Blake Crosley 完全指南](https://blakecrosley.com/guides/claude-code)、社区实践

---

## 一、基础概念

### 1.1 Claude Code 是什么？

Claude Code 是 Anthropic 推出的**代理式编码工具（Agentic Coding Tool）**，不是一个聊天机器人，而是一个能在你的代码库中**读取文件、编辑代码、运行命令、创建提交和 PR** 的自主 AI 代理。

**核心特点：**
- 🔧 能理解整个代码库，跨多个文件工作
- 🤖 具有"代理循环"——不只是回答问题，而是自主探索、规划、实现、验证
- 🔌 支持多种环境：终端 CLI、VS Code、JetBrains、桌面应用、Web 浏览器
- 🌐 可通过 MCP 连接外部工具（数据库、GitHub、Slack 等3000+集成）
- 📱 支持跨设备：终端→手机→桌面无缝切换

**官方数据（来源：Anthropic 官方）：**
- Spotify 工程师自2025年12月起不再手动编写代码
- Anthropic 内部每位工程师每天产出10-30个PR
- 自2025年初研究预览以来13个月内增长42,896倍

### 1.2 安装与配置

#### 安装方式

```bash
# macOS / Linux / WSL（推荐：原生安装器）
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Homebrew（macOS）
brew install --cask claude-code

# WinGet（Windows）
winget install Anthropic.ClaudeCode

# Linux 包管理器（Debian/Fedora/Alpine）
# 详见 https://code.claude.com/docs/en/setup
```

**注意：** 原生安装器会自动后台更新。Homebrew 和 WinGet 安装需要手动更新。

#### 系统要求
| 平台 | 最低版本 | 备注 |
|------|---------|------|
| macOS | 13+ | Intel 和 Apple Silicon 均支持原生二进制 |
| Linux | Ubuntu 20.04+ / Debian 10+ | 需要 glibc 2.30+ |
| Windows | 10+ (x64/ARM64) | 推荐 WSL2 或安装 Git for Windows |
| RAM | 4GB 最低 | |
| Node.js | 18+（仅旧版 npm 安装路径需要）| |

#### 首次启动

```bash
cd your-project
claude          # 进入交互式会话
```

首次运行会提示登录。支持：
- Claude Pro / Max / Team / Enterprise 订阅
- Anthropic Console API Key（按token付费）
- 第三方提供商（Terminal CLI 和 VS Code 支持）

### 1.3 核心架构：三层模型

```
┌─────────────────────────────────────────────────────────┐
│                   扩展层 (Extension Layer)               │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │   MCP   │ │  Hooks  │ │  Skills │ │ Plugins │       │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘       │
├─────────────────────────────────────────────────────────┤
│                   委托层 (Delegation Layer)              │
│  ┌─────────────────────────────────────────────────┐   │
│  │         Subagents（最多10个并行）                  │   │
│  │  探索 | 规划 | 通用 | 自定义                        │   │
│  └─────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│                   核心层 (Core Layer)                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │          主对话上下文（200K tokens 标准）           │   │
│  │    工具: Read, Edit, Bash, Glob, Grep 等         │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**关键洞察（来源：Blake Crosley 指南）：** 大多数用户只在核心层工作，看着上下文膨胀、成本攀升。高效用户将探索和专业化工作推到委托层，在扩展层配置工作流，核心层只用于编排和最终决策。

### 1.4 CLAUDE.md —— 最核心的概念

CLAUDE.md 是 Claude Code 每次会话开始时自动读取的特殊 Markdown 文件。它是项目的"持久上下文"。

**文件位置与加载优先级：**
| 位置 | 作用域 | 说明 |
|------|--------|------|
| `~/.claude/CLAUDE.md` | 全局 | 应用于所有 Claude 会话 |
| `./CLAUDE.md` | 项目根 | 提交到 git，团队共享 |
| `./CLAUDE.local.md` | 项目个人 | 加入 `.gitignore`，不共享 |
| 父目录 | 单仓库 | 适合 monorepo |
| 子目录 | 按需加载 | Claude 在该目录工作时自动加载 |
| `.claude/rules/` | 路径匹配 | 使用 `paths` frontmatter 精准控制 |

**有效的 CLAUDE.md 示例：**
```markdown
# Code style
- Use ES modules (import/export), not CommonJS (require)
- Destructure imports when possible

# Workflow
- Always typecheck after making code changes
- Prefer running single tests, not the whole suite

# Build & Test
- Build: pnpm build
- Test: pnpm test -- --reporter=dot
- Lint: pnpm lint

# Never do
- Never edit .env files directly
- Never commit to main branch
```

**最佳实践：**
- ✅ 用 `/init` 自动生成基础版本，再逐步完善
- ✅ 保持简洁（官方建议200行以内）
- ✅ 只写 Claude 无法从代码推断的信息
- ✅ 使用 `@path/to/file` 语法导入其他文件
- ✅ 加入强调词（如 `IMPORTANT`、`YOU MUST`）提高遵循度
- ❌ 不要把 CLAUDE.md 当 wiki 倾倒所有文档
- ❌ 不要写 Claude 已经知道的标准语言规范
- ❌ 不要写频繁变化的信息

---

## 二、核心操作

### 2.1 日常最关键的命令

#### 斜杠命令速查表

| 命令 | 功能 | 使用场景 |
|------|------|---------|
| `/init` | 自动生成 CLAUDE.md | 新项目首次配置 |
| `/clear` | 清空当前对话 | 上下文太满时重新开始 |
| `/compact` | 压缩对话历史 | 释放上下文空间，保留关键信息 |
| `/rewind` | 回滚对话和/或代码 | Claude 走错方向时，回到上一个好状态 |
| `/context` | 查看当前上下文使用情况 | 监控 token 消耗 |
| `/cost` | 查看当前会话费用 | 控制预算 |
| `/model` | 切换模型 | 根据任务复杂度选择 |
| `/hooks` | 查看已配置的钩子 | 调试钩子配置 |
| `/permissions` | 管理权限 | 配置允许列表 |
| `/help` | 帮助文档 | 查看所有可用命令 |
| `/fork [name]` | 在当前点分叉对话 | 探索不同方案 |
| `/schedule` | 创建定时任务 | 设置周期性工作 |
| `/loop` | 在会话中重复执行提示词 | 快速轮询 |
| `/desktop` | 将终端会话转移到桌面应用 | 可视化查看差异 |
| `/login` | 登录认证 | 首次使用 |

#### CLI 非交互模式（管道 & 脚本）

```bash
# 分析日志
tail -200 app.log | claude -p "Slack me if you see any anomalies"

# CI 中自动翻译
claude -p "translate new strings into French and raise a PR for review"

# 批量操作
git diff main --name-only | claude -p "review these changed files for security issues"

# 指定模型和轮次
claude -p "Review this diff" --model sonnet --max-turns 5
```

### 2.2 Plan Mode（规划模式）

**这是最被低估的功能之一。**

规划模式让 Claude 探索和规划但不修改任何文件。强烈推荐的四阶段工作流：

```
第一阶段：探索（Plan Mode）
→ claude (plan mode): "read /src/auth and understand how we handle sessions"

第二阶段：规划（Plan Mode）
→ claude (plan mode): "I want to add Google OAuth. What files need to change?"

第三阶段：实现（Default Mode）
→ claude: "implement the OAuth flow from your plan. write tests, run them."

第四阶段：提交（Default Mode）
→ claude: "commit with a descriptive message and open a PR"
```

**快捷键：** `Ctrl+G` 可将规划打开到文本编辑器中直接编辑。

**何时跳过规划：** 改动范围明确的小修改（修复拼写、添加日志行、重命名变量）。

### 2.3 权限模式

| 模式 | 特点 | 适用场景 |
|------|------|---------|
| **Default（默认）** | 每个可能修改系统的操作都需要手动批准 | 刚开始使用 |
| **Auto Mode** | 分类器模型自动审核，仅阻止高风险操作 | 信任任务方向，减少点击 |
| **权限白名单** | 指定特定工具/命令免审批 | 已知的 安全命令如 `npm run lint` |
| **Sandbox（沙盒）** | OS 级别隔离，限制文件系统和网络访问 | 安全敏感环境 |

### 2.4 @ 引用和富内容输入

```bash
# 引用文件
claude "explain @src/auth/login.ts"

# 管道输入
cat error.log | claude "what's wrong?"

# 直接粘贴图片（截图、设计稿）
# 在对话中直接 Ctrl+V 或拖拽
```

### 2.5 模型选择策略

| 模型 | 适用场景 | 成本 |
|------|---------|------|
| **Opus** | 复杂架构推理、大规模重构、难题 | 最高 |
| **Sonnet** | 日常编码、bug修复、功能实现 | 中等 |
| **Haiku** | 快速探索、简单查询、大量文件搜索 | 最低 |

**高级策略：** 将子代理的探索任务路由到便宜模型，核心决策保留 Opus。

---

## 三、进阶功能

### 3.1 Hooks（钩子）

**核心概念：** Hooks 是在 Claude Code 生命周期特定点自动执行的 shell 命令。与 CLAUDE.md 中的指令不同，**Hooks 是确定性的——保证每次都执行**。

#### 生命周期事件

| 事件 | 触发时机 | 典型用途 |
|------|---------|---------|
| `PreToolUse` | 工具执行前 | 阻止危险操作、修改输入 |
| `PostToolUse` | 工具执行后 | 自动格式化、lint检查 |
| `Notification` | Claude 等待输入时 | 桌面通知 |
| `SessionStart` | 会话开始时 | 注入上下文 |
| `Stop` | Claude 完成任务时 | 最终检查、写入记忆 |

**退出码含义：**
- `0` = 允许继续
- `2` = 阻止操作（Claude 收到原因并调整）

#### 实战示例

**1. 自动格式化（PostToolUse）**
```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
        }]
      }
    ]
  }
}
```

**2. 阻止编辑受保护文件（PreToolUse）**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": ".claude/hooks/protect-files.sh"
        }]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# .claude/hooks/protect-files.sh
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/")
for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Blocked: $FILE_PATH matches protected pattern '$pattern'" >&2
    exit 2
  fi
done
exit 0
```

**3. 阻止危险 Bash 命令**
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "if [[ \"$CLAUDE_TOOL_INPUT\" == *\"rm -rf\"* ]]; then echo 'Dangerous command blocked!' && exit 2; fi"
      }]
    }]
  }
}
```

**4. PR 前必须通过测试**
```bash
#!/bin/bash
# .claude/hooks/pre-pr-requires-tests.sh
if pnpm -s test -- --reporter=dot; then
  exit 0
else
  echo "Tests are failing. Fix tests before creating a PR." >&2
  exit 2
fi
```

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "mcp__github__create_pull_request",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/pre-pr-requires-tests.sh"
      }]
    }]
  }
}
```

**5. 压缩后重新注入上下文**
```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "compaction",
      "hooks": [{
        "type": "command",
        "command": "echo 'Remember: you are working on the auth module refactor. Current status: OAuth implemented, session handling pending.'"
      }]
    }]
  }
}
```

**Hook 类型扩展（2026年新增）：**
- **Prompt Hook**：用 LLM 评估是否应执行某操作
- **HTTP Hook**：发送 HTTP 请求
- **Subagent Hook**：触发子代理执行

### 3.2 Skills（技能）

Skills 是可复用的 Markdown 文件，包含知识、工作流或指令。

#### 创建技能

```markdown
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

#### 可调用的工作流技能

```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes
5. Write and run tests to verify
6. Create a descriptive commit message
7. Push and create a PR
```

使用：`/fix-issue 1234`

**技能位置：** `.claude/skills/` 目录下

**关键区别：**
- Skill vs CLAUDE.md：CLAUDE.md 每次加载，Skills 按需加载
- Skill vs Hook：Skill 由 Claude 解释执行（非确定性），Hook 是确定性执行
- 设置 `disable-model-invocation: true` 防止有副作用的技能被自动触发

### 3.3 Subagents（子代理）

**子代理是在隔离上下文中运行的独立工作单元，完成后只返回摘要。**

#### 子代理的优势
- **上下文隔离**：大量文件读取不会污染主对话
- **并行执行**：最多10个子代理同时运行
- **模型分层**：子代理可使用便宜模型做探索
- **成本控制**：只消耗子代理自己的 token

#### 使用场景
| 场景 | 示例 |
|------|------|
| 研究任务 | "搜索代码库了解认证流程，返回关键发现" |
| 并行任务 | 同时研究前端和后端方案 |
| 验证任务 | "检查这个修改是否影响其他模块" |
| 大量文件操作 | 读取几十个文件但只需要结论 |

#### 何时使用子代理 vs 留在主对话
- **用子代理**：生成大量工具输出的任务、可并行的子任务、上下文快满时
- **留在主对话**：简单的顺序单步任务

### 3.4 Agent Teams（代理团队）—— 实验性功能

**子代理的升级版**：多个独立的 Claude Code 会话，通过**邮箱系统**进行点对点通信。

**与子代理的区别：**
| 特性 | 子代理 | 代理团队 |
|------|--------|---------|
| 上下文 | 独立，结果返回调用者 | 独立，完全独立 |
| 通信 | 只向主代理报告 | 队友间直接通信 |
| 协调 | 主代理管理所有工作 | 共享任务列表，自协调 |
| 适用场景 | 只需结果的聚焦任务 | 需要讨论和协作的复杂工作 |
| Token 成本 | 较低 | 较高 |

**配置：** 需要在设置中显式启用（实验性功能）。

### 3.5 MCP 集成（Model Context Protocol）

MCP 是连接 Claude Code 到外部服务的开放标准协议。

#### 添加 MCP 服务器

```bash
# 基本用法
claude mcp add <name> <command> [args...]

# 示例：添加 GitHub MCP
claude mcp add github npx -y @anthropic-ai/mcp-server-github

# 示例：添加数据库
claude mcp add postgres npx -y @anthropic-ai/mcp-server-postgres

# 查看已添加的
claude mcp list

# 移除
claude mcp remove <name>
```

#### MCP 作用域优先级
```
local > project > user
```

#### 常见 MCP 服务器
| 服务器 | 用途 |
|--------|------|
| `@anthropic-ai/mcp-server-github` | GitHub 集成 |
| `@anthropic-ai/mcp-server-postgres` | PostgreSQL 数据库 |
| `@anthropic-ai/mcp-server-slack` | Slack 集成 |
| `@anthropic-ai/mcp-server-google-drive` | Google Drive |
| `@anthropic-ai/mcp-server-brave-search` | Brave 搜索 |
| `@anthropic-ai/mcp-server-memory` | 持久记忆 |
| Figma MCP | 设计稿集成 |
| Sentry MCP | 错误监控 |

**MCP vs Skill 区别：** MCP 给 Claude 连接外部系统的**能力**；Skill 给 Claude 使用这些系统的**知识**。两者互补。

### 3.6 Plugins（插件）—— 2026年新增

插件是**打包分发**机制，将 Skills、Hooks、Subagents、MCP 服务器捆绑为一个可安装单元。

- 通过 `/plugins` 安装
- 插件技能带命名空间（如 `/my-plugin:review`）
- 适合跨仓库复用和团队分发
- 支持 **Plugin Marketplaces**

### 3.7 多模态能力

- **图片输入**：在终端中粘贴或拖拽图片（截图、设计稿、架构图）
- **Chrome 扩展**：Claude in Chrome 可在浏览器中打开新标签页测试 UI
- **Voice Mode（2026年3月）**：语音交互模式

---

## 四、高级技巧

### 4.1 性能优化

#### 上下文窗口管理（最重要！）

**核心理念：** Claude 的上下文窗口是最重要的资源。90% 使用率时，不仅更慢，还会"变笨"——重要指令被埋没、早期上下文丢失、开始犯低级错误。

**优化策略：**

1. **精简 CLAUDE.md**
   - 每行问自己："删除这行会导致 Claude 犯错吗？"不会就删
   - 目标：200行以内
   - 用 `.claude/rules/` + `paths` frontmatter 精准控制加载

2. **善用 /compact 和 /clear**
   - 上下文到 70-80% 时主动 `/compact`
   - 走错方向时用 `/rewind` 回到上一个好状态（不要继续错上加错）
   - 完全卡住时 `/clear` 重新开始

3. **推工作到子代理**
   - 大量文件探索 → 子代理
   - 只需结论的研究 → 子代理
   - 主对话保持干净

4. **监控工具**
   - `/context` 查看上下文使用量
   - 配置自定义状态行持续监控
   - `/cost` 查看费用

#### 模型路由优化

```bash
# 简单任务用 Haiku
claude --model haiku -p "what does this function do?"

# 日常开发用 Sonnet
claude --model sonnet -p "fix the bug in auth.ts"

# 复杂架构用 Opus
claude --model opus -p "redesign the data layer for horizontal scaling"
```

### 4.2 自动化工作流

#### CLI 管道组合

```bash
# 监控日志异常
tail -f app.log | claude -p "alert me on errors"

# PR 差异审查
git diff origin/main...HEAD | claude -p "review for security issues"

# 代码库搜索
git grep "TODO" | claude -p "prioritize these items"
```

#### Git Worktree 并行工作

```bash
# 创建 worktree
claude --worktree feature-a  # 在隔离的 git 分支中工作
claude --worktree feature-b  # 另一个隔离分支

# 注意（v2.1.133+）：默认从 origin/<default> 创建
# 要保留未推送的提交，设置 worktree.baseRef: "head"
```

#### 定时任务（Routines & /loop）

```bash
# 在 CLI 会话中重复执行
/loop "check for new issues and summarize" --interval 30m

# Routines（Anthropic 基础设施）
/schedule  # 创建定时任务
```

Routines 运行在 Anthropic 管理的基础设施上，即使你的电脑关机也会继续运行。也支持 API 调用和 GitHub 事件触发。

### 4.3 GitHub Actions 集成

#### 自动 PR 审查

```yaml
# .github/workflows/claude-auto-review.yml
name: Claude Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
permissions:
  contents: read
  pull-requests: write
jobs:
  auto_review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
      - name: Run AI Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ github.token }}
        run: |
          claude -p "Review this PR diff for code quality issues. Comment on problems." --max-turns 5
```

#### @claude 触发

在 PR 或 issue 中 `@claude` 提及，Claude 会自动分析代码并实现修改。

#### 差异大小控制

```bash
DIFF=$(git diff origin/main...HEAD)
DIFF_SIZE=$(echo "$DIFF" | wc -c)
if [ "$DIFF_SIZE" -gt 100000 ]; then
  echo "Diff too large for AI review ($DIFF_SIZE bytes). Skipping."
  exit 0
fi
```

### 4.4 团队协作最佳实践

1. **CLAUDE.md 提交到 Git**：让团队共同维护项目约定
2. **CLAUDE.local.md 放入 .gitignore**：个人偏好不共享
3. **创建共享 Skills**：团队通用的审查清单、部署流程
4. **MCP 统一配置**：通过项目级 settings.json 共享工具连接
5. **Plugin 分发**：将团队工具链打包为 Plugin
6. **Git 分支约定**：在 CLAUDE.md 中明确定义分支命名和 PR 流程

---

## 五、实战案例

### 5.1 从零构建应用（Plan Mode 工作流）

```bash
# 1. 探索（Plan Mode）
claude> "I want to build a task management app with React + Node.js. 
         Read the current project structure and tell me what exists."

# 2. 规划（Plan Mode，Ctrl+G 编辑）
claude> "Create a detailed implementation plan for: 
         - User authentication with JWT
         - CRUD endpoints for tasks
         - React frontend with drag-and-drop
         Output a step-by-step plan."

# 3. 逐功能实现（Default Mode）
claude> "Implement step 1 from the plan: set up Express server with auth middleware.
         Write tests for the auth endpoints. Run them."

# 4. 验证
claude> "Run the full test suite and fix any failures."
```

### 5.2 自动修复 GitHub Issue

```bash
# 创建 Skill
# .claude/skills/fix-issue/SKILL.md
---
name: fix-issue
description: Automatically fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.
1. Use `gh issue view $ARGUMENTS` to get details
2. Search the codebase for relevant files
3. Implement the fix
4. Write and run tests
5. Commit and create a PR

# 使用
claude> /fix-issue 1234
```

### 5.3 全栈 PR 审查自动化

```yaml
# .github/workflows/full-review.yml
name: Full Claude Review Pipeline
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Review this PR specifically for security vulnerabilities.
            Check for: SQL injection, XSS, auth bypass, sensitive data exposure.
            
  code-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Review code quality: naming, structure, test coverage,
            error handling, and adherence to project conventions in CLAUDE.md.
```

### 5.4 使用子代理进行大规模代码迁移

```bash
claude> "I need to migrate all class components to hooks in this React project.
         Spawn subagents to: 
         1. Research agent: Find all class components and list them
         2. For each component, spawn a subagent to do the migration
         3. After all migrations, run the test suite"
```

### 5.5 利用 Hook 系统构建质量控制管线

```
SessionStart → 注入项目上下文
    ↓
PreToolUse [Bash] → 阻止 rm -rf 等危险命令
    ↓
PreToolUse [Edit|Write] → 阻止编辑 .env 等受保护文件
    ↓
PostToolUse [Edit|Write] → 自动运行 Prettier 格式化
    ↓
PostToolUse [Edit|Write] → 运行 ESLint 并将结果反馈给 Claude
    ↓
PreToolUse [mcp__github__create_pull_request] → 确保测试通过才允许创建 PR
    ↓
Stop → 最终验证 + 写入记忆
```

---

## 六、常见坑点

### 6.1 ❌ 新手最常见的错误

#### 1. CLAUDE.md 写成 wiki 倾倒场
**问题：** 把所有文档塞进去，导致每次会话加载 20000+ tokens，Claude 忽略重要指令。  
**解决：** 每行问"删了会出错吗？"不会就删。超过200行就拆分到 `.claude/rules/` 或 Skills。

#### 2. 不使用 Plan Mode 直接开始编码
**问题：** Claude 跳过探索直接写代码，结果解决的是错误的问题。  
**解决：** 不确定的任务先用 Plan Mode，明确的小修改可以直接做。

#### 3. 上下文满了还继续
**问题：** 90% 上下文使用率时 Claude 开始"遗忘"和犯错。  
**解决：** 定期 `/compact`，走错方向立即 `/rewind`，卡住了 `/clear` 重来。

#### 4. 走错方向不回退
**问题：** Claude 出错了继续让它修，错误累积、上下文被污染。  
**解决：** 用 `/rewind`（或 Esc Esc）回到最后一个好状态，不要在错误基础上修。

#### 5. 不提供验证方式
**问题：** "实现一个邮箱验证函数"——Claude 可能产生看起来对但实际不工作的代码。  
**正确做法：** "写一个 validateEmail 函数。测试用例：user@example.com → true, invalid → false。实现后运行测试。"

#### 6. 权限审批疲劳
**问题：** 第十个审批后你不再认真看，只是机械点"允许"。  
**解决：** 配置 Auto Mode 或权限白名单。

#### 7. 所有东西都放主对话
**问题：** 大量文件探索填满上下文。  
**解决：** 需要读取大量文件时用子代理，只要结论。

### 6.2 ⚠️ 过时信息标注

| 过时信息 | 当前正确信息 |
|---------|------------|
| 旧版安装方式：`npm install -g @anthropic-ai/claude-code` | 推荐使用原生安装器 `curl -fsSL https://claude.ai/install.sh \| bash`（v2.1.113+ 默认为原生二进制） |
| Homebrew `brew install anthropic/claude/claude` | 改为 `brew install --cask claude-code` |
| `claude@latest` vs `claude-code` 不明确 | `claude-code` 是稳定版（延迟约1周），`claude-code@latest` 是最新版 |
| worktree 默认基于 local HEAD | v2.1.133 起默认改为 `origin/<default>`（`fresh`），需设置 `worktree.baseRef: "head"` 保留旧行为 |
| `/context` 会输出 ASCII 网格 | 已修复（v2.1.132+ 不再浪费 ~1.6k tokens） |
| 早期教程中 hooks 只有 PreToolUse/PostToolUse | 2026年已有12+个生命周期事件 |
| 子代理是唯一的并行方式 | Agent Teams（实验性）提供了更强