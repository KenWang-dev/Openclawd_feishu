#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { getApiKey, recordUsage } from './key-pool.mjs';

console.log("Getting API key...");

function usage() {
  console.error(`Usage: search.mjs "query" [-n 5] [--deep] [--topic general|news] [--days 7]`);
  process.exit(2);
}

const args = process.argv.slice(2);
if (args.length === 0 || args[0] === "-h" || args[0] === "--help") usage();

const query = args[0];
let n = 5;
let searchDepth = "basic";
let topic = "general";
let days = null;

for (let i = 1; i < args.length; i++) {
  const a = args[i];
  if (a === "-n") {
    n = Number.parseInt(args[i + 1] ?? "5", 10);
    i++;
    continue;
  }
  if (a === "--deep") {
    searchDepth = "advanced";
    continue;
  }
  if (a === "--topic") {
    topic = args[i + 1] ?? "general";
    i++;
    continue;
  }
  if (a === "--days") {
    days = Number.parseInt(args[i + 1] ?? "7", 10);
    i++;
    continue;
  }
  console.error(`Unknown arg: ${a}`);
  usage();
}

// 使用 Key 池获取 API Key
const apiKey = getApiKey();
if (!apiKey) {
  console.error("No Tavily API Key available");
  process.exit(1);
}

let body = {
  api_key: apiKey,
  query: query,
  search_depth: searchDepth,
  topic: topic,
  max_results: Math.max(1, Math.min(n, 20)),
  include_answer: true,
  include_raw_content: false,
};

if (topic === "news" && days) {
  body.days = days;
}

let data = await doSearch(body);

// 如果遇到配额限制(432)，自动切换 Key 重试
async function doSearch(reqBody) {
  const resp = await fetch("https://api.tavily.com/search", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reqBody),
  });

  // 记录使用次数
  recordUsage();

  // 如果遇到配额限制，自动切换 Key 重试
  if (resp.status === 432) {
    const text = await resp.text().catch(() => "");
    console.error(`[Key Pool] Key 配额用尽 (432)，切换到下一个 Key 重试...`);
    
    // 切换到下一个 Key
    const state = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'key-pool.json'), 'utf-8'));
    state.currentIndex = (state.currentIndex + 1) % state.keys.length;
    state.usageCount = 0;
    fs.writeFileSync(path.join(process.cwd(), 'key-pool.json'), JSON.stringify(state, null, 2));
    
    // 使用新 Key 重试
    const newApiKey = state.keys[state.currentIndex];
    reqBody.api_key = newApiKey;
    
    const retryResp = await fetch("https://api.tavily.com/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(reqBody),
    });
    
    recordUsage();
    
    if (!retryResp.ok) {
      const retryText = await retryResp.text().catch(() => "");
      throw new Error(`Tavily Search failed after retry (${retryResp.status}): ${retryText}`);
    }
    
    return await retryResp.json();
  }
  
  if (!resp.ok) {
    const text = await resp.text().catch(() => "");
    throw new Error(`Tavily Search failed (${resp.status}): ${text}`);
  }
  
  return await resp.json();
}

// Print AI-generated answer if available
if (data.answer) {
  console.log("## Answer\n");
  console.log(data.answer);
  console.log("\n---\n");
}

// Print results
const results = (data.results ?? []).slice(0, n);
console.log("## Sources\n");

for (const r of results) {
  const title = String(r?.title ?? "").trim();
  const url = String(r?.url ?? "").trim();
  const content = String(r?.content ?? "").trim();
  const score = r?.score ? ` (relevance: ${(r.score * 100).toFixed(0)}%)` : "";
  
  if (!title || !url) continue;
  console.log(`- **${title}**${score}`);
  console.log(`  ${url}`);
  if (content) {
    console.log(`  ${content.slice(0, 300)}${content.length > 300 ? "..." : ""}`);
  }
  console.log();
}
