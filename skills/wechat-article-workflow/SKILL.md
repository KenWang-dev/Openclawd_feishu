---
name: wechat-article-workflow
description: Complete 7-stage workflow for creating professional procurement WeChat articles. Use when user asks to write article, create procurement content, or provides article ideas. Transforms inputs into published WeChat drafts with cover image, illustrations, and formatting. IP persona Laowang the procurement expert.
---

# WeChat Article Workflow — 老王说采购

七阶段流水线：**素材 → 初稿 → 评审 → 修复 → 验收 → 封面配图 → 发布**

## Quick Start

用户只需提供素材或想法，系统自动运行完整流水线：

```
input/   (素材MD 或 直接文本)
    ↓
阶段1: α 生成初稿
    ↓
阶段2: β 质检评审
    ↓
阶段3: Ω 修复问题
    ↓
阶段4: γ 验收放行
    ↓
output/  (成品文章 + 人工确认)
    ↓
阶段5: κ 生成封面图
    ↓
阶段6: δ 正文配图
    ↓
阶段7: ε 排版发布到微信草稿箱
```

## Input 格式

### 方式1：直接文本（推荐）
用户直接输入想法或素材，无需任何格式。

### 方式2：MD文件（可选）
在 `input/` 目录下放置素材文件，文件名任意。

## 七阶段角色

### 阶段1-4：内容创作流水线

#### α-公众号写作专家（老王说采购）
- **输入**：用户素材/想法
- **输出**：初稿（备选标题+正文+创作说明）
- **能力**：15年500强采购经验，专业但不学术，实战导向
- **参考**：`references/alpha-forge.md`

#### β-公众号文章评审官
- **输入**：初稿
- **输出**：7维21项质检报告
- **能力**：受众命中/标题引力/钩子效能/内容硬度/结构骨架/风格基因/传播基因
- **参考**：`references/beta-inspector.md`

#### Ω-公众号文章修复师
- **输入**：初稿+质检报告
- **输出**：修复日志+修复成品
- **能力**：6种修复操作（定点改写/内容补强/段落新增/结构调序/风格调谐/冗余裁剪）
- **参考**：`references/omega-healer.md`

#### γ-公众号文章验收官
- **输入**：初稿+质检报告+修复报告
- **输出**：验收裁决
- **能力**：三重验证引擎（DIFF透镜+完整性校验+回归检测）
- **参考**：`references/gamma-verifier.md`

### 阶段5-7：自动发布流水线

#### κ-封面图生成专家
- **输入**：验收通过的文章标题和核心信息
- **输出**：封面图文件 (cover.png)
- **能力**：5维定制 (Type×Palette×Rendering×Text×Mood)，支持9种配色+6种渲染风格
- **外部Skill**：`D:/solution/baoyu/.agents/skills/baoyu-cover-image`
- **生成引擎**：`D:/solution/baoyu/.agents/skills/baoyu-image-gen`

#### δ-文章配图专家
- **输入**：验收通过的文章MD
- **输出**：配图方案 + 生成的插图文件
- **能力**：Type×Style二维分析，智能识别配图位置
- **外部Skill**：`D:/solution/baoyu/.agents/skills/baoyu-article-illustrator`
- **生成引擎**：`D:/solution/baoyu/.agents/skills/baoyu-image-gen`

#### ε-微信发布专家
- **输入**：封面图+配图后的文章MD
- **输出**：微信公众号草稿箱
- **能力**：Markdown转HTML + 自动填充 + 保存草稿
- **外部Skill**：`D:/solution/baoyu/.agents/skills/baoyu-post-to-wechat`

## IP人设：老王说采购

| 维度 | 定位 |
|------|------|
| **专业度** | 有体系、有框架、有数据支撑，不说正确的废话 |
| **实战感** | 案例来自真实场景，方法可直接落地 |
| **洞察力** | 用第一性原理拆解问题 |
| **亲和力** | 像朋友聊天一样分享经验 |
| **价值感** | 每篇文章读完都学到东西 |

## 完整执行流程

### 阶段1-4：内容创作

#### Step 1: 调用α生成初稿
加载 `references/alpha-forge.md`，生成初稿

#### Step 2: 调用β质检初稿
加载 `references/beta-inspector.md`，输出7维质检报告

#### Step 3: 调用Ω修复问题
加载 `references/omega-healer.md`，根据质检报告修复问题

#### Step 4: 调用γ验收放行
加载 `references/gamma-verifier.md`，三重验证后输出成品

#### Step 5: 输出成品
将验收通过的成品文章写入 `output/` 目录

### 人工确认点

**⚠️ 阶段4完成后，暂停等待用户确认**

用户可选项：
- **确认继续** → 进入阶段5-7自动配图发布
- **要求修改** → 返回α/β/Ω/γ调整
- **直接结束** → 仅保留文章MD文件

### 阶段5：封面图生成

#### Step 6: 生成封面图
调用 `baoyu-cover-image` 生成文章封面

**5维定制系统**：

| 维度 | 选项 | 说明 |
|------|------|------|
| **Type** | hero, conceptual, typography, metaphor, scene, minimal | 视觉构图类型 |
| **Palette** | warm, elegant, cool, dark, earth, vivid, pastel, mono, retro | 配色方案 |
| **Rendering** | flat-vector, hand-drawn, painterly, digital, pixel, chalk | 渲染风格 |
| **Text** | none, title-only, title-subtitle, text-rich | 文字密度 |
| **Mood** | subtle, balanced, bold | 情感强度 |

**推荐配置**（采购类文章）：
- Type: `conceptual` 或 `typography`（突出核心观点）
- Palette: `elegant` 或 `cool`（专业商务感）
- Rendering: `flat-vector` 或 `digital`（现代简洁）
- Text: `title-only`（仅标题，≤8字）
- Mood: `balanced`（中等强度）

```bash
# 使用 baoyu-cover-image 的脚本
SKILL_DIR="D:/solution/baoyu/.agents/skills/baoyu-cover-image"

# 示例：自动选择 + 快速模式
npx -y bun ${SKILL_DIR}/scripts/main.ts \
  articles/article.md --quick --output cover.png

# 示例：手动指定5维
npx -y bun ${SKILL_DIR}/scripts/main.ts \
  articles/article.md \
  --type conceptual --palette elegant --rendering flat-vector \
  --text title-only --mood balanced --aspect 16:9
```

### 阶段6：正文配图

#### Step 7: 分析文章配图需求
调用 `baoyu-article-illustrator` 分析文章结构，生成配图方案

**配图类型（Type）**：
- `infographic` - 数据/指标类
- `scene` - 叙事/情感类
- `flowchart` - 流程/步骤类
- `comparison` - 对比/优劣类
- `framework` - 框架/模型类
- `timeline` - 历史/演进类

**视觉风格（Style）**：
- `notion` - 知识分享（默认）
- `elegant` - 商务专业
- `blueprint` - 架构设计
- `minimal` - 极简风格

#### Step 8: 生成配图
调用 `baoyu-image-gen` 批量生成插图

```bash
SKILL_DIR="D:/solution/baoyu/.agents/skills/baoyu-image-gen"

npx -y bun ${SKILL_DIR}/scripts/main.ts \
  --prompt "配图描述" \
  --image images/01.png \
  --provider google \
  --ar 16:9
```

#### Step 9: 更新文章MD
在对应段落插入图片引用：
```markdown
![配图说明](images/01.png)
```

### 阶段7：发布到微信

#### Step 10: 选择排版主题
询问用户选择主题（或在配置中预设）：

| Theme | 风格 |
|-------|------|
| `default` | 经典主题 - 传统排版，标题居中带底边 |
| `grace` | 优雅主题 - 文字阴影，圆角卡片 |
| `simple` | 简洁主题 - 现代极简风，不对称圆角 |

#### Step 11: 生成HTML预览
```bash
SKILL_DIR="D:/solution/baoyu/.agents/skills/baoyu-post-to-wechat"

npx -y bun ${SKILL_DIR}/scripts/md-to-wechat.ts \
  articles/article.md --theme <chosen-theme>
```

#### Step 12: 发布到草稿箱
```bash
npx -y bun ${SKILL_DIR}/scripts/wechat-article.ts \
  --markdown articles/article.md --theme <chosen-theme>
```

## 收敛原则

当质检发现红灯项大于等于3个时，仅修复P0，P1/P2暂缓。

## 快速通道

对于简单需求，可跳过β/Ω/γ，α直接输出成品后进入配图发布流程。

## 环境变量配置

在项目根目录创建 `.env` 文件：

```bash
# baoyu-image-gen 配图API (使用 Google provider)
GOOGLE_API_KEY=你的Aiberm_API密钥
GOOGLE_BASE_URL=https://aiberm.com
GOOGLE_IMAGE_MODEL=gemini-3-pro-image-preview

# baoyu-post-to-wechat 微信发布 (可选)
WECHAT_BROWSER_CHROME_PATH=Chrome路径 (如需指定)
```

## 输出目录结构

```
output/
├── {文章标题}.md           # 最终文章MD
├── {文章标题}-illustrated.md  # 带配图的版本
├── cover.png               # 封面图
└── images/
    ├── 01-infographic-xxx.png
    ├── 02-scene-yyy.png
    └── ...
```

## Baoyu Skills 完整映射

| 功能 | Skill | 脚本 |
|------|-------|------|
| 封面图生成 | baoyu-cover-image | scripts/main.ts |
| 正文配图分析 | baoyu-article-illustrator | (分析流程) |
| 图片生成API | baoyu-image-gen | scripts/main.ts |
| HTML预览 | baoyu-post-to-wechat | scripts/md-to-wechat.ts |
| 发布草稿 | baoyu-post-to-wechat | scripts/wechat-article.ts |
