import re,sys,os,glob
root=sys.argv[1]
def slug(h):
    h=h.strip().lower()
    h=re.sub(r'[^\w\- ]','',h,flags=re.U)
    return h.replace(' ','-')
anch={}
files=glob.glob(os.path.join(root,'**/*.md'),recursive=True)
for f in files:
    seen={}
    a=set()
    incode=False
    for l in open(f,encoding='utf-8'):
        if l.startswith('```'): incode=not incode
        if incode: continue
        m=re.match(r'^(#{1,6})\s+(.*)',l)
        if m:
            s=slug(re.sub(r'`','',m.group(2)))
            n=seen.get(s,0); seen[s]=n+1
            a.add(s if n==0 else f'{s}-{n}')
    anch[os.path.abspath(f)]=a
bad=0
for f in files:
    txt=open(f,encoding='utf-8').read()
    for m in re.finditer(r'\]\(([^)\s]+)\)',txt):
        t=m.group(1)
        if re.match(r'^[a-z]+:',t): continue
        p,_,frag=t.partition('#')
        tgt=os.path.abspath(os.path.join(os.path.dirname(f),p)) if p else os.path.abspath(f)
        if not os.path.exists(tgt):
            print('MISSING',os.path.relpath(f,root),t); bad+=1; continue
        if frag and tgt.endswith('.md') and frag not in anch.get(tgt,set()):
            print('ANCHOR',os.path.relpath(f,root),t); bad+=1
print('bad',bad)
