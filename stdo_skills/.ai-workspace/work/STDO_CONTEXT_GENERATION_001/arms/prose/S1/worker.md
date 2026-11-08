# S1 proposed direct Writer context

**Status: proposed, with fictional execution bindings pending. Do not execute this exercise.** This file is the requested Worker-shaped context for the direct Writer allowed by S1-11. The task is one run-local implementation repair, not a separate coordinating activation. Apply the exact released `stdo-work` skill W if an authorized future execution is bound.

## Task, law and subject

Starting from fictional source cut `seed-r7`, produce a repair candidate for `/fictional/seed-context/candidate/context_select.py` and its focused tests. Upstream requirement and design `D-seed-2` remain unchanged (S1-01, 08). The owner reports that the present helper omits unresolved records, slices the reachable records to the budget, and reports complete; verify that report when execution is actually admitted. Do not report it as your own observation (S1-03).

`select_context(records, roots, budget)` accepts a finite list of uniquely identified records, a root-ID list and a nonnegative integer budget. Each record has a nonempty string `id`, a `requires` list of IDs and opaque JSON-compatible fields. Malformed types and duplicate record IDs are excluded (S1-02).

Preserve these exact requirements (S1-04–07):

- Success is exactly `{status: complete, records: [...]}` with the whole finite transitive dependency closure, each complete record once, sorted by ID. Preserve every payload field and all inputs. A required record's `standing` never removes it.
- Unknown roots refuse with reason `unknown_root`. Dangling references anywhere in the supplied graph, including unselected records, refuse with `dangling_reference`. A distinct full closure larger than budget returns exactly `{status: refused, reason: budget_exceeded, records: []}`. Precedence is unknown root, then dangling reference, then budget exceeded. The brief does not specify additional envelope fields for the first two refusals; retain their explicit reason and do not invent authority for extra success behavior.
- Valid cycles and duplicate paths are supported. Empty roots and budget zero return complete/empty only if the entire graph is valid. For A requiring B and C, C's unresolved standing still requires all three records and budget at least three.

Use accepted `D-seed-2`: finite visited set and work queue, followed by materializing full records. This is not an assessment of record standing and cannot change record meaning. A defect under this unchanged law is a repair, not requirement/design repricing.

## Acquisition and effect boundary

The fictional grant is S1-10: read this brief, `/fictional/seed-context/specification/requirements.md`, `/fictional/seed-context/design/D-seed-2.md`, and `/fictional/seed-context/candidate/context_select.py` plus `/fictional/seed-context/candidate/test_context_select.py`. Edit only those two candidate files, perform focused in-memory Python checks, and write `/fictional/seed-context/work/run-8/RETURN.md`. No other project, Git, network, installation or publication operation is granted. Do not infer wider reads from narrower writes or a tool's availability.

Before hypothetical effect, bind the exact Product/control selection, basis verification, capable actor, run contract identity/digest and its admission mechanism/authority/decision/evidence. The brief does not supply those receipts. This draft supplies no admission; preserve S1-10's existing owner grant without inventing or automatically creating a ticket. If a required binding cannot be resolved inside its authorized route, return the missing condition to the owner without execution (A Admission; R activation packet). No fictional path has been accessed in this generation exercise.

## Proposed proof and return

Derive focused checks from the requirement and design: unresolved dependencies; full records including arbitrary payload fields; stable input values; exact success and budget refusal structures; dangling references outside the selected subgraph; valid cycles and multiply reached records; budgets around exact distinct-closure size; empty roots/budget zero; and multi-error examples establishing refusal precedence. These are suggestions for falsification, not a prewritten result. Reconcile actual implementation and tests with the complete requirement. The old smoke result at `seed-r7` covers only a resolved dependency-free root and proves none of the missing repair cases or successor currentness (S1-09).

Return to the fictional owner through `/fictional/seed-context/work/run-8/RETURN.md`: exact candidate identity and predecessor, changed paths, unchanged governing requirement/design, execution admission binding if execution occurred, checks actually run with their observations, unevaluated coverage, residual uncertainty and the bounded work result. Use the core result meanings in F for evaluations; a planned check not performed has no result. Do not confuse the function's `complete` status with a satisfied work claim. Only evaluated, satisfied applicable conditions support bounded closure. Independent review is not required by S1-11, and no ticket is required for this run-local result.

Stop at that return. A missing evidence/authority condition withholds the affected claim; changed governing meaning re-enters its owner. Material input change, basis change or a declared revising observation invalidates the affected evidence before reliance; retain unrelated valid historical evidence with its exact scope. There are no external effects to reconcile and no release/adoption request (S1-12; A closed result/reuse).

The real author of this context has common-source and host-injected background exposure; no actual Worker was activated, measured or tested. A future actor must bind its actual inheritance and envelope rather than assume this document clears prior context.

## Qualified sources

`S1-nn` names the fact in `/Users/jim/src/apps/specification_methodology/stdo_skills/.ai-workspace/work/STDO_CONTEXT_GENERATION_001/inputs/S1.md`, SHA-256 `acd89137b657a7d0025ae98133721fcd3f3f91dd3c4aa99e0d133a9a38a774a4`. Fictional paths and cut labels are declared coordinates, never observed hashes. `M` is `/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001/store/releases/v3.0.5-rc.1`. Method basis: `stdo://releases/v3.0.5-rc.1/`, manifest SHA-256 `64c026667abba933d289317793dbe80b5f9ab822a9870307795584402e460e1c`.

| Short reference | Exact acquired source under M; SHA-256; selector |
|---|---|
| W | `plugins/spec/skills/stdo-work/SKILL.md`; `9dc06e03fd6f64483fa485ed55f35e414fefae472bb69aa930ecef9335585b35`; full file |
| V | `plugins/spec/skills/stdo-review/SKILL.md`; `b90b3a2014d7891e25b40c11e5f3638accb9f3408cb3f0cf3922d26f17bc57df`; full file |
| A | `standards/ACTIVATION.md`; `56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d`; Admission/Applicability lines 402–488, Roles and delegation 619–692, context construction 693–901, closed result/reuse 1681–1749 |
| R | `standards/REFERENCE_FRAME.md`; `4bf3bb18f8590b8096f5ff2de6554787d29a164224be697c76640289d2096d64`; activation packet lines 933–1011 |
| E | `standards/EVALUATION.md`; `b856cf04e2cf6ea0ba8b5f9de8b455a3a5f95cdb05fe7337f077f1b7547c7485`; independent assessment and review results lines 190–336 |
| F | `standards/FOUNDATIONS.md`; `7fe9ecf257ad9aa725e7ae87ba23e406f6993dbd143c429d53df06284023127e`; Results lines 732–805 |

The shared inputs and selected freeze authorize document generation only. The real release manifest and selected member hashes were checked locally. The installation's prior verification is supplied by BASIS.json; no current Product-definition verification, fictional admission, dispatch or task execution was performed.
