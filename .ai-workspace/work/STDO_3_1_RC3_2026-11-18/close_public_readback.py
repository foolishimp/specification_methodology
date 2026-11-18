from pathlib import Path
import hashlib,json,subprocess
w=Path(__file__).resolve().parent;r=w.parents[2]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,j):p.write_text(json.dumps(j,indent=2)+'\n')
def git(*args):return subprocess.check_output(['git','-C',str(r),*args],text=True).strip()
def api(path):return json.loads(subprocess.check_output(['gh','api',path]))
public=read(w/'public-readback/RESULT.json');assert public['valid'];assets=read(w/'public-readback/ASSET_READBACK.json');assert assets['valid'] and len(assets['assets'])==6
remote=git('ls-remote','origin');(w/'REMOTE_AFTER.txt').write_text(remote+'\n');refs={line.split('\t')[1]:line.split('\t')[0] for line in remote.splitlines()};plan=read(w/'REF_PLAN.json')
for row in plan['refs']:assert refs[row['destination']]==row['object'],row['destination']
before={line.split('\t')[1]:line.split('\t')[0] for line in (w/'REMOTE_BEFORE.txt').read_text().splitlines()}
protected={name:obj for name,obj in before.items() if name.startswith('refs/tags/') and '-rc.' in name}
for name,obj in protected.items():assert refs[name]==obj,name
old=read(w/'RC2_PUBLIC_BEFORE.json');now=api('repos/foolishimp/specification_methodology/releases/445750557');save(w/'RC2_PUBLIC_AFTER.json',now)
identity=lambda j:{'id':j['id'],'tag':j['tag_name'],'draft':j['draft'],'prerelease':j['prerelease'],'body':j['body'],'assets':sorted([(a['id'],a['name'],a['size'],a['digest']) for a in j['assets']])}
assert identity(old)==identity(now)
latest=api('repos/foolishimp/specification_methodology/releases/latest');assert latest['id']==public['release_id'];save(w/'GITHUB_LATEST.json',latest)
primary=Path('/Users/jim/src/apps/specification_methodology');status=subprocess.check_output(['git','-C',str(primary),'status','--porcelain=v1','-z']);diff=subprocess.check_output(['git','-C',str(primary),'diff','--binary']);pri={'head':subprocess.check_output(['git','-C',str(primary),'rev-parse','HEAD'],text=True).strip(),'status_sha256':hashlib.sha256(status).hexdigest(),'tracked_diff_sha256':hashlib.sha256(diff).hexdigest()};prev=read(w/'PRIMARY_BEFORE_PUBLICATION.json');pri['same_as_prepublication_observation']=all(pri[k]==prev[k] for k in ['head','status_sha256','tracked_diff_sha256']);pri['writer_effects']='None in primary checkout; any concurrent primary changes remain outside this release worktree.';save(w/'PRIMARY_AFTER_PUBLICATION.json',pri)
cohort=read(w/'assets/cohort-release-v3.1.0-rc.3.json');source=read(w/'SOURCE_CARRIER.json');host=read(w/'public-readback/host-checks/RESULT.json');browser=read(w/'public-readback/visual-browser/RESULT.json');assert browser['status']=='passed';assert all(x['passed'] for x in host['operations'])
for name,h in host['hosts'].items():
 assert h['removed'] and all(x['covered'] for x in h['contexts'])
 assert all(x['covered'] for x in h['boundary_controls'] if x['case'] in ['acceptance','qualification','release','work','triage'])
closure={'kind':'stdo.public-release-closure/1','version':'3.1.0-rc.3','status':'published-and-public-install-verified','release_id':public['release_id'],'url':public['url'],'normal_latest_release':True,'native':source['native'],'source_carrier':source['carrier'],'native_manifest_sha256':public['native_manifest_sha256'],'cohort_sha256':sha(w/'assets/cohort-release-v3.1.0-rc.3.json'),'atomic_ref_count':len(plan['refs']),'public_assets':assets['assets'],'companion_members':226,'public_host_operations':len(host['operations']),'public_browser_checks':len(browser['checks']),'covered_queries_per_host':8,'prior_immutable_tag_objects_and_peels_preserved':len(protected),'rc2_release_assets_unchanged':True,'construction_basis':'stdo://releases/v3.0.4/','independent_reports':['assessment/native-02/ASSESSMENT.md','assessment/semantic-03/ASSESSMENT.md','assessment/identity-01/ASSESSMENT.md'],'limits':cohort['limits'],'consumer_adoption':False,'global_install_changed':False,'public_observation':'Anonymous six-asset acquisition with expected/GitHub digests; fresh isolated offline manager installation, native install from public Git, two host bindings and browser observations.'};save(w/'RESULT.json',closure);save(w/'PUBLIC_CLOSURE.json',closure)
(w/'RELEASED.md').write_text(f'''# STDO 3.1.0-rc.3 released

[Public release]({public['url']}) — GitHub release {public['release_id']}, normal
Latest, six assets. Native A `{source['native']}`; source carrier B
`{source['carrier']}`. Native manifest `{public['native_manifest_sha256']}`.

The method is self-contained. Tracking, needed fact preservation and reconciliation
to authoritative workspace truth remain required. The generic register is an
optional example, with equivalent mechanisms permitted. ODD does not impose a
runtime ledger/replay/API architecture. Product specifies the intended end state;
Goals hold current epics. Authority audits, semantic judgment and no-drift proof
obligations remain.

The leased atomic transaction published all 25 refs. Anonymous public acquisition
verified all six assets against expected and GitHub-advertised hashes. A fresh
isolated macOS arm64 CPython 3.13 environment installed the locked manager and
exact native cut from public Git. All 226 companion files matched the inventory;
{len(host['operations'])} public installed-host operations and {len(browser['checks'])} offline browser checks passed.
Eight exact queries on each host used actual independent support; unknown or
invalid inputs refused their dependent claims. Removal preserved unrelated files.

Native, exact-query semantic and identity assessments are retained under
assessment/. Original failed reviews and repairs remain. Source review is
Claude-family independent of Codex construction, not earlier Claude-family
architectural direction. Unchanged visual/constraint evidence is reused only
under recorded applicability. Scope is finite; no whole-method qualification,
arbitrary-query coverage, automatic host pickup, human exact-cut acceptance or
consumer adoption is claimed. Construction stays on STDO 3.0.4; global installs
remain unchanged. All {len(protected)} observed earlier immutable RC tag objects/peels and RC2
release asset identities are preserved. RESULT.json and public-readback/ contain
the actual observations and exact bindings.
''')
# Commit only new durable run evidence. Public downloads, venv/store and extracted
# source are reconstructible from exact public assets/refs and remain local.
names=[Path(x) for x in git('ls-files','-m','-o','--exclude-standard',str(w.relative_to(r))).splitlines()];selected=[]
for p in names:
 rel=p.relative_to(w.relative_to(r));parts=rel.parts
 if parts[0] in ['manager','manager-source','native-store','assets','assets-02','assets-03','attempts','packaged-products','packaged-products-02','packaged-products-03']:continue
 if len(parts)>1 and parts[0]=='public-readback' and parts[1] in ['assets','manager','runtime','products','store']:continue
 if '__pycache__' in parts or '.git' in parts or p.suffix=='.pyc':continue
 selected.append(str(p))
for start in range(0,len(selected),180):subprocess.run(['git','-C',str(r),'add','--',*selected[start:start+180]],check=True)
subprocess.run(['git','-C',str(r),'commit','-m','Retain STDO 3.1 RC3 publication and fresh public-install evidence'],check=True,stdout=subprocess.DEVNULL)
post=git('rev-parse','HEAD');p=subprocess.run(['git','-C',str(r),'push','--atomic','--force-with-lease=refs/heads/main:'+source['carrier'],'origin',post+':refs/heads/main'],capture_output=True);(w/'BOOKKEEPING_PUSH.stdout').write_bytes(p.stdout);(w/'BOOKKEEPING_PUSH.stderr').write_bytes(p.stderr);p.check_returncode()
after={x.split('\t')[1]:x.split('\t')[0] for x in git('ls-remote','origin').splitlines()};assert after['refs/heads/main']==post
for row in plan['refs']:
 if row['destination']!='refs/heads/main':assert after[row['destination']]==row['object']
for name,obj in protected.items():assert after[name]==obj
save(w/'BOOKKEEPING.json',{'postpublication_commit':post,'remote_main':after['refs/heads/main'],'source_carrier_preserved':source['carrier'],'release_refs_unchanged':24,'status':'pushed-and-read-back','standing':'Evidence-only postpublication source commit; released immutable tags still select original native A and carrier B.'});print(json.dumps({'published':public['url'],'postpublication_commit':post,'host_operations':len(host['operations']),'browser_checks':len(browser['checks']),'earlier_immutable_refs_preserved':len(protected)}),flush=True)
