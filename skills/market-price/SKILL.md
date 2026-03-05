---
name: market-price
description: 电子元器件价格监控系统。用于监控电子物料（Mouser/Digi-Key/LCSC）的实时价格和库存，支持价格变动检测、缺货预警、定时任务。当用户询问元件价格、库存、监控、涨价预警时触发。
---

# Market Price - 电子元器件价格监控

## 快速开始

### 运行监控

```bash
cd /path/to/market-price/scripts
node fetch-mouser-monitor.js
```

### 目录结构

```
scripts/
├── fetch-mouser-api.js        # Mouser API 客户端
├── fetch-mouser-monitor.js    # 监控主脚本
├── data-store.js             # 数据存储
└── data/
    ├── components.json        # 监控物料列表
    └── history/               # 历史价格记录
```

### 配置

1. **API Key**：复制 `.env.example` 为 `.env`，填入你的 API Key
   ```bash
   cp scripts/.env.example scripts/.env
   # 编辑 .env 填入 MOUSER_API_KEY=你的Key
   ```
   
   ⚠️ **安全警告**：`.env` 文件包含敏感信息，**禁止提交到 Git**，已配置自动忽略

2. **监控物料**：编辑 `data/components.json`
   ```json
   {
     "part_number": "STM32F103C8T6",
     "min_stock": 10,
     "price_threshold": 0.05,
     "enabled": true
   }
   ```

3. **税率**：编辑 `fetch-mouser-api.js` 中 `taxRate`

## 价格记录格式

每次运行后自动生成汇总 CSV：`data/price-summary.csv`

| 列 | 说明 |
|---|---|
| 时间 | 查询日期 (YYYY| 物料类型-MM-DD) |
 | 芯片/模块/传感器等 |
| MPN | 制造商料号 |
| 品牌 | 制造商名称 |
| 含税单价(¥) | 含13%增值税的价格 |
| 批量 | 价格阶梯数量 |
| 库存 | 当前库存 |
| 供应商 | Mouser/立创等 |
| 备注 | 交期等信息 |

## 定时任务

每4小时运行：
```bash
0 */4 * * * cd /path/to/scripts && node fetch-mouser-monitor.js
```

## 输出示例

```
批量价格 (1500+片): ¥24.16 (不含税)
含税价格 (1500+片): ¥27.30 (含13%税)
库存: 8519
```
