"""Compare the narrow metadata successor with its exact frozen preimage."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ITERATION = HERE.parent
TENANT = ITERATION.parents[2]
PACKAGE = TENANT / 'successor/interpretation'
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HERE, text=True).strip())
PREIMAGE = 'b6ae34502fdc9eb6d8289db2db16d84650d2d2b2'
ACCOUNT = 'ed950af6ba3d1fea77088c9d2e19c2cce26c4b98bcc9be4ce317ce7fd4fc946b'
STANDING = 'Author conditional argument; source-specific specialization and policy are explicit; independent entailment/fidelity judgment remains separate.'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def old_bytes(path):
    return subprocess.check_output(['git', 'show', PREIMAGE + ':' + str(path.relative_to(REPO))], cwd=REPO)


def read(path):
    return json.loads(path.read_text())


def require(value, reason):
    if not value:
        raise ValueError(reason)


def remove_rows(document):
    ids = []
    for row in document['determinations']:
        argument = row.get('argument', {})
        if argument.get('standing') == STANDING:
            require(all(argument.get(k) for k in ('premises', 'conditional_consequence', 'policy_choices', 'source_refs')), 'Argument loses nonempty semantic content: ' + row['id'])
            del argument['standing']
            ids.append(row['id'])
    return ids


def remove_payloads(clauses):
    ids = []
    for row in clauses:
        for argument in row['arguments']:
            if argument['role'].endswith('#semantic-record'):
                value = json.loads(argument['literal'])
                if value.get('argument', {}).get('standing') == STANDING:
                    del value['argument']['standing']
                    argument['literal'] = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
                    ids.append(row['uri'])
    return ids


def main():
    original_account = ITERATION / 'DETERMINATIONS.json'
    require(sha(original_account.read_bytes()) == ACCOUNT, 'Original account changed')
    old = json.loads(old_bytes(PACKAGE / 'source-account.json'))
    current = read(PACKAGE / 'source-account.json')
    changed = remove_rows(old)
    require(len(changed) == 67 and old == current, 'Current account changes exceed the 67 permitted deletions')
    program = json.loads(old_bytes(PACKAGE / 'program.json'))
    changed_clauses = remove_payloads(program['clauses'])
    require(len(program['clauses']) == 734 and len(changed_clauses) == 67 and program == read(PACKAGE / 'program.json'), 'Native program changed beyond permitted metadata')
    logical_map = json.loads(old_bytes(PACKAGE / 'map.json'))
    current_map = read(PACKAGE / 'map.json')
    map_changed = remove_payloads(logical_map['clauses'])
    require(set(map_changed) == set(changed_clauses), 'Map payload changes differ from program')
    for field in ('program_sha256', 'map_sha256'):
        logical_map[field] = current_map[field]
    require(logical_map == current_map, 'Map graph, sources or other structure changed')
    source = json.loads(old_bytes(PACKAGE / 'SOURCE_INVENTORY.json'))
    current_source = read(PACKAGE / 'SOURCE_INVENTORY.json')
    for field in ('program_file_sha256', 'semantic_account_sha256'):
        source['interpretation'][field] = current_source['interpretation'][field]
    require(source == current_source, 'Source coordinates changed beyond derived digest updates')
    unchanged = ['MAPPING.json', 'FRAMES.md', 'SIGNATURE.md', 'README.md', 'bindings.py']
    for name in unchanged:
        require(old_bytes(PACKAGE / name) == (PACKAGE / name).read_bytes(), 'Unchanged carrier member drifted: ' + name)
    checker = ITERATION / 'check_interpretation.py'
    require(old_bytes(checker) == checker.read_bytes(), 'Prior mechanical checker changed')
    prior = read(HERE / 'current/MECHANICAL_RESULT.json')
    require(old_bytes(HERE / 'current/MECHANICAL_RESULT.json') == (HERE / 'current/MECHANICAL_RESULT.json').read_bytes(), 'Prior controls report was relabelled')
    projection_impact = []
    for selection in prior['selected_projections']:
        projection = read(ITERATION / prior['retained_evidence_directory'] / selection['files'][0])
        affected = sorted(set(projection['closure']['clauses']) & set(changed_clauses))
        projection_impact.append({'index': selection['index'], 'unchanged_closure_count': len(projection['closure']['clauses']),
                                  'metadata_affected_clauses': affected, 'preimage_measured_bytes': selection['bytes'],
                                  'successor_projection_bytes': 'not remeasured'})
    validation = read(HERE / 'current/validation.json')
    require(validation['status'] == 'valid' and not validation['diagnostics'], 'Successor native validation failed')
    report = {'kind': 'exact-metadata-successor-comparison', 'valid': True, 'preimage_commit': PREIMAGE,
        'original_account_unchanged_sha256': ACCOUNT, 'account_rows_compared': len(current['determinations']),
        'native_clauses_compared': len(program['clauses']), 'removed_field_count': len(changed),
        'removed_json_field': '/argument/standing', 'exact_removed_value': STANDING, 'affected_ids': changed,
        'semantic_arguments_and_shared_contracts': 'unchanged apart from the exact67 author-standing fields',
        'ids_operators_typed_edges_sources_indexes_and_native_map_adjacency': 'identical',
        'unchanged_package_members': unchanged, 'native_validation': 'fresh successor validation passed',
        'prior_controls_report_sha256': sha((HERE / 'current/MECHANICAL_RESULT.json').read_bytes()),
        'control_reuse_applicability': 'The same checker code and pinned native checker apply. Original sources/anchors/body pins, semantic IDs, all typed edges, local pointer targets, operators, index roots and relation/constraint kinds are identical. Only nonreferenced author-standing text is removed; fresh native validation binds the new payload/map digests. Prior13 controls remain evidence on their original subject with this exact applicability relation; they were not rerun or relabelled.',
        'projection_impact': projection_impact,
        'current_interpretation_package_bytes': sum(p.stat().st_size for p in PACKAGE.iterdir() if p.is_file()),
        'current_members': [{'path': p.name, 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())} for p in sorted(PACKAGE.iterdir()) if p.is_file()],
        'limits': ['No source-law or semantic-account author repair occurs here.', 'No new projection emission, semantic fidelity, actual-use, acceptance or release claim.']}
    (HERE / 'INTERPRETATION_METADATA_04.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'valid': True, 'removed_fields': len(changed), 'rows_compared': len(current['determinations']),
                      'native_clauses_compared': len(program['clauses']), 'package_bytes': report['current_interpretation_package_bytes']}))


if __name__ == '__main__':
    main()
