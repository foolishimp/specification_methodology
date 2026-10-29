# Reusable formal gate interface

The public entry is `scripts/formal_gate.py verify --request REQUEST.json --output NEW_DIR`.
Python integration calls `verify(request, output_dir, limits=None)`. Request shape is
fixed by `profiles/formal-gate-request.schema.json`. Empty selections with null supplied_views request model-only verification and make no projection claim. Paths are resolved by the
caller; CLI relative paths are relative to the request file. Source bytes are
retained, with exact raw digests required. Supplied views are the ordered JSON
list returned by `ac_graph.project_many`, with no rewritten fields. Context binding
is supplied exact metadata; the caller remains responsible for proving it names
the actual bytes delivered. Integration must compare that binding at use.

Result `schema` is `a_c.formal-gate.result/1`. Status is `verified`, `refused`,
`unsupported`, or `incomplete` (CLI exits 0, 2, 3, 4). A result carries exact input,
selection, code/profile/proof/toolchain pins, retained artifact hashes, checked
claims, stage timings and explicit limits. Budget excess or a supported invalid
model/projection refuses. Unknown signature/profile is unsupported. Runtime,
compiler or resource failures are incomplete, never verified. The result JSON
is evidence, not an authentication root: `check-evidence --bundle DIR --output
NEW_DIR` rebuilds the exact request from retained source and executes the trusted
selected verifier again. It can reuse an exact locally established cold proof
under the origin contract below; a saved `status` field never establishes that origin.

The output directory must be fresh and cannot overlap an input path or old bundle.
The verifier never receives code, executable arguments, schema overrides or a
proof library from the request. Only the selected trusted tenant runtime controls
those. A consumer must invoke/recheck that runtime and compare all exact bindings.

Ordinary generation is admitted by a tenant-owned parameterized signature profile,
with subject-derived namespace, fixed schemas/domains/cardinalities, and a bounded
relation-kind catalog. A self-defined arbitrary schema is not accepted. Existing
two pinned T011 signatures retain their exact legacy contracts.

The Graphify boundary mapping compares exact parent, seeds/budget, included/excluded
identities, all eight complete populations, external resolution tuples, omitted
local-reference occurrences, retained residuals and invalidation against actual
Lean output. Legacy string paths are checked against typed source reference paths.
Crossing relations are separately recomputed from source and selected records;
that metadata check is not presented as a Lean theorem. Excluded residual records
remain explicit in the formal evidence even though the existing Graphify view
schema has no separate field for them.

Compiler execution belongs in a declared integration effect boundary. The pure
Graphify context core does not launch it. Gate evidence is stored beside exact
proposal/context bytes, rather than inserted into its own hashed rendered input.

## Proof and support boundary

`AC.Model`, `AC.Closure` and `AC.Projection` retain their T011 definitions.
`AC.GateProof` is the fresh replay root, importing exactly the generic projection and structural proof libraries. `AC.GateRuntime` imports that internal proof module; JSON serialization remains compiled, pinned and output-tested outside the proof root. Each cold `verify` produces full `GateData.lean`, local/external character-source modules, a global identity certificate, reference/bounds checks, concrete `GateModel.lean` and
`GateViews.lean`, and a `GateRun.lean` executable. Generated proof declarations
use kernel reduction with `debug.skipKernelTC=false`; no native proof shortcut
is admitted. A second kernel replay checks the request's proof modules. The actual
Lean runtime emits the entire imported model and all requested projections;
Python compares that emitted structure with every retained source field and the
independently computed certificate. Opaque string payloads are retained in full,
including control characters and Unicode; no digest replaces the model data.

Small models use the original finite structural decision. Larger models can use
`AC.Structure`: exact record-key range, identity uniqueness, external separation,
and bounded edge/reference checks imply the *unchanged* `Model.WellFormed`.
Identity witnesses retain every original string. Exact `String.ofList` equalities
bind character lists to the local and external identities. A permutation-preserving
Nat-label sort reconstructs their complete concatenation. Every adjacent character
comparison, including proof-block boundaries, is checked; exact zip equality ties
those pairs to the complete order. Checked `String.ofList` injectivity transports
uniqueness to strings. One combined uniqueness result supplies both local/external
uniqueness and their separation. External membership is proved once per exact
bounded block index and reused by the complete reference checks.

The optimization is a proof certificate, not a stronger assumption. Resource
exhaustion in any concrete proof remains `incomplete`. Successful model checking
is performed once per batch; each selection reuses that exact theorem.

### Explicit trace witnesses

`gate_codegen.views_source` receives the exact imported model and certificates.
For each trace step it selects an actual dependency edge from a parent already
in the seeds or preceding trace. Generated kernel proofs establish both that
parent's membership in the preceding known set and the child's membership in
`model.dependencies parent`, which retains the original full edge relation.
Nested witnesses construct the existing `Witness` proposition directly. No
precomputed dependency table or altered dependency definition is introduced.

Seed nonemptiness, seed inclusion in the exact key range, trace-set inclusion in
that range and final dependency closure retain their original finite kernel
decisions. These four propositions and the explicit witness prove the unchanged
`checkCertificate model.dependencies model.localKeys seeds trace = true` premise.
The exact-set, reachability, success/refusal, `projectWithProof` and pointwise
runtime-equality suffix is unchanged. A missing parent is an internal generation
inconsistency retained as `incomplete`; it cannot create a proof or a verified
result. The focused generator test checks that failure retention.

This construction passed the actual 29-record case that exhausted the prior
combined decision. It does not establish a unique allocator cause: the preceding
range and closure probes discharged separately, and failed instrumentation is
retained in the diagnosis. Kernel negatives separately reject a real edge whose
parent is not yet known, a known parent with no such edge, and an omitted required
residual. Generic Lean definitions and the established support remain unchanged.

### Proof-directed runtime

The reusable gate executes `projectWithProof`, a specialization of the unchanged
`project` operation. It requires proofs of `checkModel m = true` and
`checkCertificate m.dependencies m.localKeys seeds trace = true` for those exact
dependent inputs. Its generic theorem proves equality to `project`; each generated
selection also proves that equality for the current model, seeds, trace and budget.
All of those declarations are axiom-audited and included in fresh kernel replay.

The runtime computes the original budget branch, `traceSet`, and `makeProjection`,
including record filtering and every boundary field. It then serializes the actual
result through `selectionResultJson`. No projection or success status is supplied
by a request or accepted from a prior result. Missing proof premises cannot inhabit
the generated call. Budget exhaustion still returns the existing refusal with no
truncated view. Full actual model/projection and supplied-view correspondence checks
remain mandatory.

This avoids recomputing already proved structural predicates at runtime. It does
not claim that the original `checkModel` or the direct `gateSelectionJson` wrapper
now runs faster. On the full 1,987-record subject, direct `checkModel` alone reached
the 90-second limit; model initialization and complete serialization each finished
in approximately 1.3 seconds. That original limitation remains recorded in T013.

A selected `profiles/proof-support-v1.json` records the exact compiler, generic
sources, imported source/object/IR/runtime files and fresh base-kernel replay.
Paths are relative to this tenant. The manifest is trusted selected verifier
configuration, never a request-supplied cache label. `formal_support.py` checks
its member hashes before and after every successful gate. Loader variables are
removed and Lean's search roots are constructed from the pinned Lake manifest,
with the fresh request directory as the only dynamic extension. New unselected
objects in the import search roots are refused to prevent import shadowing.

The public `identity` command prints only `{sha256,pins}`. Pin names are relative
paths under the selected tenant root. The consumer independently checks these
source/profile/manifest pins before executing the verifier. The selected support
manifest then binds the large import population without trusting a child-reported
success label. The consumer separately selects its Python executable and trusted
host runtime. Host Python/OS semantics remain part of the importer/runtime trust
boundary; this is not a proof of Python or an OS sandbox.

The selected standalone startup is `PINNED_PYTHON -I -S -B
scripts/formal_gate.py ...`. A plain CLI invocation re-executes under those flags
before importing deciding helpers. The scripts namespace must contain exactly
the declared flat `.py` files, with no packages, extension modules, sourceless
bytecode or symlinks. The sole permitted directory is an inert `__pycache__`
containing regular `.pyc` files. Before helper loading, the CLI checks that shape,
then compiles each selected helper's exact source bytes in dependency order under
controlled module aliases; it never consumes cached bytecode. Loaded helper hashes
must still match current identity pins. A supervising consumer checks namespace
shape and selected pins independently before starting the interpreter. Calling
the Python API directly leaves interpreter startup, imports and the host module
namespace under the trusted caller's control. A plain invocation cannot undo code
that already ran during Python initialization; explicit isolated startup avoids
that ambient initialization boundary for the supervised CLI.

Compiler effects run in private process groups. Timeouts and incoming termination
signals trigger bounded TERM/KILL/reap cleanup; cleanup uncertainty is incomplete.
An enclosing supervisor must account for those nested groups before its own
force-kill fallback. Retained outputs are regular files, avoiding an unbounded
pipe drain when a descendant outlives its parent.

## Portable setup and evidence

The repository locks retrievable upstream compiler archives and Mathlib/dependency
commits. The selected compiled-artifact support manifest is platform/build
specific. A different platform or rebuilt object population requires an explicit
new local support establishment and checker selection; matching source versions
alone do not silently admit new objects. Preserve the previous manifest, then run
`python3 scripts/formal_support.py --output profiles/proof-support-v1.json` with
the destination absent. Establishment rebuilds only the generic tenant targets
against the pinned cached imports and performs fresh base-kernel replay. The
caller then explicitly pins the new `identity` output. No global toolchain or
installed STDO basis is changed.

An evidence directory retains original raw `input.json`, optional raw
`supplied-views.json`, the original request, a path-rewritten replay request,
recovered `model.json`, certificates, generated sources/objects and diagnostic
logs. `request_sha256` hashes the canonical original request before path resolution
or retention rewriting. The model's raw-coordinate retained path names the
original input for model requests and the exact recovered model for carriers.
Every portable result limits `whole-model-source-correspondence` to that supplied
or carrier-recovered model JSON. Original prose/corpus-to-model `F_P` fidelity
remains opaque and unproved; retaining corpus coordinates does not establish it.
Both raw carrier custody and recovered canonical model identity are recorded.

`check-evidence` checks retained members, current deciding pins and exact replay
bindings, then creates a new immutable bundle with current checks. Its request
digest describes that newly issued replay request. Without an eligible trusted
local establishment it executes fresh concrete proofs. Portable evidence stays
inspectable and replayable; a public origin hint, saved success label or supplied
proof JSON is neither a credential nor a grant of operation authority.

The T012 local support used a conserved extension of an earlier
successful fresh establishment. That earlier manifest, successful log and exact
root source are embedded byte-for-byte in `origin.retained_text`, with fixed
selected SHA-256 identities in `formal_support.py`. All 30,392 prior members were
compared: 30,387 remain unchanged; only the tenant runtime source and four of its
compiled artifacts changed. The extension checks every new or changed tenant
module (`Structure`, `GateProof`, `GateRuntime`) against those exact imported
artifacts and audits the fixed generic theorem names for standard axioms. No new
external proof import is admitted. Ordinary gate requests cannot select a prior
manifest or invoke this setup-only extension. Unknown or changed external imports
stop reuse. The initial successful fresh replay took 74.01 seconds; subsequent
300-second fresh attempts were retained as incomplete, followed by the successful
16.16-second bounded extension. No failed replay was relabelled as success.

T013 explicitly extends that exact successful T012 manifest. The prior file is
hashed as raw bytes before UTF-8 decoding; a CRLF variant is refused before any
compiler effect. Every external/core source and object remains pinned. Only the
selected `Structure`, `GateProof` and `GateRuntime` tenant source/object delta is
allowed, with explicit direct imports and fresh replay of all affected tenant
modules. The manifest records exact changed/conserved populations and retains the
prior origin chain. This setup-only conservation is separate from dynamic request
proof reuse: every cold `verify` still generates, checks and replays its complete
concrete obligations. Dynamic reuse has its own completed-cold origin below.

## Exact local-origin reuse

`verify` always performs cold checking. Optional `check-evidence` reuse uses
`scripts/formal_reuse.py`, included in the exact helper namespace and source
identity. Explicit setup is `python3 -I -S -B scripts/formal_gate.py init-origin`.
It accepts no store or key argument and creates an absent owner-only
`.cache/formal-origin-v1/` beneath this selected tenant, with a random 32-byte
`origin.key`, fixed `selection.json`, `entries/` and `pending/`. Ordinary gate
requests never initialize, repair, rotate or import an origin. The public
selection's digest is pinned at exactly
`.cache/formal-origin-v1/selection.json`; identity output never contains key bytes.

The entire fixed subtree is reserved before ordinary request/input/evidence
reads or output creation, including when no origin is selected. Existing
ancestors must be nonsymlinked; ordinary files must be regular and singly linked.
Existing ancestor device/inode identity catches case aliases on Darwin. A missing
reserved suffix conservatively reserves its case variants. Output paths cannot
contain the protected subtree. Reads use no-follow descriptors and regular-file
checks. This reserves actual targets, not every registered root containing them.
The Graphify adapter independently implements that reservation without loading
Lean or reading the private key. Ordinary artifacts and local packages must
exclude the **whole** origin subtree, including public selection, keys, entries
and pending material; `.cache` Git exclusion alone is not package validation.

After all requested cold claims, theorem audits, kernel replay, actual output/view
comparisons and final source/support checks complete, the gate finalizes its
immutable result and manifest. Only that internal completed-cold path can seal an
entry. The entry binds the original request digest, exact fixed-relocation replay
request, all effective resource limits, full model/input/claim/source/support
identities, actual proof module/audit population, raw result and manifest digests,
and every retained artifact. The HMAC-SHA256 domain is fixed by the versioned
entry schema; canonical finite JSON rejects duplicate keys. No caller-provided
result can invoke a sign/import endpoint. Python host/API administration remains
trusted, including direct access to private helper functions.

Publication writes/fsyncs a protected pending entry, atomically inserts the public
`local-origin.json` hint, then atomically inserts the private final entry **last**.
No-overwrite insertion preserves existing entry meaning. Only that private final
namespace commits eligibility; pending files and manufactured public hints never
hit. A committed origin can exist after interruption before the caller observed
return. The receipt establishes completed checking, not observed caller delivery.

A local hit needs full runtime identity equality, the selected private key/seal,
and exact authenticated artifact bindings. Current input import/reconstruction,
ordered selection/certificate creation, full support checks before/after, actual
retained runtime model/projection/view correspondence, artifact bytes and origin
currentness all run again. Request matching uses canonical bytes, including
boolean/integer distinctions. Reuse launches no compiler, kernel replay or Lean
runtime and never imports retained `.olean` files. Those files are hashed as
original proof artifacts. Current observations explicitly record zero such
invocations and retain the original result, manifest, request and replay request
under fixed `origin-*` names. Original proof costs remain in `origin-result.json`;
current costs are separate. A reused bundle points directly to the same cold
establishment, with no chain or request index.

Standalone portable cold compatibility validates both complete identity
aggregates, removes only the exact fixed origin-selection pin from copied pin
maps, and requires every remaining pin and its population to agree. An origin-only
or absent-origin difference forces a current cold check. Changed deciding code,
profiles, proofs or support refuse. This exception never relaxes Graphify live
checker-policy/receipt/runtime equality. Missing optional origin material or hint
can cold-fallback; malformed or altered alleged local bindings refuse. Required
support unavailability remains incomplete; unknown profiles remain unsupported.

Internal elapsed time covers checking and excludes final bundle/origin publication.
Complete public wall cost must be measured externally through process exit. The
original and current result retain that scope and Darwin child-RSS limits. The
4096 MB, 90-second process and 600-second public invocation bounds are unchanged.
`tests/test_formal_reuse.py` uses isolated synthetic stores and stubbed proof/support
processes only. It is control evidence, not real formal qualification. The added
helper and selected origin participate in identity. A deciding-source or origin
selection change requires fresh exact-current establishment and qualification;
prior successful public results cannot be retrospectively signed or imported.
The actual small/full cold and reuse runs for the integrated predecessor are
retained under `T013_PRACTICAL_FORMAL_GATE/reuse/qualification-001`.

Qualification observations under `T012_FORMAL_GATE/runtime/qualification-002`
cover two new test-authored subjects and the actual Graphify view mapping. Small
successful invocations took approximately 16–17 seconds, including about four
seconds for each complete support recheck. `child_maxrss_native_units` uses
`resource.getrusage(RUSAGE_CHILDREN).ru_maxrss`: on this Darwin host the units are
bytes and the value is the process-lifetime maximum over reaped children. It is
not a measurement of one named proof stage; API batches may include earlier
children. The first isolated public CLI reported approximately 3.41 GB. The
1,987-record frozen subject did not pass the T012 attempts. T013 preserves those
negative observations, then establishes full identity/reference/model/view proofs
with the unchanged core definitions. Its final public execution outcomes are
recorded separately under `T013_PRACTICAL_FORMAL_GATE/lean`; proof completion alone
does not establish runtime or supplied-view qualification. The compiler setting
`-M4096` is not an OS physical-RSS cap. The public 600-second outer limit, individual
90-second checking limits, configured Lean memory and observed RSS are distinct
observations.

### Full-size T013 observations

The candidate frozen in `T013_PRACTICAL_FORMAL_GATE/lean/final-source-002`
completed these sequential public invocations on the same verifier identity:

| Actual request | Public result | External elapsed | Aggregate child high-water RSS |
| --- | --- | ---: | ---: |
| Complete 1,987-record model and supplied nine-record Graphify view | Verified | 269.83 s | 12.73 GB |
| Same view with its retained residual omitted | Refused at supplied-view correspondence | 269.89 s | 13.02 GB |
| Same closure with budget eight | Verified refusal, no truncated projection | 263.82 s | 12.77 GB |

The model retains all 1,021 external resolutions, 16,498 reference occurrences
and 3,995 edges. The selected view retains one unresolved residual and 18 external
boundary entries. Every invocation freshly compiled all deciding data/proof
modules and replayed all six generated proof modules. The positive invocation's
replay took 28.37 seconds and actual proof-directed runtime took 9.69 seconds.
The runtime emitted the complete model, and both model and projection JSON
matched independent source-derived output. No request proof or saved verdict was
reused. The original raw `checkModel` timeout remains a separate limitation.

These are single-host observations, not an OS memory guarantee or a general
performance claim. `-M4096` applies to the Lean compiler; the selected checker has
no memory flag. The RSS figures are process-lifetime maxima over all reaped
children of each external invocation, not measurements attributed to a named
stage. Failed identity encodings, representation experiments and the first public
runtime timeout remain retained. The exact scale return links their evidence and
the separate source-currentness, literal-escaping and raw-origin controls.

### Current explicit-parent cut

The source review at `T013_PRACTICAL_FORMAL_GATE/review/view-repair-source-001`
and public Phase A at `real-use/runtime-preparation-003/execution-001` bind the
current full runtime identity
`f492806bfb58bcabad63a89caa4c62c57bd37f8ed99b8fed764a9a6c5b8908c9`.
Its origin-free portable identity is
`4f9e8402122f1722559a4bb7d7559b09ce107f8de8a38de600aedc947611072d`;
only the fixed origin-selection coordinate is omitted. The support manifest
remains `7198879c3dfefe52ee4c980b33990197cd338eb19ac4e84cce3dd26a4cd66363`.

That public invocation verified the complete original 1,987-record model, seeds
182 and 278, 27-step trace and supplied 29-record view at budget 29. It freshly
compiled all seven dynamic proof modules, replayed the concrete proof and ran
the actual projection/runtime under the unchanged limits. Result
`72ad6dc64938ab0e76476f5d479c9154035131354423ebbbb9fde38c8737dfe4`
and evidence manifest
`fc0801aa9ecdd6c2cfd411e420246da66c78d445d87946cec4ac366bad0f699a`
identify that exact success; no previous proof result was imported as current.

Phase B at `real-use/runtime-preparation-003/execution-002` records the two
selected real Worker calls and authenticated returns. Execution completion does
not decide task quality, practical benefit, semantic acceptance or release.
Package selection/delivery records identify each local archive and installed
execution separately; origin-free installation must execute its own current
cold fallback. Conserving exact Darwin-arm64 support is not fresh-machine or
cross-platform qualification.
