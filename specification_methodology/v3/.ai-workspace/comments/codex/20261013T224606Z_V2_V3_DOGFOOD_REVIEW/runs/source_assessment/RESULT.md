# Independent source-first comparison: STDO 2.5.1-rc.2 (v2) vs frozen Codex v3 source 9bc8962

**Standing.** rc.2 remains the governing construction authority. v3 is assessed only as a candidate. Every finding below comes from reading the supplied excerpts. I executed nothing and computed no digests. Where I say something is "absent from packet", I make no claim about the corpus. I make no claim about whole-corpus acceptance, superiority, release readiness, or the independence of historically ported text.

---

## 1. Coverage

| Supplied | Not supplied (absent from packet, corpus status unknown) |
|---|---|
| v3 `FOUNDATIONS.md` L1–235, L296–643 | v3 FOUNDATIONS L236–295 (likely contains "Orthogonal descriptions", which L1–235 references) and the body of `## Core contract derivations` after L643 |
| v3 `TRANSFORMATION_LIBRARY.md` L1–275 (appears complete, but this is not established) | Any v2 FOUNDATIONS or TRANSFORMATION_LIBRARY. Whether v2 had them is unknown. |
| v3 RFM L344–508 (RF-001–017), L628–773 (Engagement, Conjunction), L1376–1405 | v3 and v2 RFM `#position`, `#authority`, Lens and Role sections, Closure items 3 onward (v3) |
| v2 RFM L289–447, L562–710, L1312–1344 | SPEC_METHOD (UP-013/014/020/021, bounded-context resolution), DESIGN_MODULE_METHOD (UP-016/017, totality), Baseline, AXIOMATIC_CALCULUS, TICKET/RELEASE methods, `frames/*.md`, the stdo-work SKILL |
| v2 `authority_compressions/stdo_bootstrap.md` (whole) | The v3 bootstrap compression, and the v2 README |
| v3 `standards/README.md` L1–105 | All consumer instances, fixtures and qualification records |

**Observation from packet headers only.** The v2 bootstrap's `source_digests.REFERENCE_FRAME_METHOD.md` (`6e9148d7…`) equals the supplied v2 RFM whole-member digest. The v3 RFM digest (`7faacabc…`) differs. Under the asset's own `stale_if_source_digest_changes: true`, this asset would therefore be stale against v3. Whether a regenerated v3 counterpart exists is indeterminate, because none was supplied.

---

## 2. Preservation (v2 → v3, within the supplied slices)

- **Verbatim carry-over.**
  - RF-001 to RF-008, RF-010, RF-011, RF-013 to RF-015 and the supplied part of RF-016 are textually unchanged.
  - The Engagement sections are unchanged: Establish the Evaluation Basis, Applicability and Required Results, Reconfigure When Necessary.
  - Co-evaluation, Translation and Material Composition are unchanged.
  - These are preserved by carriage. I make no claim that this ported text was re-reviewed independently.
- **RF-009 additions (v3).** v3 adds a configuration pointer and the sentence "Roles label selected responsibilities…". This is consistent with the v2 no-hierarchy law and with FOUNDATIONS `## Configuration`, which says "do not uniquely derive a hierarchy or a fixed inventory of roles".
- **Conjunction protections are preserved and tightened.** v2's "Common agreement cannot discard a … counterexample found by only one contributor" and "aggregate green status cannot replace them" survive in three places:
  - v3 RFM `### Result Conjunction`: "Counting agreeing frames cannot discharge…"
  - FOUNDATIONS `## Result conjunction` rule 1 (falsification precedence).
  - FOUNDATIONS rule 4: "An empty list proves nothing unless the declared required set is established as empty."
- **Authority.** RF-006 and RF-007 are unchanged. FOUNDATIONS `## Judgment and authority` and TL `## Foundational contract` (F6: "Sufficient evidence for P cannot supply G") add explicit no-minting statements. FOUNDATIONS `## Finite capacity and total handling` makes clear that RF-014 supplies no delegation grant. I found no clause in the supplied v3 text that widens authority.
- **Basis selection.** v3 README `## Distribution and entry` keeps the bootstrap's exact-cut discipline: "A mutable source head or moving selector cannot replace it". It also adds that a local copy is operative only when explicitly bound and verified.
- **Result template.** v3 RFM `## Minimal Evaluation Result` keeps every v2 line. It adds three: "exact predicate and domain refinement", "core verdict and original domain outcome", and "performance and known effect state".

---

## 3. Findings

### F1 — Medium: admission and basis failure classification can diverge, and the Reconfigure triggers were not updated

**Clauses involved.**
- RF-005 (unchanged): "A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or requires reactivation."
- v3 RF-012: "A declared ambiguity that prevents admission therefore falsifies admission". An admission prohibition "is no counterexample to downstream fitness". The downstream slot otherwise "stays absent".
- FOUNDATIONS `## Result algebra`: a precondition is evidence "unless the plan separately requires that precondition as a predicate".
- FOUNDATIONS `## Result conjunction`: "A failed admission condition prevents an interpretation".
- v3 `### Select And Activate`: activation now returns "an RF-012 activation refusal". v2 returned "a refusal or `out_of_frame` pressure".
- `### Reconfigure When Necessary` (unchanged): triggers only on `out_of_frame`, invalid-basis, repeated indeterminate, or incompatible.

**Counterexample.** Evaluation E is activated on subject S, and the basis has two candidate manifests (ambiguous). Three defensible outcomes follow:
1. A reader applying RF-005 reports `invalid_basis`. Reconfigure fires.
2. A reader applying RF-012 reports admission `falsified` and leaves the work slot absent. The composite verdict is then `indeterminate`, and Reconfigure fires only if this repeats.
3. If the plan lists admission as a required predicate, conjunction rule 1 makes the composite `falsified`. No Reconfigure trigger names that case.

**Consequence.** The same world state can route to reconfiguration, to waiting, or toward a falsified composite that a UP-020 consumer (not supplied) might dispose as reject. Each clause is internally coherent. The defect is the missing harmonisation. RF-005 should state which predicate it binds, and Reconfigure should name "activation refusal / admission falsified".

### F2 — Medium: `out_of_frame` was narrowed, so RF-003 insufficiency lost its explicit verdict route

**What changed.**
- v2 RF-012: `out_of_frame` meant "the evaluation requires an undeclared material relation or capability".
- v3 FOUNDATIONS: "The predicate is outside the evaluation's bound scope or capability".
- v3 TL `## Foundational contract`: "F2 requires a truthful unknown when material support is insufficient".

**Effect.** A frame discovered mid-evaluation to omit a material relation (RF-003 insufficiency, with the predicate still in scope) is, under v3, most naturally `indeterminate`. Under v2 it was `out_of_frame`. Because Reconfigure triggers on `out_of_frame` but only on *repeated* indeterminate, v3 can delay frame revision. It can also encourage re-running the same insufficient frame.

**Mitigation.** FOUNDATIONS "the actor reports the misfit" partly compensates. However, that clause addresses *capacity* misfit, not undeclared-relation insufficiency.

**Severity basis.** This is a semantic change to a core law's routing with no visible migration statement.

### F3 — Medium (conditional): v2 externally owned algebra extensions have no visible successor route

**What changed.**
- v2 RF-012 permitted "An externally owned compatible extension may refine this algebra while preserving… pressure."
- v3 forbids a parallel algebra (TL `## Evaluate`; FOUNDATIONS bounded construction: "does not introduce another method result algebra").
- v3 requires a "total, reason-sensitive map". A missing required reason maps the claim to `indeterminate` and makes it inadmissible as deciding support.

**Counterexample.** A v2 extension outcome such as `accepted`, recorded without a reason, was a satisfied-class result under v2. Re-read under v3, it becomes `indeterminate`.

**Consequence.** Historic results may lose standing on upgrade. That may be the correct outcome, but it needs a successor-conservation disposition. Release Method UP-015 (not supplied) would own that disposition. No consumer migration proof is visible. This is **indeterminate, not a demonstrated defect**.

### F4 — Low: RF-012's "remains `not_performed`" default conflicts with the performance evidence condition

**Clauses involved.**
- v3 RF-012: "Successful activation satisfies admission only. The work remains `not_performed` until actually undertaken."
- FOUNDATIONS performance table: `not_performed` requires that "Evidence establishes that the evaluation was not undertaken. Dispatch or admission alone does not establish performance."

**Counterexample.** An evaluation is activated and dispatched, and the return is lost. Read literally, RF-012 gives `not_performed`. FOUNDATIONS gives `unconfirmed`, and RF-012's own next paragraph also says "retain the core `unconfirmed`".

**Consequence.** A reader taking `not_performed` may re-dispatch. The separate unknown-effect reconciliation rule in `## Workspace and context` limits the damage for effectful work. The duplicated-evaluation risk remains for evaluations whose effect is classed `not_requested`.

**Fix.** Scope the sentence to "before dispatch".

### F5 — Low: the explicit anti-churn reuse guard is no longer stated in the supplied v3 text

**What changed.**
- v2 `### Return A Closed Result`: "Role, conversation or resumption changes alone do not invalidate it."
- The v2 bootstrap, item 8, says the same.
- v3 replaces this with a pointer to FOUNDATIONS reuse: "adequate current basis and evidence… required independent authorship".

**What v3 keeps.** It keeps restart and resumption non-invalidation: TL `## Recovery law` ("A process restart by itself is an acquisition event") and FOUNDATIONS ("neither erases progress").

**What v3 drops, in the supplied text.** The statement that a *role change* does not invalidate is gone. "Adequate current" can also be read as requiring re-observation.

**Consequence.** Possible redundant re-derivation, which is a cost regression rather than a safety regression. A v3 bootstrap that restores the guard may exist, but none was supplied.

### F6 — Low–Medium: Foundations and RFM depend on each other, which widens invalidation

**The dependency loop.**
- FOUNDATIONS and TL import the authority vocabulary from `REFERENCE_FRAME_METHOD.md#authority`.
- RFM in turn depends on `FOUNDATIONS#result-algebra`, `#workspace-and-context` and `#configuration` (RF-009, RF-012, Select And Activate, Result Conjunction).
- Both import sections say a changed source member "requires fresh applicability before use".

**Consequence.**
- Any RFM edit reopens Foundations, then TL, then every consumer of the core algebra.
- Foundations edits reopen RFM.
- The "premise layer" is not upstream of the method it governs. This is a layering inversion: FOUNDATIONS says "Particular methods own their deciding clauses", yet its own authority vocabulary comes from a particular method.

**Severity basis.** This is not a logical contradiction, because the concepts are disjoint. The cost is assurance blast radius.

### F7 — Low: TL's import declarations do not cover the core result terms it consumes

TL declares imports for the RFM authority vocabulary. Its `## Foundational contract` declares F1–F6 premise ownership.

The `## Evaluate`, `## Conjoin` and `## Recovery law` sections also consume the result algebra, conjunction and workspace/context terms. These are not F1–F6. TL has no stated import for them, even though FOUNDATIONS insists that "no shared default interpretation is inferred" and TL says "Equal spelling is no equivalence or import."

Whether owner-qualified hyperlinks satisfy SPEC_METHOD bounded-context resolution is **indeterminate** (not supplied). The same question applies to v3 RFM `#position`.

### F8 — Low: two duplicated paraphrase tables cannot be checked against their source

FOUNDATIONS and TL each carry an identical six-row table restating `RFM#authority` definitions as "Exact source concept". RFM `#authority` is absent from the packet, in both versions, so fidelity cannot be checked.

**Consequence.** Two copies of a paraphrase drift independently. A divergent paraphrase would be an unlawful local definition by these members' own rules.

### F9 — Low: the "Return A Closed Result" prose and the record definitions are not quite aligned

- v3 `### Return A Closed Result` drops v2's "evaluation" from its list and replaces it with "predicate". FOUNDATIONS, however, requires that "The activation identifies that evaluation separately from dispatch, admission". Performance is defined per evaluation. The template still has `evaluation:`, so the gap is in the prose list only.
- The FOUNDATIONS core record includes "unresolved obligations". The RFM template has only "residual uncertainty".

### F10 — Info/Low: complexity and attention cost

**Size.** v2 RF-012 is about 15 lines. Its v3 replacement is RF-012 (about 35 lines) plus FOUNDATIONS result algebra and conjunction (about 150 dense lines).

**What the growth buys.** By inspection it closes real gaps. FOUNDATIONS' own examples show this:
- an aborted suite with a witnessed failure is "performed + falsified";
- a load test that cannot generate its required load is "performed + indeterminate";
- a lost acknowledgment is `unknown`;
- "completed deployment followed by completed rollback is reverted".

**Join check.** I checked the effect join by case reasoning only. It is consistent with the value definitions. It is associative over normalized parts if `partial` is treated as {completed, not_started}.

**Costs.**
- The rule that every possibly-affected part "under its supported operating model" must be observed or else is `unknown` will make `unknown` common for broad operations. The rule that this prevents satisfaction only "where the predicate requires a known effect state" contains the damage.
- RF-002 (finite attention) applies to the method's own consumers. Whether `frames/*.md` projections fit actor envelopes is indeterminate (not supplied).

**Deliberate tightening, not a regression.** v2 let the declared rule decide how "conflict" is handled. v3 mandates that a falsification cannot be downgraded. This is conservative. The cost is that a spurious authenticated falsification dominates until re-evaluation is routed.

---

## 4. Context, recovery and authority summary

**Context and recovery: strengthened, judged by inspection.** v3 `## Workspace and context` and TL `## Recovery law` add:
- the rule that absence from a partial projection does not show absence in the subject;
- freshness and concurrency binding;
- the rule that retry needs established idempotence;
- the rule that "A same-context exercise cannot establish" claims of continuity independent of private actor state.

v2 had RF-013 and reuse rules, but the supplied v2 text has none of these explicitly.

**Authority: preserved.** I found no minting path. Disposition (TL `## Dispose`) is bound to the actor carrying decision authority under UP-020, which was not supplied.

---

## 5. Unresolved obligations

1. Harmonise RF-005, RF-012 and the Reconfigure triggers (F1). Declare the verdict route for RF-003 insufficiency (F2).
2. Provide a successor-conservation disposition for v2 externally owned algebra extensions and reasonless legacy outcomes (F3; owner: Release Method, not supplied).
3. Verify the `RFM#authority` text against both import tables (F8). Confirm that RFM `#position` and TL declare imports of the Foundations result terms (F7).
4. Obtain the v3 bootstrap or compression. Check that it is regenerated against v3 digests, that it lists FOUNDATIONS and TL if it projects their duties, and that it keeps the role-change reuse guard (F5) and the Executive no-mutation guard. The latter is owned by the Baseline, which was not supplied.
5. Supply FOUNDATIONS L236–295 and the content after L643 (`Core contract derivations`) before any claim about full-member coherence.
6. Consumer proof for these is **indeterminate, not defective**: Baseline WorkerResult and Reviewer mappings, the UP-020 Spec disposition mapping, UP-016/017/021 design admission, and the `frames/*.md` projections.
7. Re-read F4's "remains `not_performed`" sentence and scope it to before dispatch.

**Overall.** Within the supplied bytes, v3 preserves v2's frame, conjunction and authority laws. It materially strengthens result, performance, effect and recovery handling. It introduces three medium-severity routing and compatibility seams (F1–F3) and a dependency-layering cost (F6). None of these is shown to permit a false `satisfied` or an authority widening. This does not establish adoption fitness for v3.
