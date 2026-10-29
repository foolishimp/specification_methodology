# Independent review of staged T013 reuse implementation 001

No actionable S0–S4 defect found in the inspected cut. I recommend that the
Executive integrate this exact source candidate for actual qualification. This
is an assessment and recommendation, not an operation grant, Product acceptance,
or a verified cold/reuse performance result.

## Exact subject and review boundary

The subject is the isolated staged tree at
`../../reuse/implementation-001/candidate/a_c`, not the unchanged live tenant.

| Record | SHA-256 |
| --- | --- |
| Author CLOSED.json | `2cdcd1cebc7a91cdc0a4a54062a9d81676389b20e720042d22012cfd702afe45` |
| candidate.patch | `cdccf9fdd55ac558f1b248c8139ac7e7372fd9e2133feaa74d81f0c1299aebc6` |
| SOURCE-PINS.json | `9f69e8559f33b4048071ea55541dd16de0dc34218d87e294ee9e0ba39cda2789` |
| HANDOFF.md | `4e568f5f5ef89370f5e1c35c6e3b327c9aa103be030839659455d582fc8e332b` |
| Approved revision-002 design | `2a0cf59bff21aafe20f28830ecaf0749b3835e547a219cde32da5f26751c5775` |

All 41 staged source pins and 38 refreshed before-source pins match. The exact
delta contains eight modified baseline files and three new files. Thirty of
the baseline files are unchanged in the candidate; the author's statement that
38 live baseline files remained unchanged describes staging custody, not 38
unchanged candidate files. The appended full-size observations in the Lean
design are preserved through the recorded baseline refresh.

I inspected the approved design and both acquisition refinements, the complete
new origin helper, the changed gate and adapter paths, selected acquisition in
generation/repair/grounding/SourceRefs, and the unchanged live Context and
preflight/dispatch/supervisor consumer. I verified the hashes of the author's
three logs reporting 60 synthetic/compatibility controls; I did not rerun them.

The independent `inspect_in_memory.py` has 31 passing source/hash, in-memory
envelope and ordinary-ancestor metadata discriminators. It compiles only selected
function definitions from the pinned files, imports no candidate module, and
never invokes a gate, compiler, kernel checker, actor or real origin operation.
Its synthetic envelopes are expressly not proof evidence. The two initial probe
setup errors (missing `re` and a constant-expression extraction assumption)
were in this review harness and were repaired before the retained run. All writes
are confined to this review directory. No Git, candidate, live cache or key effect
occurred. Packaging/transport assessment is separately delegated.

## Actual-path assessment

All source locations below are relative to the staged `candidate/a_c` root.

### Cold completion is the only public establishment path

`build_tenants/lean/scripts/formal_gate.py:169` keeps public `verify` cold.
The reusable branch is an internal argument, not a request field or CLI option.
The request's exact field set is enforced at line 108. The cold path at lines
249–282 generates all eight source modules, compiles the seven deciding modules,
audits the concrete theorem names, replays all six proof modules and runs the
actual proof-directed runtime. The shared continuation at lines 315–350 compares
the complete model, ordered projections and supplied views, rechecks source and
support, rejects insufficient budgets, and requires requested/checked claims to
agree before setting completion.

Only the completed branch after immutable result/manifest publication reaches
`formal_reuse._establish` (`formal_gate.py:366`). The fixed origin key is loaded
from protected local setup, never supplied by a request or receipt. Ordinary
CLI paths provide no sign, import, move-pending or caller-result establishment
endpoint. Direct Python host administration remains the explicitly trusted
boundary; this review does not reinterpret private helper calls as a sandbox.

### Authentication, exact inputs and current checking survive reuse

`build_tenants/lean/scripts/formal_reuse.py:339` looks up only the exact final
entry named by a grammar-checked hint under the selected origin. It verifies
the HMAC with `compare_digest`, the body-derived entry identity, exact original
artifact/result/manifest binding, full current runtime identity and type-exact
resource limits. A manufactured hint without a final private entry misses.
A bad alleged local seal refuses. Refreshing public metadata cannot replace the
authenticated body. The independent in-memory probes exercised those cases.

`formal_gate.py:378` validates the retained bundle, original request digest and
fixed replay relocation before lookup. Its canonical comparison preserves
boolean/integer distinctions. On a hit, lines 285–313 also require the exact
canonical replay request, limits, model, inputs, claims and freshly checked
support. Current import/reconstruction and certificates still run; original
artifact bytes are checked during copying, current complete output/view
correspondence runs again, and lines 331–344 repeat support, runtime and origin
currentness. Retained `.olean` files are inert bytes on this branch and never
imported. There is no path from a caller's `verified` field alone to skipped proof.

The current gate/helper/profile identity and selected compiler/library/source
support remain deciding inputs. `formal_gate.py:96` includes the new helper and
optional origin selection in runtime identity; the CLI loads exact source bytes
and preserves its flat namespace checks. The unchanged support checker still
checks every selected member and import-shadowing restrictions. The original
model, closure, projection, character-witness generator and support machinery
are conserved; no new whole-Mathlib replay is justified by this source delta.

### Standalone portability does not relax live Graphify identity

`formal_reuse.py:226` validates both complete identity aggregates before removing
only `.cache/formal-origin-v1/selection.json` for standalone cold compatibility.
Changed helpers, support, extra pins or malformed aggregates do not pass this
exception. `formal_gate.py:393` uses local lookup only for full identity equality;
an origin-only difference takes cold verification with current identity.

The Graphify consumer remains stricter. `ac_formal_gate.py:174` checks all selected
pins before invocation; lines 359–363 bind a successful emitted result to retained
bytes and exact configured identity; lines 400–415 bind rechecking to the current
retained receipt. `ac_support_effects.py:674` checks actual rendered Context bytes
and reacquires the model; lines 751–798 keep current policy, activation, model,
views, protected receipt, result bytes and checker selection tied together.
Standalone cold portability cannot re-admit an old live preflight under another
origin. Existing authority and composition checks still decide permission.

### Publication and original provenance are honest

`formal_reuse.py:318` constructs the binding only after completed cold checking,
writes a protected pending entry, publishes the untrusted public hint, and inserts
private final eligibility last. `_install` at line 296 is atomic and refuses a
different existing entry. Lookup never searches pending entries. Interruption
before final insertion cannot become reuse merely by manufacturing the hint.
Interruption after insertion may leave valid completed checking without an
observed caller return; `formal_gate.py:371` and the retained provenance do not
claim otherwise.

`formal_reuse.py:263` maps the fixed original metadata directly for reused layout.
`formal_gate.py:291` retains the original result/manifest/request and artifacts,
and line 369 republishes a hint to the same original entry. The independent
lookup probe confirms direct cold-body identity through the reused layout.
There is no growing receipt chain. Current observations report zero proof/runtime
invocations and preserve original costs in `origin-result.json`. Complete process
wall cost must still be measured externally; the internal elapsed field excludes
publication and is not a whole-command cost claim.

### Selected acquisition reserves private origin material before data reads

The Lean guard (`formal_reuse.py:63`) and Graphify guard
(`ac_formal_gate.py:64`) compare actual ancestor device/inode identities, reject
symlinks and multiply linked regular inputs, and reserve missing suffix case
variants conservatively. Independent metadata-only probes on this Darwin host
confirmed case-alias ancestor and absent-suffix refusal in both implementations.
Broad input directories remain eligible; only actual protected targets and
overlapping outputs are refused.

The shared generation startup/checkpoint path (`ac_generate.py:228`, `:255`,
`:284`, `:389`) resolves selection before ordinary subject acquisition, guards
actual paths and scans the selected retained run using metadata only. The scan
does not follow a directory symlink. Subsequent confined actor/journal reads are
covered by that inspected territory under the declared cooperative-host premise.
The direct repair request guard (`ac_repair.py:232`) and direct normalization
journal guard (`ac_grounding.py:231`) run before their first retained data read.
`ac_support_core.py:662` applies reservation to both normal SourceRef acquisition
and absent Writer targets before their return; actual source acquisition remains
subject to the existing scope, digest and recipient-authority checks.

The two fixed operator-owned inherited startup metadata reads remain an explicit
trusted bootstrap, not an authenticated arbitrary run-directory selector. An
explicit first selection guards even those reads. Unselected behavior is
conserved. Host policy replacement, unselected access deliberately granted by the
operator, and adversarial concurrent filesystem replacement remain outside the
selected mediated boundary. The review found no need to enlarge that boundary.

## Conditions discharged and still open

| Condition | Assessment of this exact cut |
| --- | --- |
| R1, fixed origin-only cold compatibility with strict live identity | Discharged in source and bounded in-memory discriminators |
| R2, private eligibility commit last; no hint/pending promotion | Discharged in source; author's synthetic interruption controls are retained |
| R3, shared selected acquisition, direct entry guards and aliases | Discharged in source and bounded independent alias probes under the declared host premise |
| Exact current request/support/output binding and direct original provenance | Discharged at source review level |
| Actual integrated cold establishment and authenticated reuse | Open; no real origin or new final-runtime proof was exercised in this review |
| Final identity, owner/checker selection and current Worker delivery | Open; the changed support Core requires the planned source/owner re-entry before activation |
| Actual adverse reuse controls and whole-process cost | Open; execute on the integrated identity with externally measured cost |
| Matched actual F_P tasks, outcome quality and practical benefit | Open; retain the approved maximum of two Worker runs and allow benefit to remain unestablished |
| Actual portable archive/install and final independent acceptance | Open; separate packaging review and later execution |

The earlier exact full-size cold result remains valid at its own frozen identity.
It cannot be retrospectively signed into this new helper/origin identity. The
next useful step is the already selected integration and bounded actual small/
full cold→reuse qualification, followed by the real Worker trial. No additional
design expansion or new general hardening campaign is requested by this review.
