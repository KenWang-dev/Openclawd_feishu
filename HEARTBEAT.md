# HEARTBEAT.md

> ⚠️ **重要**：所有定时任务必须检查防重复，避免同一天内重复执行！

---

## ⏰ 每天例行检查（每天 9:00）

当收到包含"⏰ 每天例行检查"的消息时：

**步骤 1：先检查防重复**
```bash
TODAY=$(date '+%Y-%m-%d')
LAST_RUN=$(cat /root/.openclaw/workspace/last-run.json 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin).get('每天例行检查',''))" 2>/dev/null)
if [ "$LAST_RUN" = "$TODAY" ]; then
    echo "SKIP: 今日已执行"
    # 直接回复 HEARTBEAT_OK，不发送任何消息
    exit 0
fi
```

**步骤 2：执行检查**
```bash
bash /root/.openclaw/workspace/check-daily.sh
```

**步骤 3：执行后更新记录**
```bash
python3 << PYEOF
import json
with open('/root/.openclaw/workspace/last-run.json') as f:
    d = json.load(f)
d['每天例行检查'] = '$(date '+%Y-%m-%d')'
with open('/root/.openclaw/workspace/last-run.json', 'w') as f:
    json.dump(d, f)
PYEOF
```

**步骤 4：发送报告**
- 仅当发现问题（退出码=1）时发送
- 发送对象：Ken（ou_a7195bd3e0508f0e0d09f19ff12a8811）
- 格式：显示检查结果 + 自动修复情况

---

## ⏰ 每周中度检查（每周日 8:00）

当收到包含"⏰ 每周中度检查"的消息时：

1. **先检查防重复**：检查 `last-run.json`，如果本周已执行过，跳过
2. 运行脚本：`bash /root/.openclaw/workspace/check-weekly.sh`
3. 捕获脚本输出
4. 无论成功与否，都通过飞书发送报告给 Ken
5. **执行后更新记录**

---

## ⏰ 每月大度检查（每月1日 8:00）

当收到包含"⏰ 每月大度检查"的消息时：

1. **先检查防重复**：检查 `last-run.json`，如果本月已执行过，跳过
2. 运行脚本：`bash /root/.openclaw/workspace/check-monthly.sh`
3. 捕获脚本输出
4. 无论成功与否，都通过飞书发送详细报告给 Ken
5. **执行后更新记录**

---

## ⏰ 天气报告（每天 7:35）

当收到包含"⏰ 天气报告"或"天气提醒任务"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/weather-notify.sh`
2. 捕获脚本输出
3. 解析天气数据，写入飞书知识库首页（doc_token: FA9Ld20Xvoz6bix7vj1cKOvGnud）
4. 使用 feishu_doc append 追加内容

格式：
```
### YYYY年M月D日
- 当前：🌤️ 雾，3°C | 湿度：100% | 风力：≤3级（南）
- 白天：晴，19°C | 晚上：3°C
- 穿衣：厚外套、毛衣、长裤
```

---

## 📋 每日备份通知（每天 9:00）

当收到包含"📋 每日备份通知"或"备份完成通知"的消息时：

1. **先检查防重复**
2. 检查 GitHub 最新提交时间
3. 通过飞书发送美化的备份通知给 Ken

---

## ⏰ SSH 防护检查（每 5 分钟）

当收到包含"⏰ SSH 防护检查"的消息时：

1. 运行脚本：`bash /root/.openclaw/workspace/ssh-protect.sh`
2. 如果有新封禁的 IP，记录到日志

---

# 其他时间

如果没有收到上述特定消息，回复：HEARTBEAT_OK

---

## 📋 待办清单检查（每天 1 次）

在没有特定任务时，可选择性检查待办清单：

1. 读取 `pending-tasks.md`
2. 检查是否有待处理事项
3. 如有重要待办，可提醒 Ken

---

## ⏰ OpenClaw 动态监控（每天 8:00）

当收到包含"⏰ OpenClaw 动态监控"的消息时：

**步骤 1：先检查防重复**
```bash
TODAY=$(date '+%Y-%m-%d')
LAST_RUN=$(cat /root/.openclaw/workspace/last-run.json 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin).get('OpenClaw动态监控',''))" 2>/dev/null)
if [ "$LAST_RUN" = "$TODAY" ]; then
    echo "SKIP: 今日已执行"
    exit 0
fi
```

**步骤 2：执行监控**
```bash
bash /root/.openclaw/workspace/openclaw-monitor.sh
```

**步骤 3：判断是否有重大更新**
- 退出码=1：检测到重大更新，需要发送报告
- 退出码=0：无重大更新，不发送

**步骤 4：发送报告（仅当有重大更新时）**
使用 `research` skill 或直接搜索收集以下信息：
1. GitHub 最新 release / commits
2. Twitter @openclaw 最新推文
3. Reddit r/openclaw 热门讨论
4. Hacker News OpenClaw 相关讨论

**步骤 5：发送格式**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🦞 OpenClaw 动态监控 - YYYY-MM-DD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 官方动态
• [版本] xxx
• [功能] xxx

💬 社区热点
• xxx

🔧 技术更新
• xxx

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
无重大更新
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**步骤 6：执行后更新记录**
```bash
python3 << PYEOF
import json
with open('/root/.openclaw/workspace/last-run.json') as f:
    d = json.load(f)
d['OpenClaw动态监控'] = '$(date '+%Y-%m-%d')'
with open('/root/.openclaw/workspace/last-run.json', 'w') as f:
    json.dump(d, f)
PYEOF
```

**推送对象**：Ken（ou_d81ad689104f8c660a5834c10740aea8）
