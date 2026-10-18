"""Integrate frozen authored I5 changes over the exact own I4 account.

This tool authenticates source coordinates and explicit patch coverage. It does
not infer source meaning, author missing rows, coarsen lost blocks, or assess
fidelity. Source-dependent publication is a later separately frozen step.
"""
import argparse
import copy
import json
from pathlib import Path

import build_interpretation as build
from account_protocol import PROTOCOL, heading_units, source_path, make_owner
from context import HERE, PRIOR, PACKAGE, REPO, INPUTS, encoded, exact_source, git_bytes, read, sha, verify_common, write


def body(owner, raw):
    if owner.get('unit_scope') == 'whole_member':
        return raw, 0, len(raw)
    try:
        unit = heading_units(raw)[owner['anchor']]
    except KeyError as error:
        raise ValueError('Missing owned heading: ' + owner['path'] + '#' + owner['anchor']) from error
    return unit['body'], unit['byte_start'], unit['byte_end']


def rebind_owner(owner, raw):
    if owner.get('unit_scope') == 'whole_member':
        result = {'path': owner['path'], 'anchor': '', 'unit_scope': 'whole_member', 'body_sha256': sha(raw)}
    else:
        result = make_owner(owner['path'], owner['anchor'], raw)
    for key in ('member_sha256', 'sha256'):
        if key in owner:
            result[key] = sha(raw)
    return result


def relocate_blocks(row, previous, old_raw, new_raw, explicitly_replaced):
    """Retain unchanged block identity only where its exact bytes survive once."""
    _, start, end = body(row['owner'], new_raw)
    current = new_raw[start:end]
    old_blocks = {b['id']: b for b in previous.get('source_clauses', [])}
    for block in row.get('source_clauses', []):
        if explicitly_replaced:
            if not (start <= block['byte_start'] <= block['byte_end'] <= end):
                raise ValueError('Authored block escapes owned section: ' + row['id'])
            if sha(new_raw[block['byte_start']:block['byte_end']]) != block['sha256']:
                raise ValueError('Authored block pin differs: ' + row['id'] + '#' + block['id'])
        else:
            old = old_blocks.get(block['id'])
            if not old:
                raise ValueError('Block insertion was not explicitly authored: ' + row['id'])
            fragment = old_raw[old['byte_start']:old['byte_end']]
            if not fragment or sha(fragment) != old['sha256']:
                raise ValueError('Prior block pin differs: ' + row['id'] + '#' + block['id'])
            # Historical explicit blocks may span more than the immediate
            # heading. Preserve their actual source scope, never narrow it by
            # the integration tool's representation assumption.
            if old_raw == new_raw:
                at = old['byte_start']
            else:
                _, old_start, old_end = body(previous['owner'], old_raw)
                within_owner = old_start <= old['byte_start'] <= old['byte_end'] <= old_end
                search, offset = (current, start) if within_owner else (new_raw, 0)
                if search.count(fragment) != 1:
                    raise ValueError('Changed or ambiguous block needs authored replacement: ' + row['id'] + '#' + block['id'])
                at = offset + search.index(fragment)
            if new_raw[at:at + len(fragment)] != fragment:
                raise ValueError('Changed or ambiguous block needs authored replacement: ' + row['id'] + '#' + block['id'])
            block.update(byte_start=at, byte_end=at + len(fragment), sha256=sha(fragment))
    blocks = {b['id']: b for b in row.get('source_clauses', [])}
    for role in row.get('source_clause_roles', []):
        block = blocks.get(role['source_block_id'])
        if not block or role['source_clause_id'] != row['id'] + '#' + block['id']:
            raise ValueError('Authored clause role lost its block: ' + row['id'])
        role.update(source_block_sha256=block['sha256'], source_byte_start=block['byte_start'], source_byte_end=block['byte_end'])


def rebind_argument_rows(value, source, source_commit, changes, identifier):
    """A table row may move; its content is never silently reauthored."""
    if isinstance(value, list):
        for child in value:
            rebind_argument_rows(child, source, source_commit, changes, identifier)
    elif isinstance(value, dict):
        record = value.get('source_row')
        if isinstance(record, dict) and all(k in record for k in ('path', 'anchor', 'sha256')):
            raw = source.get(record['path'])
            if raw is None:
                raise ValueError('Unselected argument source: ' + record['path'])
            unit = heading_units(raw).get(record['anchor'])
            if unit is None:
                raise ValueError('Missing argument heading: ' + identifier)
            hits = [i for i, line in enumerate(unit['body'].splitlines(keepends=True))
                    if sha(line) == record['sha256'] or sha(line.rstrip(b'\r\n')) == record['sha256']]
            if len(hits) != 1:
                raise ValueError('Changed argument row needs explicit consumer patch: ' + identifier + '/' + record['anchor'])
            before = copy.deepcopy(record)
            if 'line' in record:
                record['line'] = unit['start_line'] + hits[0]
            if 'member_sha256' in record:
                record['member_sha256'] = sha(raw)
            if 'source_commit' in record:
                record['source_commit'] = source_commit
            if record != before:
                changes.append({'id': identifier, 'before': before, 'after': copy.deepcopy(record)})
        for child in value.values():
            rebind_argument_rows(child, source, source_commit, changes, identifier)


def validate_patch(patch):
    if patch.get('schema_version') != PROTOCOL:
        raise ValueError('Unknown authored patch protocol')
    for key, expected in [('common_input', INPUTS['common_input']), ('source_preimage', INPUTS['starting_tenant'])]:
        if patch.get(key) != expected:
            raise ValueError('Patch basis differs: ' + key)
    if not patch.get('producer') or not isinstance(patch.get('owner_paths'), list) or not patch['owner_paths']:
        raise ValueError('Patch lacks producer or owner territory')
    for path in patch['owner_paths']:
        source_path(path)
    for key in ('updates', 'new_rows'):
        if not isinstance(patch.get(key), list):
            raise ValueError('Patch needs an explicit ' + key + ' array')


def integrate(prior, old_source, source, patches, source_commit):
    account = copy.deepcopy(prior)
    previous = {r['id']: r for r in prior['determinations']}
    rows = {k: copy.deepcopy(v) for k, v in previous.items()}
    updates, insertions, producers = {}, {}, {}
    permitted = build.SEMANTIC_FIELDS | build.EVIDENCE_FIELDS
    for patch in patches:
        validate_patch(patch)
        for item in patch['updates']:
            identifier = item['id']
            if identifier not in previous:
                raise ValueError('Update has no I4 row; use explicit new_rows: ' + identifier)
            if identifier in updates or identifier in insertions:
                raise ValueError('Overlapping authored row: ' + identifier)
            if previous[identifier]['owner']['path'] not in patch['owner_paths']:
                raise ValueError('Update escapes producer owner territory: ' + identifier)
            fields = item.get('semantic_fields')
            if not isinstance(fields, dict) or not fields:
                raise ValueError('Empty authored update: ' + identifier)
            if set(fields) - permitted or set(fields) & {'id', 'owner'}:
                raise ValueError('Unknown or identity-changing authored fields: ' + identifier)
            updates[identifier] = item
            producers[identifier] = patch['producer']
        for row in patch['new_rows']:
            identifier = row['id']
            if identifier in rows or identifier in insertions or identifier in updates:
                raise ValueError('Duplicate authored new identity: ' + identifier)
            if row.get('owner', {}).get('path') not in patch['owner_paths']:
                raise ValueError('New row escapes producer owner territory: ' + identifier)
            if set(row) - permitted or not row.get('owner', {}).get('body_sha256'):
                raise ValueError('Unclassified or unpinned new row: ' + identifier)
            for key in ('family', 'representation_kind', 'source_clauses'):
                if key not in row:
                    raise ValueError('New row lacks ' + key + ': ' + identifier)
            insertions[identifier] = copy.deepcopy(row)
            producers[identifier] = patch['producer']
    changes, coordinates, support_changes, argument_moves = [], [], [], []
    for identifier, row in rows.items():
        original = previous[identifier]
        path = original['owner']['path']
        before, _, _ = body(original['owner'], old_source[path])
        after, _, _ = body(original['owner'], source[path])
        item = updates.get(identifier)
        if before != after and item is None:
            raise ValueError('Changed owned source has no authored patch: ' + identifier)
        if item:
            if item.get('preimage_body_sha256') != sha(before) or item.get('candidate_body_sha256') != sha(after):
                raise ValueError('Authored source preimage/current pin differs: ' + identifier)
            row.update(copy.deepcopy(item['semantic_fields']))
            changes.append({'id': identifier, 'producer': producers[identifier],
                            'fields': sorted(item['semantic_fields']), 'before_body_sha256': sha(before), 'body_sha256': sha(after)})
        owner = rebind_owner(original['owner'], source[path])
        if owner != original['owner']:
            coordinates.append(identifier)
        row['owner'] = owner
        if 'owner_body_sha256' in row:
            row['owner_body_sha256'] = owner['body_sha256']
        if 'source_member_sha256' in row:
            row['source_member_sha256'] = sha(source[path])
        relocate_blocks(row, original, old_source[path], source[path], bool(item and 'source_clauses' in item['semantic_fields']))
        for n, support in enumerate(row.get('supporting_sources', [])):
            path = support['path']
            rebound = rebind_owner(support, source[path])
            if support.get('body_sha256') and support['body_sha256'] != rebound['body_sha256']:
                support_changes.append({'id': identifier, 'owner': rebound,
                                        'standing': 'current coordinates; changed support applicability requires assessment'})
            row['supporting_sources'][n] = rebound
    for identifier, row in insertions.items():
        path = row['owner']['path']
        actual = rebind_owner(row['owner'], source[path])
        if actual['body_sha256'] != row['owner']['body_sha256']:
            raise ValueError('Authored new owner pin differs: ' + identifier)
        row['owner'] = actual
        relocate_blocks(row, {}, b'', source[path], True)
        rows[identifier] = row
    for identifier, row in rows.items():
        rebind_argument_rows(row, source, source_commit, argument_moves, identifier)
    represented = {}
    for row in rows.values():
        represented.setdefault((row['owner']['path'], row['owner'].get('anchor', '')), []).append(row['id'])
    heading_inventory = []
    for path, raw in source.items():
        old_units = heading_units(old_source.get(path, b''))
        for anchor, unit in heading_units(raw).items():
            row_ids = represented.get((path, anchor), [])
            if anchor not in old_units and not row_ids:
                raise ValueError('New source heading has no authored determination: ' + path + '#' + anchor)
            heading_inventory.append({'path': path, 'anchor': anchor, 'body_sha256': sha(unit['body']),
                                      'determination_ids': row_ids,
                                      'standing': 'represented; fidelity unassessed' if row_ids else 'inherited unrepresented/structural scope; not a semantic pass'})
    account['determinations'] = sorted(rows.values(), key=lambda r: r['id'])
    member_records = {m['path']: copy.deepcopy(m) for m in account.get('source_members', [])}
    for path, raw in source.items():
        member_records.setdefault(path, {'path': path}).update(sha256=sha(raw), bytes=len(raw))
    account['source_members'] = sorted(member_records.values(), key=lambda m: m['path'])
    account['coverage'] = {'prior_subject': copy.deepcopy(prior.get('subject')),
                           'prior_coverage': copy.deepcopy(prior.get('coverage')),
                           'current_heading_inventory': heading_inventory,
                           'new_rows': sorted(insertions), 'updated_rows': sorted(updates),
                           'standing': 'explicit source-coordinate account; complete semantic coverage not established'}
    account['subject'] = {'source_commit': source_commit, 'common_input': INPUTS['common_input'],
                          'source_preimage': INPUTS['starting_tenant'], 'activation': 'EC-CODEX-I5-01',
                          'installed_builder': INPUTS['installed_builder'], 'manifest_sha256': INPUTS['manifest_sha256']}
    account['standing'] = 'Current I5 authored construction account; no independent fidelity or acceptance judgment.'
    report = {'source_commit': source_commit, 'prior_subject': prior.get('subject'),
              'direct_patches': changes, 'new_rows': sorted(insertions), 'coordinate_updates': coordinates,
              'argument_row_coordinate_changes': argument_moves, 'changed_support_requiring_assessment': support_changes,
              'rows': len(rows), 'source_heading_inventory_rows': len(heading_inventory),
              'limits': ['Source pins and explicit authored coverage are not semantic fidelity.',
                         'Inherited coverage keeps its prior subject; no historical review is repinned.',
                         'Changed supporting sources require applicability assessment before evidence reuse.']}
    return account, report


def frozen_patch(selector):
    commit, relative = selector.split(':', 1)
    path = HERE / relative
    if Path(relative).is_absolute() or '..' in Path(relative).parts or not relative.startswith('source/'):
        raise ValueError('Patch must be an I5 source return')
    raw = git_bytes(commit, path.relative_to(REPO))
    if path.read_bytes() != raw:
        raise ValueError('Patch differs from its selected frozen return: ' + relative)
    return json.loads(raw), {'path': relative, 'commit': commit, 'sha256': sha(raw)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--patch', action='append', required=True, help='Exact commit:I5-relative source/.../ACCOUNT_PATCH.json')
    args = parser.parse_args()
    verify_common()
    _, documentary_members = exact_source(args.source_commit)
    prior_path = PRIOR / 'DETERMINATIONS.json'
    prior_raw = git_bytes(INPUTS['prior_account_commit'], prior_path.relative_to(REPO))
    if prior_raw != prior_path.read_bytes():
        raise ValueError('Historical I4 account changed')
    prior = json.loads(prior_raw)
    patches, selected = [], []
    for selector in args.patch:
        patch, record = frozen_patch(selector)
        patches.append(patch); selected.append(record)
    paths = {r['owner']['path'] for r in prior['determinations']}
    paths |= {s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', [])}
    paths |= {p for patch in patches for p in patch['owner_paths']}
    old_source, source = {}, {}
    for path in paths:
        source_path(path)
        old_source[path] = git_bytes(INPUTS['starting_tenant'], (PACKAGE / path).relative_to(REPO))
        source[path] = (PACKAGE / path).read_bytes()
    account, report = integrate(prior, old_source, source, patches, args.source_commit)
    account['source_members'] = documentary_members
    current, excluded = build.semantic_projection(account)
    build.validate_account(current)
    report.update(common_input=INPUTS['common_input'], prior_account_commit=INPUTS['prior_account_commit'],
                  prior_account_sha256=sha(prior_raw), patch_inputs=selected,
                  excluded_construction_metadata_count=len(excluded),
                  validation='authored source pins, block integrity, semantic references and explicit new heading coverage passed')
    write(HERE / 'DETERMINATIONS.json', account)
    write(HERE / 'ACCOUNT_INTEGRATION.json', report)
    print(json.dumps({'rows': len(current['determinations']), 'new_rows': len(report['new_rows']),
                      'updated_rows': len(report['direct_patches']), 'source_commit': args.source_commit}))


if __name__ == '__main__':
    main()
