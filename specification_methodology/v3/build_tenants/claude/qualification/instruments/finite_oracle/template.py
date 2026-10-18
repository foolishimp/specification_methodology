"""Finite oracle template: exhaust a declared finite domain against an
independently specified oracle, and bind the result to its exact inputs.

A qualification instrument; it is not candidate law and supports no
disposition. An instance is a directory with three files:

- model.py, the implementation under test: it encodes one rule of a member
  and declares, in SOURCE, the member and the digests of the sections it
  encodes;
- mutants.py, deliberately wrong variants of that rule, returned by
  variants(model);
- check.py, the oracle: the declared domain, the properties written from
  their sources (declared in ORACLE_SOURCES) without reading the model, the
  cardinalities derived by hand, the expected counterexamples of each
  mutant, and the limits of what the check proves. It loads this template
  and calls run().

run() refuses (exit 2), writing nothing, when a declared section has
changed since it was encoded. Otherwise it enumerates every case of the
domain; asserts every property on every lawful value of every output of
the model; evaluates the same properties on each mutant and counts its
counterexamples, a counterexample being a case on which any output fails
any property, and counts the cases on which its outputs, its flat reported
values and its records differ from the model's; asserts the expected
cardinalities and counts; binds the digests of source, oracle sources,
model, mutants and executables; and writes the result. A failed assertion
writes nothing.
`--check` writes nothing and exits 1 when the result on disk differs from
the one the run would write.

Pattern ported from Codex qualification/C3/a_c/finite_check.py at 31f28f9;
README.md records the lines kept verbatim and the adaptations.
"""
import hashlib
import itertools
import json
from pathlib import Path
import importlib.util
import sys

if not __debug__:
    raise SystemExit('Finite proof refuses disabled assertions; run without -O/PYTHONOPTIMIZE.')

TEMPLATE = Path(__file__).resolve()
TENANT_ROOT = TEMPLATE.parents[3]
SECTION_RULE = TEMPLATE.parents[1] / 'generate_frames.py'


def load(name, path):
    """Load a module by path; `python3 -I` puts no script directory on sys.path."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def refuse(message):
    """A refusal writes nothing and exits 2, as generate_frames.py does."""
    print(message, file=sys.stderr)
    raise SystemExit(2)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    """A tenant-relative POSIX path, so the result is the same on every checkout."""
    path = Path(path).resolve()
    try:
        return path.relative_to(TENANT_ROOT).as_posix()
    except ValueError:
        refuse(f'refusal: {path}: bound file is outside the tenant root {TENANT_ROOT}')


class Count:
    """Every assertion of the check goes through check(), so the number made is measured."""

    def __init__(self):
        self.made = 0

    def check(self, condition, message):
        self.made += 1
        assert condition, message


def bind(declaration, frames):
    """Return the binding of one declared source, or refuse if a declared section changed.

    The section extents follow the one section rule of generate_frames.py
    (design/CROSS_SYNTHESIS.md part 5, requirements 1 and 2).
    """
    path = (TENANT_ROOT / declaration['path']).resolve()
    data = path.read_bytes()
    try:
        member = frames.Member(declaration['path'], data)
    except frames.Refusal as refusal:
        refuse(str(refusal))
    sections = []
    for anchor, declared in declaration['sections'].items():
        try:
            start, end, extent = member.section(anchor)
        except frames.Refusal as refusal:
            refuse(str(refusal))
        actual = hashlib.sha256(extent).hexdigest()
        if actual != declared:
            refuse(
                f'refusal: {declaration["path"]}#{anchor}: section sha256 {actual} differs from the '
                f'declared {declared}; the encoding was judged against the declared bytes only, so it '
                'must be re-reviewed against the changed section and re-declared before this check runs')
        sections.append({'anchor': anchor, 'lines': f'{start + 1}-{end}', 'sha256': actual})
    return {'path': declaration['path'], 'sha256': hashlib.sha256(data).hexdigest(), 'sections': sections}


def evaluate(oracle, model, rule, case):
    """Outputs of one rule on one case, with the properties each lawful value fails."""
    results = []
    for label, lawful, record in oracle.outputs(model, rule, case):
        failed = set()
        if not lawful:
            failed.add('lawful_value_exists')
        for value in sorted(lawful):
            failed |= {name for name, holds in oracle.properties(case, value, record).items() if not holds}
        results.append((label, lawful, record, failed))
    return results


def plain(case):
    return {key: list(value) if isinstance(value, tuple) else value for key, value in case.items()}


def run(oracle, argv):
    check_only = argv[1:] == ['--check']
    if argv[1:] and not check_only:
        raise SystemExit('usage: check.py [--check]')
    root = Path(oracle.__file__).resolve().parent
    frames = load('section_rule', SECTION_RULE)
    model = load('model', root / 'model.py')
    mutants = load('mutants', root / 'mutants.py')
    source = bind(model.SOURCE, frames)
    oracle_sources = [bind(declaration, frames) for declaration in oracle.ORACLE_SOURCES]

    names = [name for name, _ in oracle.DIMENSIONS]
    domain = [dict(zip(names, values)) for values in itertools.product(*[v for _, v in oracle.DIMENSIONS])]
    count = Count()

    # Model: every property on every lawful value of every output, as an assertion.
    classes = {}
    outputs = value_checks = 0
    model_outputs = []
    for case in domain:
        evaluated = evaluate(oracle, model, model.RULE, case)
        model_outputs.append(evaluated)
        for label, lawful, record, failed in evaluated:
            outputs += 1
            value_checks += len(lawful)
            count.check(lawful, f'no lawful value: {plain(case)} {label}')
            for value in sorted(lawful):
                for name, holds in oracle.properties(case, value, record).items():
                    count.check(holds, f'{name} fails on the model: {plain(case)} {label} value={value} record={record}')
        _, lawful, record, _ = evaluated[0]
        for name in oracle.classes(case, lawful, record):
            classes[name] = classes.get(name, 0) + 1

    # Mutants: the same properties, counted; a counterexample is a case on which any output fails any.
    mutant_reports = {}
    for name, rule in mutants.variants(model).items():
        by_property, first_by_property = {}, {}
        counterexamples = output_differs = value_set_differs = record_differs = 0
        first = None
        for case, expected in zip(domain, model_outputs):
            evaluated = evaluate(oracle, model, rule, case)
            failed = set().union(*(f for _, _, _, f in evaluated))
            if failed:
                counterexamples += 1
                example = {'case': plain(case), 'failed': sorted(failed),
                           'model': {'lawful': sorted(expected[0][1]), 'record': expected[0][2]},
                           'mutant': {'lawful': sorted(evaluated[0][1]), 'record': evaluated[0][2]}}
                first = first or example
                for prop in failed:
                    by_property[prop] = by_property.get(prop, 0) + 1
                    first_by_property.setdefault(prop, example['case'])
            if [(l, s, r) for l, s, r, _ in evaluated] != [(l, s, r) for l, s, r, _ in expected]:
                output_differs += 1
            if evaluated[0][1] != expected[0][1]:
                value_set_differs += 1
            if [r for _, _, r, _ in evaluated] != [r for _, _, r, _ in expected]:
                record_differs += 1
        mutant_reports[name] = {
            'predicate': f'the variant {name} meets every property on the declared domain',
            'core_value': 'falsified' if counterexamples else 'satisfied',
            'counterexample_cases': counterexamples,
            'by_property': dict(sorted(by_property.items())),
            'output_differs_from_model': output_differs,
            'value_set_differs_from_model': value_set_differs,
            'record_differs_from_model': record_differs,
            'first_counterexample': first,
            'first_counterexample_by_property': dict(sorted(first_by_property.items())),
        }

    # Independently derived cardinalities and counterexample counts (declared in check.py).
    expected = oracle.EXPECTED
    count.check(len(domain) == expected['cases'], f'cases {len(domain)} != {expected["cases"]}')
    count.check(outputs == expected['outputs'], f'outputs {outputs} != {expected["outputs"]}')
    count.check(value_checks == expected['value_checks'], f'value checks {value_checks} != {expected["value_checks"]}')
    count.check(classes == expected['classes'], f'classes {classes} != {expected["classes"]}')
    count.check(set(mutant_reports) == set(oracle.EXPECTED_MUTANTS), 'mutant set differs from the declared one')
    for name, report in mutant_reports.items():
        want = oracle.EXPECTED_MUTANTS[name]
        count.check(report['counterexample_cases'] > 0, f'mutant {name} is not detected')
        for key in ('counterexample_cases', 'by_property', 'output_differs_from_model',
                    'value_set_differs_from_model', 'record_differs_from_model'):
            count.check(report[key] == want[key], f'mutant {name} {key} {report[key]} != {want[key]}')

    bound = lambda path: {'path': relative(path), 'sha256': sha256(path)}
    report = {
        'kind': 'finite_oracle_result',
        'instance': oracle.INSTANCE,
        'evidence_class': 'tested against an independently specified oracle',
        'result': {'predicate': oracle.PREDICATE, 'core_value': 'satisfied',
                   'domain_outcome': f'all {count.made} assertions hold; every declared mutant is falsified'},
        'bindings': {
            'source': source,
            'oracle_sources': oracle_sources,
            'model': bound(root / 'model.py'),
            'mutants': bound(root / 'mutants.py'),
            'executable': [bound(TEMPLATE), bound(Path(oracle.__file__)), bound(SECTION_RULE)],
        },
        'domain': oracle.DOMAIN_DESCRIPTION,
        'properties': oracle.PROPERTIES,
        'counts': {'cases': len(domain), 'outputs': outputs, 'value_checks': value_checks,
                   'assertions': count.made, 'classes': dict(sorted(classes.items()))},
        'mutants': mutant_reports,
        'limits': oracle.LIMITS,
    }
    text = json.dumps(report, indent=2) + '\n'
    if check_only:
        on_disk = (root / 'FINITE_RESULT.json')
        if not on_disk.is_file() or on_disk.read_text() != text:
            print('drift: FINITE_RESULT.json differs from the result this run would write')
            return 1
        print('FINITE_RESULT.json is current')
        return 0
    (root/'FINITE_RESULT.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
    return 0
