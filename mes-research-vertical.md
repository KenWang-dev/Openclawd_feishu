# MES（制造执行系统）纵向信息收集报告

## 1. 起源追溯

### 1.1 MES 概念的诞生

- **MES（Manufacturing Execution System，制造执行系统）** 一词由 **AMR Research** 于 **1990年** 首次提出（部分来源记为1992年）。AMR Research 全称为 Advanced Manufacturing Research，是一家总部位于美国波士顿的制造业研究与咨询公司。  
  - 来源: [grokipedia.com](https://grokipedia.com/page/Manufacturing_execution_system) | [aptean.com](https://www.aptean.com/en-US/insights/blog/what-is-mes) | [facilelogin.com](http://blog.facilelogin.com/2013/07/)

- AMR 于提出 MES 的同时，提出了著名的 **三层制造信息化模型**：计划层（ERP/MRP）— 执行层（MES）— 控制层（SCADA/DCS/PLC），明确了 MES 位于计划管理系统与底层控制系统之间的"中间执行层"地位。  
  - 来源: [cnblogs.com/edisonchou](https://www.cnblogs.com/edisonchou/p/mes_baisc_foundation_chap2.html) | [36dianping.com](https://www.36dianping.com/dianping/5480520123)

- AMR 将 MES 定义为"位于上层的计划管理系统与底层的工业控制之间的面向车间层的管理信息系统"。

- **注**：MES 的前身概念可追溯到 CIM（Computer Integrated Manufacturing，计算机集成制造），该术语在1980年代末由普渡大学首次提出，而 MES 被 AMR 视为 CIM 概念的继承者。  
  - 来源: [plantengineering.com](https://www.plantengineering.com/articles/understanding-the-differences-between-mom-and-mes/)

### 1.2 诞生背景

- **1970年代后期至1980年代**，制造业面临两个关键变化：
  1. **需求端**：客户需求从大批量标准化产品转向多品种、小批量的柔性生产，企业竞争因素发生重大变化。
  2. **技术端**：计算机网络和大型数据库等信息技术持续发展，推动信息系统从局部事后处理向全局实时处理转变。
  
- 当时企业面临的核心痛点是 **"信息断层"**：上层的 ERP/MRP 计划系统和底层的 DCS/PLC 控制系统之间缺乏有效的执行层信息传递，导致：
  - **信息孤岛**：各单一功能系统（设备监控、质量管理、生产统计等）互不相通
  - **计划与执行脱节**：ERP 的生产计划无法有效传递到车间执行
  - **响应迟缓**：无法对生产条件变化做出迅速反应
  
  - 来源: [cnblogs.com/edisonchou](https://www.cnblogs.com/edisonchou/p/mes_baisc_foundation_chap2.html) | [CSDN](https://blog.csdn.net/ylz_yg/article/details/138293861)

### 1.3 早期形态

- **1970年代后半期**：出现了解决单一问题的车间管理系统（专用 Point Solutions），如设备状态监控系统、质量管理系统、生产管理系统等。各系统彼此独立，没有整体解决方案。
- **1980年代**：生产现场各个单一功能开始整合，逐步产生了 **MES 原型**。此时也叫 Shop Floor Control（车间控制），SFC。
- **早期 MES vs 现代 MES**：
  - 早期：功能单一、信息孤岛、事后处理为主、缺乏实时性、仅面向单一车间
  - 现代：集成化、实时化、覆盖全生产过程、与 ERP/SCADA/DCS 无缝连接、支持多工厂多行业
  
  - 来源: [cnblogs.com/edisonchou](https://www.cnblogs.com/edisonchou/p/mes_baisc_foundation_chap2.html) | [numberanalytics.com](https://www.numberanalytics.com/blog/mes-applications-manufacturing-transformation)

### 1.4 MESA International

- **MESA International**（全称 Manufacturing Enterprise Solutions Association International，制造企业解决方案协会）成立于 **1990年代**，总部位于美国，是一个非营利性行业协会。
- **成立背景**：随着 MES 概念的普及和系统复杂度的增加，各厂商对 MES 的定义和理解各不相同，市场出现混乱。MESA 的使命是就 MES 的有效应用提供咨询，解决 MES 的定义和标准化问题。
- **角色**：
  - 制定 MES 功能标准模型（MESA-11、C-MES、Strategic Initiatives Model）
  - 发布行业研究和最佳实践
  - 组织行业会议和教育活动
  - 推动制造运营管理的战略发展
- 核心赞助成员包括西门子、罗克韦尔等知名 MES 厂商。
  - 来源: [mesa.org](https://mesa.org/topics-resources/mesa-model/history-of-the-mesa-models/) | [tulip.co](https://tulip.co/blog/mes-isa-95-mes-11-cmes-namur/)

---

## 2. 发展阶段

### 2.1 1990年代：概念提出与早期发展

| 时间 | 事件 |
|------|------|
| 1990年 | AMR Research 正式提出 MES 概念和三层模型 |
| 1992年 | MESA 开始发布关于 MES 功能的早期研究成果 |
| 1995年 | ISA（国际自动化学会）开始制定 ISA-95 标准 |
| 1996年 | MESA 发布 MESA-11 功能模型的原始版本 |
| 1997年 | MESA 正式定义了 MES 的 **11个核心功能模块**（MESA-11 模型）|

- **关键技术突破**：车间级数据采集技术、局域网技术在工厂中的应用
- **代表性厂商/产品**：早期的点解决方案厂商（CIMx、Intellution、Wonderware 等）
- **行业特点**：MES 首先在流程制造业（如石化、医药）获得成功，因为流程制造业对设备依赖性强、自动化水平高、有大量传感器可实时采集数据
  
  - 来源: [mesa.org](https://mesa.org/topics-resources/mesa-model/history-of-the-mesa-models/) | [control.com](https://control.com/technical-articles/an-introduction-to-manufacturing-execution-systems-mes/)

### 2.2 2000年代：标准化与集成化

| 时间 | 事件 |
|------|------|
| 2000年 | ISA-95.00.01 第一版发布 |
| 2003年 | ISA-95.00.02 发布（对象模型） |
| 2004年 | MESA 发布 C-MES（协作型 MES）模型 |
| 2005年 | ISA-95.00.03 发布（活动模型） |
| 2005年 | VDI 5600 标准发布（德国工程师协会） |
| 2007年 | ISA-95.00.05 发布（B2M 事务） |
| 2008年 | MESA 发布 Strategic Initiatives Model（战略举措模型） |
| 2009年 | Gartner 以6400万美元收购 AMR Research |

- **关键技术突破**：
  - ISA-95 标准的逐步完善，为 ERP-MES 接口标准化奠定基础
  - OPC 技术的发展促进了控制系统与 MES 的集成
  - Web 技术使 MES 界面更加友好、部署更加灵活
  - SOA（面向服务架构）理念引入 MES 设计
  
- **MES 与 ERP 的关系演变**：
  - 2000年代初期：MES 主要作为 ERP 的补充，功能偏重执行层
  - 2000年代后期：ISA-95 标准明确了 MES 与 ERP 的接口和边界，MES 在 Level 3 独立定位
  - MES 开始承担质量、维护、库存等更广泛的运营管理职能
  
- **代表性厂商/产品**：
  - **Siemens**（西门子）：SIMATIC IT（后被整合为 Opcenter）
  - **SAP**：SAP ME / SAP MII
  - **Rockwell**（罗克韦尔）：FactoryTalk
  - **GE Digital**：Proficy
  - **Wonderware**（后被施耐德收购）：InTouch/MES
  
  - 来源: [ISA 官网](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard) | [mesa.org](https://mesa.org/topics-resources/mesa-model/history-of-the-mesa-models/) | [Gartner Wikipedia](https://en.wikipedia.org/wiki/Gartner)

### 2.3 2010年代：工业4.0、物联网与云计算

| 时间 | 事件 |
|------|------|
| 2011年 | 德国提出 "工业4.0"（Industrie 4.0）战略 |
| 2013年 | MES 概念在中国"智能制造"战略中开始获得广泛关注 |
| 2013年 | ISA-95.00.03 更新版发布 |
| 2014年 | 美国推出"工业互联网"战略（GE 主导） |
| 2015年 | 中国发布《中国制造2025》战略规划 |
| 2016年 | 中国发布电子行业标准 SJ/T 11666（MES规范系列） |
| 2018年 | ISA-95.00.04 发布 |
| 2019年 | MESA 发布新一代 Strategic Initiatives Model |

- **关键技术突破**：
  - **工业物联网（IIoT）**：大量传感器和联网设备产生海量实时数据，为 MES 提供更丰富的数据源
  - **云计算**：云端 MES（Cloud MES）概念兴起，降低部署门槛和总拥有成本
  - **大数据分析**：MES 开始集成高级分析能力，从"记录"转向"预测"
  - **数字孪生**：车间数字孪生技术开始与 MES 集成
  - **移动化**：MES 界面从 PC 端扩展到移动端和平板
  
- **代表性产品/公司**：
  - 西门子推出 **Opcenter** 品牌（整合了 SIMATIC IT、Camstar、Preactor 等）
  - SAP 推出 **SAP Digital Manufacturing**
  - **SaaS MES 新势力**出现（如 Tulip、Fourleaf 等）
  
- **行业事件**：
  - 2018年，IDC 报告显示中国 MES 市场规模快速增长，CAGR 超 16%
  - 分析师观察到 MES 正向"应用和微服务"模式转变
  
  - 来源: [cnblogs.com/edisonchou](https://www.cnblogs.com/edisonchou/p/mes_baisc_foundation_chap2.html) | [tulip.co](https://tulip.co/blog/mes-isa-95-mes-11-cmes-namur/) | [symestic.com](https://www.symestic.com/en-us/what-is/mesa-11)

### 2.4 2020年代至今：数字化转型、AI/ML、低代码与云原生

| 时间 | 事件 |
|------|------|
| 2020年 | 疫情推动制造业数字化转型加速 |
| 2021年 | 中国 MES 市场规模达 128 亿元 |
| 2022年 | IIoT 在制造业渗透率大幅提升 |
| 2023年 | GenAI 开始进入工业应用场景 |
| 2024年 | 西门子 Opcenter X 云 SaaS 版本全面推出 |
| 2024年 | GenAI 占工业 AI 项目的 6%（2023年仅1%） |
| 2025年 | ISA-95.00.01 最新版发布（2025版） |
| 2025年 | 边缘 AI 和 Agentic AI 成为工业 AI 新焦点 |

- **核心趋势**：

  **① AI/ML 深度集成**：
  - MES 集成预测性维护（Predictive Maintenance）、质量预测、智能排产
  - GenAI 在 2024 年占工业 AI 项目的 6%（从 2023 年的 1% 快速增长）
  - 边缘 AI 和智能代理 AI 成为 2026 年重点发展方向
  
  **② 云原生与 SaaS 化**：
  - 云端 MES（Cloud MES）大幅降低中小企业部署门槛
  - Siemens Opcenter X、SAP Digital Manufacturing Cloud 等云版本推出
  - Gartner 预测 2025 年 70% 的新企业应用将使用低代码/无代码平台
  
  **③ Composable MES（可组合 MES）**：
  - 打破传统"大一统" MES 架构，采用模块化、微服务方式
  - 每个模块处理独立功能（追踪、质检、维护等），灵活组合
  
  **④ 数字孪生集成**：
  - Siemens Opcenter X Intosite 提供基于云的数字孪生方案
  - 将工厂变成交互式可视化数据驱动体验
  
  **⑤ 低代码/无代码平台**：
  - 低代码平台市场 2024 年超 300 亿美元
  - 制造业企业通过低代码快速定制 MES 工作流
  
  **⑥ 碳排放管理**：
  - 预计 2025 年超过 50% 的大型制造企业 MES 具备碳排放管理功能
  
  - 来源: [Siemens Opcenter](https://blogs.sw.siemens.com/opcenter/) | [iot-analytics.com](https://iot-analytics.com/industrial-ai-market-insights-how-ai-is-transforming-manufacturing/) | [rtinsights.com](https://www.rtinsights.com/report-industrial-ai-poised-for-rapid-growth/) | [Gartner via jitterbit.com](https://www.jitterbit.com/blog/the-future-of-low-code/)

---

## 3. 标准演变

### 3.1 ISA-95 标准

ISA-95 是目前全球最广泛采用的 MES 相关标准，全称 "Enterprise-Control System Integration（企业系统与控制系统集成）"。

| 标准编号 | 名称 | 发布时间 |
|----------|------|----------|
| ISA-95.00.01 | 模型和术语（Models and Terminology） | 1995年（2000/2010/2025修订） |
| ISA-95.00.02 | 对象模型属性（Object Model Attributes） | 2001/2003修订 |
| ISA-95.00.03 | 制造运营管理活动模型（Activity Models of MOM） | 2005/2013修订 |
| ISA-95.00.04 | MOM 对象模型属性（MOM Object Model Attributes） | 2010/2018修订 |
| ISA-95.00.05 | 企业到制造事务（B2M Transactions） | 2007 |

- **开发机构**：ISA（International Society of Automation，国际自动化学会）与 ANSI（美国国家标准学会）
- **核心架构**：基于普渡大学 PERA 模型的 **五层架构**（Level 0-4）：
  - Level 0：物理过程（传感器、执行器）
  - Level 1：智能设备（传感器信号处理）
  - Level 2：控制系统（PLC、DCS、OCS）
  - **Level 3：制造运营管理（MES/MOM）**
  - Level 4：业务计划与物流（ERP）
- **四大运营领域**：生产、质量、维护、库存
- 最新版本：**ANSI/ISA-95.00.01-2025**（2025年8月发布）
  
  - 来源: [ISA 官网](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard) | [ANSI Blog](https://blog.ansi.org/ansi/ansi-isa-95-00-01-2025-enterprise-control-system/) | [symestic.com](https://www.symestic.com/en-us/blog/mes/isa95)

### 3.2 IEC 62264

- IEC 62264 是 ISA-95 的 **国际版（IEC 采纳版）**，由 IEC（国际电工委员会）发布
- ISA-95.00.01 对应 IEC 62264-1（Models and Terminology）
- ISA-95.00.02 对应 IEC 62264-2
- ISA-95.00.03 对应 IEC 62264-3
- 在中国，IEC 62264 被等同采用
  - 来源: [ANSI Webstore](https://webstore.ansi.org/preview-pages/ISA/preview_ANSI+ISA+95.00.01-2010+(IEC+62264-1+Mod).pdf)

### 3.3 MESA 模型

MESA 模型经历了四个主要版本：

| 版本 | 年份 | 名称 | 特点 |
|------|------|------|------|
| V1 | 1992 | MESA Functions | 最早的 MES 功能列表 |
| V2 | 1996/1997 | Context Model / MESA-11 | 定义了 **11个核心功能模块** |
| V3 | 2004 | C-MES（协作型 MES） | 增加供应链优化、资产优化、业务运营协同 |
| V4 | 2008 | Strategic Initiatives Model | 扩展到企业战略层面 |

**MESA-11 核心功能模块**：
1. 工序详细调度（Operations/Detailed Sequencing）
2. 生产单元分配（Dispatching Production Units）
3. 产品追踪与追溯（Product Tracking & Genealogy）
4. 劳动力资源管理（Labor Management）
5. 质量管理（Quality Management）
6. 维护管理（Maintenance Management）
7. 资源分配与状态管理（Resource Allocation & Status）
8. 文档管理（Document Control）
9. 性能分析（Performance Analysis，典型如 OEE）
10. 过程管理（Process Management）
11. 数据采集与获取（Data Collection & Acquisition）

**C-MES（2004）新增关注**：供应链优化、资产优化，MES 作为信息中枢连接采购、CRM、BI、CAD/CAM、PLM、TMS/WMS、PLC/DCS、合规系统等。

**Strategic Initiatives Model（2008）七大战略**：资产绩效管理（APM）、精益制造、产品生命周期管理（PLM）、质量与合规、实时企业、制造绩效指标、投资回报率（ROI）。
  
  - 来源: [mesa.org](https://mesa.org/topics-resources/mesa-model/history-of-the-mesa-models/) | [tulip.co](https://tulip.co/blog/mes-isa-95-mes-11-cmes-namur/) | [control.com](https://control.com/technical-articles/an-introduction-to-manufacturing-execution-systems-mes/) | [symestic.com](https://www.symestic.com/en-us/what-is/mesa-11)

### 3.4 其他标准

- **VDI 5600**：德国工程师协会于 2004 年发布，基于 ISA-95 和 MESA-11，为 MES 在德国制造业提供更具体的定义
- **NAMUR 推荐**：专注于流程工业（化工、制药），基于 ISA-95 做行业特化
  - 来源: [tulip.co](https://tulip.co/blog/mes-isa-95-mes-11-cmes-namur/)

### 3.5 中国标准

**电子行业标准 SJ/T 11666 系列**（2016年发布）：

| 标准编号 | 内容 |
|----------|------|
| SJ/T 11666.1-2016 | MES 规范 第1部分：模型和术语 |
| SJ/T 11666.3-2016 | MES 规范 第3部分：功能构件 |
| SJ/T 11666.7-2016 | MES 规范 第7部分：导入实施指南 |
| SJ/T 11666.11-2016 | MES 规范 第11部分：冶金行业软件功能 |
| SJ/T 11666.12-2016 | MES 规范 第12部分：造船行业软件功能 |
| SJ/T 11666.13-2016 | MES 规范 第13部分：造纸行业软件功能 |

- **SJ/T 11362-2006**：《企业信息化技术规范 制造执行系统(MES)规范》（更早版本）
- 归口单位：中国电子工业标准化技术协会企业信息化标准工作委员会
- 主管部门：工业和信息化部
- 主要起草单位包括：上海宝信软件、石化盈科、中国电子技术标准化研究院等
  
  - 来源: [国家标准信息平台](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=8B1827F140EDBB19E05397BE0A0AB44A) | [upbz.net](https://www.upbz.net/subject/Std79333557.html) | [nssei.org.cn](https://www.nssi.org.cn/nssi/front/114702063.html)

---

## 4. 术语演进

### 4.1 从 MES 到 MOM

- **MOM（Manufacturing Operations Management，制造运营管理）** 概念大约在 **2005年前后** 随 ISA-95 标准的扩展而正式出现。
- 在 ISA-95 Part 3（2005年发布）中，MOM 被明确定义为一个更广义的范畴，包含四个运营域：
  - **Production（生产）**
  - **Quality（质量）**
  - **Maintenance（维护）**
  - **Inventory（库存）**
  
- **关键区别**：
  | 维度 | MES | MOM |
  |------|-----|-----|
  | 定义方式 | 以功能为导向（MESA-11） | 以信息架构为导向（ISA-95） |
  | 覆盖范围 | 车间执行层（Level 3） | Level 3 整体 + 更广泛的运营协同 |
  | 演变方向 | 逐步被 MOM 概念替代/包含 | 作为更全面的战略框架 |
  | 定位 | 系统产品名称 | 管理理念/战略层面概念 |

- **市场现实**：尽管 MESA 和 ISA 在约2008年宣布应"放弃 MES 术语，转向 MOM"，但 15 年后 MES 在制造业 IT 领域仍然被广泛使用。许多软件公司将 MOM 作为营销手段，定位其产品为"最新一代"。实际上，MOM 是 MES 的上层概念，MES 是 MOM 在执行层面的具体实现。
  - 来源: [parsec-corp.com](https://www.parsec-corp.com/blog/mom-vs-mes-manufacturing-execution-systems) | [mpdv.com](https://www.mpdv.com/en/industry-4-0/smart-factory-glossary/manufacturing-operations-management-mom) | [plantengineering.com](https://www.plantengineering.com/articles/understanding-the-differences-between-mom-and-mes/) | [LNS Research](https://blog.lnsresearch.com/bid/116384/manufacturing-operations-management-mom-vs-mes-and-the-winner-is)

### 4.2 与相关概念的边界

| 概念 | 层级 | 功能定位 | 与 MES 的关系 |
|------|------|----------|--------------|
| **SCADA** | Level 1-2 | 数据采集与监控 | MES 的数据源，为 MES 提供实时过程数据 |
| **DCS** | Level 2 | 分布式过程控制 | 同上，偏流程行业 |
| **PLC** | Level 1-2 | 可编程逻辑控制 | 同上，偏离散行业 |
| **WMS** | Level 3/4 | 仓储管理 | MES 的子系统/伙伴系统，MES 管理 WMS 的物料进退 |
| **ERP** | Level 4 | 企业资源计划 | MES 的上层计划系统，ISA-95 定义了两者的接口 |
| **APS** | Level 3/4 | 高级计划排程 | 可作为 MES 的排产模块，也可独立于 MES 在 ERP 层面 |
| **SCM** | Level 4 | 供应链管理 | MES 的上层，通过 MOM 与 SCM 交互 |
| **PLM** | Level 4 | 产品生命周期管理 | MES 的上游，向 MES 传递产品设计/BOM 信息 |

  - 来源: [ISA-95 via Siemens](https://www.siemens.com/en-us/technology/isa-95-framework-layers/) | [tulip.co](https://tulip.co/blog/mes-isa-95-mes-11-cmes-namur/) | [Siemens Opcenter MOM](https://blogs.sw.siemens.com/opcenter/manufacturing-operations-management-mom-harmonized-mes-qms-aps-and-mi/)

---

## 5. 中国市场

### 5.1 引入时间与发展历程

| 阶段 | 时间 | 特征 |
|------|------|------|
| **引进期** | 1980年代-1999年 | 宝钢于1980年代作为改革开放排头兵率先引进 MES，成为中国**第一家应用 MES 的企业**。仅少数大型国企引入 |
| **消化吸收期** | 2000-2010年 | 从拆解研究到市场推广，MES 概念在国内逐步扩散。"十五"期间 MES 主要围绕石化和钢铁两大行业展开 |
| **快速增长期** | 2011-2015年 | 石化 MES 市场走向成熟，应用范围不断扩散。2010年后，中国具备自主知识产权的 MES 产品开始推向市场。仅 2010-2015 年，MES 企业就达到 80 家 |
| **政策驱动期** | 2015-2020年 | 2015年"中国制造2025"战略发布，MES 迎来历史性机遇，成为智能制造的重要推手 |
| **深化发展期** | 2020年至今 | 数字化转型加速，云 MES、SaaS MES、AI 集成 MES 成为新趋势 |

  - 来源: [前瞻产业研究院](https://bg.qianzhan.com/trends/detail/506/230220-efd6504d.html) | [知乎](https://zhuanlan.zhihu.com/p/378098557) | [bill-sj.com](https://bill-sj.com/Blog/Item/AA87CD20BD5A48AC8BC4772455081FF0)

### 5.2 中国本土 MES 厂商

**第一梯队（行业龙头）**：

| 厂商 | 背景 | 核心行业 | 市场地位 |
|------|------|----------|----------|
| **宝信软件**（600845） | 1978年源于宝钢自动化部，2001年上市 | 钢铁/冶金（市占率超60%） | 2021年中国MES市场第三（7.2%），钢铁行业绝对龙头 |
| **中控技术**（688777） | 1999年成立，源于浙大中控 | 流程工业（化工、食品等） | 工业自动化+MES 核心企业 |
| **鼎捷数智**（原鼎捷软件 300378） | 1982年成立（台湾鼎新），深耕制造业40余年 | 离散制造 | 连续三年IDC离散制造MES市占率第一（32%） |
| **石化盈科** | 2002年成立，中石化+香港电讯盈科合资 | 石化/能源化工 | 石化行业MES领导者 |

**第二梯队（快速增长）**：

| 厂商 | 特点 |
|------|------|
| **黑湖科技/黑湖智造** | SaaS MES 新势力，IDC 2023年市场份额第二 |
| **赛意信息**（300687） | 泛ERP服务商，MES 快速增长 |
| **新核云** | SaaS MES 新势力，IDC 2023年市场份额第三 |
| **用友网络/金蝶** | 传统ERP厂商，延伸至 MES 领域 |
| **能科科技** | 仿真+MES一体化方案 |

**国际厂商在华**：

| 厂商 | 市场地位 |
|------|----------|
| **西门子（Siemens）** | 2021年中国MES市场第一（10.9%），但份额从2020年的9.4%下降至2023年的7.5% |
| **SAP** | 2021年第二（7.7%） |
| **罗克韦尔（Rockwell）** | 持续深耕 |

- **2021年市场规模**：128亿元人民币，同比增长16.36%
- **市场集中度**：CR3仅25.8%，CR5仅33.2%，竞争较分散
- **中国MES渗透率**：仍低于 ERP、CAD 等成熟工业软件
- 根据IoT Analytics报告，全球范围内约 **54%** 的中小型工厂仍使用纸笔/表格作为"MES"替代
  
  - 来源: [前瞻产业研究院](https://bg.qianzhan.com/trends/detail/506/230220-efd6504d.html) | [新浪财经](https://t.cj.sina.com.cn/articles/view/5675440730/152485a5a02001woz8) | [secrss.com](https://www.secrss.com/articles/49494) | [siscmag.com](https://siscmag.com/news/show-4665.html) | [腾讯新闻](https://news.qq.com/rain/a/20250117A04ZLP00)

### 5.3 政策推动

| 政策 | 时间 | 内容 |
|------|------|------|
| **《中国制造2025》** | 2015年5月 | 国务院发布，智能制造为主攻方向，MES 作为实现智能制造的重要推手 |
| **《智能制造发展规划（2016-2020年）》** | 2016年 | 明确支持企业引入 MES 系统 |
| **"十四五"规划** | 2021年起 | 持续推动产业数字化发展 |
| **工业互联网相关政策** | 持续 | 推动工厂上云、设备联网，为 MES 提供基础设施 |
| **两化融合政策** | 持续 | 促进信息化与工业化深度融合 |

- 国家及各部委持续出台政策支持 MES 产业发展，重点在于推动智能制造
- 2025年中国MES市场以超18%的年复合增长率快速扩张，领先全球10.8%的增速
  
  - 来源: [前瞻产业研究院](https://bg.qianzhan.com/trends/detail/506/230220-efd6504d.html) | [jiandaoyun.com](https://www.jiandaoyun.com/blog/article/1671788/) | [CIO时代网](https://www.cioage.com/article/567852.html)

---

## 附录：关键时间线总结

```
1970s ── 单一功能车间系统出现（设备监控、质量管理等）
1978 ─── 宝钢引进MES（中国第一家）
1980s ── 各单一功能开始整合，MES原型出现
1990 ─── AMR Research 提出 MES 概念和三层模型
1992 ─── AMR 正式定义 MES
1995 ─── ISA 开始制定 ISA-95 标准
1996/97 ─ MESA 发布 MESA-11 模型（11个核心功能）
2000 ─── ISA-95.00.01 第一版发布
2002 ─── 石化盈科成立（中石化+电讯盈科合资）
2004 ─── MESA 发布 C-MES 模型；VDI 5600 发布
2005 ─── MOM 概念随 ISA-95 Part 3 正式确立
2006 ─── 中国 SJ/T 11362-2006 发布
2008 ─── MESA 发布 Strategic Initiatives Model
2009 ─── Gartner 收购 AMR Research
2010s ── 工业4.0（2011）、工业互联网（2014）、中国制造2025（2015）
2016 ─── 中国 SJ/T 11666 系列标准发布
2020s ── 云MES、AI/ML、Composable MES、低代码、数字孪生
2025 ─── ISA-95.00.01 最新版发布
```

---

*报告生成时间：2026-06-12*
*信息来源：公开网络资料，以一手来源优先（MESA官网、ISA官网、前瞻产业研究院、行业研究机构报告等）*
