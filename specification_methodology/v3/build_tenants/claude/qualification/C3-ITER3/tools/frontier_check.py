import re,sys
def rows(path):
    out=[];sec=None
    for n,l in enumerate(open(path,encoding='utf-8'),1):
        if l.startswith('## '): sec=l[3:].strip(); continue
        if not l.startswith('| ') or l.startswith('|---'): continue
        c=l.rstrip('\n').split(' | ')
        if len(c)<2: continue
        key=None
        m=re.search(r'`(#[^`]+)`',c[1]) if len(c)>1 else None
        if m: key=(sec,m.group(1))
        else:
            m=re.match(r'\| `([^`]+)`',l)
            if m and sec and ('member' in sec.lower() or 'beyond' in sec.lower() or 'Auxiliary' in sec): key=(sec,m.group(1))
        if key: out.append((n,key))
    return out
common=rows(sys.argv[1]); tenant=rows(sys.argv[2])
ck=[k for _,k in common]; tk=[k for _,k in tenant]
from collections import Counter
cc=Counter(ck); tc=Counter(tk)
print('common rows',len(ck),'tenant rows',len(tk))
missing=[k for k in cc if tc[k]<cc[k]]
extra=[(n,k) for n,k in tenant if tc[k]>cc.get(k,0)]
print('missing from tenant',len(missing),missing[:5])
print('tenant-only rows',len(extra)); [print(' ',n,k) for n,k in extra[:10]]
