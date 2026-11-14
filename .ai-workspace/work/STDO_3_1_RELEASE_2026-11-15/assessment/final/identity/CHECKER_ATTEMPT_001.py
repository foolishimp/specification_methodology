from pathlib import Path
import subprocess,json,hashlib,zipfile
from datetime import datetime,timezone
c=Path('/Users/jim/src/apps/specification_methodology-3.1-release');w=Path('/Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15');out=w/'assessment/final/identity';out.mkdir(exist_ok=True)
def git(*args):return subprocess.check_output(['git','-C',str(c),*args])
def g(*args):return git(*args).decode().strip()
def sha(raw):return hashlib.sha256(raw).hexdigest()
plan=json.loads((w/'REF_PLAN.json').read_text());cohort=json.loads((w/'COHORT_DRAFT.json').read_text());graph=json.loads((w/'REF_GRAPH.json').read_text());a=cohort['native']['commit'];b=cohort['source']['carrier'];assert b=='f68e8f47db69425205db313ba72fbc9cad94c2b9'
# Bind exactly the immutable content graph, not its later review envelope.
canonical=json.dumps(graph['refs'],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode();assert sha(canonical)==graph['sha256']==cohort['ref_graph_sha256']
remote_raw=git('ls-remote','origin');(out/'REMOTE_BEFORE.txt').write_bytes(remote_raw);remote={line.split('\t')[1]:line.split('\t')[0] for line in remote_raw.decode().splitlines()};refs=[]
assert len(plan['refs'])==25 and len({r['destination'] for r in plan['refs']})==25
for row in plan['refs']:
 assert g('rev-parse',row['source'])==row['object'];assert remote.get(row['destination'],'')==row['expected_remote'];assert g('rev-parse',row['source']+'^{commit}')==row['commit']
 typ=g('cat-file','-t',row['source']);assert typ==('tag' if row['destination'].startswith('refs/tags/') else 'commit')
 refs.append({**row,'actual_type':typ,'actual_peel':g('rev-parse',row['source']+'^{commit}'),'remote_expectation_matches':True})
subprocess.run(['git','-C',str(c),'merge-base','--is-ancestor',remote['refs/heads/main'],b],check=True)
assert g('rev-parse',b+':specification_methodology/v3/build_tenants/common')==g('rev-parse',a+':specification_methodology/v3')==cohort['source']['native_source_tree']
products=[]
for p in cohort['products']:
 assert g('rev-parse',p['commit']+':'+p['root'])==p['subtree_tree'];definition=git('show',p['definition']['commit']+':'+p['definition']['path']);assert sha(definition)==p['definition']['sha256']
 products.append({'namespace':p['namespace'],'commit':p['commit'],'subtree_tree':p['subtree_tree'],'definition_sha256':sha(definition),'definition_id':json.loads(definition)['id']})
assets=[]
for row in cohort['assets']:
 raw=(w/'assets'/row['name']).read_bytes();assert sha(raw)==row['sha256'] and len(raw)==row['bytes'];assets.append(row)
with zipfile.ZipFile(w/'assets/stdo-products-v3.1.0-rc.1.zip') as z:
 inventory=json.loads(z.read('PRODUCTS.json'));expected={'PRODUCTS.json','INSTALLATION.md'}
 for name,p in inventory['products'].items():
  for row in p['members']:
   key=name+'/'+row['path'];raw=z.read(key);assert sha(raw)==row['sha256'] and len(raw)==row['bytes'];expected.add(key)
 assert set(z.namelist())==expected and len(z.namelist())==len(expected)
 package={'members':len(expected),'product_members':len(expected)-2,'products_inventory_sha256':sha(z.read('PRODUCTS.json')),'identity_pins':{k:v['identity_sha256'] for k,v in inventory['products'].items()}}
 for p in cohort['products']:
  if p['namespace']!='specification_methodology':assert p['distribution']['members']==inventory['products'][p['namespace']]['members']
 # The semantic inputs and current visual are exact bytes from their B subjects.
 equal=[]
 for name in ['python-pure-refactor-v2','sdlc-workflow-v1']:
  for fn in ['INDEX.json','PURPOSE.json','SOURCES.json']:
   path='purpose_context/skills/stdo-context/indexes/stdo-3.1.0-rc.1-'+name+'/'+fn;assert z.read(path)==git('show',b+':'+path);equal.append(path)
 for path in ['stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/run/generation/proposal/model.json','stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/run/generation/proposal/explorer.html']:
  assert z.read(path)==git('show',b+':'+path);equal.append(path)
 package['semantic_members_equal_to_B']=equal
 # Stage/source public surfaces differ by an explicit distribution projection.
 relation=json.loads(z.read('purpose_context/SOURCE_RELATION.json'));(out/'PURPOSE_CONTEXT_SOURCE_RELATION.json').write_text(json.dumps(relation,indent=2)+'\n')
 for path in ['stdo_skills/INVENTORY.json','stdo_skills/DEPENDENCIES.json','stdo_skills/specification/composition/DEPENDENCIES.json']:
  if path in z.namelist():(out/(path.replace('/','__'))).write_bytes(z.read(path))
evidence=[]
for e in cohort['qualification']['evidence']:
 raw=git('show',e['commit']+':'+e['path']);assert sha(raw)==e['sha256'];evidence.append({**e,'verified_in_B':True})
qualified=[]
for row in plan['qualified_files']:
 assert sha(Path(row['path']).read_bytes())==row['sha256'];qualified.append(row)
value={'kind':'stdo.final-identity-operator-readback/1','observed_at_utc':datetime.now(timezone.utc).isoformat(),'native':a,'carrier':b,'carrier_parents':g('show','-s','--format=%P',b).split(),'ref_graph_sha256':graph['sha256'],'repository':g('config','--get','remote.origin.url'),'refs':refs,'remote_main_is_ancestor_of_B':True,'native_source_tree_equals_A':True,'products':products,'assets':assets,'companion_package':package,'cohort_evidence':evidence,'qualified_files_checked':len(qualified),'working_tree_clean':g('status','--porcelain','--untracked-files=no')=='','standing':'Actual local prepublication objects/content and fresh remote expectations verified. Atomic push and public readback are unperformed.'}
(out/'INPUT_READBACK.json').write_text(json.dumps(value,indent=2)+'\n');print(json.dumps({k:value[k] for k in ['native','carrier','ref_graph_sha256','remote_main_is_ancestor_of_B','native_source_tree_equals_A','qualified_files_checked','working_tree_clean']}));print(json.dumps(package))
