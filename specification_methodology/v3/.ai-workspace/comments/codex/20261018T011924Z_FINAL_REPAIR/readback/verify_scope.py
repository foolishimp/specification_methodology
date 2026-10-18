"""Independent read-only checks of the frozen affected package; no qualification run."""
import hashlib, json, posixpath, re, subprocess
from pathlib import Path

REPO = '/Users/jim/src/apps/specification_methodology'
FINAL = '5a5b5ad80f0ba4b56b83aadd42ac130de53ba803'
BASE = '92fdb01c52bc4c6c7a7e265f92a668d0adb65098'
SOURCE = '91b06ebbecc3c0ac3eab4838e94f4544b076a217'
GENERATION = '810cc87dc3f0cbd8d31c6c023a31ccb56f8e7bfb'
TENANT = 'specification_methodology/v3/build_tenants/codex/'
RC = 'qualification/C3/rc5/integration/'
cache = {}
def raw(p, c=FINAL):
    key=(c,p)
    if key not in cache:
        cache[key]=subprocess.check_output(['git','-C',REPO,'show',c+':'+TENANT+p])
    return cache[key]
def doc(p,c=FINAL): return raw('successor/'+p,c)
def obj(p,c=FINAL): return json.loads(raw(p,c))
def sha(b): return hashlib.sha256(b).hexdigest()
def check(ok, label):
    if not ok: failures.append(label)
def headings(b):
    lines=b.decode().splitlines(keepends=True); result=[]; fence=None; seen={}
    for i,line in enumerate(lines):
        stripped=line.lstrip()
        m=re.match(r'(`{3,}|~{3,})',stripped)
        if m:
            if fence is None: fence=m.group(1)[0]
            elif m.group(1)[0]==fence: fence=None
            continue
        if fence is not None: continue
        m=re.match(r'^(#{1,6}) +(.+?) *#*\s*$',line)
        if not m: continue
        slug=re.sub(r'[^\w -]','',m.group(2).lower()).replace(' ','-')
        n=seen.get(slug,0);seen[slug]=n+1
        if n: slug+='-'+str(n)
        result.append((i,len(m.group(1)),slug))
    return lines,result
def sections(b,anchor):
    lines,hs=headings(b)
    entries=[(n,h) for n,h in enumerate(hs) if h[2]==anchor]
    if len(entries)!=1: raise ValueError(('anchor',anchor,len(entries)))
    n,(start,level,_)=entries[0]
    immediate=hs[n+1][0] if n+1<len(hs) else len(lines)
    hierarchical=next((h[0] for h in hs[n+1:] if h[1]<=level),len(lines))
    return list(dict.fromkeys([''.join(lines[start:end]) for end in [immediate,hierarchical]]))
def normalized_links(s,p):
    def replace(m):
        dest=m.group(2)
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',dest): return m.group(0)
        file,mark,anchor=dest.partition('#')
        absolute=posixpath.normpath(posixpath.join(posixpath.dirname(p),file)) if file else p
        return m.group(1)+absolute+(mark+anchor if mark else '')+m.group(3)
    return re.sub(r'(\[[^\]]*\]\()([^\n]+?)(\))',replace,s).strip()

failures=[]; summary={'subject':FINAL,'source':SOURCE,'generation':GENERATION,'baseline':BASE}
inv=obj('successor/interpretation/SOURCE_INVENTORY.json')['document_members']
source_delta=[]; generation_delta=[]
for m in inv:
    b=doc(m['path']);check(sha(b)==m['sha256'] and len(b)==m['bytes'],'inventory:'+m['path'])
    if b!=doc(m['path'],SOURCE): source_delta.append(m['path'])
    if b!=doc(m['path'],GENERATION): generation_delta.append(m['path'])
summary['document_members_checked']=len(inv)
summary['source_to_package_document_delta']=source_delta
summary['generation_to_package_document_delta']=generation_delta
check(not source_delta,'source/documentary equality');check(not generation_delta,'generation/documentary equality')
pins=0
for m in inv:
    p=m['path']
    if not p.startswith('standards/authority_compressions/') or not p.endswith('.md'): continue
    s=doc(p).decode()
    if not s.startswith('---'):continue
    front=s.split('---',2)[1]
    single=re.search(r'^source_ref: (.+)$',front,re.M)
    if single:
        digest=re.search(r'^source_digest: ([0-9a-f]{64})$',front,re.M).group(1)
        owner=posixpath.normpath(posixpath.join(posixpath.dirname(p),single.group(1)))
        check(sha(doc(owner))==digest,'compression:'+p+':'+owner);pins+=1
    for owner,digest in re.findall(r'^  ([\w/.-]+): ([0-9a-f]{64})$',front,re.M):
        check(sha(doc('standards/'+owner))==digest,'compression:'+p+':'+owner);pins+=1
summary['compression_pins_checked']=pins
index=obj(RC+'FRAME_INPUTS.json');excerpts=0;frame_failures=[]
for frame in index['frames']:
    p=frame['path'];b=doc(p);s=b.decode()
    check(sha(b)==frame['sha256'] and len(b)==frame['bytes'],'frame identity:'+p)
    markers=list(re.finditer(r'^Source: \[[^\n]+\]\(([^)]+)\); SHA256 `([0-9a-f]{64})`\.\n\n',s,re.M))
    check(len(markers)==len(frame['routes']),'frame marker count:'+p)
    for j,(m,route) in enumerate(zip(markers,frame['routes'])):
        owner=route['owner'];ob=doc(owner);end=markers[j+1].start() if j+1<len(markers) else len(s)
        body=s[m.end():end].strip()
        choices=sections(ob,route['anchor'])
        choices=[x.rstrip()+'\n' for x in choices if sha((x.rstrip()+'\n').encode())==route['section_sha256']]
        check(sha(ob)==m.group(2)==route['owner_sha256'],'frame owner:'+p+':'+owner)
        ok=any(normalized_links(body,p)==normalized_links(x,owner) for x in choices)
        if not ok: frame_failures.append({'frame':p,'owner':owner,'anchor':route['anchor'],'source_scope_matches':len(choices)})
        check(ok,'frame excerpt:'+p+':'+owner+'#'+route['anchor']);excerpts+=1
summary['frames_checked']=len(index['frames']);summary['frame_excerpts_checked']=excerpts;summary['frame_failures']=frame_failures
patch=obj(RC+'ACCOUNT_PATCH.json');ds=obj(RC+'DETERMINATIONS.json');portable=obj('successor/interpretation/source-account.json')
rows={d['id']:d for d in ds['determinations']};prows={d['id']:d for d in portable['determinations']}
summary['account_determination_count']=len(rows);summary['portable_determination_count']=len(prows)
native_program=obj('successor/interpretation/program.json')
row_checks=[]
projection_metadata_removed=0
def semantic_projection(value):
    if isinstance(value,dict):return {k:semantic_projection(v) for k,v in value.items() if k!='standing'}
    if isinstance(value,list):return [semantic_projection(v) for v in value]
    return value
for u in patch['updates']:
    d=rows[u['id']];pd=prows[u['id']];source=doc(d['owner']['path']);span_count=0
    check(any(sha(s.encode())==d['owner']['body_sha256'] for s in sections(source,d['owner']['anchor'])),'account owner:'+d['id'])
    for clause in d.get('source_clauses',[]):
        check(sha(source[clause['byte_start']:clause['byte_end']])==clause['sha256'],'account source span:'+d['id']+':'+clause['id']);span_count+=1
    compared=[]
    for key in ['predicate','obligations','permissions_exceptions','dependencies','result_mapping','argument','source_clauses','source_clause_ids','source_clause_roles']:
        if key in d:
            left=semantic_projection(d[key]) if key in ['argument','result_mapping'] else d[key]
            right=semantic_projection(pd.get(key)) if key in ['argument','result_mapping'] else pd.get(key)
            check(left==right,'portable field:'+d['id']+':'+key);compared.append(key)
    native_clauses=[cl for cl in native_program['clauses'] if cl['uri'].endswith(':'+d['id'])]
    check(len(native_clauses)==1,'native clause cardinality:'+d['id'])
    native=json.loads(native_clauses[0]['arguments'][0]['literal'])
    for key in compared:check(native.get(key)==pd.get(key),'native semantic field:'+d['id']+':'+key)
    row_checks.append({'id':d['id'],'source_spans_checked':span_count,'portable_semantic_fields_compared':compared,'native_semantic_fields_compared':compared,'native_clause_count':len(native_clauses)})
summary['affected_account_checks']=row_checks
summary['comparison_conventions']={'frame_sections':'Exact source section with trailing blank lines normalized to one terminal newline; local links compared after resolution.','portable_account':'Construction standing metadata is outside the product projection; all other compared semantic fields remain equal.'}
base_rows={d['id']:d for d in obj('qualification/C3/rc4/integration/DETERMINATIONS.json',BASE)['determinations']}
for key in ['SPEC_METHOD.testing-strategy-taxonomy','SPEC_METHOD.verification-layers']:
    d=rows[key];bd=base_rows[key]
    check(d['owner']['body_sha256']==bd['owner']['body_sha256'],'relocated owner changed:'+key)
    for before,after in zip(bd['source_clauses'],d['source_clauses']):
        check(before['sha256']==after['sha256'],'relocated source content changed:'+key)
cons=obj(RC+'CONSERVATION.json');cr={d['id']:d for d in cons['rows']};questions=obj(RC+'REPLACEMENT_QUESTIONS.json')['questions']
worked='REFERENCE_FRAME_METHOD.md#worked-binding-product-chain-drift-evaluation';rf='REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates';wr=cr[worked]
check(wr['disposition']=='superseded' and wr['successor_relation']['owner_decision'] is None,'worked replacement standing')
q=[q for q in questions if any(r['claim']==worked for r in q['rows'])]
check(len(q)==1 and any(r['claim']==rf for r in q[0]['rows']) and q[0]['decision']=={'status':'pending','record':None},'worked/RF005 question join')
check(next(r['relation'] for r in q[0]['rows'] if r['claim']==worked)==wr['successor_relation'],'worked question relation equality')
summary['conservation_count']=len(cr);summary['replacement_count']=sum(r['disposition']=='superseded' for r in cr.values());summary['question_count']=len(questions)
summary['worked_replacement']={'relation':wr['successor_relation']['id'],'question':q[0]['id'],'owner_decision':wr['successor_relation']['owner_decision'],'question_decision':q[0]['decision']}
summary['failures']=failures;summary['passed']=not failures
Path(__file__).with_name('CHECKS.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['affected_account_checks','frame_failures','failures']},indent=2))
print(json.dumps({'failure_count':len(failures),'first_failures':failures[:10]}))
raise SystemExit(1 if failures else 0)
