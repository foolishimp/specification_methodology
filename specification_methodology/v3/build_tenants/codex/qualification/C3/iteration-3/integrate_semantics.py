"""Integrate disjoint authored semantic contributions without changing source law."""
import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / 'successor'
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HERE, text=True).strip())
BASE_COMMIT = 'fe4fcbe'
BASE_SHA = 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
DOCUMENT_SOURCE = '6bcc4126efd54c41e412affc29e3801dc9deeb5b'
BASE_DOCUMENT_SOURCE = 'f2cb3e593757d094d008102551925e871a0204ff'
GROUPS = {
    'core': {'AXIOMATIC_CALCULUS', 'FOUNDATIONS', 'IDENTITY_METHOD', 'REFERENCE_FRAME_METHOD', 'STDO_REFERENCE_FRAME_BASELINE', 'TRANSFORMATION_LIBRARY'},
    'method': {'SPEC_METHOD', 'TICKET_METHOD', 'RELEASE_METHOD', 'POSTING_GUIDE', 'WRITING_GUIDE'},
    'construction': {'DESIGN_MODULE_METHOD', 'ODD_METHOD', 'TRAVERSAL_OCCURRENCE_PROFILE'},
    'model': {'WORLD_MODEL_METHOD', 'UX_METHOD'},
}
SEMANTIC_FIELDS = {
    'family', 'representation_kind', 'interpretation_standing', 'applicability',
    'predicate', 'definition', 'obligations', 'permissions_exceptions',
    'dependencies', 'dependency_relations', 'result_mapping', 'argument',
    'inputs', 'required_unknown_inputs', 'source_references', 'source_clause_ids',
    'semantic_roles', 'source_clause_roles',
    'signature_components', 'population_map', 'fields', 'closed_fields',
    'tuple', 'states', 'concept_identities',
    'contract_bindings', 'imported_concepts', 'translation', 'locator_meaning',
    'state_classifier', 'external_inputs',
    'decision_rule', 'function_contracts', 'causal_equation', 'compute_predicates',
    'semantic_cut', 'effect_predicates',
}
CONTRIBUTION_EVIDENCE_FIELDS = {
    'id', 'owner', 'owner_body_sha256', 'source_member_sha256',
    'unrepresented_scope', 'bounded_discriminator_projection', 'ready_row_repair',
    'proof_standing_ref',
    'prior_standing',
    'coverage_standing',
}
SHARED_FIELDS = {
    'shared_contracts': 'shared_contract',
    'owner_scopes': 'owner_scope',
    'external_input_catalog': 'input_contract',
    'shared_result_contracts': 'result_contract',
    'argument_contracts': 'argument_contract',
}
SHARED_REFERENCE_FIELDS = {'contract_ref', 'scope_ref', 'input_ref'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_text())


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n').encode()


def contribution(group):
    """Join named closed phases, preserving their original partial returns."""
    first = read(HERE / 'semantic-contributions' / group / 'bindings.json')
    if group != 'core':
        return first
    second = read(HERE / 'semantic-contributions/core/baseline/bindings.json')
    for row in (first, second):
        if row.get('source_commit') != BASE_DOCUMENT_SOURCE or row.get('input_account_sha256') != BASE_SHA:
            raise ValueError('Core continuation input mismatch')
    result = copy.deepcopy(first)
    result['bindings'] += second['bindings']
    represented = {r['id'] for r in result['bindings']}
    unfinished = []
    for part in (first, second):
        for key in ('unfinished_units', 'unfinished_ids', 'unfinished_source_ids', 'unresolved_construction_ids'):
            unfinished += [v if isinstance(v, str) else v['id'] for v in part.get(key, [])]
            result.pop(key, None)
    result['unfinished_ids'] = sorted(set(unfinished) - represented)
    result['shared_contracts'] = copy.deepcopy(first.get('shared_contracts', {}))
    for key, value in second.get('shared_contracts', {}).items():
        if key in result['shared_contracts'] and result['shared_contracts'][key] != value:
            raise ValueError('Core phases disagree on shared contract ' + key)
        result['shared_contracts'][key] = value
    result['phase_input_sha256'] = [sha(json_bytes(first)), sha(json_bytes(second))]
    return result


def base_account():
    data = subprocess.check_output(['git', 'show', BASE_COMMIT + ':' + str((HERE / 'DETERMINATIONS.json').relative_to(REPO))], cwd=REPO)
    if sha(data) != BASE_SHA:
        raise ValueError('Frozen account preimage mismatch')
    return json.loads(data)


def normalize(row, families):
    row = copy.deepcopy(row)
    if not row.get('applicability'):
        scope = row.get('applicability_ref') or row['owner']['path']
        if scope in families:
            row['applicability'] = families[scope].get('applicability')
    relations = list(row.get('dependency_relations') or [])
    dependencies = []
    for item in row.get('dependencies') or []:
        if isinstance(item, str):
            dependencies.append(item)
        else:
            target = item.get('id') or item.get('target') or item.get('target_id')
            if not target:
                raise ValueError(row['id'] + ': dependency has no target')
            dependencies.append(target)
            relations.append(dict(item, id=target))
    row['dependencies'] = sorted(set(dependencies))
    row['dependency_relations'] = list({json.dumps(v, sort_keys=True): v for v in relations}.values())
    if 'required_unknown_inputs' in row:
        # This is the returned, more specific input set, not an extension of an
        # older generic request to interpret the source.
        row['inputs'] = row.pop('required_unknown_inputs')
    if 'external_inputs' in row:
        row['inputs'] = row.pop('external_inputs')
    return row


def normalize_shared(contribution, group):
    """Give shared meanings exact identities; preserve references, not copies."""
    part = copy.deepcopy(contribution)
    contracts = {}
    for field, kind in SHARED_FIELDS.items():
        for key, value in part.get(field, {}).items():
            contracts[group + '.' + field + '.' + key] = dict(value, contract_kind=kind)

    def resolve(value, path=()):
        if isinstance(value, list):
            return [resolve(item, path) for item in value]
        if not isinstance(value, dict):
            return value
        result = {}
        for key, item in value.items():
            field = None
            if key == 'scope_ref' and 'owner_scopes' in part:
                field = 'owner_scopes'
            elif key == 'input_ref' and 'external_input_catalog' in part:
                field = 'external_input_catalog'
            elif key == 'contract_ref':
                if 'argument' in path and item in part.get('argument_contracts', {}):
                    field = 'argument_contracts'
                elif 'result_mapping' in path and item in part.get('shared_result_contracts', {}):
                    field = 'shared_result_contracts'
                elif item in part.get('shared_contracts', {}):
                    field = 'shared_contracts'
                else:
                    raise ValueError(group + ': unresolved shared contract ' + str(item))
            if field:
                target = group + '.' + field + '.' + item
                if target not in contracts:
                    raise ValueError(group + ': unresolved shared reference ' + target)
                result[key] = target
            else:
                result[key] = resolve(item, path + (key,))
        return result

    part['bindings'] = [resolve(row) for row in part['bindings']]
    contracts = {key: resolve(value) for key, value in contracts.items()}
    return part, contracts


def check_semantics(row):
    identifier = row['id']
    kind = row.get('representation_kind')
    if kind not in {'constraint', 'definition_data', 'consumer_binding', 'non_deciding_locator'}:
        raise ValueError(identifier + ': unknown representation kind')
    if kind == 'non_deciding_locator':
        if row.get('predicate'):
            raise ValueError(identifier + ': locator cannot assert a deciding predicate')
        return
    for field in ('applicability', 'result_mapping', 'argument'):
        if not row.get(field):
            raise ValueError(identifier + ': missing ' + field)
    if kind == 'constraint' and not row.get('predicate'):
        raise ValueError(identifier + ': deciding row lacks a predicate')
    if kind == 'consumer_binding' and not row.get('predicate') and not (row.get('definition') and row.get('dependencies')):
        raise ValueError(identifier + ': consumer lacks a predicate or defined owner relation')
    if kind == 'definition_data' and not (row.get('definition') or row.get('predicate')):
        raise ValueError(identifier + ': definition lacks semantic content')
    if any(word in str(row.get('interpretation_standing', '')) for word in ('pending', 'unfinished', 'unrepresented')):
        raise ValueError(identifier + ': source construction remains unfinished')
    for field in ('obligations', 'permissions_exceptions', 'dependencies'):
        if not isinstance(row.get(field), list):
            raise ValueError(identifier + ': ' + field + ' must be explicit')


def check_shared_references(value, contracts, subject):
    if isinstance(value, list):
        for item in value:
            check_shared_references(item, contracts, subject)
    elif isinstance(value, dict):
        for key, item in value.items():
            if key in SHARED_REFERENCE_FIELDS and item not in contracts:
                raise ValueError(subject + ': unresolved semantic reference ' + str(item))
            check_shared_references(item, contracts, subject)


def merge(base, contributions, carrier):
    result = copy.deepcopy(base)
    rows = {row['id']: row for row in result['determinations']}
    original_ids = set(rows)
    replacements = set()
    records, contracts = [], {}
    for group, contribution in contributions.items():
        if contribution.get('schema', contribution.get('schema_version')) != 'stdo.semantic-contribution.v1':
            raise ValueError(group + ': unsupported contribution schema')
        if contribution.get('input_account_sha256') != BASE_SHA or contribution.get('source_commit') != BASE_DOCUMENT_SOURCE:
            raise ValueError(group + ': contribution input drift')
        if any(contribution.get(k) for k in ('unresolved_construction_ids', 'unfinished_ids', 'unfinished_source_ids', 'unfinished_units')):
            raise ValueError(group + ': contributor returned unfinished work')
        contribution, shared = normalize_shared(contribution, group)
        for key, value in shared.items():
            if key in contracts and contracts[key] != value:
                raise ValueError('Conflicting shared semantic contract: ' + key)
            contracts[key] = value
        for binding in contribution['bindings']:
            identifier = binding['id']
            unknown_fields = set(binding) - SEMANTIC_FIELDS - CONTRIBUTION_EVIDENCE_FIELDS
            if unknown_fields:
                raise ValueError(identifier + ': unclassified contribution fields: ' + ', '.join(sorted(unknown_fields)))
            if identifier not in rows or identifier.split('.', 1)[0] not in GROUPS[group]:
                raise ValueError(group + ': out-of-territory or unknown ID ' + identifier)
            if identifier in replacements:
                raise ValueError('Duplicate semantic replacement: ' + identifier)
            if binding.get('unrepresented_scope'):
                raise ValueError(identifier + ': contributor preserves unfinished representation')
            original = rows[identifier]
            if binding.get('owner_body_sha256') != original['owner']['body_sha256']:
                raise ValueError(identifier + ': owner body preimage mismatch')
            semantic = {k: v for k, v in binding.items() if k in SEMANTIC_FIELDS}
            row = dict(original, **semantic)
            row.pop('remaining_work_ref', None)
            row.pop('unrepresented_scope', None)
            row['coverage_standing'] = 'bounded_author_binding'
            rows[identifier] = normalize(row, base['owner_families'])
            check_semantics(rows[identifier])
            replacements.add(identifier)
        input_names = ['semantic-contributions/' + group + '/bindings.json']
        if group == 'core':
            input_names.append('semantic-contributions/core/baseline/bindings.json')
        records.append({'group': group, 'bindings': len(contribution['bindings']),
                        'input_files': [{'path': name, 'sha256': sha((HERE / name).read_bytes())} for name in input_names],
                        'normalized_contribution_sha256': sha(json_bytes(contribution))})
    # Every pending source unit must receive a real returned semantic binding.
    pending = {row['id'] for row in base['determinations'] if row.get('coverage_standing') == 'source_carried_clause' and row.get('representation_kind') != 'non_deciding_locator'}
    if pending - replacements:
        raise ValueError('Unconstructed source units: ' + ', '.join(sorted(pending - replacements)))
    for identifier, row in list(rows.items()):
        rows[identifier] = normalize(row, base['owner_families'])
        check_semantics(rows[identifier])
    if carrier.get('input_account_sha256') != BASE_SHA or carrier.get('source_commit') != BASE_DOCUMENT_SOURCE:
        raise ValueError('Carrier input drift')
    for row in carrier['bindings']:
        identifier = row['id']
        if identifier in rows or not identifier.startswith('CARRIER.'):
            raise ValueError('Carrier identity collision: ' + identifier)
        row = normalize(row, {})
        row['coverage_standing'] = 'bounded_author_binding'
        check_semantics(row)
        rows[identifier] = row
    if not original_ids <= set(rows):
        raise ValueError('Original source unit erased')
    for row in rows.values():
        missing = set(row['dependencies']) - set(rows)
        if missing:
            raise ValueError(row['id'] + ': missing dependencies ' + ', '.join(sorted(missing)))
        check_shared_references(row, contracts, row['id'])
    for key, contract in contracts.items():
        check_shared_references(contract, contracts, key)
    inverse = {key: [] for key in rows}
    for row in rows.values():
        for dep in row['dependencies']:
            inverse[dep].append(row['id'])
    for key, row in rows.items():
        row['consumers'] = sorted(inverse[key])
    result['schema_version'] = 'stdo.determinations.v1.4'
    result['subject']['source_commit'] = DOCUMENT_SOURCE
    result['subject']['source_preimage'] = BASE_DOCUMENT_SOURCE
    result['determinations'] = [rows[key] for key in sorted(rows)]
    result['standing'] = 'Authored semantic construction; independent source fidelity and actual instance evidence are separate obligations.'
    result['construction_inputs'] = {'base_account_sha256': BASE_SHA, 'source_contributions': records, 'carrier_sha256': sha(json_bytes(carrier))}
    result['semantic_contracts'] = contracts
    pins = {m['path']: m for m in result['source_members']}
    for pin in carrier['additional_source_members']:
        pins[pin['path']] = pin
    result['source_members'] = [pins[key] for key in sorted(pins)]
    coverage = result['coverage']
    coverage['material_semantic_completeness'] = 'All declared source-account units have authored construction or an explicit nondeciding role; independent completeness and fidelity remain unassessed.'
    coverage['construction_complete'] = True
    coverage['source_units'] = len(rows)
    coverage['bounded_bindings'] = sorted(k for k, r in rows.items() if r['representation_kind'] != 'non_deciding_locator')
    coverage['source_carried_clauses'] = []
    coverage['source_bound_residuals'] = []
    coverage['owner_partition'] = [{'owner_path': p, 'binding_ids': sorted(k for k,r in rows.items() if r['owner']['path'] == p)} for p in sorted(pins)]
    coverage['outside_raw_standard_account'] = copy.deepcopy(carrier['package_member_classification'])
    # These changed summaries retain their old subject in the input account and
    # their new identity here. No deciding source or contribution was changed.
    for member in coverage['outside_raw_standard_account']:
        path = member['path']
        current = (PACKAGE / path).read_bytes()
        frozen = subprocess.check_output(['git', 'show', DOCUMENT_SOURCE + ':' + str((PACKAGE / path).relative_to(REPO))], cwd=REPO)
        if current != frozen:
            raise ValueError('Documentary drift: ' + path)
        if sha(current) != member['sha256'] and member['kind'] != 'source_bound_view':
            raise ValueError('Changed non-view carrier input: ' + path)
        member.update(sha256=sha(current), bytes=len(current))
    result.pop('remaining_work_contracts', None)
    result['limitations'] = ['This account supplies no instance truth, operation grant, independent review, acceptance or release.', 'Source-first semantic fidelity, complete material dependency sufficiency and actual use require independent evidence.', 'Preserved comparison and construction records are qualification evidence, excluded from the packaged semantic projection.']
    return result


def source_checks(account):
    members = {p['path']: p for p in account['source_members']}
    for path, pin in members.items():
        data = (PACKAGE / path).read_bytes()
        if sha(data) != pin['sha256']:
            raise ValueError('Source pin mismatch: ' + path)
    for row in account['determinations']:
        source = (PACKAGE / row['owner']['path']).read_bytes()
        if row['owner'].get('unit_scope') == 'whole_member' and sha(source) != row['owner']['body_sha256']:
            raise ValueError('Carrier body mismatch: ' + row['id'])
        for block in row.get('source_clauses', []):
            if sha(source[block['byte_start']:block['byte_end']]) != block['sha256']:
                raise ValueError('Clause body mismatch: ' + row['id'] + '#' + block['id'])


def integration_controls(base, contributions, carrier):
    """Counterexamples to data loss and false completeness at this boundary."""
    controls = []

    def refused(name, mutate, expected):
        changed = copy.deepcopy(contributions)
        mutate(changed)
        try:
            merge(base, changed, carrier)
        except ValueError as error:
            if expected not in str(error):
                raise ValueError(name + ': wrong refusal: ' + str(error)) from error
            controls.append({'case': name, 'result': str(error)})
        else:
            raise ValueError(name + ': unsafe integration succeeded')

    refused('Previously unclassified semantic field',
            lambda c: c['method']['bindings'][0].update(new_semantic_gate='must survive'),
            'unclassified contribution fields')
    pending = {r['id'] for r in base['determinations'] if r.get('coverage_standing') == 'source_carried_clause'}
    missing_id = next(r['id'] for r in contributions['method']['bindings'] if r['id'] in pending)
    refused('Missing source construction',
            lambda c: c['method'].update(bindings=[r for r in c['method']['bindings'] if r['id'] != missing_id]),
            'Unconstructed source units')
    refused('Changed owner preimage',
            lambda c: c['construction']['bindings'][0].update(owner_body_sha256='0' * 64),
            'owner body preimage mismatch')
    def missing_scope(c):
        r = next(r for r in c['model']['bindings'] if r.get('applicability', {}).get('scope_ref'))
        r['applicability']['scope_ref'] = 'absent-scope'
    refused('Dangling shared applicability', missing_scope, 'unresolved shared reference')
    def missing_dependency(c):
        c['method']['bindings'][0]['dependencies'].append('ABSENT.required-owner')
    refused('Dangling owner dependency', missing_dependency, 'missing dependencies')
    def missing_predicate(c):
        next(r for r in c['construction']['bindings'] if r['representation_kind'] == 'constraint')['predicate'] = None
    refused('Undecomposed deciding source', missing_predicate, 'deciding row lacks a predicate')
    return controls


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    contributions = {group: contribution(group) for group in GROUPS}
    carrier = read(HERE / 'semantic-contributions/carrier/bindings.json')
    base = base_account()
    account = merge(base, contributions, carrier)
    source_checks(account)
    report = {'valid': True, 'source_commit': DOCUMENT_SOURCE, 'count': len(account['determinations']),
              'kinds': dict(Counter(r['representation_kind'] for r in account['determinations'])),
              'sha256': sha(json_bytes(account)), 'independent_fidelity': 'unassessed'}
    if args.self_test:
        report['counterexamples'] = integration_controls(base, contributions, carrier)
    if args.write:
        (HERE / 'DETERMINATIONS.json').write_bytes(json_bytes(account))
        (HERE / 'SEMANTIC_INTEGRATION_CHECK.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
