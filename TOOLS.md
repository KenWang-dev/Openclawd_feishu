# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

### 📋 飞书待办事项表格
- **URL**：https://procurement-leap.feishu.cn/base/NTSzbkeB5aBEtes3ZhQc5iFRnIe
- **Base Token**：NTSzbkeB5aBEtes3ZhQc5iFRnIe
- **Table ID**：tbl7bMlQsUtgz82f
- **字段**：任务名称、状态（待办/进行中/已完成/已取消）、优先级（🔴高/🟡中/🟢低）、分类（商务/技术/行政/个人/其他）、需要处理的时间、提醒时间、创建时间（自动）、备注
- **用途**：Ken 的个人待办管理，随时可通过 lark-cli 增删改查
- **创建时间**：2026-04-13
- **提醒策略**：飞书日历原生提醒
  - 每次添加待办同时创建飞书日历日程
  - 设前1天晚上20:00(1140min) + 前2小时(120min)双提醒
  - 不再额外设 cron 推送
- **添加待办 SOP**：
  1. lark-cli base +record-upsert 写入多维表格
  2. lark-cli calendar events create 创建日历日程 + 双提醒
