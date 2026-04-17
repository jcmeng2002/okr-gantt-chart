# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 目标框架图 V4 — π型人才(设计感版)
π是画面主角，每个笔画承载内容，腾讯科技风信息图
- 横杠 → 「横贯」专业基石 (蓝色)
- 左竖 → 「纵深」业务穿透 (红色)
- 右腿 → 「延展」多元探索 (紫色)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path
import numpy as np

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()
print(f"✅ 腾讯体已加载: {font_prop.get_name()}")

# ============================================================
# 画布
# ============================================================
fig, ax = plt.subplots(figsize=(20, 15), dpi=180)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

# 颜色系统 — 腾讯科技风
C_BLUE    = "#0052D9"   # 主蓝 - 专业
C_RED     = "#E03A3E"   # 红 - 业务纵深
C_PURPLE  = "#7B61FF"   # 紫 - 探索延展
C_GREEN   = "#00A870"   # 绿 - 基础
C_ORANGE  = "#ED7B2F"   # 橙 - 交付节点
C_DARK    = "#1a1a2e"   # 深色文字
C_GRAY    = "#888888"
C_BG      = "#F7F9FC"

# ════════════ 渐变背景 ════════════
for i in range(100):
    alpha = 0.008 * (1 - i/100)
    ax.axhspan(i, i+1, facecolor=C_BLUE, alpha=alpha*0.4, zorder=0)

# ════════════ 标题区 ════════════
title_box = FancyBboxPatch(
    (2, 92.5), 96, 6.5,
    boxstyle="round,pad=0.02,rounding_size=0.6",
    facecolor=C_BLUE, edgecolor='none', zorder=10,
    transform=ax.transData
)
ax.add_patch(title_box)

# 标题装饰线
ax.plot([2, 98], [95.5, 95.5], '-', color='white', lw=0.5, alpha=0.25, zorder=11)

ax.text(50, 95.8,
    'π · P A I  T Y P E   H R B P',
    ha='center', va='center', fontsize=11, color='white',
    fontproperties=font_prop, alpha=0.55, zorder=11)

ax.text(50, 94.2,
    '目标：π型HRBP —— 横贯专业 · 纵深业务 · 延展探索',
    ha='center', va='center', fontsize=16, fontweight='bold', color='white',
    fontproperties=font_prop, zorder=12)

ax.text(50, 93.0,
    '值得业务信赖的好伙伴  |  AMS HRBP实习生 nelsonmeng',
    ha='center', va='center', fontsize=8.5, color='white', alpha=0.75,
    fontproperties=font_prop, zorder=12)


# ============================================================
# ★ π 绘制 — 每个笔画是一个带圆角的内容容器
# ============================================================

def draw_pi_stroke(vertices, color, label, sublabel, items, label_pos='top'):
    """
    绘制π的一个笔画区域
    vertices: [(x,y), ...] 定义形状顶点
    """
    codes = [Path.MOVETO]
    for _ in range(len(vertices) - 2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
    
    path = Path(vertices, codes)
    
    # 外层阴影
    shadow = PathPatch(path, facecolor=color, alpha=0.06,
                       transform=ax.transData, zorder=2)
    ax.add_patch(shadow)
    # 移动一点做偏移效果
    
    # 主体填充
    fill = PathPatch(path, facecolor='white', edgecolor=color,
                     linewidth=2.8, alpha=0.95,
                     transform=ax.transData, zorder=5)
    ax.add_patch(fill)
    
    # 内部浅色填充
    inner_fill = PathPatch(path, facecolor=color, alpha=0.05,
                           transform=ax.transData, zorder=4)
    ax.add_patch(inner_fill)
    
    return path


# ──────────── π 的三个笔画坐标定义 ────────────

# === 1. 横杠: 横贯 — 专业基石 ===
heng_vertices = np.array([
    [22, 70],
    [78, 70],
    [76, 82],
    [24, 82],
])
draw_pi_stroke(heng_vertices, C_BLUE, "横", "专业基石", [], 'center')

# 横杠内容
ax.text(50, 79.5, "━ 横贯：专业基石",
    ha='center', va='center', fontsize=13, fontweight='bold',
    color=C_BLUE, fontproperties=font_prop, zorder=20)
ax.text(50, 77.5, "规章制度体系化学习 · 挑起「大梁」",
    ha='center', va='center', fontsize=8, color=C_GRAY,
    fontproperties=font_prop, zorder=20)

heng_items = [
    ("HR政策体系", "OD / 招聘 / 通道 / 绩效 / 培养"),
    ("CDG HR合作模式", "运营机制、沟通方式"),
    ("组织架构全流程", "潜龙 / 干部晋升 / 360评估"),
]
for idx, (t, d) in enumerate(heng_items):
    ix = 28 + idx * 17
    ax.plot(ix, 74.2, 's', markersize=5, color=C_BLUE, alpha=0.85, zorder=20)
    ax.text(ix + 1.5, 74.2, t, ha='left', va='center', fontsize=7.5,
        fontweight='bold', color=C_DARK, fontproperties=font_prop, zorder=20)
    ax.text(ix + 1.5, 72.5, d, ha='left', va='center', fontsize=6.5,
        color=C_GRAY, fontproperties=font_prop, zorder=20)


# === 2. 左竖: 纵深 — 业务穿透 ===
zong_vertices = np.array([
    [14, 22],
    [26, 22],
    [28, 34],
    [28, 68],
    [18, 68],
    [16, 56],
    [16, 34],
    [12, 34],
])
draw_pi_stroke(zong_vertices, C_RED, "竖", "业务穿透", [], 'right')

# 左竖内容
ax.text(19.5, 65, "│ 纵深：业务穿透",
    ha='center', va='center', fontsize=13, fontweight='bold',
    color=C_RED, fontproperties=font_prop, zorder=20)
ax.text(19.5, 63, "T型人才的「一竖」\n深入广告业务 & 团队",
    ha='center', va='center', fontsize=7.2, color=C_GRAY,
    fontproperties=font_prop, zorder=20, linespacing=1.35)

zong_items_left = [
    ("【团队】AMS各职能分工 / 微广各中心工作"),
    ("【团队】访谈管理团队 & Core team梯队"),
    ("【团队】挖掘组织人才痛点 · 输出洞察"),
    ("【团队】建立友好连接与亲密互动"),
]
zong_items_right = [
    ("【业务】AMS逻辑 / 规划 / 流量特征"),
    ("【行业】趋势热点 · 流量现状痛点"),
]

for idx, item in enumerate(zong_items_left):
    iy = 57.5 - idx * 6.5
    ax.plot(13.8, iy, 'o', markersize=3.2, color=C_RED, zorder=20)
    ax.text(15.2, iy, item, ha='left', va='center', fontsize=6.6,
        color=C_DARK, fontproperties=font_prop, zorder=20)

for idx, item in enumerate(zong_items_right):
    iy = 57.5 - idx * 6.5
    ax.plot(23.5, iy, 'D', markersize=2.8, color=C_ORANGE, zorder=20)
    ax.text(25, iy, item, ha='left', va='center', fontsize=6.6,
        color=C_DARK, fontproperties=font_prop, zorder=20)

# 交付标签
delivery_y = 29.5
deliv_box = FancyBboxPatch((12.5, delivery_y), 17, 4.5,
    boxstyle="round,pad=0.02,rounding_size=0.4",
    facecolor=C_RED, alpha=0.1, edgecolor=C_RED, linewidth=1.2, zorder=18)
ax.add_patch(deliv_box)
ax.text(21, delivery_y + 2.3, "◆ 交付节点",
    ha='center', va='center', fontsize=7, fontweight='bold', color=C_RED,
    fontproperties=font_prop, zorder=20)
ax.text(21, delivery_y + 0.8,
    "广告报告(5/3)  WXG(5/10)  演进报告(5/24)",
    ha='center', va='center', fontsize=6, color=C_RED, alpha=0.8,
    fontproperties=font_prop, zorder=20)


# === 3. 右腿: 延展 — 多元探索 ===
yan_vertices = np.array([
    [66, 44],
    [74, 44],
    [88, 44],
    [86, 54],
    [72, 54],
    [72, 68],
    [64, 68],
    [64, 52],
    [62, 48],
    [62, 46],
    [64, 44],
])
draw_pi_stroke(yan_vertices, C_PURPLE, "腿", "延展探索", [], 'left')

# 右腿内容
ax.text(71, 65, "┘ 延展：多元探索",
    ha='center', va='center', fontsize=13, fontweight='bold',
    color=C_PURPLE, fontproperties=font_prop, zorder=20)
ax.text(71, 63, "多条腿走路\n探索新事物 · 差异化竞争力",
    ha='center', va='center', fontsize=7, color=C_GRAY,
    fontproperties=font_prop, zorder=20, linespacing=1.3)

yan_items = [
    ("AI专项月度产出", ["5/17 → 6/14", "→ 7/12 → 8/09"]),
    ("微广研发价值链", ["输出研发价值链", "& 工作流程图"]),
    ("协助BP日常工作", ["by case交付", "大评估等"]),
]

for idx, (title, lines) in enumerate(yan_items):
    iy = 57 - idx * 8
    ax.text(67, iy, title, ha='left', va='center', fontsize=7.5,
        fontweight='bold', color=C_DARK, fontproperties=font_prop, zorder=20)
    for li, line in enumerate(lines):
        ax.text(69, iy - 2 - li * 2, f"· {line}", ha='left', va='center',
            fontsize=6, color=C_GRAY, fontproperties=font_prop, zorder=20)


# === 4. 中间基础区: + 夯实根基 ===
base_vertices = np.array([
    [32, 38],
    [60, 38],
    [58, 56],
    [34, 56],
])
draw_pi_stroke(base_vertices, C_GREEN, "基", "夯实根基", [], 'top')

ax.text(46, 53, "+ 夯实根基",
    ha='center', va='center', fontsize=12, fontweight='bold',
    color=C_GREEN, fontproperties=font_prop, zorder=20)
ax.text(46, 51, "新人培训 · 文化融入 · 人才培养",
    ha='center', va='center', fontsize=7, color=C_GRAY,
    fontproperties=font_prop, zorder=20)

base_items = [
    ("AMS新人培训课程", "至 05-03"),
    ("公司课程学习", "至 04-19"),
    ("文化荣誉激励体系", ""),
    ("培养体系 / 招聘编制", ""),
]
for idx, (t, d) in enumerate(base_items):
    bx = 34 + (idx % 2) * 13
    by = 47 - (idx // 2) * 5.5
    full = f"{t} {d}".strip()
    ax.plot(bx, by, 'o', markersize=3.5, color=C_GREEN, zorder=20)
    ax.text(bx + 1.5, by, full, ha='left', va='center', fontsize=6.5,
        color=C_DARK, fontproperties=font_prop, zorder=20)


# ============================================================
# ★ 结构标注 — 连接线 + 说明气泡
# ============================================================
callouts = [
    {"xy": (50, 80), "pos": (90, 87),
     "text": "「大梁」\n专业制度撑起\nHRBP能力基座", "color": C_BLUE},
    {"xy": (19.5, 45), "pos": (3, 42),
     "text": "「纵深」\n业务穿透是T型\n人才核心竞争力", "color": C_RED},
    {"xy": (73, 49), "pos": (93, 40),
     "text": "「延展」\n多条腿走路\n差异化竞争力", "color": C_PURPLE},
    {"xy": (46, 43), "pos": (46, 30),
     "text": "「地基」\n培训与文化融入", "color": C_GREEN},
]

for c in callouts:
    ax.annotate(c["text"],
        xy=c["xy"], xytext=c["pos"],
        fontsize=7, color=c["color"], fontweight='bold',
        fontproperties=font_prop, ha='center', va='bottom' if c["pos"][1] < c["xy"][1] else 'bottom',
        arrowprops=dict(arrowstyle='->', color=c["color"], lw=1.5,
                        connectionstyle='arc3,rad=0.15',
                        shrinkA=8, shrinkB=4),
        bbox=dict(boxstyle='round,pad=0.35', fc='white', ec=c["color"],
                  lw=1.2, alpha=0.97),
        zorder=30)


# ============================================================
# ★ 底部时间轴
# ============================================================
ax.plot([10, 90], [18.5, 18.5], '-', color='#D0D5DD', lw=2, zorder=3,
        solid_capstyle='round')

milestones = [
    ("04-12", "入职", C_BLUE, 12),
    ("04-19", "公司课", C_BLUE, 23),
    ("04-26", "阶段1完成", C_RED, 34),
    ("05-03", "广告报告", C_ORANGE, 44),
    ("05-10", "WXG报告", C_ORANGE, 55),
    ("05-24", "演进报告", C_GREEN, 66),
    ("05-08月", "AI持续", C_PURPLE, 77),
    ("持续", "在岗实践", C_GREEN, 88),
]

for label, desc, col, mx in milestones:
    ax.plot(mx, 18.5, 'o', markersize=7, color=col, zorder=8,
            markeredgecolor='white', markeredgewidth=1.5)
    ax.text(mx, 16.8, label,
        ha='center', va='top', fontsize=6.5, fontweight='bold', color=col,
        fontproperties=font_prop, zorder=8)
    ax.text(mx, 15.2, desc,
        ha='center', va='top', fontsize=5.5, color=C_GRAY,
        fontproperties=font_prop, zorder=8)

# 时间轴标题
ax.text(50, 13, "━━━ 关键里程碑时间轴 ━━━",
    ha='center', va='center', fontsize=8, color=C_GRAY, alpha=0.5,
    fontproperties=font_prop, zorder=5)


# ============================================================
# ★ 角落装饰元素
# ============================================================
# 左上角 π 大字装饰
ax.text(5, 89, 'π',
    ha='left', va='top', fontsize=36, color=C_BLUE,
    fontweight='bold', fontproperties=font_prop, alpha=0.08, zorder=1)

# 右下角装饰
ax.text(96, 3, 'v4',
    ha='right', va='bottom', fontsize=8, color='#CCCCCC',
    fontproperties=font_prop, zorder=5)


plt.tight_layout(pad=0.8)
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Pi_Talent_Target_v4.png"
fig.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"\n✅ 已保存: {out}")
