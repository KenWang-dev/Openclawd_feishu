
# 第五卷：综合实战

> **学习目标**：通过 4 个完整实战项目，将前面学到的所有知识串联起来。读完本卷后，你已具备独立使用 Claude Code 完成真实项目的能力。

---

## 第27章：实战 1 —— 从零搭建全栈应用

### 27.1 项目概述

**目标**：用 Claude Code 从零搭建一个任务管理应用（TaskBoard），包含前后端和数据库。

**技术栈**：
- 前端：React + TypeScript + Tailwind CSS
- 后端：Node.js + Express + TypeScript
- 数据库：SQLite（通过 Prisma ORM）
- 测试：Vitest（前端）+ Jest（后端）

### 27.2 Step 1：项目初始化

```bash
mkdir taskboard && cd taskboard
git init
claude
```

**给 Claude 的指令**：

```
我要从零搭建一个任务管理应用 TaskBoard。

技术栈：
- 前端：React + TypeScript + Tailwind CSS（Vite）
- 后端：Node.js + Express + TypeScript
- 数据库：SQLite + Prisma ORM
- 测试：Vitest + Jest

项目结构要求：
```
taskboard/
├── client/          # React 前端
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.tsx
│   └── package.json
├── server/          # Express 后端
│   ├── src/
│   │   ├── routes/
│   │   ├── middleware/
│   │   └── index.ts
│   └── package.json
├── prisma/
│   └── schema.prisma
├── CLAUDE.md
└── README.md
```

请先用 /init 生成 CLAUDE.md，然后用 Plan Mode 制定完整的实现计划。
```

### 27.3 Step 2：规划阶段（Plan Mode）

```
在 Plan Mode 中，制定分阶段实现计划：

阶段 1：基础架构（数据模型 + API 骨架）
阶段 2：核心 API 实现（CRUD）
阶段 3：前端框架搭建
阶段 4：前后端联调
阶段 5：测试
阶段 6：优化和文档

每个阶段列出：
- 需要创建的文件
- 主要功能
- 验证方式
```

### 27.4 Step 3：数据模型设计

Claude 在 Plan Mode 中输出的 Prisma schema：

```prisma
// prisma/schema.prisma
datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

generator client {
  provider = "prisma-client-js"
}

model Task {
  id          String   @id @default(cuid())
  title       String
  description String?
  status      String   @default("todo") // todo | in-progress | done
  priority    String   @default("medium") // low | medium | high
  dueDate     DateTime?
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}
```

**审查要点**：
- 字段类型是否合理
- 默认值是否正确
- 是否有遗漏字段（比如 userId）

### 27.5 Step 4：后端 API 实现

```
退出 Plan Mode（Ctrl+G），按计划执行阶段 1 和 2。

实现以下 API 端点：
- GET /api/tasks — 获取所有任务（支持筛选：status, priority）
- GET /api/tasks/:id — 获取单个任务
- POST /api/tasks — 创建任务
- PUT /api/tasks/:id — 更新任务
- DELETE /api/tasks/:id — 删除任务

每个端点要求：
- 输入验证（title 必填）
- 错误处理（404, 400, 500）
- 合适的 HTTP 状态码

实现后跑测试确认。
```

### 27.6 Step 5：前端实现

```
实现前端页面：

1. 任务列表页：显示所有任务，支持筛选和排序
2. 创建任务表单：标题、描述、优先级、截止日期
3. 任务卡片：显示状态、优先级，支持拖拽改状态

UI 要求：
- 响应式设计
- 加载状态和错误提示
- 空状态提示

实现后在浏览器中验证。
```

### 27.7 Step 6：测试

```
为后端 API 编写集成测试：
- 创建任务 → 验证返回
- 获取任务列表 → 验证筛选
- 更新任务状态 → 验证更新
- 删除任务 → 验证删除
- 边界情况：空标题、不存在的 ID

跑所有测试，确保通过。
```

### 27.8 Step 7：提交

```
将所有代码提交到 Git。
创建一个 PR，描述包括：实现了什么、技术栈、如何运行、如何测试。
```

### 27.9 完整命令记录

```bash
# 1. 初始化
mkdir taskboard && cd taskboard && git init && claude

# 2. 用 Claude 生成 CLAUDE.md
> /init

# 3. Claude 规划并实现（四阶段工作流）
> [按上述指令执行]

# 4. 验证
cd client && npm run dev    # 启动前端
cd server && npm run dev    # 启动后端

# 5. 测试
cd server && npm test
cd client && npm test

# 6. 提交
git add -A && git commit -m "feat: 初始版本 TaskBoard 全栈应用"
```

**预计耗时**：有 Claude Code 辅助，**30-60 分钟**完成全部。手动需要 2-3 天。

---

## 第28章：实战 2 —— 大型代码库上手

### 28.1 项目概述

**目标**：克隆一个真实的开源项目，用 Claude Code 快速理解架构，并提交第一个 PR。

**选择项目标准**：
- 有 5k+ star（说明有一定复杂度）
- 有完善的 README 和文档
- 有未解决的 Issue（方便贡献）
- 技术栈与你熟悉的匹配

**推荐**：`expressjs/express`、`vercel/next.js`、`facebook/react`（选你熟悉的领域的）

### 28.2 Step 1：克隆和理解

```bash
git clone https://github.com/expressjs/express.git
cd express
claude
```

```
这是一个大型开源项目。请帮我理解它的架构：

1. 项目整体结构（用树状图展示，只到第 2-3 层）
2. 核心模块和它们的职责
3. 请求处理流程（从接收请求到返回响应）
4. 中间件系统是如何工作的
5. 扩展点在哪里

输出控制在 50 行以内，重点关注我需要理解的"骨架"。
```

### 28.3 Step 3：找一个 Issue

```
查看这个项目的 open issues。
找一个标记为 "good first issue" 或 "help wanted" 的 issue。
告诉我：
1. Issue 编号和标题
2. 问题描述
3. 涉及哪些文件
4. 难度评估（简单/中等/困难）
```

### 28.4 Step 4：Plan Mode 制定方案

```
（Ctrl+G 进入 Plan Mode）

针对选定的 issue，制定修复方案：
1. 需要修改哪些文件
2. 每个文件做什么修改
3. 需要添加什么测试
4. 预计影响范围

评估风险：这个修改会破坏现有功能吗？
```

### 28.5 Step 5：实现和测试

```
（Ctrl+G 退出 Plan Mode）

按计划实现修复。
修改完成后：
1. 跑项目现有的测试套件
2. 添加针对这次修复的测试
3. 检查代码风格是否符合项目规范
```

### 28.6 Step 6：提交 PR

```
创建分支并提交：
1. 基于最新的 main 创建分支
2. 分支名格式：fix/issue-编号-简短描述
3. Commit message 引用 Issue 编号
4. PR 描述模板：
   - 问题描述
   - 修复方案
   - 测试方式
   - Closes #issue编号
```

### 28.7 经验总结

**学到了什么**：
- 如何快速理解大型代码库
- 如何在 Plan Mode 中安全地制定方案
- 如何遵循开源项目的规范提交 PR
- 如何用 Claude Code 加速开源贡献

**关键洞察**：Claude Code 理解大型代码库的能力，是它区别于"代码补全工具"的核心竞争力。Copilot 只能看到当前文件，Agent 能看到整个项目。

---

## 第29章：实战 3 —— 搭建自动化工作台

### 29.1 项目概述

**目标**：将 GitHub、Notion、Slack 三个工具通过 MCP 连接到 Claude Code，搭建一个统一的自动化工作台。

### 29.2 Step 1：MCP 配置

```json
// .mcp.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": { "GITHUB_TOKEN": "REDACTED_TOKENxxx" }
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": { "NOTION_API_KEY": "ntn_xxx" }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-slack"],
      "env": { "SLACK_BOT_TOKEN": "xoxb-xxx" }
    }
  }
}
```

### 29.3 Step 2：创建工作流 Skill

```
帮我创建一个 Skill "daily-standup"：
1. 从 GitHub 读取我昨天和今天的 commit
2. 从 Notion 读取我的任务列表和进度
3. 整合成一份站会报告
4. 输出格式：
   - 昨天完成了什么
   - 今天计划做什么
   - 有没有阻塞项
```

### 29.4 Step 3：工作流编排

```
让 Claude Code 自动完成以下工作流：

1. 每天早上 9 点（用 cron）：
   - 拉取 GitHub 的 open issues
   - 对比 Notion 的任务列表
   - 在 Slack 发送每日工作建议

2. 每次 PR 创建时（用 CI/CD）：
   - 自动审查代码
   - 在 Slack 通知团队
   - 在 Notion 更新任务状态
```

### 29.5 Step 4：验证

```
测试完整工作流：
1. 创建一个测试 Issue
2. 在 Notion 创建对应任务
3. 运行 daily-standup Skill
4. 确认 Slack 收到通知
5. 确认 Notion 任务状态更新
```

### 29.6 关键收获

| 收获 | 说明 |
|------|------|
| MCP 是连接器 | 一个配置文件，连接无限工具 |
| Skill 是粘合剂 | 把多个 MCP 工具组合成一个工作流 |
| Claude Code 是编排器 | 用自然语言描述工作流，自动执行 |
| 数据在工具间流动 | GitHub → Claude → Notion → Slack |

---

## 第30章：实战 4 —— 团队协作最佳实践

### 30.1 共享 CLAUDE.md

团队中最重要的 Claude Code 资源就是 **CLAUDE.md**。确保团队所有人共享同一份：

```bash
# CLAUDE.md 放在仓库根目录，提交到 Git
git add CLAUDE.md
git commit -m "docs: 添加团队共享的 CLAUDE.md"
```

**团队 CLAUDE.md 应包含**：
- 项目技术栈和架构
- 代码风格规范（强制）
- Git commit 规范
- 测试要求
- 安全红线（"禁止硬编码密钥"）
- API 设计规范

### 30.2 共享 Skills

将团队常用的 Skills 提交到仓库：

```
.claude/
├── settings.json          # Hooks 配置（团队共享）
├── agents/                # 自定义 Subagents
│   ├── code-reviewer.md
│   └── api-designer.md
└── skills/                # 团队 Skills
    ├── pr-review/
    ├── daily-standup/
    └── deploy-check/
```

**团队 Skills 规范**：
- 每个 Skill 有清晰的触发条件
- 包含完整的步骤说明
- 有输出格式规范
- 定期维护更新

### 30.3 Hooks 团队配置

在 `.claude/settings.json` 中配置团队级的 Hooks：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "阻止 rm -rf / 和 DROP TABLE 等危险命令"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "修改 .ts/.js 文件后自动运行 eslint --fix"
      }
    ]
  }
}
```

### 30.4 代码审查自动化

**CI/CD 中的 Claude Code**：

```yaml
# .github/workflows/claude-review.yml
# 每次 PR 自动触发 Claude 代码审查
# 审查结果作为 PR 评论发布
# 严重问题自动打上 "needs-review" 标签
```

**结合 GitHub CODEOWNERS**：
- 关键文件的变更自动触发更严格的审查
- Claude Code 负责第一轮审查，人类做最终确认

### 30.5 知识沉淀

**定期更新 CLAUDE.md**：
- 每季度审查一次
- 新增的技术栈和规范及时更新
- 删除过时的约束
- 收集团队反馈，持续改进

**创建团队知识库**：
```
docs/
├── architecture/          # 架构文档
├── decisions/             # ADR（架构决策记录）
├── runbooks/              # 运维手册
└── onboarding/            # 新人指南（含 Claude Code 使用指南）
```

让 Claude Code 在 `docs/` 中生成和维护文档：

```
@src/ 基于当前代码，更新 docs/architecture/overview.md。
保持与代码同步。
```

### 30.6 团队使用 Checklist

- [ ] 团队共享 CLAUDE.md 已提交到仓库
- [ ] 至少 3 个团队 Skills 已创建
- [ ] Hooks 配置已启用（至少危险命令防护）
- [ ] CI/CD 中的 Claude Code 审查已配置
- [ ] 新人入职流程包含 Claude Code 培训
- [ ] 定期（季度）更新 CLAUDE.md 和 Skills
- [ ] MCP 配置已共享（如需要）
- [ ] 团队规范文档在 docs/ 中维护

---



---

## 第27章补充：完整全栈实战详解

### 27.10 前端组件实现细节

**任务列表组件**：

让 Claude 实现时，给出精确的 UI 规范：

```
实现 TaskList 组件，要求：
- 使用 Tailwind CSS 样式
- 每个任务显示为一行卡片
- 左侧显示状态图标（✅ 完成 / 🔄 进行中 / ⬜ 待办）
- 中间显示标题和描述
- 右侧显示优先级标签（🔴高 / 🟡中 / 🟢低）
- 底部显示截止日期（如果有的话）
- 支持点击切换状态
- 空列表时显示友好的空状态提示
- 添加加载骨架屏效果
```

**为什么给这么详细？** 因为前端 UI 的"好"和"不好"差别很大。模糊指令（"做个列表"）可能得到一个功能正确但视觉粗糙的结果。精确指令确保 UI 质量一致。

### 27.11 API 错误处理规范

```
所有 API 端点统一错误处理格式：

成功响应：
{ "success": true, "data": {...} }

错误响应：
{ "success": false, "error": { "code": "VALIDATION_ERROR", "message": "Title is required" } }

HTTP 状态码规范：
- 200：成功
- 201：创建成功
- 400：请求参数错误
- 404：资源不存在
- 500：服务器错误

在 server/src/middleware/errorHandler.ts 中实现统一的错误处理中间件。
```

### 27.12 部署准备

```
为这个项目准备部署配置：

1. 创建 Dockerfile（前端 + 后端分别打包）
2. 创建 docker-compose.yml（app + db）
3. 创建 .env.example（环境变量模板）
4. 添加 health check 端点 GET /api/health
5. 创建 nginx.conf（前端静态文件 + API 反向代理）

不要实际部署，只生成配置文件。
```

### 27.13 项目总结

完成这个实战后，你应该掌握：

| 能力 | 对应章节 |
|------|----------|
| 项目初始化和规范 | 第5章 CLAUDE.md |
| 四阶段工作流 | 第7章 |
| Plan Mode 规划 | 第8章 |
| 代码审查 | 第10章 |
| Git 工作流 | 第11章 |
| 错误调试 | 第12章 |

**这就是为什么前面花了 12 章打基础**——实战只是把这些基础知识串联起来。如果前面没有好好理解，实战中就会手忙脚乱。

---

## 第28章补充：开源贡献进阶

### 28.8 理解大型项目的阅读策略

面对 10k+ 文件的项目，不要试图"读完全部代码"。用以下策略：

**策略 1：从入口文件开始**

```
告诉我这个项目的入口文件是什么，从入口文件追踪请求处理流程。
只关注主路径，忽略错误处理和边缘情况。
```

**策略 2：按功能模块理解**

```
列出所有功能模块，每个模块用一句话描述职责。
然后我选择一个感兴趣的模块深入分析。
```

**策略 3：先测试后代码**

```
先跑测试套件，了解项目的测试覆盖情况。
然后选一个测试文件，通过测试反推代码的功能。
```

### 28.9 如何写出让维护者满意的 PR

**PR 描述模板**：

```markdown
## 问题描述
[简述 Issue]

## 修复方案
[你的修改方案，为什么这样改]

## 变更内容
- [文件1] 修改了什么
- [文件2] 新增了什么

## 测试
- [ ] 通过了现有测试
- [ ] 添加了新测试
- [ ] 手动验证了 [场景]

## 截图（如果有 UI 变更）
[截图]
```

**让 Claude Code 帮你写 PR 描述**：

```
分析这个分支的所有 commit，生成一份 PR 描述。
遵循上面的模板格式。
```

---

## 第29章补充：MCP 工作流模式

### 29.7 三种常见工作流模式

**模式 1：数据同步**

```
GitHub Issue → Claude 分析 → Notion 任务创建
```

适合：将外部工具的事件同步到你的项目管理系统。

**模式 2：情报收集**

```
GitHub + Slack → Claude 聚合 → 每日摘要
```

适合：每天从多个信息源收集重要更新。

**模式 3：自动化操作**

```
触发事件 → Claude 决策 → 多工具联动
```

适合：基于条件自动执行操作（如：PR 合并后自动通知+更新文档）。

### 29.8 工作流调试技巧

```
MCP 连接不工作。请帮我排查：
1. 检查 .mcp.json 格式是否正确
2. 手动运行每个 MCP Server 的命令，看有没有报错
3. 检查环境变量是否正确设置
4. 查看 Claude Code 的日志
```

---

## 第30章补充：团队成熟度模型

### 30.7 Claude Code 团队成熟度四级

**Level 1：个人探索（1-2 人）**
- 个人使用 Claude Code
- 有个人 CLAUDE.md
- 没有团队规范

**Level 2：规范建立（3-5 人）**
- 团队共享 CLAUDE.md
- 基本的 Hooks 配置
- 1-2 个团队 Skills
- CI/CD 中集成 Claude Code

**Level 3：流程优化（5-15 人）**
- 多个专业 Skills
- MCP 集成多个工具
- 自动化代码审查
- 新人培训包含 Claude Code

**Level 4：深度整合（15+ 人）**
- Agent Teams 协作
- 完整的自动化工作流
- 自定义 MCP Server
- 数据驱动的效率度量

**建议**：不要试图从 Level 1 直接跳到 Level 4。每级稳定使用 1-2 个月后再升级。


## 附录 A：命令速查表

### 交互式命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `/help` | 查看所有可用命令 | `/help` |
| `/compact` | 压缩上下文 | `/compact` |
| `/status` | 查看当前状态 | `/status` |
| `/model` | 切换模型 | `/model claude-opus-4` |
| `/plan` | 进入 Plan Mode | `/plan` |
| `/edit` | 退出 Plan Mode | `/edit` |
| `/init` | 生成 CLAUDE.md | `/init` |
| `/fast` | 切换 Fast Mode | `/fast` |
| `/loop` | 循环执行 | `/loop` |
| `/powerup` | 管理 Power-ups | `/powerup` |
| `/subagents` | 查看 Subagents | `/subagents` |

### CLI 命令

| 命令 | 说明 |
|------|------|
| `claude` | 启动交互式会话 |
| `claude -p "prompt"` | 非交互式执行（Headless） |
| `claude "prompt"` | 快速执行单次任务 |
| `claude --version` | 查看版本 |
| `claude /init` | 初始化项目 |

### 管道输入

```bash
cat file.ts | claude "审查这段代码"
git diff | claude "审查变更"
git log --oneline -10 | claude "总结最近提交"
error.log | claude "分析错误原因"
```

---

## 附录 B：配置文件完整参考

### CLAUDE.md 模板

```markdown
# 项目名称

## 技术栈
- 语言：TypeScript 5.x
- 框架：Next.js 14 (App Router)
- 数据库：PostgreSQL + Prisma
- 测试：Vitest + Playwright

## 代码规范
- 使用 ESLint + Prettier
- 函数不超过 30 行
- 所有 public API 必须有 JSDoc
- 错误使用自定义 Error 类

## Git 规范
- Commit 格式：类型(范围): 描述
- 分支命名：feature/xxx、fix/xxx、refactor/xxx

## 测试要求
- 新功能必须包含测试
- 覆盖率不低于 80%
- PR 必须通过所有测试才能合并

## 安全红线
- 禁止硬编码密钥
- 所有用户输入必须验证
- SQL 必须用参数化查询
```

### .claude/settings.json 模板

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "your-safety-check-script.sh"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "your-lint-script.sh"
      }
    ]
  }
}
```

### .mcp.json 模板

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@scope/mcp-server-package"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

---

## 附录 C：推荐学习资源

### 官方资源

| 资源 | 链接 | 用途 |
|------|------|------|
| Claude Code 文档 | docs.anthropic.com/claude-code | 权威参考 |
| Anthropic Cookbook | github.com/anthropics/anthropic-cookbook | 示例代码 |
| MCP 协议规范 | modelcontextprotocol.io | MCP 开发 |
| Claude API 文档 | docs.anthropic.com/en/docs | API 参考 |

### 社区资源

| 资源 | 类型 | 说明 |
|------|------|------|
| Reddit r/ClaudeAI | 论坛 | 社区讨论 |
| Twitter/X #ClaudeCode | 社交 | 最新动态和技巧 |
| YouTube "Claude Code Tutorial" | 视频 | 视频教程 |
| GitHub Topics: claude-code | 代码 | 开源项目和工具 |

### 进阶阅读

| 资源 | 说明 |
|------|------|
| "Building AI Agents"（Anthropic Blog） | Agent 设计原则 |
| "Prompt Engineering Guide"（DAIR.AI） | Prompt 技巧大全 |
| "The Bitter Lesson"（Rich Sutton） | 为什么通用方法最终胜出 |

---

## 附录 D：常见问题 FAQ

### 安装与配置

**Q：安装后 claude 命令找不到？**
A：npm 全局路径未加入 PATH。运行 `npm config get prefix`，将输出的 bin 目录加入 PATH。

**Q：Node.js 版本不满足要求？**
A：使用 nvm 安装最新 LTS：`nvm install --lts`。

**Q：登录一直超时？**
A：检查网络代理。或使用 API Key 方式：`export ANTHROPIC_API_KEY=sk-ant-xxx`。

### 使用问题

**Q：Claude 改了不该改的文件怎么办？**
A：`git checkout -- <file>` 恢复。建议在操作前先创建分支，方便回滚。

**Q：对话太长，Claude 开始"健忘"？**
A：运行 `/compact` 压缩上下文，或开新会话。超过 75% 上下文使用率就该注意了。

**Q：Claude 写的代码有 bug？**
A：正常。用四步恢复法：识别→定位→修复→验证。永远不要跳过审查。

**Q：Plan Mode 和普通模式有什么区别？**
A：Plan Mode 只读不写，适合理解和规划。普通模式可以修改文件。

### 成本问题

**Q：一个月大概花多少钱？**
A：轻度使用 $20 内，中度 $20-50，重度 $50-100。设置 Anthropic Console 的月度限额。

**Q：如何降低成本？**
A：用 /compact、用 Subagent 隔离长任务、日常任务用便宜模型、定期开新会话。

### 团队问题

**Q：团队如何共享 Claude Code 配置？**
A：将 CLAUDE.md、.claude/ 目录提交到 Git 仓库。所有成员共享同一套规范。

**Q：Claude Code 能替代代码审查吗？**
A：不能。Claude 做第一轮审查（速度快），人类做最终确认（质量高）。两者结合效率最高。

---

> **全书完**
>
> 本指南基于 2026 年 5 月公开资料及实际使用经验整理。Claude Code 更新频繁，建议关注官方文档获取最新特性。
>
> **记住**：工具会变，但方法论不变。四阶段工作流、验证思维、上下文管理——这些原则无论 Claude Code 怎么更新都适用。
>
> 祝你在 AI Agent 时代，成为一个高效的产品经理型开发者。🚀
