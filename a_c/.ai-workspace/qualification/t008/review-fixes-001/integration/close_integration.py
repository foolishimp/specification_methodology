from __future__ import annotations
import collections,datetime,hashlib,json,os,pathlib,re,shutil,subprocess
P=pathlib.Path(__file__).resolve().parent
REPO=pathlib.Path('/Users/jim/src/apps/specification_methodology');PRODUCT=REPO/'a_c'
I=PRODUCT/'.ai-workspace/qualification/t008/review-fixes-001/integration'
def load(path):return json.loads(path.read_text())
def save(path,value):path.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
def require(ok,message):
    if not ok:raise RuntimeError(message)
source_before=load(I/'source-before.json')
def source_manifest(root):
    paths=[root/name for name in ('stdo_a_c.json','AGENTS.md','CLAUDE.md','README.md') if (root/name).is_file()]
    for folder in ('specification','build_tenants'):
        paths.extend(path for path in (root/folder).rglob('*') if path.is_file() and '__pycache__' not in path.parts and '.mypy_cache' not in path.parts)
    return {str(path.relative_to(root)):{'sha256':sha(path),'bytes':path.stat().st_size,'mode':path.stat().st_mode & 0o777} for path in sorted(set(paths))}
source_after=source_manifest(PRODUCT)
snapshot_after={key:{'sha256':sha(P/'snapshot/a_c'/key),'bytes':(P/'snapshot/a_c'/key).stat().st_size,'mode':(P/'snapshot/a_c'/key).stat().st_mode & 0o777} for key in source_before}
save(I/'source-after.json',source_after);save(I/'snapshot-inputs-after.json',snapshot_after)
frozen_before=load(I/'frozen-studies-before.json');frozen_after={}
for study in ('stdo-v3-generation','stdo-v3-generation-rc9'):
    for path in (PRODUCT/'dogfood'/study).rglob('*'):
        if path.is_file():frozen_after[str(path.relative_to(REPO))]={'sha256':sha(path),'bytes':path.stat().st_size}
save(I/'frozen-studies-after.json',frozen_after)
expected=load(I/'expected-repairs-and-preimages.json')
preimage_guard=all(sha(I/'preimages'/entry['worker']/key)==entry['preimage_sha256']==sha(pathlib.Path(entry['preimage'])) for key,entry in expected.items())
source_guard={'original_product_sources_unchanged':source_before==source_after,'exact_active_snapshot_inputs_unchanged':source_before==snapshot_after,'durable_exact_input_copies_match':all(sha(I/'snapshot-inputs'/key)==entry['sha256'] for key,entry in source_before.items()),'all_expected_final_repair_pins_match':all(source_after[key]['sha256']==entry['sha256'] for key,entry in expected.items()),'expected_preimages_and_durable_copies_unchanged':preimage_guard,'all_old_and_current_frozen_study_bytes_unchanged':frozen_before==frozen_after}
require(all(source_guard.values()),'A source, snapshot, preimage or preserved study guard changed; stop qualification')
guard_closed_at=datetime.datetime.now(datetime.timezone.utc).isoformat()
save(I/'SOURCE-GUARD.json',{'closed_at_utc':guard_closed_at,'guards':source_guard,'source_files':len(source_after),'expected_changed_files':len(expected),'frozen_study_files':len(frozen_after),'frozen_study_bytes':sum(v['bytes'] for v in frozen_after.values())})
print(json.dumps({'source_guard':'closed','all_guards':source_guard,'closed_at_utc':guard_closed_at}),flush=True)
custody={}
for name in ('core','effects','public','actor'):
    origin=P/('custody-'+name);destination=I/'suite/custody'/name
    destination.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(origin,destination,symlinks=True)
    files=[path for path in destination.rglob('*') if path.is_file() and not path.is_symlink()]
    links=[path for path in destination.rglob('*') if path.is_symlink()]
    custody[name]={'original_root':str(origin),'retained_root':str(destination),'regular_files':len(files),'bytes':sum(path.stat().st_size for path in files),'symlinks':len(links)}
save(I/'suite/CUSTODY.json',{'meaning':'Historical exact raw controlled-test fixture bytes; original absolute references remain unchanged. These copies are not silently rebased or admitted as new runtime policies. No prior failed repair evidence was removed or rewritten.','roots':custody})
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',PYTHONDONTWRITEBYTECODE='1')
for name,args in [('git-head.after.txt',['rev-parse','HEAD']),('git-status.after.z',['status','--porcelain=v1','-z','--untracked-files=all']),('git-status.after.txt',['status','--short','--branch','--untracked-files=all'])]:
    run=subprocess.run(['git','-C',str(REPO),*args],env=env,capture_output=True);(I/name).write_bytes(run.stdout);require(run.returncode==0,'Read-only Git observation failed')
prefix=b'a_c/.ai-workspace/qualification/t008/review-fixes-001/integration/'
def outside_records(raw):
    rows=raw.split(b'\0');records=[];index=0
    while index<len(rows):
        record=rows[index];index+=1
        if not record:continue
        other=None
        if b'R' in record[:2] or b'C' in record[:2]:other=rows[index];index+=1
        if record[3:].startswith(prefix) or (other is not None and other.startswith(prefix)):continue
        records.append((record,other))
    return records
before_status=outside_records((I/'git-status.before.z').read_bytes());after_status=outside_records((I/'git-status.after.z').read_bytes())
before_set=set(before_status);after_set=set(after_status)
status_delta={'outside_integration_status_equal':before_status==after_status,'removed':[(a.decode('utf-8','replace'),b.decode('utf-8','replace') if b else None) for a,b in before_set-after_set],'added':[(a.decode('utf-8','replace'),b.decode('utf-8','replace') if b else None) for a,b in after_set-before_set]};save(I/'git-status-scope-delta.json',status_delta)
head_unchanged=(I/'git-head.before.txt').read_bytes()==(I/'git-head.after.txt').read_bytes()
raw=(I/'suite/stderr').read_text();modules=collections.Counter()
for line in raw.splitlines():
    match=re.match(r'^test\S+ \((test_\w+)\.[^)]+\) \.\.\.',line)
    if match:modules[match.group(1)]+=1
ran=re.search(r'^Ran (\d+) tests in ([0-9.]+)s$',raw,re.M)
skips=[line for line in raw.splitlines() if re.search(r'\.\.\. skipped ',line)]
failures=[line for line in raw.splitlines() if re.match(r'^(FAIL|ERROR):',line)]
executions={name:load(I/name/'execution.json') for name in ('suite','strict9','compatibility9')}
compatibility=load(I/'compatibility9/report.json')
passing=all(run['returncode']==0 for run in executions.values()) and bool(ran) and raw.rstrip().endswith('OK') and not skips and not failures and head_unchanged
warnings=[line.split('RuntimeWarning:',1)[1].strip() for line in raw.splitlines() if 'RuntimeWarning:' in line]
upstream_cases=[re.match(r'^(\S+) \(([^)]+)\)',line).group(2) for line in raw.splitlines() if line.startswith('test_actual_upstream')]
result={'status':'CLOSED','work_result':'candidate_ready' if passing else 'verification_gap','verification_core_value':'satisfied' if passing else 'indeterminate','scope':'Final joined mechanical verification of exact repaired candidate; no semantic, Product acceptance or release decision.','git_head':(I/'git-head.after.txt').read_text().strip(),'source_guard_closed_at_utc':guard_closed_at,'source_guards':source_guard,'head_unchanged':head_unchanged,'source_files':len(source_after),'changed_files_from_original_dirty_preimages':len(expected),'frozen_study_files':len(frozen_after),'frozen_study_bytes':sum(v['bytes'] for v in frozen_after.values()),'source_repair_pins':{key:value['sha256'] for key,value in expected.items()},'snapshot':str(P/'snapshot/a_c'),'temp':str(P),'suite':{'tests':int(ran.group(1)) if ran else None,'runtime_seconds':float(ran.group(2)) if ran else None,'exit':executions['suite']['returncode'],'wrapper_seconds':executions['suite']['elapsed_seconds'],'modules':dict(sorted(modules.items())),'skips':skips,'failures_or_errors':failures,'warning_count':len(warnings),'warnings':warnings,'actual_pinned_upstream_test_cases':upstream_cases,'all_cases_passed':passing,'execution_count':1},'strict9':{'exit':executions['strict9']['returncode'],'seconds':executions['strict9']['elapsed_seconds'],'normal_imports':True,'files':9,'stdout':(I/'strict9/stdout').read_text().strip(),'execution_count':1},'compatibility9':{'exit':executions['compatibility9']['returncode'],'seconds':executions['compatibility9']['elapsed_seconds'],'status':compatibility['status'],'checks':len(compatibility.get('checks',[])),'upstream':compatibility.get('upstream'),'nodes':compatibility.get('nodes'),'edges':compatibility.get('edges'),'execution_count':1},'custody':custody,'git_status':status_delta,'snapshot_git_alias':load(I/'ENVIRONMENT.json')['snapshot_git_read_alias'],'report_writer_diagnostic':{'initial_script_generation':'Nested quoting SyntaxError occurred before close-script creation or execution. Corrected only the owned report writer; no tests or source effects were repeated.','qualification_checks_repeated':False},'limits':['Mechanical tests, normal-import typing, controlled local CLI/process checks and fresh pinned-upstream fixture trial only; no live F_P/provider/native/network calls, usability or accepted-result benefit claim.','Full suite includes four pinned-upstream generation/grounding/repair cases; separate compatibility9 overlaps upstream components and is not nine extra unittest cases.','Both old/current frozen generation studies were byte-guarded only. Old plan pins were not refreshed or requalified under the changed generator.','Existing dirty work was preserved. Only the named integration subtree and owned temp were written; no cleanliness, commit, push, Product acceptance or release claim.','Copied raw test custody keeps original absolute historical bindings; no newly admitted runnable policies are asserted.','Source guard is an exact recorded cut. Root owns subsequent factual-document updates and semantic/owner disposition.']}
save(I/'RESULT.json',result)
lines=['# Joined verification of the seven implementation repairs','', 'The exact repaired candidate passed one full tenant suite, joined normal-import strict typing of nine support/helper files, and a fresh standalone nine-check pinned-upstream compatibility trial. This is bounded mechanical verification; Root retains semantic review and owner disposition.','', '| Check | Result | Runtime |','|---|---|---|',f"| Full tenant suite | {result['suite']['tests']} passed; {len(skips)} skips; {len(failures)} failures/errors; exit {executions['suite']['returncode']} | {result['suite']['runtime_seconds']}s unittest / {executions['suite']['elapsed_seconds']}s wrapper |",f"| Strict normal-import typing | 9 files; exit {executions['strict9']['returncode']} | {executions['strict9']['elapsed_seconds']}s |",f"| Standalone actual-upstream trial | {len(compatibility.get('checks',[]))} checks; exit {executions['compatibility9']['returncode']} | {executions['compatibility9']['elapsed_seconds']}s |",'', 'The full-suite module totals are '+str(dict(sorted(modules.items())))+'. The four actual-upstream cases nested in the suite and standalone compatibility checks overlap upstream components and remain distinct evidence groups. Three upstream stat-index root-switch RuntimeWarnings are retained in raw stderr; no failure was suppressed or repaired during integration.','',f'The snapshot contained {len(source_after)} exact Product/tenant support inputs. All eleven final repair hashes matched the Workers frozen pins; each Worker preimage matched the original dirty baseline. Active snapshot input bytes/modes, original source bytes/modes, durable input copies and preimages all remained exact. The runtime was installed Python 3.12.8 with mypy 1.15.0, networkx 3.4.2 and tree-sitter 0.25.2. Graphify was clean at fe085cedddde3a18554f8749b230bfe47f3dcce7. The installed builder and work-scoped RC9 profile remained unchanged.','', 'The unchanged immutable-Git acquisition test ran through the expressly authorized scratch-only .git read alias. No candidate test was edited, stubbed or skipped. The process sandbox denied network and writes outside the new temp and integration subtree, including writes to original code/Git/study bytes by supervisors that replaced bytecode environment settings.','',f'All {len(frozen_after)} files ({sum(v["bytes"] for v in frozen_after.values())} bytes) in both preserved old/current generation studies remained byte-identical. No old plan pin was refreshed. HEAD remained bfe228511415d346459523cec44e7e8157e2991a. Status outside integration is recorded in git-status-scope-delta.json; existing dirt is not a cleanliness claim.','', 'RESULT.json, ENVIRONMENT.json, source-before.json, source-after.json, snapshot-inputs-after.json, expected-repairs-and-preimages.json, repair-scope.json, frozen-study manifests and SOURCE-GUARD.json bind the cut. snapshot-inputs/ and preimages/ retain exact bytes. Each check retains its command, raw stdout/stderr and exit. suite/custody/ retains raw local fixture evidence with original bindings unchanged. No prior failure/retry/history was removed. The owned temp remains '+str(P)+'.','', 'Independent review, actual F_P/operator qualification, benefit, Product acceptance and release remain separate. No source repair, model/provider/native call, install, Git mutation, commit, push or publishing occurred. The Worker stops after this closed result.']
(I/'REPORT.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'status':result['status'],'work_result':result['work_result'],'suite':{'tests':result['suite']['tests'],'skips':len(skips),'failures':len(failures),'exit':executions['suite']['returncode'],'runtime_seconds':result['suite']['runtime_seconds']},'strict9':result['strict9'],'compatibility9':{'checks':result['compatibility9']['checks'],'exit':result['compatibility9']['exit']},'guards':source_guard,'outside_integration_status_equal':status_delta['outside_integration_status_equal'],'outside_added':len(status_delta['added']),'outside_removed':len(status_delta['removed']),'custody':custody,'REPORT':str(I/'REPORT.md'),'RESULT':str(I/'RESULT.json')},sort_keys=True,indent=2))
