#!/usr/bin/env python3
"""Bind only current 3.0.5 Skills source; historical packages are not installed."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / 'VERSION', ROOT / 'scripts/manage_skills.py', ROOT / 'scripts/package_305.py',
         ROOT / 'specification/RELEASE_3_0_5.md', ROOT / 'release/3.0.5/README.md']
for host in ('codex', 'claude'):
    paths.extend(p for p in (ROOT / 'build_tenants' / host / 'current').rglob('*') if p.is_file())
files = []
for path in sorted(paths):
    if path.is_symlink() or '__pycache__' in path.parts:
        raise ValueError('Non-source package member: ' + str(path))
    raw = path.read_bytes()
    files.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
manifest = {'kind': 'stdo-skills.package/1', 'version': '3.0.5',
            'product': 'urn:stdo:product-definition:stdo-skills',
            'builder': {'uri': 'stdo://releases/v3.0.4/', 'manifest_sha256': '102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b'},
            'target': 'stdo://releases/v3.0.5/',
            'workflow_owner': 'verified native plugins/spec core5 plus Claude refresh',
            'files': files}
path = ROOT / 'release/3.0.5/manifest.json'
path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
print(json.dumps({'manifest': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'files': len(files)}))
