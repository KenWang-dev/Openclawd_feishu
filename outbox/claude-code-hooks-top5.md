# Claude Code Hooks TOP5：大幅提升效率与正确率的用法

> 总原则：**凡是"每次都要叮嘱 Claude"的事，都该变成 hook。**
>
> 配置入口：Claude Code 内输入 `/hooks` 交互式配置；改完 `settings.json` 当场生效，无需重启。

---

## 🥇 1. PostToolUse + 自动格式化 —— 消灭"改完代码风格烂"

**价值**：Claude 写的代码永远是统一风格，省掉一轮人工 review 和 lint 争吵。

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "npx prettier --write \"$CLAUDE_FILE_PATHS\" 2>/dev/null || true"
      }]
    }]
  }
}
```

**技巧**：
- 按项目类型换工具——Go 用 `gofmt -w`，Python 用 `ruff format`，前端用 prettier
- 加 `|| true` 防止格式化工具报错阻断 Claude

---

## 🥈 2. PreToolUse + 敏感文件保护 —— 正确率的最大保险

**价值**：Claude 最危险的错误就是改了不该改的文件。一次配置、永久生效的护栏。

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "echo \"$CLAUDE_FILE_PATHS\" | grep -qE '\\.env|secret|credentials|\\.pem|lock$' && echo '禁止编辑敏感/生成文件' >&2 && exit 2 || exit 0"
      }]
    }]
  }
}
```

**技巧**：
- `.env`、密钥文件、`package-lock.json` 这类生成文件都挡掉
- 改 lock 文件是 Claude 常见低级错误，拦截即可避免

---

## 🥉 3. PreToolUse + 危险命令拦截 —— 防灾难

**价值**：`rm -rf`、`git push --force`、`DROP TABLE`……一次拦截就是救一次生产环境。

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/guard-bash.py"
      }]
    }]
  }
}
```

配套脚本 `guard-bash.py`：从 stdin 读 JSON，匹配危险模式（`rm -rf /`、`--force`、`git reset --hard`、`drop database`）就 `exit 2`。

**技巧**：
- stderr 里写清楚"为什么拦"，Claude 会据此换一个安全方案，而不是卡死

---

## 4. Stop + 完成通知 —— 解放注意力

**价值**：长任务跑着你去干别的，结束时自动提醒，不空等也不漏接。

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Claude 完成了\" with title \"Claude Code\"' 2>/dev/null || notify-send 'Claude Code' '任务完成'"
      }]
    }]
  }
}
```

**技巧**：
- 进阶玩法——Stop 时自动跑一次 `lint + test`，把结果输出到 stdout 给 Claude 看，让它**自己验收自己**，正确率显著提升

---

## 5. UserPromptSubmit + 上下文注入 —— 自动带上项目约定

**价值**：每次提问自动注入关键约束，比反复在 prompt 里强调可靠得多。

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{
        "type": "command",
        "command": "cat .claude/rules.md 2>/dev/null; git branch --show-current | sed 's/^/当前分支: /'"
      }]
    }]
  }
}
```

`rules.md` 写：代码规范、禁止操作、当前迭代注意事项。stdout 会自动进入 Claude 的上下文。

**技巧**：
- 把 CLAUDE.md 里"总被忽略"的规则挪到这里——每轮强制注入，比被动记忆有效

---

## 附：事件速查表

| 事件 | 触发时机 |
|---|---|
| `PreToolUse` | 工具调用**前**（可拦截，退出码 2 阻止） |
| `PostToolUse` | 工具调用**后** |
| `UserPromptSubmit` | 用户提交 prompt 时 |
| `Notification` | Claude 发通知时 |
| `Stop` / `SubagentStop` | Claude 回答结束时 |
| `PreCompact` | 上下文压缩前 |
| `SessionStart` / `SessionEnd` | 会话开始/结束 |

## 附：控制逻辑

- **退出码 0**：放行；stdout 可作为额外上下文给 Claude
- **退出码 2**：**阻断**（PreToolUse 时）；stderr 反馈给 Claude 让它换方案
- 其他非零：非阻断错误

## 建议配置顺序

**2（敏感文件）→ 3（危险命令）先上**（保命）→ **1（格式化）**（提效）→ 按需加 4 和 5
