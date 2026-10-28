"""Bounded private process groups for compiler/setup effects, with signal cleanup."""
from __future__ import annotations
import os
import signal
import subprocess
import threading
import time

class CleanupUnresolved(RuntimeError):
    pass

def _alive(group):
    try:os.killpg(group,0);return True
    except ProcessLookupError:return False

def _cleanup(process):
    for sig in (signal.SIGTERM,signal.SIGKILL):
        try:os.killpg(process.pid,sig)
        except ProcessLookupError:pass
        try:process.wait(timeout=2)
        except subprocess.TimeoutExpired:pass
        until=time.monotonic()+2
        while _alive(process.pid) and time.monotonic()<until:time.sleep(.02)
        if not _alive(process.pid):return
    raise CleanupUnresolved('compiler process group cleanup remains unresolved')

def run(command,*,cwd,env,stdout,timeout,check=False):
    """No pipe collection: caller owns a regular retained diagnostic file."""
    previous={}
    def interrupted(signum,_frame):raise InterruptedError('interrupted during compiler effect: '+str(signum))
    if threading.current_thread() is threading.main_thread():
        for sig in (signal.SIGTERM,signal.SIGINT):
            previous[sig]=signal.signal(sig,interrupted)
    process=None
    try:
        process=subprocess.Popen(command,cwd=cwd,env=env,stdout=stdout,stderr=subprocess.STDOUT,start_new_session=True)
        try:code=process.wait(timeout=timeout)
        except BaseException:
            _cleanup(process)
            raise
        if _alive(process.pid):
            _cleanup(process)
            raise CleanupUnresolved('compiler exited with surviving descendants; group was terminated')
        result=subprocess.CompletedProcess(command,code)
        if check:result.check_returncode()
        return result
    finally:
        for sig,handler in previous.items():signal.signal(sig,handler)
