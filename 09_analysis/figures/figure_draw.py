"""Draw the Case Four figures in style v3 (minimal, Helvetica) from the data files."""
import sys,csv; sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from figure_style import *
import matplotlib.colors as mc
D=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/'
rd=lambda f:list(csv.DictReader(open(D+f)))
V=['serves','mixed','does not serve']
tot={(r['instrument'],r['verdict']):int(r['answers']) for r in rd('fig_s4_verdict_totals.csv')}
def col(ax,x,y,s,**k):
    k.setdefault('fontsize',8.5); ax.text(x,y,s,transform=ax.get_yaxis_transform(),va='center',**k)

def verdict_bars(ax,h=0.22,g=0.14,vs=9):
    for i,v in enumerate(V):
        for inst,c,off in [('thin',THIN,-g),('Organon',ORG,g)]:
            val=tot[(inst,v)]; bar(ax,i+off,val,h,c); ax.text(val+2.5,i+off,str(val),va='center',fontsize=vs)
    ax.set_yticks(range(3)); ax.set_yticklabels(V)
    ax.text(129+2.5,-0.47,'thin (brief instruction)',fontsize=vs-1,color=THIN,ha='right')
    ax.text(46+2.5,0.43,'thick (Organon)',fontsize=vs-1,color=ORG)

# 1. Section 4 (report)
fig=plt.figure(figsize=(7,3.2)); ax=fig.add_axes([0.17,0.08,0.55,0.62]); bare(ax,150,3); verdict_bars(ax)
title(fig,'Same answers, same judge, two instructions','The same 150 answers, one evaluator, verdicts under each instruction',gap=0.11)
fig.text(0.76,0.52,'84 of 150 pairs differed,\nevery one toward a more\nadverse thick (Organon)\nassessment.',fontsize=9,va='top',linespacing=1.4)
save(fig,'fig_s4_verdict_comparison')

# 2. Section 5 (registered figure 1)
rows=rd('fig_s5_divergence_by_question.csv')
fig=plt.figure(figsize=(6.7,3.3)); ax=fig.add_axes([0.21,0.13,0.38,0.58]); bare(ax,100,5); pctaxis(ax,5)
X=lambda d:1+d/(0.38*6.7)  # column position, d inches right of the axis
for i,r in enumerate(rows):
    p=float(r['divergence_pct']); bar(ax,i,p,0.36,NEUTRAL); whisker(ax,i,float(r['wilson95_low_pct']),float(r['wilson95_high_pct']))
    col(ax,X(0.15),i,f"{r['divergent_pairs']} of 30",fontsize=9); col(ax,X(0.85),i,f"{p:.1f}%",color=SUB,fontsize=9); col(ax,X(1.45),i,f"{float(r['wilson95_low_pct']):.1f} to {float(r['wilson95_high_pct']):.1f}",color=SUB,fontsize=9)
col(ax,X(0.15),-0.95,'divergent',color=SUB,fontsize=8.5); col(ax,X(1.45),-0.95,'Wilson 95%',color=SUB,fontsize=8.5)
ax.set_yticks(range(5)); ax.set_yticklabels([r['question']+(' (control)' if r['question']=='teacher' else '') for r in rows],fontsize=9.5)
title(fig,'Divergence by question','Pairs with different verdicts, of 30 per question; lines: Wilson 95% intervals',gap=0.1)
save(fig,'fig_s5_divergence_by_question')

# 3. Section 6 (report)
RROWS=rd('fig_s6_reading_classifications.csv')
defs={'named':"thin's reasoning reaches what thick\n(Organon) treated as decisive",'gestured':'partial contact that does not\nmeet the standard','absent':"nothing in thin's reasoning reaches\nwhat thick (Organon) treated as decisive"}
def reading(fig,ax,vs=9.5,ds=8,ls=10):
    bare(ax,84,3)
    for i,r in enumerate(RROWS):
        k=int(r['divergent_pairs']); bar(ax,i,k,0.36,NEUTRAL); ax.text(k+1.2,i,f"{k}  ({float(r['pct_of_84']):.1f}%)",va='center',fontsize=vs)
        ax.text(-0.04,i-0.05,r['classification'],ha='right',va='bottom',fontsize=ls,transform=ax.get_yaxis_transform())
        ax.text(-0.04,i+0.02,defs[r['classification']],ha='right',va='top',fontsize=ds,color=SUB,transform=ax.get_yaxis_transform(),linespacing=1.25)
    ax.set_yticks([])
fig=plt.figure(figsize=(6.7,3.4)); ax=fig.add_axes([0.38,0.06,0.48,0.7]); reading(fig,ax)
title(fig,"What thin's reasoning addressed","The 84 divergent pairs; the author's classifications",gap=0.1)
save(fig,'fig_s6_reading_classifications')

# 4. Section 7 (unregistered, descriptive)
rows=rd('fig_s7_gender_assigned.csv')
fig=plt.figure(figsize=(7,1.9)); ax=fig.add_axes([0.2,0.05,0.62,0.52]); bare(ax,120,2)
for i,r in enumerate(rows):
    k=int(r['gender_assigned']); c=THIN if r['instrument']=='thin' else ORG; bar(ax,i,k,0.36,c)
    ax.text(k+1.5,i,f"{k} of 120  ({float(r['pct']):.1f}%)",va='center',fontsize=9)
ax.set_yticks(range(2)); ax.set_yticklabels(['thin (brief instruction)','thick (Organon)'])
title(fig,'Gender assigned to an asker who gave none','The four questions that give no gender; 120 evaluations per instruction',gap=0.17)
save(fig,'fig_s7_gender_assigned')

# 5. Section 8 (registered figure 2)
rows=sorted(rd('fig_s8_lens_rates_predicted_observed.csv'),key=lambda r:-float(r['fail_rate_pct']))
pred={'Glaciation':'passes broadly','Misfire':'none','Typecasting':'fires rarely','False Confidence':'fires highest','Mere Means':'none','Usurping':'fires on everything'}
mark={'held':'held','did not hold':'did not hold','no rate prediction':'no rate prediction'}
fig=plt.figure(figsize=(6.7,3.6)); ax=fig.add_axes([0.2,0.11,0.24,0.6]); bare(ax,100,6); pctaxis(ax,6)
X=lambda d:1+d/(0.24*6.7)
for i,r in enumerate(rows):
    p=float(r['fail_rate_pct']); bar(ax,i,p,0.36,ORG); whisker(ax,i,float(r['wilson95_low_pct']),float(r['wilson95_high_pct']))
    col(ax,X(0.12),i,f"{r['fails']}/{r['assessable']}",fontsize=9); col(ax,X(0.72),i,f"{p:.1f}%",color=SUB,fontsize=9)
    col(ax,X(1.27),i,pred[r['lens']],fontsize=9); o=r['outcome_section8']; col(ax,X(2.77),i,mark[o],color=INK if o!='no rate prediction' else SUB,fontsize=9)
    if o=='no rate prediction': ax.plot([X(2.59),X(2.67)],[i,i],color=SUB,lw=0.9,transform=ax.get_yaxis_transform(),clip_on=False)
    else: ax.scatter([X(2.63)],[i],s=30,marker='o',facecolor=INK if o=='held' else 'white',edgecolor=INK,linewidth=0.9,transform=ax.get_yaxis_transform(),clip_on=False,zorder=5)
for x,t in [(0.12,'fails'),(1.27,'registered prediction'),(2.57,'outcome')]: col(ax,X(x),-1.0,t,color=SUB,fontsize=8.5)
ax.set_yticks(range(6)); ax.set_yticklabels([r['lens'] for r in rows],fontsize=9.5)
title(fig,'Registered predictions and observed lens results','Lens failure rates, 150 thick (Organon) evaluations; lines: Wilson 95% intervals',gap=0.1)
save(fig,'fig_s8_lens_rates_predictions')

# 6. Appendix E (registered figure 3)
rows=rd('fig_app_cofiring_counts.csv'); L=[r['lens'] for r in rows]; M=[[int(r[c]) for c in L] for r in rows]
off=[M[i][j] for i in range(6) for j in range(6) if i!=j]; lo,hi=min(off),max(off)
cmap=mc.LinearSegmentedColormap.from_list('rust',['#f6efea','#d9a88f',ORG,'#7a3a1d'])
fig=plt.figure(figsize=(6.2,5.4)); ax=fig.add_axes([0.24,0.15,0.62,0.66])
for i in range(6):
    for j in range(6):
        v=M[i][j]
        if i==j:
            ax.add_patch(Rectangle((j+0.04,i+0.04),0.92,0.92,fc=PAGE,ec=RULE,lw=0.6)); ax.text(j+0.5,i+0.44,str(v),ha='center',va='center',fontsize=9)
            ax.text(j+0.5,i+0.7,'lens total',ha='center',va='center',fontsize=7,color=SUB)
        else:
            c=cmap((v-lo)/(hi-lo)); ax.add_patch(Rectangle((j+0.04,i+0.04),0.92,0.92,fc=c,ec='none'))
            lum=0.2126*c[0]+0.7152*c[1]+0.0722*c[2]; ax.text(j+0.5,i+0.5,str(v),ha='center',va='center',fontsize=9,color='white' if lum<0.45 else INK)
ax.set_xlim(0,6); ax.set_ylim(6,0); ax.set_xticks([k+0.5 for k in range(6)]); ax.set_yticks([k+0.5 for k in range(6)])
ax.set_xticklabels(L,rotation=35,ha='right',fontsize=8.5); ax.set_yticklabels(L,fontsize=8.5)
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(length=0,colors=INK)
title(fig,'Lenses failing together','Thick (Organon) evaluations, of 150, failing both lenses; diagonal: lens totals',x=0.03,y=0.97,gap=0.065)
save(fig,'fig_appE_lenses_failing_together')

# LinkedIn images: editorial style (chosen by the author, 26 October)
from matplotlib.lines import Line2D
BG='#f7f4ef'; SERIF='TeX Gyre Pagella'
def li_frame(headline,sub,hl_lines):
    fig=plt.figure(figsize=(4.5,5.625),facecolor=BG)
    fig.add_artist(Line2D([0.07,0.93],[0.965,0.965],color=INK,lw=2.2))
    for k,line in enumerate(headline.split('\n')):
        fig.text(0.07,0.935-k*0.052,line,fontsize=17,family=SERIF,fontweight='bold',va='top')
    fig.text(0.07,0.94-0.052*hl_lines-0.03,sub,fontsize=8.5,color=G,va='top',linespacing=1.35)
    return fig
def li_save(fig,name): fig.savefig(OUT+name,dpi=240,facecolor=BG); plt.close(fig)

# LinkedIn 1: verdicts
fig=li_frame('The same 150 answers.\nThe same AI judge.\nTwo different evaluation\ninstructions.','Verdicts given by Claude Opus 5.0 under each instruction',4)
ax=fig.add_axes([0.3,0.27,0.62,0.33]); ax.set_facecolor(BG); bare(ax,150,3); verdict_bars(ax,vs=9.5)
fig.text(0.07,0.17,'84 of 150 pairs differed, every one toward a more\nadverse thick (Organon) assessment.',fontsize=9.5,linespacing=1.4)
fig.add_artist(Line2D([0.07,0.93],[0.12,0.12],color='#cfc9bf',lw=0.6))
fig.text(0.07,0.035,"Thin asks how good the response is ethically; thick (Organon) asks whether\nit served the person's moral agency. The study does not establish which\nassessment is more justified.",fontsize=7.4,color=G,linespacing=1.45)
li_save(fig,'linkedin_1_verdicts.png')

# LinkedIn 2: reading classifications
fig=li_frame('What thin saw','The 84 answers on which the two instructions disagreed, by whether\nthin reaches what thick (Organon) treated as decisive',1)
defs2={'named':"thin's reasoning reaches what thick (Organon) treated as decisive",'gestured':'partial contact that does not meet the standard','absent':"nothing in thin's reasoning reaches what thick (Organon) treated as decisive"}
W=0.86; y0=0.72
for k,r in enumerate(RROWS):
    y=y0-k*0.15; n=int(r['divergent_pairs'])
    fig.text(0.07,y,r['classification'],fontsize=10.5,va='bottom')
    fig.text(0.93,y,f"{n} of 84",fontsize=10.5,va='bottom',ha='right')
    fig.add_artist(Rectangle((0.07,y-0.03),W,0.02,transform=fig.transFigure,fc='#e8e3da',ec='none'))
    fig.add_artist(Rectangle((0.07,y-0.03),W*n/84,0.02,transform=fig.transFigure,fc=NEUTRAL,ec='none'))
    fig.text(0.07,y-0.058,defs2[r['classification']],fontsize=7.6,color=G,va='bottom')
fig.text(0.07,0.195,"On 54 of the 84, thin's reasoning was classified as reaching\nwhat thick (Organon) treated as decisive, and on 53 of\nthose thin still passed the response.",fontsize=9.5,linespacing=1.4)
fig.add_artist(Line2D([0.07,0.93],[0.15,0.15],color='#cfc9bf',lw=0.6))
fig.text(0.07,0.035,"The author's classifications of the written evaluations, not made blind.\nNamed does not mean every component was explicitly recognised.\nVarying the readings affected by rules refined during the audit gives\n47 to 61 named.",fontsize=7.4,color=G,linespacing=1.45)
li_save(fig,'linkedin_2_reading.png')
print('done')
