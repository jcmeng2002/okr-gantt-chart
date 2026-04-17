# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 目标框架图 V5 — 终极设计版
π型HRBP — 真正有设计感的信息图
- 大π作为视觉中心(半透明)
- 三张精美卡片对应三个维度
- 底部时间轴
- 腾讯科技风 + 腾讯体 + 高信息密度
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Wedge
import matplotlib.font_manager as fm
import numpy as np

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()
print(f"✅ {font_prop.get_name()}")

# ════════════ 画布 & 配色 ════════════
fig, ax = plt.subplots(figsize=(20, 14), dpi=180)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

C = {
    'blue':   '#0052D9',
    'red':    '#D0443E',
    'purple': '#6B3EF0',
    'green':  '#00A870',
    'orange': '#ED7B2F',
    'dark':   '#1D2129',
    'gray':   '#86909C',
    'light':  '#F2F3F5',
    'bg':     '#F7F8FA',
}

# ━━━━━━━━ 背景 ━━━━━━━━
ax.add_patch(Rectangle((0,0),100,100,fc=C['bg'],zorder=0))
for i in range(50):
    a = 0.006 * (1 - i/50)
    ax.axhspan(i*2, i*2+2, facecolor=C['blue'], alpha=a*0.5, zorder=0)

# ━━━━━━━━ 标题栏 ━━━━━━━━
hdr = FancyBboxPatch((0,92),100,8,
    boxstyle="round,pad=0.01,rounding_size=0", fc=C['blue'], ec='none', zorder=10)
ax.add_patch(hdr)
ax.text(50,96.2,'目标：π 型 HRBP',ha='center',va='center',
    fontsize=20, fontweight='bold', color='white', fontproperties=font_prop, zorder=11)
ax.text(50,93.8,'横贯专业 · 纵深业务 · 延展探索  —  值得业务信赖的好伙伴',
    ha='center', va='center', fontsize=10, color='white', alpha=0.75,
    fontproperties=font_prop, zorder=11)


# ════════════ 大 π 视觉中心 ════════════
pi_x, pi_y = 50, 52
pi_size = 38
ax.text(pi_x, pi_y+2, '\u03c0', ha='center', va='center',
    fontsize=pi_size*3, color='#E8EDFB', fontweight='bold',
    fontproperties=font_prop, alpha=0.35, zorder=1)

# π 笔画装饰线 (粗线条)
lw_pi = 14
pi_c = "#DEE8FD"
# 横
ax.plot([pi_x-pi_size*0.55, pi_x+pi_size*0.55], [pi_y+pi_size*0.35, pi_y+pi_size*0.35],
        '-',color=pi_c,lw=lw_pi,solid_capstyle='round',zorder=1)
# 左竖
ax.plot([pi_x-pi_size*0.22, pi_x-pi_size*0.22], [pi_y-pi_size*0.45, pi_y+pi_size*0.35],
        '-',color=pi_c,lw=lw_pi,solid_capstyle='butt',zorder=1)
# 右腿 (竖+弯)
ax.plot([pi_x+pi_size*0.18, pi_x+pi_size*0.18], [pi_y, pi_y+pi_size*0.35],
        '-',color=pi_c,lw=lw_pi,solid_capstyle='butt',zorder=1)
tx_c=np.linspace(pi_x+pi_size*0.18, pi_x+pi_size*0.48,30)
ty_c=np.ones(30)*pi_y
ax.plot(tx_c,ty_c,'-',color=pi_c,lw=lw_pi,solid_capstyle='round',zorder=1)


# ════════════ 卡片绘制函数 ════════════
def card(x,y,w,h,title,sub,color,items,icon=None,badge=None):
    """精美圆角卡片"""
    # 阴影
    sh = FancyBboxPatch((x+0.3,y-0.3),w,h,
        boxstyle="round,pad=0.02,rounding_size=0.8",
        fc='#00000008',ec='none',zorder=4)
    ax.add_patch(sh)
    # 主体
    body = FancyBboxPatch((x,y),w,h,
        boxstyle="round,pad=0.02,rounding_size=0.8",
        fc='white',ec=color,lw=2,zorder=5,alpha=0.97)
    ax.add_patch(body)
    # 顶部色条
    top = FancyBboxPatch((x+0.15,y+h-0.45),w-0.3,0.45,
        boxstyle="round,pad=0.01,rounding_size=0.25",
        fc=color,ec='none',alpha=0.85,zorder=6)
    ax.add_patch(top)
    
    # 标题区
    ty = y+h-2.0
    # icon circle
    if icon:
        cicon = Circle((x+2.2,ty+0.6),1.1,fc=color,ec='none',alpha=0.12,zorder=7)
        ax.add_patch(cicon)
        ax.text(x+2.2,ty+0.6,icon,ha='center',va='center',
            fontsize=9,color=color,fontweight='bold',zorder=8,fontproperties=font_prop)
        txt_x = x+4.2
    else:
        txt_x = x+1.5
    
    ax.text(txt_x,ty+0.7,title,ha='left',va='center',
        fontsize=12,fontweight='bold',color=color,fontproperties=font_prop,zorder=8)
    if sub:
        ax.text(txt_x,ty-0.95,sub,ha='left',va='center',
            fontsize=7,color=C['gray'],fontproperties=font_prop,zorder=8,style='italic')
    
    # badge
    if badge:
        bw=len(badge)*0.72+1.6
        bb=FancyBboxPatch((x+w-bw-1.2,ty-0.65),bw,2.1,
            boxstyle="round,pad=0.01,rounding_size=0.25",
            fc=color,ec='none',alpha=0.12,lw=0.5,zorder=7)
        ax.add_patch(bb)
        ax.text(x+w-bw/2-1.2,ty+0.37,badge,
            ha='center',va='center',fontsize=6.5,fontweight='bold',
            color=color,fontproperties=font_prop,zorder=8)
    
    # 分割线
    line_y = ty - 2.5 if sub else ty - 2.2
    ax.plot([x+1,x+w-1],[line_y,line_y],'-',color='#EEEEEE',lw=0.8,zorder=7)
    
    # 要点
    sy=line_y-2.2
    step=min((sy-y-1.2)/max(len(items),1),3.8)
    for ii,it in enumerate(items):
        iy=sy-ii*max(step,3.3)
        if iy<y+1.3: break
        # 小色点
        ax.plot(x+1.6,iy,'o',ms=2.8,color=color,zorder=8)
        ax.text(x+2.8,iy,it,ha='left',va='center',fontsize=6.8,
            color=C['dark'],fontproperties=font_prop,zorder=8,linespacing=1.25)


# ════════════ 三张主卡片 ════════════

# --- A. 横贯：专业基石 (上方) ---
card(
    x=16, y=64.5, w=68, h=17,
    title="━ 横贯：专业基石",
    sub="规章制度体系化学习 · 挑起「大梁」— 专业能力过硬",
    color=C['blue'], icon="\u2015",
    badge="[横杠]",
    items=[
        "HR政策体系：OD / 招聘 / 通道 / 绩效 / 培养 / 文化激励 — 重点掌握AMS特有政策要求",
        "CDG HR团队合作模式：运营机制、沟通方式、高效承接部门的HR管理相关工作及需求",
        "组织架构全流程：潜龙体系 / 干部晋升 / 360评估 / 绩效通道管理(目标/考核/面谈/申诉)",
    ]
)

# 连线标注：横杠 → 大梁
ax.annotate("「大梁」\n专业制度撑起\n整个能力基座",
    xy=(50,74), xytext=(88,84),
    fontsize=7.2, color=C['blue'], fontweight='bold',
    fontproperties=font_prop, ha='center', va='bottom',
    arrowprops=dict(arrowstyle='->',color=C['blue'],lw=1.3,
                    connectionstyle='arc3,rad=-0.12',shrinkA=12,shrinkB=5),
    bbox=dict(boxstyle='round,pad=0.35',fc='white',ec=C['blue'],lw=1.2),
    zorder=30)


# --- B. 纵深：业务穿透 (左下) ---
card(
    x=3, y=26, w=29, h=36,
    title="│ 纵深：业务穿透",
    sub="T型人才的核心「一竖」— 深入广告业务 & 团队",
    color=C['red'], icon="\u2502",
    badge="[第一竖]",
    items=[
        "【团队】熟悉AMS各职能/部门合作分工、微广各中心和小组工作",
        "【团队】熟悉并拜访谈微广核心的管理团队、Core team 及人才梯队",
        "【团队】挖掘微广在组织和人才方面的痛点，输出洞察和发现",
        "【团队】和微广团队建立友好连接与亲密互动",
        "【业务】理解AMS的业务逻辑和规划、流量则各平台业务的特征",
        "【业务】关注AMS行业的新趋势和热点、流量业务现状和痛点探寻",
        "【交付】◆ 广告业务学习报告(05-03)",
        "【交付】◆ WXG学习报告(05-10)  |  设计/AI演进报告(05-24)",
    ]
)

# 标注
ax.annotate("「纵深」\n业务穿透是\n核心竞争力",
    xy=(17.5,44), xytext=(1,52),
    fontsize=7.2, color=C['red'], fontweight='bold',
    fontproperties=font_prop, ha='center', va='bottom',
    arrowprops=dict(arrowstyle='->',color=C['red'],lw=1.3,
                    connectionstyle='arc3,rad=0.15',shrinkA=10,shrinkB=5),
    bbox=dict(boxstyle='round,pad=0.35',fc='white',ec=C['red'],lw=1.2),
    zorder=30)


# --- C. 延展：多元探索 (右下) ---
card(
    x=66, y=34, w=31, h=21,
    title="┘ 延展：多元探索",
    sub="多条腿走路 · 探索新事物 — 差异化竞争力来源",
    color=C['purple'], icon="\u2589",
    badge="[右腿]",
    items=[
        "【AI专项】月度探索产出：05-17 → 06-14 → 07-12 → 08-09 四个节点",
        "【研发】理解微广研发业务，输出研发价值链和工作流程图",
        "【协助】协助BP落地日常工作 by case交付大评估等",
    ]
)

# 标注
ax.annotate("「延展」\n多条腿走路\n差异化竞争力",
    xy=(81.5,44.5), xytext=(96,54),
    fontsize=7.2, color=C['purple'], fontweight='bold',
    fontproperties=font_prop, ha='center', va='bottom',
    arrowprops=dict(arrowstyle='->',color=C['purple'],lw=1.3,
                    connectionstyle='arc3,rad=-0.15',shrinkA=10,shrinkB=5),
    bbox=dict(boxstyle='round,pad=0.35',fc='white',ec=C['purple'],lw=1.2),
    zorder=30)


# --- D. 夯实根基 (中间) ---
card(
    x=34, y=33, w=29, h=19,
    title="+ 夯实根基",
    sub="新人培训 & 文化融入 & 人才培养",
    color=C['green'],
    items=[
        "【培训】AMS新人培训课程 (至05-03)  |  【培训】公司课程学习 (至04-19)",
        "【文化】文化荣誉激励体系  |  【培养】培养体系现状梳理  |  【招聘】招聘编制管理(BP合作)",
    ]
)

# 标注
ax.annotate("「地基」\n培训与文化\n融入基础层",
    xy=(48.5,42), xytext=(48.5,26),
    fontsize=7.2, color=C['green'], fontweight='bold',
    fontproperties=font_prop, ha='center', va='top',
    arrowprops=dict(arrowstyle='->',color=C['green'],lw=1.3,
                    connectionstyle='arc3,rad=0',shrinkA=10,shrinkB=5),
    bbox=dict(boxstyle='round,pad=0.35',fc='white',ec=C['green'],lw=1.2),
    zorder=30)


# ════════════ 底部时间轴 ════════════
ax.plot([8,92],[21,21],'-',color='#E0E3E8',lw=2,zorder=3,solid_capstyle='round')

ms = [
    ("04-12","入职",C['blue'],10),
    ("04-19","公司课",C['blue'],22),
    ("04-26","阶段1完成",C['red'],33),
    ("05-03","广告报告",C['orange'],43),
    ("05-10","WXG报告",C['orange'],53),
    ("05-24","演进报告",C['green'],64),
    ("05~08月","AI持续",C['purple'],76),
    ("持续","在岗实践",C['green'],87),
]
for lb,ds,col,mx in ms:
    ax.plot(mx,21,'o',ms=6,color=col,mec='white',mew=1.5,zorder=8)
    ax.text(mx,19.5,lb,ha='center',va='top',fontsize=6.5,
        fontweight='bold',color=col,fontproperties=font_prop,zorder=8)
    ax.text(mx,17.8,ds,ha='center',va='top',fontsize=5.5,
        color=C['gray'],fontproperties=font_prop,zorder=8)

ax.text(50,14.5,'\u2500\u2500\u2500  关键里程碑时间轴  \u2500\u2500\u2500',
    ha='center',va='center',fontsize=8,color=C['gray'],alpha=0.45,
    fontproperties=font_prop,zorder=5)
ax.text(50,11.5,'AMS HRBP实习生 nelsonmeng  \u00b7  实习期 OKR 规划',
    ha='center',va='center',fontsize=8.5,color='#BBBBBB',
    fontproperties=font_prop,zorder=5)

plt.tight_layout(pad=0.5)
out="/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Pi_Talent_Target_v5.png"
fig.savefig(out,dpi=200,bbox_inches='tight',facecolor='white')
plt.close(fig)
print(f"\n✅ {out}")
