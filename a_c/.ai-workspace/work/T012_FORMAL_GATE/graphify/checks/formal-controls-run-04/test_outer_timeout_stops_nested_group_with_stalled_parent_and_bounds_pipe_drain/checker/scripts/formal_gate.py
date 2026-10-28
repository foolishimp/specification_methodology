import subprocess,sys,pathlib,time,signal,json,os
signal.signal(signal.SIGTERM,signal.SIG_IGN)
while not pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-formal-control-wzy2sr7k/spawn-after-first-census').exists(): time.sleep(0.01)
p=subprocess.Popen([sys.executable,'-c',"import pathlib,time,signal; signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(8); pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-formal-control-wzy2sr7k/descendant-completed').write_text('escaped')"],start_new_session=True)
pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-formal-control-wzy2sr7k/descendant.pid').write_text(str(p.pid))
pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-formal-control-wzy2sr7k/spawn.json').write_text(json.dumps({'parent_pid':os.getpid(),'child_pid':p.pid,'child_pgid':os.getpgid(p.pid),'spawned_monotonic_ns':time.monotonic_ns()}))
time.sleep(30)
