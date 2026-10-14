--- v2/standards/STDO_REFERENCE_FRAME_BASELINE.md
+++ v3/standards/STDO_REFERENCE_FRAME_BASELINE.md
@@ -4,10 +4,11 @@
 
 `REFERENCE_FRAME_METHOD.md` defines the finite engagement atom. The selected
 complete STDO cut defines specification, design, construction, assessment,
 disposition, checkpoint, continuation, identity, and release law. This profile
 maps three practical engagement frames onto those existing owners:
+
 
 ```text
 existing project authority
   + selected complete STDO and Reference Frame Method basis
   + exact governed Product or Product-chain outcome and workspace basis
@@ -19,10 +20,26 @@
   -> existing bounded decision authority, result recording, and next lawful action
   -> updated basis, coverage, residuals, and frontier
   -> repeat or stop
 ```
 
+The [configuration relation](FOUNDATIONS.md#configuration) derives the need to
+allocate bounded tasks from finite context, finite attention, dependencies,
+capabilities and assurance requirements. It does not derive one hierarchy or
+an exhaustive role inventory. This optional profile chooses three useful task
+frames: construction, independent assessment where required, and coordination
+where long-term delivery cannot be covered by the direct work frame. Their
+labels are Worker, Reviewer and Executive. Other admitted configurations may
+use a single sufficient frame, peers or adaptive allocation.
+
+This profile consumes the [shared result algebra](FOUNDATIONS.md#result-algebra),
+[conjunction](FOUNDATIONS.md#result-conjunction) and
+[workspace/context relation](FOUNDATIONS.md#workspace-and-context). The
+[transformation library](TRANSFORMATION_LIBRARY.md) supplies reusable
+responsibilities. Exact operation grants and Product-owned adoption retain
+their separate authority; the selected configuration cannot grant it.
+
 The three available frames are overlapping evaluation contexts, not a hierarchy
 or actor topology. The Worker supplies the candidate subject but never activates the
 Reviewer. The Reviewer evaluates but does not implement. The Executive applies
 only decision authority already granted by Product, Goals, requirements,
 accepted design, ticket, identity, or release law. The Worker carries only the
@@ -83,11 +100,12 @@
   relation, while each adopting Product authority owns its concrete Project
   Reference-Frame Basis.
 
 | Relation | Normative owner | Use in this profile |
 |---|---|---|
-| frame declaration, activation, result algebra, conjunction, translation, coverage, and revision | `REFERENCE_FRAME_METHOD.md` | defines each engagement frame and the active configuration |
+| shared result, conjunction, current state and acquired context | `FOUNDATIONS.md` | supplies the one core result and continuation contracts |
+| frame declaration, activation, frame-specific result refinement, translation, coverage, and revision | `REFERENCE_FRAME_METHOD.md` | defines each engagement frame and the active configuration |
 | bounded-frame conservation and execution intake | `DESIGN_MODULE_METHOD.md` `STDO-UP-017..019`; `SPEC_METHOD.md` `STDO-UP-020` | supplies the Worker activation basis |
 | construction, self-review, assessment, disposition, checkpoint, and continuation | `SPEC_METHOD.md` `STDO-UP-020` | supplies the complete execution transition relation |
 | author/implementer and independent-review separation | `TICKET_METHOD.md` `STDO-UP-007` | supplies Reviewer independence and exact-verdict traceability |
 | exact assurance subject, evidence population, and generic-method freeze | `SPEC_METHOD.md` `STDO-UP-022` | supplies review-boundary and qualification constraints |
 | module-derived unit proof | `DESIGN_MODULE_METHOD.md` Design-to-Module evidence route and Module-Derived Unit Test Rule | supplies the unit frame's module ownership basis while this profile limits its claim and evidence altitude |
@@ -245,13 +263,16 @@
 
 ### Executive
 
 **Executive** is the profile label for the frame that selects or confirms the
 bounded activation configuration and consumes closed Worker and Reviewer
-results under existing project decision authority. It holds the complete
-Product view and current MVP or release mandate needed to assign priority,
-apply disposition, and select the next authorized action.
+results under existing project decision authority. It maintains a sufficient
+bounded delivery view of the long-term outcome, current MVP or release mandate,
+unresolved obligations, dependencies and exact returned results needed to
+assign priority, apply disposition and select the next authorised action.
+The underlying workspace carries the durable frontier; the Executive need not
+load the whole Product, every historical result or every worker's context.
 
 It may be occupied by direct human authority or by a bounded proxy admitted
 under `STDO-UP-020`, `IDENTITY_METHOD.md`, and the current project authority.
 It is not a universal semantic owner, controller, manager service, or runtime
 executive observer.
@@ -306,18 +327,30 @@
   assign priority and boundary effect only under the current Product mandate
   invalidate affected results when the subject or basis changes
   update U from coverage, dependencies, conflicts, and discovered materiality
 
 stop only when every mandatory evaluation is closed, or governing authority
-has explicitly retained every remaining residual consistently with the claim
+has explicitly retained every remaining residual consistently with the claim,
+or an applicable stop returns every remaining obligation as open
 ```
 
 This relation requires no scheduler or frame engine. `M` may contain parallel
 activations. Recursion follows declared evaluation dependencies and bounded
 refinements; it does not nest or join undifferentiated copies of every frame.
-The Executive retains the frontier and closed-result ledger in attention, not
-the undocumented working context of every evaluator.
+The Executive acquires the portion of the durable frontier and closed results
+material to its current decision. If that decision does not fit, it refines the
+coordination question, obtains another bounded evaluation or returns the
+applicable stop retaining the unresolved obligation; it cannot drop a material
+dependency. Closed results retain source routes, blockers, uncertainty
+and invalidators so long-term coordination does not require each evaluator's
+private context. An omitted obligation remains open in the workspace.
+
+After context loss, Executive applies the shared workspace/context contract:
+observe current work, reacquire the admitted outcome and relevant dependencies,
+check retained result validity, reconcile stale summaries and unresolved
+effects, then select the next lawful action. No private Executive memory or
+complete historical replay is an admission prerequisite.
 
 Severity supplied by Reviewer is evaluation evidence. Priority, current-boundary
 effect, `STDO-UP-020` disposition, and subsequent action are Executive decisions.
 They remain distinct ledger entries even when a Product-defined policy maps one
 to another.
@@ -466,27 +499,36 @@
 coordinated branch that consumer is Executive. It exists only after successful
 Worker activation. An `activation_refusal` returns to the assigning authority
 or declared result carrier and creates neither a Worker activation nor a
 Worker result.
 
-The work-result variants are profile carriers, not new STDO semantic
-dispositions. They are disjoint by their accompanying Reference Frame Method
-result:
-
-- `candidate_ready` accompanies `satisfied`: an exact candidate and transition
-  evidence are available;
-- `refused` accompanies `falsified`: lawful activation occurred, but a
-  governing prohibition or owner-valid construction refusal defeats the
-  requested construction;
-- `incomplete` accompanies `indeterminate`: the valid activation has not
-  produced a candidate because admissible evidence or bounded execution cannot
-  yet decide or complete the relation; and
-- `re_entry_requested` accompanies `out_of_frame` or `invalid_basis`: a
-  material decision lies outside Worker authority or the activated basis can no
-  longer support the work.
-
-The mapping is total and exclusive after lawful activation. Payload wording,
+The work-result variants are finer domain outcomes, not another result algebra
+or STDO semantic dispositions. Every result carries the shared core record,
+the actual performance and effect state, and one exact predicate: “the requested
+candidate and transition evidence are available on the activated basis within
+the admitted grant's declared bounds”. The bounds include a delivery time only
+where the grant requires it. A later delivery does not repair a missed bound
+on the original predicate; changed bounds identify a successor claim. The refined
+cases map as follows:
+
+| Original work outcome and cause | Predicate and evidence condition | Core verdict |
+|---|---|---|
+| `candidate_ready` | the bound availability predicate is established, including its declared bounds | `satisfied` |
+| `refused` | an established governing prohibition or owner-valid refusal defeats the bound availability predicate after lawful activation | `falsified` |
+| `incomplete`, `undecided` | admissible evidence or unfinished bounded work cannot establish the bound availability predicate | `indeterminate` |
+| `incomplete`, `postcondition_defeated` | an observed missing delivery, missed declared bound or missing required transition evidence defeats the bound availability predicate | `falsified` |
+| `re_entry_requested`, `outside_frame` | a material relation, decision or capability needed to establish the claim lies outside the activated frame | `out_of_frame` |
+| `re_entry_requested`, `basis_invalid` | the activated subject or basis cannot support the claim | `invalid_basis` |
+| any variant lacking its required cause or its row's evidence condition | retain the raw outcome without inventing deciding support; independently admissible evidence on the same bound predicate remains available | apply the core missing-reason rule; the unsupported label supplies no verdict |
+
+The cause makes the mapping exclusive; a generic re-entry request without it
+is insufficient. `candidate_ready` establishes availability only, not fitness,
+admission, acceptance or publication. A consumer cannot conjoin different
+predicates merely because their verdicts agree. Known non-performance or an
+uncertain effect remains explicit whatever the verdict.
+
+The mapping is total over these declared cases after lawful activation. Payload wording,
 stop timing, or actor preference cannot select another variant. A capability,
 authority, stale-basis, ambiguous-basis, or topology mismatch known during
 activation is an `activation_refusal`, not a synthetic Worker result.
 
 Consumers choose the representation. `STDO-UP-020` remains the owner of the
@@ -1267,11 +1309,11 @@
 
 ## Complete Engagement Transition
 
 The following steps describe the coordinated branch selected under Engagement
 Applicability. Direct Worker engagement preserves the same sufficient intake,
-work-result algebra, closure conditions and owner boundaries without inserting
+work-result refinement, closure conditions and owner boundaries without inserting
 Executive appointment or a review that no applicable condition requires.
 
 ### 1. Existing Authority Selects The Basis
 
 Goals, Product, requirements, accepted design, ticket, release, or an admitted
@@ -1302,27 +1344,35 @@
 Worker frame is active, no Worker evaluation occurs, and Executive must not
 manufacture a Worker result to represent the failed activation.
 
 ### 3. Worker Returns To Executive
 
-Every coordinated Worker activation terminates in one closed work result sent
-to Executive. Direct work uses its declared result consumer:
+Every completed coordinated Worker activation returns one closed work result
+to Executive. Interruption or loss of the actor is observed as unreturned work;
+it cannot be recorded as a completed activation. Direct work uses its declared
+result consumer:
 
 ```text
 WorkerResult
   = candidate_ready(exact_subject, transition_evidence, residuals)
   | refused(reason, authority, evidence)
-  | incomplete(residuals, evidence, stop_basis)
-  | re_entry_requested(owner, material_relation, evidence)
+  | incomplete(cause, predicate, residuals, evidence, stop_basis)
+  | re_entry_requested(cause, owner, material_relation, evidence)
 ```
 
 The notation is explanatory and mandates no schema.
 
-Each variant accompanies exactly one Reference Frame Method result under the
-mapping in `Work result`: `satisfied -> candidate_ready`, `falsified ->
-refused`, `indeterminate -> incomplete`, and `out_of_frame | invalid_basis ->
-re_entry_requested`. The mapping applies only after lawful activation.
+Each refined case accompanies exactly one core verdict under the mapping in
+`Work result`. The original outcome, predicate, cause, performance and known
+effects travel with it. A verdict alone cannot reconstruct the finer outcome.
+The mapping applies only after lawful activation; the refused activation has
+its own admission result rather than a fabricated Worker result.
+
+If execution or evaluation cannot be confirmed, the enclosing coverage retains
+`unconfirmed` performance and its evidence gap. It does not fabricate a Worker
+judgment. Observed effects retain their own state; lack of a returned result
+does not establish that no effect occurred.
 
 The Worker does not send a candidate directly into an implicitly active
 Reviewer. It stops after returning the result.
 
 ### 4. Executive Evaluates The Work Result
@@ -1383,16 +1433,16 @@
   uncertainty where supportable; and
 - invalidation conditions and re-entry owner where applicable.
 
 ### Reviewer Result And Triage Projection
 
-The Reviewer payload projection is total across the Reference Frame Method
-result algebra. `complete`, `indeterminate`, and `not_applicable` below classify
+The Reviewer payload projection is total across the shared core verdicts as
+bound by RF-012. `complete`, `indeterminate`, and `not_applicable` below classify
 the finding-level triage payload; they are not new evaluation results,
 dispositions, priorities, or lifecycle states.
 
-| Reference Frame Method result | Finding and triage payload | Executive consumption constraint |
+| Core verdict for the review predicate | Finding and triage payload | Executive consumption constraint |
 |---|---|---|
 | `satisfied` | explicit no-finding state; triage `not_applicable`; evidence, residuals, and invalidation remain present | priority and current-boundary effect are `not_applicable` to this review result unless another exact consumed result supplies a finding |
 | `falsified` | one or more exact findings; triage is `complete` where supported and preserves `indeterminate` fields where evidence cannot close them | apply Product-owned priority and boundary policy without mechanically mapping severity to disposition |
 | `indeterminate` | partial finding or observation state; triage `indeterminate`; exact evidence gaps and residual uncertainty | retain uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or a closed finding |
 | `out_of_frame` | the evaluated claim requires an undeclared material relation or evaluator capability; triage `indeterminate`; name the missing relation or capability and exact reconfiguration pressure | refine or reconfigure a capable activation and retain the claim as unresolved; do not consume the result as satisfaction or falsification |
@@ -1408,11 +1458,11 @@
 direct the repair, or authorize continuation.
 
 ### 7. Executive Disposes And Checkpoints
 
 The Executive verifies that every consumed result remains bound to the current
-subject and basis, revalidates the complete Product view and current MVP or
+subject and basis, revalidates the sufficient bounded delivery view and current MVP or
 release mandate, applies any declared result conjunction, assigns priority,
 records the effect on the current promotion boundary, and acts on exactly one
 `STDO-UP-020` disposition within its grant:
 
 - `accept`;
@@ -1885,20 +1935,20 @@
 2. the complete selected STDO and Reference Frame Method remain the governing
    sources;
 3. Executive, Worker, and Reviewer are available finite evaluation frames,
    activated only where applicable, not hierarchy or actor identities;
 4. activation refusal remains distinct from Worker results, and every Worker
-   result maps exclusively from one closed Reference Frame Method result and
+   refined result maps to one core verdict on its exact predicate and
    returns to its declared consumer, first to Executive in the coordinated
    branch;
 5. existing work authority determines whether an exact candidate requires
    independent review; the coordinated Executive activates Reviewer where
    required, while the sufficient direct branch adds no such activation;
 6. required Reviewer assessment binds the exact subject, evidence population,
    verdict, evidence-bound technical triage, and independence conditions;
 7. an activated Executive consumes closed results and technical triage against
-   the complete Product view and current MVP or release mandate, keeps severity, priority,
+   the sufficient bounded delivery view and current MVP or release mandate, keeps severity, priority,
    frame result, and boundary effect distinct, and applies only the existing
    `STDO-UP-020` disposition and continuation relation;
 8. specialist frames and result relations cover every known material
    evaluation and interaction or retain an explicit residual;
 9. frame, basis, capability, evidence, and topology change can invalidate and
