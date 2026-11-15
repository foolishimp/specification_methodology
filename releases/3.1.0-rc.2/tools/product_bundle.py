#!/usr/bin/env python3
"""Package only the five explicitly selected companion Product distributions."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--context-stage', type=Path, required=True)
    parser.add_argument('--visual-selection', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    selected = json.loads(args.visual_selection.read_text())
    if selected['version'] != '3.1.0-rc.2':
        raise ValueError('Wrong visual version')
    files = {}
    products = {}

    def add(product, path, data, expected=None):
        relative = PurePosixPath(path)
        if relative.is_absolute() or '..' in relative.parts or not relative.parts:
            raise ValueError('Unsafe member path')
        if any(part in {'__pycache__', '.DS_Store', '.ai-workspace', '.git', '.venv', '.lake'} for part in relative.parts):
            raise ValueError('Excluded member')
        key = product + '/' + path
        if key in files:
            raise ValueError('Duplicate member: ' + key)
        row = {'path': path, 'bytes': len(data), 'sha256': digest(data)}
        if expected and any(row[k] != expected[k] for k in row):
            raise ValueError('Changed selected member: ' + key)
        files[key] = data
        products.setdefault(product, {'members': []})['members'].append(row)

    for product in ['purpose_context', 'stdo_skills']:
        source = args.context_stage / product
        for path in sorted(source.rglob('*')):
            if path.is_symlink():
                raise ValueError('Distribution symlink: ' + str(path))
            if path.is_file():
                add(product, path.relative_to(source).as_posix(), path.read_bytes())
    for product in ['a_c', 'stdo_representation', 'axiom_indexer']:
        rows = selected['products'][product]['members']
        if len(rows) != selected['products'][product]['member_count']:
            raise ValueError('Incomplete visual selection')
        for row in rows:
            path = args.root / product / row['path']
            if path.is_symlink():
                raise ValueError('Visual symlink: ' + str(path))
            add(product, row['path'], path.read_bytes(), row)
    for name, product in products.items():
        identity_path = 'INVENTORY.json' if name == 'stdo_skills' else 'PUBLIC_MANIFEST.json'
        product['identity_path'] = identity_path
        product['identity_sha256'] = digest(files[name + '/' + identity_path])
        product['member_count'] = len(product['members'])
        product['members'].sort(key=lambda row: row['path'])
    inventory = {'kind': 'stdo.companion-products/1', 'version': '3.1.0-rc.2',
                 'native_method': {'uri': 'stdo://releases/v3.1.0-rc.2/',
                    'manifest_sha256': 'ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa'},
                 'products': products,
                 'limits': ['Product definitions and ownership remain separate.',
                            'Exact source-carrier and tag bindings are in the external cohort asset.',
                            'Installing bytes does not adopt a consumer basis or establish arbitrary-query coverage.']}
    files['PRODUCTS.json'] = (json.dumps(inventory, indent=2) + '\n').encode()
    files['INSTALLATION.md'] = b'''# STDO 3.1 companion Products

Keep these five sibling directories together after extraction. Their explicit
public manifests and PRODUCTS.json inventory describe the delivered bytes.
Install the native Method separately using the published manager and manifest.

Start with stdo_skills/GETTING_STARTED.md and scripts/INSTALLATION.md for exact
Method/Purpose Context selection and fresh Codex/Claude installation. The package
already binds its distributed Purpose Context manifest. Select optional visual
support explicitly; it is not needed for context construction.

purpose_context/README.md explains purposes, unknown facts, source re-entry and
assessment boundaries. Its distribution catalog contains the two current 3.1
indexes. Source history retains older exact indexes; SOURCE_RELATION.json records
the distribution projection. Supplied assessment judgments apply only to their
exact subject and query, never to arbitrary work.

The historical 3.0.4/3.0.5 evidence links in purpose_context/README.md belong to
the full source catalog. Read those preserved files in the immutable source tag:
https://github.com/foolishimp/specification_methodology/tree/purpose_context%2Fv3.1.0-rc.2/purpose_context/skills/stdo-context/indexes
They are deliberately outside this two-index portable distribution.

For visual documentation, read a_c/INSTALLATION.md and
stdo_representation/INSTALLATION.md. The fresh STDO artifact covers ACTIVATION,
SDLC_DEFAULTS and TICKETS with explicit residuals. Axiom Indexer is an optional
mechanical conversion/validation/projection tool; read its INSTALLATION.md.

Publication does not change existing Product definitions, global skills or
installed consumers. Review the migration guides before selecting the new basis.
The old five-Product cohort updater is historical and does not migrate this bundle.
'''
    with zipfile.ZipFile(args.out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, (2026, 11, 15, 0, 0, 0))
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(entry, data)
    print(json.dumps({'archive': str(args.out), 'sha256': digest(args.out.read_bytes()),
                      'bytes': args.out.stat().st_size, 'products': {n: p['member_count'] for n, p in products.items()},
                      'inventory_sha256': digest(files['PRODUCTS.json'])}))


if __name__ == '__main__':
    main()
