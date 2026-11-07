"""Bind prepared runtime operators to the actual published-install handoff only."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

ROOT = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).absolute().parent
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):
    return {'path': str(path), 'sha256': sha(path), 'bytes': Path(path).stat().st_size}

parser = argparse.ArgumentParser()
parser.add_argument('--handoff', type=Path, required=True)
parser.add_argument('--sha256', required=True)
parser.add_argument('--plan-sha256', required=True)
args = parser.parse_args()
assert sha(HERE / 'PLAN.json') == args.plan_sha256
plan = json.loads((HERE / 'PLAN.json').read_bytes())
assert args.handoff.absolute() == Path(plan['handoff'])
assert sha(args.handoff) == args.sha256
handoff = json.loads(args.handoff.read_bytes())
assert handoff['workspace'] == plan['workspace'] and handoff['version'] == plan['version']
assert handoff['native_commit'] == plan['native_commit']
assert handoff['native_manifest']['sha256'] == plan['native_manifest_sha256']
assert Path(handoff['native_root']) == Path(plan['workspace']) / 'store/releases/v3.0.5-rc.1'
target = Path(plan['portable_root'])
assert target.is_dir() and not target.is_symlink()
selected = [(ROOT / row['path'], target / Path(row['path']).name, row) for row in plan['files']]
for source, destination, row in selected:
    assert sha(source) == row['sha256'] and source.stat().st_size == row['bytes']
    assert not destination.exists() and not destination.is_symlink()
assert not (target / 'SELECTED_HANDOFF.json').exists() and not (target / 'BINDING.json').exists()
for source, destination, row in selected:
    shutil.copyfile(source, destination)
    assert sha(destination) == row['sha256']
shutil.copyfile(args.handoff, target / 'SELECTED_HANDOFF.json')
record = {'kind': 'stdo.rc-reset.public-runtime-binding/1', 'status': 'bound_unexecuted',
    'plan': ref(HERE / 'PLAN.json'), 'binder': ref(Path(__file__)), 'handoff': ref(args.handoff),
    'selected_operators': [ref(destination) for _, destination, _ in selected],
    'scope': 'Actual handoff custody only. Execute only the assigned fixed-interface phase; this binding is no qualification verdict.'}
(target / 'BINDING.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps(ref(target / 'BINDING.json')))
