"""Assemble the iteration 3 fragments into one axiomatic program, with the tenant pre-check.

This is the tenant pre-check of design/INTERPRETATION.md section 4. It is
not a mechanical result of the Axiom Indexer: it checks only the rules of
a_c/i3/SIGNATURE.md that the checker's schema does not, and it establishes
no fidelity.

Usage, from the tenant root:
    python3 -I a_c/i3/tools/assemble.py            # write program, bindings, coverage
    python3 -I a_c/i3/tools/assemble.py --check    # write nothing; exit 0 if outputs are current
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
I3 = ROOT / 'a_c' / 'i3'
V = 'urn:stdo-3:claude:i3:vocabulary:'
STANDING = 'urn:stdo-3:claude:i3:standing:'
CORE = 'urn:stdo-3:claude:i3:core:'
CORE_VALUES = {CORE + v for v in ('satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis')}
SOURCE = 'stdo-3://build_tenants/claude/standards/'
SUPPORT_KINDS = ('stated-formula', 'discharged-argument', 'mechanically-checked-structure',
                 'externally-assessed-predicate', 'execution-evidence')
ASSURANCE_SECTIONS = ('construction-relation', 'construction-synthesis', 'assurance-relations',
                      'preservation-through-construction', 'assertions-and-observation',
                      'parallel-derivation-and-mutual-assurance', 'quantified-assurance',
                      'change-impact-and-evidence-reuse', 'formal-representation')  # FOUNDATIONS §4 Formal representation (I5)
DISPOSITIONS = ('encoded', 'encoded-in-part', 'uses owner', 'refines owner', 'residual', 'no determination', 'not-encoded-i3')


class Refusal(Exception):
    pass


def slug(heading):
    return re.sub(r'[^\w\- ]', '', heading.strip().lower().replace('`', ''), flags=re.U).replace(' ', '-')


def headings(path):
    """Return the heading slugs of one member, in order, with duplicate suffixes."""
    out, seen, code = [], {}, False
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('```'):
            code = not code
        if code:
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            s = slug(m.group(2))
            n = seen.get(s, 0)
            seen[s] = n + 1
            out.append(s if n == 0 else f'{s}-{n}')
    return out


def args(clause, role):
    return [a for a in clause['arguments'] if a['role'] == V + 'role:' + role]


def check_clause(clause, uris, residuals):
    """Return the list of pre-check failures for one clause."""
    errors = []
    u = clause['uri']
    standing = args(clause, 'standing')
    if len(standing) != 1 or standing[0].get('ref', '').removeprefix(STANDING) not in (
            'premise', 'consequence', 'policy-choice', 'observation', 'unresolved'):
        errors.append(f'{u}: not exactly one standing')
        return errors
    kind = standing[0]['ref'].removeprefix(STANDING)
    if kind == 'consequence':
        support = args(clause, 'support')
        if not support or any(a.get('ref') not in uris for a in support):
            errors.append(f'{u}: consequence without resolvable support')
    if kind == 'policy-choice':
        owner, choice, among = args(clause, 'owner'), args(clause, 'choice'), args(clause, 'among')
        if not (owner and choice and among):
            errors.append(f'{u}: hollow policy choice: owner, choice and among are all required')
        elif choice[0].get('literal', '').strip() == clause['statement'].strip():
            errors.append(f'{u}: hollow policy choice: the whole rule is filed as the choice')
    if kind == 'unresolved' and not args(clause, 'blocked-by'):
        errors.append(f'{u}: residual-dependent clause without blocked-by')
    for a in args(clause, 'blocked-by'):
        if a.get('ref') not in residuals:
            errors.append(f'{u}: blocked-by names no residual')
    if clause['operator'] == V + 'operator:maps-to':
        cores = args(clause, 'core-value')
        if len(cores) != 1 or cores[0].get('ref') not in CORE_VALUES:
            errors.append(f'{u}: refinement must map to exactly one core value')
        if not args(clause, 'predicate') or not args(clause, 'refined-value'):
            errors.append(f'{u}: refinement without its predicate or refined value')
    for a in args(clause, 'force'):
        if a.get('literal') not in ('must', 'must-not', 'should', 'should-not', 'may'):
            errors.append(f'{u}: force literal outside the five')
    support_kind = args(clause, 'support-kind')
    if len(support_kind) > 1 or any(a.get('literal') not in SUPPORT_KINDS for a in support_kind):
        errors.append(f'{u}: support-kind must be one literal among the five kinds of support')
    section = clause['source_refs'][0].rsplit('#', 1)[-1] if clause.get('source_refs') else ''
    if section in ASSURANCE_SECTIONS and len(support_kind) != 1:
        errors.append(f'{u}: a clause of the construction or assurance relations carries exactly one support-kind')
    return errors


def source_ok(ref, cache):
    if not ref.startswith(SOURCE):
        return True
    path, _, anchor = ref[len(SOURCE):].partition('#')
    f = ROOT / 'standards' / path
    if not f.exists():
        return False
    if path not in cache:
        cache[path] = set(headings(f))
    return not anchor or anchor in cache[path]


def read_dispositions(member_file):
    rows = {}
    for line in member_file.read_text(encoding='utf-8').splitlines():
        m = re.match(r'^\| `#([^`]+)` \| ([^|]+) \| ([^|]*) \| ([^|]*) \|$', line)
        if m:
            rows.setdefault(m.group(1), []).append(m.group(3).strip())
    return rows


def assemble(fragment_paths, disposition_dir):
    symbols, clauses, residuals, indexes = {}, {}, {}, {}
    for p in fragment_paths:
        f = json.loads(Path(p).read_text(encoding='utf-8'))
        for key, store in (('symbols', symbols), ('clauses', clauses), ('residuals', residuals), ('frame_indexes', indexes)):
            for item in f.get(key, []):
                if item['uri'] in store:
                    raise Refusal(f'duplicate URI {item["uri"]}')
                store[item['uri']] = item
    uris = set(symbols) | set(clauses) | set(residuals)
    errors, cache = [], {}
    for c in clauses.values():
        errors += check_clause(c, uris, residuals)
        for a in c['arguments']:
            if 'ref' in a and a['ref'] not in uris and not a['ref'].startswith((STANDING, CORE)):
                errors.append(f'{c["uri"]}: argument ref does not resolve: {a["ref"]}')
    for item in list(symbols.values()) + list(clauses.values()) + list(residuals.values()) + list(indexes.values()):
        for r in item.get('source_refs', []):
            if not source_ok(r, cache):
                errors.append(f'{item["uri"]}: source ref does not resolve to a current heading: {r}')
    for ix in indexes.values():
        for r in ix['clause_refs']:
            if r not in clauses:
                errors.append(f'{ix["uri"]}: clause ref does not resolve: {r}')
    coverage = {}
    if disposition_dir is not None:
        for d in sorted(Path(disposition_dir).glob('*.md')):
            member = d.stem + '.md'
            rows = read_dispositions(d)
            expected = headings(ROOT / 'standards' / member)
            counts = {k: 0 for k in DISPOSITIONS}
            for h in expected:
                values = rows.get(h, [])
                if len(values) != 1 or values[0] not in DISPOSITIONS:
                    errors.append(f'{member}#{h}: needs exactly one disposition, has {values}')
                    continue
                counts[values[0]] += 1
            for h in rows:
                if h not in expected:
                    errors.append(f'{member}#{h}: disposition for a heading that does not exist')
            coverage[member] = counts
    if errors:
        raise Refusal('\n'.join(errors))
    return symbols, clauses, residuals, indexes, coverage


def program(symbols, clauses, residuals, indexes):
    standing_and_core = sorted({a['ref'] for c in clauses.values() for a in c['arguments']
                                if 'ref' in a and a['ref'].startswith((STANDING, CORE))})
    extra = [{'uri': u, 'kind': V + ('kind:standing' if u.startswith(STANDING) else 'kind:core-value'),
              'label': u.rsplit(':', 1)[1], 'source_refs': [SOURCE + ('FOUNDATIONS.md#results' if u.startswith(CORE) else 'FOUNDATIONS.md#3-commitments')]}
             for u in standing_and_core if u not in symbols]
    syms = sorted(list(symbols.values()) + extra, key=lambda s: s['uri'])
    vocab = sorted({s['kind'] for s in syms} | {c['operator'] for c in clauses.values()}
                   | {a['role'] for c in clauses.values() for a in c['arguments']})
    frames = sorted({ix['frame_ref'] for ix in indexes.values()})
    canon = lambda item: dict(item, **{k: sorted(set(item[k])) for k in ('source_refs', 'clause_refs', 'residual_refs', 'subject_refs', 're_entry_refs') if k in item})
    symbols = {u: canon(x) for u, x in symbols.items()}
    clauses = {u: canon(x) for u, x in clauses.items()}
    residuals = {u: canon(x) for u, x in residuals.items()}
    indexes = {u: canon(x) for u, x in indexes.items()}
    return {
        'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
        'uri': 'urn:stdo-3:claude:i3:program', 'calculus_ref': 'stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md',
        'source_basis': SOURCE, 'frame_refs': frames, 'vocabulary_refs': vocab,
        'symbols': syms, 'clauses': sorted(clauses.values(), key=lambda c: c['uri']),
        'residuals': sorted(residuals.values(), key=lambda r: r['uri']),
        'frame_indexes': sorted(indexes.values(), key=lambda i: i['uri']),
    }


BINDINGS = {'kind': 'axiom-indexer.binding-set', 'schema_version': 1, 'bindings': [
    {'uri_prefix': SOURCE, 'path': '../../standards'},
    {'uri_prefix': 'stdo://releases/v2.5.1-rc.2/standards/',
     'path': '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards'}]}


def main(argv):
    frags = sorted((I3 / 'fragments').glob('*.json'))
    try:
        parts = assemble(frags, I3 / 'dispositions')
    except Refusal as r:
        print('refusal:\n' + str(r))
        return 2
    outputs = {
        I3 / 'axiomatic-program.json': json.dumps(program(*parts[:4]), indent=2, ensure_ascii=False) + '\n',
        I3 / 'bindings.json': json.dumps(BINDINGS, indent=2) + '\n',
        I3 / 'coverage.json': json.dumps(parts[4], indent=2, sort_keys=True) + '\n',
    }
    if '--check' in argv:
        stale = [p.name for p, t in outputs.items() if not p.exists() or p.read_text(encoding='utf-8') != t]
        print('current' if not stale else 'stale: ' + ', '.join(stale))
        return 0 if not stale else 1
    for p, t in outputs.items():
        p.write_text(t, encoding='utf-8')
    print(f'{len(parts[1])} clauses, {len(parts[2])} residuals, {len(parts[3])} frame indexes written')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
