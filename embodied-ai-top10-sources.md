# 具身智能研究 TOP 10 信息源

> 编制日期：2026年6月4日
> 适用方向：Embodied AI / 人形机器人 / VLA模型 / 灵巧操作 / 仿真平台

---

## 一、学术论文类

### 1️⃣ arXiv（具身智能方向专题）

- **网址**：https://arxiv.org
- **搜索关键词**：`embodied AI` / `VLA` / `robot learning` / `manipulation` / `locomotion` / `world model`
- **入选原因**：具身智能论文首发阵地，几乎所有重要工作先上 arXiv。
- **必读里程碑综述**：
  - Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI（arXiv: 2407.06886）
  - A Survey on Vision-Language-Action Models for Embodied AI（arXiv: 2405.14093）
  - Towards Embodied Agentic AI: LLM/VLM-Driven Robot Autonomy（arXiv: 2508.05294）
  - A Comprehensive Survey on World Models for Embodied AI（arXiv: 2510.16732）

---

### 2️⃣ 中国知网 CNKI（国内论文）

- **网址**：https://www.cnki.net
- **入选原因**：国内具身智能论文的主要阵地。搜索"具身智能""人形机器人""灵巧操作""强化学习""世界模型"等关键词。2025年已上线 CNKI AI 学术研究助手（接入 DeepSeek），支持语义检索。清华、北大、南大、上交等团队的中文综述都在这里首发。
- **国内代表性综述方向**：白辰甲/许华哲/李学龙《大模型驱动的具身智能：发展与挑战》（腾讯新闻刊载）；南京大学《从物理模拟器和世界模型中学习具身智能》万字综述。

---

### 3️⃣ Semantic Scholar（AI 驱动论文检索）

- **网址**：https://www.semanticscholar.org
- **入选原因**：覆盖 2 亿+ 论文，支持语义检索而非纯关键词匹配。提供免费 API，支持文献引用图谱分析，非常适合追踪具身智能领域的知识脉络（如 VLA 模型的演进路线）。

---

## 二、GitHub 开源仓库类

### 4️⃣ LeRobot（Hugging Face 出品）

- **GitHub**：https://github.com/huggingface/lerobot
- **文档**：https://huggingface.co/docs/lerobot
- **入选原因**：具身智能学习的"Hugging Face Hub"。端到端机器人学习开源库，涵盖数据采集 → 数据集存储 → 策略训练 → 硬件部署全链路。LeRobot Hub 已收录 58,000+ 数据集，支持 Unitree G1 等硬件。已发布配套的低成本 3D 打印人形机器人 LeRobot Humanoid。是具身智能入门和研究的首选平台。

---

### 5️⃣ Awesome Embodied AI 系列（论文 + 资源导航）

| 仓库 | 地址 | 说明 |
|------|------|------|
| Embodied-AI-Guide | https://github.com/TianxingChen/Embodied-AI-Guide | Lumina 社区出品，10K+ Stars，最全面的中文具身智能技术指南 |
| Embodied AI Paper List | https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List | 中山大学维护，持续更新的具身智能论文索引 |
| Embodied-AI-Paper-TopConf | https://github.com/Songwxuan/Embodied-AI-Paper-TopConf | 收录顶会（ICLR/NeurIPS/ICML/CoRL/ICRA/IROS）具身论文 |
| Awesome-Embodied-AI | https://github.com/wadeKeith/Awesome-Embodied-AI | VLA 模型、数据集、仿真器、人形机器人全覆盖 |

- **入选原因**：省去漫无目的搜索，直接拿到按主题分类的论文、代码、数据集索引。

---

### 6️⃣ 仿真平台（具身智能的核心基础设施）

| 平台 | 地址 | 亮点 |
|------|------|------|
| NVIDIA Isaac Lab | https://github.com/isaac-sim/IsaacLab | GPU 加速，工业级 RL/IL 训练框架，具身智能研究标配 |
| NVIDIA Isaac Sim | https://developer.nvidia.com/isaac/sim | 高保真物理仿真 + 合成数据生成，支撑从仿真到部署 |
| Genesis | https://github.com/Genesis-Embodied-AI/genesis-world | 新一代通用仿真，GPU 加速 80 倍+，支持多物理场 |
| MuJoCo | https://github.com/google-deepmind/mujoco | DeepMind 出品，机器人动力学仿真的事实标准 |

- **入选原因**：做具身智能研究**必须**有仿真环境。Isaac Lab 是当前主流选择，Genesis 是新兴竞品，MuJoCo 是最基础也最广泛使用的物理引擎。

---

## 三、头部机器人硬件平台 & 数据集类

### 7️⃣ 宇树科技 Unitree（国内人形机器人龙头）

- **GitHub**：https://github.com/unitreerobotics
- **H1 SDK 文档**：https://support.unitree.com/home/en/H1_developer
- **G1 SDK 文档**：https://support.unitree.com/home/en/G1_developer
- **H2 SDK 文档**：https://support.unitree.com/home/en/H2_developer
- **入选原因**：提供 unitree_sdk2 统一 SDK，支持 Go2/B2/H1/G1/H2/R1/A2 全系列机器人。开发者文档完善，覆盖底层运动控制 → 高层技能开发 → 遥操作 → 强化学习全流程。是国内性价比最高的人形机器人开发平台。

---

### 8️⃣ Boston Dynamics Spot SDK

- **开发者文档**：https://dev.bostondynamics.com
- **GitHub**：https://github.com/boston-dynamics/spot-sdk
- **入选原因**：四足机器人领域最成熟的商业 SDK，提供完整的 gRPC API 文档、Python SDK、负载开发指南。可在真实机器人上验证导航、操作、感知等具身智能算法，是学术界和工业界的标准测试平台。

---

### 9️⃣ AgiBot World（智元机器人 · 百万真机数据集）

- **GitHub**：https://github.com/OpenDriveLab/AgiBot-World
- **项目主页**：https://agibot-world.cn
- **入选原因**：全球首个百万级真机数据集，100+ 真实场景、80+ 技能、3000+ 物品种类，覆盖商业/家居/工业/酒店/安防五大领域。2026 版已上线。数据规模是 Google Open X-Embodiment 的 10 倍。智元承诺后续还将开源千万仿真数据和具身基座大模型。

---

### 🔟 Open X-Embodiment（Google DeepMind）

- **项目主页**：https://robotics-transformer-x.github.io
- **GitHub**：https://github.com/google-deepmind/open_x_embodiment
- **入选原因**：Google 牵头，20+ 机构联合发布的跨本体机器人学习数据集，包含 1M+ 真机轨迹、22 种机器人形态、500+ 技能。配套 RT-1-X 和 RT-2-X 模型，是跨实体具身智能学习的基础数据集和基线模型。

---

## 四、补充推荐（值得持续关注）

| 资源 | 地址 | 说明 |
|------|------|------|
| Figure AI | https://www.figure.ai / https://github.com/figurerobotics | 通用人形机器人，已接入 OpenAI，56 个 GitHub 仓库 |
| Open X-Humanoid | https://github.com/Open-X-Humanoid | 开源人形机器人数据集，107K 真机轨迹、479 任务 |
| 上海 AI 实验室 | https://www.shlab.org.cn | 具身智能开源周：导航/操作大模型 + 评测工具 + 数据集 |
| MolarData 数据集汇总 | https://www.molardata.com/article/EmbodiedAIDatasets | 全球高质量具身智能数据集合集 |
| ToddlerBot | https://toddlerbot.github.io | 开源低成本人形机器人平台，30 自由度 |
| 慧思开物 | 北京人形机器人创新中心出品 | 通用具身智能平台，技术架构计划开源 |
| NVIDIA Newton | 2025 年联合发布 | 新一代开源物理引擎，GPU 加速 70 倍，兼容 MuJoCo 和 Isaac Lab |

---

## 五、研究链路总结

本 TOP 10 的覆盖逻辑如下：

```
论文发现（arXiv/CNKI/Semantic Scholar）
    ↓
开源工具 + 仿真（LeRobot/awesome系列/Isaac Lab/MuJoCo）
    ↓
硬件 SDK（Unitree/Boston Dynamics）
    ↓
真实数据集（AgiBot World/Open X-Embodiment）
    ↓
从"看论文 → 写代码 → 跑仿真 → 上真机"完整闭环
```

---

*本文档由 AI 助手自动整理，链接和信息截至 2026 年 6 月。建议定期更新。*
