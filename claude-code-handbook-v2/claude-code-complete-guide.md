# Claude Code 从入门到精通自学指南（100页完整版）

> **版本**: 2026年5月 | **基于**: Claude Code v1.x 最新版 | **方法论**: 第一性原理 × 帕累托法则 × 认知阶梯理论

---



---

# 引言：AI 编程时代的生存指南

## 2026 年的编程世界

2026 年，AI 编程已经从"新鲜事"变成了"基础设施"。

来看看几组数据：
- GitHub 上超过 40% 的新代码由 AI 辅助生成（GitHub Octoverse 2025 报告）
- Anthropic 的 Claude Code 在发布一年内成为开发者社区最受欢迎的 AI 编程工具之一
- 全世界有超过 200 万开发者在使用某种形式的 AI 编程助手

这意味着什么？**如果你不会用 AI 编程工具，你不是落后一步——你是落后一个时代。**

但"会用"和"用好"是两回事。就像有了汽车不等于你会开车。Claude Code 就是那辆高性能赛车——本书就是你的驾驶手册。

## 为什么需要一本 100 页的指南？

市面上关于 Claude Code 的内容很多：
- 官方文档很全面，但像字典——你知道在哪查，但不知道从哪开始读
- 博客文章很实用，但像碎片——每个讲一个技巧，没有体系
- 视频教程很直观，但像快餐——看完就忘，不能反复查阅

本书的不同之处：
- **有体系**：30 章从零到精通，每章是下一章的前提
- **有深度**：不只讲"怎么做"，更讲"为什么这样做"
- **有节奏**：每一步台阶都经过精心设计，不会太陡也不会太平
- **可反复查阅**：PDF 格式，随时随地翻到任何一页

## 本书的独特方法

本书基于四个方法论构建：

**第一性原理**：不满足于"别人这么做"，追问"为什么要这样做"。比如，我们不会只告诉你"用 Plan Mode"，而是解释为什么只读规划模式能大幅减少返工。

**帕累托法则（80/20）**：Claude Code 有上百个功能，但我们只深入 20% 最重要的功能，因为这 20% 能覆盖 80% 的使用场景。

**认知阶梯理论**：学习像爬楼梯——每一级都要稳固，才能安全地爬到下一级。本书的 30 章就是 30 级台阶，每一级都在前一级的基础上递进。

**金字塔原理**：每个章节都是"结论先行→逐层展开"。你可以只看每章的第一段就掌握核心观点，有需要再深入细节。

## 如何使用本书

**如果你是完全的新手**：从头到尾读一遍。预计 3-4 周的周末时间。

**如果你已经用过 Claude Code**：跳到第二卷开始，快速补齐方法论。

**如果你是团队管理者**：直接跳到第五卷（综合实战）和第 30 章（团队协作）。

**作为参考手册**：用目录定位到你需要的章节，直接查阅。

## 一个承诺

读完本书后，你的 Claude Code 使用效率至少提升 3 倍。

这不是夸张——大部分开发者只用 Claude Code 做简单对话（相当于只用了 10% 的能力）。本书帮你解锁剩下的 90%。

准备好了吗？让我们开始。


# 第一卷：认知重启

> **学习目标**：建立正确的 Agent 心智模型，完成安装，写出第一份 CLAUDE.md，掌握 Prompt 纪律。读完本卷后，你应该能用 Claude Code 独立完成小型项目。

---

## 第1章：什么是 Agent 而不是 Chat

### 1.1 LLM 的三种存在形态

大语言模型有三种存在形态，能力依次递增。理解这个谱系是学 Claude Code 的第一步：

**形态一：Chatbot（聊天机器人）**

你问一句，它答一句。对话结束，一切归零。

典型代表：ChatGPT 网页版、Claude.ai 对话界面。

局限：没有记忆、没有工具、没有行动力。它是个"百科全书式问答机"。

**形态二：Copilot（副驾驶）**

附着在你的 IDE 里，你写代码时它提建议。你选不选都可以。

典型代表：GitHub Copilot、Cursor Tab 补全。

局限：被动响应，不能主动执行，没有完整的项目视角。

**形态三：Agent（代理）**

它能**自主行动**——读文件、写代码、跑命令、开浏览器、创建 PR。你给它一个目标，它自己去规划路径并执行。

典型代表：Claude Code、Devin、OpenHands。

这就是 Claude Code 所在的位置——**Agent**。

### 1.2 Agent vs Copilot：本质区别

| 维度 | Copilot | Agent |
|------|---------|-------|
| 主动性 | 被动等待 | 主动规划并执行 |
| 操作范围 | 当前文件/光标 | 整个项目 |
| 工具使用 | 无 | Shell、文件系统、浏览器、MCP |
| 多步骤 | 一次建议 | 多轮迭代直到完成 |
| 错误恢复 | 你自己修 | 自己发现、自己修 |

一句话总结：Copilot 是自动补全，Agent 是自动执行。

### 1.3 核心心智转变

使用 Claude Code 需要一次根本性的心智转变：

| | 旧方式 | 新方式 |
|--|--------|--------|
| 你的角色 | **打字员**：手敲每一行代码 | **产品经理**：描述需求和验收标准 |
| Claude 的角色 | 搜索引擎 | **初级工程师**：能干活但需要指导 |
| 交互方式 | "帮我写一个函数" | "用户注册需要邮箱验证，加上去" |
| 质量控制 | 写完再测 | 每一步验证，不让错误积累 |

**关键理解**：你不是在用 AI 写代码。你是在**管理一个 AI 工程师**。

### 1.4 Claude Code 的独特优势

- **原生理解代码**：基于 Claude（Anthropic）模型，代码能力业界顶尖
- **终端原生**：直接在你的终端运行，完整的系统权限
- **确定性 Hooks**：通过 Hooks 系统实现确定性控制，不依赖 prompt 约束
- **上下文管理**：智能的上下文压缩和窗口管理
- **MCP 生态**：通过 Model Context Protocol 连接无限工具

### 1.5 "像管员工一样管 Claude Code"

把 Claude Code 想象成一个能力很强但经验不足的初级工程师：

- ✅ 给他清晰的任务描述
- ✅ 告诉他验收标准
- ✅ 审查他的产出
- ✅ 修正他犯的错
- ✅ 随着时间推移，给他更多自主权
- ❌ 不要替他做决策
- ❌ 不要无条件信任他的输出
- ❌ 不要一次给太模糊的任务

这就是 CLAUDE.md 存在的意义——它是给这个"员工"的入职手册。

---

## 第2章：安装与5分钟跑通

### 2.1 环境准备

Claude Code 需要 Node.js 运行环境。

**检查 Node.js 版本**：

```bash
node --version
# 需要 >= 18
```

**安装 Node.js**（三选一）：

```bash
# 方式1：NodeSource（Linux 推荐）
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 方式2：nvm（版本管理器，强烈推荐）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install 22
nvm use 22

# 方式3：Homebrew（macOS）
brew install node@22
```

**Windows 用户**：推荐使用 WSL2（Windows Subsystem for Linux），而不是原生 PowerShell。Claude Code 对 Unix 环境支持最好。

```powershell
# Windows 上安装 WSL2
wsl --install
# 进入 WSL 后按 Linux 方式安装
```

**验证环境**：

```bash
node --version   # v22.x.x
npm --version    # 10.x.x
```

看到以上版本号，环境准备完成。

### 2.2 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

**验证安装**：

```bash
claude --version
```

看到版本号输出，安装成功。

### 2.3 首次启动与登录

```bash
claude
```

首次运行会进入交互式登录流程：

1. 终端显示一个认证 URL
2. 在浏览器中打开该 URL
3. 用 Anthropic 账号登录（或 Google/GitHub）
4. 授权完成后，终端自动连接

**登录成功后你会看到**：

```
╭─────────────────────────────────────╮
│  Claude Code v1.x.x                │
│  Type /help for available commands  │
│  Type your message to begin         │
╰─────────────────────────────────────╯
>
```

恭喜，Claude Code 已就绪。

### 2.4 API Key 方式（CI/CD 环境）

如果你不想通过浏览器登录，可以用 API Key：

```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxx
claude
```

适合 CI/CD 环境或 Headless 模式。

### 2.5 VS Code 扩展（推荐但非必需）

如果你使用 VS Code，安装官方扩展获得更好体验：

1. 打开 VS Code → 搜索 "Claude Code" → 安装
2. `Ctrl+Shift+P`（macOS: `Cmd+Shift+P`）→ 输入 "Claude Code"

VS Code 扩展提供：内联代码建议、侧边栏对话、文件上下文自动注入、快捷键支持。

### 2.6 你的第一个命令

安装后的第一个验证：

```bash
claude "列出当前目录下的文件，并告诉我这个项目是用什么语言写的"
```

**预期输出**：

```
> 这是一个 Node.js 项目，使用 TypeScript 编写。主要依赖包括：
> - express (Web 框架)
> - prisma (ORM)
> - jest (测试框架)
>
> 项目结构如下：
> ├── src/
> │   ├── index.ts
> │   ├── routes/
> │   └── utils/
> ├── package.json
> └── tsconfig.json
```

**看到这个输出 → 一切正常。**

### 2.7 常见安装问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `command not found: claude` | npm 全局路径未加入 PATH | `npm config get prefix` 然后加入 PATH |
| `EACCES: permission denied` | npm 全局目录权限 | `sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin}` |
| 登录超时 | 网络问题 | 检查代理设置，或用 API Key |
| `bad CPU type` | Node.js 架构不匹配 | 确认 x64/arm64，重新安装 |

---

## 第3章：订阅与成本认知

### 3.1 五档订阅对比

| 计划 | 月费 | Claude Code 权限 | 适用人群 |
|------|------|-----------------|----------|
| Free | $0 | 有限使用 | 体验 |
| Pro | $20 | 正常使用 | 个人开发者 |
| Max | $100-200 | 高用量 + 优先级 | 重度用户 |
| Team | $30/人 | 共享 + 管理 | 小团队 |
| Enterprise | 定制 | SSO + 审计 + 合规 | 企业 |

**帕累托建议**：90% 的个人开发者选 Pro 就够了。每天使用超过 4 小时，考虑 Max。

### 3.2 Token 计费模型

理解 Token 是控制成本的第一步。

**什么是 Token？**

Token 是 LLM 处理文本的最小单位。粗略换算：
- 1 个英文单词 ≈ 1.3 Token
- 1 个中文字符 ≈ 2-3 Token

**三种 Token 消耗**：

| 类型 | 说明 | 价格比 |
|------|------|--------|
| Input Token | 发送给模型的内容 | 1x |
| Output Token | 模型生成的回复 | 3-5x |
| Cache Token | 重复内容（上下文前缀） | 0.1x |

**关键洞察**：Cache Token 比普通 Input 便宜 10 倍。Claude Code 的上下文前缀缓存机制能大幅降低成本。

### 3.3 一个月大概花多少钱？

基于实际使用估算（Pro 计划，Claude 3.5 Sonnet）：

| 使用强度 | 每日时长 | 月度成本 | 特征 |
|----------|----------|---------|------|
| 轻度 | 1-2 小时 | $20 内 | 偶尔问问题、改 bug |
| 中度 | 2-4 小时 | $20-50 | 日常开发、代码审查 |
| 重度 | 4-8 小时 | $50-100 | 全天使用、大项目 |
| 疯狂 | 8+ 小时 | $100+ | CI/CD 集成、多项目 |

**控制成本的 5 个习惯**：

1. 用 `/compact` 及时压缩上下文
2. 用 Subagent 隔离长任务
3. Plan Mode 先读后改
4. 给精确的指令（模糊 → 多轮澄清 → 更多 Token）
5. 定期开新会话

### 3.4 设置支出上限

```bash
# 查看当前用量
claude /status

# 在 Anthropic Console 设置月度限额
# https://console.anthropic.com/settings/limits
```

建议：个人开发者月度限额 $50-100。初期从 $20 开始。

**认知提醒**：Claude Code 是 Agent 模式，每次操作（读文件、跑命令、写代码）都触发 API 调用。每次它"动手"都在花你的钱。理解这一点，才能用好它。

---

## 第4章：心智模型建立

### 4.1 核心转变：从"写代码"到"描述需求"

这是最关键的一步。很多人安装了 Claude Code，但思维模式还停留在 Copilot 时代。

**Copilot 思维**：
```
我：帮我写一个函数来解析 CSV
Claude：[生成代码]
我：复制粘贴，修改，调试
```

**Agent 思维**：
```
我：用户导入 CSV 文件时，支持自定义分隔符，并在导入后显示预览
Claude：[读取项目] → [理解架构] → [创建修改计划] → [写代码] → [跑测试] → [提交]
我：审查代码，确认没问题
```

区别：你不再关心"怎么写"，你关心"要做什么"。

### 4.2 能力与边界

**Claude Code 擅长**：
- ✅ 理解大型代码库的结构和逻辑
- ✅ 按需求生成新代码
- ✅ 重构和优化现有代码
- ✅ 写测试用例
- ✅ 调试和修复 bug
- ✅ 生成文档和注释
- ✅ 执行 Shell 命令
- ✅ 操纵 Git（commit、PR、branch）
- ✅ 集成外部工具（通过 MCP）

**Claude Code 不擅长**（至少目前）：
- ❌ 需要大量 GUI 交互的操作
- ❌ 理解没有文档的业务逻辑
- ❌ 跨会话的长期记忆
- ❌ 大规模并行（但 Subagent 可以辅助）

### 4.3 第一个实战：创建 TODO 应用

用 Claude Code 做一个完整的实战。这不是"Hello World"——而是一个能跑起来的应用。

**Step 1：创建项目**

```bash
mkdir my-todo && cd my-todo
git init
claude
```

**Step 2：给 Claude 第一个任务**

```
创建一个命令行 TODO 应用：
1. Python 3 实现
2. 数据存储在 todo.json
3. 支持：添加、列表、完成、删除
4. 清晰的帮助信息
5. 写好注释
```

**Step 3：观察 Claude 的工作**

Claude 会依次：
1. 读取当前目录（确认空项目）
2. 创建 `todo.py` 主文件
3. 写入完整实现
4. 创建 `todo.json` 数据文件
5. 可能创建 `README.md`

**Step 4：运行验证**

```bash
python3 todo.py --help
python3 todo.py add "学习 Claude Code"
python3 todo.py add "练习 Prompt"
python3 todo.py list
# [ ] 1. 学习 Claude Code
# [ ] 2. 练习 Prompt

python3 todo.py done 1
python3 todo.py list
# [x] 1. 学习 Claude Code
# [ ] 2. 练习 Prompt
```

**看到以上输出 → 你已经用 Claude Code 完成了第一个完整项目。**

**Step 5：提交到 Git**

```
把刚才创建的文件提交到 Git，写一个清晰的 commit message
```

### 4.4 效率对比

| | 手动完成 | 用 Claude Code |
|--|---------|---------------|
| 写代码 | 20-30 分钟 | — |
| 调试 | 10-15 分钟 | — |
| 写 README | 5 分钟 | — |
| Git 提交 | 2 分钟 | — |
| **总计** | **40-50 分钟** | **5 分钟** |

**效率提升 8-10 倍。**

但注意：这个倍率只适用于你**明确知道要做什么**的场景。如果你自己都不清楚需求，Claude Code 也帮不了你。

**核心原则：想清楚再动手。想不清楚就让 Claude Code 帮你想（Plan Mode）。**

---

## 第5章：你的第一份 CLAUDE.md

### 5.1 CLAUDE.md 是什么？

CLAUDE.md 是你给 Claude Code 的"入职手册"——每次启动新会话时，Claude Code 会自动读取项目根目录的 CLAUDE.md。

**类比**：
- CLAUDE.md = 员工手册
- 你 = 项目经理
- Claude Code = 新入职的工程师

### 5.2 用 /init 自动生成

```bash
claude
> /init
```

Claude 会扫描项目，分析技术栈，自动生成 CLAUDE.md：

```markdown
# Project: my-todo

## Tech Stack
- Language: Python 3.11
- Runtime: None (CLI application)
- Data Storage: JSON file

## Project Structure
├── todo.py          # Main application
├── todo.json        # Data storage
└── README.md        # Documentation

## Code Style
- Follow PEP 8
- Use type hints where appropriate

## Common Commands
python3 todo.py --help    # Show help
python3 todo.py add "task" # Add a task
python3 todo.py list       # List tasks
python3 todo.py done N     # Mark done
python3 todo.py delete N   # Delete task
```

### 5.3 逐行解读

| 部分 | 作用 | 重要性 |
|------|------|--------|
| Tech Stack | 告诉 Claude 用什么技术 | ⭐⭐⭐ 避免用错技术 |
| Project Structure | 文件结构 | ⭐⭐ Claude 知道去哪找 |
| Code Style | 代码风格 | ⭐⭐⭐ 保持一致性 |
| Common Commands | 常用命令 | ⭐⭐⭐ Claude 可直接执行 |

### 5.4 手动精简原则

自动生成的 CLAUDE.md 是起点，不是终点。

**必须保留**：Tech Stack、关键风格约束、常用命令

**建议添加**：项目特定规范、禁止事项、测试要求

**应该删除**：Claude 能自动推断的信息、过度详细的目录结构

**精简示例**：

```markdown
# my-todo

## 规范
- Python 3.11，遵循 PEP 8
- 函数必须有 docstring
- 修改代码后跑 python3 todo.py list 验证

## 禁止
- 不要修改 todo.json 的格式
- 不要引入第三方依赖
```

**原则**：CLAUDE.md 越短越好。每一行都应有**增量价值**。Claude 不看也能推断出来的就删掉。

### 5.5 CLAUDE.md 的层级

| 文件位置 | 作用域 | 加载时机 |
|----------|--------|----------|
| `~/.claude/CLAUDE.md` | 全局 | 始终加载 |
| `项目根/CLAUDE.md` | 当前项目 | 在项目目录下时 |
| `子目录/CLAUDE.md` | 特定模块 | 操作该目录文件时 |

**建议**：
- 全局：个人偏好（"中文回复"、"commit message 用中文"）
- 项目级：项目规范（技术栈、风格、测试命令）
- 子目录：模块特定规则（"这个目录不要重构"）

### 5.6 提交到 Git

```bash
git add CLAUDE.md
git commit -m "docs: 添加 CLAUDE.md 项目规范"
```

团队协作时，让最了解项目的人维护 CLAUDE.md。这比口头约定有效 10 倍——因为 Claude Code **每次都会读它**。

---

## 第6章：对话基础与 Prompt 纪律

### 6.1 自然语言交互的 10 个例子

Claude Code 最强大的地方在于你不需要学特殊语法：

```
# 1. 简单请求
给 User 模型加一个 email 字段

# 2. 指定文件
@src/auth.ts 告诉我这个登录逻辑有没有安全问题

# 3. 创建功能
创建一个中间件，验证所有 /api/ 路由的 JWT token

# 4. 修复 bug
测试报告说当用户名为空时应用崩溃，修复它

# 5. 重构
utils.ts 太大了，拆分成日期工具和字符串工具

# 6. 添加测试
给 payment.ts 写单元测试，覆盖率至少 80%

# 7. 代码审查
审查最近的 commit，有没有潜在的性能问题

# 8. 生成文档
给 src/api/ 下所有路由生成 OpenAPI 文档

# 9. 多步骤
1. 创建 POST /users 路由  2. 添加请求验证  3. 写测试  4. 更新 README

# 10. 调试
npm test 第 47 个测试失败了，帮我看看原因
```

### 6.2 进阶：引用文件、图片、管道

**@ 引用文件**：

```
@src/config.ts 把 database url 改成环境变量
```

**多文件引用**：

```
@src/auth.ts @src/middleware.ts 这两个文件的认证逻辑有重复，提取到公共模块
```

**粘贴图片**：直接在终端粘贴截图，Claude Code 会分析。适合 UI 问题排查。

**管道输入**：

```bash
cat error.log | claude "分析这个错误日志，告诉我根本原因"
git diff | claude "审查这个 diff，关注安全问题"
```

### 6.3 反面教材：10 个低效 Prompt vs 高效写法

| # | ❌ 低效 | ✅ 高效 | 为什么 |
|---|--------|--------|--------|
| 1 | "帮我改一下代码" | "给 User 模型加 email 字段，需要唯一约束" | 精确 > 模糊 |
| 2 | "这个函数有问题" | "validateToken() 在 token 过期时没有抛异常" | 定位问题 |
| 3 | "改好看点" | "表格组件加上斑马纹和 hover 效果" | 具体视觉 |
| 4 | "性能不好" | "API 响应超过 2 秒，优化到 500ms 内" | 可量化目标 |
| 5 | "写个测试" | "给 charge() 写测试，覆盖正常支付、余额不足、超时" | 明确覆盖 |
| 6 | "帮我重构" | "utils.ts 超 500 行，按功能拆分成独立模块" | 明确范围 |
| 7 | "文档不好" | "给所有 public API 加 JSDoc" | 具体标准 |
| 8 | "为什么不工作？" | "`npm test` 报 'Cannot find module express'" | 错误信息 |
| 9 | "安全吗？" | "检查 SQL 注入风险，所有输入用参数化查询了吗？" | 具体检查 |
| 10 | "优化一下" | "首页 3.2 秒，目标 1 秒内。用 Lighthouse 分析" | 基线+目标 |

### 6.4 验证思维：给 Claude 成功标准

最高效的 Prompt 包含三个要素：

1. **做什么**（任务描述）
2. **怎么做**（约束条件）
3. **怎么验证**（成功标准）

```
# 差
写一个排序函数

# 好
写一个 JavaScript 排序函数：
- 支持数字和字符串数组
- 支持自定义比较函数
- 不修改原数组（返回新数组）
- 验证：[3,1,2] 排序返回 [1,2,3]
```

### 6.5 Prompt 纪律的 4 条铁律

| # | 铁律 | 理由 |
|---|------|------|
| 1 | **精确 > 模糊** | Claude 不读心术，你说不清它会猜 |
| 2 | **给约束 > 不给约束** | 无约束时 Claude 的选择可能不符合预期 |
| 3 | **给错误信息 > 描述症状** | 精确错误 > "测试不通过" |
| 4 | **给成功标准 > 不给标准** | Claude 不知道"好"的标准是什么 |

### 6.6 快捷操作速查

| 操作 | 方式 |
|------|------|
| 引用文件 | `@path/to/file` |
| 粘贴图片 | 直接粘贴截图 |
| 管道输入 | `command \| claude "prompt"` |
| 查看命令 | `/help` |
| 压缩上下文 | `/compact` |
| 查看状态 | `/status` |
| 切换模型 | `/model` |

---

## 第6.5补充：Prompt 高级技巧

### 多轮对话的上下文保持

长对话中，Claude 可能"忘记"早期的约定。解决方法：

**技巧 1：重复关键约束**

```
（第 5 轮对话时）
记住：所有 API 返回必须用 Result<T> 格式包装，这是项目规范。

现在继续修改 payment.ts...
```

**技巧 2：使用 @ 引用之前的输出**

```
@messages 上一次你说要用 Strategy 模式，请按那个方案实现。
```

**技巧 3：分阶段确认**

```
阶段 1 确认：数据模型这样设计可以吗？（列出方案）
等确认后再继续。
```

### "给 Claude 代码而不是描述"

有时候，与其用语言描述期望的行为，不如直接给代码：

```
# 差：用语言描述
写一个中间件，验证 token 是否有效，如果无效返回 401

# 好：给代码模板
按照这个模式写中间件：

const middleware = (req, res, next) => {
  try {
    // 验证逻辑
  } catch (err) {
    // 错误处理
  }
};
```

### Prompt 模板库

在你的全局 CLAUDE.md（~/.claude/CLAUDE.md）中维护常用 Prompt 模板：

```markdown
## Prompt 模板

### 新功能
实现 [功能描述]：
- 涉及文件：[文件列表]
- 验收标准：[标准]
- 约束：[约束条件]

### Bug 修复
修复 [Bug 描述]：
- 错误信息：[完整错误]
- 复现步骤：[步骤]
- 预期行为：[描述]

### 代码审查
审查 [文件/PR]：
- 重点关注：[安全/性能/可读性]
- 输出格式：严重/建议/亮点
```

### 从 Copilot 迁移的常见误区

| 误区 | 真相 |
|------|------|
| "Claude Code 应该一次写对" | Agent 模式下，迭代是正常的 |
| "我不需要理解代码了" | 你是审查者，理解力更重要 |
| "所有代码都应该让 Claude 写" | 简单的代码自己写更快 |
| "Claude 不需要指导" | 越精确的指令，越好的结果 |
| "一个会话搞定一切" | 分会话、分阶段、分任务 |


# 第二卷：核心方法论

> **学习目标**：掌握四阶段工作流、Plan Mode、上下文管理、代码审查、Git 工作流、错误调试。读完本卷后，你应该能用 Claude Code 高效地开发中等复杂度的功能。

---

## 第7章：四阶段工作流

### 7.1 为什么需要工作流？

没有工作流的 Claude Code 使用就像没有流程的团队——每次对话都在自由发挥，效率忽高忽低，质量没有保证。

四阶段工作流是 Claude Code 的核心使用范式，也是区分"随便用用"和"系统使用"的分水岭。

### 7.2 四阶段详解

**阶段 1：探索（Read Only）**

在动手之前，先让 Claude 理解现有代码。

```
@src/ 读取整个 src 目录的代码，告诉我：
1. 整体架构是什么模式
2. 主要模块有哪些，各自职责
3. 数据流是怎样的
```

**目的**：建立上下文，避免盲改。

**常见错误**：跳过这个阶段直接改代码。结果：Claude 不理解上下文，写的代码风格不一致，甚至引入 bug。

**阶段 2：规划（Plan Mode）**

按 `Ctrl+G` 或输入 `/plan` 进入 Plan Mode，让 Claude 制定修改计划。

```
基于上面的理解，我需要添加一个"用户收藏"功能。请制定实现计划：
- 涉及哪些文件
- 需要新建什么
- 修改顺序是什么
- 有什么风险
```

在 Plan Mode 中，Claude **只读取和分析，不修改任何文件**。你可以反复讨论和调整计划。

**阶段 3：实现（Edit Mode）**

再次按 `Ctrl+G` 退出 Plan Mode，让 Claude 按计划执行。

```
按照上面的计划执行。每完成一个步骤，跑一下相关测试确认没有破坏现有功能。
```

关键：让 Claude 边写边测，不要一次全改完再测。

**阶段 4：提交（Commit & PR）**

```
把所有改动提交到 Git。commit message 总结所有变更。
如果涉及多个逻辑变更，分多个 commit。
```

### 7.3 一图看懂四阶段

```
探索 ──→ 规划 ──→ 实现 ──→ 提交
(只读)  (只计划) (写代码)  (Git)
  ↓        ↓       ↓        ↓
理解上下文 制定路线 执行变更  保存成果
```

**每个阶段的退出条件**：

| 阶段 | 退出条件 |
|------|----------|
| 探索 | Claude 准确描述了项目架构 |
| 规划 | 你认可了实现计划，没有遗漏 |
| 实现 | 所有测试通过，功能符合预期 |
| 提交 | 代码已提交，PR 已创建（如需） |

### 7.4 何时可以跳过探索和规划？

| 场景 | 能跳过吗 | 原因 |
|------|----------|------|
| 小 bug 修复 | ✅ 可以 | 改动范围小，上下文简单 |
| 新增一个简单函数 | ⚠️ 谨慎 | 看似简单可能有隐含依赖 |
| 新增完整功能 | ❌ 不行 | 涉及多文件，需要上下文 |
| 重构 | ❌ 不行 | 理解现有设计才能重构好 |
| 修复复杂 bug | ❌ 不行 | 需要理解根因，不能盲改 |

### 7.5 实战：用四阶段添加"用户收藏"功能

假设你有一个博客系统，要添加"收藏文章"功能。

**Step 1：探索**

```
@src/ 读取项目代码。告诉我：
1. 用户认证是怎么做的？
2. 文章数据模型长什么样？
3. 现有的 API 路由结构
```

确认 Claude 理解了项目结构。

**Step 2：规划（Ctrl+G）**

```
需要添加"收藏文章"功能。用户可以收藏/取消收藏文章，查看收藏列表。
请制定实现计划，包括数据库变更、API 端点、前端组件、修改顺序。
```

讨论和调整计划，直到满意。

**Step 3：实现（Ctrl+G 退出）**

```
按计划执行。每完成一个步骤确认代码写好、跑测试、告诉我进度。
```

**Step 4：提交**

```
所有改动提交到 Git。创建一个 PR。
```

### 7.6 四阶段工作流的关键收益

| 收益 | 说明 |
|------|------|
| 减少返工 | 先理解再动手，避免改错方向 |
| 提高质量 | 规划阶段发现潜在问题 |
| 保持控制 | 你在每一步都有决定权 |
| 可追溯 | 计划记录了"为什么这样做" |
| 效率稳定 | 不依赖"运气好" |

---

## 第8章：Plan Mode 深度实践

### 8.1 Plan Mode 是什么？

Plan Mode 是 Claude Code 的**只读规划模式**。进入后，Claude 只能读取和分析代码，**不能修改任何文件**。

这是一个强大的"安全阀"——你可以在没有风险的环境下让 Claude 理解项目、分析问题、制定计划。

### 8.2 进入和退出

```bash
# 快捷键
Ctrl+G       # 切换 Plan Mode（开关式）

# 命令
/plan        # 进入 Plan Mode
/edit        # 退出 Plan Mode
```

### 8.3 Plan Mode 中的 5 种对话技巧

**技巧 1：问架构**

```
分析这个项目的整体架构。画出模块依赖关系。
```

**技巧 2：问影响范围**

```
如果我修改 User 模型添加一个 role 字段，会影响哪些文件？
```

**技巧 3：问风险**

```
这个重构计划有什么潜在风险？最坏情况是什么？
```

**技巧 4：让 Claude 做技术选型**

```
我需要添加全文搜索功能。比较 Elasticsearch 和 Meilisearch 在我们这个项目中的优劣。
```

**技巧 5：生成检查清单**

```
生成一个完整的实现检查清单，包括需要修改的每个文件和每个步骤。
```

### 8.4 规划粒度控制

| 问题 | 表现 | 解决方案 |
|------|------|----------|
| **太细** | 计划写了 30 步包括每行代码 | 保留到模块/函数级别 |
| **太粗** | "添加搜索功能" 就结束了 | 至少列出文件、数据模型、API 端点 |
| **太理想** | 没考虑错误处理和边界情况 | 要求列出风险和边界 |
| **太静态** | 没有步骤之间的依赖关系 | 要求标注执行顺序和依赖 |

**好的规划粒度**：每个步骤对应一个可以独立验证的变更。

```
# 太粗
1. 添加搜索功能

# 太细
1. 在 line 47 插入 import { SearchService }
2. 在 line 123 添加 search() 方法...

# 刚好
1. 创建 SearchService 模块（search.ts）
2. 添加 search API 路由（routes/search.ts）
3. 在 Product 模型添加搜索相关字段
4. 创建搜索 UI 组件
5. 添加搜索结果页面
```

### 8.5 实战：重构遗留函数

假设你有一个 200 行的 `processOrder()` 函数需要重构。

**Step 1：进入 Plan Mode（Ctrl+G）**

```
@src/services/order.ts 读取 processOrder() 函数。
分析它做了什么，分成哪些逻辑块。
制定重构计划：如何拆分成更小的函数。
```

**Step 2：讨论计划**

```
这个计划不错，但我担心拆分后性能受影响。能分析一下函数调用开销吗？
```

**Step 3：退出 Plan Mode，执行**

```
（Ctrl+G 退出）按计划重构。重构后跑所有测试确认没有破坏功能。
```

### 8.6 Plan Mode 的心理价值

Plan Mode 不仅仅是一个功能——它改变了你与 Claude Code 的交互模式：

- **降低焦虑**：不用担心 Claude 乱改文件
- **提高质量**：有时间思考和讨论
- **学习机会**：在安全环境下理解代码
- **信任建立**：看到 Claude 的分析能力后，更放心让它执行

---

## 第9章：上下文管理

### 9.1 上下文窗口是什么？

想象 Claude Code 的上下文窗口是一个**白板**。

每次对话，白板上会写入：
- 系统提示（CLAUDE.md、工具定义等）
- 你说的话
- Claude 的回复
- Claude 读到的文件内容
- Claude 跑命令的输出

白板有大小限制（通常 200k Token）。**白板满了之后，早期内容会被挤出去。**

**比喻**：200k Token ≈ 一本 300 页的书。看起来很多，但一次复杂任务（读多个文件、多次修改）很快就会填满。一旦满了，Claude 就"忘了"早期的对话内容。

### 9.2 上下文填满后的性能退化

**实验数据**（基于社区反馈）：

| 上下文使用率 | Claude 表现 |
|-------------|-------------|
| 0-50% | 精准、高效 |
| 50-75% | 轻微退化，偶尔忘记早期细节 |
| 75-90% | 明显退化，可能重复之前的对话 |
| 90-100% | 严重退化，可能产生幻觉 |

**关键洞察**：不是"满了才出问题"，而是**超过 75% 就开始退化**。

### 9.3 五种管理策略

**策略 1：@ 引用而非粘贴**

```
# 差：把文件内容粘贴到对话中
[粘贴 500 行代码] 请帮我优化这个函数

# 好：用 @ 引用
@src/utils/parser.ts 优化 parseData() 函数
```

Claude Code 会智能地只加载文件中相关的部分，而不是整个文件。

**策略 2：管道输入**

```bash
# 不把整个文件加载到对话上下文
cat error.log | claude "分析最近的错误，告诉我根因"
git diff | claude "审查这个 diff"
```

管道输入创建一个独立的小上下文，不污染主会话。

**策略 3：Subagent 隔离**

```
让 Subagent 分析 src/legacy/ 目录下所有文件的代码质量，输出一份报告。
```

Subagent 在独立会话中运行，完成后结果回传。主会话上下文不受影响。

**策略 4：/compact 及时压缩**

```
/compact
```

当感觉对话变长时运行。Claude 会总结之前的对话，用更少的 Token 保留关键信息。

**策略 5：定期开新会话**

```
# 好习惯
会话1：完成用户模块重构
会话2：完成支付模块重构
会话3：完成 API 文档更新

# 坏习惯
会话1：用户模块 + 支付模块 + 文档 + 测试 + ...
```

### 9.4 状态栏监控

Claude Code 的状态栏显示当前上下文使用情况：

```
Context: 125k/200k (62%) | Tokens: $0.42 | Model: claude-sonnet-4
```

**阈值建议**：
- 🟢 绿灯（< 50%）：放心使用
- 🟡 黄灯（50-75%）：注意控制
- 🔴 红灯（> 75%）：考虑 /compact 或开新会话

### 9.5 帕累托法则

80% 的上下文问题来自 20% 的坏习惯：

| 坏习惯 | 占上下文 | 解决方案 |
|--------|---------|----------|
| 贴大文件 | 30-50% | 用 @ 引用 |
| 不用 Subagent | 20-30% | 耗时任务用 Subagent |
| 不压缩长对话 | 15-25% | 定期 /compact |
| 一个会话做太多事 | 10-20% | 分会话 |

掌握这四个习惯，你的上下文管理就能超越 90% 的用户。

---

## 第10章：代码审查与验证

### 10.1 为什么必须审查

Claude Code 很强大，但它**不是完美的**。

常见问题：
- 可能引入安全漏洞
- 可能选择不当的实现方式
- 可能忽略边界情况
- 可能写出不符合项目风格的代码
- 可能过度工程化

**铁律：Claude 写的每一行代码都需要你审查。**

这不是不信任——这是职业习惯。即使是最资深的同事提交的代码，你也会做 Code Review。

### 10.2 审查清单

每次 Claude 修改代码后，按以下清单审查：

**安全检查**：
- [ ] 没有硬编码的密钥/密码
- [ ] 用户输入有验证和清洗
- [ ] SQL 查询用了参数化（防注入）
- [ ] 文件路径没有遍历风险
- [ ] 权限检查到位

**性能检查**：
- [ ] 没有 N+1 查询
- [ ] 没有不必要的循环嵌套
- [ ] 大数据集有分页
- [ ] 没有内存泄漏风险

**可读性检查**：
- [ ] 变量命名清晰
- [ ] 函数不超过 50 行
- [ ] 有必要的注释（但不过度）
- [ ] 符合项目代码风格

**正确性检查**：
- [ ] 逻辑正确
- [ ] 边界情况处理
- [ ] 错误处理完善
- [ ] 与现有代码兼容

### 10.3 测试驱动验证

与其写完再审查，不如让 Claude 先写测试：

```
我要修改 payment.ts 中的 charge() 方法，支持分期付款。

步骤：
1. 先为 charge() 写测试，覆盖当前行为（回归测试）
2. 跑测试确认全部通过（记录基线）
3. 修改 charge() 添加分期功能
4. 添加分期相关的测试用例
5. 跑所有测试确认通过
```

好处：
- 自动验证没有破坏现有功能
- 测试用例就是"可执行的需求文档"
- 出了问题容易定位

### 10.4 Chrome 扩展做 UI 验证

对于涉及 UI 的修改，安装 Claude Code Chrome 扩展：

1. 安装扩展
2. 在 Chrome 中打开你的应用
3. 让 Claude 对比修改前后截图

```
修改前：[粘贴当前 UI 截图]
修改后：[让 Claude 截取新 UI]
对比两张截图，确认 UI 变更符合预期。
```

### 10.5 让 Claude 自我审查

```
刚才你修改了 auth.ts，请告诉我：
1. 改了什么
2. 为什么这样改
3. 有没有潜在的安全风险
4. 有没有遗漏的边界情况
```

---

## 第11章：Git 工作流

### 11.1 让 Claude 做 Commit 和 PR

Claude Code 可以直接操作 Git——这是 Agent 模式的核心优势之一。

**创建 Commit**：

```
把所有改动提交到 Git。commit message 用中文，简洁描述改了什么。
```

**创建 PR**：

```
基于当前分支创建一个 Pull Request。
PR 描述包括：改了什么、为什么改、怎么验证。
```

### 11.2 Commit Message 规范

在 CLAUDE.md 中定义 commit 规范，Claude 会自动遵守：

```markdown
## Git 规范

### Commit Message 格式
类型(范围): 简短描述

类型：
- feat: 新功能
- fix: 修复 bug
- refactor: 重构
- docs: 文档
- test: 测试
- chore: 构建/工具

示例：
feat(auth): 添加 JWT 刷新机制
fix(payment): 修复金额计算精度问题
refactor(utils): 拆分 parseData 为独立模块
```

### 11.3 Git Worktrees 并行开发

Git Worktree 让你同时在不同分支工作。Claude Code 支持通过 Subagent + Worktree 实现并行开发。

**场景**：同时开发两个 feature。

```
Subagent 1 在 worktree-A（feature/search）上工作
Subagent 2 在 worktree-B（feature/export）上工作
主会话保持干净
```

### 11.4 完整 Feature 分支流程

```bash
# Step 1：创建分支
git checkout -b feature/user-favorites

# Step 2：用 Claude Code 开发
claude
> （按四阶段工作流完成开发）

# Step 3：推送并创建 PR
git push origin feature/user-favorites
```

### 11.5 Git 相关技巧

| 技巧 | Claude 能做的 |
|------|--------------|
| "看看最近的 commit" | git log 查看 |
| "这个 PR 改了什么" | 分析 git diff |
| "回滚到上一个 commit" | git reset |
| "合并冲突了" | 分析冲突并解决 |
| "创建 release branch" | 创建并推送 |

---

## 第12章：错误处理与调试

### 12.1 Claude 犯错时的恢复策略

Claude Code 不是完美的。它有时候会：
- 写有 bug 的代码
- 误解你的需求
- 忽略边界情况
- 选择不当的实现

**错误是正常的，关键是快速恢复。**

### 12.2 四步恢复法

**Step 1：识别错误**

```
跑一下测试，看看有没有失败。
```

**Step 2：定位问题**

```
# 好：给 Claude 精确的错误信息
运行 npm test 输出以下错误：
TypeError: Cannot read properties of undefined (reading 'email')
  at UserSerializer.serialize (src/serializers/user.ts:15:23)

帮我定位根因。
```

**Step 3：修复**

```
找到原因了。请修复 user.ts 中的序列化逻辑，添加 null 检查。
```

**Step 4：验证**

```
修复后重新跑测试，确认通过。
```

### 12.3 "粘贴错误信息 > 描述症状"

这是调试效率的分水岭：

| ❌ 描述症状 | ✅ 粘贴错误信息 |
|------------|----------------|
| "代码跑不起来" | `Error: ECONNREFUSED 127.0.0.1:5432` |
| "测试失败了" | `FAIL src/auth.test.ts > should reject invalid token` |
| "性能不好" | `Response time: 3400ms (P95), DB queries: 47/request` |
| "页面白屏了" | `Uncaught TypeError: undefined at App.tsx:23` |

**一个精确的错误信息 = 省掉 5 轮来回澄清。**

### 12.4 调试循环：假设→验证→修复

有效的调试遵循科学方法论：

```
假设：可能是数据库连接超时导致
验证：查看数据库日志，确认连接状态
  → 假设成立 → 修复连接池配置
  → 假设不成立 → 提出新假设
```

让 Claude Code 也按这个循环工作：

```
测试失败了。请按以下步骤调试：
1. 分析错误信息，提出 2-3 个可能的原因
2. 对每个假设设计验证方法
3. 按可能性从高到低验证
4. 找到根因后修复
5. 验证修复有效
```

### 12.5 常见错误模式

| 错误模式 | 表现 | 应对策略 |
|----------|------|----------|
| **幻觉** | 声称不存在的函数/模块 | 让 Claude 先验证文件是否存在 |
| **过度修改** | 改了太多不该改的 | Plan Mode 先确认修改范围 |
| **忽略上下文** | 代码风格不一致 | CLAUDE.md 中明确风格约束 |
| **循环修改** | 改了又改，越改越乱 | 开新会话，重新从探索开始 |
| **Token 溢出** | 对话太长开始"健忘" | /compact 或开新会话 |

### 12.6 终极调试技巧

```
我在修复一个 bug，已尝试 X 和 Y 都没解决。
当前错误信息是：[粘贴完整错误]

请帮我：
1. 回顾整个修改历史
2. 分析 X 和 Y 为什么没解决
3. 提出新的假设和验证步骤
```

有时候 Claude 在新会话中反而能发现问题——没有"历史包袱"，会从全新角度分析。

---

## 第12章补充：调试进阶

### 二分法调试

当代码库很大、bug 位置不明时，用二分法缩小范围：

```
这个功能在某个时间点之后坏了。
帮我用 git bisect 找到引入 bug 的 commit。

步骤：
1. git bisect start
2. git bisect bad HEAD（当前版本有问题）
3. git bisect good <最后一个正常版本>
4. 每次告诉我测试结果，我来决定继续

先帮我执行 git bisect start，然后我来提供信息。
```

### 性能分析

```
这个 API 端点响应时间超过 2 秒，帮我分析瓶颈。

步骤：
1. 添加计时日志到关键路径
2. 识别最慢的步骤
3. 分析原因（数据库查询？循环？外部 API？）
4. 提出优化方案
5. 实现优化并验证
```

### 安全审计清单

让 Claude 做一次全面的安全审计：

```
对 src/ 目录下的所有代码做安全审计，检查以下 OWASP Top 10：
1. 注入（SQL、NoSQL、命令）
2. 认证失效
3. 敏感数据暴露
4. XML 外部实体（XXE）
5. 访问控制失效
6. 安全配置错误
7. 跨站脚本（XSS）
8. 不安全的反序列化
9. 使用含已知漏洞的组件
10. 日志和监控不足

输出严重等级：🔴 关键  🟡 中等  🟢 低风险
每个问题附上具体文件和行号。
```


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


# 第四卷：高级工作流

> **学习目标**：掌握 Worktrees 并行开发、Chrome 扩展 UI 验证、Web 版使用、Headless CI/CD、Power-ups、Remote Control、语音输入、Slack 集成。读完本卷后，你掌握了 Claude Code 的全部核心功能。

---

## 第19章：Git Worktrees 并行开发

### 19.1 什么是 Git Worktree？

Git Worktree 允许你在同一个仓库下，**同时检出多个分支到不同目录**。每个 worktree 是独立的工作目录，但共享同一个 `.git` 仓库。

**比喻**：一个仓库，多间办公室。每间办公室处理不同的事务，但共享同一份档案。

### 19.2 为什么需要 Worktree？

| 问题 | 没有 Worktree | 有 Worktree |
|------|--------------|-------------|
| 同时开发两个 feature | 需要频繁 stash/checkout | 各自独立工作 |
| 一个紧急 bug 中断当前工作 | stash → 修复 → stash pop | 开新 worktree 直接修 |
| Claude 改一半想试另一个方向 | 保存当前进度 → 回来恢复 | 直接在新 worktree 试 |

### 19.3 基本操作

```bash
# 创建 worktree
git worktree add ../my-project-feature-search feature/search

# 列出所有 worktree
git worktree list

# 删除 worktree
git worktree remove ../my-project-feature-search
```

### 19.4 Claude Code 中的 Worktree 操作

Claude Code 可以通过内置工具直接操作 Worktree：

```
创建一个新的 worktree，分支名为 feature/user-search，路径为 ../my-project-search。
在新的 worktree 中实现用户搜索功能。
```

Claude 会自动：
1. `git worktree add` 创建目录
2. 在新目录中开发
3. 完成后告诉你结果

### 19.5 Subagent + Worktree 隔离

**最佳实践**：让 Subagent 在独立 Worktree 中工作，避免互相干扰。

```
让 Subagent 在 worktree ../my-project-search（分支 feature/search）中实现搜索功能。
同时让另一个 Subagent 在 worktree ../my-project-export（分支 feature/export）中实现导出功能。
```

两个 Subagent 在不同目录、不同分支上并行工作，互不影响。

### 19.6 Worktree 使用流程

```
1. git worktree add ../project-branch-name branch-name
2. claude（在 worktree 目录中启动）
3. 正常开发...
4. git push origin branch-name
5. git worktree remove ../project-branch-name
```

**注意事项**：
- 同一个分支不能同时出现在多个 worktree 中
- 用完记得删除 worktree，避免积累
- Worktree 目录默认在仓库的上级目录，保持整洁

### 19.7 常见问题

| 问题 | 解决方案 |
|------|----------|
| "branch already checked out" | 该分支已在其他 worktree 中，换一个分支 |
| Worktree 目录残留 | `git worktree prune` 清理 |
| Claude 在错误的 worktree | 明确指定路径 `cd ../project-branch-name` |

---

## 第20章：Chrome 扩展

### 20.1 什么是 Claude Code Chrome 扩展？

Claude Code Chrome 扩展让 Claude Code 能**看到你的浏览器页面**——截图、分析 DOM、对比 UI 变更。

**核心能力**：
- 截取当前页面截图
- 分析页面结构和内容
- 对比修改前后的 UI
- 在 Claude Code 中直接引用浏览器中的信息

### 20.2 安装与配置

1. 打开 Chrome → 访问 Chrome Web Store
2. 搜索 "Claude Code" 扩展 → 安装
3. 点击扩展图标 → 连接到你的 Claude Code 实例
4. 确认连接成功（图标状态变化）

### 20.3 使用方式

**截图分析**：

```
[在 Chrome 中点击 Claude Code 扩展图标，截图当前页面]

分析这个页面的布局。告诉我：
1. 整体布局结构
2. 导航栏是否响应式
3. 有没有明显的 UX 问题
```

**UI 变更验证**：

```
[修改前截图] 这是当前的登录页面。

现在让我修改登录页面的样式。

[修改后截图] 这是修改后的页面。

对比两张截图，确认变更符合预期。
特别关注：按钮位置、表单对齐、错误提示位置。
```

**截图对比**：

```
[截图 A] 修改前
[截图 B] 修改后

列出所有差异。有没有意外的变更？
```

### 20.4 实战：实现并验证 UI 组件

```
我需要给表格组件添加排序功能。

步骤：
1. 先用 Chrome 扩展截图当前表格
2. 在 Claude Code 中实现排序逻辑
3. 刷新页面，再次截图
4. 对比两张截图，确认排序功能正常
5. 测试升序、降序、不同列排序
```

### 20.5 Chrome 扩展的局限

| 局限 | 说明 |
|------|------|
| 无法交互 | 只能截图和分析，不能点击按钮 |
| 静态快照 | 看到的是截图那一刻的状态 |
| 需要手动触发 | 每次截图需要点击扩展图标 |

对于需要交互的场景，Claude Code 内置的浏览器控制能力（headless browser）更适合。

---

## 第21章：Claude Code on the Web

### 21.1 claude.ai/code 是什么？

Anthropic 提供了 Claude Code 的网页版本，可以直接在 claude.ai 上使用，不需要本地安装。

**访问方式**：https://claude.ai/code

### 21.2 与本地版的区别

| 维度 | 本地版 | Web 版 |
|------|--------|--------|
| 安装 | 需要 npm + Node.js | 无需安装 |
| 系统权限 | 完整权限（文件、Shell） | 受限（沙箱环境） |
| 模型选择 | 任意 Anthropic 模型 | Anthropic 指定模型 |
| 定制化 | CLAUDE.md、Hooks、Skills | 有限支持 |
| 数据安全 | 数据在你本地 | 数据在 Anthropic 服务器 |
| 网络要求 | 首次登录需要 | 始终需要 |

### 21.3 适用场景

**Web 版适合**：
- 快速体验 Claude Code
- 没有本地开发环境
- 临时使用（出差、借用电脑）
- 简单的代码问题

**本地版适合**：
- 日常开发工作
- 需要系统权限（文件、Shell）
- 需要定制化（CLAUDE.md、Hooks）
- 数据安全要求高

### 21.4 建议

如果你认真学 Claude Code，**本地版是必须的**。Web 版可以作为补充——不方便带电脑时临时使用。

---

## 第22章：Headless 模式与 CI/CD

### 22.1 什么是 Headless 模式？

Headless 模式是 Claude Code 的**非交互式执行模式**——不需要人工参与，Claude Code 自动完成任务。

这是将 Claude Code 集成到自动化流程（CI/CD）的基础。

### 22.2 基本用法

```bash
# 单次执行
claude -p "审查最近的 commit，输出安全风险报告"

# 管道输入
git diff | claude -p "审查这个 diff"

# 指定输出格式
claude -p "生成 API 文档" --output-format json
```

`-p` 参数表示"print mode"：执行任务后输出结果并退出，不进入交互式会话。

### 22.3 实战：GitHub Actions 集成

在 `.github/workflows/claude-review.yml` 中：

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "审查这个 PR 的所有变更。关注：安全性、性能、代码风格。输出结构化审查报告。" \
            --output-format text > review.md

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('review.md', 'utf8');
            github.rest.issues.createComment({
              ...context.repo,
              issue_number: context.issue.number,
              body: review
            });
```

每次创建或更新 PR 时，Claude Code 自动审查并将结果作为 PR 评论发布。

### 22.4 实战：GitLab CI/CD 集成

```yaml
# .gitlab-ci.yml
claude-review:
  stage: review
  image: node:22
  before_script:
    - npm install -g @anthropic-ai/claude-code
  script:
    - claude -p "审查最近的 commit，输出安全审查报告" --output-format text
  variables:
    ANTHROPIC_API_KEY: $CLAUDE_API_KEY
  only:
    - merge_requests
```

### 22.5 Headless 模式最佳实践

| 实践 | 说明 |
|------|------|
| 限制输出长度 | 用 `--max-tokens` 避免超长输出 |
| 指定输出格式 | `--output-format json/text/markdown` |
| 设置超时 | `timeout` 命令包裹，避免无限运行 |
| 缓存控制 | CI 环境中注意 Token 成本 |
| 幂等性 | 确保 Claude 的操作是幂等的（多次运行结果一致） |

---

## 第23章：Power-ups 与 Fast Mode

### 23.1 什么是 Power-ups？

Power-ups 是 Claude Code 的**增强功能模块**——可以为当前会话添加额外的能力和上下文。

### 23.2 /powerup 命令

```
/powerup
```

Claude 会展示可用的 Power-ups 列表，你可以选择启用。

**典型 Power-ups**：
- **代码搜索增强**：更智能的代码搜索
- **文档生成**：自动为修改的代码生成文档
- **测试建议**：基于代码变更建议测试用例

### 23.3 Fast Mode

Fast Mode 是 Claude Code 的**快速响应模式**——用更小的模型处理简单任务，降低延迟和成本。

```
/fast
```

**适用场景**：
- 简单的代码查询
- 文件搜索
- 格式化操作
- 不需要深度推理的任务

**不适用场景**：
- 复杂的架构设计
- 难以定位的 bug
- 需要深度推理的任务

### 23.4 模式切换策略

```
日常简单任务 → Fast Mode（快速+便宜）
复杂开发任务 → 正常模式（Claude Sonnet）
特别复杂任务 → 高级模式（Claude Opus）
```

---

## 第24章：Remote Control

### 24.1 什么是 Remote Control？

Remote Control 让你在**一个 Claude Code 会话中控制另一个远程会话**。

**场景**：你在本地电脑上运行 Claude Code，但需要在远程服务器上执行操作。

### 24.2 使用方式

```bash
# 在远程服务器上启动 Claude Code（作为被控端）
claude --remote

# 在本地连接到远程会话
claude --connect user@server:18789
```

### 24.3 典型工作流

```
本地 Claude Code → SSH 连接 → 远程服务器上的 Claude Code
                                    ↓
                              操作远程文件
                              运行远程命令
                              修改远程配置
```

### 24.4 注意事项

- 需要网络连接稳定
- API 调用发生在本地（本地需要 API Key）
- 敏感操作建议在 Plan Mode 中先审查

---

## 第25章：Voice Dictation

### 25.1 语音输入

Claude Code 支持语音输入——用自然语言描述需求，而不需要打字。

### 25.2 使用方式

在支持的终端或 VS Code 中：

1. 点击麦克风图标（或按快捷键）
2. 说出你的需求
3. Claude Code 将语音转文字，然后正常处理

**适合场景**：
- 手不方便打字时
- 边想边说的头脑风暴
- 描述复杂需求时（说话比打字快）

### 25.3 语音输入的最佳实践

- **语速适中**：太快会识别错误
- **说完整句子**：不要只说关键词
- **环境安静**：噪音影响识别精度
- **说完检查**：确认转写结果正确后再发送

---

## 第26章：Slack 集成与 @Claude

### 26.1 Slack 中的 Claude Code

Claude Code 可以集成到 Slack 工作空间，在 Slack 频道或 DM 中直接与 Claude 交互。

### 26.2 配置方式

1. 在 Slack 创建一个 Bot 应用
2. 获取 Bot Token
3. 在 Claude Code 配置中添加 Slack 通道

```json
{
  "channels": {
    "slack": {
      "botToken": "xoxb-xxxxx",
      "appToken": "xapp-xxxxx"
    }
  }
}
```

### 26.3 使用方式

在 Slack 中：
- **DM**：直接给 Claude Bot 发消息
- **频道**：@Claude 提及，Claude 会回复
- **线程**：在特定线程中与 Claude 交互

### 26.4 团队使用场景

| 场景 | 说明 |
|------|------|
| 代码审查 | PR 链接发给 Claude，自动审查 |
| 知识问答 | 团队成员 @Claude 问技术问题 |
| 任务分配 | "Claude，创建一个 issue 描述这个 bug" |
| 文档生成 | "Claude，根据这个讨论生成设计文档" |

### 26.5 Slack vs 其他通道

| 维度 | Slack | 飞书 | Telegram |
|------|-------|------|----------|
| 团队协作 | ⭐⭐⭐ 最佳 | ⭐⭐ 好 | ⭐ 个人用 |
| 代码片段 | ⭐⭐ 好 | ⭐⭐ 好 | ⭐ 一般 |
| 文件传输 | ⭐⭐ 好 | ⭐⭐⭐ 最佳 | ⭐ 一般 |
| 配置复杂度 | 中等 | 中等 | 简单 |

选择适合你团队的通道即可，Claude Code 对所有通道的支持基本一致。

---

## 第22章补充：CI/CD 进阶

### 多阶段 Claude Code 工作流

```yaml
# .github/workflows/claude-full.yml
name: Claude Code Full Workflow

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install
        run: npm install -g @anthropic-ai/claude-code

      - name: Security Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.CLAUDE_KEY }}
        run: |
          claude -p "安全审查这个 PR 的所有变更。检查 OWASP Top 10。" \
            --output-format text > security-report.md

      - name: Performance Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.CLAUDE_KEY }}
        run: |
          claude -p "性能审查：检查 N+1 查询、内存泄漏、不必要的循环。" \
            --output-format text > perf-report.md

      - name: Style Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.CLAUDE_KEY }}
        run: |
          claude -p "代码风格审查：命名、结构、注释、一致性。" \
            --output-format text > style-report.md

      - name: Post Combined Review
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const security = fs.readFileSync('security-report.md', 'utf8');
            const perf = fs.readFileSync('perf-report.md', 'utf8');
            const style = fs.readFileSync('style-report.md', 'utf8');
            const body = `## 🔒 安全审查\n${security}\n\n## ⚡ 性能审查\n${perf}\n\n## 🎨 风格审查\n${style}`;
            github.rest.issues.createComment({
              ...context.repo,
              issue_number: context.issue.number,
              body
            });
```

### Claude Code 在自动化中的最佳实践

| 实践 | 说明 |
|------|------|
| 限制审查范围 | 只审查 diff，不审查整个代码库 |
| 设置 Token 上限 | `--max-tokens 4096` 控制输出长度 |
| 分离关注点 | 安全、性能、风格分别审查 |
| 缓存依赖 | CI 中缓存 npm 包减少构建时间 |
| 并行执行 | 多个审查任务并行运行 |
| 结果聚合 | 多个审查结果合并成一条评论 |

### Docker 中的 Claude Code

```dockerfile
FROM node:22-bookworm

RUN npm install -g @anthropic-ai/claude-code

# 复制项目代码
WORKDIR /app
COPY . .

# 复制 CLAUDE.md
COPY CLAUDE.md ./

ENV ANTHROPIC_API_KEY=your-key

# Headless 模式执行
CMD ["claude", "-p", "审查代码并输出报告"]
```


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


---

# 后记：从工具到思维方式的进化

## 你已经学到了什么

翻到这一页，你已经读完了 30 章 + 4 个附录，覆盖了 Claude Code 从安装到团队协作的全部知识。但更重要的是，你可能已经意识到：

**Claude Code 不只是一个工具——它是一种全新的工作方式。**

回顾你的学习路径：

| 阶段 | 你学到的 | 你的角色变化 |
|------|----------|-------------|
| 第一卷 | 安装、配置、CLAUDE.md | 从"用户"变成"管理者" |
| 第二卷 | 四阶段工作流、Plan Mode | 从"写代码"变成"描述需求" |
| 第三卷 | Hooks、Subagents、Skills | 从"单个Agent"变成"系统构建者" |
| 第四卷 | Worktrees、CI/CD、MCP | 从"本地使用"变成"流程自动化" |
| 第五卷 | 实战项目、团队协作 | 从"个人效率"变成"团队效率" |

## 四个核心思维模型

经过 100 页的学习，真正需要记住的其实只有四个思维模型：

**1. 管理者思维**
> 你不是在用 AI 写代码，你是在管理一个 AI 工程师团队。

**2. 验证思维**
> 永远给 Claude 成功标准。不要说"改好看点"，要说"加上斑马纹和 hover 效果"。

**3. 分层思维**
> Plan Mode 想清楚 → Hooks 约束行为 → Skills 封装流程 → Subagent 隔离任务。

**4. 迭代思维**
> 不追求一次写对。快速迭代、频繁验证、及时 /compact。

## 为什么方法论比工具重要

Claude Code 会更新。也许明年就出了 Claude Code v2，界面变了、命令变了、甚至底层架构都变了。

但四阶段工作流不会变。验证思维不会变。上下文管理的原则不会变。

这就是为什么这本指南花了大量篇幅在"思维方式"上——因为**工具是会过时的，但思维方式是永久的**。

## 接下来做什么

**如果你是个人开发者**：
1. 把 CLAUDE.md 用起来（第5章）
2. 坚持四阶段工作流一周（第7章）
3. 安装 2-3 个 MCP Server 试试（第16章）

**如果你是团队管理者**：
1. 建立团队共享 CLAUDE.md（第30章）
2. 配置 Hooks 安全防护（第13章）
3. 在 CI/CD 中集成代码审查（第22章）

**如果你是高级玩家**：
1. 创建自定义 MCP Server（第16章补充）
2. 搭建多工具自动化工作流（第29章）
3. 尝试 Agent Teams（第18章）

## 最后的话

Claude Code 的核心开发者 Boris Cherny 说过：

> "我从来没像今天这样享受写代码——因为我再也不用处理那些琐事了。"

这就是 Agent 时代的承诺：**让机器处理琐事，让人专注于创造。**

但这个承诺有个前提——你需要学会如何管理 Agent。而你已经学完了这本指南。

**现在，去创造吧。** 🚀

---

> 本指南总字数约 4 万字，覆盖 30 个章节和 4 个附录。
> 基于 2026 年 5 月的 Claude Code 最新版本编写。
> 建议关注 docs.anthropic.com/claude-code 获取最新更新。

> **全书完**
>
> 本指南基于 2026 年 5 月公开资料及实际使用经验整理。Claude Code 更新频繁，建议关注官方文档获取最新特性。
>
> **记住**：工具会变，但方法论不变。四阶段工作流、验证思维、上下文管理——这些原则无论 Claude Code 怎么更新都适用。
>
> 祝你在 AI Agent 时代，成为一个高效的产品经理型开发者。🚀
