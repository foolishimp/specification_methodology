--- v2/standards/AXIOMATIC_CALCULUS.md
+++ v3/standards/AXIOMATIC_CALCULUS.md
@@ -3,10 +3,24 @@
 ## Position
 
 The **STDO Axiomatic Calculus for Governed Symbolic Systems**, written `a_c`,
 is STDO's domain-specific, carrier-neutral constitutional calculus for
 representing and relating governed symbolic systems.
+
+The [foundations](FOUNDATIONS.md) supply interpretation, identity, composition,
+finite-capacity and authority premises. Given an explicit interpretation and
+typed subject, AC-003, AC-004 and AC-006 require resolved, compatible references
+on one exact basis before a model's judgment can be consumed. The signature,
+record kinds, closure operator and functor-kind classification below are the
+calculus's additional choices; finite capacity alone does not derive them.
+
+AC-007 and AC-014 consume the shared
+[result algebra](FOUNDATIONS.md#result-algebra); AC-016 consumes its
+[conjunction](FOUNDATIONS.md#result-conjunction) where a composite claim needs
+several judgments. The [transformation library](TRANSFORMATION_LIBRARY.md)
+provides reusable responsibilities. It does not replace AC-013's exact
+transformation contract or establish category-theoretic functor laws.
 
 Its stable concept identity is:
 
 ```text
 urn:stdo:concept:axiomatic-calculus:a-c
@@ -79,14 +93,15 @@
   uncertainty, and capability fit from
   [`REFERENCE_FRAME_METHOD.md#reference-frame-laws`](REFERENCE_FRAME_METHOD.md#reference-frame-laws); and
 - singular released authority from
   [`SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001`](SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001).
 
-These references establish provenance. The definitions and laws below are the
-sole normative authority for the meaning of `a_c` within the selected complete
-STDO cut. A consumer does not need an implicit STDO representation, GTL
-carrier, or downstream implementation to interpret the calculus.
+These references establish provenance. The definitions and laws below own the
+`a_c` specialization within the selected complete STDO cut and explicitly
+consume its common result and composition owners. A consumer does not need an
+implicit STDO representation, GTL carrier, or downstream implementation to
+interpret the calculus.
 
 This standard introduces the generic calculus identities `F_D`, `F_P`, and
 `F_H`. It does not import those identities from an equal-spelled graph,
 runtime, ODD, or application shorthand. The predecessor clauses establish the
 substrate-neutral evaluation, probabilistic-processing, human-adjudication,
@@ -410,13 +425,52 @@
 coordinates do not create a coherent composite basis by proximity.
 
 ### AC-007 Constraint And Refusal
 
 Each constraint names its governed subject, predicate, judgment kind,
-latitude, and refusal. A failed, missing, indeterminate, out-of-scope, or
-invalid-basis result follows the declared result algebra rather than being
-coerced to success.
+latitude, and refusal. Its evaluation produces the
+[core result](FOUNDATIONS.md#result-algebra). Its finer constraint outcome
+maps exactly once on that same subject, basis and predicate:
+
+| Constraint outcome | Core verdict |
+|---|---|
+| admissible evidence establishes the predicate | `satisfied` |
+| an admissible counterexample defeats the predicate | `falsified` |
+| admissible evidence does not decide the predicate | `indeterminate` |
+| a necessary material relation or capability lies outside the frame | `out_of_frame` |
+| the exact subject or basis cannot support this evaluation | `invalid_basis` |
+
+The result retains the original outcome, performance and known effect state.
+Non-performance alone establishes neither a negative domain finding nor a
+positive proof. Separately admissible counterevidence retains its deciding
+force under the shared legal pairs without inventing execution. A finer refusal
+names its cause and map; no refusal is
+coerced to success. Missing mandatory evaluations remain explicit coverage
+residuals when judgments are conjoined.
+
+The outcome shorthands used by projection, transformation, interpretation and
+admission below are refinements under the same rule. Returning a projection,
+proposed successor or model candidate establishes only its declared production
+predicate. `accepted` and `admitted` establish the exact authorised decision
+predicate and preserve the actual decision evidence. They do not establish
+another model's semantic truth.
+
+`hold`, `gap`, `refusal` and `refuse` always carry a declared cause: an undecided
+predicate maps to `indeterminate`; missing material frame scope or capability
+to `out_of_frame`; an unusable basis to `invalid_basis`; and an admissible
+counterexample to that predicate to `falsified`. An established prohibition
+falsifies only the permission or admission predicate it defeats. Refusing an
+interpreter because its grant is absent does not falsify the model's constraint
+predicate. On that constraint, retain the actual evaluation performance and
+any separately admissible counterevidence or supported scope/basis diagnosis;
+without deciding support the unevaluated predicate remains `indeterminate`.
+The refusal of permission is a separately bound result.
+
+The pair of original outcome and cause, not the shorthand alone, identifies one
+refinement case. A bare stop word cannot satisfy a consumer. Implementations
+bind these mappings before execution and retain performance, known effects,
+evidence and residuals.
 
 ### AC-008 Explicit Latitude
 
 Two values may differ lawfully only through an applicable latitude or
 transformation relation. An implementation preference, probabilistic choice,
@@ -650,20 +704,51 @@
   owner,
   scope,
   basis,
   evaluator,
   authority,
+  predicate,
+  verdict,
   decision,
+  performance,
+  effects,
   evidence,
+  residuals,
   provenance,
   decided_at
 }
 ```
 
 Issuing a judgment does not transform, rewrite, reissue, or rename its subject.
 Promotion is an explicit relation between the unchanged subject and its
 admission or acceptance judgment.
+
+`predicate`, `verdict`, `performance`, `effects`, `evidence` and `residuals`
+bind the shared result contract. `decision` retains the original calculus or
+interpreted-domain outcome; it is not another verdict enum. The exact
+interpretation declares its map before the judgment is used. A carrier may
+encode these relations through resolved records rather than repeated bodies.
+Each field is required by this semantic contract. The selected signature closes
+its value domain and cardinality as well as its identity-bearing reference
+domains. Performance uses the shared legal pairs and retains the observed
+extent: an interrupted evaluation already undertaken is `performed`, not an
+unperformed evaluation. An absent effect observation cannot default a requested
+operation to `not_requested`.
+
+`predicate` resolves the adopted predicate contract; identity-bearing
+`residuals` resolve the calculus's existing residual records. `effects` records
+the shared effect state at the boundary named by that predicate and its
+evidence. Existing subject, evidence and provenance identities identify the
+observed operation and owning observation; this relation introduces no nested
+effect-identity schema. These are semantic obligations of the selected
+calculus contract, not a mandatory serialisation layout for every external
+model or carrier. A subject interpretation declares its exact bindings.
+
+An external checker remains bound to its own released schema and semantics.
+Passing an older pinned checker proves only that checker's declared predicate.
+It does not silently upgrade an older judgment record to this successor
+contract, or establish semantic acceptance of an `a_c.X` interpretation.
 
 ## Traversals And Functor Kinds
 
 A traversal is a typed contract:
 
@@ -699,11 +784,15 @@
 F_K[v](X_v) -> Y_v | Omega_v
 ```
 
 where `F_K` is one functor kind, `v` is one exact traversal identity, `X_v` and
 `Y_v` are its typed input and result domains, and `Omega_v` is its closed stop
-algebra.
+refinement. The traversal binds each outcome in `Y_v` or `Omega_v` to one core
+verdict on an explicit predicate and preserves the original outcome. Its
+declared domain includes graceful refusal, uncertainty and recovery or
+termination dispositions for observations it cannot decide. This total
+handling contract does not prove an external actor or world will terminate.
 
 - `F_D` classifies deterministic evaluation or proof over declared properties.
   It returns a judgment and does not perform the domain construction being
   judged.
 - `F_P` classifies bounded probabilistic interpretation, construction, or
@@ -723,10 +812,16 @@
 `Functor Kind` is an `a_c` term for this traversal classification. It does not
 by itself assert a category-theoretic functor. A model claiming categorical
 functor laws additionally defines its source and target categories and proves
 identity and composition preservation.
 
+For a construction traversal, satisfying `an exact candidate is available`
+does not satisfy `the candidate conforms` or `the candidate is accepted`.
+Evaluation and authorised disposition require their own predicates and
+evidence. Likewise, a completed human decision records that exact decision;
+human presence does not turn a rejected candidate into a conforming one.
+
 ### AC-015 Functor Classification
 
 Every functor application binds exactly one functor kind and one traversal
 identity. Applying any `F_*` kind without bracketed traversal identity `[v]` is
 incomplete.
@@ -743,10 +838,30 @@
 Composition retains both traversal identities, intermediate results,
 judgments, evidence, authority, provenance, and stop states. It cannot flatten
 probabilistic proposal, deterministic evaluation, and human decision into one
 undifferentiated operation. `a_c` prescribes no universal `F_P -> F_D -> F_H`
 sequence; each application owns its lawful topology.
+
+When the composition claims that several constraints hold, it uses
+[core conjunction](FOUNDATIONS.md#result-conjunction) over their exact
+predicates and coverage. A stop at one traversal cannot erase a valid
+counterexample from another; a successful traversal does not satisfy an
+unperformed dependent traversal. Otherwise the application declares the outer
+predicate, exact leaf predicates, material joins, and disjoint, exhaustive truth
+and falsity conditions on its fully decided admitted domain. Its result uses
+the declared-operator rule in
+[result conjunction](FOUNDATIONS.md#result-conjunction), with only the
+dependencies needed to decide that predicate. A fallback may establish its
+declared outer predicate while retaining an earlier failed leaf; it cannot
+report that every stage succeeded. An absent dependent return remains an absent
+slot, with its known performance or uncertainty. An uninterpretable operator
+declaration supplies no guessed success. This clause owns typed traversal
+composition; the core owns result evaluation for the declared outer operator.
+
+Effect-sensitive composition also binds
+the current-state and uncertainty rules in
+[workspace and context](FOUNDATIONS.md#workspace-and-context).
 
 ## Interpretation And Models
 
 An interpretation applies `a_c` to an exact subject:
 
@@ -898,10 +1013,18 @@
 finite set of clauses from which this edition was derived. Every principle
 reference is one clause identified under `Derivation Provenance`, resolves
 inside that predecessor cut, and is retained without a hard-coded member count.
 The set is recomputed when the derivation account changes. It cannot depend on
 the publication carrier or calculus-basis identity being created.
+
+The exact historical addresses and byte predicates can resolve through
+successor-owned [derivation verification material](IDENTITY_METHOD.md#derivation-verification-material).
+Its immutable publication membership binds the evidence; its reconstructed
+historical bytes bind the original predecessor manifest and fragments. This
+resolution keeps the derivation record and its identity unchanged and requires
+no predecessor installation or remote retrieval. Evidence does not make the
+historical clauses operative for a successor consumer.
 
 `publication_basis` binds the distinct immutable successor carrier and this
 standard's exact bytes. Its member URI resolves inside its release URI. The
 record is external because this standard cannot contain its own final byte
 digest. Same-release references that cite this calculus are publication or
