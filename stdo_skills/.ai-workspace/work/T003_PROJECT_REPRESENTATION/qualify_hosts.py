#!/usr/bin/env python3
"""One bounded native host trial on an owned disposable non-STDO project."""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

WORK = Path(__file__).resolve().parent
REPO = WORK.parents[3]
SKILLS = REPO / 'stdo_skills'
TOOL = REPO / 'a_c/build_tenants/graphify/code/ac_project.py'


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n' if not isinstance(value, str) else value)


def trial(host, attempt):
    home = WORK / ('host-' + host + f'-{attempt:02d}')
    home.mkdir(exist_ok=False)
    project = home / 'invoice-project'
    project.mkdir()
    source = '# Invoice export\n\nExport rows as CSV with columns id, amount, currency in that order.\nPreserve every supplied decimal digit in amount; binary floating-point conversion is forbidden.\nFor zero rows, emit the header alone.\n\n## Unresolved rounding policy\n\nRounding is not yet specified. Retain this as unresolved; do not invent a rounding rule.\n'
    write(project / 'specification/PRODUCT.md', source)
    write(project / 'specification/INTENT.md', '# Intent\nMake invoice export reproducible while preserving exact supplied decimal amounts.\n')
    write(project / 'specification/GOALS.md', '# Goals\nBuild a source-linked proposal representation for this qualification project.\n')
    definition = copy.deepcopy(json.loads((SKILLS / 'stdo_skills.json').read_text()))
    definition['product'] = {'definition_id': 'urn:example:invoice-export:' + host,
                             'name': 'Invoice export ' + host, 'source_project': './',
                             'bounded_context': {'id': 'urn:example:invoice-export:' + host + ':context',
                                                 'definition': './specification/PRODUCT.md'}}
    definition['constitution']['additional_authorities'] = ['./specification/PRODUCT.md']
    definition['reference_frame_bases'] = [{'uri': './FRAME_BASIS.md', 'authority': ['./AGENTS.md'],
                                           'applies_to': [definition['product']['definition_id']]}]
    definition['what'] = {'intent': './specification/INTENT.md', 'product': './specification/PRODUCT.md',
                          'specification': ['./specification/']}
    definition['how'] = {'common': [], 'build_tenants': [{'id': 'urn:example:invoice-export:local',
                          'root': './build_tenants/local/', 'design': ['./build_tenants/local/design/'],
                          'implementation': ['./build_tenants/local/code/']}]}
    write(project / 'FRAME_BASIS.md', '# Representation frame\nThe owner selects exact WHAT source interpretation, proposal construction and structural checks. This frame confers no semantic acceptance or publication.\n')
    write(project / 'build_tenants/local/design/README.md', '# Local realization\nThe selected task builds a representation; executable invoice delivery remains open.\n')
    (project / 'build_tenants/local/code').mkdir()
    definition['composition'] = []
    definition_path = project / 'stdo_invoice.json'
    write(definition_path, definition)
    if host == 'codex':
        shutil.copytree(SKILLS / 'build_tenants/codex/skills/stdo-work', project / '.agents/skills/stdo-work')
        invocation = '$stdo-work'
    else:
        shutil.copytree(SKILLS / 'build_tenants/claude/skills', project / '.claude/skills')
        invocation = '/stdo-tool-operations'
    run = project / '.ai-workspace/representations/invoice-01'
    grant = ('# Qualification activation\n\nYou are a Worker building a source representation of this nominated project. '
             'The owner authorizes the direct local source route and writes only within .ai-workspace/representations/ '
             'for this task. Read the installed skill and the selected provider contract. Do not edit project source, '
             'change method basis, launch child agents, publish or use Git. No mediated composition restriction is '
             'selected for this synthetic local subject. A representation is a proposal, not acceptance.\n')
    write(project / 'AGENTS.md', grant)
    write(project / 'CLAUDE.md', grant)
    prompt = (f'{invocation} Build an a_c representation of my nominated project at {project}. '
              f'Its Product Definition is {definition_path}. Use the default WHAT source scope, direct mode, '
              f'and create the run at {run}. The selected provider is {TOOL}, with Python {sys.executable} '
              f'and stdo manager {shutil.which("stdo")}. You have the Worker grant in AGENTS.md/CLAUDE.md. '
              'Author the real project interpretation in this session and return the built artifacts and actual check scope. '
              'Use your installed skill. Stop on a genuine blocked prerequisite; do not substitute a canned model or invent success.')
    write(home / 'prompt.txt', prompt)
    verify = subprocess.run(['stdo', 'status', '--definition', str(definition_path), '--verify'], capture_output=True, text=True)
    write(home / 'manager-readback.json', json.loads(verify.stdout))
    if verify.returncode:
        write(home / 'REPORT.json', {'host':host, 'actor_started':False, 'reason':'invalid qualification fixture', 'failures':json.loads(verify.stdout).get('failures')})
        raise RuntimeError('fixture Product Definition failed actual manager verification')
    env = dict(os.environ, AC_PROJECT_TOOL=str(TOOL), AC_PROJECT_PYTHON=sys.executable,
               PYTHONDONTWRITEBYTECODE='1')
    if host == 'codex':
        command = ['codex', 'exec', '--json', '--ephemeral', '--sandbox', 'workspace-write',
                   '--skip-git-repo-check', '--cd', str(project), '--output-last-message', str(home / 'last-message.txt'),
                   '-c', 'features.multi_agent=false', '-c', 'features.apps=false', '-c', 'features.memories=false',
                   '-c', 'web_search="disabled"', '-']
    else:
        command = ['claude', '-p', '--output-format', 'stream-json', '--verbose', '--permission-mode', 'acceptEdits',
                   '--allowedTools', 'Read,Write,Edit,Bash,Skill', '--tools', 'Read,Write,Edit,Bash,Skill',
                   '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}', '--no-session-persistence']
    write(home / 'invocation.json', {'host':host, 'command':command, 'cwd':str(project), 'timeout_seconds':240,
                                    'provider_sha256':hashlib.sha256(TOOL.read_bytes()).hexdigest(),
                                    'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest()})
    started = time.monotonic()
    timed_out = False
    with (home / 'events.jsonl').open('wb') as events, (home / 'stderr.txt').open('wb') as errors:
        process = subprocess.Popen(command, cwd=project, env=env, stdin=subprocess.PIPE,
                                   stdout=events, stderr=errors, start_new_session=True)
        try:
            process.communicate(prompt.encode(), timeout=240)
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
    write(home / 'final-status.json', json.loads(inspection.stdout or inspection.stderr))
    report = {'host':host, 'exit_code':process.returncode, 'timed_out':timed_out,
              'elapsed_seconds':round(time.monotonic()-started,3),
              'build_exists':(run / 'BUILD.json').is_file(), 'status_exit':inspection.returncode,
              'source_unchanged':(project / 'specification/PRODUCT.md').read_text()==source,
              'scope':'one explicitly invoked native host; no automatic discovery reliability or semantic acceptance claim'}
    write(home / 'REPORT.json', report)
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host',choices=('codex','claude'))
    parser.add_argument('--attempt',type=int,default=1)
    args=parser.parse_args()
    trial(args.host,args.attempt)
