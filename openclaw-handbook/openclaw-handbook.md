# OpenClaw 从入门到精通自学手册

> **版本**: 2026年5月 | **基于**: OpenClaw v2026.2.25 | **原则**: 第一性原理 x 帕累托法则 x MECE x 金字塔原理

---

## 引言：为什么 OpenClaw 值得系统学习

OpenClaw 是一个**开源、自托管的 AI Agent 网关**——不是又一个聊天机器人，而是一个能让 AI 从被动回答者变成主动任务执行者的运行时平台。

**核心定位**：本地优先（Local-First）、多通道（Multi-Channel）、Agent 原生（Agent-Native）。

**数据说话**：
- 2026年成为 GitHub 最火开源项目之一
- BBC、知乎、腾讯云等主流媒体专题报道
- 阿里云百炼平台官方集成支持
- 26 个内置工具 + 53+ 官方 Skills
- 支持 20+ 消息通道（Telegram、WhatsApp、Discord、飞书、Slack 等）

**关键理解**：
- OpenClaw 不生产 AI 模型——它消费 AI 模型
- OpenClaw 不是 ChatGPT 套壳——它是 Agent 运行时
- OpenClaw 不是云服务——它跑在你自己的机器上

---

## 第一部分：快速上手（Day 1）

### 1.1 什么是 OpenClaw？

OpenClaw 是一个**自托管的 Gateway**，连接你的消息应用和 AI Agent。架构极其简洁：

```
消息应用（飞书/Telegram/Discord...）→ Gateway → AI Agent（Claude/GPT/Gemini...）
```

Gateway 是唯一的控制平面，负责会话管理、路由分发、工具调度。

**与其他方案的本质区别**：

| 维度 | ChatGPT/Claude.ai | Cursor/Copilot | OpenClaw |
|------|-------------------|----------------|----------|
| 托管方式 | 云端 | 本地IDE | 自托管 |
| 消息通道 | 仅网页/APP | 仅IDE | 20+ 通道 |
| 模型选择 | 锁定自家 | 有限选择 | 任意模型 |
| 工具能力 | 有限 | 代码为主 | 全系统权限 |
| 数据控制 | 不在你手里 | 本地 | 完全自主 |
| 自动化 | 无 | 无 | Cron + 心跳 |

### 1.2 安装与首次启动

**前置条件**：
- Node.js >= 22（推荐 24）
- 一个 AI 模型的 API Key（Claude / GPT / GLM 等）
- 5 分钟

```bash
# 安装
npm install -g openclaw@latest

# 引导式初始化（含 Gateway 安装）
openclaw onboard --install-daemon

# 打开浏览器控制面板
openclaw dashboard
```

控制面板默认地址：http://127.0.0.1:18789/

**飞书接入（最快通道）**：
1. 在飞书开放平台创建机器人应用
2. 获取 App ID 和 App Secret
3. 在配置文件中填入凭证
4. 发布应用，开始对话

### 1.3 核心概念速览

在深入之前，先建立对 OpenClaw 架构的全局认知：

| 概念 | 一句话解释 | 类比 |
|------|-----------|------|
| Gateway | 中枢服务，连接消息和 AI | 总机 |
| Session | 一次对话的上下文 | 一通电话 |
| Workspace | Agent 的工作目录 | 办公桌 |
| Skills | 可插拔的能力模块 | 技能包 |
| Cron | 定时任务 | 闹钟 |
| Heartbeat | 周期性巡检 | 定时巡逻 |
| Nodes | 手机/远程设备 | 遥控器 |
| Memory | 文件化的记忆系统 | 笔记本 |
| Subagent | 独立子代理 | 助手 |

### 1.4 第一次对话

安装完成后，通过任意消息通道发送一条消息即可。Agent 会：
1. 接收你的消息
2. 调用 AI 模型生成回复
3. 根据需要使用工具（搜索、读写文件、执行命令等）
4. 返回结果

**心智转变**：
- ❌ 旧方式："打开网页和 AI 聊天"
- ✅ 新方式："从手机飞书/Telegram 发消息，AI 在你的服务器上帮你干活"

---

## 第二部分：核心能力掌握（Day 1-3）

### 2.1 工作空间与文件体系

工作空间是 Agent 的"家"，默认位于 `~/.openclaw/workspace/`。

**核心文件**：

| 文件 | 用途 | 加载时机 |
|------|------|----------|
| `SOUL.md` | Agent 的人格、性格、行为准则 | 每次会话 |
| `AGENTS.md` | 工作规范、安全规则、操作手册 | 每次会话 |
| `USER.md` | 用户信息、偏好、习惯 | 每次会话 |
| `IDENTITY.md` | Agent 的身份信息 | 每次会话 |
| `HEARTBEAT.md` | 心跳巡检任务清单 | 心跳时 |
| `TOOLS.md` | 工具使用本地笔记 | 每次会话 |
| `MEMORY.md` | 长期记忆（精华） | 主会话 |
| `memory/YYYY-MM-DD.md` | 每日记录 | 当天+昨天 |

**关键洞察**：这些文件就是 Agent 的"大脑"。Agent 每次醒来（新会话）都是白纸，但这些文件让它保持连续性。这是 OpenClaw 与无状态聊天机器人的根本区别。

### 2.2 SOUL.md：塑造你的 Agent 人格

SOUL.md 定义 Agent 是谁。这是一个持续进化的文件：

```markdown
# SOUL.md

## 核心特质
- 直言不讳，不拍马屁
- 有自己的观点和偏好
- 先动手解决问题，再问问题
- 简洁精准，拒绝废话

## 边界
- 私密信息绝不泄露
- 对外操作（发邮件、发推）先问
- 群聊中不代用户发言

## 风格
- 专业但不冰冷
- 中文为主，技术术语保留英文
```

**帕累托提示**：SOUL.md 的 80% 价值来自 20% 的内容——重点定义"行为风格"和"安全边界"。

### 2.3 AGENTS.md：Agent 的操作手册

AGENTS.md 是 Agent 的"员工手册"，定义工作规范：

```markdown
# AGENTS.md

## 安全
- 不对外发送私有数据
- 破坏性操作前必须确认
- trash > rm（可恢复优于不可恢复）

## 工具使用
- 读取文件、搜索、组织学习：自由执行
- 发邮件、推文、公开发帖：先问

## 群聊行为
- 被提及或有价值时才回复
- 不需要的场景回复 HEARTBEAT_OK

## 心跳
- 每 30 分钟一次，按 HEARTBEAT.md 执行
- 深夜（23:00-08:00）除非紧急否则安静
```

### 2.4 Memory 系统：让 Agent 越用越聪明

OpenClaw 的记忆系统是**文件化、结构化、可持久化**的：

**三层记忆架构**：

| 层级 | 文件 | 内容 | 类比 |
|------|------|------|------|
| 身份层 | SOUL.md | 人格、价值观 | 性格 |
| 规则层 | AGENTS.md | 操作规范 | 员工手册 |
| 知识层 | MEMORY.md | 长期记忆 | 经验积累 |

**记忆维护**：
- 每日记录写入 `memory/YYYY-MM-DD.md`
- 定期（每隔几天）在心跳中回顾日志
- 将重要信息蒸馏提炼到 `MEMORY.md`
- 清理过时的日志文件

**为什么这很重要**：几周后，你的 Agent 会了解你的偏好、记住项目上下文、不重复犯错。与无状态聊天机器人的差距是指数级的。

### 2.5 Skills：Agent 的技能包系统

Skills 是 OpenClaw 的插件系统——模块化能力包。

**发现和安装**：

```bash
# 搜索可用 Skills
openclaw skill search weather

# 安装
openclaw skill install weather

# 查看已安装
openclaw skill list
```

**2026 必装 Skills（帕累托 Top 10）**：

| Skill | 功能 | 核心价值 |
|-------|------|----------|
| weather | 天气预报 | 日常必备 |
| github | GitHub 操作 | 开发者核心 |
| healthcheck | 服务器安全巡检 | 运维自动化 |
| gh-issues | Issue/PR 自动修复 | 效率倍增器 |
| skill-creator | 创建新 Skill | 元能力 |
| qqbot-cron | 定时提醒 | 任务管理 |
| tmux | 远程终端控制 | 高级运维 |
| stock-analysis | 股票分析 | 投资辅助 |
| khazix-writer | 公众号写作 | 内容创作 |
| agent-reach | 多平台接入 | 通道扩展 |

**创建自定义 Skill**：

```bash
# 用内置工具快速创建
openclaw skill create my-skill
```

每个 Skill 就是一个文件夹，核心是 `SKILL.md` 文件，描述技能的能力、使用场景和具体指令。Agent 在需要时自动加载对应 Skill。

---

## 第三部分：自动化引擎（Week 1-2）

### 3.1 Cron：精准定时任务

Cron 让 Agent 在指定时间自动执行任务，运行在**隔离会话**中。

**基本语法**：

```bash
openclaw cron add \
  --name "每日早报" \
  --cron "0 7 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --wake now \
  --announce \
  --channel telegram \
  --to "YOUR_CHAT_ID" \
  --message "搜索过去24小时的AI新闻，整理5条摘要"
```

**Cron 表达式速查**：

| 表达式 | 含义 |
|--------|------|
| `0 8 * * *` | 每天 08:00 |
| `0 9 * * 1` | 每周一 09:00 |
| `0 8 * * 1-5` | 工作日 08:00 |
| `*/30 * * * *` | 每 30 分钟 |
| `0 10 1 * *` | 每月 1 日 10:00 |
| `0 0 * * 0` | 每周日 00:00 |

**关键参数**：

| 参数 | 作用 | 建议 |
|------|------|------|
| `--session isolated` | 隔离会话，不污染主对话 | 始终开启 |
| `--announce` | 完成后通知你 | 始终开启 |
| `--best-effort-deliver` | 投递失败不影响任务状态 | 多通道时开启 |
| `--timeout-seconds N` | 超时保护 | 日报 600，周报 900，月报 1200 |
| `--model MODEL` | 指定模型 | 日常任务用便宜模型 |
| `--tz` | 时区 | 始终明确指定 |

**管理命令**：

```bash
openclaw cron list          # 查看所有任务
openclaw cron edit --id ID  # 编辑任务
openclaw cron remove --id ID  # 删除任务
```

### 3.2 Heartbeat：周期性巡检

Heartbeat 是 Gateway 每 30 分钟触发一次的巡检机制。Agent 读取 `HEARTBEAT.md` 中的任务清单，执行后回复 `HEARTBEAT_OK`（无事发生）或发送提醒。

**配置**：

```markdown
# HEARTBEAT.md
# 邮件检查（每2-4小时一次）
# 日历检查（每日1-2次）
# 天气检查（出门前）
```

**优化心跳**：

```bash
# 延长间隔到每小时
openclaw config set agents.defaults.heartbeat.every 1h

# 限制活跃时段
openclaw config set agents.defaults.heartbeat.activeHours.start 9:00
openclaw config set agents.defaults.heartbeat.activeHours.end 22:00

# 重启生效
openclaw gateway restart
```

### 3.3 Heartbeat vs Cron：何时用哪个？

| 维度 | Heartbeat | Cron |
|------|-----------|------|
| 精确时间 | 不需要 | 必须精确 |
| 会话上下文 | 共享主对话 | 隔离独立 |
| 适合任务 | 批量检查 | 定时报告 |
| 模型选择 | 当前模型 | 可指定不同模型 |
| API 成本 | 较高（加载完整历史） | 较低（独立上下文） |

**最佳实践**：将类似的周期性检查批量放入 HEARTBEAT.md，减少 Cron 数量。精确时间的报告和提醒用 Cron。

---

## 第四部分：高级能力（Week 2-4）

### 4.1 多通道接入

OpenClaw 的杀手级特性——一个 Gateway 同时服务所有消息通道：

**支持的主流通道**：
- 即时通讯：Telegram、WhatsApp、Signal、飞书、Slack、Discord、iMessage
- 企业工具：Microsoft Teams、Google Chat、钉钉、企业微信
- 开放协议：Matrix、IRC、Mattermost
- 特殊：WebChat（内置）、Twitch、Nostr

**飞书配置要点**：

```json
{
  "channels": {
    "feishu": {
      "appId": "your-app-id",
      "appSecret": "your-app-secret",
      "verificationToken": "your-token",
      "encryptKey": "your-key"
    }
  }
}
```

**多通道同时使用**：手机飞书发快捷消息，电脑 WebChat 做长会话，Agent 保持上下文一致。

### 4.2 多 Agent 路由

OpenClaw 支持多 Agent 架构——不同通道/用户路由到不同的 Agent，每个 Agent 有独立的 Workspace 和 Session。

```bash
# 创建独立 Agent
openclaw agents create my-agent --workspace /path/to/workspace

# 配置路由
openclaw agents route --channel feishu --agent my-agent
```

### 4.3 Subagents：子代理并行

主 Agent 可以生成子代理处理复杂任务，结果自动回传：

```
> /subagents spawn 研究Claude Code最新功能并写一份总结
```

子代理运行在隔离会话中，不影响主对话。适合：
- 耗时研究任务
- 并行处理多个独立任务
- 需要不同模型的任务

### 4.4 Nodes：手机/设备节点

将手机或远程设备配对为 Node，Agent 可以：
- 拍照（相机）
- 获取位置
- 发送通知
- 控制远程设备

**配对流程**：在手机上安装 OpenClaw App，扫码配对。

### 4.5 浏览器控制

内置浏览器自动化，Agent 可以：
- 导航网站
- 填写表单
- 截图对比
- 提取数据

适合与没有 API 的网站交互。

### 4.6 模型配置与多模型策略

OpenClaw 不锁定单一模型，支持灵活的多模型配置：

```bash
# 查看当前模型
openclaw config get agents.defaults.model

# 切换模型
openclaw config set agents.defaults.model claude-sonnet-4-20250514

# 会话内临时切换
/model gpt-4o
```

**多模型策略（帕累托最优）**：

| 场景 | 推荐模型 | 理由 |
|------|----------|------|
| 复杂推理/编程 | Claude Opus | 最强推理能力 |
| 日常对话/搜索 | GLM-4 / GPT-4o | 性价比最高 |
| 定时报告/摘要 | Haiku / 便宜模型 | 成本敏感 |
| 创意写作 | GPT-5 | 创意能力突出 |
| 数据分析 | Gemini Pro | 多模态优势 |

**成本控制**：
```bash
# 设置每会话额度
openclaw config set agents.defaults.maxTokensPerSession 100000

# 查看用量
/status
```

---

## 第五部分：实战案例（边学边练）

### 案例 1：每日早报系统（Day 1）

```bash
openclaw cron add \
  --name "每日早报" \
  --cron "30 7 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated --wake now --announce \
  --channel feishu \
  --to "your-open-id" \
  --message "生成今日早报：1.天气 2.日历 3.未读邮件摘要 4.AI新闻3条"
```

**学习重点**：Cron 基本用法、多 Skill 组合。

### 案例 2：GitHub 自动巡检（Day 3）

```bash
openclaw cron add \
  --name "GitHub巡检" \
  --cron "0 9 * * 1-5" \
  --tz "Asia/Shanghai" \
  --session isolated --announce \
  --channel telegram \
  --message "检查我的GitHub仓库：新Issue、未读PR、CI失败，输出摘要"
```

**学习重点**：工作日调度、Skill 调用、结果摘要。

### 案例 3：27 任务监控系统（Week 1）

这正是我们今天搭建的"天网系统"的架构——27 个 Cron 任务覆盖 AI 动态、供应链、政策法规，通过飞书投递，三步存档。

**架构**：
```
27个Cron → 隔离Session → Skill（搜索+分析）→ 飞书消息 → 本地Archive → 知识库
```

**学习重点**：大规模 Cron 管理、错峰调度、best-effort-deliver、超时保护。

### 案例 4：多 Agent 协作（Week 2）

```
主Agent（飞书对话）
  ├── 研究Agent（子代理）：搜索并整理资料
  ├── 写作Agent（子代理）：基于资料写文章
  └── 审核Agent（子代理）：审查质量
```

**学习重点**：Subagents 并行、结果合成。

---

## 第六部分：常见陷阱与避坑指南

### 6.1 新手 Top 10 错误

| # | 错误 | 正确做法 |
|---|------|----------|
| 1 | 用默认密码/API Key | 立即更换，设置支出上限 |
| 2 | 安装在主力设备 | 用独立 VPS/虚拟机 |
| 3 | 不配安全策略 | 设置 allowFrom 白名单 |
| 4 | Cron 全部扎堆同一时间 | 错峰调度（15分钟间隔） |
| 5 | 不设超时保护 | 日报 600s，周报 900s，月报 1200s |
| 6 | HEARTBEAT.md 太满 | 只放必要检查，避免 token 浪费 |
| 7 | 不写 MEMORY.md | Agent 无法跨会话记忆 |
| 8 | Cron 投递失败报 error | 开启 best-effort-deliver |
| 9 | 从不更新 | 定期 `npm update -g openclaw` |
| 10 | 不监控成本 | 用 /status 检查，设 API 额度 |

### 6.2 成本优化

| 策略 | 节省幅度 |
|------|----------|
| 定时任务用便宜模型 | 节省 60-80% |
| 心跳间隔从 30 分钟改 1 小时 | 节省 50% |
| 限制心跳活跃时段 | 节省 30-50% |
| 隔离会话避免加载完整历史 | 节省 20-40% |
| /compact 及时压缩上下文 | 节省 10-30% |

---

## 第七部分：学习路线图（8 周计划）

| 周次 | 主题 | 目标 |
|------|------|------|
| **Week 1** | 安装配置 + 首次对话 + 飞书接入 | 能通过飞书和 Agent 正常对话 |
| **Week 2** | SOUL.md + AGENTS.md + Memory | 建立规范的工作空间，Agent 有"人味" |
| **Week 3** | Skills 安装与使用 | 安装 5+ 个实用 Skill，掌握 Skill 生态 |
| **Week 4** | Cron 定时任务 | 搭建 3-5 个自动化任务 |
| **Week 5** | Heartbeat + 成本优化 | 配置心跳巡检，控制月度成本 |
| **Week 6** | 多模型策略 | 配置模型路由，不同任务用不同模型 |
| **Week 7** | Subagents + 多通道 | 子代理并行，多通道同时使用 |
| **Week 8** | 综合实战 | 端到端搭建完整的自动化工作流 |

---

## 附录

### A. 常用命令速查

| 命令 | 说明 |
|------|------|
| `openclaw onboard` | 引导式初始化 |
| `openclaw dashboard` | 打开控制面板 |
| `openclaw status` | 系统状态诊断 |
| `openclaw gateway start/stop/restart` | Gateway 控制 |
| `openclaw cron add/list/edit/remove` | 定时任务管理 |
| `openclaw config get/set` | 配置管理 |
| `openclaw skill search/install/list` | Skill 管理 |
| `/status` | 会话状态 |
| `/model MODEL` | 切换模型 |
| `/compact` | 压缩上下文 |
| `/reasoning` | 切换推理模式 |
| `/subagents spawn` | 启动子代理 |

### B. 配置文件层级

| 文件 | 位置 | 用途 |
|------|------|------|
| `openclaw.json` | `~/.openclaw/` | 主配置（模型、通道、插件） |
| `SOUL.md` | `workspace/` | Agent 人格 |
| `AGENTS.md` | `workspace/` | 工作规范 |
| `USER.md` | `workspace/` | 用户信息 |
| `MEMORY.md` | `workspace/` | 长期记忆 |
| `HEARTBEAT.md` | `workspace/` | 心跳任务清单 |
| `TOOLS.md` | `workspace/` | 工具本地笔记 |

### C. 推荐学习资源

| 资源 | 类型 | 链接 |
|------|------|------|
| 官方文档 | 权威 | docs.openclaw.ai |
| GitHub 仓库 | 源码 + Issue | github.com/openclaw/openclaw |
| 知乎 3.2W 字完全指南 | 中文深度 | zhuanlan.zhihu.com（搜索 OpenClaw） |
| SeeAI 教程 | 实用教程 | seeai.net/openclaw/how-to-use-openclaw |
| 阿里云百炼文档 | 集成指南 | help.aliyun.com（搜索 OpenClaw） |
| BBC 中文报道 | 背景了解 | bbc.com（搜索 OpenClaw） |
| OpenClaw 技能中心 | Skill 生态 | openclawnote.com |
| ClawHub | Skill 市场 | clawhub.com |

### D. 安全清单

- [ ] 设置 API Key 支出上限
- [ ] 配置消息白名单（allowFrom）
- [ ] 不在主力设备安装
- [ ] 定期检查 cron 任务状态
- [ ] 定期更新 OpenClaw 版本
- [ ] 备份 workspace 目录
- [ ] 审查已安装的 Skills 权限
- [ ] 使用 VPS 而非本地机器

---

> **本手册基于 2026 年 5 月公开资料及实际部署经验整理。OpenClaw 更新频繁，建议关注官方文档获取最新特性。**
>
> 整理方法：第一性原理（理解 Agent Runtime 本质）→ 帕累托法则（20% 功能覆盖 80% 价值）→ MECE（不重不漏分类）→ 金字塔原理（结论先行、逐层展开）
