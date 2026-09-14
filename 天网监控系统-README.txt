# 天网监控系统 (Skynet Monitor) v1.0.1

> AI × 采购全维度情报监控系统 — 27 个监控任务覆盖 AI 动态、供应链、政策法规、行业市场

## 📋 任务总览

完整的 27 个监控任务清单、编码规则、阶段分类、搜索策略详见 **[TASK-INDEX.md](TASK-INDEX.md)**。

## 架构

```
skynet-monitor/
├── TASK-INDEX.md                 # 📋 监控任务总索引（27个任务唯一注册表）
├── SKILL.md                      # 系统主入口（路由 → 搜索 → 分析 → 报告 → 存档）
├── ai/                           # AI 类监控（11个任务）
│   ├── α-ai-giants/              #   α1 AI三巨头动态（OpenAI/Anthropic/Google DeepMind）
│   ├── β-ai-capital/             #   β1 AI投融资风向 + β2 AI投融资事件汇总
│   ├── γ-ai-policy/              #   γ1 AI产业政策与资金支持 + γ2 中美AI监管政策
│   ├── δ-ai-talent/             #   δ1 AI人才招聘与流动 + δ2 AI岗位数量与薪资
│   ├── ε-ai-society/             #   ε1 AI就业与阶层分化 + ε2 AI就业伦理与教育变革
│   ├── ζ-ai-application/         #   ζ2 AI降本增效落地案例
│   └── η-blog/                   #   η1 顶级技术博客AI精选（Karpathy源）
├── procurement/                  # 采购与供应链类（14个任务）
│   ├── A-electronics/            #   A1 电子供应链断供涨价情报 + A2 电子供应链周度战略
│   ├── B-supply-risk/            #   B1 供应链原材料地缘风险 + B2 供应链21项风控指标
│   ├── C-policy/                 #   C1 贸易制裁与环保法规 + C2 贸易制裁关税出口管制 + C3 贸易政策与合规月报
│   ├── D-macro-finance/          #   D1 原材料汇率利率宏观 + D2 利率汇率与融资成本
│   ├── E-market/                 #   E2 半导体行业波特五力分析
│   ├── F-best-practice/          #   F2 AI赋能采购最佳实践
│   ├── G-voice/                  #   G2 全球采购从业者痛点与心声
│   ├── H-esg/                    #   H2 ESG合规与绿色供应链
│   └── I-supplier-ecosystem/     #   I2 供应商并购与技术突破
├── weekly/                       # 综合周报（2个任务）
│   ├── W-director-weekly/        #   W1 采购总监情报周报（全系统精华提炼）
│   └── W-boss-weekly/            #   W2 老板决策简报（3个关键数字+NO.1优先级）
├── references/                   # 参考资料
│   ├── tasks/                    #   各任务详细配置（27个 .md）
│   ├── templates/                #   报告模板（daily/weekly/monthly/director/boss）
│   ├── analysis/                 #   分析框架（ai-sector/supply-chain/macro-finance 等）
│   ├── personas.md               #   用户画像
│   ├── indicator-ownership.md    #   指标归属
│   ├── schedule.md               #   调度时间表
│   └── sources.md                #   数据源
├── archive/                      # 历史报告存档
├── reports/                      # 执行报告
└── logs/                         # 执行日志
```

## 编码规则

| 字段 | 说明 | 示例 |
|------|------|------|
| 类型 | AI 类用希腊字母（α-η），采购类用英文大写（A-I） | α = AI三巨头，A = 电子供应链 |
| 后缀 | 1=日报，2=周报，3=月报 | α1 = 三巨头日报，C3 = 政策月报 |
| 阶段 | 生存/发展/可持续（MECE 三分法） | 生存 11 + 发展 7 + 可持续 7 + 综合 2 = 27 |

## 统计

| 频率 | AI | 采购 | 综合 | 合计 |
|------|-----|------|------|------|
| 日报 | 6 | 4 | — | 10 |
| 周报 | 5 | 9 | 2 | 16 |
| 月报 | — | 1 | — | 1 |
| **合计** | **11** | **14** | **2** | **27** |

## 设计原则

- **直球执行**：每个 SKILL.md 包含完整的搜索指令和输出格式，AI 读一个文件即可执行
- **搜索充足**：Tavily + Brave 双引擎，中英文全覆盖
- **结构化输出**：6维评分体系 + Top5 核心情报 + 数据溯源

## 使用

配合 [OpenClaw](https://github.com/openclaw/openclaw) 使用，通过 cron 定时触发各监控任务。
