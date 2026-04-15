# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 规划甘特图 V8 — 最终修正版
修正：
1. 标题改为 "AMS HRBP实习生nelsonmeng OKR规划甘特图"
2. 条形开始日期精确对齐（含当天，不留空）
3. 阶段分隔线按周对齐
4. X轴末端写 "W19及以后"
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
# ★ 任务数据（严格按文档表格2）
# ============================================================
tasks_raw = [
    # ====== 阶段1: HR管理机制了解 ======
    ("公司课程学习", "2026-04-12", "2026-04-19", "#0052D9", None),
    ("HRBP职责与课程体系\n(组织架构/绩效通道/培养文化)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("招聘编制管理\n(BP与招聘合作方式)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("组织架构与晋升规则\n(潜龙/干部晋升/360评估等)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("绩效通道管理\n(目标制定/考核/面谈/申诉)", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("培养体系现状", "2026-04-12", "2026-04-26", "#0052D9", None),
    ("文化荣誉激励体系", "2026-04-12", "2026-04-26", "#0052D9", None),

    # ====== 阶段2: 业务了解 ======
    ("计算广告课程&教材学习", "2026-04-12", "2026-04-26", "#FF7A45",
     "◆ 广告业务学习报告(4/26)"),
    ("AMS新人培训课程", "2026-04-12", "2026-04-26", "#FF7A45", None),
    ("深入了解部门业务(WXG/TAD)\n(业务目标/核心干部)", "2026-04-12", "2026-05-10", "#FF7A45", None),
    ("了解工作内容/工作模式\n沟通习惯", "2026-04-12", "2026-05-10", "#FF7A45", None),

    # ====== 阶段3: 在岗实践 & 产出 ======
    ("设计职能演进思考报告", "2026-04-27", "2026-05-17", "#00B96B",
     "◆ AI产品经理+设计演进报告(5/17)"),
    ("AI产品经理演进思考报告", "2026-04-27", "2026-05-17", "#00B96B", None),
    ("协助BP落地日常工作\n(by case交付大评估等)", "2026-04-12", None, "#00B96B",
     "◆ 阶段2完成"),
    ("AI专项 (by月产出)", "2026-04-12", None, "#00B96B",
     "◆ 5/10·6/14·7/12·8/16"),
]

# 解析 + 按**结束日期升序**排列（先完成的在上）
tasks = []
for name, s_str, e_str, color, ms in tasks_raw:
    start = datetime.strptime(s_str, "%Y-%m-%d")
    end = datetime.strptime(e_str, "%Y-%m-%d") if e_str else None
    tasks.append((name, start, end, color, ms))

def sort_key(t):
    return t[2] if t[2] else datetime.max
tasks.sort(key=sort_key)

N = len(tasks)
plot_start = datetime(2026, 4, 12)  # 从4/12开始

# X轴显示到 W19 (19周后)
total_display_days = 19 * 7  # 133天
H = 0.50

fig, ax = plt.subplots(figsize=(22, 14), dpi=150)

# ========== 绘制条形图 ==========
for i, (name, start, end, color, milestone) in enumerate(tasks):
    left = (start - plot_start).days  # 开始偏移量

    if end is not None:
        # 含开始和结束当日：(end-start).days 天间隔 → 宽度 = 间隔天数
        # 例如 4/27到5/17 = 20天间隔，bar宽度=20，左边缘精确在4/27位置
        width = (end - start).days
    else:
        width = total_display_days + 5 - left

    ax.barh(y=i, width=width, height=H, left=left,
            color=color, ec='white', lw=0.7, zorder=3)

    # 条形内时间文字
    mid_x = left + min(width * 0.55, total_display_days * 0.45)
    if end is not None:
        label = f"{start.strftime('%m/%d')}-{end.strftime('%m/%d')}"
    else:
        label = f"{start.strftime('%m/%d')}-及以后"
    ax.text(mid_x, i, label,
            ha='center', va='center', fontsize=7, color='white',
            fontweight='bold', fontproperties=font_prop, zorder=4)

    # 里程碑标记
    if milestone:
        if end is not None:
            mx = (end - plot_start).days
        elif "AI专项" in name or "by月" in name:
            # AI专项的月度交付节点标在条形右侧
            mx = total_display_days - 5
        else:
            mx = left + width - 3
        ax.plot(mx, i, 'D', ms=10, color='#E02020',
                mec='white', mew=1.5, zorder=6)
        ax.annotate(milestone, xy=(mx, i),
                    xytext=(mx + 1.5, i - 0.72),
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

# ========== X轴: W1 到 W19 及以后 ==========
ticks, tick_labs = [], []
for w_idx in range(20):  # W1..W19 + W20(及以后)
    d = plot_start + timedelta(days=w_idx * 7)
    ticks.append((d - plot_start).days)
    if w_idx < 19:
        tick_labs.append(f"W{w_idx+1}\n({d.strftime('%m/%d')})")
    else:
        tick_labs.append("W19及以后")

ax.set_xticks(ticks)
ax.set_xticklabels(tick_labs, fontproperties=font_prop, fontsize=7.2)
ax.set_xlim(-2, total_display_days + 6)

# ========== 阶段背景 — 按周边界对齐 ==========
# 阶段1: W1~W2 (4/12~4/25, 约14天) → day 0 ~ day 14
# 阶段2: W3~W4 (4/26~5/09, 约14天) → day 14 ~ day 28
# 阶段3: W5起 (5/10起) → day 28 起
phases = [
    ("阶段1", 0, 14, "#0052D9"),       # W1-W2
    ("阶段2", 14, 29, "#FF7A45"),      # W3-W4 (到5/10前一天)
    ("阶段3", 29, total_display_days + 3, "#00B96B"),  # W5起
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
    mpatches.Patch(color="#0052D9", label="阶段1: HR管理机制了解 (~2周)"),
    mpatches.Patch(color="#FF7A45", label="阶段2: 业务了解 (~1月)"),
    mpatches.Patch(color="#00B96B", label="阶段3: 在岗实践 & 独立产出 (持续)"),
], loc='upper right', prop=font_prop, frameon=True,
    fancybox=True, edgecolor='#DDDDDD')
leg.get_frame().set_alpha(0.95)

# 标题 — 按用户要求修改
ax.set_title(
    'AMS HRBP实习生nelsonmeng OKR规划甘特图\n'
    '[2026年4月12日起 · 并行推进 · 详细版 · 严格按文档时间]',
    fontproperties=font_prop, fontsize=16, fontweight='bold',
    color='#333333', pad=30)

# Y轴倒置: 先完成的上
ax.set_ylim(N + 1.2, -0.6)

plt.tight_layout()
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v8.png"
fig.savefig(out, dpi=180, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"\n✅ 已保存: {out}")

print("\n📋 排序验证 (从上→下):")
for i, (n, s, e, c, _) in enumerate(tasks):
    e_s = e.strftime('%m/%d') if e else "及以后"
    print(f"  [{i:2d}] {s.strftime('%m/%d')}-{e_s} | {n.replace(chr(10),' ')[:22]}")
