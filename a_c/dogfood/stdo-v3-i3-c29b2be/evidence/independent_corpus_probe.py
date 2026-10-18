import sys,json,gzip,hashlib,tarfile,subprocess,statistics,copy
from pathlib import Path
p=Path('a_c/dogfood/stdo-v3-i3-c29b2be');sys.path.insert(0,str(p))
import representation as r
import ac_graph as ac
pins={'representation.py':'4f4ce6d51e9319187d1be514a3a1529376ea295c00199c2ebb978897b2cbc78a','artifacts/manifest.json':'4c4cc00caa6ddff6ab84378e67c9998dc237e3244939753cb42c1cf94d76bb9b'}
for f,s in pins.items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==s
subject,model,manifest=r.load_representation(p/'artifacts')
assert model.sha256=='e488272cb5f01c623b9af970d066e118666218abaa1fd7aae0fe8708f162636a'
# Compare every archived byte directly with the named immutable Git input.
pre='specification_methodology/v3/build_tenants/codex/successor/'
for name,raw in subject.members.items():
 expected=subprocess.check_output(['git','show',r.SOURCE_COMMIT+':'+pre+name]);assert expected==raw,name
# Independently inspect raw authored argument sequence and compare typed values.
clauses=subject.program['clauses'];selectors=subject.program['frame_indexes'];residuals=subject.program['residuals'];adj={};nref=nroute=inline=0
for clause in clauses:
 uid=clause['uri'];val=model.records[uid].fields['value'];args=clause['arguments'];pairs=[];routes=[]
 for i,arg in enumerate(args):
  if 'ref'in arg:
   assert i>0 and args[i-1]['role'].endswith('#reference-location')
   pairs.append({'ordinal':i,'pointer':args[i-1]['literal'],'role':arg['role'],'target':arg['ref']});nref+=1
  if arg['role'].endswith('#acquisition-route'):
   native=json.loads(arg['literal']);routes.append({'ordinal':i,'payload':arg['literal'],'target':native['target'],'target_index':native['target_index']});nroute+=1
  inline+=arg['role'].endswith('#inlined-contract')
 assert val['required_refs']==pairs,(uid,'required')
 assert val['routes']==routes,(uid,'routes')
 assert json.loads(val['native_json'])==clause
 adj[uid]={a['ref'] for a in args if 'ref'in a}
# Independent full fixed-point closure from frozen raw refs, rather than r.native_closure.
views=ac.project_many(model,[([s['uri']],None) for s in selectors]);counts=[]
for s,v in zip(selectors,views):
 inc=set(s['clause_refs'])
 while True:
  nxt=inc|set().union(*(adj[u] for u in inc))
  if nxt==inc:break
  inc=nxt
 rr=set(s['residual_refs'])|{q['uri'] for q in residuals if inc.intersection(q['subject_refs'])}
 assert set(v['included'])==inc|rr|{s['uri']},s['uri']
 counts.append(len(inc))
# All route references are non-governing; all direct targets govern by their exact slot.
for ref in model.references:
 if ref.path[:2]==('value','routes'):assert ref.schema['governing'] is False
 if ref.path[:2]==('value','required_refs'):assert ref.schema['governing'] is True
release=r.select(subject,model,'RELEASE_METHOD.open-questions');assert len(release['projection']['populations']['residuals'])==2
for short in ['AXIOMATIC_CALCULUS.ac-016-typed-composition','AXIOMATIC_CALCULUS.ac-017-interpretation-fidelity']:
 sel=r.select(subject,model,short)
 assert sel['acquisition_routes']['conditional']
 assert all(e['route']['qualification']['required_when'] for e in sel['acquisition_routes']['conditional'])
try:ac.project(model,[selectors[0]['uri']],len(views[0]['included'])-1)
except ac.Refusal:pass
else:raise AssertionError('short budget accepted')
assert r.recover_program(model)==subject.program
assert not any(model.document['populations'][f] for f in ['relations','constraints','latitude','traversals','transformations','judgments'])
for f,s in pins.items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==s
print(json.dumps({'status':'passed','git_byte_equal_members':len(subject.members),'pins':subject.pin_counts,'required_occurrences':nref,'route_occurrences':nroute,'inline_arguments':inline,'all_actual_selectors':len(views),'closure_min_median_max':[min(counts),statistics.median(counts),max(counts)],'model_sha256':model.sha256,'source_program_json_recovery':True,'budget_refusal':True,'lawful_empty_families':True},sort_keys=True))
