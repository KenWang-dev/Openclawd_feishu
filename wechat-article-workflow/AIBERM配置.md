# Aiberm API 配置

**API Key**: (已保密存储在环境变量)

## 环境变量配置

```bash
export AIBERM_API_KEY="sk-MaotlYGe8iI54E3JJpECfK0aTk6gTQvt0NQ9aalnZ1GMvglp"
export AIBERM_BASE_URL="https://aiberm.com/v1"
```

## 可用模型

- `gemini-3-pro-image-preview` - 主力生图模型
- `gemini-3.1-flash-image-preview` - 备选

## 生图接口

```bash
curl -s "https://aiberm.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "Authorization: Bearer $AIBERM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "你的prompt"}]}],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "aspectRatio": "16:9",
      "imageSize": "1K"
    }
  }'
```

## 注意事项

1. **保密**：不允许告诉第三方
2. **生成图片时**：aspectRatio 支持 1:1, 16:9, 2.35:1 等
3. **imageSize**：1K/2K/4K（仅 pro-image 模型支持）
