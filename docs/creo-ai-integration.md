# AI 直接操作 Creo：方法、原理与落地路径

> **核心结论**：通过 CREOSON（开源 HTTP/JSON 接口）+ MCP Server，AI Agent 可以直接控制 PTC Creo Parametric 执行工程操作，无需 PTC 内核知识，无需闭源 SDK。

---

## 一、为什么 Creo 需要特殊的集成方式

Creo 不同于 Blender、FreeCAD 等开源 CAD 软件。后者拥有完整的 Python API，AI Agent 可以直接调用；Creo 作为商业闭源软件，其自动化接口是封闭且碎片化的：

| 接口 | 语言 | 开放度 | 适用场景 |
|------|------|--------|---------|
| JLink | Java | PTC 官方，免费但笨重 | 深度二次开发 |
| Creo Object TOOLKIT | C++ | 需付费许可证 | 原生插件开发 |
| Web Link | HTTP（功能受限） | 免费但命令少 | 简单任务 |
| Mapkey + Trail | 宏录制 | 免费但极其脆弱 | 不推荐 |
| **CREOSON** | **HTTP/JSON（任意语言）** | **开源免费，150+ 函数** | **推荐方案** |

**关键差异**：Blender 可以用 CLI-Anything 自动分析 Python API 生成命令行接口；Creo 没有开放的 Python API，因此 CLI-Anything 方案不适用。

---

## 二、CREOSON：桥梁

### 2.1 是什么

CREOSON 是由 Simplified Logic, Inc. 开发的开源项目，在 Creo 内部运行一个 Micro-Server，将 Creo 操作封装为标准 HTTP + JSON 接口。

```
AI Agent (Claude Code / 任何 LLM)
    ↕ HTTP POST (JSON)
CREOSON Micro-Server
    ↕ JLink
Creo Parametric
```

### 2.2 核心优势

- **语言无关**：任何能发 HTTP 请求的语言都能用（Python、Node.js、Shell、curl）
- **无需 PTC 内核知识**：150+ 预封装函数，覆盖日常工程操作
- **通配符支持**：批量操作（如批量修改参数、批量导出）一条命令搞定
- **久经考验**：20+ 年工程实践，14000+ 下载，社区活跃
- **已验证 AI 集成**：官方已展示 Claude + MCP + CREOSON 方案

### 2.3 能做什么

| 命令组 | 典型操作 |
|--------|---------|
| 文件操作 | 打开、关闭、保存、另存为、批量重命名 |
| 参数管理 | 读取、设置、删除参数（支持通配符批量） |
| 装配体 | 组件列表、添加/移除组件、装配约束 |
| 绘图 | 创建视图、标注、导出 PDF/DWG |
| 特征 | 列表、抑制/恢复、删除 |
| BOM | 导出物料清单 |
| 层/视图 | 管理、切换、显示控制 |
| 模型信息 | 质量、体积、材料、几何属性 |

---

## 三、落地路径：三步走

### 第一步：安装 CREOSON

1. 从 creoson.com 下载 CREOSON Server（含 Java 运行时）
2. 在 Creo 中注册 CREOSON 插件
3. 启动 Micro-Server（默认监听 29080 端口）

验证安装：
```bash
curl http://localhost:29080/creoson/ -d '{"command":"status"}'
# 返回 {"status":{"success":true,...}}
```

### 第二步：Python 桥接（可选但推荐）

安装 creopyson：
```bash
pip install creopyson
```

如果需要 MCP Server（让 Claude Code 直接调用），编写一个轻量 MCP Server，将 CREOSON 函数暴露为工具调用。核心代码约 50 行。

### 第三步：AI Agent 集成

| 方式 | 复杂度 | 适用 |
|------|--------|------|
| **Python 脚本 + AI 生成** | ★☆☆ | 快速验证、批量自动化 |
| **MCP Server + Claude Code** | ★★☆ | 交互式设计、实时对话 |
| **自定义 Agent 工作流** | ★★★ | 完整自动化流水线 |

---

## 四、与 CLI-Anything + Blender 方案对比

| 维度 | CLI-Anything → Blender | CREOSON → Creo |
|------|----------------------|-----------------|
| 原理 | 自动分析 Python API 生成 CLI | 预封装 HTTP/JSON 接口 |
| 自动化程度 | 全自动（一条命令） | 半自动（需安装 Server） |
| 可靠性 | 实验性，API 变动可能中断 | 生产级，20+ 年验证 |
| 功能覆盖 | 理论上全功能 | 150+ 函数，覆盖核心工程操作 |
| AI 集成 | 通过 CLI stdin/stdout | 通过 HTTP（天然适合 MCP） |

**结论**：不必强套 CLI-Anything 的框架。Creo 的技术栈决定了 CREOSON 是最短路径——HTTP/JSON 是 AI Agent 最自然的通信协议，不需要额外的 CLI 抽象层。

---

## 五、限制与建议

### 已知限制

- CREOSON 依赖 JLink，某些新版 Creo 特性可能尚未封装
- 复杂的参数化建模（如从零创建特征）仍需 Creo 原生 API
- Micro-Server 需要与 Creo 运行在同一台机器上

### 建议

1. **从参数管理和批量操作入手**：这是 CREOSON 最强、ROI 最高的场景
2. **BOM 导出 + AI 分析**：将 Creo BOM 导出后交给 AI 做成本分析、替代料评估
3. **渐进式集成**：先用 Python 脚本验证，再升级为 MCP Server 交互模式
4. **关注 PTC 自身的 AI 进展**：Creo 13（2026年8月发布）已内置 AI Assistant，可作为补充

---

## 参考

- CREOSON 官网：https://creoson.com
- GitHub：https://github.com/SimplifiedLogic/creoson
- Python 库：https://creopyson.readthedocs.io
- CLI-Anything（Blender 方案参考）：https://github.com/HKUDS/CLI-Anything
