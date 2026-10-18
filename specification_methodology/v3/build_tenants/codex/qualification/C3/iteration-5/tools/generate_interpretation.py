"""Generate the current interpretation through the checked shared compiler.

All I5 evidence is written under this iteration. Stable program identities and
the I3 repaired compiler rules are retained; no historical receipt is rebound.
"""
import argparse
import build_interpretation as build
from pathlib import Path
import subprocess
import sys
from context import HERE, PACKAGE, REPO, INPUTS, git_bytes, library, read, sha, write, verify_common


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--account-commit', required=True)
    parser.add_argument('--theory-root', type=Path, required=True)
    args = parser.parse_args()
    verify_common()
    account_path = HERE / 'DETERMINATIONS.json'
    account_raw = account_path.read_bytes()
    if git_bytes(args.account_commit, account_path.relative_to(REPO)) != account_raw:
        raise ValueError('Account differs from its frozen commit')
    account = read(account_path)
    current, exclusions = build.semantic_projection(account)
    rows = build.validate_account(current)
    commit, members = build.documentary_inventory(args.source_commit)
    if account['subject']['source_commit'] != commit or account['subject']['common_input'] != INPUTS['common_input']:
        raise ValueError('Account source/common basis differs')
    dependencies = build.verify_dependencies(args.theory_root)
    program, mapping, frames = build.build_program(current)
    expanded, _, _ = build.build_program(current, compact_qualifications=False)
    equivalence = build.qualification_equivalence(program, expanded)
    mapped = {'kind': 'stdo.method-interpretation-mapping', 'schema_version': 1,
              'document_source_input_commit': commit, 'rows': mapping,
              'optional_family_indexes': build.family_mappings(current),
              'source_route_rule': 'Stable original source identity; native checker aliases resolve the same exact heading/body. Source provenance and conditional acquisition retain their declared roles.'}
    inventory = {'kind': 'stdo.method-interpretation-source', 'schema_version': 1,
        'document_source_input_commit': commit, 'document_members': members,
        'excluded_from_documentary_subject': ['interpretation/'],
        'encoding_theory': {'release_uri': build.THEORY_URI, 'manifest_sha256': build.MANIFEST_SHA,
            'member': 'standards/AXIOMATIC_CALCULUS.md', 'member_sha256': build.THEORY_SHA},
        'checker': {'product': 'urn:stdo:product-definition:axiom-indexer',
            'release_ref': 'refs/tags/axiom_indexer/v2.5.1-rc.2',
            'commit': '9a9c479776ffd974fbcafcf48341980918209aef',
            'executable_sha256': build.TOOL_SHA,
            'inventory_sha256': dependencies['inventory_sha256']},
        'interpretation': {'program_uri': program['uri'], 'program_file_sha256': sha(build.json_bytes(program)),
            'semantic_account_sha256': sha(build.json_bytes(current)), 'vocabulary_sha256': sha(build.SIGNATURE.encode()),
            'frames_sha256': sha(frames.encode()), 'mapping_sha256': sha(build.json_bytes(mapped))},
        'carrier': {'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
            'schema_sha256': sha((build.INSTALL / 'skills/axiomatize-corpus/references/program.schema.json').read_bytes())}}
    output = PACKAGE / 'interpretation'
    contents = {'README.md': build.README.encode(), 'SIGNATURE.md': build.SIGNATURE.encode(),
                'FRAMES.md': frames.encode(), 'bindings.py': build.BINDINGS_SCRIPT.encode()}
    contents.update({k:build.json_bytes(v) for k,v in {
        'SOURCE_INVENTORY.json':inventory, 'MAPPING.json':mapped,
        'source-account.json':current, 'program.json':program}.items()})
    for name, data in contents.items():
        (output / name).write_bytes(data)
    evidence = HERE / 'interpretation'
    evidence.mkdir(exist_ok=True)
    binding_path = evidence / 'bindings.json'
    write(binding_path, {'kind':'axiom-indexer.binding-set','schema_version':1,
        'bindings':[{'uri_prefix':build.URI,'path':str(PACKAGE)},
                    {'uri_prefix':build.THEORY_URI,'path':str(args.theory_root.resolve())}]})
    run = subprocess.run([sys.executable, '-B', str(build.TOOL), 'validate',
        '--program', str(output/'program.json'), '--bindings', str(binding_path),
        '--output', str(evidence/'validation.json'), '--emit-map', str(output/'map.json')],
        capture_output=True,text=True)
    if run.returncode:
        raise RuntimeError(run.stdout + run.stderr)
    write(evidence/'DEPENDENCY_VERIFICATION.json', dependencies)
    report = {'document_source_input_commit':commit, 'common_input_commit':INPUTS['common_input'],
              'account_input_commit':args.account_commit, 'account_sha256':sha(account_raw),
              'semantic_account_sha256':sha(build.json_bytes(current)),
              'determinations':len(rows),'clauses':len(program['clauses']),
              'indexes':len(program['frame_indexes']),'residuals':len(program['residuals']),
              'shared_contracts':len(current['semantic_contracts']),
              'compiler_sha256':sha(Path(build.__file__).read_bytes()),
              'qualification_equivalence':equivalence,
              'excluded_construction_metadata':exclusions,
              'native_validation':'passed',
              'limits':['Mechanical resolution and structure only; source fidelity and actual use remain separately assessed.']}
    write(evidence/'GENERATION.json',report)
    write(evidence/'QUALIFICATION_EQUIVALENCE.json',equivalence)
    print({k:report[k] for k in ('determinations','clauses','indexes','residuals','native_validation')})


if __name__ == '__main__':
    main()
