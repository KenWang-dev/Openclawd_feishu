# HEARTBEAT.md

## 2026-10-25 修复记录
- [x] SSH 自动防护 cron 连续 2 次 error——根因：任务要求"通过飞书发送"，违反 Ken 的投递规则（只走会话）。已改为纯报告输出 + 手动触发验证通过

## 2026-10-16 运维
- [x] 磁盘清理 ✅ 68%→60%（日志+npm缓存），10/16 完成
- [ ] Brave Search API key 续费/重申请（403 订阅停用，需 Ken 操作）

- [x] Tavily — ✅ 10/2 修复：simple-search.mjs 改用 key-pool + Bearer 头，忽略旧 TAVILY_API_KEY_* 环境变量（旧 env key 已轮换是 401 根因）；7 把 pool key 实测全部 200
  - ⚠️ 10/7：α1/B1 cron 报「Tavily 脚本缺失」——脚本实际存在且可用（本机实测 200），cron agent 请用**绝对路径**调用：`node /root/.openclaw/workspace/skills/tavily-search/scripts/simple-search.mjs "query"`

## 2026-09-10 Claude Code GLM 1210 修复跟踪
- [x] ✅ **已解决（9/30 确认）**：官方在 [v2.1.268](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) 修复 —— "Fixed every turn failing with HTTP 400 on third-party Anthropic-compatible endpoints since 2.1.265: a regex in the Artifact tool's input schema that those endpoints reject"
- 行动：Windows 机器 `npm install -g @anthropic-ai/claude-code@latest`（最新 v2.1.285），2.1.263 可退役；restore-claude.bat 清理旧环境变量
- 参考：cc-switch issue #7236 已关闭（completed）

## 2026-08-25 财报跟踪
- [x] **美的集团（000333）**2026年半年报 — ✅ 8/28已披露，已通知Ken
- [x] **龙旗科技（603341）**2026年半年报 — ✅ 8/28已披露，已通知Ken
- [x] 华勤技术（603296）2026半年报 — ✅ 已披露（约8/26），已通知Ken：营收~940亿(+~40%)，归母净利~30亿(+59%)
