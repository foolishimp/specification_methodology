#!/usr/bin/env python3
"""Replay the frozen frame renderers only in disposable Git archives."""
import datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile

sys.dont_write_bytecode = True
REPO = Path('/Users/jim/src/apps/specification_methodology')
OUT = Path(__file__).resolve().parent
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
SUBJECTS = {'codex': '99f932cfece1a7c9ba6f85c44c47d2403a486aa7', 'claude': '5da6bdec6ca383b4a9c91fe5b45a293aa03d8ff2'}

def digest(b):
    return hashlib.sha256(b).hexdigest()

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m

record = {'time_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'common': COMMON, 'method': 'Candidate renderer replay plus independent SHA-256 checks of frame bytes and owner pins, in isolated archives. No sufficiency or semantic completeness inference.', 'subjects': {}}
for tenant, commit in SUBJECTS.items():
    scratch = Path(tempfile.mkdtemp(prefix=f'i5-acquisition-{tenant}-')).resolve()
    territory = f'specification_methodology/v3/build_tenants/{tenant}'
    archive = subprocess.check_output(['git', '-C', str(REPO), 'archive', commit, '--', territory])
    with tarfile.open(fileobj=io.BytesIO(archive)) as f:
        f.extractall(scratch, filter='data')
    root = scratch / territory
    package = root / 'successor' if tenant == 'codex' else root
    manifest_path = root / 'qualification/C3/iteration-5/FRAME_INPUTS.json' if tenant == 'codex' else root / 'standards/frames/FRAME_INPUTS.json'
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    rows, failures = [], []
    for frame in manifest['frames']:
        frame_bytes = (package / frame['path']).read_bytes()
        owner_pins = []
        for route in frame['routes'] + frame.get('argument_routes', []) + frame.get('binds', []):
            if 'owner' not in route:
                continue
            observed = digest((package / route['owner']).read_bytes())
            valid = observed == route['owner_sha256']
            owner_pins.append({'owner': route['owner'], 'anchor': route['anchor'], 'valid': valid, 'declared_sha256': route['owner_sha256'], 'observed_sha256': observed})
            if not valid:
                failures.append(f"{frame['path']} owner pin {route['owner']}#{route['anchor']}")
        row = {'path': frame['path'], 'observed_bytes': len(frame_bytes), 'sha256': digest(frame_bytes), 'manifest_size_matches': len(frame_bytes) == frame['bytes'], 'manifest_digest_matches': digest(frame_bytes) == frame['sha256'], 'routes': owner_pins}
        rows.append(row)
    if tenant == 'codex':
        renderer = module('codex_frame_renderer', root / 'qualification/C3/iteration-3/refresh_current.py')
        changes, regenerated_manifest = renderer.render_views(package, manifest_path.parent, COMMON)
        generated = {p: value.encode() for p, value in changes.items()}
        manifest_match = regenerated_manifest == manifest
    else:
        renderer = module('claude_frame_renderer', root / 'qualification/instruments/generate_frames.py')
        generated = renderer.build(root, manifest_path)
        manifest_match = generated[manifest_path] == manifest_bytes
    for row in rows:
        frame_path = package / row['path']
        row['regenerated_bytes_match'] = generated[frame_path] == frame_path.read_bytes()
        if not row['regenerated_bytes_match']:
            failures.append(row['path'] + ' render drift')
    observation = {'commit': commit, 'scratch_archive_root': str(scratch), 'archive_bytes': len(archive), 'manifest_sha256': digest(manifest_bytes), 'frame_count': len(rows), 'manifest_regeneration_matches': manifest_match, 'frames': rows, 'failures': failures}
    if tenant == 'claude':
        result = subprocess.run([sys.executable, '-B', str(root / 'a_c/i3/tools/assemble.py'), '--check'], cwd=root, text=True, capture_output=True)
        observation['interpretation_precheck'] = {'command': 'python3 -B a_c/i3/tools/assemble.py --check', 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr, 'standing': 'Current partial-publication check only; README declares I5 rebuild unfinished.'}
    record['subjects'][tenant] = observation

target = OUT / 'frame_reproduction.json'
target.write_text(json.dumps(record, indent=2) + '\n')
for tenant, result in record['subjects'].items():
    print(json.dumps({'tenant': tenant, 'frames': result['frame_count'], 'all_frame_bytes_reproduced': all(r['regenerated_bytes_match'] for r in result['frames']), 'manifest_matches': result['manifest_regeneration_matches'], 'owner_pin_failures': len(result['failures']), 'interpretation_precheck': result.get('interpretation_precheck', {}).get('exit_code')}))
print('artifact_sha256=' + digest(target.read_bytes()))
