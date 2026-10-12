"""Prepare four isolated RC6 native contexts from a frozen cohort candidate.

Only observations and custody are computed here. The independent oracle owns
semantic assessment; it is never copied into an operator worksite.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import jsonschema

HERE = Path(__file__).resolve().parent
PROOF = HERE.parent
ROOT = PROOF.parents[4]
SCRATCH = Path('/private/tmp/stdo-rc6-native-20260906T130745Z')
CUT = 'v2.5.0-rc.6'
ORACLE_SHA = '503bd94a1048d8fba74b5d15dfd2bac9ba0f5974b53b3bb67c2813bee2bf8dce'
TASK_SHA = '27f31eb1c887b65d9babf271309de2f4ef8f1fe06a5bfe4ab47f4bd0d93cae0d'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value, indent=2) + '\n')


def snapshot(root):
    return {str(p.relative_to(root)): {'kind': 'symlink', 'target': str(p.readlink())}
            if p.is_symlink() else {'kind': 'file', 'sha256': sha(p)}
            for p in sorted(root.rglob('*')) if p.is_file() or p.is_symlink()}


def profile(base, work, runtime):
    quote = lambda x: json.dumps(str(x))
    lines = ['(version 1)', '(allow default)']
    hidden = ['/Users/jim/src', '/Users/jim/.codex', '/Users/jim/.codex-alt',
              '/Users/jim/.claude', '/Users/jim/.agents']
    lines += ['(deny file-read* (subpath ' + quote(p) + '))' for p in hidden]
    condition = ('(require-all (subpath ' + quote(base) + ') '
                 '(require-not (subpath ' + quote(work) + ')) '
                 '(require-not (subpath ' + quote(runtime) + '))')
    lines += ['(deny file-read-data ' + condition + '))',
              '(deny file-read-metadata ' + condition + ' (require-not (literal '
              + quote(base) + ')) (require-not (literal ' + quote(work.parent) + '))))',
              '(deny file-write* (require-all (require-not (subpath ' + quote(runtime)
              + ')) (require-not (subpath "/dev"))))']
    return '\n'.join(lines) + '\n'


def copy_product(name, declaration, destination, revision):
    source = ROOT / name
    for member in declaration['subject']['members']:
        src, dst = source / member['path'], destination / member['path']
        observed = hashlib.sha256(os.readlink(src).encode()).hexdigest() if src.is_symlink() else sha(src)
        assert observed == member['sha256'], str(src)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if member['type'] == 'symlink':
            assert os.readlink(src) == member['target']
            dst.symlink_to(member['target'])
        else:
            shutil.copy2(src, dst)
    # External authority/discovery records remain explicitly outside the Product inventory.
    for path in ['AGENTS.md', 'CLAUDE.md', 'specification/GOALS.md',
                 'specification/INTENT.md', 'specification/PRODUCT.md',
                 'specification/REFERENCE_FRAME_BASIS.md', 'releases/v2.5.0.md',
                 'stdo_default.json' if name == 'axiom_indexer' else 'stdo_representation.json']:
        src, dst = source / path, destination / path
        if src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            data = subprocess.check_output(['git', 'show', f'{revision}:{name}/{path}'], cwd=ROOT)
            dst.write_bytes(data)
    definition_name = 'stdo_default.json' if name == 'axiom_indexer' else 'stdo_representation.json'
    definition = json.loads((destination / definition_name).read_text())
    for frame in definition['reference_frame_bases']:
        for reference in frame['authority']:
            path = reference.split('#', 1)[0].removeprefix('./')
            if path.startswith('.ai-workspace/decisions/'):
                dst = destination / path
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(subprocess.check_output(['git', 'show', f'{revision}:{name}/{path}'], cwd=ROOT))


def main():
    assert not SCRATCH.exists(), 'Refuse to overwrite a previous run'
    manifest = json.loads((ROOT / 'stack_release.json').read_text())
    assert manifest['cohort']['cut'] == CUT
    installed = json.loads((PROOF / 'stdo-install.json').read_text())
    source = Path('/Users/jim/Library/Application Support/STDO/releases') / CUT
    assert sha(source / 'manifest.json') == installed['manifest_sha256']
    assert manifest['products']['specification_methodology']['freeze']['installed_manifest_sha256'] == installed['manifest_sha256']
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    committed_manifest = subprocess.check_output(['git', 'show', revision + ':stack_release.json'], cwd=ROOT)
    assert committed_manifest == (ROOT / 'stack_release.json').read_bytes(), 'Commit-B manifest is not frozen'
    oracle = PROOF / 'native-oracle.json'
    task = PROOF / 'native-task.md'
    assert oracle.is_file() and task.is_file()
    assert sha(oracle) == ORACLE_SHA and sha(task) == TASK_SHA, 'Independent task/oracle freeze differs'
    SCRATCH.mkdir()
    write(SCRATCH / 'withheld-sibling.txt', 'Confinement probe; not task evidence.\n')
    cases = []
    for host in ('codex', 'claude'):
        for arm in ('map-first', 'source'):
            name = f'executive-delivery-{host}-{arm}'
            work = SCRATCH / name / 'worksite'
            runtime = SCRATCH / name / 'runtime'
            dest = HERE / 'attempts' / name
            work.mkdir(parents=True)
            runtime.mkdir()
            dest.mkdir(parents=True)
            write(runtime / 'zsh/.zshenv', 'export TMPPREFIX="$TMPDIR/zsh"\n')
            store = work / 'native/stdo-store'
            shutil.copytree(source, store / 'releases' / CUT)
            axi = work / 'native/axiom_indexer'
            rep = work / 'native/stdo_representation'
            copy_product('axiom_indexer', manifest['products']['axiom_indexer'], axi, revision)
            if arm == 'map-first':
                copy_product('stdo_representation', manifest['products']['stdo_representation'], rep, revision)
            write(work / 'task.md', task.read_text())
            write(work / 'native/cohort.json', manifest)
            bindings = {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
                        'bindings': [{'uri_prefix': f'stdo://releases/{CUT}/',
                                      'path': str(store / 'releases' / CUT)}]}
            write(work / 'native/bindings.json', bindings)
            definition = {'$schema': f'stdo://releases/{CUT}/standards/schemas/product-definition.schema.json',
                'kind': 'stdo.product-definition',
                'product': {'definition_id': 'urn:rc6-qualification:delivery', 'name': 'Delivery qualification fixture', 'source_project': './', 'bounded_context': None},
                'constitution': {'stdo': {'source': {'repository': 'https://github.com/foolishimp/specification_methodology.git'},
                    'selector': 'stdo://channels/2.5.0', 'basis': {'uri': f'stdo://releases/{CUT}/', 'manifest_sha256': installed['manifest_sha256']}},
                    'additional_authorities': ['./task.md'], 'entrypoints': [{'basis': '#/constitution/stdo/basis', 'uri': 'standards/authority_compressions/stdo_bootstrap.md'}],
                    'agent_bootstrap': {'entrypoint': '#/constitution/entrypoints/0', 'targets': ['./AGENTS.md', './CLAUDE.md']}},
                'local_constitution': {'axioms': [], 'overrides': [], 'disambiguations': []},
                'reference_frame_bases': [{'uri': './qualification-basis.md', 'authority': ['./task.md'], 'applies_to': ['urn:rc6-qualification:delivery']}],
                'what': {'intent': './task.md', 'product': './task.md', 'specification': ['./task.md']},
                'how': {'common': [], 'build_tenants': [{'id': 'urn:rc6-qualification:delivery-model', 'root': './',
                    'design': ['./task.md#accepted-contracts'], 'implementation': ['./task.md#current-delivery-observations']}]},
                'ticketing': {'goals': './task.md', 'tickets': {'root': './records/', 'lanes': {'backlog': './records/', 'active': './records/', 'completed': './records/'}}, 'comments': {'root': './records/'}}, 'composition': []}
            schema = json.loads((source / 'standards/schemas/product-definition.schema.json').read_text())
            jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(definition)
            write(work / 'stdo_task.json', definition)
            write(work / 'qualification-basis.md', f'''# Qualification frame basis

This controlled fixture selects exact {CUT}, manifest {installed['manifest_sha256']}.
The task owns its hypothetical Product facts and finite evaluation grant.
Acquire the Executive frame and material testing/owner constraints from the
selected STDO baseline. Perform the task's bounded evaluation and return to
the qualification coordinator. Read-only tool use and stdout computation are
allowed. No candidate mutation, actual Worker activation, publication or
consumer adoption is granted. This is a fixture binding, not acceptance of a
real Product or an assertion that the construction candidate is published.
''')
            context = {'subject': 'exact commit-B construction candidate', 'candidate_revision': revision,
                'grant': 'Owner-authorized RC6 qualification; read-only evaluation and stdout computation',
                'caller_definition': 'stdo_task.json', 'caller_frame_basis': 'qualification-basis.md',
                'source_store': str(store), 'source_basis': definition['constitution']['stdo']['basis'],
                'cohort_manifest': 'native/cohort.json', 'axiom_root': str(axi),
                'representation_root': str(rep) if arm == 'map-first' else None,
                'bindings': 'native/bindings.json', 'presentation': arm}
            write(work / 'native-context.json', context)
            names = ['axiomatize-corpus'] + (['stdo-representation'] if arm == 'map-first' else [])
            for hostdir in ('.agents', '.claude'):
                for skill in names:
                    target = 'axiom_indexer' if skill == 'axiomatize-corpus' else 'stdo_representation'
                    link = work / hostdir / 'skills' / skill
                    link.parent.mkdir(parents=True, exist_ok=True)
                    link.symlink_to(f'../../native/{target}/skills/{skill}')
            route = ('Use the discovered stdo-representation skill and begin from its exact selected map. '
                     'Select applicable frames explicitly and re-enter exact source when necessary.'
                     if arm == 'map-first' else
                     'Use the exact Source STDO standards in the bound source store as your governing input. '
                     'No Representation map is supplied in this source-control arm.')
            instruction = ('This is a fresh isolated qualification worksite. Read task.md, native-context.json, '
                           'stdo_task.json and qualification-basis.md. ' + route + '\n'
                           'The candidate inventory and source are exact frozen qualification inputs, not a published Install claim. '
                           'The task grants read-only evaluation; no files may be written. For pure joining, invoke the selected '
                           'ac.py CLI with join --input /dev/stdin, supply your own ordered label/text array on stdin, '
                           'and omit --output so the request is returned on stdout. '
                           'Return the task result, your exact ordered array, and the joined request in your final response. '
                           'Record source re-entry and actual tool observations.\n')
            write(work / 'AGENTS.md', instruction)
            write(work / 'CLAUDE.md', instruction)
            write(dest / 'prompt.txt', 'Complete task.md under the exact qualification grant and supplied native context. Return only the bounded task result and required handoff evidence.\n')
            write(dest / 'sandbox.sb', profile(SCRATCH, work, runtime))
            write(dest / 'snapshot-before.json', snapshot(work))
            shutil.copytree(work, dest / 'input', symlinks=True)
            cases.append({'name': name, 'host': host, 'arm': arm, 'worksite': str(work),
                'runtime': str(runtime), 'directory': str(dest), 'outer_profile': str(dest / 'sandbox.sb'),
                'allowed_writes': [], 'status': 'ready_for_isolation_preflight'})
    write(HERE / 'coverage-selection.json', {'candidate_revision': revision,
        'cohort_manifest_sha256': sha(ROOT / 'stack_release.json'), 'source_manifest_sha256': installed['manifest_sha256'],
        'oracle_sha256': sha(oracle), 'task_sha256': sha(task), 'prepare_sha256': sha(Path(__file__)),
        'scope': 'One Executive task in each host and presentation; no repeated-J stability claim.', 'contexts': cases})
    print(json.dumps({'contexts': len(cases), 'candidate_revision': revision}))


if __name__ == '__main__':
    main()
