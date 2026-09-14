---
name: skill-usage-tracker
description: "Track and analyze skill usage frequency from conversation history. Use when you want to understand which skills are being used most/least, generate optimization recommendations, or audit your skill ecosystem. Triggered by phrases like 'skill usage', '哪些技能用得最多', '技能使用统计', '分析技能使用情况'."
triggers:
  - "skill usage"
  - "哪些技能用得最多"
  - "技能使用统计"
  - "分析技能使用情况"
  - "skill frequency"
  - "unused skills"
---

# Skill Usage Tracker

Analyze which skills/tools are being used in your conversations and generate optimization recommendations.

## Quick Reference

| Command | Description |
|---------|-------------|
| `bash skills/skill-usage-tracker/analyze.sh` | Run full analysis |

## How It Works

1. **Parse session history** - Extract tool/skill invocations from recent sessions
2. **Calculate frequency** - Daily, weekly, monthly usage counts
3. **Generate report** - Visual breakdown with recommendations

## Output Format

```markdown
# 📊 Skill Usage Report

## Usage Statistics
| Skill | Today | This Week | This Month | Trend |
|-------|-------|-----------|------------|-------|
| xxx   | 5     | 20        | 85         | 📈   |

## Recommendations
- 🟢 **Keep**: High frequency skills
- 🟡 **Review**: Medium frequency skills
- 🔴 **Remove**: Unused skills (>30 days)
```

## Manual Tracking

You can also manually log skill usage by adding entries:

```bash
echo "$(date '+%Y-%m-%d %H:%M:%S') - skill-name" >> skills/skill-usage-tracker/usage.log
```
