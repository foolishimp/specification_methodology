"""Run one bounded fresh no-tool actor, preserving input/output and measured limits."""
import argparse, hashlib, json, subprocess, tempfile, time
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('prompt');p.add_argument('output');p.add_argument('--model',default='opus');p.add_argument('--budget',type=float,default=2);p.add_argument('--seconds',type=int,default=900);a=p.parse_args()
source=Path(a.prompt).resolve();out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=False)
b=source.read_bytes()
if len(b)>120000: raise SystemExit('Selected prompt exceeds declared input envelope')
(out/'PROMPT.txt').write_bytes(b)
argv=['claude','-p','--safe-mode','--restricted','--tools','','--permission-mode','dontAsk','--output-format','json','--no-session-persistence','--model',a.model,'--effort','high','--max-turns','1','--max-budget-usd',str(a.budget)]
r={'argv':argv,'prompt_sha256':hashlib.sha256(b).hexdigest(),'selected_input_bytes':len(b),'input_limit_bytes':120000,'wall_limit_seconds':a.seconds,'spend_limit_usd':a.budget,'tools':[],'standing':'bounded fresh-actor output, requires interpretation','limits':['Measured input excludes provider system prompts and hidden processing.','A fresh context alone is not proof of independent authorship.']}
start=time.monotonic()
with tempfile.TemporaryDirectory(prefix='stdo-v3-actor-',dir='/private/tmp') as cwd:
 r['cwd']=cwd
 try:
  proc=subprocess.run(argv,input=b,capture_output=True,cwd=cwd,timeout=a.seconds)
  (out/'PROVIDER.json').write_bytes(proc.stdout);(out/'STDERR.txt').write_bytes(proc.stderr)
  r['exit_code']=proc.returncode
  try:
   final=json.loads(proc.stdout)
   for k in ['is_error','total_cost_usd','usage','modelUsage','session_id','num_turns','subtype']:r[k]=final.get(k)
   (out/'RESULT.md').write_text(final.get('result','')+'\n')
  except (json.JSONDecodeError,AttributeError):r['transport']='no parseable final result'
 except subprocess.TimeoutExpired as error:
  (out/'PROVIDER.json').write_bytes(error.stdout or b'');(out/'STDERR.txt').write_bytes(error.stderr or b'');r['transport']='timeout'
r['elapsed_seconds']=round(time.monotonic()-start,3)
(out/'MEASUREMENT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r.get(k) for k in ['exit_code','is_error','subtype','selected_input_bytes','elapsed_seconds','total_cost_usd','transport']}))
raise SystemExit(0 if r.get('exit_code')==0 and r.get('is_error') is False else 1)
