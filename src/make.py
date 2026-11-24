import json
import qr
SITE_URL='https://mlokanath2007-sketch.github.io/tpa-mindmap/'  # live link used by the Share button and QR code
d=json.load(open('content.json'))
j=json.dumps(d,ensure_ascii=False).replace('</','<\\/')
import crisp
mm=json.dumps({'branch':crisp.BRANCH,'c':{k:[v[0],v[1]] for k,v in crisp.C.items()}},ensure_ascii=False).replace('</','<\\/')
t=open('template.html').read().replace('/*DATA*/',j).replace('/*MM*/',mm)
t=t.replace('<!--QRSVG-->',qr.svg(SITE_URL)).replace('{{SITE_URL}}',SITE_URL).replace('{{SITE_SHORT}}',SITE_URL.split('://',1)[1].rstrip('/').replace('/','/<wbr>'))
open('../dist/classic.html','w').write(t)
print(len(t.encode())//1024,'KB')
