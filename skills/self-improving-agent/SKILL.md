---
name: self-improvement
description: "Captures learnings, errors, and corrections to enable continuous improvement."
version: "1.0.11"
author: pskoett
---

# Self-Improvement Skill

Log learnings and errors to markdown files for continuous improvement.

## Quick Reference

| Situation | Action |
|-----------|--------|
| Command/operation fails | Log to `.learnings/ERRORS.md` |
| User corrects you | Log to `.learnings/LEARNINGS.md` with category `correction` |
| User wants missing feature | Log to `.learnings/FEATURE_REQUESTS.md` |
| API/external tool fails | Log to `.learnings/ERRORS.md` |
| Knowledge was outdated | Log to `.learnings/LEARNINGS.md` with category `knowledge_gap` |
| Found better approach | Log to `.learnings/LEARNINGS.md` with category `best_practice` |
| Broadly applicable learning | Promote to `MEMORY.md`, `TOOLS.md`, or `SOUL.md` |

## Log Files

Create in workspace:
```bash
mkdir -p ~/.openclaw/workspace/.learnings
```

Files:
- `LEARNINGS.md` — corrections, knowledge gaps, best practices
- `ERRORS.md` — command failures, exceptions
- `FEATURE_REQUESTS.md` — user-requested capabilities

## Format

### Learning Entry
```markdown
## [LRN-YYYYMMDD-XXX] category

**Logged**: ISO-8601 timestamp
**Priority**: low | medium | high | critical
**Status**: pending

### Summary
One-line description

### Details
Full context

### Metadata
- Source: conversation | error | user_feedback
```

### Error Entry
```markdown
## [ERR-YYYYMMDD-XXX] command_name

**Logged**: ISO-8601 timestamp
**Priority**: high
**Status**: pending

### Summary
Brief description

### Error
```
Actual error message
```

### Suggested Fix
How to resolve
```

## Promotion

When learnings are broadly applicable, promote to:
- `MEMORY.md` - long-term memory
- `TOOLS.md` - tool gotchas
- `SOUL.md` - behavioral patterns
