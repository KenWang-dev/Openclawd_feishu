# daily-diary

每日日记技能。根据当天对话记录生成工作日志，发送到飞书。

## 触发条件

- 用户要求写日记
- 定时任务触发（每天 20:00 北京时间）

## 执行步骤

### 1. 获取对话历史（方案A为主，方案B为辅）

**方案A（主）**：通过 sessions_history 获取 main 会话当天对话
```bash
# 获取最近 50 条对话记录
sessions_history --sessionKey main --limit 50
```

**方案B（辅）**：从 memory 目录读取当天文件作为补充参考
```bash
# 仅当方案A无法获取足够信息时使用
MEMORY_FILE="$WORKSPACE/memory/$(date '+%Y-%m-%d').md"
```

### 2. 生成日记格式

```
# YYYY-MM-DD 工作日志

**星期X** | 北京时间 HH:mm

---

## 📋 今日对话记录
（精简记录，3-5条关键对话）

## 💡 认知迭代
（1-3条今日学到的教训或认知更新）

## 🗓️ 明日待办
- [ ] 待办1
- [ ] 待办2
```

### 3. 发送飞书

- 使用 message 工具
- target: `ou_d81ad689104f8c660a5834c10740aea8`（Ken）
- 文件保存到 `/root/.openclaw/workspace/memory/YYYY-MM-DD.md`

---

**更新时间**：2026-03-24
