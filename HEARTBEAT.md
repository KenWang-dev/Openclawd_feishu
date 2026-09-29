# HEARTBEAT.md

## 2026-09-10 Claude Code GLM 1210 修复跟踪
- [ ] 监控 Claude Code 接入 GLM 报 400 [1210] 的修复情况（cc-switch issue #7236 + 新版本 release notes）
- 背景：2.1.265 引入回归（Artifact schema 的 Unicode \p{...} pattern），对应 anthropics/claude-code #92964/#93029，至 9/29 仍 open；最新版本 2.1.284 未确认修复，继续观望
- cc-switch 侧：farion1231/cc-switch #6890（body override 无删除语义导致 GLM 1210）9/19 提出仍 open，无官方修复
- ✅ 当前方案：Ken 已降级至 2.1.263（9/10 验证 GLM 正常，Windows 机器），等官方修复后升回最新
- 升级命令备用：`npm install -g @anthropic-ai/claude-code@latest`（restore-claude.bat 可删除之前设置的环境变量）
- 搜索词参考：`Claude Code GLM 1210 修复`、`cc-switch issue 7236`、`claude-code releases`

## 2026-08-25 财报跟踪
- [x] **美的集团（000333）**2026年半年报 — ✅ 8/28已披露，已通知Ken
- [x] **龙旗科技（603341）**2026年半年报 — ✅ 8/28已披露，已通知Ken
- [x] 华勤技术（603296）2026半年报 — ✅ 已披露（约8/26），已通知Ken：营收~940亿(+~40%)，归母净利~30亿(+59%)
