#!/usr/bin/env python3
"""Rebind unchanged authored content to an exact successor source coordinate set.

This operation is not authoring and does not issue a semantic or formal verdict.
It writes a new model and a complete invertible coordinate ledger. Independent
provider validation, derived views, review and formal evidence remain separate.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def file_ref(path):
    raw = path.read_bytes()
    return {'path': str(path.absolute()), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def coordinate_kind(path):
    """The finite declared paths, independently callable by release consumers."""
    patterns = (
        (r'/basis/subject/inventory/\d+/id', 'section'),
        (r'/external_resolutions/\d+/(external_identity|resolved_target_identity)', 'section'),
        (r'/identity_universe/\d+', 'section'),
        (r'/interpretation/dispositions/\d+/source', 'section'),
        (r'/populations/(objects/\d+/value|constraints/\d+/predicate|relations/\d+/qualifiers|latitude/\d+/(allowed_variation|forbidden_variation)|residuals/\d+/uncertainty)/grounding/\d+/path', 'path'),
        (r'/populations/(objects/\d+/value|constraints/\d+/predicate|relations/\d+/qualifiers|latitude/\d+/(allowed_variation|forbidden_variation)|residuals/\d+/uncertainty)/grounding/\d+/section', 'section'),
    )
    return next((kind for pattern, kind in patterns if re.fullmatch(pattern, path)), None)


def transform(predecessor, old_prefix, new_prefix, current_files, source_identity):
    """Return the unique allowed transform and ledger; refuse hidden prose edits."""
    require(old_prefix != new_prefix and old_prefix.endswith('/') and new_prefix.endswith('/'), 'distinct source-directory prefixes required')
    for prefix in (old_prefix, new_prefix):
        require(not Path(prefix).is_absolute() and all(p not in ('', '.', '..') for p in prefix.rstrip('/').split('/')), 'unsafe source prefix')
    require(len({row['path'] for row in current_files}) == len(current_files), 'duplicate source file')
    require(all(row['path'].startswith(new_prefix) for row in current_files), 'source inventory outside new prefix')
    old_files = [{**row, 'path': old_prefix + row['path'][len(new_prefix):]} for row in current_files]
    require(digest(old_files) == predecessor['basis']['subject']['sha256'], 'predecessor source inventory mismatch')
    require(digest(predecessor['interpretation']['dispositions']) == predecessor['interpretation']['selection_ledger']['sha256'], 'predecessor selection ledger mismatch')
    require(digest({'files': old_files, 'sections': predecessor['basis']['subject']['inventory']}) == predecessor['interpretation']['source_reentry']['sha256'], 'predecessor source reentry mismatch')
    model = copy.deepcopy(predecessor)
    subject = predecessor['basis']['subject']['id']
    old_sections = {row['id'] for row in predecessor['basis']['subject']['inventory']}
    section_prefix = subject.rstrip('/') + '/source/' + old_prefix
    require(all(s.startswith(section_prefix) and '#' in s for s in old_sections), 'source section outside declared prefix')
    source_paths = {row['path'] for row in old_files}
    ledger = []

    def visit(value, path=''):
        if isinstance(value, dict):
            return {key: visit(item, path + '/' + key.replace('~', '~0').replace('/', '~1')) for key, item in value.items()}
        if isinstance(value, list):
            return [visit(item, path + '/' + str(index)) for index, item in enumerate(value)]
        if not isinstance(value, str) or old_prefix not in value:
            return value
        kind = coordinate_kind(path)
        if kind == 'path':
            require(value in source_paths, 'unbound grounding file: ' + path)
            new = new_prefix + value[len(old_prefix):]
        elif kind == 'section':
            require(value in old_sections, 'unbound source section: ' + path)
            new = subject.rstrip('/') + '/source/' + new_prefix + value[len(section_prefix):]
        else:
            raise ValueError('old source prefix outside declared coordinate: ' + path)
        ledger.append({'path': path, 'old': value, 'new': new})
        return new

    model = visit(model)
    old_sha = model['basis']['subject']['sha256']; new_sha = digest(current_files)
    model['basis']['subject']['sha256'] = new_sha
    ledger.append({'path': '/basis/subject/sha256', 'old': old_sha, 'new': new_sha})
    derived = {
        'selection_ledger': digest(model['interpretation']['dispositions']),
        'source_reentry': digest({'files': current_files, 'sections': model['basis']['subject']['inventory']}),
    }
    for field, value in derived.items():
        coordinate = model['interpretation'][field]
        ledger.append({'path': '/interpretation/' + field + '/sha256', 'old': coordinate['sha256'], 'new': value})
        coordinate['sha256'] = value
    # The model identity is a function of the original exact model, new source S,
    # and finite coordinate ledger; no statement or arbitrary caller ID enters it.
    map_digest = digest({'predecessor_model_sha256': digest(predecessor),
                         'source_identity_sha256': source_identity, 'coordinates': ledger})
    identity = 'urn:a-c:coordinate-rebind:model:' + map_digest
    ledger.append({'path': '/id', 'old': model['id'], 'new': identity}); model['id'] = identity
    inverse = copy.deepcopy(model)
    for row in reversed(ledger):
        parts = [p.replace('~1', '/').replace('~0', '~') for p in row['path'].split('/')[1:]]
        parent = inverse
        for part in parts[:-1]:
            parent = parent[int(part)] if isinstance(parent, list) else parent[part]
        key = int(parts[-1]) if isinstance(parent, list) else parts[-1]
        require(parent[key] == row['new'], 'inverse coordinate differs')
        parent[key] = row['old']
    require(inverse['basis']['subject']['sha256'] == digest(old_files), 'inverse source inventory digest differs')
    require(inverse['interpretation']['selection_ledger']['sha256'] == digest(inverse['interpretation']['dispositions']), 'inverse selection ledger digest differs')
    require(inverse['interpretation']['source_reentry']['sha256'] == digest({'files': old_files, 'sections': inverse['basis']['subject']['inventory']}), 'inverse source reentry digest differs')
    require(canonical(inverse) == canonical(predecessor), 'inverse is not the exact predecessor')
    return model, ledger, map_digest


def verify_transform(predecessor, current, old_prefix, new_prefix, current_files, source_identity):
    """Reproduce the closed transform instead of accepting a caller patch ledger."""
    expected, ledger, map_digest = transform(predecessor, old_prefix, new_prefix, current_files, source_identity)
    require(canonical(current) == canonical(expected), 'current model differs from the permitted coordinate transform')
    return ledger, map_digest


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('predecessor', 'model-output', 'predecessor-source-freeze', 'source-freeze', 'current-source-inventory', 'source-root', 'report'):
        p.add_argument('--' + name, required=True, type=Path)
    p.add_argument('--old-source-prefix', required=True)
    p.add_argument('--new-source-prefix', required=True)
    args = p.parse_args(argv)
    try:
        inputs = [args.predecessor, args.predecessor_source_freeze, args.source_freeze, args.current_source_inventory]
        outputs = [args.model_output, args.report]
        require(len({x.resolve() for x in outputs}) == 2, 'output collision')
        require(all(not x.exists() and not x.is_symlink() and x.resolve() not in {i.resolve() for i in inputs} for x in outputs), 'output exists or aliases input')
        old = json.loads(args.predecessor_source_freeze.read_bytes()); new = json.loads(args.source_freeze.read_bytes())
        require(old['members'] == new['members'] and old['native_contracts'] == new['native_contracts'], 'semantic source members changed; reauthoring assessment required')
        inventory = json.loads(args.current_source_inventory.read_bytes())
        members = sorted(new['members'] + new['native_contracts'], key=lambda x: x['path'])
        expected = sorted([{'path': args.new_source_prefix + row['path'], 'sha256': row['sha256'], 'bytes': row['bytes']} for row in members], key=lambda x: x['path'])
        require(inventory == expected, 'current source inventory differs from exact freeze')
        source_root = args.source_root.resolve(strict=True)
        actual = set()
        for file in source_root.rglob('*'):
            require(not file.is_symlink(), 'source corpus contains a symlink')
            if file.is_file(): actual.add(file.relative_to(source_root).as_posix())
        require(actual == {row['path'] for row in members}, 'source corpus population differs')
        for row in members:
            observed = file_ref(source_root / row['path'])
            require((observed['sha256'], observed['bytes']) == (row['sha256'], row['bytes']), 'source bytes differ: ' + row['path'])
        predecessor = json.loads(args.predecessor.read_bytes())
        model, ledger, map_digest = transform(predecessor, args.old_source_prefix, args.new_source_prefix, inventory, new['source_identity_sha256'])
        raw = (json.dumps(model, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()
        report = {'kind': 'stdo-representation.coordinate-rebind/1', 'status': 'rebound', 'producer': file_ref(Path(__file__)),
                  'inputs': [file_ref(x) for x in inputs], 'source_identity_sha256': new['source_identity_sha256'],
                  'source_members_equal': len(members), 'old_source_prefix': args.old_source_prefix, 'new_source_prefix': args.new_source_prefix,
                  'predecessor_model': {'id': predecessor['id'], 'sha256': digest(predecessor)},
                  'current_model': {'id': model['id'], 'sha256': digest(model), 'raw_sha256': hashlib.sha256(raw).hexdigest()},
                  'coordinate_map_sha256': map_digest, 'coordinates': ledger, 'inverse_equal': True,
                  'claim': 'Exact coordinate-only rebind of prior authored content. No fresh authoring, semantic acceptance or formal-verification verdict.'}
        for path in outputs: path.parent.mkdir(parents=True, exist_ok=True)
        with args.model_output.open('xb') as stream: stream.write(raw)
        with args.report.open('x') as stream: json.dump(report, stream, ensure_ascii=False, indent=2, sort_keys=True); stream.write('\n')
        print(json.dumps({k: report[k] for k in ('kind', 'status', 'current_model', 'coordinate_map_sha256', 'source_members_equal', 'inverse_equal')}))
        return 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({'status': 'refused', 'reason': str(exc)})); return 2


if __name__ == '__main__':
    sys.exit(main())
