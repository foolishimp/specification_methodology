"""Current source-package checks; artifact success is not semantic acceptance."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from refresh_current import (HERE, TENANT, PACKAGE, PREVIOUS, PARSE, load_module,
                             read, sha, verify_common, protected_pins, render_views,
                             refresh_views, compression_body, compression_owners)


def fingerprint():
    return hashlib.sha256(json.dumps({
        'package': PARSE.tree_pins(PACKAGE),
        'inputs': {n: sha(HERE / n) if (HERE / n).exists() else None for n in
                   ['CANDIDATE.json', 'FRAME_INPUTS.json', 'CONSERVATION.json', 'FRONTIER.json',
                    'refresh_current.py', 'check_current.py', 'check_conservation.py']}
    }, sort_keys=True).encode()).hexdigest()


def generation_experiment(common):
    """Repeat real generation in a disposable copy and test preservation guards."""
    with tempfile.TemporaryDirectory(prefix='i3-package-check-') as td:
        root = Path(td).resolve()
        package, support = root / 'package', root / 'support'
        shutil.copytree(PACKAGE, package)
        support.mkdir()
        for name in ['FRAME_INPUTS.json', 'CONSERVATION.json', 'FRONTIER.json']:
            shutil.copyfile(HERE / name, support / name)
        # Arbitrary current/unknown semantic fields must survive unchanged.
        p = support / 'CONSERVATION.json'
        value = read(p)
        value['preservation_probe'] = {'meaning': 'retain-current-author-proposal', 'unknown_future_field': [0, False, None]}
        p.write_text(json.dumps(value) + '\n')
        before = protected_pins(support)
        def state():
            return {'package': PARSE.tree_pins(package), 'index': sha(support / 'FRAME_INPUTS.json')}
        initial = state()
        refresh_views(common, package, support)
        first = state()
        refresh_views(common, package, support)
        second = state()
        conservation_preserved = protected_pins(support) == before
        # A changed owner's body cannot be silently blessed by a digest refresh.
        owner = package / 'standards/FOUNDATIONS.md'
        owner.write_text(owner.read_text() + '\nChanged-owner probe.\n')
        unchanged_before_refusal = state()
        try:
            refresh_views(common, package, support)
            source_drift_refused = False
        except ValueError:
            source_drift_refused = state() == unchanged_before_refusal
        owner.write_bytes((PACKAGE / 'standards/FOUNDATIONS.md').read_bytes())
        view = package / 'standards/authority_compressions/stdo_bootstrap.md'
        view.write_text(view.read_text() + '\nUnreconciled summary probe.\n')
        unchanged_before_refusal = state()
        try:
            refresh_views(common, package, support)
            body_drift_refused = False
        except ValueError:
            body_drift_refused = state() == unchanged_before_refusal
        return {'already_current': initial == first, 'repeat_identical': first == second,
                'semantic_map_and_frontier_preserved': conservation_preserved,
                'changed_owner_refused_before_writes': source_drift_refused,
                'unreconciled_summary_refused_before_writes': body_drift_refused,
                'scope': 'Generation behavior in a disposable copy; no semantic fidelity conclusion.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--idempotence', action='store_true')
    parser.add_argument('--draft', action='store_true', help='Check working source before final freeze; cannot yield frozen-artifact validity')
    args = parser.parse_args()
    started = time.monotonic()
    before = fingerprint()
    current = read(HERE / 'CANDIDATE.json')
    common = read(HERE / 'FRAME_INPUTS.json')['input_commit']
    verify_common(common)
    # Explicit current inputs; no rebinding a historical __file__ or outputs.
    checker = load_module('selected_artifact_algorithms', PREVIOUS / 'synthesis/check_artifacts.py')
    checker.HERE, checker.SUPPORT = HERE, HERE
    checker.TENANT, checker.PACKAGE = TENANT, PACKAGE
    checker.COMMON = TENANT.parents[1] / 'specification/requirements/PREDECESSOR_CLAIMS.md'
    check = checker.Check()
    methods = ['links_and_surface', 'excerpts', 'compressions', 'ownership_signals']
    if not args.draft:
        methods.insert(0, 'inventory')
    for method in methods:
        try:
            getattr(check, method)()
        except Exception as error:
            check.fail(method, type(error).__name__ + ': ' + str(error))
    try:
        for path in (PACKAGE / 'standards/authority_compressions').glob('*.md'):
            pair = compression_body(path)
            if pair is None:
                continue
            review = read(HERE / 'FRAME_INPUTS.json')['compression_body_reviews'].get(str(path.relative_to(PACKAGE)), {})
            if (review.get('body_sha256') != hashlib.sha256(pair[1].encode()).hexdigest()
                    or review.get('owner_pins') != compression_owners(path)):
                check.fail('compression_reconciliation', str(path.relative_to(PACKAGE)))
        # The same pure rendering must produce the exact current frame bodies.
        changes, expected_index = render_views(PACKAGE, HERE, common)
        for path, text in changes.items():
            if path.read_text() != text:
                check.fail('generation', 'Current derivative differs: ' + str(path.relative_to(PACKAGE)))
        if expected_index != read(HERE / 'FRAME_INPUTS.json'):
            check.fail('generation', 'Frame index differs from current generation')
    except Exception as error:
        check.fail('generation', str(error))
    if not args.draft:
        if current.get('source_input_commit') != common or not current.get('document_source_input_commit'):
            check.fail('source', 'Common/document source coordinates are missing or inconsistent')
        run = subprocess.run([sys.executable, '-B', str(HERE / 'check_conservation.py'), '--require-frozen', '--no-write'],
                             cwd=TENANT, capture_output=True, text=True)
        try:
            report = json.loads(run.stdout)
        except ValueError:
            report = {}
        check.details['conservation_owner_check'] = {'exit_code': run.returncode,
            'checker_sha256': sha(HERE / 'check_conservation.py'), 'report': report,
            'stderr': run.stderr}
        if run.returncode or not report.get('draft_valid'):
            check.fail('conservation', 'Owning conservation check did not establish a current frozen draft')
    if args.idempotence:
        experiment = generation_experiment(common)
        check.details['generation_experiment'] = experiment
        for name, result in experiment.items():
            if result is False:
                check.fail('generation_experiment', name)
    # Reuse schema validation without pretending the new source interpretation
    # has a selected immutable-release packaging/installation contract.
    try:
        from jsonschema import Draft202012Validator
        for name in ['product-definition.schema.json', 'installed-release-manifest.schema.json']:
            Draft202012Validator.check_schema(read(PACKAGE / 'standards/schemas' / name))
        check.counts['schemas_structurally_valid'] = 2
    except Exception as error:
        check.fail('schema', str(error))
    after = fingerprint()
    if before != after:
        check.fail('subject', 'Source or determining inputs changed during checking')
    report = {'kind': 'stdo.current-source-artifact-check', 'draft': args.draft,
              'valid': not check.failures, 'frozen_artifact_valid': not args.draft and not check.failures,
              'source_input_commit': common, 'inventory_input_commit': current.get('inventory_input_commit'),
              'document_source_input_commit': current.get('document_source_input_commit'),
              'fingerprint_before': before, 'fingerprint_after': after,
              'checker_sha256': sha(Path(__file__)), 'historical_algorithms_sha256': sha(PREVIOUS / 'synthesis/check_artifacts.py'),
              'python_executable': sys.executable, 'python_version': sys.version,
              'counts': check.counts, 'details': check.details, 'failures': check.failures,
              'elapsed_seconds': round(time.monotonic() - started, 3),
              'limits': ['Author artifact checks, not semantic acceptance or whole-method fitness.',
                         'Exact excerpts and declared routes do not establish frame sufficiency.',
                         'Compression body reconciliation is author evidence, not independent fidelity.',
                         'interpretation/ is source-package material; its issued installation contract remains unselected.',
                         'Schemas checked for structure only; no installed-v3 publication, plugin-host or adoption claim.',
                         'External links not fetched; exact installed rc.2 logical routes checked locally.']}
    (HERE / 'ARTIFACT_CHECK.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k:report[k] for k in ['valid','draft','counts','failures','elapsed_seconds']}, indent=2))
    return 0 if report['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
