# Integration review: candidate 875a56e3 against preimage 5b4aebb

## Coverage

I read COMMON first, then CORE (Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, Core contract derivations), then the diff hunks for `RELEASE_METHOD.md`, `SPEC_METHOD.md` and `TICKET_METHOD.md`.

I saw only the changed text plus about 15 lines of context per hunk. I did not see:
- the omitted bodies of those three members;
- the rest of `FOUNDATIONS.md`;
- `TRANSFORMATION_LIBRARY`, `REFERENCE_FRAME_METHOD`, `DESIGN_MODULE_METHOD`, `PRINCIPLES`, `PREDECESSOR_CLAIMS`.

Findings marked *coverage-conditioned* may already be discharged by text I did not see. This is a working source check, not acceptance of any member and not approval of the review policy.

---

## F1 (high): An override admission maps `falsified` to `satisfied`

**Location:** `TICKET_METHOD.md` → *Execution Contract Admission*

**Text:** "`admitted` maps to `satisfied`". The section keeps "without deterministic admission or explicit human override".

**Counterexample:**
1. Deterministic admission finds a demonstrated violation, so the admissibility predicate is `falsified`.
2. A human override then sets the carrier state to `admitted`.
3. The map turns that into `satisfied` for "this exact contract is admissible under this cited work authority and basis".

**What it contradicts:**
- COMMON *Single Result Algebra* item 3: a falsified result never maps to satisfied.
- CORE: "A new result over a different predicate does not overwrite the earlier result."
- CORE: "Recording the decision is not its authority."

**Repair:** "`admitted` maps to `satisfied` only where deterministic admission established the predicate. An explicit human override is a decision result on its own predicate (override of this exact contract under the bound authority); it leaves the admission evaluation's verdict unchanged."

## F2 (high): `local_repair` is not reason-sensitive, and proof gaps lose their predecessor remedy

**Location:** `SPEC_METHOD.md` → *Proportional Disposition*

**Text:** "`local_repair` | a demonstrated implementation or proof defect defeats the claim … | `falsified`". It is followed by "Insufficient evidence returns `indeterminate` … without … forcing a disposition".

**Counterexample:** The implementation is correct, but its proof omits a required relation case, or a test asserts the wrong expectation.
- That is not a counterexample to "the candidate closes its declared cone and preserves every affected governing relation". Under CORE `falsified` ("establishes a counterexample") it should be `indeterminate`.
- If it is mapped `falsified`, the verdict is wrong.
- If it is mapped `indeterminate`, the text forbids attaching a disposition. The predecessor's `local_repair` for "proof is locally defective" then has no path.
- The predecessor's assessment always returned a disposition. CORE *Bounded construction* requires a total control contract.

**Repair:** Make the row reason-sensitive. A demonstrated implementation defect maps to `falsified`. A proof defect or proof gap maps to `indeterminate` on the candidate claim; it is `falsified` only on the proof's own predicate. `local_repair` may accompany `indeterminate` as the proposed remedy.

## F3 (medium): `re_enter` and `invalid_basis` decide the same case two ways

**Location:** `SPEC_METHOD.md` → *Proportional Disposition*

**Counterexample:** An accepted requirement and the accepted design in the cone contradict each other.
- The table says `re_enter`/`falsified`, because no candidate "can satisfy the current contract without changing" them.
- The paragraph says "an unusable basis returns `invalid_basis` … without forcing a disposition".
- CORE *Result conjunction* requires the declaration to fix whether such a relation is an admission condition or a material join: "The result names that declared role".
- The predecessor routed this case to `re_enter` ("requirement … or accepted design must change").

**Repair:** "Coherence of the governing basis is an admission condition of this assessment. When it fails, the verdict is `invalid_basis` and `re_enter` may accompany it as the proposed remedy. `re_enter`/`falsified` applies when the contract is coherent but the intended candidate cannot meet it."

## F4 (medium): Re-entry paths still name `Code` after the chain link became `Realisation`

**Location:** `SPEC_METHOD.md` → *Constitutional Chain*, and the change classes in the intake-triage section

**Text:** The chain now reads "Design → Realisation → Observations", and "code is the software case". The context lines are unchanged:
- "Repricing updates … design, or code";
- every change class "flows through … Design, Code, and Evidence";
- "code without a design decision — creates accidental law".

**Counterexample:** A human-process tenant takes a `design_reframe`. Read literally, the re-entry path passes through Code, which does not exist for that tenant. Its performed procedure is never re-entered. This loses the predecessor obligation that realisation follows design, and it conflicts with COMMON *Build-Tenant Binding* item 2.

**Repair:** Replace `Code` with `Realisation` in the repricing bullet, the accidental-law sentence and the change-class lines. Alternatively, add one sentence: "In these paths Code names the tenant's Realisation."

## F5 (medium): A withdrawn obligation can reach `completed` and read as delivery

**Location:** `TICKET_METHOD.md` → *Allowed Status*, together with *Repricing* and *Condition-Based Closure And Reuse*

**Counterexample:** Ticket T has one obligation, O1. Repricing withdraws O1.
- Closure is evaluated over "every applicable declared obligation". That set is now established empty by the withdrawal decision, so CORE rule 4 allows `satisfied`, and T moves to `completed`.
- The base status model has no other terminal state, because `cancelled` is optional.
- A consumer reading the completed lane counts T as delivered. Repricing forbids exactly that: "Withdrawal or deferral cannot be projected as successful delivery".

**Repair (in *Allowed Status*):** "Where obligations were withdrawn or deferred, `completed` carries those decision results; the lane does not assert delivery of a withdrawn or deferred obligation."

## F6 (medium): The admission and qualification maps are not total in the way CORE requires

**`TICKET_METHOD.md` → *Execution Contract Admission*:**
- "A reason accompanies every refusal" is stated as a duty.
- CORE requires the map to include "an explicit missing-reason case".
- A `rejected` with no reason, or with an unlisted reason, has no mapping.
- **Repair:** "A `rejected` without its required reason maps to `indeterminate`, inadmissible as deciding support, retaining the raw outcome."

**`RELEASE_METHOD.md` → *Exact-Cut Qualification*:**
- "A passed item maps to `satisfied`" has no performance condition.
- **Counterexample:** a runner reports `passed` with zero tests collected or all of them skipped, or a cached `passed` comes from a job whose run on this cut is unconfirmed.
- The result is `satisfied` paired with `not_performed`/`unconfirmed`, which CORE marks as an illegal pair ("Satisfaction requires the declared procedure's conclusion"; "An empty list proves nothing").
- **Repair:** "…maps to `satisfied` only when its declared procedure concluded (`performed`) on the exact cut with its required coverage."

## F7 (medium-low): An event recording an effect is demoted below current observation

**Location:** `SPEC_METHOD.md` → intake triage paragraph

**Text:** "An old conversation, event or work summary supplies a route to evidence, not a veto on current reality."

**Counterexample:**
1. An event records an irreversible notification sent to a customer.
2. The local workspace holds no trace of it.
3. Triage treats the event as only a route, observes "current reality", calls the event a stale belief and recommends resending.

This conflicts with CORE: "Conflicting or insufficient observations leave the part unknown"; "A later timestamp alone is no supersession argument"; "An empty local log … does not establish no effect".

**Repair:** Append: "An event that records an effect is an effect observation; a later observation supersedes it only with a supported supersession argument, otherwise the effect is `unknown`."

## F8 (low-medium): Completing a publication later can pass as an atomic cohort

**Location:** `RELEASE_METHOD.md`, in two places:
- the new publication paragraph: "complete or repair only the still-authorised missing relation";
- *Qualification And Recovery*: "use the existing authorised recovery relation".

**Counterexample:** A non-atomic push leaves a partial cohort. Some actor completes the missing refs. Post-publication qualification "verifies the same relation from remote refs" and now passes. This is exactly what the next paragraph forbids: recovery "represented as an atomic cohort that existed at the original publication". For this case, the visible text never says which relation is still authorised.

**Repair:** "A cohort completed after partial publication retains that history in its publication result and is not qualified as atomic; completion requires the separately authorised recovery law below, otherwise the result stays unresolved."

## F9 (low): Required judgments and rulings are bound but not conjoined

**Location:** `TICKET_METHOD.md` → *Condition-Based Closure And Reuse*

The predecessor required "all required judgments and owner rulings are present and applicable". The successor's predicate names only obligations and non-closure conditions, and says "Bind … the required judgments and rulings before conjoining".

**Repair:** "Each required judgment and owner ruling is a required conjunct; an absent or inapplicable one is uncovered."

---

## Coverage-conditioned items

**Build-Tenant Binding (`SPEC_METHOD.md` → *WHAT, HOW, And Work Carriers*).** The visible text covers COMMON items 1 and 4 in part. I do not see:
- **Item 2:** author identity, actor identity and operation kind kept distinct; a person performing an operation is not thereby human adjudication.
- **Item 3:** units and boundaries, human effort, and operational assumptions. Only "measured at the boundary" appears.
- **Item 5:** a calculus may be reused across tenants. "its computational calculus" does not forbid reuse, but does not state it.
- **Item 6:** an a_c representation neither prescribes the executor nor establishes conformance by structural validation alone.

If none of these appears elsewhere in the member, they are missing obligations. Each needs about one sentence in this section.

**UP-015 disposition rows (`PREDECESSOR_CLAIMS`, unseen).** These predecessor claims changed meaning and each needs a `superseded` row that names its successor locus:
- "Events record what actually happened" / "Projection reconstructs current truth from the event stream";
- "logged in runtime/event truth" (two places in Ticket Method);
- "Assessment returns one of these semantic dispositions", now a proposal applied only by decision authority;
- the predecessor "proposed restart" clause, now split into ordinary restart and discard/rebuild.

## Checked with no finding

- **Release publication predicate and transport `unknown`:** consistent with CORE effects.
- **Qualification vs owner decision vs adoption:** the predicates are kept separate.
- **"An unperformed decision remains `not_performed`":** consistent with CORE's absent-slot rule.
- **Spec separation of assessment and decision results, including a lawful `reject` without a counterexample:** matches CORE.
- **Sufficient Execution Intake addition:** consistent with CORE.
- **Ticket repricing dispositions as decision outcomes:** consistent with CORE.
- **Status values declared "not a second result algebra":** consistent with CORE.
- **Recorded Judgment reuse delegated to CORE:** CORE's supported-applicability rule conserves the predecessor's revising-observation and independence clauses.
