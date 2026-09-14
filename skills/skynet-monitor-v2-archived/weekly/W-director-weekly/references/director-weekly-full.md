# W1 - 采购总监周报（综合）

| 属性 | 值 |
|------|-----|
| 编码 | W1 |
| 阶段 | — |
| 频率 | 每周 |
| 时间范围 | 过去7天 |
| 领域 | — |
| 模板 | director-weekly |
| 画像 | W1 采购总监（参照 `references/personas.md`） |
| 调度 | 周日 15:15 |
| 类型 | 综合（二次提炼，非搜索采集） |

## 执行方式

**不使用搜索引擎**。直接从本周 archive 存档中读取过去 7 天的所有任务报告，二次提炼生成综合周报。

## 数据来源

```bash
# 读取过去 7 天的所有 archive 报告
find /root/.openclaw/workspace/archive/ -name "*.md" -mtime -7 ! -name "*-index.md" ! -name "README.md"
```

### 数据来源映射

| 报告板块 | 数据来自 |
|---------|---------|
| TOP5 核心洞察 | 全部 25 任务综合提炼 |
| 供应链风险仪表盘 | B1/B2 供应链风险 |
| 成本与价格趋势 | D1/D2 宏观财务 + A1 电子供应链 |
| AI 技术趋势 | α1 三巨头 + ζ2 应用落地 + F2 AI采购 |
| 行业与政策 | C1/C2 政策法规 + E2 行业市场 |
| 行动清单 | 从上述板块提炼 |

## 报告结构

参照 `references/templates/director-weekly.md` 模板。

## 执行步骤

1. 读取 `references/templates/director-weekly.md` 模板
2. 扫描 `/root/.openclaw/workspace/archive/` 下过去 7 天所有报告
3. **Archive 完整性检查**（见下方）
4. 按模板 6 大板块逐一提炼数据
5. 价格传导 ROI 必须用实际数据计算
6. 保存到 archive
7. 通过飞书发送（4 条消息）

## Archive 完整性检查

在提炼报告前，先统计本周 archive 覆盖情况：

### 检查清单

```
预期 25 个任务（10 日报 × 7 天 + 14 周报 + 1 月报(如适用)）
实际找到 N 个报告文件
覆盖率 = N / 预期 × 100%
```

### 降级策略

| 覆盖率 | 策略 |
|--------|------|
| ≥80% | 正常生成，在报告头部标注缺失的任务编码 |
| 50%-79% | 生成报告，头部加 ⚠️ 警告："本周数据不完整（覆盖率 X%），以下板块基于有限数据" |
| <50% | 生成精简版报告，头部加 🔴 警告："本周数据严重不足（覆盖率 X%），建议人工补充" |

### 缺失标注格式

报告中引用缺失任务数据时，用以下格式标注：
```
⚠️ [B2 供应链风险周报] 本周未生成，风险数据来源降级为 B1 日报汇总
```

## 特殊规则

- **必须从 archive 提取实际数据**，禁止模板化占位符
- 核心洞察按影响级别排序：🔴高→🟡中→🟢低
- 在所有 14 个周报完成后执行
- 禁止发送执行过程信息
- Archive 完整性检查结果写入报告头部统计区

## 飞书发送（4 条消息）

```javascript
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第1条：标题+TOP5" });
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第2条：风险仪表盘+成本" });
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第3条：AI趋势+行业政策" });
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第4条：行动清单+统计" });
```

## 存档

```bash
WEEK=$(date +%Y-W%V)
mkdir -p "/root/.openclaw/workspace/archive/W1-采购总监周报"
echo -e "$REPORT" > "/root/.openclaw/workspace/archive/W1-采购总监周报/W1-$WEEK.md"
```
