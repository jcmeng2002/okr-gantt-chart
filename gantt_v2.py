import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# ============================================================
# 腾讯品牌风格甘特图 V2 - 基于OKR文档第二个表格（更新版）
# 字体：TencentSans-W7.otf（本地已安装）
# ============================================================

FONT_PATH = '/Users/mengjiachen/Library/Fonts/TencentSans-W7.otf'
font_prop = fm.FontProperties(fname=FONT_PATH)
fm.fontManager.addfont(FONT_PATH)

plt.rcParams['axes.unicode_minus'] = False

# 腾讯品牌色系
TENCENT_BLUE = '#0052D9'
TENCENT_BLUE_LIGHT = '#E6F0FF'
TENCENT_BLUE_DARK = '#003380'
ORANGE = '#ED7B2F'
ORANGE_LIGHT = '#FFF0E8'
GREEN = '#00A870'
GREEN_LIGHT = '#E8F8F0'
PURPLE = '#7B61FF'
GRAY_TEXT = '#666666'
WHITE = '#FFFFFF'

# 时间基准：假设入职日为4月14日左右
START_DATE = datetime(2025, 4, 14)

def day_offset(days):
    return START_DATE + timedelta(days=days)

# ============================================================
# 任务数据 - 基于表格中的具体时间节奏
# ============================================================
tasks = [
    # 阶段1：HR管理机制了解（~2周）
    {'name': '公司课程学习', 'detail': 'HRBP能力要求与职责范围',
     'start': 0, 'end': 5,
     'color': TENCENT_BLUE, 'phase': 1},
    {'name': 'AMS/流量侧招聘及编制管理', 'detail': 'BP合作方式/规则',
     'start': 3, 'end': 12,
     'color': TENCENT_BLUE, 'phase': 1},
    {'name': '组织架构与干部晋升', 'detail': '潜龙/360评估/发文规范',
     'start': 5, 'end': 12,
     'color': TENCENT_BLUE, 'phase': 1},
    {'name': '绩效及通道管理', 'detail': '目标制定/考核/面谈/系统配置',
     'start': 7, 'end': 12,
     'color': TENCENT_BLUE, 'phase': 1},
    {'name': '培养体系 & 文化荣誉激励', 'detail': '',
     'start': 9, 'end': 12,
     'color': TENCENT_BLUE, 'phase': 1},

    # 阶段2：业务了解（~2周）
    {'name': '计算广告课程&教材学习', 'detail': '',
     'start': 7, 'end': 12,
     'color': ORANGE, 'phase': 2},
    {'name': '参加AMS新人培训', 'detail': '',
     'start': 12, 'end': 20,
     'color': ORANGE, 'phase': 2},
    {'name': '深入了解部门业务信息', 'detail': '业务目标/核心干部/WXG/TAD',
     'start': 14, 'end': 26,
     'color': ORANGE, 'phase': 2},

    # 阶段3：在岗实践（2-3个月）
    {'name': '协助BP落地日常工作', 'detail': '大评估bycase交付',
     'start': 26, 'end': 105,
     'color': GREEN, 'phase': 3},
    {'name': 'AI产品经理演进思考', 'detail': '关注微信广告部AI变革',
     'start': 18, 'end': 33,
     'color': GREEN, 'phase': 3},
    {'name': '设计职能演进思考', 'detail': '关注设计中心AI变革',
     'start': 22, 'end': 33,
     'color': GREEN, 'phase': 3},
    {'name': 'HR AI流程再造探索', 'detail': 'S3 AI应用 / AMS HR场景落地',
     'start': 30, 'end': 105,
     'color': GREEN, 'phase': 3},
]

milestones = [
    {'name': '广告业务学习报告', 'day': 12, 'desc': '4月26日前'},
    {'name': 'AI产品经理演进思考报告', 'day': 33, 'desc': '5月17日前'},
    {'name': '设计职能演进思考报告', 'day': 33, 'desc': '5月17日前'},
    {'name': '大评估日常工作交付', 'day': 50, 'desc': 'By Case'},
    {'name': 'AI专项产出交付', 'day': 75, 'desc': 'By Month'},
]

# ============================================================
# 绘图
# ============================================================

fig, ax = plt.subplots(figsize=(28, 18), dpi=100)
fig.patch.set_facecolor(WHITE)
ax.set_facecolor(WHITE)

n_tasks = len(tasks)
bar_height = 0.6

# X轴范围（用date2num）
x_start = mdates.date2num(day_offset(-3))
x_end = mdates.date2num(day_offset(110))

# ---- 标题 ----
ax.set_title('AMS HRBP OKR 规划甘特图\n基于阶段化学习目标 · 具体工作与交付节奏',
             fontsize=26, fontweight='bold', color=TENCENT_BLUE_DARK,
             pad=22, fontproperties=font_prop)

# ---- 阶段背景色带 ----
phase_bg = [
    (day_offset(0), day_offset(13), TENCENT_BLUE_LIGHT),
    (day_offset(12), day_offset(27), ORANGE_LIGHT),
    (day_offset(26), day_offset(108), GREEN_LIGHT),
]
for ps, pe, pcolor in phase_bg:
    ax.axvspan(mdates.date2num(ps), mdates.date2num(pe),
               alpha=0.35, facecolor=pcolor, zorder=0)

# ---- 绘制任务条 ----
for i, task in enumerate(tasks):
    y = n_tasks - 1 - i
    s = mdates.date2num(day_offset(task['start']))
    e = mdates.date2num(day_offset(task['end']))
    dur = e - s

    bar = FancyBboxPatch(
        (s, y - bar_height / 2), dur, bar_height,
        boxstyle="round,pad=0.03,rounding_size=0.25",
        facecolor=task['color'], edgecolor='white',
        linewidth=1.5, alpha=0.92, zorder=3)
    ax.add_patch(bar)

    # 条形内天数
    ax.text((s + e) / 2, y, f'{int(dur)}天',
            ha='center', va='center', fontsize=9,
            fontweight='bold', color='white', fontproperties=font_prop)

    # 左侧任务名
    label = task['name']
    if task['detail']:
        label += f"\n({task['detail']})"
    ax.text(x_start + 1, y, label,
            ha='left', va='center', fontsize=12,
            fontproperties=font_prop, color='#333333')

# ---- 绘制里程碑 ----
ms_y_base = n_tasks + 0.8
for j, ms in enumerate(milestones):
    my = ms_y_base - j * 0.9
    mx = mdates.date2num(day_offset(ms['day']))

    # 菱形标记
    ds = 0.28
    diamond = plt.Polygon([
        [mx, my], [mx + ds * 0.55, my + ds],
        [mx, my + ds * 2], [mx - ds * 0.55, my + ds]],
        closed=True, facecolor=PURPLE, edgecolor='white',
        linewidth=1.5, zorder=5, alpha=0.95)
    ax.add_patch(diamond)

    # 连线
    ax.plot([x_start + 1, mx], [my + ds, my + ds],
            color=PURPLE, linewidth=1.2, linestyle='--', alpha=0.45)

    # 名称
    ax.text(x_start + 1, my + ds, f"★ {ms['name']}  ({ms['desc']})",
            ha='left', va='center', fontsize=11.5, fontproperties=font_prop,
            color=PURPLE, fontweight='bold')

# ---- 关键日期垂直虚线 ----
key_dates = [
    (12, '4月26日\n阶段1结束', TENCENT_BLUE),
    (26, '5月10日\n阶段2结束', ORANGE),
    (33, '5月17日\nO2报告交付', PURPLE),
]
for kd_day, klabel, kclr in key_dates:
    kx = mdates.date2num(day_offset(kd_day))
    ax.axvline(x=kx, color=kclr, linestyle='--', linewidth=1.5, alpha=0.6, zorder=2)
    ax.text(kx, n_tasks - 0.15, klabel, ha='center', va='bottom',
            fontsize=8, fontproperties=font_prop, color=kclr,
            bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=kclr, alpha=0.9))

# ---- 周数标注 ----
for w in range(0, 108, 7):
    wx = mdates.date2num(day_offset(w))
    if wx < x_end:
        week_n = day_offset(w).isocalendar()[1]
        ax.axvline(x=wx, color='#E8E8E8', linestyle='-', linewidth=0.4, zorder=0)
        ax.text(wx, n_tasks + 0.35, f"W{week_n}",
                ha='center', va='bottom', fontsize=7,
                color=GRAY_TEXT, fontproperties=font_prop, rotation=45)

# ---- 坐标轴设置 ----
ax.set_xlim(x_start, x_end)
ax.set_ylim(-len(milestones) * 0.9 - 0.3, n_tasks + 1.2)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y年%m月'))
ax.tick_params(axis='x', labelsize=11, colors=TENCENT_BLUE_DARK)
for lbl in ax.get_xticklabels():
    lbl.set_fontproperties(font_prop)

ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#D0D0E0')
ax.grid(axis='x', linestyle='-', alpha=0.25, color='#E0E0E0', zorder=0)

# ---- 图例 ----
ly = -len(milestones) * 0.9 - 0.05
legend_items = [
    (TENCENT_BLUE, '阶段1：HR管理机制了解（~2周）'),
    (ORANGE, '阶段2：业务了解（~2周）'),
    (GREEN, '阶段3：在岗实践与独立产出（~3月）'),
    (PURPLE, '关键交付里程碑'),
]
for idx, (clr, lbl) in enumerate(legend_items):
    lx = 0.02 + idx * 0.24
    rect = plt.Rectangle((lx, ly - 0.04), 0.02, 0.16,
                          transform=ax.transAxes, facecolor=clr,
                          edgecolor='none', alpha=0.85)
    ax.add_patch(rect)
    ax.text(lx + 0.025, ly, lbl, transform=ax.transAxes, fontsize=9,
            fontproperties=font_prop, color='#444444')

# ---- 底部说明 ----
fig.text(0.5, 0.01,
         '总周期：约 16 周 | 数据来源：OKR O1 文档第二张表格 | 字体：Tencent Sans W7',
         ha='center', fontsize=9.5, fontproperties=font_prop, color=GRAY_TEXT)

plt.subplots_adjust(left=0.06, right=0.98, top=0.92, bottom=0.05)
out_path = '/Users/mengjiachen/WorkBuddy/20260414135125/OKR_Gantt_Chart_v2.png'
plt.savefig(out_path, dpi=160, bbox_inches='tight', facecolor=WHITE, edgecolor='none')
print(f"✅ 已保存: {out_path}")
