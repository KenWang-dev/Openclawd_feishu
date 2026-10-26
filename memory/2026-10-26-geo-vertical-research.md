# GEO（Generative Engine Optimization）纵向历史调研纪要
> 调研日期：2026-10-26。用途：深度研究报告素材。注：标注 ⚠ 的条目来自模型通识/未逐字核验的来源 URL，引用前建议复核。

## 一、GEO 概念起源

### 1.1 奠基论文（已核验）
- **论文**：Aggarwal, Murugappan Venkataraman, Vivek Nair, Yuchao Jiang, Diyang Tang, Huang Fang, Weiwei Te, Nitish Anshuman, Mausab Sardar, Ranjita Naik, Hamed Zamani, Wuwei Lan, Shir Baer, Osnaghi 等（普林斯顿大学、乔治亚理工、Allen AI、IIT Delhi 等机构合作；第一作者 Pranjal Aggarwal）。⚠ 完整作者名单以论文页为准。
- **arXiv 2311.09735**，v1 提交于 **2023-11-16**，后被 **KDD 2024** 接收。
  - 摘要页：https://arxiv.org/abs/2311.09735
- **核心内容**：
  - 首次提出"生成式引擎（Generative Engine, GE）"统一框架与"GEO"术语——首个帮助内容创作者提升在生成式引擎响应中可见性的黑盒优化范式。
  - 发布 **GEO-bench**：跨多领域、上万条用户查询的大规模基准（论文正文称约 10K 查询）。
  - **核心发现**：应用 GEO 策略可使内容在生成式引擎响应中的可见性最高提升 **40%**；不同策略效果因领域而异，需要领域专属优化。
  - 论文中的策略包括：引用来源（cite sources）、加入统计数据（quotation/statistics）、权威语气、关键词填充（效果反而最差）等。

### 1.2 2024–2026 概念演化
- 2024 上半年：论文在 KDD 2024 发表后，SEO 圈开始引用"GEO"术语；Gartner 同期预测（见 3.1）加速了讨论。
- 2024–2025：创业公司（Profound、Scrunch、Peec AI 等）与大厂工具（Semrush、Ahrefs、Adobe LLM Optimizer、HubSpot）陆续入场，GEO 从 SEO 的子话题演变为独立品类/独立预算线。
- 2026：Google 官方发布针对生成式 AI 搜索的优化指南，称 AEO/GEO "本质上仍是 SEO"；Microsoft Advertising 则正式区分 AEO（面向 Copilot 等智能体）与 GEO（面向生成式搜索环境）。
  - 维基百科词条（已核验）：https://en.wikipedia.org/wiki/Generative_engine_optimization

## 二、关键推动事件时间线

- **2022-11**：ChatGPT 上线（OpenAI），对话式信息获取习惯的开端。（背景事件）
- **2022-12**：Perplexity AI（Aravind Srinivas 等）上线，定位"答案引擎"。⚠ https://www.perplexity.ai/
- **2023-02-07**：微软发布 Bing Chat（后来的 Copilot），GPT 驱动搜索。⚠ https://blogs.microsoft.com/blog/2023/02/07/introducing-the-new-bing/
- **2023-05**：Google I/O 发布 **SGE（Search Generative Experience）** 实验功能，AI Overviews 前身。⚠ https://blog.google/products/search/generative-experience-search-2023/
- **2023-11-16**：GEO 论文提交（arXiv 2311.09735）——学术命名起点。
- **2024-01**：SGE 从 Labs 开放给更多用户。⚠
- **2024-02-19**：**Gartner 预测**"到 2026 年传统搜索引擎流量将下降 25%"，被 GEO 行业广泛引用。
  - 原文（Gartner 有反爬）：https://www.gartner.com/en/newsroom/press-releases/2024-02-19-gartner-predicts-search-engine-volume-will-drop-25-percent-by-2026-due-to-ai-chatbots-and-other-virtual-agents
- **2024-05-14**：Google I/O 正式推出 **AI Overviews**（美国先行），随后引发"Google 崩了把烂答案喂给用户"等舆论事件。⚠ https://blog.google/products/search/ai-overviews/
- **2024-06**：SparkToro/Datos 研究：**2024 年美国约 60.45% 的 Google 搜索零点击**（详见 2.1 数据）。
- **2024-09**：**/llms.txt 提案**发布（见 4.3）。
- **2024-10-31**：**ChatGPT Search** 上线（对 Plus 用户先行开放，直接挑战 Google）。⚠ https://openai.com/index/introducing-chatgpt-search/
- **2024Q4–2025**：品牌方/AI 可见性监测创业潮：Profound、Goodie、Peec AI、Otterly.ai、Scrunch（后被 Sitecore 收购）等。Profound 于 **2025 年 2 月完成由 Sequoia 领投的 2000 万美元 A 轮**。⚠ https://techcrunch.com/tag/profound/
- **2025-04-17**：Ahrefs 研究：AI Overviews 使第一位的 CTR 下降 **34.5%**（已核验，见 2.1）。
- **2025**：Adobe 推出 LLM Optimizer；a16z 发文使用"GEO"一词，风投背书使其主流化（维基百科已核验）。
- **2025-06（SparkToro 更新）**：AI Overviews 出现在 20%+ 的搜索中，出现时 CTR 降近 60%。
- **2026**：Google 官方指南称"为生成式 AI 搜索优化仍是 SEO"；Adobe Brand Visibility 以 GEO 平台营销；微软广告双术语体系（维基百科已核验）。
- **2026-06**：SparkToro/Similarweb：**2026 前四个月 68.01% 的 Google 搜索零点击**（已核验）。

### 2.1 流量下滑关键数据（已核验）
- SparkToro 2024 零点击研究（Rand Fishkin，基于 Datos 点击流数据）：美国 Google 搜索 58.5%→60.45% 零点击；2026 年更新为 **68.01%**，两年增长 7.5 个百分点，"十年来最快加速"。
  - https://sparktoro.com/blog/2024-zero-click-study/ （现已重定向至 2026 版：https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ ）
- Ahrefs（2025-04-17，Ryan Law）：300K 关键词分析，AI Overview 存在时首位结果 CTR **下降 34.5%**。
  - https://ahrefs.com/blog/ai-overviews-reduce-clicks/
- Ahrefs 后续（2026）：86.3 万 SERP 中仅 **38%** 的 AI Overview 引用来自自然排名前 10（一年前为 76%）——排名与 AI 引用脱钩，成为 GEO 独立性的核心论据。
  - https://ahrefs.com/blog/ai-overview-citations-top-10/ ；SEJ 报道：https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/

## 三、行业标准化与格局

### 3.1 市场规模预测（各家口径差异极大，报告需注明）
- Market Intelo：2025 年 $848M → 2034 年 $19.8B（CAGR 50.5%）。https://marketintelo.com/report/generative-engine-optimization-geo-market
- Market Decipher / Superlines：2026 年约 $1.09B → 2034 年 $17–33B。https://www.marketdecipher.com/report/generative-engine-optimization-market ；https://www.superlines.io/articles/geo-market-size-statistics/
- AllAboutAI 汇总：2024 年 $886M → **$7.3B（2030 左右）**。https://www.allaboutai.com/resources/ai-statistics/generative-engine-optimization-statistics/
- Dimension Market Research（仅美国）：2026 年 $365M → 2034 年 $6.36B（CAGR 42.9%）。https://dimensionmarketresearch.com/report/generative-engine-optimization-geo-market/
- 提示：多数报告来自 SEO 内容站背景的中小研究机构，数据可信度参差。

### 3.2 命名之争（已核验，来源维基百科词条）
- 同义术语：**GEO**（生成式引擎优化）、**AEO**（答案引擎优化）、**LLMO**（大语言模型优化）、**AIO**（AI 优化）、AI SEO。
  - 注：⚠ "AEO"一词早于 GEO 论文（2018 年前后语音搜索/featured snippet 时代已被 SEO 圈使用，Conductor、Brent Csutoras 等有早期文章），GEO 论文使其获得学术表达。
- 立场分化：
  - **Google（2026 官方指南）**：AEO/GEO "仍是 SEO"。
  - **Microsoft Advertising**：AEO=面向智能体/助手，GEO=面向生成式搜索环境（双术语）。
  - **Bing 文档**：使用"GEO"但强调 SEO 基础决定 AI 体验资格。
  - **HubSpot** 用 AEO；**Profound** 认为 AEO/GEO 同义但嫌 GEO 与地理（geography）混淆；**Adobe**（Semrush 所有权下）用 AI SEO/AI Visibility；**Sitecore**（收购 Scrunch）用 AEO；**Peec AI** 自称"AI search analytics"。
- **反方观点（报告必备）**：Forrester 分析师 Nikhil Lai（2025）：AEO/GEO 等新词与 SEO"有显著但非根本性差异"，从业者"夸大差异以在营销技术栈中 carve 出初创公司-sized 的空位"。（维基百科引用）
- **Perplexity 官方**：使用 GEO 一词，但警告供应商夸大其专业度。

### 3.3 标准化/行业协会
- 截至 2026-10，**尚无公认的行业标准和权威协会**；学术侧出现评测标准化尝试，如 arXiv 2610.23541《Humanity's Last Choice: A Common Evaluation Standard for Generative Engine Optimization》（2026-10-16）——学界开始呼吁统一评估标准。
  - https://arxiv.org/abs/2610.23541 （已核验存在）

## 四、方法论框架演变（大致先后）

1. **Cite sources / 统计数据引用**（2023-11，GEO 论文首创）：论文实验发现引用来源、引用统计是可见性提升最显著的策略；关键词堆砌无效甚至有害。
2. **结构化数据 / Schema.org / FAQ 标记**（2024，SEO 圈迁移）：行业普遍建议沿用 schema.org、JSON-LD、FAQPage 等帮助 LLM 理解内容；⚠ 综述类来源：https://www.searchenginejournal.com/?s=generative+engine+optimization
3. **/llms.txt 提案**（2024-09，Answer.AI 的 Jeremy Howard 提出）：网站根目录放置 markdown 文件为 LLM 提供"精炼导读"。**未被 Google 等主流搜索引擎/生成式引擎官方接纳为抓取指令**（Google 的 John Mueller 明确不看好），但被数千家开发者文档站、Mintlify 等文档平台自动生成，Chrome Lighthouse 甚至在 agentic browsing 审计中检查该文件；2026 年发布 v2（追加 .md 页面规范）。已核验：https://llmstxt.org/
4. **品牌提及量 / Mention Share & Citation Share**（2024Q4 起，随 Profound 等工具兴起）：以"AI 答案中的品牌提及份额/引用份额"替代传统排名指标，成为行业核心 KPI；⚠ 代表工具：https://www.profound.com/
5. **平台官方指南化**（2025–2026）：Bing Webmaster Tools 推出 AI 性能报告、Google Search Console 推出 AI Overview 效果报告（维基百科已核验）；Google 2026 指南、Microsoft Advertising 双术语定义。

### 4.1 GEO 学术后续（已核验，arXiv API 检索）
2025–2026 学术产出爆发，代表方向：
- 评测基准：VoteGEO-Bench（选举可见性，2610.21330）、多轮对话场景评测（2609.40069）、提示词语料决定"答案市场"（2609.06811）、统一评测标准（2610.23541）
- 机制研究：地域对 GEO 的影响（2610.24081 Chen & Koudas）、内容/检索/模型知识三因素（2610.15033）、ChatGPT 生产环境引用研究（2610.15382）
- 商业化：GEO 与 GEM 的因果推断营销建模（2609.11915）
- 负外部性：卖家智能体自发"GEO"扭曲工具市场（2610.28454）——说明概念已外溢到 agent 经济。
- 检索命令：`curl -s "https://export.arxiv.org/api/query?search_query=all:%22generative+engine+optimization%22&max_results=15&sortBy=submittedDate&sortOrder=descending"`

## 五、代表性数据/研究结论汇总

| 时间 | 结论 | 来源 |
|---|---|---|
| 2023-11 | GEO 策略最高提升可见性 **40%**；策略效果因领域而异 | https://arxiv.org/abs/2311.09735 |
| 2024-02 | Gartner：2026 年传统搜索量将降 **25%**（因 AI 聊天机器人） | Gartner 新闻稿（URL 见上） |
| 2024-06 | 美国 Google 零点击 **58.5%**（2019 为 56.1%） | https://sparktoro.com/blog/2024-zero-click-study/ |
| 2025-04 | AI Overview 使首位 CTR **降 34.5%** | https://ahrefs.com/blog/ai-overviews-reduce-clicks/ |
| 2025 | AI Overviews 覆盖 20%+ 查询，出现时 CTR 降近 **60%** | 同 SparkToro 2026 更新引用 |
| 2026-06 | 美国 Google 零点击达 **68.01%** | https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ |
| 2026 | 仅 **38%** 的 AI Overview 引用来自自然前 10（去年 76%） | https://ahrefs.com/blog/ai-overview-citations-top-10/ |
| 2026 | GEO 市场规模口径：$1.09B（2026）→ $7–33B（2030s，各家不一） | 见 3.1 各链接 |

## 六、给报告的叙事建议
- 主线：学术命名（2023-11）→ 平台落地（2024 AI Overviews/ChatGPT Search）→ 流量恐慌数据（Gartner + SparkToro + Ahrefs 2024-2025）→ 工具/资本入场（2025 Profound/Sequoia、Adobe、a16z）→ 命名与正当性之争（2025-2026，Google"仍是 SEO" vs 独立品类叙事）→ 2026 评测标准化尝试 + agent 经济外溢。
- 关键张力点：① SEO 延续论 vs 独立行业论（Forrester vs 创业公司）；② llms.txt 社区热 vs 引擎冷；③ 市场规模数字严重不可比——报告应明示口径。
