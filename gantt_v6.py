# -*- coding: utf-8 -*-
"""
AMS HRBP OKR 规划甘特图 V6 — 最终修正版
核心原则：
1. 先完成的在上方（升序排列）
2. 并行任务真实展示时间重叠
3. 阶段标签不被遮挡
4. 坐标与内容严格对齐
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
# 任务数据
# ============================================================
tasks_raw = [
    # ====== 阶段3 ======
    ("AI专项产出[By月]",          "2026-05-11", "2026-08-10", "#00B96B", None),
    ("大评估日常工作[By Case]",   "2026-05-04", "2026-08-03", "#00B96B", None),
    ("协助BP落地日常工作",        "2026-05-04", "2026-08-31", "#00B96B", "阶段2完成"),
    ("设计职能演进思考报告",      "2026-04-27", "2026-05-17", "#00B96B", "◆AI产品经理+设计\n  演进思考报告(5/17)"),
    ("AI产品经理演进思考报告",    "2026-04-27", "2026-05-17", "#00B96B", None),
    # ====== 阶段2 ======
    ("深入了解工作内容/情况",     "2026-04-27", "2026-05-09", "#FF7A45", None),
    ("深入了解部门业务(WXG/TAD)", "2026-04-21", "2026-05-10", "#FF7A45", None),
    ("AMS新人培训课程",           "2026-04-14", "2026-05-02", "#FF7A45", None),
    ("计算广告课程&教材学习",     "2026-04-14", "2026-04-26", "#FF7A45", "◆广告业务\n  学习报告(4/26)"),
    # ====== 阶段1 ======
    ("文化荣誉激励体系",         "2026-04-21", "2026-04-27", "#0052D9", None),
    ("培养体系现状",             "2026-04-19", "2026-04-25", "#0052D9", None),
    ("绩效通道管理",             "2026-04-18", "2026-04-24", "#0052D9", None),
    ("组织架构与晋升规则",       "2026-04-16", "2026-04-23", "#0052D9", None),
    ("招聘编制管理",             "2026-04-15", "2026-04-22", "#0052D9", None),
    ("HRBP职责与课程体系\n(组织架构/绩效通道/培养文化)", "2026-04-14", "2026-04-20", "#0052D9", None),
    ("公司课程学习",             "2026-04-14", "2026-04-19", "#0052D9", None),
]

# 解析 + 按**结束日期升序**排列（先完成的前面）
tasks = []
for name, s, e, color, ms in tasks_raw:
    start = datetime.strptime(s, "%Y-%m-%d")
    end = datetime.strptime(e, "%Y-%m-%d")
    tasks.append((name, start, end, color, ms))
tasks.sort(key=lambda t: t[2])  # 升序！最早结束的 index=0

N = len(tasks)
plot_start = min(t[1] for t in tasks)   # 4/14
plot_end = max(t[2] for t in tasks)     # 8/31
total_days = (plot_end - plot_start).days
H = 0.52  # 条形高度

fig, ax = plt.subplots(figsize=(21, 15), dpi=150)

# ========== 绘制条形 ==========
for i, (name, start, end, color, milestone) in enumerate(tasks):
    w = (end - start).days + 1
    left = (start - plot_start).days
    
    ax.barh(y=i, width=w, height=H, left=left,
            color=color, ec='white', lw=0.7, zorder=3)

    # 日期文字
    mid = left + w / 2
    ax.text(mid, i, f"{start.strftime('%m/%d')}-{end.strftime('%m/%d')}",
            ha='center', va='center', fontsize=7.3, color='white',
            fontweight='bold', fontproperties=font_prop, zorder=4)

    # 里程碑
    if milestone:
        mx = (end - plot_start).days
        ax.plot(mx, i, 'D', ms=10, color='#E02020',
                mec='white', mew=1.5, zorder=6)
        ax.annotate(milestone, xy=(mx, i),
                    xytext=(mx + 2.5, i - 0.72),
                    fontsize=7.2, color='#C01818',
                    ha='left', va='top', fontweight='bold',
                    fontproperties=font_prop,
                    bbox=dict(boxstyle='round,pad=0.25', fc='white',
                              ec='#E02020', alpha=0.93, lw=1),
                    arrowprops=dict(arrowstyle='-', color='#E02020',
                                    lw=1, shrinkB=5), zorder=6)

# ========== Y轴 — 与barh坐标一致 ==========
labels = [t[0] for t in tasks]
ax.set_yticks(range(N))
ax.set_yticklabels(labels, fontproperties=font_prop, fontsize=9)

# ========== X轴周刻度 ==========
ticks, tick_labs = [], []
for w_idx in range(total_days // 7 + 3):
    d = plot_start + timedelta(days=w_idx * 7)
    if d <= plot_end + timedelta(days=3):
        ticks.append((d - plot_start).days)
        tick_labs.append(f"W{w_idx+1}\n({d.strftime('%m/%d')})")

ax.set_xticks(ticks)
ax.set_xticklabels(tick_labs, fontproperties=font_prop, fontsize=7.3)
ax.set_xlim(-1.5, total_days + 3)

# ========== 阶段背景 ==========
phases = [
    ("阶段1", "2026-04-14", "2026-04-28", "#0052D9"),
    ("阶段2", "2026-04-28", "2026-05-11", "#FF7A45"),
    ("阶段3", "2026-05-11", "2026-09-01", "#00B96B"),
]
for pn, ps_s, pe_s, pc in phases:
    ps = datetime.strptime(ps_s, "%Y-%m-%d")
    pe = datetime.strptime(pe_s, "%Y-%m-%d")
    xs = max(0, (ps - plot_start).days)
    xe = min(total_days, (pe - plot_start).days)
    ax.axvspan(xs, xe, facecolor=pc, alpha=0.06, zorder=0)

# 阶段标签放在图的最顶部（y > N 的区域）
for pn, ps_s, pe_s, pc in phases:
    ps = datetime.strptime(ps_s, "%Y-%m-%d")
    pe = datetime.strptime(pe_s, "%Y-%m-%d")
    mid_x = ((ps + (pe - ps) / 2) - plot_start).days
    ax.text(mid_x, N + 0.35, pn, ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=pc,
            fontproperties=font_prop, zorder=10)

# ========== 网格 & 边框 ==========
ax.set_axisbelow(True)
ax.xaxis.grid(True, ls='--', alpha=0.30, color='gray', zorder=1)
ax.yaxis.grid(False)
for sp in ['top', 'right']:
    ax.spines[sp].set_visible(False)
for sp in ['bottom', 'left']:
    ax.spines[sp].set_color('#CCCCCC')

# 图例
leg = ax.legend(handles=[
    mpatches.Patch(color="#0052D9", label="阶段1: HR管理机制了解"),
    mpatches.Patch(color="#FF7A45", label="阶段2: 业务了解"),
    mpatches.Patch(color="#00B96B", label="阶段3: 在岗实践 & 产出"),
], loc='upper right', prop=font_prop, frameon=True,
    fancybox=True, edgecolor='#DDDDDD')
leg.get_frame().set_alpha(0.95)

# 标题
ax.set_title(
    'AMS HRBP OKR 规划甘特图 V6\n'
    '[2026年4月起 · 并行推进 · 详细版 · ✅先完成在上]',
    fontproperties=font_prop, fontsize=16, fontweight='bold',
    color='#333333', pad=28)

# ★ 关键：ylim 让顶部有空间放阶段标签，且不反转Y轴
# barh默认 y=0 在底部，y=N-1 在顶部
# 我们要让 index=0（最早完成）在顶部 → 不用invert_yaxis，而是让y轴范围反过来
ax.set_ylim(N + 1.2, -0.6)  # 大值在上，小值在下 → 自动倒置！

plt.tight_layout()
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v6.png"
fig.savefig(out, dpi=180, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"✅ 已保存: {out}")

# 打印排序验证
print("\n📋 排序验证（从上到下）:")
for i, (n, s, e, c, _) in enumerate(tasks):
    print(f"  [{i:2d}] {e.strftime('%m/%d')} 结束 | {n}")
