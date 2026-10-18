from pathlib import Path
import datetime, hashlib, json, os, subprocess, tempfile, time
ROOT=Path('/Users/jim/src/apps/specification_methodology')
EVIDENCE=ROOT/'a_c/.ai-workspace/qualification/t008/upstream'
PIN='fe085cedddde3a18554f8749b230bfe47f3dcce7'
URL='https://github.com/Graphify-Labs/graphify.git'
TEMP=Path(tempfile.mkdtemp(prefix='ac-graphify-t008-upstream-')).resolve()
CHECKOUT=TEMP/'checkout'
(TEMP/'gitconfig').write_text('')
(TEMP/'empty-template').mkdir()
OVERRIDES={'GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':str(TEMP/'gitconfig'),'GIT_TERMINAL_PROMPT':'0','PYTHONDONTWRITEBYTECODE':'1'}
ENV={**os.environ,**OVERRIDES}
STATE={'activation':'T-008-upstream-001','upstream_url':URL,'required_commit':PIN,'temporary_root':str(TEMP),'checkout':str(CHECKOUT),'environment_overrides':OVERRIDES,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'steps':[],'old_incomplete_checkout':'preserved, untouched'}
def save():
    (EVIDENCE/'acquisition.json').write_text(json.dumps(STATE,sort_keys=True,indent=2)+'\n')
def run(name,argv,timeout=180):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock=time.monotonic()
    try:
        p=subprocess.run(argv,cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
        code=p.returncode; out=p.stdout; err=p.stderr; expired=False
    except subprocess.TimeoutExpired as e:
        code=None; out=e.stdout or b''; err=e.stderr or b''; expired=True
    (EVIDENCE/(name+'.stdout')).write_bytes(out)
    (EVIDENCE/(name+'.stderr')).write_bytes(err)
    record={'name':name,'argv':argv,'cwd':str(ROOT),'environment_overrides':OVERRIDES,'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-clock,'returncode':code,'timeout':expired,'stdout':name+'.stdout','stderr':name+'.stderr','stdout_sha256':hashlib.sha256(out).hexdigest(),'stderr_sha256':hashlib.sha256(err).hexdigest()}
    STATE['steps'].append(record); save()
    print(json.dumps({'step':name,'returncode':code,'timeout':expired,'checkout':str(CHECKOUT)}),flush=True)
    if code!=0:
        raise SystemExit(2)
    return out.decode('utf-8').strip()
save()
run('01-clone',['git','-c','core.hooksPath=/dev/null','-c','submodule.recurse=false','clone','--no-checkout','--depth','1','--template='+str(TEMP/'empty-template'),URL,str(CHECKOUT)])
run('02-fetch-pin',['git','-C',str(CHECKOUT),'-c','core.hooksPath=/dev/null','fetch','--depth','1','origin',PIN])
run('03-checkout-pin',['git','-C',str(CHECKOUT),'-c','core.hooksPath=/dev/null','checkout','--detach',PIN])
head=run('04-head',['git','-C',str(CHECKOUT),'rev-parse','HEAD'])
status=run('05-status',['git','-C',str(CHECKOUT),'status','--porcelain=v1','--untracked-files=all'])
tree=run('06-tree',['git','-C',str(CHECKOUT),'rev-parse','HEAD^{tree}'])
remote=run('07-remote',['git','-C',str(CHECKOUT),'remote','get-url','origin'])
STATE.update({'head':head,'tree':tree,'status_porcelain':status,'origin_url':remote,'exact_clean_checkout':head==PIN and status=='','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
save()
if not STATE['exact_clean_checkout']:
    raise SystemExit(2)
print(json.dumps({'status':'acquired','head':head,'tree':tree,'checkout':str(CHECKOUT)}),flush=True)
