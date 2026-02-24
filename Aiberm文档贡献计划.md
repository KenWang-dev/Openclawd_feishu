# Aiberm 文档贡献计划

## 🎯 项目信息

**仓库**：https://github.com/aiberm/aiberm-docs
**奖励**：
- 贡献一篇中英文文档：**10 刀 credit**
- 发现疏漏提交 PR：**2 刀 credit**

**缺少的 IDE 文档**：
- Cursor
- Trae
- Antigravity
- 其他...

---

## 📋 需要贡献的内容

### 任务概述
为 Aiberm API 编写 IDE 配置教程文档，包括：
- 环境准备
- API Key 配置
- 示例代码
- 截图说明（英文版）
- 中英文双语

### 文档要求
1. **格式**：MDX（Markdown + React 组件）
2. **语言**：中英文双语
3. **内容**：
   - IDE 安装/设置
   - Aiberm API 配置
   - 代码示例
   - 截图说明
   - 故障排除

---

## 🔍 可以贡献的 IDE

### 1. Cursor ⭐⭐⭐⭐⭐（推荐）

**简介**：AI 原生代码编辑器，基于 VS Code

**优势**：
- 我熟悉 VS Code 生态系统
- 配置方法清晰
- 用户群体大
- 文档需求明确

**文档内容**：
- 安装 Cursor
- 配置 HTTP 客户端（REST Client）
- 设置环境变量
- API 调用示例
- AI 辅助功能集成

**预估难度**：⭐⭐（简单）

---

### 2. Trae ⭐⭐⭐

**简介**：需要进一步研究

**调研需求**：
- 这是什么 IDE？
- 主要功能是什么？
- 如何配置 API？

**行动**：
- 使用 Tavily Search 搜索信息
- 了解配置方法
- 编写文档

**预估难度**：⭐⭐⭐（中等）

---

### 3. Antigravity ⭐⭐⭐

**简介**：需要进一步研究

**调研需求**：
- 这是什么工具？
- 是 IDE 还是编辑器？
- 如何与 Aiberm API 集成？

**行动**：
- 搜索相关信息
- 了解集成方法
- 编写文档

**预估难度**：⭐⭐⭐⭐（较难）

---

## 💡 执行计划

### Phase 1：调研（30分钟）
1. 搜索 Cursor 的详细信息
2. 搜索 Trae 的详细信息
3. 搜索 Antigravity 的详细信息
4. 了解各 IDE 的配置方法

### Phase 2：编写文档（1-2小时）
选择一个 IDE（推荐 Cursor），创建：
- 英文版文档（含截图）
- 中文版文档（含截图）
- 符合项目 MDX 格式

### Phase 3：提交 PR（15分钟）
1. Fork 仓库
2. 创建分支
3. 提交文档
4. 创建 Pull Request

---

## 🛠️ 技术要求

### 文档格式（MDX）

```mdx
---
layout: ../../layouts/DocsLayout.astro
title: IDE Integration - Cursor
lang: en
activeId: ide-cursor
---

import CodeExample from '../../components/CodeExample.tsx';
import Callout from '../../components/Callout.tsx';

# Cursor Integration Guide

## Prerequisites

- Cursor installed
- Aiberm API key

## Installation

<Callout client:load type="info" title="Note">
Make sure you have the latest version of Cursor.
</Callout>

## Configuration

### Step 1: Get API Key

1. Visit https://aiberm.com
2. Sign up/Login
3. Navigate to API Keys
4. Copy your API key

### Step 2: Configure Cursor

<CodeExample
  client:load
  examples={[
    {
      key: 'bash',
      label: 'Environment Variable',
      code: `export AIBERM_API_KEY="your_api_key_here"`
    },
    {
      key: 'json',
      label: 'Settings JSON',
      code: `{
  "aiberm.apiKey": "your_api_key_here"
}`
    }
  ]}
/>

## Usage

### Example Request

<CodeExample
  client:load
  examples={[{
    key: 'python',
    label: 'Python',
    code: `import requests

response = requests.get(
  "https://api.aiberm.com/v1/chat",
  headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
  }
)`
  }]}
/>

---

## 中文版（src/pages/zh/ide-cursor.mdx）

```mdx
---
layout: ../../layouts/DocsLayout.astro
title: Cursor 集成指南
lang: zh
activeId: ide-cursor
---

import CodeExample from '../../components/CodeExample.tsx';
import Callout from '../../components/Callout.tsx';

# Cursor 集成指南

## 前置要求

- 已安装 Cursor
- Aiberm API 密钥

## 安装步骤

<Callout client:load type="tip" title="提示">
确保你安装了最新版本的 Cursor。
</Callout>

## 配置方法

### 步骤 1：获取 API 密钥

...
```

---

## ✅ 文档质量检查清单

### 内容完整性
- [ ] 前置要求说明
- [ ] 安装步骤清晰
- [ ] 配置方法详细
- [ ] 代码示例可运行
- [ ] 截图清晰（英文版）
- [ ] 故障排除指南

### 格式规范
- [ ] 符合 MDX 格式
- [ ] 使用正确的 React 组件
- [ ] 代码语法高亮正确
- [ ] 中英文双语对应

### 项目要求
- [ ] 更新 navigation.ts
- [ ] 添加到正确的语言目录
- [ ] 通过本地构建测试

---

## 🎁 预期奖励

### 保守估计
- 贡献 1 篇文档（Cursor）：**10 刀 credit**
- 发现 1-2 个疏漏：**2-4 刀 credit**
- **总计**：12-14 刀 credit

### 乐观估计
- 贡献 2-3 篇文档：**20-30 刀 credit**
- 发现多个疏漏：**5-10 刀 credit**
- **总计**：25-40 刀 credit

---

## 🚀 下一步行动

### 立即可做
1. ✅ 使用 Tavily Search 搜索 IDE 信息
2. ✅ 选择一个 IDE 开始贡献
3. ✅ 创建文档草稿

### 需要你的协助
1. **GitHub 账号**：需要账号来提交 PR
   - 你有 GitHub 账号吗？
   - 用户名是什么？

2. **Fork 权限**：需要 fork 仓库
   - 我可以帮你操作吗？

3. **Aiberm 账号**：用于接收 credit
   - 需要你的 Aiberm 用户名或 ID

---

## 📝 建议开始顺序

### 第一优先级：Cursor（推荐）
- 最容易编写
- 用户群体大
- 我熟悉 VS Code 生态
- 预计 1-2 小时完成

### 第二优先级：Trae
- 需要先调研
- 难度中等
- 预计 2-3 小时完成

### 第三优先级：Antigravity
- 需要深入调研
- 难度较高
- 预计 3-4 小时完成

---

**准备好了吗？** 让我搜索一下这些 IDE 的信息，然后开始编写文档！

需要我：
1. **立即开始搜索 IDE 信息**？
2. **先调研一下，然后制定详细计划**？
3. **其他建议**？

告诉我你的选择，我们开始贡献！🚀🪭
