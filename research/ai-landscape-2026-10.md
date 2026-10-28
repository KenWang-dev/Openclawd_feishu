# AI 大模型赛道横向竞争格局（2026年10月底切面）— 调研笔记

> 用途：Anthropic 深度研究报告"横向分析"部分素材。所有关键事实附来源；未经核实处已标注。

## 0. 头部格局速览（对比表素材）

| 公司 | 估值（2026年10月） | 年化营收 run-rate | 旗舰模型（切面时点） | 路线 |
|---|---|---|---|---|
| Anthropic | $965B（5月 Series H，$65B 融资） | $65B（7月底，CNBC 确认）；5月 $47B；2025底 $9B | Claude Fable 5.1 / Mythos 5.1（9/1）、Opus 5.5（9/22） | 闭源、企业/agent 优先 |
| OpenAI | $852B（3/31 完成 $122B 轮，未证实 $500B 传闻——实际更高） | ~$50B（9月底，Bloomberg）；预计年底 $70B | GPT-6 Astra（9/3）、Sol/Luna（9/22）、Instant（10/7） | 闭源、消费者+广告+企业混合 |
| Google DeepMind | 母公司市值支撑 | 未单独披露 | Gemini 4 Argon（10/13 GA）、3.5 Flash（5/19） | 闭源+价格战+全家桶绑定 |
| xAI | ~$230-250B（1月 $20B Series E；2月被 SpaceX 收购，6月合并上市） | 未披露 | Grok 4.7（9/21，$2/$6） | 闭源+政府/军方合同 |
| Meta (MSL) | — | — | Muse Spark（闭源，Q1 2026 起）、放弃 Llama 开源线 | **由开源转闭源** |
| Mistral | €21B（9月 €3B Series D，三星领投） | 未披露 | 开源权重主权 AI | 欧洲开源+合规牌 |
| 中国阵营 | DeepSeek/智谱/MiniMax/月之暗面等约 $20-75B 区间 | — | GLM 5.2（华为昇腾训练）、Kimi K3（2.8T 最大开源权重）、Qwen 3.8 Max、DeepSeek V4 | 几乎全线开源权重（MIT/Apache） |

来源：sacra.com/c/openai；bloomberg.com/news/articles/2026-10-09（OpenAI $70B）；cnbc.com/2026/08/17（Anthropic $65B）；theaitrack.com/anthropic-funding-round-965-billion-valuation；finance.yahoo.com/news/xai-raises-additional-20-billion；frenchtechjournal.com（Mistral）；newmarketpitch.com/blogs/news/foundation-model-top-startups-valuation

---

## 1. OpenAI

- **营收/估值**：2026-09 年化营收 ~$50B，年底指引 $70B+（Bloomberg, 2026-10-09: https://www.bloomberg.com/news/articles/2026-10-09/openai-expects-70-billion-in-annualized-revenue-by-end-of-2026 ）。$852B 估值（3/31，$122B 轮）（https://sacra.com/c/openai ）。Sacra 估 7 月年化 $40B。⚠️ 任务中"$500B+"传闻偏低——实际 $852B。2026 全年确认收入预计 ~$36B（Fortune/FT 转引）。
- **用户/广告**：ChatGPT 周活 2026-02 达 900M → 9 月 1.2B；ChatGPT Ads 2/9 上线，6 周年化 $100M，600+ 广告主（https://www.digitalapplied.com/blog/chatgpt-ads-100m-revenue-self-serve-april-guide ）。
- **产品线**：GPT-6 Astra（9/3 公开，编程 token 效率领先，比 GPT-5.6 Sol 省 ~70% token；BrowseComp 91.5%、ExploitBench 100%、SRE-Bench 88%；但 AA Intelligence Index 61 分，落后 Claude Fable 5.1 的 66）（https://finance.biggo.com/news/14792e0b 、https://openai.com/index/gpt-6-astra 、https://en.wikipedia.org/wiki/GPT-6 ）。⚠️ 未找到名为 "GPT-6 Terra" 的产品——实际为 Astra/Sol/Luna/Instant 四线，任务前提可能不准确。
- **与微软关系重构**：2026-04-27 新协议：微软仍是主要云伙伴、OpenAI 产品 Azure 优先，但 OpenAI 可上任何云；微软不再向 OpenAI 付营收分成；微软保留 IP 非独占许可至 2032（https://openai.com/index/next-phase-of-microsoft-partnership 、https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership ）。10/27 OpenAI 又扩大与 Oracle 合作（openai.com/index/continuing-microsoft-partnership 页面侧栏可见）。
- **商业化差异 vs Anthropic**：消费者订阅（1.2B 周活）+ 广告 + 企业混合变现；Anthropic 纯 B2B/API/编码工具路线，无广告、无大规模 C 端。

## 2. Google DeepMind / Gemini

- **产品节奏**：Gemini 3.5 Flash（5/19，$1.50/$9，比 3.1 Pro 便宜 25%，coding/agentic benchmark 反超）；Gemini 3.1 Pro（2M 上下文）；⚠️ Gemini 3.5 Pro 多次跳票（据称重训底座）；**Gemini 4 Argon** 9/30 发布、10/13 全球 GA，$2/$10 定价，主打长程 coding/研究/网安（https://aireleasetracker.com/model/google/gemini-4-argon 、https://deepmind.google/models/model-cards/gemini-4-argon 、https://geotoolbox.ai/blog/gemini-pricing ）。
- **价格战**：Google 自称 per-token 价格自 2024 年以来降 98%；2.5 Flash-Lite $0.10/$0.40；GPT-5 系 $1.25/$10 开打价格战（https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026 、https://www.metacto.com/blogs/the-true-cost-of-google-gemini-a-guide-to-api-pricing-and-integration ）。
- **云绑定**：Gemini Enterprise 分层收费（入门 SKU 约 $23-30/用户/月）；Gemini agent（Gemini at Work 2026 发布）；Gemini 4 走 Antigravity/AI Studio/API 全渠道分发。
- **企业 API 份额**：Ramp 2026-08 数据：Anthropic 43.5% > OpenAI 39.7% > xAI 4%；Google 未进前二（https://ramp.com/data/ai-index-august-2026 、https://apito.ai/en/blog/news/anthropic-overtakes-openai-enterprise-ramp-may-2026 ）。

## 3. xAI / Meta / Mistral / 中国阵营

- **xAI**：2026-01 完成 $20B Series E，估值 ~$230B；2026-02 被 SpaceX 收购，6 月合并 IPO（https://www.turingpost.com/p/xai 、https://finance.yahoo.com/news/xai-raises-additional-20-billion-161407195.html ）。Grok 4.7（9/21，$2/$6，综合基准落后 GPT-6 约 34 点 per shattered.io）。政府线：GSA OneGov 合作（每机构 $0.42）、国防部 "Frontier AI" 选型（https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-xai-partner-to-accelerate-federal-ai-adoption-09252025 ）。⚠️"军方用于对伊朗打击"仅见单一来源，未核实。
- **Meta**：Meta Superintelligence Labs（Alexandr Wang 任 Chief AI Officer）**放弃 Llama 开源路线**，转闭源商业模型 Muse Spark；分析师估带来 $4-7B 增量收入（2027）；动因包括 Llama 4 Behemoth 内部受挫与架构暴露顾虑（https://www.remio.ai/post/meta-superintelligence-labs-abandons-llama-for-tighter-control-1 、https://www.digitimes.com/news/a20251211PD206/ 、https://ca.finance.yahoo.com/news/meta-deepens-ai-push-superintelligence-194647169.html ）。
- **Mistral**：9 月 €3B Series D（三星领投），估值 €21B（近乎翻倍）；定位"主权、开源权重、EU AI Act/GDPR 合规"，瞄准欧洲政府与受监管行业（https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier 、https://www.frenchtechjournal.com/mistral-ai-3-billion-funding-21-billion-valuation ）。
- **中国阵营**（几乎全线开源权重，MIT/Apache 为主）：
  - **DeepSeek**：V4 / V4.1 Flash；OpenRouter 文本请求份额第一（24.4%，2026-09 周），token 用量第一（V4.1 Flash 30 天 42.7T）（https://www.usecarly.com/blog/llm-market-share 、https://tokenmaxxing.com/openrouter-rankings ）。
  - **智谱 GLM**：GLM 5.2（~744B，**华为昇腾硬件训练**，数周内登顶 Code Arena/Design Arena）；GLM 5.3 Flash 在 OpenRouter token 量第 2（30 天 50.8T）；GLM-4 Flash 定价低至 $0.10/$0.40（https://a2aprotocol.ai/insights/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash ）。
  - **月之暗面 Kimi**：K3（2.8T，WAIC 上海发布，**史上最大开源权重模型**），$0.28/$18；阿里曾领投 ~$800M（https://blog.prompt20.com/posts/chinese-ai-labs-complete-guide ）。
  - **阿里通义**：Qwen 3.8 Max（2.4T，7/19 预览，自称仅次 Claude Fable），$2/$6。
  - **字节豆包、百度 ERNIE**：走分发/国内企业市场。
  - 结构性信号：OpenRouter 上中国系模型 token 占比从一年前 <2% 升至 ~46%（https://presenc.ai/research/openrouter-model-usage-ratings-2025 ，见 presenc.ai/research/openrouter-model-usage-rankings-2026）。

## 4. 关键对比维度

### 4.1 能力口碑（coding/agent）
- AA Intelligence Index：Claude Opus 5.5 = 57.6（v4.3.2，页面记录最大单日涨幅，超 Fable 5.1 4.3 分）> GPT-6 Astra = 61（另一口径）> Grok 4.7 落后 GPT-6 约 34 点（composite，口径杂，需谨慎）（https://felloai.com/best-ai-models 、https://shattered.io/gemini-4-early-launch-catch-up-openai-anthropic-2026 ）。
- 编码 agent 三强：Claude Code 赢复杂多文件重构/代码质量盲测；Codex CLI 省 ~4x token、便宜；Gemini CLI 长上下文/monorepo 强但被批不稳定（https://wetheflywheel.com/en/comparisons/codex-vs-claude-code-vs-gemini-cli 、https://www.deployhq.com/blog/comparing-claude-code-openai-codex-and-google-gemini-cli ）。
- Anthropic 在 OpenRouter token 份额 ~12.3%，但 Ramp 首次采购 AI 工具的公司中 Anthropic 拿下 73% 支出（vs OpenAI 27%）（https://www.siliconrepublic.com/machines/anthropic-google-broadcom-announce-3-5gw-tpu-deal ）。

### 4.2 定价（价格战烈度）
- 前沿档：Claude（1M 上下文 Opus/Sonnet 4.6 标准价）、GPT-5 $1.25/$10、GPT-6 系激进定价、Gemini 3.5 Flash $1.50/$9、Grok 4.7 $2/$6。
- 中国开源权重把地板打穿：GLM-4 Flash $0.10/$0.40、Doubao Lite $0.20/$0.80。
- Kimi K3 输出 $18/M 为最贵之一（长推理 token 多）。（https://tokenease.io/models 、https://www.optimnow.io/post/open-weight-model-pricing-deepseek-qwen-kimi-glm ）

### 4.3 企业客户
- Anthropic：$1M+ 年化企业客户 4 月翻倍至 1,000+（Bloomberg 转述）；任务中"1900 家"未在本次检索中直接证实，最新公开口径为 1,000+（⚠️ 标注）。7 月 $1M+ 客户数与 $65B run-rate 同步披露（https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html ）。
- OpenAI：4 月报告 200 万 business users；Ramp 企业渗透率 8 月 39.7%，被 Anthropic 43.5% 反超。
- Claude Code：2 月年化 $2.5B+，企业占一半以上；Menlo Ventures 估计 coding 已是 $4B 企业 AI 品类（https://codeconductor.ai/blog/claude-code-anthropic-profitability ）。
- 300K+ 企业用 Claude API；~18.9M C 端 MAU（远小于 OpenAI）（https://www.kristian-larsen.com/info/claude-statistics ）。

### 4.4 算力/资本
- Anthropic：Google TPU 扩至 100 万颗（>1GW，2026 上线，数百亿美元级，2025-10-23 宣布）；2026 新协议：2027 起 via Broadcom 约 3.5GW 下一代 TPU；另有传闻与 Microsoft/Nvidia 合作、$30B Azure 容量采购 + MSFT $5B/NVDA $10B 投资（⚠️ 来自 Facebook 转帖，需主渠道核实——但 Microsoft-Nvidia-Anthropic 合作 CNBC 有报道框架）（https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services 、https://www.anthropic.com/news/google-broadcom-partnership-compute 、https://www.crn.com/news/cloud/2026/broadcom-signs-anthropic-google-tpu-groundbreaking-deals ）
- OpenAI：Nvidia 承诺投资（7 月报道 $600B 框架 → 8 月落地 $105B 担保）、Oracle ~$300B 五年算力采购；Stargate 多数据中心。
- 中国：GLM 5.2 用昇腾训练 = 出口管制下的国产算力验证。

## 5. 行业结构性趋势（2026）

- **Agent 经济/computer use**：三家旗舰全部把 agentic/长程任务作为主打卖点（GPT-6 Astra computer use + hosted shell；Gemini 4 Argon 长程工作；Fable 5.1 定位"小时级"agentic 任务，Terminal-Bench 55.8%）。GPT-6 发布选择以"智能 UI/agent 界面"为叙事而非纯跑分（https://shattered.io/gpt-6-intelligent-ui-chatgpt-rollout-2026 ）。
- **算力金融化 / circular deals**：Nvidia 投资 AI lab → lab 买数据中心 → 数据中心买 Nvidia 芯片；Oracle-OpenAI $300B 循环；Bloomberg 做"循环交易地图"，警示需求不及预期时亏损放大；Nvidia 公开回应"我们看法不同"（https://www.bloomberg.com/graphics/2026-ai-circular-deals 、https://ai-circular-economy.com 、https://phys.org/news/2026-10-paying-circular-money-machine-ai.html 、https://finance.yahoo.com/markets/stocks/articles/nvidia-brushes-off-circular-financing-021004579.html ）。Noah Smith 提供反方"良性循环"论（https://www.noahpinion.blog/p/should-we-worry-about-ais-circular ）。GPU 租赁 SPV/Firmus 案例见 phys.org 文。
- **泡沫争议**：Ramp 8 月 AI Index 自带"Cracks in the AI thesis"标题；Altman 承认部分 AI 创业估值过高；Altman 拒绝"我们是一家	exports 圈钱公司"类质疑（ Reddit r/StockMarket 有转载）。
- **监管**：美国 2026-01 起对华 AI 芯片出口从"自动拒绝"改为"逐案许可"；Q1 强力执法（$252M 非法再出口和解）；3 月起草新一轮芯片管制新规；美国控制全球 ~75% AI 算力 vs 中国 ~15%；欧盟 AI Act 2026-08-02 全面执行，罚则至 €35M 或全球营收 7%（https://www.ces-intelligence.com/analysis/ai-sovereignty-export-controls-2026 、https://www.globaltradeandsanctionslaw.com/reported-draft-rules-signal-new-semiconductor-export-controls-framework ）。
- **开源 vs 闭源分化**：美国闭源三强（OpenAI/Anthropic/Google）+ xAI；Meta 转闭源是标志性事件；开源权重领导权实际已移交给中国阵营（OpenRouter ~46% token），Mistral 打"欧洲主权开源"差异化。

## 6. 开发者真实口碑（代表帖）

- HN "A week of using Codex more than Claude"（217 分）："mid-Aug 2026 codex is good, both cli and desktop, you get lots of usage on any plan"（https://news.ycombinator.com/item?id=49393051 ）
- HN Claude Code on the web：高赞评论"没有人能否认 Claude Code 是最 full-featured、用起来最舒服的 CLI coding agent"（https://news.ycombinator.com/item?id=45647166 ）
- Reddit r/ClaudeCode "Claude Code vs Codex vs Gemini Code Assist"：代表性评论"Gemini is DUMB. Codex 和 Claude 接近，Codex 更高效更便宜"（https://www.reddit.com/r/ClaudeCode/comments/1s709w5/ ）
- 综合口径（wetheflywheel 对比文汇总 Reddit 共识）："Claude Code writes better code, but Codex is 4x cheaper to run" —— Reddit 决定性因素常是限额/成本。
- ⚠️ 未找到切面时点 X/Twitter 上的代表性 threads（tavily 无法直接搜 X），如需可后续用 agent-reach/twitter 渠道补。

## 7. 未找到/需核实清单

1. "GPT-6 Terra" —— 未找到此名；实际产品线为 Astra/Sol/Luna/Instant。
2. Anthropic "1900 家 $1M+ 客户" —— 公开口线为 4 月"翻倍至 1,000+"；1900 可能来自更近的内部口径，未检索到公开来源。
3. Anthropic-Microsoft $30B Azure 交易及 NVDA/MSFT 投资额 —— 仅社交转帖，需 CNBC/官方稿核实。
4. xAI 军事应用细节 —— 单一来源。
5. OpenAI 是否 IPO —— 未来搜索预测站（futuresearch.ai）讨论 2027 IPO 情景，未有确定消息。
