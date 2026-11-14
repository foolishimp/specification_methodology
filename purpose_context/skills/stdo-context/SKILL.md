---
name: stdo-context
description: Use Purpose Context to reuse an exact purpose index for STDO code constraints or SDLC work and QA decisions, or construct one from selected source when no eligible index exists.
---

# Purpose Context

Use an existing matching purpose index before constructing a new one. Purpose
Context owns this skill, runtime and [catalog](indexes/CATALOG.json); STDO Skills
supplies host bindings. The helper uses Python 3.11+ and the standard library.
It invokes no model and needs no representation or provider runtime.

Resolve the actual Product/task, selected source and existing work grant. The
reusable corpus names governing source; target Product, task and grant are caller
coordinates. An index supplies constraints, not task authority or correctness.
When source-first independent review is required, derive obligations from eligible
source before opening candidate-derived indexes or judgments.

For ticketed work, bind the current ticket after your own control intake. It is
the durable work-state reference; use its admitted scope, linked authority,
evidence, residuals and next action to construct this task's context. Where the
selected law permits another work carrier, use that sufficient carrier. The
ticket does not override governing law or contrary current evidence. A generated
context, handoff or chat summary is a disposable account, not a second truth store.

Acquire only the material relations needed for the next decision, with qualified
resolvable source/evidence references. Follow the selected method's context
envelope and acquisition rules. Where a context capacity is declared, measure
the selected material in its declared unit and boundary before reading it and
record the comparison; a delivered body's byte count does not measure all
host-supplied context. Keep that measured fit separate from whole-step fit and
adequate attention. Insufficient fit requires a lawful bounded route, never
silent omission of material obligations. No universal capacity measurement gate
is introduced. Before resuming or reusing, reacquire relevant actual state and
check invalidators. Missing conversation history is not evidence of undone work
or an absent effect; reconcile uncertain completion and an unestablished effect
end sufficiently before repetition or dependent action.

## Choose the purpose

| Actual decision | Read this usage reference |
|---|---|
| SDLC work, ordinary QA, triage/re-entry, repair verification, named boundaries or evidence reuse | [SDLC workflow](references/sdlc-workflow.md), purpose `sdlc-workflow/1` |
| Preconstruction constraints for pure/local Python 3.12 refactoring under adopted DESIGN_MODULE, including conditional ODD/UX law | [Python refactoring](references/python-pure-refactor.md), purpose `python-pure-refactor/2` |
| A different source or purpose with no eligible catalog entry | The construction path below, when authoring is within the work scope |

Read the relevant recipe, not every purpose reference. Different claims in one
task can need both purposes; keep their queries and coverage separate. No entry
covers all builds, Product-specific law or STDO 3.* releases.

## Reuse and apply

Use the physical `scripts/context.py` as `<cli>`. Host aliases resolve the same
physical Product; STDO Skills forwards arguments through `provider.py context --`.
A portable copy retains every file selected by `PUBLIC_MANIFEST.json`. Obtain
`<public-sha>` from the independently selected dependency binding; hashing an
arbitrary replacement does not select it.

1. Run `python3 -B <cli> indexes --public-manifest-sha256 <public-sha>`. Match the
   actual source/method, ordered members, purpose and family guard. An older
   consumer uses its exact matching entry. The 3.1 release-target entries bind
   the caller's actual native cut. The retained SDLC development projection is
   separately selected alongside the complete operative constitution.
2. Follow the selected recipe to bind actual source bytes and write `QUERY.json`
   as `{id, purpose_id, facts}` using that purpose's declared meanings. Observed
   adoption/scope facts are not values copied from a fixture. Missing, null or
   wrong-type deciding facts remain unknown; never assert future verification.
3. Select and consume through the same runtime. False family applicability refuses;
   unknown applicability reports `incomplete` (exit 3), with no selected delivery.
   Material source or purpose drift requires owning-source re-entry, not a newer
   label or an invented fact.
4. Supply an applicable external assessment for the exact canonical index, corpus
   and complete query, or retain an authorized trial binding where permitted.
   Trial use reports `covered: false`; without either, use is withheld. These
   states do not replace the task's actual assessment or acceptance requirements.
5. Check the actual JSON and Markdown against the same independently supplied
   inputs, assessment/trial binding and recipient byte budget. Overflow refuses
   the whole body. Recover clipped windows and establish actual receipt before
   relying on native consumption; saved output alone is insufficient.

Apply the constraints through the native work/review workflow. Keep the exact
outcome, subject, basis, scope and decision boundary. The SDLC default routes
causal findings to their owner and verifies affected claims before continuation
or closure, retaining valid support and required independence. It does not make
another full review round automatic. Unknown coverage requires source inspection
and an explicit limit; it does not invent an approval gate for otherwise lawful work.

## Construct when no eligible index exists

For a different selected corpus or purpose, use the same engine. Write `SOURCES.json` with `subject_id`, `method: {uri, manifest_sha256}` and `files: [{id, path}]`; paths are absolute or relative to that file. Write `PURPOSE.json` with `id`, `description`, and `facts` mapping names to meanings. Verify the caller-selected method through its applicable resolver. Generic preparation pins the supplied identity and actual selected source bytes; it does not independently authenticate arbitrary method URIs.

Run `prepare --sources SOURCES.json --purpose PURPOSE.json --out context-work`, then read `context-work/AUTHORING.md` and the [authoring contract](references/authoring.md). Use `catalog`, `search --text TEXT` and `read --source ID` with `--bundle context-work`; follow cursors and read deciding conditions, exceptions and dependencies. If the host clips a response, reduce pages and recover actual missing windows. Saved output alone does not prove receipt.

The current session authors `INDEX.json` under the [schema](references/index.schema.json), then runs `validate --bundle context-work --index INDEX.json`. Retain failed attempts. Build with `build --bundle context-work --index INDEX.json --query QUERY.json --trial-binding <existing-authorized-scope> --byte-budget <recipient-bound> --out delivery`. Check with `check --bundle context-work --index INDEX.json --query QUERY.json --trial-binding <existing-authorized-scope> --byte-budget <recipient-bound> --context delivery/CONTEXT.json --markdown delivery/CONTEXT.md`. A new catalog entry is an explicit Product change with exact assets and scope; do not relabel the initial index or widen its family in place.

Mechanical validity is distinct from source-semantic adequacy. `covered` stays false without a separately selected assessment bound to the exact index, corpus and query; material unknowns still prevent it. `--assessment FILE` carries that judgment to consume/build/check. Do not manufacture a supported assessment to enable use. Required independence and approvals come from the governing contract. For an assessment governed by the indexed STDO bases, EVALUATION §3 retains authorship and evidence independence and defaults same-model-family semantic judgments to non-independent unless the governing policy establishes otherwise; a fresh session alone is insufficient. This is the selected STDO rule, not a new default imposed on unrelated generic source corpora. Existing authorized experimental use may carry `--trial-binding`; without it or an assessment, use is marked `withheld`.

Return the selected source/method/purpose/query and exact index/context identities,
actual check and coverage standing, remaining decisions and the native task's
next action/owner. Distinguish governing-context coverage from task admission,
verification, acceptance and release. Report only observed outcomes.

Pass those results to the existing ticket or other authorized work carrier through
the native workflow. The granted Writer preserves step-produced facts, evidence
links, decisions, unknown effects and continuation state before handoff; invoking
this skill adds no ticket-edit authority. On restart, reconstruct from that current
record and the workspace, rather than requiring the previous actor's private context.

For release-target authoring and final-cut packaging, follow the
[method-target policy](references/method-targets.md). It separates the latest
selected semantic source, construction basis and actual caller basis. Preserve
historical entries and applicable evidence; a new release label transfers no
assessment. SDLC requirement-led regeneration is in its
[rebuilding guide](references/sdlc-workflow.md#source-led-rebuilding).
