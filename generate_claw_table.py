import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "企业级龙虾产品全景图"

# Header style
header_font = Font(name="微软雅黑", bold=True, size=11, color="FFFFFF")
header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Category fill
cat_font = Font(name="微软雅黑", bold=True, size=11, color="1F4E79")
cat_fill = PatternFill(start_color="D6E4F0", end_color="D6E4F0", fill_type="solid")

# Cell style
cell_font = Font(name="微软雅黑", size=10)
cell_align = Alignment(vertical="top", wrap_text=True)
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)

# Headers
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

# Column widths
widths = [6, 14, 10, 26, 32, 30, 28, 28, 28, 40, 30, 36]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w

# Data
data = [
    # 云厂商
    ["一、云厂商", "", "", "", "", "", "", "", "", "", "", ""],
    [1, "阿里云", "云厂商", "百炼专属版（含OpenClaw镜像）",
     "Qwen3系列+多模型接入；云端/私有化部署均可",
     "阿里云企业级安全架构，等保三级；数据本地化可选",
     "高，SLA 99.9%；日均调用增长15倍",
     "推理成本低至0.8元/百万Token；Coding Plan包月免费额度",
     "产品迭代快，文档可能滞后；模型切换需注意兼容性",
     "Agent开发框架ModelStudio-ADK/ADP（高低代码双引擎）、长期记忆库、Deep Research、企业级长记忆",
     "金融、医疗、电信运营商等高合规行业",
     "2026.3正式推向国际市场；ClawHub技能生态原生支持"],
    [2, "阿里云（Higress团队）", "云厂商", "HiClaw",
     "基于OpenClaw+Higress AI网关+Matrix IM协议；独立分布式部署",
     "多Agent协作全程审计回溯，人工监督机制完善",
     "企业级协作首选，稳定性高",
     "开源免费，企业部署需自行承担算力",
     "社区生态尚在成长，文档相对少",
     "多Agent协同执行、人工监督介入、审计回溯、任务分配",
     "开源社区，适合中大型企业内部部署",
     "非阿里官方商业产品，是Higress团队开源项目；底层集成OpenClaw"],

    # 互联网公司
    ["二、互联网公司", "", "", "", "", "", "", "", "", "", "", ""],
    [3, "字节跳动", "互联网", "ArkClaw（火山引擎）",
     "豆包大模型+第三方模型；云上SaaS托管",
     "火山引擎企业级安全方案，AI助手安全全面升级",
     "7×24在线；字节工程能力保障",
     "9.9元/月体验价；Coding Plan订阅制",
     "功能聚焦云端托管，私有化部署弱；字节生态绑定深",
     "一键云端部署、Coze 2.0工作流、扣子空间任务拆解、Vibe Coding",
     "字节生态用户、中小企业",
     "2026.3.9上线；与Coze/飞书深度联动"],
    [4, "字节跳动", "互联网", "HiAgent 2.0（火山引擎）",
     "豆包模型+多模型；企业级私有化部署",
     "企业级安全合规",
     "高，支撑字节内部大规模使用",
     "企业级定价，需商务洽谈",
     "功能较重，学习曲线陡",
     '"1+N+X"智能体工作站、AgentKit企业级Agent平台、MCP生态、全链路观测',
     "企业级客户（金融、运营商等）",
     "2025 Force大会发布2.0；与ArkClaw定位互补"],
    [5, "腾讯", "互联网", "WorkBuddy（腾讯云CodeBuddy团队）",
     "混合模型接入；本地安装+云端协同",
     "基于CodeBuddy统一账号和安全审计体系",
     "公测阶段；打通企微/QQ/飞书/钉钉",
     "新用户送5000积分；公测免费",
     "公测阶段功能可能不完善",
     "AI一号员工定位、OpenClaw技能兼容、多渠道接入（企微/QQ/飞书/钉钉）、远程操控电脑",
     "腾讯云生态企业",
     "2026.3.9上线公测；与QClaw形成双轨"],
    [6, "腾讯", "互联网", "QClaw（腾讯电脑管家团队）",
     "OpenClaw商业化封装；本地安装",
     "腾讯安全体系",
     "公测中",
     "公测免费",
     "定位偏个人，企业级功能待验证",
     "微信远程操控电脑、扫码绑定、手机操控桌面Agent",
     "个人用户为主",
     '2026.3.9上线；"微信遥控版龙虾"'],
    [7, "百度", "互联网", "DuClaw（百度智能云）",
     "文心大模型+DeepSeek/Kimi/GLM/MiniMax；全托管云端",
     "百度云企业级安全",
     "百度云基础设施保障",
     "17.8元首月体验；全托管零部署",
     "预发布/早期阶段；百度文库/搜索生态绑定",
     "零部署、内置百度搜索/百科/学者、企业微信/钉钉/飞书接入规划",
     "百度智能云大客户",
     "2026.3.11发布；尚处早期"],
    [8, "百度", "互联网", "千帆AppBuilder",
     "文心大模型为主+200+模型；云端部署",
     "等保三级+企业级安全",
     "累计构建超130万Agents",
     "推理成本行业较低；免费额度+节省计划",
     "模型生态封闭倾向",
     "Agent Infra全栈、Deep Research、企业级长记忆、60+工具组件、RAG检索",
     "金融、政务、制造、零售",
     "国内Agent平台标杆；百度独家能力整合"],

    # 大模型公司
    ["三、大模型公司", "", "", "", "", "", "", "", "", "", "", ""],
    [9, "智谱AI（GLM）", "大模型", "GLM-Claw",
     "GLM-5-Turbo/5.1为主；云端托管",
     "数据本地化存储、敏感数据加密、实时可视化监控",
     "智谱云基础设施",
     "体验月卡39元/3500万Token；进阶99元/1亿Token",
     "2026年API涨价20%；对原生ClawHub兼容度一般",
     '"一群懂你的AI虾兵"多智能体协同、统一调度、企业级安全管理',
     "中小企业+个人开发者",
     '2026.3发布；从纯API转为"数字员工"订阅模式'],
    [10, "智谱AI", "大模型", "AutoClaw（澳龙）",
     "GLM模型+AutoGLM浏览器操作；本地一键安装",
     "本地部署，数据不出端",
     "依赖本地硬件",
     "下载免费，模型调用按量",
     "本地部署需硬件支持",
     "内置50+ Skills、AutoGLM浏览器自动化操作、一键安装",
     "个人开发者",
     "2026.3发布；国内首款一键安装的本地OpenClaw客户端"],
    [11, "月之暗面（Kimi）", "大模型", "KimiClaw",
     "Kimi K2.5/K2.6万亿参数模型；云端托管",
     "云端安全，40GB专属存储",
     "24/7云端在线",
     "Kimi会员内含；付费用户月增80倍",
     "不支持私有化部署；渠道以官方App为主",
     "零部署浏览器端、企业级搜索（Pro-Grade Search）、实时数据挂载、Grounding降幻觉",
     "月之暗面生态用户",
     "2026.2中旬上线；v1.8.0（2026.3）"],
    [12, "MiniMax", "大模型", "MaxClaw（MiniMax Agent）",
     "MiniMax M2.5多模态模型；云端SaaS",
     "MiniMax企业级安全",
     "7×24在线",
     "MiniMax订阅制；ARPPU $73（Agent产品最高）",
     "早期产品，功能持续迭代",
     "一键云端部署、多Agent协作、子Agent垂直领域专家团、Vibe Coding",
     "50,000+企业客户（全球90+国家）",
     "2026.2.26发布；与腾讯云战略合作部署Agent RL沙箱"],

    # 硬件厂商
    ["四、硬件厂商", "", "", "", "", "", "", "", "", "", "", ""],
    [13, "浪潮信息", "硬件", "元脑企智EPAI",
     "支持多元算力芯片（昇腾等）；一体机+私有化部署",
     "数据本地化、权限控制、加解密",
     "金融级稳定性；每秒上千笔指令",
     "一体机采购+软件授权；商务定价",
     "软件平台能力弱于纯云厂商；偏底层算力",
     "端到端AI开发（数据处理→模型训练→部署服务）、算力协同优化、多元算力芯片适配",
     "金融（国有六大行）、运营商、高校",
     "非OpenClaw生态产品，但为企业级AI Agent基础设施；2026推广EPAI一体机"],
    [14, "浪潮信息", "硬件", "AIStation",
     "支持主流大模型；企业级训练推理平台",
     "企业级安全",
     "面向训练推理场景",
     "软件授权+硬件绑定",
     "偏训练推理平台，非Agent应用层",
     "模型开发/训练/部署/测试全流程、统一资源管理、大模型推理加速",
     "金融、运营商",
     "与EPAI互补；AIStation做底层推理，EPAI做上层应用"],

    # 其它AI应用厂商
    ["五、其它AI应用厂商", "", "", "", "", "", "", "", "", "", "", ""],
    [15, "Dify", "AI应用", "Dify企业版",
     "开源框架，兼容100+ LLM；私有化/云端均可",
     "开源可控、等保三级+ISO27001",
     "GitHub高星开源项目；社区活跃",
     "社区版免费；企业版需商务",
     "大规模分布式部署运维有挑战",
     "可视化工作流编排、RAG检索、Multi-Agent协同、全栈LLMOps、Prompt IDE",
     "百度千帆集成、电商/客服标杆",
     "国产AI框架明星；2026已发布企业版"],
    [16, "金智维", "AI应用", "Ki-AgentS",
     "多模型接入；企业级私有化部署",
     "等保三级+ISO27001；金融级安全",
     "连续三年中国AI数字员工市场份额第一",
     "商务定价",
     "产品偏RPA+AI融合，纯Agent能力相对弱",
     "RPA+AI融合、金融级稳定性、嵌入银行核心交易系统、每秒千笔指令",
     "国有六大行、1300+政企客户",
     "RPA老牌厂商转型AI Agent；金融行业首选"],
    [17, "BetterYeah", "AI应用", "BetterYeah AI",
     "自研多模型接入；私有化/云端",
     "等保三级+ISO27001、五层安全防护",
     "服务近10万企业团队、亿级任务调用量",
     "商务定价",
     "品牌知名度低于大厂",
     "NeuroFlow可视化工作流、VisionRAG多模态知识库、100+模型接入、Multi-Agent协同",
     "百丽国际800+节点、添可客服提效22倍",
     "2026平台测评得分较高"],
]

# Write data
row = 2
for item in data:
    if isinstance(item[0], str) and (item[0].startswith("一、") or item[0].startswith("二、") or item[0].startswith("三、") or item[0].startswith("四、") or item[0].startswith("五、")):
        # Category row
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
        ws.row_dimensions[row].height = 80
    row += 1

# Freeze header
ws.freeze_panes = "A2"

# Auto filter
ws.auto_filter.ref = f"A1:L{row-1}"

output_path = "/root/.openclaw/workspace/国内企业级龙虾产品全景图_20260424.xlsx"
wb.save(output_path)
print(f"Saved to {output_path}")
