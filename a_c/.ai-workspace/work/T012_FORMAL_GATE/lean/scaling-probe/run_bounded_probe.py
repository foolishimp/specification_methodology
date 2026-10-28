#!/usr/bin/env python3
"""Own-territory Lean probes; never builds or mutates imported support."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import selectors
import signal
import subprocess
import sys
import time

work = Path(__file__).resolve().parent
tenant = Path('/Users/jim/src/apps/specification_methodology/a_c/build_tenants/lean')
compiler = tenant / '.toolchain/lean-4.35.0-darwin_aarch64/bin/lean'
probe = sys.argv[1]
assert probe in ('Probe2', 'Probe3')
source = work / (probe + '.lean')
assert not (work / (probe + '-result.json')).exists(), 'One execution only per probe'
env = {k:v for k,v in os.environ.items() if not k.startswith(('LEAN','LAKE','LD_','DYLD_'))}
env['LEAN_PATH'] = ':'.join(str(p) for p in [tenant / '.lake/build/lib/lean', *sorted((tenant / '.lake/packages').glob('*/.lake/build/lib/lean'))])

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

support_paths = [compiler, tenant / 'lean-toolchain', tenant / 'lake-manifest.json', tenant / 'lakefile.lean']
support_paths += list((tenant / 'AC').glob('*.lean'))
support_paths += list((tenant / '.lake/build/lib/lean/AC').glob('*.olean*'))
support_paths += [tenant / '.lake/packages/mathlib/Mathlib/Data/Finset/Basic.lean', tenant / '.lake/packages/mathlib/Mathlib/Data/Finset/Card.lean']
for module in ('Basic', 'Card'):
    support_paths += list((tenant / '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Data/Finset').glob(module+'.olean*'))
support_paths = sorted(set(p for p in support_paths if p.is_file()))
identities = {str(p.relative_to(tenant)):sha(p) for p in support_paths}
version = subprocess.run([str(compiler),'--version'],env=env,cwd=tenant,check=True,capture_output=True,text=True).stdout.strip()
command = [str(compiler),'-j','1','-M','4096',str(source)]
started_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
metadata = {'probe':probe,'started_at':started_at,'command':command,'cwd':str(tenant),'lean_path':env['LEAN_PATH'],'compiler_version':version,'source_sha256':sha(source),'support_sha256':identities,'timeout_seconds':60,'memory_megabytes':4096,'async_elaboration':False}
(work / (probe+'-input.json')).write_text(json.dumps(metadata,indent=2)+'\n')
start = time.monotonic()
process = subprocess.Popen(command,cwd=tenant,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,start_new_session=True)
selector = selectors.DefaultSelector()
selector.register(process.stdout,selectors.EVENT_READ)
events = []
pending = b''
timed_out = False
with (work / (probe+'.log')).open('wb') as log:
    while selector.get_map():
        elapsed = time.monotonic()-start
        if elapsed >= 60 and process.poll() is None:
            timed_out = True
            os.killpg(process.pid,signal.SIGKILL)
            process.wait()
        for key,_ in selector.select(timeout=min(0.25,max(0,60-elapsed)) if not timed_out else 0.25):
            data = os.read(key.fileobj.fileno(),65536)
            if not data:
                selector.unregister(key.fileobj)
                continue
            log.write(data)
            log.flush()
            pending += data
            while b'\n' in pending:
                line,pending = pending.split(b'\n',1)
                event = {'seconds':round(time.monotonic()-start,6),'text':line.decode('utf-8',errors='replace')}
                events.append(event)
                print(json.dumps(event),flush=True)
    if pending:
        events.append({'seconds':round(time.monotonic()-start,6),'text':pending.decode('utf-8',errors='replace')})
    exit_code = process.wait()
duration = time.monotonic()-start
selector.close()
process.stdout.close()
after = {str(p.relative_to(tenant)):sha(p) for p in support_paths}
result = {**metadata,'status':'timeout' if timed_out else ('passed' if exit_code == 0 else 'failed'),'exit':exit_code,'seconds':duration,'events':events,'support_unchanged':after == identities,'support_after_sha256':after,'source_after_sha256':sha(source),'children_maxrss_bytes_on_macos':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,'process_reaped':True,'active_processes':False,'log_sha256':sha(work/(probe+'.log'))}
(work / (probe+'-result.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('probe','status','exit','seconds','support_unchanged','children_maxrss_bytes_on_macos','process_reaped')}),flush=True)
