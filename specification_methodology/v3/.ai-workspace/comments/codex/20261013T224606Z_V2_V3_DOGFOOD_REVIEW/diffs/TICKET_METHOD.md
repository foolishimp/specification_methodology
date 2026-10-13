--- v2/standards/TICKET_METHOD.md
+++ v3/standards/TICKET_METHOD.md
@@ -1,6 +1,17 @@
 # Ticket Method
+
+This work-carrier member binds the shared [transformation library](TRANSFORMATION_LIBRARY.md)
+to durable work identity, admission, recording and closure. Given finite actor
+context and obligations that may outlive it, continuing work needs a recoverable
+source independent of private memory. The
+[workspace/context relation](FOUNDATIONS.md#workspace-and-context) supplies that
+requirement; Work-Carrier-To-Execution chooses the smallest carrier for its
+actual lifetime. Tickets, sprints and the default file layout are this member's
+additional policy, not universal consequences of finite capacity. Admission and
+closure consume the shared [result algebra](FOUNDATIONS.md#result-algebra) and
+[conjunction](FOUNDATIONS.md#result-conjunction) at their deciding boundaries.
 
 ## Core Model
 
 ### Goals
 
@@ -93,11 +104,11 @@
 
 They exist so the system can:
 
 - classify the work before execution
 - admit or reject the drafted classification against deterministic criteria
-- log the admitted execution basis into runtime/event truth
+- record the admitted execution basis on the selected durable work surface
 - assemble prompts from admitted work law instead of from raw user phrasing
 - evaluate closure against the same admitted criteria
 
 So the intended loop is:
 
@@ -707,16 +718,43 @@
 - `rejected`
 - `superseded`
 
 An admitted execution contract should be:
 
-- logged in runtime/event truth
-- available to prompt assembly
+- recorded in the selected work carrier, including an event log when that is
+  its declared realisation
+- available to frame or prompt assembly
 - available to later closure checking
+
+Admission evaluates `this exact contract is admissible under this cited work
+authority and basis`. Its result preserves the original admission outcome:
+`admitted` maps to `satisfied` when the admission evaluation establishes that
+predicate; `rejected` with a demonstrated violation maps to
+`falsified`; missing deciding evidence maps to `indeterminate`; missing
+admission scope or capability maps to `out_of_frame`; and unusable authority
+or subject coordinates map to `invalid_basis`. A reason accompanies every
+refusal. For every original outcome, including an `admitted` label whose claim
+is not established, apply the [core result law](FOUNDATIONS.md#result-algebra)
+and its legal performance pairs. Missing deciding support gives `indeterminate`;
+the label cannot override separately admissible counterevidence or a basis/scope
+diagnosis. Missing required reasons follow that same core law. A required
+admission evaluation with no result remains an absent slot, with its known
+performance or uncertainty; a carrier state does not fabricate a result.
+`drafted` and `superseded` are carrier states, not evaluation verdicts.
+An old admission is not a current grant merely because its text remains in
+the workspace. Neither admission satisfaction nor `active` status establishes
+that the admitted work has been performed or completed.
 
 The system must not allow the model to silently self-certify its own execution
 basis without deterministic admission or explicit human override.
+
+An explicit override has a separate decision result on the exact contract and
+bound mandate. It can authorise work only within that mandate and leaves the
+admission evaluation's existing verdict intact. If no evaluation result exists,
+its required slot remains absent with the known performance fact or uncertainty;
+the override supplies only its own decision result and bounded authority. The
+carrier's `admitted` state cannot convert failure or absence into satisfaction.
 
 Execution-contract admission validates a proposed contract against its cited
 Product outcome, prerequisite, or experiment basis; it does not admit that
 growth basis. Admission or renewal of the basis belongs to the authority owning
 the selected Goals work wave, or its explicitly bounded proxy, and remains
@@ -782,17 +820,19 @@
 computed facts/evidence, responsible actor and authority, conclusion and
 scope, uncertainty, and a concrete revising observation. That observation must
 let a consumer determine whether the conclusion still applies. A rule-settled
 question needs no invented J record.
 
-Later roles and resumed runs recover the result and check applicability rather
-than re-author unchanged judgment. Changed material evidence, basis or the
-stated revising observation causes affected reassessment, preserving the
-original result and its successor relation. Retain unrelated conclusions only
-where their independence from the change is supported. A new role or
-conversation alone is not an invalidator. The result may reference current C
-outputs; reuse cannot silently turn unknown facts into established premises.
+Later activations apply the core
+[workspace/context validity rule](FOUNDATIONS.md#workspace-and-context) to the
+recorded result. They observe the relevant current workspace and check the
+question, exact basis and revising conditions rather than re-author unchanged
+judgment. Preserve the original result and its successor relation when
+reassessment is required. The result may reference current C outputs; reuse
+cannot silently turn unknown facts into established premises. Recovery does not
+require a complete historical transcript when the current state and valid
+evidence suffice. Unknown effects still require their owning observation.
 
 Required independent assessment may consume valid C, but its assessor acquires
 sufficient exact evidence and supplies its own judgment under the actual
 independence condition. Reusing the author's J cannot satisfy that condition.
 
@@ -814,10 +854,16 @@
 dependencies; copy no unaffected history into a parallel ledger. Present an
 owner decision as the short consequence delta needed to decide it while
 preserving the original ruling separately. A general instruction to continue
 does not accept an undisclosed architectural or scope change.
 
+These disposition words remain the original domain outcomes of decision
+results under the core contract. Their predicate concerns the authorised
+disposition on the exact obligation and basis, not whether the original
+delivery obligation has been fulfilled. Withdrawal or deferral cannot be
+projected as successful delivery.
+
 ### Bounded-Context Term Binding
 
 Ticket and work-instruction terms resolve under `SPEC_METHOD.md`'s
 Bounded-Context Semantic Resolution law. A ticket may use an unqualified term
 when its cited Product, re-entry surface, execution basis, and affected scope
@@ -866,30 +912,37 @@
 non-closure condition by itself. It may be deferred only under the
 path-relative authority and explicit disposition rules in `SPEC_METHOD.md`.
 
 ### Condition-Based Closure And Reuse
 
-A work claim is complete only when every applicable declared obligation is
-satisfied by valid evidence for its exact subject, basis and scope, all required
-judgments and owner rulings are present and applicable, and no active
-non-closure condition remains. A mandatory but unknown applicability or
-insufficient-evidence result withholds the dependent claim; evidence presence
-alone is not satisfaction. The existing owner decides any reserved acceptance.
+Closure evaluates `every applicable declared obligation of this exact work
+claim is satisfied and no active non-closure condition remains` through
+[core conjunction](FOUNDATIONS.md#result-conjunction). Bind the obligation set,
+each predicate and its subject/basis before conjoining, including every required
+judgment and owner ruling as a required conjunct. Each ruling is evidence for
+the exact disposition that closure requires on this subject and basis under
+its mandate: for example, `the authorised owner accepted this exact subject`.
+Lawfulness of a different disposition does not satisfy that predicate. Retain
+the original ruling and its own decision result rather than relabeling it as
+the required acceptance. A known failure remains visible when another obligation
+has no assessment. Missing or unknown applicability cannot become satisfaction.
+The core result records the original closure outcome, actual performance,
+effects and residuals; evidence presence alone is not completion. The existing
+owner decides any reserved acceptance.
 
 Review evaluates these conditions; its occurrence is not the closing event.
 Where applicable law requires no independent review or reserved acceptance,
 the authorized Writer may record the satisfied bounded result in the existing
 carrier without adding a ticket, Executive appointment, review or design-view
 recreation solely to mark completion. This does not waive a condition that
 actually applies, including sprint-close or design-method law.
 
-An unchanged obligation reuses valid applicable evidence and recorded J/O.
-A material counterexample, changed evidence or basis invalidates the affected
-claim and its dependent results before further reliance. An unrelated
-observation is retained as bounded repricing input; it does not reopen a
-satisfied claim or expand work automatically. Closure recording preserves the
-exact evaluated scope, satisfied conditions, evidence and remaining residuals.
+Reuse and invalidation follow the core current-state contract and Recorded
+Judgment And Owner-Ruling Continuity. An unrelated observation is retained as
+bounded repricing input; it does not reopen a satisfied claim or expand work
+automatically. Closure recording preserves the exact evaluated scope,
+satisfied conditions, evidence and remaining residuals.
 
 ### Test Case Authority
 
 Tests are proof projections from admitted work authority.
 
@@ -1288,10 +1341,18 @@
 
 Projects may add `blocked`, `cancelled`, or other explicit local states later
 if needed, but the base method starts with `backlog`, `active`, and
 `completed`.
 
+These values select work-carrier state, not a second result algebra. A claim
+that a state transition is valid carries its own core result and exact
+predicate. `completed` is recorded only after Condition-Based Closure And
+Reuse holds, including any required owner decision; lane placement cannot
+make it hold. A cancelled activity does not thereby satisfy its original
+delivery predicate. Where obligations were withdrawn or deferred, completed
+carrier state retains those decisions and does not assert their delivery.
+
 ### Ticket Lanes
 
 Backlog tickets live at the Product Definition Overlay's
 `ticketing.tickets.lanes.backlog` binding. The default is:
 
