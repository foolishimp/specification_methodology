---
name: stdo-tool-operations
description: Use when governed STDO work in this repository needs a supported tool operation — acquiring deciding sources, observing the workspace, or writing an effect through the a_c public CLI — and when a tool returns an unsupported method or an execution error. Covers bounded context acquisition. Not for unrelated tasks.
---

# STDO tool operations — supported use and bounded context

Use this skill to bind each required operation to an exact, supported tool
contract, and to acquire only the context the task needs.

## Transport and operations (SK-04)

The ordinary transport is the a_c public CLI. Send one full request envelope on
stdin; no request file is needed:

```
<python> -B <a_c>/build_tenants/graphify/code/ac_support.py \
  --policy <worker-policy.json> --policy-sha256 <sha256> \
  --principal <principal-id> call --request -
```

The policy path, `--policy-sha256`, `--principal`, and the `grant_id` used by
effect operations are supplied by the current activation context. Do not embed a
specific activation's policy, sha, principal, or grant in reusable instructions.

Discover exact schemas with `tools.describe` before first use, then reuse the
acquired schema; do not reload it for ceremony. Supported, commonly used
operations:

- `source.read` — `arguments {source: SourceRef, encoding: "utf8"}`; returns the
  content plus a retained acquisition artifact.
- `workspace.observe` — `arguments {scope: [{root, path, kind}], previous?}`;
  returns an observation artifact at `result.artifact` (pass that ref, not the
  top-level operation evidence, where an observation basis is required).
- `work.write` — `arguments {grant_id, target: SourceRef (sha256 null only for a
  confirmed-absent file), mode: "replace"|"append", record: {text, provenance:
  SourceRef}, interpretation: null|{text, author}, observations: [observation
  ArtifactRef]}`. Each effect needs a unique request `id`; ensure the target's
  parent exists and observe the target before writing. Retain the returned
  postimage and effect evidence.

Each operation used for a 3.0.1 claim needs an established compatible contract.
Reading opaque bytes under an honest legacy acquisition contract makes only that
acquisition claim; it does not upgrade a lifecycle profile.

## Verification effects stay within the grant

Actor-authored scratch files, shell redirection and deletion are effects even
when used only to verify a result. A temporary name grants neither territory nor
ownership. Never overwrite or delete fixed `/tmp` paths as a verification
shortcut. Without a scratch grant, compare bytes or hashes in memory and use the
retained native observations and write receipts; stdout or stdin need no request
file. A separately granted scratch location remains usable after checking its
current ownership/preimage and the scope of creation, use and cleanup. Deleting
a file does not undo an overwrite or authorize the earlier effect.

## Acquire only the deciding context (SK-05)

Acquire the deciding Product, requirements, scenarios, frame, and owner material
through the declared source routes, plus the specific sources your change
touches. Retain each acquisition's evidence id. Keep in the working context the
exact outcome, subject/basis, material relations, authority, required evidence,
capability limits, return consumer, and invalidators. Equal candidate bytes do
not erase a differing retained assessment, an unresolved obligation, or a
currentness fact — those still require different handling. A sufficient task
context implies no general optimal-compression claim.

## When a tool fails (SK-04 discriminator, Q06)

- If an operation returns an **unsupported method** (for example native
  `results.conjoin`, which `tools.describe` lists as unsupported), retain the
  actual refusal and withhold the dependent claim. Do not relabel another path
  as the result.
- If an operation returns an **execution error**, retain the error and the
  unknown-effect state, withhold the dependent claim, and identify the next
  supported re-entry.
- Never replace a required tool result with an invented check, a narrative of
  intended calls, or an unqualified alternate path. Independent useful work may
  continue within the grant, but the blocked claim stays blocked.

## After an uncertain effect (Q08)

If an effect's completion is uncertain (timeout, interrupted acknowledgment),
reconcile by re-observing the target before any retry. A repeated request must
not duplicate an uncertain effect, and a timeout does not prove rollback. See
`stdo-continuation`.

## Method sources (cited, not reproduced)

Within `stdo://releases/v3.0.1-rc.1/standards/`: `ACTIVATION.md` section 2 and
`REFERENCE_FRAME.md` sections 3 and 11 for context sufficiency, currentness, and
acquisition; `ACTIVATION.md` section 3 and `AXIOMATIC_CALCULUS.md` sections 5 and
7 for result, effects, and disposition; `ASSURANCE.md` sections 7 to 9 for
actual-path proof semantics.

## Scope and limits

Tool harmonisation is owned by a_c; this skill consumes supported contracts and
reports defects, it does not fork tool semantics. Output availability from an
operation is not semantic acceptance of the result.
