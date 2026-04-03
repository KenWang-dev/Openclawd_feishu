# 待办清单

---

## 🔄 天网新旧版对比迁移（2026-03-30 ~ 2026-04-05）

> 每天对比 2~3 个旧 cron job vs 新 SKILL，结论：休眠 or 借鉴后休眠

### 旧版天网 job 清单（28个）

| # | 旧版 Cron Job | 对应新版 SKILL | 状态 |
|---|--------------|---------------|------|
| 1 | 天网-α1-AI三巨头监控 | ai/α-ai-giants | ⏳ |
| 2 | 天网-A1-电子供应链每日情报 | procurement/A-electronics | ⏳ |
| 3 | 天网-B1-供应链风险日报 | procurement/B-supply-risk | ⏳ |
| 4 | 天网-C1-政策与法规日报 | procurement/C-policy | ⏳ |
| 5 | 天网-D1-宏观财务日报 | procurement/D-macro-finance | ⏳ |
| 6 | 天网-β1-AI资本风向监控 | ai/β-ai-capital | ⏳ |
| 7 | 天网-γ1-AI政策推手监控 | ai/γ-ai-policy | ⏳ |
| 8 | 天网-δ1-AI人才流动监控 | ai/δ-ai-talent | ⏳ |
| 9 | 天网-ε1-AI社会影响监控 | ai/ε-ai-society | ⏳ |
| 10 | 天网-η1-Karpathy博客精选 | ai/η-blog | ⏳ |
| 11 | 天网-A2-电子供应链周度战略 | procurement/A-electronics | ⏳ |
| 12 | 天网-B2-供应链风险周报 | procurement/B-supply-risk | ⏳ |
| 13 | 天网-C2-政策与法规周报 | procurement/C-policy | ⏳ |
| 14 | 天网-D2-宏观财务周报 | procurement/D-macro-finance | ⏳ |
| 15 | 天网-E2-行业市场监控周报 | procurement/E-market | ⏳ |
| 16 | 天网-β2-AI资本风向周报 | ai/β-ai-capital | ⏳ |
| 17 | 天网-γ2-AI政策推手周报 | ai/γ-ai-policy | ⏳ |
| 18 | 天网-δ2-AI人才流动周报 | ai/δ-ai-talent | ⏳ |
| 19 | 天网-ε2-AI社会影响周报 | ai/ε-ai-society | ⏳ |
| 20 | 天网-ζ2-AI应用落地周报 | ai/ζ-ai-application | ⏳ |
| 21 | 天网-F2-AI采购最佳实践周报 | procurement/F-best-practice | ⏳ |
| 22 | 天网-G2-全球采购心声周报 | procurement/G-voice | ⏳ |
| 23 | 天网-H2-ESG绿色采购周报 | procurement/H-esg | ⏳ |
| 24 | 天网-I2-供应商生态系统周报 | procurement/I-supplier-ecosystem | ⏳ |
| 25 | 天网-W1-采购总监周报 | weekly/W-director-weekly | ⏳ |
| 26 | 天网-W2-老板周报 | weekly/W-boss-weekly | ⏳ |
| 27 | 天网-C3-政策与法规月报 | procurement/C-policy | ⏳ |
| 28 | (无对应) AI 三巨头监控（非天网版） | ai/α-ai-giants | ⏳ |

### 排期

| 日期 | 对比编号 | 任务 |
|------|---------|------|
| Day 1 (03-30) | #1, #2, #3 | α1, A1, B1 |
| Day 2 (03-31) | #4, #5, #6 | C1, D1, β1 |
| Day 3 (04-01) | #7, #8, #9 | γ1, δ1, ε1 |
| Day 4 (04-02) | #10, #11, #12 | η1, A2, B2 |
| Day 5 (04-03) | #13, #14, #15 | C2, D2, E2 |
| Day 6 (04-04) | #16, #17, #18 | β2, γ2, δ2 |
| Day 7 (04-05) | #19~#28 | ε2~C3 + 收尾 |

### 对比维度
1. **功能覆盖**：新版是否完全覆盖旧版功能
2. **搜索策略**：新旧版的搜索关键词、引擎、频率差异
3. **输出格式**：新版格式是否优于旧版
4. **参考知识库**：新版 references 是否更完整
5. **可借鉴点**：旧版有但新版缺失的价值点
6. **结论**：🟢 直接休眠 / 🟡 借鉴后休眠（需说明借鉴什么）

### 执行方式
- 在每日 heartbeat 中执行当天的对比任务
- 对比结果记录到 `memory/天网迁移-对比.md`
- 所有对比完成后，汇总报告给你审批
- 审批通过后，永久休眠旧版 cron job

---
