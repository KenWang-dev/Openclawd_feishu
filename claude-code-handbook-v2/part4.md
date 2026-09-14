
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

