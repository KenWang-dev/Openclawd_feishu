# 🚀 Next.js Vibe Coding 学习路线（Ken 定制版）

> 核心原则：**不系统学，直接干。AI 写代码，你负责描述需求、调试、理解。**
> 版本：V1.0 | 2026-04-14

---

## 传统学习 vs Vibe Coding

```
传统路线：JavaScript → TypeScript → React → Next.js → 数据库 → 部署
          （学完理论再动手，3-6个月才出成果）

Vibe Coding：想做什么 → 描述给 AI → AI 生成代码 → 跑起来 → 遇到问题再学
           （第一天就有成果，边做边理解）
```

**你的优势**：你有采购业务逻辑 + Python 基础 + AI 工具链。你缺的不是知识，是**肌肉记忆**。

---

## 三阶段路线

### Stage 1：能跑（第1-3天）

**目标：搭建一个能在线访问的网站**

```
Day 1：
1. 让 AI（Claude Code / Cursor）帮你创建项目
   提示词："帮我用 Next.js 创建一个个人网站，包含首页、关于我、联系方式三个页面，用 Tailwind CSS 样式"
   
2. AI 会生成一堆文件，你只需要：
   - npm run dev → 看效果
   - 看不懂的代码问 AI
   - 想改什么直接说，AI 改

Day 2：
3. 改内容：把你的真实信息填进去
4. 部署：让 AI 帮你部署到 Vercel
   提示词："帮我把这个项目部署到 Vercel，步骤写清楚"
   
Day 3：
5. 自定义域名绑定
6. 发朋友圈炫耀 ✅
```

**这个阶段你只需要理解一个概念：文件路由**
```
app/
├── page.tsx        → 你的域名首页
├── about/page.tsx  → 你的域名/about
└── contact/page.tsx → 你的域名/contact
```
文件夹结构 = URL 路径，就这样。

**采购类比**：这个阶段 = 你第一天上班，先学会用采购系统，别管系统怎么开发的。

---

### Stage 2：能改（第1-2周）

**目标：不依赖 AI 也能做基础修改**

**需要理解的 3 个核心概念（边做边学）：**

**1. Server Component vs Client Component**
```tsx
// 默认就是 Server Component（在服务端运行）
// 像 Excel 公式：你在单元格里写 =SUM(A1:A10)，Excel 在后台算
export default function Page() {
  return <h1>这个在服务端渲染，用户看不到你的代码</h1>
}

// 需要"用户交互"才加 "use client"
// 像 Excel 的按钮：用户点击才触发
"use client"
export default function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>点了{count}次</button>
}
```

**规则：能用 Server Component 就用 Server，需要交互才用 Client。**

**2. 数据展示（读）**
```tsx
// Server Component 里直接 fetch，就像 Python 里直接 requests.get()
async function Suppliers() {
  const data = await fetch('https://api.example.com/suppliers')
  const suppliers = await data.json()
  return (
    <ul>
      {suppliers.map(s => <li key={s.id}>{s.name}</li>)}
    </ul>
  )
}
```

**3. 数据提交（写）**
```tsx
// Server Actions：不用写 API，直接处理表单
// 就像你直接在采购系统里点"提交审批"
"use client"
import { createSupplier } from '@/app/actions'

export function AddForm() {
  return (
    <form action={createSupplier}>
      <input name="name" placeholder="供应商名称" />
      <button type="submit">添加</button>
    </form>
  )
}
```

**这个阶段的练习方式：**
- 想改什么 → 先自己试 → 不行就问 AI → 看 AI 怎么改的 → 下次记住
- 每天改一点点，积累手感

**采购类比**：这个阶段 = 你开始学会修改采购系统里的供应商信息、调整审批流程参数。

---

### Stage 3：能建（第2-4周）

**目标：从零做一个完整项目**

**推荐项目：AI 采购助手（直接结合你的主业）**

```
功能规划：
├── 供应商信息管理（CRUD）
├── 物料比价工具（输入物料，自动比价）
├── AI 询价邮件生成
└── 采购数据分析仪表盘

技术栈：
├── 前端：Next.js + Tailwind CSS
├── 后端：Next.js API Routes + Server Actions
├── 数据库：SQLite（本地开发）→ PostgreSQL（上线）
├── ORM：Drizzle（比 Prisma 轻量，适合小项目）
├── AI：Vercel AI SDK + GLM/Claude API
├── 部署：Vercel（免费）或你的 4G 服务器
└── 认证：NextAuth.js（飞书登录）
```

**这个阶段的 Vibe Coding 方法：**

```
你负责：
- 描述需求（用中文自然语言）
- 评审 AI 生成的代码（看逻辑对不对）
- 测试功能（点点点，看有没有 bug）
- 做业务决策（这个按钮放左边还是右边）

AI 负责：
- 写代码
- 修 bug
- 解释概念
- 推荐最佳实践
```

**采购类比**：这个阶段 = 你从采购员升级到采购经理，开始搭建自己的采购管理体系。

---

## 关键工具配置

| 工具 | 用途 | 你的选择 |
|------|------|---------|
| **Cursor** | AI 编程 IDE（推荐新手） | 免费，直接用 |
| **Claude Code** | 终端 AI 编程（进阶） | 你已有，服务器上可用 |
| **Vercel** | 部署（一键上线） | 免费额度够个人项目 |
| **V0.dev** | AI 生成 UI 组件 | 免费额度，适合设计界面 |
| **bolt.new** | 浏览器里直接写项目 | 适合快速原型验证 |

---

## Vibe Coding 黄金法则

1. **先跑通，再理解** —— 能用就行，别纠结"为什么"
2. **需求驱动学习** —— 遇到什么学什么，不提前预习
3. **AI 是你的搭档** —— 把 AI 当初级开发，你是技术总监
4. **复制粘贴是正经事** —— 不用背 API，AI 会写
5. **项目 > 教程** —— 做 1 个真实项目 > 看 10 个教程

---

## 常见坑（提前避雷）

| 坑 | 现象 | 解法 |
|----|------|------|
| "use client" 忘了 | 点击没反应、useState 报错 | 加 `"use client"` 到文件顶部 |
| async 组件不会用 | fetch 数据报错 | Server Component 默认支持 async |
| 图片太大 | 页面加载慢 | 用 `next/image` 而不是 `<img>` |
| 环境变量泄露 | API Key 暴露 | 密钥放 `.env.local`，别提交到 Git |
| 数据库连接失败 | Prisma/Drizzle 报错 | 先检查 `.env` 配置 |

---

*这份路线会随你的学习进度持续更新。遇到任何问题直接问我。*
