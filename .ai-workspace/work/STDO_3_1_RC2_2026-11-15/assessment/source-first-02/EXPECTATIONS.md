# Source-only addendum: what `product_acceptance` means, the successor condition, dependency guards, and corrections (STDO 3.1.0-rc.2, acceptance selector)

## 0. Standing

- **What this is:** expectations written from the supplied sources only, before seeing any candidate. It contains no candidate verdict, no patch and no publication authority.
- **Tools:** I made no tool calls, including the advisor tool, because the instruction said not to use tools. The host account reminder and environment metadata were not used. Any other hidden host context is unmeasured.
- **What I did not see:** the W35 rule object, the rule index, the query, RC2 bytes, test output and any verdict. `context_core.py` (the rendering and guard logic) was not supplied either, so anything below about rendering is a requirement drawn from the authoring contract. It is not a description of how the engine actually behaves.
- **Citation key:**
  - **P** = PURPOSE.json
  - **U** = references/sdlc-workflow.md
  - **M** = references/method-targets.md
  - **D** = design/DESIGN.md
  - **S** = requirements/SDLC-WORKFLOW.md
  - **R** = requirements/README.md
  - **A** = references/authoring.md
  - **E5** = installed EVALUATION §5
  - **R9** = installed RELEASE §9
  - **PA** = the prior source-only Claude report

## 1. What `product_acceptance` denotes, and what its name does not establish

**Declared meaning.** `boundary_kind` is "The actual decision boundary: none, landing, work_closure, product_acceptance, qualification, or release. A name does not establish its conditions or authority." (P). U adds: "the selected boundary's actual conditions remain to be established", and "Named landing, closure, acceptance, qualification and release decisions retain their own conditions … they create no extra lifecycle or universal review gate."

**My reading.** The value records an observation by the caller: the actual decision in this request is an acceptance decision. This is the decision E5 separates from the others: "Record these as separate decisions" (landing, work closure, release). It means acceptance as E5 ¶1 describes it: "the decision owner's disposition over an unchanged subject". That law is general. It is not limited to one named boundary, and its successor clause ("Where the subject is a successor…", E5 ¶2) is a condition on the subject, not on the label.

**What the label does not establish:**

| # | Not inferable from `boundary_kind = product_acceptance` | Source |
|---|---|---|
| N1 | That acceptance occurred, is authorized, or that any condition is met | P "A name does not establish its conditions or authority"; S coverage predicate; U "Neither … authorizes a boundary" |
| N2 | Who the decision owner is, or whether a bounded proxy was admitted | E5 ¶1 |
| N3 | That a declared cross-Product acceptance gate exists. That kind of gate requires an explicit declaration naming both Products, the relation, the candidate, review, conditions and owner. | E5 "Declared Product acceptance gates": "co-location, a dependency or this available mechanism creates none" |
| N4 | That the subject is a successor. No declared fact carries successor status (see §2). | P fact list |
| N5 | That this is acceptance of an immutable release cut. `release` is a separate value, and E5 says "release applies the separately selected publication and acceptance conditions of RELEASE". If a request accepts an exact cut, whether the caller labels it `product_acceptance` or `release` is the caller's observation. The supplied sources do not settle it. | P; E5 "Landing, closure and release" |
| N6 | Which review, independence or Product cutoff policy applies, or whether review is required | E5 "A required review holds…"; "The decision cutoff is the adopting Product's policy"; S PC-S04 |
| N7 | Any relation between `boundary_kind` and `action`. For example, nothing says whether `product_acceptance` is only meaningful when `action = boundary`. | No supplied source (gap G2) |

## 2. Can the existing successor condition stay in rule text without a new fact? Yes, lawfully, and this is my own reading.

- **No successor fact exists.** The 15 declared facts are listed in P. None of them means "the subject is a successor". `reuse_evidence` and `source_changed` mean other things, and reading them as a successor flag would change their declared meanings.
- **Keeping the condition as text is lawful, and is what the sources prescribe:**
  - A: "Use only declared purpose fact names and predicates justified by the source. Preserve richer conditions as text … rather than manufacturing facts"
  - A: "Do not … turn conditional rules into universal ones"
  - D: "Rich causal, permission, review and policy premises stay complete conditional obligations; query flags do not purport to prove future work"
  - S: "Complete conditional obligations name the evidence and owning Product inputs the consumer must obtain"
- **A new fact would be out of scope.** Adding a successor fact, or changing an existing fact's meaning, is a semantic purpose change: S "existing purpose and fact meanings are preserved unless an explicit semantic change establishes a new purpose boundary"; S PC-S06. That falls outside the admitted outcome ("purpose/fact meanings remain unchanged").
- **What may change.** D, "Latest method source rebinding", allows the purpose *description* to change to name the newly selected release while the purpose ID and fact meanings stay the same.
- **The text must keep four things, uninverted:**
  - the condition "where the subject is a successor" (E5 ¶2);
  - its population: "every predecessor claim capable of affecting the successor" (R9 ¶1);
  - the consumer's duty to establish successor status from task inputs;
  - when the condition is absent, the general acceptance law of E5 ¶1 still applies.
- **Open representational point (gap G3).** The sources do not decide whether the in-text successor condition must also appear as a material rule `unknown`, which would block a covered claim (A: "Rule `unknowns` are material when that rule is selected"). The rule is still selectable from `boundary_kind`, and the successor branch is a complete conditional instruction, so I count either representation as lawful. It becomes a falsifier only if the condition is dropped, made universal, or replaced by a manufactured fact.

## 3. Rendered dependency rules whose own guards are false or unknown

**Source law:**
- A: "Dependencies retain other local rules together; a false dependency remains visibly inapplicable."
- A: "A missing, null or incompatible fact yields unknown."
- A: "Unknown exception applicability prevents a covered claim."
- S: "Unknown facts deciding which constraints apply remain material gaps."
- A: "Similar labels do not establish either relation." Each dependency must be warranted by a source.

**Expectations for the later assessor:**

| # | Situation | Expected rendering and standing |
|---|---|---|
| X1 | Dependency guard false (e.g. `reuse_evidence = false`, `review_in_scope = false`, `profile_executive = false`) | The dependency is delivered with the dependent rule and is visibly inapplicable. It is not silently dropped and not shown as binding. |
| X2 | Dependency guard unknown | Retained and marked unknown, not false and not true. It is a material gap, and no covered claim follows. |
| X3 | A false or inapplicable dependency must not empty out the selected rule | If any of O1–O9 (PA §2) exists only inside a dependency whose guard is false at `product_acceptance`, the obligation is effectively absent. That is a falsifier. |
| X4 | A false fact must not hide a known applicability | P: `finding_present`, `reuse_evidence` and `source_changed` set false "must not conceal" known matters. `profile_executive` false "does not waive required assessment". A false `review_in_scope` does not waive a required review (S PC-S04; E5). |
| X5 | Selection is not truth | Rendering the dependency does not make its premise true. A passing `check` stays `covered: false` (U). |

## 4. Prior-actor expectations that need qualification or correction

The left column is what the prior report said. The right column is my correction.

| PA item | Correction or qualification |
|---|---|
| Row B and Row C (successor yes/no/unknown as query cases) | **Correct.** No successor fact exists, so these are not selector cases. Rows A, B and C get the same selection result. Row C's substance moves into the obligation the consumer applies: unestablished successor status must not be treated as "not a successor". |
| "Two admissible forms"; second: "selection gated on an existing declared fact" | **Qualify.** No existing declared fact denotes successor status. Selection can only turn on existing facts such as `boundary_kind` and `action`, with the successor condition kept in text (§2). A successor fact is outside the admitted outcome. |
| Row G "Boundary fact unknown → incomplete" | **Correct.** D says the family guard covers SDLC scope and adopted defaults. Named boundaries are rule conditions. An unknown `boundary_kind` therefore makes W35's own guard unknown (a material gap, not covered). It does not make the family selection "incomplete". Family-level incomplete applies only to family facts (U; R PC-R03). |
| Row G, implicit | **Add (gap G1).** An out-of-list string such as `"acceptance"` is type-compatible, so the scalar test `eq` gives false, not unknown (A). The supplied sources contain no value-list validation. A misspelled value could therefore quietly deselect W35. |
| Row A "RC1 shows the defect as absent; RC2 must show it present" | **Qualify.** I have not verified RC1's absence. It is the predecessor finding, carried as an admitted repair premise, and per the instruction it is not a new RC2 verdict. |
| Row A: RELEASE §8 not transferred | **Keep, with a qualification.** The purpose's fact meanings do not establish whether a particular acceptance of an exact cut is `product_acceptance` or `release` (N5). The context must not present cut-specific conditions as the generic acceptance law. |
| Row D and Row E citations to RELEASE §3 and §8 | **Qualify.** They were not supplied in this packet. Only R9 ("blocks qualification") and E5 ("release applies … acceptance conditions of RELEASE") are re-grounded here. The regression expectation that W35 stays present at qualification and release is still source-supported. |
| Row F (no W35 at work, QA or landing) | **Keep.** Also, `work_closure` was not addressed. No supplied source requires W35 at work closure: closure applies its stated condition (E5). If the stated closing condition names acceptance or qualification, that relation comes from the task's condition, not from a selector fact. |
| O10 citation "Purpose Context PRODUCT 'makes no release decision'" | **Replace.** PRODUCT was not supplied. Use instead: S coverage predicate "does not assert … any boundary has passed"; U "Neither result proves the task's repair or authorizes a boundary". |
| §3 "39 unaffected rules text-stable" | **Qualify.** U lists 40 rules: 35 original plus 5 continuity, with W01 role wording reconciled for the release. For RC1 → RC2, every rule other than W35 needs its meaning conserved, and each byte change (e.g. W01 release identity, the purpose description) needs an individual disposition (R9; S rebuild paragraph). Fact meanings must be semantically unchanged. |
| §3 release identity (25 refs, atomic push, GitHub assets) and the cross-family assessor | **Mark out of scope.** No source supplied here grounds these. They remain prior-actor expectations, and the 25-ref count is that actor's own inference. |
| O1–O9 and K1–K7 | **Keep.** They are re-grounded in E5 ¶2 and R9 as supplied. |

## 5. Fixed falsifiers for the later candidate assessor

| ID | Falsifier |
|---|---|
| F1 | At `boundary_kind = product_acceptance`, W35's obligation (O1–O9) is not delivered, or reaches the reader only through a dependency that is false or inapplicable (X3). |
| F2 | The successor condition is removed, made universal, or turned into a manufactured fact, or the predecessor-claim population is narrowed. |
| F3 | A new purpose fact is added, or an existing fact's meaning changes (rather than just the release-naming description). |
| F4 | An unknown, null or ill-typed `boundary_kind` yields W35 as false or covered rather than unknown, or the family result is misreported. |
| F5 | W35 is no longer present at `qualification` or `release`, compared with the predecessor. |
| F6 | W35 is selected at `none`, `landing` or ordinary QA as if it were an acceptance gate (S PC-S02). |
| F7 | A dependency with a false guard is omitted or shown as binding, or one with an unknown guard is shown as resolved. |
| F8 | Any rendering, check or label implies that acceptance, qualification or coverage passed, or that a declared cross-Product gate exists (N1, N3). |
| F9 | Changes to rules other than W35, or to fact meanings, appear without individual dispositions. RC1 assessments are reused for RC2's index, corpus or query (M; R PC-R16; S PC-S09). |

## 6. Missing sources that would decide the open points

- **G1:** whether `boundary_kind` values are validated against the allowed list. This would be in the core or schema, which was not supplied.
- **G2:** whether `boundary_kind` is meaningful independently of `action`.
- **G3:** whether the in-text successor branch must be listed as a material rule unknown.
- **G4:** whether, for this Product, acceptance of an exact release cut is labelled `product_acceptance` or `release`. The caller's Product governs this; it was not supplied.
- **Other unsupplied sources:** the full text of RELEASE §3 and §8, ACTIVATION, FOUNDATIONS and PRODUCT. I made no expectations that depend on them.
