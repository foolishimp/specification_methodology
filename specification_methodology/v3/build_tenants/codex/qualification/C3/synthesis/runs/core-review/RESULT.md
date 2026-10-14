# Independent Source Review: Codex core at 3cfb2ab (FOUNDATIONS, TRANSFORMATION_LIBRARY)

**Scope.** I reviewed the two supplied members against the Common Requirements. Consumer members are not supplied: SPEC_METHOD, REFERENCE_FRAME_METHOD, DESIGN_MODULE_METHOD, AXIOMATIC_CALCULUS, TICKET_METHOD, RELEASE_METHOD, the Baseline, frame catalogues, PREDECESSOR_CLAIMS and SKILL.md. Every claim about them is therefore listed as outstanding integration, not as a finding. Two things are outside this judgment: whether the imported historical concepts are faithful, and whether the owner approves the review policy. This review does not decide whether the release is accepted.

---

## 1. Core meaning that is correct as stated

These parts meet the requirements and need no change:

**Verdict domain and standing rules** (Foundations › Result algebra)
- Each of the five verdicts has a clear meaning against its bound predicate.
- Performance is scoped to the named predicate, not to the whole activation.
- `not_started` requires evidence that dispatch did not occur.
- A lost acknowledgment is treated as `unknown`.
- An empty log or discarded context does not establish that no effect happened.
- The prohibition on raising standing covers all four cases of requirement 3.
- Availability, fitness and acceptance are separate predicates (requirement 5).
- Recording a decision is not its authority.
- Not-applicable needs a supported judgment.

**Conjunction** (Foundations › Result conjunction)
- Contributions are authenticated before use.
- A missing planned judgment is distinct from uncovered coverage outside the plan.
- Falsification dominates.
- An empty list proves nothing unless the required set is shown to be empty.
- A disjunction cannot be relabelled as a conjunction.
- Reordering needs an effect-independence law beyond associativity.

**Workspace and context** (Foundations › Workspace and context)
- Context is a fallible, disposable account of the workspace.
- An observation binds its source and its time or version.
- Resumption needs no transcript replay.
- Reuse requires supported applicability.
- Retry requires idempotence established for the actual operation.
- An event log is not universally the work state.
- Observations do not license changing a requirement to match the implementation.

This substantively carries Bounded Transitions item 5.

**Configuration** (Foundations › Configuration)
- No inventory of roles or hierarchy is derived.
- Producing, checking and accepting are separate responsibilities.
- A fresh context does not supply independence.
- Authority comes from grants, not names.

**Categorical claims** (Foundations › Orthogonal descriptions; Library › Composition law)
- A, I and C_H are held as hypotheses until objects, arrows and laws are supplied.
- Conformance, semantic equivalence, computational equivalence and categorical equivalence are kept distinct.

**Library structure**
- Bind/Acquire/Transform/Evaluate/Conjoin/Dispose are responsibilities, not stages.
- Evaluate forbids a parallel algebra.
- Dispose keeps the assessor's classification separate from the authoritative disposition.

---

## 2. Material defects

### D1. The core value space is undefined: verdict × performance combinations
**Heading:** Foundations › Result algebra

**Counterexample.** A WorkerResult `refused`, where the precondition was unmet and nothing was attempted, or an AC-013 `hold`, must map to "exactly one core value." The core record requires a verdict. The text also says a missing evaluation "supplies no fabricated child result."
- No verdict means "not evaluated."
- `indeterminate` is defined as "available evidence does not decide." That describes a performed evaluation.
- `out_of_frame` asserts a scope exclusion that has not been established.

Several combinations are left neither legal nor illegal:
- `{not_performed, satisfied}`
- `{not_performed, out_of_frame}`
- `{performed, invalid_basis}`

**Impact.**
- Mappers will diverge. Some will write `{not_performed, indeterminate}`.
- Any projection that carries only the verdict (a frame summary, a dashboard, a parent's view) then merges "not performed" with "undecidable." That breaks requirement 3, bullet 3, at the first lossy consumer.
- Requirement 2 ("maps to exactly one core value") cannot be checked when the codomain is unspecified.

**Minimum correction.** Add a table of legal combinations:
- `not_performed` ⇒ no verdict is present. State this explicitly as absence, not as a sixth value.
- `satisfied`, `falsified` and `indeterminate` ⇒ `performed`.
- State the performance for `out_of_frame` and `invalid_basis`. These are usually decided by a scope or basis check, which is a different predicate from the one in the slot.
- Require that no projection drops the performance field.

### D2. The fallback for a missing reason is non-deterministic and covers only the verdict
**Heading:** Foundations › Result algebra, paragraph "A domain refinement preserves…"

**Counterexample.** The text says: "Missing required reason or evidence leaves the claimed predicate indeterminate *or* invalid on its actual basis."

Take a `refused` with no reason, conjoined with a sibling that is `out_of_frame`:
- Mapper A picks `indeterminate`. The aggregate is `out_of_frame`.
- Mapper B picks `invalid_basis`. The aggregate is `invalid_basis`.

The same input produces two aggregates. The text also gives no default for performance when it is unknown whether the evaluation ran. The binary field cannot express that. Nor does it give a default for effect observation when a requested effect has no evidence.

**Impact.**
- This breaks "every refined value maps to exactly one core value."
- Aggregate outcomes depend on which mapper was used.
- A mapper may default the effect to `not_requested`, which violates requirement 3, bullet 4.

**Minimum correction.** Fix one rule. A contribution whose required reason or evidence is missing is unauthenticated for its slot:
- The slot remains the missing required evaluation, `not_performed` in the enclosing coverage, under the existing conjunction rule.
- The raw domain outcome is retained as evidence.
- Any requested effect without observation is `unknown`.
- `invalid_basis` arises only from a separate, authenticated basis finding.

### D3. Composition is defined only for the conjunction verdict
**Heading:** Foundations › Result conjunction. Requirement 6 is "conjunction *and composition* … defined once, over the core."

**Counterexample.** Conjoin R1 `{performed, satisfied, effect: completed}` with R2 `{performed, indeterminate, effect: unknown}`.
- The aggregate verdict is defined: `indeterminate`.
- The aggregate's own performance and effect observation are not defined.
- An implementation that reports the conjunction's effect as `not_requested` (because the conjunction itself performed none) presents an effect-uncertain composite as effect-free at the summary level. A Dispose that consumes the summary may then re-dispatch.

Sequential composition T;S, with T `falsified` and S not run, is only told to record S as `not_performed`. No rule gives the composite verdict, or says whether sequence is a conjunction of stage predicates.

**Impact.**
- Requirement 6 is unmet.
- Effect uncertainty can vanish at aggregation, even though the components retain it.

**Minimum correction.** Define:
- **Aggregate performance:** `performed` when the composite rule is applied, with component performances retained.
- **Effect join:**
  - Any `unknown` ⇒ `unknown`.
  - All `not_requested` ⇒ `not_requested`.
  - All in {`completed`, `not_requested`} with at least one `completed` ⇒ `completed`.
  - All in {`not_started`, `not_requested`} with at least one `not_started` ⇒ `not_started`.
  - Otherwise ⇒ `partial`, under D5's definition.
- **Sequential composition:** state that its result is the conjunction of the stage predicates over the declared composite basis, with downstream `not_performed` slots. Alternatively, declare it as its own operator under the same record.

### D4. Regrouping is presented as safe but does not preserve the verdict (unsupported associativity)
**Heading:** Foundations › Result conjunction, last paragraph. The sentence "associativity alone supplies no such permission" presupposes associativity.

**Counterexample.** Take A `falsified` (authenticated), with B and C `satisfied`.
- **Flat A∧B∧C** over an interpretable basis gives `falsified` (rule 1).
- **Grouped (A∧B)∧C:** suppose the intermediate composite basis for A∧B cannot be interpreted, for example because there is no declared join topology for the bases of A and B.
  - A∧B is then `invalid_basis` (the "composite subject or governing basis itself cannot be interpreted" clause overrides rule 1).
  - The outer conjunction sees `invalid_basis` and `satisfied`, and yields `invalid_basis`.

Regrouping changed `falsified` into `invalid_basis`. The failure survives in the components, but the verdict at every higher level no longer shows it.

**Impact.**
- Composition is not well-defined independently of how a planner nests evaluations.
- A known failure is demoted at the aggregate level. Standing is not raised, but the result is still order-sensitive. That runs against "defined once."

**Minimum correction.** Do one of the following:
- **(a)** State that the verdict is the maximum over the total order `falsified > invalid_basis > out_of_frame > indeterminate > satisfied`. Then state that regrouping preserves the verdict only when every intermediate composite basis is interpretable. Give the evidence class as mathematical argument.
- **(b)** Let an authenticated falsification of an independently valid required component dominate even when an intermediate composite basis is uninterpretable.

### D5. `partial` has no defined boundary against `unknown`
**Heading:** Foundations › Result algebra, effect observation paragraph

**Counterexample.** A two-step write: step 1 is acknowledged, step 2 is dispatched, and its acknowledgment is lost.
- If this is recorded as `partial`, a consumer reads it as "known incomplete" and re-dispatches step 2. Step 2 may have completed, so the effect is duplicated.
- The text defines when `unknown` applies, but not what `partial` asserts about the remainder.

**Impact.** This lets unknown completion map to a value that implies known non-completion of the remainder. That defeats the unknown-effect protection in requirement 3, bullet 4, and Bounded Transitions item 5.

**Minimum correction.** Define `partial` as "some but not all of the selected effect is observed to have occurred, *and* the remainder is observed not to have occurred." Any remainder that has not been observed makes the observation `unknown`, which may carry the observed completed parts as evidence.

### D6. Total handling has two owning loci in Foundations, and one introduces a second "algebra"
**Headings:** Foundations › Finite capacity and total handling, and Foundations › Bounded construction. The owner relation to DESIGN_MODULE_METHOD's totality rule is also involved.

**Counterexample.** The two loci define the same determination differently:
- *Finite capacity* covers "every input in its declared control domain." Its list is: failure, incomplete work, refusal, recovery, **exhausted authority**.
- *Bounded construction* covers "every admitted control state." Its list is: unavailable input, unknown world, failed preconditions, **partial effects**, **exhausted capability**.

A control contract that handles exhausted capability and partial effects, but not a grant revoked mid-run, is total under one locus and not total under the other. Finite capacity also says "an enclosing finite control algebra handles failure… truthfully." That is an unanchored second algebra. Nothing states that its outcomes are core results, but requirement 1 places stops and work results in the one algebra.

**Impact.**
- This violates Single Ownership items 1 and 7.
- It creates an implied rival algebra.
- DMM's "closed design handling" cannot name a single generic owner to refine.

**Minimum correction.**
- Make Bounded construction the single owner, using the union of both lists.
- Reduce Finite capacity to a reference.
- Replace "finite control algebra" with "finite control contract whose outcomes are core results."

### D7. The unknown-effect rule has several owners, one of them unanchored
**Headings:**
- Foundations › Workspace and context: "Before repeating an operation with uncertain effects…"
- Library › Work/recovery specialization, row 4: "Computed Classification And Treatment supplies the unknown-effect rule"
- Library › Transform: "Observe uncertain external effects before repeating them"
- Library › Recovery law

**Counterexample.** The library assigns "the unknown-effect rule" to Computed Classification And Treatment. That locus has no link and no member. Foundations states the same rule itself. If CCT's freshness or reconciliation policy permits a retry that Foundations would hold, there are two answers to one question and no stated precedence. Requirement 7 forbids resolving this by precedence.

**Impact.** This is competing ownership of the central recovery determination. The cited owner cannot be resolved from the subject.

**Minimum correction.**
- Foundations › Workspace and context owns the generic rule.
- Row 4 should say that CCT (with a link to its member and section) *refines* it with domain freshness and reconciliation policy.
- Transform and Recovery law should keep references only.

### D8. Misfit handling diverges between Foundations and Library
**Headings:** Foundations › Finite capacity ("the existing human authority named in RF-014 may select refinement, another actor…; the actor acts on an already authorized response, requests the owning decision, or stops") versus Library › Acquire ("refine under the grant, acquire a capable actor or return…")

**Counterexample.** Under the Library text, an actor facing a misfit may itself "acquire a capable actor." Under Foundations, choosing another actor belongs to RF-014's human authority, unless it is already authorized. The Library also omits "request the owning decision."

**Impact.**
- This gives two readings of who may reconfigure.
- One of them lets capacity pressure act as a configuration grant, which Foundations itself denies ("capacity supplies no configuration grant").

**Minimum correction.** Make Library › Acquire refer to the Foundations rule, or change its wording to "act on an already authorized refinement or reassignment, request the owning decision, or return…"

### D9. The Library restates UP-020's deciding conditions and assessor classes without a copy marking, and the classes are an outcome outside the core
**Headings:**
- Library › Evaluate, UP-020 paragraph (five assessor-disposition classes)
- Library › Dispose, last paragraph ("Accept requires… Local repair applies when… Re-entry applies when… Reject applies to…")
- Also Evaluate's "a Baseline Reviewer retains its evaluation-only grant"

**Counterexample.**
- If UP-020 routes a "violated governing relation" to re-entry when the relation itself must change, the Library's "Reject applies to a violated governing relation" decides the same case differently.
- The five assessor classes (cone preserved / local defect / needs re-entry / governing violation / undisposed competing path) are explicitly "assessment evidence" and have no map into the core. That leaves an outcome outside the core, which requirement 2 prohibits.
- The Baseline grant characterization makes a Baseline determination inside the Library, which says it assigns no role authority.

**Impact.**
- The deciding clauses have two owners. Foundations says "particular methods own their deciding clauses," and the Library does not mark these as non-owning copies (Single Ownership items 3 and 4).
- An assessment outcome has no core value.

**Minimum correction.**
- Replace the Dispose condition paragraph with a reference to UP-020, or mark it as a copy with an exact selector to UP-020.
- State that the assessor classification is the original domain outcome of a result on the cone-preservation predicate, and that UP-020 owns its map. For example: preserved → `satisfied`; the four others → `falsified`, with the class as the reason.
- Remove the "evaluation-only" characterization, or cite the Baseline as its owner.

### D10. Decision and disposition results have no core predicate form
**Headings:** Library › Dispose ("Other instances retain their original domain classifications as core refinements") and Foundations › Result algebra ("A decision result binds the mandate actually exercised")

**Counterexample.**
- `accept`, `reject`, `conserved` and `intentionally removed` are decisions, not verdicts on an assessed predicate.
- A naive map of `accept` → `satisfied` *on the cone predicate* merges acceptance with assessment, which violates requirement 5.
- A map of `reject` → `falsified` asserts a counterexample that may not exist, for example a rejection on policy grounds.
- The Library asserts these are core refinements, but the core never says what predicate a decision result is about.

**Impact.** Requirement 1 ("stops, work…") and requirement 5 cannot be met uniformly. Every owner will invent its own predicate.

**Minimum correction.** Add one sentence to Result algebra. A decision result's predicate is "disposition D on subject S at basis B was made under mandate M by the bound authority." Its verdict concerns that predicate, and never stands in for the verdict of the assessed predicate.

### D11. Stop and insufficiency results use vocabulary outside the core
**Headings:**
- Library › Foundational contract: "a truthful unknown"; "admitted insufficient/unknown outcome"; "The instance owns its admitted outcome set, including how it represents unknown or refused handling"
- Foundations › Workspace and context: "return the unresolved result"
- Foundations › Finite capacity: "explicit unresolved result"

**Counterexample.**
- "Unknown" is a core *effect* value, not a verdict.
- An instance told that it "owns how it represents unknown" may emit a domain `unknown` and map it to `indeterminate` with effect `not_requested`. That loses a dispatched-effect uncertainty.
- "Unresolved result" maps to nothing.

**Impact.**
- Stops, which requirement 1 names, have no stated mapping.
- The "unknown" for verdicts and the "unknown" for effects are conflated.

**Minimum correction.**
- Define a stop as a result on the destination or task predicate. Its verdict is typically `indeterminate`, it states performance, its effect observations are as observed, and its unresolved obligations field is non-empty.
- Replace "unknown/insufficient" in the Library with `indeterminate`.
- Change "owns how it represents unknown" to "owns its original outcomes; its map into the core preserves verdict and effect uncertainty per Result algebra."

### D12. Configuration: allocation of authority, the tier of the Executive paragraph, and the missing design obligation
**Heading:** Foundations › Configuration

**Counterexamples.**
- **(a)** "A configuration allocates operations, information *and permitted effects*." An Executive configuration that assigns a worker permission to publish is an allocation under this text, but under F6 it needs a delegable grant. Finite capacity requires "a separate applicable grant"; Configuration omits that condition.
- **(b)** "In a task-based Executive arrangement, the coordination frame holds… requests further bounded evaluation…" is a determination about an operational arrangement placed in the Foundations tier. Tier obligations assign the Executive procedure to an operational profile, so this competes with that owner.
- **(c)** Bounded Transitions item 4 requires that "its design explains the allocation, including material resource limits and assumptions about failure." The core never states this obligation or where it is recorded.

**Impact.**
- Configuration can be read as a source of authority.
- The Executive determination has two owners.
- Derived configurations carry no explanation obligation at the core.

**Minimum correction.**
- (a) Change the wording to "assigns effects only within grants the allocator holds and may delegate."
- (b) Mark the Executive paragraph as illustrative, or move it to the Executive procedure and reference it.
- (c) Add one sentence: the allocation is justified in the existing design or frame record against operations, dependencies, capabilities, assurance, resource limits and failure assumptions.

### D13. The core-owned families lack foundation-to-law accounting
**Headings:** Foundations › Result algebra, Result conjunction, Workspace and context, Configuration. Compare Foundations › Foundational commitments: "A family without that argument remains an unsupported specialisation."

**Counterexample.** By its own rule, Foundations leaves its own deciding families unsupported:
- None of these sections names its premises (F2/F5/F6, F3, F4).
- None separates consequences from choices.
- The conjunction precedence `invalid_basis > out_of_frame > indeterminate` is a policy choice with no owner named.
- Only work/recovery and transformation-admission get the argument, and the Library rightly does not present those two as covering every member.

**Impact.** Relationship 1 of the Standalone Successor Requirement is unmet for the core's own deciding contracts.

**Minimum correction.** Add a compact table of premises, consequences and choices (with owners) for the result algebra, conjunction (including the precedence order), workspace/context and configuration.

### D14. Symbol collision inside the Foundations bounded context
**Headings:** Foundations › Orthogonal descriptions (A = algorithmic account; C_H) versus Foundations › Bounded construction (A = current state; A → B → C)

**Counterexample.** "A -> I" and "A → B → C" occur in one context that claims ownership of "locally defined explanatory symbols." A reader of the categorical span cannot tell which A is meant.

**Impact.** The context's own bounded-context resolution is violated.

**Minimum correction.** Rename the state symbols, for example S₀ → S₁ → … .

### D15. "Independence" carries two senses in one paragraph
**Heading:** Foundations › Workspace and context, reuse paragraph. Library work/recovery row 3 also says "when independence is unproved."

**Counterexample.** The paragraph says "required independent authorship" (reviewer independence) and then "when independence cannot be established, inspect the wider affected scope" (independence from changed support). A reader may answer a failure of reviewer independence by widening scope instead of obtaining an independent assessor.

**Minimum correction.** Use "dependency independence" for the second sense and "assessor independence" for the first.

### D16. The Library redefines UP-014 and adds an ownerless selection rule
**Heading:** Library › Cost and contraction ("Method proportionality *is* ambiguity removed relative to effective reasoning complexity") and Library › Recovery law ("Use the cheapest focused proof…")

**Counterexample.**
- Foundations says UP-014 owns method-burden justification, but the Library supplies the definition without marking it as a copy.
- "Cheapest" has no stated measure. Cost and contraction says measures are selected per claim. "Cheapest" also has no owner, and it can select a same-author check where independence is required.

**Minimum correction.**
- Cite UP-014's definition rather than paraphrasing it.
- Change "cheapest" to "a proof adequate to falsify the affected relation, satisfying any required independence; its cost selection follows UP-014."

---

## 3. Dead, unanchored or competing references

| Location | Reference | Problem |
|---|---|---|
| Library › Work/recovery rows 3–4 | "Computed Classification And Treatment" | No member or link; claims ownership of the unknown-effect rule (D7) |
| Library › Work/recovery row 3 | "Ticket condition-based reuse" | No link to its section |
| Library › Transformation-admission | UP-021 ("alone owns admission…", "UP-021 admission owner") | No member or link; "admission owner" is unresolved |
| Library › Work/recovery rows 1–2; Foundations › Finite capacity | RF-003, RF-005, RF-014 | Unlinked; RF-014's "human authority" is relied on but not anchored |
| Library › Transform | AC-013 outcomes | Unlinked; no map supplied |
| Foundations › Reference-only imports | "the common outcome type below" | No such heading; it presumably means Result algebra |
| Foundations › Reference-only imports | "ODD runtime roles" | No owner or link |
| Both members | RF-012 and AC-007 | **Not referenced at all.** The two predecessor algebras that requirement 1 unifies are not named as superseded or refined, so they may remain live owners |
| Library › Work/recovery | `../plugins/spec/skills/stdo-work/SKILL.md` | A packaging-tier artifact is cited as the method's locus for recovery material; packaging owns no method determination |
| Foundations › Finite capacity | "finite control algebra" | An implied second algebra (D6) |
| Library › Dispose; UP-016; UP-020 | "competing truth path" disposition | Three loci touch the same question; ownership cannot be verified from the subject |

---

## 4. Outstanding integration (consumer files not supplied)

These cannot be judged as defects from the supplied text. Acceptance depends on them.

1. **RF-012 and AC-007 dispositions.** Each needs a UP-015 disposition (superseded, with the successor relation named, or conserved as a refinement with a map). This must be recorded in PREDECESSOR_CLAIMS and stated at the receiving loci.
2. **Refinement maps.** Each needs a total, reason-sensitive map that names Foundations › Result algebra as owner (Single Ownership item 3):
   - WorkerResult (`candidate_ready`/`refused`/`incomplete`/`re_entry_requested`)
   - AC-013 (`M_b_prime*`/`hold`/`gap`/`refusal`)
   - AC-007 constraint and refusal outcomes
   - Ticket sprint/paydown and closure
   - Release UP-015 dispositions
   - UP-020 assessor classes and dispositions
   - ODD outcomes
   - DMM admission outcomes
3. **Requirement 7.** Each frame catalogue whose task returns a result must carry the core algebra or the profile's map.
4. **Relationship 2 (use points).** The Spec Method and profiles must apply Bind/Acquire/Conjoin/Dispose and the result algebra where actors enter them, not only by cross-reference.
5. **UP-020, UP-016 and UP-021.** Confirm that the Library's Dispose and Evaluate text matches UP-020 exactly or is removed (D9), and that a single owner decides competing-path disposition.
6. **DMM's totality rule** must refine the single Foundations totality owner (D6).
7. **Configuration explanation** (Bounded Transitions item 4) must appear in existing design and frame records (D12c).
8. **Build-Tenant Binding.** This is not addressed in these members. That is acceptable only if the Spec Method states and applies it.
9. **Ticket "condition-based closure."** The Library places recording under *operation* authority. Ticket Method must confirm which *decision* authority the closure exercises.

---

**Summary.** The core's semantic intent is sound in the areas reviewed:
- The verdict, performance and effect distinctions.
- Prohibiting a raise in standing.
- Keeping candidate, fitness and acceptance separate.
- The context as a disposable account of a persistent workspace.
- Non-hierarchical configuration.
- Holding categorical claims as hypotheses.

The material gaps are in four areas:
- **The codomain and composition of the algebra:** D1–D5.
- **Single ownership of recovery, totality and disposition rules:** D6–D9 and D16.
- **Decision and stop results:** D10–D11.
- **The core's own foundation-to-law accounting:** D13.

Each gap has a bounded correction. The integration items in section 4 cannot be judged until the consumer files are supplied.
