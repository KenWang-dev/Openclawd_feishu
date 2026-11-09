# Semantica 供应链知识图谱 POC
from semantica.kg import KnowledgeGraph, GraphBuilderWithProvenance
from semantica.ontology import OntologyEngine, SHACLGenerator, OWLGenerator
from semantica.provenance import ProvenanceManager

entities = [
    # 物料
    {"id": "MAT-CHIP", "label": "主控芯片 MCU-A1", "type": "Material", "props": {"category": "电子"}},
    {"id": "MAT-RES", "label": "贴片电阻 R10K", "type": "Material", "props": {"category": "电子"}},
    {"id": "MAT-CONN", "label": "连接器 CN-8P", "type": "Material", "props": {"category": "结构件"}},
    {"id": "MAT-BATT", "label": "锂电池 5000mAh", "type": "Material", "props": {"category": "电池"}},
    {"id": "MAT-ALT-CHIP", "label": "主控芯片 MCU-B2(替代)", "type": "Material", "props": {}},
    {"id": "MAT-CASE", "label": "外壳铝件", "type": "Material", "props": {}},
    # 供应商
    {"id": "SUP-TSM", "label": "台积供应商 A", "type": "Supplier", "props": {"country": "TW", "fin_risk": "low"}},
    {"id": "SUP-X", "label": "单一来源商 X(高财务风险)", "type": "Supplier", "props": {"country": "CN", "fin_risk": "high", "debt_ratio": 0.91}},
    {"id": "SUP-Y", "label": "电池供应商 Y", "type": "Supplier", "props": {"country": "JP", "fin_risk": "medium"}},
    {"id": "SUP-Z", "label": "连接器供应商 Z", "type": "Supplier", "props": {"country": "CN", "fin_risk": "low"}},
    {"id": "SUP-W", "label": "替代芯片供应商 W", "type": "Supplier", "props": {"country": "CN", "fin_risk": "low"}},
    {"id": "SUP-C", "label": "外壳供应商 C", "type": "Supplier", "props": {"country": "CN", "fin_risk": "low"}},
    # 工厂
    {"id": "FAC-SZ", "label": "深圳组装厂", "type": "Factory", "props": {"loc": "深圳"}},
    {"id": "FAC-VN", "label": "越南组装厂", "type": "Factory", "props": {"loc": "北宁"}},
    # BOM/成品
    {"id": "PROD-S1", "label": "智能手表 S1", "type": "Product", "props": {}},
    {"id": "PROD-G2", "label": "网关设备 G2", "type": "Product", "props": {}},
    {"id": "BOM-S1", "label": "BOM-S1 v3.2", "type": "BOM", "props": {"version": "3.2"}},
    {"id": "BOM-G2", "label": "BOM-G2 v1.1", "type": "BOM", "props": {"version": "1.1"}},
    # 订单
    {"id": "ORD-1001", "label": "订单#1001 (S1×10k)", "type": "Order", "props": {"qty": 10000, "due": "2026-12-15"}},
    {"id": "ORD-1002", "label": "订单#1002 (G2×5k)", "type": "Order", "props": {"qty": 5000, "due": "2026-11-30"}},
    # 风险事件 / 物流
    {"id": "EVT-FIN", "label": "供应商X债务违约风险事件", "type": "RiskEvent", "props": {"sev": "high", "date": "2026-11-01"}},
    {"id": "EVT-PORT", "label": "红海航运中断事件", "type": "RiskEvent", "props": {"sev": "medium", "date": "2026-10-20"}},
    {"id": "LANE-RED", "label": "红海-盐田航线", "type": "LogisticsLane", "props": {"status": "disrupted"}},
    {"id": "LANE-ALT", "label": "中欧班列备选", "type": "LogisticsLane", "props": {"status": "normal"}},
]

# 60+ 关系：supply, sourced_by, includes(物料), produced_at, defines, orders, triggers, affects, transits, alternate, depends_on
rels = [
    # 供应商→物料
    {"subject": "SUP-TSM", "object": "MAT-CHIP", "relationship_type": "SUPPLIES"},
    {"subject": "SUP-X",   "object": "MAT-BATT", "relationship_type": "SUPPLIES"},
    {"subject": "SUP-Y",   "object": "MAT-RES", "relationship_type": "SUPPLIES_SECONDARY"},
    {"subject": "SUP-Z",   "object": "MAT-CONN", "relationship_type": "SUPPLIES"},
    {"subject": "SUP-W",   "object": "MAT-ALT-CHIP", "relationship_type": "SUPPLIES"},
    {"subject": "SUP-C",   "object": "MAT-CASE", "relationship_type": "SUPPLIES"},
    # 替代料
    {"subject": "MAT-CHIP", "object": "MAT-ALT-CHIP", "relationship_type": "HAS_ALTERNATE", "properties": {"pin_compatible": True}},
    {"subject": "MAT-BATT", "object": "MAT-CONN", "relationship_type": "NO_ALTERNATE", "properties": {"note": "验证中"}},  # 反例：显式标注
    # BOM 定义
    {"subject": "BOM-S1", "object": "MAT-CHIP", "relationship_type": "INCLUDES", "properties": {"qty": 1}},
    {"subject": "BOM-S1", "object": "MAT-BATT", "relationship_type": "INCLUDES", "properties": {"qty": 1}},
    {"subject": "BOM-S1", "object": "MAT-CASE", "relationship_type": "INCLUDES", "properties": {"qty": 1}},
    {"subject": "BOM-S1", "object": "MAT-CONN", "relationship_type": "INCLUDES", "properties": {"qty": 2}},
    {"subject": "BOM-G2", "object": "MAT-CHIP", "relationship_type": "INCLUDES", "properties": {"qty": 2}},
    {"subject": "BOM-G2", "object": "MAT-RES",  "relationship_type": "INCLUDES", "properties": {"qty": 40}},
    {"subject": "BOM-G2", "object": "MAT-CONN", "relationship_type": "INCLUDES", "properties": {"qty": 4}},
    # 成品↔BOM
    {"subject": "PROD-S1", "object": "BOM-S1", "relationship_type": "USES_BOM"},
    {"subject": "PROD-G2", "object": "BOM-G2", "relationship_type": "USES_BOM"},
    {"subject": "PROD-S1", "object": "MAT-BATT", "relationship_type": "DEPENDS_ON"},
    {"subject": "PROD-S1", "object": "MAT-CHIP", "relationship_type": "DEPENDS_ON"},
    {"subject": "PROD-G2", "object": "MAT-CHIP", "relationship_type": "DEPENDS_ON"},
    # 工厂
    {"subject": "FAC-SZ", "object": "PROD-S1", "relationship_type": "PRODUCES"},
    {"subject": "FAC-VN", "object": "PROD-S1", "relationship_type": "PRODUCES_BACKUP"},
    {"subject": "FAC-SZ", "object": "PROD-G2", "relationship_type": "PRODUCES"},
    {"subject": "FAC-SZ", "object": "MAT-CASE", "relationship_type": "RECEIVES_FROM", "o": "SUP-C"},
    # 订单
    {"subject": "ORD-1001", "object": "PROD-S1", "relationship_type": "ORDERS"},
    {"subject": "ORD-1002", "object": "PROD-G2", "relationship_type": "ORDERS"},
    {"subject": "ORD-1001", "object": "FAC-SZ", "relationship_type": "ASSIGNED_TO"},
    {"subject": "ORD-1002", "object": "FAC-SZ", "relationship_type": "ASSIGNED_TO"},
    # 风险事件
    {"subject": "EVT-FIN",  "object": "SUP-X", "relationship_type": "RISK_OF"},
    {"subject": "EVT-FIN",  "object": "MAT-BATT", "relationship_type": "THREATENS"},
    {"subject": "EVT-FIN",  "object": "PROD-S1", "relationship_type": "IMPACTS"},
    {"subject": "EVT-FIN",  "object": "ORD-1001", "relationship_type": "JEOPARDIZES"},
    {"subject": "EVT-PORT", "object": "LANE-RED", "relationship_type": "CAUSES"},
    {"subject": "LANE-RED", "object": "SUP-Z", "relationship_type": "CARRIES"},
    {"subject": "LANE-RED", "object": "MAT-CONN", "relationship_type": "DISRUPTS"},
    {"subject": "EVT-PORT", "object": "PROD-S1", "relationship_type": "IMPACTS"},
    {"subject": "LANE-ALT", "object": "LANE-RED", "relationship_type": "FALLBACK_FOR"},
    # 采购来源关系 (supplier→factory supply path)
    {"subject": "SUP-X", "object": "FAC-SZ", "relationship_type": "SHIPS_TO"},
    {"subject": "SUP-Z", "object": "FAC-SZ", "relationship_type": "SHIPS_TO"},
    {"subject": "SUP-TSM", "object": "FAC-SZ", "relationship_type": "SHIPS_TO"},
    {"subject": "SUP-W", "object": "FAC-SZ", "relationship_type": "SHIPS_TO"},
    {"subject": "SUP-Y", "object": "FAC-VN", "relationship_type": "SHIPS_TO"},
    {"subject": "MAT-ALT-CHIP", "object": "BOM-S1", "relationship_type": "APPROVED_FOR", "properties": {"ecr": "ECR-2026-077"}},
    {"subject": "MAT-CASE", "object": "BOM-S1", "relationship_type": "APPROVED_FOR"},
    {"subject": "SUP-X", "object": "SUP-Y", "relationship_type": "RISK_SHARES", "properties": {"note": "同行业敞口"}},
    {"subject": "PROD-G2", "object": "MAT-CONN", "relationship_type": "DEPENDS_ON"},
    {"subject": "PROD-G2", "object": "MAT-RES", "relationship_type": "DEPENDS_ON"},
    {"subject": "ORD-1001", "object": "LANE-RED", "relationship_type": "USES_LANE"},
]

prov = ProvenanceManager(storage_path="poc_prov.db")
for e_ in entities:
    prov.track_entity(entity_id=e_["id"], source="POC模拟数据(supply_chain_poc.py)", agent_id="ken-poc", metadata={"entity_type": e_["type"]})
gb = GraphBuilderWithProvenance(provenance=True, agent_id="ken-poc")
graph = gb.build(sources={"entities": entities, "relationships": rels})
graph = {"entities": graph["entities"] if isinstance(graph, dict) else graph["entities"],
         "relationships": graph["relationships"] if isinstance(graph, dict) else graph["relationships"]}
print('entities:', len(graph['entities']), 'relationships:', len(graph['relationships']))

# —— 保存 KnowledgeGraph 快照 ——
kg = KnowledgeGraph(entities=graph["entities"], relationships=graph["relationships"])

# —— 本体：从图数据推断 ontology，导出 SHACL / OWL ——
oe = OntologyEngine()
onto = oe.from_data({
    "entities": graph["entities"],
    "relationships": graph["relationships"],
})
classes = onto.get("classes", [])
props = onto.get("properties", onto.get("object_properties", []))
print("ontology classes:", len(classes), [c.get("name") if isinstance(c, dict) else c for c in classes][:10])
shacl = oe.to_shacl(onto, format="turtle")
print("SHACL turtle len:", len(shacl))
print("\n".join(shacl.splitlines()[:12]))
owl = oe.to_owl(onto, format="turtle")
print("OWL turtle len:", len(owl))
rep = oe.quality_check(onto) if hasattr(oe, "quality_check") else None
print("quality:", str(rep)[:200])

# —— 多跳查询：哪些成品依赖“单一来源 + 高财务风险”供应商的物料 ——
import collections
supply = collections.defaultdict(list)   # material -> [suppliers]
for r in graph["relationships"]:
    if r.get("relationship_type") in ("SUPPLIES", "SUPPLIES_SECONDARY"):
        supply[r["object"]].append(r["subject"])

single_source_high = []
for mat, sups in supply.items():
    high = [s for s in sups if any((e.get("props") or {}).get("fin_risk") == "high" for e in graph["entities"] if e["id"] == s)]
    if len(sups) <= 1 and high:
        single_source_high.append((mat, high[0]))

# 传播：material -> BOM -> Product
def products_using(mat):
    out = set()
    for r in graph["relationships"]:
        if r.get("relationship_type") == "INCLUDES" and r["object"] == mat:
            for r2 in graph["relationships"]:
                if r2.get("relationship_type") == "USES_BOM" and r2["object"] == r["subject"]:
                    out.add(r2["subject"])
    return out

print("\n=== 单一来源×高风险供应商 影响分析 ===")
for mat, sup in single_source_high:
    prods = products_using(mat)
    orders = [r["subject"] for r in graph["relationships"] if r.get("relationship_type") == "ORDERS" and r["object"] in prods]
    print(f"物料 {mat} ← 单一供应商 {sup}(高风险) → 影响成品 {sorted(prods)} → 受威胁订单 {sorted(orders)}")

# 替代料缓解
print("\n=== 替代料缓解路径 ===")
for r in graph["relationships"]:
    if r.get("relationship_type") == "HAS_ALTERNATE":
        print(f"{r['subject']} → 替代 {r['object']} (pin_compatible={(r.get('properties') or r.get('props') or {}).get('pin_compatible')})")

# —— 溯源 ——
print("\nProvenanceManager api:", [x for x in dir(prov) if not x.startswith('_')])
for meth in ("get_entity_provenance", "get_provenance", "query"):
    if hasattr(prov, meth):
        try:
            raw = getattr(prov, meth)("MAT-BATT")
        except TypeError:
            try: entries = getattr(prov, meth)(entity_id="MAT-BATT")
            except Exception as e: entries = [("err", str(e))]
        break
print("=== MAT-BATT 溯源 ===")
if isinstance(raw, dict):
    print("entity_id:", raw.get("entity_id"), "| source:", raw.get("source_document"), "| agent:", raw.get("agent_id"))
    print("checksum:", raw.get("checksum"), "| integrity_verified:", raw.get("integrity_verified"))
    print("prov fields:", sorted(raw.keys())[:15], "...")
    print("溯源字段总数:", len(raw))
else:
    print(raw)
    entries = prov.get_lineage("MAT-BATT")
    print("lineage chain len:", len(entries.get("lineage_chain", [])), "| sources:", entries.get("source_documents"))
# (export_prov 到 RDF json 需要 rdflib json-ld 插件，见报告"坑")
