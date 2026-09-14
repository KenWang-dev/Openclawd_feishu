---
name: common-search
description: |
  天网监控系统的搜索引擎统一接口。提供 Tavily/Brave/WebSearch 三种搜索方式，
  支持普通模式和 Deep 模式，内置降级策略（Tavily → Brave → 标注缺失）。
  这是共享基础层，被所有监控 Skill 调用。
---

# 天网搜索接口

> 共享搜索引擎层 — 所有监控任务统一使用此接口进行数据采集。

## 支持的搜索引擎

| 引擎 | 模式 | 用途 | 计费 |
|------|------|------|------|
| **Tavily** | 普通 / Deep | AI 优化搜索，精确查询 | 普通 1x，Deep 2x |
| **Brave** | 普通 | 中文内容补充，Tavily 备用 | 免费 |
| **WebSearch** | 普通 | Claude 内置搜索，最后备用 | 免费 |

## 调用接口

### Tavily 搜索

```bash
# 普通模式
node /root/.openclaw/workspace/skills/tavily-search/scripts/search.mjs \
  "{查询词}" --topic news --days {1|7|30} -n {5-20}

# Deep 模式（红灯验证、重要周报）
node /root/.openclaw/workspace/skills/tavily-search/scripts/search.mjs \
  "{查询词}" --deep --topic news --days {1|7|30} -n {5-20}
```

**参数说明**：
- `--days 1`：过去 24 小时（日报）
- `--days 7`：过去 7 天（周报）
- `--days 30`：过去 30 天（月报）
- `-n 10`：返回 10 条结果（可调整为 5-20）

### Brave 备用搜索

```javascript
// Claude 内置 WebSearch
web_search({
  query: "{查询词}",
  freshness: "{day|week|month}",
  count: {5-10},
  country: "CN"  // 中文搜索
})
```

### 降级策略

```
Tavily 失败
    ↓
Brave 重试（相同关键词）
    ↓
仍失败 → 跳过该搜索，在报告中标注 ⚠️ 数据缺失
    ↓
全部失败 → 输出空报告："⚠️ 搜索服务不可用，本期暂停"
```

**永不中断执行流程**，单个搜索失败不影响其他搜索。

## 搜索模式推荐

| 任务类型 | 推荐模式 | 理由 |
|---------|---------|------|
| 红灯事件验证 | Tavily Deep | 需要多源交叉验证 |
| 重要周报 | Tavily Deep | 深度分析，覆盖面广 |
| 日常日报 | Tavily 普通 | 快速扫描，节省配额 |
| 中文补充 | Brave | 更懂中文语境 |
| 综合周报（W1/W2） | 无搜索 | 直接读 archive |

## Tavily Key 轮换

6 个 Key 按任务类型分配，避免并发冲突：

| Key 编号 | 分配给 | 用途 |
|---------|--------|------|
| Key 1-2 | 日报（生存级：α1/A1/B1/C1） | 高优先级 |
| Key 3 | 日报（其余：D1/β1/γ1/δ1/ε1） | |
| Key 4-5 | 全部周报 | 周报搜索量大 |
| Key 6 | Deep 模式专用 + 月报 | Deep 计 2 倍 |

周日并行时：日报用 Key 1-3，周报用 Key 4-6。

## 配额管理

- 6 个 key × 1000 次/月 = 6000 次/月
- 预估用量：~2000 次/月（33% 利用率）
- 余量充足，无需过度节省

## 结果解析

Tavily 返回格式：
```json
{
  "title": "标题",
  "url": "原文链接",
  "content": "摘要",
  "score": 0.95,
  "publishedDate": "2026-03-28"
}
```

Brave/WebSearch 返回格式类似，含 title/snippet/url。

## 外部脚本（η1 专用）

```bash
# Karpathy 博客精选
npx -y bun /root/.openclaw/workspace/skills/karpathy-digest/scripts/digest.ts
```

此脚本独立运行，不使用 Tavily/Brave。
