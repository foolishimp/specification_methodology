#!/usr/bin/env python3
"""Author a bounded integration patch; never write the receiving account."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
ROOT = TENANT.parents[3]
SOURCE = 'cd19955505a0350b5d9b0f19d00c89e6d1810aa6'
PATCH_SOURCE = '0044d45f7ac4a49e204a8abebfe3a0b07551d62f'
ACCOUNT_SHA = 'b8c43489311b387045de129db459ef1bf29c1334724fcccc36474ea9565fedcd'
ACCOUNT = TENANT / 'qualification/C3/iteration-4/DETERMINATIONS.json'
PREFIX = str(TENANT.relative_to(ROOT)) + '/'
F = 'FOUNDATIONS'
T = 'TRANSFORMATION_LIBRARY'
R = 'REFERENCE_FRAME_METHOD'
B = 'STDO_REFERENCE_FRAME_BASELINE'
SPEC = 'SPEC_METHOD'
DESIGN = 'DESIGN_MODULE_METHOD'
AC = 'AXIOMATIC_CALCULUS'
TABLES = [F+'.core-contract-derivations', T+'.foundational-contract',
          T+'.workrecovery-specialization', T+'.transformation-admission-specialization',
          R+'.reference-frame-laws', B+'.status-and-authority-boundary']
AUDIT_WHEN = ('Only when assessing this family argument, its applicability, '
              'consequence, conservation, coverage or fidelity against this '
              'consumer. This is not an unconditional operational dependency.')
FAMILY_WRAPPER = ('Apply the exact source-family argument(s) below only in their '
                  'declared consumer scope. Their consequence does not imply '
                  'their additional chosen policies.')


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def git_text(commit, path):
    return subprocess.check_output(['git', 'show', commit+':'+path], cwd=ROOT).decode()


def slug(value):
    value = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', value)
    return re.sub(r'[^\w\- ]', '', value.lower()).replace(' ', '-')


def headings(text):
    lines = text.splitlines(keepends=True)
    entries, fence = [], False
    for index, line in enumerate(lines):
        if line.lstrip().startswith(('```', '~~~')):
            fence = not fence
        if fence:
            continue
        match = re.match(r'^(#{1,6}) (.+?)\s*$', line)
        if match:
            entries.append({'anchor': slug(match[2]), 'level': len(match[1]),
                            'start': index, 'heading': match[2]})
    for i, item in enumerate(entries):
        item['body_end'] = entries[i+1]['start'] if i+1 < len(entries) else len(lines)
        item['subtree_end'] = next((x['start'] for x in entries[i+1:]
                                   if x['level'] <= item['level']), len(lines))
    return lines, {item['anchor']: item for item in entries}


def root(member, anchor):
    return member+'.'+anchor


def main():
    account_bytes = ACCOUNT.read_bytes()
    assert sha(account_bytes) == ACCOUNT_SHA, 'Receiving account changed; rebind before authoring.'
    account = json.loads(account_bytes)
    by_id = {row['id']: row for row in account['determinations']}
    patch_path = PREFIX+'qualification/C3/iteration-4/source/core/ACCOUNT_PATCH.json'
    original = json.loads(git_text(PATCH_SOURCE, patch_path))
    exact_tables = {row['id']: row['source_family_rows'] for row in original['changes']
                    if 'source_family_rows' in row}
    sources, parsed = {}, {}

    def document(path):
        if path not in sources:
            sources[path] = git_text(SOURCE, PREFIX+'successor/'+path)
            parsed[path] = headings(sources[path])
        return sources[path]

    def rule(member, token):
        candidates = [identity for identity in by_id if identity.startswith(member+'.')
                      and (identity.split('.', 1)[1].startswith(token+'-')
                           or identity.endswith('-'+token))]
        assert len(candidates) == 1, (member, token, candidates)
        return candidates[0]

    rf = lambda n: rule(R, 'rf-'+str(n).zfill(3))
    up = lambda n: rule(SPEC, 'stdo-up-'+str(n).zfill(3))
    design_up = lambda n: rule(DESIGN, 'stdo-up-'+str(n).zfill(3))
    ac = lambda n: rule(AC, 'ac-'+str(n).zfill(3))
    ticket = root('TICKET_METHOD', 'work-carrier-to-execution-rule')
    classify = root(SPEC, 'computed-classification-and-treatment')
    admission = root(DESIGN, 'admission-contract-use')
    acquire_frame = root(R, 'select-and-activate')
    executive = root(B, 'executive-attention-evaluation-and-action')

    # Each list is the source's named owning/consuming scope. Heading scopes
    # include descendants; a member scope is expressly marked with .*.
    routes = {
        TABLES[0]: [
            [root(F,'interpretation-and-representation'), root(T,'faithful-projection'), ac(17), rf(17)],
            [root(F,'purpose-and-interfaces'), up(13), up(14)],
            [root(F,'identity-state-and-evidence'), 'IDENTITY_METHOD.*', root(F,'workspace-and-context')],
            [root(F,'typed-composition-and-conservation'), root(F,'orthogonal-descriptions'), root(T,'composition-law'), ac(16)],
            [root(F,'result-algebra'), rf(12), root(T,'evaluate')],
            [root(F,'result-algebra'), root(B,'work-result'), rf(12), root(T,'dispose')],
            [root(F,'result-conjunction'), root(T,'conjoin'), root(R,'result-conjunction'), root(B,'coverage-application')],
            [root(F,'workspace-and-context'), root(T,'acquire'), root(T,'recovery-law'), ticket],
            [root(F,'workspace-and-context'), root(T,'recovery-law'), root(T,'transform')],
            [root(F,'bounded-construction'), up(20), root(DESIGN,'8-totality-rule')],
            [root(F,'configuration'), rf(9), executive],
        ],
        TABLES[1]: [
            [root(T,'contract-application'), admission, up(21), acquire_frame],
            [root(T,'faithful-projection'), rf(17), ac(17)],
            [root(T,'composition-law'), design_up(16), design_up(17), up(21), ac(16), root(R,'using-frames-in-conjunction')],
            [root(T,'recovery-law'), up(20), classify, ticket],
        ],
        TABLES[2]: [
            [up(20), rf(5)],
            [rf(3), rf(14), 'CARRIER.plugins.spec.skills.stdo-work.SKILL.md'],
            [classify, ticket],
            [root(F,'workspace-and-context'), classify],
            [up(20), root(F,'result-conjunction'), executive],
        ],
        TABLES[3]: [
            [design_up(16), admission],
            [design_up(17), up(21), admission],
            [design_up(16), up(21), admission],
            [design_up(16), admission],
        ],
        TABLES[4]: [
            [rf(1), acquire_frame, root(R,'diagnostic-order')],
            [rf(2), rf(3), rf(4), rf(13), rf(14), acquire_frame],
            [rf(5), rf(11), root(R,'return-a-closed-result'), root(R,'reconfigure-when-necessary')],
            [rf(6), rf(7), rf(8), root(R,'evaluate'), root(R,'evidence-or-coordinate-translation')],
            [rf(9), rf(16), root(R,'human-frame-set-declaration'), root(R,'frame-set-optimization'), root(R,'agentic-use')],
            [rf(10), root(R,'using-frames-in-conjunction')],
            [rf(12), rf(15), root(R,'return-a-closed-result'), root(R,'result-conjunction')],
            [rf(17), acquire_frame],
            [root(R,'applicability-and-required-results'), root(R,'workspace-coverage'), root(R,'engagement')],
            [root(R,'discovery-and-revision'), root(R,'completeness-boundary'), root(R,'frame-qualification'), root(R,'method-self-qualification'), root(R,'diagnostic-order'), root(R,'closure')],
        ],
        TABLES[5]: [
            [root(B,'engagement-applicability')],
            [executive],
            [root(B,'product-chain-basis'), root(B,'executive-drift-locks'), root(B,'handoff-projection'), root(B,'2-executive-activates-worker'), root(B,'4-executive-evaluates-the-work-result'), root(B,'5b-candidate-requires-independent-review'), root(B,'7-executive-disposes-and-checkpoints')],
            [root(B,'work-result'), root(B,'3-worker-returns-to-executive'), root(B,'4-executive-evaluates-the-work-result'), root(B,'5a-candidate-does-not-require-independent-review'), root(B,'5b-candidate-requires-independent-review'), root(B,'6-reviewer-returns-to-executive'), root(B,'reviewer-result-and-triage-projection')],
            [root(B,'coverage-application'), root(B,'derived-generic-specialist-frame-set'), root(B,'derived-product-testing-frame-set'), root(B,'derived-end-to-end-interface-integration-frame'), root(B,'missing-frame-and-re-entry-application')],
            [root(B,'product-owned-adoption-or-project-defined-configuration'), root(B,'baseline-specific-project-basis-additions'), root(B,'baseline-specific-activation-additions')],
            [root(B,'profile-qualification')],
            [root(B,'failure-classification'), root(B,'anti-patterns'), root(B,'closure')],
        ],
    }
    # These phrase-to-locus joins are supported by the stated receiving body.
    joins = {
        (TABLES[0], 3): 'Identity/state/evidence explicitly routes reuse to Workspace and context; Identity Method is a named whole-member consumer. Its local identity policies remain separate.',
        (TABLES[0], 11): 'Configuration explicitly links its optional Executive arrangement to this Executive owner; the binding applies only when that arrangement is adopted and lawfully selected.',
        (TABLES[1], 4): 'Recovery law names Spec Product progress/re-entry and Ticket carrier use; UP-020 and Computed Classification supply those concrete Product continuation decisions.',
        (TABLES[2], 2): 'The work/recovery body links the ordinary work-entry skill after the table; its responsibility-frame route is the named work-entry consumer.',
        (TABLES[3], 1): 'The paragraph following the four-row table binds its complete contract to Design admission-contract-use.',
        (TABLES[3], 2): 'The paragraph following the four-row table binds its complete contract to Design admission-contract-use.',
        (TABLES[3], 3): 'The paragraph following the four-row table binds its complete contract to Design admission-contract-use.',
        (TABLES[3], 4): 'The paragraph following the four-row table binds its complete contract to Design admission-contract-use.',
        (TABLES[4], 3): 'Return A Closed Result applies currentness to result reuse; Reconfigure When Necessary is expressly named in the table.',
        (TABLES[4], 8): 'Select And Activate explicitly applies RF-017 to its acquired packet and current material subject.',
        (TABLES[5], 3): 'The transition activation/assessment/disposition bodies bind exact candidate/basis and consume returns through Handoff Projection.',
        (TABLES[5], 4): 'Step 6 explicitly routes findings through the triage projection below; that projection retains its own more-specific local argument.',
        (TABLES[5], 6): 'The choice cell names this profile adoption additions; the two additions bodies explicitly restrict themselves to adopted profile basis/activation content.',
    }
    instance_bound = {
        (TABLES[1], 2): ['domain publications'],
        (TABLES[1], 4): ['adopted runtime recovery'],
    }

    def locus(identity):
        row = by_id[identity]
        return {'path': row['owner']['path'], 'anchor': row['owner'].get('anchor',''),
                'role': 'provenance', 'required_when': AUDIT_WHEN}

    def declared_locus(consumer):
        if consumer in by_id:
            return locus(consumer)
        if consumer.endswith('.*'):
            path, anchor = 'standards/'+consumer[:-2]+'.md', ''
        else:
            member, anchor = consumer.split('.', 1)
            path = 'standards/'+member+'.md'
        return {'path': path, 'anchor': anchor, 'role': 'provenance',
                'required_when': AUDIT_WHEN}

    def scope(consumer):
        if consumer.endswith('.*'):
            path = 'standards/'+consumer[:-2]+'.md'
            document(path)
            return [identity for identity, row in by_id.items() if row['owner']['path'] == path]
        if consumer in by_id:
            row = by_id[consumer]
            path, key = row['owner']['path'], row['owner'].get('anchor','')
        else:
            # An empty enclosing heading may have no immediate-body unit, but
            # its source descendants still carry the named consumer scope.
            member, key = consumer.split('.',1)
            path = 'standards/'+member+'.md'
        document(path)
        hs = parsed[path][1]
        if key not in hs:
            # A whole carrier is one account unit, not a synthetic heading set.
            assert consumer.startswith('CARRIER.'), (consumer, key)
            return [consumer]
        h = hs[key]
        return [identity for identity, candidate in by_id.items()
                if candidate['owner']['path'] == path
                and candidate['owner'].get('anchor') in hs
                and h['start'] <= hs[candidate['owner']['anchor']]['start'] < h['subtree_end']]

    families, selected_rows, consumer_bindings = {}, [], {}
    for owner in TABLES:
        row = by_id[owner]
        path, key = row['owner']['path'], row['owner']['anchor']
        text = document(path)
        # The four source owners remain exactly the frozen documentary source.
        assert (TENANT/'successor'/path).read_text() == text, 'Source drift: '+path
        lines, hs = parsed[path]
        section = hs[key]
        expected = exact_tables[owner]['rows']
        actual = []
        for index in range(section['start']+1, section['body_end']):
            line = lines[index]
            if not line.startswith('|'):
                continue
            cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
            if cells in expected:
                actual.append((index, line, cells))
        assert [cells for _,_,cells in actual] == expected, 'Table differs: '+owner
        assert len(expected) == len(routes[owner]), owner
        families[owner] = []
        for number, (index, line, cells) in enumerate(actual, 1):
            four = len(cells) == 4
            premise = cells[1] if four else cells[0]
            arguments = {
                'family': cells[0],
                'declared_consumer_scope': cells[0] if four else cells[2],
                'premises': sorted(set(re.findall(r'F[1-6]', premise))),
                'premise_and_pillar_argument': premise,
                'conditional_consequence': cells[2] if four else cells[1],
                'additional_policy_and_owner': cells[3] if four else cells[2],
                'source_row': {'path': path, 'anchor': key, 'line': index+1,
                               'sha256': sha(line), 'hash_boundary': 'Exact Markdown row including terminal newline.'},
                'source_refs': [{'path': path, 'anchor': key, 'role': 'provenance',
                                 'required_when': AUDIT_WHEN}],
                'required_when': AUDIT_WHEN,
            }
            if (owner, number) in instance_bound:
                arguments['instance_bound_consumer_scope'] = {
                    'phrases': instance_bound[(owner, number)],
                    'standing': 'Parametric domain consumer, not a closed enumeration or a missing source premise.',
                    'binding_requirement': 'When a concrete publication or adopted runtime-recovery decision is selected, its domain contract binds its own source/consumer/adoption relation. No universal consumer or mandatory optional profile is inferred.'}
            families[owner].append(arguments)
            roots = routes[owner][number-1]
            selected_rows.append({'owner': owner, 'row': number, 'source_row': arguments['source_row'],
                                  'declared_consumer_scope': arguments['declared_consumer_scope'],
                                  'named_scope_roots': roots,
                                  'scope_join_evidence': joins.get((owner,number), 'Explicitly named governing or consuming locus in the row; enclosing headings include their source descendants.')})
            for consumer in roots:
                for target in scope(consumer):
                    binding = consumer_bindings.setdefault(target, {}).setdefault(
                        (owner,number), copy.deepcopy(arguments))
                    selected_locus = locus(target)
                    binding['audit_consumer_loci'] = [selected_locus]
                    binding.setdefault('consumer_scope_bindings', []).append({
                        'declared_root': declared_locus(consumer),
                        'binding_kind': 'whole_named_member' if consumer.endswith('.*') else ('named_consumer' if consumer == target else 'descendant_of_named_consumer'),
                        'scope_condition': 'This consequence applies only to the decision relation named in this row within the enclosing consumer. It does not derive every independent local policy or replace the consumer local argument.',
                        'source_evidence': joins.get((owner,number), 'The source table names this owning/consuming scope.'),
                        'role': 'provenance', 'required_when': AUDIT_WHEN,
                    })

    # The source Anti-Patterns body states fourteen numbered violations. Bind
    # each to the current decision-specific family, not a uniform umbrella.
    anti_cases = {1:[2], 2:[1,10], 3:[7,11], 4:[6,7], 5:[3,14],
                  6:[4,5], 7:[8], 8:[13], 9:[9], 10:[12]}
    anti_id = root(R,'anti-patterns')
    anti_source = document(by_id[anti_id]['owner']['path'])
    for row_number, cases in anti_cases.items():
        binding = copy.deepcopy(families[TABLES[4]][row_number-1])
        binding['audit_consumer_loci'] = [locus(anti_id)]
        binding['consumer_scope_bindings'] = [{
            'binding_kind': 'explicit_source_case_relation',
            'cases': cases,
            'scope_condition': 'Only the named numbered violations in Anti-Patterns are explained by this family; retain each other local claim and policy.',
            'source_evidence': 'REFERENCE_FRAME_METHOD.md#anti-patterns states these numbered frame/coverage violations; the source family named here supplies their corresponding deciding relation.',
            'role': 'provenance', 'required_when': AUDIT_WHEN,
        }]
        consumer_bindings.setdefault(anti_id,{})[(TABLES[4],row_number)] = binding

    def core_family(family):
        source = family.get('source_row', {})
        owner = source.get('path','').replace('standards/','').replace('.md','')+'.'+source.get('anchor','')
        refs = family.get('source_refs', [])
        return owner in TABLES or any(isinstance(ref,str) and ref in TABLES for ref in refs)

    changes, stale_copies, old_hashes = [], 0, set()
    owned_origins = [{'path': by_id[identity]['owner']['path'],
                      'anchor': by_id[identity]['owner']['anchor']}
                     for identity in TABLES]
    old_affected = set()
    for identity, row in by_id.items():
        for field in ('definition','argument'):
            container = row.get(field,{})
            for family in container.get('source_family_arguments',[]) if isinstance(container,dict) else []:
                if core_family(family):
                    stale_copies += 1
                    old_affected.add(identity)
                    old_hashes.add(family.get('source_row',{}).get('sha256') or family.get('source_row_sha256'))
    for identity in sorted(set(consumer_bindings) | set(TABLES) | old_affected):
        original_row = by_id[identity]
        fields, altered = {}, []
        if identity in TABLES:
            definition = copy.deepcopy(original_row.get('definition',{}))
            assert isinstance(definition,dict), identity
            definition['source_family_arguments'] = [family for family in definition.get('source_family_arguments',[]) if not core_family(family)] + copy.deepcopy(families[identity])
            fields['definition'] = definition
            altered.append('definition.source_family_arguments')
        old_arg = original_row.get('argument',{})
        existing = old_arg.get('source_family_arguments',[])
        old_core = [family for family in existing if core_family(family)]
        incoming = list(consumer_bindings.get(identity,{}).values())
        if old_core or incoming:
            argument = copy.deepcopy(old_arg)
            retained = [family for family in existing if not core_family(family)]
            argument['source_family_arguments'] = retained + incoming
            altered.append('argument.source_family_arguments')
            if old_core and not incoming:
                argument['source_family_arguments'].append({
                    'standing': 'unresolved_source_family_binding',
                    'unresolved': 'No current source table row is established for the previously bound scope.',
                    'source_refs': [locus(identity)], 'required_when': AUDIT_WHEN,
                    'resolution': 'Assess the current source consumer and identify the exact governing family before claiming argument coverage.'})
            if old_core and argument.get('conditional_consequence') == FAMILY_WRAPPER:
                argument['conditional_consequence'] = ('Each current source_family_arguments entry applies only to its stated consumer relation and conditions. '
                    'Its exact premises, consequence and additional policy stay separate; these family bindings do not replace more-specific local arguments.')
                altered.append('argument.conditional_consequence')
                if all(isinstance(value,str) and re.fullmatch(r'F[1-6]',value)
                       for value in argument.get('premises',[])):
                    argument['premises'] = [{'kind':'conditional_source_family_premises',
                        'binding':'Use the exact premises of each applicable source_family_arguments entry within its declared consumer scope. No uniform premise set is assigned to this whole source unit.'}]
                    altered.append('argument.premises')
            fields['argument'] = argument
        if fields:
            dotted_set = {field: fields[field.split('.',1)[0]][field.split('.',1)[1]]
                          for field in altered}
            scoped = {field: {
                'mode': 'replace_owned_source_rows_preserving_current_other_entries',
                'owned_source_rows': owned_origins,
                'legacy_source_refs': TABLES,
                'incoming_entries': 'Use only entries in this dotted set value whose source_row path/anchor matches an owned source row. The unowned entries in the set value document the held-preimage result only.',
                'application': 'At application time, retain every current array entry outside the owned source rows (including entries added by earlier integration patches), then append the incoming owned entries in supplied order. Legacy exact source_refs naming an owned table also identify an owned entry. Do not blindly replace this array after another patch adds unowned families.',
                'preserve_unowned_entries': True,
            } for field in altered if field.endswith('.source_family_arguments')}
            changes.append({'id':identity, 'set':dotted_set,
                'scoped_replacements':scoped,
                'changed_nested_fields':altered,
                'preserve':'All other semantic fields, direct authored obligations, local clause arguments, dependencies, result mappings and proof standing remain byte-equivalent JSON values.'})

    # Apply only in memory to validate the author patch; never emit an account.
    simulated = copy.deepcopy(by_id)
    scoped_checks, new_exact_semantic_refs = 0, []

    def check_new_values(value, location):
        if isinstance(value,str) and value in by_id:
            new_exact_semantic_refs.append(location)
        elif isinstance(value,list):
            for index,item in enumerate(value):
                check_new_values(item,location+'['+str(index)+']')
        elif isinstance(value,dict):
            for key,item in value.items():
                check_new_values(item,location+'.'+key)

    for change in changes:
        original_row = by_id[change['id']]
        for field, value in change['set'].items():
            container, nested = field.split('.',1)
            target = simulated[change['id']].setdefault(container,{})
            if field in change['scoped_replacements']:
                before = target.get(nested,[])
                incoming = [entry for entry in value if core_family(entry)]
                target[nested] = ([entry for entry in target.get(nested,[]) if not core_family(entry)]
                                  + incoming)
                assert target[nested] == value, (change['id'],field,'Held-preimage merge differs from declared set value.')
                sentinel = {'family':'Later integration foreign-family preservation check',
                            'source_row':{'path':'standards/UNOWNED_TEST.md','anchor':'other-family'},
                            'local_argument':{'literal':'preserved'}}
                rebased = ([entry for entry in before+[sentinel] if not core_family(entry)]
                           + incoming)
                assert sentinel in rebased
                assert all(entry in rebased for entry in before if not core_family(entry))
                check_new_values(incoming,change['id']+'.'+field)
                scoped_checks += 1
            else:
                target[nested] = copy.deepcopy(value)
                check_new_values(value,change['id']+'.'+field)
        new = simulated[change['id']]
        changed_roots = {field.split('.',1)[0] for field in change['set']}
        for key,value in original_row.items():
            if key not in changed_roots:
                assert new[key] == value, (change['id'],key)
        for field in ('definition','argument'):
            if field not in changed_roots:
                continue
            for key,value in original_row.get(field,{}).items():
                if field+'.'+key not in change['changed_nested_fields']:
                    assert new[field][key] == value, (change['id'],field,key)
    stale_after, unresolved = [], []
    for identity,row in simulated.items():
        for field in ('definition','argument'):
            container = row.get(field,{})
            for family in container.get('source_family_arguments',[]) if isinstance(container,dict) else []:
                old = family.get('source_row',{}).get('sha256') or family.get('source_row_sha256')
                if old and old in old_hashes:
                    stale_after.append((identity,field,old))
                if family.get('standing') == 'unresolved_source_family_binding':
                    unresolved.append(identity)
    assert not stale_after, stale_after
    assert not new_exact_semantic_refs, new_exact_semantic_refs
    assert ACCOUNT.read_bytes() == account_bytes, 'Receiving account changed during authoring.'
    output = {
        'schema_version':'stdo.authored-semantic-fields-patch.v1',
        'activation':'I4-CORE-ACCOUNT-ROUTES',
        'standing':'Authored account integration input; no source, account, generated artifact or independent fidelity judgment is changed by this patch.',
        'source_commit':SOURCE, 'original_patch_commit':PATCH_SOURCE,
        'receiving_account':{'path':str(ACCOUNT.relative_to(TENANT)), 'sha256':ACCOUNT_SHA,
                             'standing':'Parent-held provisional integration shape, not a frozen accepted account.'},
        'frozen_semantic_preimage':'199c6d29bc02590a8b7f252043fc43223c09808d',
        'integration':'For each existing ID, apply only patches[].set dotted fields. For either source_family_arguments array, scoped_replacements is normative: replace only entries from the six owned source tables and preserve every current unowned family, including additions by earlier integration patches. Each set array is also the exact result against the held account for audit. Do not replace whole argument or definition objects. Other scalar/array fields change only when the held-preimage stale wrapper is still present; otherwise retain the later local field and report a conflict for author review.',
        'acquisition':'source_refs, audit_consumer_loci, source_row and consumer_scope_bindings are provenance. Family evidence has explicit required_when. No operational dependency or result mapping is added or removed.',
        'patches':changes,
        'unresolved_source_bindings':sorted(set(unresolved)),
        'instance_bound_consumer_phrases':[{'owner':owner,'row':number,'phrases':phrases} for (owner,number),phrases in instance_bound.items()],
    }
    (HERE/'ACCOUNT_PATCH.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
    report = {
        'standing':'Author structural/routing checks, not independent semantic fidelity.',
        'source_commit':SOURCE, 'receiving_account_sha256':ACCOUNT_SHA,
        'source_tables':len(families), 'source_rows':sum(len(rows) for rows in families.values()),
        'affected_determination_ids':len(changes), 'consumer_units':len(consumer_bindings),
        'old_copies_replaced':stale_copies, 'old_copy_hashes':sorted(h for h in old_hashes if h),
        'old_affected_units':len(old_affected),
        'stale_core_copies_after_in_memory_application':stale_after,
        'unresolved_source_bindings':sorted(set(unresolved)),
        'local_arguments_preserved':True, 'dependencies_and_result_mappings_preserved':True,
        'scoped_array_applications_checked':scoped_checks,
        'later_integration_foreign_family_preserved':True,
        'new_owned_family_exact_semantic_id_values':new_exact_semantic_refs,
        'receiving_account_unchanged':True,
        'source_members':{path:sha(text) for path,text in sources.items()},
        'scope_expansion':selected_rows,
        'limits':['Enclosing-heading inheritance is conditional on the stated decision relation, never a derivation of every local policy.','Identity Method is bound at the documentary source commit before the disjoint Identity selector repair; preserve local authored fields if integration rebases that source.','Domain publications and adopted runtime recovery are parametric instance scopes, not closed catalogs.','No generated/native acquisition or independent fidelity result is asserted.'],
    }
    (HERE/'CHECKS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({key:report[key] for key in ['source_tables','source_rows','affected_determination_ids','consumer_units','old_copies_replaced','stale_core_copies_after_in_memory_application','unresolved_source_bindings']}))


if __name__ == '__main__':
    main()
