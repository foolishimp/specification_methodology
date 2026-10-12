"""Prepare two isolated RC7 native contexts from a frozen cohort candidate.

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
SCRATCH = PROOF / 'native-short-temp2.20260915T093130Z'
CUT = 'v2.5.0-rc.7'
ORACLE_SHA = 'ce1a9c8bc6e04761b006146fda377e0a34903f7a61e891fd45d05044d625cc14'
TASK_SHA = '31708b75f8af7af320022ef919a4781cc4a94f60e1367194a8b699d303152f47'


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
    # Task-local temporary worksites are inside the grant's evidence root.
    # Permit their exact data and ancestor metadata, while withholding all other
    # repository data, actor history and the oracle through the same OS boundary.
    for path in hidden:
        exclusion = '(require-all (subpath ' + quote(path) + ') (require-not (subpath ' + quote(work) + ')) (require-not (subpath ' + quote(runtime) + ')))'
        lines += ['(deny file-read-data ' + exclusion + ')']
        if not str(work).startswith(path + '/'):
            lines += ['(deny file-read-metadata (subpath ' + quote(path) + '))']
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
            data = src.read_bytes()
            dst.write_bytes(data)
    definition_name = 'stdo_default.json' if name == 'axiom_indexer' else 'stdo_representation.json'
    definition = json.loads((destination / definition_name).read_text())
    for frame in definition['reference_frame_bases']:
        for reference in frame['authority']:
            path = reference.split('#', 1)[0].removeprefix('./')
            if path.startswith('.ai-workspace/decisions/'):
                dst = destination / path
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes((source / path).read_bytes())


def main():
    assert not SCRATCH.exists(), 'Refuse to overwrite a previous run'
    manifest = json.loads((ROOT / 'stack_release.json').read_text())
    assert manifest['cohort']['cut'] == CUT
    installed = json.loads((PROOF / 'stdo-install.json').read_text())
    source = Path('/Users/jim/Library/Application Support/STDO/releases') / CUT
    assert sha(source / 'manifest.json') == installed['manifest_sha256']
    assert manifest['products']['specification_methodology']['freeze']['installed_manifest_sha256'] == installed['manifest_sha256']
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    assert revision == 'ddeb971da89ee47065359c99897a825b803eedd4', 'Unexpected Stage A HEAD'
    assert sha(ROOT / 'stack_release.json') == '8658c9bfdb6540960b1fbb0510d8c4123b982e7818841318ed46f844e0afa587', 'Candidate carrier drift'
    assert json.loads((PROOF / 'stage-b-mechanical-checks.json').read_text())['status'] == 'satisfied'
    oracle = PROOF / 'native-oracle.md'
    task = PROOF / 'native-task.md'
    assert oracle.is_file() and task.is_file()
    assert sha(oracle) == ORACLE_SHA and sha(task) == TASK_SHA, 'Independent task/oracle freeze differs'
    SCRATCH.mkdir()
    write(SCRATCH / 'withheld-sibling.txt', 'Confinement probe; not task evidence.\n')
    cases = []
    for host in ('codex', 'claude'):
        for arm in ('map-first',):
            name = f'executive-attention-{host}-{arm}'
            work = SCRATCH / name / 'worksite'
            runtime = SCRATCH / name / 'runtime'
            dest = HERE / 'attempts2' / name
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
            import re
            c1, c2 = re.findall(r'```markdown\n(.*?)```', task.read_text(), re.S)
            assert c1.endswith('\n') and c2.endswith('\n')
            write(work / 'fixtures/C1/current.md', c1)
            write(work / 'fixtures/C2/current.md', c2)
            write(work / 'draft/current.md', c2)
            write(work / 'evidence.json', {
                'kind': 'controlled-fixture-observations', 'authority': 'task.md',
                'not_live_test_or_review_results': True,
                'snapshots': 'task.md#work-record-snapshots',
                'C1': {'path': 'fixtures/C1/current.md', 'sha256': sha(work / 'fixtures/C1/current.md')},
                'C2': {'path': 'fixtures/C2/current.md', 'current_path': 'draft/current.md', 'sha256': sha(work / 'fixtures/C2/current.md')},
                'E1': {'candidate': 'C1', 'observation': 'passing mechanical rendering/link check', 'independent': False},
                'E2': {'candidate': 'C2', 'observation': 'passing mechanical rendering/link check', 'independent': False},
                'H0': {'observation': 'historical RC6 link unchanged', 'valid': True},
                'J1': {'candidate': 'C1', 'actor': 'W', 'class': 'author self-review'},
                'J2': {'candidate': 'C2', 'actor': 'W', 'class': 'author self-review'},
                'R1': {'candidate': 'C1', 'class': 'independent review', 'rendering_assessment': 'invalidated for C2 by material markup change'},
                'R2': {'availability': 'S7 only; not available in S5', 'exact_record': 'task.md#work-record-snapshots'},
                'row_independence': 'Consume only the evidence supplied by each task snapshot; do not import another row.'})
            write(work / 'native/cohort.json', manifest)
            bindings = {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
                        'bindings': [{'uri_prefix': f'stdo://releases/{CUT}/',
                                      'path': str(store / 'releases' / CUT)}]}
            write(work / 'native/bindings.json', bindings)
            definition = {'$schema': f'stdo://releases/{CUT}/standards/schemas/product-definition.schema.json',
                'kind': 'stdo.product-definition',
                'product': {'definition_id': 'urn:rc7-qualification:delivery', 'name': 'Delivery qualification fixture', 'source_project': './', 'bounded_context': None},
                'constitution': {'stdo': {'source': {'repository': 'https://github.com/foolishimp/specification_methodology.git'},
                    'selector': 'stdo://channels/2.5.0', 'basis': {'uri': f'stdo://releases/{CUT}/', 'manifest_sha256': installed['manifest_sha256']}},
                    'additional_authorities': ['./task.md'], 'entrypoints': [{'basis': '#/constitution/stdo/basis', 'uri': 'standards/authority_compressions/stdo_bootstrap.md'}],
                    'agent_bootstrap': {'entrypoint': '#/constitution/entrypoints/0', 'targets': ['./AGENTS.md', './CLAUDE.md']}},
                'local_constitution': {'axioms': [], 'overrides': [], 'disambiguations': []},
                'reference_frame_bases': [{'uri': './qualification-basis.md', 'authority': ['./task.md'], 'applies_to': ['urn:rc7-qualification:delivery']}],
                'what': {'intent': './task.md', 'product': './task.md', 'specification': ['./task.md']},
                'how': {'common': [], 'build_tenants': [{'id': 'urn:rc7-qualification:delivery-model', 'root': './',
                    'design': ['./task.md#work-and-authority'], 'implementation': ['./task.md#work-record-snapshots']}]},
                'ticketing': {'goals': './task.md', 'tickets': {'root': './records/', 'lanes': {'backlog': './records/', 'active': './records/', 'completed': './records/'}}, 'comments': {'root': './records/'}}, 'composition': []}
            schema = json.loads((source / 'standards/schemas/product-definition.schema.json').read_text())
            jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(definition)
            write(work / 'stdo_task.json', definition)
            write(work / 'qualification-basis.md', f'''# Qualification frame basis

This controlled fixture selects exact {CUT}, manifest {installed['manifest_sha256']}.
The task owns its hypothetical Product facts and finite evaluation grant.
Acquire the Executive and Reviewer frames and material owner constraints from the
selected STDO baseline. Perform the task's bounded evaluation and return to
the qualification coordinator. Read-only tool use and stdout computation are
allowed. No candidate mutation, actual Worker activation, publication or
consumer adoption is granted. This is a fixture binding, not acceptance of a
real Product or an assertion that the construction candidate is published.
''')
            context = {'subject': 'exact pre-commit-B construction candidate', 'stage_a_revision': revision, 'candidate_manifest_sha256': sha(ROOT / 'stack_release.json'),
                'grant': 'Owner-authorized RC7 qualification; read-only evaluation and stdout computation',
                'caller_definition': 'stdo_task.json', 'caller_frame_basis': 'qualification-basis.md',
                'source_store': str(store), 'source_basis': definition['constitution']['stdo']['basis'],
                'cohort_manifest': 'native/cohort.json', 'axiom_root': str(axi),
                'representation_root': str(rep) if arm == 'map-first' else None,
                'bindings': 'native/bindings.json', 'presentation': arm,
                'candidate_evidence_routes': {'C1': 'fixtures/C1/current.md', 'C2': 'fixtures/C2/current.md', 'current': 'draft/current.md', 'observations': 'evidence.json', 'snapshots': 'task.md#work-record-snapshots'}}
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
            write(dest / 'prompt.txt', 'Complete task.md under the exact qualification grant and supplied native context. Return only the bounded task result and required handoff evidence. Keep the JSON concise, targeting 900 words including the joined request. Read the native skill and exact context, then use targeted JSON extraction and ac.py project for material frames; do not dump the complete program, map, or corpus. One compact inspection can recover the exact relevant baseline sections. Seven handoff sections can each be one or two sentences.\n')
            write(dest / 'sandbox.sb', profile(SCRATCH, work, runtime))
            write(dest / 'snapshot-before.json', snapshot(work))
            shutil.copytree(work, dest / 'input', symlinks=True)
            cases.append({'name': name, 'host': host, 'arm': arm, 'worksite': str(work),
                'runtime': str(runtime), 'directory': str(dest), 'outer_profile': str(dest / 'sandbox.sb'),
                'allowed_writes': [], 'status': 'ready_for_isolation_preflight'})
    write(HERE / 'coverage-selection.json', {'candidate_revision': revision,
        'cohort_manifest_sha256': sha(ROOT / 'stack_release.json'), 'source_manifest_sha256': installed['manifest_sha256'],
        'oracle_sha256': sha(oracle), 'task_sha256': sha(task), 'prepare_sha256': sha(Path(__file__)),
        'scope': 'One controlled Executive ledger and pure-join Reviewer handoff per host/arm. No runtime notification, wall-clock intervention, repeated-run reliability or model/cost superiority claim.', 'contexts': cases})
    print(json.dumps({'contexts': len(cases), 'candidate_revision': revision}))


if __name__ == '__main__':
    main()
