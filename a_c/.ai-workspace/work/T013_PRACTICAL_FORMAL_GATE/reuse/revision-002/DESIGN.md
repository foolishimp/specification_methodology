# T013 reuse design revision 002

This successor changes only the R1–R3 algorithms, affected guard placement and
tests in the [original design](../DESIGN.md), SHA-256
`e1744a44a53887795aacbcf8784abd6f5a9a829ad9b9e97ebc9e83ced8f73a1e`.
Unaffected clauses remain proposed as written there. It responds to the closed
[source review](../../review/reuse-design-001/REVIEW.md), whose closed return is
`28580ead58fb6efde66cb227457f6b2df6c5524a4adceafac1563c5343561325`.
This is a source-level proposal for independent assessment, not implementation
or proof evidence. The original design/closure remain unchanged.

## R1 — Separate local reuse identity from portable cold compatibility

Replace the unconditional saved/current identity equality at the beginning of
standalone `check-evidence` with the following classification. Define one
code-owned constant, exactly:

```text
ORIGIN_SELECTION_PIN = ".cache/formal-origin-v1/selection.json"
```

1. Validate both complete identity objects: exact `{sha256,pins}` shape,
   well-formed relative pin names/digests, and `sha256 == digest(pins)` for each.
   Acquire the current identity through the normal sealed namespace/source
   path. Do not modify either original identity or its retained digest.
2. Compute `same_full_identity = saved_identity == current_identity`.
3. For **standalone cold-fallback compatibility only**, remove that one exact
   dictionary key from copies of both `pins` maps. Compare the resulting maps
   for exact equality. Do not compare the original aggregate hashes after
   removing a coordinate, and do not accept a caller-provided ignore list,
   origin prefix, alternate path or label. Every deciding code/profile/support/
   toolchain pin and its population remains strict.
4. If these remaining maps differ, refuse stale/incompatible evidence. A
   changed generator, helper, theorem, support manifest or extra pin is not an
   origin-only difference and does not reach this fallback.
5. Validate the retained manifest/member bytes, original request digest and
   exact replay relocation as before. If the full identities differ only in
   origin selection, take the **cold path**, regardless of the public hint.
   Absence of this coordinate on one side is allowed here. Neither a foreign
   nor absent selection can qualify as local reuse.
6. Only `same_full_identity` permits the existing selected-origin eligibility
   lookup. Missing/foreign hint or absent final local entry still takes cold
   verification. An alleged local entry with a bad seal or changed exact
   binding remains refused, as in the original design.

Cold fallback calls the current `verify` on the actual retained input/view and
exact replay request, with fresh generated modules, actual compiler/kernel
execution, actual-output correspondence and full current support checks. Its
result contains the **current full identity**, current costs and the reason
reuse was unavailable. It inherits no checked claim or success standing from
the old result. A new local receipt may be established only by that new complete
cold success. Optional origin availability does not waive required proof support.

This exception is private to standalone portable-bundle checking. Do not
change Graphify `_pins`, `_result`, `recheck`, `_recheck_formal`, checker-policy
hashes or their receipt/runtime equality. A live preflight issued under origin
A cannot silently dispatch under origin B or no origin. It needs a new current
preflight under the existing authority contract. A standalone successful cold
fallback does not itself re-admit the old live receipt.

## R2 — The private final entry is the eligibility commit

Replace the original private-entry-then-public-pointer order. Preserve the
requirement that all cold proof, requested/checked claim equality, runtime
correspondence and final source/support checks succeed before publication.
Then perform this sequence:

1. Finalize and hash the complete cold public result and artifact manifest.
   Construct the exact entry body and seal only through the internal completed
   cold-success path.
2. Write the complete sealed entry to a protected pending namespace, using
   exclusive creation and fsync. Pending files have a fixed distinct temporary
   layout, are never looked up as entries, and confer no eligibility. No
   ordinary API can move, import or finalize one.
3. Atomically publish the public `local-origin.json` lookup hint without
   overwriting an existing file. It is still untrusted metadata. Failure or
   interruption here leaves no eligible private final entry.
4. **Last**, atomically insert the already complete entry into the protected
   `entries/<entry_id>.json` namespace with a no-overwrite operation. This
   private namespace insertion is the sole eligibility commit. The helper
   checks that any concurrent existing final entry is byte-identical; it never
   refreshes an established entry's meaning. Apply the selected durability
   flushes and clean up pending files without changing the final entry.

Lookup reads only the exact final private entry after validating the hint's
fixed grammar, current selected origin, HMAC and complete claim/artifact
bindings. It never enumerates or accepts pending files. A manufactured hint
cannot complete an interrupted pre-commit establishment. A missing final entry
can cause cold fallback; it can never produce a reuse hit.

Distinguish three observations:

- Cold checking completed: the exact proof/output checks finished successfully.
- Local establishment completed: the protected final entry was atomically
  inserted after those checks. The untrusted hint does not prove this event.
- Caller return observed: the calling process received the actual completed
  invocation result. This is a separate transport observation.

Interruption before the private commit creates no eligible entry even if a
complete public hint/result exists. Interruption after the private commit may
leave a valid local establishment whose caller return was never observed. A
later verified lookup can use that completed establishment, but must not claim
the earlier caller saw success. Process exit and complete public wall cost
remain externally measured; no post-commit rewrite of the sealed cold result
is required. The public pointer stays outside the sealed original manifest,
as specified previously, and it cannot authenticate publication status.

## R3 — Shared checkpoint protection after a narrow trusted bootstrap

### Existing authority and scope

The current [Graphify formal-gate design](../../../../../build_tenants/graphify/design/formal-gate.md)
defines `checker.json` as operator-selected trusted startup configuration and
states that the plan plus `formal-selection.json` retain it and later commands
inherit it (Trusted selection; Ordinary generation). `prepare` writes those
fixed metadata files. `_formal_selection` already compares inherited selection,
retained selection and an explicit override. It does not authenticate an
arbitrary author of a replacement plan.

Accordingly, retain the existing cooperative-host premise: the operator selects
the retained generation run and maintains custody of its startup selection.
F_P answers, corpus bytes, member paths, retained model/evidence and ordinary
mediated SourceRefs remain untrusted. Rewriting or replacing the selected
startup plan/selection, deliberately choosing another unselected run, or
granting arbitrary host reads is operator/host administration outside this
boundary. A hosted wrapper must own this run/selection choice; it cannot
promote an untrusted request's arbitrary run directory to trusted startup.
No new cryptographic authentication of generation plans is claimed.

This distinction permits a small bootstrap instead of new CLI arguments or a
selection registry. The **only pre-reservation reads** for an inherited
selection are the fixed operator-owned `plan.json` and, when present,
`formal-selection.json`. Read them solely as configuration: parse JSON, extract
and reconcile selection, and inspect no plan-named paths or subject content.
Their regular-file/no-alias custody is a trusted startup precondition. The
bootstrap must not retain their bytes as subject inputs, execute them, or print
raw content on a parse failure. It does not claim that origin-path guards
already ran before these two trusted configuration reads.

The risk is explicit: if an operator instead points these configuration
locators at origin material or permits another actor to replace their
selection, the trust premise is broken before ordinary-input reservation is
available. This is the same excluded startup-policy rewrite, not a reason to
add new resume semantics. A caller-supplied corpus/member path, by contrast,
is inside the protected boundary and must be guarded before any read.

### Concrete checkpoint algorithm

Split the selection resolver from `_formal_selection` into a read-only helper
used at the top of shared `checkpoint`. Keep `_formal_selection` as the existing
explicit-selection persistence operation, using that same resolver. The
resolver preserves current equality/missing-selection refusal rules and has no
ordinary write or origin-store effect.

When an explicit trusted first-assemble/run checker is already available,
guard the bootstrap metadata paths before reading them as well. The narrow
pre-reservation configuration read is needed only for inherited selection.

1. Read only the fixed trusted startup metadata described above. Reconcile
   `plan.formal_checker`, retained `formal-selection.json` and an already
   supplied explicit first-assemble/run selection. Resolve at most one exact
   selected checker. A missing prepared selection or changed override refuses
   before any manifest, chunks or corpus acquisition.
2. If no checker is selected, continue the current unselected checkpoint path:
   no Lean/store lookup, origin initialization, new source restriction or
   invocation. Do not apply a blanket reserved-name rule to unrelated
   unselected paths.
3. If a checker is selected, validate it using the current trusted adapter
   rules. Derive its fixed reserved origin subtree. Apply the precise path
   guard to output territory and the two bootstrap files before proceeding;
   confirm their current bytes still equal the configuration just read.
4. Before each ordinary `read_bytes`/`load`, guard the **actual** source
   manifest, chunks, each corpus member, and selected upstream prompt or other
   checkpoint dependency. Revalidate relative-member grammar and symlink/
   hard-link/regular-file constraints at acquisition, rather than trusting a
   previous `prepare`. Check all current digests as before. No dependency hash
   calculation may read a protected target first and refuse afterwards.
5. Return the existing `(plan, chunks)` result. Shared later acquisitions use
   the selected guard when reopening members or preparing output targets;
   upstream extraction receives only the actual paths already checked at its
   boundary. Do not claim adversarial concurrent filesystem isolation.

`stage`, `build_discovery`, ordinary `assemble`, public `run`,
`actor_evidence`, and grounding/repair callers already enter shared
`checkpoint`; moving protection there covers their **first** dependent read.
They need no new inherited-selection argument. Existing first `assemble`/`run`
overrides must reach the checkpoint bootstrap before its dependent reads,
through an optional internal `checkpoint(..., formal_checker=...)` argument.
Initial `prepare` already has the trusted checker argument and guards manifest,
corpus members and output before their first ordinary access.

Keep the original selected-only `source_path` guard before both the normal and
absent-Writer return. A broad registered read root remains lawful. Only actual
protected targets/aliases and overlapping Writer/output targets refuse.
Unselected SourceRef operations gain no Lean/store dependency.

## Focused validation additions

| Finding | Required controls |
| --- | --- |
| R1 | Same deciding pins with origin A, origin B and no-origin selection: standalone origin-only differences reach actual cold verification and report current full identity; matching origin may reuse. Change any other pin, add a caller-labelled origin pin, or corrupt an aggregate identity: refuse. |
| R1 live consumer | Keep an admitted Graphify receipt/configuration from A, change selection to B or none, and prove existing strict current/config/receipt checks prevent dispatch. Portable fallback does not update the old receipt. |
| R2 pre-commit | Stop after pending entry, after public hint, and immediately before private final insertion. Supply a manufactured valid-looking hint in each retained bundle. No reuse hit or automatic pending-entry promotion; cold fallback must actually execute. |
| R2 post-commit | Stop immediately after private insertion and before observed caller return. The completed private entry may support a later exact hit; evidence must retain that the original caller return was unobserved. Concurrent publication cannot overwrite another final entry. |
| R3 inherited resume | Keep the operator-owned plan/selection fixed. Substitute origin aliases for source-manifest, chunks, corpus members and selected upstream prompt. Invoke `stage`, `build_discovery`, `assemble`/`run`, and representative grounding/repair shared-checkpoint callers. Refuse before the targeted read, not merely after its digest differs. |
| R3 explicit first selection | A previously unselected prepared plan receives an explicit checker at first assemble/run. Its checkpoint acquisitions are guarded before `_formal_selection` persists the choice. |
| R3 compatibility | Existing inherited selected commands require no new flags. A normal source under a broad read root still works; actual protected SourceRef/absent-Writer targets refuse. Genuinely unselected generation and SourceRef calls retain their existing behavior and need no Lean installation. |

The proposed candidate write set is otherwise the original one. The
`ac_generate.py` scope is now `checkpoint`/its acquisition helpers and existing
first-selection call sites, in addition to `prepare`/`_formal_selection`.
Graphify design documentation must describe the trusted bootstrap exception
and exact public compatibility. No new resume CLI/schema, generic cache/index,
proof fragment, authority mechanism or model-selection framework is selected.

No code, test, key, cache, model, proof or Git effect was performed in preparing
this revision. Implementation still waits for the full public cold success,
source ownership handover, independent design disposition and exact new grant.
