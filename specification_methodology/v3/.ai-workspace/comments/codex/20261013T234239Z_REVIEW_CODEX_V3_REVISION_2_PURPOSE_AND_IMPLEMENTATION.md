# REVIEW: Codex v3 revision 2 — purpose and implementation

**Author**: Dimitar Popov
**Date**: 2026-10-13T23:42:39Z
**Addresses**: STDO v3 purpose and the second Codex synthesis candidate, source `9bc8962e44aff2cd1dc29a9bac95356cdccf7cdd`, evidence `3ad1fca31dc93ba0847bbbbf308312a554daa1f6`
**Status**: Open

## Summary

The revised implementation has a coherent purpose and a substantial realization of it. It gives finite actors a shared contract for acquiring current state, performing bounded work, preserving dependencies, combining judgments and continuing after interruption. Those contracts now reach the deciding operations in the sampled method families. The separation of predicate, evaluation performance, domain outcome, effects and authority is the strongest part of the revision.

**Verdict: retain this core design; request three contained corrections to its entry material.** I found no architectural blocker in the inspected core and consumer paths. This is a credible construction candidate, with incomplete product qualification. The complete formal interpretation, ordinary installed-v3 use, categorical acceptance instance and member acceptance are still open. Another general rewrite is not justified by these findings.

This review assesses v3 against its own purpose. It does not compare tenant candidates, rate v2, accept C3 or authorize a release.

## Subject, provenance and review boundary

The assessor is this Codex session, based on the GPT-6 family, using the Codex client and local command tools. The exact backend model revision and this session's token/cost counters are not exposed. Codex is also the family that authored the subject. This activation did not author or repair revision 2. The user's express request supplies the reason for this same-family review; this is not a cross-family or blind acceptance review.

The conversation contains earlier review conclusions and summaries about both candidates. Memory was consulted for review-only and source-first working conventions. These are prior context, not evidence for the findings. Each finding below was checked against frozen source bytes. No peer candidate or concurrent peer review was opened for this review.

| Alias | Frozen subject and path prefix |
|---|---|
| G | `04b0c9a52b7c893ee792273babe0927da26e17f1:specification_methodology/v3/` — governing v3 purpose and requirements |
| P | `9bc8962e44aff2cd1dc29a9bac95356cdccf7cdd:specification_methodology/v3/build_tenants/codex/successor/` — candidate method package |
| E | `3ad1fca31dc93ba0847bbbbf308312a554daa1f6:specification_methodology/v3/build_tenants/codex/` — tenant design, interpretation and qualification evidence |

Citations below use these aliases plus exact file and line or JSON identity. Resolve them with `git show <commit>:<prefix><path>`; line numbers belong to the frozen bytes. `main` contains the older candidate, so reading the same candidate paths from `main` would assess the wrong implementation. The revised source and evidence checkpoints have identical `successor/` tree identity `c1a1363b9435f6a06ed3dd7fe88670a1dd107db7`. The common specification and Product Definition are unchanged between the build's selected common input `98102157321990bdc483cd1c37f83f2b7aa477b9` and G.

Repository inputs were acquired with `git show` or `git archive`. The installed builder verification returned valid for `v2.5.1-rc.2`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. Checks ran against an external scratch copy. No candidate, specification, ticket, installation or Git ref in a user repository was changed. The sole repository write is this commentary post, under a separately declared bounded Writer activation. No commit was made.

The semantic sample covers Foundations and Transformation Library, then selected deciding clauses in Spec, Frame, a_c, Design, Ticket, Release, the operational Baseline, ODD, Traversal, World Model and UX. Entry, compression and formal-model routes were also inspected. The package inventory and generated views received complete mechanical checks. This is not an exhaustive semantic assessment of all 80 members or 691 predecessor dispositions; those unexamined claims remain unassessed.

## Purpose and implementation assessment

V3's purpose is sufficiently concrete to assess. Its destination is a method for software and processes, with shared laws, bounded context and attention, explicit execution bindings, a formal interpretation and separately demonstrated categorical claims. The implementation should make lawful work and truthful continuation possible without depending on an actor's private memory. Merely adding mathematical vocabulary would not deliver that outcome. Sources: G `specification/INTENT.md:5–33`; G `specification/PRODUCT.md:35–76`.

| Purpose | Implementation inspected | Assessment and practical consequence |
|---|---|---|
| Foundational explanation with declared policy choices | P `standards/FOUNDATIONS.md:53–83,643–654`; P `standards/TRANSFORMATION_LIBRARY.md:59–141`; P `standards/DESIGN_MODULE_METHOD.md:5–30` | The premises, conditional consequences and additional choices are distinguishable. Finite resources do not purport to derive purpose, grants, domain policy or a unique hierarchy. This is a defensible foundation for the sampled contracts, not a theorem covering every clause. |
| Persistent work with disposable context | P `standards/FOUNDATIONS.md:532–581`; P `standards/SPEC_METHOD.md:1297–1306`; P `standards/TICKET_METHOD.md:815–845`; P `standards/RELEASE_METHOD.md:224–231` | The actual consumers reacquire current state, preserve a selected frozen basis, retain valid independent work and reconcile uncertain effects before dependent retry. Current observation does not silently rewrite a requirement. These distinctions support useful recovery. |
| One shared result contract | P `standards/FOUNDATIONS.md:296–530`; P `standards/REFERENCE_FRAME_METHOD.md:433–468`; P `standards/AXIOMATIC_CALCULUS.md:427–471`; P `standards/SPEC_METHOD.md:1681–1717` | Undertaking an evaluation, reaching a conclusion and observing an effect are separate. Known failure survives missing coverage. Availability, fitness and disposition remain different predicates. Sampled consumers apply the core at their deciding operations, rather than merely mentioning it. |
| Closure without false success | P `standards/TICKET_METHOD.md:915–937`; P `standards/RELEASE_METHOD.md:250–270`; P `standards/ODD_METHOD.md:1194–1226`; P `standards/WORLD_MODEL_METHOD.md:1092–1101`; P `standards/UX_METHOD.md:320–331` | A lawful rejection or yield can be successful as a decision without making the product fit or complete. Sparse evidence does not erase a failed admission obligation. Domain distinctions survive the common algebra in this sample. |
| Human, machine and mixed realizations | P `standards/SPEC_METHOD.md:824–859,1000–1030`; E `design/DESIGN.md:3–22` | Operations, composition, effects, assumptions and evidence belong to an explicit tenant binding. Human participation does not automatically make an operation adjudication. The tenant supplies a mixed construction process. The aggregate compression still needs the correction in F3. |
| Roles proportional to task and assurance | P `standards/FOUNDATIONS.md:618–641`; P `standards/STDO_REFERENCE_FRAME_BASELINE.md:1310–1315`; P `plugins/spec/skills/stdo-work/SKILL.md`, Construct And Prove | Direct work remains available where one sufficient frame and grant suffice. Coordination and required independence are conditional. This supports the purpose without imposing one organizational form on all work. |
| Formal representation and categorical direction | P `standards/FOUNDATIONS.md:236–268`; E `qualification/C3/synthesis/a_c/program.json`, its three residual identities; E `qualification/C3/synthesis/a_c/model.py` | The demonstration standard is stated, and a bounded interpretation is implemented. Full formal coverage and a worked categorical join are not delivered yet. Structural validity is correctly kept separate from semantic proof. |

For the source-level result and recovery review I used these concrete cases: a performed but inconclusive load test; an absent planned return; a failed required assessment with separate uncovered coverage; an admission refusal versus downstream fitness; a candidate available but unfit; a lawful rejection; a lost acknowledgment with non-idempotent effects; deployment followed by rollback; stale context disagreeing with a selected subject; and a human procedure realizing the same requirement as software. The inspected source preserves the required distinctions. This is logical review, not an executed proof of every consumer or a fresh-actor usability result.

## Findings

### F1 — Moderate: the compression guide denies the standing of the new core owners

P `standards/authority_compressions/README.md:7–9` says that Foundations and the library are “non-deciding explanations”; lines 58–60 repeat the explanatory characterization. This conflicts with P `standards/FOUNDATIONS.md:55–56,296–530,643–651`, which owns the foundational commitments, result record and conjunction, and P `standards/TRANSFORMATION_LIBRARY.md:3–11`, which owns shared conditional contracts. The standards index itself correctly identifies those owners at P `standards/README.md:14–22`.

A reader entering through the compression guide receives an incorrect answer to the question “which clauses decide the common result and recovery obligations?” This matters directly to the single-ownership and ownership-and-use requirements; the issue is the advertised standing of governing law, not a preferred wording. The guide cannot override its sources, but its contradictory instruction impairs acquisition.

**Smallest correction:** distinguish the non-deciding projections from their deciding source owners; retain genuinely explanatory passages at their actual standing. Check both README passages against the source and the bootstrap. The mechanical package check currently passes despite this contradiction, so digest refresh alone is not a verification.

### F2 — Moderate: the declared a_c entry selects the previous interpretation as current

G `stdo_3.json`, `/how/build_tenants/0/implementation`, locates `build_tenants/codex/a_c/`. E `a_c/README.md:3–7` labels the old six-clause program and 608-case token check under `qualification/C3/a_c/` as the “Current C3 interpretation”. Opening that source confirms the old two-token fixture and its selected qualitative relations. It is not the rebuilt interpretation of the new result/context contracts.

The actual revision-2 interpretation is under E `qualification/C3/synthesis/a_c/`: its program has 53 clauses, and its source inventory binds the revised package. E `qualification/C3/synthesis/AC_RETURN.md:41–55` explains that subject. The general C3 return routes correctly to the synthesis, but the direct formal-implementation entry does not.

A consumer following the Product Definition's formal-implementation route can inspect and validate a historical model while believing it is the current interpretation. No such consumer outcome was executed here; the wrong selection is established directly from the route and target bytes.

**Smallest correction:** update the tenant's a_c landing page to identify and link the exact current program, signature, bindings, source inventory and qualification boundary. Mark the earlier six-clause interpretation historical. Relocation of all evidence or a new common Product Definition is unnecessary if the existing entry locates the correct subject.

### F3 — Low: the aggregate authority flow still presents the software-only chain as universal

P `standards/authority_compressions/stdo_compressed.md:271–278` presents `Design -> Code -> Events` without a software-specific qualifier. Its source owner now states `Design -> Realisation -> Observations`, explicitly including a human procedure and making events a selected durable carrier: P `standards/SPEC_METHOD.md:1000–1030`.

The difference matters to the explicit v3 purpose of supporting human and mixed processes. An ordinary compressed reader is given a narrower construction model than the owner. The raw source is correct, so this is a projection defect with a straightforward workaround: re-enter the owner.

**Smallest correction:** project the broadened chain and retain code/events as its software specialization. Check the meaning as well as the digest. This finding was independently verified against both frozen passages; a prior ticket summary also mentioned this discrepancy.

## Qualification still needed

These are incomplete product claims, separate from F1–F3 and from any allegation that the construction return claimed acceptance.

1. **The formal interpretation covers selected laws, not the whole promised method.** I inspected the actual 53-clause program, its consumption relations and `core-coverage`, `family-coverage` and `semantic-proof` residuals. The finite code implements selected result, refinement, effect and recovery cases; its recovery function takes already-established effect, idempotence and grant facts. It does not acquire or authenticate real workspace state. E `qualification/C3/synthesis/a_c/SOURCE.md:128–152` and `AC_RETURN.md:99–113` accurately expose this boundary. Product purpose includes the method's formal interpretation (G `specification/PRODUCT.md:5,25,68`), so complete realization and fidelity cannot be inferred from the green checker. The next work is source-to-interpretation coverage and independent fidelity for the accepted claim set. A production workflow engine is not required by this gap.
2. **Ordinary v3 use and exact result handoffs remain unqualified.** The current work skill requires the verified selected basis: P `plugins/spec/references/PRODUCT_BASIS.md:24–40` and `plugins/spec/skills/stdo-work/SKILL.md:14–51`. The retained ordinary-entry fixture selects rc.2, and the actor therefore used rc.2 owners; E `qualification/C3/synthesis/entry/bound/RETURN.md:83–118` accurately says this. That is a truthful basis selection, not a reason to weaken the guard. The frozen-frame trials support bounded behavior, but some raw C2/C3b/C5/C6 results leave effect values or the evaluated procedure ambiguous. I inspected those raw returns, not only their grading summary. Because the core is a semantic contract rather than a mandatory JSON serialization, free prose alone is not an error; it must nevertheless make the material coordinates unambiguous. Re-test ordinary entry, cold continuation and result consumption on one truthfully selected immutable v3 qualification installation, with independent expected outcomes and no manual normalization of the actor's result.
3. **Categorical capability remains a direction with a stated proof obligation.** P `standards/FOUNDATIONS.md:245–268` specifies what categories, functors, approximations and the worked join must show. It does not provide the method's accepted categories or worked algorithm/computation join. G `specification/PRODUCT.md:103–119` explicitly leaves selection of the steel thread open and requires it under the installed builder before evidence-driven amendment. This does not block recognizing the source candidate as constructed. It blocks claiming that the complete categorical capability has been demonstrated.
4. **Member acceptance remains unassessed here.** All 691 author disposition coordinates resolve, but that is not independent semantic acceptance of 691 claims. This review does not supply all C3 per-member criteria, imported-part acceptance policy or release qualification. G `specification/PRODUCT.md:358–371` retains those conditions. No missing observation is scored as a missing implementation.

## Reproduced evidence

The following commands ran on an archived scratch copy, with the source and evidence checkpoints available read-only through a scratch Git object reference. No paid actor was started; existing actor proposals were replayed, not regenerated.

| Check | Observed result | What it establishes |
|---|---|---|
| `check_artifacts.py --idempotence` | Pass: 80 package members, 691 mapped rows, 553 local links, 89 exact excerpt sections in six views, 32 compression pins; isolated regeneration unchanged | Inventory, coordinates and projection reproducibility; not meaning preservation |
| `synthesis/a_c/qualify.py` | Pass: 53 clauses, 14 symbols, five frame indexes; native checks and bounded finite suite reproduce | Selected structure and finite-model consistency; not whole-method fidelity |
| `derivation_material.py --test` | Pass: 14 historical references, three reconstructed members, 19 rejected negative controls; six package data reads and zero outside-package/network reads within the audited verification boundary | Package-contained historical identity verification on the hypothetical publication fixture; not an issued release |
| Retained `use-77` proposals through `apply_and_check.py` | Ten applications; 81 host checks met, two unmet; 21 subprocess executions | Reproduces the retained D1 failures and the other tested behavior. The command correctly exits nonzero. These actors used `77f2efb`, not the final source cut. |
| Explicit D1 hard-cut successor at `9bc8962` | One application; 11 checks met; six subprocess executions | The separately clarified task passes; it does not erase the original failures |
| Independent replay of D1 guard/consumer counterexample | Four commands: old shell guard reports `ok` while Python reads an empty token; corrected guard rejects that environment | Confirms the concrete fixture defect and the narrower successor behavior |

Artifact and identity checks initially encountered a missing `jsonschema` package in the generic Python interpreter. Re-running with the recorded STDO toolchain interpreter `/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python` completed them. This was an assessor-environment mismatch, not a candidate failure. No dependency was installed.

Scratch evidence is retained at `/tmp/stdo-v3-independent-i8_uvcu5/`; `REVIEW_EVIDENCE_MANIFEST.json` records the seven new report digests. Key report SHA-256 values:

- Artifact check: `89318c67ad778d5859323a3c1fb6c0c3e457419ef1074a79f2553fa886be209b`.
- a_c mechanical check: `f057a79b9bd9dd1df7840dd27127ef95da9003c26ccdf18b56ff3a00b9f6323c`.
- Finite interpretation check: `26601b3f7437cfa7f5ab30bd2dbe7e662cd63d554f847e0049359736cc281f1d`.
- Identity verification: `912e01881519912727c91e731431405e855d1db1dfd12d74d4711786d14533d4`.
- Ten-case replay: `dc3c2fa35c315b2141536ee78c960ac989c4146558fab1362bc64485b5a7f2fe`.
- D1 successor replay: `33486e3f33d9ea7f7dbd5e130c62d9a0a40ad3094ec3b1bf56285deb115e65d0`.
- Additional guard check: `08ea73119d0aa0c08d5bb49a3dafd29cdae9bc1e2fd2d52482ed8f3eeee3c127`.

The finite suite's many enumerations overlap and mostly share author-owned expectations; they are not a count of independent semantic proofs. Existing live-actor evidence has its original actor-family and subject limitations. This review adds independent source inspection and host execution, not a new cross-family robustness experiment. New probe spend: **USD 0**. Session usage is unavailable.

## Recommended action

Keep the foundation/result/context architecture and its deciding consumers. Correct F1–F3 in one bounded change, then check the affected routes semantically; the current green artifact suite misses all three kinds of drift. These are small documentary repairs, an estimate rather than measured implementation cost.

For substantive completion, select the already specified categorical steel thread, derive amendments only from causally attributed findings, and complete the affected interpretation and fidelity checks against that frozen successor. This tests whether the categorical direction contributes usable construction law. It should not become another general vocabulary expansion.

Qualify that unchanged candidate through ordinary v3 entry and a persisted partial-work continuation. Require the returned predicate, actual evaluation performance, effects and missing coverage to survive a later actor's consumption. Keep member acceptance and release decisions separate from these bounded experiments. The remaining semantic-review and experiment effort is **unknown** from this review; artifact and fixture rerun times do not estimate it.

The recommendation is to finish and test this implementation against its purpose. The source findings do not justify replacing its core design or restarting the two-tenant comparison.
