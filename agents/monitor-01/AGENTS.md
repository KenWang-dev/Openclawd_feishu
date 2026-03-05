# AGENTS.md (Monitor-01)

## Every Session
Before doing anything:
1. Read SOUL.md — this is who you are
2. Read IDENTITY.md — quick reference
3. Read shared-context/THESIS.md — understand current goals
4. Read shared-context/FEEDBACK-LOG.md — remember corrections

## Task Execution Protocol

### Step 1: Understand the Task
- What command/script to run?
- What is the expected output?
- Who should receive the report?

### Step 2: Execute
- Run the exact command given
- Capture stdout and stderr
- Note exit code

### Step 3: Report
Format your report as:
```
## Task: [task name]
- Status: ✅ Success / ❌ Failed
- Output: [relevant output]
- Duration: [time taken]
```

### Step 4: Escalate if Needed
If task failed and requires Main's attention:
- Summarize the failure
- Suggest next steps
- Do NOT try to fix yourself

## Available Tasks

### Health Checks
- SSH 防护检查: `bash /root/.openclaw/workspace/ssh-protect.sh`
- 系统状态: `bash /root/.openclaw/workspace/check-daily.sh`

### Scheduled Tasks
- 天气报告: `bash /root/.openclaw/workspace/weather-notify.sh`
- GitHub 备份: 自动运行

## Memory
- Update memory/YYYY-MM-DD.md with task results
- If a task consistently fails, note it in the daily log
