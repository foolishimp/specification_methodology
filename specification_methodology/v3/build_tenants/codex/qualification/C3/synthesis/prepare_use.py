"""Freeze independent tasks and method inputs for sandbox use trials."""
from pathlib import Path
import argparse,hashlib,json,subprocess

q=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--destination',default='use');parser.add_argument('--oracle',default='runs/oracle/ORACLE.json');args=parser.parse_args()
destination=q/args.destination
if destination.resolve().parent!=q:raise ValueError('destination must be one synthesis child')
base=q.parents[2];root=base/'successor'
oracle_path=q/args.oracle
oracle=json.loads(oracle_path.read_text())
cut=subprocess.check_output(['git','rev-parse','HEAD'],cwd=base,text=True).strip()
for case in oracle['cases']:
 target=destination/case['id'];target.mkdir(parents=True,exist_ok=False)
 workspace=target/'workspace';workspace.mkdir(exist_ok=True)
 for name,body in case['workspace'].items():
  dest=workspace/name
  if workspace not in dest.resolve().parents:raise ValueError('out-of-scope fixture path')
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(body)
 (target/'TASK.json').write_text(json.dumps({'id':case['id'],'task':case['task'],'workspace':case['workspace']},indent=2)+'\n')
 frame='EVALUATION_CONJUNCTION.md' if case['id'].startswith(('C5','C6','C7')) else 'WORK_RECOVERY.md'
 material=(root/'standards/frames'/frame).read_text()
 prompt='''You are a fresh actor in a controlled actual-use experiment. You did not author the supplied method and have no prior conversation. Apply the method to the task and actual sandbox workspace below. The host has verified the selected frozen candidate source for this experiment; it is the subject under test, not a claim of an installed or accepted release. The task's workspace contains the actual work grant and constraints. You may propose edits only within them. You have no services or execution tools; do not claim commands ran or effects occurred. Return JSON ONLY: {"edits":[{"path":"relative/file","content":"entire replacement file"}],"report":"observations, work, unresolved matters with method sources","results":[...]} . The host will apply your proposals to real sandbox files, check allowed effects and run any selected assertions separately. Do not ask for already supplied authority or invent a mandatory extra actor. If a material input is actually missing, preserve that unresolved result. No hidden oracle, original worker memory or later assistance is available.\n\nFROZEN METHOD COMMIT: '''+cut+'\nMETHOD FRAME: '+frame+'\n'+material+'\nTASK AND OBSERVED WORKSPACE\n'+json.dumps({'task':case['task'],'workspace':case['workspace']},indent=2)
 (target/'PROMPT.txt').write_text(prompt)
 (target/'INPUT.json').write_text(json.dumps({'candidate_commit':cut,'frame':frame,'frame_sha256':hashlib.sha256(material.encode()).hexdigest(),'prompt_bytes':len(prompt.encode()),'workspace_sha256':hashlib.sha256(json.dumps(case['workspace'],sort_keys=True).encode()).hexdigest(),'oracle_sha256':hashlib.sha256(oracle_path.read_bytes()).hexdigest(),'oracle_excluded':True},indent=2)+'\n')
 print(case['id'],len(prompt.encode()))
