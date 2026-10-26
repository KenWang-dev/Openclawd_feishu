# GEO（生成式引擎优化）横纵分析报告

> 研究时间：2026-10-27 | 所属领域：搜索营销 / AI 搜索 | 研究对象类型：技术范式与新兴行业

## 一、一句话定义

GEO（Generative Engine Optimization，生成式引擎优化）是一套让品牌内容更容易被 ChatGPT、Perplexity、Google AI Overviews 等生成式搜索引擎**引用、提及和推荐**的方法体系——如果说 SEO 优化的是"排名"，GEO 优化的就是"被 AI 引用的概率"。

## 二、纵向分析：从一篇论文到一个行业

### 2.1 起源：2023 年冬天的一篇论文

GEO 不是从营销圈长出来的，而是从计算机科学圈"空降"下来的。

2023 年 11 月 16 日，普林斯顿大学、佐治亚理工、艾伦人工智能研究所、IIT Delhi 的研究者（一作 Pranjal Aggarwal）在 arXiv 提交了论文《GEO: Generative Engine Optimization》（arXiv:2311.09735），后来进入 KDD 2024。这篇论文做了三件后来定义整个行业的事：

1. **造了"生成式引擎（GE）"这个概念**，把 ChatGPT/Perplexity/New Bing 这类"用生成结果替代链接列表"的搜索形态单独定义；
2. **造了 GEO 这个术语**，并明确区分它与 SEO——SEO 优化的是用户点击，GEO 优化的是内容被生成引擎引用与呈现；
3. **发布了 GEO-bench**（1 万条真实 query），并用实验给出核心结论：在文档已被模型检索进上下文的前提下，**引用来源、加引文、补充统计数据**等策略最高可将可见性指标提升约 40%，而传统关键词堆砌无效；排名靠后的网站受益最大（"均衡器效应"，低排名站点加引用来源可见性 +115%）。

这个 40% 的数字后来被整个行业引用了无数次——但很少人提它的前提：文档已经进入了模型上下文。这个细节是后来 2026 年学界质疑的引线。

值得注意的是，几乎同时，SEO 老兵 Kevin Gray 在 Search Engine Land 上首次用了 "Generative Engine Optimization" 这个短语（2023-08），但只给了定义没给方法。学术圈给了理论，实践圈抢着用了名字——GEO 的行业化，是两条线在 2024 年汇合的结果。

### 2.2 助推器：AI 搜索的爆发（2022-2024）

GEO 之所以成立，前提是"生成式搜索"本身成为主流入口。时间线很紧凑：

- **2022-12**：Perplexity AI 上线（前身 Answer.ai，创始人 Aravind Srinivas 来自 OpenAI）；
- **2023-02**：微软发布 Bing Chat（GPT-4 驱动）；
- **2023-05**：Google I/O 发布 SGE（Search Generative Experience）实验版；
- **2024-02-19**：Gartner 发出著名预测——到 2026 年传统搜索引擎流量将下降 25%；
- **2024-05-14**：Google I/O 宣布 AI Overviews 正式全量发布，这是标志性时刻——AI 摘要不再是实验，而是 Google 默认体验；
- **2024-10-31**：OpenAI 发布 ChatGPT Search。

流量数据的印证随之而来。SparkToro 的零点击研究：美国搜索零点击比例从 2024 年的 60.45% 升到 2026 年的 68.01%。Ahrefs 测算 AI Overviews 使首位自然结果 CTR 下降 34.5%。Adobe 统计 2024 年假日季，AI 驱动的推荐流量同比增长 1300%。

但真正让 GEO 独立于 SEO 成立的，是另一个数字：**AI Overview 的引用来源中，只有 38% 来自自然搜索排名前 10**（Ahrefs，2026 年初口径；一年前这个数字是 76%）。换句话说——你在 Google 排第一，不代表 AI 会引用你。这个断裂，就是 GEO 这个行业的存在理由。

### 2.3 行业化：命名之争、资本入场与标准缺位（2024Q4-2026）

2024 年第四季度起，GEO 从概念变成生意，三条线同时展开。

**命名之战。** GEO、AEO（Answer Engine Optimization）、LLMO（LLM Optimization）、AIO、AI SEO，五个词在 2024-2025 年轮番刷屏。AEO 是 2023 年初 Bing 的聊天助手先带火的，后被 SEO 圈挪用指代 AI 搜索优化；LLMO 是 2023 年底日本和英文 SEO 圈的平行发明；GEO 有学术背书，成了最终幸存的通用词。但至今没有共识——Microsoft Advertising 在 2025 年的官方口径里把 AEO 定义为"面向智能体（Agentic）的优化"、GEO 定义为"面向生成式搜索的优化"，等于官方下场把两个词又拆开了。Forrester 分析师 Nikhil Lai 的批评很直接：这些新词只是"给初创公司划地盘"。Google 官方立场更是釜底抽薪——Search VP 对 CMO 们说"好的 SEO 仍然是 AI 优化所需的一切"（ppc.land 报道），2026 年的官方指南也明确表示不存在专门的"AI SEO"。

**资本入场。** 监测工具在 2024-2025 年密集融资：Profound 种子轮 $3.5M（2024.8）→ A 轮 $20M（Kleiner Perkins，2025.6）→ B 轮 $35M（Sequoia，2025.8），累计 $58.5M；柏林的 Peec AI 2025.11 拿下 €18M A 轮；Scrunch AI 2026 年 $15M A 轮；Brandlight 累计约 $36M。真金白银投进来，行业就算立住了。

**标准缺位。** 没有行业协会、没有统一指标定义、没有权威认证。市场规模测算各家口径相差一个数量级：$886M-$1.09B（2025-26 年，MarketsandMarkets/Analysias Mason 等口径）到 2030 年代 $7B-$33B 的预测，基本属于"自由心证"。2026 年 10 月才出现学界主导的评测标准化尝试（arXiv:2610.23541）。

### 2.4 方法论的演变：从"加引用"到"品牌资产"

GEO 的方法论库是分层沉淀的，顺序很值得玩味：

1. **2023：内容格式层。** 原论文首创：引用来源、引文、统计数据、权威语气。这是所有后续方法的胚胎。
2. **2024：技术结构层。** SEO 从业者把既有工具迁移过来：Schema 结构化数据、FAQ 格式、可抓取性优化。
3. **2024-09：llms.txt 提案。** Jeremy Howard（Answer.AI）提出在网站根目录放一个给 LLM 看的 markdown 索引。有意思的是它的命运：从未被任何主流 AI 引擎官方采纳（Google 的 John Mueller 明言"没有任何 AI 系统在用它"，2026 年被业界比作"meta keywords 还魂"），但被数千个文档站自发部署——Vercel 的 Mintlify 甚至自动生成，Lighthouse 加了审计项。它成了开发者社区的一种"仪式"，一个技术文化的活化石。
4. **2024Q4-2025：品牌资产层。** Profound 这代公司把 KPI 从"排名"换成"引用份额（citation share）"和"提及份额（mention share）"，Ahrefs 的大规模相关性研究（75K 品牌）给足了弹药：品牌 web 提及与 AI 引用的相关性 0.664，是外链（0.218）的 3 倍；YouTube 提及相关性最高（0.737）。Reddit 成为 ChatGPT、Gemini、AI Overviews 全平台第一引用来源，Perplexity 引用 Reddit 高达 46.7%。
5. **2025-2026：平台官方工具层。** Google Search Console 增加 AI 触发查询报告，Profound/Semrush 推出官方级监测，GEO 从"玄学"慢慢走向"可测量"——尽管测量本身仍然问题重重。

### 2.5 2026 年的反噬：半泡沫的真相

2026 年上半年，学界开始算总账。Martinez 的批判综述（arXiv:2607.14035，覆盖 45 项研究）结论残酷：**没有任何 GEO 技术被证明对自然可发现性或下游流量有稳定、跨平台、纵向的因果效应**。SAGEO Arena 的端到端测试（17.1 万文档）显示，只改写正文反而使最终引用率下降 6%；C-SEO Bench（1900 queries）54 个方法-领域组合里只有 3 个显著为正。

同时，引用数据本身剧烈波动：Google AI Mode 每周更换 56% 的引用源，ChatGPT 换 74%——行业里管这叫 "citation drift"。temperature=0 重复运行仍有 9-28% 的决策变化。你在周一测的可见性份额，周五可能就不作数了。

The Verge 讽刺这是"新 SEO 恐慌营销"，Adobe 调查显示 98% 的营销人员对 AI 优化没有清晰路线图。预算先行、方法论滞后——典型的泡沫特征。

但需求侧是真的：AI Overviews 激活率从 2025 年初的 6.5% 涨到 2026 年的约 50%（美国查询）；chatbot 引荐流量从 2024 年初不足百万次/月涨到 2025 年 9 月的 2.3 亿次/月（WSJ）。**需求真实、方法论超前于证据**——这是我对 GEO 行业现状的基本判断，我叫它"半泡沫"。

## 三、横向分析：2026 年的竞争图谱与方法证据链

### 3.1 赛道格局：三层市场，两端挤压

2026 年的 GEO 工具市场已经分化为三层：

**纯监测层（$29-500/月，正在商品化）。** Otterly.AI（奥地利，$29 起，最低门槛）、Peec AI（柏林，€85-95 起，自助式性价比路线）、AthenaHQ（YC W25，ex-Google 搜索工程师创办）。这一层技术门槛低、同质化严重，是价格战的坟场。

**监测+优化建议层（$250-1000/月）。** Scrunch AI（明确从监测转向"代理式 web 优化"）、Goodie AI、AthenaHQ 高端档。卖点从"告诉你可见性多少"升级为"告诉你怎么改"。

**企业 AI 营销平台层（定制报价，年付起）。** Profound 一家独大（$58.5M 融资、Sequoia 背书），已从监测扩展为"agentic 时代营销平台"：对话探索分析、代理执行、内容产出闭环。Brandlight 走咨询型高客单。明星案例：金融科技公司 Ramp 用 Profound 把 AI 可见性从 3.2% 做到 22.2%（7 倍）。

**SEO 大厂的降维打击**是悬在纯玩家头上的剑：Semrush 推出 AI Visibility Toolkit（$99/月/域名）并发布被广泛引用的"AI 最常引用域名"研究；Ahrefs 的 Brand Radar 把 AI 追踪免费含进订阅（数据回溯到 2025 年）；Conductor 发布 AI Search Performance，其 2026 基准报告称 ChatGPT 占网站 AI 引荐流量的 87.4%。

我的判断：纯监测层一年内会被 SEO 巨头和 Profound 两端挤死，胜负手在"监测→执行→归因"的闭环能力和真实 ROI 证明。监测工具还有一个原罪：它们普遍在"含引用的回答"这个有偏分母上计算份额，且不同引擎引用源重叠度极低（仅 11% 域名同时被 ChatGPT 和 Perplexity 引用，6.8 亿引用样本）——跨工具的数字根本不可比。

### 3.2 方法证据链：从强到弱排序

把 2026 年所有可得证据按强度排序，是这样一条链：

**第一梯队（强证据）：**
- **品牌提及与权威引用建设**——Ahrefs 75K 品牌研究相关性 0.664，是最强单一因子；
- **社区平台渗透**——Reddit/YouTube/LinkedIn 是全平台引用头部来源，多伦多大学研究（arXiv:2509.08919）证实 AI Search 系统性偏爱 earned media（第三方权威源）；
- **传统 SEO 基本功**——Cyrus Shepard 对 54 项研究的加权评分中，URL 可访问性（9.5）和搜索排名（9.4）仍是 AI 引用最强的两个预测因子。

**第二梯队（中等证据，有前提）：**
- **内容格式优化**（引用来源、统计、FAQ）——原论文的 +40% 依赖"已入上下文"前提；后续复现研究显示改写有反效果风险。

**第三梯队（弱/证伪）：**
- **llms.txt**——已被基本证伪，Google 官方确认忽略；
- **Schema 结构化数据、知识图谱实体优化**——业界普遍推荐，但缺乏独立因果证据。

**技术层常识**（2026 年的必修课）：GPTBot（训练爬虫）与 OAI-SearchBot（搜索引用爬虫）是分开的开关——封锁 OAI-SearchBot 会让你的网站从 ChatGPT 引用中直接消失。AI 爬虫策略是技术 GEO 的第一道门。

### 3.3 竞品的纵向对比：三条源流，殊途不同归

把主要玩家也放回时间线，会发现三条不同的源流：

- **学术线**（原论文团队 → GEO-bench → 2026 年的批判性复现研究）：先立论、后自我质疑，是行业唯一诚实的镜子；
- **SEO 从业线**（SEO 圈 → AEO/LLMO → llms.txt → Schema 迁移）：把旧手艺换新名字卖，动力最强、证据最弱，泡沫的主要来源；
- **创业线**（Perplexity 生态 → Profound 等监测工具 → 资本化）：从"测量"这个最确定的需求切入，往"执行"这个最不确定的方向扩张。

今天的每个核心优势与劣势都能溯源：GEO 的"科学外衣"来自学术线的论文背书；它的"泡沫体质"来自 SEO 从业线的术语繁殖；它唯一的护城河——数据基础设施——来自创业线的资本投入。而 Google 的官方不承认态度，恰好说明它踩中了 Google 的软肋：AI Overviews 正在瓦解 Google 自己的广告基本盘，GEO 行业某种意义上是"寄生在 Google 转型阵痛上的行业"。

## 四、横纵交汇：适用场景、实操 Skill 集与未来推演

### 4.1 什么业务最值得做 GEO

横轴（场景差异）和纵轴（成熟度）交叉后，适用性分层很清晰：

| 场景 | 策略侧重 | 成熟度 | 值不值得投入 |
|---|---|---|---|
| **B2B SaaS** | 进入"best XX tool"类推荐清单；被 G2/Reddit/评测站引用；建 entity 权威 | 高 | **最值得**。高客单+长决策链，买家的"X vs Y"提问直接决定 shortlist |
| **开发者工具** | 文档可被 LLM 检索（llms.txt、docs 静态化）、GitHub/Stack Overflow 生态渗透 | 中高（工程化程度最高） | **值得**，工程师用户几乎全员 AI 化 |
| **电商** | Product/Offer/Review schema、feed 结构化、Agentic Commerce Protocol（OpenAI 即时结账，2025-09 起） | 中高，随 agentic commerce 快速演进 | 分品类：高决策成本品类值得，冲动型低价零售性价比低 |
| **本地服务** | Google Business Profile + 评论 + NAP 一致性 + Yelp 等本地 citation | 中 | 值得，AI 本地推荐大量依赖 Yelp/GBP；建议 50% 本地 SEO + 50% GEO |
| **专业服务/金融/医疗（YMYL）** | 权威 entity + earned media + 合规内容 | 中 | 值得，AI 是这类"高风险提问"的天然入口 |
| **媒体/内容出版** | 官方授权合作（OpenAI/Perplexity 协议）+ licensing，而非"优化" | 中低 | 最被动，议价权集中在头部，中小 publisher 基本无解 |
| **个人品牌/专家 IP** | Person schema + Reddit/Quora/YouTube/播客渗透 | 早期 | 值得但无成熟工具，靠笨功夫 |

**转化质量的底层逻辑**是 GEO 值得做的核心论据：AI 引流虽然占比小（多数站点 <2% 总流量），但增速惊人（+357% YoY）且质量极高——多个独立口径显示 AI 引流转化率是传统搜索的 4-8 倍（Previsible 4.4×、Neil Patel 口径约 8×、Ziptie 引 ChatGPT 转化 15.9%）。AI 用户带着更深的问题来，被引用的品牌直接进 shortlist。McKinsey 预测 2028 年将有 $750B 美国收入经 AI 搜索转化。

### 4.2 企业落地工作流（五步）

1. **审计**：固定 prompt 集（几十到几百条买家会问的问题）定期跑五大引擎（ChatGPT/Perplexity/Gemini/AI Overviews/Copilot），记录品牌提及与引用；分析 server log 中 AI 爬虫抓取行为；审计 robots.txt（OAI-SearchBot 必须放行）、schema、llms.txt。
2. **内容改造**：机器可扫读 + 可论证——明确结论句、数据、引文、FAQ 结构；补齐 Wikipedia/Wikidata/行业目录 entity；每引擎差异化策略。
3. **技术改造**：允许 AI 爬虫、完整 schema 且与可见内容一致、好页面体验。
4. **分发**：主动经营 Reddit、YouTube、Quora、行业评测站——AI 引用率最高的第三方源，这是当前证据最强的杠杆。
5. **度量**：Citation Share、Mention/Visibility Rate、AI Share of Voice、Sentiment、AI referral 流量转化归因。关键提醒：引用周级波动 56-74%，任何月度数据都必须多轮采样平滑。

### 4.3 市面最佳 Skill 集

**开源/自托管（适合有技术能力的团队）：**
- `amplifying-ai/awesome-generative-engine-optimization`（GitHub）——最全的 GEO 资源总表：指南、工具、论文、案例；
- `firecrawl/llmstxt-generator`、`apify/actor-llmstxt-generator`——llms.txt 生成器；
- GitHub topic `ai-visibility-tracking`：Citratra 等开源 AI 可见性监测平台；
- Agent skill 范式：`orangeo-ai-visibility-skill`（开源 GEO 审计 skill，自动跑首轮可见性审计 + 生成买家 prompt 集）、SEOmator SEO Audit skill（Playwright 渲染 + 251 条规则）。"LLM agent 自动跑 prompt 集 + 抓引用 + 生成内容改造建议"是当前 agent 化的主流形态。

**付费分档：**
- 小预算（$29-100/月）：Otterly.AI（单品牌性价比最高）、Peec AI；
- 企业级：Profound（Ramp 案例）、Similarweb AI Search、Semrush AI Toolkit、AthenaHQ；
- 免费组合：手动 prompt 监测模板（Similarweb 提供免费 KPI 模板）+ Google Search Console AI 触发查询 + server log 分析。零预算也能做审计，只是费人力。

**官方指南（一切方法的锚点）：**
- Google（2025-05 官方博文）：无专门"AI SEO"——独特的人本内容、好页面体验、技术可抓取，三样老东西；注意 Google-Extended（AI 训练爬虫）与 Googlebot（搜索爬虫）是分开的开关；
- OpenAI：GPTBot 与 OAI-SearchBot 分开控制（platform.openai.com/docs/bots）；
- Perplexity：Publishers' Program（2024-07，与 TIME、Der Spiegel 等收入分成）——但仅对头部 publisher 有意义。

**如果只能做三件事**，按证据强度排：① 确保所有 AI 引用爬虫（OAI-SearchBot、PerplexityBot、ClaudeBot）可抓取；② 经营 Reddit/YouTube 等高引用率第三方平台的品牌存在；③ 建立固定 prompt 集的 citation share 月度监测（免费手动即可起步）。

### 4.4 未来推演：三个剧本

**最可能剧本——"并购与收敛"（我判断概率最高）。** 纯监测工具 12-18 个月内被 SEO 大厂收购或挤死，Profound 成为独立巨头，行业指标逐步收敛（学界标准化努力生效），GEO 变成 SEO 服务商的一个标准交付模块。"独立 GEO 行业"不会存在，"GEO 学科"会存在。

**最危险剧本——"引用经济崩塌"。** citation drift 持续恶化 + AI 引用比例下滑（AI Overview 引用 top-10 的比例已从 76% 跌到 38%，趋势未止），导致监测数据彻底不可信、ROI 无法归因，预算退潮，行业重演 2000 年互联网泡沫破灭。WSJ 曝光的"付费种植品牌话术"操纵若被大规模揭发，将触发平台方严厉反制（类似 Google 打击 link farm）。

**最乐观剧本——"代理 commerce 闭环"。** OpenAI 的 Agentic Commerce Protocol 成熟，AI 推荐直接带交易（用户在 ChatGPT 里完成购买），GEO 从"营销可见性"升维成"销售渠道"，监测工具进化为归因与交易优化平台，行业获得独立于 Google 的商业根基。2026 年 OpenAI 转向 merchant-controlled checkout 的动作，是这个剧本的第一块砖。

### 4.5 交汇洞察

把纵横两轴交叠，我的核心判断有三条：

**一、GEO 的本质不是新技术，而是"分发权力的再谈判"。** 过去三十年，品牌与用户之间隔着 Google 这个唯一的守门人，SEO 是向守门人交的税。现在守门人从一个变成五六个，且规则不透明、天天变。GEO 行业贩卖的不是优化技术，而是"在新守门人面前的不确定性管理"。这也解释了为什么方法论证据如此薄弱、预算却照涨不误——企业买的不是效果，是安心。

**二、证据最强的方法恰恰最"古老"。** 引用来源、统计数据、权威第三方提及——这些是 2023 年论文就写下的东西，也是今天唯一扛住复现检验的东西。三年来行业发明的"新武器"（llms.txt、激进改写）几乎全部被证伪或反噬。在 AI 时代，内容营销的真理惊人地保守：**成为值得引用的来源，然后让权威的第三方谈论你**。AI 模型本质上是人类信任结构的压缩包，压缩包不会因为你在网页里塞了 Schema 就改变它对世界的信任。

**三、对中小企业的实操建议：别买工具，先做免费的三件事。** 放行 AI 爬虫（10 分钟）、经营一个 Reddit/YouTube 阵地（长期）、每月手动跑 30 条 prompt 记一次引用（半天）。等这三件事做完、且业务属于 B2B SaaS/开发者工具/高客单服务这类"AI 推荐敏感型"，再考虑 Otterly 或 Peec 这种 $100 级工具。Profound 级平台，留给拿到 B 轮的公司吧。

## 五、信息来源

**学术论文：**
- GEO: Generative Engine Optimization, arXiv:2311.09735（KDD 2024）— https://arxiv.org/abs/2311.09735
- Martinez 批判综述, arXiv:2607.14035（2026-07）— 经 ppc.land 报道
- 多伦多大学 earned media 研究, arXiv:2509.08919
- GEO 评测标准化, arXiv:2610.23541（2026-10）

**行业研究：**
- Ahrefs 75K 品牌 AI 可见性相关性研究 — https://ahrefs.com/blog/ai-brand-visibility-correlations/
- Ahrefs AI Overview 引用 top-10 比例变化 — https://ahrefs.com/blog/ai-overview-citations-top-10/
- Semrush AI 最常引用域名 — https://www.semrush.com/blog/most-cited-domains-ai/
- SparkToro 零点击研究（2024/2026）；Gartner 搜索量预测（2024-02）
- 5WPR State of AI Citations 2026 — https://www.5wpr.com/research/state-of-ai-citations-2026/
- Cyrus Shepard 54 项研究加权评分 — https://ppc.land/23-factors-that-actually-get-your-content-cited-by-ai-search-engines/

**官方文档：**
- Google "Succeeding in AI search" — https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search
- OpenAI 爬虫文档 — https://platform.openai.com/docs/bots
- Perplexity Publishers' Program — https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program
- llms.txt 提案 — https://llmstxt.org

**融资与市场：**
- Profound B 轮 $35M（Sequoia）— https://fortune.com/2025/08/12/ai-search-startup-profound-raises-35-million-series-b-sequoia/
- Peec AI €18M A 轮 — peec.ai 及 SERanking 评测（2026-08）
- The Verge 行业批评 — https://www.theverge.com/tech/900302/ai-seo-industry-google-search-chatgpt-gemini-marketing

**工具与开源：**
- awesome-generative-engine-optimization — https://github.com/amplifying-ai/awesome-generative-engine-optimization
- Profound Ramp 案例 — https://www.tryprofound.com/case-studies/ramp
- Similarweb GEO KPI — https://aisearch.similarweb.com/blog/geo-kpis/

（以上来源访问时间：2026-10-26/27）

**方法论说明**：本报告采用横纵分析法（Horizontal-Vertical Analysis，数字生命卡兹克提出）——纵轴追踪研究对象从诞生到当下的完整历程，横轴在当前时间截面上做系统性横向对比，两轴交汇产出综合判断。
