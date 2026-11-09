# Semantica 供应链知识图谱 POC 技术评估

> 评估对象：[semantica-agi/semantica](https://github.com/semantica-agi/semantica) v0.7.0（pip 包名 `semantica`，MIT License）
> 评估日期：2026-11-09 ｜ 评估人：OpenClaw agent（受 Ken 委托）
> POC 代码：`poc/supply_chain_poc.py` ｜ 运行环境：Python 3.11.6 / OpenCloudOS x64 / venv

---

## 结论速览

**可行性打分：7.5 / 10**

- 核心卖点（本体 SHACL/OWL、溯源 PROV-O、确定性推理、图构建）**全部实测可用**，POC 一次跑通"单一来源×高风险供应商→成品→订单"的多跳影响分析。
- 定位是"语义/上下文基础设施层"而非现成供应链产品，数据建模、查询逻辑都要自己写。
- 与 Ken 之前看的 Microsoft Ontology-Playground（教学工具）相比，Semantica 是**真正可落地的工程库**，且自带 MCP Server。

---

## 1. 安装与上手

| 项 | 结果 |
|---|---|
| 安装命令 | `python3 -m venv poc/semantica-venv && pip install semantica`（用清华源） |
| 安装耗时 | **4 分 10 秒**（依赖较重：rdflib、networkx、scikit-learn、neo4j driver 等全家族） |
| Python 要求 | 3.11+（README 明确标注） |
| 版本 | 0.7.0，迭代很快（2025-06 创建，至今 14.5k stars） |

**API 上手难度：中等。** 文档（docs.getsemantica.ai）齐全，DeepWiki 有 AI 问答。坑在 API 命名和文档不完全同步：

### 踩过的坑（都记录在 POC 代码注释里）
1. **`GraphBuilder.build(sources, ...)` 是单一 `sources` 参数**，entities/relationships 要打包进一个 dict 传入，不能 `build(entities=..., relationships=...)`。
2. **关系字典键名必须是 `source/target` 或 `subject/object` + `relationship_type`**。用 `s/t/r` 这类自定义键会被**静默全部丢弃**（只打一条 warning："All relationships were dropped"），不报错——这是最大的坑，排障花了 20 分钟。
3. `OntologyEngine` 没有 `define_class()`，正确姿势是 `oe.from_data({"entities":..., "relationships":...})` 从数据**自动推断**本体，再 `to_shacl()` / `to_owl()` 导出。
4. `ProvenanceManager(storage="sqlite")` 不对，要用 `ProvenanceManager(storage_path=...)`。
5. `export_prov(format="json")` 需要 rdflib 的 json-ld 插件，缺了会 KeyError（可改 yaml/ttl 或装插件）。
6. LLM 后端（openai/litellm）是**可选依赖**，不装也完全不影响 KG/本体/溯源——这点对数据敏感场景很友好。

---

## 2. POC 概况（贴近 Ken 的采购业务域）

- **24 个实体 / 48 条关系**，8 类实体：物料、供应商、工厂、BOM、成品、订单、风险事件、物流航线。
- 覆盖全部要求场景：
  - **单一来源物料**：锂电池 5000mAh 仅由高风险供应商 X 供货
  - **供应商财务风险**：供应商 X 债务违约风险事件（debt_ratio=0.91）
  - **物流中断**：红海航线中断 → 影响连接器供应 → 波及 S1/G2
  - **替代料**：MCU-A1 ↔ MCU-B2 pin 兼容（含 ECR 审批号）

## 3. 四项核心能力实测

### (a) 本体定义 ✅
`oe.from_data()` 从图数据自动推断出 8 个类 + 11 个属性（coverage 1.0，quality_check 通过），一行导出：
- `to_shacl(format="turtle")` → 4.7KB 标准 `sh:NodeShape`（targetClass 正确）
- `to_owl(format="turtle")` → 2.5KB OWL 本体
- SKOS 词表模块也有（`list_concepts` / vocabularies），本次未深测
- 额外有 `OntologyQualityGate`、`CompetencyQuestions` 等企业级功能

### (b) 图查询（多跳）✅
用内置关系遍历实现"**哪些成品依赖单一来源的高风险供应商**"：
```
物料 MAT-BATT ← 单一供应商 SUP-X(高风险) → 影响成品 [PROD-S1] → 受威胁订单 [ORD-1001]
```
也支持 SPARQL（reasoning 模块 `SPARQLQueryResult`）和 Neo4j/FalkorDB 等 LPG 后端（polyglot storage，可换后端不改代码）。注意：**没有内置 Cypher 风格的多跳 DSL，复杂图查询要么走 SPARQL 要么自己写遍历**。

### (c) 溯源/审计 ✅（本项目最强项）
`ProvenanceManager` 完整实现 W3C PROV-O：每条事实带 39 个溯源字段（agent_id、source_document、checksum 链、derived_from_id、invalidated_by、时间戳、confidence），支持 `get_lineage` / `trace_descendants` / `verify_chain`（checksum 完整性校验）/ `revision_history` / 时效（valid_from/until）。`GraphBuilderWithProvenance` 建图时自动为每个实体/关系记录 provenance。对"采购决策留痕"场景是杀手级能力。

### (d) LLM 集成 ✅（完全可选）
- `semantica.llms`：OpenAI/Anthropic/Gemini/DeepSeek/Ollama/LiteLLM 等 10+ 后端，统一接口
- 用途：LLM 抽取实体/关系（`ner_method="llm"`）、LLM Ontology 生成、RAG 检索
- 默认**不需要任何 API key**：NER/relation/triplet 抽取有本地 pattern/ml 后端，图构建/推理/溯源全程确定性
- GraphRAG 形态：KG + `NodeEmbedder`(node2vec) + vector_store 模块，检索是"图遍历+语义搜索"混合，不是纯向量 RAG

---

## 4. 与 Agent/MCP 工具链对接

**内置 MCP Server**（`semantica.mcp_server`），实测暴露 15 个工具：
`extract_entities / extract_relations / add_entity / add_relationship / query_graph / run_reasoning / get_graph_analytics / export_graph / record_decision / query_decisions / find_precedents / get_causal_chain / get_graph_summary / update_node / delete_node`

→ Claude/OpenClaw 等任何 MCP 客户端可以**零代码**把 KG 当工具用，"记录决策→查先例→查因果链"这套对采购 AI 助手非常契合。另有 LangChain/CrewAI/Agno drop-in 集成、CLI、REST API。

## 5. 项目活跃度快照（2026-11-09）

| 指标 | 值 |
|---|---|
| Stars / Forks | **14,480 / 1,707** |
| 创建时间 | 2025-06（约 17 个月冲到 14k+ stars，Trendshift 榜单项目） |
| 最近 push | 2026-11-09（评估当天，**极活跃**） |
| Open issues | 120 |
| License | MIT |
| CI | GitHub Actions（含 install matrix），OpenSSF Scorecard |
| 商业实体 | getsemantica.ai（开源核心 + 文档站 + Discord，open-core 模式迹象） |

⚠️ 注意：项目年轻、大版本 0.x，API 可能破坏性变更；但开发速度和社区热度都是头部水平。

## 6. 与供应链场景的匹配点

| 场景 | 匹配度 | 说明 |
|---|---|---|
| 单一来源风险监控 | ★★★★★ | 多跳影响分析直接命中（本次 POC 已验证） |
| 采购决策审计留痕 | ★★★★★ | PROV-O + Decision Intelligence 原生支持，监管可答辩 |
| 替代料管理 | ★★★★ | HAS_ALTERNATE 边 + 属性（pin 兼容/ECR），SHACL 可约束验证规则 |
| 物流中断传导 | ★★★★ | 图传播天然适合；航线→供应商→物料→成品→订单链路清晰 |
| BOM 多层穿透 | ★★★ | 本 POC 单层 BOM 已通；多层 BOM 需自建递归，无现成 BOM 语义 |
| 与 ERP 对接 | ★★★ | 有 Databricks/Snowflake/SAP OData 连接器（未实测 SAP） |

## 7. 落地路线建议（3 步）

1. **第 1 步（1-2 周）：真实数据小图。** 从 Ken 的 ERP/BOM 表导出 100-500 个真实物料+供应商，跑 `from_data` 自动本体 + SHACL 校验，验证数据清洗成本。关键验证点：关系键名规范化 pipeline。
2. **第 2 步（2-4 周）：接 MCP 到现有 AI 助手。** 启动 semantica MCP Server，让采购助手获得 `query_graph / record_decision / find_precedents` 能力，采购员日常问"这个料断供影响哪些订单"。
3. **第 3 步（1-2 月）：接入 SAP OData + 风险事件流**（天眼查/海关/新闻），用 LLM 抽取非结构化风险信号入图，配 GraphBuilderWithProvenance 全程留痕，形成风险预警闭环。

## 8. 是否替代/补充 NVIDIA auto-ontology？

**建议：补充 + 主力，而非简单替代。**

| | Semantica | NVIDIA auto-ontology |
|---|---|---|
| 定位 | 完整 KG 基础设施（构建+查询+推理+溯源+MCP） | 本体自动生成（偏建模环节） |
| 溯源审计 | 原生 PROV-O | 弱 |
| Agent 对接 | MCP Server 现成 | 无 |
| 生态绑定 | MIT，零绑定 | NVIDIA 生态 |

- Semantica 的 `LLMOntologyGenerator` 可覆盖 auto-ontology 的"从数据生成本体"职能；
- 若已深度投入 NVIDIA/RAPIDS 栈，可保留 auto-ontology 做本体草案，**用 Semantica 做下游的图构建、溯源、推理和 Agent 服务层**；
- 相比 Ontology-Playground（纯教学），Semantica 是当前最值得投入真实工时的选择。

---

## 附：POC 复现

```bash
python3 -m venv poc/semantica-venv
poc/semantica-venv/bin/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple semantica
poc/semantica-venv/bin/python poc/supply_chain_poc.py   # 输出见 poc/poc_output.txt
```
