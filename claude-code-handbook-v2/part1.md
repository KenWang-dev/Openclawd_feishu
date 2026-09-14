# Claude Code 从入门到精通自学指南（100页完整版）

> **版本**: 2026年5月 | **基于**: Claude Code v1.x 最新版 | **方法论**: 第一性原理 × 帕累托法则 × 认知阶梯理论

---

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

