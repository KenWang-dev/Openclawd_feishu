#!/bin/bash
# 飞书文档索引扫描脚本 v3
# 用法: bash feishu-indexer.sh <space_id> <space_name> [batch] [max_docs]
set -euo pipefail

SPACE_ID="${1:?用法: $0 <space_id> <space_name> [batch] [max_docs]}"
SPACE_NAME="$2"
BATCH="${3:-第1批}"
MAX_DOCS="${4:-0}"

BASE_TOKEN="Az2tbTUoJaUdG6s7VLKcB7FXnmq"
TABLE_ID="tblotLM0ZUqyXVF7"
LOG="/tmp/feishu-indexer-${SPACE_ID}.log"
FEISHU_BASE="https://procurement-leap.feishu.cn"

TMPNODES=$(mktemp)
trap "rm -f $TMPNODES" EXIT

echo "=== 飞书文档索引扫描 ==="
echo "知识库: $SPACE_NAME ($SPACE_ID)"
echo "批次: $BATCH | 最大文档数: $([ $MAX_DOCS -gt 0 ] && echo $MAX_DOCS || echo '不限')"
echo ""

# ===== 阶段1: BFS 递归扫描节点 =====
echo "📋 阶段1: 扫描节点树..."

# 用 Python 处理整个 BFS，避免 bash 管道符冲突
python3 << 'PYEOF' "$SPACE_ID" "$TMPNODES" >> "$LOG" 2>&1
import json, subprocess, sys

space_id = sys.argv[1]
outfile = sys.argv[2]

def list_nodes(parent_token, page_token=""):
    params = {"space_id": space_id, "parent_node_token": parent_token}
    if page_token:
        params["page_token"] = page_token
    result = subprocess.run(
        ["lark-cli", "wiki", "nodes", "list", "--params", json.dumps(params)],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    items = data.get("data", {}).get("items", [])
    next_page = data.get("data", {}).get("page_token", "")
    return items, next_page

# BFS
queue = [("", "", 0)]  # (parent_token, parent_path, depth)
all_nodes = []

while queue:
    parent_token, parent_path, depth = queue.pop(0)
    
    page_token = ""
    while True:
        items, page_token = list_nodes(parent_token, page_token)
        for item in items:
            nt = item.get("node_token", "")
            ot = item.get("obj_token", "")
            t = item.get("title", "")
            oty = item.get("obj_type", "")
            hc = item.get("has_child", False)
            ct = item.get("node_created_time", 0)
            mt = item.get("node_modified_time", 0)
            cr = item.get("creator", "")
            cn = cr.get("name", "") if isinstance(cr, dict) else str(cr)
            
            # 计算当前路径
            cp = parent_path
            if t:
                cp = f"{cp} / {t}" if cp else t
            
            all_nodes.append({
                "node_token": nt, "obj_token": ot, "title": t,
                "obj_type": oty, "has_child": hc, "created": ct,
                "modified": mt, "creator": cn, "depth": depth, "path": cp
            })
            
            if hc:
                queue.append((nt, cp, depth + 1))
        
        if not page_token:
            break

# 写入文件（用制表符分隔，避免管道符问题）
with open(outfile, "w", encoding="utf-8") as f:
    for n in all_nodes:
        f.write("\t".join(str(n.get(k, "")) for k in [
            "node_token", "obj_token", "title", "obj_type",
            "has_child", "created", "modified", "creator", "depth", "path"
        ]) + "\n")

print(f"扫描完成: {len(all_nodes)} 个节点", file=sys.stderr)
PYEOF

total_nodes=$(wc -l < "$TMPNODES")
echo "  ✅ 扫描完成: $total_nodes 个节点"

# ===== 阶段2: 获取文档详情并写入 =====
echo ""
echo "📊 阶段2: 获取文档详情并写入表格..."

python3 << 'PYEOF2' "$BASE_TOKEN" "$TABLE_ID" "$SPACE_NAME" "$SPACE_ID" "$BATCH" "$FEISHU_BASE" "$MAX_DOCS" "$TMPNODES"
import json, subprocess, sys
from datetime import datetime, timezone, timedelta

base_token = sys.argv[1]
table_id = sys.argv[2]
space_name = sys.argv[3]
space_id = sys.argv[4]
batch = sys.argv[5]
feishu_base = sys.argv[6]
max_docs = int(sys.argv[7])
nodes_file = sys.argv[8]

tz = timezone(timedelta(hours=8))

# 读取节点
nodes = []
with open(nodes_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 10:
            nodes.append({
                "node_token": parts[0], "obj_token": parts[1], "title": parts[2],
                "obj_type": parts[3], "has_child": parts[4], "created": int(parts[5]),
                "modified": int(parts[6]), "creator": parts[7], "depth": int(parts[8]),
                "path": parts[9]
            })

total_docs = 0
total_chars = 0
total_blocks = 0
failed = 0

for node in nodes:
    if not node["obj_token"]:
        continue
    
    total_docs += 1
    if max_docs > 0 and total_docs > max_docs:
        print(f"  ⏹️ 达到最大文档数限制 ({max_docs})")
        break
    
    title = node["title"]
    obj_token = node["obj_token"]
    
    # 获取文档详情
    try:
        result = subprocess.run(
            ["lark-cli", "docs", "+fetch", "--doc", obj_token,
             "-q", "{chars: (.data.total_length // 1), blocks: (.data.length // 1)}"],
            capture_output=True, text=True, timeout=30
        )
        info = json.loads(result.stdout)
        char_count = info.get("chars", 0)
        block_count = info.get("blocks", 0)
    except Exception:
        char_count = 0
        block_count = 0
        failed += 1
        print(f"  [{total_docs}] {title} ... ❌")
        continue
    
    total_chars += char_count
    total_blocks += block_count
    
    # 日期格式化
    ct_str = datetime.fromtimestamp(node["created"] / 1000, tz=tz).strftime("%Y/%m/%d %H:%M") if node["created"] > 0 else ""
    mt_str = datetime.fromtimestamp(node["modified"] / 1000, tz=tz).strftime("%Y/%m/%d %H:%M") if node["modified"] > 0 else ""
    
    url = f"{feishu_base}/wiki/{node['node_token']}"
    
    record = {
        "文档标题": title,
        "知识库名称": space_name,
        "知识库ID": space_id,
        "文件夹路径": node["path"],
        "文档类型": node["obj_type"],
        "字符数": char_count,
        "Block数": block_count,
        "创建时间": ct_str,
        "最后编辑时间": mt_str,
        "URL": url,
        "文档Token": obj_token,
        "节点Token": node["node_token"],
        "扫描批次": batch,
        "层级深度": node["depth"]
    }
    
    # 写入记录
    try:
        subprocess.run(
            ["lark-cli", "base", "+record-upsert",
             "--base-token", base_token, "--table-id", table_id,
             "--json", json.dumps({"fields": record}, ensure_ascii=False)],
            capture_output=True, text=True, timeout=15
        )
        print(f"  [{total_docs}] {title} ... ✅ {char_count}字 {block_count}块")
    except Exception:
        failed += 1
        print(f"  [{total_docs}] {title} ... ⚠️ 写入失败")

print("")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"📊 扫描报告")
print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"知识库: {space_name}")
print(f"总文档: {total_docs} | 总字符: {total_chars} | 总Block: {total_blocks}")
print(f"失败: {failed} | 批次: {batch}")
print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
PYEOF2
