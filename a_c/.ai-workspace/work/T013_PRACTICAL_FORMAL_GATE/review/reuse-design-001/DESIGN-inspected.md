# T013 exact local-origin reuse design

Design preparation by `/root/ac_scale_reuse_worker`, under
[ACTIVATION.json](ACTIVATION.json). This proposes tenant HOW under unchanged
FR-008–FR-014. It implements the conditions in
[REUSE_DESIGN_ASSESSMENT.md](../review/REUSE_DESIGN_ASSESSMENT.md); it is not an
implemented or independently qualified result. The installed builder remains
STDO v2.5.1-rc.2. Represented STDO 3.0.2 remains subject data.

## 1. Smallest useful scope

Keep `verify` cold. It can establish an eligible origin after complete success.
Let `check-evidence` reuse an exact authenticated original cold establishment.
Do not add a subject cache, request index, general path normalization, proof
fragment reuse, cross-Context reuse, or caller-selected trust root. Each reused
bundle points directly to the original cold establishment; no receipt chain is
needed.

This serves the current actual path: Graphify `_verify_formal` calls `verify`
at preflight; `_recheck_formal` calls `check-evidence` at dispatch and again
inside the supervisor's final launch guards. Both use the original preflight
run. Public Graphify checker/configuration, Context, policy, receipt and result
schemas can remain unchanged. Its internal adapter needs path guards before
its own I/O, and its fresh-replay docstrings need to describe current checking
with an eligible established proof.

The exact source changed during this read-only preparation because the scaling
Worker owns the Lean tenant. The closing record identifies the last observed
files; it is not a candidate freeze. In that observation, the dynamic modules
are `GateData`, `GateIdentities`, `GateBounds`, `GateModel`, `GateViews` and
`GateRun`. Reuse must consume the completed scaling implementation, not replace
its proof/module construction.

## 2. Selected local origin and protection before I/O

Add one standard-library-only helper, `scripts/formal_reuse.py`. The selected
tenant code fixes its store to `ROOT/.cache/formal-origin-v1/`; no request,
bundle, environment variable or output argument supplies another store or key.
An explicit setup-only `init-origin` command, without a store/key argument,
creates an absent store, a random 32-byte key and this public selection file:

```json
{
  "schema": "a_c.formal-gate.local-origin-selection/1",
  "origin_id": "32 lowercase hexadecimal characters",
  "store_relative": ".cache/formal-origin-v1",
  "key_sha256": "64 lowercase hexadecimal characters"
}
```

The fixed names are `selection.json`, `origin.key` and `entries/`. The
selection file is trusted local startup configuration, not request evidence.
`runtime_identity()` includes the selection file's relative name/hash when
present, so existing Graphify pin checks and explicit checker selection bind
it without changing their schema. Neither identity output nor result evidence
contains key bytes. The helper source is added to `SCRIPT_FILES`, exact CLI
helper loading and ordinary source pins. Merely importing it has no effects.

No selection means cold verification without origin publication. Ordinary
verification never initializes, rotates, repairs or replaces origin material.
Setup uses exclusive creation, owner-only directory/key permissions, regular
files and non-symlinked ancestors. It validates the selected key digest and
ownership/mode before use. Same-user administration that rewrites the trusted
runtime/private store remains outside the cooperative-host model.

Reserve the whole fixed store subtree even when no selection exists. Reject
ordinary inputs inside it and outputs equal to, below, or containing it. Check
resolved paths and all existing ancestors; reject symlinks, special-file inputs,
and multiply-linked ordinary files so a hard-link alias cannot disclose the
key. Use no-follow regular-file opens and descriptor checks for input bytes.
These checks precede any request parsing, retained-member hashing, copying,
output directory creation or diagnostic write:

| Entry | Required early guards |
| --- | --- |
| Lean CLI `verify` | `--request` itself and `--output`, before reading request JSON; then its input/view paths before retention. |
| Lean API `verify` | Resolved input/view paths and output before `mkdir` or reading/copying source bytes. |
| Lean `check-evidence` | Bundle and output before `resolve`-then-read loses alias information; every retained member before reading/copying it. |
| Graphify `verify` | Output before its existing `mkdir`, input/view/request writes and checker stdout/stderr writes. |
| Graphify `recheck` | Bundle/result and output before its existing `_regular` read and output creation. |
| Selected Graphify generation | `prepare` checks the manifest, each corpus member and output before reading/copying them; `_formal_selection` checks the prepared output territory before resumed generation writes. |

Graphify can conservatively derive the same reserved subtree from its already
selected checker root. It needs no key access or helper import to refuse those
paths. Generation uses the same internal guard with its trusted selected checker;
checking only `check_formal_proposal` would be too late because preparation
already copies corpus bytes. Its pin check may read the public selection file as trusted startup
configuration. Error messages report a protected-path refusal without printing
origin contents. The Lean helper's trusted entry lookup is distinct from an
ordinary input path; it accepts only a validated hexadecimal establishment ID,
never a supplied filename.

Reserve actual mediated SourceRef targets in `source_path` when the runtime
has a selected `formal_gate.checker`. `read_source` otherwise reaches a broadly
registered file before the formal adapter runs. After existing root/scope and
component checks, but before either the ordinary return or the `allow_absent`
early return, reject a resolved target in the protected subtree. For Writer
targets, reject overlap with it. Check existing final files for hard-link
aliases before `_regular_bytes` reads them. Derive the reserved subtree from
the trusted checker root; do not import Lean or read its key.

A repository-wide source read scope remains valid: a normal file under that
scope is acquired normally, while a request naming the protected subtree is
refused. Do not reject broad source registrations just because they contain
the store. When no formal checker is selected, source operations retain their
existing behavior and acquire no Lean/store dependency. The fixed formal
adapter/generation output guards still run before their own writes. This is
protection against ordinary mediated request paths, not against operator-level
policy changes, direct host reads or separately administered services that
deliberately expose the store; those remain trusted-host responsibilities.

The entire private subtree, including selection, key, temporary publication
files and entries, is excluded from packages and generic artifact collection.
Existing `.cache/` Git exclusion is useful but is not the package check. A
package has no inherited local origin; its own explicit setup/selection is
required before reuse can be established.

## 3. Exact binding and receipt format

Use the existing replay relocation only: copy the original request and replace
`input.path` by `input.json` and non-null `supplied_views.path` by
`supplied-views.json`. All other fields must remain exactly equal, including
schema, format, raw digests, ordered selections and ordered seeds, explicit null
versus integer budget, and the entire Context/activation binding. Raw input and
view bytes must still hash to those values. This is not normalization of
arbitrary newly supplied paths or substantively equivalent JSON. The full
original request hash is also retained. Require exact merged resource limits,
including byte/selection limits, not only the record budget.

The private immutable entry has `{schema, body, hmac_sha256}`. Its body is:

| Field | Bound value |
| --- | --- |
| `origin_id`, `origin_selection_sha256` | Exact selected local origin/configuration. |
| `request_sha256`, `replay_request` | Original canonical request digest and the exact fixed-relocation request object. |
| `resource_limits` | Complete effective `DEFAULT_LIMITS` plus allowed API overrides used by this establishment. |
| `model`, `inputs`, `requested_claims`, `checked_claims` | Exact final cold result fields, including raw carrier/model/view and recovered canonical model identities. |
| `runtime_identity`, `support` | Complete source/profile/generator/proof pins and selected support manifest identity/member count/platform from the cold result. |
| `proof_modules`, `theorem_audit` | Actual generated proof-module list and checked theorem/axiom reports captured by the cold path. No new caller list. |
| `result_sha256`, `manifest_sha256`, `members` | Raw final cold result and manifest digests plus the entire manifest member mapping. This binds all result fields, proof costs, generated sources/objects, certificates, actual-runtime log and supplied-view comparison. |

The schema fixes the HMAC algorithm and domain separation. Serialize with UTF-8,
sorted object keys, compact separators, finite JSON numbers and duplicate-key
rejection. `entry_id = sha256(canonical(body))` and
`hmac_sha256 = HMAC-SHA256(key, fixed_domain_prefix || canonical(body))`.
Use constant-time tag comparison. Member names must be plain basenames, and
every claimed artifact must be a regular file with exactly the signed bytes.
No digest substitutes for retaining the actual input, model or runtime output.

A public `local-origin.json` sidecar contains only the versioned schema,
`origin_id`, `entry_id` and a fixed `cold`/`reuse` layout discriminator. It is a
lookup hint, not an authentication root. The selected private entry must exist,
authenticate and match all reconstructed bindings. A caller's store, key,
success label or refreshed manifest cannot create that relation. The private
entry or key is never copied into the public bundle.

## 4. Cold establishment and atomic publication

Preserve the completed cold path: input/profile/import/reconstruction checks,
complete support check, all generated concrete proofs and theorem audits,
dynamic kernel replay, actual runtime model/projection comparison, actual
supplied-view comparison, final deciding-source and complete support rechecks,
and sufficient-budget result. Only `status == verified` with exact equality of
requested/checked claims reaches the origin publication call.

Finalize and hash the complete cold bundle and `result.json` first. There is
no CLI/API import-or-sign endpoint for caller-supplied result JSON. Only the
internal completed cold control path may call the helper's private publication
operation. No publication follows refused, unsupported, incomplete, timeout,
cleanup uncertainty or a source/support change.

Write and fsync an entry temporary file under the protected store, then publish
the immutable final entry with an atomic no-overwrite operation. Publish the
public pointer last, also atomically and without overwrite. An interrupted
pre-commit attempt has no complete entry/pointer pair and cannot hit. Temporary
or orphan entries are ignored; ordinary requests do not repair them. The final
pointer commit marks completed local establishment; a later transport failure
does not retrospectively invent an observed caller return.

The pointer is a reserved optional sidecar outside the already sealed cold
manifest, preventing a result/manifest/receipt hash cycle. No later mutation
refreshes the original result or entry. Concurrent attempts may create distinct
complete establishments because their measured cold results differ; no index
or mutable “latest” entry is required.

Existing full-size success before this implementation cannot be signed or
imported afterwards. Adding the helper and selecting a new origin changes the
runtime identity. One fresh full-size cold run under the final selected identity
is required to establish the first full-size reusable proof.

## 5. Reuse path and unchanged consumer checks

Keep `verify(request, output_dir, limits=None, *, base_dir=None)` and
`check_evidence(bundle, output_dir, limits=None)` public signatures. Refactor
their shared acquisition/comparison/finalization logic internally; do not add
an untrusted origin argument to the request or public API.

`check-evidence` still checks its current bundle manifest, result binding,
current runtime identity, original request digest and exact replay mapping.
If there is an eligible selected-origin pointer, authenticate the private entry
and compare the full original cold result/manifest/artifacts. Then:

1. Re-read and retain current exact input/view bytes after protected-path checks.
   Re-run request/profile/import/reconstruction and resource-limit validation.
2. Check the helper namespace/current source identity and call the unchanged
   full `formal_support.check()`, including its unselected-object scan.
3. Recompute closure certificates from current exact seeds/budgets. Compare
   them and the imported/recovered model with their established artifacts.
4. Parse the authenticated retained `actual-runtime.log` as data. Re-run
   `model_output`, `projection_output` and actual supplied `graphify_view`
   correspondence checks against the current import/certificates. Retained
   runtime execution is explicitly attributed to the original establishment.
5. Recheck complete artifact bytes, exact origin/configuration, current source
   identity and the full support population before returning verified reuse.

The reused path launches no Lean compiler or checker and loads no saved `.olean`.
Those objects are hashed as retained proof artifacts only. The cold fallback
always generates fresh modules in a fresh output directory; it never adds a
caller bundle to the Lean import search path.

For a reusable output, retain the original cold `result.json`, `manifest.json`,
`request.json` and `replay-request.json` as fixed `origin-result.json`,
`origin-manifest.json`, `origin-request.json` and `origin-replay-request.json`.
Other original signed artifacts keep their names. Current request/replay,
manifest and result keep the ordinary names. The fixed layout maps the four
metadata names only; no caller-provided mapping or nested receipt chain is
accepted. A later reuse checks the same original cold entry directly. Copy only
the validated signed public artifacts, never a private-store file or an
unlisted directory member.

Current `result.json` retains schema/status semantics and records
`observations.reuse = "local-origin"`, the original entry/result/manifest
identities, separate current stage costs, and explicit zero current dynamic
proof/kernel invocations. Preserve the entire original result and original
proof-stage costs; do not relabel those times as current work. The current
request hash still describes the newly issued replay request.

Graphify continues its independent current checker identity/result checks,
source acquisition through `read_source`, rendered Context equality, current
selection/view/activation binding, policy/grant checks and final stdin digest
comparison. `_formal_inputs`, `_verify_formal`, `_recheck_formal`, pure Core and
the supervisor's authority checks keep their current decision/result semantics;
the selected actual-source-path exclusion above protects origin storage. A
current proof does not preserve a removed permission or changed Context.

## 6. Failure and cost contract

- No selected origin, no pointer, a foreign origin, or a missing local entry:
  record why reuse was unavailable and use the existing fresh cold path on the
  actual validated retained inputs. Never recreate a key automatically.
- A purported local entry with a bad seal, changed binding/artifact, malformed
  layout or stale deciding source/support: refuse the affected evidence. Do
  not hide observed tampering behind a cache hit.
- Unavailable optional origin material may cause an explicit cold fallback;
  unavailable required proof support or interrupted cold/current checking is
  incomplete. Unsupported request/profile remains unsupported. Resource
  exhaustion remains incomplete; an insufficient record budget remains refused.
- Reuse does not establish original prose fidelity, semantic dependency
  sufficiency, authority, acceptance, general host isolation or benefit.

Measure each public invocation externally from process start through exit and
bundle publication, plus per-stage importer/support/artifact/correspondence/
origin costs. The current internal `elapsed_seconds` ends before final artifact
publication; it must not be advertised as the complete public wall time. Record
that scope or extend instrumentation without circularly rewriting sealed
results. Preserve the Darwin child-RSS scope and record parent/child measurement
coverage. Keep 4,096 MB, 90 seconds per checking process and 600 seconds per
public invocation. Run heavy checks sequentially.

## 7. Bounded implementation and validation grant requested next

After the complete cold scaling result closes and source ownership is handed
over, the minimal candidate write set is:

- Lean `scripts/formal_gate.py`, new `scripts/formal_reuse.py`,
  `tests/test_formal_gate.py`, new `tests/test_formal_reuse.py`, and
  `design/FORMAL_GATE.md`.
- Graphify `code/ac_formal_gate.py`, the narrow selected-target `source_path`
  protection in `code/ac_support_core.py`, the early selected-generation guards
  in `code/ac_generate.py` (`prepare`/`_formal_selection`), and
  `test_env/test_ac_formal_gate.py`, limited to protected-path guards,
  descriptions and applicable tests.
- Separately granted local setup/evidence territory for the selected private
  origin and retained verification results. No secret belongs in work records.

No reuse change is currently needed in `formal_support.py`, Lean proof sources,
common requirements or public Graphify schemas. The scaling Worker's changed
support establishment must remain intact.

| Validation | Required evidence |
| --- | --- |
| Cheap isolated origin controls | Explicit setup; no request-selected store/key; immutable publication; duplicate/nonfinite JSON refusal; missing/wrong key or tag never gives a hit. Unit stubs are not proof qualification. |
| Success gate controls | Force each pre-publication stage to refuse/fail/interrupt; no eligible complete pointer/entry. A success-looking partial result cannot be imported or signed. |
| Real small public cold and reuse | New supported subject with nontrivial supplied view, one actual cold establishment, one actual `check-evidence` reuse and one reuse of the reused bundle. Same model/claims/input/view/selection/budget/Context; no current compiler/kernel invocation on hits. |
| Exact-binding adversaries | Change raw model/carrier, canonical model, view, selection order, seed order, budget, Context/activation, resource limits, result, generated source/object, runtime log and theorem report. Refresh caller manifests where relevant. No verified reuse. |
| Runtime currentness | Change helper/source/profile/namespace, selected support member or an earlier-root shadow object; preserve current refusal/incomplete behavior and final recheck detection. |
| Foreign portable bundle | A valid complete public bundle without this selected local origin executes real fresh verification on a small subject; a caller-created verified bundle cannot skip proof work. |
| Protected paths | Exercise CLI request, input, view, bundle, API, selected generation corpus/manifest and Graphify output against key/store/ancestors, symlinked ancestors and hard-link aliases. Under one broad registered read scope, ordinary files still work and protected actual SourceRef/Writer paths refuse before acquisition, including absent Writer targets. Unselected source operations gain no Lean dependency. Protected bytes stay unchanged and absent from output/diagnostics. |
| Crash/concurrency | Stop before final publication; observe no eligible entry/pointer pair. Concurrent immutable publication cannot overwrite a prior establishment. No chain/cycle syntax is admitted. |
| Actual Graphify consumer | Existing bounded executor controls observe preflight cold, dispatch/supervisor reuse, changed Context and revoked grant refusal, unchanged actual stdin binding. Do not add a third real F_P trial. |
| Full subject and cost | After final freeze/setup, one sequential cold then reuse on all 1,987 records/1,021 externals and the selected actual supplied view. Preserve every artifact and complete public costs under the retained limits. |
| Package check | Explicit package inventory/extraction contains no private-origin subtree, selection, key, entry or temporary file; foreign fresh verification remains possible. Independent Reviewer assesses the exact candidate/evidence. |

Preparation stops here. No code, test, key, cache, model, proof, Git or package
effect is authorized by this design document.
