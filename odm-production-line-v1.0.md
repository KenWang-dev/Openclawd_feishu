# 手机ODM产线全流程图谱（V1.0）

> 编制日期：2026年6月4日
> 方法论：第一性原理 × MECE × 端到端分析
> 覆盖范围：NPI → SMT → PCBA测试 → 整机组装 → 整机测试 → 老化终检 → 包装出库 + 支撑体系

---

## 一、第一性原理

**手机 ODM 产线的本质是什么？**

从第一性原理出发：ODM 产线就是把 **"一堆散件"** 变成 **"一台可用的手机"** 的全过程。拆到最底层，每个环节只做三件事：

1. **把东西放对位置**（贴片、组装、装配）
2. **确认放对了**（检测、测试、校准）
3. **让东西能工作**（焊接、烧录、调试）

所有设备、人员、流程，都服务于这三个基本动作。

---

## 二、MECE 七大阶段框架

按时间顺序、从原材料到成品出库，**7 个阶段相互独立、完全穷尽**：

```html
<div class="flow-diagram">

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #667eea, #764ba2);">P0<br>NPI<br>新产品导入</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">📋</span><span class="step-name">DFM分析</span><span class="step-desc">Gerber/BOM<br>可制造性评审</span></div>
    <div class="step"><span class="step-icon">🔧</span><span class="step-name">EVT</span><span class="step-desc">工程验证<br>10-50台</span></div>
    <div class="step"><span class="step-icon">🔬</span><span class="step-name">DVT</span><span class="step-desc">设计验证<br>100-500台</span></div>
    <div class="step"><span class="step-icon">🏭</span><span class="step-name">PVT</span><span class="step-desc">生产验证<br>1000+台</span></div>
    <div class="step"><span class="step-icon">📝</span><span class="step-name">SOP发行</span><span class="step-desc">标准作业<br>工时/人员</span></div>
    <div class="step"><span class="step-icon">✅</span><span class="step-name">量产放行</span><span class="step-desc">良率≥95%<br>直通率达标</span></div>
  </div>
</div>

<div class="arrow-row">
  <div class="arrow-label"></div>
  <div class="arrow-content"><span>▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼</span></div>
</div>

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #f093fb, #f5576c);">P1<br>SMT<br>表面贴装</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">⬆️</span><span class="step-name">上板</span><span class="step-desc">PCB送入<br>产线</span></div>
    <div class="step"><span class="step-icon">🖨️</span><span class="step-name">锡膏印刷</span><span class="step-desc">DEK/MPM<br>印刷机</span></div>
    <div class="step"><span class="step-icon">🔍</span><span class="step-name">SPI</span><span class="step-desc">锡膏<br>厚度检测</span></div>
    <div class="step"><span class="step-icon">🤖</span><span class="step-name">贴片</span><span class="step-desc">高速+泛用<br>多功能机×3-6</span></div>
    <div class="step"><span class="step-icon">📷</span><span class="step-name">炉前AOI</span><span class="step-desc">贴装<br>质量检测</span></div>
    <div class="step"><span class="step-icon">🔥</span><span class="step-name">回流焊</span><span class="step-desc">10-12温区<br>回流炉</span></div>
    <div class="step"><span class="step-icon">📷</span><span class="step-name">炉后AOI</span><span class="step-desc">焊接<br>质量检测</span></div>
    <div class="step"><span class="step-icon">☢️</span><span class="step-name">X-Ray</span><span class="step-desc">BGA<br>焊点检测</span></div>
    <div class="step"><span class="step-icon">⬇️</span><span class="step-name">下板</span><span class="step-desc">PCBA<br>出线</span></div>
  </div>
</div>

<div class="arrow-row">
  <div class="arrow-label"></div>
  <div class="arrow-content"><span>▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼</span></div>
</div>

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #4facfe, #00f2fe);">P2<br>PCBA测试<br>与烧录</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">🔌</span><span class="step-name">ICT/FCT</span><span class="step-desc">开短路/阻抗<br>电压测试</span></div>
    <div class="step"><span class="step-icon">💾</span><span class="step-name">软件烧录</span><span class="step-desc">Bootloader<br>固件/IMEI</span></div>
    <div class="step"><span class="step-name">RF校准</span><span class="step-desc">WiFi/BT/GPS<br>射频参数</span></div>
    <div class="step"><span class="step-icon">👁️</span><span class="step-name">PCBA目检</span><span class="step-desc">显微镜<br>焊点外观</span></div>
  </div>
</div>

<div class="arrow-row">
  <div class="arrow-label"></div>
  <div class="arrow-content"><span>▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼</span></div>
</div>

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #43e97b, #38f9d7);">P3<br>整机<br>组装</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">📱</span><span class="step-name">屏幕贴合</span><span class="step-desc">OCA贴合机</span></div>
    <div class="step"><span class="step-icon">📐</span><span class="step-name">主板入壳</span><span class="step-desc">压合治具</span></div>
    <div class="step"><span class="step-name">电池安装</span><span class="step-desc">FPC连接</span></div>
    <div class="step"><span class="step-icon">📷</span><span class="step-name">摄像头/副板</span><span class="step-desc">螺丝锁附</span></div>
    <div class="step"><span class="step-name">屏幕合壳</span><span class="step-desc">合壳机</span></div>
    <div class="step"><span class="step-name">打胶</span><span class="step-desc">密封胶</span></div>
    <div class="step"><span class="step-name">声学/按键</span><span class="step-desc">扬声器/麦克风</span></div>
    <div class="step"><span class="step-icon">🔩</span><span class="step-name">锁螺丝</span><span class="step-desc">自动螺丝机</span></div>
  </div>
</div>

<div class="arrow-row">
  <div class="arrow-label"></div>
  <div class="arrow-content"><span>▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼</span></div>
</div>

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #fa709a, #fee140);">P4<br>整机测试<br>与校准</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">📡</span><span class="step-name">RF耦合测试</span><span class="step-desc">天线效率<br>SAR测试</span></div>
    <div class="step"><span class="step-name">校准</span><span class="step-desc">RF/WiFi<br>BT/GPS</span></div>
    <div class="step"><span class="step-icon">🧪</span><span class="step-name">综合测试MMI</span><span class="step-desc">屏幕/摄像头<br>按键/传感器</span></div>
    <div class="step"><span class="step-name">电流测试</span><span class="step-desc">待机/通话<br>充电电流</span></div>
    <div class="step"><span class="step-name">声学测试</span><span class="step-desc">听筒/喇叭<br>音频自动测</span></div>
  </div>
</div>

<div class="arrow-row">
  <div class="arrow-label"></div>
  <div class="arrow-content"><span>▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼</span></div>
</div>

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #a18cd1, #fbc2eb);">P5<br>老化<br>与终检</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">🌡️</span><span class="step-name">高温老化</span><span class="step-desc">40-55°C<br>4-8小时</span></div>
    <div class="step"><span class="step-icon">👁️</span><span class="step-name">外观全检</span><span class="step-desc">划痕/变形<br>缝隙/涂胶</span></div>
    <div class="step"><span class="step-name">功能抽检</span><span class="step-desc">AQL抽检</span></div>
    <div class="step"><span class="step-icon">🏷️</span><span class="step-name">IMEI关联</span><span class="step-desc">MES追溯</span></div>
  </div>
</div>

<div class="arrow-row">
  <div class="arrow-label"></div>
  <div class="arrow-content"><span>▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼</span></div>
</div>

<div class="phase">
  <div class="phase-label" style="background: linear-gradient(135deg, #ffecd2, #fcb69f);">P6<br>包装<br>与出库</div>
  <div class="phase-content">
    <div class="step"><span class="step-icon">📦</span><span class="step-name">配件装盒</span><span class="step-desc">充电器/数据线<br>说明书/耳机</span></div>
    <div class="step"><span class="step-name">封装</span><span class="step-desc">热缩膜<br>封盒</span></div>
    <div class="step"><span class="step-name">贴外标</span><span class="step-desc">IMEI标签<br>外箱标签</span></div>
    <div class="step"><span class="step-icon">⚖️</span><span class="step-name">称重检测</span><span class="step-desc">配件<br>齐全性</span></div>
    <div class="step"><span class="step-icon">✅</span><span class="step-name">OQC出货</span><span class="step-desc">AQL抽检<br>出货品质</span></div>
    <div class="step"><span class="step-icon">🚚</span><span class="step-name">入库发货</span><span class="step-desc">仓储<br>按单配货</span></div>
  </div>
</div>

</div>
```

---

## 三、各阶段详情

### Phase 0: NPI 新产品导入（量产前准备）

> **本质**：在正式量产前，验证"能不能造、怎么造、造得好不好"。

| 步骤 | 内容 | 关键人员 | 关键工具 |
|------|------|---------|---------|
| DFM 分析 | 审核客户设计文件（Gerber/BOM/结构图），评估可制造性 | NPI 工程师 | Mentor Valor / CAM350 |
| EVT（工程验证） | 首批 10-50 台手工/半自动组装，验证电路和结构 | PE/ME 工程师 + 操作员 | 手工台 + 基础测试设备 |
| DVT（设计验证） | 100-500 台试产，验证工艺稳定性和 BOM 完整性 | NPI 项目经理 + 全工程团队 | 试产线（小规模） |
| PVT（生产验证） | 1000+ 台量产模拟，验证产线节拍、良率、直通率 | IE 工程师 + 产线主管 | 正式产线 |
| SOP 发行 | 确定标准作业指导书、工时、人员配置 | IE + PE 工程师 | MES 系统 |
| 量产放行 | 良率 ≥ 95%、直通率达标、ECN 关闭 | 质量总监 + 客户确认 | 质量报告 |

**关键人员**：NPI 项目经理（1人统筹）、PE/ME 工程师（3-5人）、IE 工程师（1-2人）、SQE（1-2人）
**配置**：8-12 人（项目制，非常驻）

---

### Phase 1: SMT 表面贴装（PCB → PCBA）

> **本质**：把几千个电子元件精确贴到 PCB 上，通过高温焊接固定。
> **自动化程度：⭐⭐⭐⭐⭐ 最高**
> **设备投资：1500-3000 万/线**

| 工序 | 核心设备 | 功能 | 人员配置 |
|------|---------|------|---------|
| PCB 上板 | 上板机/上下板机 | 自动将 PCB 送入产线 | 自动化（1人监控多线） |
| 锡膏印刷 | 锡膏印刷机（DEK/MPM） | 将锡膏精确印刷到 PCB 焊盘 | SMT 操作员（1人/线） |
| 印刷检测 | SPI（Solder Paste Inspection） | 检测锡膏厚度、偏移、漏印 | 自动化（IPQC 抽检） |
| 元件贴装 | 高速贴片机 + 泛用贴片机 + 多功能贴片机 | 将元件贴到 PCB 上 | 技术员（调机）/ 操作员（上料换料） |
| 炉前检测 | AOI（炉前） | 检测贴装偏移、缺件、翻件 | 自动化 |
| 回流焊接 | 回流炉（10-12 温区） | 高温熔化锡膏，冷却固定 | 自动化（技术员监控温度曲线） |
| 炉后检测 | AOI（炉后） | 检测连锡、空焊、立碑等 | 自动化 + 维修员返修 |
| X 光检测 | X-Ray / AXI | 检测 BGA/POP 不可见焊点 | 自动化（IPQC 判读） |
| PCB 下板 | 下板机/分板机 | PCBA 从连板分离 | 自动化 |

**一条 SMT 线人员配置（单班）：7-11 人**
- SMT 技术员 1-2人 | 操作员 3-5人 | 维修员 1-2人 | IPQC 1人 | 组长 1人

---

### Phase 2: PCBA 测试与烧录（裸板验证）

> **本质**：PCBA 还没装进外壳前，验证电路功能是否正常。
> **自动化程度：⭐⭐⭐⭐**
> **设备投资：300-800 万**

| 工序 | 核心设备/工具 | 功能 | 人员 |
|------|-------------|------|------|
| ICT/FCT | ICT 治具 + 测试仪 | 开短路、阻抗、电压测试 | 测试技术员 + 操作员 |
| 软件烧录 | 烧录台/烧录夹具 | 写入 bootloader、固件、IMEI | 烧录操作员（1-2人）|
| RF 校准（裸板）| 屏蔽箱 + CMU200/综测仪 | 校准 WiFi/BT/GPS 射频参数 | RF 技术员 |
| PCBA 目检 | 放大镜/显微镜 | 焊点、元件外观 | 目检员（1-2人）|

**人员配置：4-6 人/线**

---

### Phase 3: 整机组装（PCBA + 外壳 + 屏幕 + 电池 → 手机）

> **本质**：**人力最密集的环节**，自动化改造难度最大。把"裸板"变成"手机"。
> **自动化程度：⭐⭐ 中等**
> **设备投资：200-500 万**

| 工序 | 核心设备/工具 | 功能 | 人员 |
|------|-------------|------|------|
| 屏幕贴合 | 贴合机/OCA 贴合机 | 触摸屏+显示模组+OCA胶贴合 | 贴合操作员（1-2人）|
| 主板入壳 | 半自动压合治具 | PCBA 装入中框/后壳 | 组装操作员（1-2人）|
| 电池安装 | 人工/半自动 | 安装电池 + 连接 FPC | 组装操作员（1人）|
| 副板/摄像头安装 | 人工 + 螺丝锁附 | 副板、摄像头模组、天线 | 组装操作员（2-3人）|
| 屏幕合壳 | 合壳机/人工 | 屏幕模组与中框压合 | 组装操作员（1-2人）|
| 打胶/点胶 | 点胶机 | 屏幕边缘密封胶 | 点胶操作员（1人）|
| 声学器件安装 | 人工 | 扬声器、麦克风、听筒 | 组装操作员（1人）|
| 侧键/SIM卡槽 | 人工 | 音量键、电源键、SIM卡托 | 组装操作员（1人）|
| 螺丝锁附 | 自动螺丝机（部分工站） | 固定各模块 | 组装操作员（1人）|

**人员配置：10-15 人/线（人力最密集环节）**

---

### Phase 4: 整机测试与校准

> **本质**：手机装好了，验证"能不能正常用"。
> **自动化程度：⭐⭐⭐⭐**
> **设备投资：500-1000 万**

| 工序 | 核心设备 | 功能 | 人员 |
|------|---------|------|------|
| RF 耦合测试 | 屏蔽箱 + 综测仪 + 耦合天线 | 天线效率、SAR | RF 测试操作员 |
| 校准 | 校准治具 + 屏蔽箱 | RF/WiFi/BT/GPS 参数 | 校准操作员 |
| 综合测试（MMI）| 综测工站 + 测试软件 | 屏幕/摄像头/按键/传感器/WiFi/BT/通话/充电全检 | 综测操作员（1-2人/工站）|
| 电流测试 | 电流测试治具 | 待机/通话/充电电流 | 测试操作员 |
| 声学测试 | 声学测试箱 | 听筒/喇叭自动化音频测试 | 自动化 |

**人员配置：6-10 人/线**

---

### Phase 5: 老化与终检（可靠性 + 外观）

> **本质**：量产前最后把关，防止"刚用就坏"或"到手有瑕疵"的手机流出。
> **自动化程度：⭐⭐⭐**
> **设备投资：100-300 万（老化房）**

| 工序 | 核心设备 | 功能 | 人员 |
|------|---------|------|------|
| 高温老化 | 老化房/老化架（40-55°C）| 整机 4-8 小时老化 | 自动化（OQC 监控抽检）|
| 外观全检 | 人工 + 光源检测台 | 屏幕划痕、外壳变形、缝隙、涂胶不均 | 外观检验员（5-8人/线）|
| 功能抽检 | 抽检工站 | AQL 抽检整机功能 | OQC 检验员（1-2人）|
| IMEI/条码关联 | 条码扫描枪 + MES | IMEI 与生产记录关联 | 包装操作员 |

**人员配置：7-11 人/线**

---

### Phase 6: 包装与出库

> **本质**：把合格成品安全送到客户手中。
> **自动化程度：⭐⭐⭐**
> **设备投资：100-200 万**

| 工序 | 核心设备 | 功能 | 人员 |
|------|-------------|------|------|
| 配件装盒 | 人工 | 手机+充电器+数据线+说明书+耳机→包装盒 | 包装操作员（3-5人）|
| 封装 | 自动封盒机/人工 | 热缩膜封盒 | 1人 |
| 贴外标 | 标签打印机+人工 | IMEI 标签、外箱标签 | 1人 |
| 称重检测 | 重量检测机 | 配件齐全性验证 | 自动化 |
| OQC 抽检出货 | — | AQL 0.65/1.5 抽检出货品质 | OQC（1人）|
| 入库/发货 | AGV/叉车 + 仓储系统 | 入库、按订单配货、发货 | 仓储人员（2-3人）|

**人员配置：7-10 人/线**

---

## 四、全景数据总览

### 4.1 人员配置汇总

```html
<div class="staff-bar">
<h3>各阶段单线单班人员配置（人）</h3>
<div class="staff-row">
  <div class="bar-label">P3 整机组装</div>
  <div class="bar-track"><div class="bar-fill" style="width:75%;background:linear-gradient(90deg,#43e97b,#38f9d7);">10-15</div></div>
  <div class="bar-value">最多</div>
</div>
<div class="staff-row">
  <div class="bar-label">P5 老化终检</div>
  <div class="bar-track"><div class="bar-fill" style="width:55%;background:linear-gradient(90deg,#a18cd1,#fbc2eb);">7-11</div></div>
  <div class="bar-value"></div>
</div>
<div class="staff-row">
  <div class="bar-label">P6 包装出库</div>
  <div class="bar-track"><div class="bar-fill" style="width:50%;background:linear-gradient(90deg,#ffecd2,#fcb69f);">7-10</div></div>
  <div class="bar-value"></div>
</div>
<div class="staff-row">
  <div class="bar-label">P1 SMT</div>
  <div class="bar-track"><div class="bar-fill" style="width:50%;background:linear-gradient(90deg,#f093fb,#f5576c);">7-11</div></div>
  <div class="bar-value"></div>
</div>
<div class="staff-row">
  <div class="bar-label">P4 整机测试</div>
  <div class="bar-track"><div class="bar-fill" style="width:45%;background:linear-gradient(90deg,#fa709a,#fee140);">6-10</div></div>
  <div class="bar-value"></div>
</div>
<div class="staff-row">
  <div class="bar-label">P2 PCBA测试</div>
  <div class="bar-track"><div class="bar-fill" style="width:30%;background:linear-gradient(90deg,#4facfe,#00f2fe);">4-6</div></div>
  <div class="bar-value"></div>
</div>
</div>
```

### 4.2 设备投资与自动化程度

| 阶段 | 单线单班人数 | 自动化程度 | 设备投资/线 | 投资等级 |
|------|------------|-----------|------------|---------|
| P0: NPI | 8-12 人（项目制）| 低 | 试产线 + 测试设备 | — |
| P1: SMT | 7-11 人 | ⭐⭐⭐⭐⭐ 极高 | 1500-3000 万 | `inv-top` 最高 |
| P2: PCBA 测试 | 4-6 人 | ⭐⭐⭐⭐ 高 | 300-800 万 | `inv-mid` |
| P3: 整机组装 | 10-15 人 | ⭐⭐ 中等 | 200-500 万 | `inv-low` |
| P4: 整机测试 | 6-10 人 | ⭐⭐⭐⭐ 高 | 500-1000 万 | `inv-mid` |
| P5: 老化终检 | 7-11 人 | ⭐⭐⭐ 中等 | 100-300 万 | `inv-low` |
| P6: 包装出库 | 7-10 人 | ⭐⭐⭐ 中等 | 100-200 万 | `inv-low` |
| **合计（不含NPI）** | **41-63 人/线/班** | — | **2700-5800 万/线** | — |

**规模估算**：两班倒 ≈ 80-126 人/线，按 10 条线规模 ≈ **800-1200 人**的工厂。

---

## 五、支撑体系（横跨全流程的职能部门）

```html
<div class="support-grid">
<div class="support-card">
  <div class="card-title">🔧 工程部（PE/ME/TE）</div>
  <div class="card-info">15-30 人<br>工艺开发、设备维护<br>治具设计、异常处理</div>
</div>
<div class="support-card">
  <div class="card-title">✅ 质量部（IQC/IPQC/OQC/QA/SQE）</div>
  <div class="card-info">20-40 人<br>来料检验、制程巡检<br>出货检验、供应商管理</div>
</div>
<div class="support-card">
  <div class="card-title">📐 IE 工业工程</div>
  <div class="card-info">5-10 人<br>产线平衡、工时制定<br>效率优化</div>
</div>
<div class="support-card">
  <div class="card-title">📊 PMC（生产计划与物料控制）</div>
  <div class="card-info">10-20 人<br>排产、物料齐套<br>库存管理</div>
</div>
<div class="support-card">
  <div class="card-title">🏭 仓储物流</div>
  <div class="card-info">15-30 人<br>原材料仓、线边仓<br>成品仓、发货</div>
</div>
<div class="support-card">
  <div class="card-title">💻 IT/MES</div>
  <div class="card-info">5-10 人<br>生产追溯系统<br>数据采集、报表</div>
</div>
<div class="support-card">
  <div class="card-title">👥 生产管理</div>
  <div class="card-info">班组长 10-20 人<br>现场调度、人员管理<br>产量达成</div>
</div>
<div class="support-card">
  <div class="card-title">📋 质量环</div>
  <div class="card-info">IQC→IPQC→OQC<br>SQE→QA<br>全流程品质闭环</div>
</div>
<div class="support-card">
  <div class="card-title">🔄 MES系统</div>
  <div class="card-info">生产追溯、防错料<br>条码关联、数据看板<br>SPC监控</div>
</div>
</div>
```

---

## 六、核心洞察

### 6.1 三个"最"

- **SMT 是技术核心**：投资最大（1500-3000 万/线）、自动化最高、设备精度最高。一条 SMT 线的好坏直接决定产品品质。
- **整机组装是人力核心**：最难自动化（涉及柔性装配、多种物料形态）、人数最多（10-15 人/线）、离职率最高。这是 ODM 厂最大的成本瓶颈。
- **测试是品质核心**：工站最多（SMT 有 4-5 个检测工站、PCBA 有 3-4 个、整机有 5+ 个）、设备种类最杂。测试策略直接影响良率和出货品质。

### 6.2 MECE 验证

| 维度 | 不重叠？ | 不遗漏？ | 说明 |
|------|---------|---------|------|
| P0-P6 按时间顺序 | ✅ 严格顺序，无重叠 | ✅ 从设计到出货全覆盖 | — |
| 每阶段内部工序 | ✅ 各工序功能独立 | ⚠️ 部分OEM/ODM有微调 | 如有的产线把RF校准放在P4而非P2 |
| 人员/设备/物料 | ✅ 分别归属不同部门管理 | ✅ 全部纳入了支撑体系 | — |
| 质量控制 | ✅ IQC/IPQC/OQC 贯穿各阶段 | ✅ 覆盖来料→制程→出货 | — |

---

*本文档由 AI 助手基于第一性原理 + MECE 法则系统性生成，信息截至 2026 年 6 月。*
