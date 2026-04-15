# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 规划甘特图 V9 — 最终版
修正：
1. 阶段边界严格按周刻度对齐
2. 条形起始精确到天（4/27就是4/27，不是4/26）
3. AI专项的4个月度交付点在坐标轴上逐一标出红色菱形
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

PLOT_START = datetime(2026, 4, 12)

# ============================================================
# ★ 任务数据
# ============================================================
tasks_raw = [
    # ====== 阶段1 ======
    ("公司课程学习", "04-12", "04-19", "#0052D9", None),
    ("HRBP职责与课程体系\n(组织架构/绩效通道/培养文化)", "04-12", "04-26", "#0052D9", None),
    ("招聘编制管理\n(BP与招聘合作方式)", "04-12", "04-26", "#0052D9", None),
    ("组织架构与晋升规则\n(潜龙/干部晋升/360评估等)", "04-12", "04-26", "#0052D9", None),
    ("绩效通道管理\n(目标制定/考核/面谈/申诉)", "04-12", "04-26", "#0052D9", None),
    ("培养体系现状", "04-12", "04-26", "#0052D9", None),
    ("文化荣誉激励体系", "04-12", "04-26", "#0052D9", None),

    # ====== 阶段2 ======
    ("计算广告课程&教材学习", "04-12", "04-26", "#FF7A45",
     "◆ 广告业务学习报告(4/26)"),
    ("AMS新人培训课程", "04-12", "04-26", "#FF7A45", None),
    ("深入了解部门业务(WXG/TAD)\n(业务目标/核心干部)", "04-12", "05-10", "#FF7A45", None),
    ("了解工作内容/工作模式\n沟通习惯", "04-12", "05-10", "#FF7A45", None),

    # ====== 阶段3 ======
    ("设计职能演进思考报告", "04-26", "05-17", "#00B96B",
     "◆ 设计/AI产品经理\n   演进报告(5/17)"),
    ("AI产品经理演进思考报告", "04-26", "05-17", "#00B96B", None),
    ("协助BP落地日常工作\n(by case交付大评估等)", "04-12", None, "#00B96B",
     "◆ 阶段3完成"),
    # AI专项: 4个独立交付节点
    ("AI专项 (by月产出)", "04-12", None, "#00B96B", "__MILESTONES__"),
]

def parse_d(s):
    """解析 MM-DD 字符串为 datetime"""
    return datetime(2026, int(s[:2]), int(s[3:]))

# 解析并排序（先完成的在上）
tasks = []
for name, s_str, e_str, color, ms in tasks_raw:
    start = parse_d(s_str)
    end = parse_d(e_str) if e_str else None
    tasks.append((name, start, end, color, ms))

tasks.sort(key=lambda t: t[2] if t[2] else datetime.max)

N = len(tasks)
MAX_DAY = 19 * 7  # W19 = 133天
H = 0.50

fig, ax = plt.subplots(figsize=(23, 14), dpi=150)

# ========== 绘制条形图 ==========
for i, (name, start, end, color, milestone) in enumerate(tasks):
    left = (start - PLOT_START).days  # 精确到天的起始偏移

    if end is not None:
        width = (end - PLOT_START).days - left  # 结束位置 - 起始位置 = 精确宽度
    else:
        width = MAX_DAY + 8 - left

    ax.barh(y=i, width=width, height=H, left=left,
            color=color, ec='white', lw=0.7, zorder=3)

    # 时间文字
    mid_x = left + min(width * 0.5, MAX_DAY * 0.42)
    label = f"{start.strftime('%m/%d')}-{end.strftime('%m/%d')}" if end else f"{start.strftime('%m/%d')}-及以后"
    ax.text(mid_x, i, label,
            ha='center', va='center', fontsize=6.8, color='white',
            fontweight='bold', fontproperties=font_prop, zorder=4)

    # ========== 里程碑标记 ==========
    if milestone == "__MILESTONES__":
        # ★ AI专项：在坐标轴上逐一标出4个月度交付点
        ai_dates = ["05-17", "06-14", "07-12", "08-09"]
        for d_str in ai_dates:
            d = parse_d(d_str)
            mx = (d - PLOT_START).days
            if mx <= MAX_DAY + 2:
                ax.plot(mx, i, 'D', ms=9, color='#E02020',
                        mec='white', mew=1.3, zorder=6)
                ax.annotate(f"◆{d.strftime('%m/%d')}", xy=(mx, i),
                            xytext=(mx, i - 0.68),
                            fontsize=6.5, color='#C01818',
                            ha='center', va='top', fontweight='bold',
                            fontproperties=font_prop, zorder=6)

    elif milestone:
        mx = (end - PLOT_START).days if end else left + width - 2
        ax.plot(mx, i, 'D', ms=10, color='#E02020',
                mec='white', mew=1.5, zorder=6)
        ax.annotate(milestone, xy=(mx, i),
                    xytext=(mx + 1.5, i - 0.72),
                    fontsize=6.8, color='#C01818',
                    ha='left', va='top', fontweight='bold',
                    fontproperties=font_prop,
                    bbox=dict(boxstyle='round,pad=0.25',
                              fc='white', ec='#E02020', alpha=0.93, lw=1),
                    arrowprops=dict(arrowstyle='-', color='#E02020',
                                    lw=1, shrinkB=5), zorder=6)

# ========== Y轴标签 ==========
ax.set_yticks(range(N))
ax.set_yticklabels([t[0] for t in tasks], fontproperties=font_prop, fontsize=9)

# ========== X轴：每周刻度 ==========
ticks, labs = [], []
for w in range(20):
    d = PLOT_START + timedelta(days=w * 7)
    ticks.append((d - PLOT_START).days)
    labs.append(f"W{w+1}\n({d.strftime('%m/%d')})" if w < 19 else "W19及以后")

ax.set_xticks(ticks)
ax.set_xticklabels(labs, fontproperties=font_prop, fontsize=7)
ax.set_xlim(-3, MAX_DAY + 8)

# ========== 阶段背景 — 边界对齐到周刻度 ==========
# W1=4/12(day0), W2=4/19(day7), W3=4/26(day14), W4=5/3(day21), W5=5/10(day28)
phases_data = [
    ("阶段1", 0,   14,  "#0052D9"),   # day0~day14 (W1起点~W3起点)
    ("阶段2", 14,  28,  "#FF7A45"),   # day14~day28 (W3起点~W5起点)
    ("阶段3", 28,  MAX_DAY+5, "#00B96B"),  # day28起 (W5起点起)
]
for pn, ds, de, pc in phases_data:
    ax.axvspan(ds, de, facecolor=pc, alpha=0.06, zorder=0)
    ax.text((ds+de)/2, N+0.35, pn, ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=pc,
            fontproperties=font_prop, zorder=10)

# ========== 网格 & 边框 ==========
ax.set_axisbelow(True)
ax.xaxis.grid(True, ls='--', alpha=0.30, color='gray', zorder=1)
ax.yaxis.grid(False)
for sp in ['top','right']: ax.spines[sp].set_visible(False)
for sp in ['bottom','left']: ax.spines[sp].set_color('#CCCCCC')

# 图例
leg = ax.legend(handles=[
    mpatches.Patch(color="#0052D9", label="阶段1: HR管理机制了解 (~2周)"),
    mpatches.Patch(color="#FF7A45", label="阶段2: 业务了解 (~1月)"),
    mpatches.Patch(color="#00B96B", label="阶段3: 在岗实践 & 独立产出 (持续)"),
], loc='upper right', prop=font_prop, frameon=True,
    fancybox=True, edgecolor='#DDDDDD')
leg.get_frame().set_alpha(0.95)

# 标题
ax.set_title(
    'AMS HRBP实习生nelsonmeng OKR规划甘特图',
    fontproperties=font_prop, fontsize=16, fontweight='bold',
    color='#333333', pad=30)

ax.set_ylim(N+1.2, -0.6)

plt.tight_layout()
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v9.png"
fig.savefig(out, dpi=180, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"\n✅ 已保存: {out}")

# ★ 验证关键日期对齐
print("\n📏 关键日期验证:")
check_dates = [
    ("公司课程学习 开始", "04-12"),
    ("AMS新人培训 结束", "04-26"),
    ("设计/AI产品演进 开始", "04-27"),
    ("设计/AI产品演进 结束", "05-17"),
    ("深入了解部门业务 结束", "05-10"),
]
for label, d_str in check_dates:
    d = parse_d(d_str)
    day_offset = (d - PLOT_START).days
    week = day_offset // 7 + 1
    print(f"  {label}: {d_str} = 第{week}周, 偏移量={day_offset}天")
