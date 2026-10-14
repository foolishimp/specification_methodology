# REVIEW: Claude v3 revision 2 — purpose and implementation

**Author**: Dimitar Popov  
**Date**: 2026-10-14T00:05:19Z  
**Addresses**: STDO v3 Claude candidate, `tenant/claude/c3-synthesis`, commit `768cf8c5915d23b2721f47e96ad196ffef7e05ec`; purpose, deciding rules, acquisition and qualification  
**Status**: Open

## Summary

Retain the candidate's foundational architecture, but require changes before accepting the revised implementation. It supplies useful laws for bounded construction, actor configuration, recovery, common results and human or machine realisation. These are implemented in the deciding members and in current task frames. This is substantive method work.

Two deciding rules still need repair. The frame-revision guidance can leave affected results closed when an activation or its evidence changes. The occurrence profile can classify a demonstrated failure as indeterminate solely because the effect's termination is unknown. The current a_c interpretation is also missing: the available models bind earlier member bytes. A finite conjunction check passes its own tests but misses an incorrect reported result; generated frames have a smaller navigation defect.

The candidate is a credible prose implementation in progress. It is not yet an accepted standalone successor, a qualified categorical construction method, or a complete prose-and-a_c product. Its handoff explicitly acknowledges unfinished acceptance and re-encoding; these are completion gaps, not concealed claims.

The common specification changed during this review. The new requirement for demonstrated foundational reduction strengthens the next construction task. I assess that change separately from defects in the frozen revision-2 subject.

## Analysis

### Scope, provenance and frozen inputs

This is the same purpose-and-implementation review requested for the revised Codex line, applied only to Claude. It does not rank the candidates, repeat the original cross-assessment grid, or constitute all-member C3 acceptance.

Assessor: Codex, GPT-6 family, Codex client. The exact backend model identifier and session token/cost counters are not exposed. Codex built the competing candidate, and the subject incorporates named Codex-origin parts. I therefore have a model-family interest and cannot count this review as author-independent acceptance of those ported parts merely because Claude integrated them. An owner-bound acceptance assignment must settle that boundary.

This conversation includes previous comparisons and opinions. A brief memory lookup supplied review conventions: inspect content first, freeze the revised subject, and separate structural checks from semantic qualification. None of those opinions or memories is evidence for a finding here. The tenant handoff and earlier findings served as leads; the findings below were checked against frozen source, raw results or reproduced checks.

Source coordinates used throughout:

| Symbol | Frozen input |
|---|---|
| S | Claude commit `768cf8c5915d23b2721f47e96ad196ffef7e05ec`, prefix `specification_methodology/v3/build_tenants/claude/` |
| G0 | Common specification at review entry, commit `04b0c9a52b7c893ee792273babe0927da26e17f1`, prefix `specification_methodology/v3/specification/` |
| G1 | Common specification observed during review, commit `c78de0d6794cc39b616d11f1c4ced80a3663da4b`, same prefix |
| B | Installed `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` |

A citation such as S:standards/ACTIVATION.md:1242–1254 means those exact lines at S, not whichever bytes later occupy the path. S's standards tree is `83b0af965c89097ae9a36c7474cd7c68a08c4b73`; its a_c tree is `cc1ec282a55b013f459a0731caa2e80b24ca930c`. The candidate's declared construction input was `a7eba66` (S:qualification/C3-SYNTHESIS/HANDOFF.md:7–14).

Repository content was acquired with Git into scratch outside the repositories. The installed baseline verification command returned valid with no failures. The Claude worktree was clean and its HEAD remained S. The main checkout advanced while I reviewed; I archived G1 separately and inspected the common-contract delta. I did not treat that advancement as permission to change the subject or as evidence against its earlier construction grant.

The semantic sample follows the shared owners into consumers: FOUNDATIONS, ACTIVATION, EVALUATION and REFERENCE_FRAME; SPEC_METHOD's build binding; PROFILES; occurrence result/effect mappings; design evaluation; release/adoption; bootstrap, templates and frames. It checks permissions, conditions, negative results, authority, basis changes and retained distinctions. This is not an exhaustive semantic comparison of every predecessor claim or every profile clause.

### Purpose and architectural fit

The candidate gives the method a coherent job: interpret an exact subject, select a purpose and contract, transform within authority, evaluate claims, and recover or conclude from current state under uncertainty (S:standards/README.md:9–14).

Several choices should survive further work:

- **The foundation distinguishes premises from consequences and choices.** The standing table and family index give readers a route from deciding rules to their premises. A reference is not itself a derivation, and an owner's policy remains a choice. This is useful discipline, although the 21-family index is not proof that every entry has been independently established. Sources: S:standards/FOUNDATIONS.md:339–348, 483–559.
- **The result core retains the question being answered.** The five values travel with the evaluated predicate and domain outcome. An unperformed evaluation has no result; producing a candidate does not establish fitness or acceptance. Conjunction retains known failures and distinguishes missing planned results from uncovered requirements. Sources: S:standards/FOUNDATIONS.md:671–774, 863–951; S:standards/ACTIVATION.md:677–714.
- **Bounded work does not imply a universal management hierarchy.** Configuration follows task dependencies, capabilities, authority and assurance needs. Direct work, peers and adaptive allocation are possible. Context size and actual attention are separate; overflow requires a lawful change of acquisition or allocation, or a truthful stop. Sources: S:standards/ACTIVATION.md:251–440, 466–543.
- **Recovery starts from durable material state.** A disposable actor account cannot reset the workspace. Valid independent work survives, changed material evidence invalidates affected reuse, and an uncertain external effect must be reconciled before dependent action. Sources: S:standards/ACTIVATION.md:1013–1137, 1233–1254.
- **Human, machine and mixed execution use the same binding relation.** The common requirements, computational calculus and concrete execution environment remain distinct. A faster plan cannot erase independence or a required human decision. Sources: S:standards/SPEC_METHOD.md:1626–1763; S:design/CONSTRUCTION_BINDING.md:43–86.
- **Categorical claims have an explicit proof boundary.** The formal fragment asks for objects, arrows, equality, identity and composition before claiming preservation. Exact refinement differs from bounded approximation; an end-to-end bound is required. H1 remains a hypothesis. Sources: S:standards/FOUNDATIONS.md:622–669; S:standards/ACTIVATION.md:851–916; S:standards/EVALUATION.md:246–319.

These distinctions reach consumers. For example, the design gate's not-applicable value satisfies the declared disjunction “meets the axiom or does not apply”; it does not establish actual conformance to an inapplicable axiom. That is a defensible predicate-specific refinement, rather than success manufactured from non-performance (S:standards/DESIGN_MODULE.md:1407–1454). The occurrence profile retains partial effects and re-entry obligations even when its core result is negative or indeterminate (S:standards/TRAVERSAL_OCCURRENCE.md:1023–1029).

The ordinary resume route now selects ACTIVATION's work-state and reuse law (S:standards/README.md:29). It does not route that entry to a qualification case's expected answers.

### Findings

#### F1 — High: unchanged declarations are used as a reason not to reopen affected results

**Source:** S:standards/REFERENCE_FRAME.md:858–874, especially 867–870.

The revision guidance gives clarification of an activation or acquisition of evidence without changing a declaration as an example of a non-material revision, then says it reopens no result.

Unchanged declarations do not establish that an evaluation is unaffected. FOUNDATIONS defines materiality by its effect on results, basis, evidence and authority; ACTIVATION explicitly invalidates affected reuse after a material input change or revising observation even when the subject's bytes are unchanged. EVALUATION likewise permits changed evidence to invalidate a verdict without changing the law. Sources: S:standards/FOUNDATIONS.md:60–61; S:standards/ACTIVATION.md:1242–1254; S:standards/EVALUATION.md:101–104.

The ambiguity affects actual use. Both frozen C3S-01 Task-B outputs withdraw or mark a wrong-family activation, then infer “non-material” and “reopens nothing” because no frame declaration changes:

- S:qualification/runs/C3S-01/TASK-B-r1/steps/TASK-B-r1.out.md:94–102.
- S:qualification/runs/C3S-01/TASK-B-r2/steps/TASK-B-r2.out.md:127–139.

Both outputs retain the counterexample/conflict and withhold closure. They do not demonstrate an unsafe acceptance. They do demonstrate the suspect rule being applied to the recovery decision.

**Consequence:** an actor can confuse “the frame definition needs no new coordinate” with “prior activation, applicability and result validity need no reconsideration.” That contradicts the candidate's recovery purpose.

**Smallest repair and verification:** separate frame-coordinate revision from result invalidation. A clarification can leave the frame definition unchanged while invalidating a misbound result. Test two otherwise identical cases: harmless explanatory metadata preserves reuse; changed admissible evidence or a wrong-family activation reopens the affected claims while preserving demonstrably independent work. This needs a local law repair, not wholesale work invalidation.

**Evidence:** source review plus independently inspected existing actor outputs.

#### F2 — High: unknown termination can mask a demonstrated failure of the intended effect

**Source:** S:standards/TRAVERSAL_OCCURRENCE.md:927–953 and 1307–1324.

The occurrence profile classifies a partial effect as falsified only when evidence establishes that the effect has ended. Every other partial effect is the unknown variant and maps to indeterminate. Its stated parent predicate is “the intended effect occurred.”

The parent law instead distinguishes evidence that the intended effect did not occur in full from evidence that cannot decide whether it occurred. It does not universally require proof of worker termination before a counterexample can decide the intended outcome. Sources: S:standards/ACTIVATION.md:791–811; S:standards/FOUNDATIONS.md:50, 676–707.

A bounded counterexample makes the difference clear. The selected outcome requires all five updates by 12:00. At 12:01, admitted evidence establishes that only three completed within that interval; whether the worker has terminated remains unknown. The declared outcome is defeated. Later completion cannot make those two updates occur within the closed interval. The profile nevertheless selects its unknown variant because termination is unestablished.

Two facts must survive: the deadline-bound outcome failed, and the effect's remaining activity is uncertain. Neither fact authorises repetition. An indeterminate overall outcome loses the established counterexample; a claim of no partial effects would lose the uncertainty.

The existing C3S-03 fixture supplies a defeated whole outcome after three of five updates and an error response. Both recorded actors select indeterminate for lack of an explicit termination witness; one spells out that reasoning at S:qualification/runs/C3S-03/TASK-r1/steps/TASK-r1.out.md:31–38. The fixture's error response alone is not proof of termination. I therefore do not settle its disputed score by assuming that it is. The closed-interval example above is a separate reviewer desk trace that removes that ambiguity.

**Consequence:** the domain refinement does not preserve the parent's deciding distinction for an outcome whose failure is already provable while execution continues.

**Smallest repair and verification:** distinguish established non-attainment of the declared predicate from an undecidable effect outcome. Retain termination uncertainty as its own residual when failure is known. Test a lost-response case with no counterexample and a closed-interval failure with unknown termination. Preserve partial-effect evidence and the prohibition on blind retry in both.

**Evidence:** source counterexample/desk trace; supporting existing-use observation. The new closed-interval case was not run through an actor.

#### F3 — High completion gap: the revised product has no current a_c interpretation

**Sources:** S:a_c/README.md:11–27; S:a_c/set-6/README.md:19–54; G0:requirements/A_C_DEPENDENCY.md:5–11, 60–74.

The a_c directory says its programs predate the rebuild. I checked that assertion against the source bindings. The set-5 and set-6 inventories match only POSTING_GUIDE and WRITING_GUIDE among their 23 listed members. Each validation report resolves 21 substantive source members; none of those 21 digests matches S. Earlier checked sets also bind changed source bytes.

For example, the bound ACTIVATION digest is `eac7dbd7d9519dcd8cb5acfd9e153833a7375797f29e8a5d5a8129a6c65b2ec9`; S's ACTIVATION is `179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed`.

The current verbatim frames provide a usable prose acquisition route. They are not a replacement for the required formal interpretation. Its models, maps and fidelity evidence are part of the Product, even though the calculus and checker are separate dependencies.

**Consequence:** historical checker success cannot qualify the revised shared laws or their consumer mappings. G1's explicit constraint-surface requirement makes this still more consequential, but the missing current interpretation was already a G0 completion gap.

**Smallest next verification:** after settling the changed laws, freeze and encode the affected shared owners and their consumer bindings, publish exact coverage and source-to-model dispositions, then perform the selected mechanical check and independent source-first fidelity review. Permitted, prohibited and unresolved cases must agree between prose and model. A partial current encoding can establish its declared scope, not completion of the whole product.

**Evidence:** reproduced digest inspection. I did not rerun the old formal model and present it as a check of new law.

#### F4 — Medium: the finite oracle misses invalid reported conjunction values

**Sources:** S:qualification/instruments/finite_oracle/conjunction/check.py:87–104; S:qualification/instruments/finite_oracle/README.md:95–125; S:standards/FOUNDATIONS.md:912–942.

The unmodified finite check passes. Its P0–P5 properties verify core membership, conditions for success, retained component failures, gap records, unchanged component values and reachable success. They do not verify all restrictions on the reported non-satisfied value.

I executed a scratch-only variant that swaps falsified and out_of_frame in the returned value set while leaving the component record intact. Across 516 cases, 1,920 outputs and 3,228 value checks:

- no P0–P5 property failed;
- the existing aggregate class/cardinality expectations still matched;
- 284 cases had a wrong reported value set.

The smallest example is one mandatory falsified component reported as out_of_frame, with the falsified component correctly retained in the record. FOUNDATIONS requires selection from the returned non-satisfied values; out_of_frame is not one of them.

The README attributes the absence of a value-level detection to the lack of an order among non-satisfied values. Lack of ordering does not permit an invented value. This counterexample concerns the tested properties and aggregate counts; I did not claim the complete template's separate mutant-comparison bookkeeping accepted the injected variant.

**Consequence:** the finite result is useful bounded evidence about records and success suppression, but does not establish fidelity of every reported-value rule. No defect in the unmodified model's output is established by this mutation.

**Smallest repair and verification:** specify permissible reported values independently of the model, test reported-value-only mutations, and retain the existing record checks. State the limited domain: one to three mandatory components, agreeing bases, no non-mandatory contributors and no outside counterexample. Extend that domain only for an explicitly selected further claim.

**Evidence:** executed reviewer counterexample, in outside-repository scratch.

#### F5 — Low: verbatim frames break ordinary rendered source links

**Sources:** S:qualification/instruments/generate_frames.py:214–243; S:standards/frames/bootstrap.md:44; S:standards/templates/PRODUCT_DEFINITION_TEMPLATE.json:25–29.

The generator copies source sections into the deeper frames directory without rebasing their relative links. In the bootstrap frame, the PRODUCT_DEFINITION link resolves to standards/frames/PRODUCT_DEFINITION.md, which does not exist. The owner is one directory above.

The frame header explains the owner-relative convention and supplies correct owner links. That provides a manual workaround. It does not make copied links function in an ordinary Markdown reader.

**Consequence:** the published entry route has avoidable navigation friction. This is not evidence that the owning rule is absent or that byte fidelity failed.

**Smallest repair and verification:** provide a working link-resolution/rendering convention or a generated presentation with rebased links and separately retained source identities. Check destination resolution from the actual published entry location.

**Evidence:** generated-source inspection and filesystem resolution.

### Executed checks and existing-use evidence

All new execution stayed in outside-repository scratch. No paid probe actor was invoked.

| Check | Result and limit |
|---|---|
| Installed rc.2 verification with the named manifest digest | Valid; establishes the builder bytes |
| Frame generator --check | Passed; current generated bytes |
| Frame-generator test suite | 35 tests passed; parser, selection/refusal and regeneration mechanics |
| Finite conjunction --check | Passed; 24,531 assertions for its declared finite domain, not all semantic cases |
| Reviewer reported-value mutation | Exposed F4; P0–P5 and aggregate counts did not reject it |
| Current a_c source binding audit | Exposed F3; historical interpretation, no current fidelity result |
| All 18 existing actor runs: input/output hashes and supplied frame bytes | Matched their records and current frame bytes |

The finite check's requirement section was acquired at its declared common input a7eba66; that section's meaning is unchanged by G0 or G1. No test was silently rebound to a different oracle.

The archived suite has nine tasks run twice with claude-sonnet-5-5. Its measured historical spend is USD 3.2215305; summed actor wall time is 851.189 seconds, not elapsed review time. Supplied inputs range from 64,833 to 94,045 bytes; recorded context-token counts range from 25,770 to 35,999. These are the tenant's already completed executions, not newly purchased evidence.

I inspected selected task predicates in both C3S-01 Task-B runs, both C3S-03 runs, both C3S-07 runs and both C3S-08 runs, and the first C3S-06 run. I did not independently rescore all 18 complete answers.

The useful observations include:

- The recovery runs preserve the 379 still-valid items, isolate 30 invalidated items and three missing ones, keep an unperformed independent review distinct from an indeterminate result, and refuse to repeat the uncertain external batch without reconciliation. One answer still misses the task's explicit pre-send review-gate implication, so these observations are not a whole-task pass claim. Sources: S:qualification/cases/C3S-08/TASK.md; corresponding TASK-r1 and TASK-r2 outputs, especially r1:35–73 and r2:44–45.
- The binding runs identify the lost independence of a second assessor who reads the first assessment and the loss of a required human decision in an automated award. They permit shared computational machinery while preserving those constraints. Sources: S:qualification/cases/C3S-07/TASK.md; corresponding TASK-r1 and TASK-r2 outputs.
- The sampled configuration answer allocates bounded work to fitting actors and keeps author review from becoming independent through a fresh session. It supplies bounded application evidence, not an optimality proof. Sources: S:qualification/cases/C3S-06/TASK.md; TASK-r1 output.
- The revision and partial-effect runs expose the interpretation risks described in F1 and F2.

Input integrity and fresh contexts do not establish independent authorship of the task oracle. The recorded actors are one model family; cross-family robustness is unproven. This review supplies source-first scrutiny and a new mechanical counterexample, not a new controlled actor experiment.

### What remains unqualified

| Question | Assessment |
|---|---|
| Fit to the revision-2 common purpose | Substantial deciding prose and acquisition support; F1/F2 block affected semantic claims and F3 blocks complete product implementation |
| Categorical readiness | Declaration, refinement and preservation obligations exist; H1 remains a hypothesis. No accepted end-to-end categorical join is established by this review |
| Demonstrated use | Bounded existing-use evidence supports several distinctions and exposes others. Selected answers were inspected; no universal competence or attention claim follows |
| Successor conservation and C3 acceptance | Open. The frontier's recorded dispositions are author claims until independently compared against the exact predecessor and successor meanings |
| Release qualification | Open. Member acceptance, unresolved packaging/compression dispositions, current interpretation and exact-cut release evidence still have to close |

The frontier contains 696 rows: 659 conserved, seven superseded, 20 not applicable and ten unresolved. Five child rows explain the increase over the common 691-row list. The ten unresolved rows concern predecessor compression members (S:frontier/PREDECESSOR_CLAIMS.md:802–811). Counts establish inventory, not semantic conservation.

The 303-row re-proof span is explicitly a working bound for changed/dependent work. It says earlier working judgments do not count toward acceptance and its dependency detection is a lower bound (S:qualification/C3-SYNTHESIS/span/SPAN.md:3–35). It cannot narrow all-member acceptance to those 303 rows.

The categorical steel thread retains its separately selected scope under the common Product. Its absence is an unresolved demonstration, not evidence that the method's hypothetical categorical claim is false. A release manifest and release note belong to exact-cut qualification; producing them early would not repair these method defects.

### Effect of the common specification's advancement

G1 adds a fourth relationship to “restated on the axioms”: demonstrated reduction. It requires shared owners to replace recurring determinations in actual consumers, justified remaining primitives, and a comparison of decisions and acquisition. It also requires the current prose and a_c interpretation to expose recoverable obligations, permission, dependencies and unresolved conditions. Sources: G1:requirements/README.md:31–66; G1:PRODUCT.md:35–55; G1:conformance/README.md:10–18.

The candidate has useful starting machinery for that reconstruction: the shared result algebra, imports, configuration and recovery contracts. But a family table, a verbatim frame, the share rewritten, and successful structural checks do not establish contraction. The inspected evidence does not yet identify and verify the repeated decisions or cross-document reconciliations made unnecessary across the method. F1 and F2 are concrete seams where consumers still fail to determine the same question consistently.

G1:GOALS.md:11 and REFERENCE_FRAME_BASIS.md:20 keep iteration-3 work authority and peer-line activation distinct. I do not retroactively treat the new requirement as a missed instruction in Claude's a7eba66-bound rebuild, nor issue a new construction grant. For a subsequent Claude revision, the new requirement needs an explicit bound task and evidence. It cannot be satisfied by merely adding another foundation introduction or updating the old model's hashes.

## Recommended Action

Keep the architecture and repair the deciding seams before broad reconstruction or acceptance.

1. **Resolve F1 and F2 at their owners.** Separate frame-coordinate changes from result validity, and proven outcome failure from unknown effect termination. Fix the corresponding expectations before rerunning the affected tasks. Preserve independent completed work and uncertain-effect residuals. Cost: estimated local semantic and consumer repair; hours and repair rounds unknown.
2. **Strengthen the narrow checks and repair entry navigation.** Add an independently specified permissible-value check and reported-value-only mutations; make published frame links usable. Regenerate exact frames and rerun checks affected by those changes. Cost: estimated small tooling work; no measured implementation estimate.
3. **Bind the next reconstruction to the current common requirements.** Demonstrate one shared law replacing recurring decisions at real consumers, using independently specified permitted, refused and unresolved cases; state what remains independently necessary. Then expand to the other material families. Do not assume a different file layout or fewer words is the proof. Cost: unknown until the owner selects scope and acquisition conditions.
4. **Produce a current a_c interpretation with fidelity evidence.** Freeze the repaired owners and consumers, encode their dependencies and residual conditions, and use the separately selected checker contract. Compare actual decisions through prose and model; preserve the source-first fidelity boundary. Cost: unknown; a digest refresh is insufficient.
5. **Complete member acceptance and release qualification separately.** Assign independent reviewers with an explicit policy for ported authorship, close every required frontier disposition, and execute the separately selected categorical thread before accepting its capability claims. Only then qualify the exact release cut. Cost: unknown; the 303-row span and historical actor spend are not estimates of acceptance effort.

Writer activation: this actor changed from Reviewer to bounded Writer solely to create this new post in the Codex comments directory. The grant covers this commentary artifact and no candidate or constitutional effect.

No candidate source, common requirement, ticket, installed product or existing review was changed by this assessment. One commentary post was written; nothing was committed. New paid probe spend: USD 0. Review elapsed time: 18 minutes 24 seconds from 2026-10-13T23:46:55Z to the post timestamp. Session model usage: unavailable in this client.
