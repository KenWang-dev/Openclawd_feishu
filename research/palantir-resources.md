# Palantir（PLTR）深度研究资料合集

> 整理日期：2026-09-24
> 说明：本次整理时部分搜索引擎不可用，链接验证以直接抓取为准。
> 标记说明：✅ = 已验证可访问；⚠️ = 未能在本次会话中直接验证（palantir.com 对爬虫返回 404，浏览器访问一般正常），请以浏览器为准。

---

## 〇、建议学习顺序

1. **先建立全景**：Palantir Wikipedia / CNBC 访谈 → 知道公司是干嘛的
2. **理解产品**：Foundry / Gotham / AIP 官方页 + docs.palantir.com 的 Ontology 文档
3. **理解方法论（核心）**：Ontology → FDE 模式 → AIP Bootcamp（这是 Palantir 与其他企业 AI 公司的本质区别）
4. **看演示**：AIPCon 视频、AIP CONAN 演示（直观感受"operational AI"长什么样）
5. **读人**：Karp 的股东信、《The Technological Republic》、访谈 → 理解其意识形态与商业哲学
6. **读书**：《The Philosopher in the Valley》、Forward Deployed
7. **第三方视角**：媒体深度报道、商业模式分析
8. **财务与一手材料**：股东信、财报电话会、10-K、GitHub/文档

---

## 一、官方案例（Customer Cases / Case Studies）

- **Palantir 官网 Case Studies 入口**
  - 链接：https://www.palantir.com/customers/ ⚠️（页面路径可能调整，建议从 palantir.com 首页导航 "Customers / Case Studies" 进入）
  - 类型：官方案例库
  - 说明：官方客户案例合集，覆盖政府/国防、医疗、能源、制造、金融等，是了解"产品在真实组织里怎么落地"的第一手材料。

- **NHS England（英国国家医疗服务体系）FDP 案例**
  - 链接：https://www.palantir.com/nhsengland/ ⚠️（亦可搜索 "Palantir NHS Federated Data Platform"）
  - 类型：官方案例 + 公共报道
  - 说明：Foundry 在英国医疗系统最大规模部署（Federated Data Platform，合约约 3.3 亿英镑），是商业化民用案例的标杆，也伴随隐私争议，两面都值得读。

- **US Army / Vantage 与 Maven Smart System**
  - 链接：https://www.palantir.com/govproducts/ ⚠️；补充搜索 "Maven Smart System Palantir Army"
  - 类型：官方 + 国防报道
  - 说明：Palantir 政府业务的支柱。Army Vantage 是美军数据平台，Maven 是 AI 目标识别/战场决策系统，政府收入主要来源。

- **Rio Tinto（矿业）**
  - 链接：https://www.palantir.com/customers/ ⚠️（站内搜索 Rio Tinto）
  - 类型：官方案例
  - 说明：Foundry 在采矿/资源行业的经典案例，供应链与生产调度优化，早期商业化的样板客户。

- **Airbus（航空制造）**
  - 链接：https://www.palantir.com/customers/ ⚠️（站内搜索 Airbus）
  - 类型：官方案例
  - 说明：飞机制造与供应链的 Foundry 部署，制造业"数据操作系统"式用法的代表。

- **AIP CONAN 演示（AIPCon 2023）**
  - 链接：Palantir YouTube 频道搜索 "AIP CONAN"；AIPCon 直播回放：https://www.youtube.com/@palantir ⚠️
  - 类型：产品演示视频
  - 说明：AIP 发布时的标志性演示——虚构的"CONAN the Operator"用 LLM 在军事场景中调用工具、执行决策闭环，定义了 Palantir 的 "operational AI" 叙事，几乎所有后续 AIP 演示的母版。

---

## 二、方法论（Ontology / FDE / Bootcamp / 产品架构）

- **官方文档站 docs.palantir.com**
  - 链接：https://docs.palantir.com/ ✅
  - 类型：官方文档
  - 说明：Foundry / AIP / Gotham 全量文档入口，方法论最权威的来源，比任何二手文章都准确。

- **Ontology（本体论）官方文档**
  - 链接：https://palantir.com/docs/foundry/ontology-overview/ ⚠️（也可在 docs.palantir.com ✅ 内搜 "Ontology"）
  - 类型：官方文档
  - 说明：Palantir 的核心思想——把组织的数据、业务对象、行动（Actions）和决策建模为一张可执行的语义图谱，"让 AI 在业务对象上工作而不是在表格上工作"。理解 Palantir 的钥匙。

- **AIP Bootcamps**
  - 链接：https://bootcamp.palantir.com/ ⚠️（另见 https://www.palantir.com/aip-bootcamps/ ⚠️）
  - 类型：官方方法 + 营销体系
  - 说明：1-5 天让客户团队在真实数据上做出可用 AI 应用的"边做边卖"打法，既是获客漏斗也是交付方法论，被全行业效仿。这是 Palantir 增长飞轮的核心，必须搞懂。

- **Forward Deployed Engineer (FDE) 模式**
  - 类型：组织模式（无单一官方页面）
  - 入口：官方博客 https://blog.palantir.com/ ✅（Medium，内有多篇 FDE 文化文章）；招聘页 palantir.com/careers 搜 "Forward Deployed Software Engineer" ⚠️
  - 说明：工程师直接嵌入客户一线交付的模式，是 Palantir 组织能力的根基，也是 OpenAI/Anthropic 纷纷效仿的对象。理解 FDE = 理解 Palantir 为什么"贵但有效"。

- **"Operational AI" 理念**
  - 入口：Alex Karp 历年 CEO Letter to Shareholders（https://www.palantir.com/q2-2026-letter/ ⚠️，官网 Investors 栏可查历季）✅（路径在官网 HTML 中确认存在）
  - 类型：官方信件/博客
  - 说明：Karp 的股东信是半哲学半商业宣言，反复阐述"AI 必须进入运行中的决策系统（operations）而非停留在演示层面"，是官方意识形态的最佳文本。

- **Foundry / Gotham / AIP 产品架构**
  - 链接：https://www.palantir.com/foundry/ 、https://www.palantir.com/gotham/ 、https://www.palantir.com/aip/ ⚠️
  - 类型：官方产品页
  - 说明：三大产品线定位——Gotham（政府/国防决策）、Foundry（企业数据操作系统）、AIP（把 LLM 挂到 Ontology 上的运营 AI 层）。对照 docs.palantir.com 的架构文档一起看。

---

## 三、深度文章 / 书籍

- **《The Philosopher in the Valley: Alex Karp, Palantir, and the Rise of the Surveillance State》— Michael Steinberger**
  - 链接：https://books.google.com/books/about/The_Philosopher_in_the_Valley.html?id=azYMEQAAQBAJ ✅（出版信息已验证，2025-11 出版）
  - 类型：传记（Karp 官方授权传记）
  - 说明：记者 Steinberger 撰写的首部 Karp 传记，含大量新传记细节与心理画像，2025 年底最重要的 Palantir 文献。（注：任务中提到的"2026"实际为 2025 年 11 月出版。）

- **《The Technological Republic: Hard Power, Soft Beliefs, and the Future of the West》— Alex Karp（2025）**
  - 链接：搜索书名（Penguin Press / Crown 出版）
  - 类型：Karp 亲笔著作
  - 说明：Karp 的宣言式著作，论西方科技业为何背弃国防与国家能力，是理解 Palantir 意识形态立场的第一手文本。

- **《Forward Deployed: Inside the Palantir Framework》**
  - 链接：https://forwarddeployedbook.com/ ✅（已验证）
  - 类型：第三方研究书籍
  - 说明：拆解 Palantir 的 FDE 体系如何系统性解决企业转型五大失败原因（赞助、变革理由、变革管理、治理、能力建设），含十章章纲，是把 FDE 方法论整理得最系统的公开材料。

- **Maarten Sukel（前 Palantir FDE）的写作**
  - 链接：https://sukel.org ⚠️ / 搜索 "Maarten Sukel forward deployed"
  - 类型：从业者文章/Newsletter
  - 说明：前 Palantir FDE 撰写的一线交付视角文章，讲 FDE 如何在客户现场工作。（注：注意区分《The Palantir Papers》——archive.org 上的 "palantir-papers" ✅（https://archive.org/details/palantir-papers）是另一份泄露的公司内部文件集，非 Sukel 著作，亦有研究价值但需甄别。）

- **"Palantir Knows Everything About You" — Andy Greenberg, Wired（2020）**
  - 链接：搜索 "Wired Palantir Knows Everything About You"
  - 类型：媒体深度报道
  - 说明：Wired 资深记者对 Palantir 数据能力与隐私争议的经典长篇，第三方批判视角的必读篇。

- **"Palantir Has Secretly Been Using New Orleans to Test Its Predictive Policing System" — The Verge（2018）**
  - 链接：搜索 "The Verge Palantir New Orleans"
  - 类型：调查报道
  - 说明：揭露 Palantir 预测警务在新奥尔良的秘密测试，是理解公众争议与"监控国家"叙事的关键文本。

- **Vanity Fair 相关长篇（Steinberger 等）**
  - 链接：搜索 "Vanity Fair Palantir Karp"
  - 类型：媒体特稿
  - 说明：Vanity Fair 多年持续跟踪 Palantir/Karp，配合传记出版有新特稿，适合补充人物侧写。

---

## 四、视频 / 播客

- **Alex Karp @ Lex Fridman Podcast（#459，2025 年初）**
  - 链接：https://lexfridman.com/alex-karp/ ⚠️（本次抓取 404，请以 YouTube 搜 "Lex Fridman Alex Karp" 为准）
  - 类型：长访谈（3+ 小时）
  - 说明：Karp 少见的超长深谈，覆盖 AI、战争、意识形态、Palantir 哲学，是了解其思想效率最高的单集。

- **Palantir 官方 YouTube 频道**
  - 链接：https://www.youtube.com/@palantir ⚠️
  - 类型：官方视频
  - 说明：AIPCon 历届直播回放（含 CONAN 等产品演示）、DevCon 技术演讲、客户案例视频都在这里，一手演示素材最全。

- **AIPCon 系列大会**
  - 链接：YouTube @palantir 搜 "AIPCon" ⚠️
  - 类型：产品大会直播
  - 说明：每届都有真实客户现场演示"在 AIP 上做了什么"，是观察其客户结构与产品迭代节奏的最佳窗口。

- **Shyam Sankar（CTO）演讲与访谈**
  - 链接：搜索 "Shyam Sankar TED talk"（2024 TED 演讲）、"Shyam Sankar interview"
  - 类型：演讲/访谈
  - 说明：CTO 对 "operational AI"、国防科技、代理式 AI（agentic AI）的阐述，比 Karp 更技术、更具体。

- **CNBC 对 Karp 的专访（2026-08）**
  - 链接：https://www.youtube.com/watch?v=-1BYgqw6hYk ✅
  - 类型：电视访谈
  - 说明：近期 Karp 谈公司战略与市场的完整访谈，了解其当下口径。

---

## 五、第三方分析

- **Stratechery（Ben Thompson）关于 Palantir 的分析**
  - 链接：https://stratechery.com（站内搜 Palantir）⚠️
  - 类型：商业战略分析
  - 说明：从战略/商业模式角度拆解 Palantir 的定位与国防科技生态，Stratechery 也做过 Palantir 高管访谈（站内可查）。

- **Every.to 对 Palantir/Ontology/FDE 的分析**
  - 链接：https://every.to（搜 Palantir）⚠️
  - 类型：AI 商业评论
  - 说明：Dan Shipper 团队从"AI 如何进企业"视角分析 Palantir 的 Ontology 与 FDE 打法，适合 AI 从业者读。

- **Latent Space 播客相关内容**
  - 链接：https://www.latent.space（搜 Palantir）⚠️
  - 类型：技术播客/文章
  - 说明：AI 工程师社区视角看 Palantir 的运营 AI 与 agent 架构，偏工程实现。

- **财务/估值分析框架**
  - 入口：Karp CEO Letters（palantir.com 投资者栏目）✅、10-K（SEC EDGAR：https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=PLTR ⚠️）、财报电话会（YouTube/Investor Relations）⚠️
  - 类型：一手财务材料
  - 说明：PLTR 估值长期处于极高水位，建议用"Rule of 40、政府 vs 商业收入结构、RPO/合同额、客户数×客单价"框架自己拆，勿直接采信卖方结论。

---

## 六、一手材料入口

- **官方文档**：https://docs.palantir.com/ ✅（Foundry/AIP/Gotham 全文档）
- **官方博客**：https://blog.palantir.com/ ✅（Medium 承载，工程与方法论文章）
- **GitHub（palantir org）**：https://github.com/palantir ✅（开源项目：Blade/UI 工具包 22k+ stars、typescript-strict-plugin、osquery-windows-event-forwarding、pyspark-style-guide 等；另有 AIP/Foundry SDK 文档见 docs 站）
- **投资者关系**：https://investors.palantir.com ⚠️（股东信、10-K、财报电话会实录——Karp 股东信是必读一手文本）
- **AIP Bootcamp**：https://bootcamp.palantir.com ⚠️

---

## 精简摘要

**Palantir 是什么**：把企业/政府的原始数据建模成"可执行的语义图谱"（Ontology），再把 AI（AIP/LLM）挂到这张图上直接驱动真实业务决策的公司。产品三件套：Gotham（国防）、Foundry（企业数据操作系统）、AIP（运营 AI 层）。

**核心方法论（最值得深挖）**：
1. **Ontology**——AI 不在表格上工作，而在业务对象与行动上工作（官方文档 ✅）
2. **FDE**——工程师驻场一线交付，解决企业 AI"落地难"的组织答案（forwarddeployedbook.com ✅ 系统拆解）
3. **AIP Bootcamp**——几天内让客户在自己数据上做出可用应用，获客即交付的飞轮

**必读清单（按顺序）**：docs.palantir.com 的 Ontology 文档 → AIPCon/CONAN 演示视频 → Karp 股东信 → Lex Fridman 访谈 → 《The Technological Republic》→ 《The Philosopher in the Valley》(Steinberger, 2025-11) → Wired/The Verge 批判性报道 → 自己用财报拆估值。

**一句话**：研究 Palantir 的本质是研究"AI 如何从演示走进组织的运行系统"，Ontology + FDE + Bootcamp 三者缺一不可。

**注意事项**：① palantir.com 站内具体路径对爬虫返回 404（本次未能逐条验证，浏览器访问官网导航即可找到，勿把 ⚠️ 链接当死链）；② 任务中提到的 Karp 传记实际出版时间为 2025 年 11 月（非 2026）；③ 《The Palantir Papers》在 archive.org 上是泄露文件集，与 Maarten Sukel 无关，引用时注意区分。
