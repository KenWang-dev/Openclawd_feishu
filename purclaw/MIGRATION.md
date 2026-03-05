# purclaw 移植指南

## 📦 项目简介

**purclaw**（Purchase Claw）是一个基于 Node.js 的电子元器件价格监控系统，集成 Mouser Search API，实时监控元器件价格和库存。

**主要功能**：
- ✅ 自动价格监控（每 4 小时）
- ✅ 批量价格查询（取最高阶梯批量价）
- ✅ 含税价格计算（13% 税率）
- ✅ 价格变动检测
- ✅ 缺货预警
- ✅ 历史数据记录

**技术栈**：
- Node.js v18+
- JavaScript（ES6+）
- Mouser Search API v1
- JSON 文件存储

---

## 🚀 快速开始

### 方法 1：一键安装（推荐）

```bash
# 1. 进入 purclaw 目录
cd /path/to/purclaw

# 2. 运行安装脚本
bash install.sh
```

安装脚本会自动：
- 检测并安装 Node.js（如果需要）
- 检查必需文件
- 创建数据目录
- 运行测试验证

### 方法 2：手动安装

#### 1. 检查环境

```bash
# 检查 Node.js 版本
node --version  # 需要 >= 18

# 如果未安装，请先安装 Node.js
# Ubuntu/Debian:
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# CentOS/RHEL:
curl -fsSL https://rpm.nodesource.com/setup_22.x | sudo bash -
sudo yum install -y nodejs
```

#### 2. 配置 API Key

编辑 `scripts/fetch-mouser-api.js`，替换 API Key：

```javascript
const API_KEY = '你的_Mouser_API_Key';
```

获取 API Key：https://api.mouser.com/api/docs/ui/index

#### 3. 创建数据目录

```bash
mkdir -p data/history
```

#### 4. 测试运行

```bash
node scripts/fetch-mouser-monitor.js
```

---

## 📁 目录结构

```
purclaw/
├── scripts/
│   ├── fetch-mouser-api.js         # Mouser API 客户端
│   ├── fetch-mouser-monitor.js     # 监控主逻辑
│   └── data-store.js              # 数据存储模块
├── data/
│   ├── components.json             # 监控物料列表
│   └── history/                    # 历史价格记录
│       ├── STM32F103C8T6.json
│       ├── ESP32-S3-WROOM-1.json
│       └── CH340G.json
├── run-monitor.sh                  # 启动脚本
├── install.sh                      # 一键安装脚本
├── MIGRATION.md                    # 本文档
└── README.md                       # 项目说明
```

---

## ⚙️ 配置说明

### 1. 监控物料列表

编辑 `data/components.json`：

```json
[
  {
    "id": 1,
    "part_number": "STM32F103C8T6",
    "description": "STM32 32位微控制器",
    "category": "芯片",
    "min_stock": 10,
    "price_threshold": 0.05,
    "enabled": true
  }
]
```

**字段说明**：
- `part_number`: 制造商料号（如 STM32F103C8T6）
- `min_stock`: 最小库存量（低于此值触发警告）
- `price_threshold`: 价格变动阈值（如 0.05 = 5%）
- `enabled`: 是否启用监控

### 2. API Key 配置

在 `scripts/fetch-mouser-api.js` 中：

```javascript
const API_KEY = 'your-mouser-api-key-here';
```

### 3. 税率配置

在 `scripts/fetch-mouser-api.js` 中：

```javascript
let taxRate = 0.13; // 默认 13% 税率
```

---

## 🎯 使用方法

### 手动运行

```bash
# 方式 1：直接运行监控脚本
cd /path/to/purclaw
node scripts/fetch-mouser-monitor.js

# 方式 2：使用启动脚本
bash run-monitor.sh
```

### 配置定时任务

#### 使用 crontab（Linux）

```bash
# 编辑 crontab
crontab -e

# 添加以下行（每 4 小时运行一次）
0 */4 * * * cd /path/to/purclaw && node scripts/fetch-mouser-monitor.js >> /var/log/purclaw.log 2>&1
```

#### 使用 systemd（可选）

创建服务文件 `/etc/systemd/system/purclaw.service`：

```ini
[Unit]
Description=Purclaw Price Monitor
After=network.target

[Service]
Type=oneshot
WorkingDirectory=/path/to/purclaw
ExecStart=/usr/bin/node /path/to/purclaw/scripts/fetch-mouser-monitor.js
User=your-username

[Install]
WantedBy=multi-user.target
```

然后创建定时器 `/etc/systemd/system/purclaw.timer`：

```ini
[Unit]
Description=Purclaw Price Monitor Timer
Requires=purclaw.service

[Timer]
OnBootSec=5min
OnUnitActiveSec=4h
Unit=purclaw.service

[Install]
WantedBy=timers.target
```

启用服务：
```bash
sudo systemctl enable purclaw.timer
sudo systemctl start purclaw.timer
```

---

## 📊 数据说明

### 价格策略

- **基础价格**：不含税
- **含税价格**：基础价格 × 1.13（13% 税率）
- **批量价格**：取最高阶梯价格（最大批量优惠）
- **历史记录**：保存含税价格

### 数据格式

历史记录示例（`data/history/STM32F103C8T6.json`）：

```json
[
  {
    "supplier": "Mouser",
    "price": 27.30,
    "priceBase": 24.16,
    "priceBreakQuantity": 1500,
    "taxRate": 0.13,
    "stock": 8519,
    "availability": "8519 库存量",
    "leadTime": "91 天数",
    "mouserPartNumber": "511-STM32F103C8T6",
    "manufacturer": "STMicroelectronics",
    "description": "ARM微控制器 - MCU 32BIT Cortex M3 64KB 20KB RAM 2X12 ADC",
    "captured_at": "2026-02-28T12:37:56.123Z"
  }
]
```

---

## 🔧 常见问题

### 1. API 请求失败

**错误**：`❌ Mouser API 查询失败`

**解决方案**：
- 检查 API Key 是否正确
- 检查网络连接
- 确认 API Key 未过期
- 检查是否超出速率限制

### 2. 某些料号找不到

**原因**：Mouser 可能没有该料号

**解决方案**：
- 检查料号是否正确
- 尝试使用制造商料号
- 考虑添加其他供应商

### 3. 价格不准确

**原因**：API 返回的是基础价格

**说明**：
- API 返回：基础价格（不含税）
- 实际采购：含税价格（基础价格 × 1.13）
- 当前使用：批量价格（最高阶梯）

### 4. 定时任务不执行

**检查**：
```bash
# 查看 cron 日志
grep CRON /var/log/syslog

# 测试脚本
cd /path/to/purclaw
node scripts/fetch-mouser-monitor.js
```

---

## 📈 进阶功能

### 添加其他供应商

复制 `fetch-mouser-api.js`，修改为其他供应商的 API：

```javascript
// 示例：Digi-Key API
function searchDigiKey(partNumber) {
  // 实现 Digi-Key API 调用
}
```

### 飞书通知

在监控脚本中添加飞书通知：

```javascript
// 发送飞书消息
function sendFeishuNotification(message) {
  // 使用 OpenClaw 的 message 工具
  // 或调用飞书 Webhook
}
```

### 数据库存储

当前使用 JSON 文件，可升级为数据库：

```javascript
// 使用 SQLite
const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('purclaw.db');
```

---

## 🔐 安全建议

1. **API Key 管理**
   - 不要提交到 Git
   - 使用环境变量
   - 定期更换

2. **数据备份**
   ```bash
   # 定期备份历史数据
   tar -czf purclaw-backup-$(date +%Y%m%d).tar.gz data/history/
   ```

3. **日志管理**
   ```bash
   # 定期清理日志
   find /var/log/purclaw.log -mtime +30 -delete
   ```

---

## 📞 支持

**Mouser API 文档**：
- API 文档：https://api.mouser.com/api/docs/ui/index
- 获取 API Key：https://www.mouser.com/api-search/api-key

**项目相关**：
- GitHub：https://github.com/KenWang-dev/Openclawd_feishu
- 问题反馈：创建 Issue

---

## 📝 更新日志

### v2.0.0 (2026-02-28)
- ✅ 集成 Mouser Search API
- ✅ 支持批量价格查询（最高阶梯）
- ✅ 含税价格计算（13% 税率）
- ✅ 价格变动检测
- ✅ 历史数据记录

### v1.0.0
- 初始版本（模拟数据）

---

**创建时间**：2026-02-28
**版本**：v2.0.0
**状态**：✅ 生产就绪
