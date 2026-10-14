"""Build the iteration 3 fragments from a declared encoding spec, quoting the source verbatim.

Each clause's statement is extracted from its owning section at the current
bytes: the sentence that begins with the spec's `find` text, or the table
row whose first cell contains the spec's `row` text. Nothing is
paraphrased. A `find` or `row` that does not occur exactly once in its
section refuses the build. The spec is the encoding decision; this tool
only quotes the source and writes the fragment JSON.

Usage, from the tenant root:
    python3 -I a_c/i3/tools/build_fragments.py
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
I3 = ROOT / 'a_c' / 'i3'
sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble as A  # noqa: E402
from spec import CONCEPTS, FRAGMENTS, RESIDUALS, INDEXES  # noqa: E402

_gf = importlib.util.spec_from_file_location('gf', ROOT / 'qualification' / 'instruments' / 'generate_frames.py')
gf = importlib.util.module_from_spec(_gf)
_gf.loader.exec_module(gf)
_members = {}

P = 'urn:stdo-3:claude:i3:'


def section(member, anchor):
    if member not in _members:
        _members[member] = gf.Member('standards/' + member, (ROOT / 'standards' / member).read_bytes())
    return _members[member].section(anchor)[2].decode('utf-8')


def flat(member, anchor):
    return re.sub(r'\s+', ' ', re.sub(r'\n\|[^\n]*', '', section(member, anchor)))


def sentence(member, anchor, find, until=None):
    text = flat(member, anchor)
    if text.count(find) != 1:
        raise SystemExit(f'refusal: {member}#{anchor}: "{find[:50]}" occurs {text.count(find)} times')
    i = text.index(find)
    if until:
        j = text.find(until, i)
        if j < 0:
            raise SystemExit(f'refusal: {member}#{anchor}: "{until[:40]}" not found after "{find[:40]}"')
        return text[i:j + len(until)].strip()
    m = re.compile(r'[.:](?=\s+[A-Z(\[`-]|\s*$)').search(text, i + len(find) - 1)
    return text[i:m.end() if m else len(text)].strip()


def row(member, anchor, first):
    pattern = first if first.startswith('|') else f'| {first} |'
    rows = [l for l in section(member, anchor).splitlines() if l.startswith('| ') and pattern in l]
    if len(rows) != 1:
        raise SystemExit(f'refusal: {member}#{anchor}: row "{first}" matches {len(rows)} rows')
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', rows[0].strip('| ').replace(' | ', ' — '))


def src(member, anchor):
    return A.SOURCE + f'{member}#{anchor}'


def arg(role, ref=None, literal=None):
    a = {'role': A.V + 'role:' + role}
    if ref is not None:
        a['ref'] = ref
    else:
        a['literal'] = literal
    return a


def build_clause(group, c):
    member, anchor = c['at']
    statement = row(member, anchor, c['row']) if 'row' in c else sentence(member, anchor, c['find'], c.get('until'))
    if 'predicate_at' in c:
        member_p, anchor_p, start = c['predicate_at']
        found = [m for m in re.findall(r'predicate "([^"]+)"', flat(member_p, anchor_p)) if m.startswith(start)]
        if len(found) != 1:
            raise SystemExit(f'refusal: {len(found)} quoted predicates starting "{start}" at {member_p}#{anchor_p}')
        c = dict(c, predicate=found[0])
    args = [arg('standing', ref=A.STANDING + c['standing'])]
    args += [arg('subject', ref=P + 'concept:' + s) for s in c.get('subjects', [])]
    for role in ('force', 'condition', 'exception', 'qualification', 'owner', 'choice', 'among', 'consumer',
                 'refined-value', 'predicate'):
        if role in c:
            args.append(arg(role, literal=c[role]))
    args += [arg('support', ref=P + 'clause:' + s) for s in c.get('support', [])]
    if 'core' in c:
        args.append(arg('core-value', ref=A.CORE + c['core']))
    args += [arg('blocked-by', ref=P + 'residual:' + r) for r in c.get('blocked_by', [])]
    op = c.get('op', 'requires')
    return {'uri': P + 'clause:' + c['id'], 'clause_type': 'relation' if op in ('uses', 'maps-to') else 'constraint',
            'operator': A.V + 'operator:' + op, 'arguments': args, 'statement': statement,
            'source_refs': [src(member, anchor)]}


def main():
    (I3 / 'fragments').mkdir(exist_ok=True)
    emitted = set()
    for group, clauses in FRAGMENTS.items():
        used = {s for c in clauses for s in c.get('subjects', [])} - emitted
        emitted |= used
        frag = {
            'group': group,
            'symbols': [{'uri': P + 'concept:' + k, 'kind': A.V + 'kind:concept', 'label': CONCEPTS[k][0],
                         'source_refs': [src(*CONCEPTS[k][1])]} for k in sorted(used)],
            'clauses': [build_clause(group, c) for c in clauses],
            'residuals': [dict(r, uri=P + 'residual:' + r['uri']) for r in RESIDUALS if r.get('group') == group],
            'frame_indexes': [dict(ix, uri=P + 'frame-index:' + ix['uri'],
                                   clause_refs=[P + 'clause:' + x for x in ix['clause_refs']])
                              for ix in INDEXES if ix.get('group') == group],
        }
        for item in frag['residuals'] + frag['frame_indexes']:
            item.pop('group', None)
        (I3 / 'fragments' / f'{group}.json').write_text(json.dumps(frag, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(group, len(frag['clauses']), 'clauses')


if __name__ == '__main__':
    main()


GROUP_MEMBERS = ['FOUNDATIONS.md', 'IDENTITY.md', 'PROFILES.md', 'ACTIVATION.md', 'CONFORMANCE.md',
                 'EVALUATION.md', 'AXIOMATIC_CALCULUS.md', 'REFERENCE_FRAME.md']


def write_dispositions():
    """One row per heading section of each G1 to G4 member; unencoded sections are `not-encoded-i3`."""
    encoded = {}
    for clauses in FRAGMENTS.values():
        for c in clauses:
            encoded.setdefault(c['at'], []).append(c['id'])
    (I3 / 'dispositions').mkdir(exist_ok=True)
    for member in GROUP_MEMBERS:
        lines = (ROOT / 'standards' / member).read_text(encoding='utf-8').splitlines()
        heads, code = [], False
        for n, line in enumerate(lines, 1):
            if line.startswith('```'):
                code = not code
            if not code and re.match(r'^#{1,6}\s', line):
                heads.append(n)
        slugs = A.headings(ROOT / 'standards' / member)
        rows = []
        for k, (n, s) in enumerate(zip(heads, slugs)):
            end = heads[k + 1] - 1 if k + 1 < len(heads) else len(lines)
            ids = encoded.get((member, s))
            title = lines[n - 1].lstrip('#').strip().lower()
            if ids:
                d, why = 'encoded-in-part', ', '.join('clause:' + i for i in ids) + '; the rest of the section is not encoded'
            elif title.endswith('source dispositions'):
                d, why = 'no determination', 'records where predecessor claims are carried; decides nothing'
            else:
                d, why = 'not-encoded-i3', 'outside the iteration 3 encoding scope (ledger variance, step 4)'
            rows.append(f'| `#{s}` | {n}-{end} | {d} | {why} |')
        text = (f'# Dispositions: {member}\n\nOne row per heading section of `standards/{member}` at the source-settlement '
                'commit. Values are those of `a_c/i3/SIGNATURE.md`. `not-encoded-i3` is uncovered.\n\n'
                '| Section | Lines | Disposition | Clauses or reason |\n|---|---|---|---|\n' + '\n'.join(rows) + '\n')
        (I3 / 'dispositions' / (member[:-3] + '.md')).write_text(text, encoding='utf-8')


if __name__ == '__main__' and '--dispositions' in sys.argv:
    write_dispositions()
