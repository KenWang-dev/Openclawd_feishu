---
name: skill-registry
description: "Skill 注册表管理器。自动扫描所有已安装 skill，生成 INDEX.md 索引文件，并在 git commit/pull 时自动触发更新。触发：注册 skill、更新索引、扫描技能、skill 索引、skill registry、管理技能清单。"
---

# Skill Registry

## 核心功能

自动扫描 `skills/` 目录下所有 SKILL.md，提取 name、description、路径，生成结构化索引。

## 工作流程

### 1. 手动触发
```bash
bash ~/.openclaw/workspace/skills/skill-registry/register.sh
```

### 2. 自动触发（git hooks）
- **pre-commit**：每次 commit 自动更新索引
- **post-merge**：每次 pull 自动更新索引
- **cron 兜底**：每天自动检查一次

### 3. AI 启动加载
AI 启动时读取 `skills/INDEX.md`，获得所有可用 skill 的名称、路径和触发场景。

## 索引格式

索引输出到 `skills/INDEX.md`，按体系分类：

```markdown
# Skills Index
> 自动生成，勿手动编辑。运行 `bash skills/skill-registry/register.sh` 更新。

## 体系名称
| Skill | 路径 | 触发场景 |
|-------|------|----------|
| name | relative/path/SKILL.md | description 前50字 |
```

## 安装 Git Hooks

```bash
bash ~/.openclaw/workspace/skills/skill-registry/install-hooks.sh
```

## 注意事项

- INDEX.md 由脚本自动生成，**不要手动编辑**
- 新增/删除 skill 后，commit 时会自动更新
- 如果手动修改了 skill 的 SKILL.md，运行 register.sh 即可同步
- 索引包含相对路径，AI 读取时拼上 `~/.openclaw/workspace/` 前缀

---

*Skill Registry v1.0 — 让每个 skill 都被看见*
