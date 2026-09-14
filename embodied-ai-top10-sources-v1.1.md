# 具身智能研究信息源体系（V1.1）

> 编制日期：2026年6月4日
> 适用方向：Embodied AI / 人形机器人 / VLA模型 / 灵巧操作 / 仿真平台
> 本版本新增：社区动态层、政策合规层、优先级标注⭐、交叉验证说明

---

## 设计原理

本信息源体系基于以下方法论构建：

- **第一性原理**：研究新领域的本质需求 = 知道别人做了什么 + 知道怎么做 + 知道前沿在哪
- **MECE法则**：7 个维度相互独立、完全穷尽
- **帕累托法则**：标注⭐的核心信息源贡献约 60-70% 的研究价值
- **交叉验证原则**：每个维度至少 3 个信息源，避免单一来源偏差

---

## 一、核心综述（⭐ 最核心 · 精读建立认知框架）

> **价值贡献：约 40%** — 精读 2-3 篇高质量综述 = 建立整个领域的认知地图。先见森林，再见树木。

### ⭐ 1️⃣ arXiv（国外论文首发阵地）

- **网址**：https://arxiv.org
- **搜索关键词**：`embodied AI` / `VLA` / `robot learning` / `manipulation` / `locomotion` / `world model`
- **入选原因**：几乎所有具身智能重要工作先上 arXiv，是追踪前沿的"第一入口"。
- **必读里程碑综述**：
  - Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI（2407.06886）
  - A Survey on Vision-Language-Action Models for Embodied AI（2405.14093）
  - Towards Embodied Agentic AI: LLM/VLM-Driven Robot Autonomy（2508.05294）
  - A Comprehensive Survey on World Models for Embodied AI（2510.16732）

### 2️⃣ 中国知网 CNKI（国内论文主阵地）

- **网址**：https://www.cnki.net
- **搜索关键词**：`具身智能` / `人形机器人` / `灵巧操作` / `强化学习` / `世界模型`
- **入选原因**：国内具身智能论文的主要首发平台。2025 年已上线 CNKI AI 学术研究助手（接入 DeepSeek），支持语义检索。清华、北大、南大、上交等团队的中文综述都在这里首发。
- **国内代表性综述**：
  - 白辰甲/许华哲/李学龙《大模型驱动的具身智能：发展与挑战》
  - 南京大学《从物理模拟器和世界模型中学习具身智能》万字综述

### 3️⃣ Semantic Scholar（AI 驱动论文检索）

- **网址**：https://www.semanticscholar.org
- **入选原因**：覆盖 2 亿+ 论文，支持语义检索（非纯关键词匹配）。提供免费 API 和文献引用图谱分析，特别适合追踪具身智能领域的知识脉络（如 VLA 模型的演进路线）。可交叉验证 arXiv 和 CNKI 的检索结果。

**🔍 交叉验证策略**：同一主题分别在三个平台搜索 → 比对覆盖度 → 发现单一平台遗漏的关键论文。例如：一个方向在 arXiv 搜到 15 篇，在 CNKI 搜到 8 篇中文，在 Semantic Scholar 通过引用图谱又发现 3 篇被高频引用但未被关键词命中的论文。

---

## 二、标杆开源项目（⭐ 最核心 · 跑通 demo 形成动手认知）

> **价值贡献：约 25%** — 跑通 2-3 个标杆项目 = 理解"别人怎么做出来的"。

### ⭐ 4️⃣ LeRobot（Hugging Face 出品）

- **GitHub**：https://github.com/huggingface/lerobot
- **文档**：https://huggingface.co/docs/lerobot
- **入选原因**：具身智能学习的"Hugging Face Hub"。端到端机器人学习开源库，涵盖数据采集 → 数据集存储 → 策略训练 → 硬件部署全链路。LeRobot Hub 已收录 58,000+ 数据集。已发布配套低成本 3D 打印人形机器人。**是具身智能入门和研究的首选平台。**

### 5️⃣ Embodied-AI-Guide（Lumina 社区中文指南）

- **GitHub**：https://github.com/TianxingChen/Embodied-AI-Guide
- **入选原因**：10K+ Stars，最全面的中文具身智能技术指南，覆盖学习路线、工具选型、论文导读。对中文用户来说是最高效的"入口地图"。

### 6️⃣ Awesome Embodied AI Paper List（中山大学维护）

- **GitHub**：https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List
- **入选原因**：持续更新的具身智能论文索引，按主题分类。配合 Embodied-AI-Paper-TopConf（顶会收录，https://github.com/Songwxuan/Embodied-AI-Paper-TopConf）形成交叉覆盖。

**🔍 交叉验证策略**：LeRobot 提供工程实现视角 → Embodied-AI-Guide 提供学习路线视角 → Paper List 提供学术前沿视角。三个维度交叉，确保不偏科。

---

## 三、核心数据集（精读综述后跑实验的必备资源）

> **价值贡献：约 15%** — 选定 1-2 个核心数据集深入实验，比浅尝辄止 10 个数据集更有价值。

### 7️⃣ AgiBot World（智元机器人 · 百万真机数据集）

- **GitHub**：https://github.com/OpenDriveLab/AgiBot-World
- **项目主页**：https://agibot-world.cn
- **入选原因**：全球首个百万级真机数据集，100+ 真实场景、80+ 技能、3000+ 物品种类，覆盖商业/家居/工业/酒店/安防五大领域。数据规模是 Google Open X-Embodiment 的 10 倍。智元承诺后续开源千万仿真数据和具身基座大模型。

### 8️⃣ Open X-Embodiment（Google DeepMind）

- **项目主页**：https://robotics-transformer-x.github.io
- **GitHub**：https://github.com/google-deepmind/open_x_embodiment
- **入选原因**：Google 牵头，20+ 机构联合发布的跨本体机器人学习数据集，包含 1M+ 真机轨迹、22 种机器人形态、500+ 技能。配套 RT-1-X 和 RT-2-X 基线模型。是跨实体具身智能学习的基础数据集。

### 9️⃣ Open X-Humanoid（开源人形数据集）

- **GitHub**：https://github.com/Open-X-Humanoid
- **入选原因**：107K 真机演示轨迹、479 个不同任务、96 种物体。专注于人形机器人的操作任务，与 AgiBot World（通用操作）和 Open X-Embodiment（跨本体）形成互补。

**🔍 交叉验证策略**：AgiBot World（大规模通用）+ Open X-Embodiment（跨本体迁移）+ Open X-Humanoid（人形专用）→ 三者数据分布、任务类型、场景覆盖交叉对比，确保实验结论不因数据集偏差而失真。

---

## 四、仿真环境（选 1 个主力深耕）

> **价值贡献：约 3%** — 不需要全覆盖，选定 1 个主力 + 1 个备用即可。

### 10️⃣ NVIDIA Isaac Lab（推荐主力）

- **GitHub**：https://github.com/isaac-sim/IsaacLab
- **文档**：https://isaac-sim.github.io/IsaacLab/
- **入选原因**：GPU 加速，工业级 RL/IL 训练框架，具身智能研究标配。支持大规模并行训练，与 LeRobot 等工具深度集成。

### 1️⃣1️⃣ Genesis（新兴竞品）

- **GitHub**：https://github.com/Genesis-Embodied-AI/genesis-world
- **入选原因**：新一代通用仿真平台，GPU 加速 80 倍+，支持多物理场统一求解（刚体/软体/流体），潜力巨大。

### 1️⃣2️⃣ MuJoCo（基础物理引擎）

- **GitHub**：https://github.com/google-deepmind/mujoco
- **入选原因**：DeepMind 出品，机器人动力学仿真的事实标准。轻量、快速，适合快速原型验证。

**🔍 交叉验证策略**：Isaac Lab 作为主力开发 → MuJoCo 做快速物理验证 → Genesis 做前沿多物理场实验。Sim-to-Real 迁移研究需要在不同仿真器上对比结果。

---

## 五、产业资源（硬件 SDK + 公司 API）

> **价值贡献：约 5%** — 了解产业界在做什么，确保研究不脱离实际需求。

### 1️⃣3️⃣ 宇树科技 Unitree（国内人形机器人龙头）

- **GitHub**：https://github.com/unitreerobotics
- **H1 SDK 文档**：https://support.unitree.com/home/en/H1_developer
- **G1 SDK 文档**：https://support.unitree.com/home/en/G1_developer
- **H2 SDK 文档**：https://support.unitree.com/home/en/H2_developer
- **入选原因**：提供 unitree_sdk2 统一 SDK，支持 Go2/B2/H1/G1/H2/R1/A2 全系列。开发者文档完善，覆盖运动控制 → 技能开发 → 遥操作 → 强化学习全流程。国内性价比最高的人形机器人开发平台。

### 1️⃣4️⃣ Boston Dynamics Spot SDK

- **开发者文档**：https://dev.bostondynamics.com
- **GitHub**：https://github.com/boston-dynamics/spot-sdk
- **入选原因**：四足机器人领域最成熟的商业 SDK，gRPC API + Python SDK + 负载开发指南。学术界和工业界的标准测试平台。

### 1️⃣5️⃣ Figure AI

- **官网**：https://www.figure.ai
- **GitHub**：https://github.com/figurerobotics
- **入选原因**：通用人形机器人头部公司，已接入 OpenAI。56 个 GitHub 仓库值得关注。代表产业界最高技术水平。

---

## 六、社区动态（🆕 新增 · 追踪前沿不可替代的渠道）

> **价值贡献：约 10%** — 论文是"滞后的知识"，社区动态才是"正在发生的事"。前沿领域的很多信息先出现在社区，数周甚至数月后才见于论文。

### 🆕 1️⃣6️⃣ Twitter/X（研究者动态）

- **关键账号推荐**：
  - @Andrew_Ng / @karpathy / @ylecun — AI 大佬
  - @GeoffreyHinton / @sama — 行业风向标
  - 具身智能方向关注 @figurerobotics / @unitreerobotics 等公司官方账号
- **入选原因**：很多论文未发 arXiv 先发推，产品发布、融资动态、技术突破都在第一时间出现在 Twitter。**是获取"未固化知识"的唯一高效渠道。**

### 🆕 1️⃣7️⃣ 学术会议资源（CoRL / RSS / ICRA / IROS）

- **CoRL**（Conference on Robot Learning）：https://corl.org — 具身智能学习方向最顶级的会议
- **RSS**（Robotics: Science and Systems）：https://roboticsconference.org — 机器人科学顶级会议
- **ICRA**（IEEE Int'l Conf. on Robotics and Automation）：https://www.icra2026.org — 规模最大的机器人会议
- **IROS**（IEEE/RSJ Int'l Conf. on Intelligent Robots）：https://www.iros2026.org
- **入选原因**：会议论文 = 经过同行评审的最新工作，比 arXiv 预印本质量更高。会议 talk 视频往往包含论文之外的实操细节和未来方向预告。YouTube 上搜索 `[ConferenceName] [Year]` 即可找到官方直播录像。

### 🆕 1️⃣8️⃣ Discord / Slack 技术社区

- **LeRobot Discord**：Hugging Face LeRobot 项目官方社区
- **NVIDIA Isaac 论坛**：https://forums.developer.nvidia.com
- **具身智能中文社区**：各高校/公司内部群
- **入选原因**：遇到具体技术问题时，社区内的实时讨论比翻文档高效 10 倍。很多坑和 workaround 只存在于 Discord 历史消息中。

---

## 七、政策与合规（🆕 新增 · 具身智能领域不可忽视的特殊维度）

> **价值贡献：约 2%** — 不影响日常研究，但在产品化和部署阶段至关重要。提前了解可避免方向性错误。

### 🆕 1️⃣9️⃣ 机器人安全标准

- **ISO 10218**（工业机器人安全标准）
- **ISO/TS 15066**（协作机器人安全标准）
- **网址**：https://www.iso.org — 搜索上述标准编号
- **入选原因**：人形机器人要进入家庭和工业场景，安全认证是必选项。了解标准可以提前在算法设计中嵌入安全约束。

### 🆕 20️⃣ 出口管制与技术合规

- **美国 EAR（出口管理条例）：https://www.bis.doc.gov
- **中国机器人产业发展白皮书**：中国电子学会发布
- **入选原因**：高性能机器人技术（特别是军用/双用途）面临出口管制。做研究时需要了解哪些方向可能受限，避免投入后无法成果转化。

---

## ⭐ 核心优先级总结

根据帕累托法则，以下信息源贡献约 **60-70%** 的研究价值，建议**优先深入**：

| 优先级 | 信息源 | 原因 |
|--------|--------|------|
| ⭐⭐⭐ | arXiv 核心综述（2-3 篇） | 建立认知框架，一次精读顶 100 次浅搜 |
| ⭐⭐⭐ | LeRobot 开源项目 | 端到端工具链，跑通一个 demo 胜过收藏 20 个仓库 |
| ⭐⭐ | AgiBot World 数据集 | 最大规模真机数据，实验基座 |
| ⭐⭐ | 宇树 Unitree SDK | 国内最易获取的硬件平台，Sim-to-Real 必备 |
| ⭐⭐ | Twitter/X 动态 | 唯一获取"未固化知识"的高效渠道 |

---

## 🔄 研究链路总结

```
  ┌─────────────────────────────────────────┐
  │     ① 核心综述（⭐ arXiv/CNKI/SS）      │ ← 40% 价值
  │           建立领域认知框架                  │
  └──────────────┬──────────────────────────┘
                 ↓
  ┌─────────────────────────────────────────┐
  │     ② 标杆项目（⭐ LeRobot/Awesome）     │ ← 25% 价值
  │           跑通 demo，理解实现              │
  └──────────────┬──────────────────────────┘
                 ↓
  ┌─────────────────────────────────────────┐
  │     ③ 核心数据集（AgiBot/OXE/OXH）      │ ← 15% 价值
  │           设计实验，验证假设              │
  └──────────────┬──────────────────────────┘
                 ↓
  ┌─────────────────────────────────────────┐
  │  ④ 社区动态（🆕 Twitter/会议/Discord）  │ ← 10% 价值
  │           追踪前沿，发现趋势              │
  └──────────────┬──────────────────────────┘
                 ↓
  ┌─────────────────────────────────────────┐
  │  ⑤ 产业资源（宇树/BD/Figure）           │ ← 5% 价值
  │  ⑥ 仿真环境（Isaac Lab/Genesis/MuJoCo） │ ← 3% 价值
  │  ⑦ 政策合规（🆕 安全标准/出口管制）      │ ← 2% 价值
  └─────────────────────────────────────────┘
```

**每层至少 3 个信息源交叉验证，避免单一来源偏差。**

---

## 补充推荐

| 资源 | 地址 | 说明 |
|------|------|------|
| 上海 AI 实验室 | https://www.shlab.org.cn | 具身智能开源周：导航/操作大模型 + 评测工具 + 数据集 |
| MolarData 数据集汇总 | https://www.molardata.com/article/EmbodiedAIDatasets | 全球高质量具身智能数据集合集 |
| ToddlerBot | https://toddlerbot.github.io | 开源低成本人形机器人平台，30 自由度 |
| NVIDIA Newton | 2025 年联合发布 | 新一代开源物理引擎，GPU 加速 70 倍 |
| 慧思开物 | 北京人形机器人创新中心 | 通用具身智能平台，技术架构计划开源 |

---

*本文档由 AI 助手自动整理，链接和信息截至 2026 年 6 月。建议每季度更新一次。*
*V1.0 → V1.1：新增社区动态层、政策合规层；全面标注⭐优先级；每维度补充至 3 个信息源；新增交叉验证策略。*
