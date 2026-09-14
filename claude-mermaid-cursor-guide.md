# 安装 claude-mermaid（Mermaid 图表渲染能力）

## 安装步骤

**1. 全局安装 claude-mermaid**

打开终端，运行：

```bash
npm install -g claude-mermaid
```

> 如果下载 Chromium 失败（国内网络），先设置镜像再装：
> ```bash
> PUPPETEER_DOWNLOAD_HOST=https://registry.npmmirror.com/mirrors/chromium-browser-snapshots npm install -g claude-mermaid
> ```

**2. 配置 Cursor 的 MCP**

找到 Cursor 的 MCP 配置文件：
- macOS: `~/.cursor/mcp.json`
- Windows: `%APPDATA%\Cursor\User\globalStorage\mcp.json`

在文件中添加以下内容（如果文件已有内容，把 `claude-mermaid` 部分合并到 `mcpServers` 中即可）：

```json
{
  "mcpServers": {
    "claude-mermaid": {
      "command": "claude-mermaid"
    }
  }
}
```

**3. 重启 Cursor**

完全退出 Cursor 再重新打开，让 MCP Server 生效。

## 使用方法

安装完成后，你可以直接在 Cursor 中要求 Claude 画图，例如：

- "帮我画一个用户注册流程图"
- "画一个微服务架构图"
- "用 mermaid 画一个 ER 图"
- "把这个系统设计画成时序图"

Claude 会自动调用 claude-mermaid 渲染图表并在浏览器中预览。

## 支持的图表类型

| 类型 | 说明 | 示例 |
|------|------|------|
| flowchart | 流程图 | 业务流程、决策树 |
| sequence | 时序图 | API 调用顺序、用户交互 |
| class | 类图 | 代码架构、对象关系 |
| er | ER 图 | 数据库设计 |
| gantt | 甘特图 | 项目排期 |
| mindmap | 思维导图 | 知识整理、头脑风暴 |
| state | 状态图 | 状态机、生命周期 |
| pie | 饼图 | 数据占比 |

## 验证是否安装成功

在 Cursor 中输入：

```
画一个简单的流程图测试一下：开始 -> 处理 -> 结束
```

如果能在浏览器中看到渲染出的图表，说明安装成功。

## 常见问题

**Q: 渲染报错 "Failed to launch the browser process"**
A: macOS 一般不会遇到。Linux 用户需要确保安装了 Chromium 依赖：
```bash
sudo apt install -y libnss3 libatk-bridge2.0-0 libdrm2 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2 libxshmfence1
```

**Q: 国内安装很慢或失败**
A: 使用镜像源：
```bash
PUPPETEER_DOWNLOAD_HOST=https://registry.npmmirror.com/mirrors/chromium-browser-snapshots npm install -g claude-mermaid
```

**Q: Cursor 里 MCP 列表看不到 claude-mermaid**
A: 确认 mcp.json 格式正确，然后完全退出 Cursor（不是最小化）再重开。
