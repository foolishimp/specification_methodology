--- v2/standards/ODD_METHOD.md
+++ v3/standards/ODD_METHOD.md
@@ -1,6 +1,57 @@
 # ODD Method
+
+<!-- STDO3_PROFILE_BINDING_START -->
+## Governing Relations
+
+This member is the graph-native ODD constitutional method surface of STDO;
+its declared obligations apply in a Product-declared ODD scope under lawful activation.
+It maps [Foundations](FOUNDATIONS.md) and the
+[Transformation Library](TRANSFORMATION_LIBRARY.md). Availability, Product
+adoption and execution-scoped activation remain distinct relations;
+availability supplies no Product semantics, concrete runtime identity or grant.
+Related owner routes are [Spec Method](SPEC_METHOD.md),
+[Design Module Method](DESIGN_MODULE_METHOD.md),
+[Reference Frame Method](REFERENCE_FRAME_METHOD.md),
+[Ticket Method](TICKET_METHOD.md) and [Release Method](RELEASE_METHOD.md), each
+under its own applicability. This list adds no dependency to the composition
+declared below; release remains a separate process surface.
+[World Model Method](WORLD_MODEL_METHOD.md) and [UX Method](UX_METHOD.md)
+retain their separate applicability and semantic owners.
+
+The premises are an adopted ODD outcome, a published typed traversal contract,
+an admitted basis and capable bounded actors. Shared
+[bounded construction](FOUNDATIONS.md#bounded-construction) then requires each
+traversal to preserve its enclosing obligations, and
+[workspace and context](FOUNDATIONS.md#workspace-and-context) requires current
+observation before relying on a remembered work state. Scoped identity and
+authority prevent a capable worker or a read model from acquiring undeclared
+control.
+
+ODD makes additional choices: graph-native actions, cumulative typed
+environments, admitted runtime facts and the consequence loop below. These
+choices apply in the adopted scope; finite context alone does not require a
+graph executor, event log or particular actor hierarchy. Consumer-bound ODD,
+GTL and ABG roles select no concrete package and transfer no Product meaning.
+
+| Shared operation | ODD deciding consumer |
+|---|---|
+| Bind | Recover the selected Product outcome, any admitted bounded prerequisite or experiment, IntentLineage, exact target obligations, published action contract, execution basis and consumer-bound authorities. A target or controller label supplies no authority. |
+| Acquire | Observe the worksite, runtime facts and admitted source truth; retain current gap pressure, structural source coherence and lineage-reachable evidence. Observation, model synthesis and admitted evidence remain different relations. |
+| Transform | A published action under the exact A3/A14 action-publication contracts performs bounded construction under the admitted vector contract. The worker retains internal HOW, produces required evidence for owning native admission and returns control to the bound ABG authority. This row grants no runtime-event or ledger mutation. |
+| Evaluate | The exact §11.5D function table owns one synthesis and three evaluation functions: synthesize_model -> ProductAssetModel; eval_gap -> ObservationSnapshot + GapPressureRow; evaluate_action -> EdgeFulfillmentLedger + EdgeClosureDecision; evaluate_next -> PriorityProjection + NextActionProjection + selected_action, including the typed no-action result while post_reprice is unresolved. No name or partial output in this account replaces that table or confers Reviewer control. |
+| Conjoin | Compatible published refinements and cumulative environments preserve their outer contract, exact producer coordinates, admitted evidence, unresolved obligations and zoom-stable closure. A local green path does not decide enclosing acceptance. |
+| Dispose | evaluate_action folds admitted evidence into EdgeFulfillmentLedger and EdgeClosureDecision under F_D/ABG/product admission. Separately, evaluate_next consumes that admitted decision and fresh eval_gap truth to produce its exact next-action outputs; it cannot decide prior closure. ABG admission/traversal authority separately admits ConstructionIntent. A11's conceptual disposition versus invocational selection and the no-rival-control-path law remain operative; this row appoints no replacement owner. |
+
+The consumers below return the shared [result record](FOUNDATIONS.md#result-algebra)
+and use [result conjunction](FOUNDATIONS.md#result-conjunction) for required
+obligations. Domain decisions retain their original outcome and exact predicate.
+The operations add no compulsory six-stage workflow, runtime API or categorical-equivalence
+claim. The IntentLineage-to-NextActionProjection loop applies within a selected
+ODD scope.
+
+<!-- STDO3_PROFILE_BINDING_END -->
 
 ## 1. Position
 
 `ODD_METHOD.md` exists to make one instruction precise:
 
@@ -260,10 +311,20 @@
 contract invalidates the affected specialization until reevaluated.
 
 The method governs the traversal contract, evidence, provenance, and control
 truth. It does not make the framework the executor of the domain's internal
 solution strategy.
+
+The traversal return uses the shared
+[result record](FOUNDATIONS.md#result-algebra) for every compute means. An
+`F_D` success establishes only its declared decidable predicate; an `F_P`
+candidate establishes only availability; fitness and acceptance remain separate.
+An
+`F_H` decision records the exact mandate exercised rather than unlimited human
+authority. Each binding declares evidence, permitted stops, recovery and
+effect observations. The implementation follows the
+[Spec Method tenant binding](SPEC_METHOD.md#what-how-and-work-carriers).
 
 ### Graph Functions
 
 Graph functions are named constructive programs that realize vectors.
 
@@ -671,10 +732,17 @@
 - checkpoint overlays
 - provenance overlays
 - domain-specific explainability overlays
 
 It must not redefine ABG runtime facts.
+
+This projection describes admitted runtime facts, not the whole material
+workspace. The workspace remains the current reality being constructed. Fresh
+observation can expose divergence from an earlier projection or belief;
+admission then records the relevant evidence under the existing authority.
+Discarding private actor context does not discard that workspace or require
+replaying every historical body into the next actor's frame.
 
 ### 11.5A ABG Owns Continuation And Re-Entry
 
 An ODD application over GTL/ABG is a cooperative subsystem, not a replacement
 runtime.
@@ -938,16 +1006,28 @@
 ```
 
 The consistency rule is:
 
 ```text
-W can change without being true.
+W can change without satisfying the governed contract.
 L can be true without being the whole W.
 Closure can only use W through L.
 Eval can only judge W through L.
 Eval only affects traversal after its own L/E admission.
 ```
+
+Here `true` qualifies an admitted claim, not the existence of the workspace.
+L cannot overrule contrary current observations of W. The evidence-admission
+owner admits the supported observation and the affected currentness uncertainty
+into L/E under the existing evidence contract before dependent closure or
+next-action selection. Those consumers read that admitted evidence through L;
+while its interpretation is unresolved, the affected claim is not reused as
+current support. Recording the observation supplies no verdict on the claim.
+Its admitted interpretation invalidates affected claims through the declared
+re-entry relation. Missing admission supplies no currentness proof. It is not
+silently discarded because the earlier ledger is immutable. The immutable
+history remains an account of what was admitted at its stated basis.
 
 Every closure-relevant F_P callout that does work needs ledger admission.
 Evaluator work is not outside F_P merely because it reads ledgers. Evaluator work
 is F_P work over governed ledger state, and its result must be admitted into the
 immutable ledger/event spine before it can affect closure, routing, or traversal.
@@ -1067,10 +1147,19 @@
 AdmittedEvidence
 -> EdgeFulfillmentLedger
 -> EdgeClosureDecision
 ```
 
+`evaluate_action` consumes the admitted `TargetObligationBinding` and its required
+evidence set, fixed before the action, before folding them with the shared
+[result conjunction](FOUNDATIONS.md#result-conjunction). A known falsified
+obligation and its citations survive alongside a different unassessed
+obligation. Missing evidence, a worker that did not run and uncertain effects
+remain explicit; none becomes success through an empty fold, a green sibling
+or a smaller target selected after the action. The admitted fold is the basis
+of the closure decision, not permission for the evaluator to select new work.
+
 **A7. Ledger Is Evidence, Not Action Selector**
 
 `EdgeFulfillmentLedger` records evidence and convergence:
 
 ```text
@@ -1100,19 +1189,53 @@
 ```
 
 Each disposition is replay-visible and must carry basis and reason refs
 sufficient to reproduce the decision.
 
+These are domain dispositions refining the shared
+[result algebra](FOUNDATIONS.md#result-algebra), not a competing verdict set.
+The `EdgeClosureDecision` result binds the predicate that this disposition was
+lawfully issued for this subject, current basis and mandate. Satisfaction of
+that decision predicate requires its F_D/ABG/product admission; an unadmitted
+evaluator proposal supplies no admission fact. A lawful decision
+can be `satisfied` while the edge's fitness remains falsified or unresolved.
+The ledger retains the separate obligation assessments that justify that
+decision, with their predicates, performance, evidence and effects:
+
+- `close` requires `satisfied` for the complete declared edge-closure predicate;
+- a demonstrated obligation violation is `falsified` even when the disposition
+  selects `repair`, `retry`, `re-enter`, `reprice`, `block` or `yield`;
+- an undecided closure predicate is `indeterminate` only when core conjunction
+  has no deciding falsification, invalid basis or out-of-frame result; pending
+  work or evidence remains visible, including on a productive `yield`;
+- an unusable basis is `invalid_basis`; a request outside the admitted action
+  domain is `out_of_frame`;
+- an unperformed evaluation retains `performance = not_performed`; the
+  worker's non-start is a separate observed fact about the assessed work and
+  its effects, not non-performance of an evaluation that actually ran.
+
+If the evaluation's performance cannot be established, retain `unconfirmed`;
+report the worker's observed execution and effects separately. The predicate follows the core legal
+pairs, including any independently established counterevidence or diagnosis.
+The decision's complete return preserves its original domain disposition and
+the ledger's assessment records. It cannot relabel an obligation failure as a
+successful product outcome. Each result therefore has one verdict on its own
+explicit predicate; the disposition determines permitted subsequent treatment.
+`evaluate_next` separately judges lawful next-action selection. A valid typed
+no-action return can satisfy that selection contract while the product remains
+incomplete; it cannot satisfy the product-completion predicate. This mapping
+preserves A9: yielding is not itself evidence of semantic failure.
+
 **A9. Yield Is Lawful Iterate**
 
 `yield` is the lawful iteration boundary:
 
 ```text
 same edge or attempt remains lawful
 progress or waiting state is admitted
 resume basis is replay-visible
-control returns without failure classification
+the yield disposition adds no failure classification; retained assessments remain
 ```
 
 Yield is not retry. Yield is not block. Yield is not timeout. Yield is not a
 local CLI loop. It is the pressure-release state that lets long-running,
 bounded, or partially productive work return control without losing the current
@@ -1161,10 +1284,18 @@
 + visible policy refs
 ```
 
 If replay cannot reproduce the decision, the implementation has created hidden
 state.
+
+Replayability does not require retaining the complete ledger in an actor's
+context or redoing still-valid evaluations. Acquire the sufficient reachable
+subset for the selected action, checking its basis and invalidators. After an
+interruption, observe the current worksite and reconcile any `unknown` or
+`partial` effect before a dependent repeat. Current admission and replay then
+reconstruct lawful control without resetting the workspace. A lost response
+after invocation is not evidence of `not_started` or `completed`.
 
 **A13a. Causal Chain Integrity**
 
 Each governing admitted or replay-derived carrier and projection in the loop
 must reference its causal predecessor refs:
@@ -1265,11 +1396,14 @@
 service method output
 ```
 
 If any of those artifacts conflict with the admitted `EdgeFulfillmentLedger`,
 `EdgeClosureDecision`, or `NextActionProjection`, the ledger, decision, and
-projection chain wins. If that chain is absent, the edge has not
+projection chain governs admitted closure and next-action selection. A contrary current
+observation still triggers affected re-observation and evidence admission
+under A1; historical admission does not prove present conformance. If that
+chain is absent, the edge has not
 constitutionally closed and the next action has not been constitutionally
 selected.
 
 The constitutional equation is:
 
