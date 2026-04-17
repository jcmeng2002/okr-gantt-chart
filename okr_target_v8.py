# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 目标框架图 V8
严格仿照用户提供的原始模板图（3D型HRBP三列式）
内容100%来自O1.docx OKR文档，不做任何杜撰
改进：紧凑布局 · 大字体 · 腾讯风
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
import matplotlib.font_manager as fm
import numpy as np

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()

fig, ax = plt.subplots(figsize=(18, 11), dpi=180)
ax.set_xlim(0, 100); ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

# 配色 — 参考原图的红/绿/蓝
C1 = "#C41E00"   # 懂组织 - 红
C2 = "#00A870"   # 懂政策 - 绿  
C3 = "#0052D9"   # 懂业务 - 蓝
C_HDR = "#0052D9"
K = "#222222"; Gy = "#555555"

# ══════════ 标题栏 ══════════
hdr = FancyBboxPatch((0,92.5),100,7.5,
    boxstyle="square,pad=0",fc=C_HDR,ec='none',zorder=10)
ax.add_patch(hdr)
ax.text(50,97,
    '目标：3D型HRBP：懂组织、懂政策、懂业务 —— 值得业务信赖的好伙伴',
    ha='center',va='center',fontsize=15,fontweight='bold',color='white',
    fontproperties=font_prop,zorder=11)

# ══════════ 三列定义（内容100%来自OKR文档） ══════════
col_w = 29; gap = 2; x0 = 4.5

cols = [
    {
        "title": "懂组织", "color": C1, "x": x0,
        "bullets": [
            "熟悉AMS各职能/部门合作和分工",
            "熟悉微广的各中心和小组工作",
            "熟悉并拜访谈微广核心的管理团队",
            "熟悉并访谈微广Core team及梯队",
            "挖掘微广在组织和人才方面的痛点，\n输出洞察和发现",
            "和微广团队建立友好连接和亲密互动",
        ],
        "tags": [("组织", C1), ("人才", C1)],
        "summary": "懂组织和人才；\n和团队建立连接",
    },
    {
        "title": "懂政策", "color": C2, 
        "x": x0 + col_w + gap,
        "bullets": [
            "熟悉和BP相关的HR政策\n（重点OD、招聘、通道），\n其中AMS特有的政策需要重点了解",
            "熟悉CDG HR团队的合作模式、\n运营机制、沟通方式",
            "高效承接部门的HR管理相关工作及需求",
        ],
        "tags": [("政策", C2), ("机制", C2)],
        "summary": "懂政策和机制；\n给团队提供支持",
    },
    {
        "title": "懂业务", "color": C3,
        "x": x0 + 2*(col_w + gap),
        "bullets": [
            "理解AMS的业务逻辑和规划、\n流量则各平台业务的特征",
            "关注AMS行业的新趋势和热点",
            "挖掘流量业务的现状和痛点，\n并探寻HR在里面可以做什么",
            "理解微广研发业务，\n输出研发价值链和工作流程图",
        ],
        "tags": [("业务", C3), ("研发", C3)],
        "summary": "懂AMS和研发；\n梳理业务流程",
    },
]

# ══════════ 绘制三列 ══════════
for ci, col in enumerate(cols):
    cx = col["x"]; co = col["color"]
    
    # 列背景框
    bg = FancyBboxPatch((cx, 14), col_w, 75,
        boxstyle="round,pad=0.02,rounding_size=0.6",
        fc='#FAFAFA',ec=co,lw=2.2,zorder=3)
    ax.add_patch(bg)
    
    # 列标题区（带浅色底）
    tb = FancyBboxPatch((cx+0.8, 84.5), col_w-1.6, 4,
        boxstyle="round,pad=0.01,rounding_size=0.35",
        fc=co,ec='none',alpha=0.13,zorder=4)
    ax.add_patch(tb)
    ax.text(cx+col_w/2, 86.5, col["title"],
        ha='center',va='center',fontsize=14,fontweight='bold',color=co,
        fontproperties=font_prop,zorder=5)
    
    # 要点列表 — 紧凑！字号9pt
    by_start = 82
    line_h = min(10.8 / max(len(col["bullets"]), 1), 9.5)
    for bi, bullet in enumerate(col["bullets"]):
        by = by_start - bi * line_h
        if by < 17:
            break
        ax.plot(cx+1.6, by, 'o', ms=3.5, color=co, zorder=5)
        ax.text(cx+3.2, by, bullet, ha='left', va='center',
            fontsize=9, color=K, fontproperties=font_prop, zorder=5, linespacing=1.28)
    
    # 右侧标签组 + 大括号
    tags = col["tags"]
    tg_x = cx + col_w - 2.5
    tg_top = by_start - 1
    tg_bot = tg_top - (len(tags)-1)*7 - 1
    tg_mid = (tg_top + tg_bot) / 2
    
    # 简单括号线
    bx = tg_x + 2.2
    ax.plot([bx,bx+1],[tg_top,tg_top],'-',co,lw=1.4,zorder=4)      # 上横
    ax.plot([bx,bx+1],[tg_bot,tg_bot],'-',co,lw=1.4,zorder=4)      # 下横
    ax.plot([bx+0.5]*2,[tg_top,tg_mid],'-',co,lw=1.4,zorder=4)     # 上竖
    ax.plot([bx+0.5]*2,[tg_mid,tg_bot],'-',co,lw=1.4,zorder=4)     # 下竖
    
    for ti,(tn,tc) in enumerate(tags):
        ty = tg_top - ti*7
        ax.text(tg_x+1.4, ty, tn, ha='center',va='center',
            fontsize=10, fontweight='bold', color=tc, fontproperties=font_prop, zorder=5)

# ══════════ 底部箭头流程区 ══════════
flow_y = 8
centers = [c["x"]+col_w/2 for c in cols]
for ci,cx in enumerate(centers):
    ax.text(cx, flow_y+1.8, cols[ci]["summary"],
        ha='center',va='center',fontsize=9,color=C_HDR,fontweight='bold',
        fontproperties=font_prop,zorder=6)

ay = flow_y - 0.8
for sx,ex in [(centers[0]+col_w/2+2, centers[1]-col_w/2-2),
              (centers[1]+col_w/2+2, centers[2]-col_w/2-2)]:
    ax.annotate('',xy=(ex,ay),xytext=(sx,ay),
        arrowprops=dict(arrowstyle='->',color=C_HDR,lw=2.8,
                        mutation_scale=22),zorder=6)

plt.tight_layout(pad=0.5)
out='/Users/mengjiachen/WorkBuddy/20260414135125/OKR_3D_HRBP_Target_v8.png'
fig.savefig(out,dpi=200,bbox_inches='tight',facecolor='white')
plt.close(fig)
print(f'✅ {out}')
