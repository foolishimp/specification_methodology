from pathlib import Path
import hashlib,json
BASE=Path('/Users/jim/src/apps/specification_methodology/a_c')
APP=BASE/'applications/stdo-v3-common-35fb4824'
H=BASE/'.ai-workspace/qualification/t010/handoff/packaging-r1-001'
REPAIR=BASE/'.ai-workspace/qualification/t010/packaging/repair-002'
REVIEW=BASE/'.ai-workspace/qualification/t010/package-review/packaging-r1-001'
SOURCE=Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021')
REVIEW_SOURCE=Path('/Users/jim/tmp/a_c-common-rc1-packaging-review-20261021')
ID='a_c-stdo-v3-common-35fb4824-packaging-r1'

def identity(path):
 raw=path.read_bytes();return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def save(path,value):path.write_text(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
def create(source,target):
 assert not target.exists() and not target.is_symlink(),str(target)
 target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(source.read_bytes())
 assert identity(source)==identity(target),str(target)
 return {'source':str(source),'destination':str(target),**identity(target)}

manifest=json.loads((H/'selected-promotion-manifest.json').read_text())
assert not REPAIR.exists() and not REVIEW.exists()
assert identity(REVIEW_SOURCE/'preparation/CLOSED.json')['sha256']=='cc8dbb8adf78599a1e36306eb136aee2042a8cff3ff93237cde688e5bba4b11e'
applied=[]
for row in manifest['entries']:
 source=Path(row['source']);target=Path(row['destination'])
 assert identity(source)=={k:row[k] for k in ['bytes','sha256']},str(source)
 if target==REPAIR/'README.md':
  continue
 if row['operation']=='replace_exact_preimage':
  assert identity(target)==row['precondition']['existing'],str(target)
  target.write_bytes(source.read_bytes());record={'source':str(source),'destination':str(target),**identity(target),'operation':'replaced_exact_preimage','preimage':row['precondition']}
 else:
  record={**create(source,target),'operation':row['operation']}
 applied.append(record)
# Preserve the detached historical notes verbatim, and apply the explicit current-README override.
applied.append({**create(SOURCE/'proof/PROMOTION-NOTES.md',REPAIR/'proof/PROMOTION-NOTES.md'),'operation':'create_historical_notes_verbatim_override'})
applied.append({**create(SOURCE/'proof/PROMOTION-MANIFEST.json',REPAIR/'PROMOTION-MANIFEST.json'),'operation':'copy_detached_selected_manifest_exact'})
copy_vector=[]
for row in json.loads((H/'selected-review-copy-vector.json').read_text()):
 source=Path(row['origin']);target=REVIEW/row['relative_path'];assert identity(source)=={k:row[k] for k in ['bytes','sha256']}
 copy_vector.append(create(source,target))
save(H/'review-copy-vector.json',copy_vector)

repair_readme='''# Current common packaging-r1 repair and promotion

The Executive selected the three supported packaging HOW repairs and reviewed
`a_c-stdo-v3-common-35fb4824-packaging-r1` as current local preparation. The two
live code replacements and exact reviewed artifact are materialized; the
original representation bundle/archive and review baseline are preserved.
This is a packaging revision, without semantic acceptance, Product RC/release,
publication, adoption or installation.

The repairs reject overlapping archive/checksum outputs before effects, accept
only the exact authenticated original or portable source-readiness record, and
check both release-index source identities against the checked bindings.
All 19 focused author controls and all 48
[nonauthor focused assessment controls](../../package-review/packaging-r1-001/assessment-001/REVIEW.md)
passed. The extracted README recipe rebuilt solely from bundled inputs plus
explicit pinned Graphify/Python-networkx dependencies; all rebuilt file and
archive bytes were identical. The
[assessment closure](../../package-review/packaging-r1-001/assessment-001/CLOSED.json)
binds that result.

The [application README](../../../../../applications/stdo-v3-common-35fb4824/README.md)
links the current views and archive. The
[promotion handoff](../../handoff/packaging-r1-001/) records Root's decision,
preimages, selected/applied manifests, exact copy and preservation checks.
The [isolated repair closure](proof/CLOSED.json) remains exact historical
construction evidence. [Original promotion notes](proof/PROMOTION-NOTES.md)
are preserved verbatim as historical proof; their earlier proposal language is
superseded by the separately recorded promotion disposition here.

Tests and scripts under this evidence tree retain their original isolated
execution context. They are historical executed source, not a relocated generic
application test suite. Review copies likewise preserve original bodies and
absolute execution coordinates. No fixtures, rebuilt/extracted copies, cache,
private native run or hidden reasoning were copied.

Source/model/public receipts/static display payloads are unchanged. The builder
remains STDO 2.5.1-rc.2 and represented common remains checkpoint35fb4824,
`not_ready`. Semantic/calculus/global-governing/actual-use/benefit and required
provider-family qualification remain open; interactive UI remains unverified.
'''
assert not (REPAIR/'README.md').exists();(REPAIR/'README.md').write_text(repair_readme)
applied.append({'destination':str(REPAIR/'README.md'),'operation':'authored_current_factual_readme_override',**identity(REPAIR/'README.md'),'selected_source_notes_preserved_verbatim_as':str(REPAIR/'proof/PROMOTION-NOTES.md')})

readme='''# Common V3 representation

Current local preparation is the reviewed **packaging-r1** artifact built from
common checkpoint `35fb4824a064a84df5af214a0d0e2da597c18ac6`, package tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`. Construction and selected release
preparation are complete. The artifact remains an uncommitted, unpublished
proposal, without a Product version, RC, tag, adoption or installation.

Start with the [bundle index](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/index.html),
[Graphify map](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/graph.html),
[record browser](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/records.html) or
[portable guide and rebuild recipe](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/README.md).
The representation retains all 81 source files, 58 semantic inputs, 845 sections,
1,987 records and 2,491 physical grounding occurrences. Five record families
are populated; traversals, transformations and judgments are explicitly empty.

All 1,987 records are displayed, with zero omitted or aggregated records.
[Display scope](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/view-scope.json)
accounts for 2,218 reference pairs, 2,225 local reference occurrences and 14,273
external coordinate occurrences omitted from display plumbing. Family colours
and connectivity establish no semantic communities or governing closure. Full
content remains in the reversible carriers and
[processing coverage](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/coverage.json).

## Portable use

Download the [current archive](dist/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz)
and [external checksum](dist/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256).
It contains 213 files, 110,473,751 bytes unpacked and 10,089,542 bytes compressed.
Archive SHA256:

`989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b`

Python 3 standard library is sufficient for checking and inspection:

```sh
tar -xzf a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz
cd a_c-stdo-v3-common-35fb4824-packaging-r1
python3 -B -S release_tools/bundle_check.py .
python3 -B -S codec/ac_graph.py find carrier.json admission
AC_RECORD='urn:a-c:generation:0657852b6fd1fa48457c3f7d:record:5fec0f21265016ca449d4389511dce49'
python3 -B -S codec/ac_graph.py inspect carrier.json "$AC_RECORD"
python3 -B -S codec/ac_graph.py project carrier.json --seed "$AC_RECORD" --out /tmp/common-selected-projection.json
python3 -B -S release_tools/source_reentry.py standards/ACTIVATION.md --start 1 --end 30
```

Use fresh output filenames outside the bundle. For an ordinary local visual
preview, run `python3 -B -S release_tools/serve_preview.py .` and open the printed
loopback URL; Ctrl-C stops it. No CDN or model service is needed. Interactive
browser behavior remains **unverified**; this delivery used static checks and
CLI replay. The guide's rebuild recipe additionally requires the explicit pinned
Graphify checkout and existing Python/networkx environment.

## Evidence and standing

Three supported packaging defects are fixed: overlapping archive output,
rebuilding from authenticated portable source readiness, and duplicate release
source identities. All 19 focused author checks and
[48 focused nonauthor checks](../../.ai-workspace/qualification/t010/package-review/packaging-r1-001/assessment-001/REVIEW.md)
passed. The documented extracted-input rebuild produced byte-identical bundles
and archives. [Repair/promotion record](../../.ai-workspace/qualification/t010/packaging/repair-002/README.md)
and [handoff](../../.ai-workspace/qualification/t010/handoff/packaging-r1-001/)
retain exact subjects and preimages.

The correct [original representation archive](dist/a_c-stdo-v3-common-35fb4824.tar.gz)
and [bundle](bundle/a_c-stdo-v3-common-35fb4824/README.md) are preserved. Its
[72-control review](../../.ai-workspace/qualification/t010/package-review/final-003/REVIEW.md)
applies to that original bounded baseline; it does not qualify the new code.
The unchanged [source-first nonauthor semantic review](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/evidence/reviews/review-001/REVIEW.md)
found no actionable defect in 44 fixed cases, four logical acquisition tasks
and 11 interventions. A3 concrete invariant reconstruction was not performed.

See [BUILD](BUILD.md), [frozen source readiness](SOURCE-READINESS.md) and
[release preparation](RELEASE-PREPARATION.md). Frozen common remains `not_ready`,
owner acceptance is absent and covering source review unassigned. This model
review replaces none of those gates. Semantic acceptance, fresh actor use,
required provider-family independence, global governing acquisition,
whole-calculus conformance, efficiency/benefit and Product/RC/installed
qualification remain unqualified. The a_c builder remains STDO 2.5.1-rc.2.

The [separate private STDO 3.0.0 RC1 trial](/Users/jim/tmp/STDOv3-3.0.0-rc.1-test-20261020/README.md)
used three nonsemantic packaging deltas in its own pipeline. Its RC1 identity is
separate from this packaging-r1 identifier; it neither rebases the a_c model or
source custody nor adds a dependency.

Public receipts exclude raw private invocations, events, configuration and
hidden reasoning and do not supply complete private actor replay. Existing
licenses retain their scope; distribution terms for a_c-owned/new material
remain an owner choice, without a new license or automatic publication gate.
'''
prep='''# Common representation release preparation

Current local preparation is the reviewed `a_c-stdo-v3-common-35fb4824-packaging-r1`
artifact. The Executive adopted three supported packaging HOW repairs and
materialized the exact reviewed code/artifact after consuming the independent
focused assessment. The [application README](README.md) provides entrypoints.
This remains a local, uncommitted, unpublished proposal, without semantic
acceptance, Product version/RC/tag, installation or adoption.

## Current subject and artifact

Represented common checkpoint:
`35fb4824a064a84df5af214a0d0e2da597c18ac6`; package tree:
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`. Canonical model SHA256:
`691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf`.
The builder remains exact STDO 2.5.1-rc.2. [BUILD](BUILD.md) and
[SOURCE-READINESS](SOURCE-READINESS.md) preserve authoring and source-stage facts.

The [current bundle](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/README.md)
has 213 files and 110,473,751 bytes. The
[archive](dist/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz) has 10,089,542 bytes,
SHA256 `989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b`;
[external checksum](dist/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256)
file SHA256 is `39c3d997f3a75f38b9599cf970ba962df76a3d42ee0beb8825e7e4527a9bcb76`.
Complete 213-file vector SHA256 is
`22def4fbec18e4ec543d01ddf2ae71a59fc1cf5e2d20c3601b09ede4f84df6fd`.
[Inventory](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/inventory.json),
[checksums](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/SHA256SUMS) and
[RELEASE.json](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/RELEASE.json)
retain the exact scope. All 1,987 records remain displayed, none omitted or
aggregated; [display scope](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/view-scope.json)
separates reference projection from the full carriers.

The five raw model/carrier/export/coverage/result files, 81 source members,
three manifests and original authentic construction/semantic-review receipts
remain unchanged. Public construction receipt SHA256 remains
`1f19d4ab142bd857694e4ab2a10f978bb290d99cbf68dd028f50f37a1268373c`;
bounded semantic-review receipt SHA256 remains
`542c2330eca15ff9a3804e186b7d31b83ef3ae62f5d7dfdc2073f793a1d3dbdd`.
The [receipt contract](release_tools/PUBLIC-RECEIPTS.md) checks source/section,
model/raw-artifact and readable-report bindings. It proves neither issuer
legitimacy nor semantic truth. Private native events/invocations/configuration
and hidden reasoning remain excluded; public receipts do not provide complete
private actor replay.

## Supported repairs and consumed assessment

Archive/checksum paths are resolved and checked for overlap before output
effects, including direct archive calls; valid sibling and safe parent-dist
layouts remain supported. Source readiness accepts only the exact sealed
original or authenticated portable projection and remains idempotent. Duplicate
release `source_commit` and `package_tree` fields must match checked source
bindings, including when an outer inventory has been regenerated.

All 19 focused author controls and all 48
[focused nonauthor assessment controls](../../.ai-workspace/qualification/t010/package-review/packaging-r1-001/assessment-001/REVIEW.md)
passed within PKG-R01–R04, with no actionable defect. Its
[closure](../../.ai-workspace/qualification/t010/package-review/packaging-r1-001/assessment-001/CLOSED.json)
binds the exact code and artifact. The actual command parsed from the extracted
README rebuilt using only bundled inputs plus explicit pinned Graphify and
existing Python/networkx dependencies; every rebuilt file and archive byte was
identical. [Repair/promotion record](../../.ai-workspace/qualification/t010/packaging/repair-002/README.md)
and [promotion handoff](../../.ai-workspace/qualification/t010/handoff/packaging-r1-001/)
retain preimages, selected/applied manifests and preservation evidence.
Historical tests/scripts retain their isolated execution context; they are not
an installed generic application test suite. Provider-family independence is
not certified by this focused nonauthor assessment.

Current `package_release.py` SHA256:
`324fe8242ecb4f67c6f6ed77c6ff3f674245f53c73f17ba1029f0e9f03b28ccb`.
Current receipt helper SHA256:
`ab91aae1bd08d64c167833095735735235919e0dd32a040b39d95c60291cf3b3`.
Portable checker remains
`74beb6365104bc4352b691725c9e18fe3521d01fe50a080c0c9cc735a4a141f5`;
exact codec remains
`2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667`.
Graphify stays pinned at `fe085cedddde3a18554f8749b230bfe47f3dcce7`, with exact
SRI-pinned vis-network 9.1.6 and scoped source/license custody retained under
[release_tools](release_tools/). No rebuild/export/reauthoring occurred during
promotion.

## Preserved baseline and limits

The correct [original representation archive](dist/a_c-stdo-v3-common-35fb4824.tar.gz)
(10,087,425 bytes, SHA256
`2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386`)
and its [bundle](bundle/a_c-stdo-v3-common-35fb4824/README.md) remain unchanged.
Its [72-control actual archive review](../../.ai-workspace/qualification/t010/package-review/final-003/REVIEW.md)
and [packaging closure](../../.ai-workspace/qualification/t010/packaging/final-001/CLOSED.json)
apply to that original bounded baseline, not qualification of the repaired code.
Earlier [receipt-binding repair](../../.ai-workspace/qualification/t010/packaging/repair-001/CLOSED-REPAIR.json)
and [portable-document repair](../../.ai-workspace/qualification/t010/packaging/documentation-repair-001/CLOSED.json)
remain historical preparation evidence.

The unchanged [source-first nonauthor semantic review](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/evidence/reviews/review-001/REVIEW.md)
found no actionable defect in 44 fixed preservation cases, four logical
acquisition tasks and 11 grounding interventions. A3 concrete invariant
reconstruction was not performed. Frozen common remains `not_ready`, owner
acceptance `not_given`, covering independent source review `unassigned`, and
actual use on repaired source unperformed. Representation semantic acceptance,
fresh actor use, required provider-family independence, global governing
acquisition, whole-calculus conformance, measured benefit and Product/RC/installed
qualification remain open. Connectivity supplies no governing closure or truth.
Interactive UI remains unverified; static conservation/CLI replay supplies no
interactive qualification. No browser/server workaround was used.

The [separate private STDO 3.0.0 RC1 trial](/Users/jim/tmp/STDOv3-3.0.0-rc.1-test-20261020/README.md)
has its own native pipeline and three nonsemantic packaging deltas. It does not
rebase this a_c model/source custody, replace the selected builder or add a
dependency. Packaging-r1 is this representation's packaging identifier.

Existing licenses retain their scope. No license was assigned here to
a_c-owned/new material; distribution terms remain an owner choice without an
invented automatic publication gate. Owner acceptance, publication and adoption
remain reserved. No Git effects or ticket move are part of this promotion.
'''
ticket='''# T-010: Common V3 representation and release preparation

Status: selected local construction and reviewed packaging-r1 preparation
complete and materialized. No ticket move selected; this record remains in
`active/`. Owner: Jim. Coordinating Executive: `/root`.
Change class: `realization_refactor`, an application of existing a_c HOW.

## Selected outcome and basis

Jim instructed: “we have a final spec method build tenant i think under common,
i want you to build the representation for that and pepare it for release”.
The selected scope is the separate representation artifact. Clarification was
optional and unanswered; the Executive proceeded under that scope. No STDO/a_c
Product publication or adoption was selected.

Represented common checkpoint:
`35fb4824a064a84df5af214a0d0e2da597c18ac6`, payload commit
`7d0516f37716298f038548c4152a1a697ce70f95`, package
`specification_methodology/v3/build_tenants/common`, tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`.
The [application README](../../../applications/stdo-v3-common-35fb4824/README.md)
provides current views, archive, portable commands and evidence.

The builder remains `stdo://releases/v2.5.1-rc.2/`, installed manifest SHA256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`
and calculus SHA256
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
The [a_c Product Definition](../../../stdo_a_c.json), requirements, tenant design
and composition remain unchanged. Common is the represented subject.

## Completed conditions and packaging repair

All 81 source files remain frozen: 58 semantic, 13 derived frame and ten
host/legal/release metadata members, with 223 inherited frame-owner bindings.
[SOURCE-READINESS](../../../applications/stdo-v3-common-35fb4824/SOURCE-READINESS.md)
retains exact source decisions; [BUILD](../../../applications/stdo-v3-common-35fb4824/BUILD.md)
records F_P construction over 845 sections/18 chunks. The unchanged proposal
has 1,987 records and 2,491 physical grounding occurrences, exact native/upstream
carrier recovery and original authentic public construction/review receipts.

Source-first nonauthor bounded semantic assessment found no actionable defect
in 44 fixed cases, four logical acquisition tasks and 11 interventions. A3
concrete invariant reconstruction was not performed. All records remain displayed.

Three supported packaging HOW defects were reproduced and repaired: archive
output overlap, reuse of authenticated portable source readiness, and duplicate
release source identities. All 19 focused author checks and all 48
[focused nonauthor checks](../../qualification/t010/package-review/packaging-r1-001/assessment-001/REVIEW.md)
passed. The documented extracted-input build using bundled inputs plus explicit
pinned dependencies produced a byte-identical second bundle/archive. The
[assessment closure](../../qualification/t010/package-review/packaging-r1-001/assessment-001/CLOSED.json)
was consumed before Root selected the repaired code/artifact as current local
preparation. [Repair/promotion record](../../qualification/t010/packaging/repair-002/README.md)
and [handoff](../../qualification/t010/handoff/packaging-r1-001/) bind the applied
paths, preimages, reviews and preservation results. Historical tests are retained
as executed isolated-context evidence, not an installed generic test suite.

Current artifact identifier is `a_c-stdo-v3-common-35fb4824-packaging-r1`:
213 files, 110,473,751 bytes unpacked, 10,089,542 bytes compressed, archive SHA256
`989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b`.
The correct original representation archive/bundle are preserved. The earlier
[72-control review](../../qualification/t010/package-review/final-003/REVIEW.md)
applies to that original bounded baseline, not the new code's qualification.

The [separate private STDO 3.0.0 RC1 trial](/Users/jim/tmp/STDOv3-3.0.0-rc.1-test-20261020/README.md)
uses its own native pipeline with three nonsemantic packaging deltas. Its RC1
identity is separate from packaging-r1 and does not rebase a_c model/source
custody or add a dependency.

## Reserved decisions

Frozen common remains `freeze_readiness: not_ready`, owner acceptance `not_given`,
covering independent source review `unassigned`, and actual use on repaired
source unperformed. The model review replaces no source acceptance or covering
review. Representation semantic admission/acceptance, fresh actor use, required
provider-family independence, global governing acquisition, whole-calculus
conformance, efficiency/benefit and Product/RC/installed qualification remain
unqualified. Interactive UI behavior remains unverified.

The local artifact is uncommitted and unpublished, with no Product semver,
RC/tag, installation or adoption. Private invocations/events/configuration and
hidden reasoning remain excluded; public receipts are not complete private
actor replay. Existing licenses retain their scope, with distribution terms
for a_c-owned/new material an owner choice. Owner acceptance and publication
remain reserved outside this completed bounded delivery. No Git effects occurred.
'''
for rel,body in [('applications/stdo-v3-common-35fb4824/README.md',readme),('applications/stdo-v3-common-35fb4824/RELEASE-PREPARATION.md',prep),('.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md',ticket)]:
 target=BASE/rel;pre=H/'preimages'/rel;assert target.read_bytes()==pre.read_bytes(),str(target)
 target.write_text(body);applied.append({'destination':str(target),'operation':'update_exact_granted_document','preimage':identity(pre),**identity(target)})
record={'profile':'ac.common.applied-packaging-promotion-manifest/1','status':'materialized_pending_final_checks','selected_manifest':identity(H/'selected-promotion-manifest.json'),'root_decision':str(H/'activation-and-root-decision.json'),'entries':applied,'review_copy_vector':str(H/'review-copy-vector.json'),'documentation_override':{'selected_source':str(SOURCE/'proof/PROMOTION-NOTES.md'),'preserved_verbatim':str(REPAIR/'proof/PROMOTION-NOTES.md'),'authored_current_readme':str(REPAIR/'README.md'),'reason':'Root documentation-only override; historical proposed wording is preserved, current status is factual; original archive is the original representation archive'},'no_export_rebuild_reauthoring':True,'no_git_effects':True}
save(H/'applied-promotion-manifest.json',record)
native=Path('/Users/jim/tmp/STDOv3-3.0.0-rc.1-test-20261020/README.md');assert identity(native)['sha256']=='415dca07bf2fa1350c61f398782179409ca33cb3afa1786318822093de66bb5d'
save(H/'consumed-native-handoff.json',{'readme':{'path':str(native),**identity(native)},'root_consumed_handoff_closed_sha256':'1059a4c38dcb28a6e6f801434fa1fa83b689c0e3b01f71be706c185316277d97','scope':'Separate private native STDO3.0.0 RC1 trial; no rebase/dependency of this representation; no native root effects by this Writer'})
print(json.dumps({'applied_manifest':str(H/'applied-promotion-manifest.json'),'materialized_entries':len(applied),'review_copies':len(copy_vector),'documents':[{ 'path':str(BASE/rel),**identity(BASE/rel)} for rel in ['applications/stdo-v3-common-35fb4824/README.md','applications/stdo-v3-common-35fb4824/RELEASE-PREPARATION.md','.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md']]},indent=2))
