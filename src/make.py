import json
d=json.load(open('content.json'))
j=json.dumps(d,ensure_ascii=False).replace('</','<\\/')
import crisp
mm=json.dumps({'branch':crisp.BRANCH,'c':{k:[v[0],v[1]] for k,v in crisp.C.items()}},ensure_ascii=False).replace('</','<\\/')
t=open('template.html').read().replace('/*DATA*/',j).replace('/*MM*/',mm)
open('../dist/classic.html','w').write(t)
print(len(t.encode())//1024,'KB')
