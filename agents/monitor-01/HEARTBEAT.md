# HEARTBEAT.md (Monitor-01)

## Self-Health Check

Run on each heartbeat to verify Monitor is functioning:

### 1. Can Read Files?
- Test: Read a small file from workspace
- If fail: Report "Cannot access workspace"

### 2. Can Execute Scripts?
- Test: Run `echo "test" | head -1`
- If fail: Report "Cannot execute commands"

### 3. Can Spawn Sub-Agents?
- Test: List current subagents
- If fail: Report "Cannot spawn sub-agents"

## Standard Health Checks

When Main requests a health check, run these:

| Check | Command | Alert Threshold |
|-------|---------|-----------------|
| SSH 防护 | `bash /root/.openclaw/workspace/ssh-protect.sh` | Any new ban |
| 系统状态 | `bash /root/.openclaw/workspace/check-daily.sh` | Exit code ≠ 0 |
| 定时任务 | Check cron status | Any stale job |

## Reporting Format

### Normal (All Good)
```
✅ Monitor-01 健康检查通过
- 文件访问: ✅
- 命令执行: ✅
- 子Agent: ✅
```

### Issue Found
```
⚠️ Monitor-01 发现问题
- 问题: [description]
- 详情: [output]
- 建议: [what Main should do]
```

## Escalation Rules（上报规则）

**立即上报 Main（小辉）的情况**：
1. 任务执行失败且无法确定原因
2. 连续失败2次以上
3. 基础设施问题（磁盘满、服务宕机）
4. 安全问题（异常访问尝试）
5. **任何不确定的情况**
