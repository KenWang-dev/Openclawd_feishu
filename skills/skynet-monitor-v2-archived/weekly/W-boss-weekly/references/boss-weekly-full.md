# W2 - 老板周报（综合）

| 属性 | 值 |
|------|-----|
| 编码 | W2 |
| 阶段 | — |
| 频率 | 每周 |
| 时间范围 | 过去7天 |
| 领域 | — |
| 模板 | boss-weekly |
| 画像 | W2 老板（参照 `references/personas.md`） |
| 调度 | 周日 15:30 |
| 类型 | 综合（基于 W1 + archive 二次提炼） |

## 执行方式

**不使用搜索引擎**。在 W1(采购总监周报) 完成后执行，引用 W1 分析结果 + archive 存档，提炼为老板视角周报。

## 数据来源

1. **W1 采购总监周报**（核心）
2. 本周全部 archive 存档报告（补充）

## 报告结构

参照 `references/templates/boss-weekly.md` 模板。

核心差异（vs W1）：
- **3 个关键数字**取代 TOP5 洞察
- **ROI 仪表盘**取代详细风险表
- **本周 NO.1 优先级**取代行动清单
- 老板视角：关注"花多少钱/省多少钱/值不值"

## 执行步骤

1. 读取 `references/templates/boss-weekly.md` 模板
2. 读取 W1 采购总监周报（**必须存在，否则中止**）
3. 扫描本周 archive 补充数据
4. **Archive 完整性检查**：继承 W1 的覆盖率评估，若 W1 已标注缺失则直接引用
5. 按老板视角提炼：数字→金额→ROI
6. 保存到 archive
7. 通过飞书发送（3 条消息）

## W1 依赖检查

W2 强依赖 W1。执行前必须确认：

| 检查项 | 通过条件 | 失败处理 |
|--------|---------|---------|
| W1 报告存在 | archive 中找到本周 W1 文件 | 🔴 中止 W2，飞书通知"W1 未完成，W2 暂停" |
| W1 覆盖率 | W1 头部有覆盖率统计 | 继承 W1 覆盖率，同等降级策略 |

## 特殊规则

- W2 在 W1 之后执行，可直接引用 W1 结论
- **ROI 必须有数据支撑**（公式 + 实际数字）
- 禁止模板化占位符
- 禁止发送执行过程

## 飞书发送（3 条消息）

```javascript
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第1条：标题+3个关键数字" });
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第2条：本周优先级+ROI仪表盘" });
message({ action: "send", channel: "feishu", target: "ou_a7195bd3e0508f0e0d09f19ff12a8811", message: "第3条：下周关注+统计" });
```

## 存档

```bash
WEEK=$(date +%Y-W%V)
mkdir -p "/root/.openclaw/workspace/archive/W2-老板周报"
echo -e "$REPORT" > "/root/.openclaw/workspace/archive/W2-老板周报/W2-$WEEK.md"
```
