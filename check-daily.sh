#!/bin/bash
# 每天例行健康检查脚本
# 用途：检查系统健康状况，供 OpenClaw cron 调用

echo "=== 系统信息 ==="
hostname
uptime
echo ""

echo "=== 磁盘使用 ==="
df -h / /home 2>/dev/null
echo ""

echo "=== 内存使用 ==="
free -h
echo ""

echo "=== CPU负载 ==="
nproc
cat /proc/loadavg
echo ""

echo "=== OpenClaw 网关状态 ==="
openclaw gateway status 2>&1 | head -15
echo ""

echo "=== 系统更新检查 ==="
(yum check-update --quiet 2>/dev/null | tail -5 || apt list --upgradable 2>/dev/null | tail -5 || echo "无包管理器或无更新")
