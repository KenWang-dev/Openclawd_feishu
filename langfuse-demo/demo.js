"""
Langfuse 示例 - Node.js 版本
=============================
如果你更习惯Node.js，用这个版本。

使用方法：
  1. npm init -y
  2. npm install langfuse
  3. 把 PK 和 SK 换成你的
  4. node demo.js
  5. 打开 Langfuse 网页查看 Traces
*/

const { Langfuse } = require("langfuse");

const langfuse = new Langfuse({
  publicKey: "pk-lf-xxxxxxxxxxxxx",   // ← 换成你的
  secretKey: "sk-lf-xxxxxxxxxxxxx",   // ← 换成你的
  host: "https://cloud.langfuse.com"
});

// ============================================================
// 模拟工具
// ============================================================
function weatherTool(city) {
  return {
    city,
    temperature: "32°C",
    weather: "晴天",
    humidity: "75%",
    suggestion: "紫外线较强，建议防晒"
  };
}

function knowledgeSearch(query) {
  const kb = [
    { docId: "KB001", content: "退款政策：3-5个工作日原路退回" },
    { docId: "KB002", content: "会员权益：金卡会员享免费快递、专属折扣" },
    { docId: "KB003", content: "配送时效：深圳同城次日达" },
  ];
  return kb.filter(doc => query.split("").some(w => doc.content.includes(w))).slice(0, 2);
}

// ============================================================
// 用 langfuse.trace() 包裹每一步
// ============================================================
async function handleUserMessage(userInput) {
  const trace = langfuse.trace({
    name: "customer-service-agent",
    input: userInput,
    metadata: { source: "demo", version: "1.0" }
  });

  // Step 1: 意图识别
  const intentStep = trace.generation({
    name: "intent-recognition",
    model: "gpt-4o-mini",
    input: userInput,
    output: userInput.includes("天气")
      ? { intent: "weather_query", city: "深圳" }
      : { intent: "general_query" },
    usage: { promptTokens: 50, completionTokens: 20, totalTokens: 70 }
  });
  console.log(`🧠 意图: ${JSON.stringify(intentStep.output)}`);

  // Step 2: 工具调用
  const intentData = intentStep.output;
  let toolResult;
  if (intentData.intent === "weather_query") {
    toolResult = weatherTool(intentData.city);
    trace.span({
      name: "tool-call:weather-api",
      input: { city: intentData.city },
      output: toolResult
    });
  } else {
    toolResult = knowledgeSearch(userInput);
    trace.span({
      name: "tool-call:knowledge-base",
      input: { query: userInput },
      output: toolResult
    });
  }
  console.log(`🔧 工具返回: ${JSON.stringify(toolResult).slice(0, 80)}...`);

  // Step 3: 生成回答
  const response = intentData.intent === "weather_query"
    ? `${toolResult.city}：${toolResult.temperature}，${toolResult.weather}，${toolResult.suggestion}`
    : `感谢提问「${userInput}」，已记录，稍后专人跟进。`;

  trace.generation({
    name: "response-generation",
    model: "gpt-4o",
    input: { userQuery: userInput, toolResult },
    output: response,
    usage: { promptTokens: 200, completionTokens: 80, totalTokens: 280 }
  });

  trace.update({ output: response });
  console.log(`🤖 回答: ${response}\n`);
}

// ============================================================
// 运行
// ============================================================
async function main() {
  console.log("Langfuse Demo - Node.js 版\n");

  const messages = [
    "深圳今天天气怎么样？",
    "我的退款怎么还没到账？",
  ];

  for (const msg of messages) {
    await handleUserMessage(msg);
  }

  await langfuse.flushAsync();
  console.log("✅ 完成！打开 Langfuse 网页查看 Traces");
}

main();
