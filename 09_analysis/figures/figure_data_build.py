"""Rebuild the Case Four figure data files (six figures) from the published records.
Usage: python3 figure_data_build.py <release_folder> <output_folder>"""
import csv,math,collections,sys,os,re
R=sys.argv[1].rstrip('/')+'/'; OUT=sys.argv[2]; os.makedirs(OUT,exist_ok=True)
ex={int(r['run_no']):r for r in csv.DictReader(open(R+'05_extraction/extraction_sheet.csv'))}
po={int(r['run_no']):r for r in csv.DictReader(open(R+'05_extraction/run_order_and_pairing.csv'))}
def wilson(k,n,z=1.959963984540054):
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return round(100*(c-h),1),round(100*(c+h),1)
pairs=collections.defaultdict(dict)
for n,r in po.items(): pairs[(r['question'],r['answer_source'],r['answer_run'])][r['instrument']]=n
P=[dict(q=k[0],thin=v['thin'],thick=v['thick'],tc=ex[v['thin']]['code'].strip().lower(),kc=ex[v['thick']]['code'].strip().lower()) for k,v in pairs.items()]
assert len(P)==150
codes=['serves','mixed','does not serve']; rank={c:i for i,c in enumerate(codes)}
def write(name,head,rows):
    with open(os.path.join(OUT,name),'w',newline='') as f: c=csv.writer(f); c.writerow(head); c.writerows(rows)
# section 4
rows=[]
for t in codes:
    for k in codes:
        n=sum(1 for p in P if p['tc']==t and p['kc']==k)
        rows.append([t,k,n,'agree' if t==k else ('divergent, Organon more adverse' if rank[k]>rank[t] else 'divergent, thin more adverse')])
write('fig_s4_verdict_comparison.csv',['thin_verdict','organon_verdict','answers','relation'],rows)
# section 5
rows=[]
for q in ['professor','pregnancy','teacher','diary','medicine']:
    S=[p for p in P if p['q']==q]; d=sum(p['tc']!=p['kc'] for p in S); lo,hi=wilson(d,len(S))
    rows.append([q,d,len(S),f'{100*d/len(S):.1f}',lo,hi,sum(p['tc']=='serves' for p in S),sum(p['kc']=='serves' for p in S)])
write('fig_s5_divergence_by_question.csv',['question','divergent_pairs','answers','divergence_pct','wilson95_low_pct','wilson95_high_pct','thin_passes','organon_passes'],rows)
# section 6 (counts from the reading sample; definitions verbatim from section 6.2 of the report)
rs=list(csv.DictReader(open(R+'06_reading_sample/reading_sample.csv').readlines()[1:]))
cnt=collections.Counter(r['same_passage'].strip() for r in rs if r['set']=='divergent')
sec6=open(R+'report/06_what_thin_saw.md').read()
defs={k:re.search(r'- \*\*'+k.capitalize()+r'\.\*\* (.+)',sec6).group(1).strip() for k in ['named','gestured','absent']}
tot=sum(cnt.values())
write('fig_s6_reading_classifications.csv',['classification','divergent_pairs','pct_of_84','definition_section6_2_verbatim'],[[k,cnt[k],f'{100*cnt[k]/tot:.1f}',defs[k]] for k in ['named','gestured','absent']])
# section 8 and appendix
L=[('Glaciation','L1_glaciation_normalised'),('Misfire','L2_misfire_normalised'),('Typecasting','L3_typecasting_normalised'),('False Confidence','L4_false_confidence_normalised'),('Mere Means','L5_mere_means_normalised'),('Usurping','L6_usurping_normalised')]
thick=[n for n,r in po.items() if r['instrument']=='thick']
st=lambda n,c:{'FAILS':1,'MEETS':0}.get(ex[n][c].strip().upper())
pred={'Glaciation':('Glaciation passes broadly.','held','Passes on 121 of 150 (80.7%).'),'Misfire':('','no rate prediction',''),
'Typecasting':('Typecasting fires rarely and returns not-assessable often.','did not hold','Fails on 79 of 150 (52.7%), third of six; not assessable on none.'),
'False Confidence':('False Confidence fires highest.','held','109 of 150 (72.7%), 8.0 points above the next lens.'),
'Mere Means':('','no rate prediction','The registered Mere Means prediction concerns the kind of failure, not its rate (section 8.1: did not hold).'),
'Usurping':('Usurping fires on everything, "since every question is a person stuck on a decision".','did not hold','Fails on 97 of 150 (64.7%).')}
rows=[]
for i,(nm,c) in enumerate(L,1):
    s=[st(n,c) for n in thick]; f=s.count(1); m=s.count(0); lo,hi=wilson(f,f+m)
    rows.append([i,nm,f,f+m,s.count(None),f'{100*f/(f+m):.1f}',lo,hi]+list(pred[nm]))
write('fig_s8_lens_rates_predicted_observed.csv',['order_in_framework','lens','fails','assessable','not_assessable','fail_rate_pct','wilson95_low_pct','wilson95_high_pct','registered_prediction_section8_wording','outcome_section8','observed_section8_wording'],rows)
co=[];ph=[]
for a,ca in L:
    rc=[a];rp=[a]
    for b,cb in L:
        xs=[(st(n,ca),st(n,cb)) for n in thick]; xs=[x for x in xs if None not in x]
        n11=sum(1 for x,y in xs if x and y); rc.append(n11 if a!=b else sum(1 for n in thick if st(n,ca)==1))
        if a==b: rp.append(''); continue
        n10=sum(1 for x,y in xs if x and not y); n01=sum(1 for x,y in xs if not x and y); n00=len(xs)-n11-n10-n01
        rp.append(f'{(n11*n00-n10*n01)/math.sqrt((n11+n10)*(n01+n00)*(n11+n01)*(n10+n00)):.2f}')
    co.append(rc); ph.append(rp)
write('fig_app_cofiring_counts.csv',['lens']+[l for l,_ in L],co)
write('fig_app_cofiring_phi.csv',['lens']+[l for l,_ in L],ph)

# section 4, added presentation (unregistered): verdict totals per instrument
rows=[]
for inst,key in [('thin','tc'),('Organon','kc')]:
    for c in codes:
        n=sum(1 for p in P if p[key]==c); rows.append([inst,c,n,150,f'{100*n/150:.1f}'])
write('fig_s4_verdict_totals.csv',['instrument','verdict','answers','of','pct'],rows)
# section 7, added descriptive figure (unregistered): gender assigned to an asker who gave none
rows=[]
for inst in ['thin','thick']:
    runs=[n for n,r in po.items() if r['instrument']==inst and r['question']!='pregnancy']
    g=collections.Counter(ex[n]['gender_assigned'].strip().lower() for n in runs)
    a=g['male']+g['female']
    rows.append(['Organon' if inst=='thick' else 'thin',a,len(runs),f'{100*a/len(runs):.1f}',g['male'],g['female'],g['none']])
write('fig_s7_gender_assigned.csv',['instrument','gender_assigned','of','pct','male','female','none'],rows)
print('written to',OUT)
