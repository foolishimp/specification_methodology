from pathlib import Path
import json,hashlib,stat,time
R=Path('/Users/jim/src/apps/specification_methodology');D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY';P=D/'public-qualification-001';O=Path(__file__).parent
refs={}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def get(p,h=None):
 p=Path(p);p=p if p.is_absolute() else R/p;raw=p.read_bytes()
 if h:assert sha(raw)==h,str(p)
 refs[str(p)]={'path':str(p),'sha256':sha(raw),'bytes':len(raw)};return json.loads(raw)
def ref(r):
 d=get(r['path'],r['sha256']);p=Path(r['path']);p=p if p.is_absolute() else R/p;assert refs[str(p)]['bytes']==r['bytes'];return d
def digestfile(p):
 h=hashlib.sha256()
 with p.open('rb')as stream:
  for b in iter(lambda:stream.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
start=time.time_ns()
h=get(P/'HANDOFF.json','7a135d31f453f6352e182b13ae376134f34a38412d42ecefa6babb7f52db944e')
a=ref(h['installed_byte_attestation']);m=ref(h['installed_native_manifest']);external=ref(h['external_manifest']);assets=ref(h['assets'])
assert h['transport_mode']=='public_readback' and assets['unauthenticated'] is True and len(assets['assets'])==5
for receipt in assets['assets']:
 d=ref(receipt);assert d['http_status']==200 and d['unauthenticated'] and not d['authorization_header_present'] and not d['cookie_header_present'];assert d['expected']['sha256']==d['body']['sha256'] and d['expected']['bytes']==d['body']['bytes']
assert h['native_commit']==m['release']['commit']=='d1f13c53ab733a73993615498f66251041a74073'
assert h['native_tag_object']==m['release']['tag_object']=='8eccce113086a15a042580c4c4158eea96ec17e2'
assert h['native_root_tree']==m['release']['tree']=='9e139bf53fbfea5594317436d64ae539db367c42'
assert h['source_package_tree']==m['release']['project_subtree_tree']=='e65f9e879d0695e75fb617e6226ef4fcaacd6c4a'
assert h['native_manifest']['sha256']==external['native']['manifest']['sha256']==h['installed_native_manifest']['sha256']=='9304727d370ae58a0b955d1f831ee15e8dddeb2ca3e8886454233a8422846142'
inv=get(D/'cohort-recovery-020/NATIVE_INPUT_INVENTORY.json')['files'];expected={r['path']:{'sha256':r['sha256'],'bytes':r['bytes']}for r in inv};expected['manifest.json']={'sha256':h['native_manifest']['sha256'],'bytes':h['native_manifest']['bytes']}
assert len(expected)==172 and {r['installed_path']:{k:r[k]for k in ('sha256','bytes')}for r in a['members']}==expected
native=Path(h['native_root']);observed=[]
for row in a['members']:
 q=Path(row['path']);assert q==native/row['installed_path'];s=q.lstat();assert stat.S_ISREG(s.st_mode) and s.st_size==row['bytes'] and oct(stat.S_IMODE(s.st_mode))==row['mode'] and s.st_mtime_ns==row['mtime_ns'];assert digestfile(q)==row['sha256'];observed.append(row)
paths=list(native.rglob('*'));assert not any(p.is_symlink() for p in paths);assert {p.relative_to(native).as_posix() for p in paths if p.is_file()}==set(expected)
verify=ref(h['verify']);v=ref(verify['stdout']);assert verify['returncode']==0 and v['valid'] is True and v['failures']==[] and v['manifest']==m and v['manifest_sha256']==h['native_manifest']['sha256'] and v['path']==str(native)
assert verify['argv']==[h['manager']['manager']['path'],'--store',h['store'],'verify','v3.0.5','--manifest-sha256',h['native_manifest']['sha256']]
reconciliation=ref(h['operator_reconciliation']);assert reconciliation['no_install_or_verify_rerun'] and reconciliation['actual_verify']['sha256']==verify['stdout']['sha256'];ref(reconciliation['original_stop'])
source=ref(h['manager']['source_match']);identities=ref(h['manager']['identities']);assert source['version']==identities['manager_version']=='3.0.5';assert {x['name']:x['version']for x in identities['dependencies']}==h['manager']['selected_distribution_population']
assert len(source['members'])==13
for name,digest in source['members'].items():assert digestfile(Path(source['site'])/name)==digest
assert digestfile(Path(h['manager']['manager']['path']))==h['manager']['manager']['sha256']
ready=get(P/'MATERIALIZATION_CHECK.json','474f9c294452ba4daf68a1af90bc2618ddf8f431934d1271400c33f35abe48c4')
obs=get(O/'browser-public001/OBSERVATION.json','29ea11e788c2252bc1796d693d6152bd26d6ab0188d6d239108d6cf3488e099c')
assert obs['status']=='observed' and obs['owned_browser_closed'] and not obs['errors'] and not obs['blocked_requests'] and not obs['request_failures']
assert set(obs['observations'])=={'3d','2d','layered','source','files'} and all(x['observed'] for x in obs['observations'].values())
assert obs['page']['path']==str(Path(h['workspace'])/'source-tools/stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/explorer.html')
assert all(obs['pages_unchanged_after'].values()) and all(r['url'].startswith('file://') for r in obs['network_requests'])
screens=[]
for x in list(obs['observations'].values())+obs['documentation_observations']:
 if 'screenshot'in x:
  pin=x['screenshot'];q=Path(pin['path']);assert q.stat().st_size==pin['bytes'] and digestfile(q)==pin['sha256'];screens.append(pin)
assert len(screens)==9
for row in a['members']:
 s=Path(row['path']).lstat();assert s.st_size==row['bytes'] and s.st_mtime_ns==row['mtime_ns'] and oct(stat.S_IMODE(s.st_mode))==row['mode']
for r in list(refs.values()):assert digestfile(Path(r['path']))==r['sha256']
report={'kind':'stdo.independent-public-native-browser-review/1','assessor':'/root/stdo305_integration_review','authors':['/root/stdo305_release_tools','/root/stdo305_tools_skills','/root/stdo305_representation'],'conclusion':'satisfied_within_public_native_and_browser_scope','findings':[],'open_required_findings':[],'source_checkpoint':h['source_checkpoint'],'published_carrier':h['carrier'],'release_id':h['release_id'],'external_manifest_sha256':h['external_manifest']['sha256'],'native_commit':h['native_commit'],'native_tag_object':h['native_tag_object'],'native_manifest_sha256':h['native_manifest']['sha256'],'actual_workspace':h['workspace'],'checks':['Actual published native manifest and complete172-file ordinary population independently match the previously reviewed exact171 native input inventory plus manifest. Byte hashes, modes, mtimes and no-extra/no-symlink population agree with the public install attestation.','Actual public verify receipt uses the explicit public001 manager/store and reports valid=true, failures=[], exact native manifest and root. The operator status-key assertion failure is preserved and reconciled against this unchanged actual result; no install/verify rerun by this Reviewer.','All13 installed manager source hashes and declared21-distribution metadata agree with the exact selected public manager binding. Anonymous acquisition receipts for five assets preserve HTTP200/no-auth/no-cookie and expected identities; no new HTTP download performed by Reviewer.','Fresh actual public001 mapped explorer observed offline through3D, visible2D labels, Layered, source passage, source-file navigation and back/selection continuity.','Installed documentation landing reaches current native explorer and proofreader. Actual selected result theorem, lexical AC.project link, Back and complete current source line were followed. Nine retained screenshots visually inspected.','Only five file:// document requests observed; no page/console/blocked/request failure, all four page hashes unchanged. Isolated browser context closed before report sealing.','Independent source pages/native checks and all selected small record references stable after observation; no source/repository/native writes.'],'raw_browser_observation':refs[str(O/'browser-public001/OBSERVATION.json')],'screenshots':screens,'browser':obs['browser'],'elapsed_browser_seconds':obs['elapsed_seconds'],'owned_browser_closed':True,'limits':['Public runtime establishment, installed full Lean result, complete public aggregate gate, Latest and final public readback are separate pending claims, not established by this report.','No new Lean/compiler/support scan, native LLM actor, semantic review or model regeneration. Source021/accepted local evidence remain their original subjects.','Browser behavior is this finite fresh Chrome156/Playwright file observation, not all browsers/platforms or general accessibility/host isolation. Page requests are observed; OS background traffic is not packet-captured.','No private credentials or global browser configuration inspected/changed. Scratch outputs only.'],'started_ns':start,'finished_ns':time.time_ns(),'references':list(refs.values())}
out=O/'PUBLIC_NATIVE_BROWSER_REVIEW.json';out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'path':str(out),'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'conclusion':report['conclusion'],'screenshots':len(screens),'native_files':len(observed),'references':len(refs)},indent=2))
