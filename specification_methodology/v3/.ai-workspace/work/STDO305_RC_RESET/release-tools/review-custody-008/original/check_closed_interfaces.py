from pathlib import Path
import hashlib,json
R=Path('/Users/jim/src/apps/specification_methodology');D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET';Q=D/'tools-skills/installed-qualification-002';B=D/'release-tools/cohort-002';O=Path(__file__).parent
checked={};large=[]
def raw(ref):
 p=Path(ref['path']);p=p if p.is_absolute() else R/p
 b=p.read_bytes();assert len(b)==ref['bytes'] and hashlib.sha256(b).hexdigest()==ref['sha256'],str(p)
 checked[str(p)]={'path':str(p),'sha256':ref['sha256'],'bytes':len(b)};return b
def get(ref):return json.loads(raw(ref))
def pinfile(p,h):
 b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==h;checked[str(p)]={'path':str(p),'sha256':h,'bytes':len(b)};return json.loads(b)
c=pinfile(Q/'CLOSED_INTERFACES.json','5b52116a5337d27ff1df7fb85540b16eaae845fe593a5199d79b1c3b89705be0')
records={}
for row in c['records']:
 w=get(row['execution']);e=w['execution'];assert e['returncode']==0 and e['elapsed_seconds']>0
 for x in e['inputs']+e['outputs']+[e['stdout'],e['stderr']]:
  if x['bytes']<=8*1024*1024:raw(x)
  else:large.append(x)
 raw(row['result']);records[row['operation']]=w
for x in c['selected']:raw(x)
assert len(records)==19 and 'installed-full-current-verify' not in records
basis={'uri':'stdo://releases/v3.0.5-rc.1/','manifest_sha256':'64c026667abba933d289317793dbe80b5f9ab822a9870307795584402e460e1c'}
W=Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/local-002')
for host,refs in c['hosts'].items():
 cfg=get(refs['configuration']);receipt=get(refs['receipt']);setup=get(refs['setup']);policy=get(refs['policy']);method=get(refs['method_verification']);raw(refs['stdin'])
 assert cfg['basis']==basis and cfg['ac_root']==str(W/'runtime/a_c') and cfg['method_root']==str(W/'store/releases/v3.0.5-rc.1')
 launch=cfg['manager_identity']['runtime_launcher'];assert launch['store']==str(W/'store') and launch['manifest_sha256']==basis['manifest_sha256'];assert launch['manager']==str(W/'manager/bin/stdo')
 assert hashlib.sha256(Path(cfg['stdo']).read_bytes()).hexdigest()==launch['sha256']
 anchor=json.loads(Path(cfg['definition']).read_bytes());assert anchor['constitution']['stdo']['selector']=='stdo://channels/3.0.5' and anchor['constitution']['stdo']['basis']==basis
 assert anchor['$schema']==basis['uri']+'standards/schemas/product-definition.schema.json'
 assert method['basis']==basis['uri'] and method['manifest_sha256']==basis['manifest_sha256'] and method['valid'] is True and method['failures']==[]
 runtime=get(next(x['result'] for x in c['records'] if x['operation']==host+'-check-runtime'));assert runtime['status']=='verified' and runtime['configuration']==cfg
 initialized=get(next(x['result'] for x in c['records'] if x['operation']==host+'-early-initializer'));assert initialized['Product_work_grants']==initialized['model_calls']==initialized['registered_executors']==0
 replies=get(next(x['result'] for x in c['records'] if x['operation']=='codex-early-mcp'))
 assert replies[0]['result']['serverInfo']['version']=='3.0.5-rc.1'
 assert 'source.read' in [t['name'] for t in replies[1]['result']['tools']]
 v=replies[2]['result']['structuredContent'];assert replies[2]['result']['isError'] is False and v['operation']=='source.read' and v['refusal'] is None
 content=v['result']['value'];native=(W/'anchors/codex/stdo_runtime.json').read_bytes();assert content['content'].encode()==native and hashlib.sha256(native).hexdigest()==content['selected_sha256']==content['source']['sha256']
der=get(next(x for x in c['selected'] if x['path'].endswith('observed/runtime/bootstrap/derivation.json')));assert der['status']=='support-established' and der['source_identity_sha256']=='c0f3bd303d4c107a0f2483c3ad6b4d201ac6363869bfd9b2b38a4378f22bdb06';assert der['profile_sha256']=='f35dcd22b148938f3d53690058cca3a77151bd90cf4da0c1d7ed60c31a2efec7'
assert der['allowed_source_delta']=='build_tenants/lean/profiles/proof-support-v1.json' and der['predecessor']['sha256']=='97564a106ef25ca5b9d8e913cfad30d8d7edb511463afb8dda145725f5c74782'
g=get(next(x['result'] for x in c['records'] if x['operation']=='actual-upstream-roundtrip'));assert g['status']=='verified' and g['model']['raw_sha256']=='b40ecc595d1a58ad96a9ba0be4942e015123224adee1832a58a6c3b53f21eeb7';assert g['upstream_trial']['decoded_model_sha256']==g['model']['canonical_sha256']=='6be53084229a3e8552a4495b470a82844f62f9d2b7abcace6975dbe4e0066544';assert [x['budget_records'] for x in g['selections']]==[21,17,11,5,15]
f=pinfile(B/'CLOSED_BINDINGS_002.json','0165147c47e92482f7b7d13d5a72ce027cd7ac71cd83a5f68f82c5381bc3c719');installed=get(f['installation']);assert installed['runtime_derivation']['sha256']=='535b2a95644aff301f344636d90ccf8b6629ca406eb54fb4e3a91f3246718475' and len(installed['files'])==429
assert installed['acquisition']['commit']=='b5b00b896d44804e0f5d615a9bc23a02345888b3' and installed['acquisition']['manifest_sha256']==basis['manifest_sha256']
execution_comparisons=[]
for claim,x in f['evidence'].items():
 w=get(x);assert w['claim']==claim and w['source_identity_sha256']==installed['source_identity_sha256']
 assert w.get('installation')==f['installation'];assert all(installed['subjects'][k]==v for k,v in w['subjects'].items())
 if 'original_execution' in w and 'execution' in w:
  old=get(w['original_execution']);e=old.get('execution',old)
  assert e==w['execution'],claim
  execution_comparisons.append(claim)
for row in checked.values():
 p=Path(row['path']);assert p.stat().st_size==row['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
result={'kind':'stdo.independent-closed-interface-join-check/1','assessor':'/root/stdo305_integration_review','status':'consistent','interfaces_sha256':checked[str(Q/'CLOSED_INTERFACES.json')]['sha256'],'bindings_sha256':checked[str(B/'CLOSED_BINDINGS_002.json')]['sha256'],'recorded_operations':list(records),'wrapper_execution_equal_to_original':execution_comparisons,'checked_metadata_refs':list(checked.values()),'large_refs_retained_without_new_rehash':large,'limits':['No support/runtime tree scan, kernel or actor execution. Current proof excluded until closed.','Cache metadata and fresh-support execution are distinct; no cached support verdict transferred.','Source-side wrapper executions remain source-side and retain exact original execution fields.']}
(O/'CLOSED_INTERFACES_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'consistent','operations':len(records),'metadata_refs':len(checked),'wrapper_execution_comparisons':execution_comparisons,'large_refs':len(large),'result_sha256':hashlib.sha256((O/'CLOSED_INTERFACES_CHECK.json').read_bytes()).hexdigest()}))
