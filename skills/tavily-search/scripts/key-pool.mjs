#!/usr/bin/env node
/**
 * Tavily API Key 循环池管理器
 * 自动切换到下一个 Key，当当前 Key 使用次数达到 950 次
 */

import fs from 'fs';
import path from 'path';

const ENV_FILE = path.join(process.cwd(), '../.env');
const POOL_FILE = path.join(process.cwd(), 'key-pool.json');
const SWITCH_THRESHOLD = 950;

// 加载 .env
function loadEnv() {
  const envContent = fs.readFileSync(ENV_FILE, 'utf-8');
  const keys = {};
  envContent.split('\n').forEach(line => {
    const match = line.match(/^(TAVILY_KEY_\d+)=(.+)$/);
    if (match) {
      keys[match[1]] = match[2].trim();
    }
  });
  return Object.values(keys).filter(k => k);
}

// 获取/初始化 Key 池状态
function getPoolState() {
  if (!fs.existsSync(POOL_FILE)) {
    const keys = loadEnv();
    const state = {
      keys: keys,
      currentIndex: 0,
      usageCount: 0,
      lastReset: new Date().toISOString().split('T')[0]
    };
    fs.writeFileSync(POOL_FILE, JSON.stringify(state, null, 2));
    return state;
  }
  
  const state = JSON.parse(fs.readFileSync(POOL_FILE, 'utf-8'));
  
  // 每天重置计数器
  const today = new Date().toISOString().split('T')[0];
  if (state.lastReset !== today) {
    state.usageCount = 0;
    state.lastReset = today;
    savePoolState(state);
  }
  
  return state;
}

function savePoolState(state) {
  fs.writeFileSync(POOL_FILE, JSON.stringify(state, null, 2));
}

// 获取当前可用的 Key
export function getApiKey() {
  const state = getPoolState();
  
  // 检查是否需要切换 Key
  if (state.usageCount >= SWITCH_THRESHOLD) {
    state.currentIndex = (state.currentIndex + 1) % state.keys.length;
    state.usageCount = 0;
    console.error(`[Key Pool] 切换到 Key ${state.currentIndex + 1} (使用次数: ${state.usageCount})`);
    savePoolState(state);
  }
  
  return state.keys[state.currentIndex];
}

// 记录使用次数（每次 API 调用后调用）
export function recordUsage() {
  const state = getPoolState();
  state.usageCount++;
  savePoolState(state);
}

// 获取当前状态
export function getStatus() {
  const state = getPoolState();
  return {
    currentKey: state.keys[state.currentIndex]?.slice(0, 15) + '...',
    currentIndex: state.currentIndex + 1,
    totalKeys: state.keys.length,
    usageCount: state.usageCount,
    lastReset: state.lastReset
  };
}

// CLI 模式
if (import.meta.url === `file://${process.argv[1]}`) {
  const cmd = process.argv[2];
  
  if (cmd === 'get') {
    console.log(getApiKey());
  } else if (cmd === 'record') {
    recordUsage();
    console.log('Usage recorded');
  } else if (cmd === 'status') {
    const s = getStatus();
    console.log(JSON.stringify(s, null, 2));
  } else {
    console.log('Usage: key-pool.mjs [get|record|status]');
  }
}
