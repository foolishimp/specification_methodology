#!/usr/bin/env python3
"""Check current Product routing and exact public bindings; not release qualification."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    inventory = json.loads((ROOT / 'DEVELOPMENT_PRODUCTS.json').read_text())
    failures = []
    if inventory.get('kind') != 'stdo.development-product-navigation/1' or len(inventory['products']) != 6:
        failures.append('Expected the explicit six-Product development navigation')
    for product in inventory['products']:
        if 'public_manifest_sha256' in product:
            try:
                actual = hashlib.sha256((ROOT / product['public_manifest']).read_bytes()).hexdigest()
                if actual != product['public_manifest_sha256']:
                    failures.append('Stale navigation public manifest: ' + product['name'])
            except (OSError, KeyError, TypeError):
                failures.append('Missing navigation public manifest: ' + product['name'])
        for root in product['roots']:
            if not (ROOT / root / 'README.md').is_file():
                failures.append('Missing Product source root: ' + root)
        for definition in product['definitions']:
            try:
                value = json.loads((ROOT / definition).read_text())
                if value['kind'] != 'stdo.product-definition':
                    failures.append('Invalid Product Definition: ' + definition)
            except (OSError, ValueError, KeyError):
                failures.append('Missing or malformed Product Definition: ' + definition)
    adapter = ROOT / 'stdo_skills/skills/stdo-context'
    for host in ['.agents', '.claude']:
        selected = ROOT / host / 'skills/stdo-context'
        if not selected.is_symlink() or selected.resolve() != adapter:
            failures.append('Incorrect root Skills discovery route: ' + host)
        for retired in ['stdo-representation', 'axiomatize-corpus']:
            p = ROOT / host / 'skills' / retired
            if p.exists() or p.is_symlink():
                failures.append('Retired root route remains: ' + str(p.relative_to(ROOT)))
    for retired in ['stdo_skills/skills/stdo-context/scripts/context.py',
                    'stdo_skills/skills/stdo-context/scripts/covering_index.py',
                    'stdo_skills/scripts/package_305.py',
                    'specification_methodology/v3/build_tenants/common-tools',
                    'scripts/check_stack_release.py']:
        if (ROOT / retired).exists():
            failures.append('Retired active implementation remains: ' + retired)
    method = json.loads((ROOT / 'specification_methodology/v3/stdo_3.json').read_text())
    if any('common-tools' in p for tenant in method['how']['build_tenants'] for p in tenant.get('implementation', [])):
        failures.append('Method still registers the retired constructor family')
    spec = importlib.util.spec_from_file_location('skills_binding', adapter / 'scripts/provider.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    try:
        path, value = module.configuration()
        components = {}
        for name in ['purpose_context', 'visual']:
            root, manifest = module.component(value, name, path)
            components[name] = {'product_definition_id': manifest['product_definition_id'],
                                'manifest_sha256': value['components'][name]['manifest_sha256']}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures.append(str(exc)); components = {}
    print(json.dumps({'status': 'checked' if not failures else 'refused',
                      'scope': 'finite current source routing and public dependency identity only',
                      'products': len(inventory['products']), 'components': components,
                      'failures': failures,
                      'limits': ['No semantic completeness', 'No native host pickup', 'No release qualification']}, indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
