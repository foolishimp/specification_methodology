# Independent review of Codex candidate `97e3484` against installed STDO 2.5.1 RC2

**Method and limits.** You told me not to use tools, so I did not call the advisor, check git or run a diff. I compared the predecessor and successor texts by reading them in full, predecessor first. My conclusion that "no other textual change exists" therefore rests on careful reading, not a byte diff. A mechanical diff would make that conclusion exact.

These owners were not supplied and cannot be judged here: `SPEC_METHOD.md` (including UP-020/UP-022), `DESIGN_MODULE_METHOD.md`, `TICKET_METHOD.md`, `IDENTITY_METHOD.md` and `RELEASE_METHOD.md`. Wherever Foundations or the Transformation Library summarise those owners, that summary is `out_of_frame` for this review. Those are limits on what I could check, not findings against the candidate.

## Verdicts

| Member | Result |
|---|---|
| `AXIOMATIC_CALCULUS.md` | **satisfied** |
| `REFERENCE_FRAME_METHOD.md` | **satisfied** |
| `STDO_REFERENCE_FRAME_BASELINE.md` | **satisfied** (one low-severity editorial finding) |

## 1. `AXIOMATIC_CALCULUS.md`: satisfied

**What changed.** One paragraph was added under §Position, after the first paragraph. Everything else matches the predecessor verbatim, including:
- Derivation Provenance;
- the core signature and `RecordKind_ac`;
- the five record shapes, plus the traversal, transformation and judgment records;
- AC-001 to AC-020 in full, including every AC-013 partition and witness equation;
- the `AxiomaticCalculusBasis` identity, the Exclusions and Conformance Obligations 1–10.

**Why it holds:**
- **Predecessor determinations are conserved.** "The definitions and laws below are the sole normative authority" is retained, and so is the one-way derivation direction.
- **The member is still standalone.** The added sentence says this member "specifies their calculus specialization through the signature, records and AC laws below". The meaning of `a_c` therefore stays complete inside this member, which agrees with "A consumer does not need an implicit STDO representation…".
- **No new record fields.** The library's instance contract (purpose, consumer and so on) could have threatened AC-001's closed records ("has exactly"; "Unknown kinds and fields are not extensions"). It doesn't, for two reasons:
  - the added text says applications express the library's responsibilities "through these exact records and laws";
  - the library itself says it is "not a mandatory record schema".
- **The name collision is handled.** "Its vocabulary does not replace AC-013's transformation contract" separates the library's *Transform* from the AC-013 transformation.
- **No stronger category theorem.** "…or establish category-theoretic functor laws" matches the §Traversals rule ("does not by itself assert a category-theoretic functor"). It also matches Foundations §Orthogonal descriptions, which requires identity and composition preservation before a functor claim.
- **Result algebras don't clash.** The calculus uses `accepted | refuse`, `admitted | refuse` and `hold | gap | refusal`. Two library statements cover this: "Domain members determine their admitted outcome and disposition sets" and, under Dispose, "Other instances retain their own result domains". The library's five-valued Evaluate therefore does not override the calculus.
- **Ownership links resolve correctly.** Foundations links `#ac-017-interpretation-fidelity` and `#ac-014-judgment-separation`, and those anchors exist.
- **No category violations in the added text.** It contains no construction-state narration, no new quota and no authority transfer.

**Low-severity residual (AC-S1).** The phrases "foundations supply the general premises" and "their calculus specialization" set up a relation to a member that exists only in the successor release. Under §Exact Calculus Identity:
- `principle_refs` may contain only clauses listed under Derivation Provenance from the predecessor cut;
- "Same-release references … are publication or cross-context relations, not derivation provenance".

The added text never calls Foundations derivation provenance, so nothing contradicts. The risk is that someone issuing the basis reads "specialization" as derivation and adds Foundations to `principle_refs`. The law already rules that out, so this is a clarity matter only.

## 2. `REFERENCE_FRAME_METHOD.md`: satisfied

**What changed.** One paragraph was added under §Position. Everything else matches verbatim, including:
- RF-001 to RF-017, the definitions and the method-function signatures;
- Applicability And Required Results and the conjunction rules;
- coverage, the completeness boundary, Frame Qualification and the self-qualification table;
- the worked Product-Chain binding, which matters for meaning and is unchanged.

**Why it holds:**
- **Ownership is not narrowed.** The added list ("declaration, activation, evaluation, result, coverage and revision") omits basis, relation and qualification. The following, unchanged paragraph still lists all of them, so the new list is a subset and not a reduction.
- **The specialization claim keeps the member's own rules.** "Method functions … specialize [library responsibilities] while retaining their exact applicability, result algebras, owner boundaries and qualification obligations" protects the RF-012 algebra and the `conjoin → decision | conflict | indeterminate` signature.
- **Conjunction agrees with the library.** Library Conjoin ("Satisfaction requires every applicable material predicate and seam…"; "unknown applicability prevents a wider satisfied claim") matches §Result Conjunction and §Applicability. Its planned-slot rule only applies when an admission contract declares slots, so it is not a new general quota.
- **No new authority, quota or test-to-Product leakage was found.**

## 3. `STDO_REFERENCE_FRAME_BASELINE.md`: satisfied

**What changed.** One paragraph was added in §Canonical Compression. Everything else matches verbatim, including:
- the ownership table, Engagement Applicability and every Executive section (drift locks, event-driven attention, steel thread);
- Work result and its total mapping;
- the Reviewer frame and triage projection, the twelve specialist families and four testing frames;
- the Interface Integration claim boundaries, obligations and qualification cases;
- the transition steps 1–7, Handoff, Profile Qualification 1–26 and Closure 1–24.

**Why it holds.** "Refines activation, construction, assessment, conjunction and decision responsibilities through the existing owners below" and "…retain their distinct responsibilities" restate the §Status And Authority Boundary rule ("an exact application of a cited owning STDO relation…"). No owner gains or loses authority.

**Finding BL-E1 (editorial, low severity; meaning conserved).** The new paragraph sits between "…maps three practical engagement frames onto those existing owners:" and the diagram that the colon introduced in the predecessor.
- **Effect:** the colon now introduces the Foundations paragraph instead of the mapping, and the diagram follows "retain their distinct responsibilities".
- **Why it doesn't falsify:** the diagram is unchanged and still determines the mapping, so no rule is lost.
- **Possible correction:** move the paragraph above that sentence or below the diagram. That is a technical observation; ordering and priority belong to the decision owner.

## 4. Foundations and Library bindings: any concrete contradiction?

None with the assigned members. Where Foundations or the Library is worded more loosely than a member, the member's more detailed rule governs. Some wording differences are worth recording; each is low severity and lives in those two files, which were not assigned:

| ID | Foundations / Library text | Member rule | Assessment |
|---|---|---|---|
| FL-1 | Foundations: "Each activation declares the actor and resource envelope needed by its claim" | Capability envelope = competence, context capacity, tools, access, independence, configuration. RFM §Frame-Set Optimization: no universal "resource ledger, benchmark, budget or measurement gate". | "Needed by its claim" lets this map onto the capability envelope. Read on its own, "resource" (time, storage) could look like a new declaration duty. Not a contradiction. |
| FL-2 | Library §Cost and contraction: "Measure costs appropriate to the claim…" | Baseline: "no universal cost, budget or accounting gate"; RFM as above | It is limited by the claim and creates no gate. Read as an imperative, it could look like a general measurement duty. |
| FL-3 | Foundations: "Severity describes evidenced harm; priority selects work" | Baseline: severity "grades consequence if the finding manifests"; Executive *assigns* priority; priority, boundary effect, disposition and next action are separate ledger entries | Slight drift: "evidenced harm" leans toward harm that actually happened, and "priority selects work" blurs priority with action selection. The Baseline governs; no contradiction. |
| FL-4 | Library: "Frame Method owns evaluation and composition" | RFM: the *owning application* declares material composition. AC-016 owns traversal composition within `a_c` ("sole normative authority"). | Overbroad attribution. Both members' own rules still govern, and the AC paragraph limits what the library vocabulary can do. Not a concrete conflict. |

Other bindings I checked showed no stronger claim and no contradiction:
- Foundations' category, functor and Markov statements ("neither asserts nor rejects them universally");
- the library's "not a universal category theorem";
- the identity and digest rules (consistent with AC-002 and AC-013);
- Foundations' finite-capacity handling ("reconfigure within authority"; never replace a hard relation with an easier claim), which is consistent with RF-014.

## Severity versus disposition

None of the items above is a falsifying technical finding against the assigned members. BL-E1 and AC-S1 are editorial or clarity points; FL-1 to FL-4 sit in the Foundations and Library files. Ordering, priority and whether to accept or repair belong to the decision owner, not to this review. Whether the corpus works in practice, and publication, are separate claims this review does not cover.
