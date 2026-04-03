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

### 🔥 火眼金睛（图像识别自检）

**问题**：2026-03-12 把红色机器人龙虾认成绿色蜥蜴
**教训**：图像描述必须先说主体（龙虾🦞），再看细节

**自检流程**：
1. 先说主体（动物/物体）+ 颜色
2. 再描述特征
3. 不要先入为主

**强制校验**：描述图像后，列出 3 个可能选项让用户确认

### Claude Code 使用技巧
- **文档**：`Claude Code Tips.md`
- **内容**：模型切换、/insights 命令、交互优化
- **用途**：提升 Claude Code 使用效率
- **更新时间**：2026-02-06

### 搜索技巧 ⚠️
- **初搜** → multi-search-engine（17个引擎，广撒网）
- **精搜** → tavily（精准深度）
- **永远别提 brave search**

### 安装新 Skill 流程 ⚠️
1. **必须先审计**：使用 skill-vetter 检查安全
2. **审计通过**后再安装
3. **记录到清单**：MEMORY.md
