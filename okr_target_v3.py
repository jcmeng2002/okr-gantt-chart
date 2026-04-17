# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 目标框架图 V3 — π(派)型人才模型(优化版)
横向=专业能力/规章制度(大梁)
第一竖=业务纵深(广告+团队)
竖弯钩=AI探索(多条腿走路)

腾讯风格 + 腾讯体 + 高信息密度 + 紧凑布局
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
import numpy as np

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()
print(f"✅ 腾讯体已加载: {font_prop.get_name()}")

fig, ax = plt.subplots(figsize=(20, 14), dpi=180)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

# 颜色
C_BLUE   = "#0052D9"
C_RED    = "#E03A3E"
C_GREEN  = "#00B96B"
C_ORANGE = "#FF7A45"
C_PURPLE = "#7B61FF"
C_GRAY   = "#555555"

# ═══════ 标题栏 ═══════
header_box = mpatches.FancyBboxPatch(
    (0, 93), 100, 7,
    boxstyle="round,pad=0.02,rounding_size=0.4",
    facecolor=C_BLUE, edgecolor='none', zorder=10
)
ax.add_patch(header_box)
ax.text(50, 96.5,
    '目标：π(派)型HRBP —— 横向专业过硬 · 纵向业务纵深 · 弯钩多元探索',
    ha='center', va='center', fontsize=15.5, fontweight='bold', color='white',
    fontproperties=font_prop, zorder=11)

# ═══════ π 符号背景装饰 ═══════
pi_color = "#E8F0FE"
pi_lw = 24

# 横杠
ax.plot([27, 73], [78.5, 78.5], '-', color=pi_color, lw=pi_lw, solid_capstyle='round', zorder=1)
# 左竖 |
ax.plot([35.5, 35.5], [30, 78.5], '-', color=pi_color, lw=pi_lw, solid_capstyle='butt', zorder=1)
# 右竖弯钩 ┘ (上段竖直 + 下段向右弯)
ax.plot([64.5, 64.5], [48, 78.5], '-', color=pi_color, lw=pi_lw, solid_capstyle='butt', zorder=1)
cx_curve = np.linspace(64.5, 75, 30)
cy_curve = np.ones(30) * 48
ax.plot(cx_curve, cy_curve, '-', color=pi_color, lw=pi_lw, solid_capstyle='round', zorder=1)

# 大π字水印
ax.text(50, 81.5, 'π',
    ha='center', va='center', fontsize=72, color="#C5D7F5",
    fontweight='bold', fontproperties=font_prop, alpha=0.35, zorder=2)

# ═══════ 内容区域绘制函数 ═══════
def draw_section(x, y, w, h, title, subtitle, color, items, badge=None):
    """绘制一个内容区域（带左侧色条+圆角背景）"""
    # 背景
    bg = mpatches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.6",
        facecolor=color, edgecolor=color, alpha=0.07, linewidth=1.8, zorder=3
    )
    ax.add_patch(bg)
    
    # 左侧粗色条
    bar = mpatches.FancyBboxPatch(
        (x, y), 0.6, h,
        boxstyle="round,pad=0.01,rounding_size=0.25",
        facecolor=color, alpha=0.88, edgecolor='none', zorder=4
    )
    ax.add_patch(bar)
    
    # 标题
    ty = y + h - 2.0
    ax.text(x + 1.6, ty + 0.4, title,
        ha='left', va='center', fontsize=12.5, fontweight='bold', color=color,
        fontproperties=font_prop, zorder=6)
    
    if subtitle:
        ax.text(x + 1.6, ty - 1.4, subtitle,
            ha='left', va='center', fontsize=7.2, color=C_GRAY,
            fontproperties=font_prop, zorder=6, style='italic')
    
    # Badge
    if badge:
        bw = len(badge) * 0.85 + 1.8
        bx = x + w - bw - 1
        bb = mpatches.FancyBboxPatch(
            (bx, ty - 0.65), bw, 2.2,
            boxstyle="round,pad=0.01,rounding_size=0.28",
            facecolor=color, alpha=0.15, edgecolor=color, linewidth=0.8, zorder=5
        )
        ax.add_patch(bb)
        ax.text(bx + bw/2, ty + 0.4, badge,
            ha='center', va='center', fontsize=7.2, fontweight='bold', color=color,
            fontproperties=font_prop, zorder=6)
    
    # 要点列表
    start_y = ty - 3.3 if subtitle else ty - 3.0
    avail_h = start_y - y - 1.2
    line_h = min(avail_h / max(len(items), 1), 4.0)
    
    for ii, item in enumerate(items):
        iy = start_y - ii * max(line_h, 3.7)
        if iy < y + 1.2:
            break
        ax.plot(x + 1.6, iy, 'o', markersize=3.2, color=color, zorder=5)
        ax.text(x + 3.0, iy, item,
            ha='left', va='center', fontsize=7.0, color='#333',
            fontproperties=font_prop, zorder=5, linespacing=1.28)


# ═══════ A区: 横杠 — 专业能力 ═══════
draw_section(
    x=26.5, y=69, w=47, h=10,
    title="━ 横向：专业能力 · 挑起「大梁」",
    subtitle="规章制度体系化学习 — 打牢HRBP地基",
    color=C_BLUE, badge="[横杠]",
    items=[
        "HR政策体系：OD / 招聘 / 通道 / 绩效 / 培养 — 重点掌握AMS特有政策",
        "CDG HR合作模式：运营机制、沟通方式、高效承接部门需求",
        "组织架构：潜龙 / 干部晋升 / 360评估 / 绩效通道全流程",
    ]
)

# ═══════ B区: 第一竖 — 业务纵深 ═══════
draw_section(
    x=3.5, y=28, w=26, h=39,
    title="│ 第一竖：业务纵深",
    subtitle="深入广告业务 & 团队 — T型人才的「一竖」",
    color=C_RED, badge="[竖一]",
    items=[
        "【团队】熟悉AMS各职能分工、微广各中心工作内容",
        "【团队】访谈微广管理团队、Core team 及人才梯队",
        "【团队】挖掘组织和人才痛点，输出洞察和发现",
        "【团队】和微广团队建立友好连接与亲密互动",
        "【业务】理解AMS业务逻辑、规划及流量平台特征",
        "【业务】关注行业新趋势热点、流量业务现状与痛点",
        "【交付】◆ 广告业务学习报告(5/3)",
        "【交付】◆ WXG学习报告(5/10) · 设计/AI演进报告(5/24)",
    ]
)

# ═══════ C区: 竖弯钩 — AI探索 ═══════
draw_section(
    x=62.5, y=28, w=34, h=19.5,
    title="┘ 竖弯钩：多元探索",
    subtitle="多条腿走路 — AI专项月度产出 & 研发价值链",
    color=C_PURPLE, badge="[弯钩]",
    items=[
        "【AI专项】月度探索产出：5/17 → 6/14 → 7/12 → 8/09 四节点",
        "【研发】理解微广研发业务，输出研发价值链和工作流程图",
        "【协助】落地日常工作 by case交付大评估等",
    ]
)

# ═══════ D区: 中间基础区 ═══════
draw_section(
    x=31.5, y=41, w=28.5, h=26,
    title="+ 基础夯实",
    subtitle="新人培训 & 文化融入 & 培养体系",
    color=C_GREEN,
    items=[
        "【培训】AMS新人培训课程 (至05-03)",
        "【培训】公司课程学习 (至04-19)",
        "【文化】文化荣誉激励体系了解",
        "【培养】培养体系现状梳理",
        "【招聘】招聘编制管理 (BP与招聘合作方式)",
    ]
)

# ═══════ 结构标注连线 ═══════
ann_style = dict(boxstyle='round,pad=0.3', fc='white', lw=1.0, alpha=0.94)

annotations_data = [
    ("大梁 — 专业制度\n撑起HRBP能力基座", 50, 77.5, 84, 83, C_BLUE),
    ("纵深 — 业务穿透\nT型人才核心竞争力", 16.5, 52, 1, 59, C_RED),
    ("多腿 — 探索新事物\n差异化竞争力来源", 70, 40, 89, 33, C_PURPLE),
]

for txt, px, py, tx, ty, col in annotations_data:
    ax.annotate(txt,
        xy=(px, py), xytext=(tx, ty),
        fontsize=7.2, color=col, fontweight='bold',
        fontproperties=font_prop, ha='center', va='bottom',
        arrowprops=dict(arrowstyle='->', color=col, lw=1.3,
                        connectionstyle='arc3,rad=0.18', shrinkA=10, shrinkB=6),
        bbox=dict(boxstyle='round,pad=0.3', ec=col, fc='white', lw=1.0, alpha=0.94),
        zorder=15)

# ═══════ 底部时间轴 ═══════
ax.plot([7, 93], [23, 23], '-', color='#D0D5DD', lw=1.5, zorder=3)
time_points = [
    ("04-12", "入职", C_BLUE, 10),
    ("04-19", "公司课", C_BLUE, 21),
    ("04-26", "阶段1完", C_RED, 32),
    ("05-03", "广告报告", C_ORANGE, 43),
    ("05-10", "WXG报告", C_ORANGE, 54),
    ("05-24", "演进报告", C_GREEN, 66),
    ("05~08月", "AI持续", C_PURPLE, 78),
    ("持续", "在岗实践", C_GREEN, 89),
]
for label, desc, col, tx in time_points:
    ax.plot(tx, 23, 'o', markersize=5.5, color=col, zorder=5)
    ax.text(tx, 21.3, f"{label}\n{desc}",
        ha='center', va='top', fontsize=5.8, color=C_GRAY,
        fontproperties=font_prop, zorder=5, linespacing=1.25)

ax.text(50, 15.5,
    'AMS HRBP实习生 nelsonmeng  ·  实习期 OKR 规划',
    ha='center', va='center', fontsize=8.5, color='#AAAAAA',
    fontproperties=font_prop, zorder=5)

plt.tight_layout(pad=0.6)
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Pi_Talent_Target_v3.png"
fig.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"\n✅ 已保存: {out}")
