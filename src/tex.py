import numpy as np, io, base64
from PIL import Image
rng=np.random.default_rng(11)
def periodic(n,m,scale_x,scale_y):
    a=rng.standard_normal((n,m))
    fy=np.fft.fftfreq(n)[:,None]; fx=np.fft.fftfreq(m)[None,:]
    f=np.exp(-((fx*scale_x)**2+(fy*scale_y)**2))
    r=np.real(np.fft.ifft2(np.fft.fft2(a)*f))
    r=(r-r.min())/(r.max()-r.min()); return r
def b64(img,fmt='JPEG',q=78):
    buf=io.BytesIO(); img.save(buf,fmt,quality=q,optimize=True); return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
N=512
blot=periodic(N,N,110,110); mid=periodic(N,N,18,18); fine=rng.standard_normal((N,N)); fib=periodic(N,N,3,120)
base=np.array([243,234,211],float)
stain=np.clip((blot-0.6)*1.5,0,1)
img=base[None,None,:]-stain[...,None]*np.array([30,40,62])-(mid[...,None]-.5)*np.array([10,12,16])-fine[...,None]*3.2-(np.clip(fib-.6,0,1)[...,None])*np.array([14,16,20])
# a few foxing spots
for _ in range(14):
    y,x=rng.integers(0,N,2); r=rng.uniform(1.5,4.5)
    yy,xx=np.ogrid[:N,:N]; d=np.minimum(abs(yy-y),N-abs(yy-y))**2+np.minimum(abs(xx-x),N-abs(xx-x))**2
    img-= (np.exp(-d/(2*r*r))[...,None])*np.array([28,48,70])*rng.uniform(.4,1)
paper=Image.fromarray(np.clip(img,0,255).astype('uint8'))
W,H=1024,512
grain=periodic(H,W,2,160); knots=periodic(H,W,40,10)
wb=np.array([42,26,14],float)
w=wb[None,None,:]+(grain[...,None]-.5)*np.array([34,22,12])+(knots[...,None]-.5)*np.array([18,12,6])+rng.standard_normal((H,W))[...,None]*2
wood=Image.fromarray(np.clip(w,0,255).astype('uint8'))
L=periodic(256,256,90,90); lf=rng.standard_normal((256,256))
lb=np.array([90,23,18],float)
l=lb[None,None,:]+(L[...,None]-.5)*np.array([30,10,8])+lf[...,None]*6
leather=Image.fromarray(np.clip(l,0,255).astype('uint8'))
P=b64(paper,q=72); Wd=b64(wood,q=70); Le=b64(leather,q=72)
print(len(P)//1024,len(Wd)//1024,len(Le)//1024,'KB')
import os; os.makedirs('../tools/previews',exist_ok=True); paper.save('../tools/previews/paper.png'); wood.save('../tools/previews/wood.png')
open('tex.json','w').write(__import__('json').dumps({'paper':P,'wood':Wd,'leather':Le}))
