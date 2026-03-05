#!/bin/bash
# purclaw - 元器件价格监控系统（Mouser API 版本）

echo "========================================"
echo "📊 purclaw 价格监控"
echo "⏰ $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================"
echo ""

# 运行监控脚本（Mouser API）
node /root/.openclaw/workspace/purclaw/scripts/fetch-mouser-monitor.js

echo ""
echo "✅ 监控完成"
echo ""
echo "📁 数据保存位置:"
echo "   /root/.openclaw/workspace/purclaw/data/"
echo ""
echo "📋 历史记录:"
ls -lh /root/.openclaw/workspace/purclaw/data/history/ | tail -5
