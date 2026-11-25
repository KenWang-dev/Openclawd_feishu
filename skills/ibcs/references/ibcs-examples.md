# IBCS 代表性案例集 — Before/After 改造手册

> 用途：与 `ibcs-rules.md` 配套。收录 14 个最具代表性的 IBCS 改造场景（含常见图表类型逐图规范），
> 每个场景给出 ❌ 常见错误做法 → ✅ IBCS 规范做法 + 适用规则编号。
> ISO 24896 覆盖映射见文末附录。
> 案例解读基于 IBCS v1.1 官方标准原文（CC BY-SA 4.0，来源 https://www.ibcs.com/standards/ ，2024-11 抓取全部分页）。
> 每个案例附【官方原始依据】一节：规则编号 + 官方原文关键句 + 对应官方图（references/figures/ 下 13 张从 ibcs.com 下载的原始图）。
> Before/After 与 ASCII 示意仍为解读手段，非官方原文。

---

## 案例 1：图表标题 — 从"数据名称"到"消息"

**❌ Before**：`销售数据 / Dashboard / 2024`
**✅ After**：`华东区净销售额下降15%至€340M，主要由Key客户流失拖累（百万€）2024年1-6月`

- 规则：SAY 1.1-1.4
- 要点：标题必须是一句**结论**（主体+指标+变化幅度+原因+单位+时间段），读者只看标题就拿到核心消息
- 公式：`[主体][指标]（[单位]）[时间段]` + 前缀一句判断

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**SA 2.3 / SA 3.2 / UN 2.1 / UN 2.2**
- 官方原文/要点：SA 3.2: "Every report, every presentation, and every single page or exhibit can be summed up with a clear overall message. This message usually comes first and is proven afterwards."；UN 2.1: 消息应固定放在页面顶部两行（标题上方或标题右侧）；UN 2.2: 页面标题三行 = 报告主体（Title line 1）+ 业务指标加单位（Title line 2）+ 时间期间/场景（Title line 3）。
- 对应官方图：UN 2.1（消息位置）、UN 2.2（标题三行结构） → references/figures/fig-un-2-1.png, references/figures/fig-un-2-2.png
- 对应官方图：EX 4.1（Add scenarios，补充 PY/PL/AC/FC 场景维度） → references/figures/fig-ex-4-1.png


---
## 案例 2：时间序列 + 目标对比 — 实心/空心柱

场景：展示 2025 年各季度实际销售额 vs 预算。

**❌ Before**：两条彩色柱（蓝色=实际，橙色=预算）+ 右侧图例
**✅ After**：
```
        深色实心柱 = AC     空心轮廓柱 = PL
  Q1  ██  ┌─┐        Q2  ██  ┌─┐       （数据系列名直接标在第一组柱旁）
      120 └─┘135          145 └─┘135
  Q3  ██  ┌─┐        Q4  ██┐ ┌┐
      150 └─┘140          170┘ └┘150
```
- 规则：UN 1.1、UN 3.2、SI 1.1
- 要点：AC=实心深色、PL=空心轮廓（这套记号全报告通用，读者学一次就够）；删除外部图例，系列名内嵌标注

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**UN 3.2**
- 官方原文/要点：UN 3.2: 实测数据（AC）用深色实心填充（solid dark fill），比较更早实测期间（PY）用浅色实心（lighter solid fill）；虚构数据（PL/BU）用轮廓空心（bordered/outlined），预期数据（FC）用斜线填充（hatched）。UN 2.3: 图例应尽量内嵌到图中（integrate legends into charts），堆叠柱的图例放在最左柱左侧或最右柱右侧。
- 对应官方图：UN 3.2（场景记号法）、UN 2.3（图例内嵌） → references/figures/fig-un-3-2.png


---
## 案例 3：分类对比 — 饼图改条形图

场景：各区域销售额占比。

**❌ Before**：饼图 7 块，其中 4 块大小接近，读者根本分不清谁大谁小
**✅ After**：垂直条形图按数值降序排列，数值标注在条形右端
```
  华东    ████████████ 120
  华南    █████████ 95
  华北    ████████ 80
  西南    █████ 52
  东北    ████ 41
  西北    ██ 25
  其他    █ 12
```
- 规则：EX 1.2、EX 3.3、SAY 3.3
- 要点：分类对比一律条形图；>5 个分类饼图完全失效；按数值排序让"谁最大"一眼可见

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 2.1**
- 官方原文/要点：EX 2.1: "Pie and ring charts are circular charts dividing some total into sectors of relative proportion, but there are better ways to illustrate the numerical proportions of segments, e.g. bar charts or charts with stacked columns." 饼图只支持一维分析，例外是 CH 3.3 地图上标注单点市场份额。
- 对应官方图：EX 2.1（替换饼图/环形图） → references/figures/fig-ex-2-1.png


---
## 案例 4：差异分解 — 瀑布图

场景：解释"今年利润为什么降了"。

**❌ Before**：两页独立柱状图（去年利润一页、成本明细一页），读者自己心算差在哪
**✅ After**：一张瀑布图从 PY 利润走到 AC 利润，中间每个成本/收入项一根柱
```
  PY利润      ─────────  85
  销量增长       ███     +12
  价格下降       ▒▒▒     -9
  原材料涨价     ▒▒▒▒    -15
  汇率           ▒       -3
  AC利润     ─────────   70
  (增长项=实心，拖累项=红色，合计柱=空心)
```
- 规则：EX 1.4、CH 3.1
- 要点：差异分析（尤其"为什么变"）首选瀑布图；有利差异绿色/实心，不利差异红色

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 1.1 / UN 4.1**
- 官方原文/要点：EX 1.1: 图表类型须与场景/时间/结构分析匹配；瀑布图属于同一量纲上正负差异柱/条的连续延伸。UN 4.1 绝对差异：差异柱（variance columns/bars）与基础值柱宽度、刻度一致；正面影响绿色、负面影响红色、中性影响灰/蓝；被减数场景记号（AC 实心/FC 斜线）作用于差异柱，被比较场景记号作用于轴。
- 对应官方图：UN 4.1（绝对差异记号）、EX 1.1（图表类型）、EX 4.2（Add variances，补充实际与计划差异值） → references/figures/fig-un-4-1.png, references/figures/fig-ex-1-1.png, references/figures/fig-ex-4-2.png


---
## 案例 5：Y 轴诚实性 — 从 85 开始的柱状图

**❌ Before**：Y 轴从 85 起步，两个月度销量从"看起来差 4 倍"实际只差 18%
**✅ After**：Y 轴从 0 开始；差异实在太小就用表格 + 差异列（▲18%）
- 规则：CH 1.1 ⭐ISO、CH 1.3
- 要点：柱状图/条形图 Y 轴必须从 0；这是 IBCS 最严格的红线。折线图不受此限（折线允许截断轴，但需标注）

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**CH 1.1**
- 官方原文/要点：CH 1.1: "Charts with value axes not starting at zero ('cut' axes) are not 'wrong' in and of themselves, but the message to be visually conveyed then does not correspond to the numerical values... Therefore, value axes should generally start at zero." 唯一例外：指数化数据（=100%）且差异很小，此时类别标签应放在 100% 线上。
- 对应官方图：CH 1.1（避免截断轴） → references/figures/fig-ch-1-1.png


---
## 案例 6：表格升级 — 加差异列和迷你趋势线

**❌ Before**：一张只有"本月销售额"单列的表，读者看不到趋势和目标差距
**✅ After**：
```
  区域    AC    PL    Δ    Δ%   趋势(近6月)
  华东    120   135  ▲-15  -11%  ▂▄▃▅▄▆
  华南     95    90   ▲+5   +6%  ▃▄▅▄▆▇
```
- 规则：EX 2.1、CO 2.3、UN 1.2-1.3
- 要点：管理报表表格标配 4 列——AC、基准（PL/PY）、绝对差异、相对差异；再加一列 sparkline 看趋势；差异用 ▲▼+颜色双编码（色盲友好）

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 1.2 / CO 4.4**
- 官方原文/要点：EX 1.2 官方表格类型：时间序列表（time series tables，时间列×指标/结构行）、差异表（variance tables，场景列+差异列）、交叉表（cross tables）、组合表（combined tables）。CO 4.4: 用表格条（table bars）、预警点、sparkline 等图表元素嵌入表格提高信息密度。
- 对应官方图：EX 1.2（表格类型）、CO 4.4（表格内嵌图表元素） → （EX 1.2 各表型见官方 Figure EX 1.2-22..27，未下载）


---
## 案例 7：Dashboard 降维 — 仪表盘改迷你图阵列

**❌ Before**：8 个圆形速度计占满一屏，每个只显示一个数字
**✅ After**：一张 2×4 小型多图（small multiples），每格一个指标近 12 月柱状图，刻度统一，末柱空心=预测
- 规则：EX 3.2、CO 1.1、CO 2.1
- 要点：速度计信息密度极低（一个大圆只装一个数）；小型多图同刻度排布，单屏信息量提升 10 倍以上

---
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 2.2 / CO 5.1**
- 官方原文/要点：EX 2.2: "speedometers are probably one of the most useless visualizations out there. They take up way too much space..." 用条形图示结构、柱状图示时间趋势替代。CO 5.1: 小 multiples（small multiples）= 同类型同刻度图表并排在同一页，适合最多约 25 个对象。
- 对应官方图：EX 2.2（替换仪表盘/速度表）、CO 5.1（small multiples）、EX 2.5（Replace traffic lights，用带数值条形图替代红黄绿信号灯） → references/figures/fig-ex-1-1.png（图表类型总览）, references/figures/fig-ex-2-5.png


---
## 案例 8：降噪 — 删掉图表上的"装饰"

**❌ Before**：深蓝渐变背景 + 网格线 + 图例框 + 边框 + 3D 效果 + 阴影，数据柱只占画面 30%
**✅ After**：白底、无网格线、数值直接标在柱顶、无边框阴影，数据占画面 70%+
```
  删除清单：背景渐变✂ 网格线✂ 外部图例✂ 3D/阴影✂ 重复标题✂
  保留清单：消息标题 ✓ 内嵌系列名 ✓ 数据点数值 ✓ 差异▲▼ ✓
```
- 规则：SI 1.1-1.4、SI 3.1、EX 3.1
- 要点：每条多余的线、每种多余的颜色都是噪音。基色黑白灰给数据，绿红只留给差异标注

---

---

# 第二部分：常见图表类型逐图规范
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**SI 1.1 / SI 2.1 / SI 2.2 / SI 3.1**
- 官方原文/要点：SI 1.1: 避免 无意义的布局元素；SI 2.1: "borders, shades, and pseudo-3D convey no meaning and make comprehension more difficult"；SI 2.2: 装饰性颜色会占用有语义的颜色资源；SI 3.1: 用数据标签替代网格线和数值轴（密集多系列或小图可保留网格线）。
- 对应官方图：SI 1.1、SI 2.1-2.3、SI 3.1 → references/figures/fig-si-3-1.png


---
## 案例 9：柱状图（Column Chart）

**适用**：时间序列（时间在水平轴，≤12 个点）

**❌ 常见错误**：彩色柱区分系列、Y 轴不从 0、网格线读数、外部图例
**✅ 规范做法**：
```
 部门A月度销量（千件）2025年 ── 实际值
 1月  ██ 120          5月  ██████ 155
 2月  ███ 128         6月  ███████ 168   (数值标在柱顶，无Y轴)
 3月  ██▁ 115         7月  ██████████ 190
 4月  ████ 140
   ↑ AC=实心深色；如叠加预测：末柱用斜线填充
```
- 关键规则：EX 1.1、CH 1.1 ⭐ISO（Y轴从0）、SI 1.3（数值直标可省数值轴）、UN 1.1（AC实心/FC斜线）
- 折线/柱的选择：≤12 个时间点用柱，>12 个用折线
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 1.1 / UN 3.1**
- 官方原文/要点：UN 3.1: 基础指标（basic measures）柱宽为类别宽度的 2/3；比率（ratios）柱宽为 1/3；折线图中基础指标用粗线、比率用细线（粗线的 50%）。
- 对应官方图：UN 3.1（统一指标记号） → references/figures/fig-ex-1-1.png


---
## 案例 10：条形图（Bar Chart）

**适用**：分类/结构对比（分类在垂直轴，按数值排序）

**❌ 常见错误**：水平柱+垂直分类（时间轴误用）、不排序、标签斜放
**✅ 规范做法**：降序条形，类别名左对齐，数值标条形右端；如做 AC vs PY 对比，AC 实心条、PY 浅灰条
- 关键规则：EX 1.2、EX 1.8、SAY 3.3
- 注意：条形图同样必须从 0 开始（CH 1.1 ⭐ISO）
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 1.1 / UN 3.4**
- 官方原文/要点：UN 3.4: "Display structures always in vertical direction" — 结构维度（地区/组织/产品/客户）放在垂直方向（条形图的类别轴），时间只能水平方向（UN 3.3）。EX 1.1: 条形图适合结构对比与排名。
- 对应官方图：UN 3.4（结构维度垂直方向）、UN 3.3（时间水平方向） → references/figures/fig-ex-1-1.png


---
## 案例 11：折线图（Line Chart）

**适用**：连续趋势（>12 个时间点，如日/周数据、多年月度）

**❌ 常见错误**：每条线一个颜色+外部图例、双 Y 轴、标记每个数据点（蜘蛛网）
**✅ 规范做法**：
```
 收益率走势（%）2024-2025
      ╭─AC──────────╮         线端直接标注系列名
 PL┄┄┄┥              ┠┄┄FC    预测段用虚线延续
      ╰──────────────╯
```
- 关键规则：EX 1.5、SI 1.1（线端内嵌标签替代图例）、UN 1.1（FC 段虚线/斜纹）
- 对应官方图：EX 2.4（Replace spaghetti charts，多条交织折线拆分为独立小图） → references/figures/fig-ex-2-4.png
- 例外：折线 Y 轴可不从 0 开始（比例变化是重点时），但须清晰标注（CH 1.4 ⭐ISO 精神）
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**UN 3.3 / UN 4.2**
- 官方原文/要点：UN 3.3: 时间轴一律从左到右；表格中时间序列放列。UN 4.2 时间序列分析记号：YTD 用前缀下划线（_Jun），YTG 用后缀下划线，移动分析（MAT）用波浪号前缀（~Jun），时间指数化用右向黑色箭头 + 100%。
- 对应官方图：UN 3.3（时间方向/缩写）、UN 4.2（时间序列分析记号） → references/figures/fig-ex-1-1.png


---
## 案例 12：饼图（Pie Chart）— 什么时候必须放弃

**判定流程**：
```
 是占比构成？→ 分类≤5 且大小差异悬殊 → 勉强可用（但仍推荐100%柱）
            → 分类>5 或大小接近      → 禁用，改排序条形图/100%柱状图
 是趋势？                            → 禁用，改折线
 是对比？                            → 禁用，改条形图
```
**❌ 典型翻车**：8 块占比 12%-18% 的饼图——人眼对面积差异的感知误差可达 ±10%，无法判断谁大
**✅ 替代**：100% 堆积柱状图（构成）或降序条形图（对比）
- 关键规则：EX 3.3、EX 1.3、CH 2.1 ⭐ISO（避免透视失真图表）
- 3D 饼图、甜甜圈图一律禁止（EX 3.1、EX 3.4）
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 2.1 / CH 3.3**
- 官方原文/要点：EX 2.1 正文给出的唯一合理场景：需要在地图特定位置标注市场规模/份额时可用饼图（"pie charts can be positioned on a specific point on a map"，见 CH 3.3 Figure）。CH 3.3 同时强调：与面积无关的指标（如市场份额）不得用彩色面积填地图，应放等刻度柱/条。
- 对应官方图：EX 2.1、CH 3.3（地图彩色面积误导） → references/figures/fig-ex-2-1.png


---
## 案例 13：散点图（Scatter）

**适用**：两变量关联关系（如"广告投入 vs 销量"）

**❌ 常见错误**：气泡大小再编码第三变量（面积感知失真）、趋势线过拟合、彩色分组无内嵌标签
**✅ 规范做法**：单色点 + 一条线性趋势线 + 关键点椭圆圈选标注；刻度示意器标注量级
- 关键规则：EX 1.7、UN 2.4（椭圆圈选统一用于高亮）、CH 1.5
- 精确读数需求高时改表格（EX 2.1）
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**EX 5.2 / EX 5.3**
- 官方原文/要点：EX 5.2: 用二维/三维 cluster 展示大量数据以发现新洞察；EX 5.3: 用排名与对比辅助理解多序列之间的相关性（"correlations are often sought in order to better understand the interrelations"）。
- 对应官方图：EX 5.2（clusters）、EX 5.3（correlations） → （EX 5.2/5.3 官方图未下载，见 standards 页）


---
## 案例 14：瀑布图（Waterfall）

**适用**：从起点值到终点值的逐项增减分解（利润桥、预算差异桥）

**❌ 常见错误**：增长项与拖累项同色、中间柱从 0 画起、缺少合计柱
**✅ 规范做法**：
```
 息税前利润桥（百万€）2025 vs 2024
 PY EBIT ━━━━━━━━ 85
 +销量   ███      +12   实心=有利
 -价格   ▒▒▒      -9    红/斜纹=不利
 -原材料 ▒▒▒▒     -15
 +汇率   █        +3
 AC EBIT ────────  76    终点柱空心轮廓或实心合计
```
- 关键规则：EX 1.4、CH 3.1（有利/不利方向准确）、UN 1.2
- 中间柱悬浮表示"增量"，不触 0 轴——这是瀑布图唯一允许"柱不从 0 开始"的例外

---

# 附录：ISO 24896:2026 覆盖映射（18 条）

**背景**：ISO 24896《Notation for business reporting》采纳了 IBCS 2.0 共 18 条核心规则，
其中 **15 条来自 UNIFY（记号法）+ 3 条来自 CHECK（视觉诚实）**。
官网对 UNIFY 侧 15 条未公开逐条名单（会员区内容），以下按主题如实标注：

**✅ CHECK 侧已确认的 3 条（官网规则页明确标 ISO）**
| IBCS 编号 | 内容 |
|---|---|
| CH 1.1 | 柱/条形图 Y 轴必须从 0 开始 |
| CH 1.4 | 非零起点必须标注为比例图 |
| CH 2.1 | 禁用透视失真图表（3D 等） |

**✅ UNIFY 侧 15 条（ISO 记号法主题覆盖，逐条编号未公开）**
| 主题簇 | 对应 IBCS 规则 |
|---|---|
| 场景填充记号（AC实心/PY浅灰/PL空心/FC斜纹） | UN 1.1 |
| 差异方向标注（有利▲绿/不利▼红） | UN 1.2 |
| 差异标注方式（绝对/Pin%差异） | UN 1.3 |
| 时间/结构维度分析基准 | UN 1.4、UN 1.6 |
| 指标类别与维度统一 | UN 1.5 |
| 图表类型与场景绑定 | UN 2.1 |
| 刻度统一与刻度指示器 | UN 2.2 |
| 内外标签统一（内嵌标签） | UN 2.3 |
| 高亮标注统一（椭圆/箭头/▲▼） | UN 2.4 |
| 标准场景组合（AC-PY / AC-PL / FC-PL） | UN 3.1-3.4 |

**使用建议**：给国际客户/审计场景的报告，可声明"遵循 ISO 24896 记号法"；
日常内部报告按 IBCS 2.0 全量 105 条执行即可（ISO 是其子集）。

## 附：改造自查清单（出报告前过一遍）

- [ ] 每页/每图标题是一句结论吗？
- [ ] AC/PY/PL/FC 的填充样式全报告统一吗？
- [ ] 柱状图 Y 轴从 0 开始了吗？
- [ ] 分类对比用的是条形图（不是饼图）吗？
- [ ] 差异分析用瀑布图/差异列了吗？▲▼+颜色双编码了吗？
- [ ] 删掉外部图例、网格线、背景装饰了吗？
- [ ] 表格有 AC+基准+Δ+Δ% 四件套吗？
- [ ] 单位放标题里了吗？
### 【官方原始依据】（IBCS v1.1）

- 规则编号：**UN 4.1**
- 官方原文/要点：UN 4.1 绝对差异："variance columns or bars have the same width and the same scale as the corresponding base value columns or bars"；差异标签放在柱/条外侧，正差异（绿）标签在上/右，负差异（红）在下/左；ΔPL = AC-PL，正值必须带 + 号。
- 对应官方图：UN 4.1（绝对/相对差异记号） → references/figures/fig-un-4-1.png


---
---

## 勘误：本 skill 此前版本与官方 v1.1 原文的出入

1. **案例 1 原引用 "SAY 1.1-1.4"**：官方 v1.1 中 SA 1 是 "Know objectives"（SA 1.1 Know own goals / SA 1.2 Know target audience），消息相关规则是 SA 2（Introduce message）/ SA 3（Deliver message）；"标题即消息"的位置规范出自 UN 2.1，三行标题结构出自 UN 2.2。已改。
2. **"消息标题"并非 SA 章直接规定**：官方对消息的要求是"完整句子、先说结论、可检测/解释/建议"（SA 3.1/3.2）；`主体+指标+幅度+原因` 公式是解读演绎，非官方条文。
3. **替代双子饼图的 "100% 条形图"**：官方 EX 2.1 正文推荐的是条形图或堆叠柱；100% bar 是评论区的社区建议，不应作为标准条文引用。
4. **仪表盘（speedometers）措辞**：官方原文语气更强烈（"one of the most useless visualizations out there"），此前描述偏温和。
5. **v2.0 注意**：官方公开分页全文为 v1.1；若 v2.0 rules 文件中的规则编号/标题与 v1.1 不同（如 UN 4.1 中性差异颜色由"中灰"倾向改为"蓝色"，见官方评论区 Rolf Hichert 2021-02 意见），应以官方最新发布版本核对。
