"""Read-only consumer of the selected RC1 coordinate-rebind operation.

The authored predecessor stays historical. A closed owner transform and current
provider results establish source correspondence; no semantic verdict is inferred.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess

PRODUCER = 'stdo_representation/scripts/rebind_source_coordinates.py'
PREDECESSOR_MANIFEST = '84a0c3747f8915592a2a1628fa8227f6891d8389737fdc0c5a0e8c806d5c3c4f'
PREDECESSOR_MODEL = '0efcfe8ce9fb8c8abad1db75ee53982b50460d3048ff7060eb3c94ef5b472a2e'
PREDECESSOR_CARRIER = '2fe5f355e02ae77f70106126c098f210887a4b06'
OLD_PREFIX = 'build_tenants/a_c/representation/stdo-v3.0.5/source/'
NEW_PREFIX = 'build_tenants/a_c/representation/stdo-v3.0.5-rc.1/source/'


def verify(view, record, manifest, api):
    import stable_stack_release as s
    import stable_release_evidence as e
    facts, identity = e.model_facts(view, manifest, api)
    selected = facts['rebind']
    s.require(s.is_rc(manifest) and manifest['cohort']['cut'] == 'v3.0.5-rc.1' and
              record.get('operation') == 'coordinate_rebind', 'coordinate rebind is limited to its selected RC1 subject')
    predecessor_manifest = s.pinned(view, selected['predecessor_manifest'], api)
    s.require(selected['predecessor_manifest']['sha256'] == PREDECESSOR_MANIFEST, 'wrong original published cohort custody')
    s.require(api.git_bytes(view.root, PREDECESSOR_CARRIER + ':stack_release.json') ==
              s.pinned(view, selected['predecessor_manifest'], api, as_json=False), 'original published carrier/cohort differs')
    old_facts = predecessor_manifest['components']['representation']['facts']
    old = s.pinned(view, selected['predecessor_model'], api)
    current = s.pinned(view, facts['model'], api, as_json=False)
    emitted = selected['emitted_model']
    s.require(s.pinned(view, emitted, api, as_json=False) == current, 'actual rebound output differs from current canonical model')
    s.require(selected['predecessor_model']['sha256'] == old_facts['model']['sha256'] == PREDECESSOR_MODEL,
              'wrong exact authored predecessor model')
    old_source = s.pinned(view, selected['predecessor_source'], api)
    source = s.pinned(view, manifest['source'], api)
    s.require(selected['predecessor_source']['sha256'] == predecessor_manifest['source']['sha256'] and
              old_source['members'] == source['members'] and old_source['native_contracts'] == source['native_contracts'],
              'rebind changes the normative source population or bytes')
    # Preserve original producer and assessment custody; these are not new runs.
    prior_evidence = predecessor_manifest['components']['representation']['evidence']
    generation = s.pinned(view, prior_evidence['source_current_model'], api)
    semantic = s.pinned(view, prior_evidence['independent_semantic_review'], api)
    s.require(generation['claim'] == 'source_current_model' and generation['status'] == 'passed' and
              generation['source_identity_sha256'] == old_source['source_identity_sha256'] and
              old_facts['generated_model']['sha256'] == PREDECESSOR_MODEL,
              'authored predecessor generation custody differs')
    for ref in (generation['result'], generation['producer'], semantic['report']):
        s.pinned(view, ref, api, as_json=False)
    s.require(semantic['claim'] == 'independent_semantic_review' and semantic['conclusion'] == 'satisfied' and
              semantic['open_required_findings'] == [] and semantic['source_identity_sha256'] == old_source['source_identity_sha256'],
              'predecessor bounded assessment custody differs')
    s.require((selected['old_source_prefix'], selected['new_source_prefix']) == (OLD_PREFIX, NEW_PREFIX),
              'unselected source-coordinate mapping')
    root = 'stdo_representation/' + NEW_PREFIX.rstrip('/')
    s.require(selected['source_root'] == root and facts['source_copy_prefix'] == NEW_PREFIX,
              'current source-copy route differs')
    rows = source['members'] + source['native_contracts']
    inventory = s.pinned(view, selected['current_source_inventory'], api)
    expected = sorted([{**row, 'path': NEW_PREFIX + row['path']} for row in rows], key=lambda row: row['path'])
    s.require(inventory == expected and set(view.files(root)) == {root + '/' + row['path'] for row in rows},
              'rebind source corpus is not the exact current closure')
    for row in rows:
        s.pinned(view, {**row, 'path': root + '/' + row['path']}, api, as_json=False)
    old_root = 'stdo_representation/' + OLD_PREFIX.rstrip('/')
    def modes(revision, prefix):
        lines = api.git(view.root, 'ls-tree', '-r', revision, '--', prefix).stdout.splitlines()
        return {line.split('\t', 1)[1][len(prefix) + 1:]: line.split(' ', 1)[0] for line in lines}
    old_modes = modes(PREDECESSOR_CARRIER, old_root)
    current_modes = modes(view.revision, root) if view.revision else {
        row['path']: ('100755' if (view.root / root / row['path']).stat().st_mode & 0o111 else '100644') for row in rows}
    s.require(set(old_modes) == {row['path'] for row in rows} and old_modes == current_modes,
              'rebound source copy modes differ from the exact published predecessor')
    inputs = [selected['predecessor_model'], selected['predecessor_source'], manifest['source'], selected['current_source_inventory']]
    locate = lambda ref: e.artifact_location(view, ref, api)
    report = s.pinned(view, selected['report'], api)
    args = ['--predecessor', locate(inputs[0]), '--model-output', locate(emitted),
            '--predecessor-source-freeze', locate(inputs[1]), '--source-freeze', locate(inputs[2]),
            '--current-source-inventory', locate(inputs[3]), '--source-root', str(view.root.absolute() / root),
            '--old-source-prefix', OLD_PREFIX, '--new-source-prefix', NEW_PREFIX, '--report', locate(selected['report'])]
    result = e.execution(view, record, api, PRODUCER, args, inputs=inputs)
    s.require(any(row['path'] == emitted['path'] and row['sha256'] == emitted['sha256'] for row in record['execution']['outputs']) and
              any(row['path'] == selected['report']['path'] and row['sha256'] == selected['report']['sha256'] for row in record['execution']['outputs']),
              'rebound model/report must be actual produced artifacts')
    owner_members = {row['path']: row for row in manifest['products']['stdo_representation']['subject']['members']}
    s.require(owner_members[PRODUCER]['sha256'] == record['producer']['sha256'] and
              report['producer'] == {'path': locate(record['producer']), 'sha256': record['producer']['sha256'],
                                     'bytes': len(s.pinned(view, record['producer'], api, as_json=False))},
              'rebind owner producer differs from selected Product source')
    s.require(report['inputs'] == [{'path': locate(ref), 'sha256': ref['sha256'], 'bytes': len(s.pinned(view, ref, api, as_json=False))} for ref in inputs],
              'rebind report input provenance differs')
    # Invoke only the fixed, pinned owner's read-only closed transform. Its
    # finite coordinate rules and derived hashes are not caller-defined patches.
    code = ('import importlib.util,json,sys;from pathlib import Path;'
            'spec=importlib.util.spec_from_file_location("rebind_owner",sys.argv[1]);'
            'm=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);'
            'load=lambda p:json.loads(Path(p).read_bytes());'
            'ledger,identity=m.verify_transform(load(sys.argv[2]),load(sys.argv[3]),sys.argv[4],sys.argv[5],load(sys.argv[6]),sys.argv[7]);'
            'print(json.dumps({"coordinate_map_sha256":identity,"ledger_sha256":m.digest(ledger)}))')
    python = e.python_identity(record['execution']['environment']['python'], api)
    checked = subprocess.run([python, '-I', '-B', '-c', code, locate(record['producer']), locate(inputs[0]), locate(facts['model']),
                              OLD_PREFIX, NEW_PREFIX, locate(inputs[3]), source['source_identity_sha256']],
                             capture_output=True, timeout=120)
    s.require(checked.returncode == 0 and json.loads(checked.stdout) == {
        'coordinate_map_sha256': report['coordinate_map_sha256'], 'ledger_sha256': api.canonical_value_sha256(report['coordinates'])},
        'current model/ledger is not the reproduced closed coordinate transform')
    expected_result = {'kind': 'stdo-representation.coordinate-rebind/1', 'status': 'rebound',
                       'current_model': {**identity, 'raw_sha256': facts['model']['sha256']},
                       'coordinate_map_sha256': report['coordinate_map_sha256'], 'source_members_equal': len(rows), 'inverse_equal': True}
    expected_result['current_model'].pop('profile', None)
    s.require(result == expected_result and all(report[key] == value for key, value in expected_result.items()) and
              report['source_identity_sha256'] == source['source_identity_sha256'] and
              (report['old_source_prefix'], report['new_source_prefix']) == (OLD_PREFIX, NEW_PREFIX) and
              report['predecessor_model'] == {'id': old['id'], 'sha256': api.canonical_value_sha256(old)},
              'rebind execution/result identity differs')
    binding = s.pinned(view, facts['current_binding'], api)
    s.require(binding['source_identity_sha256'] == manifest['source']['source_identity_sha256'] and
              binding['source_freeze_raw_sha256'] == manifest['source']['sha256'] and
              binding['model_raw_sha256'] == facts['model']['sha256'] and binding['model_identity'] == identity,
              'rebound current model source binding differs')
    for field, command, extras, inputs in (
        ('owner_validation', 'validate', [], [facts['model']]),
        ('owner_materialization', 'materialize', ['--out', locate(facts['carrier'])], [facts['model']]),
        ('owner_decode', 'decode', ['--out', locate(selected['decoded_model'])], [facts['carrier']]),
    ):
        child = s.pinned(view, selected[field], api)
        path = locate(facts['carrier'] if command == 'decode' else facts['model'])
        value = e.execution(view, child, api, e.GRAPH, [command, path, *extras], inputs=inputs)
        s.require(value.get('model') == identity and value.get('status') == {
            'validate': 'structurally-checked', 'materialize': 'proposal-view', 'decode': 'decoded'}[command], 'current provider model/carrier relation differs')
        if command != 'validate':
            produced = facts['carrier'] if command == 'materialize' else selected['decoded_model']
            s.require(any(row['path'] == produced['path'] and row['sha256'] == produced['sha256'] for row in child['execution']['outputs']),
                      'current carrier/decode was not the selected actual output')
    s.require(api.canonical_value_sha256(s.pinned(view, selected['decoded_model'], api)) == identity['sha256'],
              'current carrier does not recover the exact rebound model')
