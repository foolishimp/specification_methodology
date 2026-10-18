import copy, dataclasses, hashlib, importlib.util, json, sys, time
from pathlib import Path
root=Path('/Users/jim/src/apps/specification_methodology/a_c/dogfood')
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); sys.modules[name]=m; s.loader.exec_module(m); return m
v=module('v3transportreview',root/'v3_graphify.py')
indexer_path=Path('/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/a_c/install/axiom_indexer-v2.5.1-rc.2/build_tenants/core/code/ac.py')
assert hashlib.sha256(indexer_path.read_bytes()).hexdigest()=='5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8'
i=module('pinnedindexerreview',indexer_path)
reports=[]
for tenant in ('claude','codex'):
 t=time.monotonic(); s=v.load_subject(tenant)
 prep=module('prepare_'+tenant,s.root/'prepare.py')
 if tenant=='codex':
  exact=prep.acquire(Path('/Users/jim/src/apps/specification_methodology-codex'))
 else:
  archive,manifest,subject=prep.acquire(Path('/Users/jim/src/apps/specification_methodology-claude'))
  exact={'input/candidate.tar.gz':archive,'input/manifest.json':prep.json_bytes(manifest),'subject.json':prep.json_bytes(subject)}
 assert all((s.root/path).read_bytes()==raw for path,raw in exact.items())
 m=v.build_model(s)
 assert v.recover_program(m)==s.program
 selectors=s.program['frame_indexes']
 views=v.ac.project_many(m,[([row['uri']],None) for row in selectors])
 for selector,view in zip(selectors,views):
  native=i.reference_closure(s.program,[selector])
  expected={value for family in native.values() for value in family}|{selector['uri']}
  assert set(view['included'])==expected,(tenant,selector['uri'],expected^set(view['included']))
  assert all(m.records[k].fields['value']['native_family'] not in ('envelope','source_members') for k in view['included'])
 symbol_refs=sum(1 for cl in s.program['clauses'] for a in cl['arguments'] if a.get('ref') in {x['uri'] for x in s.program['symbols']})
 report={'tenant':tenant,'custody_reproduced':True,'selectors_vs_pinned_rc2':len(selectors),'native_roundtrip':True,'symbol_argument_refs':symbol_refs,'native_counts':{f:len(s.program[f]) for f in v.FAMILIES},'elapsed_seconds':round(time.monotonic()-t,3)}
 # Independent synthetic counterexample: residual applies to both a clause and a symbol,
 # attachment from either one must acquire the other and then close the other subject's refs.
 p=copy.deepcopy(s.program); first=p['clauses'][0]['uri']
 if not p['symbols']:
  p['symbols'].append({'uri':'urn:review:symbol','kind':'urn:review:symbol-kind','label':'review symbol','source_refs':[]})
 sym=p['symbols'][0]['uri']
 residual={'uri':'urn:review:multi-subject-residual','kind':'unresolved','subject_refs':[first,sym],'detail':'review two distinct subjects','re_entry_refs':[],'source_refs':[]}
 p['residuals'].append(residual)
 sel={'uri':'urn:review:index','frame_ref':p['frame_refs'][0],'scope':'review','clause_refs':[first],'residual_refs':[],'source_refs':[]}
 p['frame_indexes'].append(sel)
 synthetic=dataclasses.replace(s,program=p); v.validate_native(synthetic); sm=v.build_model(synthetic)
 for seed in (first,sym,residual['uri']):
  # The actual indexer has selectors only, so use temporary selector rooted at clause
  # or residual, and use a clause explicitly referring to the symbol for the symbol case.
  if seed==sym:
   new={'uri':'urn:review:symbol-seed-clause','clause_type':'relation','operator':'urn:review:operator','arguments':[{'role':'urn:review:role','ref':sym}],'statement':'review','source_refs':[]}
   pp=copy.deepcopy(p); pp['clauses'].append(new); ss=dict(sel,clause_refs=[new['uri']]); pp['frame_indexes'][-1]=ss
   mm=v.build_model(dataclasses.replace(s,program=pp)); vv=v.ac.project(mm,[ss['uri']]); nn=i.reference_closure(pp,[ss]); expected={x for xs in nn.values() for x in xs}|{ss['uri']}
  else:
   ss=dict(sel,clause_refs=[seed] if seed==first else [],residual_refs=[seed] if seed==residual['uri'] else [])
   pp=copy.deepcopy(p); pp['frame_indexes'][-1]=ss; mm=v.build_model(dataclasses.replace(s,program=pp)); vv=v.ac.project(mm,[ss['uri']]); nn=i.reference_closure(pp,[ss]); expected={x for xs in nn.values() for x in xs}|{ss['uri']}
  assert set(vv['included'])==expected,(tenant,seed,set(vv['included'])^expected)
 report['multi_subject_residual_vs_pinned_rc2']=True
 # Required closure must refuse an undersized budget, with no returned partial result.
 try: v.ac.project(m,[selectors[0]['uri']],0)
 except v.ac.Refusal: report['zero_budget_refused']=True
 else: raise AssertionError('undersized budget accepted')
 reports.append(report); print(json.dumps(report),flush=True)
Path('/tmp/v3_i5_nonauthor_review.json').write_text(json.dumps(reports,indent=2))
