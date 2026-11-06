"""Actual bounded child-group cleanup, including an inherited grandchild."""
import os
import errno
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import runtime_process
import formal_support

class RuntimeProcessTests(unittest.TestCase):
    def test_denied_group_probe_retains_unsettled_identity_and_cause(self):
        denied=PermissionError(errno.EPERM,'controlled group probe denial')
        with patch.object(runtime_process.os,'killpg',side_effect=denied) as signal_group:
            with self.assertRaises(runtime_process.CleanupUnresolved) as observed:
                runtime_process._alive(12345)
        signal_group.assert_called_once_with(12345,0)
        self.assertIs(observed.exception.__cause__,denied)
        self.assertIn('probe denied',str(observed.exception))
        self.assertIn('PGID=12345, errno=1',str(observed.exception))

    def test_denied_group_signal_retains_unsettled_identity_and_cause(self):
        denied=PermissionError(errno.EPERM,'controlled group signal denial')
        process=Mock(pid=12345)
        with patch.object(runtime_process.os,'killpg',side_effect=denied) as signal_group:
            with self.assertRaises(runtime_process.CleanupUnresolved) as observed:
                runtime_process._cleanup(process)
        signal_group.assert_called_once_with(12345,runtime_process.signal.SIGTERM)
        process.wait.assert_not_called()
        self.assertIs(observed.exception.__cause__,denied)
        self.assertIn('signal SIGTERM denied',str(observed.exception))
        self.assertIn('PGID=12345, errno=1',str(observed.exception))

    def test_denied_initial_launch_is_not_classified_as_cleanup(self):
        denied=PermissionError(errno.EACCES,'controlled initial launch denial')
        with patch.object(runtime_process.subprocess,'Popen',side_effect=denied), \
             patch.object(runtime_process.os,'killpg') as signal_group:
            with self.assertRaises(PermissionError) as observed:
                runtime_process.run(['selected-program'],cwd=Path.cwd(),env={},stdout=None,timeout=1)
        self.assertIs(observed.exception,denied)
        signal_group.assert_not_called()

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
