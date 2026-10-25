import json,os,signal,subprocess,sys,time
from pathlib import Path
control=Path(sys.argv[2])
stop=control/'stop-child'
if sys.argv[1]=='child':
 (control/'child-ready').write_text(str(os.getpid()))
 deadline=time.monotonic()+20
 continuous=sys.argv[3]=='continuous'
 while not stop.exists() and time.monotonic()<deadline:
  if continuous and (control/'actor-ready').exists():
   try: os.write(1,b'descendant tail '*4096)
   except BrokenPipeError: continuous=False
  else: time.sleep(0.01)
 (control/'child-ended').write_text('fixture stop observed')
 raise SystemExit(0)
sys.stdin.buffer.read()
if sys.argv[3]=='ignore-term': signal.signal(signal.SIGTERM,signal.SIG_IGN)
child=subprocess.Popen([sys.executable,'-B',__file__,'child',str(control),sys.argv[3]],stdin=subprocess.DEVNULL)
deadline=time.monotonic()+2
while not (control/'child-ready').exists() and time.monotonic()<deadline: time.sleep(0.005)
print('retained stdout before termination',flush=True)
print('retained stderr before termination',file=sys.stderr,flush=True)
(control/'actor-ready').write_text(json.dumps({'parent':os.getpid(),'child':child.pid}))
time.sleep(20)
