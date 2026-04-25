---
name: stock-deep-analysis
description: A股深度分析工具。基于AKShare，支持实时行情、K线、技术指标（MA/RSI/MACD）、资金流向、基本面查询。当用户要求分析A股个股、查看技术面、资金面时使用。
---

# A股深度分析 Skill

基于 AKShare 开源库的 A 股深度分析工具，覆盖技术面、资金面、基本面。

## 触发场景

- "分析一下 600519"
- "茅台技术面怎么样"
- "看看比亚迪的资金流向"
- "600519 RSI/MACD 是多少"
- "给我出一份个股分析报告"

## 核心命令

### 完整分析报告
```bash
cd /root/.openclaw/workspace/skills/stock-deep-analysis
python3 scripts/stock_analysis.py <股票代码>
```
输出：实时行情 + 30日K线 + 资金流向 + 技术指标（MA/RSI/MACD）

### 单项查看

```bash
# 仅看实时行情
python3 scripts/stock_analysis.py 600519 --quote

# 仅看K线（默认30天，可自定义）
python3 scripts/stock_analysis.py 600519 --kline --days 60

# 仅看资金流向
python3 scripts/stock_analysis.py 600519 --flow

# 仅看技术指标
python3 scripts/stock_analysis.py 600519 --tech

# 周K线
python3 scripts/stock_analysis.py 600519 --kline --period weekly --days 90
```

## 技术指标说明

| 指标 | 用途 | 关键信号 |
|------|------|---------|
| MA5/10/20 | 趋势判断 | 多头排列看涨，空头排列看跌 |
| RSI(14) | 超买超卖 | >70 超买，<30 超卖 |
| DIF/DEA/MACD | 动能判断 | 红柱多头，绿柱空头 |

## 资金流向说明

- 主力净流入：大单买入 - 大单卖出
- 超大单：机构级别资金
- 小单：散户资金
- 正值=流入（看多），负值=流出（看空）

## 数据源

- **实时行情**：腾讯财经（qt.gtimg.cn）
- **K线/历史数据**：新浪财经（money.finance.sina.com.cn）
- **技术指标**：本地计算（基于K线数据）
- 延迟约 1-3 分钟（非交易时段为上一交易日收盘数据）

## 已知限制

- 腾讯云服务器限制了东方财富批量 API，故使用腾讯+新浪替代
- 资金流向（主力/散户）使用量价数据替代，非真实资金流
- 不支持港股/美股（腾讯/新浪接口有对应端点但未封装）
- 技术指标为本地计算，非专业终端级别

## 依赖

- Python 3.11+
- akshare >= 1.18（已安装）
