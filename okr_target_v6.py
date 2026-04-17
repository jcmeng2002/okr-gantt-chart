# -*- coding: utf-8 -*-
"""
AMS HRBP 实习生 nelsonmeng OKR 目标框架图 V6 — π为中心版
核心思路：
1. 苍劲有力的大π占据画面正中心(视觉绝对主角)
2. 夯实根基并入横贯(都是打基础)
3. 内容以精简的「标注块」形式环绕π的三个笔画
4. 腾讯科技风 · 高设计感 · 不啰嗦
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, PathPatch, Polygon
from matplotlib.path import Path
import matplotlib.font_manager as fm
import numpy as np

FONT_PATH = "/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf"
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
plt.rcParams['font.family'] = font_prop.get_name()

fig, ax = plt.subplots(figsize=(20, 15), dpi=180)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('#FAFBFC')

# ═════ 配色 ═════
B = '#0052D9'   # 蓝 - 横贯
R = '#C9353A'   # 红 - 纵深
P = '#7B61FF'   # 紫 - 延展
G = '#008F5D'   # 绿 - 交付
O = '#E86828'   # 橙 - 交付点
K = '#1a1a2e'   # 深色文字
Gy = '#8C9099'  # 灰色文字

# ═════ 背景 ═════
ax.add_patch(Rectangle((0,0),100,100,fc='#FAFBFC',zorder=0))

# ━━━ 标题栏 ━━━
hdr = FancyBboxPatch((0,93.5),100,6.5,
    boxstyle="square,pad=0",fc=B,ec='none',zorder=10)
ax.add_patch(hdr)
ax.text(50,97,'目标：\u03c0 型 HRBP',
    ha='center',va='center',fontsize=22,fontweight='bold',
    color='white',fontproperties=font_prop,zorder=11)
ax.text(50,94.5,
    '横贯专业  \u00b7  纵深业务  \u00b7  延展探索   \u2014   值得业务信赖的好伙伴',
    ha='center',va='center',fontsize=10,color='white',alpha=0.7,
    fontproperties=font_prop,zorder=11)


# ================================================================
# ★★★ 大π绘制 ★★★ —— 苍劲有力的视觉中心
# ================================================================
pi_cx, pi_cy = 50, 51     # π中心坐标
scale = 40               # 缩放系数

# π 的三段路径定义 (归一化坐标 * scale + offset)
def make_pi_path(cx, cy, s):
    """返回π的三段路径数据"""
    # --- 横杠 ---
    h_x = [cx - s*0.52, cx + s*0.55]
    h_y = [cy + s*0.32] * 2
    
    # --- 左竖 ---
    v1_x = [cx - s*0.20] * 2
    v1_y = [cy - s*0.42, cy + s*0.32]
    
    # --- 右腿 ---
    # 上半段：竖直
    leg_v_x = [cx + s*0.16] * 2
    leg_v_y = [cy - s*0.02, cy + s*0.32]
    # 下半段：向右弯 (用多段折线近似弧形)
    leg_curve_n = 25
    leg_cx = np.linspace(cx + s*0.16, cx + s*0.48, leg_curve_n)
    leg_cy = np.ones(leg_curve_n) * (cy - s*0.02)
    
    return h_x, h_y, v1_x, v1_y, leg_v_x, leg_v_y, leg_cx, leg_cy

hx, hy, v1x, v1y, lvx, lvy, lcx, lcy = make_pi_path(pi_cx, pi_cy, scale)

# ---- 绘制多层实现苍劲效果 ----

# 第1层：最外层光晕
for seg_x, seg_y in [(hx,hy),(v1x,v1y),(lvx,lvy),(lcx,lcy)]:
    ax.plot(seg_x,seg_y,'-',color=B,alpha=0.04,lw=36,solid_capstyle='round',zorder=1)

# 第2层：外阴影
for seg_x, seg_y, c in [(hx,hy,B),(v1x,v1y,R),(lvx+lcv if 'lcv' in dir() else lvx,lvy,R)]:
    pass
for seg_x, seg_y in [(hx,hy),(v1x,v1y),(np.concatenate([lvx,lcx]),np.concatenate([lvy,lcy]))]:
    ax.plot(seg_x,seg_y,'-',color='#00000008',lw=26,solid_capstyle='round',zorder=2)

# 第3层：主色填充
# 横杠 - 蓝色
ax.plot(hx,hy,'-',color=B,lw=18,solid_capstyle='round',zorder=4)
# 左竖 - 红色
ax.plot(v1x,v1y,'-',color=R,lw=18,solid_capstyle='butt',zorder=4)
# 右腿上段 - 紫色
ax.plot(lvx,lvy,'-',color=P,lw=18,solid_capstyle='butt',zorder=4)
# 右腿下弯 - 紫色
ax.plot(lcx,lcy,'-',color=P,lw=18,solid_capstyle='round',zorder=4)

# 第4层：高光线 (白色/浅色内发光)
ax.plot(hx,hy,'-',color='#FFFFFF20',lw=6,solid_capstyle='round',zorder=5)
ax.plot(v1x,v1y,'-',color='#FFFFFF18',lw=6,solid_capstyle='butt',zorder=5)
ax.plot(lvx,lvy,'-',color='#FFFFFF18',lw=6,solid_capstyle='butt',zorder=5)
ax.plot(lcx,lcy,'-',color='#FFFFFF18',lw=6,solid_capstyle='round',zorder=5)

# 第5层：深色芯线
ax.plot(hx,hy,'-',color=B,lw=4,solid_capstyle='round',zorder=6)
ax.plot(v1x,v1y,'-',color=R,lw=4,solid_capstyle='butt',zorder=6)
ax.plot(lvx,lvy,'-',color=P,lw=4,solid_capstyle='butt',zorder=6)
ax.plot(lcx,lcy,'-',color=P,lw=4,solid_capstyle='round',zorder=6)


# ================================================================
# ★ 环绕π的标注块
# ================================================================

def label_block(x, y, w, h, title, desc, items, color,
                arrow_to=None, arrow_color=None, align='left'):
    """一个紧凑的标注块"""
    # 阴影
    ax.add_patch(FancyBboxPatch((x+0.25,y-0.25),w,h,
        boxstyle="round,pad=0.02,rounding_size=0.6",fc='#00000006',ec='none',zorder=12))
    # 白底圆角框
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle="round,pad=0.02,rounding_size=0.6",
        fc='white',ec=color,lw=1.8,zorder=13,alpha=0.97))
    # 顶部细色条
    ax.add_patch(FancyBboxPatch((x+0.2,y+h-0.38),w-0.4,0.38,
        boxstyle="round,pad=0.01,rounding_size=0.18",
        fc=color,ec='none',alpha=0.88,zorder=14))
    
    ha_a = 'left' if align=='left' else ('right' if align=='right' else 'center')
    tx = x + (1.2 if align=='left' else (w-1.2 if align=='right' else w/2))
    
    # 标题行
    ty = y + h - 2.0
    ax.text(tx, ty+0.5, title, ha=ha_a, va='center',
        fontsize=11, fontweight='bold', color=color, fontproperties=font_prop, zorder=15)
    if desc:
        ax.text(tx, ty-0.85, desc, ha=ha_a, va='center',
            fontsize=6.6, color=Gy, fontproperties=font_prop, zorder=15, style='italic')
    
    # 分割线
    dly = ty - 2.2 if desc else ty - 1.9
    ax.plot([x+1,x+w-1],[dly,dly],'-',color='#EEE',lw=0.7,zorder=14)
    
    # 内容
    sy = dly - 1.8
    step = min(max((sy-y-1)/max(len(items),1), 2.8), 3.4)
    for ii, it in enumerate(items):
        iy = sy - ii*step
        if iy < y+1: break
        al = 'left' if align!='right' else 'right'
        px = x+1.4 if al=='left' else x+w-1.4
        ax.plot(px+(0.5 if al=='left' else -0.5),iy,'o',ms=2.2,color=color,zorder=15)
        ax.text(px+(1.3 if al=='left' else -1.3),iy,it,ha=al,va='center',
            fontsize=6.4,color=K,fontproperties=font_prop,zorder=15,linespacing=1.2)
    
    # 连线到π
    if arrow_to and arrow_color:
        # 计算块边缘朝向π的方向
        if x + w/2 < pi_cx:
            ax_from = (x+w+0.3, y+h/2)
            ax_to = arrow_to
        elif x > pi_cx:
            ax_from = (x-0.3, y+h/2)
            ax_to = arrow_to
        else:
            ax_from = (x+w/2, y-0.3)
            ax_to = arrow_to
        
        ax.annotate('', xy=ax_to, xytext=ax_from,
            arrowprops=dict(arrowstyle='->',color=arrow_color,lw=1.2,
                            connectionstyle='arc3,rad=0.12',
                            shrinkA=3,shrinkB=8),
            zorder=11)


# ━━━━ Block A: 横贯(上方) — 合并了夯实根基 ━━━━
label_block(
    x=14, y=72, w=72, h=17.5,
    title='\u2501  横贯：专业基石',
    desc='规章制度体系化学习 \u00b7 新人培训文化融入 \u00b7 打牢地基挑起\u201c大梁\u201d',
    color=B,
    items=[
        '\u3010HR政策\u3011OD / \u62db\u8058 / \u901a\u9053 / \u7ee9\u6548 / \u57f9\u517b / \u6587\u5316\u6fc0\u52b1 \u2014 AMS\u7279\u6709\u653f\u7b56\u91cd\u70b9\u638c\u63e1',
        '\u3010CDG\u5408\u4f5c\u3011\u8fd0\u8425\u673a\u5236 / \u6c9f\u901a\u65b9\u5f0f / \u9ad8\u6548\u627f\u63a5\u90e8\u95e8HR\u7ba1\u7406\u5de5\u4f5c\u53ca\u9700\u6c42',
        '\u3010\u7ec4\u7ec7\u67b6\u6784\u3011\u6f5c\u9f99 / \u5e72\u90e8\u664b\u5347 / 360\u8bc4\u4f30 / \u7ee9\u6548\u901a\u9053\u5168\u6d41\u7a0b',
        '\u3010\u57fa\u7840\u5939\u5b9e\u3011AMS\u65b0\u4eba\u57f9\u8bad(\u81f405-03) \u00b7 \u516c\u53f8\u8bfe\u7a0b(\u81f404-19) \u00b7 \u57f9\u517b\u4f53\u7cfb / \u62db\u8058\u7f16\u5236',
    ],
    arrow_to=(50, pi_cy+scale*0.32),
    arrow_color=B,
)


# ━━━━ Block B: 纵深(左下) ━━━━
label_block(
    x=2, y=24, w=30, h=37.5,
    title='\u2502  \u7eb5\u6df1\uff1a\u4e1a\u52a1\u7a7f\u900f',
    desc='T\u578b\u4eba\u624d\u7684\u201c\u4e00\u7ad6\u201d \u2014 \u6df1\u5165\u5e7f\u544a\u4e1a\u52a1 & \u56e2\u961f',
    color=R,
    items=[
        '\u3010\u56e2\u961f\u3011\u719f\u6089AMS\u5404\u804c\u80fd/\u90e8\u95e8\u5206\u5de5\u3001\u5fae\u5e7f\u5404\u4e2d\u5fc3\u5de5\u4f5c',
        '\u3010\u56e2\u961f\u3011\u62dc\u8bbf\u5fae\u5e7f\u6838\u5fc3\u7ba1\u7406\u56e2\u961f / Core team\u53ca\u68af\u961f',
        '\u3010\u56e2\u961f\u3011\u6316\u639e\u7ec4\u7ec7\u4eba\u624d\u75db\u70b9\uff0c\u8f93\u51fa\u6d1e\u5bf1\u548c\u53d1\u73b0',
        '\u3010\u56e2\u961f\u3011\u548c\u5fae\u5e7f\u56e2\u961f\u5efa\u7acb\u53cb\u597d\u8fde\u63a5\u4e0e\u4eb2\u5bc6\u4e92\u52a8',
        '\u3010\u4e1a\u52a1\u3011\u7406\u89e3AMS\u4e1a\u52a1\u903b\u8f91/\u89c4\u5212/\u6d41\u91cf\u5e73\u53f0\u7279\u5f81',
        '\u3010\u4e1a\u52a1\u3011\u5173\u6ce8\u884c\u4e1a\u65b0\u8d8b\u52bf\u70ed\u70b9\u3001\u6d41\u91cf\u73b0\u72b6\u75db\u70b9',
        '\u25c6 \u3010\u4ea4\u4ed8\u3011\u5e7f\u544a\u4e1a\u52a1\u5b66\u4e60\u62a5\u544a(05-03)',
        '\u25c6 \u3010\u4ea4\u4ed8\u3011WXG\u5b66\u4e60\u62a5\u544a(05-10) | \u6f14\u8fdb\u62a5\u544a(05-24)',
    ],
    arrow_to=(pi_cx-scale*0.20, pi_cy),
    arrow_color=R,
)


# ━━━━ Block C: 延展(右下) ━━━━
label_block(
    x=66, y=33, w=32, h=21,
    title="\u2518  \u5ef6\u5c55\uff1a\u591a\u5143\u63a2\u7d22",
    desc='\u591a\u6761\u817f\u8d70\u8def \u00b7 \u63a2\u7d22\u65b0\u4e8b\u7269 \u2014 \u5dee\u5f02\u5316\u7ade\u4e89\u529b',
    color=P,
    items=[
        '\u3010AI\u4e13\u9879\u3011\u6708\u5ea6\u63a2\u7d22\u4ea7\u51fa\uff1a05-17 \u2192 06-14 \u2192 07-12 \u2192 08-09',
        '\u3010\u7814\u53d1\u3011\u7406\u89e3\u5fae\u5e7f\u7814\u53d1\u4e1a\u52a1\uff0c\u8f93\u51fa\u7814\u53d1\u4ef7\u503c\u94fe&\u5de5\u4f5c\u6d41\u7a0b\u56fe',
        '\u3010\u534f\u52a9\u3011\u534f\u52a9BP\u843d\u5730\u65e5\u5e38\u5de5\u4f5c by case\u4ea4\u4ed8\u5927\u8bc4\u4f30\u7b49',
    ],
    arrow_to=(pi_cx+scale*0.32, pi_cy-scale*0.02),
    arrow_color=P,
    align='left',
)


# ══════════ 底部时间轴 ══════════
ax.plot([8,92],[19.5,19.5],'--',color='#DDD',lw=1.5,zorder=3)

ms_data=[
    ("04-12","\u5165\u804c",B,10),
    ("04-19","\u516c\u53f8\u8bfe",B,22),
    ("04-26","\u9636\u6bb51\u5b8c\u6210",R,33),
    ("05-03","\u5e7f\u544a\u62a5\u544a",O,44),
    ("05-10","WXG\u62a5\u544a",O,55),
    ("05-24","\u6f14\u8fdb\u62a5\u544a",G,66),
    ("05~08\u6708","AI\u6301\u7eed",P,77),
    ("\u6301\u7eed","\u5728\u5c97\u5b9e\u8df5",G,88),
]
for lb,ds,col,mx in ms_data:
    ax.plot(mx,19.5,'o',ms=5.5,color=col,mec='white',mew=1.3,zorder=8)
    ax.text(mx,18,lb,ha='center',va='top',fontsize=6,
        fontweight='bold',color=col,fontproperties=font_prop,zorder=8)
    ax.text(mx,16.5,ds,ha='center',va='top',fontsize=5.2,
        color=Gy,fontproperties=font_prop,zorder=8)

ax.text(50,13,'\u2500\u2500\u2500  \u5173\u952e\u91cc\u7a0b\u7891\u65f6\u95f4\u8f74  \u2500\u2500\u2500',
    ha='center',va='center',fontsize=7.5,color=Gy,alpha=0.4,
    fontproperties=font_prop,zorder=5)
ax.text(50,10,'AMS HRBP\u5b9e\u4e60\u751f nelsonmeng  \u00b7  \u5b9e\u4e60\u671f OKR \u89c4\u5212',
    ha='center',va='center',fontsize=8,color='#BBBBBB',
    fontproperties=font_prop,zorder=5)

plt.tight_layout(pad=0.5)
out="/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Pi_Talent_Target_v6.png"
fig.savefig(out,dpi=200,bbox_inches='tight',facecolor='#FAFBFC')
plt.close(fig)
print(f"\u2705 {out}")
