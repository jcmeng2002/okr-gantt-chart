# -*- coding: utf-8 -*-
"""
AMS HRBP OKR 规划甘特图 V5
- 详细版（每项任务单独展示）
- 按完成时间倒序（先完成的放上面）
- 腾讯体字体
- 并行关系展示 + 关键交付点标记
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from datetime import datetime, timedelta

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"

font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()

print(f"✅ 腾讯体已加载: {font_prop.get_name()}")

# ============================================================
# 任务数据 — 详细版（基于文档第二张表格）
# 格式: (名称, 开始日期字符串, 结束日期字符串, 颜色, 阶段, 里程碑文本)
# ============================================================
tasks_data = [
    # ====== 阶段3: 在岗实践 & 产出 (绿色) ======
    ("AI专项产出[By月]",          "2026-05-11", "2026-08-10", "#00B96B", "阶段3", None),
    ("大评估日常工作[By Case]",   "2026-05-04", "2026-08-03", "#00B96B", "阶段3", None),
    ("协助BP落地日常工作",        "2026-05-04", "2026-08-31", "#00B96B", "阶段3", "阶段2完成"),
    ("设计职能演进思考报告",      "2026-04-27", "2026-05-17", "#00B96B", "阶段3", "AI产品经理+设计\n演进思考报告"),
    ("AI产品经理演进思考报告",    "2026-04-27", "2026-05-17", "#00B96B", "阶段3", None),

    # ====== 阶段2: 业务了解 (橙色) ======
    ("深入了解工作内容/情况",     "2026-04-27", "2026-05-09", "#FF7A45", "阶段2", None),
    ("深入了解部门业务(WXG/TAD)", "2026-04-21", "2026-05-10", "#FF7A45", "阶段2", None),
    ("AMS新人培训课程",           "2026-04-14", "2026-05-02", "#FF7A45", "阶段2", None),
    ("计算广告课程&教材学习",     "2026-04-14", "2026-04-26", "#FF7A45", "阶段2", "广告业务\n学习报告"),

    # ====== 阶段1: HR管理机制了解 (蓝色) ======
    ("文化荣誉激励体系",         "2026-04-21", "2026-04-27", "#0052D9", "阶段1", None),
    ("培养体系现状",             "2026-04-19", "2026-04-25", "#0052D9", "阶段1", None),
    ("绩效通道管理",             "2026-04-18", "2026-04-24", "#0052D9", "阶段1", None),
    ("组织架构与晋升规则",       "2026-04-16", "2026-04-23", "#0052D9", "阶段1", None),
    ("招聘编制管理",             "2026-04-15", "2026-04-22", "#0052D9", "阶段1", None),
    ("HRBP职责与课程体系(组织架构/绩效通道/培养文化)", "2026-04-14", "2026-04-20", "#0052D9", "阶段1", None),
    ("公司课程学习",             "2026-04-14", "2026-04-19", "#0052D9", "阶段1", None),
]

n_tasks = len(tasks_data)

# 解析数据并按结束时间倒序排列（晚结束的排前面 = 数组索引小 = 图上位置高）
parsed_tasks = []
for name, start_str, end_str, color, phase, milestone in tasks_data:
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.strptime(end_str, "%Y-%m-%d")
    parsed_tasks.append((name, start, end, color, phase, milestone))

# 按 end 降序排列（最晚结束的在 index 0 → 最上面）
parsed_tasks.sort(key=lambda x: x[2], reverse=True)

# 时间范围
all_starts = [t[1] for t in parsed_tasks]
all_ends = [t[2] for t in parsed_tasks]
plot_start = min(all_starts)
plot_end = max(all_ends)

total_days = (plot_end - plot_start).days
bar_height = 0.55

fig, ax = plt.subplots(figsize=(22, 15), dpi=150)

# 绘制条形图 — 使用倒序后的索引直接作为 y 坐标
for i, (name, start, end, color, phase, milestone) in enumerate(parsed_tasks):
    duration = (end - start).days + 1
    start_offset = (start - plot_start).days
    
    y_pos = i  # i=0 是最上面的（最晚结束的）
    
    bar = ax.barh(
        y=y_pos,
        width=duration,
        height=bar_height,
        left=start_offset,
        color=color,
        edgecolor='white',
        linewidth=0.8,
        zorder=3,
    )

    # 条形中间显示时间范围
    mid_x = start_offset + duration / 2
    date_range = f"{start.strftime('%m/%d')}-{end.strftime('%m/%d')}"
    ax.text(mid_x, y_pos, date_range,
            ha='center', va='center',
            fontsize=8, color='white', fontweight='bold',
            fontproperties=font_prop)

    # 里程碑标记（红色菱形）
    if milestone:
        marker_x = (end - plot_start).days
        ax.plot(marker_x, y_pos, 'D', markersize=12,
                color='#E02020', markeredgecolor='white', markeredgewidth=1.5,
                zorder=5)
        ax.annotate(milestone, xy=(marker_x, y_pos),
                    xytext=(marker_x - 4, y_pos + 0.65),
                    fontsize=8, color='#E02020',
                    ha='center', va='bottom', fontweight='bold',
                    fontproperties=font_prop,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                              edgecolor='#E02020', alpha=0.95, linewidth=1))

# ========== 设置Y轴标签（与y坐标一一对应）==========
y_labels = [t[0] for t in parsed_tasks]
ax.set_yticks(range(n_tasks))
ax.set_yticklabels(y_labels, fontproperties=font_prop, fontsize=10)

# ========== X轴设置 ==========
num_weeks = total_days // 7 + 2
week_ticks = []
week_labels = []

for w in range(num_weeks):
    week_start = plot_start + timedelta(days=w * 7)
    if week_start <= plot_end:
        week_ticks.append((week_start - plot_start).days)
        w_num = w + 1
        week_labels.append(f"W{w_num}\n({week_start.strftime('%m/%d')})")

ax.set_xticks(week_ticks)
ax.set_xticklabels(week_labels, fontproperties=font_prop, fontsize=8)
ax.set_xlim(-0.5, total_days + 1)

# 阶段分隔背景
phase_colors_bg = {
    "阶段1": ("#0052D9", 0.04),
    "阶段2": ("#FF7A45", 0.06),
    "阶段3": ("#00B96B", 0.05),
}

for phase_name, (bg_color, alpha) in phase_colors_bg.items():
    if phase_name == "阶段1":
        p_start = 0
        p_end = (datetime.strptime("2026-04-28", "%Y-%m-%d") - plot_start).days
    elif phase_name == "阶段2":
        p_start = (datetime.strptime("2026-04-28", "%Y-%m-%d") - plot_start).days
        p_end = (datetime.strptime("2026-05-11", "%Y-%m-%d") - plot_start).days
    else:
        p_start = (datetime.strptime("2026-05-11", "%Y-%m-%d") - plot_start).days
        p_end = total_days + 1

    ax.axvspan(p_start, p_end, facecolor=bg_color, alpha=alpha, zorder=0)
    mid_phase = (p_start + p_end) / 2
    ax.text(mid_phase, n_tasks - 0.3, phase_name,
            ha='center', va='top', fontsize=13, color=bg_color,
            fontweight='bold', fontproperties=font_prop, zorder=1)

# 网格线
ax.set_axisbelow(True)
ax.xaxis.grid(True, linestyle='--', alpha=0.35, color='gray', zorder=1)
ax.yaxis.grid(False)
ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4, zorder=2)

# 边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['bottom', 'left']:
    ax.spines[spine].set_color('#CCCCCC')

# 图例
legend_patches = [
    mpatches.Patch(color="#0052D9", label="阶段1: HR管理机制了解"),
    mpatches.Patch(color="#FF7A45", label="阶段2: 业务了解"),
    mpatches.Patch(color="#00B96B", label="阶段3: 在岗实践 & 产出"),
]
leg = ax.legend(handles=legend_patches, loc='upper right',
                prop=font_prop, frameon=True, fancybox=True,
                shadow=False, edgecolor='#DDDDDD')
leg.get_frame().set_alpha(0.95)

# 标题
ax.set_title('AMS HRBP OKR 规划甘特图 V5\n'
             '[2026年4月起 · 并行推进 · 详细版 · 按完成时间倒序]',
             fontproperties=font_prop, fontsize=17, fontweight='bold',
             color='#333333', pad=20)

# Y轴范围
ax.set_ylim(-0.5, n_tasks - 0.5)
ax.invert_yaxis()  # 让 index 0（最晚结束）在最上方

plt.tight_layout()
output_path = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v5.png"
fig.savefig(output_path, dpi=180, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close(fig)

print(f"✅ 已保存: {output_path}")
