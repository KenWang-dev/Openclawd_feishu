# Celestica（天弘科技）调研报告

> **调研日期**：2026年6月25日  
> **报告版本**：v1.0

---

## 一、公司基本情况

### 1.1 基本信息

| 项目 | 详情 |
|------|------|
| **全称** | Celestica Inc.（天弘科技） |
| **成立时间** | 1994年（作为IBM加拿大子公司成立），1996年被Onex Corporation收购后独立运营 |
| **总部** | 加拿大安大略省多伦多 |
| **上市信息** | 纽约证券交易所（NYSE: CLS）+ 多伦多证券交易所（TSX: CLS），1998年双重上市 |
| **控股股东** | Onex Corporation（2025年年报披露，Onex已不再是控股股东） |
| **员工规模** | 约29,591人（2025年MacroTrends数据）/ 官网披露"超过27,000人全球员工" |
| **全球布局** | 全球40+制造和设计中心，覆盖美洲、欧洲、亚洲11+国家 |

> 来源：Wikipedia、MacroTrends、Celestica官网

### 1.2 公司定位

Celestica已从**传统EMS（电子制造服务）**成功转型为**高端ODM/JDM（联合设计制造）**模式。目前定位为：
- **全球数据中心基础设施和先进技术解决方案领导者**
- 在ODM模式中为客户提供研发、设计、制造、供应链管理的一站式服务
- 客户在其EMS和ODM能力中均有受益：制造规模化、供应链管理、高可靠性组装

> 来源：Celestica 2025 Annual Report、SEC Filing

### 1.3 主要客户（交换机/网络设备领域）

Celestica不公开披露客户名称，但根据行业分析和财报数据可推断：

| 客户类型 | 推断客户 | 备注 |
|----------|----------|------|
| **超大规模云厂商（Hyperscaler）** | 疑似Microsoft、Google、Meta之一 | 占营收36%（2025全年）/ Q4 2025占36% |
| **超大规模云厂商** | 疑似另一家hyperscaler | 占营收14-15% |
| **网络设备品牌** | 疑似Cisco/Arista之一 | 占营收12% |
| **半导体合作伙伴** | AMD（Helios联合项目）、Broadcom、Marvell、Intel | 技术合作+ODM代工 |

> 注：Celestica财报中仅披露"three customers individually represented 10% or more"，不点名。行业分析师普遍认为第一大客户为Microsoft，因其大规模采用Celestica的800G交换机。

---

## 二、业务结构

### 2.1 两大业务板块

Celestica自2024年起将业务调整为两大报告板块：

#### ① Connectivity & Cloud Solutions（CCS，连接与云解决方案）
- **组成**：通信（Communications）+ 企业（Enterprise，含服务器和存储）
- **2025年Q3数据**：通信占公司总营收61%，企业占15%（来源：Q3 2025 Earnings Presentation）
- **2025全年趋势**：CCS板块营收大幅增长，Q4 2025达$28.6亿（同比+64%），占公司总营收约**80%**

#### ② Advanced Technology Solutions（ATS，先进技术解决方案）
- **组成**：航空航天与国防、工业、医疗科技（HealthTech）、资本设备
- **2025 Q4**：$8.0亿（同比-1%），占公司总营收约**20%**
- **板块利润率**：5.0-5.5%

> 来源：Celestica Q2-Q4 2025 Financial Results、Q1 2026 Financial Results

### 2.2 交换机/网络设备业务详情

#### 产品线
Celestica的交换机产品以**白牌（White Box）**和**开放网络**为核心，主要系列包括：

| 产品系列 | 规格 | 用途 |
|----------|------|------|
| **DS6000系列** | 64端口 1.6TbE（OSFP224），总带宽102.4Tbps | AI数据中心骨干交换，2026年4月开放订购 |
| **DS5000系列** | 800G/400G端口 | AI后端网络交换 |
| **DS3000系列** | 40GbE/100GbE，基于Broadcom Trident III | 数据中心ToR交换 |
| **DS2000系列** | 10GbE/25GbE，基于Broadcom Trident III | 数据中心接入层交换 |

#### 代工的客户类型
1. **超大规模云厂商**：直接供应白牌交换机，运行SONiC或定制NOS
2. **网络设备品牌商**：为Cisco等提供JDM联合设计的交换机硬件
3. **AI芯片厂商合作伙伴**：与Broadcom、AMD、Marvell等合作开发基于其芯片的交换平台

#### Dell'Oro Group市场地位
- 2025年Q1：Celestica在**800G数据中心以太网交换机**市场获得最高市场份额增长
- 累计出货超过**160万个800Gbps端口**（截至2025年Q1）
- 获得2024年Dell'Oro**以太网交换机-AI网络**和**高速网络（≥800G）**两项市场份额领导奖

> 来源：Dell'Oro Group Q1 2025报告、Kavout分析、Celestica官网

### 2.3 主要竞争对手

| 竞争对手 | 总部 | 主要领域 | 与Celestica的竞争关系 |
|----------|------|----------|----------------------|
| **Accton Technology（旭鹏）** | 台湾新竹 | 白牌交换机ODM | **主要直接竞争对手**，Accton+Celestica合计占数据中心白牌交换机约90%市场份额 |
| **Quanta Computer（广达）QCT** | 台湾 | 白牌交换机+服务器 | 在hyperscaler白牌交换机市场直接竞争 |
| **Wistron（纬创）** | 台湾 | 服务器+网络设备 | WiWynn（纬颖，Wistron分拆）在AI服务器领域增长强劲 |
| **Delta（台达）** | 台湾 | 网络设备+电源 | 在白牌交换机市场有份额 |
| **Foxconn（富士康）** | 台湾 | 服务器+网络 | OCP服务器/网络设备竞争 |
| **Flex、Jabil** | 新加坡/美国 | EMS代工 | 在AI服务器机架集成和近岸制造领域竞争 |

> 来源：Valuates市场报告、Verified Market Reports、PortersFiveForce

---

## 三、最新财务数据（2025-2026）

### 3.1 年度财务数据

| 指标 | FY2024 | FY2025 | YoY变化 |
|------|--------|--------|---------|
| **营收** | $96.5亿 | $123.9亿 | **+28%** |
| **GAAP EPS** | $3.61 | $7.16 | **+98%** |
| **调整后EPS（Non-GAAP）** | $3.88 | $6.05 | **+56%** |
| **毛利率（调整后）** | ~10% | ~10.8% | +80bps |
| **调整后营业利润率** | ~6% | ~7.8% | 提升 |

> 来源：Celestica Q4/FY2025 Financial Results（2026年1月28日发布）

### 3.2 季度财务数据

| 季度 | 营收 | 同比 | CCS营收 | ATS营收 | 调整后EPS | 调整后营业利润率 |
|------|------|------|---------|---------|-----------|------------------|
| **Q1 2025** | $26.5亿 | - | - | - | $1.20 | 7.1% |
| **Q2 2025** | $29.3亿（推算） | +21% | $20.7亿 | $8.2亿 | - | 8.3%(CCS) |
| **Q3 2025** | $31.9亿 | +28% | $24.1亿 | $7.8亿 | - | 8.3%(CCS) |
| **Q4 2025** | $36.5亿 | +44% | $28.6亿 | $8.0亿 | $1.89 | 7.7%(CCS) |
| **Q1 2026** | **$40.5亿** | **+53%** | **$32.4亿** | **$8.1亿** | **$2.16** | **8.0%** |

### 3.3 硬件平台解决方案（HPS）营收

HPS是Celestica增长最快的业务子板块（属于CCS）：

| 时期 | HPS营收 | 同比增长 |
|------|---------|---------|
| Q2 2025 | ~$12亿 | +82% |
| Q3 2025 | ~$14亿 | +79% |
| Q4 2025 | ~$14亿 | +72% |
| Q1 2026 | ~$17亿 | +63% |

HPS涵盖800G交换机、AI/ML计算平台等高端产品。

### 3.4 2026全年展望（最新上调）

| 指标 | 2026年展望 | 较前次变化 |
|------|-----------|-----------|
| **营收** | **$190亿** | 上调自$170亿（原$160亿） |
| **调整后EPS** | **$10.15** | 上调自$8.75（原$8.20） |
| **调整后营业利润率** | **8.1%** | 上调自7.8% |
| **自由现金流** | $5.0亿 | 维持不变 |
| **资本支出** | **$10亿** | 扩张性投资 |

> 来源：Celestica Q1 2026 Financial Results（2026年4月27日发布）

### 3.5 股价表现

| 指标 | 数据 |
|------|------|
| **当前股价**（2026年6月24日） | $367.40 |
| **市值** | **约$423亿** |
| **P/E比率** | 42.45 |
| **52周股价范围** | $347.57 - $376.54 |
| **分析师共识评级** | "买入"（Buy） |
| **共识目标价** | ~$365.60 |

> 来源：Robinhood、Yahoo Finance、Kavout

---

## 四、供应链地位

### 4.1 在交换机代工领域的排名

Celestica与Accton（旭鹏）**共同主导**全球数据中心白牌交换机市场，两者合计约占据**90%**的市场份额。Celestica是白牌交换机ODM的Tier 1玩家。

在AI后端以太网交换机细分市场，Dell'Oro Group数据显示Celestica是**市场份额增长最快**的厂商之一，800G端口出货量领先。

> 来源：Valuates Data Center White Box Switches市场报告、Dell'Oro Group

### 4.2 与主要竞争对手对比

| 维度 | Celestica | Accton（旭鹏） | Quanta QCT（广达） |
|------|-----------|---------------|-------------------|
| **总部** | 加拿大多伦多 | 台湾新竹 | 台湾龟山 |
| **业务模式** | EMS+ODM/JDM | ODM | ODM+服务器 |
| **白牌交换机份额** | 与Accton共占90% | 与Celestica共占90% | 较小份额 |
| **800G领先性** | Dell'Oro份额增长第一 | 紧随其后 | 有参与 |
| **1.6T产品** | DS6000已发布 | 有布局 | 有布局 |
| **AI服务器** | 通过JDM参与 | 有限 | WiWynn（纬颖）分拆后领先 |
| **地理布局** | 全球40+据点，北美近岸制造 | 以亚洲为主 | 以亚洲为主 |
| **关键差异化** | Broadcom CPO合作伙伴、AMD Helios联合开发、液冷技术、Fort Worth近岸制造 | Edgecore品牌（子公司） | OCP服务器领先 |

### 4.3 AI服务器/数据中心新动向

#### 关键里程碑

1. **DS6000系列1.6T交换机**（2026年4月）：64端口1.6TbE，102.4Tbps总带宽，采用OSFP224接口，面向AI训练集群，**已开放订购**

2. **CPO（共封装光学）交换机项目**（2026年Q1公布）：获得某hyperscaler客户的设计制造订单，使用1.6Tb交换芯片+共封装光学互连+液冷技术，面向AI scale-out网络

3. **AMD Helios联合项目**（2026年3月宣布）：与AMD战略合作开发rack-scale AI平台，Celestica负责R&D、设计和制造scale-up网络交换机，基于OCP ORW（Open Rack Wide）标准

4. **Fort Worth新工厂**（2026年5月）：投资$8.76亿在德州Fort Worth建立2座制造工厂，创造1,700个就业岗位，战略意义在于**近岸制造**（Near-shoring），满足美国客户对供应链安全的要求

5. **Broadcom深度合作**：Celestica是Broadcom Tomahawk 6（102.4Tbps CPO交换芯片）的早期合作伙伴，在其TH6-Davisson CPO方案的推出中担任关键系统集成角色

6. **液冷技术**：提供混合冷却（液冷+风冷）解决方案，集成到AI基础设施产品线中

> 来源：Celestica官网新闻稿、AMD新闻稿、Community Impact Fort Worth

---

## 五、客户关系深度

### 5.1 客户集中度

Celestica的客户集中度**极高**，是其核心风险之一：

| 时期 | 客户1占比 | 客户2占比 | 客户3占比 | 前10客户合计 |
|------|-----------|-----------|-----------|-------------|
| **2024全年** | - | - | - | 73% |
| **2025全年** | 32% | 14% | 12% | **79%** |
| **Q4 2025** | 36% | 15% | 12% | - |

> 来源：Celestica Q4/FY2025 Financial Results、Trefis分析

### 5.2 Cisco与Celestica的关系

**关于"Cisco是否是最大客户"的分析：**

- **大概率不是最大客户**。行业分析师普遍认为Celestica的第一大客户（占32-36%营收）是一家**超大规模云厂商**（hyperscaler），最可能是**Microsoft**，因其大规模采用Celestica的800G白牌交换机用于AI数据中心
- Cisco确实是Celestica的重要客户之一，但更可能是**第二或第三大客户**（12-15%占比范围）
- Celestica与Cisco的合作模式更偏向**JDM（联合设计制造）**，而非纯EMS代工
- Cisco在2025财年的交换机代工需求增长，但增长更快的是hyperscaler的白牌需求

> 注意：以上为客户身份推断，Celestica从未在公开文件中点名任何客户。

### 5.3 与品牌方的合作模式

Celestica的客户合作模式涵盖**多层级**：

| 合作模式 | 描述 | 典型客户类型 |
|----------|------|-------------|
| **纯EMS代工** | Build-to-print，按客户图纸制造 | 传统OEM客户 |
| **JDM联合设计** | Celestica参与产品设计和工程，与客户共同开发 | Cisco等品牌客户 |
| **ODM自主设计** | Celestica自主设计产品线（如DS系列），客户直接采购或贴牌 | Hyperscaler客户 |
| **技术平台合作** | 与芯片厂商联合开发参考平台 | AMD Helios、Broadcom CPO |
| **端到端解决方案** | 从设计到制造到供应链到售后全流程 | 高端AI基础设施客户 |

> 来源：Celestica 2024/2025 Letter to Shareholders

### 5.4 客户关系风险与机遇

**风险**：
- 客户集中度过高（前3大客户占营收63%+），受制于少数客户的资本开支周期
- Hyperscaler可能自研交换机（如Google的定制网络芯片），长期威胁ODM订单
- 客户议价能力强，压制毛利率空间

**机遇**：
- AI基础设施建设处于超级周期，客户需求可见性延伸至2027年
- 新的技术合作（CPO、1.6T、液冷）加深了与客户的绑定
- 近岸制造（Fort Worth工厂）降低了地缘政治风险，增加了美国客户黏性

---

## 六、综合评估

### 6.1 Celestica的核心竞争力

1. **800G/1.6T交换机的市场领导地位**：Dell'Oro认证的市场份额增长第一
2. **深度技术绑定**：与Broadcom（CPO）、AMD（Helios）的联合开发关系
3. **全球供应链+近岸制造**：40+全球据点+Fort Worth近岸工厂，满足供应链多元化需求
4. **从EMS到ODM/JDM的转型成功**：利润率持续提升，营业利润率从6%向8%迈进
5. **HPS业务爆发增长**：硬件平台解决方案营收从$12亿/季增至$17亿/季

### 6.2 核心风险

1. **客户集中度极高**：前3大客户占63%+营收
2. **毛利率依然偏低**：调整后毛利率~11%，营业利润率~8%，远低于纯软件/芯片公司
3. **估值较高**：P/E 42x，市场已定价大量增长预期
4. **技术迭代风险**：1.6T/CPO等技术路线是否顺利量产存在不确定性
5. **竞争加剧**：Accton、Quanta、WiWynn等在AI网络和服务器领域持续加码

### 6.3 结论

Celestica是**AI数据中心基础设施供应链中不可忽视的关键节点**。它从IBM的EMS子公司成功转型为高端网络交换机ODM领导者，在800G/1.6T白牌交换机市场处于绝对领先地位。2025-2026年的AI资本开支超级周期为其带来了爆发式增长（营收从$96.5亿→$123.9亿→$190亿预测）。

对于电子供应链采购和元器件行业而言，Celestica的动向具有重要意义：
- 其白牌交换机业务增长反映了**品牌客户向ODM转移**的大趋势
- 其与Broadcom/AMD的深度合作预示了**AI网络技术路线的关键方向**
- 其Fort Worth近岸投资反映了**供应链地缘政治化的现实应对**

---

## 参考来源

1. Celestica Q4/FY2025 Financial Results - corporate.celestica.com (2026-01-28)
2. Celestica Q1 2026 Financial Results - corporate.celestica.com (2026-04-27)
3. Celestica Q2/Q3 2025 Financial Results - corporate.celestica.com
4. Celestica Wikipedia - en.wikipedia.org/wiki/Celestica
5. MacroTrends Employee Data - macrotrends.net
6. Robinhood CLS Stock - robinhood.com (2026-06-24)
7. Kavout Analysis - kavout.com "Is Celestica Poised to Dominate the AI Infrastructure Boom"
8. Trefis Customer Concentration Analysis - trefis.com
9. Valuates Data Center White Box Switches Report - valuates.com
10. Dell'Oro Group Q1 2025 Ethernet Switch Report (cited via Kavout)
11. AMD Helios Announcement - amd.com (2026-03-16)
12. Celestica DS6000 Press Release - corporate.celestica.com (2026-04-29)
13. Celestica Fort Worth Expansion - expansionsolutionsmagazine.com (2026-05-19)
14. SEC 2025 Annual Report - sec.gov (2026-02-27)
15. 新浪财经"天弘科技吃下146亿蛋糕" - finance.sina.com.cn (2025-07-07)
16. The Globe and Mail "Celestica's AI Surge" - theglobeandmail.com
17. Wedbush Investor Report - investor.wedbush.com (2026-02-12)
