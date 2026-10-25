# F_P grounding repair

`code/ac_repair.py` is a separate, optional F_P construction-support profile,
`a_c.grounding.f-p-repair/1`. It preserves the expensive source-authored statements
and requests small patches when a draft's grounding has a misspelled section ID,
paraphrased quotation or incorrect source range. It does not alter the frozen
source generator, initial author schema, F_D normalizer or their evidence gates.

Selecting another source section is a semantic evidence choice and can change
source-derived record identities. A successful repair therefore creates a **new
proposed interpretation with invariant non-grounding statement bytes**. It does
not prove semantic equivalence, fidelity, completeness or acceptance.

## Scope and F_P responsibility

Only mechanically invalid entries in the parent's existing five record-family
grounding arrays are eligible. A patch identifies a known family, exact record
key and existing grounding index, and replaces only `section_id`, `quote`,
`start_line` and `end_line`. Strict-valid anchors remain fixed. New/deleted or
reordered grounding entries, records, keys, populations, statements, conditions,
exceptions, relation endpoints, residual meaning, dispositions and limitations
are outside this profile.

The F_P actor receives the complete immutable parent draft, all current invalid
grounding diagnostics, the exact same dispatched source chunk and the same bounded
Graphify discovery cue for graph treatments. Direct treatments receive no graph
cue. Parent content, source, embedded prompts and diagnostics are explicitly DATA.
No private assessment oracle, review answer, external source or additional file
enters the repair prompt. The actor must refuse if the unchanged statement lacks
support in this exact source or needs a substantive rewrite. Choosing a merely
related quotation to satisfy a checker is explicitly prohibited by the prompt.
Mechanical validation cannot establish whether the F_P actor followed that semantic
instruction; independent source-based assessment remains necessary.

The closed output schema contains only a patch list or explicit refusal, reasons
and limitations. Preparation expands its replacement `section_id` into an enum of
the exact supplied source-section IDs and its target keys into an enum of invalid
record keys. This prevents another opaque-ID transcription error without choosing
which evidence is appropriate. The fully expanded schema is retained, hash-pinned
and recomputed from the exact chunk during verification. The initial author schema
is unchanged.

## Parent custody and patch chains

An original parent must be the latest completed original author attempt and pass
the unchanged `ac_grounding.evidence` custody gate, including its exact initial
author prompt, settings, schema, source, isolation, usage and recorded failure.
There is no exception to that exact-author-prompt rule. The repair actor has its
own prompt, schema, profile and evidence verifier.

Before spending a repair call, mechanical preflight rejects known non-grounding
defects in keys, endpoints, attachment subjects and disposition shape/coverage.
Every proposed patch must target an invalid existing entry once, select a supplied
section and quote exact source at an exact range. Canonical JSON comparison masks
only the four grounding fields and proves every other value and array position
unchanged. The complete unchanged `author_check` remains decisive.

A repair with full strict success has status `complete_patch`. A scope-valid patch
that leaves other mechanically invalid grounding has status `incomplete_patch`,
with the recomputed whole-draft error and remaining invalid-anchor list. Such a
draft is only an audited input to a later repair call; it cannot enter a complete
assembly. A whole-draft failure with no invalid grounding left is an unsupported
consistency defect, not an incomplete grounding chain. It refuses as an invalid
patch. The actor may also return an explicit `refuse` decision.

Each child request pins its parent repair journal and derived bytes. Verification
replays the chain to the immutable original author draft, checks every distinct
actor's evidence and usage, reapplies every patch, recomputes failure states and
proves non-grounding invariants at each step. Cycles, changed parents, source,
schemas, code, raw actor files, derived meaning or witnesses refuse. Refreshing
a changed draft's hash does not establish a valid repair.

## Shared call ceiling and execution

The total per-chunk F_P ceiling is **three**, shared by original author attempts
under `actors/author/CHUNK/` and repair attempts under
`grounding-repairs/CHUNK/`. Failed and unfinished attempts count. A prepared repair
directory reserves one of these slots, conservatively preventing a fourth call;
reservation is not reported as backend token usage. The inventory's
`invocation_recorded` field reports whether the corresponding invocation file is
present, without inferring model execution or billing from it.

Preparation, execution and all assembly selections check the same combined
namespace, including strict-original and explicitly excluded chunks. Pending
repair reservations block another repair preparation for that chunk. Root
scheduling owns the separate global ceiling of four concurrent model calls;
this helper does not independently dispatch or retry batches.

`execute` uses unchanged `ac_generate.run_actor`, with the frozen original model,
settings and CLI version. It retains a separate repair invocation, prompt, expanded
schema, events, stderr, actual usage, patch response and raw CLI result. The repair
verifier checks the actual argv, ephemeral read-only sandbox, empty workspace,
disabled tool/document/MCP scope, event item types, usage and artifact hashes. A
separate repair journal records patch application and whole-draft validation; raw
CLI results and original author failures are never relabeled. Time and actual
reported usage remain distinct, with no inferred price or invented discount.

## Artifacts and API

`prepare` creates a fresh immutable `grounding-repairs/CHUNK/attempt-NNN/` containing
the request, parent draft, exact custom prompt and expanded patch schema. `execute`
adds `actor/`, optional `derived-answer.json` and `journal.json`. It never overwrites
an existing attempt. Failed original and repair calls remain part of the evidence
and cost of obtaining the final proposed draft.

From `a_c/`:

```sh
.venv/bin/python build_tenants/graphify/code/ac_repair.py prepare --output RUN --chunk CHUNK
.venv/bin/python build_tenants/graphify/code/ac_repair.py execute --output RUN --attempt ABSOLUTE_ATTEMPT --codex /Users/jim/bin/codex
.venv/bin/python build_tenants/graphify/code/ac_repair.py verify --output RUN --attempt ABSOLUTE_ATTEMPT
.venv/bin/python build_tenants/graphify/code/ac_repair.py assemble --output RUN --upstream UPSTREAM
```

The coordinator can import:

- `prepare(output, chunk_id, parent_repair=None) -> absolute_attempt_path`;
- `execute(output, attempt, codex="codex", timeout=1200) -> journal`;
- `verify(output, attempt, require_complete=True) -> (draft_or_none, journal)`;
- `assemble(output, normalization_name="normalization", allow_partial=False,
  upstream=None) -> result`.

`prepare --parent-repair ATTEMPT` selects an audited incomplete predecessor.
`verify --allow-incomplete` verifies a draft or refusal for coordination, without
qualifying a complete model. Execution is explicit; the module launches no actor
from preparation, verification, assembly or import.

Assembly accepts strict originals, independently verified F_D grounding drafts or
complete verified F_P repair chains. It preserves exact source/model/signature/
selection-ledger and repair provenance, then uses the unchanged adapter and codec.
Both graph treatments build/export through actual pinned Graphify and recover the
exact repaired model. Output goes to separate `repaired-proposal/`. Explicit
`--allow-partial` excludes retained failed/refused/incomplete repair scopes or F_D
refusals into `repaired-partial-proposal/`, with refused source dispositions. It
never ignores corruption of supposedly successful proofs or changed source/schema.

Tests use synthetic actor artifacts and no model calls. They cover scope, exact
expanded schemas, invariant statements/dispositions/order, shared budgets,
unfinished calls, replayed incomplete chains, explicit refusal, failed usage,
tool-isolation violations, tampering despite hash refresh, F_D integration, partial
scope and actual pinned-upstream carrier recovery. They do not establish semantic
fitness or owner acceptance of repaired interpretations.
