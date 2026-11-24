import re,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import oldfx
src=open('../dist/classic.html').read()
a=src.index('<style>'); b=src.index('</style>')+len('</style>')
css=open('old_style.css').read().replace('</style>',oldfx.CSS+'</style>')
out=src[:a]+css+src[b:]
out=re.sub(r'<link href="https://fonts.googleapis.com/css2\?[^"]+" rel="stylesheet">','<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&display=swap" rel="stylesheet">',out)
cover='''<div class="cover-ov" id="coverOv" role="dialog" aria-label="Book cover">
  <div class="book">
    <div class="inner">Sections 5 to 55, with Sections 3 and 56</div>
    <button class="lid" id="lid" aria-label="Open the book">
      <span class="front"><span class="orn">❦</span><span class="ct">Transfer of Property Act, 1882</span><span class="rule"></span><span class="cb">by Madhi Lokanath</span></span>
      <span class="back"></span>
    </button>
    <button class="press" id="press">Press here to open the book</button>
  </div>
</div>
<div class="pagewrap"><div class="page">
<div class="wrap">'''
out=out.replace('<body>\n<div class="wrap">','<body>\n'+cover,1)
out=out.replace('\n<div class="reader" id="reader"','\n</div></div>\n<div class="reader" id="reader"',1)
out=out.replace('<div class="rwrap" id="rbody"></div>','<div class="rpage"><div class="rwrap" id="rbody"></div></div>',1)
js='''<script>
{const ov=document.getElementById("coverOv");
 if(/^#s-/.test(location.hash)){ov.remove()}else{
 let opened=false;const go=()=>{if(opened)return;opened=true;ov.classList.add("open");const rm=matchMedia("(prefers-reduced-motion: reduce)").matches;setTimeout(()=>ov.classList.add("gone"),rm?50:1350);setTimeout(()=>ov.remove(),rm?700:2000)};
 document.getElementById("lid").addEventListener("click",go);document.getElementById("press").addEventListener("click",go);
 document.addEventListener("keydown",e=>{if(document.body.contains(ov)&&(e.key==="Enter"||e.key===" ")){e.preventDefault();go()}},{once:false});
 setTimeout(()=>{const l=document.getElementById("lid");if(l)l.focus()},50);}}
</script>
</body>'''
out=out.replace('</body>',js,1)
os.makedirs('../dist',exist_ok=True)
open('../dist/index.html','w').write(out)
print(len(out)//1024,'KB', out.count('class="pagewrap"'), out.count('class="rpage"'))
