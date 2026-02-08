# 📋 待办事项 - Ken

## 技术类

### 🔑 OpenRouter API Key 创建
- **状态**：⏸️ 待处理
- **优先级**：P3（低）
- **描述**：解决 OpenRouter 创建 API Key 时的 403 错误
- **当前问题**：
  - 创建 API Key 时报错："应用程序错误：发生客户端异常"
  - 控制台显示 403 Forbidden：`/api/frontend/organization/users`
  - 账户正常，能访问 Settings 页面
- **可能原因**：
  - 需要先绑定支付方式
  - 需要最小充值（$5-10）
  - 新账户验证要求
- **下一步**：检查 Billing 页面，确认是否需要充值
- **创建时间**：2026-02-06

### 🔧 OpenClaw 浏览器连接配置
- **状态**：⏸️ 待处理
- **优先级**：P2（中）
- **描述**：配置 OpenClaw Chrome 扩展，实现浏览器自动化数据抓取
- **所需步骤**：
  1. 用户安装 OpenClaw Chrome 扩展
  2. 用户访问 https://hq.smm.cn/ 并连接标签页
  3. 测试抓取 SMM 金属价格数据
  4. 封装为自动化脚本
- **预期收益**：可直接抓取登录后的网页数据，解决 SMM 价格获取问题
- **创建时间**：2026-02-03

---

## 数据源类

### 🌐 SMM 数据源优化
- **状态**：⏸️ 待处理
- **优先级**：P1（高）
- **描述**：优化上海有色网数据抓取，获取完整金属价格
- **当前问题**：
  - 部分页面需要登录
  - 价格数据动态加载
  - 有反爬虫机制
- **备选方案**：
  1. Cookies 认证（需用户提供）
  2. 浏览器自动化（需连接 Chrome）
  3. 付费数据源（聚源、Wind 等）
- **创建时间**：2026-02-03

---

## 依赖配置类

### 📦 Python 数据分析依赖
- **状态**：✅ 已完成
- **描述**：安装 pandas, matplotlib, seaborn
- **安装版本**：
  - pandas: 3.0.0
  - matplotlib: 3.10.8
  - seaborn: 0.13.2
- **安装时间**：2026-02-03
- **备注**：csv-data-summarizer 技能现已可用

### 🔬 deep-research 使用建议
- **状态**：⏸️ 暂不推荐使用
- **描述**：Token 成本过高，建议手动研究
- **详细建议**：见 `skills/data-analysis/deep-research/USAGE-ADVICE.md`
- **Ken 的反馈**：一次跑300个网页，承受不了
- **推荐替代**：手动研究 + 轻量级技能组合
- **创建时间**：2026-02-03

---

## 技能开发类

### 🌐 英语学习程序出海计划
- **状态**：⏸️ 规划中
- **优先级**：P1（高）
- **描述**：英语学习程序升级为出海产品
- **依赖**：英语学习程序（已完成）
- **技术栈**：
  - 数据库：Supabase
  - 部署：Vercel
  - 支付：待定（Stripe/PayPal）
- **功能清单**：
  - [ ] 接入 Supabase 数据库（用户数据、学习记录）
  - [ ] 开发个人网页（Landing Page）
  - [ ] 部署到 Vercel
  - [ ] 用户注册/登录页面
  - [ ] 支付功能集成
  - [ ] 出海合规准备
- **战略意义**：
  - 验证 AI Coding 完整产品流程
  - 积累出海经验
  - 探索商业化可能性
- **创建时间**：2026-02-06

### 📊 procurement-daily-report
- **状态**：⏸️ 规划中
- **优先级**：P1（高）
- **描述**：创建采购日报生成技能
- **依赖**：metal-price-tracker
- **功能**：
  - 汇总金属价格
  - 整合市场资讯
  - 生成洞察分析
  - 支持定时推送
- **创建时间**：2026-02-03

---

## 已完成 ✅

- [x] metal-price-tracker 技能创建
- [x] 技能体系框架建立
- [x] weather 技能每日定时任务
- [x] awesome-claude-skills 仓库克隆
- [x] invoice-organizer 技能转换（P1）
- [x] content-research-writer 技能转换（P1）
- [x] file-organizer 技能转换（P2）
- [x] internal-comms 技能转换（P2）
- [x] pdf 技能转换（document-processing）
- [x] csv-data-summarizer 技能转换（P2，外部仓库）
- [x] deep-research 技能转换（P1，外部仓库）

---

*最后更新：2026-02-06*
