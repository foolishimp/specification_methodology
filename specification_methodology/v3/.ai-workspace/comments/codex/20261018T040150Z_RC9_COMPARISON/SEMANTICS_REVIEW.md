My narrow preference is **Codex for the generic method core**, with moderate confidence. Claude has the better separation of document responsibilities. Both RC9 candidates now implement the substantive construction and assurance model; the old comparison does not justify treating one as conceptually incomplete.

I formed expectations from the ratified common Product, requirements and Assurance before reading candidate bodies: lawful A→Z construction must preserve the outer obligations without claiming progress or completion automatically; required meaning, observations and predictions must remain distinct; shared laws must decide actual consumer behavior; result mappings must preserve failure, nonperformance and uncertain effects; and reuse must establish applicability on the new subject.

Reviewed subjects:

- Claude: `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3`. Its standards are unchanged at the current handoff.
- Codex: `5592168e26759f37e730aed12c030a6061709ec4`. Its standards are unchanged at the current handoff.

**Why I narrowly prefer Codex**

Codex gives the generic construction, evidence and recovery questions a comparatively direct center in Foundations, with an explicitly scoped transformation contract used by its consumers. Its A→Z relation distinguishes required conditions, actual observations and prediction; permits discovering a strategy; preserves independent work; and refuses to confuse exhaustion with completion. See [FOUNDATIONS.md:961](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/FOUNDATIONS.md:961). Claude supplies substantially the same behavior in [ACTIVATION.md:198](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/ACTIVATION.md:198).

The practical advantage is how Codex carries several awkward situations through that center:

- Its result law explicitly separates the evaluated predicate, actual performance and observed effects, including a witnessed failure before an aborted suite, an absent return, a lost acknowledgment and unintended effects.
- Its effect conjunction explains normalization across sequential actions: deployment, rollback and reapplication cannot be combined by merely joining their local “completed” labels.
- Its reuse law directly explains that old evidence retains its historical subject, while an applicability relation supports the current claim; repairing or relaxing an obligation does not rewrite the original failure.

These are useful decision examples, not evidence that serialized performance fields are required or that Claude’s alternative is wrong. Codex explicitly calls its record a semantic contract rather than a mandatory format. See [FOUNDATIONS.md:365](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/FOUNDATIONS.md:365), [FOUNDATIONS.md:496](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/FOUNDATIONS.md:496) and [FOUNDATIONS.md:833](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/FOUNDATIONS.md:833).

Claude’s predicate-first refinements are coherent. Its `not_effected` means the intended outcome cannot be attained, **not** that nothing happened; an effect may still be acting, and that uncertainty remains a separate residual. Its recovery law prohibits blind repetition. This is not an unknown-effect safety defect. The explanation is more demanding for a consumer because it must carry both the outcome predicate and the effect-ended condition. See [ACTIVATION.md:1122](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/ACTIVATION.md:1122).

**Where Claude is better**

Claude’s separate `PRODUCT_DEFINITION`, `ASSURANCE`, `ACTIVATION` and `EVALUATION` owners give a maintainer a clearer answer to “where does this kind of rule belong?” Codex’s `SPEC_METHOD` still combines Product Definition, semantic resolution, construction, assurance, migration and operational entry in one large member.

Claude also gives unusually explicit source-to-law and law-to-consumer traces. These help audit what was conserved and what a profile adds. The cost is substantial repeated explanation: consequence tables, consumer lists, provenance and assertions that a consumer “states no second relation” often surround the deciding clause. Codex is usually easier to read locally; Claude is easier to audit by responsibility. Neither advantage establishes superior actual use without matched trials.

I would preserve this architectural advantage as a bounded design input after selecting a basis. It does not justify a last-minute wholesale synthesis.

**Verified remaining defect**

**Moderate derivation-fidelity defect; limited to Claude’s world-model rationale, not a demonstrated unsafe execution path.**

[WORLD_MODEL.md:178](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/WORLD_MODEL.md:178) puts “the attribute ledger is append-only” in the *Consequence that follows* column from P4b, P3, P6 and source sovereignty. But [FOUNDATIONS.md:495](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/FOUNDATIONS.md:495) requires needed produced facts to be recorded and recoverable. That does not select this particular ledger policy.

A countermodel is an authenticated history of complete snapshots with a replaceable materialized current view. It can preserve the required historical facts, exact identities and authority without deriving an append-only attribute ledger from those premises.

The profile may legitimately choose append-only ledgers, and its downstream law already does. The repair is to identify that choice as **domain policy**, preserving its existing scope and modal force—not remove the ledger requirement. Codex makes precisely this distinction at [WORLD_MODEL_METHOD.md:38](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/WORLD_MODEL_METHOD.md:38).

I found no other verified semantic blocker in this bounded review. In particular, I did **not** confirm a contradiction between Claude’s stale-result handling and evidence reuse: direct reliance on an old result and retaining its evidence under a new applicability relation are different operations.

**Old findings and RC9 readback**

| Earlier concern | Current finding |
|---|---|
| Codex generic assessment requires live **code** | **Repaired.** It now assesses the exact live **realisation under the selected computational binding**. The generic Method permits human realization and direct observation. [SPEC_METHOD.md:1894](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/SPEC_METHOD.md:1894), [SPEC_METHOD.md:3398](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/SPEC_METHOD.md:3398). |
| Claude observation sufficiency treats any two subjects as a failure | **Repaired.** It now requires equal observations with opposite predicate truth. [ASSURANCE.md:691](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/ASSURANCE.md:691). |
| Claude progress shorthand drops acceptance | **Not a current defect.** The shorthand explicitly sends the reader to §5, whose owner defines progress as accepted material movement. [ACTIVATION.md:186](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/ACTIVATION.md:186), [ACTIVATION.md:1413](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/ACTIVATION.md:1413). |
| Claude append-only policy presented as foundational consequence | **Persists narrowly**, as described above. |
| Codex mandatory adoption of the whole Design Module profile | **Not present.** Generic design laws and optional profile policies have an explicit applicability split. [DESIGN_MODULE_METHOD.md:5](/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/successor/standards/DESIGN_MODULE_METHOD.md:5). |

The latest Claude scenario-observation correction passes an independent bounded source readback:

1. **Implementation returns 10, broken decoder reports 1, expected 10:** the scenario reports an observation/expectation disagreement. It cannot establish actual implementation disagreement without the observation binding; diagnose the decoder.
2. **Implementation returns 10, sound decoder, expected 11:** actual behavior differs from the expectation, but a Product defect does not follow until that expectation is justified; diagnose the expectation or governing requirement.
3. **Implementation returns 9, sound decoder, justified expected 10:** the observation supports the actual discrepancy and implementation counterexample.

[ASSURANCE.md:62](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/ASSURANCE.md:62), its rationale at line 99, and disposition at line 1150 agree with [FOUNDATIONS.md:1230](/Users/jim/src/apps/specification_methodology-claude/specification_methodology/v3/build_tenants/claude/standards/FOUNDATIONS.md:1230). I regard **RC8-01 as corrected in the RC9 source within this scope**. Acceptance of the proposed predecessor replacement is a separate owner act.

Both candidates also preserve the important practical cases I traced: a known failure remains visible beside missing coverage; a predictive error does not by itself prove Product failure; an implementation-derived assertion cannot establish upstream conformance without justification; an unchanged hash alone cannot establish evidence applicability; and resumption neither erases valid progress nor authorizes repeating an uncertain effect.

My preference is therefore a **source-quality judgment**, not an observed usability win or a full release verdict. It covers substantive owners and representative triage, assurance, recovery and profile-entry consumers. It does not supply exhaustive predecessor conservation, complete interpretation fidelity, matched fresh-actor use, or a whole-corpus proof.
