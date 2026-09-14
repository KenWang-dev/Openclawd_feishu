# 🦊 Claude Code 动态监控 - 2026年5月21日

## 📦 版本更新

### v2.1.145 (2026-05-19)

**事实：**
- `claude agents --json` 支持输出 JSON 格式的活跃会话列表，便于脚本集成
- OTEL span 增加 `agent_id` 和 `parent_agent_id`，后台子 agent span 正确嵌套
- `/plugin` 安装前可预览插件的 commands、agents、skills、hooks、MCP/LSP servers
- 修复了权限绕过漏洞：Bash 中对非白名单环境变量的裸赋值不再自动批准
- Read tool 超出 token 限制时返回截断的首页 + "PARTIAL view" 提示，而非硬报错
- 修复 `context: fork` 的 skill 无限递归调用自身的问题

**是什么：**
- 让 `claude agents` 从交互工具变成可编程接口，方便 tmux-resurrect、状态栏、会话选择器等集成
- 安全修复很重要 — 之前可以通过环境变量赋值绕过权限提示
- PARTIAL view 让大文件读取不再直接报错中断工作流

**洞察：**
- 如果你在用 `claude agents` 做自动化，`--json` 输出是很有用的改进
- 权限绕过修复提醒我们及时更新，这个版本应该尽快升级
- Read 的 PARTIAL view 对处理大文件场景（如日志分析）有实际帮助

---

### v2.1.144 (2026-05-19)

**事实：**
- `/resume` 现在支持后台会话（`claude --bg`）
- `/model` 改为仅影响当前会话，按 `d` 可设置新会话默认模型
- 修复启动时 `api.anthropic.com` 不可达导致挂起 75s 的问题，侧通道超时改为 15s
- 修复 MCP `tools/list` 分页响应只返回第一页的问题（静默丢失工具）
- 修复 MCP 图片 MIME 类型不支持时（如 SVG）中断会话的问题
- 修复 Bedrock/Vertex 用户无法选择 "Opus (1M context)" 的回退问题
- 大量 Windows 和后台会话相关的稳定性修复

**是什么：**
- 后台会话体验大幅改善 — resume、model 保持、detach/preserve 设置等
- API 不可达时不再卡死 75 秒，对网络不稳定环境很关键
- MCP 工具丢失是严重 bug，之前可能导致 MCP 工具莫名消失

**洞察：**
- 如果你在用 MCP + Bedrock/Vertex，这个版本是必升级的
- 后台会话的完善说明 Claude Code 在向 "agent OS" 方向演进
- 启动超时修复对中国用户特别有用（网络环境经常不稳定）

---

### v2.1.143 (2026-05-15)

**事实：**
- 插件依赖强制执行：禁用被依赖的插件会提示依赖链
- 新增 `worktree.bgIsolation: "none"` 设置，允许后台会话直接编辑工作副本
- PowerShell 工具默认启用（Windows）
- 修复 macOS 后台会话在 Full Disk Access 保护目录下崩溃的问题
- 修复 stop hook 无限循环的问题（8 次连续 block 后强制结束）

**是什么：**
- 插件依赖管理让多插件协作更安全
- `worktree.bgIsolation: "none"` 对不使用 git worktree 的项目很实用
- stop hook 防循环是重要的稳定性改进

**洞察：**
- 插件生态越来越成熟，依赖管理是必经之路
- 如果你用了很多插件，注意检查依赖关系

---

## 📊 总体趋势

1. **Agent 化加速**：`claude agents --json`、后台会话 resume、OTEL span 嵌套 — Claude Code 正在变成一个 agent 编排平台
2. **安全意识增强**：连续修复权限绕过漏洞，对环境变量操作更严格
3. **Windows 体验大幅改善**：大量 Windows 相关 bug 修复
4. **MCP 生态成熟度提升**：分页、图片、工具列表等问题逐步修复
5. **后台会话成为一等公民**：resume、model 保持、detach/preserve — 后台工作流基本可用

---

*注：Brave Search API 配额已耗尽，社区热点和竞品动态部分基于 GitHub 数据分析。*
*数据来源：GitHub Releases API*
*监控时间：2026-05-21 09:30 GMT+8*
