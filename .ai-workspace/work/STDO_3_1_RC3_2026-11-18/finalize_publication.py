from pathlib import Path
import json,hashlib,re,subprocess
w=Path(__file__).resolve().parent;r=w.parents[2];tool=r/'releases/3.1.0-rc.3/tools';a=w/'assessment/identity-01'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def run(name,args):
 p=subprocess.run(list(map(str,args)),cwd=r,capture_output=True);(w/(name+'.stdout')).write_bytes(p.stdout);(w/(name+'.stderr')).write_bytes(p.stderr);save(w/(name+'_COMMAND.json'),{'argv':list(map(str,args)),'exit':p.returncode});print(name,p.returncode,flush=True);p.check_returncode();return p
assert read(a/'EXECUTION.json')['exit_code']==0
report=(a/'ASSESSMENT.md').read_text();j=next(json.loads(x) for x in re.findall(r'```json\s*(.*?)\s*```',report,re.S) if json.loads(x).get('kind')=='stdo.rc3-identity-assessment/1');s=read(w/'SOURCE_CARRIER.json');assert j['result']=='satisfied' and j['carrier']==s['carrier'] and j['native']==s['native']
for row in read(a/'FREEZE.json')['files']:assert sha(Path(row['path']))==row['sha256'],row['path']
q=read(w/'PREPUBLICATION_QUALIFICATION.json')
for row in q['qualified_files']:assert sha(Path(row['path']))==row['sha256'],row['path']
q['identity_readback_supplement']=read(w/'IDENTITY_READBACK_SUPPLEMENT.json')
q['qualified_files'] += [{'path':str(p),'sha256':sha(p)} for p in [w/'IDENTITY_READBACK_SUPPLEMENT.json',w/'assessment/native-01/ASSESSMENT.md',w/'assessment/native-01/stdout.jsonl',w/'assessment/semantic-02/ASSESSMENT.md',w/'assessment/semantic-02/stdout.jsonl']]
q['identity_assessment']={'result':j['result'],'report':str(a/'ASSESSMENT.md'),'report_sha256':sha(a/'ASSESSMENT.md'),'scope':j.get('scope'),'independence':'Claude review independent of Codex construction; not earlier Claude-family architecture direction.'};q['qualified_files'] += [{'path':str(p),'sha256':sha(p)} for p in [a/'ASSESSMENT.md',a/'EXECUTION.json',a/'FREEZE.json',w/'TAG_INTERNAL_READBACK.json',w/'REF_PLAN.json']];q['limits'][0]='Finite declared native, context, visual, package and local ref identity claims; public installation is the separate mandatory postpublication gate.';save(w/'FINAL_QUALIFICATION.json',q)
cohort=w/'assets/cohort-release-v3.1.0-rc.3.json';run('FINAL_COHORT',['python3','-B',tool/'cohort_record.py','--root',r,'--work',w,'--plan',w/'REF_PLAN.json','--qualification',w/'FINAL_QUALIFICATION.json','--out',cohort,'--carrier',s['carrier']])
draft=read(w/'COHORT_DRAFT.json');final=read(cohort);assert {k:v for k,v in draft.items() if k!='qualification'}=={k:v for k,v in final.items() if k!='qualification'}
selection=read(r/'releases/3.1.0-rc.3/COHORT_INPUTS.json');assets=[{'name':n,'bytes':(w/'assets'/n).stat().st_size,'sha256':sha(w/'assets'/n)} for n in selection['assets']];assert len(assets)==6;save(w/'EXPECTED_ASSETS.json',{'kind':'stdo.expected-public-assets/1','version':'3.1.0-rc.3','assets':assets})
run('FINAL_REF_CHECK',['python3','-B',tool/'ref_transaction.py','check','--root',r,'--plan',w/'REF_PLAN.json','--result',w/'FINAL_REF_CHECK.json'])
extra=[w/'FINAL_QUALIFICATION.json',cohort,w/'EXPECTED_ASSETS.json',w/'GITHUB_RELEASE_NOTES.md',Path(__file__)]
gate={'kind':'stdo.final-prepush-gate/1','result':'satisfied-for-declared-publication','carrier':s['carrier'],'native':s['native'],'ref_graph_sha256':final['ref_graph_sha256'],'identity_verdict':j,'metadata_only_cohort_change':True,'qualified_files':q['qualified_files']+[{'path':str(p),'sha256':sha(p)} for p in extra],'public_verification':'Required after publication; not yet performed.'};save(w/'FINAL_PREPUSH_GATE.json',gate)
for row in gate['qualified_files']:assert sha(Path(row['path']))==row['sha256'],row['path']
run('REF_PUBLISH',['python3','-B',tool/'ref_transaction.py','publish','--root',r,'--plan',w/'REF_PLAN.json','--result',w/'REF_PUBLISH.json'])
# Owner approval explicitly includes publication. Exact six assets and retained notes.
run('GITHUB_CREATE',['gh','release','create','specification_methodology/v3.1.0-rc.3',*[w/'assets'/row['name'] for row in assets],'--verify-tag','--title','STDO 3.1.0 (RC3)','--notes-file',w/'GITHUB_RELEASE_NOTES.md','--latest'])
p=run('GITHUB_READ',['gh','api','repos/foolishimp/specification_methodology/releases/tags/specification_methodology%2Fv3.1.0-rc.3']);release=json.loads(p.stdout);assert not release['draft'] and not release['prerelease'];save(w/'GITHUB_RELEASE.json',release);print(json.dumps({'published':True,'id':release['id'],'url':release['html_url'],'assets':len(release['assets'])}),flush=True)
