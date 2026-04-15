# -*- coding: utf-8 -*-
"""
AMS HRBP OKR 规划甘特图 V7 — 严格按文档时间修正版
修正点：
1. 起始日期从4月12日开始（不是4月14日）
2. 不设结束时间的任务延伸到"及以后"
3. 时间严格对照文档表格2的原始数据
4. 先完成在上、并行展示、坐标对齐、阶段标签不遮挡
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
# ★ 任务数据 — 严格按文档表格2 ★
# (名称, 开始, 结束(或None=无固定结束), 颜色, 里程碑)
# ============================================================
tasks_raw = [
    # ====== 阶段1: HR管理机制了解 (4/12起) ======
    # Row 1: 公司课程学习 — 入职后一周
    ("公司课程学习", "2026-04-12", "2026-04-19", "#0052D9", None),
    # Row 2-7: 其他全部都是！入职后两周 (4/12-4/26)
    ("HRBP职责与课程体系\n(组织架构/绩效通道/培养文化)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("招聘编制管理\n(BP与招聘合作方式)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("组织架构与晋升规则\n(潜龙/干部晋升/360评估等)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("绩效通道管理\n(目标制定/考核/面谈/申诉)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("培养体系现状", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("文化荣誉激励体系", "2026-04-12", "2026-04-26", "#0052D9", None),

    # ====== 阶段2: 业务了解 ======
    # Row 8-9: 计算广告+AMS新人培训 (入职后两周), 交付: 4/26前报告
    ("计算广告课程&教材学习", "2026-04-12", "2026-04-26", "#FF7A45",
     "◆ 广告业务学习报告(4/26)"),
    ("AMS新人培训课程", "2026-04-12", "2026-04-26", "#FF7A45", None),
    # Row 10: 深入了解部门业务 (入职后一月), 交付: 5/17两份报告
    ("深入了解部门业务(WXG/TAD)\n(业务目标/核心干部)", "2026-04-12", "2026-05-10", "#FF7A45", None),
    # Row 11: 了解工作内容情况 (入职后一月)
    ("了解工作内容/工作模式\n沟通习惯", "2026-04-12", "2026-05-10", "#FF7A45", None),

    # ====== 阶段3: 在岗实践 & 产出 ======
    # 两份演进报告 (5/17交付)
    ("设计职能演进思考报告", "2026-04-27", "2026-05-17", "#00B96B",
     "◆ AI产品经理+设计\n   演进报告(5/17)"),
    ("AI产品经理演进思考报告", "2026-04-27", "2026-05-17", "#00B96B", None),
    # Row 12: 协助BP — 无固定结束时间
    ("协助BP落地日常工作\n(by case交付大评估等)", "2026-04-12", None, "#00B96B",
     "◆ 阶段2完成"),
    # Row 13: AI专项 — 从4/12至结束，by月交付节点
    ("AI专项\n(by月产出)", "2026-04-12", None, "#00B96B",
     "◆5/10·6/14·7/12·8/16"),
]

# 解析 + 按**结束日期升序**排列（先完成的前面 = index小 = 图上方）
tasks = []
for name, s_str, e_str, color, ms in tasks_raw:
    start = datetime.strptime(s_str, "%Y-%m-%d")
    end = datetime.strptime(e_str, "%Y-%m-%d") if e_str else None
    tasks.append((name, start, end, color, ms))

# 排序: 有结束时间的按结束时间排，无结束时间的排最后
def sort_key(t):
    if t[2] is None:
        return datetime.max  # 无结束时间的排最下面
    return t[2]
tasks.sort(key=sort_key)

N = len(tasks)
plot_start = datetime(2026, 4, 12)  # 从4/12开始

# 确定X轴终点：W18之后显示"及以后"
# W18 = 4/12 + 17*7 = 4/12 + 119天 ≈ 8/10
# 让X轴画到 W18 结束位置，然后留空间写"及以后"
plot_end_for_display = plot_start + timedelta(days=17 * 7)  # W18末
total_display_days = (plot_end_for_display - plot_start).days  # ~119天

H = 0.50

fig, ax = plt.subplots(figsize=(22, 15), dpi=150)

# ========== 绘制条形图 ==========
for i, (name, start, end, color, milestone) in enumerate(tasks):
    left = (start - plot_start).days

    if end is not None:
        # 精确到结束日期，不延伸
        width = (end - start).days  # 精确天数，不加+1
        bar_color = color
    else:
        # 无固定结束 → 延伸到 X 轴右侧尽头
        width = total_display_days + 6 - left
        bar_color = color

    ax.barh(y=i, width=width, height=H, left=left,
            color=bar_color, ec='white', lw=0.7, zorder=3,
            alpha=None)

    # 条形内文字
    mid_x = left + min(width, total_display_days) / 2
    if end is not None:
        label = f"{start.strftime('%m/%d')}-{end.strftime('%m/%d')}"
    else:
        label = f"{start.strftime('%m/%d')}-及以后"

    ax.text(mid_x, i, label,
            ha='center', va='center', fontsize=7, color='white',
            fontweight='bold', fontproperties=font_prop, zorder=4)

    # 里程碑标记
    if milestone:
        mx = (end - plot_start).days if end else left + width - 3
        ax.plot(mx, i, 'D', ms=10, color='#E02020',
                mec='white', mew=1.5, zorder=6)
        ax.annotate(milestone, xy=(mx, i),
                    xytext=(mx + 2, i - 0.72),
                    fontsize=7, color='#C01818',
                    ha='left', va='top', fontweight='bold',
                    fontproperties=font_prop,
                    bbox=dict(boxstyle='round,pad=0.25',
                              fc='white', ec='#E02020', alpha=0.93, lw=1),
                    arrowprops=dict(arrowstyle='-', color='#E02020',
                                    lw=1, shrinkB=5), zorder=6)

# ========== Y轴标签 ==========
labels = [t[0] for t in tasks]
ax.set_yticks(range(N))
ax.set_yticklabels(labels, fontproperties=font_prop, fontsize=9)

# ========== X轴周刻度 (W1-W18 + 及以后) ==========
ticks, tick_labs = [], []
for w_idx in range(19):  # W1 到 W19 (多一个用于"及以后")
    d = plot_start + timedelta(days=w_idx * 7)
    ticks.append((d - plot_start).days)
    if w_idx < 18:
        tick_labs.append(f"W{w_idx+1}\n({d.strftime('%m/%d')})")
    else:
        tick_labs.append("及以后")

ax.set_xticks(ticks)
ax.set_xticklabels(tick_labs, fontproperties=font_prop, fontsize=7.5)
ax.set_xlim(-2, total_display_days + 8)

# ========== 阶段背景区域 ==========
phases = [
    ("阶段1", 0, 16, "#0052D9"),      # 4/12-4/28 ≈ 16天
    ("阶段2", 16, 29, "#FF7A45"),     # 4/28-5/11 ≈ 28-29天
    ("阶段3", 29, total_display_days + 5, "#00B96B"),
]
for pn, day_s, day_e, pc in phases:
    ax.axvspan(day_s, day_e, facecolor=pc, alpha=0.06, zorder=0)
    mid_x = (day_s + day_e) / 2
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
    mpatches.Patch(color="#0052D9", label="阶段1: HR管理机制了解 (2周)"),
    mpatches.Patch(color="#FF7A45", label="阶段2: 业务了解 (约1月)"),
    mpatches.Patch(color="#00B96B", label="阶段3: 在岗实践 & 独立产出 (2-3月+)"),
], loc='upper right', prop=font_prop, frameon=True,
    fancybox=True, edgecolor='#DDDDDD')
leg.get_frame().set_alpha(0.95)

# 标题
ax.set_title(
    'AMS HRBP OKR 规划甘特图 V7\n'
    '[2026年4月12日起 · 并行推进 · 详细版 · 严格按文档时间]',
    fontproperties=font_prop, fontsize=16, fontweight='bold',
    color='#333333', pad=30)

# Y轴倒置: 大值在上 → 先完成的在顶部
ax.set_ylim(N + 1.2, -0.6)

plt.tight_layout()
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v7.png"
fig.savefig(out, dpi=180, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"\n✅ 已保存: {out}")

# 排序验证
print("\n📋 排序验证 (从上到下):")
for i, (n, s, e, c, _) in enumerate(tasks):
    e_str = e.strftime('%m/%d') if e else "无结束(及以后)"
    print(f"  [{i:2d}] 结束={e_str} | {n.replace(chr(10),' ')}")
