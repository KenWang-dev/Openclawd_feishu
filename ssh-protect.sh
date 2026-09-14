#!/bin/bash

# SSH Protection Script
# Checks for failed login attempts and blocks suspicious IPs

LOG_FILE="/var/log/secure"
BLOCKED_IPS_FILE="/root/.openclaw/workspace/blocked_ips.log"
ALERT_LOG="/root/.openclaw/workspace/ssh-alerts.log"
THRESHOLD=5  # Block IPs after 5 failed attempts
CURRENT_TIME=$(date '+%Y-%m-%d %H:%M:%S')

# Create necessary directories and files
mkdir -p /root/.openclaw/workspace
touch "$BLOCKED_IPS_FILE"
touch "$ALERT_LOG"

echo "=== SSH Protection Scan - $CURRENT_TIME ===" >> "$ALERT_LOG"

# Extract IPs with failed login attempts
FAILED_LOGINS=$(grep "Failed password\|Invalid user" "$LOG_FILE" 2>/dev/null | tail -1000)

if [ -z "$FAILED_LOGINS" ]; then
    echo "No failed login attempts found in recent logs." >> "$ALERT_LOG"
    echo "No new blocked IPs."
    exit 0
fi

# Analyze failed login attempts
echo "Analyzing failed login attempts..." >> "$ALERT_LOG"

# Extract IPs and count failed attempts
IP_ATTEMPTS=$(echo "$FAILED_LOGINS" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort | uniq -c | sort -nr)

# Check each IP for suspicious activity
echo "$IP_ATTEMPTS" | while read count ip; do
    if [ "$count" -ge "$THRESHOLD" ]; then
        # Check if IP is already blocked
        if ! grep -q "$ip" "$BLOCKED_IPS_FILE"; then
            echo "NEW IP BLOCKED: $ip ($count failed attempts)"
            echo "[$CURRENT_TIME] BLOCKED: $ip (Failed attempts: $count)" >> "$BLOCKED_IPS_FILE"
            echo "[$CURRENT_TIME] NEW BLOCKED IP: $ip with $count failed attempts" >> "$ALERT_LOG"
            
            # Send Feishu alert
            feishu_message="🚨 SSH安全警告\n\n检测到新的恶意IP攻击：\n\n• IP地址: $ip\n• 失败尝试次数: $count\n• 攻击时间: $CURRENT_TIME\n\n建议立即检查服务器安全状态并考虑永久封禁此IP。"
            
            echo "Sending Feishu alert for IP: $ip" >> "$ALERT_LOG"
            echo "$feishu_message"
        else
            echo "Already blocked: $ip"
            echo "[$CURRENT_TIME] Already blocked: $ip" >> "$ALERT_LOG"
        fi
    else
        echo "IP $ip has $count attempts (below threshold $THRESHOLD)"
    fi
done

echo "SSH protection scan completed." >> "$ALERT_LOG"
echo "" >> "$ALERT_LOG"

# Summary report
BLOCKED_COUNT=$(grep -c "BLOCKED:" "$BLOCKED_IPS_FILE" 2>/dev/null || echo "0")
echo "Total blocked IPs to date: $BLOCKED_COUNT" >> "$ALERT_LOG"

echo "Scan completed. Check $ALERT_LOG for details."