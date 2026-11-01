#!/usr/bin/env python3
"""Retain a separate native invocation resuming an interrupted T003 fixture."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

WORK = Path(__file__).resolve().parent
REPO = WORK.parents[3]
TOOL = REPO / 'a_c/build_tenants/graphify/code/ac_project.py'


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n' if not isinstance(value, str) else value)


def resume(host):
    original = WORK / f'host-{host}-02'
    home = original / 'resume-01'
    home.mkdir(exist_ok=False)
    project = original / 'invoice-project'
    run = project / '.ai-workspace/representations/invoice-01'
    source_before = {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (project / 'specification').rglob('*') if p.is_file()}
    invocation = json.loads((original / 'invocation.json').read_text())
    command = invocation['command']
    if host == 'codex':
        command[command.index('--output-last-message') + 1] = str(home / 'last-message.txt')
    skill = '$stdo-work' if host == 'codex' else '/stdo-tool-operations'
    prompt = (f'{skill} Resume my interrupted representation build for {project}. '
              f'The exact existing run is {run}; do not prepare a replacement. '
              'The previous invocation reached its time bound; effects may already exist. '
              'Use the installed representation skill, reconcile through status, complete pending '
              'authoring in this host session and perform build or checked reuse and final status. '
              f'The selected provider is {TOOL}; Python is {sys.executable}. '
              'The existing AGENTS.md/CLAUDE.md Worker grant and direct local mode still apply. '
              'Return links to the actual artifacts with the performed check scope. '
              'Do not edit project source, publish, run Git or launch other actors.')
    save(home / 'prompt.txt', prompt)
    save(home / 'invocation.json', dict(invocation, command=command, timeout_seconds=600,
         prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(), resumes='../REPORT.json'))
    started = time.monotonic()
    timed_out = False
    env = dict(os.environ, AC_PROJECT_TOOL=str(TOOL), AC_PROJECT_PYTHON=sys.executable,
               PYTHONDONTWRITEBYTECODE='1')
    with (home / 'events.jsonl').open('wb') as events, (home / 'stderr.txt').open('wb') as errors:
        process = subprocess.Popen(command, cwd=project, env=env, stdin=subprocess.PIPE,
                                   stdout=events, stderr=errors, start_new_session=True)
        try:
            process.communicate(prompt.encode(), timeout=600)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    inspection = subprocess.run([sys.executable, '-B', str(TOOL), 'status', '--run', str(run)],
                                capture_output=True, text=True)
    status = json.loads(inspection.stdout or inspection.stderr)
    save(home / 'final-status.json', status)
    source_after = {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (project / 'specification').rglob('*') if p.is_file()}
    report = {'host': host, 'exit_code': process.returncode, 'timed_out': timed_out,
              'elapsed_seconds': round(time.monotonic() - started, 3),
              'build_exists': (run / 'BUILD.json').is_file(), 'status_exit': inspection.returncode,
              'status': status.get('status'), 'source_unchanged': source_before == source_after,
              'scope': 'one explicit native resume; retains original timeout; no reliability or acceptance claim'}
    save(home / 'REPORT.json', report)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', choices=('codex', 'claude'))
    resume(parser.parse_args().host)
