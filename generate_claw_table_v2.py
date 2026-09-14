import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "企业级龙虾产品全景图"

# Styles
header_font = Font(name="微软雅黑", bold=True, size=11, color="FFFFFF")
header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

cat_font = Font(name="微软雅黑", bold=True, size=11, color="1F4E79")
cat_fill = PatternFill(start_color="D6E4F0", end_color="D6E4F0", fill_type="solid")

cell_font = Font(name="微软雅黑", size=10)
cell_align = Alignment(vertical="top", wrap_text=True)
thin_border = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"), bottom=Side(style="thin"),
)

headers = [
    "序号", "厂商", "类型", "企业级龙虾产品名", "模型架构/部署方式",
    "安全性", "稳定性", "成本", "风险", "核心功能",
    "客户案例", "备注"
]

for col, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = thin_border

widths = [6, 16, 12, 28, 34, 30, 28, 30, 30, 42, 32, 38]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w

data = [
    # ===== 一、云厂商 =====
    ["一、云厂商", "", "", "", "", "", "", "", "", "", "", ""],
    [1, "阿里云", "云厂商", "百炼专属版（含OpenClaw镜像+Coding Plan）",
     "Qwen3系列+200+多模型接入；云端/私有化部署均可",
     "阿里云企业级安全架构，等保三级；数据本地化可选",
     "高，SLA 99.9%；日均调用增长15倍",
     "推理成本低至0.8元/百万Token；Coding Plan包月免费额度",
     "产品迭代快，文档可能滞后；模型切换需注意兼容性",
     "Agent开发框架ModelStudio-ADK/ADP（高低代码双引擎）、长期记忆库、Deep Research、企业级长记忆、60+工具组件",
     "金融、医疗、电信运营商等高合规行业",
     "2026.3正式推向国际市场；ClawHub技能生态原生支持；国内Agent平台标杆"],
    [2, "阿里云（无影团队）", "云厂商", "JVS Claw",
     "Qwen系列为主+多模型；云端+本地双模式；手机App（iOS/Android/Pad/网页）",
     "云端安全隔离环境ClawSpace；操作全程可控、可人工接管",
     "阿里云基础设施保障",
     "免费体验版+包年包月；内测阶段",
     "尚处内测阶段，功能持续迭代",
     "手机一键养虾（3分钟上手）、自进化万能Skill、ClawSpace实时操作可视化、多端互通、多Agent协同群聊",
     "阿里云生态用户、个人开发者",
     "2026.3.13发布；前身无影JVS，从开发者工具拓展为通用AI智能体产品"],
    [3, "阿里云（Higress团队）", "云厂商", "HiClaw（开源Team版）",
     "基于OpenClaw+Higress AI网关+Matrix IM协议；独立分布式部署",
     "多Agent协作全程审计回溯，人工监督机制完善；Worker仅持临时令牌",
     "企业级协作首选，容器级故障隔离与水平扩展",
     "开源免费，企业部署需自行承担算力",
     "社区生态尚在成长，文档相对少；非阿里官方商业产品",
     "多Agent协同执行（Manager-Worker架构）、人工监督介入、审计回溯、ClawManager集群管理",
     "开源社区，适合中大型企业内部部署",
     "Higress团队开源项目；Manager-Worker高度解耦架构；支持OpenClaw/CoPaw热插拔"],

    # ===== 二、互联网公司 =====
    ["二、互联网公司", "", "", "", "", "", "", "", "", "", "", ""],
    [4, "字节跳动", "互联网", "ArkClaw（火山引擎）",
     "豆包大模型+第三方模型；云上SaaS托管",
     "火山引擎企业级安全方案，AI助手安全全面升级",
     "7×24在线；字节工程能力保障",
     "9.9元/月体验价；Coding Plan订阅制",
     "功能聚焦云端托管，私有化部署弱；字节生态绑定深",
     "一键云端部署、Coze 2.0工作流、扣子空间任务拆解、Vibe Coding",
     "字节生态用户、中小企业",
     "2026.3.9上线；与Coze/飞书深度联动"],
    [5, "字节跳动", "互联网", "HiAgent 2.0（火山引擎）",
     "豆包模型+多模型；企业级私有化部署",
     "企业级安全合规",
     "高，支撑字节内部大规模使用",
     "企业级定价，需商务洽谈",
     "功能较重，学习曲线陡",
     '"1+N+X"智能体工作站、AgentKit企业级Agent平台、MCP生态、全链路观测、长短记忆管理',
     "企业级客户（金融、运营商等）",
     "2025 Force大会发布2.0；与ArkClaw定位互补（HiAgent偏深度企业，ArkClaw偏轻量托管）"],
    [6, "腾讯", "互联网", "WorkBuddy（腾讯云CodeBuddy团队）",
     "混合模型接入；本地安装+云端协同",
     "基于CodeBuddy统一账号和安全审计体系",
     "公测阶段；打通企微/QQ/飞书/钉钉",
     "新用户送5000积分；公测免费",
     "公测阶段功能可能不完善",
     "AI一号员工定位、OpenClaw技能兼容、多渠道接入（企微/QQ/飞书/钉钉）、远程操控电脑",
     "腾讯云生态企业",
     "2026.3.9上线公测；与QClaw形成双轨"],
    [7, "腾讯", "互联网", "ADP Agent Portal（腾讯云智能体开发平台）",
     "混合模型接入；云端平台",
     "企业级Agent治理方案成熟；统一纳管分散AI使用行为",
     "腾讯云基础设施",
     "企业级定价",
     "跨系统流程自动化需搭配第三方RPA",
     "统一入口/调度/监控/治理、OpenClaw纳管、与微信/企微/腾讯会议无缝集成",
     "已深度使用腾讯云的企业",
     "腾讯云TokenHub全栈式产品矩阵；Agent治理方案成熟"],
    [8, "百度", "互联网", "DuClaw（百度智能云）",
     "文心大模型+DeepSeek/Kimi/GLM/MiniMax；全托管云端",
     "百度云企业级安全",
     "百度云基础设施保障",
     "17.8元首月体验；全托管零部署",
     "预发布/早期阶段；百度文库/搜索生态绑定",
     "零部署、内置百度搜索/百科/学者、企业微信/钉钉/飞书接入规划",
     "百度智能云大客户",
     "2026.3.11发布；尚处早期"],
    [9, "百度", "互联网", "千帆AppBuilder",
     "文心大模型为主+200+模型；云端部署",
     "等保三级+企业级安全",
     "累计构建超130万Agents",
     "推理成本行业较低；免费额度+节省计划",
     "模型生态封闭倾向",
     "Agent Infra全栈、Deep Research、企业级长记忆（跨Agent共享）、60+工具组件、RAG检索",
     "金融、政务、制造、零售",
     "国内Agent平台标杆；2025.10品牌升级整合AppBuilder+ModelBuilder"],

    # ===== 三、大模型公司 =====
    ["三、大模型公司", "", "", "", "", "", "", "", "", "", "", ""],
    [10, "智谱AI（GLM）", "大模型", "GLM-Claw",
     "GLM-5-Turbo/5.1为主；云端托管",
     "数据本地化存储、敏感数据加密、实时可视化监控",
     "智谱云基础设施",
     "体验月卡39元/3500万Token；进阶99元/1亿Token",
     "2026年API涨价20%；对原生ClawHub兼容度一般",
     '"一群懂你的AI虾兵"多智能体协同、统一调度、企业级安全管理',
     "中小企业+个人开发者",
     '2026.3发布；从纯API转为"数字员工"订阅模式；Coding Plan免费额度'],
    [11, "智谱AI", "大模型", "AutoClaw（澳龙）",
     "GLM模型+AutoGLM浏览器操作；本地一键安装",
     "本地部署，数据不出端",
     "依赖本地硬件",
     "下载免费，模型调用按量",
     "本地部署需硬件支持",
     "内置50+ Skills、AutoGLM浏览器自动化操作、一键安装",
     "个人开发者",
     "2026.3发布；国内首款一键安装的本地OpenClaw客户端"],
    [12, "月之暗面（Kimi）", "大模型", "KimiClaw",
     "Kimi K2.5/K2.6万亿参数模型；云端托管",
     "云端安全，40GB专属存储",
     "24/7云端在线",
     "Kimi会员内含；付费用户月增80倍，ARR破1亿美元",
     "不支持私有化部署；渠道以官方App为主",
     "零部署浏览器端、企业级搜索（Pro-Grade Search）、实时数据挂载、Grounding降幻觉",
     "月之暗面生态用户",
     "2026.2中旬上线；v1.8.0（2026.3）；20天收入超去年全年"],
    [13, "MiniMax", "大模型", "MaxClaw（MiniMax Agent）",
     "MiniMax M2.5多模态模型；云端SaaS",
     "MiniMax企业级安全",
     "7×24在线",
     "MiniMax订阅制；ARPPU $73（Agent产品最高）",
     "早期产品，功能持续迭代",
     "一键云端部署、多Agent协作、子Agent垂直领域专家团、Vibe Coding",
     "50,000+企业客户（全球90+国家）",
     "2026.2.26发布；与腾讯云战略合作部署Agent RL沙箱；已港股上市"],

    # ===== 四、硬件/通信厂商 =====
    ["四、硬件/通信厂商", "", "", "", "", "", "", "", "", "", "", ""],
    [14, "浪潮信息", "硬件", "企千虾",
     "基于元脑服务器本地化部署；元脑x86服务器+元脑AI服务器分离架构；深度融合ClawManager",
     "沙箱隔离+底层管控；所有实例安全沙箱运行，宿主机零风险；CSV批量导入用户+配额分配",
     "金融级稳定性；K8s原生架构支撑数千实例集群管理",
     "一体机采购+软件授权；商务定价",
     "需企业自备K8s环境和算力硬件；非OpenClaw生态原生产品",
     "数千OpenClaw实例一键批量部署、集群统一升级、Skills一键迁移、全生命周期集中管理、分钟级自动化交付",
     "金融、运营商、大型企业（私有化部署场景）",
     "2026.4.2发布；业界首个企业级OpenClaw方案；开源ClawManager为龙虾管家"],
    [15, "中兴通讯", "硬件/通信", "Co-Claw企业版（含AI一体机）",
     "多模型接入；AiCube一体机/云电脑/内网部署",
     "五维安全防护体系（从下载到审计）；每10分钟自动健康检查并修复；全调用链穿透审计",
     "高稳定性；从个人工具到企业生产力基础设施的系统性重构",
     "商务定价；一体机模式降低TCO",
     "产品较新，生态尚在建设中",
     "一键安装、OA/ERP深度对接、飞书/钉钉集成、MaaS与Skill广场跨部门共享、数据不出户",
     "政企客户、通信行业",
     "2026.2上线企业版；2026.4.9发布Co-Claw AI一体机；强调可控安全规模化"],

    # ===== 五、其它AI应用厂商 =====
    ["五、其它AI应用厂商", "", "", "", "", "", "", "", "", "", "", ""],
    [16, "Dify", "AI应用", "Dify企业版",
     "开源框架，兼容100+ LLM；私有化/云端均可",
     "开源可控、等保三级+ISO27001",
     "GitHub高星开源项目；社区活跃",
     "社区版免费；企业版需商务",
     "大规模分布式部署运维有挑战",
     "可视化工作流编排、RAG检索、Multi-Agent协同、全栈LLMOps、Prompt IDE",
     "百度千帆集成、电商/客服标杆",
     "国产AI框架明星；2026已发布企业版"],
    [17, "金智维", "AI应用", "Ki-AgentS",
     "多模型接入；企业级私有化部署",
     "等保三级+ISO27001；金融级安全",
     "连续三年中国AI数字员工市场份额第一",
     "商务定价",
     "产品偏RPA+AI融合，纯Agent能力相对弱",
     "RPA+AI融合、金融级稳定性、嵌入银行核心交易系统、每秒千笔指令",
     "国有六大行、1300+政企客户",
     "RPA老牌厂商转型AI Agent；金融行业首选"],
    [18, "BetterYeah", "AI应用", "BetterYeah AI",
     "自研多模型接入；私有化/云端",
     "等保三级+ISO27001、五层安全防护",
     "服务近10万企业团队、亿级任务调用量",
     "商务定价",
     "品牌知名度低于大厂",
     "NeuroFlow可视化工作流、VisionRAG多模态知识库、100+模型接入、Multi-Agent协同",
     "百丽国际800+节点、添可客服提效22倍",
     "2026平台测评得分较高"],
]

row = 2
for item in data:
    if isinstance(item[0], str) and (item[0].startswith("一、") or item[0].startswith("二、") or item[0].startswith("三、") or item[0].startswith("四、") or item[0].startswith("五、")):
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=12)
        cell = ws.cell(row=row, column=1, value=item[0])
        cell.font = cat_font
        cell.fill = cat_fill
        cell.alignment = Alignment(horizontal="left", vertical="center")
        cell.border = thin_border
        for c in range(2, 13):
            ws.cell(row=row, column=c).fill = cat_fill
            ws.cell(row=row, column=c).border = thin_border
        ws.row_dimensions[row].height = 24
    else:
        for col, val in enumerate(item, 1):
            cell = ws.cell(row=row, column=col, value=val)
            cell.font = cell_font
            cell.alignment = cell_align
            cell.border = thin_border
        ws.row_dimensions[row].height = 90
    row += 1

ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:L{row-1}"

output_path = "/root/.openclaw/workspace/国内企业级龙虾产品全景图_20260424_v2.xlsx"
wb.save(output_path)
print(f"Saved to {output_path}")
