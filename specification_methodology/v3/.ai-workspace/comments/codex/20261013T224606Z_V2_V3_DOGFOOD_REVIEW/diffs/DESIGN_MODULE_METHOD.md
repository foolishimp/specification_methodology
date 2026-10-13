--- v2/standards/DESIGN_MODULE_METHOD.md
+++ v3/standards/DESIGN_MODULE_METHOD.md
@@ -1,6 +1,36 @@
 # Design Module Method
+
+## Governing Relations
+
+The premises are a governed Product outcome, admitted requirements, a current
+material boundary, finite actor capacity and an actual design grant. Given
+those premises, [bounded construction](FOUNDATIONS.md#bounded-construction)
+requires the boundary to expose the obligations a local transformation must
+preserve. [Workspace and context](FOUNDATIONS.md#workspace-and-context)
+requires its reconstruction from current source and still-valid evidence,
+rather than the designer's remembered account. Authority does not follow from
+capability or from a plausible implementation.
+
+This method makes additional design choices: Ontology-first semantic ownership,
+Prime contraction, an irreducible carrier set, three related design views and
+explicit effect boundaries. Those choices refine the shared obligations; they
+are not logical consequences of finite capacity alone. The applicable clauses
+below own their conditions and exceptions. ODD alignment, Python typing, UX and
+world-model refinements retain their declared adoption scopes.
+Theoretical analogies supply no additional prerequisite. Cross-member
+references preserve each relation's declared semantic scope and owner.
+
+At design admission, bind the candidate boundary, its basis, material relation
+set and grant. Acquire the source and seam evidence needed for that relation
+set. Design and implementation transform within it. Evaluate each required
+relation and use the shared [result conjunction](FOUNDATIONS.md#result-conjunction)
+at the cross-view gate. The design authority disposes of the resulting
+candidate under its grant. These operations instantiate the
+[Transformation Library](TRANSFORMATION_LIBRARY.md); they do not add a
+compulsory workflow or a second acceptance record.
+
 
 ## 1. Purpose
 
 This method exists for projects that want a stronger implementation discipline
 than "write code that passes."
@@ -98,13 +128,16 @@
 The core rule is:
 
 **semantic steps should read as transforms over admitted truth; effects should
 be explicit and pushed to the edge**
 
-If a reader must inspect orchestration code, mutable workspace state, service
-methods, or fallback defaults to determine what the system means, the design is
-too imperative and too coupled.
+If a reader must infer governing meaning from orchestration code, mutable
+workspace conventions, service methods or fallback defaults rather than the
+admitted contract, the design is too imperative and too coupled. Inspecting
+current workspace state remains necessary to determine what is actually
+present and which contract facts still hold; that observation does not make
+incidental state the authority for intended meaning.
 
 ## 3A. ODD Alignment And Escalation Rule
 
 When this method is used inside an ODD-governed product, reviewers must first
 ask whether the boundary is an operative graph traversal.
@@ -839,10 +872,48 @@
   being identified as a constituent, replica, replacement, or deliberately
   independent realization; or
 - a projection-triggered reaction uses its own reconstructive state as
   self-authenticating admission evidence.
 
+#### Admission contract use
+
+Bind the relation above through the library's
+[transformation-admission specialization](TRANSFORMATION_LIBRARY.md#transformation-admission-specialization).
+Here its input domain is the declared candidate and predecessor on the scoped
+entity, under an interpretable authoritative admission basis and with the
+material support the owning relation requires. Its output domain is that
+relation's declared durable result or other supported outcome. These are
+semantic parameters, not a new carrier
+schema or common result enum. This method owns the design completeness test;
+UP-021 owns the admission decision and standing-test semantics.
+
+The admission assessment returns the shared
+[result record](FOUNDATIONS.md#result-algebra) on the predicate that this exact
+candidate satisfies the declared admission relation at its current basis.
+For this assessment, predecessor continuity, predecessor currentness and the
+admitter's grant are material joins of that predicate. Established stale
+predecessor state or a defeated grant therefore falsifies the admission claim
+under an interpretable governing basis; it is not relabelled a missing basis.
+Missing evidence about those joins leaves the admission claim `indeterminate`.
+An uninterpretable or contradictory governing basis is `invalid_basis`; an
+unsupported evaluation boundary is `out_of_frame`. Preserve the domain
+admission outcome and evidence. `satisfied` requires the whole admission
+predicate, including its joins. Basis advancement before the semantic commit
+still prevents effect and requires the current-basis re-entry owned by UP-021.
+An assessment not performed retains `performance = not_performed`. Construction
+of a well-formed candidate is a different predicate and cannot stand in for
+admission. The effect component records the actual commit/publication state,
+including `partial` or `unknown` where appropriate.
+
+Apply that specialization in the existing admission assessment: a
+shape-correct candidate reconstructed by a projector cannot establish
+admission when it lacks the required predecessor continuity or admitter grant.
+The same candidate with authentic current-basis support and actual authority
+is evaluated against the owning predicate; those facts alone do not guarantee
+admission. Where a governing seam remains unresolved, use UP-017's affected
+relation set and the owning result algebra rather than inventing a local pass.
+
 ### Atomic Functions And Higher-Order Composition
 
 The Ontology must derive the smallest parameterized atomic function families
 that make the entity lifecycles logically complete. Variation that changes only
 an entity kind, projection kind, transition kind, policy, or subordinate payload
@@ -1428,21 +1499,46 @@
 Controller-local memory is not a lawful source of lifecycle truth when the
 product declares replay, event, graph, or carrier ownership.
 
 ### Cross-view axiom evaluation
 
-The design pack must evaluate every applicable product, graph, language,
-runtime, handler, and module axiom with one of:
-
-- `pass`;
-- `fail`; or
-- `not_applicable`, with a reason.
+The design pack evaluates every applicable product, graph, language, runtime,
+handler and module axiom using the shared
+[result algebra](FOUNDATIONS.md#result-algebra). Applicability and conformance
+are separate predicates on the named design boundary and governing basis.
+Existing `pass`, `fail` and `not_applicable` labels retain their original domain
+meaning and map on the predicate actually evaluated:
+
+- `pass` maps to `satisfied` on the exact axiom predicate with its evidence;
+- `fail` maps to `falsified` on that predicate with its counterexample;
+- a supported `not_applicable` falsifies "this axiom applies to this boundary"
+  under the owning applicability law. It reports no conformance judgment on
+  the excluded axiom;
+- an unsupported exclusion leaves that applicability predicate `indeterminate`
+  and cannot remove the axiom from required coverage.
+
+Missing decisive evidence remains `indeterminate`; an unusable governing basis
+remains `invalid_basis`. An applicable axiom outside the evaluation's bound
+scope or capability is `out_of_frame`, not excluded. Performance uses the shared
+legal pairs. An interrupted evaluation already undertaken remains `performed`
+with its extent and any witnessed counterexample; a check never undertaken
+remains `not_performed`, and uncertain execution remains `unconfirmed`.
+
+Only supported applicability results determine exclusions. The conformance
+gate retains those results as coverage evidence; it does not conjoin a true
+exclusion's falsified applicability predicate as if it were a failed required
+axiom. Unresolved applicability keeps coverage unresolved.
 
 The minimum evaluation columns are:
 
-| Axiom | Ontology evidence | Authority | Domain evidence | Sequence evidence | State evidence | Native enforcement | Admission/compiler enforcement | Verdict | Gap owner |
-|---|---|---|---|---|---|---|---|---|---|
+| Axiom and evaluated predicate | Exact subject and basis | Ontology evidence | Authority | Domain evidence | Sequence evidence | State evidence | Native enforcement | Admission/compiler enforcement | Original domain outcome | Core verdict | Performance and extent | Effects | Residual and gap owner |
+|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
+
+Columns may resolve existing evidence and result records rather than duplicate
+them. The core verdict is one of the five shared values. The table retains the
+selected predicate and original label, including a reasoned applicability
+result; a bare `pass`, `fail` or `not_applicable` is not a complete handoff.
 
 The cross-view evaluation must prove that:
 
 - every element in each view derives from the accepted Ontology;
 - every discovered functionality row has a derived, deferred, excluded, or gap
@@ -1466,10 +1562,19 @@
 `semantic_not_realized` constructor is a blocking gap. It may not be replaced
 by imperative glue in a plugin, shell, service, script, or test harness.
 
 ### Gate and retrospective work
 
+Conjoin the required Ontology, design-view, constructability and axiom results
+using [result conjunction](FOUNDATIONS.md#result-conjunction). Keep each
+predicate, failure, citation and unresolved obligation. A proved failure in
+one view remains visible when another view has no assessment. No view count,
+empty result set or supported exclusion substitutes for the complete required
+set. The conjunction supports the design authority's decision; it is not that
+decision. Domain dispositions such as `accepted` and `non-accepted` remain
+reported with their authority and the predicate actually decided.
+
 For a new or semantically changed boundary, the Ontology and design verdict must
 both be `accepted` before the affected implementation, public contract, or
 semantic carrier is promoted or the work claims design-method closure. Any
 failed applicable axiom, missing functionality disposition, unresolved
 authority path, or blocking realization gap keeps the verdict non-accepted.
@@ -1533,10 +1638,23 @@
 the domain design into its computational realization: abstract data types,
 identity and key structures, algorithms, algebraic laws, mutation and effect
 boundaries, selected implementations, and domain-to-computational mappings. The
 cross-view evaluation extends to prove the domain views and this projection
 describe one system.
+
+This projection applies the build-tenant binding owned by
+[SPEC_METHOD's WHAT, HOW, And Work Carriers](SPEC_METHOD.md#what-how-and-work-carriers).
+The tenant design binds common requirements to executable operations and their
+actual environment under that law. A machine stack, a human procedure and a
+mixed process each state their operations, composition, effect locations,
+authority and material resource measures, with their units and observation
+boundaries. An operation performed by a person
+retains its input, outcome, refusal and recovery contract; a role title is not
+its implementation. The domain, algorithmic, informational and computational
+accounts must agree on the same obligations. Software-module mechanics apply
+where software realizes the boundary, not as a demand to disguise every human
+step as code.
 
 For a material producer-to-consumer path, this projection identifies fact
 establishment, consuming operations, applicable basis and invalidators, effect
 boundaries, retained alternatives and accumulated work. Use the validity and
 reuse relation owned by `SPEC_METHOD.md` `STDO-UP-021`; method and assurance
@@ -1882,10 +2000,18 @@
 ## 8. Totality Rule
 
 Semantic functions should be total or as close to total as the language and
 problem allow.
 
+At a method boundary their outcomes use the
+[shared result record](FOUNDATIONS.md#result-algebra), retaining the function's
+domain outcome. Invalid basis, an unsupported input domain, insufficient
+evidence and a demonstrated failure remain distinct. A typed return says what
+happened; it does not guarantee that an external computation terminates. The
+owning transition states its permitted recovery, re-entry, yield or termination
+for each supported result, including unknown effects.
+
 Preferred shape:
 
 - invalid input is rejected at the boundary
 - semantic kernels consume admitted carriers only
 - failure is returned in a typed and explicit form when practical
@@ -1924,10 +2050,18 @@
 
 1. admit or parse the authoritative input
 2. transform it into a typed plan or outcome
 3. apply effects at the edge using that plan or outcome
 4. publish resulting events or projections downstream
+
+The effect return preserves `not_requested`, `not_started`, `completed`,
+`partial`, `reverted` or `unknown` in the shared record as observed. A transport failure
+after dispatch is not proof that an effect did not occur. Re-entry observes the
+current owning state before any dependent repeat, through
+[workspace and context](FOUNDATIONS.md#workspace-and-context). It can reacquire
+a sufficient frame after private context is discarded without resetting the
+workspace or assuming every effect is idempotent.
 
 If a function both decides the semantic meaning and directly performs the write,
 the design should be treated as suspect.
 
 ---
