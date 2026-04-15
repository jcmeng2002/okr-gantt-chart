# -*- coding: utf-8 -*-
"""
OKR甘特图 - 腾讯品牌风格
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# ==================== 腾讯品牌配色方案 ====================
TENCENT_BLUE = '#0052D9'
TENCENT_BLUE_LIGHT = '#4DA1FF'
TENCENT_BLUE_DARK = '#1A3C6E'
TENCENT_BLUE_PALE = '#D6E8FF'
TENCENT_ORANGE = '#FA8C16'
TENCENT_GREEN = '#52C41A'
TENCENT_PURPLE = '#722ED1'

BG_COLOR = '#FFFFFF'
TEXT_COLOR = '#262626'
SUB_TEXT_COLOR = '#595959'
GRID_COLOR = '#E8E8E8'

# 设置中文字体 - 使用系统可用字体
plt.rcParams['font.family'] = ['STHeiti', 'Songti SC', 'Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

# ==================== 任务数据定义 ====================
# 基于OKR文档的3个阶段，总时长约4个月（约17周）
# 阶段1: 2周 | 阶段2: 2周 | 阶段3: 12-13周(约3个月)
# 假设从第1周开始

tasks = [
    # ====== 阶段1: HR管理机制了解 (第1-2周) ======
    {'name': '阶段1: HR管理机制了解', 'phase': 1, 'start': 0, 'duration': 2, 'color': TENCENT_BLUE, 'is_header': True},
    {'name': '  1.1 HRBP能力要求与职责学习', 'phase': 1, 'start': 0, 'duration': 2, 'color': TENCENT_BLUE_LIGHT},
    {'name': '  1.2 招聘及编制管理规则', 'phase': 1, 'start': 0.2, 'duration': 1.6, 'color': TENCENT_BLUE_LIGHT},
    {'name': '  1.3 组织架构/潜龙/晋升/360评估规则', 'phase': 1, 'start': 0.3, 'duration': 1.7, 'color': TENCENT_BLUE_LIGHT},
    {'name': '  1.4 绩效及通道管理（目标制定/考核/面谈）', 'phase': 1, 'start': 0.4, 'duration': 1.6, 'color': TENCENT_BLUE_LIGHT},
    {'name': '  1.5 培养体系现状了解', 'phase': 1, 'start': 0.8, 'duration': 1.2, 'color': TENCENT_BLUE_LIGHT},
    {'name': '  1.6 文化体系与荣誉激励表彰体系', 'phase': 1, 'start': 1.0, 'duration': 1.0, 'color': TENCENT_BLUE_LIGHT},

    # ====== 阶段2: 业务了解 (第3-4周) ======
    {'name': '阶段2: AMS业务了解', 'phase': 2, 'start': 2, 'duration': 2, 'color': TENCENT_ORANGE, 'is_header': True},
    {'name': '  2.1 参加AMS新人培训课程', 'phase': 2, 'start': 2, 'duration': 1.5, 'color': '#FFB84D'},
    {'name': '  2.2 深入了解支持部门业务及组织信息', 'phase': 2, 'start': 2.2, 'duration': 1.8, 'color': '#FFB84D'},
    {'name': '  2.3 了解微信广告部产运/TAD业务', 'phase': 2, 'start': 2.5, 'duration': 1.5, 'color': '#FFB84D'},

    # ====== 阶段3: 在岗实践与独立产出 (第5-17周, 约3个月) ======
    {'name': '阶段3: 在岗实践、独立产出', 'phase': 3, 'start': 4, 'duration': 13, 'color': TENCENT_GREEN, 'is_header': True},
    
    # O1 交付物
    {'name': '  【O1交付】广告业务学习报告', 'phase': 3, 'start': 4, 'duration': 4, 'color': '#95DE64'},
    {'name': '  【O1交付】流量平台(WXG)学习报告', 'phase': 3, 'start': 5, 'duration': 3, 'color': '#95DE64'},
    
    # O2 交付物
    {'name': '  【O2交付】AI产品经理演进思考报告', 'phase': 3, 'start': 5, 'duration': 5, 'color': '#B7EB8F'},
    {'name': '  【O2交付】设计职能演进思考报告', 'phase': 3, 'start': 6, 'duration': 5, 'color': '#B7EB8F'},
    {'name': '  【O2交付】大评估等日常工作交付', 'phase': 3, 'start': 4, 'duration': 12, 'color': '#BFE5E2'},  # 持续性工作
    
    # O3 AI专项
    {'name': '  【O3-AI】熟悉腾讯/S3在AI应用发展', 'phase': 3, 'start': 4, 'duration': 4, 'color': TENCENT_PURPLE, 'alpha': 0.7},
    {'name': '  【O3-AI】选取HR场景+AI流程再造探索', 'phase': 3, 'start': 7, 'duration': 6, 'color': '#B995F0', 'alpha': 0.7},
    {'name': '  【O3-AI】AI专项产出交付', 'phase': 3, 'start': 12, 'duration': 4, 'color': '#D5BBF3', 'alpha': 0.8},
    
    # 日常BP工作
    {'name': '  协助BP落地业务部门相关工作', 'phase': 3, 'start': 4, 'duration': 12, 'color': '#BAE7FF'},  # 持续性
]

# ==================== 绑制甘特图 ====================
fig, ax = plt.subplots(figsize=(18, 14), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

total_weeks = 17  # 总共约17周

# Y轴：任务列表（反转顺序，让第一个任务在上面）
y_positions = list(range(len(tasks), 0, -1))
task_names = [t['name'] for t in tasks]

# 绘制每个任务条
for i, task in enumerate(tasks):
    y = len(tasks) - i - 1
    start = task['start']
    duration = task['duration']
    color = task.get('color', TENCENT_BLUE)
    alpha = task.get('alpha', 1.0)
    is_header = task.get('is_header', False)
    
    if is_header:
        # 阶段标题行 - 用粗体条形
        bar_height = 0.75
        rect = FancyBboxPatch(
            (start, y - bar_height / 2), duration, bar_height,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            facecolor=color, edgecolor='none', alpha=0.9,
            linewidth=0
        )
        ax.add_patch(rect)
        # 白色文字
        ax.text(start + duration / 2, y, f"{int(duration)}周",
                ha='center', va='center', fontsize=10, fontweight='bold',
                color='white')
    else:
        # 子任务条形
        bar_height = 0.55
        # 渐变效果用透明度模拟
        rect = FancyBboxPatch(
            (start, y - bar_height / 2), duration, bar_height,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            facecolor=color, edgecolor='none', alpha=alpha,
            linewidth=0
        )
        ax.add_patch(rect)
        
        # 在长条上显示周数
        if duration >= 2:
            ax.text(start + duration / 2, y, f"{duration}w",
                    ha='center', va='center', fontsize=8, fontweight='bold',
                    color=TENCENT_BLUE_DARK if alpha > 0.75 else TEXT_COLOR)

# ==================== 坐标轴设置 ====================
# X轴：周数
ax.set_xlim(-0.5, total_weeks + 0.5)
ax.set_ylim(-0.6, len(tasks))

# X轴标签
weeks = list(range(0, total_weeks + 1))
week_labels = [f'W{w}' for w in weeks]
ax.set_xticks(weeks)
ax.set_xticklabels(week_labels, fontsize=10, color=SUB_TEXT_COLOR)

# Y轴标签（任务名称）
ax.set_yticks(list(range(len(tasks))))
ytick_labels = ax.set_yticklabels(task_names, fontsize=10.5, color=TEXT_COLOR)
for i, t in enumerate(tasks):
    if t.get('is_header'):
        ytick_labels[i].set_fontweight('bold')

# 网格线（仅垂直）
for w in range(total_weeks + 1):
    ax.axvline(x=w, color=GRID_COLOR, linewidth=0.5, zorder=0)

# 阶段分隔线（虚线）
phase_lines = [(2, '第2周末\n阶段1→2'), (4, '第4周末\n阶段2→3')]
for x, label in phase_lines:
    ax.axvline(x=x, color=TENCENT_BLUE_DARK, linewidth=1.5, linestyle='--', alpha=0.5, zorder=1)
    ax.text(x, len(tasks) - 0.3, label, ha='center', va='bottom', fontsize=8,
            color=TENCENT_BLUE_DARK, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=TENCENT_BLUE_PALE, edgecolor='none', alpha=0.6))

# 标题
ax.set_title('AMS HRBP OKR 具体规划时间线甘特图\n（总周期：约17周 / 约4个月）',
             fontsize=18, fontweight='bold', color=TENCENT_BLUE_DARK, pad=20)

ax.set_xlabel('时间线（周）', fontsize=12, color=SUB_TEXT_COLOR, labelpad=10)
ax.set_ylabel('任务清单', fontsize=12, color=SUB_TEXT_COLOR, labelpad=10)

# 移除边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_color(GRID_COLOR)

# ==================== 图例 ====================
legend_elements = [
    mpatches.Patch(facecolor=TENCENT_BLUE, edgecolor='none', label='阶段1: HR管理机制了解（W1-W2, 2周）'),
    mpatches.Patch(facecolor=TENCENT_ORANGE, edgecolor='none', label='阶段2: AMS业务了解（W3-W4, 2周）'),
    mpatches.Patch(facecolor=TENCENT_GREEN, edgecolor='none', label='阶段3: 在岗实践、独立产出（W5-W17, ~3个月）'),
    mpatches.Patch(facecolor=TENCENT_PURPLE, edgecolor='none', alpha=0.7, label='O3-HR AI任务探索落地'),
]
leg = ax.legend(handles=legend_elements, loc='upper right', fontsize=9.5,
                frameon=True, facecolor='#FAFAFA', edgecolor=GRID_COLOR,
                bbox_to_anchor=(1.0, 1.0))

# ==================== 底部里程碑标注 ====================
milestones = [
    (2, '阶段1完成', TENCENT_BLUE),
    (4, '阶段2完成', TENCENT_ORANGE),
    (8, 'O1/O2报告初稿', TENCENT_GREEN),
    (12, 'AI流程再造方案', TENCENT_PURPLE),
    (16, '全部交付完成', TENCENT_BLUE_DARK),
]

for mx, ml, mc in milestones:
    ax.plot(mx, -0.35, marker='v', markersize=10, color=mc, zorder=5)
    ax.text(mx, -0.48, ml, ha='center', va='top', fontsize=8, color=mc, fontweight='bold')

# 调整布局
plt.tight_layout()
plt.subplots_adjust(bottom=0.08)

# 保存
output_path = '/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart.png'
plt.savefig(output_path, dpi=200, bbox_inches='tight', 
            facecolor=BG_COLOR, edgecolor='none')
print(f"甘特图已保存至: {output_path}")
