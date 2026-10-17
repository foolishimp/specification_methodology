#!/usr/bin/env python3
"""Replay four source-unit acquisition indexes in the archived Codex package."""
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile

REPO = Path('/Users/jim/src/apps/specification_methodology')
OUT = Path(__file__).resolve().parent
CHECKER = '9a9c479776ffd974fbcafcf48341980918209aef'
THEORY = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
IDS = ['FOUNDATIONS.workspace-and-context', 'SPEC_METHOD.universal-intake-triage', 'FOUNDATIONS.change-impact-and-evidence-retention', 'SPEC_METHOD.what-how-and-work-carriers']

def sha(b):
    return hashlib.sha256(b).hexdigest()

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

prior = json.loads((OUT / 'frame_reproduction.json').read_text())['subjects']['codex']
package = Path(prior['scratch_archive_root']) / 'specification_methodology/v3/build_tenants/codex/successor'
checker_root = Path(tempfile.mkdtemp(prefix='i5-acquisition-checker-')).resolve()
with tarfile.open(fileobj=io.BytesIO(git('archive', CHECKER, '--', 'axiom_indexer'))) as archive:
    archive.extractall(checker_root, filter='data')
pins = []
note = git('show', CHECKER + ':axiom_indexer/releases/v2.5.1.md').decode()
for match in re.finditer(r'^\| (?:file|symlink) \| `([^`]+)`.*?\| `([a-f0-9]{64})` \|$', note, re.M):
    path, expected = match.groups()
    actual = sha(git('show', CHECKER + ':axiom_indexer/' + path))
    pins.append({'path': path, 'expected': expected, 'actual': actual, 'matches': actual == expected})
if len(pins) != 7 or not all(p['matches'] for p in pins):
    raise RuntimeError('Checker Product membership or byte mismatch')
bindings = checker_root / 'bindings.json'
bound = subprocess.run([sys.executable, '-B', str(package / 'interpretation/bindings.py'), '--theory-root', str(THEORY)], cwd=package, capture_output=True)
if bound.returncode:
    raise RuntimeError(bound.stderr.decode())
bindings.write_bytes(bound.stdout)
mapping = json.loads((package / 'interpretation/MAPPING.json').read_bytes())
index_by_id = {r['id']: r['index'] for r in mapping['rows']}
record = {'candidate': prior['commit'], 'checker_commit': CHECKER, 'checker_members': pins, 'theory_root': str(THEORY), 'theory_manifest_sha256': sha((THEORY / 'manifest.json').read_bytes()), 'bindings_verification_exit': bound.returncode, 'bindings_sha256': sha(bound.stdout), 'scratch_output_root': str(checker_root), 'projections': []}
for name in IDS:
    target = checker_root / (name + '.json')
    command = [sys.executable, '-B', str(checker_root / 'axiom_indexer/build_tenants/core/code/ac.py'), 'project', '--program', str(package / 'interpretation/program.json'), '--map', str(package / 'interpretation/map.json'), '--bindings', str(bindings), '--frame-index', index_by_id[name], '--mode', 'materialized', '--output', str(target)]
    result = subprocess.run(command, cwd=package, capture_output=True, text=True, timeout=30)
    row = {'id': name, 'frame_index': index_by_id[name], 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr, 'command': command}
    if target.exists():
        data = target.read_bytes()
        obj = json.loads(data)
        row.update(output_sha256=sha(data), output_bytes=len(data), output_shape={k: {'type': type(v).__name__, 'length': len(v) if hasattr(v, '__len__') else None} for k, v in obj.items()})
    record['projections'].append(row)
target = OUT / 'projection_reproduction.json'
target.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'checker_member_pins_match': all(x['matches'] for x in pins), 'bindings_exit': bound.returncode, 'projections': [{'id': x['id'], 'exit_code': x['exit_code'], 'output_bytes': x.get('output_bytes'), 'shape': x.get('output_shape')} for x in record['projections']], 'artifact_sha256': sha(target.read_bytes())}, indent=2))
