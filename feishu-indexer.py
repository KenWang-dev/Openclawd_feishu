#!/usr/bin/env python3
"""飞书文档索引扫描 - BFS 遍历 + 详情获取 + 写入 Bitable"""
import json, subprocess, sys, time
from datetime import datetime, timezone, timedelta

def main():
    if len(sys.argv) < 3:
        print("用法: python3 feishu-indexer.py <space_id> <space_name> [batch] [max_docs]")
        sys.exit(1)
    
    space_id = sys.argv[1]
    space_name = sys.argv[2]
    batch = sys.argv[3] if len(sys.argv) > 3 else "第1批"
    max_docs = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    
    BASE_TOKEN = "Az2tbTUoJaUdG6s7VLKcB7FXnmq"
    TABLE_ID = "tblotLM0ZUqyXVF7"
    FEISHU_BASE = "https://procurement-leap.feishu.cn"
    tz = timezone(timedelta(hours=8))
    
    print(f"=== 飞书文档索引扫描 ===")
    print(f"知识库: {space_name} ({space_id})")
    print(f"批次: {batch} | 最大文档数: {max_docs or '不限'}")
    print()
    
    # ===== 阶段1: BFS 递归扫描节点 =====
    print("📋 阶段1: 扫描节点树...")
    
    def list_nodes(parent_token, page_token=""):
        params = {"space_id": space_id, "parent_node_token": parent_token}
        if page_token:
            params["page_token"] = page_token
        result = subprocess.run(
            ["lark-cli", "wiki", "nodes", "list", "--params", json.dumps(params)],
            capture_output=True, text=True, timeout=30
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
        time.sleep(0.3)  # API 限流
    
    print(f"  ✅ 扫描完成: {len(all_nodes)} 个节点")
    
    # ===== 阶段2: 获取文档详情并写入 =====
    print()
    print("📊 阶段2: 获取文档详情并写入表格...")
    
    total_docs = 0
    total_chars = 0
    total_blocks = 0
    failed = 0
    
    for node in all_nodes:
        if not node["obj_token"]:
            continue
        
        total_docs += 1
        if max_docs > 0 and total_docs > max_docs:
            print(f"  ⏹️ 达到最大文档数限制 ({max_docs})")
            break
        
        title = node["title"]
        obj_token = node["obj_token"]
        
        try:
            result = subprocess.run(
                ["lark-cli", "docs", "+fetch", "--doc", obj_token,
                 "-q", "{chars: (.data.total_length // 1), blocks: (.data.length // 1)}"],
                capture_output=True, text=True, timeout=30
            )
            info = json.loads(result.stdout)
            char_count = info.get("chars", 0)
            block_count = info.get("blocks", 0)
        except Exception as e:
            char_count = 0
            block_count = 0
            failed += 1
            print(f"  [{total_docs}] {title} ... ❌ {e}")
            continue
        
        total_chars += char_count
        total_blocks += block_count
        
        ct_str = datetime.fromtimestamp(node["created"] / 1000, tz=tz).strftime("%Y/%m/%d %H:%M") if node["created"] > 0 else ""
        mt_str = datetime.fromtimestamp(node["modified"] / 1000, tz=tz).strftime("%Y/%m/%d %H:%M") if node["modified"] > 0 else ""
        
        url = f"{FEISHU_BASE}/wiki/{node['node_token']}"
        
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
        
        try:
            subprocess.run(
                ["lark-cli", "base", "+record-upsert",
                 "--base-token", BASE_TOKEN, "--table-id", TABLE_ID,
                 "--json", json.dumps(record, ensure_ascii=False)],
                capture_output=True, text=True, timeout=15
            )
            print(f"  [{total_docs}] {title} ... ✅ {char_count}字 {block_count}块")
        except Exception:
            failed += 1
            print(f"  [{total_docs}] {title} ... ⚠️ 写入失败")
        
        time.sleep(0.5)  # API 限流
    
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📊 扫描报告")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"知识库: {space_name}")
    print(f"总文档: {total_docs} | 总字符: {total_chars:,} | 总Block: {total_blocks:,}")
    print(f"失败: {failed} | 批次: {batch}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == "__main__":
    main()
