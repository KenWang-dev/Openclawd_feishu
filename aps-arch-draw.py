#!/usr/bin/env python3
"""APS Architecture Diagram - 电子产品制造业APS排产系统架构图"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(24, 16))
ax.set_xlim(0, 24)
ax.set_ylim(0, 16)
ax.axis('off')

# Colors
C_MODULE_BG = {'blue': '#EBF0FA', 'green': '#E8F5E9', 'orange': '#FFF3E0'}
C_HEADER = {'blue': '#1A1A2E', 'green': '#2E7D32', 'orange': '#E65100'}
C_BOX = {'step': '#E8F5E9', 'decision': '#FFF3E0', 'output': '#E3F2FD', 'trigger': '#FCE4EC', 'engine': '#F3E5F5'}
C_BORDER = {'step': '#2E7D32', 'decision': '#E65100', 'output': '#1565C0', 'trigger': '#C62828', 'engine': '#6A1B9A'}
C_ARROW = '#333333'
C_FEEDBACK = '#999999'

def draw_box(ax, x, y, w, h, text, color, border_color, fontsize=9, bold=False):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", 
                         facecolor=color, edgecolor=border_color, linewidth=1.5)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, 
            fontweight=weight, color='#1A1A2E', wrap=True)

def draw_module_bg(ax, x, y, w, h, title, bg_color, header_color, module_num):
    # Background
    bg = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                         facecolor=bg_color, edgecolor=header_color, linewidth=2.5)
    ax.add_patch(bg)
    # Title bar
    title_bg = FancyBboxPatch((x+0.1, y+h-0.7), w-0.2, 0.55, boxstyle="round,pad=0.05",
                               facecolor=header_color, edgecolor=header_color, linewidth=0)
    ax.add_patch(title_bg)
    ax.text(x + w/2, y + h - 0.42, f'{module_num} {title}', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')

def arrow(ax, x1, y1, x2, y2, color=C_ARROW, style='->', lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw))

# ===== MODULE 1: 需求分析 =====
draw_module_bg(ax, 0.5, 11, 7, 4.5, '需求分析 Demand Analysis', C_MODULE_BG['blue'], C_HEADER['blue'], '①')

draw_box(ax, 1.0, 13.5, 2.5, 0.8, '客户订单\nFirm Order', C_BOX['step'], C_BORDER['step'])
draw_box(ax, 4.0, 13.5, 2.5, 0.8, '销售预测\nForecast', C_BOX['step'], C_BORDER['step'])
draw_box(ax, 2.5, 12.2, 2.5, 0.8, '需求汇聚\nConsumption Logic', C_BOX['engine'], C_BORDER['engine'])
arrow(ax, 2.25, 13.5, 3.5, 13.0)
arrow(ax, 5.25, 13.5, 4.0, 13.0)
draw_box(ax, 2.5, 11.2, 2.5, 0.7, '时间栅栏分层\n冰冻/半冰冻/自由区', C_BOX['output'], C_BORDER['output'])
arrow(ax, 3.75, 12.2, 3.75, 11.9)

# ===== MODULE 2: 供需匹配 =====
draw_module_bg(ax, 8.5, 11, 15, 4.5, '供需匹配 Supply-Demand Matching', C_MODULE_BG['green'], C_HEADER['green'], '②')

# 6 steps
steps = [
    ('① 成品库存', C_BOX['step'], C_BORDER['step']),
    ('② 半成品WIP', C_BOX['step'], C_BORDER['step']),
    ('③ 工单在制MO', C_BOX['step'], C_BORDER['step']),
    ('④ 原材料库存\n主仓+边仓+批次', C_BOX['step'], C_BORDER['step']),
    ('⑤ 在途PO', C_BOX['step'], C_BORDER['step']),
    ('⑥ 触发PR', C_BOX['trigger'], C_BORDER['trigger']),
]
for i, (label, color, border) in enumerate(steps):
    x = 9.0 + i * 2.3
    draw_box(ax, x, 13.5, 2.0, 0.9, label, color, border, fontsize=8)
    if i < 5:
        arrow(ax, x+2.0, 13.95, x+2.3, 13.95)

# Decision diamonds (simplified as rounded boxes)
decisions = ['满足?', '满足?', '满足?', '满足?', '满足?']
for i, d in enumerate(decisions):
    x = 9.0 + i * 2.3
    draw_box(ax, x, 12.3, 2.0, 0.5, d, C_BOX['decision'], C_BORDER['decision'], fontsize=7, bold=True)
    if i < 5:
        arrow(ax, x+2.0, 12.55, x+2.3, 12.55)

# YES outputs going down
for i in range(5):
    x = 9.0 + i * 2.3
    ax.text(x+1.0, 12.0, '✅', ha='center', fontsize=8)

# PR → PO cycle
draw_box(ax, 9.0, 11.2, 2.0, 0.7, 'PR→审批→PO', C_BOX['trigger'], C_BORDER['trigger'], fontsize=8)
arrow(ax, 10.0, 13.5, 10.0, 11.9)
draw_box(ax, 11.5, 11.2, 2.5, 0.7, '供应商确认交期', C_BOX['output'], C_BORDER['output'], fontsize=8)
arrow(ax, 11.0, 11.55, 11.5, 11.55)

# ===== MODULE 3: 动态排产 =====
draw_module_bg(ax, 0.5, 0.5, 7, 10, '动态排产 Dynamic Scheduling', C_MODULE_BG['orange'], C_HEADER['orange'], '③')

# Constraints
constraints = [
    '产能约束\n产线/设备/人员/OEE',
    '物料约束\n齐套时间/边仓/容量',
    '工艺约束\nSMT→AOI→组装→测试',
]
for i, c in enumerate(constraints):
    draw_box(ax, 1.0, 8.5 - i*1.2, 2.8, 0.9, c, C_BOX['step'], C_BORDER['step'], fontsize=8)

draw_box(ax, 4.5, 8.5, 2.5, 0.9, '优先级排序\nEDD+评分模型', C_BOX['step'], C_BORDER['step'], fontsize=8)

draw_box(ax, 2.0, 4.5, 3.0, 0.8, '排产引擎', C_BOX['engine'], C_BORDER['engine'], fontsize=10, bold=True)
for i in range(3):
    arrow(ax, 3.8, 8.5 - i*1.2, 3.8, 5.3)
arrow(ax, 5.75, 8.5, 4.5, 5.3)

draw_box(ax, 1.0, 3.2, 2.5, 0.8, '启发式粗排\n30s出案', C_BOX['engine'], C_BORDER['engine'], fontsize=8)
draw_box(ax, 4.0, 3.2, 2.5, 0.8, '遗传算法精排\n10-30min', C_BOX['engine'], C_BORDER['engine'], fontsize=8)
arrow(ax, 3.5, 4.5, 2.25, 4.0)
arrow(ax, 3.5, 4.5, 5.25, 4.0)

draw_box(ax, 2.0, 1.8, 3.0, 0.8, 'What-If 模拟验证', C_BOX['engine'], C_BORDER['engine'], fontsize=8)
arrow(ax, 2.25, 3.2, 3.0, 2.6)
arrow(ax, 5.25, 3.2, 4.0, 2.6)

draw_box(ax, 1.0, 0.7, 5.5, 0.7, '输出: 甘特图 + 备料指令 + 交付承诺', C_BOX['output'], C_BORDER['output'], fontsize=9, bold=True)
arrow(ax, 3.5, 1.8, 3.5, 1.4)

# ===== 串联箭头 =====
# Module 1 → Module 2
arrow(ax, 7.5, 13.5, 8.5, 13.5, C_ARROW, '->', 2.5)
ax.text(8.0, 13.8, '需求量×\n交期×优先级', ha='center', va='center', fontsize=7, color=C_HEADER['blue'], style='italic')

# Module 2 → Module 3
arrow(ax, 12.5, 11.0, 12.5, 10.5, C_ARROW, '->', 2.5)
ax.text(14.2, 10.2, '缺口+建议工单\n可承诺交期CTP\n备料计划PR/PO', ha='center', va='center', fontsize=7, color=C_HEADER['green'], style='italic')
# curve arrow down then left
ax.annotate('', xy=(7.5, 6), xytext=(12.5, 10.5),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=2.5, 
                          connectionstyle='arc3,rad=-0.3'))

# Feedback: Module 3 → Module 2
ax.annotate('', xy=(15, 11.5), xytext=(7.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=C_FEEDBACK, lw=1.5,
                          connectionstyle='arc3,rad=0.4', linestyle='dashed'))
ax.text(13.5, 7.5, '备料指令反馈\n边仓不足阻塞工单', ha='center', va='center',
        fontsize=7, color=C_FEEDBACK, style='italic')

# Feedback: PR → PO loop
ax.annotate('', xy=(9.5, 13.5), xytext=(12.5, 11.55),
            arrowprops=dict(arrowstyle='->', color=C_BORDER['trigger'], lw=1.2,
                          connectionstyle='arc3,rad=0.5', linestyle='dashed'))
ax.text(13.8, 12.5, '交期回填', ha='center', va='center', fontsize=7, color=C_BORDER['trigger'], style='italic')

# Title
ax.text(12, 15.7, '电子产品制造业 APS 排产系统架构图', ha='center', va='center',
        fontsize=18, fontweight='bold', color='#1A1A2E')
ax.text(12, 15.2, '需求驱动 · 分层解耦 · 约束闭环', ha='center', va='center',
        fontsize=11, color='#666666', style='italic')

plt.tight_layout()
plt.savefig('/root/.openclaw/workspace/aps-architecture.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("Architecture diagram saved!")
