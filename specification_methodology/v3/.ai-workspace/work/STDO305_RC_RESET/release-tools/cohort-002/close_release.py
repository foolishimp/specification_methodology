"""After actual Latest confirmation, record closure outside the frozen Product subjects."""
import hashlib
import json
from pathlib import Path
R = Path.cwd(); C = Path(__file__).resolve().parent; Q = C.parent.parent
P = Q / 'public-qualification-001'
def load(p): return json.loads(p.read_bytes())
def ref(p):
    b = p.read_bytes(); return {'path': str(p.relative_to(R)), 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}
def save(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: json.dump(x, f, indent=2, sort_keys=True); f.write('\n')
    return ref(p)
latest = load(P / 'LATEST_CONFIRMED.json'); assert latest['status'] == 'confirmed_latest'
public = load(P / 'PUBLIC_GATE_PASSED.json'); assert public['status'] == 'passed'
manifest = load(R / 'stack_release.json')
assert public['carrier'] == latest['carrier']
subjects = {row['path'] for product in manifest['products'].values() for row in product['subject']['members']}
paths = ['README.md', 'specification_methodology/v3/README.md', 'specification_methodology/v3/specification/GOALS.md']
assert not subjects.intersection(paths)
preimages = {}
for name in paths:
    path = R / name; target = Q / 'closure/preimages' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as out: out.write(path.read_bytes())
    preimages[name] = ref(target)
url = 'https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology%2Fv3.0.5-rc.1'
record = {
    'kind': 'stdo.rc-reset.release-completion/1', 'status': 'released_normal_latest_publicly_verified',
    'version': '3.0.5-rc.1', 'version_line': '3.0.5', 'release_title': 'STDO 3.0.5',
    'release_id': latest['release_id'], 'release_url': url, 'carrier': latest['carrier'],
    'external_manifest': ref(R / 'stack_release.json'), 'native': manifest['native'],
    'public_readback': ref(P / 'PUBLIC_READBACK.json'), 'public_gate': ref(P / 'PUBLIC_GATE_PASSED.json'),
    'latest': ref(P / 'LATEST_CONFIRMED.json'), 'local_acceptance': ref(C / 'LOCAL_ACCEPTANCE.json'),
    'source_builder': {'version': '3.0.4', 'definition': ref(R / 'specification_methodology/v3/stdo_3.json'), 'adoption_change': False},
    'published_refs': load(C / 'manifest-reconciliation-002/RESULT.json')['selected'],
    'bookkeeping': 'The final main commit containing this record carries post-publication evidence and navigation only. The immutable release carrier, five RC tags, five selectors, archived predecessor objects, native manifest and uploaded assets remain unchanged.',
    'limits': [
        'Five peer Products and fourteen selected component claims; formal results establish the declared five structural obligations, not whole-model semantic completeness.',
        'The representation is an independently reviewed deterministic coordinate rebind with typed inverse equality and preserved semantic content; historical authoring and bounded semantic assessment retain their original subjects.',
        'Both current fixed host interfaces and Codex MCP were exercised. No new LLM/Context trial or universal instruction/host-isolation guarantee was selected for this reset.',
        'Third-party immutable dependencies used verified independent APFS cache clones; support, origin and full proofs were established anew. Acquisition is not described as network-fresh for those cache bytes.',
        'The former unadopted stable 3.0.5 line was explicitly reset. Its exact original objects, release ID, five assets and evidence are archived; old URI continuity is not promised.',
        'Private origins, compiler/runtime trees, browser profiles, duplicate full proof ZIPs and unrelated inherited artifacts remain local and excluded. No cleanup or consumer adoption occurred.'
    ]
}
result = save(Q / 'RESULT.json', record)
text = f'''# STDO 3.0.5 released

[STDO 3.0.5]({url}) is a normal GitHub release and Latest, at the immutable exact cut `v3.0.5-rc.1`. Release ID: `{latest['release_id']}`. All five Products use that cut; their `v3.0.5` tags are version-line selectors.

The immutable carrier is `{latest['carrier']}`; its external cohort manifest SHA-256 is `{record['external_manifest']['sha256']}`. The final main bookkeeping commit adds this return and the actual post-publication receipts. It does not move those release cuts or replace uploaded bytes.

Fresh anonymous acquisition verified all five assets before executing the documented offline manager recipe. The fresh public installation verified 174 native files and materialized 243 exact tool sources. Both installed host interfaces, initialized Codex MCP, current Graphify, fresh Lean support and full proof, owner inspection, documentation checks and independent offline viewer/proof navigation passed. The final public gate passed before the same release ID was made Latest and anonymously read back.

Use the [published installation guide](https://github.com/foolishimp/specification_methodology/blob/{latest['carrier']}/specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md#new-project). Its exact cut is `v3.0.5-rc.1`; the Python manager distribution spells the version `3.0.5rc1`. Installation does not adopt a basis for an existing Product. This source project's builder remains 3.0.4.

The five formal obligations are structural checks, not semantic completeness. The representation preserves its reviewed content through a deterministic coordinate rebind; original authoring and semantic-review limits remain. Current fixed interfaces were tested; historical LLM/Context trials are not relabelled as new RC executions. Third-party dependencies used verified independent cache clones with fresh support/proof establishment.

The owner-authorized reset preserves the former stable 3.0.5 objects and assets under archival references and an explicitly superseded release. All other releases remain unchanged. Original failed attempts and operator reconciliations are retained. Private origins, compiler/runtime trees, browser profiles, duplicate proof ZIPs and unrelated inherited artifacts are preserved locally and excluded from the bookkeeping commit.

Exact closure and receipt links are in [RESULT.json](RESULT.json).
'''
with (Q / 'RELEASED.md').open('x') as f: f.write(text)
root = (R / 'README.md').read_text()
start = root.index('## STDO 3.0.3 release'); end = root.index('This repository co-locates six peer source projects:')
replacement = f'''## STDO 3.0.5 release

**STDO 3.0.5 is published as a normal release and GitHub Latest.**
[Download the exact RC1 release]({url}), immutable tag
`specification_methodology/v3.0.5-rc.1`. All five peer Products share that exact
cut; their `v3.0.5` tags select the current cut on this public version line.

The [installation guide](specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md#new-project)
verifies the five public assets before bootstrapping the exact manager and
native payload. Fresh public installation, current tool/host interfaces,
Graphify, Lean structural proof, documentation and offline navigation passed.
The [release record](specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET/RELEASED.md)
binds actual publication, public qualification and its limits.

The former unadopted stable 3.0.5 cut is explicitly archived with its original
objects and assets preserved. Other releases remain unchanged. This release
does not adopt itself for a consumer: the v3 source project's builder remains
the exact selected 3.0.4 basis.

'''
root = root[:start] + replacement + root[end:]
historical_cohort = '''The independent [`a_c/`](a_c/) source project realizes the selected published
axiomatic calculus through its own build tenants. Its Graphify tenant does not
depend on v3, Axiom Indexer or STDO Representation and is outside the existing
release-matched cohort. This adds no dependency or member to those Products.'''
assert historical_cohort in root
root = root.replace(historical_cohort, '''The independent [`a_c/`](a_c/) source project realizes its selected axiomatic
calculus through its own build tenants. The current five-Product RC cohort
includes its exact selected Graphify and Lean components and records their
release dependencies. That release selection does not change the source
project's independently owned definition or construction basis.''', 1)
root = root.replace('It has a separate lifecycle from the release-matched cohort; its\n[local bootstrap]', 'Its construction lifecycle remains independent while the current RC cohort\nselects its exact host packages; its [local bootstrap]', 1)
(R / 'README.md').write_text(root)
p = R / 'specification_methodology/v3/README.md'; source = p.read_text()
source = source.replace('**STDO 3.0.4 is published as a normal standalone release and GitHub Latest.**', '**STDO 3.0.4 remains a published normal standalone release and the selected source-project builder.**', 1)
marker = '**STDO 3.0.4 remains'
position = source.index(marker)
current = f'''**STDO 3.0.5 is published as a normal release and GitHub Latest**, using
the immutable [3.0.5-rc.1 cut]({url}) and five corresponding Product selectors.
The [current release record](.ai-workspace/work/STDO305_RC_RESET/RELEASED.md)
binds all five assets, fresh public installation and the declared current
component checks. The former stable 3.0.5 line is archived under the owner's
explicit reset; its evidence remains preserved. This publication changes no
consumer basis, and the builder selection above remains 3.0.4.

'''
p.write_text(source[:position] + current + source[position:])
p = R / 'specification_methodology/v3/specification/GOALS.md'; source = p.read_text()
old = 'Release tooling is updated first. The complete source-current candidate is\nthen built, qualified, independently reviewed and published with fresh public\ninstallation. This is selected work, not a statement that those gates pass.'
assert old in source
source = source.replace(old, 'The selected cohort is now released as normal GitHub Latest at the exact\n`v3.0.5-rc.1` cut. [The release record](../.ai-workspace/work/STDO305_RC_RESET/RELEASED.md)\nbinds the completed local/public qualification, checked atomic publication,\nactual Latest readback and retained limits.', 1)
source = source.replace('**STDO 3.0.4 is published as a normal standalone release and GitHub Latest.**', '**STDO 3.0.4 remains a published normal standalone release and the selected builder.**', 1)
p.write_text(source)
save(Q / 'closure/NAVIGATION.json', {'before': preimages, 'after': {name: ref(R / name) for name in paths}, 'basis': 'Owner-selected current publication/navigation update outside all 429 frozen Product members and the 68 normative/native-contract members; builder/adoption unchanged.'})
print(json.dumps({'result': result, 'return': ref(Q / 'RELEASED.md')}))
