"""Execute independent fresh use trials; each task and sandbox persists separately."""
from pathlib import Path
import argparse,concurrent.futures,subprocess,sys,json,time
q=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--directory',default='use');args=parser.parse_args()
directory=q/args.directory
if directory.resolve().parent!=q:raise ValueError('directory must be one synthesis child')
cases=sorted(p for p in directory.iterdir() if p.is_dir() and (p/'PROMPT.txt').is_file())
def run(p):
 started=time.monotonic()
 proc=subprocess.run([sys.executable,str(q/'run_actor.py'),str(p/'PROMPT.txt'),str(p/'actor')],capture_output=True,text=True)
 return {'case':p.name,'host_exit':proc.returncode,'elapsed_seconds':round(time.monotonic()-started,3),'summary':proc.stdout.strip(),'stderr':proc.stderr}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for f in concurrent.futures.as_completed([pool.submit(run,p) for p in cases]):
  row=f.result();rows.append(row);print(json.dumps(row),flush=True)
(directory/'EXECUTION.json').write_text(json.dumps({'actor_concurrency':3,'runs':sorted(rows,key=lambda r:r['case'])},indent=2)+'\n')
raise SystemExit(0 if all(r['host_exit']==0 for r in rows) else 1)
