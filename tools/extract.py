import re,json
L=open('../source/tpa_bare_act_indiankanoon.txt',encoding='utf-8').read().split('\n')
L=[l for l in L if not l.startswith('Indian Kanoon - http') and l.strip()!='The Transfer Of Property Act, 1882']
txt='\n'.join(L)
ids=['3']+[str(i) for i in range(5,54)]+['53A','54','55','56','57']
out={}
pos=[]
for sid in ids:
    m=re.search(r'^'+re.escape(sid)+r'\. ',txt,re.M)
    pos.append((sid,m.start() if m else None))
for k,(sid,p) in enumerate(pos[:-1]):
    if p is None: print('missing',sid);continue
    nxt=[q for s,q in pos[k+1:] if q is not None and q>p][0]
    block=txt[p:nxt]
    head,_,body=block.partition('—')
    body=re.sub(r'\s*\n\s*',' ',body).strip()
    head=re.sub(r'\s+',' ',head).strip()
    # drop duplicated copy of the same section
    dup=body.find(head)
    if dup>0: body=body[:dup].strip()
    out[sid]={'head':head,'body':body}
json.dump(out,open('../src/bare_raw.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for s in out: print(s,len(out[s]['body']),out[s]['head'][:70])
