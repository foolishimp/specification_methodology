--- v2/standards/SPEC_METHOD.md
+++ v3/standards/SPEC_METHOD.md
@@ -1,6 +1,35 @@
 # Spec-Driven Homeostatic Methodology
+
+This member owns the particular constitutional contracts of Spec Method.
+The [foundational commitments](FOUNDATIONS.md#foundational-commitments) supply
+its declared premise layer. The [shared contract](TRANSFORMATION_LIBRARY.md#foundational-contract)
+provides generic transformation vocabulary. The
+[work/recovery specialization](TRANSFORMATION_LIBRARY.md#workrecovery-specialization)
+relates those premises to this member's UP-020 and computed-treatment rules,
+identifying conditional consequences and independent purpose, policy or
+authority choices for the rows mapped there.
+
+The constitutional chain retains its direction from Goals. That selection,
+its grants and domain-specific dispositions are additional method choices,
+not consequences of finite capacity alone. The
+[bounded-construction relation](FOUNDATIONS.md#bounded-construction) governs
+how sufficient steps preserve the declared A-to-Z contract; the
+[workspace/context relation](FOUNDATIONS.md#workspace-and-context) governs
+intake and re-entry. UP-020 consumes the shared
+[result algebra](FOUNDATIONS.md#result-algebra) for construction, assessment
+and disposition without merging their predicates or authority. Neither a
+foundation argument nor a shared helper supplies permission.
+Bind, Acquire, Transform, Evaluate, Conjoin and Dispose can be composed within
+these contracts without imposing six stages or a new runtime API.
+
+The detailed members retain their own declared standing and applicability.
+Graph-native constitutional meanings remain owned by `ODD_METHOD.md`;
+module realization remains owned by `DESIGN_MODULE_METHOD.md`. Each detailed
+relation remains owned by its declared standard. Cross-member references
+consume that owner without transferring authority.
+
 
 ## Canonical Compression
 
 Spec-driven development treats specification as constitutional source, not
 commentary on code. Methodology defines the process constitution. Intent,
@@ -44,12 +73,13 @@
 ## Position
 
 Spec-driven development treats specification as constitutional source, not as
 commentary on code after the fact.
 
-The point is to make software re-derivable, auditable, and correctable under
-explicit authority.
+The point is to make governed work re-derivable, auditable, and correctable under
+explicit authority. Software, human processes and mixed processes realise the
+same declared obligations through separately bound build tenants.
 
 Its overriding bias is declarative rather than imperative.
 
 In the age of LLMs, the system should primarily declare truths, structures,
 interfaces, constraints, and evidence surfaces, then let lawful processing
@@ -195,21 +225,21 @@
 
 We define the full constitutional **what** in **requirements**, not merely a feature list.
 
 We prefer declaring desired truth and lawful boundaries over prescribing step-by-step imperative procedure.
 
-We make **design** the explicit structural bridge between requirements and code.
-
-We require **code** to be derivable from requirements and design, not defended as accidental precedent.
+We make **design** the explicit structural bridge between requirements and realisation.
+
+We require **realisation** to be derivable from requirements and design, not defended as accidental precedent.
 
 We treat spec-driven development as a **disambiguation pipeline**: each major gate reduces the space of lawful interpretations before downstream realization proceeds.
 
 We demand **evidence** for claims through scenarios, tests, events, projection, and delta.
 
 We treat **repricing** as part of correctness: when reality exposes a constitutional gap, the specification must change.
 
-We keep **authority directional** even while iterating: goals govern intent, intent governs product definition, product definition governs requirements, requirements govern design, and requirements plus design govern code.
+We keep **authority directional** even while iterating: goals govern intent, intent governs product definition, product definition governs requirements, requirements govern design, and requirements plus design govern realisation.
 
 We keep the **live operative surface** in the present tense only: once a new current reality is established, transitional paths are erased from the live product unless explicitly retained as compatibility features.
 
 We treat **derived artifacts** — indexes, trace matrices, reports, automation, generated views — as helpful read models, never as constitutional truth.
 
@@ -244,11 +274,11 @@
 
 This methodology is not only a local operating note for one implementation. It is the process constitution for building projects by spec-driven development.
 
 Its role is meta-constitutional:
 
-- it defines how goals, intent, product, requirements, design, code, evidence, and repricing relate
+- it defines how goals, intent, product, requirements, design, realisation, evidence, and repricing relate
 - it defines what counts as specification sufficiency
 - it defines what kinds of requirement truth exist
 - it defines how authority flows during iterative delivery
 
 Therefore, if a project's implementation disappears, this methodology should still be sufficient to bootstrap a new spec-driven project process from scratch.
@@ -799,10 +829,37 @@
 `WHAT` is realized by one or more independent project-owned `HOW` tenants. A
 **build tenant** is one such realization. **Build tenancy** is the one-or-more
 relation; one tenant is its singleton case and multi-build-tenancy begins when
 the same `WHAT` has more than one independent realization.
 
+The common `WHAT` is the requirements calculus: it states admissible states,
+outcomes, constraints, evidence obligations and permitted changes without
+choosing every means of execution. A tenant's design supplies its computational
+calculus and concrete binding: which operations realise those requirements,
+how they compose, which actors or mechanisms perform them, what effects they
+permit, the operational assumptions and how their outcomes are observed. The binding may use software,
+hardware, people, organisations or a mixture. A machine architecture is one
+binding, not the definition of computation for the method.
+
+A computational calculus may be reused across tenants and execution environments
+where its bindings satisfy its laws and the common obligations. A different
+language, tool or team does not by itself require a different calculus. Author
+identity, actor identity and operation kind remain distinct; neither identity
+determines operation kind. A person performing a procedure is not thereby making
+a human adjudication. An a_c representation neither selects the executor nor
+proves realisation conformance by passing structural validation.
+
+At design admission, each affected requirement identifies its realising
+operation or invariant, the preservation obligation at its interfaces, and the
+evidence capable of defeating the claimed realisation. Context, time, memory,
+communication, human effort and spend state their units and are measured at the
+boundary declared by that binding where they are material. Attention adequacy
+is evaluated through actual-use evidence; no universal attention unit or score
+is required. A requirement-to-operation route
+alone does not discharge preservation or demonstrate fitness. A tenant cannot
+repair an inconvenient requirement by silently changing the common `WHAT`.
+
 `what.intent`, `what.product`, and `what.specification` locate the current
 constitutional `WHAT`. Intent and Product each have one canonical entrypoint;
 specification may cite more than one requirement or specification surface.
 
 The **Tenant Registry** is the canonical `how.build_tenants` collection for the
@@ -941,11 +998,11 @@
 ---
 
 ## Constitutional Chain
 
 ```
-Goals → Intent → Product Definition → Requirements → Design → Code → Events → Projection → Delta
+Goals → Intent → Product Definition → Requirements → Design → Realisation → Observations → Projection → Delta
                                                                                        ↓
                                                                                   Scenarios
                                                                                        ↓
                                                                                 Gap Analysis
                                                                                        ↓
@@ -956,19 +1013,30 @@
 - **Intent** defines purpose and direction.
 - **Product Definition** defines the current product realization of the mutable source project, its key terms, and end-state shape in terms that can be decomposed into requirements.
 - **Requirements** define invariant truths the system must satisfy.
 - **Design** defines the structural decisions, interfaces, carrier surfaces, and delivery topology that make those truths achievable.
 - **ADRs** are one durable form of design record, not a second constitutional layer above design.
-- **Code** realizes those decisions.
-- **Events** record what actually happened.
-- **Projection** reconstructs current truth from the event stream.
+- **Realisation** carries those decisions in the tenant's concrete environment;
+  code is the software case, and a performed human procedure is another case.
+- **Observations** establish what occurred and what currently exists at their
+  declared boundaries. Events are a durable carrier where selected.
+- **Projection** presents the observations relevant to a declared question.
+  It is checked against its source and current state; it is not another truth
+  surface and does not require every consumer to replay a complete event stream.
 - **Delta** reveals drift between intended truth and realized state.
 - **Scenarios** test operational meaning — can the system actually do the thing the words describe?
 - **Gap analysis** identifies where real use cases hit the current model and reveal insufficiency.
-- **Repricing** updates goals, intent, product, requirements, design, or code when the system no longer harmonizes. When gap analysis reveals constitutional insufficiency, it generates new **Goals** and/or **Intent**.
-
-This is the homeostatic loop. Every link in the chain is load-bearing. A break at any link — goals with no downstream repricing path, an unowned requirement, an ungrounded design record, code without a design decision — creates accidental law.
+- **Repricing** updates goals, intent, product, requirements, design, or realisation when the system no longer harmonizes. When gap analysis reveals constitutional insufficiency, it generates new **Goals** and/or **Intent**.
+
+This is the homeostatic loop. Every link in the chain is load-bearing. A break at any link — goals with no downstream repricing path, an unowned requirement, an ungrounded design record, realisation without a design decision — creates accidental law.
+
+The workspace persists through this loop. At each activation, current material
+state and valid authority define the new A; Z names the admitted acceptance
+constraints. The actor acquires sufficient context for the next bounded
+transition. Discarding that context does not rewind A. A new observation can
+invalidate a belief or dependent result; it cannot silently change Z or create
+permission. Revising Z follows the owning re-entry relation below.
 
 `GOALS.md` is the bounded work-wave surface. It captures the current overriding concerns for the next body of work, keeps temporary focus out of deeper constitutional layers until it is intentionally repriced there, and is more immediate than intent while remaining higher-level than product definition and requirements.
 
 `PRODUCT.md` is the bridge between direction and obligation. It states the current product-definition surface of the mutable source project in present-tense terms, names the product terms and boundaries that downstream layers rely on, and provides the surface that requirements decompose.
 
@@ -1224,26 +1292,37 @@
 constrain the supported cause, preserve unresolved alternatives and uncertainty,
 and identify the smallest sufficient lawful scope of repair. The frame that
 exposes a failure need not contain its cause. Repeating the same analysis under
 different frame names supplies no additional causal evidence.
 
+Intake first applies [workspace and context](FOUNDATIONS.md#workspace-and-context):
+observe the affected current state, compare it with the report and retained
+results, and distinguish an actual defect from a stale belief. Reuse valid
+observations and rulings. If an effect may already have occurred, resolve that
+uncertainty before recommending an action that depends on its absence. An old
+conversation or work summary supplies a route to evidence, not a veto on
+current reality. Events that record effects are observations; apply the core
+effect and supported-supersession rules before treating them as stale. A local
+absence cannot erase a recorded external effect. The classification result retains the exact diagnosis
+predicate, evidence and residuals under the common result contract.
+
 Use the smallest sufficient applicable frame configuration under
 [frame applicability and conjunction](REFERENCE_FRAME_METHOD.md#method-functions), with
 [causal localization](STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization)
 where required. This does not prescribe a reviewer count or a new review round;
 required independence remains intact. A diagnosis does not grant repair effects
 or establish that governing meaning must change: a candidate may instead need
 correction under sufficient existing law.
 
 The minimum lawful change classes are:
 
-- `goal_reprice`: current bounded work-wave focus changes; re-enters at Goals and may flow through Intent, Product, Requirements, Design, Code, and Evidence where that focus changes deeper constitutional truth
-- `intent_reprice`: directional or scope change; re-enters at Intent and flows through Product, Requirements, Design, Code, and Evidence
-- `product_reprice`: current product realization changes while directional intent remains stable; re-enters at Product and flows through Requirements, Design, Code, and Evidence
-- `requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Code, and Evidence
-- `design_reframe`: realization structure changes while active intent and requirement truth remain stable; re-enters at Design and flows through Code and Evidence
-- `realization_refactor`: local code, configuration, or attribute change with no intended constitutional or structural change; re-enters at the realized surface only and must prove no upstream drift
+- `goal_reprice`: current bounded work-wave focus changes; re-enters at Goals and may flow through Intent, Product, Requirements, Design, Realisation, and Evidence where that focus changes deeper constitutional truth
+- `intent_reprice`: directional or scope change; re-enters at Intent and flows through Product, Requirements, Design, Realisation, and Evidence
+- `product_reprice`: current product realization changes while directional intent remains stable; re-enters at Product and flows through Requirements, Design, Realisation, and Evidence
+- `requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Realisation, and Evidence
+- `design_reframe`: realization structure changes while active intent and requirement truth remain stable; re-enters at Design and flows through Realisation and Evidence
+- `realization_refactor`: local implementation, procedure, configuration, or attribute change with no intended constitutional or structural change; re-enters at the realized surface only and must prove no upstream drift
 
 Smaller changes may re-enter below Goals only if they explicitly assert that no
 upstream constitutional surface is changing.
 
 The absence of a declared change class is process drift.
@@ -1532,10 +1611,17 @@
 - accepted transformation-admission relations;
 - selected computational or common-library dispositions;
 - construction and assessment authority; and
 - the conditions that require upstream re-entry.
 
+The selected frame is acquired from the current workspace and authoritative
+external inputs under [workspace and context](FOUNDATIONS.md#workspace-and-context).
+Its contract identifies current A, admitted Z, the bounded transition and the
+observations needed to establish its result. Prior summaries may locate those
+inputs; private actor memory is not a prerequisite. Context fit cannot be
+achieved by dropping a known material relation.
+
 Where `DESIGN_MODULE_METHOD.md` applies, `STDO-UP-017` bounded-frame
 conservation, `STDO-UP-016` transformation-admission completeness,
 `STDO-UP-018` invariant-reconstruction sufficiency, and `STDO-UP-019`
 computational-realization projection supply these design inputs. This section
 consumes those laws; it does not create a second design package.
@@ -1590,18 +1676,47 @@
 authority or validity conditions still requires the affected binding to be
 resolved before effect. Executive mutation restrictions remain applicable.
 
 ### Proportional Disposition
 
-Assessment returns one of these semantic dispositions:
-
-| Disposition | Condition |
-|---|---|
-| `accept` | the candidate closes its declared cone and preserves every affected governing relation |
-| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent |
-| `re_enter` | Product, requirement, identity, lifecycle, authority, public contract, or accepted design must change |
-| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path |
+Assessment evaluates the exact predicate `the candidate closes its declared
+cone and preserves every affected governing relation` through the shared
+[result algebra](FOUNDATIONS.md#result-algebra). It returns evidence and a
+proposed semantic disposition. Only the existing decision authority applies
+that disposition; an assessment verdict is not acceptance authority.
+
+| Disposition | Condition on the exact candidate claim | Core verdict |
+|---|---|---|
+| `accept` | the candidate closes its declared cone and preserves every affected governing relation | `satisfied` |
+| `local_repair`, demonstrated counterexample | a demonstrated defect defeats the claim while the governing relation remains coherent | `falsified` |
+| `local_repair`, inadequate proof | missing or defective proof leaves the candidate claim undecided; the evidence supports a local proof repair | `indeterminate` |
+| `re_enter`, defeated candidate | the intended candidate cannot satisfy an interpretable current contract without an owning-layer change | `falsified` |
+| `re_enter`, unusable governing basis | the governing requirements cannot supply a coherent interpretation for this assessment | `invalid_basis` |
+| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path | `falsified` |
+
+The proposed remedy retains its original domain outcome; the core verdict does
+not choose among remedies. Governing-requirement coherence is an admission
+condition here; the candidate's alignment, including its design's alignment
+with those requirements, is an evaluated relation. A contradictory design does
+not by itself invalidate otherwise interpretable requirements. A proof defect
+can falsify the proof's own claim without falsifying the implementation claim.
+Insufficient evidence returns `indeterminate`, a
+missing material evaluation capability returns `out_of_frame`, and an
+unusable basis returns `invalid_basis`. A proposed remedy accompanies any of
+these when its cause and authority are supported; the verdict alone neither
+forces a remedy nor forbids a useful authorised repair. Preserve missing causes
+under the core rule. Required judgments compose by
+[core conjunction](FOUNDATIONS.md#result-conjunction); a known failure survives
+alongside missing coverage. A construction result satisfying only `an exact
+candidate is available` never substitutes for this assessment predicate.
+
+The applied disposition has a separate decision result under the core contract:
+the predicate concerns that disposition on the exact subject and basis under
+the bound mandate. A lawful recorded `reject` may satisfy that decision
+predicate without establishing a candidate counterexample. It never overwrites
+the assessment result. The table classifies evidence for a proposed remedy;
+it does not turn policy decisions into fitness verdicts.
 
 Global correctness means conserving every global relation affected by the
 bounded action. It does not require proving the whole Product inside every
 local action.
 
@@ -1637,14 +1752,20 @@
 Product outcome or affected relation set.
 
 A preservation checkpoint may retain unfinished or unaccepted work under an
 existing exact operation grant. Identify its parent or predecessor, included
 territory, concurrent-writer disposition and durable evidence location. It is
-neither acceptance, promotion nor publication. A proposed restart identifies
-why repair of retained work is insufficient, which obligations and evidence
-survive, and which causal assumptions change; reconstructability alone does
-not select reconstruction.
+neither acceptance, promotion nor publication.
+
+An ordinary restart reacquires a sufficient frame over the current workspace;
+it is another iteration, not a request to rebuild from the original A. Apply
+the core current-state, result-validity and unknown-effect rules before the
+next dependent action. Preserve applicable partial work and valid evidence.
+If a proposed recovery instead discards or rebuilds work, identify why repair
+of retained work is insufficient, which obligations and evidence survive,
+which causal assumptions change and which existing operation grant permits
+that effect. Reconstructability alone does not select reconstruction.
 
 Accepted material Product movement is progress. Prerequisite work names the
 Product obligation it enables. Preservation and repeated proof are evidence,
 not new progress. Rejected or superseded construction is churn. Discovery of
 previously hidden distance revises the forecast but is not itself negative
@@ -2472,21 +2593,21 @@
 This is how the system stays alive instead of becoming a frozen constitution. The generative rule:
 
 1. A real use case (scenario, deployment, external review) hits the current model
 2. Gap analysis identifies what the constitution cannot express
 3. If the gap is constitutional (not just a missing implementation), new goals and/or intent are written
-4. The repriced surface then flows forward through the chain: product → requirements → design → code
+4. The repriced surface then flows forward through the chain: product → requirements → design → realisation
 
 New intents emerge from repeated, real use-case pressure against the current model — not from abstract speculation. The gap must be concrete before it becomes intent. Ad hoc coding pressure does not generate intent; explicit gap analysis does.
 
 This flow is not a one-pass waterfall computation. It is a cumulative iteration:
 
 - requirements and design are refined over time
-- code is repeatedly re-derived against the current constitutional surface
+- realisation is repeatedly re-derived against the current constitutional surface
 - gaps discovered during implementation, testing, replay, or scenario work feed back into repricing
 
-What must remain stable is the full direction of authority: goals govern intent, intent governs product, product governs requirements, requirements govern design, and requirements plus design govern code, even when the project advances through many iterations.
+What must remain stable is the full direction of authority: goals govern intent, intent governs product, product governs requirements, requirements govern design, and requirements plus design govern realisation, even when the project advances through many iterations.
 
 ---
 
 ## Trace Closure And Anti-Drift Rule
 
@@ -2919,11 +3040,11 @@
 
 1. Run intake triage first and classify the report as a lawful change.
 2. Then write the **Scenario** as the first substantive project artifact for the
    gap so the pressure becomes concrete and testable.
 3. Run **Gap Analysis** — is this a missing implementation or a constitutional insufficiency?
-4. If constitutional: reprice **Goals** when the current work wave changes, write a new **Intent**, then flow forward (product → requirements → design → code).
+4. If constitutional: reprice **Goals** when the current work wave changes, write a new **Intent**, then flow forward (product → requirements → design → realisation).
 5. If implementation: write requirements/design as needed, then implement.
 
 The intake source does not change this rule.
 
 A bug report, feature request, failed testcase, release blocker, or operator
