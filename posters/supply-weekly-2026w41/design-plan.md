# Design Plan — A2 供应链周报封面 2026W41

## 视觉方向
Technical editorial（技术编辑风）：深墨蓝底 + 米白正文 + 琥珀黄强调（黄灯语义）+ 绿色状态点（绿灯语义）。克制、专业、有信息密度。

## 画布
1200x1600 (3:4)，单一屏幕分辨率渲染。

## 资产拓扑
Code-native modular field：纯排版 + 几何（色块、规则线、状态点、编号格），不使用生成图像。风险条目用「维度编号格 + 标题 + 描述」的模块化行阵。

## 字体系统
- 展示标题：cjk-serif (Noto Serif SC Variable) — 中文大标题的编辑感
- 正文/条目：cjk-sans (Noto Sans SC Variable)
- 数字/西文标签：geometric-sans (Space Grotesk Variable) — 周数、风险计数

## 层级（hook → claim → detail）
1. Hook：顶部超大「第41周」数字 + 周报标题
2. Claim：风险仪表（红灯0/黄灯4）大数字对比
3. Detail：四条黄灯条目行阵 + 底部绿灯条与元信息

## 文案
全部事实来自 brief.md（0 红灯 / 4 黄灯、D1/D2/D4 条目、物流绿灯），无虚构。
