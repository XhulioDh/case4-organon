"""Case Four figure style v3: minimal, Helvetica (TeX Gyre Heros). Chosen by the author, 26 October 2026."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
THIN='#386fab'; ORG='#b25f38'; NEUTRAL='#8a8f94'
INK='#222222'; G='#7a7a7a'; RULE='#cfcfcf'; PAGE='#ffffff'
plt.rcParams.update({'font.family':'TeX Gyre Heros','font.size':9,'text.color':INK,'figure.facecolor':PAGE,'axes.facecolor':PAGE,'savefig.facecolor':PAGE,'svg.fonttype':'none'})
OUT=__import__('os').environ.get('FIG_OUT','./')
def bar(ax,y,w,h,c):
    if w>0: ax.add_patch(Rectangle((0,y-h/2),w,h,fc=c,ec='none',zorder=3))
def bare(ax,xmax,n,xmin=0):
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_xlim(xmin,xmax); ax.set_ylim(-0.7,n-0.3); ax.invert_yaxis()
    ax.add_line(plt.Line2D([0,0],[-0.5,n-0.5],color=RULE,lw=0.8))
    ax.set_xticks([]); ax.tick_params(axis='y',length=0,labelsize=9,colors=INK,pad=8)
def pctaxis(ax,n,ticks=(0,50,100)):
    """A quiet percentage scale: three ticks, no gridlines (for charts with intervals)."""
    ax.set_xticks(ticks); ax.set_xticklabels([f'{t}%' for t in ticks]); ax.tick_params(axis='x',length=3,width=0.6,colors=G,labelsize=8.5,pad=3)
    ax.spines['bottom'].set_visible(True); ax.spines['bottom'].set_color(RULE); ax.spines['bottom'].set_linewidth(0.8)
SUB='#555555'  # subtitles: darker than G, for print at A4 (27 October)
def title(fig,t,s,x=0.03,y=0.97,ts=13,ss=9.5,gap=0.1):
    fig.text(x,y,t,fontsize=ts,va='top',linespacing=1.1); fig.text(x,y-gap,s,fontsize=ss,color=SUB,va='top')
def whisker(ax,y,lo,hi):
    ax.plot([lo,hi],[y,y],color=INK,lw=0.8,zorder=4)
    for x in (lo,hi): ax.plot([x,x],[y-0.09,y+0.09],color=INK,lw=0.8,zorder=4)
def save(fig,name):
    for ext in ['png','svg']: fig.savefig(OUT+f'{name}.{ext}',dpi=300 if ext=='png' else None,bbox_inches='tight',pad_inches=0.15)
    plt.close(fig)
