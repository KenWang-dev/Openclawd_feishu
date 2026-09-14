#!/bin/bash
# OpenClaw 热门案例收集脚本
# 每天下午 14:00 执行

TODAY=$(date '+%Y-%m-%d')
OUTPUT_FILE="/tmp/openclaw-cases-${TODAY}.md"

# 清理旧文件
rm -f /tmp/openclaw-cases-*.md

cat > "$OUTPUT_FILE" << 'EOF'
**🦞 OpenClaw 热门案例**

**过去 7 天动态 · TOP 5**

更新于 DATE_PLACEHOLDER

── ─ ─ ─ ─ ─ ─ ─ ─ ─

**🥇 AI 代码助手 + 自动化**

**功能**：用 OpenClaw 作为 24/7 AI 编程助手，自动 review PR、写文档、修 bug

**受众**：开发者、技术团队

**链接**：[21 Advanced OpenClaw Automations](https://medium.com/@rentierdigital/21-openclaw-automations-nobody-talks-about-because-the-obvious-ones-already-broke-the-internet-3f881b9e0018)

**对 Ken 的价值**
- **直接可用**：用 OpenClaw 自动 review 采购合同、生成报表
- **间接启发**：多 Agent 协作模式 → 可拆成"供应商审核 Agent"+"报价分析 Agent"

── ─ ─ ─ ─ ─ ─ ─ ─ ─

**🥈 邮件自动化工作流**

**功能**：每天 7AM 自动读取邮箱，分类、汇总、标记紧急邮件

**受众**：商务人士、运营团队

**链接**：[OpenClaw Use Cases for Business](https://contabo.com/blog/openclaw-use-cases-for-business-in-2026/)

**对 Ken 的价值**
- **直接可用**：自动处理供应商邮件、分类询价邮件、标记紧急采购需求
- **间接启发**：邮件自动归档 → 可延伸为"采购询价自动入库"

── ─ ─ ─ ─ ─ ─ ─ ─ ─

**🥉 营销自动化**

**功能**：数据提取、报表生成、线索丰富化、社交媒体自动发布

**受众**：营销团队、销售

**链接**：[7 Ways to Automate Marketing Workflows](https://improvado.io/blog/openclaw-marketing-use-cases)

**对 Ken 的价值**
- **直接可用**：自动生成采购周报/月报、竞品价格报表
- **间接启发**：报表自动化 → 可做成"AI 采购日报"自动推送

── ─ ─ ─ ─ ─ ─ ─ ─ ─

**🏅 内容工厂 Multi-Agent**

**功能**：研究 → 写作 → 缩略图生成 → 自动发布，多 Agent 协作

**受众**：自媒体、内容创作者

**链接**：[Top 10 OpenClaw Use Cases](https://simplified.com/blog/automation/top-openclaw-use-cases)

**对 Ken 的价值**
- **直接可用**：AI 采购课程内容自动生产：研究选题 → AI 写作 → 配图 → 发布
- **间接启发**：多 Agent 分工 → 可建立"采购 AI 研究员"+"采购 AI 写手"+"采购 AI 运营"

── ─ ─ ─ ─ ─ ─ ─ ─ ─

**🏅 智能客服 + 知识库**

**功能**：自动回复客户问题、更新知识库、汇总常见问题

**受众**：客服团队、运营

**链接**：[15 Powerful OpenClaw Use Cases](https://kanerika.com/blogs/openclaw-usecases/)

**对 Ken 的价值**
- **直接可用**：搭建采购知识库 FAQ，学员/客户自动问答
- **间接启发**：知识库自动更新 → 可接入"供应商产品库"自动答疑

── ─ ─ ─ ─ ─ ─ ─ ─ ─

**🎯 AI × 采购 核心应用**

| 场景 | 直接价值 | 启发方向 |
|-----|---------|---------|
| 供应商评估 | 自动抓取工商信息、财务数据 | 接入天眼查/企查查 API |
| 报价处理 | PDF 报价单自动提取比对 | 做成移动端一键拍照询价 |
| 合同审查 | 条款风险自动标记 | 采购合同模板库 + AI 审核 |
| 市场情报 | 竞品动态、价格监控 | 做成小程序付费服务 |

**🎬 自媒体 核心应用**

| 场景 | 直接价值 | 启发方向 |
|-----|---------|---------|
| 内容工厂 | 选题 → 写作 → 排版 → 发布 | 做成标准化 SOP |
| 数据图表 | 行业数据 → 自动可视化 | 采购指数可视化 |
| 热点追踪 | 实时监控 → 快速产出 | 采购行业热点日报 |
| 多平台分发 | 一稿多发：公众号/小红书/X | 建立分发工作流 |

── ─ ─ ─ ─ ─ ─ ─ ─ ─

*每天下午 14:00 自动更新*
EOF

# 替换日期
sed -i "s/DATE_PLACEHOLDER/${TODAY}/g" "$OUTPUT_FILE"

# 发送到飞书
message --action send --target "ou_d81ad689104f8c660a5834c10740aea8" --message "$(cat $OUTPUT_FILE)" 2>/dev/null

echo "✅ 已发送 OpenClaw 热门案例 to Ken"
