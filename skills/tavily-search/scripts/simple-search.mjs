#!/usr/bin/env node
/**
 * Simple Tavily search without key pool
 */

import { getApiKey, recordUsage } from './key-pool.mjs';

const query = process.argv[2];
if (!query) {
  console.error('Usage: simple-search.mjs "query"');
  process.exit(1);
}

console.log("Query:", query);

// Try to get key directly from env
const apiKey = process.env.TAVILY_API_KEY_1 || getApiKey();

if (!apiKey) {
  console.error("No Tavily API Key available");
  process.exit(1);
}

console.log("Using API key...");

const body = {
  api_key: apiKey,
  query: query,
  max_results: 10,
  include_answer: true
};

fetch("https://api.tavily.com/search", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(body)
})
.then(async (resp) => {
  const text = await resp.text();
  console.log("Response status:", resp.status);
  
  if (!resp.ok) {
    throw new Error(`Tavily Search failed (${resp.status}): ${text}`);
  }
  
  const data = JSON.parse(text);
  
  // Print AI-generated answer
  if (data.answer) {
    console.log("\n## Answer\n");
    console.log(data.answer);
    console.log("\n---\n");
  }
  
  // Print results
  const results = (data.results || []).slice(0, 10);
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
})
.catch(err => {
  console.error("Error:", err.message);
  process.exit(1);
});