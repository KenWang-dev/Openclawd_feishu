
# 第三卷：进阶能力

> **学习目标**：掌握 Hooks 确定性控制、Subagents 隔离并行、Skills 工作流封装、MCP 外部工具集成、Auto Mode 自主循环、Agent Teams。读完本卷后，你已经是 Claude Code 高级用户了。

---

## 第13章：Hooks 系统

### 13.1 什么是 Hooks？

Hooks 是 Claude Code 的**确定性控制机制**——在特定事件发生时，自动执行你定义的脚本。

与 Prompt 约束不同，Hooks 是**确定性的**：不管 Claude 怎么想、怎么推理，只要触发条件满足，脚本就会执行。这是 Claude Code 中最强大的安全保障机制。

**类比**：
- Prompt 约束 = 告诉员工"请遵守规则"（软性）
- Hooks = 安装了监控摄像头和自动门禁（硬性）

### 13.2 配置文件位置

Hooks 配置在项目根目录的 `.claude/settings.json` 或全局的 `~/.claude/settings.json` 中。

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "echo '即将修改文件' >> /tmp/claude-audit.log"
      }
    ]
  }
}
```

### 13.3 五种 Hook 类型

| Hook 类型 | 触发时机 | 典型用途 |
|-----------|----------|----------|
| **PreToolUse** | Claude 调用工具**之前** | 阻止危险操作、审计日志 |
| **PostToolUse** | Claude 调用工具**之后** | 自动格式化、自动测试 |
| **Notification** | Claude 发送通知时 | 自定义通知渠道 |
| **Stop** | Claude 完成回答时 | 自动清理、结果后处理 |
| **SessionStart** | 会话启动时 | 注入上下文、环境检查 |

### 13.4 生命周期事件（按实用性排序）

**Tier 1：必掌握**

| 事件 | matcher | 用途 |
|------|---------|------|
| PreToolUse + Write/Edit | `Write\|Edit` | 文件修改审计 |
| PreToolUse + Bash | `Bash` | 阻止危险命令 |
| PostToolUse + Write/Edit | `Write\|Edit` | 保存后自动 lint/format |

**Tier 2：推荐使用**

| 事件 | matcher | 用途 |
|------|---------|------|
| PreToolUse + Read | `Read` | 限制读取敏感文件 |
| PostToolUse + Bash | `Bash` | 命令执行后检查状态 |
| SessionStart | - | 会话初始化 |
| Stop | - | 结果后处理 |

**Tier 3：按需使用**

| 事件 | matcher | 用途 |
|------|---------|------|
| PreToolUse + MCP | `mcp__*` | MCP 调用审计 |
| PostToolUse + MultiEdit | `MultiEdit` | 批量修改后检查 |
| Notification | - | 自定义通知路由 |

### 13.5 退出码行为

Hook 脚本的退出码决定了 Claude Code 的行为：

| 退出码 | 行为 |
|--------|------|
| `0` | ✅ 允许操作继续 |
| `2` | ⛔ 阻止操作（Claude 会看到错误信息） |
| 其他 | ⚠️ 警告（操作继续，但 Claude 收到警告） |

### 13.6 实战 1：阻止危险命令

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "bash -c \"if echo '$CLAUDE_TOOL_INPUT' | grep -qE 'rm -rf|DROP TABLE|mkfs|dd if='; then echo '⛔ 危险命令被阻止' >&2; exit 2; fi; exit 0\""
      }
    ]
  }
}
```

当 Claude 尝试执行 `rm -rf /` 或 `DROP TABLE users` 时，Hook 会返回退出码 2，操作被阻止。

### 13.7 实战 2：文件修改后自动 lint

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "bash -c \"file=$(echo '$CLAUDE_TOOL_INPUT' | jq -r '.file_path // .path // empty' 2>/dev/null); if [ -n \"$file\" ] && echo \"$file\" | grep -q '\\.ts$\\|\\.js$'; then npx eslint \"$file\" --fix 2>&1 | tail -3; fi; exit 0\""
      }
    ]
  }
}
```

每次 Claude 修改 `.ts` 或 `.js` 文件后，自动运行 ESLint 修复。

### 13.8 实战 3：会话开始注入上下文

```json
{
  "hooks": {
    "SessionStart": [
      {
        "command": "echo '📋 当前 Git 分支：' $(git branch --show-current 2>/dev/null || echo '非 Git 仓库'); echo '📦 未提交的改动：'; git status --short 2>/dev/null | head -5 || echo '无'; echo '🔥 最近的 commit：'; git log --oneline -3 2>/dev/null || echo '无'"
      }
    ]
  }
}
```

每次新会话启动时，自动显示当前分支、未提交改动和最近 commit。

### 13.9 Hooks 最佳实践

| 原则 | 说明 |
|------|------|
| 脚本要快 | Hook 脚本执行时间会加到每次工具调用的延迟中 |
| 只用 exit 0/2 | 退出码 0 放行，2 阻止，其他值行为不确定 |
| 输出到 stderr | 警告和错误信息输出到 stderr（>&2），Claude 会看到 |
| 渐进式添加 | 先加 PreToolUse 防护，再逐步加 PostToolUse 增强 |
| 测试 Hook | 先在安全环境测试，避免误阻正常操作 |

---

## 第14章：Subagents

### 14.1 什么是 Subagent？

Subagent 是 Claude Code 中的**隔离工作单元**——它在一个独立的会话中运行，有自己的上下文，完成后将结果回传给主会话。

**比喻**：主会话是项目经理，Subagent 是派出去做专项任务的员工。任务完成后员工汇报结果，经理的办公桌（上下文）保持干净。

### 14.2 为什么需要 Subagent？

| 问题 | 没有 Subagent | 有 Subagent |
|------|--------------|-------------|
| 长任务污染主会话 | 上下文膨胀，效率下降 | 隔离运行，主会话保持干净 |
| 多任务并行 | 只能串行 | 可以同时派多个 Subagent |
| 不同任务用不同模型 | 不行 | 每个 Subagent 可以指定不同模型 |
| 成本控制 | 长任务用贵模型 | 日常任务用便宜模型 |

### 14.3 三个内置 Subagent

Claude Code 内置了三个专用 Subagent：

**1. Explore Subagent**（探索型）

```
让 Explore Subagent 分析 src/ 目录下所有文件，输出一份架构概览报告。
```

特点：只读模式，擅长理解和分析。适合代码审查、架构分析、文档生成。

**2. Plan Subagent**（规划型）

```
让 Plan Subagent 分析当前项目的技术债务，制定一个分 3 个阶段的重构计划。
```

特点：只读+分析，输出结构化计划。适合方案设计、技术选型、影响评估。

**3. General Subagent**（通用型）

```
让 Subagent 在 src/tests/ 目录下为所有 service 文件补全单元测试。
```

特点：可读写，执行实际修改。适合代码生成、测试编写、批量重构。

### 14.4 自定义 Subagent

你可以在 `.claude/agents/` 目录下创建自定义 Subagent：

```markdown
# .claude/agents/code-reviewer.md

你是一个代码审查专家。你的任务：

1. 读取指定的代码文件
2. 检查以下维度：
   - 安全性（注入、XSS、认证）
   - 性能（N+1、内存泄漏、不必要的计算）
   - 可读性（命名、函数长度、注释）
   - 正确性（边界情况、错误处理）
3. 输出结构化审查报告，包含：
   - 严重问题（必须修复）
   - 建议改进（推荐修复）
   - 代码亮点（值得学习的写法）
```

使用：

```
/code-reviewer 审查 src/services/payment.ts
```

### 14.5 决策树：何时用 Subagent vs 主会话

```
任务需要隔离上下文吗？
├── 是 → 用 Subagent
│   ├── 只需要分析？→ Explore/Plan Subagent
│   └── 需要修改文件？→ General Subagent
└── 否 → 主会话
    ├── 需要多次交互讨论？→ 主会话
    └── 一次性任务？→ 都可以，主会话更方便
```

### 14.6 实战：并行研究三个模块

```
同时让三个 Subagent 分别研究以下模块，每个输出一份 10 行以内的摘要：
1. Explore Subagent → src/auth/ 认证模块
2. Explore Subagent → src/payment/ 支付模块
3. Explore Subagent → src/notification/ 通知模块

三个都完成后，基于三份摘要，告诉我这三个模块之间的依赖关系。
```

---

## 第15章：Skills 系统

### 15.1 什么是 Skills？

Skills 是 Claude Code 的**可复用工作流封装**——将常用的工作模式打包成一个可重复使用的单元。

**与 CLAUDE.md 的区别**：

| 维度 | CLAUDE.md | Skills |
|------|-----------|--------|
| 加载时机 | 始终加载 | 按需触发 |
| 作用域 | 整个项目 | 特定任务 |
| 内容 | 规范和约束 | 工作流和步骤 |
| 类比 | 员工手册 | SOP 操作手册 |

### 15.2 Skills 目录

Skills 放在项目的 `.claude/skills/` 目录下，每个 Skill 是一个子目录：

```
.claude/
├── settings.json
├── agents/
└── skills/
    ├── pr-review/
    │   └── SKILL.md
    ├── deploy/
    │   └── SKILL.md
    └── refactor/
        └── SKILL.md
```

### 15.3 创建第一个 Skill

`.claude/skills/pr-review/SKILL.md`：

```markdown
---
name: pr-review
description: PR 代码审查工作流
---

# PR 审查 Skill

当用户要求审查 PR 或代码变更时激活。

## 步骤

1. 运行 `git diff main...HEAD` 获取所有变更
2. 按以下维度审查每个变更文件：
   - 安全性
   - 性能
   - 可读性
   - 测试覆盖
3. 输出结构化报告：
   - 🔴 严重问题（必须修复）
   - 🟡 建议改进（推荐修复）
   - 🟢 代码亮点
4. 如果有严重问题，提供具体的修复建议

## 输出格式

### 审查摘要
- 变更文件数：X
- 新增行数：X
- 删除行数：X

### 问题列表
#### 🔴 严重问题
1. [文件:行号] 描述 + 修复建议

#### 🟡 建议改进
1. [文件:行号] 描述

#### 🟢 亮点
1. [文件] 描述
```

### 15.4 Skill Frontmatter 完整参考

```yaml
---
name: skill-name          # 技能名称（唯一标识）
description: 一句话描述    # 触发依据，Claude 据此判断何时激活
triggers:                 # 可选：显式触发词
  - "审查 PR"
  - "review code"
allowedTools:             # 可选：限制可用工具
  - Read
  - Bash
  - Glob
---
```

### 15.5 动态上下文注入

Skills 支持在加载时执行命令，将结果注入上下文：

```markdown
---
name: env-check
description: 环境检查
---

# 环境信息

当前 Node 版本：!`node --version`
当前 Git 分支：!`git branch --show-current`
最近 commit：!`git log --oneline -1`

## 检查清单

基于以上环境信息，确认：
1. Node 版本是否符合项目要求
2. 是否在正确的分支上
3. 工作区是否干净
```

`!`command`` 语法会在 Skill 加载时执行命令，结果替换到 Skill 内容中。

### 15.6 实战：创建"PR 摘要" Skill

```
帮我创建一个 Skill，当我说"PR 摘要"时：
1. 读取当前分支相对于 main 的所有 commit
2. 按功能模块分类
3. 生成一份变更摘要
```

Claude 会自动创建 `.claude/skills/pr-summary/SKILL.md`。

---

## 第16章：MCP 集成

### 16.1 什么是 MCP？

MCP（Model Context Protocol）是 Anthropic 推出的开放协议，让 AI Agent 连接外部工具和数据源。

**比喻**：Claude Code 的工具箱原本只有锤子（Shell）和螺丝刀（文件系统）。MCP 让你可以往工具箱里加电钻、扳手、激光切割机——任何外部工具。

### 16.2 .mcp.json 配置

在项目根目录创建 `.mcp.json`：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "REDACTED_TOKENxxxxx"
      }
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "ntn_xxxxx"
      }
    }
  }
}
```

### 16.3 帕累托 Top 5 MCP Server

| MCP Server | 功能 | 适用场景 |
|------------|------|----------|
| **GitHub** | Issue、PR、代码搜索 | 开发者必备 |
| **Notion** | 页面读写、数据库查询 | 项目管理 |
| **Slack** | 消息收发、频道管理 | 团队协作 |
| **PostgreSQL** | 数据库查询 | 后端开发 |
| **Puppeteer** | 浏览器自动化 | UI 测试/爬虫 |

### 16.4 实战 1：连接 GitHub

**安装**：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "REDACTED_TOKENxxxxx"
      }
    }
  }
}
```

**使用**：

```
列出我 GitHub 上 openclaw 仓库的所有 open issue。
创建一个 issue：标题"添加用户搜索功能"，描述"支持按用户名和邮箱搜索"。
```

Claude Code 现在可以直接操作 GitHub API，不需要你手动打开浏览器。

### 16.5 实战 2：连接 Notion

**安装**：

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "ntn_xxxxx"
      }
    }
  }
}
```

**使用**：

```
在 Notion 中搜索标题包含"Q2 计划"的页面。
把这段代码审查结果追加到 Notion 的"代码审查记录"页面。
```

### 16.6 调试 MCP 连接问题

| 问题 | 排查方法 |
|------|----------|
| MCP Server 不启动 | 手动运行 command 检查输出 |
| 认证失败 | 检查 API Key 和环境变量 |
| 工具不出现 | 确认 .mcp.json 格式正确 |
| 超时 | 检查网络，某些 MCP Server 需要代理 |

```bash
# 手动测试 MCP Server 是否正常
npx -y @anthropic-ai/mcp-server-github
```

---

## 第17章：Auto Mode 与自主循环

### 17.1 什么是 Auto Mode？

Auto Mode 是 Claude Code 的**自主执行模式**——Claude 完成一步后，自动继续下一步，不需要你手动批准每一步操作。

默认情况下，Claude Code 每次使用工具（写文件、跑命令等）都需要你按 Enter 确认。Auto Mode 关闭了这个确认步骤。

### 17.2 何时该开 Auto Mode？

**✅ 适合开启**：
- 你完全信任的任务（生成文档、添加测试）
- 环境可控（Docker 容器、独立分支）
- 有版本控制（随时可以 git reset）
- 任务步骤明确（Claude 不需要中途问你）

**❌ 不适合开启**：
- 生产环境或重要数据
- 你不了解的项目
- 涉及敏感操作（删除、发送）
- 首次与 Claude 合作的任务

### 17.3 Auto Mode 的安全条件

在 CLAUDE.md 中设置安全边界：

```markdown
## Auto Mode 规则
- Auto Mode 下禁止执行 rm、DROP、DELETE 等破坏性命令
- Auto Mode 下禁止发送邮件、消息
- 所有修改限制在 src/ 目录内
- 修改前必须 git stash 或创建分支
```

结合 Hooks（第13章），实现双重保障。

### 17.4 /loop 命令

`/loop` 让 Claude 反复执行一个任务，直到满足退出条件。

```
/loop 跑测试，如果有失败就修复，重新跑，直到所有测试通过。
```

Claude 会自动进入"测试→修复→测试"的循环，直到所有测试通过或达到最大迭代次数。

### 17.5 实战：自主修复测试失败

```bash
claude
```

```
Auto Mode 开启。
跑所有测试。如果有失败的：
1. 分析失败原因
2. 修复代码
3. 重新跑测试
4. 重复直到全部通过

每次修复后告诉我改了什么。如果连续 3 次修复都没通过，停下来告诉我情况。
```

### 17.6 Auto Mode 最佳实践

| 实践 | 说明 |
|------|------|
| 先在安全分支试 | `git checkout -b claude-auto-fix` |
| 设置最大迭代 | 在 prompt 中指定"最多修 5 次" |
| 结合 Hooks | 用 Hooks 阻止危险操作 |
| 检查最终结果 | Auto Mode 完成后一定要审查所有改动 |

---

## 第18章：Agent Teams

### 18.1 什么是 Agent Teams？

Agent Teams 是 Claude Code 的**多 Agent 协作机制**——多个 Claude Code 实例协同工作，每个负责不同职责。

### 18.2 与 Subagents 的区别

| 维度 | Subagents | Agent Teams |
|------|-----------|-------------|
| 架构 | 主从关系 | 对等关系 |
| 通信 | 回传结果给主会话 | Agent 之间直接通信 |
| 上下文 | 隔离 | 可共享 |
| 适用场景 | 专项任务 | 复杂项目协作 |

### 18.3 配置与启用

Agent Teams 目前处于实验阶段。在 `.claude/settings.json` 中启用：

```json
{
  "agentTeams": {
    "enabled": true,
    "agents": {
      "backend": {
        "description": "后端开发专家",
        "model": "claude-sonnet-4-20250514"
      },
      "frontend": {
        "description": "前端开发专家",
        "model": "claude-sonnet-4-20250514"
      },
      "reviewer": {
        "description": "代码审查专家",
        "model": "claude-opus-4"
      }
    }
  }
}
```

### 18.4 使用场景

**场景 1：前后端协同**

```
后端 Agent：实现 API 端点
前端 Agent：基于 API 创建 UI 组件
审查 Agent：审查双方的代码
```

**场景 2：大型重构**

```
Agent A：重构数据层
Agent B：重构业务逻辑层
Agent C：更新测试
```

### 18.5 当前限制

Agent Teams 功能仍在快速发展中。目前的限制：
- 配置较为复杂
- Agent 间通信机制仍在优化
- 调试多 Agent 交互有挑战

**建议**：对于大多数场景，Subagents 已经够用。Agent Teams 适合特别复杂、需要不同专业角色的项目。保持关注官方更新。

---

## 第16章补充：MCP 进阶

### MCP 工作原理

MCP 的架构非常简洁：

```
Claude Code ←→ MCP Client ←→ MCP Server ←→ 外部工具
```

- **MCP Client**：Claude Code 内置，负责管理连接
- **MCP Server**：独立的进程，通过 stdio 与 Client 通信
- **通信协议**：JSON-RPC 2.0

这意味着任何能通过 stdin/stdout 通信的程序都可以成为 MCP Server。

### 创建自定义 MCP Server

```typescript
// my-mcp-server/index.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server(
  { name: 'my-tools', version: '1.0.0' },
  { capabilities: { tools: {} } }
);

// 注册工具
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: 'get_weather',
    description: '获取天气信息',
    inputSchema: {
      type: 'object',
      properties: { city: { type: 'string' } },
      required: ['city']
    }
  }]
}));

// 处理工具调用
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === 'get_weather') {
    const city = request.params.arguments.city;
    // 调用天气 API...
    return { content: [{ type: 'text', text: `${city}: 晴，25°C` }] };
  }
});

// 启动
const transport = new StdioServerTransport();
await server.connect(transport);
```

### 有用的 MCP Server 列表

| MCP Server | 功能 | 安装 |
|------------|------|------|
| @anthropic-ai/mcp-server-github | GitHub Issue/PR | `npx -y` |
| @notionhq/notion-mcp-server | Notion 读写 | `npx -y` |
| @anthropic-ai/mcp-server-slack | Slack 消息 | `npx -y` |
| @anthropic-ai/mcp-server-postgres | PostgreSQL 查询 | `npx -y` |
| @anthropic-ai/mcp-server-puppeteer | 浏览器自动化 | `npx -y` |
| mcp-server-fetch | HTTP 请求 | `npx -y` |
| mcp-server-filesystem | 文件系统操作 | `npx -y` |
| mcp-server-git | Git 操作 | `npx -y` |
| mcp-server-memory | 持久化记忆 | `npx -y` |
| mcp-server-brave-search | 网络搜索 | `npx -y` |

