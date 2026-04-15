#!/usr/bin/env python3
"""
OKR甘特图 V3 — 修复版
修复：1) 时间从W1(4/14)开始 2) 布局防文字堆叠 3) 并行关系
字体：腾讯体 TencentSans-W7.otf（用户本地已安装）
配色：腾讯品牌风格 #0052D9
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from datetime import datetime, timedelta
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings('ignore')

# ─── 字体加载（腾讯体）─────────────────────────────
FONT_PATH = '/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf'
try:
    font_prop = fm.FontProperties(fname=FONT_PATH)
    FONT_NAME = font_prop.get_name()
    print(f"✅ 腾讯体已加载: {FONT_NAME}")
except Exception as e:
    print(f"⚠️ 腾讯体加载失败: {e}")
    font_prop = fm.FontProperties(family='Microsoft YaHei', weight='bold')
    FONT_NAME = 'Microsoft YaHei'

plt.rcParams['font.family'] = [FONT_NAME]
plt.rcParams['axes.unicode_minus'] = False

# ─── 颜色方案（腾讯品牌色系）──────────────────────────
TENCENT_BLUE   = '#0052D9'      # 主色（阶段1）
TENCENT_ORANGE = '#ED7B2F'       # 橙色（阶段2）
TENCENT_GREEN  = '#00A870'       # 绿色（阶段3）
TENCENT_RED    = '#E34D59'       # 红色（里程碑）
BG_LIGHT_BLUE  = '#EBF2FA'       # 浅蓝背景
BG_LIGHT_ORANGE = '#FDF4EC'      # 浅橙背景
BG_LIGHT_GREEN  = '#E7F6EE'      # 浅绿背景
TEXT_DARK      = '#333333'
TEXT_GRAY      = '#666666'

PHASE_COLORS = {
    '阶段1': TENCENT_BLUE,
    '阶段2': TENCENT_ORANGE,
    '阶段3': TENCENT_GREEN,
}
PHASE_BG = {
    '阶段1': BG_LIGHT_BLUE,
    '阶段2': BG_LIGHT_ORANGE,
    '阶段3': BG_LIGHT_GREEN,
}

# ─── 时间基准（入职日=2025年4月14日，周一，即W1开始）──
START_DATE = datetime(2025, 4, 14)

def w_date(week_num):
    """第W{week}周的开始日期"""
    return START_DATE + timedelta(weeks=(week_num - 1))

def d_offset(days_from_start):
    """从起始日期偏移的天数"""
    return START_DATE + timedelta(days=days_from_start)

def date_str(d):
    """格式化日期为 M/D"""
    return f"{d.month}/{d.day}"

def week_label(w):
    """W标签 + 具体日期"""
    wd = w_date(w)
    return f"W{w}\n({date_str(wd)})"

# ─── 任务数据（并行关系，各自有明确起止日期）───────────

tasks = [
    # ═══ 阶段1: HR管理机制了解（并行执行，4/14-4/26）═══
    {"name": "公司课程学习", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(5)},   # 4/14-4/19（入职一周内）
    {"name": "HRBP职责与课程", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(12)},  # 4/14-4/26
    {"name": "招聘编制管理", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(12)},   # 4/14-4/26
    {"name": "组织架构与晋升规则", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(12)},
    {"name": "绩效通道管理", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(12)},
    {"name": "培养体系现状", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(12)},
    {"name": "文化荣誉激励体系", "phase": "阶段1",
     "start": d_offset(0), "end": d_offset(12)},

    # ═══ 阶段2: 业务了解（并行+交错）═════════════════
    {"name": "计算广告课程&教材学习", "phase": "阶段2",
     "start": d_offset(0), "end": d_offset(12)},    # 入职-4/26
    {"name": "AMS新人培训课程", "phase": "阶段2",
     "start": d_offset(0), "end": d_offset(12)},    # 入职-4/26
    {"name": "深入了解部门业务信息\n(WXG/TAD)", "phase": "阶段2",
     "start": d_offset(6), "end": d_offset(26)},    # ~4/21-5/10
    {"name": "了解工作内容和情况", "phase": "阶段2",
     "start": d_offset(13), "end": d_offset(26)},   # 4/27-5/10

    # ═══ 阶段3: 在岗实践 & 交付物（长期并行）══════════
    {"name": "协助BP落地日常工作", "phase": "阶段3",
     "start": d_offset(0), "end": d_offset(120)},   # 入职后持续
    {"name": "AI产品经理演进思考报告", "phase": "阶段3",
     "start": d_offset(13), "end": d_offset(33)},   # ~4/27-5/17前交付
    {"name": "设计职能演进思考报告", "phase": "阶段3",
     "start": d_offset(13), "end": d_offset(33)},   # ~4/27-5/17前交付
    {"name": "大评估等日常工作(ByCase)", "phase": "阶段3",
     "start": d_offset(20), "end": d_offset(120)},  # ~5/4起持续
    {"name": "AI专项产出(By月)", "phase": "阶段3",
     "start": d_offset(27), "end": d_offset(120)},  # ~5/11起每月产出
]

# ═══ 关键里程碑（红色标记）════════════════════════════
milestones = [
    {"date": d_offset(12), "label": "广告业务\n学习报告"},          # 4/26
    {"date": d_offset(26), "label": "阶段2完成"},                   # 5/10
    {"date": d_offset(33), "label": "AI产品经理+\n设计演进报告"},    # 5/17
]

# ─── 绘图设置（加大尺寸防堆叠）────────────────────────
FIG_WIDTH = 22        # 宽度加宽
FIG_HEIGHT = 18       # 高度加高
LEFT_MARGIN = 0.22    # 左侧留足文字空间（占图宽22%）
BAR_HEIGHT = 0.55     # 条形高度
TASK_GAP = 0.25       # 任务间距
MILESTONE_SIZE = 180  # 里程碑标记大小
Y_TOP_PAD = 0.08      # 顶部留白
Y_BOT_PAD = 0.06      # 底部留白

fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

n_tasks = len(tasks)
y_positions = list(range(n_tasks, 0, -1))  # 从上到下排列
total_y_range = n_tasks * BAR_HEIGHT + (n_tasks - 1) * TASK_GAP
y_min = 0.3
y_max = n_tasks * (BAR_HEIGHT + TASK_GAP) + Y_BOT_PAD

# 计算时间轴范围
all_dates = []
for t in tasks:
    all_dates.extend([t["start"], t["end"]])
for m in milestones:
    all_dates.append(m["date"])
t_min, t_max = min(all_dates) - timedelta(days=2), max(all_dates) + timedelta(days=5)
x_min, x_max = t_min, t_max

# 绘制阶段背景区域
phase_regions = [
    ("阶段1", d_offset(-2), d_offset(15)),
    ("阶段2", d_offset(10), d_offset(30)),
    ("阶段3", d_offset(25), d_offset(125)),
]
for pname, ps, pe in phase_regions:
    ax.axvspan(ps, pe, alpha=0.35, color=PHASE_BG[pname], zorder=0)
    mid_x = ps + (pe - ps) / 2
    ax.text(mid_x, y_max - 0.3, pname, ha='center', va='top',
            fontproperties=font_prop, fontsize=16, fontweight='bold',
            color=PHASE_COLORS[pname], alpha=0.85)

# ─── 绘制任务条形（核心改进：布局优化）────────────────
for i, task in enumerate(tasks):
    y = y_positions[i] - BAR_HEIGHT / 2  # 居中对齐
    color = PHASE_COLORS[task["phase"]]
    
    duration_days = (task["end"] - task["start"]).days
    
    bar = ax.barh(y_positions[i], duration_days, left=task["start"],
                  height=BAR_HEIGHT, color=color, alpha=0.88,
                  edgecolor='white', linewidth=0.8, zorder=3,
                  align='center')

    # 任务名称（左对齐，字号适中）
    ax.text(x_min - timedelta(days=1), y_positions[i], task["name"],
            ha='right', va='center', fontproperties=font_prop,
            fontsize=11, color=TEXT_DARK, fontweight='medium')

    # 在条形上显示时间范围
    if duration_days >= 21:
        time_text = f"{date_str(task['start'])}-{date_str(task['end'])}"
        bar_mid = task["start"] + timedelta(days=duration_days / 2)
        ax.text(bar_mid, y_positions[i], time_text,
                ha='center', va='center', fontproperties=font_prop,
                fontsize=9, color='white', fontweight='bold', alpha=0.95)

# ─── 绘制里程碑（红色菱形标记，在对应任务行附近标注）───
milestone_rows = [7, 11, 13]  # 分别对应阶段1结束、阶段2结束、报告交付附近的任务行
for idx, m in enumerate(milestones):
    my = y_positions[milestone_rows[idx]] if idx < len(milestone_rows) else y_positions[-1]
    ax.scatter(m["date"], my, marker='D', s=MILESTONE_SIZE,
               color=TENCENT_RED, zorder=6, edgecolors='white', linewidths=1.5)
    ax.annotate(m["label"], xy=(m["date"], my),
                xytext=(-20, 35), textcoords='offset points',
                fontproperties=font_prop, fontsize=10, fontweight='bold',
                color=TENCENT_RED, ha='center',
                arrowprops=dict(arrowstyle='->', color=TENCENT_RED, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor=TENCENT_RED, alpha=0.95))

# ─── 坐标轴配置 ──────────────────────────────────────
ax.set_xlim(t_min, t_max)
ax.set_ylim(y_min, y_max)
ax.invert_yaxis()

# X轴：周标签 + 具体日期
week_starts = [w_date(w) for w in range(1, 19)]  # W1~W18
ax.set_xticks(week_starts)
ax.set_xticklabels([week_label(w) for w in range(1, 19)],
                    fontproperties=font_prop, fontsize=9.5)
ax.tick_params(axis='x', length=0, pad=6)

# Y轴隐藏（任务名已用text绘制在左侧）
ax.set_yticks([])
ax.tick_params(axis='y', left=False)

# 边框和网格
for spine in ['top', 'left', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(0.8)
ax.grid(axis='x', color='#EEEEEE', linestyle='-', linewidth=0.5, zorder=1)

# ─── 标题 ────────────────────────────────────────────
ax.set_title('AMS HRBP OKR 规划甘特图 V3\n（2025年4月起 · 并行推进）',
             fontproperties=font_prop, fontsize=22, fontweight='bold',
             color=TEXT_DARK, pad=24, loc='left')

# ─── 图例（右下角）───────────────────────────────────
legend_items = [
    Patch(facecolor=TENCENT_BLUE, edgecolor='white', label='阶段1：HR管理机制了解'),
    Patch(facecolor=TENCENT_ORANGE, edgecolor='white', label='阶段2：业务了解'),
    Patch(facecolor=TENCENT_GREEN, edgecolor='white', label='阶段3：在岗实践 & 产出'),
]
leg = ax.legend(handles=legend_items, loc='lower right',
                 prop=font_prop, frameon=True, fancybox=True,
                 shadow=False, fontsize=11,
                 edgecolor='#DDDDDD').get_frame().set_alpha(0.98)

plt.subplots_adjust(left=LEFT_MARGIN, right=0.95, top=0.92, bottom=0.08)

output_path = '/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v3.png'
plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
print(f"✅ 已保存: {output_path}")
plt.close()
