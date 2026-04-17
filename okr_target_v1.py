# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 目标框架图 — 3D型HRBP风格
仿照用户提供的目标图模板，基于O1.docx的OKR内容重新绘制
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from datetime import datetime

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()
print(f"✅ 腾讯体已加载: {font_prop.get_name()}")

# ============================================================
# ★ 图表配置
# ============================================================
fig, ax = plt.subplots(figsize=(18, 10), dpi=180)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

# 颜色定义
COLOR_HEADER_BG   = "#0052D9"      # 标题栏蓝
COLOR_COL1         = "#C41E00"      # 懂组织-红
COLOR_COL2         = "#00B96B"      # 懂政策-绿
COLOR_COL3         = "#0052D9"      # 懂业务-蓝
COLOR_ARROW        = "#0070E0"      # 箭头蓝
COLOR_TEXT_MAIN    = "#333333"

col_w = 30          # 每列宽度
col_gap = 4.5       # 列间距
start_x = 3.5       # 第一列起始x

# ══════════════════ 1. 顶部标题栏 ══════════════════
header = mpatches.FancyBboxPatch(
    (0, 90), 100, 9,
    boxstyle="round,pad=0.02,rounding_size=0.6",
    facecolor=COLOR_HEADER_BG, edgecolor='none', zorder=10
)
ax.add_patch(header)
ax.text(50, 94.5,
    '目标：3D型HRBP：懂组织、懂政策、懂业务 —— 值得业务信赖的好伙伴',
    ha='center', va='center', fontsize=15, fontweight='bold', color='white',
    fontproperties=font_prop, zorder=11)

# ══════════════════ 2. 三列数据定义 ══════════════════
columns_data = [
    # ---- 懂组织 (红) ----
    {
        "title": "懂组织",
        "color": COLOR_COL1,
        "x": start_x,
        "bullets": [
            "熟悉AMS各职能/部门合作和分工",
            "熟悉微广的各中心和小组工作",
            "熟悉并拜访谈微广核心的管理团队",
            "熟悉并访谈微广 Core team 及梯队",
            "挖掘微广在组织和人才方面的痛点，\n输出洞察和发现",
            "和微广团队建立友好连接和亲密互动",
        ],
        "tags": [("组织", COLOR_COL1), ("人才", COLOR_COL1)],
        "summary": "懂组织和人才；\n和团队建立连接",
    },
    # ---- 懂政策 (绿) ----
    {
        "title": "懂政策",
        "color": COLOR_COL2,
        "x": start_x + col_w + col_gap,
        "bullets": [
            "熟悉和BP相关的HR政策（重点OD、招聘、通道），\n其中AMS特有的政策需要重点了解",
            "熟悉 CDG HR 团队的合作模式、运营机制、\n沟通方式",
            "高效承接部门的HR管理相关工作及需求",
        ],
        "tags": [("政策", COLOR_COL2), ("机制", COLOR_COL2)],
        "summary": "懂政策和机制；\n给团队提供支持",
    },
    # ---- 懂业务 (蓝) ----
    {
        "title": "懂业务",
        "color": COLOR_COL3,
        "x": start_x + 2*(col_w + col_gap),
        "bullets": [
            "理解AMS的业务逻辑和规划、流量则\n各平台业务的特征",
            "关注AMS行业的新趋势和热点",
            "挖掘流量业务的现状和痛点，并探寻\nHR在里面可以做什么",
            "理解微广研发业务，输出研发价值链\n和工作流程图",
        ],
        "tags": [("业务", COLOR_COL3), ("研发", COLOR_COL3)],
        "summary": "懂AMS和研发；\n梳理业务流程",
    },
]

# ══════════════════ 3. 绘制三列 ══════════════════
for idx, col in enumerate(columns_data):
    x0 = col["x"]
    color = col["color"]

    # --- 列背景框 ---
    bg = mpatches.FancyBboxPatch(
        (x0, 12), col_w, 74,
        boxstyle="round,pad=0.02,rounding_size=0.5",
        facecolor='#FAFAFA', edgecolor=color, linewidth=2, zorder=3
    )
    ax.add_patch(bg)

    # --- 列标题 ---
    title_bg = mpatches.FancyBboxPatch(
        (x0 + 0.5, 79.5), col_w - 1, 5.5,
        boxstyle="round,pad=0.01,rounding_size=0.35",
        facecolor=color, edgecolor='none', alpha=0.15, zorder=4
    )
    ax.add_patch(title_bg)
    ax.text(x0 + col_w/2, 82.25, col["title"],
        ha='center', va='center', fontsize=14, fontweight='bold', color=color,
        fontproperties=font_prop, zorder=5)

    # --- 要点列表 ---
    bullet_y_start = 76
    for bi, bullet in enumerate(col["bullets"]):
        by = bullet_y_start - bi * 9.8
        # 圆点
        ax.plot(x0 + 1.8, by, 'o', markersize=4.5, color=color, zorder=5)
        # 文字
        ax.text(x0 + 3.2, by, bullet,
            ha='left', va='center', fontsize=7.6, color=COLOR_TEXT_MAIN,
            fontproperties=font_prop, zorder=5,
            linespacing=1.35)

    # --- 右侧标签组 (带括号) ---
    n_tags = len(col["tags"])
    tag_x = x0 + col_w - 1.2
    tag_y_top = bullet_y_start - 2
    tag_spacing = 7

    # 右大括号
    brace_x = tag_x + 2.8
    brace_top = tag_y_top + 1.5
    brace_bottom = tag_y_top - (n_tags - 1) * tag_spacing - 1.5
    brace_mid = (brace_top + brace_bottom) / 2

    # 简单的括号线（用path绘制）
    import numpy as np
    bx = np.array([brace_x, brace_x+1.2, brace_x+1.2, brace_x])
    by_arr = np.array([brace_top, brace_top, brace_bottom, brace_bottom])
    ax.plot(bx[:2], by_arr[:2], '-', color=color, lw=1.5, zorder=4)   # 上横
    ax.plot(bx[2:], by_arr[2:], '-', color=color, lw=1.5, zorder=4)     # 下横
    ax.plot([brace_x+0.6]*2, [brace_top, brace_mid], '-', color=color, lw=1.5, zorder=4)  # 左上竖
    ax.plot([brace_x+0.6]*2, [brace_mid, brace_bottom], '-', color=color, lw=1.5, zorder=4)  # 左下竖

    for ti, (tag_text, tag_color) in enumerate(col["tags"]):
        ty = tag_y_top - ti * tag_spacing
        ax.text(tag_x + 1.4, ty, tag_text,
            ha='center', va='center', fontsize=9, color=tag_color,
            fontweight='bold', fontproperties=font_prop, zorder=5)

# ══════════════════ 4. 底部箭头流程区 ══════════════════
flow_y = 5.5
col_centers = [c["x"] + col_w/2 for c in columns_data]

for ci, cx in enumerate(col_centers):
    # 流程文字
    summary_text = columns_data[ci]["summary"]
    ax.text(cx, flow_y + 0.8, summary_text,
        ha='center', va='center', fontsize=9, color=COLOR_ARROW, fontweight='bold',
        fontproperties=font_prop, zorder=6)

# 箭头（列之间）
arrow_y = flow_y - 1.2
arr1_x = col_centers[0] + col_w/2 + 1
arr2_x = col_centers[1] - col_w/2 - 1
arr3_x = col_centers[1] + col_w/2 + 1
arr4_x = col_centers[2] - col_w/2 - 1

for sx, ex in [(arr1_x, arr2_x), (arr3_x, arr4_x)]:
    ax.annotate('', xy=(ex, arrow_y), xytext=(sx, arrow_y),
        arrowprops=dict(arrowstyle='->', color=COLOR_ARROW, lw=3,
                        mutation_scale=20), zorder=6)

plt.tight_layout(pad=0.5)
out = "/Users/mengjiachen/WorkBuddy/20260414135125/OKR_3D_HRBP_Target_v1.png"
fig.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"\n✅ 已保存: {out}")
