"""
Langfuse 完整示例：带工具调用的AI客服Agent
==============================================
这个脚本模拟一个真实场景：
  用户问"深圳今天天气怎么样" → Agent调用天气工具 → 基于结果生成回答

Langfuse 会完整记录每一步的输入输出、耗时、成本。

使用方法：
  1. 注册 https://cloud.langfuse.com ，创建Project
  2. 把下面的 PK 和 SK 换成你的
  3. pip install langfuse openai
  4. python demo.py
  5. 打开 Langfuse 网页查看 Traces
"""

from langfuse import Langfuse
from langfuse.decorators import observe
import json
import time

# ============================================================
# ① 配置你的 Langfuse Key
# ============================================================
langfuse = Langfuse(
    public_key="pk-lf-xxxxxxxxxxxxx",   # ← 换成你的 Public Key
    secret_key="sk-lf-xxxxxxxxxxxxx",    # ← 换成你的 Secret Key
    host="https://cloud.langfuse.com"     # 云版地址，不用改
)


# ============================================================
# ② 模拟工具：天气查询（不调真实API，模拟返回）
# ============================================================
def weather_tool(city: str) -> dict:
    """模拟调用天气API，返回天气数据"""
    # 模拟网络延迟
    time.sleep(0.3)
    return {
        "city": city,
        "temperature": "32°C",
        "weather": "晴天",
        "humidity": "75%",
        "wind": "东南风3级",
        "aqi": 68,
        "suggestion": "紫外线较强，建议做好防晒"
    }


# ============================================================
# ③ 模拟工具：知识库搜索
# ============================================================
def knowledge_search(query: str) -> list:
    """模拟搜索知识库，返回相关文档"""
    time.sleep(0.2)
    knowledge_base = [
        {"doc_id": "KB001", "content": "公司退款政策：3-5个工作日原路退回"},
        {"doc_id": "KB002", "content": "会员权益：金卡会员享免费快递、专属折扣"},
        {"doc_id": "KB003", "content": "配送时效：深圳同城次日达，其他城市2-3天"},
        {"doc_id": "KB004", "content": "售后服务：7天无理由退换，质量问题一年保修"},
    ]
    # 简单匹配：返回包含关键词的文档
    results = []
    for doc in knowledge_base:
        if any(word in query for word in ["退款", "会员", "配送", "售后"]) or \
           any(word in doc["content"] for word in query.split()):
            results.append(doc)
    return results if results else knowledge_base[:2]  # 没匹配到就返回前两条


# ============================================================
# ④ 用 @observe 装饰器包裹每一步
# ============================================================
@observe()  # Langfuse 自动追踪这个函数的输入输出
def intent_recognition(user_input: str) -> dict:
    """第1步：意图识别（模拟LLM调用）"""
    time.sleep(0.15)  # 模拟LLM延迟
    
    if "天气" in user_input or "温度" in user_input:
        return {"intent": "weather_query", "city": "深圳"}
    elif "退款" in user_input:
        return {"intent": "refund_query"}
    elif "配送" in user_input or "发货" in user_input:
        return {"intent": "delivery_query"}
    elif "会员" in user_input:
        return {"intent": "membership_query"}
    else:
        return {"intent": "general_inquiry"}


@observe()
def tool_execution(intent_data: dict) -> dict:
    """第2步：根据意图调用对应工具"""
    intent = intent_data.get("intent")
    
    if intent == "weather_query":
        result = weather_tool(intent_data.get("city", "深圳"))
        return {"tool": "weather_api", "result": result}
    elif intent in ["refund_query", "delivery_query", "membership_query"]:
        results = knowledge_search(intent_data.get("intent", ""))
        return {"tool": "knowledge_base_search", "result": results}
    else:
        return {"tool": "none", "result": "无工具调用"}


@observe()
def generate_response(user_input: str, intent_data: dict, tool_result: dict) -> str:
    """第3步：基于工具结果生成最终回答（模拟LLM调用）"""
    time.sleep(0.8)  # 模拟LLM生成延迟
    
    intent = intent_data.get("intent")
    
    if intent == "weather_query":
        weather = tool_result["result"]
        response = (
            f"【天气查询结果】\n"
            f"📍 {weather['city']}：{weather['temperature']}，{weather['weather']}\n"
            f"💧 湿度：{weather['humidity']}  |  🌬️ {weather['wind']}\n"
            f"📊 空气质量指数：{weather['aqi']}\n"
            f"💡 提示：{weather['suggestion']}"
        )
    elif tool_result.get("tool") == "knowledge_base_search":
        docs = tool_result["result"]
        response = f"根据知识库检索到 {len(docs)} 条相关信息：\n"
        for doc in docs:
            response += f"  📄 [{doc['doc_id']}] {doc['content']}\n"
        response += "以上信息供您参考，如需更多帮助请告诉我。"
    else:
        response = f"感谢您的提问！关于「{user_input}」，我已经记录下来，稍后会有专人跟进处理。"
    
    return response


@observe()  # 最外层的Trace
def handle_user_message(user_input: str) -> str:
    """主流程：完整的一次用户消息处理"""
    print(f"\n{'='*50}")
    print(f"👤 用户: {user_input}")
    print(f"{'='*50}")
    
    # Step 1: 意图识别
    print("🧠 [Step 1] 意图识别中...")
    intent_data = intent_recognition(user_input)
    print(f"   → 识别结果: {intent_data}")
    
    # Step 2: 工具调用
    print("🔧 [Step 2] 调用工具...")
    tool_result = tool_execution(intent_data)
    print(f"   → 工具: {tool_result['tool']}")
    if tool_result["tool"] != "none":
        print(f"   → 返回: {json.dumps(tool_result['result'], ensure_ascii=False)[:100]}...")
    
    # Step 3: 生成回答
    print("✍️  [Step 3] 生成回答...")
    response = generate_response(user_input, intent_data, tool_result)
    print(f"\n🤖 回答:\n{response}")
    
    return response


# ============================================================
# ⑤ 运行多条示例，模拟不同场景
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Langfuse Demo - AI客服Agent 可观测示例")
    print("=" * 50)
    print("\n💡 运行后请打开 Langfuse 网页查看 Traces")
    print("   你会看到每条消息的完整调用链路\n")
    
    # 模拟 4 条不同类型的用户消息
    test_messages = [
        "深圳今天天气怎么样？",          # 天气查询 → 调用天气API
        "我的退款怎么还没到账？",         # 退款查询 → 搜索知识库
        "你们会员有什么权益？",           # 会员查询 → 搜索知识库
        "配送一般要多久啊？",             # 配送查询 → 搜索知识库
    ]
    
    for msg in test_messages:
        handle_user_message(msg)
        print()
    
    # 确保数据发送到Langfuse
    langfuse.flush()
    
    print("\n✅ 全部完成！现在打开你的Langfuse项目页面，点击左侧 'Traces' 查看")
    print("   每条用户消息都是一个独立的Trace，点进去能看到完整的3步调用链路")
