# -*- coding: utf-8 -*-
"""
V7 — 紧凑高密度 π型人才OKR目标图
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.font_manager as fm
import numpy as np

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()

fig, ax = plt.subplots(figsize=(16, 12), dpi=180)
ax.set_xlim(0, 100); ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('#F5F6FA')

B='#0052D9'; R='#C92A2A'; P='#7048E8'; G='#087F5B'; O='#E67700'
K='#212529'; Gy='#6C757D'

ax.add_patch(Rectangle((0,0),100,100,fc='#F5F6FA',zorder=0))

# 标题
hdr=FancyBboxPatch((0,93),100,7,boxstyle="square,pad=0",fc=B,ec='none',zorder=10)
ax.add_patch(hdr)
ax.text(50,97.2,'目标：π 型 HRBP',ha='center',va='center',
    fontsize=20,fontweight='bold',color='white',fontproperties=font_prop,zorder=11)
ax.text(50,94.3,'横贯专业 · 纵深业务 · 延展探索 — 值得业务信赖的好伙伴',
    ha='center',va='center',fontsize=10,color='white',alpha=0.75,
    fontproperties=font_prop,zorder=11)

# π 绘制
pcx,pcy,sc = 50,49,32
hx=[pcx-sc*0.55,pcx+sc*0.58]; hy=[pcy+sc*0.30]*2
vx=[pcx-sc*0.19]*2; vy=[pcy-sc*0.38,pcy+sc*0.30]
rx=[pcx+sc*0.14]*2; ry=[pcy-sc*0.02,pcy+sc*0.30]
rcx=np.linspace(pcx+sc*0.14,pcx+sc*0.44,25); rcy=np.ones(25)*(pcy-sc*0.02)

for sxx,syy in [(hx,hy),(vx,vy),(rx,ry),(rcx,rcy)]:
    ax.plot(sxx,syy,'-',alpha=0.03,lw=28,color='#333',solid_capstyle='round' if len(sxx)>2 else 'butt',zorder=1)
ax.plot(hx,hy,'-',color=B,lw=14,solid_capstyle='round',zorder=4)
ax.plot(vx,vy,'-',color=R,lw=14,solid_capstyle='butt',zorder=4)
ax.plot(rx,ry,'-',color=P,lw=14,solid_capstyle='butt',zorder=4)
ax.plot(rcx,rcy,'-',color=P,lw=14,solid_capstyle='round',zorder=4)
for sxx,syy in [(hx,hy),(vx,vy),(rx,ry),(rcx,rcy)]:
    ax.plot(sxx,syy,'-',color='#FFFFFF18',lw=4,solid_capstyle='round' if len(sxx)>2 else 'butt',zorder=5)
ax.plot(hx,hy,'-',color=B,lw=3,solid_capstyle='round',zorder=6)
ax.plot(vx,vy,'-',color=R,lw=3,solid_capstyle='butt',zorder=6)
ax.plot(rx,ry,'-',color=P,lw=3,solid_capstyle='butt',zorder=6)
ax.plot(rcx,rcy,'-',color=P,lw=3,solid_capstyle='round',zorder=6)

# 标注块
def blk(x,y,w,h,tit,sub,items,c,ato=None,ac=None):
    bb=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.015,rounding_size=0.5",
        fc='white',edgecolor=c,lw=2,zorder=13,alpha=0.96)
    ax.add_patch(bb)
    ax.add_patch(FancyBboxPatch((x+0.12,y+h-0.35),w-0.24,0.35,
        boxstyle="round,pad=0.008,rounding_size=0.15",fc=c,ec='none',alpha=0.85,zorder=14))
    ty=y+h-1.6; tx=x+(1.0 if x<45 else w-1.0); ha_t='left' if x<45 else 'right'
    ax.text(tx,ty+0.4,tit,ha=ha_t,va='center',fontsize=11.5,
        fontweight='bold',color=c,fontproperties=font_prop,zorder=15)
    if sub:
        ax.text(tx,ty-0.75,sub,ha=ha_t,va='center',fontsize=7.5,
            color=Gy,fontproperties=font_prop,zorder=15,style='italic')
    dly=ty-2.0 if sub else ty-1.7
    ax.plot([x+0.8,x+w-0.8],[dly,dly],'-',color='#E9ECEF',lw=0.8,zorder=14)
    sy=dly-1.6; sp=min(max((sy-y-0.8)/max(len(items),1),3.0),3.8)
    for ii,it in enumerate(items):
        iy=sy-ii*sp
        if iy<y+0.8: break
        px=x+1.0 if ha_t=='left' else x+w-1.0
        ax.plot(px,iy,'o',ms=2.8,color=c,zorder=15)
        off=1.5 if ha_t=='left' else -1.5
        ax.text(px+off,iy,it,ha=ha_t,va='center',fontsize=9,
            color=K,fontproperties=font_prop,zorder=15,linespacing=1.22)
    if ato and ac:
        if x+w/2<pcx: af=(x+w+0.2,y+h/2)
        elif x>pcx: af=(x-0.2,y+h/2)
        else: af=(x+w/2,y-0.2)
        ax.annotate('',xy=ato,xytext=af,
            arrowprops=dict(arrowstyle='->',color=ac,lw=1.4,
                connectionstyle='arc3,rad=0.1',shrinkA=2,shrinkB=6),zorder=11)

# 三块内容
blk(x=10,y=71,w=80,h=20,tit='━ 横贯：专业基石',
    sub='规章制度体系化学习 · 新人培训文化融入 · 挑起「大梁」',
    items=[
        '【HR政策体系】OD / 招聘 / 通道 / 绩效 / 培养 / 文化激励 — AMS特有政策重点掌握',
        '【CDG合作】运营机制、沟通方式、高效承接部门HR管理相关工作及需求',
        '【组织架构】潜龙 / 干部晋升 / 360评估 / 绩效通道全流程(目标/考核/面谈/申诉)',
        '【基础夯实】AMS新人培训(至05-03) · 公司课程(04-19) · 培养/招聘编制',
    ],c=B,ato=(pcx,pcy+sc*0.30),ac=B)

blk(x=2,y=24,w=33,h=42,tit='│ 纵深：业务穿透',
    sub='T型人才的「一竖」— 深入广告 & 团队',
    items=[
        '【团队】熟悉AMS各职能/部门分工、微广各中心工作内容',
        '【团队】拟访微广核心管理团队、Core team 及人才梯队',
        '【团队】挖掘组织人才痛点，输出洞察发现，建立亲密互动',
        '【业务】理解AMS业务逻辑/规划/流量平台特征',
        '【业务】关注行业新趋势热点、流量业务现状痛点探寻',
        '◆ 【交付】广告业务学习报告(05-03)',
        '◆ 【交付】WXG学习报告(05-10)',
        '◆ 【交付】设计/AI演进思考报告(05-24)',
    ],c=R,ato=(pcx-sc*0.19,pcy),ac=R)

blk(x=64,y=36,w=34,h=23.5,tit='┘ 延展：多元探索',
    sub='多条腿走路 · 探索新事物',
    items=[
        '【AI专项】月度探索产出：05-17 → 06-14 → 07-12 → 08-09 四节点',
        '【研发】理解微广研发业务，输出研发价值链&工作流程图',
        '【协助】协助BP落地日常工作 by case交付大评估等',
    ],c=P,ato=(pcx+sc*0.29,pcy-sc*0.02),ac=P)

# 时间轴
ax.plot([6,94],[19,19],'-',color='#DEE2E6',lw=2,zorder=3)
for lb,ds,c,mx in [("04-12","入职",B,8),("04-19","公司课",B,19),
    ("04-26","阶段1",R,30),("05-03","广告报告",O,41),("05-10","WXG",O,52),
    ("05-24","演进",G,63),("05~08","AI",P,74),("持续","在岗",G,85)]:
    ax.plot(mx,19,'o',ms=5.5,color=c,mec='white',mew=1.3,zorder=8)
    ax.text(mx,17.5,lb,ha='center',va='top',fontsize=7,fontweight='bold',
        color=c,fontproperties=font_prop,zorder=8)
    ax.text(mx,16,ds,ha='center',va='top',fontsize=5.5,
        color=Gy,fontproperties=font_prop,zorder=8)
ax.text(50,12.5,'─── 重要里程碑 ───',ha='center',fontsize=8,
    color=Gy,alpha=0.4,fontproperties=font_prop,zorder=5)
ax.text(50,9.5,'AMS HRBP实习生 nelsonmeng · 实习期 OKR',
    ha='center',fontsize=8.5,color='#AAA',fontproperties=font_prop,zorder=5)

plt.tight_layout(pad=0.4)
out='/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Pi_Talent_Target_v7.png'
fig.savefig(out,dpi=200,bbox_inches='tight',facecolor='#F5F6FA')
plt.close(fig)
print(f'✅ {out}')
