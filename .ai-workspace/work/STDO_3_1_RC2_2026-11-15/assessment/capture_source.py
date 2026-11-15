from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
BASE = Path(__file__).resolve().parent
OUT = BASE / 'source-first-01'
INSTALLED = Path('/Users/jim/Library/Application Support/STDO/releases/v3.0.4')
PREVIOUS = 'f68e8f47db69425205db313ba72fbc9cad94c2b9'
NATIVE = 'c1e0faaa8437c169031a476343c764614135cd93'

def sha(value):
    return hashlib.sha256(value).hexdigest()

def git_member(commit, member):
    return subprocess.check_output(['git', '-C', str(ROOT), 'show', commit + ':' + member])

def main():
    OUT.mkdir(parents=True, exist_ok=False)
    manifest = (INSTALLED / 'manifest.json').read_bytes()
    assert sha(manifest) == '102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b'
    entries, chunks = [], []

    def add(label, raw, origin, ranges=None):
        lines = raw.decode().splitlines(keepends=True)
        if ranges is None:
            ranges = [(1, len(lines))]
        for a, b in ranges:
            assert 1 <= a <= b <= len(lines), (label, a, b, len(lines))
        body = ''.join('\n[Original lines %s-%s]\n' % (a, b) + ''.join(lines[a-1:b]) for a, b in ranges)
        item = {'label': label, 'origin': origin, 'source_sha256': sha(raw),
                'source_bytes': len(raw), 'selected_lines': ranges,
                'selected_body_sha256': sha(body.encode()), 'selected_body_bytes': len(body.encode())}
        entries.append(item)
        chunks.append('\n\n===== VERBATIM SOURCE: ' + label + ' =====\n' +
                      'Source SHA-256: ' + item['source_sha256'] + '\n' + body +
                      '\n===== END SOURCE =====\n')

    activation = BASE.parent / 'ACTIVATION.md'
    add('admitted RC2 activation', activation.read_bytes(), str(activation))
    for member in ['AGENTS.md', 'purpose_context/AGENTS.md', 'purpose_context/stdo_purpose_context.json',
                   'purpose_context/specification/INTENT.md', 'purpose_context/specification/PRODUCT.md',
                   'purpose_context/specification/GOALS.md', 'purpose_context/specification/REFERENCE_FRAME_BASIS.md',
                   'purpose_context/specification/requirements/README.md',
                   'purpose_context/specification/requirements/SDLC-WORKFLOW.md',
                   'releases/3.1.0-rc.1/RELEASE.md']:
        add('immutable predecessor source/' + member, git_member(PREVIOUS, member), PREVIOUS + ':' + member)

    for member, ranges in {
        'standards/RELEASE.md': None,
        'standards/EVALUATION.md': None,
        'standards/FOUNDATIONS.md': [(732, 1057), (1378, 1462)],
        'standards/ACTIVATION.md': [(1627, 1769)],
        'plugins/spec/skills/stdo-review/SKILL.md': None,
        'plugins/spec/references/PRODUCT_BASIS.md': None,
    }.items():
        path = INSTALLED / member
        add('installed construction basis/' + member, path.read_bytes(), str(path), ranges)

    comparison = []
    for name in ['RELEASE.md', 'EVALUATION.md', 'FOUNDATIONS.md', 'ACTIVATION.md']:
        installed = (INSTALLED / 'standards' / name).read_bytes()
        native = git_member(NATIVE, 'specification_methodology/v3/standards/' + name)
        comparison.append({'member': name, 'installed_3_0_4_sha256': sha(installed),
                           'native_rc1_sha256': sha(native), 'whole_member_equal': installed == native})
        if installed != native:
            add('immutable native RC1 semantic owner/' + name, native,
                NATIVE + ':specification_methodology/v3/standards/' + name)

    products = []
    for rel in ['purpose_context/stdo_purpose_context.json', 'stdo_skills/stdo_skills.json',
                'specification_methodology/v3/stdo_3.json']:
        status = json.loads(subprocess.check_output(['/Users/jim/.local/bin/stdo', 'status', '--definition', str(ROOT / rel), '--verify']))
        assert status['valid'] and status['installed'] and not status['failures']
        assert status['manifest_sha256'] == sha(manifest)
        products.append({key: status[key] for key in ['definition_id', 'basis', 'manifest_sha256', 'valid', 'installed', 'failures']})

    intake = '''# Source-first expectations for the bounded STDO 3.1 RC2 corrective release

This is expectation derivation BEFORE candidate exposure, not a candidate verdict. Read the governing sources below and return your own finite obligations and falsifiers. No RC2 implementation, authored rule/index, selected context, test output or author verdict is in this packet.

Scope: the owner's exact instruction authorizes repairing a reported missing successor-conservation obligation at Product acceptance and cutting 3.1.0-rc.2 under the existing six-Product cohort method. The activation names the reported counterexample as an input; it does not prescribe your interpretation. The current RC2 governing requirements are the existing source requirements plus this bounded repair/release instruction. Immutable RC1 source Product documents are supplied to fix the unchanged Product contract; their RC1 labels and historical results do not become RC2 results. The current constructor remains installed 3.0.4. Native RC1 source law is separately compared below because it is the index's semantic predecessor.

Actor relation: you are an actual fresh Claude-family CLI activation; the operator and Writers are Codex-family. Native CLI metadata is authoritative for model/session identity. You authored neither candidate nor supplied governing source. The operator will retain stdout as your original report. You must not repair a candidate, change scope, authorize publication or invent semantic support. Tools are requested disabled; report actual exposure or use if any. The supplied text is the complete declared source packet, not an assertion of enforced clean-room or whole-host context fit. Hidden host/system context is unmeasured. If a deciding source is missing, name its exact owning relation and explain which predicate is unresolved.

Required return:
1. A compact source-derived expectation matrix for successor Product acceptance, qualification, release, ordinary work/non-boundary and unknown/ill-typed facts. Include dependencies and no inadvertent transfer of release-only conditions into another boundary.
2. The semantic obligations carried at successor acceptance, with source citations, missing-trigger/exception/premise behavior and finite counterexamples.
3. A proportionate before/after, independent-assessment, installed-host, predecessor-conservation and release-identity verification matrix. Distinguish structural content verification, semantic coverage, actor behavior and exact-cut acceptance.
4. Rules for reusing RC1 evidence and observations without relabelling old exact-query judgments. Identify the candidate bytes, queries and evidence you will need to assess later. Do not demand unrelated new capabilities or an unbounded whole-method proof.
5. Explicit limits, ambiguity and unperformed work. There is no selected numeric severity scale; use source-grounded materiality and affected predicate, not an invented numeric grade.

Source-first expectations are fixed inputs to later independent candidate assessment, never its answer. Deliver only your expectation report, not a candidate result.

Verified construction selections (operator-computed):
'''
    packet = intake + json.dumps(products, indent=2) + '\n\nImmutable owner comparison (operator-computed):\n' + json.dumps(comparison, indent=2) + ''.join(chunks)
    (OUT / 'PACKET.md').write_text(packet)
    record = {'captured_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'packet_sha256': sha(packet.encode()), 'packet_bytes': len(packet.encode()),
              'sources': entries, 'owner_comparison': comparison, 'verified_products': products,
              'candidate_exposure': 'none; no RC2 candidate implementation, index, context, test or verdict'}
    (OUT / 'SOURCE_MANIFEST.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({key: record[key] for key in ['packet_sha256', 'packet_bytes', 'candidate_exposure']}))

if __name__ == '__main__':
    main()
