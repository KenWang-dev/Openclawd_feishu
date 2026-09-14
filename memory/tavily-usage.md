# Tavily API 使用备忘

## 状态（2026-03-29）

- KEY 1: ⛔ 额度用完
- KEY 2-7: ✅ 可用
- 搜索时必须优先用 Tavily，Brave 只做补充
- input-protocol.md 里写的搜索优先级是对的：Tavily > multi-search-engine > WebSearch

## 使用方式

```bash
source /root/.openclaw/workspace/.env
KEY=$(eval echo \$TAVILY_KEY_2)  # 优先用 KEY 2

curl -s -X POST "https://api.tavily.com/search" \
  -H "Content-Type: application/json" \
  -d '{
    "api_key": "'"$KEY"'",
    "query": "搜索内容",
    "search_depth": "advanced",
    "max_results": 10,
    "include_answer": true
  }'
```

## 注意

- 中文搜索效果可能不如英文，混合查询效果更好
- include_answer=true 会返回 AI 摘要，很有用
- search_depth: "advanced" 更深但更慢
