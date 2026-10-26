# Intel Anomalib 纵向调研纪要（截至 2026-10-24）

> 调研方式：GitHub API（repo/releases/tags/contributors）、arXiv API、仓库 README/CHANGELOG。Brave 搜索 API 当日不可用，本次调研以一手来源为主，未能交叉验证的部分已标注「暂缺」。

## 1. 起源背景

Anomalib 是 Intel 开源的深度学习工业异常检测（Visual Anomaly Detection）库，定位是"面向工业视觉质检的 SOTA 异常检测算法集合 + 实验/部署工具链"。其诞生背景是制造业质检痛点：缺陷样本稀缺、标注昂贵，因此主流研究走"仅用正常样本的无监督/自监督异常检测"路线。

与之相关的核心算法研究脉络（均经 arXiv API 查证）：
- **PaDiM**（Defard et al., CEA List, 2020-11-17, arXiv:2011.08785）：Patch 分布建模，用预训练特征 + 马氏距离做像素级异常定位。
- **DifferNet**（Rudolph et al., 2020-08-28, arXiv:2008.12577）：归一化流做半监督缺陷检测。
- **PatchCore**（Roth et al., NVIDIA 等, 2021-06-15, arXiv:2106.08265, "Towards Total Recall in Industrial Anomaly Detection"）：Memory Bank + Coreset 子采样，MVTec AD 上长期保持 SOTA，是 anomalib 中被引用最多的算法之一。
- **FastFlow**（Yu et al., 京东, 2021-11-15, arXiv:2111.07677）：2D 归一化流做无监督异常检测与定位。
- **EfficientAD**（Batzner et al., 2023-03-25, arXiv:2303.14535）：毫秒级延迟的工业异常检测，作者与 Paul McKING/Intel 圈子相关，anomalib v0.6.0 收录，并单独发布了官方预训练权重 release（2023-05-31）。
- **Anomalib 论文本身**：Akcay, Ameln, Vaidya, Lakshmanan, Ahuja, Genc（Intel 团队），《Anomalib: A Deep Learning Library for Anomaly Detection》，2022-02-16, arXiv:2202.08341。

关于"何时由谁在 Intel 内部启动"：仓库最早提交于 2021 年（GitHub repo created_at 显示 2021-11-02，实际上在此前 Intel 内部已作为 OpenVINO Training Extensions（OTE）生态的一部分孵化，v0.2.0 的 release notes 中提到 "Address compatibility issues with OTE"，可佐证其 OTE 出身）。核心创始团队为 Intel 的 Samet Akcay、Dick Ameln（djdameln）、Ashwin Vaidya、Barath Lakshmanan、Nilesh Ahuja、Utku Genc。与 Landing AI 的关系：无直接证据（「暂缺」）——Landing AI 是吴恩达的独立公司，与 anomalib 无官方隶属关系，仅同属工业视觉质检领域。

## 2. 首次开源与最初形态

- 首个公开组织：**openvinotoolkit**（github.com/openvinotoolkit/anomalib），GitHub 仓库创建时间 **2021-11-02**。
- 最初形态：PyTorch Lightning 之上的算法集合 + OpenVINO 推理导出，内置 DFM、STFPM、PaDiM、PatchCore、FastFlow 等早期算法，服务 Intel 自家的 OpenVINO Training Extensions / Geti 产品线。
- 首个正式 release **v0.2.0（2021-12-14）**；v0.2.x 系列密集发布于 2021-12 至 2022-06。

## 3. 版本迭代时间线（GitHub Releases 实测数据）

- **v0.2.0（2021-12-14）**：首个正式版，TorchMetrics 集成、ONNX 导出节点命名、DFM 修复。
- **v0.3.x（2022-04~10）**：可配置 metrics、OpenVINO 基准测试、CLI 参数体系成型（v0.3.0, 2022-04-25）。
- **v0.4.0（2023-03-01）**：大版本：加入 CFA、RKDE、CSFlow、DRAEM 时代模型；加入视频异常检测（ShanghaiTech、UCSD Ped2、Avenue 数据集）、VisA 数据集、检测任务支持。
- **v0.5.0（2023-05-09）**：src layout 重构、MVTec 3D 数据集、ruff 工具链、视频模型 WinCLIP 方向铺垫。
- **v0.6.0（2023-06-15）**：**EfficientAD 引入**、AI-VAD、OpenVINO API 2.0（弃用 1.0）。
- **v0.7.0（2023-08-29）**：modelAPI 兼容的 OpenVINO 导出（对接 Geti 部署）、仅用正常图像训练支持、EfficientAD 默认参数优化。
- **v1.0.0（2024-02-29）**：首个 1.0 稳定版，API/文档/CI 工程化收口。
- **v1.1.0（2024-05-31）**：MLFlow logger、**Anomalib Pipelines**、`from_config` API（打通 CLI 与 API）、FRE 自编码器模型、**OpenVINO 导出支持压缩与量化（NNCF）**、Discord 社区上线。
- **v1.2.0（2024-10-31）**：PIMO 指标、VLM（视觉-语言模型）异常检测模型、datumaro 标注加载、tiling 集成方法。
- **v2.0.0（2025-03-19；beta 自 2025-01 起）**：**架构大重构**：Dataclasses、PostProcessor、PreProcessor、Metrics 重设计、`AnomalyModule` 改名 `AnomalibModule`、**多 GPU 训练**、**Intel XPU 加速器支持**、AUPIMO 指标正式化。
- **v2.1.0（2025-08-01）**、**v2.2.0（2025-10-08）**：3D-ADAM、BMAD 数据集、PGn/PBn 指标、PatchCore coreset 加速。同期仓库从 openvinotoolkit 迁移至 **open-edge-platform** 组织（Intel 边缘平台统一品牌）。
- **v2.3.0（2026-03-20）→ lib/v2.7.0（2026-10-06）**：命名改为 `lib/vX.Y.Z`（暗示 monorepo/多包结构）。v2.5.0（2026-05-29）加入 **INP-Former、GLASS、AnomalyVFM（零样本）、CFM（跨模态）**；v2.6.0（2026-07-25）加入 **SuperADD（VAND 4.0 冠军方法）**、AutoVI 数据集、Kaputt 数据集切换 HuggingFace；**v2.7.0（2026-10-06，最新）**：新增 **MH-PatchCore、RAD（检索式）、FoundAD（少样本）** 三模型，checkpoint 加载默认 `weights_only=True`（安全加固），移除 legacy ONNX 导出（强制 dynamo），最低 PyTorch 升至 2.10，并完成一批弃用 API 清理。

算法数量：README 自称"最大的公开异常检测算法集合"，从最初约 5-6 种增长到 v2.7 时代的约 20+ 种（含图像/视频/3D/零样本/少样本）。（精确计数「暂缺」，建议后续以 docs 模型列表核实。）

关于 "Anomalib Studio 图形界面 / Gradio"：v1.x 提供 Gradio demo 工具（`anomalib install` 全家桶中的 `tools/gradio`）与 CLI（`anomalib train/test/export`）。名为 "Anomalib Studio" 的独立图形界面在本轮一手来源中**未见记载（暂缺）**，不排除为社区/第三方工具或传闻名称。

## 4. Intel 开源战略逻辑

- **硬件生态飞轮**：anomalib 的核心卖点之一是"大多数模型可导出 OpenVINO IR，在 Intel CPU/GPU/VPU 上加速推理"。2025 年 v2.0 又率先支持 Intel XPU，2026 年 v2.6/v2.7 跟进 ROCm/新 PyTorch。它是 Intel "AI Everywhere / 边缘 AI" 战略中把算法生态绑定到 Intel 硬件的典型抓手。
- **产品线协同**：服务于 OpenVINO Training Extensions（OTE）与 Intel Geti（可视化模型训练平台）——v0.7.0 的 "modelAPI compatible OpenVINO export" 就是为 Geti 部署格式服务的直接证据。
- **MLOps 布局**：内置实验管理、HPO、MLFlow、Pipelines、benchmarking 工具，把工业客户从"算法原型"到"边缘部署"的整条链路留在 Intel 生态内。
- 2025 年仓库迁入 `open-edge-platform` 组织，与 Intel 的 Open Edge Platform 品牌统一，进一步确认其边缘计算布局定位。

## 5. 社区规模里程碑

- **GitHub stars：6,298**（2026-10-24 实测），forks 1,015，open issues 90。
- **贡献者：126 人**（GitHub contributors API，分页合计）。
- 发布节奏：v0.x 时代约每季度一版；v2.x 进入 2026 年后近乎每月发版（2.3.0~2.7.0 共 13 个 release 在 7 个月内），显示活跃的维护与社区贡献（v2.5~2.7 的多个新模型来自外部贡献者：NickF93、josselinonduty、MaticFuc、Collics 等）。
- 社区生态：Discord 服务器（v1.1.0 加入徽章）、Discussions、OpenSSF Best Practices 认证、Trendshift 收录。
- Stars 历史增长曲线「暂缺」（需 Star History 等第三方数据）。

## 6. 与 Intel 其他项目的关系

- **OpenVINO**：最核心的下游。所有模型支持 OpenVINO IR 导出，v1.1.0 起支持 NNCF 量化/压缩，v2.7.0 强制 dynamo ONNX 导出路径。anomalib 实际上是 OpenVINO 生态里"工业质检"场景的参考实现。
- **OpenVINO Training Extensions（OTE）**：anomalib 的出生地/姊妹项目，早期代码需与 OTE 兼容（v0.2.0 PR#24）。
- **Intel Geti**：通过 modelAPI 兼容导出（v0.7.0）承接 Geti 平台的异常检测模型训练能力。
- **Open Edge Platform**：2025 年起新家，anomalib 成为其 AI 库矩阵的一员。

## 信息来源 URL

- https://github.com/open-edge-platform/anomalib （GitHub API: repos/releases/tags/contributors/contents）
- https://api.github.com/repositories/423775360
- https://raw.githubusercontent.com/open-edge-platform/anomalib/main/README.md
- https://raw.githubusercontent.com/open-edge-platform/anomalib/main/CHANGELOG.md
- arXiv: https://arxiv.org/abs/2202.08341 (Anomalib), /abs/2106.08265 (PatchCore), /abs/2011.08785 (PaDiM), /abs/2008.12577 (DifferNet), /abs/2111.07677 (FastFlow), /abs/2303.14535 (EfficientAD)
