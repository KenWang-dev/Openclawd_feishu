# 微信公众号文章工作流

## 文件夹结构

```
wechat-article-workflow/
├── input/           ← 你的素材/想法（原始输入）
├── output/          ← 生成的初稿（Alpha/Beta/Omega/Gamma 各阶段输出）
├── images/          ← AI 生成的配图（封面+正文插图）
├── prompts/         ← 4 个 prompt 文件
│   ├── Alpha-初稿改写.md
│   ├── Beta-评审.md
│   ├── Omega-修改.md
│   └── Gamma-验收.md
└── SKILL.md
```

## 三阶段流程

### 第一阶段：输入 + 研究
- 你提供素材/想法/参考文章
- 我保存到 `input/` 文件夹
- **自动调用 Tavily 深度搜索** 补充相关信息
- 格式：`input/YYYY-MM-DD-主题.md`

### 第二阶段：生成初稿（纯文本）
```
Alpha(初稿) → Beta(评审) → Omega(修改) → Gamma(验收)
```
- 每阶段输出保存到 `output/`
- 最终输出：`output/终稿-YYYY-MM-DD.md`

### 第三阶段：配图 + 发布
- 用 AI 生成封面图 → `images/封面-主题.png`
- 生成正文配图 → `images/`
- 发到公众号草稿箱
- 你确认后手动发布

## 使用方式

1. **给素材**：发想法/素材给我
2. **第一阶段**：我保存素材 + Tavily 深度搜索补充
3. **第二阶段**：我跑 Alpha→Beta→Omega→Gamma，生成纯文本初稿
4. **第三阶段**：配图 → 发草稿箱 → 你确认发布

---

## 公众号信息

- **名称**：辉正点AI采购
- **定位**：AI + 采购交叉领域
- **风格**：以前怎么做 → 现在AI怎么做了
