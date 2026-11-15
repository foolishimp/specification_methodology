#!/usr/bin/env python3
"""Assemble a locked manager runtime, conserving predecessor dependency bytes."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile
from email.parser import BytesParser


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--predecessor', type=Path, required=True)
    parser.add_argument('--wheel', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    content = {}
    with zipfile.ZipFile(args.predecessor) as source:
        old_inventory = json.loads(source.read('WHEELS.json'))
        old_by_hash = {row['sha256']: row for row in old_inventory['members']}
        for name in source.namelist():
            if name.startswith('wheels/') and name.endswith('.whl') and not name.startswith('wheels/stdo_toolchain-'):
                data = source.read(name)
                if digest(data) not in old_by_hash:
                    raise ValueError('Unrecorded predecessor dependency: ' + name)
                content[name] = data
        content['constraints-python313.txt'] = source.read('constraints-python313.txt')
    content['wheels/' + args.wheel.name] = args.wheel.read_bytes()
    rows = []
    for name, data in sorted(content.items()):
        if not name.endswith('.whl'):
            continue
        with zipfile.ZipFile(io.BytesIO(data)) as wheel:
            metadata = [p for p in wheel.namelist() if p.endswith('.dist-info/METADATA')]
            if len(metadata) != 1:
                raise ValueError('Ambiguous wheel metadata: ' + name)
            info = BytesParser().parsebytes(wheel.read(metadata[0]))
        rows.append({'name': info['Name'], 'version': info['Version'], 'path': name,
                     'bytes': len(data), 'sha256': digest(data)})
    if len(rows) != len(old_inventory['members']):
        raise ValueError('Dependency membership changed')
    manager = next(row for row in rows if row['name'] == 'stdo-toolchain')
    if manager['version'] != '3.1.0rc2':
        raise ValueError('Wrong manager version')
    inventory = {'kind': 'stdo.manager-runtime-artifacts/1', 'version': '3.1.0-rc.2',
                 'python_distribution_version': '3.1.0rc2', 'platform': 'macOS arm64',
                 'python': 'CPython3.13', 'members': rows,
                 'dependency_provenance': {'predecessor_archive_sha256': digest(args.predecessor.read_bytes()),
                     'policy': 'Every third-party wheel is byte-identical to an inventoried predecessor wheel; only the owned manager is rebuilt.'}}
    content['WHEELS.json'] = (json.dumps(inventory, indent=2) + '\n').encode()
    content['requirements-macos-arm64-cp313.txt'] = ''.join(
        f"{row['name']}=={row['version']} --hash=sha256:{row['sha256']}\n" for row in rows).encode()
    content['README.md'] = b'''# STDO manager 3.1.0-rc.2 offline runtime

This bundle selects CPython 3.13 on macOS arm64. Third-party wheels retain their
exact predecessor bytes; the manager is rebuilt as 3.1.0rc2 (PEP 440).
From this extracted directory, use a new environment:

```sh
python3.13 -m venv /absolute/new/manager
/absolute/new/manager/bin/python -m pip install --no-index --find-links wheels --require-hashes --no-deps -r requirements-macos-arm64-cp313.txt
/absolute/new/manager/bin/python -m pip check
```

Use the published native manifest with the manager's install and verify commands.
The separate companion Product ZIP provides Purpose Context, Skills and optional
visual documentation. Installing a release does not adopt it for existing Products.
The historical five-Product cohort updater does not migrate this six-Product cohort.
Other Python/platform selections need their own artifact and runtime verification.
'''
    for name, data in content.items():
        target = args.out / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    archive = args.out.parent / 'stdo-manager-runtime-v3.1.0-rc.2-macos-arm64-cp313.zip'
    if archive.exists():
        raise FileExistsError(archive)
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for name, data in sorted(content.items()):
            entry = zipfile.ZipInfo(name, (2026, 11, 15, 0, 0, 0))
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(entry, data)
    print(json.dumps({'archive': str(archive), 'sha256': digest(archive.read_bytes()),
                      'wheels': len(rows), 'third_party_wheels_conserved': len(rows) - 1}))


if __name__ == '__main__':
    main()
