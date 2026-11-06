"""Actual bounded child-group cleanup, including an inherited grandchild."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import runtime_process
import formal_support

class RuntimeProcessTests(unittest.TestCase):
    def test_timeout_terminates_actual_parent_and_grandchild(self):
        with tempfile.TemporaryDirectory(dir=formal_support.ROOT/'.cache') as directory:
            root=Path(directory);pidfile=root/'child.pid'
            program='import subprocess,sys,time,pathlib; p=subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"]); pathlib.Path(sys.argv[1]).write_text(str(p.pid)); time.sleep(30)'
            with (root/'process.log').open('wb') as log:
                with self.assertRaises(subprocess.TimeoutExpired):
                    runtime_process.run([sys.executable,'-c',program,str(pidfile)],cwd=root,env=os.environ.copy(),stdout=log,timeout=1)
            self.assertTrue(pidfile.exists())
            with self.assertRaises(ProcessLookupError):os.kill(int(pidfile.read_text()),0)

    def test_success_cannot_leave_an_inherited_background_child(self):
        with tempfile.TemporaryDirectory(dir=formal_support.ROOT/'.cache') as directory:
            root=Path(directory);pidfile=root/'child.pid'
            program='import subprocess,sys,pathlib; p=subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"]); pathlib.Path(sys.argv[1]).write_text(str(p.pid))'
            with (root/'process.log').open('wb') as log:
                with self.assertRaises(runtime_process.CleanupUnresolved):
                    runtime_process.run([sys.executable,'-c',program,str(pidfile)],cwd=root,env=os.environ.copy(),stdout=log,timeout=3)
            with self.assertRaises(ProcessLookupError):os.kill(int(pidfile.read_text()),0)

if __name__=='__main__':unittest.main()
