import sys,subprocess,json,hashlib,copy,importlib.util,collections
from pathlib import Path
sys.dont_write_bytecode=True
REPO=Path('/Users/jim/src/apps/specification_methodology-codex');TMP=Path('/private/tmp/i4-integration-review-cbe4e36')
C='cbe4e368865e1e99fd8884fba7486e1f76679379';D='01b01274b244ae6e5de10bf6bacb60087462cbb5';I3='199c6d29bc02590a8b7f252043fc43223c09808d';R='989ee2278d4a5d9bcfbfc80570570450ee811b24'
P='specification_methodology/v3/build_tenants/codex/';Q=P+'qualification/C3/iteration-4/';OLD=P+'qualification/C3/iteration-3/';PK=P+'successor/'
cache={}; reads=[]
def raw(path,commit=C):
 key=(commit,path)
 if key not in cache:
  cache[key]=subprocess.check_output(['git','show',commit+':'+path],cwd=REPO);reads.append({'commit':commit,'path':path,'bytes':len(cache[key])})
 return cache[key]
def load(path,commit=C):return json.loads(raw(path,commit))
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
checks={};fails=[]
def check(name,value,details=None):
 checks[name]=bool(value)
 if not value:fails.append({'check':name,'details':details})
# Import only frozen-equal helper modules; no command main or global rebinding.
sys.path.insert(0,str(REPO/(Q+'tools')))
for f in ['context.py','reconcile_account.py','prepare_integration_inputs.py']:
 check('frozen_helper_'+f,(REPO/(Q+'tools/'+f)).read_bytes()==raw(Q+'tools/'+f))
import context as ctx,reconcile_account as rec,prepare_integration_inputs as prep
build=ctx.library('iteration-3/build_interpretation.py');repair=ctx.library('iteration-3/review-repair/interpretation/repair_account.py')
for f,mod in [('iteration-3/build_interpretation.py',build),('iteration-3/review-repair/interpretation/repair_account.py',repair)]:
 check('frozen_library_'+f,Path(mod.__file__).read_bytes()==raw(P+'qualification/C3/'+f))
base=load(OLD+'DETERMINATIONS.json',I3);final=load(Q+'DETERMINATIONS.json');receiving=load(Q+'DETERMINATIONS.json',R);integration=load(Q+'ACCOUNT_INTEGRATION.json');inputs=load(Q+'INTEGRATION_INPUTS.json');initial=load(Q+'INPUTS.json')
check('historical_I3_account_unchanged',raw(OLD+'DETERMINATIONS.json')==raw(OLD+'DETERMINATIONS.json',I3))
check('receiving_sha',sha(raw(Q+'DETERMINATIONS.json',R))==prep.RECEIVING_SHA==inputs['receiving_account']['sha256'])
check('original_input_sha',sha(raw(OLD+'DETERMINATIONS.json',I3))==integration['input_sha256'])
rows={r['id']:copy.deepcopy(r) for r in base['determinations']};frows={r['id']:r for r in final['determinations']};rrows={r['id']:r for r in receiving['determinations']}
check('stable_unique_701_ids',len(rows)==len(frows)==len(final['determinations'])==701 and set(rows)==set(frows))
# Read complete frozen documentary bytes without sending full bodies to actor context.
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',D,'--',PK],cwd=REPO,text=True).splitlines()
source={}
for p in paths:
 rel=p[len(PK):]
 if rel.startswith('interpretation/'):continue
 b=raw(p,D);source[rel]=b;dest=TMP/'package'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
check('candidate_documentary_equals_freeze',all(raw(PK+p)==b for p,b in source.items()))
patches={};dependents=[];routing=[];patchcounts={};corepins=[]
for name in ['core','delivery','profiles']:
 part=load(Q+'source/'+name+'/ACCOUNT_PATCH.json');items=part.get('patches',part.get('changes',[]));patchcounts[name]=len(items)
 for original in items:
  item=copy.deepcopy(original)
  if name=='core':item['candidate_body_scope']='immediate_body_excluding_heading'
  assert item['id'] not in patches;patches[item['id']]=item
 dependents+=part.get('dependent_argument_refresh',[])
for selected in inputs['patches']:
 part=load(Q+selected['path']);check('patch_pin_'+selected['path'],sha(raw(Q+selected['path']))==selected['sha256'])
 patchcounts[selected['path']]=len(part['patches'])
 if selected['stage']=='source_repair':
  for item in part['patches']:assert item['id'] not in patches;patches[item['id']]=copy.deepcopy(item)
 else:routing.append((selected,part))
oldsource={p:raw(PK+p,I3) for p in {r['owner']['path'] for r in rows.values()}};units={p:repair.heading_units(b) for p,b in source.items()}
changed=[];relocated=[]
for identifier,row in rows.items():
 p,a=row['owner']['path'],row['owner']['anchor'];whole=row['owner'].get('unit_scope')=='whole_member';unit=None if whole else units[p][a]
 oldbody=repair.local_source_body(row,oldsource[p])[0];newbody=source[p] if whole else unit['body'];item=patches.get(identifier)
 check('changed_owner_patched_'+identifier,oldbody==newbody or item is not None)
 if item:
  for k in ['preimage_body_sha256','i3_source_heading_sha256']:
   if item.get(k):check(k+'_'+identifier,item[k]==sha(oldbody))
  if item.get('source_current',{}).get('sha256'):check('source_current_'+identifier,item['source_current']['sha256']==sha(newbody))
  if item.get('argument_preimage_sha256'):check('argument_preimage_'+identifier,item['argument_preimage_sha256']==sha(json.dumps(row.get('argument'),sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()))
  expected=item.get('body_sha256',item.get('candidate_body_sha256'));pinned=newbody.split(b'\n',1)[1] if item.get('candidate_body_scope')=='immediate_body_excluding_heading' else newbody
  if expected:check('candidate_body_'+identifier,expected==sha(pinned))
  if item.get('candidate_body_scope'):corepins.append({'id':identifier,'without_heading':expected==sha(pinned),'with_heading':expected==sha(newbody)})
  fields=rec.authored_fields(item,row);row.update(copy.deepcopy(fields));changed.append(identifier)
 moved=repair.remap_blocks(row,oldsource[p],source[p],unit)
 blocks=row.get('source_clauses',[]);body=[b for b in blocks if b['id']=='body']
 if len(body)>1:
  current=[b for b in body if b['sha256']==sha(newbody) and b['byte_start']==(0 if whole else unit['byte_start'])];assert len(current)==1
  row['source_clauses']=[b for b in blocks if b['id']!='body']+current;moved=sorted(set(moved+['body']))
 row['owner']=repair.make_owner(p,unit,source[p])
 if 'owner_body_sha256' in row:row['owner_body_sha256']=sha(newbody)
 if 'source_member_sha256' in row:row['source_member_sha256']=sha(source[p])
 for owner in row.get('supporting_sources',[]):
  b=source[owner['path']];whole_s=owner.get('unit_scope')=='whole_member';u=None if whole_s else units[owner['path']].get(owner.get('anchor'))
  if u is not None or whole_s:owner.update(repair.make_owner(owner['path'],u,b))
  for k in ['sha256','member_sha256']:
   if k in owner:owner[k]=sha(b)
 if moved:relocated.append({'id':identifier,'coarsened_blocks':moved})
useddependents=[]
for item in dependents:
 row=rows[item['id']]
 if 'new_direct_family_arguments' in item:
  if item['new_direct_family_arguments']:row.setdefault('argument',{})['source_family_arguments']=copy.deepcopy(item['new_direct_family_arguments']);useddependents.append(item['id'])
 elif item.get('semantic_fields'):row.update(copy.deepcopy(item['semantic_fields']));useddependents.append(item['id'])
 else:raise AssertionError(item['id'])
pre_route=copy.deepcopy(rows);preimages=0;scope_preservation=0;guards=0;coverage=[];unbound=[];all_routing=[]
for selected,part in routing:
 for item in part['patches']:
  if item['id'] in selected.get('excluded_items',{}):continue
  row=rows[item['id']];before=copy.deepcopy(row);paths=set(item.get('set',{}))|set(item.get('semantic_fields',{}));expected=selected['before_fields'][item['id']];scopes=rec.scoped_operations(item)
  check('path_guarded_'+selected['path']+':'+item['id'],not(paths-set(expected)))
  for path in paths:
   value=rec.get_path(row,path);scope=scopes.get(path)
   if scope:value=[x for x in (value or []) if rec.owned_family(x,scope)]
   check('field_preimage_'+selected['path']+':'+item['id']+':'+path,sha(dump(value))==expected[path]);preimages+=1
   original=rec.get_path(rrows[item['id']],path)
   if scope:original=[x for x in (original or []) if rec.owned_family(x,scope)]
   check('frozen_preimage_'+selected['path']+':'+item['id']+':'+path,sha(dump(original))==expected[path])
   # Any actual guarded preimage perturbation must differ.
   check('adverse_preimage_'+selected['path']+':'+item['id']+':'+path,sha(dump({'review_mutation':value}))!=expected[path]);guards+=1
  fields=rec.authored_fields(item,row);row.update(copy.deepcopy(fields));all_routing.append((selected,item,before,copy.deepcopy(row)))
  for path,scope in scopes.items():
   prev=[x for x in (rec.get_path(before,path) or []) if not rec.owned_family(x,scope)]
   after=[x for x in (rec.get_path(row,path) or []) if not rec.owned_family(x,scope)]
   check('preserve_foreign_'+selected['path']+':'+item['id']+':'+path,prev==after);scope_preservation+=1
  extra=set(fields)-{p.split('.')[0] for p in paths}
  if extra:unbound.append({'patch':selected['path'],'id':item['id'],'fields':sorted(extra),'item_keys':sorted(item)})
rowchanges=[];rowcache={p:(b,units[p]) for p,b in source.items()}
for identifier,row in rows.items():rec.bind_family_rows(row,identifier,D,repair,rowcache,rowchanges)
check('exact_rows_reproduced',rows==frows,[i for i in rows if rows[i]!=frows[i]])
check('direct_38_exact',len(changed)==38 and changed==[i['id'] for i in integration['direct_patches']])
check('dependents_67_exact',len(useddependents)==67 and useddependents==integration['dependent_patches'])
check('coarsened_exact',relocated==integration['coarsened_coordinates'])
check('row_rebindings_exact',rowchanges==integration['argument_row_coordinate_changes'])
current,excluded=build.semantic_projection(final);validated=build.validate_account(current,package=TMP/'package');check('validate_full_final_account',len(validated)==701)
# Exact row authentication independent of rebinding implementation.
source_rows=[]
def walk(v,path=''):
 if isinstance(v,dict):
  if 'source_row' in v and isinstance(v['source_row'],dict):source_rows.append((path,v['source_row']))
  for k,x in v.items():walk(x,path+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,path+'/'+str(i))
for row in final['determinations']:walk(row,row['id'])
for loc,s in source_rows:
 if not all(k in s for k in ['path','anchor','sha256']):continue
 u=units[s['path']][s['anchor']];hits=[i for i,b in enumerate(u['body'].splitlines(keepends=True)) if sha(b)==s['sha256'] or sha(b.rstrip(b'\r\n'))==s['sha256']]
 check('exact_source_row_'+loc,len(hits)==1)
 if 'line' in s:check('line_'+loc,s['line']==u['start_line']+hits[0])
 if 'member_sha256' in s:check('member_'+loc,s['member_sha256']==sha(source[s['path']]))
 if 'source_commit' in s:check('commit_'+loc,s['source_commit']==D)
# Dependency dialect and old result/effect fields.
relations=[(r['id'],d) for r in final['determinations'] for d in r.get('dependency_relations',[])]
check('dependency_id_kind_dialect',all('id' in d and 'kind' in d and 'target' not in d and 'relation' not in d for _,d in relations))
special=['result_mapping','effect_predicates','compute_predicates','state_classifier','decision_rule']
semantic_changes={i:[k for k in special if base_r.get(k)!=frows[i].get(k)] for i,base_r in {r['id']:r for r in base['determinations']}.items()};semantic_changes={i:k for i,k in semantic_changes.items() if k}
report={'subject':C,'documentary_input':D,'checks_total':len(checks),'checks_passed':sum(checks.values()),'failures':fails,'account_sha256':sha(raw(Q+'DETERMINATIONS.json')),'receiving_sha256':sha(raw(Q+'DETERMINATIONS.json',R)),'counts':{'rows':len(frows),'direct_patches':len(changed),'delivery_dependents':len(useddependents),'routing_items_applied':len(all_routing),'routing_preimages':preimages,'scoped_foreign_preservation_checks':scope_preservation,'source_row_occurrences':len(source_rows),'rebound_coordinates':len(rowchanges),'coarsened_rows':len(relocated),'dependency_relations':len(relations)},'unguarded_side_effect_fields':unbound,'core_candidate_pins':corepins,'changed_surviving_result_effect_fields':semantic_changes,'patch_counts':patchcounts,'computed_git_reads':{'unique_objects':len(reads),'bytes':sum(r['bytes'] for r in reads)}}
(TMP/'report.json').write_bytes(dump(report));(TMP/'computed-reads.json').write_bytes(dump(reads));print(json.dumps(report,indent=2))
