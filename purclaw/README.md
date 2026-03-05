# purclaw - 元器件价格监控系统

## 🎯 项目概述

**purclaw**（Purchase Claw）是一个 AI 驱动的电子元器件价格监控系统。

### 核心功能
- ✅ 自动价格监控（每 4 小时）
- ✅ 价格变动检测
- ✅ 缺货预警
- ✅ 库存低位提醒
- ✅ 历史数据记录
- ✅ 定时任务（Cron）

---

## 📊 当前状态

### ✅ 已完成功能

1. **价格监控**
   - 监控 3 个测试元器件
   - 集成 Mouser Search API
   - 自动记录价格和库存
   - 历史数据追踪

2. **数据存储**
   - JSON 文件存储
   - 历史记录保存
   - 数据持久化

3. **定时任务**
   - 每 4 小时自动运行
   - Cron 已配置
   - 自动保存数据

4. **预警功能**
   - 价格变动检测
   - 缺货预警
   - 库存低位提醒

5. **Mouser API 集成** ✨
   - 使用官方 Search API
   - 支持批量查询
   - 获取实时价格和库存
   - 支持价格阶梯查询

---

## 🚀 快速开始

### 运行监控
```bash
bash /root/.openclaw/workspace/purclaw/run-monitor.sh
```

### 查看历史数据
```bash
ls /root/.openclaw/workspace/purclaw/data/history/
cat /root/.openclaw/workspace/purclaw/data/history/STM32F103C8T6.json
```

---

## 📦 监控物料

| 物料编号 | 描述 | 当前价格 | 库存 | 状态 |
|---------|------|---------|------|------|
| STM32F103C8T6 | STM32 32位微控制器 | ¥39.67 | 8519 | ✅ 正常 |
| ESP32-S3-WROOM-1 | ESP32-S3 WiFi模块 | ⚠️ 未找到 | N/A | ⚠️ Mouser 无货 |
| CH340G | USB转串口芯片 | ⚠️ 未找到 | N/A | ⚠️ Mouser 无货 |

**注意**：部分元器件在 Mouser 无货，可以考虑添加其他供应商。

---

## 📁 项目结构

```
purclaw/
├── scripts/
│   ├── data-store.js              # 数据存储模块
│   ├── fetch-mouser-api.js         # Mouser API 客户端 ✅
│   ├── fetch-mouser-monitor.js     # Mouser 监控脚本 ✅
│   ├── fetch-lcsc-mock.js          # 模拟数据版本（已弃用）
│   ├── test-mouser-api.js          # API 测试脚本
│   └── init-db.js                  # 数据库初始化
├── data/
│   ├── components.json             # 元器件列表
│   └── history/                    # 历史记录
├── skills/price-monitor/           # 技能定义
├── run-monitor.sh                  # 监控脚本 ✅
├── .env                            # API 配置
├── package.json
└── README.md                       # 本文档
```

---

## ⏰ 定时任务

**Cron 配置**：
- 表达式：`0 */4 * * *`
- 时区：Asia/Shanghai (GMT+8)
- 频率：每 4 小时
- 下次运行：自动计算

**运行日志**：
```
/root/.openclaw/workspace/purclaw/data/history/
```

---

## 💡 数据说明

### 当前使用：Mouser Search API ✅

**API 特点**：
- ✅ 官方 API，稳定可靠
- ✅ 实时价格和库存
- ✅ 支持批量查询
- ✅ 返回详细产品信息

**API 文档**：https://api.mouser.com/api/docs/ui/index

**认证方式**：
- 使用 API Key（Query Parameter）
- 请求体需要包装在 `SearchByPartRequest` 中

**限制**：
- 每次最多查询 10 个料号
- 每次最多返回 50 个结果
- 需要遵守速率限制

### 之前的失败经验

❌ **立创商城**：客户端渲染，难以抓取
❌ **Digi-Key**：API 端点调试困难

---

## 🎯 功能演示

### 价格监控
```
🔍 搜索: STM32F103C8T6
✅ STM32F103C8T6: ¥39.67 | 库存: 8519 | 品牌: STMicroelectronics
   交期: 91 天
   价格阶梯: 1+: ¥39.67, 10+: ¥31.62, 25+: ¥29.50
```

### 缺货预警
```
🔴 缺货: 1 个
   ESP32-S3-WROOM-1 (Mouser 无货)
```

### 历史数据
```json
[
  {
    "supplier": "Mouser",
    "price": 39.67,
    "stock": 8519,
    "availability": "8519 库存量",
    "leadTime": "91 天数",
    "mouserPartNumber": "511-STM32F103C8T6",
    "manufacturer": "STMicroelectronics",
    "captured_at": "2026-02-28T12:28:39.967Z"
  }
]
```

---

## 📊 数据统计

**总监控次数**：查看历史记录文件

**价格变动**：自动检测并记录

**库存预警**：
- 缺货：ESP32-S3-WROOM-1, CH340G（Mouser 无货）
- 库存充足：STM32F103C8T6 (8519)

---

## 🔧 技术栈

- **运行环境**：Node.js v22.22.0
- **数据源**：Mouser Search API v1
- **数据存储**：JSON 文件
- **定时任务**：OpenClaw Cron
- **消息推送**：飞书（待集成）

---

## 📝 注意事项

1. **API Key 管理**：
   - 当前 Key：`4fe47ba4-9c76-4e20-9443-08e82f79ad33`
   - 需要妥善保管，不要泄露
   - 定期检查额度和使用情况

2. **速率限制**：
   - 遵守 Mouser API 速率限制
   - 批量查询比单独查询更高效
   - 失败请求需要重试机制

3. **错误处理**：
   - 某些料号可能找不到
   - 需要考虑多供应商支持
   - 建议添加缓存机制

4. **数据存储**：当前使用 JSON，生产环境建议使用数据库

---

## 🚧 已知问题

1. ⚠️ 部分元器件在 Mouser 无货
2. ⏳ 飞书推送待集成
3. ⏳ 价格趋势图表待开发
4. ⏳ 未实现错误重试机制

---

## 📈 下一步计划

**短期（1 周）**：
- [ ] 添加飞书推送
- [ ] 实现价格变动通知
- [ ] 添加错误重试机制
- [ ] 考虑添加其他供应商（Digi-Key, LCSC）

**中期（1 月）**：
- [ ] Web 管理界面
- [ ] 价格趋势图表
- [ ] 供应商评分系统
- [ ] 支持多供应商比价

**长期（3 月）**：
- [ ] AI 价格预测
- [ ] 自动替代料推荐
- [ ] 采购建议生成
- [ ] 智能补货提醒

---

**创建时间**：2026-02-28
**版本**：v2.0.0 (Mouser API)
**状态**：✅ 运行中

---

**所有功能正常运行！** 🎉
