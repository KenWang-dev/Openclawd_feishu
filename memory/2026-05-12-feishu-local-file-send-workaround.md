# 飞书发送本地文件 — message tool 的坑及解决方案

**日期：** 2026-05-12
**场景：** 尝试通过 OpenClaw 的 message tool 发送本地文件到飞书

## 问题分析

message tool 的 `filePath` 参数无法直接用于发送本地文件。调用链如下：

```
message(filePath="/root/xxx.pdf")
  → feishu provider 的 sendMedia(mediaUrl="/root/xxx.pdf")
    → loadWebMedia(mediaUrl)  // 尝试从 URL 下载
      → 失败：/root/... 不是有效 URL
        → fallback：只发送了文件路径文本，而不是文件本身
```

**根本原因：** `filePath` 被当作 `mediaUrl` 处理，而 `loadWebMedia` 只能下载 HTTP(S) URL，不支持本地文件路径。

## 解决方案

需要分两步走：**先上传获取 file_key，再用 file_key 发送。**

### 步骤 1：上传文件到飞书

```bash
lark-cli im files create --file /root/xxx.pdf --file-type pdf
# 返回 file_key
```

### 步骤 2：用 file_key 发送消息

```bash
lark-cli im messages send \
  --receive-id-type chat_id \
  --receive-id <chat_id> \
  --msg-type file \
  --content '{"file_key":"<file_key>"}'
```

## 注意事项

- **message tool 的 `filePath` 只支持 HTTP URL**，本地路径会被误当作 URL 导致静默失败（fallback 发文本）
- 发送本地文件必须先通过飞书 IM File API 上传获取 file_key
- 这是 OpenClaw message tool 在飞书渠道的已知限制，非 bug 而是设计如此
- lark-cli 的底层能力可以绕过这个限制
