--- v2/standards/TRAVERSAL_OCCURRENCE_PROFILE.md
+++ v3/standards/TRAVERSAL_OCCURRENCE_PROFILE.md
@@ -1,6 +1,58 @@
 # The `a_c` Traversal Occurrence Profile over Mutable Subjects
+
+<!-- STDO3_PROFILE_BINDING_START -->
+## Governing Relations
+
+This optional profile refines [Foundations](FOUNDATIONS.md) and the
+[Transformation Library](TRANSFORMATION_LIBRARY.md) for immutable histories over
+an externally mutable subject. It imports the exact
+[Axiomatic Calculus](AXIOMATIC_CALCULUS.md) basis through the closed instantiation
+law below. Its profile signature, adoption mapping and owner-issued grants
+retain their own identities. The foundation's generic work and evidence law does
+not enroll every model in this profile or supply a scheduler, state store,
+rollback mechanism or operation authority.
+
+The premises are a mutable subject, bounded observations, explicit operation
+authority and a claim that an immutable record describes one application. From
+[workspace and context](FOUNDATIONS.md#workspace-and-context), the record and
+the actor's context cannot replace the subject or establish unobserved effects.
+From scoped identity and compatible composition, a later application preserves
+the identity and standing of earlier claims while evaluating the current state.
+
+This profile additionally chooses append-only occurrence history, a closed
+signature and exact semantic-admission cuts. These are adopted profile policies,
+not necessary consequences of finite context or requirements on every method
+user. The closed profile fixes every finite field reference domain, cardinality,
+closed enum, inherited record family, refusal mapping, signature preimage and
+publication-resolution condition. The shared
+foundation supplies the shared result and current-state contracts; the profile determines
+its exact records and predicates. A stable SubjectBinding points to mutable
+reality, while each traversal application has a fresh immutable occurrence.
+Application, operation kind, operation, executor, actor, grant and effect
+invocation remain separate coordinates.
+
+| Shared transformation | Occurrence-profile refinement and preserved distinction |
+|---|---|
+| Bind | Resolve the exact imported calculus and profile basis, stable subject binding, traversal application, intended outcome, operation kind and existing owner-issued effect grant. No future result, judgment or event enters an occurrence seed. |
+| Acquire | Obtain bounded pre-effect and post-effect observations, currentness and invalidation evidence, exact external resolutions and the complete event frontier needed by the declared judgment. Missing, stale or ambiguous coordinates retain their prescribed refusal, hold or residual. |
+| Transform | A separately identified and authorized operation may affect the external subject only after exact effect readiness. Candidate claims, invocations, admitted events, materialized relations and later dispositions preserve their distinct immutable identities. |
+| Evaluate | Each inherited Judgment binds its unchanged subject and digest, kind, evaluator, existing authority, exact evidence, provenance and closed decision domain. Readiness, transition and projection judgments conserve the corresponding stop and re-entry laws. |
+| Conjoin | Semantic admission preserves the complete seven-member cut, three admitted judgments, required relation records, equal source-frontier bindings and unique successor frontier. Typed causal subgraphs remain distinct from wider lineage and precedence. |
+| Dispose | Existing competent Product authorities own adoption, operations, admission, correction and projection decisions. No-effect, completed-effect, partial-effect and refused-effect dispositions retain the exact evidence and further-effect restrictions stated below. |
+
+The admission and effect consumers below apply the shared
+[result algebra](FOUNDATIONS.md#result-algebra) and
+[result conjunction](FOUNDATIONS.md#result-conjunction). These bindings neither
+mint a grant nor weaken the closed signature.
+Semantic atomicity retains its profile meaning and imposes no storage
+transaction. Reapplication retains the evolving subject and prior immutable
+history; it supplies no universal side-effect idempotence or rollback guarantee.
+The exact imported calculus's derivation basis is an identity-bearing part of
+AxiomaticCalculusBasis; its exact resolution remains an admission/refusal condition.
+
+<!-- STDO3_PROFILE_BINDING_END -->
 
 ## Position
 
 The **Traversal Occurrence Profile** defines an application-neutral
 model-family signature for immutable application histories over an externally
@@ -313,12 +365,39 @@
 | `T:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
 | `J:*.kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
 | `J:*.subject` | 1 | `AnyLocal` |  | `JudgmentSubject` | `B_model or B_adopted` |
 | `J:*.evaluator` | 1 |  |  | `Evaluator` | `B_adopted` |
 | `J:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
+| `J:*.predicate` | 1 |  |  | `PredicateContract` | `B_adopted` |
+| `J:*.residuals` | 0..* | `X` |  |  | `B_model` |
 | `J:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
 | `J:*.decided_at` | 1 |  |  | `DecisionCoordinate` | `B_adopted` |
+
+The inherited AC-014 record shape, the reference-domain rows above and these
+value contracts close all nineteen Judgment fields. The following values are
+not identity references and therefore are not extra `RefDomain` rows:
+
+| Qualified field | Cardinality | Closed value contract |
+|---|---|---|
+| `J:*.id` | 1 | Exact scoped identity, unique in the model's disjoint local populations under AC-003. |
+| `J:*.subject_digest` | 1 | SHA-256 digest of the canonical unchanged subject named by `subject`. |
+| `J:*.verdict` | 1 | The five core verdicts, including `out_of_frame` for an established material scope or capability shortfall while evaluating an in-domain subject. An out-of-domain request returns `out_of_frame` at the invocation boundary, not a fabricated in-domain judgment. |
+| `J:*.decision` | 1 | Exactly one value from the closed decision domain of the judgment's declared `kind`, with its required reason and mapping below. |
+| `J:*.performance` | 1 | `performed`, `not_performed`, `unconfirmed`; the core legal pairs and evidence conditions apply. Observed extent and interruption remain in the retained outcome/evidence. |
+| `J:*.effects` | 1 field; 1..* observations | Each selected-boundary observation is `not_requested`, `not_started`, `completed`, `partial`, `reverted` or `unknown` under the core effect law. Boundaries and material parts resolve through the existing predicate, subject, evidence and provenance coordinates. |
+
+An established effect-free scope gives an explicit `not_requested` observation
+under the core rule. Any material possibly affected part, requested or
+unintended, without sufficient observation is `unknown`; an absent or empty field is
+not a default and fails this signature. Multiple stages affecting the same part
+are reconciled on the declared boundary before composition under
+[result conjunction](FOUNDATIONS.md#result-conjunction). Every material part
+remains recoverable through the existing evidence relations. These are semantic
+value contracts, not a new nested identity schema or a mandated carrier layout.
+Resolved carriers preserve them. A historical checker bound to an older
+calculus schema checks that schema only; it cannot certify these successor
+Judgment relations by accepting an older record without them.
 
 The inherited transformation's external-resolution coordinates are closed by
 the following finite expansion rather than hidden inside the three local-delta
 rows above:
 
@@ -674,61 +753,95 @@
 invalid_basis
 out_of_scope
 partial_effect
 ```
 
-Every constraint predicate returns exactly one of `satisfied`, `falsified`,
-`indeterminate`, or `invalid_basis`. `satisfied` maps to the judgment's positive
-decision, which is the first decision listed below; `invalid_basis` maps only
-to `invalid_basis`. The constraint table fixes every other mapping. An
-implementation cannot turn an omitted result, residual, or stop into success.
+Every admitted constraint evaluation returns the shared
+[result record](FOUNDATIONS.md#result-algebra) on its exact subject, basis and
+predicate. All five core verdicts are available when evaluating an in-domain
+subject. A request outside that domain returns `out_of_frame` at the invocation
+boundary; it is not forged into an in-domain judgment. Performance and effect state remain separate
+coordinates. An omitted or unperformed evaluation is never a positive result.
+
+The judgment decisions below are domain refinements. `satisfied` maps to the
+positive decision, which is first in each row; `invalid_basis` maps only to
+`invalid_basis`. The constraint table fixes other mappings. Keep the original
+decision, constraint predicate, evidence, residuals and stop in the shared
+return. The table does not define a second aggregation or result algebra.
 
 The closed judgment domains are:
 
 | Judgment kind | Unchanged subject | Decision domain | Required evidence | Stop, residual, and re-entry law |
 |---|---|---|---|---|
 | `model_validation` | `OccurrenceModelSubject` | `valid`, `hold`, `refused`, `invalid_basis` | exact model id/digest, profile basis, and typed graph populations | refusal or invalid basis; unresolved refs retain `gap` until repaired |
 | `occurrence_admission` | `Occurrence` | `admitted`, `hold`, `refused`, `invalid_basis` | exact occurrence id/digest and resolved pre-existing seed inputs | missing seed retains `hold` plus `unresolved_cause`; re-enter with a new complete occurrence candidate |
 | `event_admission` | `FrameworkEvent` | `admitted`, `hold`, `refused`, `invalid_basis`, `out_of_scope` | exact event id/digest, payload digest, scope authority, and source frontier | unresolved scope retains `hold` plus `unresolved_scope`; incompatible scope refuses |
-| `claim_admission` | `RelationClaim` | `admitted`, `hold`, `refused`, `invalid_basis` | exact claim id/digest, endpoints, qualifiers, claimant authority, and current source frontier | unresolved cause or stale frontier retains `hold`; re-enter with a new claim over the current frontier |
-| `semantic_cut_admission` | `SemanticAdmissionCut` | `admitted`, `hold`, `refused`, `invalid_basis` | exact seven-member cut and source/successor frontier equality | incomplete or inconsistent cut refuses; stale source frontier retains `hold` plus `stale_frontier` and requires reconstruction |
+| `claim_admission` | `RelationClaim` | `admitted`, `hold`, `refused`, `invalid_basis` | exact claim id/digest, endpoints, qualifiers, claimant authority, and current source frontier | unresolved cause retains `hold` plus `unresolved_cause`; established staleness falsifies admission while retaining `hold` plus `stale_frontier`; re-enter with a new claim over the current frontier |
+| `semantic_cut_admission` | `SemanticAdmissionCut` | `admitted`, `hold`, `refused`, `invalid_basis` | exact seven-member cut and source/successor frontier equality | conjoin claim/event judgments and declared cut joins; missing, held or unauthenticated judgment support retains `hold` plus `unresolved_cause`, naming its slot; established staleness falsifies admission while retaining `hold` plus `stale_frontier`; re-entry follows the unchanged-subject rule below |
 | `effect_readiness` | `EffectSubject` | `ready`, `stale`, `unauthorized`, `hold`, `invalid_basis` | exact pre-observation, invocation, operation, grant, territory, and invalidation state | stale yields `hold` plus `stale_currentness` and re-observation; unauthorized yields `refusal` and no dispatch |
 | `transition_evaluation` | `TransitionSubject` | `satisfied`, `falsified`, `partial`, `indeterminate`, `refused`, `invalid_basis` | exact pre/post observations, intended outcome, disposition, and bounded effect evidence | partial yields `partial_effect`; indeterminate retains `hold` plus a declared residual; refused yields `refusal` |
 | `frontier_projection` | `Projection` | `admitted`, `hold`, `gap`, `refused`, `invalid_basis` | exact projection/frontier ids and digests, complete members, basis, precedence law, boundary, and residuals | stale frontier retains `hold` plus `stale_frontier`; unresolved lineage retains `gap`; re-enter with a new projection |
 
 Each is an inherited `Judgment` and therefore carries unchanged subject id and
 digest, evaluator, authority, evidence, provenance, and decision coordinate.
 The judgment kind defines the applicable stops and residuals; none is inferred
 from prose.
+
+`valid`, `admitted` and `ready` mean `satisfied` only for their respective
+validation, admission or readiness predicates. They do not establish the
+intended external outcome. `hold`, `gap` and `indeterminate` retain
+`indeterminate` where decisive evidence is missing. A demonstrated false
+predicate remains `falsified`, retaining `refused`, `stale`, `unauthorized`,
+`out_of_scope` or the declared `hold` for an established stale frontier as
+mapped below. In particular `out_of_scope` from a false
+`event_scope_compatible` constraint is a falsified compatibility claim; its
+spelling does not turn it into the invocation-boundary `out_of_frame` result.
+For a `partial` transition, the exact intended-outcome predicate and evidence
+determine `falsified` if non-fulfilment is established, or `indeterminate` if
+fulfilment remains unknown. Its effect state separately retains observed
+partiality or uncertainty. These distinctions make each complete return map to
+one core verdict without discarding the profile's finer decision.
+
+Source-frontier currentness is a material join of claim admission, cut
+admission and frontier projection. Established staleness falsifies that exact
+predicate; its `hold` decision with cause `stale_frontier` prevents use and
+requires reconstruction. Unknown currentness is indeterminate. The word
+`hold` alone decides neither case. A missing material scope or capability on
+an in-domain subject retains core `out_of_frame`, stop `out_of_scope` and
+`unresolved_cause` naming the missing relation. Its decision is `hold`, or
+`indeterminate` for `transition_evaluation`, whose domain has no `hold` value.
+Re-enter with a capable frame under the original subject/basis or retain the
+stop. These diagnostic rules apply to every judgment kind without adding a
+second verdict domain.
 
 The closed constraint domains are:
 
 | Constraint kind | Subject | Deciding judgment | `falsified` mapping | `indeterminate` mapping |
 |---|---|---|---|---|
 | `identity_dependency_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
 | `occurrence_causation_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
 | `event_causation_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
 | `occurrence_seed_complete` | `Occurrence` | `occurrence_admission` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
-| `relation_claim_admissible` | `RelationClaim` | `claim_admission` | `refused` plus `refusal` | `hold` plus `unresolved_cause` or `stale_frontier` |
-| `semantic_cut_complete` | `SemanticAdmissionCut` | `semantic_cut_admission` | `refused` plus `refusal` | `hold` plus `stale_frontier` |
+| `relation_claim_admissible` | `RelationClaim` | `claim_admission` | `refused` plus `refusal`; established stale frontier retains `hold` plus `stale_frontier` | `hold` plus `unresolved_cause` |
+| `semantic_cut_complete` | `SemanticAdmissionCut` | `semantic_cut_admission` | `refused` plus `refusal`; established stale frontier retains `hold` plus `stale_frontier` | `hold` plus `unresolved_cause` naming the undecided slot or join |
 | `pre_effect_current` | `EffectSubject` | `effect_readiness` | `stale` plus `hold` and `stale_currentness` | `hold` plus `stale_currentness` |
 | `operation_grant_contains_effect` | `EffectSubject` | `effect_readiness` | `unauthorized` plus `refusal` | `hold` plus `unobserved_subject_state` |
 | `event_scope_compatible` | `FrameworkEvent` | `event_admission` | `out_of_scope` plus `refusal` | `hold` plus `unresolved_scope` |
-| `frontier_complete` | `Projection` | `frontier_projection` | `refused` plus `refusal` | `hold` plus `stale_frontier` |
+| `frontier_complete` | `Projection` | `frontier_projection` | `refused` plus `refusal`; established stale frontier retains `hold` plus `stale_frontier` | `hold` plus `unresolved_cause` |
 | `transition_subject_complete` | `TransitionSubject` | `transition_evaluation` | `refused` plus `refusal` | `indeterminate` plus `unobserved_subject_state` |
 
 Each constraint declares zero latitude unless its exact record names a
 `latitude_ref`. Silence is not latitude. The residual kind fixes re-entry:
 
 | Residual kind | Subject | Required re-entry |
 |---|---|---|
 | `unobserved_subject_state` | `SubjectBinding` | acquire a bounded observation or retain hold |
 | `partial_effect` | `EffectInvocation` | acquire post-observation and explicit disposition |
-| `unresolved_cause` | claim or event | acquire authority and evidence or retain unresolved |
+| `unresolved_cause` | exact judgment subject | acquire the named missing authority, evidence, judgment or frame capability; re-evaluate the unchanged subject when applicable, otherwise construct its successor |
 | `unresolved_scope` | `FrameworkEvent` | declare lawful scope or refuse admission |
 | `competing_lineage` | `EventFrontier` | apply an authorized `frontier_projection` judgment |
-| `stale_frontier` | `Projection` | construct a new exact frontier and projection |
+| `stale_frontier` | claim, semantic cut or projection | construct a new subject over the current exact frontier; no stale subject is rewritten in place |
 | `stale_currentness` | `EffectSubject` | re-observe and re-judge before effect |
 | `unobserved_external_mutation` | `SubjectBinding` | observe or retain an explicit material unknown |
 
 `Sigma_occurrence.FunctorKind` contains exact refs to `F_D`, `F_P`, and `F_H`
 from `b_ac` and no other functor kind. The profile changes none of their laws.
@@ -793,10 +906,18 @@
   -> successor frontier F_k_plus_1
   -> SemanticAdmissionCut a = (c, j_c, e, j_e, r, F_k, F_k_plus_1)
   -> Judgment j_a over unchanged a
 ```
 
+Evaluate `j_a` by conjoining the authenticated claim judgment `j_c`, event
+judgment `j_e` and the cut's declared material joins through
+[result conjunction](FOUNDATIONS.md#result-conjunction). `j_a` is this
+evaluation's output, never its own input. Retain each exact component judgment
+and required equality relation. A refusal remains visible beside a
+missing judgment; absence cannot erase the refusal or complete the cut. The
+conjunction does not widen the admission authority of any participant.
+
 Only `j_c.decision = admitted`, `j_e.decision = admitted`, and
 `j_a.decision = admitted` admit the complete semantic cut. `c`, `j_c`, `e`,
 `j_e`, `r`, `a`, and `j_a` have distinct identities and authority.
 Construction of `c` does not admit it. Judgment does not rewrite its subject.
 An event does not inherit the candidate's authority. Materialization cannot
@@ -817,13 +938,42 @@
 j_a.subject = a.id
 j_a.subject_digest = sha256(canonical bytes of a)
 ```
 
 Each judgment has the complete inherited context, owner, scope, basis,
-evaluator, authority, decision, evidence, provenance, and decision-time
+evaluator, authority, predicate, verdict, decision, performance, effects,
+evidence, residuals, provenance, and decision-time
 fields. A missing cut judgment, non-`admitted` decision, wrong subject or
-digest, or cross-basis judgment refuses the semantic cut.
+digest, or cross-basis judgment leaves the semantic cut unadmitted; these
+conditions do not all establish the same verdict.
+
+Contribution authentication requires the exact subject, digest, declared basis
+and judgment authority. A mismatched contribution cannot decide the required
+slot; retain the missing admissible support rather than inventing its result.
+Within an interpretable cut, the required membership and equality relations
+below are material joins. An established failure of such a join is
+counterevidence to cut admission, not a missing governing basis.
+
+Apply core conjunction before mapping `j_a`: `falsified` maps to `refused`,
+except that established source-frontier staleness retains the declared `hold`
+and `stale_frontier` without lowering the verdict. `invalid_basis` maps to
+`invalid_basis`; `indeterminate` and `out_of_frame` retain the causes and stops
+declared above. `satisfied` permits `admitted` only when `j_c` and `j_e` are
+exact admitted judgments and all required joins are established. Thus an
+authenticated refusal survives a missing companion; a held or absent judgment
+alone does not fabricate a refusal; and an invalid required basis remains
+invalid when no applicable falsification decides the conjunction. An
+uninterpretable composite basis follows the core invalid-basis rule.
+
+The downstream consumer requires the resulting `j_a` to admit the cut. A
+missing `j_a` remains that consumer's absent slot, not an input to its own
+evaluation or an invented held judgment. A new judgment may evaluate unchanged
+cut bytes after missing support is supplied. If a referenced judgment, frontier
+or other cut member changes, construct the corresponding successor cut;
+never replace a member behind an existing digest. Missing support cannot make
+an actually incomplete or mismatched cut complete. The duplicate-cut rule below
+applies to cut identity, not to a newly identified judgment over unchanged bytes.
 
 An admission event identity binds its event kind, payload digest, scope,
 optional occurrence, exact claim, claim judgment, source frontier, owner,
 scope, and basis. The materialized relation identity binds the unchanged claim,
 claim judgment, event, event judgment, and profile basis.
@@ -876,12 +1026,15 @@
 For a relation claim, one admitted semantic cut contains the unchanged claim,
 its admission judgment, the event and its scope/admission judgment, the
 deterministic materialized relation, the exact source frontier, and the unique
 successor frontier. The source frontier named by the claim, event, and cut is
 identical. The successor equals that frontier plus exactly the admitted event.
-Missing, conflicting, or inconsistent members refuse the cut. This is semantic
-atomicity; the profile does not prescribe a storage or transaction mechanism.
+A demonstrated missing or inconsistent required member defeats the complete-cut
+predicate; missing judgment support keeps the cut unadmitted under the
+conjunction rule above. No unresolved or refused cut admits a subset. This is
+semantic atomicity; the profile does not prescribe a storage or transaction
+mechanism.
 
 ### OP-003 Correction Without Erasure
 
 `corrects_event(new, existing)` retains both immutable events. Correction
 changes later projection through an explicit selection law. It does not delete,
@@ -972,23 +1125,51 @@
 does not satisfy the grant.
 
 The disposition law is closed:
 
 - `no_effect` has no dispatched invocation and records that no domain effect
-  was attempted;
+  was attempted, whether no operation was requested or a requested operation
+  stopped before dispatch;
 - `completed_effect` binds one dispatched invocation, bounded post-observation,
   and sufficient effect evidence;
 - `partial_effect` binds one dispatched invocation, bounded post-observation,
   bounded evidence, the `partial_effect` residual and stop, and explicit
   re-entry before any further effect; and
 - `refused_effect` binds the refused invocation attempt and `refusal` stop, with
-  evidence that no authorized mutation began.
+  evidence that no mutation began.
 
 `invokes_effect` exists if and only if a concrete invocation was dispatched.
 `unauthorized` or `stale` readiness never dispatches it. The immutable
 `EffectInvocation` contains no future disposition; `EffectDisposition` records
 the later outcome without rewriting the invocation.
+
+The shared return conserves the effect observation, rather than mapping labels
+without evidence. `no_effect` uses `not_requested` only for an established
+effect-free scope under the core rule, not merely an absent operation request.
+For a requested operation stopped before dispatch, `no_effect` is `not_started`
+only with authenticated non-dispatch evidence. Without that support the claimed
+disposition remains unadmitted and the requested effect is `unknown`.
+`refused_effect` with evidence that no mutation began is `not_started`;
+`completed_effect` with its required observation is `completed`.
+
+`partial_effect` retains the domain's incomplete-effect disposition and its
+re-entry requirement. At the declared core boundary, a completed part with a
+known unexecuted or reverted remainder is `partial`. If at least one part began
+and every begun part is observed reversed, the state is `reverted`, retaining
+the reversal and any unstarted remainder. Every material external part stays
+inside the boundary; a local rollback cannot conceal an irreversible message.
+Any uncertain material remainder makes the state `unknown`, retaining the
+observed parts. The original domain disposition and reason remain visible;
+these refinements add no effect-operation authority or new disposition kind.
+A dispatch followed by lost transport without resolving observation cannot
+become `no_effect`, `refused_effect` or `completed_effect`. Missing
+post-observation remains an explicit residual and prevents a complete profile
+disposition from being manufactured. Observation is required before any action
+that depends on whether that effect happened, including a repeat.
+An unauthorized mutation is still an actual effect. Lack of permission cannot
+establish `not_started` or justify a `refused_effect` disposition that conceals
+observed or uncertain mutation.
 
 `j_ready` judges the unchanged `EffectSubject` immediately before effect
 dispatch under the application's declared currentness and invalidation law. If
 the pre-observation or grant has become stale, the effect does not start; the
 application re-observes and issues a new readiness subject and judgment or
@@ -1164,10 +1345,20 @@
 digest occurs once in the predecessor manifest, and each fragment resolves one
 heading in those bytes under the publication's semantic-address rule. A string
 with the right shape, an unresolved basis record, a mismatched manifest or
 member, a missing or extra principle ref, an invented or absent fragment, an
 unbound predecessor byte sequence, or a same-carrier derivation refuses.
+
+Resolve the historical byte predicates from complete successor-owned
+[derivation verification material](IDENTITY_METHOD.md#derivation-verification-material)
+when present in the exact publication manifest. Verify the material's member
+digest, its source-member pins, reconstructed historical digests and complete
+principle-ref population before admitting the imported basis. The original
+historical manifest and clause identities remain distinct from the successor
+publication and external judgments. This evidence resolution requires neither
+the predecessor Install nor historical retrieval; absent or defective material
+retains the refusal conditions above.
 
 The profile publication member resolves by the same manifest/member rule. A
 mutable source path, strategy post, implementation, or consumer mapping cannot
 substitute for either imported basis or publication identity.
 
