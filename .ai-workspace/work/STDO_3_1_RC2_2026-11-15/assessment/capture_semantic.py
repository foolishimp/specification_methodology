from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
BASE = Path(__file__).resolve().parent
RUN = BASE.parent
OUT = BASE / 'semantic-01'
PREVIOUS = 'f68e8f47db69425205db313ba72fbc9cad94c2b9'
PREVIOUS_NATIVE = 'c1e0faaa8437c169031a476343c764614135cd93'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()

def git_member(commit, member):
    return subprocess.check_output(['git', '-C', str(ROOT), 'show', commit + ':' + member])

def main():
    freeze_path = RUN / 'context/SEMANTIC_FREEZE.json'
    freeze_raw = freeze_path.read_bytes()
    assert sha(freeze_raw) == 'c51bdf5a47e8be38c4ff7e86a00b3c45483e7659b5fc6838b7b59cea41ca2e84'
    freeze = json.loads(freeze_raw)
    for entry in freeze['files']:
        raw = Path(entry['path']).read_bytes()
        assert len(raw) == entry['bytes'] and sha(raw) == entry['sha256'], entry['path']
    binding = json.loads((RUN / 'NATIVE_BINDING.json').read_text())
    native = Path(binding['installed_root'])
    assert sha((native / 'manifest.json').read_bytes()) == binding['manifest_sha256']
    OUT.mkdir(parents=True, exist_ok=False)
    entries, chunks = [], []

    def add(label, raw, origin, kind):
        raw.decode()
        item = {'label': label, 'origin': origin, 'kind': kind, 'bytes': len(raw), 'sha256': sha(raw)}
        entries.append(item)
        chunks.append('\n\n===== ' + kind.upper() + ': ' + label + ' =====\n' +
                      'SHA-256: ' + item['sha256'] + '; bytes: ' + str(item['bytes']) + '\n' +
                      raw.decode() + '\n===== END ' + label + ' =====\n')

    def file(label, path, kind):
        add(label, path.read_bytes(), str(path), kind)

    for stage in ['source-first-01', 'source-first-02']:
        file(stage + ' fixed expectations', BASE / stage / 'EXPECTATIONS.md', 'prior independent source expectations')
    file('admitted RC2 activation', RUN / 'ACTIVATION.md', 'governing scope')
    file('current RC2 release contract', ROOT / 'releases/3.1.0-rc.2/RELEASE.md', 'governing scope')
    file('current migration', ROOT / 'releases/3.1.0-rc.2/MIGRATION.md', 'release claim')
    for rel in ['purpose_context/specification/PRODUCT.md', 'purpose_context/specification/requirements/README.md',
                'purpose_context/specification/requirements/SDLC-WORKFLOW.md', 'purpose_context/design/DESIGN.md',
                'purpose_context/skills/stdo-context/references/authoring.md']:
        file(rel, ROOT / rel, 'Product requirement or design contract')

    old_catalog = json.loads(git_member(PREVIOUS, 'purpose_context/skills/stdo-context/indexes/CATALOG.json'))
    new_catalog = json.loads((ROOT / 'purpose_context/skills/stdo-context/indexes/CATALOG.json').read_text())
    comparisons, owners = [], {}
    for row in freeze['identities']['indexes']:
        current = Path(row['index_path']).parent
        current_rel = str(current.relative_to(ROOT))
        previous_rel = current_rel.replace('3.1.0-rc.2-', '3.1.0-rc.1-')
        old_index = json.loads(git_member(PREVIOUS, previous_rel + '/INDEX.json'))
        new_index = json.loads((current / 'INDEX.json').read_text())
        old_purpose = json.loads(git_member(PREVIOUS, previous_rel + '/PURPOSE.json'))
        new_purpose = json.loads((current / 'PURPOSE.json').read_text())
        assert sha(canonical(new_index)) == row['canonical_index_sha256']
        assert new_index['corpus_sha256'] == row['corpus_sha256']
        assert sha(canonical(new_purpose)) == row['purpose_sha256']
        old_rules = {x['id']: x for x in old_index['rules']}
        new_rules = {x['id']: x for x in new_index['rules']}
        assert old_rules.keys() == new_rules.keys()
        delta = []
        for rule_id in old_rules:
            a, b = old_rules[rule_id], new_rules[rule_id]
            if a != b:
                fields = [k for k in sorted(a.keys() | b.keys()) if a.get(k) != b.get(k)]
                delta.append({'id': rule_id, 'changed_fields': fields, 'before': a, 'after': b})
        assert delta == [] if 'python' in row['index_id'] else len(delta) == 1 and delta[0]['id'] == 'W35' and delta[0]['changed_fields'] == ['when']
        old_entry = next(x for x in old_catalog['entries'] if x['id'] == row['index_id'].replace('rc.2-', 'rc.1-'))
        new_entry = next(x for x in new_catalog['entries'] if x['id'] == row['index_id'])
        assert old_entry['family_guard'] == new_entry['family_guard']
        assert old_purpose['facts'] == new_purpose['facts']
        sources = json.loads((current / 'SOURCES.json').read_text())
        old_sources = json.loads(git_member(PREVIOUS, previous_rel + '/SOURCES.json'))
        assert sources['files'] == old_sources['files']
        for source in sources['files']:
            raw = (native / source['path']).read_bytes()
            assert sha(raw) == source['sha256']
            assert raw == git_member(PREVIOUS_NATIVE, 'specification_methodology/v3/' + source['path'])
            owners[source['path']] = source
        comparison = {'index_id': row['index_id'], 'canonical_index_sha256': row['canonical_index_sha256'],
                      'corpus_sha256': row['corpus_sha256'], 'purpose_sha256': row['purpose_sha256'],
                      'predecessor_index_sha256': sha(canonical(old_index)), 'rules': len(new_rules),
                      'changed_rules': delta, 'purpose_facts_equal': True,
                      'purpose_changed_fields': [k for k in new_purpose if new_purpose[k] != old_purpose.get(k)],
                      'source_members_and_order_equal': True, 'all_selected_source_bytes_equal': True,
                      'family_guard_equal': True, 'old_family_guard': old_entry['family_guard'],
                      'current_family_guard': new_entry['family_guard']}
        comparisons.append(comparison)
        for filename in ['INDEX.json', 'PURPOSE.json', 'SOURCES.json']:
            file(row['index_id'] + '/' + filename, current / filename, 'frozen candidate')
        add(row['index_id'] + '/current catalog entry', canonical(new_entry), 'current CATALOG.json selected entry', 'frozen candidate catalog')
        add(row['index_id'] + '/predecessor catalog entry', canonical(old_entry), PREVIOUS + ':CATALOG.json selected entry', 'immutable predecessor catalog')
    for member in sorted(owners):
        file('native A/' + member, native / member, 'full governing owner')
    for member in ['plugins/spec/skills/stdo-work/SKILL.md', 'plugins/spec/skills/stdo-review/SKILL.md',
                   'plugins/spec/skills/stdo-ticket/SKILL.md']:
        file('native A/' + member, native / member, 'native workflow contract')

    observations = []
    query_rows = {x['name']: x for x in freeze['identities']['queries']}
    for case in freeze['contexts']:
        name = case['case']
        query = query_rows[name]
        query_path = Path(query['path'])
        parsed_query = json.loads(query_path.read_text())
        assert sha(canonical(parsed_query)) == query['canonical_query_sha256']
        file('query/' + name, query_path, 'frozen exact query')
        if case.get('context'):
            context = json.loads(Path(case['context']).read_text())
            assert context['markdown'].encode() == Path(case['markdown']).read_bytes()
            assert sha(canonical(context['payload'])) == context['payload_sha256']
            assert sha(context['markdown'].encode()) == context['markdown_sha256']
            payload = context['payload']
            assert payload['query'] == parsed_query
            file('delivered context/' + name, Path(case['markdown']), 'actual installed-adapter context body')
            observations.append({'case': name, 'query_sha256': query['canonical_query_sha256'],
                                 'payload_sha256': context['payload_sha256'], 'markdown_sha256': context['markdown_sha256'],
                                 'context_file_sha256': sha(Path(case['context']).read_bytes()),
                                 'selection_status': payload['selection_status'], 'covered': payload['covered'],
                                 'semantic_coverage': payload['semantic_coverage'], 'gaps': payload['gaps'],
                                 'selected_applicability': {x['rule']['id']: x['applicability'] for x in payload['selected']}})
        else:
            file('actual unknown-boundary refusal/' + name, Path(case['selection']), 'actual installed-adapter observation')
            observations.append({'case': name, 'query_sha256': query['canonical_query_sha256'],
                                 'context': None, 'standing': case['status']})
    for path in sorted((RUN / 'context/final-use-01/fixture').iterdir()):
        if path.is_file():
            file('fixture/' + path.name, path, 'admitted finite fixture and current task inputs')

    for rel in ['purpose_context/skills/stdo-context/scripts/context_core.py',
                'purpose_context/skills/stdo-context/scripts/context_catalog.py',
                'purpose_context/skills/stdo-context/scripts/context.py',
                'purpose_context/scripts/test_successor_boundaries.py']:
        file(rel, ROOT / rel, 'runtime or focused test implementation')
    for rel in ['context/ACCEPTANCE_NEGATIVE.json', 'context/acceptance-negative.stderr',
                'context/FINAL_CONTROLS.json', 'context/rc2-boundary-controls.stderr',
                'context/historical-controls.stderr', 'context/PREREQUISITE_TESTS.json',
                'NATIVE_BINDING.json', 'method/SOURCE_DELTA.json', 'method/COMMANDS.json',
                'assessment/NATIVE_READBACK.json', 'assessment/NATIVE_DELTA.patch']:
        file(rel, RUN / rel, 'retained mechanical evidence; not independent semantic judgment')
    old_evidence = ROOT / '.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15'
    for rel in ['assessment/final/context/ASSESSMENT.md', 'assessment/final/context/VERDICT.json',
                'assessment/final/visual-recheck/ASSESSMENT.md', 'RELEASED.md']:
        file('RC1/' + rel, old_evidence / rel, 'prior exact-subject evidence; no automatic transfer')
    for rel in ['visual/RETURN.md', 'visual/RESULT.json', 'visual/PREDECESSOR_DISPOSITIONS.json',
                'visual/PREDECESSOR_COMPARISON.json', 'visual/PREREQUISITE_CHECKS.json',
                'visual/final-checks-001/RESULT.json', 'visual/browser-rc2-001/RESULT.json']:
        file(rel, RUN / rel, 'closed visual Writer evidence and proposed applicability')
    visual = ROOT / 'stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.2'
    for filename in ['COVERAGE.md', 'SOURCE_BINDING.json', 'README.md']:
        file('RC2 visual/' + filename, visual / filename, 'closed visual scope and binding')

    mechanical = {'native_commit': binding['native']['native_commit'], 'manifest_sha256': binding['manifest_sha256'],
                  'semantic_freeze_sha256': sha(freeze_raw), 'comparisons': comparisons,
                  'contexts': observations, 'standing': 'Operator-computed hashes, byte equality and body readback; not semantic verdicts.'}
    (OUT / 'OPERATOR_READBACK.json').write_text(json.dumps(mechanical, indent=2) + '\n')
    add('operator exact semantic readback', canonical(mechanical), str(OUT / 'OPERATOR_READBACK.json'), 'operator-computed evidence')
    add('full semantic freeze', freeze_raw, str(freeze_path), 'Writer frozen subject')

    intake = '''# Independent assessment of the frozen STDO RC2 semantic subject

Assess the bounded corrective release from the supplied deciding sources and the previously fixed source-first expectations. This is your independent judgment, not a request to agree with the Writer. You are an actual fresh Claude-family actor; operator and candidate Writers are Codex-family. Native CLI metadata establishes your identity. No tools are permitted or needed for this supplied-text assessment; report any actual tool exposure/use. Hidden host/system context is unmeasured; no enforced clean-room or whole-host fit is claimed. Packet bytes and exact input digests are recorded separately.

Scope and sequence:
- Decide whether the frozen successor-acceptance context retains the governing obligations and avoids importing release-only duties as applicable. Read W35's complete text, all selected rule/dependency applicability, actual purpose facts and family guard, and owning EVALUATION/RELEASE law. Assess the corrected selector and conserved qualification/release/work behavior, successor condition, unknowns, and authority/result boundaries.
- The packet includes all full native owners for both purpose closures, both complete candidate indexes and purposes, exact query facts, all six delivered Markdown context bodies, machine readback and actual three unknown-family refusals. Review each exact query's governing-constraint sufficiency before the decision. This does not establish task correctness, performed work, human acceptance or release. The Python realization-refactor and ordinary SDLC query may use applicable RC1 evidence, but you must make your own new exact-subject judgment and state its scope/limits; do not relabel the old verdict.
- Source-first addendum's unknown-boundary hypothesis was conditional on not having the catalog. The actual unchanged family_guard includes the supported boundary values. Compare that real old/new guard and actual refusal outputs to the sources; revise a provisional expectation if warranted rather than forcing a candidate to fit it. No artificial successor fact was added.
- Native A's constitutional/default/frame/native-workflow owners are byte-equal to RC1. Four navigation/release metadata members change; the exact patch is supplied. Assess the predecessor conservation/applicability claims in this bounded successor, not an unrelated whole-method reconstruction.
- Visual semantics are unchanged under the explicit 306-record bijection; the closed Writer supplies exact comparisons, selected-source equality, retained independent RC1 judgment and fresh finite validation/browser observations. Assess whether that evidence is applicable to the same narrowly declared visual claims and retained residuals. Do not silently upgrade unobserved modes or turn unchanged semantics into an unbounded fresh visual review.

Construction metadata correction: the first RC2 source-delta metadata compared a preserved development recipe while naming RC1. The Writer corrected that metadata to compare actual RC1. The INDEX/PURPOSE/SOURCES/query/context bodies supplied here are digest-frozen and unchanged by that correction. These delivered bodies came from the retained first package via the actual Codex adapter. A final second-package/two-host byte comparison, manifests/dependency pins, source B/ref graph and public asset readback are later identity checks, not claimed complete here. Judge these exact semantic bytes; state required final mapping without inventing another unconditional semantic round.

Evidence standing: raw file hashes and computed comparisons are operator/Writer observations, not computations you performed. Tests and source ledgers do not supply semantic adequacy. The before-failure is kept on RC1. Historical exact-query support stays on its original subject; unknown or falsified stays so until supported new evaluation. Prior Claude judgments and source-first expectations are the same family as you and may carry confirmation bias; declare that limit. The user has authorized construction/publication conditional on checks, but no actor or fixture may manufacture exact-cut human acceptance. There is no adopted numeric severity scale for this assessment. Tie any finding to a source obligation, real trigger and affected claim; distinguish material, bounded residual, adjacent and unperformed predicates. Do not repair or choose Product priority.

Required return:
1. Your own claim-relative conclusions for W35 repair, guard/dependency behavior, all six constructed exact queries, the three refused unknown queries, native conservation and bounded visual/evidence reuse. Identify any material counterexample and required source/owner re-entry; no candidate repair or release authorization.
2. A machine-readable JSON fenced object with keys `subjects`, `claim_results`, `evidence_reuse`, `findings`, `residuals`, `unperformed`. Each `subjects` item must name `name`, `index_sha256`, `corpus_sha256`, `query_sha256`, `status` (supported, falsified or unknown), `evaluator`, nonempty `evidence`, and `scope`. Use the full canonical hashes in the frozen subject/readback. Supported is a judgment of governing-constraint sufficiency for that exact query only. The unknown-family controls have no delivered context, so distinguish correct refusal from supported semantic coverage. If a query cannot be judged, say unknown and why. The operator may serialize your explicit same-subject statuses into runtime assessment envelopes; your original report remains authoritative.
3. State exactly what remains for final identity/package/publication closure. Do not claim final B, two-host final-package checks or public acquisition before their evidence is supplied.

Start with the deciding sources and fixed expectations, then compare the candidate and actual observations. The output should be concise enough to make the verdict and remaining conditions reviewable. No universal task, whole-method, general visual fidelity, automatic host discovery, code correctness or acceptance claim is requested.
'''
    packet = intake + ''.join(chunks)
    (OUT / 'PACKET.md').write_text(packet)
    record = {'captured_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'packet_sha256': sha(packet.encode()), 'packet_bytes': len(packet.encode()),
              'sources_and_evidence': entries, 'semantic_freeze_sha256': sha(freeze_raw),
              'standing': 'Frozen independent-assessment input; no assessment verdict yet.'}
    (OUT / 'INPUT_MANIFEST.json').write_text(json.dumps(record, indent=2) + '\n')
    for entry in freeze['files']:
        assert sha(Path(entry['path']).read_bytes()) == entry['sha256'], 'Input drift during capture'
    print(json.dumps({'packet_bytes': len(packet.encode()), 'packet_sha256': sha(packet.encode()),
                      'inputs': len(entries), 'owners': len(owners), 'exact_queries': len(query_rows)}))

if __name__ == '__main__':
    main()
