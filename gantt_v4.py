#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMS HRBP OKR 甘特图 V4 - 整合+倒序+紧凑版
- 整合时间相近的培训学习任务
- 按结束时间倒序排列（先完成的在上面）
- 紧凑布局，确保完整显示
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from datetime import datetime, timedelta

# ─── 1. 腾讯体字体加载 ────────────────────────────────
FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
try:
    from matplotlib.font_manager import FontProperties
    tencent_font = FontProperties(fname=FONT_PATH)
    plt.rcParams['font.family'] = 'sans-serif'
    print(f"✅ 腾讯体已加载: TencentSans")
except Exception:
    from matplotlib.font_manager import FontProperties
    tencent_font = FontProperties(family='Arial')
    print("⚠️ 腾讯体加载失败，使用Arial")

# ─── 2. 任务定义（整合后 + 按结束日期倒序排列） ───
# 格式: (名称, 开始周偏移(0=4/14), 持续周数, 阶段颜色键, 里程碑信息)
tasks_data = [
    # ===== 阶段3：长期并行任务（最晚结束的放最上面）=====
    ("AI专项产出[By月]",           5,  12, "green",  "By Month"),
    ("大评估日常工作[By Case]",     3,  14, "green",  "By Case"),
    ("协助BP落地日常工作",          2,  15, "green",  None),
    ("设计职能演进思考报告",        1,   3, "green",  "5/17完成"),
    ("AI产品经理演进思考报告",      1,   3, "green",  "5/17完成"),
    
    # ===== 阶段2：业务了解 =====
    ("深入了解工作内容/情况",       2,   2, "orange", None),
    ("深入了解部门业务(WXG/TAD)",  1,   3, "orange", None),
    ("AMS新人培训课程",            0,   2, "orange", None),
    
    # ===== 阶段1：HR管理机制（整合后）=====
    ("计算广告课程&教材学习",      0,   2, "blue",   "4/26报告"),
    ("HRBP职责与课程体系\n(招聘/组织/绩效/培养/文化)", 
                                      0,   2, "blue",   None),
]

# ─── 3. 时间参数 ───────────────────────────────────────
START_DATE = datetime(2026, 4, 14)  # W1 起始
WEEKS_TOTAL = 18  # 显示范围

# ─── 4. 绘图设置 ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(20, 13), dpi=120)

# 颜色方案
colors = {
    "blue":   "#0052D9",
    "orange": "#ED7B2F", 
    "green":  "#00A870",
}
light_colors = {
    "blue":   "#E6F0FF",
    "orange": "#FFF3E8",
    "green":  "#E8F8F0",
}

n_tasks = len(tasks_data)

# 绘制每个任务条（已按结束日期倒序，所以索引0就是最上面的）
for i, (name, week_offset, duration, color_key, milestone) in enumerate(tasks_data):
    start_day = week_offset * 7
    end_day = (week_offset + duration) * 7
    
    # Y坐标：倒序后 i=0 在顶部
    y = n_tasks - 1 - i
    
    # 背景（阶段色带）
    bg_start = max(0, start_day - 2)
    bg_end = min(WEEKS_TOTAL * 7, end_day + 10)
    ax.axhspan(y - 0.45, y + 0.45, xmin=bg_start/(WEEKS_TOTAL*7), 
               xmax=bg_end/(WEEKS_TOTAL*7),
               facecolor=light_colors[color_key], alpha=0.5, zorder=0)
    
    # 主条形
    bar = FancyBboxPatch(
        (start_day, y - 0.32), end_day - start_day, 0.64,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor=colors[color_key], edgecolor='white', linewidth=0.8, zorder=3
    )
    ax.add_patch(bar)
    
    # 条形内文字（居中显示）
    mid_x = (start_day + end_day) / 2
    if milestone and duration >= 2:
        label_text = f"{name}\n({milestone})"
    else:
        label_text = name
    
    fontsize = 11 if len(name) > 12 else 12
    ax.text(mid_x, y, label_text, ha='center', va='center',
            fontproperties=tencent_font, fontsize=fontsize, color='white',
            fontweight='bold', zorder=4,
            linespacing=1.2)

# ─── 5. X轴：周数+具体日期 ────────────────────────────
week_starts = []
week_labels = []
for w in range(WEEKS_TOTAL):
    wdate = START_DATE + timedelta(days=w*7)
    wend = wdate + timedelta(days=6)
    week_starts.append(w * 7)
    week_labels.append(f"W{w+1}\n{wdate.strftime('%m/%d')}")

ax.set_xticks(week_starts)
ax.set_xticklabels(week_labels, fontproperties=tencent_font, fontsize=9)
ax.set_xlim(-3, WEEKS_TOTAL * 7 + 5)

# ─── 6. Y轴：任务名（左侧显示完整） ──────────────────
# 标签也要倒序，与条形的 y=n_tasks-1-i 对应
y_labels = [t[0] for t in tasks_data]  # 数据已按结束时间倒序
y_positions = [n_tasks - 1 - i for i in range(n_tasks)]  # 倒序Y坐标，匹配条形位置
ax.set_yticks(y_positions)
ax.set_yticklabels(y_labels, fontproperties=tencent_font, fontsize=11)
ax.set_ylim(-0.7, n_tasks - 0.3)

# ─── 7. 阶段分隔线 & 标注 ─────────────────────────────
phase_lines = [
    (14, "阶段1"),   # ~W3初结束
    (28, "阶段2"),   # ~W5末结束  
]
for day_x, phase_name in phase_lines:
    ax.axvline(x=day_x, color='#CCCCCC', linestyle='--', linewidth=1.2, 
               alpha=0.7, zorder=2)
    ax.text(day_x + 1, n_tasks - 0.35, phase_name, 
            fontproperties=tencent_font, fontsize=14, fontweight='bold',
            color=['#0052D9', '#ED7B2F'][phase_lines.index((day_x, phase_name))],
            alpha=0.85, va='top')

# 阶段3标注
ax.text(WEEKS_TOTAL * 7 - 5, n_tasks - 0.35, "阶段3",
        fontproperties=tencent_font, fontsize=14, fontweight='bold',
        color='#00A870', ha='right', va='top', alpha=0.85)

# ─── 8. 图例 ──────────────────────────────────────────
legend_items = [
    mpatches.Patch(color=colors["blue"], label="阶段1：HR管理机制了解"),
    mpatches.Patch(color=colors["orange"], label="阶段2：业务了解"),
    mpatches.Patch(color=colors["green"], label="阶段3：在岗实践 & 产出"),
]
leg = ax.legend(handles=legend_items, loc='upper right', frameon=True,
                fancybox=True, shadow=False, prop=tencent_font, fontsize=11,
                edgecolor='#E0E0E0')
leg.get_frame().set_linewidth(0.5)

# ─── 9. 标题 & 样式微调 ───────────────────────────────
ax.set_title(
    'AMS HRBP OKR 规划甘特图 V4\n'
    '[2026年4月起 · 并行推进 · 按完成时间倒序]',
    fontproperties=tencent_font, fontsize=18, fontweight='bold', 
    pad=16, color='#333333'
)

ax.grid(axis='x', color='#EEEEEE', linewidth=0.5, alpha=0.8, zorder=1)
ax.set_axisbelow(True)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#DDDDDD')
ax.spines['bottom'].set_color('#DDDDDD')

fig.patch.set_facecolor('white')
ax.set_facecolor('#FAFAFA')

plt.tight_layout(pad=1.5)
output_path = '/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v4.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print(f"✅ 已保存: {output_path}")
