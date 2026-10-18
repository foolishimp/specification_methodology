"""Apply explicit I4 author patches and relocate surviving source blocks.

The preimage account and I3 evidence stay untouched. A changed deciding source
without an authored patch refuses; pin refresh cannot invent its interpretation.
The original native dependency classification and local-pointer rules are kept.
"""
import argparse
import copy
from context import HERE, PRIOR, REPO, PACKAGE, INPUTS, encoded, git_bytes, library, read, sha, write


def update_path(target, path, value):
    keys = path.split('.')
    for key in keys[:-1]:
        target = target.setdefault(key, {})
    target[keys[-1]] = copy.deepcopy(value)


def get_path(target,path):
    for key in path.split('.'):
        if not isinstance(target,dict):
            return None
        target=target.get(key)
    return target


def owned_family(entry,scope):
    owners={(x['path'],x['anchor']) for x in scope['owned_source_rows']}
    source=entry.get('source_row',{})
    if (source.get('path'),source.get('anchor')) in owners:
        return True
    legacy=set(scope.get('legacy_source_refs',[]))
    return any(isinstance(x,str) and x in legacy for x in entry.get('source_refs',[]))


def scoped_operations(item):
    result=copy.deepcopy(item.get('scoped_replacements',{}))
    for path,spec in item.get('family_array_scopes',{}).items():
        if (spec['operation']!='replace_matching_origins' or
            not spec['preserve_other_current_families']):
            raise ValueError('Unknown profile family operation')
        result[path]={'mode':'replace_owned_source_rows_preserving_current_other_entries',
            'owned_source_rows':[{'path':x['path'],'anchor':x['anchor']} for x in spec['origins']],
            'legacy_source_refs':[x['id'] for x in spec['origins']]}
    return result


def bind_family_rows(value, identifier, source_commit, repair, cache, changes):
    """Rebind coordinates only after the exact authored row survives uniquely."""
    if isinstance(value,list):
        for child in value:
            bind_family_rows(child,identifier,source_commit,repair,cache,changes)
    elif isinstance(value,dict):
        record=value.get('source_row')
        if isinstance(record,dict) and all(k in record for k in ('path','anchor','sha256')):
            path=record['path']
            if path not in cache:
                raw=(PACKAGE/path).read_bytes()
                cache[path]=(raw,repair.heading_units(raw))
            raw,units=cache[path]
            unit=units.get(record['anchor'])
            if unit is None:
                raise ValueError('Missing argument-row owner: '+identifier)
            hits=[i for i,line in enumerate(unit['body'].splitlines(keepends=True))
                  if sha(line)==record['sha256'] or sha(line.rstrip(b'\r\n'))==record['sha256']]
            if len(hits)!=1:
                raise ValueError('Stale or ambiguous argument row: '+identifier+'/'+record['anchor'])
            before=copy.deepcopy(record)
            if 'line' in record:
                record['line']=unit['start_line']+hits[0]
            if 'member_sha256' in record:
                record['member_sha256']=sha(raw)
            if 'source_commit' in record:
                record['source_commit']=source_commit
            if record!=before:
                changes.append({'id':identifier,'before':before,'after':copy.deepcopy(record)})
        for child in value.values():
            bind_family_rows(child,identifier,source_commit,repair,cache,changes)


def authored_fields(item, row):
    """Normalize the three returned patch dialects without inferring semantics."""
    result = copy.deepcopy(row)
    for key, value in item.get('semantic_fields', {}).items():
        result[key] = copy.deepcopy(value)
    for key, value in item.get('set', {}).items():
        update_path(result, key, value)
    for path,scope in scoped_operations(item).items():
        if scope['mode']!='replace_owned_source_rows_preserving_current_other_entries':
            raise ValueError('Unknown scoped-family operation')
        old=get_path(row,path) or []
        incoming=get_path(result,path) or []
        update_path(result,path,[x for x in old if not owned_family(x,scope)] +
                    [x for x in incoming if owned_family(x,scope)])
    for key, values in item.get('append_unique', {}).items():
        target = result.setdefault(key, [])
        for value in values:
            if value not in target:
                target.append(copy.deepcopy(value))
    argument = result.setdefault('argument', {})
    if item.get('replace_table_argument_scope'):
        argument['premises'] = [{'id': 'FOUNDATIONS.foundational-commitments',
            'binding': 'Applicable subsets and instance premises are stated separately in each source_table_scope row.'}]
        if 'argument.conditional_consequence' not in item.get('set', {}):
            argument['conditional_consequence'] = 'Each source_table_scope row states its conditional consequence and additional owned choice for the named consumers.'
    if item.get('argument_addition') and not item.get('replace_table_argument_scope'):
        argument['source_explanation'] = item['argument_addition']
    if item.get('source_family_rows'):
        argument['source_table_scope'] = copy.deepcopy(item['source_family_rows'])
        argument['source_table_scope']['required_when'] = 'The selected task evaluates this family argument or applicability; the linked deciding owners govern operational application.'
    for value in item.get('append_source_refs', []):
        if value not in argument.setdefault('source_refs', []):
            argument['source_refs'].append(copy.deepcopy(value))
    for relation in item.get('append_dependency_relations', []):
        relation = copy.deepcopy(relation)
        if 'target' in relation:
            if 'id' in relation and relation['id'] != relation['target']:
                raise ValueError('Conflicting dependency targets')
            relation['id'] = relation.pop('target')
        if 'relation' in relation:
            relation['kind'] = relation.pop('relation')
        if relation not in result.setdefault('dependency_relations', []):
            result['dependency_relations'].append(copy.deepcopy(relation))
        if relation['id'] not in result.setdefault('dependencies', []):
            result['dependencies'].append(relation['id'])
    # This exact author-standing spelling is qualification metadata, not law.
    if argument.get('standing') == 'Writer-authored consumer binding; not independent fidelity evidence':
        argument['standing'] = 'authored_conditional_argument_not_independent_proof'
    return {k:v for k,v in result.items() if k not in row or row[k] != v}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    build = library('iteration-3/build_interpretation.py')
    repair = library('iteration-3/review-repair/interpretation/repair_account.py')
    build.documentary_inventory(args.source_commit)
    preimage = git_bytes(INPUTS['starting_tenant'], (PRIOR / 'DETERMINATIONS.json').relative_to(REPO))
    if (PRIOR / 'DETERMINATIONS.json').read_bytes() != preimage:
        raise ValueError('Historical I3 account changed')
    account = __import__('json').loads(preimage)
    rows = {r['id']: r for r in account['determinations']}
    patches = {}
    dependent = []
    patch_inputs = []
    for name in ('core','delivery','profiles'):
        path = HERE / 'source' / name / 'ACCOUNT_PATCH.json'
        part = read(path)
        if (part.get('common_input', INPUTS['common_input']) != INPUTS['common_input']
                or part.get('source_preimage', part.get('preimage')) != INPUTS['starting_tenant']):
            raise ValueError('Patch basis mismatch: ' + str(path))
        for item in part.get('patches', part.get('changes', [])):
            if item['id'] in patches:
                raise ValueError('Two writers patch one owner: ' + item['id'])
            item = copy.deepcopy(item)
            # The core author's sections() excludes the heading line. Its
            # candidate pin is exact in that convention; account pins include
            # the heading. Preserve and verify both instead of repinning it.
            if path.parent.name == 'core':
                item['candidate_body_scope'] = 'immediate_body_excluding_heading'
            patches[item['id']] = item
        dependent.extend(part.get('dependent_argument_refresh', []))
        patch_inputs.append({'path': str(path.relative_to(HERE)), 'sha256': sha(path.read_bytes())})
    if len(patch_inputs) != 3:
        raise ValueError('All three bounded source returns are required')
    integration = read(HERE/'INTEGRATION_INPUTS.json')
    routing = []
    for selected in integration['patches']:
        path = HERE / selected['path']
        if sha(path.read_bytes()) != selected['sha256']:
            raise ValueError('Integration return changed: '+selected['path'])
        part = read(path)
        patch_inputs.append({'path':selected['path'],'sha256':selected['sha256'],
                             'stage':selected['stage']})
        if selected['stage']=='source_repair':
            for item in part['patches']:
                if item['id'] in patches:
                    raise ValueError('Source repair overlaps first source delta: '+item['id'])
                patches[item['id']]=item
        elif selected['stage']=='account_routing':
            routing.append((selected,part))
        else:
            raise ValueError('Unknown integration stage')
    old_source, source, units = {}, {}, {}
    for path in {r['owner']['path'] for r in rows.values()}:
        old_source[path] = git_bytes(INPUTS['starting_tenant'], (PACKAGE / path).relative_to(REPO))
        source[path] = (PACKAGE / path).read_bytes()
        units[path] = repair.heading_units(source[path])
    changed, relocated = [], []
    for identifier, row in rows.items():
        path, anchor = row['owner']['path'], row['owner']['anchor']
        whole = row['owner'].get('unit_scope') == 'whole_member'
        unit = None if whole else units[path].get(anchor)
        if not whole and unit is None:
            raise ValueError('Lost owner heading: ' + identifier)
        old_body = repair.local_source_body(row, old_source[path])[0]
        new_body = source[path] if whole else unit['body']
        item = patches.get(identifier)
        if old_body != new_body and item is None:
            raise ValueError('Changed source has no authored semantic patch: ' + identifier)
        if item:
            if item.get('preimage_body_sha256') and item['preimage_body_sha256'] != sha(old_body):
                raise ValueError('Patch preimage differs: ' + identifier)
            if item.get('i3_source_heading_sha256') and item['i3_source_heading_sha256'] != sha(old_body):
                raise ValueError('Local source argument preimage differs: ' + identifier)
            if item.get('source_current', {}).get('sha256') and item['source_current']['sha256'] != sha(new_body):
                raise ValueError('Local source argument current body differs: ' + identifier)
            if item.get('argument_preimage_sha256'):
                canonical = __import__('json').dumps(row.get('argument'), sort_keys=True,
                    separators=(',', ':'), ensure_ascii=False).encode()
                if sha(canonical) != item['argument_preimage_sha256']:
                    raise ValueError('Local argument preimage differs: ' + identifier)
            expected_body = item.get('body_sha256', item.get('candidate_body_sha256'))
            pinned_body = new_body
            if item.get('candidate_body_scope') == 'immediate_body_excluding_heading':
                if whole:
                    raise ValueError('Heading convention on a whole-member patch')
                pinned_body = new_body.split(b'\n', 1)[1]
            if expected_body and expected_body != sha(pinned_body):
                raise ValueError('Patch current body differs: ' + identifier)
            fields = authored_fields(item, row)
            if set(fields) - build.SEMANTIC_FIELDS - build.EVIDENCE_FIELDS:
                raise ValueError('Unknown authored fields: ' + identifier)
            row.update(copy.deepcopy(fields))
            changed.append({'id': identifier, 'before_body_sha256': sha(old_body),
                            'body_sha256': sha(new_body), 'fields': sorted(fields),
                            'predicate_or_result_change': item.get('predicate_or_result_change'),
                            'standing': 'authored semantic change; independent fidelity remains separate'})
        # Reuse the coordinate transform with exact source bytes. It keeps
        # unchanged blocks and explicitly coarsens changed spans to their owner.
        moved = repair.remap_blocks(row, old_source[path], source[path], unit)
        # An old whole-body block may survive as a strict prefix when an
        # explanation is appended. The reused transformer also adds the new
        # whole body. 'body' denotes the current owner, never two byte ranges.
        blocks = row.get('source_clauses', [])
        body_blocks = [b for b in blocks if b['id'] == 'body']
        if len(body_blocks) > 1:
            current_body = [b for b in body_blocks if b['sha256'] == sha(new_body)
                            and b['byte_start'] == (0 if whole else unit['byte_start'])]
            if len(current_body) != 1:
                raise ValueError('Ambiguous whole-body relocation: ' + identifier)
            row['source_clauses'] = [b for b in blocks if b['id'] != 'body'] + current_body
            moved = sorted(set(moved + ['body']))
        row['owner'] = repair.make_owner(path, unit, source[path])
        if 'owner_body_sha256' in row:
            row['owner_body_sha256'] = sha(new_body)
        if 'source_member_sha256' in row:
            row['source_member_sha256'] = sha(source[path])
        for owner in row.get('supporting_sources', []):
            raw = (PACKAGE / owner['path']).read_bytes()
            whole_support = owner.get('unit_scope') == 'whole_member'
            support_unit = None if whole_support else repair.heading_units(raw).get(owner.get('anchor'))
            if support_unit is not None or whole_support:
                owner.update(repair.make_owner(owner['path'], support_unit, raw))
            for key in ('sha256', 'member_sha256'):
                if key in owner:
                    owner[key] = sha(raw)
        if moved:
            relocated.append({'id': identifier, 'coarsened_blocks': moved})
    if set(patches) - set(rows):
        raise ValueError('Patch has no existing determination: ' + str(sorted(set(patches)-set(rows))))
    # Dependent proposals are preserved for explicit integration; unknown
    # shapes refuse rather than silently dropping an author's affected cone.
    applied_dependents = []
    for item in dependent:
        identifier = item['id']
        if identifier not in rows:
            raise ValueError('Unknown dependent: ' + identifier)
        if 'new_direct_family_arguments' in item:
            # The returned source-specific rows replace old broad table payloads;
            # a more specific local argument is preserved. Empty selections are
            # recorded for review, not used to erase existing obligations.
            value = item['new_direct_family_arguments']
            if value:
                rows[identifier].setdefault('argument', {})['source_family_arguments'] = copy.deepcopy(value)
                applied_dependents.append(identifier)
        elif item.get('semantic_fields'):
            if identifier in patches:
                raise ValueError('Ambiguous direct/dependent patch: ' + identifier)
            rows[identifier].update(copy.deepcopy(item['semantic_fields']))
            applied_dependents.append(identifier)
        else:
            raise ValueError('Dependent argument requires explicit fields: ' + identifier)
    routing_changes=[]
    for selected, part in routing:
        for item in part['patches']:
            if item['id'] in selected.get('excluded_items',{}):
                routing_changes.append({'id':item['id'],'input':selected['path'],
                    'not_applied':selected['excluded_items'][item['id']]})
                continue
            row=rows[item['id']]
            fields=authored_fields(item,row)
            expected=selected['before_fields'][item['id']]
            paths=set(item.get('set',{})) | set(item.get('semantic_fields',{}))
            if paths - set(expected):
                raise ValueError('Unbound routing path: '+item['id'])
            for path in paths:
                value=get_path(row,path)
                scope=scoped_operations(item).get(path)
                if scope:
                    value=[x for x in (value or []) if owned_family(x,scope)]
                if sha(encoded(value)) != expected[path]:
                    raise ValueError('Routing preimage differs: '+item['id']+'/'+path)
            if set(fields) - build.SEMANTIC_FIELDS - build.EVIDENCE_FIELDS:
                raise ValueError('Unknown routing semantic fields: '+item['id'])
            row.update(fields)
            routing_changes.append({'id':item['id'],'fields':sorted(fields),
                                    'input':selected['path']})
    row_coordinate_changes=[]
    row_sources={}
    for identifier,row in rows.items():
        bind_family_rows(row,identifier,args.source_commit,repair,row_sources,row_coordinate_changes)
    account['determinations'] = sorted(rows.values(), key=lambda r:r['id'])
    for member in account['source_members']:
        raw = (PACKAGE / member['path']).read_bytes()
        member.update(sha256=sha(raw), bytes=len(raw))
    for item in account['coverage'].get('structural_sections', []):
        raw = (PACKAGE / item['path']).read_bytes()
        unit = repair.heading_units(raw).get(item['anchor'])
        if unit is None:
            raise ValueError('Lost structural heading: ' + item['anchor'])
        item['body_sha256'] = sha(unit['body'])
    account['subject'] = {'source_commit': args.source_commit,
                          'common_input': INPUTS['common_input'],
                          'source_preimage': INPUTS['starting_tenant'],
                          'activation': 'EC-CODEX-I4-01',
                          'installed_builder': 'v2.5.1-rc.2',
                          'manifest_sha256': build.MANIFEST_SHA}
    current, excluded = build.semantic_projection(account)
    build.validate_account(current)
    write(HERE / 'DETERMINATIONS.json', account)
    write(HERE / 'ACCOUNT_INTEGRATION.json', {
        'source_commit': args.source_commit, 'input_sha256': sha(preimage),
        'patch_inputs': patch_inputs, 'direct_patches': changed,
        'dependent_patches': applied_dependents, 'routing_patches':routing_changes,
        'coarsened_coordinates': relocated,
        'argument_row_coordinate_changes':row_coordinate_changes,
        'rows': len(rows), 'validation': 'source pins, semantic reference closure and pointer resolution passed',
        'limits': ['Coordinate and reference checks do not establish source fidelity.',
                   'I3 source/account and evidence files are unchanged.']})
    print({'rows': len(rows), 'direct_patches': len(changed), 'dependent_patches': len(applied_dependents)})


if __name__ == '__main__':
    main()
