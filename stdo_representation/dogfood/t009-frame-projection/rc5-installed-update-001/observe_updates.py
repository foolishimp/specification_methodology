"""Construct bounded P0 fixtures and retain actual installed RC5 CLI observations.

This is qualification preparation, not a consumer updater or native operator.
All effects are confined to this additive evidence directory. No live consumer
is consulted. Acceptance records are explicit fixture construction selections
under the Executive's grant; subprocess output is never manufactured.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[3]
MANAGER = Path('/private/tmp/stdo-rc5-installed-manager-20260906/bin/stdo')
PYTHON = MANAGER.with_name('python')
STORE = HERE / 'stdo-store'
RC4 = 'stdo://releases/v2.5.0-rc.4/'
RC5 = 'stdo://releases/v2.5.0-rc.5/'
RC4_MANIFEST = '4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e'
RC5_MANIFEST = '3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f'
CASES = ('UAT-09-A', 'UAT-09-B', 'UAT-09-C', 'UAT-13-C', 'source-digest-refusal')
PRODUCTS = (
    ('axiom_indexer', 'axiom-indexer', 'stdo_default.json', 'axiomatize-corpus'),
    ('stdo_representation', 'stdo-representation', 'stdo_representation.json', 'stdo-representation'),
)
OLD_RULE = 'The P0 handoff note must list the selected source and companion identities.'
NEW_RULE = OLD_RULE + ' It must also list every unresolved source-meaning condition before the context may be relied on.'
ENV = {k: v for k, v in os.environ.items() if k not in {'PYTHONPATH', 'PYTHONHOME'}}
ENV['PYTHONDONTWRITEBYTECODE'] = '1'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n')


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPOSITORY), *args]).decode().strip()


def command(directory, label, argv, expected):
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / (label + '.command.json')
    if target.exists():
        raise RuntimeError('Refusing to overwrite an actual command observation: ' + str(target))
    done = subprocess.run([str(x) for x in argv], capture_output=True, env=ENV, cwd=REPOSITORY)
    (directory / (label + '.stdout')).write_bytes(done.stdout)
    (directory / (label + '.stderr')).write_bytes(done.stderr)
    write(target, {'argv': [str(x) for x in argv], 'cwd': str(REPOSITORY),
                   'exit_code': done.returncode,
                   'stdout_sha256': sha(done.stdout), 'stderr_sha256': sha(done.stderr)})
    print(json.dumps({'command': label, 'exit_code': done.returncode}), flush=True)
    if done.returncode != expected:
        raise RuntimeError(f'{label}: expected {expected}, observed {done.returncode}; raw output retained')
    try:
        return json.loads(done.stdout)
    except (UnicodeError, ValueError):
        return None


def snapshot(root):
    rows = {}
    for base, dirs, names in os.walk(root, followlinks=False):
        for name in sorted(dirs + names):
            p = Path(base) / name
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                rows[rel] = {'type': 'symlink', 'target': os.readlink(p)}
            elif p.is_file():
                rows[rel] = {'type': 'file', 'sha256': sha(p.read_bytes()), 'mode': p.stat().st_mode & 0o777}
    return rows


def base_definition():
    return {
        '$schema': RC4 + 'standards/schemas/product-definition.schema.json',
        'kind': 'stdo.product-definition',
        'product': {'definition_id': 'urn:p0:product-definition:isolated-update', 'name': 'Isolated P0',
                    'source_project': './', 'bounded_context': None},
        'constitution': {'stdo': {'source': {'repository': str(REPOSITORY)}, 'selector': 'stdo://channels/2.5.0',
                                 'basis': {'uri': RC4, 'manifest_sha256': RC4_MANIFEST}},
                         'additional_authorities': [],
                         'entrypoints': [{'basis': '#/constitution/stdo/basis', 'uri': 'standards/SPEC_METHOD.md'}],
                         'agent_bootstrap': {'entrypoint': '#/constitution/entrypoints/0', 'targets': ['./AGENTS.md', './CLAUDE.md']}},
        'local_constitution': {'axioms': [], 'overrides': [], 'disambiguations': []},
        'reference_frame_bases': [{'uri': './PRODUCT.md#frames', 'authority': ['./PRODUCT.md'],
                                  'applies_to': ['urn:p0:product-definition:isolated-update']}],
        'what': {'intent': './INTENT.md', 'product': './PRODUCT.md', 'specification': ['./requirements/']},
        'how': {'common': [], 'build_tenants': [{'id': 'urn:p0:build-tenant:fixture', 'root': './',
                                               'design': ['./design/'], 'implementation': ['./src/']}]},
        'ticketing': {'goals': './PRODUCT.md', 'tickets': {'root': './tickets/',
                      'lanes': {'backlog': './tickets/backlog/', 'active': './tickets/active/', 'completed': './tickets/completed/'}},
                      'comments': {'root': './comments/'}},
        'composition': [],
    }


def context_program():
    return {'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
            'uri': 'urn:p0:program:native-handoff', 'calculus_ref': RC5 + 'standards/AXIOMATIC_CALCULUS.md',
            'source_basis': 'repo://p0/', 'frame_refs': [],
            'vocabulary_refs': ['urn:p0:operator:requires', 'urn:p0:role:requirement'],
            'symbols': [], 'residuals': [],
            'clauses': [{'uri': 'urn:p0:clause:handoff-note', 'clause_type': 'constraint',
                         'operator': 'urn:p0:operator:requires',
                         'arguments': [{'role': 'urn:p0:role:requirement', 'literal': OLD_RULE}],
                         'statement': OLD_RULE, 'source_refs': ['repo://p0/SOURCE.md#handoff-note']}]}


def prepare():
    if (HERE / 'preparation.json').exists():
        return
    command(HERE / 'setup-observations', 'install-prior-stdo',
            [MANAGER, '--store', STORE, 'install', 'v2.5.0-rc.4', '--repository', REPOSITORY,
             '--manifest-sha256', RC4_MANIFEST], 0)
    old_commit = git('rev-parse', 'refs/tags/stdo_representation/v2.5.0-rc.4^{commit}')
    for product, label, member, skill in PRODUCTS:
        dest = HERE / 'historical-installs' / product
        dest.mkdir(parents=True)
        raw = subprocess.check_output(['git', '-C', str(REPOSITORY), 'archive',
                                       f'refs/tags/{product}/v2.5.0-rc.4:{product}'])
        with tarfile.open(fileobj=io.BytesIO(raw)) as archive:
            archive.extractall(dest, filter='data')
        write(HERE / 'setup-observations' / (product + '-historical-install.json'),
              {'ref': f'refs/tags/{product}/v2.5.0-rc.4', 'commit': old_commit,
               'tree': git('rev-parse', old_commit + ':' + product), 'archive_sha256': sha(raw),
               'files': snapshot(dest)})
    indexer = REPOSITORY / 'axiom_indexer/build_tenants/core/code/ac.py'
    assert sha(indexer.read_bytes()) == '87c43389c619d9ca0e2d930a10e471a17545be9a0394d1c0f47db7e8e2c6d931'
    for name in CASES:
        case = HERE / 'cases' / name
        consumer = case / 'P0'
        consumer.mkdir(parents=True)
        (consumer / 'PRODUCT.md').write_text('# Isolated P0\n\nSynthetic consumer for the expressly granted complete-update qualification.\n\n## Frames\n\nThe supplied task and operation grant select applicable evaluations for this fixture only.\n')
        (consumer / 'INTENT.md').write_text('# P0 Intent\n\nExercise only the selected context update in this isolated fixture.\n')
        (consumer / 'SOURCE.md').write_text('# P0 Source\n\n## Handoff note\n\n' + OLD_RULE + '\n')
        (consumer / 'unrelated.txt').write_text('Prior unrelated local work; preserve these exact bytes.\n')
        (consumer / 'context').mkdir()
        (consumer / 'context/native-entry.md').write_text('# P0 native handoff entry\n\n' + OLD_RULE + '\n')
        document = base_definition()
        for product, label, member, skill in PRODUCTS:
            url = 'https://raw.githubusercontent.com/foolishimp/specification_methodology/' + old_commit
            document['composition'].append({'target_definition_id': 'urn:stdo:product-definition:' + label,
                'relation': './PRODUCT.md', 'product_definition': url + '/' + product + '/' + member,
                'contracts': [url + '/' + product + '/releases/v2.5.0.md']})
            for link, target in [(f'.products/{label}', HERE / 'historical-installs' / product)] + [
                (f'.{host}/skills/{skill}', HERE / 'historical-installs' / product / 'skills' / skill)
                for host in ['agents', 'claude']]:
                path = consumer / link; path.parent.mkdir(parents=True, exist_ok=True); path.symlink_to(target)
        write(consumer / 'stdo_p0.json', document)
        write(consumer / 'context/program.json', context_program())
        write(consumer / 'context/bindings.json', {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
              'bindings': [{'uri_prefix': 'repo://p0/', 'path': str(consumer)},
                           {'uri_prefix': RC5, 'path': '/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.5'}]})
        write(case / 'construction-grant.json', {
            'issuer': '/root', 'actor': '/root/t030_m01_review', 'represented_subject': 'P0-local',
            'source': 'Explicit bounded Writer activation: genuine isolated RC5 complete-update observations; synthetic P0 only; actual plan plus accepted positive, missing acceptance, stale source refusal, and withheld-observation attempt.',
            'write_territory': str(HERE), 'lifetime': 'this isolated qualification',
            'excluded': ['live consumers', 'fleet', 'publication', 'Product meaning', 'native operator authority']})
        command(case / 'observations', 'validate-original-context',
                [PYTHON, indexer, 'validate', '--program', consumer / 'context/program.json',
                 '--bindings', consumer / 'context/bindings.json', '--emit-map', consumer / 'context/map.json'], 0)
        shutil.copytree(consumer, case / 'original-P0', symlinks=True)
        if name in {'UAT-09-C', 'source-digest-refusal'}:
            (consumer / 'SOURCE.md').write_text('# P0 Source\n\n## Handoff note\n\n' + NEW_RULE + '\n')
        if name == 'UAT-09-C':
            command(case / 'observations', 'reindex-changed-source',
                    [PYTHON, indexer, 'validate', '--program', consumer / 'context/program.json',
                     '--bindings', consumer / 'context/bindings.json', '--emit-map', consumer / 'context/map.json'], 0)
        write(case / 'observations' / 'pre-update-state.json', snapshot(consumer))
    write(HERE / 'preparation.json', {'kind': 'rc5.isolated-update-fixture-preparation',
          'manager': str(MANAGER), 'manager_launcher_sha256': sha(MANAGER.read_bytes()),
          'source_indexer_sha256': sha(indexer.read_bytes()), 'cases': list(CASES),
          'case_facts': {'UAT-09-C': 'Source changed; original authored clause and native entry retained; actual Indexer reindex uses changed source.',
                         'source-digest-refusal': 'Source changed after map generation; actual current map retains earlier source observations.'},
          'effect_scope': str(HERE), 'live_consumers_read_or_mutated': []})


def execute(tag_object):
    ref = 'refs/tags/stdo_representation/v2.5.0-rc.5'
    assert git('rev-parse', ref) == tag_object
    commit = git('rev-parse', ref + '^{commit}')
    raw = subprocess.check_output(['git', '-C', str(REPOSITORY), 'show', commit + ':stack_release.json'])
    cohort = json.loads(raw)
    url = cohort['publication']['repository_url'].removesuffix('.git').replace('https://github.com/', 'https://raw.githubusercontent.com/')
    results = {}
    for name in CASES:
        case = HERE / 'cases' / name; consumer = case / 'P0'; obs = case / 'observations'
        selection = {'kind': 'stdo.cohort-update-selection', 'schema_version': 1,
            'definition_id': 'urn:p0:product-definition:isolated-update',
            'cohort': {'repository': str(REPOSITORY), 'ref': ref, 'tag_object': tag_object, 'path': 'stack_release.json'},
            'companions': [], 'derived_context': [{'program': 'context/program.json', 'map': 'context/map.json', 'bindings': 'context/bindings.json'}]}
        for product, label, member, skill in PRODUCTS:
            selection['companions'].append({'product': product, 'definition_member': member,
                'target_definition_id': 'urn:stdo:product-definition:' + label,
                'product_definition': f'{url}/{commit}/{product}/{member}',
                'contracts': [f'{url}/{commit}/{product}/releases/v2.5.0.md'],
                'install_root': str(HERE / 'rc5-installs' / product),
                'links': [{'path': '.products/' + label, 'member': '.'}] + [
                    {'path': f'.{host}/skills/{skill}', 'member': 'skills/' + skill} for host in ['agents', 'claude']]})
        write(case / 'selection.json', selection)
        common = [MANAGER, '--store', STORE, 'cohort-update', '--definition', consumer / 'stdo_p0.json', '--selection', case / 'selection.json']
        before = snapshot(consumer)
        command(obs, 'prior-basis-status', [MANAGER, '--store', STORE, 'status', '--definition', consumer / 'stdo_p0.json', '--verify'], 0)
        held = name == 'source-digest-refusal'
        plan = command(obs, 'complete-plan', [*common, '--dry-run'], 1 if held else 0)
        assert before == snapshot(consumer)
        if name in {'UAT-09-A', 'UAT-13-C'}:
            write(case / 'plan-acceptance.json', {'actor': '/root/t030_m01_review', 'authority': 'construction-grant.json',
                'scope': 'Apply this exact plan once to this isolated P0 under exclusive fixture write scope.',
                'plan_sha256': plan['plan_sha256'], 'plan_file_sha256': sha((obs / 'complete-plan.stdout').read_bytes()),
                'definition_sha256': plan['definition_sha256'], 'selection_sha256': plan['selection_sha256'],
                'consumer': str(consumer), 'does_not_grant': ['native operator retry', 'fleet', 'live consumer effects', 'Product acceptance']})
            applied = command(obs, 'complete-apply', [*common, '--accept-plan-sha256', plan['plan_sha256']], 0)
            assert applied['complete'] and applied['target']['manifest_sha256'] == RC5_MANIFEST
            command(obs, 'resulting-basis-status', [MANAGER, '--store', STORE, 'status', '--definition', consumer / 'stdo_p0.json', '--verify'], 0)
            installed_indexer = consumer / '.products/axiom-indexer/build_tenants/core/code/ac.py'
            command(obs, 'installed-indexer-context-validation', [PYTHON, installed_indexer, 'validate',
                    '--program', consumer / 'context/program.json', '--bindings', consumer / 'context/bindings.json',
                    '--emit-map', obs / 'installed-indexer-map.json'], 0)
            assert (obs / 'installed-indexer-map.json').read_bytes() == (consumer / 'context/map.json').read_bytes()
        elif name == 'UAT-09-B':
            command(obs, 'missing-operation-acceptance', common, 2)
            command(obs, 'unaccepted-plan-digest', [*common, '--accept-plan-sha256', '0' * 64], 2)
            assert before == snapshot(consumer)
        elif held:
            command(obs, 'held-apply-refusal', [*common, '--accept-plan-sha256', plan['plan_sha256']], 2)
            assert before == snapshot(consumer)
        after = snapshot(consumer)
        write(obs / 'post-update-state.json', after)
        write(obs / 'selected-native-routes.json', {
            link['path']: {'target': os.readlink(consumer / link['path']),
                           'resolved_path': str((consumer / link['path']).resolve()),
                           'skill_sha256': sha((consumer / link['path'] / 'SKILL.md').read_bytes())}
            for row in selection['companions'] for link in row['links'] if '/skills/' in link['path']})
        for rel in ['SOURCE.md', 'context/program.json', 'context/map.json', 'context/native-entry.md', 'unrelated.txt']:
            assert before[rel] == after[rel]
        results[name] = {'plan_sha256': plan['plan_sha256'], 'observations': str(obs.relative_to(HERE)),
                         'consumer_changed': before != after, 'source_program_map_native_entry_unrelated_preserved': True}
    write(HERE / 'execution.json', {'kind': 'rc5.installed-complete-update-observations',
        'manager': str(MANAGER), 'selected_ref': ref, 'selected_tag_object': tag_object, 'selected_commit': commit,
        'cohort_sha256': sha(raw), 'cases': results, 'scope': 'Synthetic isolated P0 consumers only; no native LLM verdict or live-consumer claim.'})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--cohort-tag-object')
    args = parser.parse_args()
    prepare()
    if not args.prepare_only:
        if not args.cohort_tag_object:
            parser.error('Exact supplied --cohort-tag-object is required for execution')
        execute(args.cohort_tag_object)


if __name__ == '__main__':
    main()
