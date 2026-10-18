# Domain Writer return

The six assigned members are drafted for the standalone common candidate. This is an author return under T-003, not independent review, acceptance or qualification. No frames, other candidate files, Git index or commits were changed by this Writer.

| Item | Receiving locus | Result |
|---|---|---|
| M1 | TRAVERSAL_OCCURRENCE, Mutable-subject effect relation | Both refusal evidence conditions require no mutation in the material effect boundary; actual or uncertain unauthorized effects stay visible. |
| M2 | UX, State transitions; Effect membrane; Msg-replay proof; Results | Outcome messages cover unresolved effects, observation and recovery precede outcome-dependent repetition, and replay success does not prove external completion. |
| M7 | DESIGN_MODULE, Foundation to law; Design review questions | Both loci withhold unsupported conformance and diagnose through the actual owner. All 56 review questions are unchanged. |
| A2 | WORLD_MODEL, Foundation to law | Append-only is the profile's selected mechanism, not a deduction from fact preservation. The operational ledger law is unchanged. |
| R5 | Outside this territory | The four agreed targets belong to core/method Writers. No extra domain rule was introduced. |

M1, M2 and M7 remain proposed meaning changes needing exact owner acceptance. This external record carries their pending standing.

All six historical source-disposition appendices, inline predecessor citations and construction-history explanations are outside the package. Exact appendices are retained in [domain.json](domain.json); the complete patch below retains every other removed passage, including World Model research provenance.

TRAVERSAL_OCCURRENCE follows the core Writer's local calculus basis: the same exact package for derivation and publication, distinct premise and member roles, complete local premise references, and no predecessor manifest. Record schemas are unchanged. Stable and RC publication URIs are allowed; instantiated identity records stay outside the member set whose manifest they name to avoid digest cycles. This standalone adaptation is additional to M1 and needs its own semantic review.

WORLD_MODEL preserves candidate construct and overlay standing, all four working refinements, the direction-native conditional-independence promotion gate, and independent entity-cut admissibility. Historical experiment claims and the external program pin are externalized; no empirical establishment claim is added. Companion routes name local method owners.

UX retains both compliance tests and their current conservative application. Q10 remains unresolved for the governing authority.

Mechanical checks resolved 847 Markdown file/fragment references within the candidate with no failure. Seed hashes match the selected frozen package; all 56 design questions and both traversal record schemas are unchanged; the operational attribute-ledger law is unchanged after provenance-citation removal. These checks establish only their named properties. Precise loci, hashes and distinguishing author walkthroughs are in [domain.json](domain.json).

Root integration still needs frame regeneration, final package checks and covering nonauthor review.

<details>
<summary>Complete patch against the frozen Claude package</summary>

```diff
--- specification_methodology/v3/build_tenants/claude/standards/TRAVERSAL_OCCURRENCE.md
+++ specification_methodology/v3/build_tenants/common/standards/TRAVERSAL_OCCURRENCE.md
@@ -21,9 +21,7 @@
 `Projection`. They claim neither the core's release cut nor its product
 lineage, nor any other member's frontier; a `frontier_projection`
 judgment judges a `Projection` record and is not an
-[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection) projection. A route written `rc.2 #anchor` is into
-`stdo://releases/v2.5.1-rc.2/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` and
-is provenance only (P3, P1).
+[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection) projection (P3, P1).
 
 ## Position
 
@@ -87,8 +85,7 @@
 
 The Scope, the Exclusions and the Conformance obligations apply these
 consequences, and every clause names the principle that requires it
-([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)). The table is
-new in this corpus. Purpose and material relation: an actor started on
+([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)). Purpose and material relation: an actor started on
 this member sees which rules follow from the foundations and which are
 choices, and who owns each choice, so no choice is presented as derived
 (P6, P1).
@@ -839,7 +836,7 @@
 | `stale_currentness` | `EffectSubject` | re-observe and re-judge before effect |
 | `unobserved_external_mutation` | `SubjectBinding` | observe or retain an explicit material unknown |
 
-Mapping to the core result algebra, new in this corpus. Purpose:
+Mapping to the core result algebra. Purpose:
 [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states every outcome in
 the core or in a refinement that maps each refined value to exactly one
 core value, and
@@ -986,7 +983,7 @@
 
 | Value | Core value | Ground |
 |---|---|---|
-| stop `hold` | indeterminate | the step stops with the deciding evidence not yet admitted (missing seed, unresolved cause or scope, stale frontier or currentness, unobserved state), so the admissible evidence cannot decide whether the application can reach its declared result ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results); rc.2 RF-012); its residual names the evidence that would decide |
+| stop `hold` | indeterminate | the step stops with the deciding evidence not yet admitted (missing seed, unresolved cause or scope, stale frontier or currentness, unobserved state), so the admissible evidence cannot decide whether the application can reach its declared result ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results); RF-012); its residual names the evidence that would decide |
 | stop `gap` | invalid_basis | a reference or lineage member the judgment requires is unresolved, its resolution still open as AC-007 defines for `gap`, so the closure it rests on is undefined on this basis (AC-003, AC-010) and the basis cannot support the judgment until repaired |
 | stop `refusal(constraint)` | falsified | the falsified constraint's defect is the counterexample, as construction availability maps `refused` to falsified (P5, P6) |
 | stop `refusal(basis)` | invalid_basis | the basis cannot support the judgment; the constraint rule above maps `invalid_basis` only to that core value |
@@ -1346,7 +1343,18 @@
   post-observation, bounded evidence, the `partial_effect` residual and
   stop, and explicit re-entry before any further effect; and
 - `refused_effect` binds the refused invocation attempt and the `refusal`
-  stop, with evidence that no authorised mutation began.
+  stop, with evidence that no mutation began within the material effect
+  boundary.
+
+A refusal records a decision about authority; it does not by itself
+establish the absence of a mutation. Where an unauthorised mutation
+occurred or remains possible within the material effect boundary, retain
+the actual invocation, observations and uncertainty. Such a case does not
+satisfy the evidence condition for `refused_effect`; its effect result
+and recovery follow [ACTIVATION §3 Effects](ACTIVATION.md#effects) and
+[ACTIVATION §5 Recovery](ACTIVATION.md#5-work-state-and-restart). `not_effected` means that
+the intended outcome was not attained, not that no effects occurred
+(P5, P6).
 
 `invokes_effect` exists if and only if a concrete invocation was
 dispatched; `unauthorized` or `stale` readiness never dispatches it. The
@@ -1354,7 +1362,7 @@
 `EffectDisposition` records the later outcome without rewriting the
 invocation (P3, P6).
 
-Mapping of the dispositions to the core, new in this corpus. Purpose:
+Mapping of the dispositions to the core. Purpose:
 [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) places the results of
 effects in the core. Material relation: whether an occurrence's effect
 may be repeated or relied on, which is the material relation of
@@ -1370,7 +1378,7 @@
 | `completed_effect` | `completed` | satisfied | the bounded post-observation and sufficient effect evidence establish that the intended effect occurred and that the effect has ended |
 | `partial_effect(not_attained)` | `not_effected` | falsified | the admitted evidence establishes that the intended outcome is not attained and that no later completion of the effect can attain it; the part that did occur is named with the value, and an end of the effect that the evidence does not establish is recorded beside it, not in it |
 | `partial_effect(undecided)` | `completion_unknown` | indeterminate | the evidence cannot decide whether the intended outcome is or will be reached |
-| `refused_effect` | `not_effected` | falsified | the evidence shows that no authorised mutation began |
+| `refused_effect` | `not_effected` | falsified | the evidence shows that no mutation began within the material effect boundary |
 | `no_effect` | `not_effected` | falsified | the admitted disposition records that no invocation was dispatched, and the record is exact because `invokes_effect` exists if and only if one was; so the occurrence effected nothing on the subject |
 
 An occurrence that no `EffectInvocation` names intends no effect.
@@ -1548,28 +1556,28 @@
 ```
 
 The imported calculus basis resolves as the exact RFC 8785 bytes of an
-`AxiomaticCalculusBasis` record with the required kind, schema, concept,
-derivation basis and publication basis. Its calculated identity equals
-both `calculus_basis_identity` fields. Its publication manifest digest
-resolves the exact manifest bytes; that manifest contains the calculus
-member path and digest once; the resolved calculus member bytes have that
-digest; and `calculus_signature_schema_clause_ref` is that exact member
-URI plus the fragment of the calculus signature clause, `#2-signature` in
-this corpus's AXIOMATIC_CALCULUS. Its distinct predecessor manifest
-resolves every sorted principle ref, without duplicates, inside the
-declared predecessor release. The principle-ref population is exactly the
-absolute predecessor-release expansion of every derivation address that
-the resolved calculus member declares: neither a selected subset nor an
-independently invented list, and its size is whatever that member's
-derivation account declares
-([AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity)). Each
-referenced predecessor member resolves as exact bytes whose digest occurs
-once in the predecessor manifest, and each fragment resolves one heading
-in those bytes under the publication's semantic-address rule. A string of
-the right shape, an unresolved basis record, a mismatched manifest or
-member, a missing or extra principle ref, an invented or absent fragment,
-an unbound predecessor byte sequence, or a derivation from the same
-carrier refuses (P3, P6, P5).
+`AxiomaticCalculusBasis` record and satisfies
+[AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity). Its
+calculated identity equals both `calculus_basis_identity` fields. Its
+publication manifest digest resolves the exact manifest bytes; that
+manifest contains the calculus member path and digest once; the resolved
+calculus member bytes have that digest; and
+`calculus_signature_schema_clause_ref` is that exact member URI plus
+`#2-signature` (P3, P5).
+
+The calculus derivation and publication bases bind the same exact
+immutable package. Their roles remain distinct: the derivation basis
+names the normative premises and owners, and the publication basis names
+the calculus member that states their application. The principle-ref
+population is exactly the sorted, duplicate-free expansion of the local
+derivation addresses that the resolved calculus member declares under
+§8: neither a selected subset nor an independently invented list. Every
+referenced member resolves to exact bytes whose digest occurs once in
+the package manifest, and each fragment resolves one heading under the
+publication's semantic-address rule. An unresolved basis record, a
+mismatched manifest or member, a missing or extra principle ref, an
+invented or absent fragment, or unbound member bytes refuse admission
+(P3, P6, P5).
 
 The profile publication member resolves by the same manifest and member
 rule. A mutable source path, a strategy post, an implementation or a
@@ -1577,7 +1585,10 @@
 publication identity (P3, P6).
 
 `publication_basis.release_uri` is one absolute immutable
-`stdo://releases/v<version>-rc.<positive-ordinal>/` URI.
+`stdo://releases/v<version>/` URI for a release or
+`stdo://releases/v<version>-rc.<positive-ordinal>/` URI for a release
+candidate. Its spelling establishes identity, not acceptance or release
+standing.
 `publication_basis.member_uri` is exactly that URI plus
 `standards/TRAVERSAL_OCCURRENCE.md`. The installed release manifest named
 by `manifest_sha256` contains exactly one standards member with that path
@@ -1591,11 +1602,13 @@
 Any change to the calculus basis, the signature refs, the closed signature
 or the profile member bytes mints a new profile basis. Supersession is an
 external Product and release judgment, and an earlier basis never silently
-advances (P3, P6). The predecessor edition's coordinates are provenance of
-this edition, not its identity: cut `stdo://releases/v2.5.1-rc.2/`, member
-`standards/TRAVERSAL_OCCURRENCE_PROFILE.md` SHA-256
-`618bb7c8f9f1eab8283cf595ac9da3533f0f9cf80a684c6f42e09142da6590c1`,
-concept identity unchanged (P3).
+advances (P3, P6).
+
+The instantiated signature and basis records are issued after their
+member bytes are frozen. They are excluded from the member set whose
+manifest digest they name; their schemas above do not embed an instance
+or its digest in those members. This keeps the identity preimages
+reconstructable without a digest depending on itself (P3).
 
 ## Exclusions
 
@@ -1655,57 +1668,3 @@
 Representative examples or checkers establish only the claims they
 actually evaluate. They do not become an occurrence engine or a semantic
 authority (P6).
-
-## Source dispositions
-
-Rows of rc.2 TRAVERSAL_OCCURRENCE_PROFILE.md received by this member, all
-25 under STDO-UP-015. Anchors are into rc.2
-TRAVERSAL_OCCURRENCE_PROFILE.md; a locus is a section of this file. Every
-conserved row is restated in this member's own text at the predecessor's
-modal force; a route is provenance only. Formal content (code blocks and
-tables) is carried exactly and the prose around it is rewritten; headings
-keep the predecessor's slugs so that the ten signature fragments resolve
-in this member. Generalisations recorded here: the publication member path
-and the calculus signature fragment follow the successor corpus; the
-notation `instantiate_signature`, `OccurrenceSignatureDefinition` and the
-`Sigma:ReferenceDomain`, `Sigma:ExternalTargetKind` and
-`Sigma:BasisRelation` populations, which neither calculus member defines,
-is stated as the profile's own; American spellings are written British in
-prose and kept in identifiers (P3, P6).
-
-Three clauses have no predecessor row and are new: the mapping of the
-judgment decisions and stop kinds to the core result algebra (Closed
-constraint, judgment, residual and stop kinds) and the mapping of the
-effect dispositions (Mutable-subject effect relation), which
-FOUNDATIONS §4 Results and AXIOMATIC_CALCULUS §5 require (P5); and the
-family table (Position, Foundation to law), in the format of
-FOUNDATIONS §3 Foundation to law (P6, P1).
-
-| rc.2 anchor | Disposition | Locus |
-|---|---|---|
-| #position | conserved; both URN blocks carried exactly; the family table under Foundation to law is new | Position |
-| #scope | conserved | Scope |
-| #imported-calculus-boundary | conserved; `RecordKind_ac` and `Population_M` pointed to AXIOMATIC_CALCULUS §2 | Imported calculus boundary |
-| #closed-semantic-object-sorts | conserved; the nineteen-sort table carried exactly | Closed semantic-object sorts |
-| #finite-reference-domain-table | conserved; the basis codes, every table row, the external-resolution expansion and `ResolutionRefDomain` carried exactly | Closed semantic-object sorts, Finite reference-domain table |
-| #closed-event-kind-population | conserved | Closed event-kind population |
-| #closed-relation-families | conserved; the twenty-four relation kinds, qualifier record, value domains, contract, cardinality function and congruence law carried exactly | Closed relation families |
-| #closed-constraint-judgment-residual-and-stop-kinds | conserved; the four kind populations and three tables carried exactly; functor-kind laws pointed to AXIOMATIC_CALCULUS §5; the mapping of the judgment decisions and stop kinds to the core algebra is new, each refinement naming its predicate, as the profile's mapping for every traversal, `hold`, `gap` and the two `refusal` values taking the core values AXIOMATIC_CALCULUS AC-007 gives them, and a traversal record's `stop_states` refining those four values by cause in the PROFILES §1 binding shape, each refined value keeping its parent's core value; values whose core value depends on their cause are split by it: `partial_effect(not_attained)` and `partial(not_attained)` map to falsified when the admitted evidence, read under the outcome contract, establishes that the intended outcome is not met and that no later completion of the effect can meet it, whether or not the effect has ended, an end not established being recorded in the `partial_effect` residual beside the value, and `partial_effect(undecided)` and `partial(undecided)` to indeterminate when the evidence cannot decide, under the conserved effect law, the loss stated for both; `refusal(constraint)` and `refused(constraint)` map to falsified when the refusal follows a falsified constraint, a row of the constraint table or a structural constraint, or closes the `unresolved_scope` re-entry without the lawful scope declaration, whatever condition of the basis the refusal also names, that condition and any co-emitted `invalid_basis` decision being reported as their own invalid_basis result, and `refusal(basis)` and `refused(basis)` to invalid_basis only when the refusal names conditions of the basis and no demonstrated violation by what is under judgment, a refusal emitted with an `invalid_basis` decision included and a violation inside an input acted on as the basis being a condition of the basis, the cause of each refusal being the one AXIOMATIC_CALCULUS AC-007 states for the conditions it names, a relation qualifier recording it where one records the cause, and a basis mismatch inside the model or a record, a qualifier record included, being AC-007's mixed bases, a condition of the basis, so that a refusal naming only it is `refusal(basis)`; an unresolved reference retains `gap` only while its resolution is open as AC-007 defines, a reference evaluated to no target being dangling | Closed constraint, judgment, residual and stop kinds |
-| #occurrence-identity | conserved | Occurrence identity |
-| #op-001-seed-acyclicity | conserved | OP-001 |
-| #candidate-judgment-event-and-relation-separation | conserved | Candidate, judgment, event and relation separation |
-| #op-002-atomic-semantic-admission | conserved | OP-002 |
-| #op-003-correction-without-erasure | conserved | OP-003 |
-| #causality-and-typed-lineage | conserved | Causality and typed lineage |
-| #op-004-precedence-is-not-authority | conserved | OP-004 |
-| #mutable-subject-effect-relation | conserved; the mapping of the four dispositions to the core through ACTIVATION §3 Effects, for an occurrence that an `EffectInvocation` names, is new | Mutable-subject effect relation |
-| #op-005-mutable-reality-conservation | conserved | OP-005 |
-| #op-006-immutable-iteration-history | conserved | OP-006 |
-| #event-frontier-and-projection | conserved | Event frontier and projection |
-| #op-007-scope-conservation | conserved | OP-007 |
-| #authority-and-adoption | conserved | Authority and adoption |
-| #exact-profile-identity | conserved | Exact profile identity |
-| #closed-profile-signature | conserved, save the sentence split to the child row below; the signature, basis and identity blocks and the ten-fragment list carried exactly, the fragments resolving to this member's headings; the member path written `standards/TRAVERSAL_OCCURRENCE.md` and the calculus clause `#2-signature`, the carried block's "Core Signature clause" being AXIOMATIC_CALCULUS §2 Signature | Exact profile identity, Closed profile signature |
-| #closed-profile-signature-fourteen-members | superseded, proposed and pending the product owner's acceptance, by AXIOMATIC_CALCULUS §8; the rc.2 sentence "For the calculus edition bound by this profile publication candidate, that population has fourteen members" counted the derivation account of the rc.2 calculus edition; §8 retains the principle-ref population as the exact expansion of the bound calculus member's derivation account, without a hard-coded count and recomputed when that account changes, so the population law stays and the edition count is replaced by the size that account yields; child row of `#closed-profile-signature`, its anchor synthetic | Closed profile signature |
-| #exclusions | conserved | Exclusions |
-| #conformance-obligations | conserved; all twenty-one obligations | Conformance obligations |
--- specification_methodology/v3/build_tenants/claude/standards/UX.md
+++ specification_methodology/v3/build_tenants/common/standards/UX.md
@@ -32,9 +32,7 @@
 function and ABG are the graph-execution profile's terms, used here as
 that profile names them; AssetSurface and workorder name carriers that a
 product's design publishes or admits (§3, §7), used here as that design
-names them. Binding declared under PROFILES §1 (new; it reads TICKETS' tier-2
-generalisation back to this profile's objects so the escrow law has an
-exact subject on a UX surface): where TICKETS §3 Compliance escrow names
+names them. Binding declared under PROFILES §1: where TICKETS §3 Compliance escrow names
 "replay proof for product-meaningful user-interface interactions" and
 "changed public published-function or public carrier contracts", a UX
 surface governed by this profile binds them to the Msg-replay proof of §8
@@ -47,18 +45,12 @@
 
 Each clause names the principle that requires it (P0 to P6, FOUNDATIONS
 §3), as [FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)
-requires. The predecessor's "must" is written in the
-indicative; its "should", "may", "may not", "recommended", "typically",
-"mandatory", "optional", "allowed", "at least" and "non-normative" keep
-their force. A route written `rc.2 #anchor` is into
-`stdo://releases/v2.5.1-rc.2/standards/UX_METHOD.md` and is provenance
-only; every predecessor row received here is restated in this text, and
-nothing here depends on that cut to be applied.
+requires.
 
 ## 1. Position
 
 This profile exists to make one instruction precise: "using the UX
-profile, build this UI surface" (P2; rc.2 #1-position). It adopts the Elm
+profile, build this UI surface" (P2). It adopts the Elm
 Architecture (TEA) as its constitutional process model: the view is a
 pure projection of typed state; state transitions are pure reductions
 over typed messages; side effects are values the reducer describes and a
@@ -75,7 +67,7 @@
 ([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)),
 recording the adoption in a product definition, ticket, design module or
 review, this profile is the sole UX realisation authority for that
-surface (P6; rc.2 #1a-constitutional-authority-rule). Project-local ADRs
+surface (P6). Project-local ADRs
 may choose the stack; they may not weaken the process model. Existing
 code, component-library convention, screenshots, comments, design
 history, prototype behaviour and generated artifacts are evidence only
@@ -133,7 +125,7 @@
 | P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); F4 imported ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)) | By P4b the record of a step is not re-acquirable from memory, so a surface's behaviour must be reproducible from its recorded inputs; continuation therefore never leaks into the view, and by P6 a closure claim needs its evidence, so a product surface claims closure only with an executable replay proof for each product-meaningful interaction family | [§8](#8-continuation-and-replay); [§8 Msg-replay proof](#msg-replay-proof) | the Msg-replay test, which replays messages against an empty state, and the six contents of a replay proof: this profile; the proof surface: the project's design module ([§12](#12-adoption), step 7) | 6, 8, 9 |
 | P3 (independent), P1 (independent), P6 (independent); I4 | By P3 a value binds one exact basis, and by I4 data crosses seams the surface does not control, so UX-consumed types come from the contract shared by front end and back end, and by P6 data crossing an untrusted or out-of-process seam is validated at runtime before it enters state | [§10](#10-type-sharing) | the six seams, at which this profile makes the preference of [DESIGN_MODULE §4](DESIGN_MODULE.md#4-functional-bias-and-typing) for parsing foreign data once at ingress an obligation, and one typed schema yielding both compile-time types and runtime validators: this profile; the schema mechanism: the project | 2, 3, 4 |
 | P2 (independent), P6 (independent); I1 | By P2 obligations follow the outcome, and by I1 a public surface is how people reach the product's capability, so a surface that is the public face of a product capability declares the accessibility minimum; by P6 an exemption needs an authority, so an internal debug surface is exempt only with its exemption recorded | [§11](#11-accessibility-minimum) | the five declarations, with WCAG AA as the recommended default for web: this profile; a stricter accessibility refinement: the project | 1, 9 |
-| P2 (independent), P1 (independent); I3 | By P2 the method fixes only what the outcome needs, and by P1 a stack's name carries no meaning, so the stack is free while the process model is preserved, and realisations are tested against the model, never ranked | [§4 Process model without stack mandate](#process-model-without-stack-mandate); [§4 Realisation discretion](#realisation-discretion) | the process model without stack mandate, mirroring [DESIGN_MODULE §4 Functional bias without language mandate](DESIGN_MODULE.md#functional-bias-without-language-mandate): this profile; which of the two compliance tests governs, the test over §4 to §10 with no §13 failure pattern or the test over §4 to §8: pending the product owner's ruling; §15 applies the stricter while the ruling is pending, under the fail-closed rule of [§1 Authority](#authority); the language, framework, state container, effect interpreter, runtime validator and toolchain: the project, in its design module | 4, 8 |
+| P2 (independent), P1 (independent); I3 | By P2 the method fixes only what the outcome needs, and by P1 a stack's name carries no meaning, so the stack is free while the process model is preserved, and realisations are tested against the model, never ranked | [§4 Process model without stack mandate](#process-model-without-stack-mandate); [§4 Realisation discretion](#realisation-discretion) | the process model without stack mandate, mirroring [DESIGN_MODULE §4 Functional bias without language mandate](DESIGN_MODULE.md#functional-bias-without-language-mandate): this profile; the two compliance tests, the test over §4 to §10 with no §13 failure pattern and the test over §4 to §8, differ in scope; §15 applies the stricter under the fail-closed rule of [§1 Authority](#authority), with the ambiguity retained for the governing authority; the language, framework, state container, effect interpreter, runtime validator and toolchain: the project, in its design module | 4, 8 |
 | P6 (independent); F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); I3 | By P6 authority exists only through an admitted grant, so an adopting surface has one UX realisation authority, and existing code, conventions and artifacts are evidence only; by F11 an ambiguity is resolved, carried, escalated or blocked, so an ambiguity fails closed through those outcomes instead of weakening the process model | [§1 Authority](#authority); [§2](#2-role-and-composition) | who adopts: Product authority, under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the adopted surfaces and scope, recorded in the adopting project's design modules ([§12](#12-adoption)); the stack: the project's ADRs, which may not weaken the process model; the map of the three exits to the ambiguity outcomes: this profile, under [ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome) | 1, 7, 9 |
 | P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F4 imported ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)), F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)), F13 imported ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution)); I5 | By P6 an exemption needs an authority and by P4b a deferred obligation persists until paid, so a scaffold is exempt only with a recorded scope and retirement condition and never becomes production by accumulation; I5 makes per-change proof costly, so a UX sprint defers proof only as visible escrow that closure still pays, and closes only with every finding classified | [§12 Scaffold and exemption](#scaffold-and-exemption); [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow) | the five default-governance conditions, the escrowable and non-escrowable items and the close triggers: this profile; the generic escrow law and the six close classifications: [TICKETS §3](TICKETS.md#3-sprint-rules); the sprint boundary: [SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) | 1, 9 |
 | P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a value decides only what its evidence establishes, and F3 gives one core, so each verdict of this profile is a refined value mapped to exactly one core value for a named predicate, and a review, a replay proof, a closure claim and a carrier check combine with other results without one being read as another or coerced to success | [§15](#15-results-of-this-profile) | the four refinements and their values: this profile | 3, 9 |
@@ -142,8 +134,7 @@
 failure patterns (§13) or the review questions (§14); these sections
 apply the consequences above, and every clause names the principle that
 requires it ([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)).
-§16 records source dispositions and decides nothing. The table is
-new in this corpus. Purpose and material relation: an actor started on
+Purpose and material relation: an actor started on
 this member sees which rules follow from the foundations and the imported
 families, and which are choices of this profile, the product or the
 project, with their owners, so no choice is presented as derived (P6,
@@ -159,7 +150,7 @@
 - Row 4, continuation and the replay proof: [§12](#12-adoption), step 7; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which may defer and cannot erase the §8 Msg-replay proof that closure requires; [§13](#13-failure-patterns), patterns 4 and 12; [§14](#14-review-questions), questions 7 and 12; [§15](#15-results-of-this-profile), replay proof and closure obligations.
 - Row 5, type sharing: [§4 Realisation discretion](#realisation-discretion), whose compliance test requires §10 to hold; [§13](#13-failure-patterns), patterns 6 and 14; [§14](#14-review-questions), questions 8 and 9; [§15](#15-results-of-this-profile), surface review.
 - Row 6, the accessibility minimum: [§12](#12-adoption), step 8; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which may defer and cannot erase the §11 obligations that closure requires; [§13](#13-failure-patterns), pattern 9; [§14](#14-review-questions), question 10; [§15](#15-results-of-this-profile), closure obligations.
-- Row 7, the process model without stack mandate and realisation discretion: [§12](#12-adoption), step 2; [§14](#14-review-questions), question 11; [§15](#15-results-of-this-profile), surface review, which applies the stricter of the two compliance tests while the product owner's ruling is pending.
+- Row 7, the process model without stack mandate and realisation discretion: [§12](#12-adoption), step 2; [§14](#14-review-questions), question 11; [§15](#15-results-of-this-profile), surface review, which applies the stricter of the two compliance tests under §1 Authority's fail-closed rule, with the ambiguity retained for the governing authority.
 - Row 8, authority and composition: [§12](#12-adoption), where Product authority adopts the profile under §1 Authority and records the adoption per project; [§13](#13-failure-patterns), pattern 16; [§15](#15-results-of-this-profile), Fail closed, which returns the surface review's value under the stricter interpretation and leaves the other two exits of §1 Authority as a re-entry or a recorded scope.
 - Row 9, scaffold exemption and sprint compliance escrow: [§2 Relationship to other members](#relationship-to-other-members), where UX work may use sprint compliance escrow under §12; [§13](#13-failure-patterns), patterns 15 and 17; [§14](#14-review-questions), questions 10 and 14; [§15](#15-results-of-this-profile), closure obligations, and its closing paragraph, where an exempt scaffold is a recorded scope and the six close classifications stay TICKETS §3's.
 - Row 10, the results of this profile: [§1 Authority](#authority), [§3](#3-product-truth-and-admitted-carriers), [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), each of which states its test or exit and leaves the result to §15; no section of another member returns these values, and the core they map to is [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), which owns it and applies no rule of this section.
@@ -172,7 +163,7 @@
 SPEC_METHOD defines constitutional process and lawful re-entry; the
 graph-execution profile defines graph-native constructive carrier law;
 DESIGN_MODULE defines deterministic module-level realisation discipline
-(P6; rc.2 #2-method-role). This profile refines DESIGN_MODULE with the
+(P6). This profile refines DESIGN_MODULE with the
 additional rules a module needs when it realises a UX surface (render
 purity, state-transition algebra, effect-membrane discipline and
 accessibility minimums) under the Elm process model. It does not
@@ -182,8 +173,7 @@
 concerns the parent does not address (render lifecycle, browser events,
 layout, accessibility), this profile is authoritative (P6, P4a).
 
-This profile composes with the upstream members per surface (P4a, P0;
-rc.2 #3-method-composition):
+This profile composes with the upstream members per surface (P4a, P0):
 
 - when a module realises a UX surface, DESIGN_MODULE and this profile both
   apply, and its design module reads both;
@@ -209,8 +199,7 @@
 visible, bounded and payable. The world-model profile
 ([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
 products that have a world-model dimension; UX surfaces over world-model
-state still bind through AssetSurface, or its equivalent, under §7 (P6;
-rc.2 #16-relationship-to-other-method-surfaces).
+state still bind through AssetSurface, or its equivalent, under §7 (P6).
 
 ### Non-goals
 
@@ -218,14 +207,12 @@
 component library, a brand or visual-identity surface, a wireframing or
 prototyping process, a research method for user studies, or a stack
 ranking or framework recommendation. Those are valid concerns; they
-belong in product-local surfaces, not in this constitutional profile (P2;
-rc.2 #17-non-goals).
+belong in product-local surfaces, not in this constitutional profile (P2).
 
 ## 3. Product truth and admitted carriers
 
 UX surfaces are projection and control surfaces: they render admitted
-truth and emit typed messages (P6, P0;
-rc.2 #3a-ux-projection-and-constructive-carrier-boundary). A UX-local Msg
+truth and emit typed messages (P6, P0). A UX-local Msg
 may govern view-local concerns such as expansion state, sort order,
 filter text, focus movement or draft input. A Msg that changes product
 truth is not merely a UX concern. Product-truth changes include:
@@ -253,8 +240,7 @@
 
 ## 4. Process model
 
-The constitutional process model is the Elm Architecture (P0, P1;
-rc.2 #4-process-model-elm-architecture):
+The constitutional process model is the Elm Architecture (P0, P1):
 
 - State: the typed state shape, held by the runtime, not by the view;
 - Msg: the typed message algebra naming every action a user or system can
@@ -280,11 +266,11 @@
 the project's choice, recorded in its design module. This mirrors
 DESIGN_MODULE §4 Functional bias without language mandate: the process
 model is constitutional and not negotiable; the stack is project-local
-and free, provided it preserves the model (P1, P6;
-rc.2 #4a-process-model-without-language-or-framework-mandate). Any
+and free, provided it preserves the model (P1, P6). Any
 realisation that preserves §4 to §8 is compliant with this profile. This
 test differs from the test of §4 Realisation discretion; §15 states which
-test applies while the product owner's ruling between them is pending.
+test applies under §1 Authority's fail-closed rule, with the ambiguity
+retained for the governing authority.
 Examples (non-normative):
 
 - a language-integrated reducer runtime, which enables typed state,
@@ -312,7 +298,7 @@
 ### Realisation discretion
 
 The profile is opinionated about the process model and not about the
-realisation stack (P1, P2; rc.2 #12-realization-discretion). The project
+realisation stack (P1, P2). The project
 chooses:
 
 - the language;
@@ -328,13 +314,13 @@
 realisations. A realisation is compliant with this profile when §4 to §10
 hold under inspection and the §13 failure patterns are absent (P6, P1).
 This test differs from the test of §4 Process model without stack
-mandate; §15 states which test applies while the product owner's ruling
-between them is pending.
+mandate; §15 states which test applies under §1 Authority's fail-closed
+rule, with the ambiguity retained for the governing authority.
 
 ## 5. State transitions
 
 State changes through typed messages applied by the pure reducer, the
-Update of §4 (P4a, P1; rc.2 #5-state-transition-law). A UX surface
+Update of §4 (P4a, P1). A UX surface
 declares:
 
 - its State shape;
@@ -349,9 +335,23 @@
 - the effect kind;
 - the typed input payload;
 - the admitted carrier or external boundary it targets;
-- the success Msg emitted back to the reducer;
-- the failure Msg emitted back to the reducer;
-- any deterministic correlation key required for replay.
+- a typed outcome Msg family covering every materially possible observed
+  or unresolved outcome of the effect, including success and failure;
+- the evidence by which an outcome Msg is selected and the observations
+  required to resolve an uncertain outcome;
+- any deterministic correlation key required to connect the Cmd, its
+  invocation, outcome messages and replay.
+
+An outcome Msg represents the available effect evidence. For an intended
+effect, its meaning uses the three effect values of
+[ACTIVATION §3 Effects](ACTIVATION.md#effects): `completed`,
+`not_effected` and `completion_unknown`. These are effect results for
+the predicate "the intended effect occurred", not a replacement for the
+product's typed message vocabulary. A lost or failed transport reply alone
+establishes neither completion nor non-completion. Sufficient independent
+observations may decide the outcome; otherwise the message and State
+retain `completion_unknown`, its correlation and the missing observation
+(P5, P4b).
 
 The reducer is pure: it does not perform I/O, log to side channels or
 mutate global state. Effects scheduled by Cmd are interpreted by the
@@ -370,8 +370,7 @@
 ## 6. Effect membrane
 
 Side effects are isolated to a declared effect membrane, which refines
-DESIGN_MODULE §10 Effect edge for UX surfaces (P0, P5;
-rc.2 #6-effect-membrane-rule). The membrane interprets Cmd values
+DESIGN_MODULE §10 Effect edge for UX surfaces (P0, P5). The membrane interprets Cmd values
 produced by the reducer and translates side-effect outcomes back into Msg
 values delivered to the reducer. Inside the membrane, I/O, subscriptions
 to external sources, and imperative interop with the host platform (DOM,
@@ -382,7 +381,14 @@
 The membrane has one job: interpret declared Cmd values. It is not where
 logic lives. Branching, conditional state derivation and multi-step
 business decisions belong in the reducer; the membrane interprets a
-single declared Cmd per effect (P6). A platform-specific effect handler,
+single declared Cmd per effect (P6). An unresolved outcome returns through
+the typed outcome Msg family; it is not converted into ordinary failure
+or success merely to keep the UI moving. Before a repeat or dependent
+effect whose safety depends on the outcome, the product observes the
+owning state and follows [ACTIVATION §5 Recovery](ACTIVATION.md#5-work-state-and-restart),
+with the current authority and effect territory retained. Recovery is an
+explicit Cmd/Msg interaction, not hidden membrane continuation (P5, P6).
+A platform-specific effect handler,
 whatever name the chosen framework gives it (`useEffect`,
 `createEffect`, `onMount`, `subscribe`, a server-action handler), is part
 of the membrane only when it interprets a declared Cmd. A handler that
@@ -394,7 +400,7 @@
 When the product publishes typed asset surfaces under the graph-execution
 profile's carrier law and the local product's design, a UX surface binds
 to one or more AssetSurface contracts as its data source and action
-target (P6, P3; rc.2 #7-assetsurface-binding-rule). Binding requirements:
+target (P6, P3). Binding requirements:
 
 - the surface's State is derived from AssetSurface projections, not from
   a UX-local re-declaration of the asset shape;
@@ -425,17 +431,14 @@
 changes product truth through UI behaviour, the prompt must name the
 admitted carrier and action path. If the prompt cannot identify that
 carrier and action path, the correct result is a block or re-entry, not
-local UI invention (P6, P5; provenance rc.2
-authority_compressions/ux_method.compressed.md, a claim no rc.2 body
-states; prompt construction is
+local UI invention (P6, P5; prompt construction is
 [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)).
 
 ## 8. Continuation and replay
 
 In the graph-execution profile the runtime owns continuation (PROFILES
 §2) and the product is a cooperative bounded-step subsystem. The UX
-twin: the view does not own state continuation (P0, P6;
-rc.2 #8-ux-twin-of-odd-115a-view-does-not-own-continuation). State
+twin: the view does not own state continuation (P0, P6). State
 transitions flow through declared Msg actions interpreted by the reducer.
 A view does not:
 
@@ -456,7 +459,7 @@
 
 Every product UX surface carries at least one executable Msg-replay proof
 for each product-meaningful interaction family before claiming closure
-under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement).
+under this profile (P4b, P6).
 Purpose and material relation: the Msg log is the surface's recorded work
 state, and replay is resumption from it
 ([ACTIVATION §5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account)).
@@ -469,7 +472,8 @@
 - an ordered Msg log;
 - the expected final State;
 - the expected ordered Cmd values;
-- the success and failure Msg values returned by interpreted Cmds;
+- the typed outcome Msg values returned by interpreted Cmds, including
+  every materially possible unresolved outcome and its recovery messages;
 - injected deterministic values for time, randomness, generated ids and
   external payloads.
 
@@ -482,13 +486,20 @@
 - view-local state that changes product behaviour after unmount or
   replay.
 
+For an interaction whose external effect can be unresolved, the proof
+covers the correlated unresolved message, its retained State and the
+recovery path, including the prohibition on an outcome-dependent repeat
+before the required observation. Reproducing that State establishes the
+replay predicate only. It does not establish that the external effect
+completed; `replay_passes` can coexist with `completion_unknown` for the
+effect predicate (P5, P4b).
+
 For a pure projection-only surface, the replay proof may be a no-effect
 proof: a Msg log plus the final State and an empty Cmd sequence (P2).
 
 ## 9. View shape
 
-A view is a pure function from typed state to a view tree (P1;
-rc.2 #9-view-shape-rule). The view:
+A view is a pure function from typed state to a view tree (P1). The view:
 
 - accepts typed input (state, props, context);
 - returns a typed view tree;
@@ -510,7 +521,7 @@
 ## 10. Type sharing
 
 UX-consumed types come from the shared front-end and back-end contract
-(P3, P1; rc.2 #10-type-sharing-rule). A UX surface does not re-declare
+(P3, P1). A UX surface does not re-declare
 back-end record shapes; it imports them from the shared contract module,
 typically the same package or a dedicated `contracts/` package.
 
@@ -535,7 +546,7 @@
 ## 11. Accessibility minimum
 
 A UX surface that is the public face of a product capability declares
-(P2, P6; rc.2 #11-accessibility-minimum):
+(P2, P6):
 
 - semantic structure (heading levels, landmarks, lists, or
   platform-equivalent affordances);
@@ -557,7 +568,7 @@
 ## 12. Adoption
 
 Product authority adopts this profile for a project (§1 Authority), and
-the adoption is recorded by (P6, P4b; rc.2 #13-adoption-guidance):
+the adoption is recorded by (P6, P4b):
 
 1. naming the profile in the project's UX-related design modules;
 2. recording the realisation stack choice (§4 Realisation discretion) and
@@ -581,7 +592,7 @@
 ### Scaffold and exemption
 
 A UX surface is governed by this profile by default when any of these are
-true (P6, P5; rc.2 #13a-scaffold-and-exemption-law):
+true (P6, P5):
 
 - it is reachable from the product shell;
 - it is used as proof for a ticket, requirement, design module, release or
@@ -612,8 +623,7 @@
 subsection is the profile's statement, which SPEC_METHOD §4 Sprint
 execution boundary admits, of when that escrow is an appropriate cost
 optimisation for UX; the generic escrow law and the close mechanics are
-TICKETS §3 Compliance escrow and Close review (P2, P6;
-rc.2 #13b-ux-sprint-compliance-escrow). A UX sprint may defer local UX
+TICKETS §3 Compliance escrow and Close review (P2, P6). A UX sprint may defer local UX
 compliance proof during a short iteration window when per-change proof
 cost is higher than expected correction cost. This is a cost-optimisation
 rule; it does not weaken the UX process model (P2).
@@ -674,8 +684,7 @@
 
 ## 13. Failure patterns
 
-A UX surface violates this profile when any of these are true (P6, P5;
-rc.2 #14-failure-pattern):
+A UX surface violates this profile when any of these are true (P6, P5):
 
 1. render code mutates state directly (assignments inside the render
    body, mutating a prop or context value);
@@ -717,8 +726,7 @@
 
 ## 14. Review questions
 
-A UX surface review under this profile should answer (P6, P2;
-rc.2 #15-review-questions):
+A UX surface review under this profile should answer (P6, P2):
 
 1. What is the surface's State, Msg and Update?
 2. What is the surface's Cmd and Sub algebra?
@@ -755,8 +763,7 @@
 the value, so a `satisfied` for one predicate never counts toward another
 ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
 and no mapping raises a result's standing: nothing is coerced to
-`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
-material relation: this profile's verdicts decide closure of a UX surface
+`satisfied` (P5, P6). Purpose and material relation: this profile's verdicts decide closure of a UX surface
 and enter conjunctions with the results of other members, which combine
 only in the core, so a review, a proof, a closure claim and a carrier
 check are each read for their own predicate and none is read as another
@@ -771,10 +778,10 @@
 
 | Refinement | Value | Core value | Ground |
 |---|---|---|---|
-| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
+| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The tests differ in scope; this mapping applies the stricter under the fail-closed rule of §1 Authority and retains the ambiguity for the governing authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
 | surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
 | surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
-| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
+| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness; reproducing an unresolved outcome proves replay only and does not establish external completion |
 | replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
 | closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
 | closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
@@ -817,55 +824,3 @@
 not a result; evaluations outside its recorded scope proceed under this
 section. The six close classifications of §12 belong to TICKETS §3 and are
 not mapped here (P6).
-
-## 16. Source dispositions
-
-Rows of rc.2 UX_METHOD.md received by this member. Anchors are into rc.2
-UX_METHOD.md; a locus is a section of this file unless another member is
-named. Every conserved row is restated in this member's own text; a route
-is provenance only. Generalisations recorded here: "UX_METHOD.md" and
-"this method" are written "this profile"; "DESIGN_MODULE_METHOD.md",
-"SPEC_METHOD.md" and "TICKET_METHOD.md" as DESIGN_MODULE, SPEC_METHOD and
-TICKETS; "ODD_METHOD.md" as the graph-execution profile, ODD (PROFILES
-§2), whose own terms graph function and ABG this tier-3 profile keeps;
-AssetSurface and workorder are kept as the names of carriers that a
-product's design publishes or admits; "WORLD_MODEL_METHOD.md" as
-WORLD_MODEL;
-"method-compliant", "method violation" and "method closure" as compliant
-with, a violation of, and closure under this profile. The predecessor's
-section numbers are written as this member's: §4 to §10 keep their
-numbers; §12 is §4 Realisation discretion; §13, §13A and §13B are §12 and
-its subsections; §14 is §13; §15 is §14; §8A is §8 Msg-replay proof.
-
-Three clauses have no predecessor row and are new: the declared binding of
-TICKETS §3's escrow terms (lead); the refinements of the core result
-algebra (§15), which FOUNDATIONS §4 Results requires of a profile with its
-own result vocabulary; and the family table (§1 Foundation to law), in
-the format of FOUNDATIONS §3 Foundation to law (P1, P5, P6).
-
-| Anchor | Disposition | Locus |
-|---|---|---|
-| #1-position | conserved; the one instruction, the four TEA statements, the view not a state owner, the three violations even where conventionally accepted; the family table under Foundation to law is new | §1 |
-| #1a-constitutional-authority-rule | conserved; sole UX realisation authority, ADRs choose the stack and may not weaken the model, the seven evidence-only kinds, fail closed with its three exits; ambiguity governance is SPEC_METHOD §5, pointed to | §1 Authority; §15 |
-| #2-method-role | conserved; the three roles, the refinement with its four additions, no duplication with the five parent rules, the four UX-only concerns | §2 |
-| #3-method-composition | conserved; the three per-surface cases, the three-answer composition rule | §2 |
-| #3a-ux-projection-and-constructive-carrier-boundary | conserved; projection and control surfaces, the five view-local concerns, the six product-truth changes, the five admitted carriers, no hidden constructive carrier, blocked until authored or repriced | §3; §15 |
-| #4-process-model-elm-architecture | conserved; the five elements with both signatures, the runtime-owned loop | §4 |
-| #4a-process-model-without-language-or-framework-mandate | conserved; model constitutional and stack free, the DESIGN_MODULE §4 mirror, compliance for preserving §4 to §8, the four non-normative examples, the four rejected realisations and three stack-independent violations, framework choice recorded with justification, no ranking; its compliance test, preservation of §4 to §8, disagrees with the test of #12-realization-discretion, and §15 applies the stricter test of #12, the choice being pending the product owner's ruling | §4 Process model without stack mandate; §15 |
-| #5-state-transition-law | conserved; the five declarations, the six Cmd fields, the pure reducer, view-local ephemera with its three conditions at "may" force, product-meaningful state without exception, the unmount discipline test | §5 |
-| #6-effect-membrane-rule | conserved; the membrane's two translations, the three allowed inside, the three forbidden outside, one job, logic in the reducer, the named handlers, the violation and its repair; stated as the UX refinement of DESIGN_MODULE §10 Effect edge | §6 |
-| #7-assetsurface-binding-rule | conserved; the five binding requirements, the same contract on both sides, the equivalent typed contract, absence blocks | §7 |
-| #8-ux-twin-of-odd-115a-view-does-not-own-continuation | conserved; the parent rule named through PROFILES §2, the three prohibitions, the state machine in the reducer, the Msg-replay test | §8 |
-| #8a-msg-replay-proof-requirement | conserved; at least one proof per product-meaningful interaction family before closure, the six contents, the four failure dependencies, the no-effect proof at "may" force | §8 Msg-replay proof; §15 |
-| #9-view-shape-rule | conserved; the five view properties, shape as a stack decision, the signature and no side effects, the out-of-render mutation violation and its membrane exception | §9 |
-| #10-type-sharing-rule | conserved; shared contract, no re-declaration, "typically", mandatory runtime validation at the six seams, the typed-schema mechanism, compile-time TypeScript not sufficient, UX-local types allowed and not shadowing | §10 |
-| #11-accessibility-minimum | conserved; the five declarations with WCAG AA as the recommended default, not optional for product capabilities, optional for debug surfaces with the exemption recorded, intentionally minimal, project-local refinement | §11 |
-| #12-realization-discretion | conserved; opinionated about the model only, the six choices, recorded with justification against §4 and §6, no ranking, the compliance test over §4 to §10 and the failure patterns; §15 applies this test as `compliant`, the stricter of the two, pending the product owner's ruling on the disagreement with #4a | §4 Realisation discretion; §15 |
-| #13-adoption-guidance | conserved; the nine adoption steps, per-project adoption at "may" with the scope recorded; step 3's structural carrier diagram is pointed to DESIGN_MODULE §6 and §7 | §12 |
-| #13a-scaffold-and-exemption-law | conserved; the five default-governance conditions, the seven exemption record items at "may be exempt only when", no production UX by accumulation and its three exits | §12 Scaffold and exemption |
-| #13b-ux-sprint-compliance-escrow | conserved; the primary use case, the cost condition at "may", not weakening the model, the seven escrowable and five non-escrowable items, the exit and the hidden-carrier rule, the "should close" condition and five triggers, the forensic walkthrough, the six classifications pointed to TICKETS §3 with the UX reading of `accepted`, the paydown and no-close conditions, defer but not erase; the generic escrow law is TICKETS §3 and SPEC_METHOD §4, pointed to | §12 UX sprint compliance escrow; TICKETS §3 |
-| #14-failure-pattern | conserved; the seventeen patterns, any one a violation, repair or reprice | §13; §15 |
-| #15-review-questions | conserved; the fourteen questions at "should answer", an unanswerable question makes the design module incomplete | §14; §15 |
-| #16-relationship-to-other-method-surfaces | conserved; the five relationships, the escrow condition, the world-model binding through §7, the read and ignore rule | §2 Relationship to other members; §2 |
-| #17-non-goals | conserved; the six non-goals and their product-local home | §2 Non-goals |
-| #18-canonical-compression | conserved; every determination of the compression is stated once where it governs: Elm model and DESIGN_MODULE refinement §1, §2; the model §4; view continuation and the replay test §8; stack recorded with justification and tested against §4 to §10 and the failure patterns §4, §13; sole authority §1; carriers and no hidden carrier §3; runtime validation §10; scaffolds §12; escrow and close review §12 | §1 to §13 |
--- specification_methodology/v3/build_tenants/claude/standards/DESIGN_MODULE.md
+++ specification_methodology/v3/build_tenants/common/standards/DESIGN_MODULE.md
@@ -67,26 +67,19 @@
 the core, which decides exclusions. A `not_applicable` axiom verdict (§7
 Cross-view axiom evaluation) is a value of a predicate declared as a
 disjunction that includes non-application, mapped there under the same
-paragraph. This statement is new in this corpus. Purpose and material
-relation: a consumer that combines this profile's outcomes with other
+paragraph. Purpose and material relation: a consumer that combines this profile's outcomes with other
 results reads each result in the one core and never reads a record entry
 as a result (P5, P6).
 
 Every clause names the principle that requires it (P0 to P6, FOUNDATIONS
-§3). The predecessor's "must" is written in the
-indicative; its "should", "may", "recommended", "typical", "preferred",
-"normally", "usually", "minimum", "where practical" and "allowed" keep
-their force. A route written `rc.2 #anchor` is into
-`stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md` and is
-provenance only; every predecessor row received here is restated in this
-text, and nothing here depends on that cut to be applied.
+§3).
 
 ## 1. Purpose and position
 
 ### Purpose
 
 This profile exists for projects that want a stronger implementation
-discipline than "write code that passes" (P2; rc.2 #1-purpose). Its bias is
+discipline than "write code that passes" (P2). Its bias is
 toward low coupling, modular composition, immutable typed carriers, total
 or nearly total semantic transforms and explicit effect boundaries. The
 goal is not language ideology. The goals are to reduce ambiguity, reduce
@@ -131,8 +124,7 @@
 
 ### Position
 
-The preferred realisation shape is functionally biased (P1, P6;
-rc.2 #2-position). That means semantic meaning should live in typed carriers and
+The preferred realisation shape is functionally biased (P1, P6). That means semantic meaning should live in typed carriers and
 explicit transforms; imperative coordination should be subordinate to
 admitted truth; side effects should be isolated to explicit boundary
 modules; and mutable shared state should be minimised and justified. The
@@ -148,7 +140,7 @@
 system means, is stated once in
 [SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape),
 scoped to boundaries this profile governs; every rule below refines it
-(P1, P6; rc.2 #3-core-rule).
+(P1, P6).
 
 ### Foundation to law
 
@@ -219,7 +211,7 @@
 | P2 (independent), P3 (independent); F13 imported; I4 | similar computation recurs (I4), and each further local rebuild adds cost with no new route to the outcome (P2), while similar code does not establish one identity (P3), so a credible recurrence yields a commonisation review, never an automatic merge, as the generic ticket rule decides (F13) | [Recurrence extraction](#recurrence-extraction) | the rule of two, the third-rebuild threshold and the commonisation order: [TICKETS §6](TICKETS.md#recurring-realisation-and-library-declaration), the generic owner; their refinement as design-method conformance: this profile; whether one implementation serves several instances: [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) Shared machinery | 4 |
 | P6 (independent), P2 (independent); F3, F4, F6 imported | a closure claim needs evidence for the exact claim, and implementation status is not that evidence (P6, F6), so a bounded check reconstructs the function of the exact claim before the claim is made, reusing accepted evidence only under the reuse law (F4); a falsified claim is never `satisfied` (F3), so an issue that falsifies the claim or an applicable hard stop blocks the design-method closure claim; a discovery outside the claim has no route to that claim (P2), so it is repricing input, not scope | [Post-ticket design review](#post-ticket-design-review) | the check's five determinations as domain triggers and the absorption conditions for boundary-local clean-up: this profile; when a finding blocks current promotion: [EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion); reuse and its invalidators: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); ticket status and closure mechanics: [TICKETS](TICKETS.md) | 9, 1 |
 | P6 (independent), P1 (independent), P3 (independent) | a meaning has one owner, declared and one (P3), with no rival authority (P6), and is read through a declared contract (P1), so each interface family has one authoritative source truth that downstream interfaces consume, and a proxy that keeps an old authority path behind a new surface leaves two owners for one meaning, which is bridge debt | [Interface bleed prohibition](#interface-bleed-prohibition); [Proxy interface prohibition](#proxy-interface-prohibition) | retained compatibility with its own authority and proof: the project's design; the bridge prohibition: [SPEC_METHOD §7](SPEC_METHOD.md#bridge-prohibition) | 9, 6 |
-| P6 (independent), P1 (independent), P2 (independent) | a design claim needs evidence (P6), so review checks the rules above for the boundary; a question that the carriers and transforms cannot answer shows meaning held outside a declared contract (P1), a realisation too coupled or too imperative; a prompt clause that enforces design law is justified only by its route to the behaviour it governs (P2), so it needs provenance and proof that it still causes or prevents that behaviour | [§11](#11-review) | the 56 questions, the 43 checks and the 14 hard-gate checks: this profile; prompt construction: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) | 9, 4 |
+| P6 (independent), P1 (independent), P2 (independent) | a design claim needs evidence (P6), so review checks the rules above for the boundary; an unanswered required relation withholds its conformance claim, and diagnosis follows evidence to the relation's actual owner under [ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation); missing authority or observation alone does not establish excessive coupling or imperative design; a prompt clause that enforces design law is justified only by its route to the behaviour it governs (P2), so it needs provenance and proof that it still causes or prevents that behaviour | [§11](#11-review) | the 56 questions, the 43 checks and the 14 hard-gate checks: this profile; prompt construction: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) | 9, 4 |
 | P6 (independent), P2 (independent); F12 imported; I1 | an optional profile governs a boundary only where the authority that may adopt it has adopted it (P6, F12), so the project applies it consistently across the named boundary; a completion claim needs its evidence (P6), and obligations follow the boundary's outcome (P2), so a design-method completion claim for a new or materially changed boundary needs its declared or cited Ontology and evidence, and partial adoption names the adopted boundary and rule family and claims no completion whose evidence it skipped | [§12 Adoption](#adoption); [the head of this member](#design_module), which declares the profile optional | who adopts: Product authority, under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the adopted boundary and rule family: that authority; the means of recording adoption, at "may" force: this profile | 1, 9 |
 | P3 (independent), P6 (independent); F8 imported | identity is declared by its authority (P3, F8) and a default confers no authority (P6), so identity generators, validators and normalisers that a runtime realisation publishes are defaults, which the owner of the identity can override | [Identity defaults from a bound runtime realisation](#identity-defaults-from-a-bound-runtime-realisation) | the permission for a consumer-bound realisation of the ABG role to publish defaults for its own runtime surfaces and the default surface kinds, limited to that role: this profile; the defaults' standing and the override law: [IDENTITY §7](IDENTITY.md#7-default-formats-and-overrides) | 2 |
 
@@ -241,7 +233,7 @@
 - Row 1, purpose, position and core rule: [SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape), which states the core rule and the non-goals for a boundary this profile governs; [UX §2](UX.md#2-role-and-composition) and [UX Relationship to other members](UX.md#relationship-to-other-members), which compose this profile with the UX and graph-execution profiles per surface; [WORLD_MODEL §4 Relation to the design profile](WORLD_MODEL.md#relation-to-the-design-profile), for §8; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) A15, which keeps this profile's realisation modules inside the ODD ownership split, as §2 requires.
 - Row 2, results and design records: [Invariant reconstruction sufficiency (UP-018)](#invariant-reconstruction-sufficiency-up-018) and [Cross-view axiom evaluation](#cross-view-axiom-evaluation), which map the two refinements where they are defined; [Gate and retrospective work](#gate-and-retrospective-work), which places the Ontology and design verdicts under ACTIVATION §3 Disposition.
 - Row 3, boundary closure evaluators: [Adoption](#adoption), which makes the evaluators explicit in the governing ADR or ticket for carrier, schema and governance migrations; [Design review questions](#design-review-questions) 4, 5, 7, 9 and 17 to 19; the [Functional realisation checklist](#functional-realisation-checklist), ingress and truth-surface checks.
-- Row 4, functional bias and typing: [UX §10](UX.md#10-type-sharing), which makes the §4 preference for parsing foreign data once at ingress an obligation at six seams; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 11; [Design review questions](#design-review-questions) 12 and 18.
+- Row 4, functional bias and typing: [UX §10](UX.md#10-type-sharing), which makes the §4 preference for parsing foreign data once at ingress an obligation at six seams; [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 11; [Design review questions](#design-review-questions) 12 and 18.
 - Row 5, ontology-first design and its projections: [PRODUCT_DEFINITION §3](PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency), which keeps an accepted design Ontology below the constitutional WHAT; [ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route) and [§15](ASSURANCE.md#15-module-derived-unit-tests), whose evidence chains start from the accepted Ontology and, where a reference realisation exists, from the reference-to-ontology mapping, through the binding at the head; [Adoption](#adoption), which requires the accepted Ontology, the Ontology evidence and the reference-to-target derivation asset before a completion claim; [Design review questions](#design-review-questions) 21 and 41 to 48.
 - Row 6, proportional sequencing and decision completeness: [SPEC_METHOD §4 Procedures](SPEC_METHOD.md#procedures), where design, implementation and tests co-evolve only when the co-evolution predicate holds; [ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route), which gates the evidence relation on decision completeness through the binding at the head; [Gate and retrospective work](#gate-and-retrospective-work), whose precondition it is; [Design review questions](#design-review-questions) 40.
 - Row 7, bounded frame conservation and invariant reconstruction: [ACTIVATION §1 Intake](ACTIVATION.md#intake), which consumes the affected set and the invariants these laws supply; [EXECUTIVE_BASELINE §8](EXECUTIVE_BASELINE.md#8-derived-executive-frame) and [§14](EXECUTIVE_BASELINE.md#14-coverage-application), which carry the bounded-frame conservation laws as governing invariants of the Executive frame and of the affected causal cone; [Post-ticket design review](#post-ticket-design-review), which treats a changed governing relation under §7 as a material input change for the affected claim.
@@ -269,9 +261,8 @@
 not (P2, P6).
 
 The table accounts for this whole member: the head, §1 to §12 and the
-binding the head declares; §13 records dispositions and decides nothing.
-Its Pillar column follows FOUNDATIONS §3. It is new in this corpus and has
-no rc.2 row. Purpose and material relation: a reader of this profile sees
+binding the head declares. Its Pillar column follows FOUNDATIONS §3.
+Purpose and material relation: a reader of this profile sees
 which of its rules rest on the commitments and imported families and which
 are choices this profile, the adopting Product or another owner makes, so
 no profile choice is presented as following from the foundations (P6, P2).
@@ -280,8 +271,7 @@
 
 When this profile is used inside a product governed by the graph-execution
 profile (PROFILES §2), reviewers first ask whether the boundary is an
-operative graph traversal (P6, P0;
-rc.2 #3a-odd-alignment-and-escalation-rule). If the boundary represents product
+operative graph traversal (P6, P0). If the boundary represents product
 movement from one typed asset state to another, the governing shape is:
 
 1. outcome traversal under the graph-execution profile;
@@ -309,8 +299,7 @@
 ## 3. Boundary closure evaluators
 
 When this profile governs a boundary, each design or implementation change
-should be judged against three overriding evaluators (P6, P2;
-rc.2 #3b-boundary-closure-evaluators). They are not optional heuristics. A
+should be judged against three overriding evaluators (P6, P2). They are not optional heuristics. A
 change that improves local ergonomics, test output or static-checker
 output but fails one of them is not real progress under this profile.
 
@@ -318,7 +307,7 @@
 
 Each change does not increase the number of truth surfaces; where
 duplicate or rival truth surfaces already exist, seam-closure work should
-reduce them (P6, P3; rc.2 #1-authority-seam-closure). This means one
+reduce them (P6, P3). This means one
 authoritative carrier or contract at each semantic boundary; no
 controller-side reconstruction of already-admitted truth; no downstream
 surface silently rebuilding source truth from raw artifacts; and no raw or
@@ -339,7 +328,7 @@
 ### Essential carrier consolidation
 
 Each change should collapse the slice to the few real identity-bearing
-carrier families (P3, P2; rc.2 #2-essential-carrier-consolidation). This
+carrier families (P3, P2). This
 means declaring the IACS first (§6), keeping Subordinate Payloads
 subordinate by default, and avoiding fragment classes, interfaces or result
 records created only to satisfy typing, serialisation or convenience
@@ -351,7 +340,7 @@
 ### Enforcement after proof
 
 Typing, schemas, validators, contracts and codecs exist to lock in a seam
-that has already been made real (P6, P1; rc.2 #3-enforcement-after-proof).
+that has already been made real (P6, P1).
 Parse, validate or construct first; admit and narrow the boundary
 explicitly; then use types or schemas to enforce the proved shape. It does
 not mean relabelling an open payload and calling it closed, wrapping loose
@@ -364,8 +353,7 @@
 
 ### Ingress collapse
 
-Foreign, dynamic or weakly typed input is lawful only at ingress (P1, P5;
-rc.2 #3b-ingress-collapse-rule). Once admitted, it collapses immediately
+Foreign, dynamic or weakly typed input is lawful only at ingress (P1, P5). Once admitted, it collapses immediately
 into local carrier truth before semantic transforms begin. The required
 shape: receive foreign input; parse, validate or normalise it once;
 construct local admitted carrier truth; consume only that local truth in
@@ -379,8 +367,7 @@
 
 ### Functional bias without language mandate
 
-Projects using this profile prefer (P4a, P5, P6;
-rc.2 #4-functional-bias-without-language-mandate): immutable data carriers over
+Projects using this profile prefer (P4a, P5, P6): immutable data carriers over
 mutable shared objects; closed typed carriers over open dictionary or
 string protocols; parsing and admitting foreign data once at ingress;
 explicit return values over hidden mutation; explicit failure carriers
@@ -404,13 +391,12 @@
 mutable carrier state where it is materially necessary, under §10
 [Immutable carriers](#immutable-carriers), and the failure-carrier
 preference only where practical. Convenience permits no departure (P6,
-P2; the predecessor's "must prefer" and "must avoid", read with the
-necessity exception of its immutable carrier rule).
+P2).
 
 ### Python typing
 
 When this profile governs a Python boundary, repo-authored Python is fully
-typed (P1; rc.2 #4a-python-typing-rule): every function, method and
+typed (P1): every function, method and
 callable surface has explicit parameter and return annotations; semantic
 carriers are closed and typed; and repo-authored tests, scripts and
 support code are typed too, with no lower bar than production code.
@@ -442,8 +428,7 @@
 ## 5. Ontology-first design
 
 Every new or materially changed active semantic boundary derives its
-semantic model from one accepted Ontology (P1, P6;
-rc.2 #4b-ontology-first-design-rule). Before a new or changed entity, function,
+semantic model from one accepted Ontology (P1, P6). Before a new or changed entity, function,
 authority, effect, Prime-conformant carrier, module boundary, public
 operation or schema is promoted, the affected boundary first produces a
 candidate Ontology slice and carries it through the acceptance sequence
@@ -502,7 +487,7 @@
 
 For one governed boundary `B`, let `M(B)` be its complete material-relation
 set (decision-complete symbolic design, below) and `U(B)` the unresolved
-members of that set (P2, P0; rc.2 #proportional-design-sequencing):
+members of that set (P2, P0):
 
 ```text
 U(B) = unresolved(M(B))
@@ -572,7 +557,7 @@
 ### Decision-complete symbolic design
 
 For one governed boundary `B`, the complete material-relation set is (P1,
-P2; rc.2 #decision-complete-symbolic-design):
+P2):
 
 ```text
 M(B) =
@@ -618,8 +603,7 @@
 
 `M(B)` closes one governed boundary. A bounded local action is taken inside
 a design frame that derives from other accepted frames, and its lawfulness
-depends on relations the acting frame does not itself own (P4b, P0;
-rc.2 #bounded-frame-conservation-stdo-up-017). Global and local are relative to
+depends on relations the acting frame does not itself own (P4b, P0). Global and local are relative to
 the selected frame. Each material design frame identifies:
 
 - the governing frames and accepted relations from which it derives;
@@ -676,8 +660,7 @@
 A semantically coherent design is not acceptable when its selected
 substrate cannot natively construct the required identities,
 relationships, transitions, authority boundaries, effects, lifecycle,
-composition, publication and retirement behaviour (P2, P5;
-rc.2 #native-constructability-before-design-acceptance-stdo-up-002). A missing
+composition, publication and retirement behaviour (P2, P5). A missing
 substrate capability remains an explicit design gap or triggers lawful
 re-entry (SPEC_METHOD §4); it is not hidden behind a reference bridge,
 adapter, filesystem runner, test double or promised future feature (P6;
@@ -692,8 +675,7 @@
 mechanism is the best realisation. Before constructing a material generic
 capability, common mechanic or algorithm, or selecting a material
 dependency, the active design boundary performs a proportional
-foundation-selection pass (P2, P6;
-rc.2 #capability-and-foundation-selection-stdo-up-023). Its governing law
+foundation-selection pass (P2, P6). Its governing law
 is [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) Shared machinery; this
 section is its selection procedure.
 
@@ -810,7 +792,7 @@
 
 The Ontology enumerates the entities inside the active boundary, their
 identities, relationships, cardinalities, invariants, lifecycle states and
-authority owners (P3, P5; rc.2 #entity-and-lifecycle-completeness). For
+authority owners (P3, P5). For
 each entity, design evidence provides this logical-completeness matrix or
 an equivalent closed representation:
 
@@ -841,7 +823,7 @@
 ### Authority model
 
 Authority is part of the Ontology, not metadata added to an operation
-after its shape has been selected (P6; rc.2 #authority-model). For every
+after its shape has been selected (P6). For every
 Ontology function or lifecycle transition that crosses a semantic,
 authority, admission, effect, persistence or public boundary, design
 evidence provides this authority matrix or an equivalent closed
@@ -881,8 +863,7 @@
 The authority matrix names who admits; it does not by itself establish the
 relation that decides which candidate transformation becomes durable
 entity truth. Two designs can complete the matrix plausibly and still leave
-two materially different ways to admit the same transformation (P6, P4b;
-rc.2 #transformation-admission-completeness-stdo-up-016).
+two materially different ways to admit the same transformation (P6, P4b).
 
 For every consequential entity-transition domain, design evidence contains
 the complete transformation-admission relation over entity identity,
@@ -961,8 +942,7 @@
 that make the entity lifecycles logically complete. Variation that changes
 only an entity kind, projection kind, transition kind, policy or
 subordinate payload should normally be a typed parameter or closed variant
-of one function family, not another peer function (P4a, P3;
-rc.2 #atomic-functions-and-higher-order-composition). The minimum
+of one function family, not another peer function (P4a, P3). The minimum
 function-derivation evidence is:
 
 | Discovered functionality | Entity | Atomic function or template | Higher-order composition | Effect class | Required authority | Disposition |
@@ -999,7 +979,7 @@
 function family, identity, authority transition, lifecycle relation,
 topology, effect, closure law or composition law that cannot be expressed
 honestly by composing other accepted atoms while preserving the same
-meaning (P3, P1; rc.2 #prime-semantic-atoms-and-universal-domain).
+meaning (P3, P1).
 
 Prime is decided at semantic-design altitude. A file, source function,
 class, schema record, public operation, diagram, module or owner category
@@ -1028,8 +1008,7 @@
 each atom in isolation. The family includes every proposed identity,
 authority transition, lifecycle relation, topology, function, composition
 law, effect and closure law. A function-and-carrier-only pass does not
-establish whole-family Prime (P3, P2;
-rc.2 #whole-family-prime-contraction). Before promotion, review asks:
+establish whole-family Prime (P3, P2). Before promotion, review asks:
 
 - can several proposed operations be typed parameters of one atomic
   function?
@@ -1057,8 +1036,7 @@
 contractions. A locally irreducible atom is not globally Prime when the
 family duplicates identity, authority, function, lifecycle, topology,
 effect or projection meaning. Local Prime-conformance of realisation units
-does not prove the semantic family globally Prime (P3, P6;
-rc.2 #recursive-prime-and-root-conservation-stdo-up-003).
+does not prove the semantic family globally Prime (P3, P6).
 
 Contraction preserves root authority and every retained semantic relation.
 Reducing files, functions, operations or authoring surfaces cannot
@@ -1074,7 +1052,7 @@
 
 ### Ontology projection
 
-The Ontology is one semantic truth (P1, P6; rc.2 #ontology-projection-law).
+The Ontology is one semantic truth (P1, P6).
 These preserve it and do not become independent semantic authorities:
 class or domain diagrams; sequence diagrams; state and lifecycle diagrams;
 authority and effect matrices; the IACS; public APIs, operation registers,
@@ -1105,8 +1083,7 @@
 part of the evidence used to accept the Ontology basis. Target design,
 IACS, modules, source functions, schemas and tests project those accepted
 atoms; they do not originate Prime meaning. Prime applies both to each
-semantic atom and to the candidate family as a whole (P3, P2;
-rc.2 #5-prime-law).
+semantic atom and to the candidate family as a whole (P3, P2).
 
 Prime-conformance applies to these realisation projections: functions,
 classes, carrier types, top-level schema records and modules. Typed
@@ -1155,8 +1132,7 @@
 
 The proportionality relation that weighs ambiguity removed against
 reasoning complexity introduced is ACTIVATION §6; this clause applies it to
-Prime contraction (P2, P0;
-rc.2 #boundary-and-governance-cost-stdo-up-005). Review cuts, realisation
+Prime contraction (P2, P0). Review cuts, realisation
 units, runtime modules and work items are distinct boundaries. They may
 relate many-to-one or one-to-many and are not forced into one-to-one
 decomposition for administrative convenience. Prime review accounts for
@@ -1170,8 +1146,7 @@
 
 When defining a schema, carrier family or typed public boundary, derive
 the IACS from the accepted Ontology before naming subordinate payloads or
-implementation modules (P3, P6;
-rc.2 #5a-irreducible-architectural-carrier-set-rule). The IACS is the smallest
+implementation modules (P3, P6). The IACS is the smallest
 set of carriers required to carry the real functionality and authority
 flow of the boundary. It should be named before subordinate payload
 records, helper result shapes or internal branch detail. It is the carrier
@@ -1218,7 +1193,7 @@
 
 The IACS is not numerically frozen. Adding, removing, merging or splitting
 a carrier is lawful through accepted Ontology and design re-entry (P6,
-P4b; rc.2 #iacs-revision-obligation). For every such revision, accepted
+P4b). For every such revision, accepted
 design:
 
 - re-derives the complete IACS and classifies every addition, removal,
@@ -1241,7 +1216,7 @@
 
 A top-level class, dataclass, TypedDict, enum or named schema record
 justifies its existence as an architectural boundary, not merely as
-payload detail (P3, P2; rc.2 #5b-promotion-test). A Subordinate Payload may
+payload detail (P3, P2). A Subordinate Payload may
 be promoted to a top-level type only when at least one of these is true:
 it is an authoritative source carrier; it is a public or persisted
 contract boundary; it is an explicit variant of a public outcome family
@@ -1265,7 +1240,7 @@
 Schema work declares the IACS, which types are authoritative, which types
 are downstream projections, which shapes are Subordinate Payloads, and
 which Subordinate Payloads are intentionally deferred from promotion (P3,
-P2; rc.2 #5c-boundary-inflation-prohibition). The rule exists to stop type
+P2). The rule exists to stop type
 proliferation from turning one migration into many parallel schema
 migrations. If a schema or ticket lists a wide family of types, it
 distinguishes the IACS from the Subordinate Payloads; failing to make that
@@ -1284,8 +1259,7 @@
 
 When a realisation is being derived from an existing design line, released
 tenant or reference implementation, design-method completion does not rest
-on code comparison alone (P6, P4b;
-rc.2 #5d-reference-derived-module-design-rule). The required derivation
+on code comparison alone (P6, P4b). The required derivation
 evidence is: (1) constitutional WHAT; (2) reference design; (3) target
 Ontology and reference-to-Ontology mapping; (4) target design mapping; (5)
 target module boundary assets; (6) implementation. The rule exists to stop
@@ -1313,8 +1287,7 @@
 
 Every new or materially changed semantic or typed module boundary carries
 one accepted Ontology and one complete three-view Mermaid design asset
-before the boundary is promoted or claims design-method closure (P6, P1;
-rc.2 #5e-ontology-and-three-view-behavioral-design-gate). When
+before the boundary is promoted or claims design-method closure (P6, P1). When
 `co_evolution_admissible(B)` holds, design evidence, implementation and
 tests may develop together before that gate; otherwise the affected
 unresolved, contradictory or materially non-equivalent relation is
@@ -1338,7 +1311,7 @@
 ### Ontology evidence
 
 The design asset cites one accepted Ontology for the active boundary and
-includes or references its (P6; rc.2 #ontology-evidence): entity and
+includes or references its (P6): entity and
 relationship inventory; invariant and cardinality law; entity-lifecycle
 completeness matrix; authority matrix; atomic-function and
 higher-order-function derivation matrix; governing composition and effect
@@ -1358,8 +1331,7 @@
 reasoning state a bounded actor needs, because the actor selecting a local
 action generally does not hold the reasoning that produced the governing
 frames. Dialogue, commentary, prior-agent memory and implementation
-folklore are not that state (P0, P4b;
-rc.2 #invariant-reconstruction-sufficiency-stdo-up-018). The general
+folklore are not that state (P0, P4b). The general
 reconstruction rule is [ACTIVATION §1 Intake](ACTIVATION.md#intake); this
 clause states what design evidence supplies to it.
 
@@ -1407,8 +1379,7 @@
 its cause selects, `indeterminate` where the admissible evidence cannot
 decide, naming what would decide (FOUNDATIONS §4 Results); where the
 cause is that the selected method basis and the accepted design do not
-suffice, the case falsifies this law, as stated below. The mapping is
-new in this corpus. Purpose and material relation: a lawful change is
+suffice, the case falsifies this law, as stated below. Purpose and material relation: a lawful change is
 never read as a violation or as an action the acting frame may accept, and
 a violation is never read as a re-entry (P4b, P6).
 
@@ -1429,7 +1400,7 @@
 ### Domain model
 
 The `classDiagram` is the structural domain projection of the Ontology
-(P1, P3; rc.2 #domain-model). It shows, for the active boundary: domain
+(P1, P3). It shows, for the active boundary: domain
 identities and cardinalities rather than helper-class decomposition;
 entity ownership, invariants and lawful lifecycle relationships; atomic
 function families and their entity inputs and outputs where they cross the
@@ -1451,7 +1422,7 @@
 ### Sequence model
 
 The `sequenceDiagram` is the behavioural projection of Ontology functions
-and authority (P1, P6; rc.2 #sequence-model). It shows the supported
+and authority (P1, P6). It shows the supported
 execution path from admitted input to result or truthful stop, and names
 the owner and required authority of every decision, admission, execution,
 projection and effect boundary. Where applicable it shows malformed input
@@ -1468,7 +1439,7 @@
 ### State model
 
 The `stateDiagram-v2` is the lifecycle projection of Ontology entities
-(P3, P5; rc.2 #state-model). It shows the complete admitted lifecycle for
+(P3, P5). It shows the complete admitted lifecycle for
 the active boundary, including refusal, blocked, continuation, retry,
 escalation and terminal states that the boundary can produce. Every
 transition binds to an Ontology function and names its owning authority,
@@ -1480,7 +1451,7 @@
 
 The design pack evaluates every applicable product, graph, language,
 runtime, handler and module axiom with one of `pass`, `fail` or
-`not_applicable` with a reason (P1, P6; rc.2 #cross-view-axiom-evaluation).
+`not_applicable` with a reason (P1, P6).
 The minimum evaluation columns are:
 
 | Axiom | Ontology evidence | Authority | Domain evidence | Sequence evidence | State evidence | Native enforcement | Admission/compiler enforcement | Verdict | Gap owner |
@@ -1539,8 +1510,7 @@
 frame does not declare; `invalid_basis` where the Ontology or design basis
 cannot support it. An applicable axiom that the pack did not evaluate has
 no result (FOUNDATIONS §4 Results, Not performed). None of these is
-`pass`. The mapping and the direct core values are new in this corpus.
-Purpose and material relation: a design gate that combines axiom verdicts
+`pass`. Purpose and material relation: a design gate that combines axiom verdicts
 with other results reads them in the one core, so an excluded axiom is
 never read as conforming or as failing, and an undecided or unevaluated
 axiom is never read as a pass or a fail (P5, P6).
@@ -1552,7 +1522,7 @@
 contract or semantic carrier is promoted or the work claims design-method
 closure. Any failed applicable axiom, missing functionality disposition,
 unresolved authority path or blocking realisation gap keeps the verdict
-non-accepted (P6; rc.2 #gate-and-retrospective-work).
+non-accepted (P6).
 
 The Ontology verdict and the design verdict are each an acceptance
 result: a decision that consumes the results of assessment, distinct from
@@ -1579,8 +1549,7 @@
 as a failed axiom does, because a combination with a non-satisfied
 mandatory result or a gap is never `satisfied`
 ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results))
-(P6, P5). The binding to ACTIVATION §3 is new in this corpus. Purpose and
-material relation: neither a passing matrix nor a produced design pack is
+(P6, P5). Purpose and material relation: neither a passing matrix nor a produced design pack is
 read as acceptance, and the design gate's acceptance combines with other
 results in the one core (P6).
 
@@ -1625,8 +1594,7 @@
 domain-distinct components rest on the same data structures and
 algorithms. Repeated machinery is therefore invisible to a domain-only
 reading, and each occurrence looks correctly owned and correctly named
-within its own entity (P1;
-rc.2 #computational-realization-projection-stdo-up-019).
+within its own entity (P1).
 
 Component role sets. Every material realisation component has an explicit
 set of semantic and operational roles. Technology capability does not
@@ -1717,8 +1685,7 @@
 
 This profile is operational and stands on its own. It does not require a
 user to adopt the world-model domain or accept any empirical ontology
-programme before using it (P1;
-rc.2 #5f-theoretical-framing-for-boundary-law). The capitalised Ontology of §5
+programme before using it (P1). The capitalised Ontology of §5
 is the engineering Ontology of one designed boundary; it does not require
 adoption of the Constraint-Emergence Ontology, a world-model theory, or
 any other metaphysical or empirical claim.
@@ -1748,7 +1715,7 @@
 ## 9. Module taxonomy
 
 When this profile governs a realisation boundary, modules should be
-classified by role (P0, P6; rc.2 #6-design-module-taxonomy). Recommended
+classified by role (P0, P6). Recommended
 roles are:
 
 - carrier module: defines typed immutable inputs, outputs, contracts,
@@ -1791,13 +1758,12 @@
 Projects using this profile prefer one algebraic primitive plus
 projections over several local decision systems, and prefer total
 functions, closed enums, explicit state and deterministic folds (P2, P5,
-P6; provenance rc.2 authority_compressions/stdo_compressed.md and
-design_module_method.compressed.md, a claim no rc.2 body states).
+P6).
 
 ### Immutable carriers
 
 Source truth should be carried in typed immutable values unless mutation
-is materially necessary (P3, P4b; rc.2 #7-immutable-carrier-rule). The
+is materially necessary (P3, P4b). The
 preferred shape: a constructor or parser produces a typed carrier;
 transforms consume one carrier and return another carrier or a closed
 result; projections read those carriers without mutating them. Mutable
@@ -1809,7 +1775,7 @@
 ### Totality
 
 Semantic functions should be total or as close to total as the language
-and problem allow (P5; rc.2 #8-totality-rule). The rule applies P5
+and problem allow (P5). The rule applies P5
 ([FOUNDATIONS §3](FOUNDATIONS.md#3-commitments)) to a semantic function,
 which can meet an input outside its admitted domain. The method's own
 results, with their non-success values, are the core result algebra of
@@ -1827,7 +1793,7 @@
 
 ### Effect edge
 
-Effects should be explicit and isolated (P5, P6; rc.2 #9-effect-edge-rule).
+Effects should be explicit and isolated (P5, P6).
 Typical effect edges include file writes, network calls, subprocess
 execution, event append, manifest publication, prompt delivery and
 database mutation. Semantic kernels should not perform these effects while
@@ -1841,8 +1807,7 @@
 ### No semantic centre
 
 No controller, manager, service method, runtime loop or public wrapper
-should be the hidden semantic centre of the system (P6, P1;
-rc.2 #10-no-semantic-center-rule). That includes deciding meaning procedurally
+should be the hidden semantic centre of the system (P6, P1). That includes deciding meaning procedurally
 in orchestration code, rebuilding truth from payload fragments,
 rehydrating current law from legacy files or fallbacks, and flattening
 typed meaning into ad hoc dictionary handling and `.get(...)` chains. A
@@ -1855,7 +1820,7 @@
 ### Coupling
 
 Coupling should be reduced by dependency shape, not only by file count
-(P6; rc.2 #11-coupling-rule). The preferred dependency direction is
+(P6). The preferred dependency direction is
 `carriers -> semantic kernels -> effect shells -> projections`, not
 `controllers -> service helpers -> mutable runtime state -> projections`.
 Design is too coupled when many modules read and mutate the same object;
@@ -1869,8 +1834,7 @@
 When a boundary governs, observes, routes, audits or evaluates another
 actor, executor, builder or substrate, it publishes governance truth, not
 imperative strategy law, unless strategy ownership is explicitly part of
-the boundary's ratified responsibility (P0 boundary commitment, P6;
-rc.2 #11a-governancestrategy-separation-rule). Lawful governance publication
+the boundary's ratified responsibility (P0 boundary commitment, P6). Lawful governance publication
 includes current state, preserved structure, unmet pressure or unresolved
 identities, route eligibility, the lawful edit or proof frontier, admitted
 policy identity, and prior-turn or prior-run continuity. Unlawful strategy
@@ -1890,7 +1854,7 @@
 
 When a realisation boundary is lawfully open for migration, refactor or
 bounded implementation work, the area should be left better than it was
-found (P2, P6; rc.2 #11b-opportunistic-optimization-rule). This does not
+found (P2, P6). This does not
 outrank constitutional truth, declared module ownership evidence or
 functional equivalence; it is subordinate to them. Opportunistic
 optimisation is lawful only when it is boundary-local to the active design
@@ -1930,8 +1894,7 @@
 
 When the same realisation pattern appears across more than one processed
 boundary, review treats that pattern as a commonisation candidate rather
-than as another purely local clean-up (P2, P4a;
-rc.2 #11c-recurrence-extraction-rule). Module boundaries make this review
+than as another purely local clean-up (P2, P4a). Module boundaries make this review
 possible: they constrain computation and evaluation enough that repeated
 local shapes can be compared honestly and consolidated into libraries
 without changing product truth. A recurrence candidate is usually not
@@ -1971,8 +1934,7 @@
 
 When a ticket applies this profile to its boundary and claims that
 boundary has been processed, the design-method closure claim should not rest on
-implementation status alone (P6, P2;
-rc.2 #11d-post-ticket-design-review-rule). The processed boundary is checked
+implementation status alone (P6, P2). The processed boundary is checked
 against its accepted design basis and exact closure claim before the
 ticket claims closure under this profile. The check may be part of the
 ticket's normal verification; it does not require a separate artifact,
@@ -2057,7 +2019,7 @@
 ### Interface bleed prohibition
 
 No interface should bleed semantic authority into another interface family
-(P6; rc.2 #12-interface-bleed-prohibition). Interface bleed exists when one
+(P6). Interface bleed exists when one
 interface reconstructs another interface's source truth; projection logic
 becomes closure logic; report or prompt logic becomes admission logic;
 public wrappers decide kernel semantics; or adapters invent meaning instead
@@ -2070,7 +2032,7 @@
 
 Projects using this profile do not use proxy or partial interface
 implementation as a substitute for real migration or real design
-completion (P6; rc.2 #13-proxy-interface-prohibition; SPEC_METHOD §7
+completion (P6; SPEC_METHOD §7
 Bridge prohibition). A proxy interface is a new-looking surface that
 forwards to the old authority path, reconstructs missing truth from the
 old path, keeps the old path executable behind a new name, or allows
@@ -2086,14 +2048,11 @@
 prompt construction. A worker may be told where to inspect and what
 contract to satisfy. A prompt clause that exists to enforce design law
 needs provenance and a proof that the clause still causes or prevents the
-intended behaviour (P6, P1; provenance rc.2
-authority_compressions/design_module_method.compressed.md, a claim no rc.2
-body states).
+intended behaviour (P6, P1).
 
 ### Design review questions
 
-When reviewing code under this profile, ask (P6;
-rc.2 #14-design-review-questions):
+When reviewing code under this profile, ask (P6):
 
 1. Does semantic law live in typed carriers or in orchestration code?
 2. Are the main steps readable as transforms over admitted truth?
@@ -2238,15 +2197,21 @@
     the foundation-selection relation before its implementation was
     retained?
 
-If these questions cannot be answered cleanly, the realisation is too
-coupled or too imperative (P6, P2).
+An unanswered required relation withholds the conformance claim that
+depends on it. Record the unanswered relation and the evidence needed to
+decide it, then diagnose the gap at its actual owner under
+[ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation).
+A missing authority declaration or observation does not by itself show
+excessive coupling or imperative design. That diagnosis requires evidence
+that meaning is held in orchestration or outside the declared carriers
+and transforms, under [SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape)
+(P6, P2, P1).
 
 ### Functional realisation checklist
 
 When a project claims functional bias, pure transforms, immutable
 carriers, single-owner truth or low-coupling realisation, review
-explicitly checks (P6, P5;
-rc.2 #14a-functional-realization-review-checklist):
+explicitly checks (P6, P5):
 
 - [ ] the change preserves the constitutional WHAT and keeps realisation
       work inside lawful HOW surfaces only;
@@ -2410,8 +2375,7 @@
 or design surfaces; naming it in the project's agent entry surface (such
 as `AGENTS.md`) as the preferred realisation discipline; using it as
 review criteria for implementation-migration tickets; and classifying
-implementation modules by the taxonomy of §9 (P2, P6;
-rc.2 #15-adoption-guidance).
+implementation modules by the taxonomy of §9 (P2, P6).
 
 When the profile is adopted, the project applies it consistently across the
 named boundary: Ontology and architecture derivation; design modules;
@@ -2452,8 +2416,7 @@
 profile governs preferred realisation structure inside implementation and
 design modules; the UX profile ([UX](UX.md)) refines this profile for UX
 surfaces with rendering, state-transition and effect-membrane rules and is
-loaded only when the work realises a UX surface (P6;
-rc.2 #16-relationship-to-other-method-surfaces). So SPEC_METHOD answers what is
+loaded only when the work realises a UX surface (P6). So SPEC_METHOD answers what is
 lawful process; RELEASE what is a lawful release, Product, install,
 exact-cut acceptance and selector-promotion decision; the graph-execution
 profile what is lawful graph-native product shape; this profile what is
@@ -2484,8 +2447,7 @@
 profile may publish default identity generators, validators and
 normalisers for its own runtime surfaces and for the default ODD surface
 kinds used by default `F_D` helpers; the permission is scoped to that role
-and does not extend to other runtime realisations (P3, P6; provenance rc.2
-IDENTITY_METHOD #defaults-from-a-bound-abg-realization). Their standing as
+and does not extend to other runtime realisations (P3, P6). Their standing as
 defaults and the identity law of their override, its preservation
 conditions and its publication surface are
 [IDENTITY §7](IDENTITY.md#7-default-formats-and-overrides).
@@ -2499,106 +2461,4 @@
 that remains required where a boundary composes higher-order or effectful
 computation are stated once in
 [SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape) (P1,
-P4a; rc.2 #17-non-goals).
-
-## 13. Source dispositions
-
-Rows of rc.2 DESIGN_MODULE_METHOD.md received by this member, and the one
-IDENTITY_METHOD row it closes. Anchors are into rc.2
-DESIGN_MODULE_METHOD.md unless the row names IDENTITY_METHOD; a locus is a
-section of this file unless another member is named. Every conserved row
-is restated in the receiving member's own text; a route is provenance
-only. Generalisations recorded here: "SPEC_METHOD.md", "RELEASE_METHOD.md",
-"TICKET_METHOD.md" and "UX_METHOD.md" are written as the tenant members
-SPEC_METHOD, RELEASE, TICKETS and the UX profile; "ODD_METHOD.md" and
-"ODD-governed" as the graph-execution profile ([ODD](ODD.md)), whose own
-terms (GTL, ABG, `F_D`, graph function, edge traversal) this tier-3
-profile keeps; "STDO-UP-021" as ACTIVATION §4, "STDO-UP-022" as
-EVALUATION §1 and §3, "STDO-UP-004" as IDENTITY §6, "Agentic Construction
-Execution" as ACTIVATION §1, "Operational Lifecycle Sufficiency Rule" as
-SPEC_METHOD §2, "Core Interface Migration Rule" and "retention relation"
-as SPEC_METHOD §7, "WORLD_MODEL_METHOD.md" as the world-model profile
-(PROFILES §5); "this method" is written "this profile"; "STDO basis" is
-written "method basis"; "graph/C constructor" is written "graph or
-computation constructor"; "section 6C", "section 11C" and the "4B and 5E"
-rules are written as their successor sections. The predecessor's "must" is
-written in the indicative; every "should", "may", "recommended",
-"typical", "preferred", "normally", "usually", "minimum", "where
-practical" and "allowed" keeps its force. Where a law already lives in
-tier 1 or 2, the row names both loci and the tier-1 or tier-2 sentence is
-pointed to, not repeated.
-
-| Anchor | Disposition | Locus |
-|---|---|---|
-| #1-purpose | conserved; the five biases, the six goals, no mandated authoring path, the co-evolution condition on same-pass derivation, bounded intermediate traversal, non-replacement of constitutional and graph law, outcomes do not decide counts, no replacement of graph carriers, the four scopes, not language-bound | §1 Purpose |
-| #2-position | conserved; the four "should" clauses, functional discipline without a functional language, the five example languages | §1 Position |
-| #3-core-rule | conserved; stated once in SPEC_METHOD §2 Realisation shape, scoped to boundaries this profile governs, at "should" force with its too-imperative test; pointed to here | SPEC_METHOD §2 Realisation shape; §1 Core rule |
-| #3a-odd-alignment-and-escalation-rule | conserved; the first question, the three-layer governing shape, the five governable kinds, the five hidden-semantics prohibitions, the "should be repriced" escalation, the realisation-cut statement | §2 |
-| #3b-boundary-closure-evaluators | conserved; "should be judged", not optional heuristics, no progress when one fails | §3 |
-| #1-authority-seam-closure | conserved; no increase in truth surfaces, "should reduce", the four meanings, the fail-closed test, the four source-coherence requirements | §3 Authority seam closure |
-| #2-essential-carrier-consolidation | conserved; "should collapse", the three meanings, the three progress and three non-progress items | §3 Essential carrier consolidation |
-| #3-enforcement-after-proof | conserved; the three steps, the three false closures, the three language examples, proof first | §3 Enforcement after proof |
-| #3b-ingress-collapse-rule | conserved; lawful only at ingress, immediate collapse, the four-step shape, the four non-lawful closures | §3 Ingress collapse |
-| #4-functional-bias-without-language-mandate | conserved; the six preferences (one "where practical") and the seven avoidances | §4 Functional bias without language mandate |
-| #4a-python-typing-rule | conserved; full typing with the three meanings, the six non-typed forms, the four required shapes, the four conditions for `Any`, `cast` and `# type: ignore`, the strict checker and its conformance consequence | §4 Python typing |
-| #4b-ontology-first-design-rule | conserved; derivation from one accepted Ontology, candidate slice before promotion of the eight kinds, subordinate to WHAT, not a replacement for design, source and authority identification, stable identities and basis, partial invalidation, no self-ratification, no second document, the material boundary definition, the refactor and delta rules, the ten-term Ontology, not a census; the reprice that invalidates is named as an instance of ACTIVATION §7's material input change, which owns the invalidators | §5; ACTIVATION §7 |
-| #proportional-design-sequencing | superseded in its repeated-surprise sentence, proposed and pending the product owner's acceptance: repeated or cross-cutting material surprises are evidence for diagnosis under ACTIVATION §1 Feedback and diagnosis and require one bounded `design_reframe` only where the diagnosis establishes that the affected design cut is underconstrained, where rc.2 took any such surprises as that evidence and required the reframe; the rest conserved: the four definitions, co-evolution and design-gated modes, the disposable spike, neither mode default, counterfactual evidence, no prior gate where no material alternative remains, evidence relation not authority, carrier placement, switch at the smallest set, serial repairs, the warranted and disproportionate gate; the proportionality relation itself is ACTIVATION §6 | §5 Proportional design sequencing; ACTIVATION §6 |
-| #decision-complete-symbolic-design | conserved in full; the nineteen-term `M(B)`, the decision-complete criterion stated as the design-gate acceptance criterion, projections of one network, underconstraint and the three cases, open local choices only when equivalent, contradictory projections block (stated as a precondition of the design gate, not a decision on a review finding), no further document | §5 Decision-complete symbolic design |
-| #bounded-frame-conservation-stdo-up-017 | conserved; the five frame items, several governing frames with the three examples, the evaluation and re-entry rule, the subordinate-frame rule, the falsifier, discovered functionality as evidence, the nine-step derivation order; the seam rule is ACTIVATION §1 Execution unit and §4 Refinement, and P4b's frame instance is FOUNDATIONS §3, both pointed to | §5 Bounded frame conservation (UP-017); ACTIVATION §1, §4; FOUNDATIONS §3 |
-| #native-constructability-before-design-acceptance-stdo-up-002 | conserved; the nine required native constructions, explicit gap or re-entry, the five forbidden hidings, obligation not prescription | §5 Native constructability (UP-002) |
-| #capability-and-foundation-selection-stdo-up-023 | conserved in full; the label-free statement, relation and mechanic factoring, the five candidate sources, bounded reproducible discovery with its per-category declarations and invalidation, the strategy boundary and no-preference rule, compositions, the eight comparison dimensions, elimination, unknowns, frontier, dominance, the trade-off owner, role and authority preservation, recursion, distinction from recurrence, proportional application; the candidate-not-adjudication law is FOUNDATIONS §4 Shared machinery, pointed to; the later candidate that invalidates selection evidence is named as an instance of ACTIVATION §7's material input change, and reuse conferring no authority as an instance of FOUNDATIONS §2 Authority kinds, What creates no authority | §5 Capability and foundation selection (UP-023); FOUNDATIONS §4; ACTIVATION §7; FOUNDATIONS §2 Authority kinds |
-| #entity-and-lifecycle-completeness | conserved; the enumeration, the seven-column matrix, the inheritance rule, the four "may" and "should normally" lifecycle readings, cell completeness, distinction from the operational lifecycle | §5 Entity and lifecycle completeness |
-| #authority-model | conserved; authority in the Ontology, the eight-column matrix, the five distinctions, role coincidence, helper inheritance, no implicit widening and its four consequences, stated as design instances of FOUNDATIONS §2 Authority kinds, What creates no authority, which owns the list; the named typed transition and owning admission boundary carry in the design the explicit authority decision FOUNDATIONS requires and do not replace it | §5 Authority model; FOUNDATIONS §2 Authority kinds |
-| #transformation-admission-completeness-stdo-up-016 | conserved in full; the six-column relation, the seven declarations, binding to ACTIVATION §4 as sole owner of admission semantics, per-owner qualification, `not_applicable` conditions, the three obligation falsifiers, singularity, competing-path disposition and retention, projection status (an instance of FOUNDATIONS §2 Authority kinds, What creates no authority), the three law falsifiers | §5 Transformation admission completeness (UP-016); ACTIVATION §4 |
-| #atomic-functions-and-higher-order-composition | conserved; smallest parameterised families, "should normally", the seven-column minimum matrix, the five row dispositions, the seven typical categories and six laws, vocabulary not required, graph and other bindings, iterative discovery only under co-evolution, reconciliation, no undeclared constructor | §5 Atomic functions and higher-order composition |
-| #prime-semantic-atoms-and-universal-domain | conserved; the definition, design altitude, many-to-many mapping, contraction before proof, admitted domain, no local fork, out-of-domain and in-domain cases, candidate atom without domain | §5 Prime semantic atoms and admitted domain |
-| #whole-family-prime-contraction | conserved in full; complete family and projections, the eight review questions, plausible families not Prime, contraction during design | §5 Whole-family Prime contraction |
-| #recursive-prime-and-root-conservation-stdo-up-003 | conserved in full; atom then family, local not global, root authority and relation preservation, no compensation by reduction, the eight evidence elements, citing the existing basis | §5 Recursive Prime and root conservation (UP-003) |
-| #ontology-projection-law | conserved; one truth, the ten non-authorities, source and preserved law, accepted loss and failure condition, structural HOW without rival meaning, tracing, ungrounded design excluded, enumeration not required | §5 Ontology projection |
-| #5-prime-law | conserved; atoms before units, projections do not originate, the five conformance kinds, typed closure insufficient, the four hard terms, Prime-conformance, the five typical lawful reasons, the nine non-conformant purposes, the four preferences, not line count | §6 |
-| #boundary-and-governance-cost-stdo-up-005 | conserved; distinct boundaries in any cardinality, governance cost, the six contraction failures, proportional evidence; the proportionality relation is ACTIVATION §6, pointed to | §6 Boundary and governance cost (UP-005); ACTIVATION §6 |
-| #5a-irreducible-architectural-carrier-set-rule | conserved; derivation before naming, the definition, "should be named", the six roles, the four non-justifications, the seven evidence steps, projection not replacement, incompleteness, co-evolution and design-gated reconciliation; the IACS is named as the carrier inventory ASSURANCE binds | §6 Irreducible architectural carrier set |
-| #iacs-revision-obligation | conserved; not frozen, lawful revision, the four revision duties (the assurance-congruence law written as EVALUATION §1 and §3), consumption without restatement, the three falsifiers | §6 IACS revision |
-| #5b-promotion-test | conserved; justification as boundary, the five promotion grounds, the five non-lawful cases, the default rule, burden on promotion, "should assume" | §6 Promotion test |
-| #5c-boundary-inflation-prohibition | conserved; the five declarations, the purpose, the distinction and drift, the four inflation conditions, design debt | §6 Boundary inflation prohibition |
-| #5d-reference-derived-module-design-rule | conserved; not code comparison alone, the six-step derivation, the purpose, the five minimum assets, the design question, incompleteness | §6 Reference-derived module design |
-| #5e-ontology-and-three-view-behavioral-design-gate | conserved; Ontology and three-view asset before promotion, co-evolution and design-gated cases, unchanged boundaries, the three views, ratified alternative format, no flowchart substitute, one surface and one decision, projections not peers | §7 |
-| #ontology-evidence | conserved; the eight included items, parent slice, copying creates a truth surface | §7 Ontology evidence |
-| #invariant-reconstruction-sufficiency-stdo-up-018 | conserved in full; reasoning state not deliverable, sufficiency to recover and decide, two distinct inputs and the duplication warning, the four-decision table, the two boundaries, bounded sufficiency, no artifact, the falsifier, the withheld-history test; the general reconstruction-without-history rule is ACTIVATION §1 Intake, pointed to. New in this corpus: the four decisions are a refinement mapped into the core of FOUNDATIONS §4 Results for "the action is admissible in the acting frame on the current governing basis", preserves and duplicates to `satisfied`, changes to `invalid_basis` as for the disposition `re_enter` of ACTIVATION §3, violates to `falsified`, and an evaluation that reaches no decision returns the core value its cause selects | §7 Invariant reconstruction sufficiency (UP-018); ACTIVATION §1 |
-| #domain-model | conserved; the twelve shown elements, the six stereotypes, the two visibility marks, the three relationship expectations | §7 Domain model |
-| #sequence-model | conserved; the execution path, owners and authority, the applicable paths, participant and message binding, no silent replacement, Ontology function binding | §7 Sequence model |
-| #state-model | conserved; the complete lifecycle with its state kinds, transition binding, controller memory not lifecycle truth | §7 State model |
-| #cross-view-axiom-evaluation | conserved; the three verdicts, the ten-column matrix, the eleven proofs, graph-native visibility, the blocking constructor. New in this corpus: the three verdicts are a refinement mapped into the core of FOUNDATIONS §4 Results for "on the exact Ontology and design basis, the boundary's design meets the axiom, or the axiom does not apply to the boundary", `pass` and `not_applicable` to `satisfied`, `fail` to `falsified`; the predicate is a disjunction that includes non-application, under ACTIVATION §1 Applicability, Exclusion and the core, which decides that `satisfied` for `not_applicable` never establishes that the design meets the axiom and that `not_applicable` requires a false applicability premise. Tightening the predecessor implies and does not state: an evaluated axiom that reaches none of the three verdicts records the core value its cause selects, and an applicable axiom not evaluated has no result; neither is `pass` | §7 Cross-view axiom evaluation; ACTIVATION §1 Applicability |
-| #gate-and-retrospective-work | conserved; both verdicts accepted, the four blockers, the unchanged-refactor proof, provisional evidence under co-evolution, the spike, retrospective review, no rationalisation, boundary-bounded asset, incompleteness and its limits. New in this corpus: each verdict is an acceptance result, the disposition of the design authority under ACTIVATION §3 Disposition, `accepted` being `accept` mapped to `satisfied` for "the candidate is accepted at its declared boundary"; it consumes the assessment results and is never inferred from them. Tightening the predecessor implies and does not state: an axiom verdict that maps to a value other than `satisfied`, an applicable axiom with no result, or an axiom with no result whose applicability is not established false, keeps the verdict non-accepted as a failed axiom does | §7 Gate and retrospective work; ACTIVATION §3 Disposition |
-| #computational-realization-projection-stdo-up-019 | conserved in full; domain-only blindness, role sets and the three cases (technology capability conferring no authority named as an instance of FOUNDATIONS §2 Authority kinds), the projection and its seven contents, the producer-to-consumer path, operational assumptions, subordinate projection and the four-step sequence, the ten dimensions, separation conditions, the two-part disposition, the four falsifiers; the cost separation and dimension declaration are ACTIVATION §6, shared machinery FOUNDATIONS §4, both pointed to | §7 Computational realisation projection (UP-019); ACTIVATION §6; FOUNDATIONS §4 |
-| #5f-theoretical-framing-for-boundary-law | conserved; stands alone, engineering Ontology without metaphysical adoption, the Markov-object framing, the four analogues, justification not prerequisite, scope not expanded | §8 |
-| #6-design-module-taxonomy | conserved; "should be classified", the six recommended roles, not naming ceremony, bounded traversal reasoning, the four review questions, recurrence visibility | §9 |
-| #6a-design-to-module-to-implementation-unit-tests-evidence-route | conserved in full; restated in tier-2 terms bound by this profile's declared binding | ASSURANCE §14 |
-| #6b-module-derived-unit-test-rule | conserved in full; restated as the realisation-authority side of the authority-source split | ASSURANCE §15 |
-| #6c-module-lifecycle-confirmation-rule | conserved in full | ASSURANCE §16 |
-| #7-immutable-carrier-rule | conserved; "should be carried", the three-part preferred shape, the three justifications, convenience insufficient | §10 Immutable carriers |
-| #8-totality-rule | conserved; "should be total", the three preferred properties ("when practical"), the three "should prefer" and three "should avoid" items; P5 is FOUNDATIONS §3 and the core result algebra FOUNDATIONS §4 Results, both pointed to; the outcome values a semantic function returns are the Product's domain values, not results of this method | §10 Totality; FOUNDATIONS §3 P5; FOUNDATIONS §4 Results |
-| #9-effect-edge-rule | conserved; "should be explicit", the seven typical edges, "should not perform", the four-step preferred sequence, "should be treated as suspect" | §10 Effect edge |
-| #10-no-semantic-center-rule | conserved; the five centres, the four inclusions, the five discovery questions, "should already exist" | §10 No semantic centre |
-| #11-coupling-rule | conserved; "should be reduced", the preferred and rejected directions, the four coupling signs, fewer places to invent meaning | §10 Coupling |
-| #11a-governancestrategy-separation-rule | conserved; governance not strategy, the seven lawful publications, the four drifts, the distinction, no replacement decision engine | §10 Governance and strategy separation |
-| #11b-opportunistic-optimization-rule | conserved; "should be left better", subordination, the five conditions, the four lawful and four non-lawful examples, repricing input, scope rule versus TICKETS, the test, the closing contrast | §10 Opportunistic optimisation |
-| #11c-recurrence-extraction-rule | conserved; commonisation candidate, the four "usually" properties, the five typical candidates, the rule of two, which TICKETS §6 owns as ticket law and this section refines as design-method conformance, the three conformance exceptions, the three-step "preferred" order (now stated once, at TICKETS §6), "should be extracted", separate decision, closure by consumption and retirement | §10 Recurrence extraction |
-| #11d-post-ticket-design-review-rule | conserved; "should not rest", the check, no separate artifact, TICKETS authority, the five determinations, complete reconstruction, what hashes, headings and green tests establish, causal closure and reuse, the five consequences, the closing rule with "should not claim"; reuse and its invalidators are ACTIVATION §7's, with a changed relation or new counterexample named as an instance of its material input change; whether a finding blocks current promotion is EVALUATION §5 When a finding blocks promotion, the five determinations being this profile's domain triggers for its four conditions, while a falsified closure claim stays blocked as a `falsified` result; "a ticket adopts" is written "a ticket applies this profile to its boundary" | §10 Post-ticket design review; ACTIVATION §7; EVALUATION §5 |
-| #12-interface-bleed-prohibition | conserved; "should bleed", the five bleed conditions, the three-part shape, non-bleed | §10 Interface bleed prohibition |
-| #13-proxy-interface-prohibition | conserved; the prohibition, the four proxy marks, bridge debt, explicit compatibility or removal | §10 Proxy interface prohibition |
-| #14-design-review-questions | conserved; all 56 questions in order, the closing rule | §11 Design review questions |
-| #14a-functional-realization-review-checklist | conserved; all 43 checks, the 14 hard-gate checks, language-agnostic scope, the unchanged-boundary gate | §11 Functional realisation checklist |
-| #15-adoption-guidance | superseded, proposed and pending the product owner's acceptance of the replacement relation (delta I3-3b, row 162): the rc.2 sentence "Projects may adopt this method by" the four means is replaced by PRODUCT_DEFINITION §7's rule that only Product authority adopts an available profile, with the four "may" means kept as the means by which that authority records its adoption; conserved unchanged: consistent application across six areas, "should make" the evaluators explicit, the four completion obligations, partial adoption "allowed" and "should be named", narrowing without skipped evidence | §12 Adoption; PRODUCT_DEFINITION §7 |
-| #16-relationship-to-other-method-surfaces | conserved; the five governances, the five answers, the graph-profile split, the UX refinement, lifecycle confirmation versus release decisions | §12 Relationship to other members |
-| #17-non-goals | conserved; stated once in SPEC_METHOD §2 Realisation shape, scoped to boundaries this profile governs: the four non-requirements, the readability requirement, the required composition and effect algebra, vocabulary optional and law not | SPEC_METHOD §2 Realisation shape; §12 Non-goals |
-| IDENTITY_METHOD #defaults-from-a-bound-abg-realization | conserved; the "may publish" permission for runtime surfaces and default surface kinds (with its graph-profile reading) is restated here; starter conventions and convenience contracts, not universal doctrine, lawful only while overridable, with the override law, are IDENTITY §7 | §12 Identity defaults from a bound runtime realisation; IDENTITY §7 |
-
-New law with no predecessor row: the family table at §1 Foundation to
-law, which decides nothing beyond the rules it cites, with
-[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law)
-owning its format and the standing of its consequences; and the paragraph
-Results and design records at the head of this member, which states where
-this profile's results are mapped, that its design-record vocabularies
-are not results, and the two senses of `not_applicable`, with its purpose
-and material relation stated there.
+P4a).
--- specification_methodology/v3/build_tenants/claude/standards/WORLD_MODEL.md
+++ specification_methodology/v3/build_tenants/common/standards/WORLD_MODEL.md
@@ -42,9 +42,7 @@
 Artifact, Composed World Model, Projection, Query Plane), with effective
 blanket, identity direction, null peer, core and coat, representation
 space, epistemic overlay, semantic kernel, publication ledger, control
-plane and data plane. Binding declared under PROFILES §1 (new; it makes
-the member map's "entity-cut law consumed by FOUNDATIONS P3" an explicit
-relation rather than a route): where FOUNDATIONS §2 defines an Object as
+plane and data plane. Binding declared under PROFILES §1: where FOUNDATIONS §2 defines an Object as
 a subject with scoped identity, a boundary, current state and declared
 material relations, and P3 makes a boundary a claim with a proof
 obligation, a world-model builder binds them to the published entity cut
@@ -57,13 +55,7 @@
 
 Each clause names the principle that requires it (P0 to P6, FOUNDATIONS
 §3), as [FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)
-requires. The predecessor's "must" is written in the
-indicative; its "should", "may", "preferred", "optional", "mandatory",
-"at minimum", "at least", "usually", "sufficient" and "lawful" keep their
-force. A route written `rc.2 #anchor` is into
-`stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md` and is
-provenance only; every predecessor row received here is restated in this
-text, and nothing here depends on that cut to be applied.
+requires.
 
 ## 1. Position
 
@@ -71,8 +63,7 @@
 needed to interpret them. World-model work builds a governed semantic
 layer over authoritative source systems, which enact bounded domain
 function through code paths, events, records, APIs, schedules,
-configurations, documents and downstream obligations (P1, P6;
-rc.2 #position). The profile starts from these claims:
+configurations, documents and downstream obligations (P1, P6). The profile starts from these claims:
 
 - source systems enact domain function and remain sovereign for
   operational truth;
@@ -94,7 +85,7 @@
 
 World-model work has two constitutional intents: build published domain
 artifacts; and compose those artifacts into higher-order world models
-(P2; rc.2 #constitutional-intents). Query, traversal and serving over
+(P2). Query, traversal and serving over
 those artifacts are important delivery concerns, but they do not define
 the constitutional identity of this profile. Those concerns may later be
 realised through a dedicated query or serving plane without changing the
@@ -103,7 +94,7 @@
 ### Manifesto
 
 The manifesto states the commitments the profile holds itself to (P1, P3,
-P6; rc.2 #manifesto):
+P6):
 
 - observe source systems before attempting to standardise them;
 - comprehend enacted semantics before flattening them into schemas;
@@ -175,10 +166,10 @@
 |---|---|---|---|---|
 | P1 (independent), P6 (independent); I1, I2 | By P1 a record does not carry its meaning, and by I2 the people who work with records already commit to the objects, so data is evidence of function and never meaning in isolation, and the world model is a derived semantic layer that makes those commitments explicit; by P6 and I1 the source systems keep operational truth, so the published semantic layer is the one truth surface for meaning, with overlays, query planes and compiled artifacts downstream of it | [§1](#1-position); [§3](#3-what-a-world-model-is), with [Single truth surface](#single-truth-surface); [§5](#5-core-claims) | the two constitutional intents, the manifesto and the order of the evidence hierarchy: this profile | 2, 6, 9 |
 | P3 (independent), P6 (independent); F8 imported ([IDENTITY §1](IDENTITY.md#1-position)); I2 | By P3 an identity binds its boundary and basis, and F8 resolves identity under owner, context and basis, so the primary published unit carries a declared identity with its boundary, authority, state, evidence, treatment, covariance and ambiguity; by P6 a claim holds only on its evidence, so the unit is discriminated from plausible alternatives at evidence altitude proportional to its claim; by P1 equal names do not establish equal meaning, so fully qualified naming removes preventable aliasing | [§6](#6-units), Entity Cut; [§8 Representation law](#representation-law); [§9 Admissibility](#admissibility); [§9 Discrimination](#discrimination); [§5](#5-core-claims) | the entity cut as that unit, its eight surfaces with three lawful values each, and its binding of FOUNDATIONS §2 Object and P3's boundary claim (this member's lead): this profile; which discrimination techniques a cut uses, none of them mandatory: the builder project | 2, 9 |
-| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent), P3 (independent); I1 | By P4b accepted facts are not erased and are not re-acquirable from memory, and by P3 a published value binds its exact cut, so the attribute ledger is append-only, and published truth should be immutable per cut and superseded by later cuts; by P6 and I1 an attribute's authority is its traced source, so every accepted attribute should be recoverable through its cut, its ledger entries, their assurance and that source | [§7](#7-flow); [§8 Materialisation law](#materialisation-law); [§8 Publication law](#publication-law); [§8 Attribute ledger law](#attribute-ledger-law); [§9 Publishing a cut](#publishing-a-cut) | Git and the filesystem as the publication ledger in the initial lane, with a later database as query plane: this profile; carriers, layouts, schemas and storage topology: consumer realisation | 2, 6, 9 |
+| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent), P3 (independent); I1 | By P4b accepted facts are not erased and are not re-acquirable from memory, and by P3 a published value binds its exact cut, so accepted facts and their provenance remain recoverable, and published truth should be immutable per cut and superseded by later cuts; by P6 and I1 an attribute's authority is its traced source, so every accepted attribute should be recoverable through its cut, its ledger entries, their assurance and that source | [§7](#7-flow); [§8 Materialisation law](#materialisation-law); [§8 Publication law](#publication-law); [§8 Attribute ledger law](#attribute-ledger-law); [§9 Publishing a cut](#publishing-a-cut) | the append-only attribute ledger as the selected mechanism for retaining accepted facts and provenance, and Git and the filesystem as the publication ledger in the initial lane, with a later database as query plane: this profile; carriers, layouts, schemas and storage topology: consumer realisation | 2, 6, 9 |
 | P1 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F2 imported ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)), F9 imported ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position)) | By P1 a mapping of fields does not carry meaning across domains, so cross-domain change is modelled as treatment, covariance and adjoint interpretation, not as naked field mapping; by F2 a treatment is a refinement or rewrite step, so it declares what it preserves and where it is not exact; by P4b a projection keeps its derivation, so it is a downstream convenience over the semantic kernel, should remain traceable to it, and is not semantic authority | [§5](#5-core-claims); [§6](#6-units), Treatment Surface, Covariance Edge, Adjoint Mapping; [§11 Projection law](#projection-law) | what a treatment preserves, its licensing law and, where it changes meaning, its adequacy relation: [ACTIVATION §4 Refinement](ACTIVATION.md#refinement); the five declared fields of a treatment and the preferred order world model, API contract, schema contract: this profile | 3, 6, 10 |
 | P1 (independent), P3 (independent); F12 imported ([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)) | By P1 equal spelling does not establish equal meaning, and by P3 a concept binds its owner and context, so imported product-lineage concepts keep their owner and meaning, and a narrower concept enters only by a declared directional specialisation, never as an alias | [§2](#2-role-and-imports); [§2 Builder Project specialisation](#builder-project-specialisation) | Builder Project and its narrowed meaning: this profile; the source concepts: [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects); the relation carrier: [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | 1, 2 |
-| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a construct's standing is what its evidence establishes, and its formal condition was tested and not met, so the Markov-object construct is held at candidate status; by F3 a failed run falsifies that run's predicate only, so the gate is not relocated; by P6 evidence is not authority, so overlays inherit the candidate class, entity cuts do not, and the pinned empirical program is research evidence, not authority | [§4 Epistemic status](#epistemic-status); [§4 Four working refinements](#four-working-refinements); [§13 Companion surfaces](#companion-surfaces) | the construct as load-bearing working vocabulary, the four working refinements and the program's pin: this profile; the statistical Markov boundary: a hypothesis of [FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses) | 2, 9 |
+| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a construct's standing is what its evidence establishes, so the Markov-object construct remains at candidate status unless its declared formal condition is met; by F3 a failed run falsifies that run's predicate only, so the gate is not relocated; by P6 evidence is not authority, so overlays inherit the candidate class, entity cuts do not, and research evidence does not amend the profile | [§4 Epistemic status](#epistemic-status); [§4 Four working refinements](#four-working-refinements); [§13 Companion surfaces](#companion-surfaces) | the construct as load-bearing working vocabulary, the four working refinements and the promotion gate: this profile; the statistical Markov boundary: a hypothesis of [FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses) | 2, 9 |
 | P3 (independent), P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F9 imported ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position)); I4 | Under I4 identity is a direction in a declared representation space, and by P3 the direction binds that space, so it is published and stored with its space, evidence and verification trace and never composed across spaces; by P6 it is accepted only on evidence, so only when a verification under held-out treatment preserves identity; by P4b and F9 its derivation from paired evidence stays traceable | [§10](#10-markov-object-overlay-construction) | the mean-offset form and its admissible supervised variants, the exclusion of principal-component and maximum-variance constructions, the three verifications, the seven publication items and the six storage items: this profile | 2, 6, 10 |
 | P2 (independent), P6 (independent), P0 (recovered); I3 | Under I3 probabilistic systems propose correspondences, and by P6 a proposal is not an accepted fact, so probabilistic correspondence belongs in an epistemic overlay on the control plane, outside the identity of the published object; by P0 and P2 delivery at volume cannot repeat judgment at each use, so accepted understanding governs compilation, and execution at scale should run through deterministic compiled artifacts | [§5](#5-core-claims); [§7](#7-flow), stages 11 and 13; [§12 Control plane and data plane](#control-plane-and-data-plane) | the split into a semantic control plane and a deterministic data plane: this profile | 8, 9 |
 | P2 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P4a (independent) | By P2 work serves a bounded outcome, and by P5 incomplete evidence is a declared gap, so a builder project may work a bounded source-object set repeatedly until its ledger is judged sufficiently saturated, with the remaining gaps explicit, and sparse first publication is lawful with its bound on evidence altitude declared; by P4a separate parts compose only through declared relations, so local published artifacts are stitched into higher-order models that keep their authority, not replaced by a central monolith | [§9 Admissibility](#admissibility); [§11 Saturation law](#saturation-law); [§11 Composition law](#composition-law) | the federated mesh as the preferred end state, with mesh topology product-local until its law is ratified: this profile | 2, 5, 9 |
@@ -190,9 +181,7 @@
 Surface, Covariance Edge and Adjoint Mapping; the opening of §9; or §13
 Output. These sections apply the consequences above, and every clause
 names the principle that requires it
-([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)). §15 records
-source dispositions and decides nothing. The table is
-new in this corpus. Purpose and material relation: an actor started on
+([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)). Purpose and material relation: an actor started on
 this member sees which rules follow from the foundations and the imported
 families, and which are choices of this profile, the builder project or a
 consumer, with their owners, so no choice is presented as derived and no
@@ -207,7 +196,7 @@
 - Row 3, the ledger, materialisation and publication: [§6](#6-units), Markov Object, whose published object is an immutable cut projected from the attribute ledger and not an in-place mutable record; [§10 Overlay publication](#overlay-publication), where overlays are never mutated in place under §8 Publication law; otherwise no separate consumer applies: carriers, layouts, schemas and storage topology are a consumer realisation, as the choice column states, and no section of another member names these sections.
 - Row 4, treatments, covariance, adjoint interpretation and projection: [§7](#7-flow), stage 8, where cross-domain meaning becomes explicit through treatment surfaces, covariance edges and adjoint mappings, and stage 12, where projections are emitted from the same semantic kernel; otherwise no separate consumer applies: what a treatment preserves and its licensing law are [ACTIVATION §4 Refinement](ACTIVATION.md#refinement)'s, as the choice column states, and no section of another member names these sections.
 - Row 5, imported lineage concepts and the Builder Project specialisation: [§6](#6-units), Builder Project, whose relation to Source Project is the directional specialisation of §2 and is not read as an unchanged import or general equivalence; otherwise no separate consumer applies: [GLOSSARY §10](GLOSSARY.md#10-recursive-product) and [§13](GLOSSARY.md#13-world-model) record the specialisation and decide nothing.
-- Row 6, the epistemic status of the construct: [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 12; [FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses), which carries the statistical Markov boundary at the candidate status this section states; [§4 Effective blanket](#effective-blanket), where the construct remains candidate-class; [§6](#6-units), Markov Object, whose theory is §4; [§10 Verification by treatment](#verification-by-treatment), where a verification battery is not a closed Markov blanket under §4 Epistemic status; [§14](#14-results-of-this-profile), promotion gate, and its closing paragraph, where a failed gate run does not falsify the construct.
+- Row 6, the epistemic status of the construct: [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 12; [FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses), which carries the statistical Markov boundary at the candidate status this section states; [§4 Effective blanket](#effective-blanket), where the construct remains candidate-class; [§6](#6-units), Markov Object, whose theory is §4; [§10 Verification by treatment](#verification-by-treatment), where a verification battery is not a closed Markov blanket under §4 Epistemic status; [§14](#14-results-of-this-profile), promotion gate, and its closing paragraph, where a failed gate run does not falsify the construct.
 - Row 7, the Markov-object overlay construction: [§4 Four working refinements](#four-working-refinements), whose fourth refinement grounds the exclusion of principal-component and maximum-variance constructions under §10; [§6](#6-units), Markov-Object Overlay, constructed and verified under §10, and Markov Object, whose representation-substrate obligations are §10's; [§8 Materialisation law](#materialisation-law), where §10 applies when the cut's selection is expressed geometrically in a declared representation space; [§14](#14-results-of-this-profile), direction acceptance, overlay publication, overlay storage and null-peer discrimination, and A verification not run, where an unrun verification leaves the direction a candidate.
 - Row 8, probabilistic correspondence and deterministic compilation: no separate consumer applies. The split is applied by a builder project when it aligns and compiles, at the stages this row names, and by the tooling it runs under them; [§13 Output](#output) lists the resulting epistemic overlays and compiled artifacts and decides nothing, and no section of another member names these sections.
 - Row 9, saturation, composition and sparse publication: [§4 Four working refinements](#four-working-refinements), whose third refinement keeps sparse first publication lawful under the Saturation law; [§7](#7-flow), stage 7, where sparse first publication is lawful under §9 Admissibility, and stage 10, where composition keeps local authority under §11 Composition law; [§14](#14-results-of-this-profile), cut admissibility and saturation.
@@ -222,7 +211,7 @@
 SPEC_METHOD defines the general constitutional method for spec-driven
 work; this profile is a domain-specific refinement of it for products
 and projects that observe existing source systems and publish bounded
-world-model artifacts (P6; rc.2 #method-role). The role split:
+world-model artifacts (P6). The role split:
 SPEC_METHOD defines the general process constitution; this profile
 defines the constitutional refinement for world-model construction work,
 including the current representation and publication law. Within the
@@ -274,8 +263,7 @@
 Builder Project is not an unchanged import or an alias for Source
 Project. It is the target of this explicit directional semantic
 translation of kind specialisation, stated with the coordinates
-PRODUCT_DEFINITION §5 requires (P1, P3;
-rc.2 #builder-project-specialization-relation):
+PRODUCT_DEFINITION §5 requires (P1, P3):
 
 - source concept: `urn:stdo:concept:recursive-product-taxonomy:source-project`,
   term Source Project, in
@@ -312,8 +300,7 @@
 ## 3. What a world model is
 
 A world model is a governed semantic layer built over existing source
-systems. It is descriptive before it is generative (P3, P6;
-rc.2 #what-a-world-model-is). Its primary semantic unit is the published
+systems. It is descriptive before it is generative (P3, P6). Its primary semantic unit is the published
 entity cut (§6 Units). Generic references to a "world-model object" are
 shorthand for this unit unless the text explicitly names a looser
 candidate or intermediate surface. A world model should make explicit:
@@ -335,7 +322,7 @@
 
 The profile should produce world models that are bounded, inspectable,
 challengeable, evidence-backed, versioned, composable,
-projection-capable and machine-reasonable (P2; rc.2 #method-objectives).
+projection-capable and machine-reasonable (P2).
 If the profile is working, it should become possible to answer:
 
 - what object is this record evidence of;
@@ -350,7 +337,7 @@
 ### Single truth surface
 
 World-model work has one constitutional truth surface: the published
-semantic layer (P6; rc.2 #single-truth-surface). That layer consists of
+semantic layer (P6). That layer consists of
 published domain artifacts; their bounded fragments and published entity
 cuts; explicit treatments, covariance edges, adjoint mappings and
 temporal reference artifacts; and composed world models built by
@@ -362,7 +349,7 @@
 ### Evidence hierarchy
 
 The profile works from the strongest available explanatory surfaces
-(P6; rc.2 #evidence-hierarchy). Preferred hierarchy:
+(P6). Preferred hierarchy:
 
 1. realised system behaviour and emitted records or events;
 2. source code, rules and configuration when available;
@@ -379,20 +366,18 @@
 ## 4. The Markov-object construct
 
 The profile treats "Markov object" as a load-bearing construct, not as
-borrowed vocabulary (P3, P1;
-rc.2 #theoretical-underpinnings-of-the-markov-object). A Markov object is
+borrowed vocabulary (P3, P1). A Markov object is
 a stable self-bounding pattern in a constraint structure whose internal
 state can be reasoned about through its effective blanket. The term is
 substrate-neutral: the same topology is expected wherever a constraint
-structure admits stable configurations, in biological systems (Friston's
-original setting), in the natural-language traces those systems emit, in
+structure admits stable configurations, in biological systems, in the natural-language traces those systems emit, in
 learned representations built over those traces (LLMs), and in the
 engineered institutional systems descended from both. The working claim
 is that world-model construction is possible because this topology
 propagates across substrates: what domain experts recognise as "objects"
-in an institutional system is the same kind of structure Friston
-described for biological systems, re-expressed through another
-substrate. The profile is the practice of making that structure explicit,
+in an institutional system is the same kind of stable constraint
+structure hypothesised for biological systems, re-expressed through
+another substrate. The profile is the practice of making that structure explicit,
 traceable and publishable (P3, P6). The generic law for boundary claims,
 their evidence and the limit on stronger Markov claims is
 [IDENTITY §2 Boundaries and sufficiency claims](IDENTITY.md#boundaries-and-sufficiency-claims);
@@ -402,8 +387,7 @@
 
 The naive reading of "blanket" is set-theoretic: a fixed set of member
 states partitioning internal from external. That reading does not survive
-contact with real representations (P1, P3;
-rc.2 #what-an-effective-blanket-actually-is):
+contact with real representations (P1, P3):
 
 - for any attribute basis over a domain (schema columns, SAE dictionary,
   feature set, vocabulary), the set of attributes that "fire" for an
@@ -422,26 +406,21 @@
 - a published Markov-object overlay is an identity direction together
   with the distributed attribute evidence supporting it.
 
-This reading is consistent with candidate evidence from a learned
-representation system. The evidence is direction-level and behavioural.
-The formal conditional-independence condition that would promote the
-construct from candidate to established has been tested and did not meet
-its predicate; the construct remains candidate-class (Epistemic status
-below) (P6).
+This reading is a working hypothesis. Direction-level and behavioural
+evidence can support an overlay without establishing the formal
+conditional-independence condition for a Markov blanket. The construct
+remains candidate-class under the promotion gate in Epistemic status
+below (P6).
 
 ### Four working refinements
 
-Four findings from the empirical program constrain how the profile treats
-Markov objects. They are working refinements: the program has produced
-candidate evidence for them, not a formal closure, and the profile adopts
-them as the best current reading of the construct (P3, P6;
-rc.2 #four-working-refinements-indicated-by-the-empirical-program). They
-are stated in the order and sense the pinned companion surface carries
-(§13 Companion surfaces), each with the experiment that grounds it, so the
-two can be checked against each other; where the companion later re-cuts
-them, the pin fixes which reading this profile adopted (P6, P3).
-
-1. Effective blanket is geometric, not set-theoretic (exp 17). A boundary
+Four working refinements constrain how this profile treats Markov
+objects. They are adopted commitments of this profile at candidate
+standing, not formal closure of the construct. An application records
+its own evidence for the boundaries and overlays it publishes; no
+refinement replaces the promotion gate (P3, P6).
+
+1. Effective blanket is geometric, not set-theoretic. A boundary
    stated as attribute-column membership leaks under bypass. The
    load-bearing structure is the identity axis, and a set-valued boundary
    over columns is an epistemic convenience rather than the object. The
@@ -452,13 +431,12 @@
    partially distributes it. Where a Markov-object overlay is published,
    it exposes the identity axis, not only the attribute profile. Schemas
    are evidence, not ontology.
-3. Core identity, not core size, is the discriminator of objecthood (exps
-   15, 16). A sparse invariant with semantically loaded content is a
+3. Core identity, not core size, is the discriminator of objecthood. A sparse invariant with semantically loaded content is a
    lawful object; a rich attribute cluster with nothing invariant under
    context variation is not. More columns do not buy more objecthood.
    This is why sparse first publication remains lawful under the
    Saturation law (§11).
-4. Identity is a DC shift, not a principal-variance axis (exp 18). Object
+4. Identity is a DC shift, not a principal-variance axis. Object
    identity appears as a mean offset in representation space, not as the
    dominant-variance direction. Characterisation by "the biggest source of
    variance in the attribute set" systematically misses identity;
@@ -474,27 +452,23 @@
 ### Epistemic status
 
 The profile commits to the Markov-object construct as load-bearing
-working vocabulary. The empirical program that sharpens it is at
-candidate status: it reports evidence consistent with the
-geometric-blanket reading but does not close the conditional-independence
-condition that would formally establish a Markov object in the
-statistical sense, which FOUNDATIONS §5 carries as a hypothesis (P6;
-rc.2 #epistemic-status-of-the-construct). Adopting this profile does not
-require that the empirical program be complete. Commitments that depend on
-a formally established conditional-independence object, for example
-claims that a published Markov-object overlay is the blanket rather than
-a candidate for it, are read as working commitments, open to revision
-when the companion program produces a conditional-independence result
-(P6, P5).
+working vocabulary at candidate status. Its geometric-blanket reading
+does not by itself establish the conditional-independence condition for
+a Markov object in the statistical sense;
+[FOUNDATIONS §5](FOUNDATIONS.md#5-hypotheses) carries that condition as a
+hypothesis. Adopting this profile does not require the hypothesis to be
+established. Claims that an overlay is the blanket rather than a
+candidate for it remain working commitments until the promotion gate is
+met for their exact subject and basis (P6, P5).
 
 Promotion gate. The experimental result that would promote the construct
 from candidate to established is a direction-native
 conditional-independence test: given the identity projection, residual
 variation along remaining components should be independent of the target
-under plausible treatments. That test has been run and did not meet its
-predicate, and its multi-layer successor did not either. The gate stands
-where it is; it has not been met and is not relocated to accommodate the
-negative result (P6).
+under plausible treatments. Candidate standing persists without a
+result that meets this predicate on the claimed subject and basis. A
+failed run falsifies that run's predicate; it does not relocate the gate
+or by itself falsify the construct (P6).
 
 This status attaches to the construct and to overlays built on it. A
 published Markov-object overlay is a candidate-class overlay of a
@@ -512,8 +486,7 @@
 
 The Markov-object framing gives a theoretical account of a design
 pressure that also appears in DESIGN_MODULE, whose §8 Theoretical framing
-names the analogues from its side (P3, P2;
-rc.2 #relation-to-design-module-method). If a Markov object is read as a
+names the analogues from its side (P3, P2). If a Markov object is read as a
 candidate identity-bearing cut, good software boundary design should
 prefer:
 
@@ -526,7 +499,7 @@
 - strongly typed semantic boundaries, so identity-bearing cuts are not
   left fuzzy, reconstructive or controller-owned.
 
-This profile does not make the empirical Markov-object program a
+This profile does not make established Markov-object theory a
 prerequisite for all design work. The relation runs the other way: this
 profile gives one theoretical framing for why these boundary disciplines
 are sound, and DESIGN_MODULE gives the general engineering law that
@@ -536,26 +509,22 @@
 
 Source systems remain sovereign. Operational truth remains with the
 systems that enact it. The world model is a derived semantic layer over
-those systems, not a replacement operational source (P6;
-rc.2 #source-systems-remain-sovereign).
+those systems, not a replacement operational source (P6).
 
 Domains are functional surfaces. A domain is defined by coherent
 function: what enters, what changes, what is owned, what is guaranteed,
-what leaves, and what adjacent domains can rely on (P3;
-rc.2 #domains-are-functional-surfaces).
+what leaves, and what adjacent domains can rely on (P3).
 
 Data is evidence, not meaning by itself. Data is a trace of constrained
-function execution; it is invalid in isolation from context (P1, P6;
-rc.2 #data-is-evidence-not-meaning-by-itself).
+function execution; it is invalid in isolation from context (P1, P6).
 
 World models externalise expert cognition. The world model is the
 inspectable form of the domain understanding that experts already carry
-implicitly (P6; rc.2 #world-models-externalize-expert-cognition).
+implicitly (P6).
 
 Mappings are semantic treatments. Cross-domain transformation is not
 plain structural rewrite. Every treatment declares preserved structure,
-changed meaning, loss, surplus and ambiguity (P1, P4b;
-rc.2 #mappings-are-semantic-treatments). A treatment is a refinement or
+changed meaning, loss, surplus and ambiguity (P1, P4b). A treatment is a refinement or
 rewrite step of
 [ACTIVATION §4 Refinement](ACTIVATION.md#refinement): what it preserves
 and its licensing law are that section's, and a treatment that changes
@@ -567,24 +536,21 @@
 Fully qualified naming is mandatory. Many cross-domain failures are
 preventable naming collisions. Fully qualified naming removes aliasing,
 so the remaining hard work is real semantic transformation; IDENTITY §2
-states the scoped identity it applies (P3, P1;
-rc.2 #fully-qualified-naming-is-mandatory).
+states the scoped identity it applies (P3, P1).
 
 Value lists are domain artifacts too. Changing code sets,
 classifications and value lists are governed temporal reference
-artifacts, not static enum decorations (P3;
-rc.2 #value-lists-are-domain-artifacts-too).
+artifacts, not static enum decorations (P3).
 
 The world model sits above APIs and schemas. API contracts and schema
 contracts are projections over the world model. They are useful because
 they publish structure and function; they are not the highest semantic
-authority (P6, P1; rc.2 #the-world-model-sits-above-apis-and-schemas).
+authority (P6, P1).
 
 Probability belongs in the epistemic overlay. The canonical published
 entity cut should remain semantic and bounded. Probability belongs in
 uncertainty, ranking, anomaly and alignment overlays, not in the
-ontological identity of the published object itself (P3, P6;
-rc.2 #probability-belongs-in-the-epistemic-overlay). That overlay may
+ontological identity of the published object itself (P3, P6). That overlay may
 include correspondence candidates; confidence and ranking; ambiguity
 registers; anomaly and surprise signals; and candidate mappings or
 treatment suggestions. The overlay is useful because it lets
@@ -596,7 +562,7 @@
 
 ## 6. Units
 
-The profile's units (P3; rc.2 #app, #builder-project and the sibling
+The profile's units (P3, #builder-project and the sibling
 unit anchors named in §15):
 
 | Unit | Definition | Requires |
@@ -624,7 +590,7 @@
 published Markov object is an immutable object cut projected from the
 attribute ledger, not an in-place mutable record; the cut is an identity
 direction together with the distributed attribute evidence that supports
-it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
+it, not an enumeration of member columns (P3, P4b).
 The Markov object is the theoretical account of why a discovered boundary
 is a real object rather than an arbitrary cluster. It is not a claim that
 the builder invents the object: institutional entities are already
@@ -639,7 +605,7 @@
 
 Entity Cut. The primary published semantic unit: an identity-bearing,
 bounded, evidence-backed cut of a recovered entity, projected from the
-attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
+attribute ledger (P3, P6). An entity cut is lawful
 without an identity direction. It publishes identity, boundary,
 authority, state, evidence, treatment, covariance and ambiguity, each
 traced to ledger entries and their assurance basis. Builder projects may
@@ -650,7 +616,7 @@
 
 ## 7. Flow
 
-The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
+The profile proceeds through these stages (P4b, P6 and
 the stage anchors named in §15):
 
 1. Observe. Gather source evidence from the strongest available surfaces
@@ -722,8 +688,7 @@
 
 ### Representation law
 
-Every published entity cut is prompt-sufficient for reasoning (P3, P1;
-rc.2 #representation-law). At minimum, the cut should make visible
+Every published entity cut is prompt-sufficient for reasoning (P3, P1). At minimum, the cut should make visible
 identity, boundary, authority, state, evidence, treatment, covariance and
 ambiguity. "Make the effective blanket explicit" means: state the
 boundary at which the entity's identity survives reinterpretation, not
@@ -741,8 +706,7 @@
 ### Materialisation law
 
 The materialised entity cut is an artifact of the world-model builder,
-not a raw artifact of the source system (P6;
-rc.2 #materialization-law). The governing split: source systems remain
+not a raw artifact of the source system (P6). The governing split: source systems remain
 sovereign for operational truth (§5); the builder observes and
 comprehends that truth; the published entity cut is the canonical
 object-level truth of the world-model layer; projections are derived from
@@ -775,7 +739,7 @@
 
 Published world-model truth should be immutable per cut; reviewable by
 diff; traceable to evidence; and superseded by explicit later cuts rather
-than silently overwritten (P4b, P3; rc.2 #publication-law). The
+than silently overwritten (P4b, P3). The
 filesystem and Git are sufficient for the publication plane in the
 initial lane. A database, if introduced later, is a query-plane
 complement rather than the constitutional publication authority. In other
@@ -789,7 +753,7 @@
 ### Attribute ledger law
 
 The attribute ledger is the immediate semantic source of an entity cut
-(P4b, P6; rc.2 #attribute-ledger-law). Every entry should be a fully
+(P4b, P6). Every entry should be a fully
 qualified claim, potentially including a value or measured quantity; a
 rule or constraint; a classification; a topology or relation claim;
 provenance and authority information; and effective, observed and
@@ -804,14 +768,14 @@
 Entities are recovered, not invented. A builder project constructs an
 entity cut by trawling authoritative source surfaces for the boundaries
 the operating model already commits to, then qualifying them into
-published truth (P3, P6; rc.2 #entity-cut-construction-law).
+published truth (P3, P6).
 
 ### Admissibility
 
 An entity cut is admissible when its identity, boundary, authority,
 state, evidence, treatment, covariance and ambiguity are explicit,
 traceable, and discriminated from plausible alternatives at evidence
-altitude proportional to the claim (P3, P6; rc.2 #admissibility). That is
+altitude proportional to the claim (P3, P6). That is
 the whole constitutional test. It binds what is true of a published cut;
 it does not prescribe how a builder establishes it (P0).
 
@@ -833,7 +797,7 @@
 "Discriminated from plausible alternatives" means the cut states why
 this boundary rather than a nearby one the operating model would treat
 differently. The claim carries its own discrimination; a stronger claim
-needs stronger discrimination (P3, P6; rc.2 #discrimination). Techniques
+needs stronger discrimination (P3, P6). Techniques
 that serve this, none of them mandatory and none of them exhaustive:
 
 - cross-context invariance: separate what holds wherever the entity
@@ -864,7 +828,7 @@
 boundary, authority, state, evidence, treatment, covariance and
 ambiguity) visible and traceable, each as a stated value, stated absence
 or stated non-applicability, and records the basis on which identity was
-discriminated (P3, P6; rc.2 #publication). Cuts are immutable: revising
+discriminated (P3, P6). Cuts are immutable: revising
 identity or boundary produces a new cut that supersedes the prior one
 (P4b). Concrete carriers, layouts, schemas and storage topology are
 consumer realisation; this profile requires that the published surfaces
@@ -876,8 +840,7 @@
 applies only where the builder operates over a declared representation
 space in which identity is a geometric direction (a learned
 representation, an embedding over ledger claims, or an equivalent metric
-space); it is not required for ordinary institutional recovery (P3, P2;
-rc.2 #markov-object-construction-law). Where it applies, a builder
+space); it is not required for ordinary institutional recovery (P3, P2). Where it applies, a builder
 project constructs the overlay by a directional, interventional
 procedure. The steps below are both how the overlay is built and the
 minimum structure that is stored when it is published. The declared
@@ -888,8 +851,7 @@
 ### Paired evidence collection
 
 For a candidate object, assemble attribute-ledger evidence across context
-variation together with evidence for at least one null peer (P3, P6;
-rc.2 #1-paired-evidence-collection):
+variation together with evidence for at least one null peer (P3, P6):
 
 - multiple contexts in which the candidate is instantiated;
 - a null-peer instance: a structurally similar thing that lacks the
@@ -904,7 +866,7 @@
 ### Identity-direction extraction
 
 Derive the identity axis as a low-rank projection over the paired
-evidence (P3, P1; rc.2 #2-identity-direction-extraction). The canonical
+evidence (P3, P1). The canonical
 form is the mean offset
 
 `d(object) = μ(evidence_object) − μ(evidence_null)`
@@ -921,8 +883,7 @@
 
 A candidate identity direction is accepted only if projection along it
 preserves object identity under held-out treatments. The builder records
-at least one acceptable verification (P6, P3;
-rc.2 #3-verification-by-treatment):
+at least one acceptable verification (P6, P3):
 
 - α-sweep: apply `x − α · d` on held-out contexts, and show the expected
   identity shift and its saturation behaviour;
@@ -935,10 +896,8 @@
 A direction that has no acceptable verification is a candidate, not an
 accepted overlay. Publishing an unverified direction violates the
 Representation law (§8). The underlying entity cut remains lawful and
-publishable without the overlay (P6, P3). The empirical program that
-motivates these treatments reports that the strongest of them,
-direction-native conditional independence, has been tested and does not
-close. Passing this battery establishes that a direction is verified for
+publishable without the overlay (P6, P3). Passing this battery establishes
+that a direction is verified for
 publication under this profile; it does not establish a formally closed
 Markov blanket (§4 Epistemic status) (P6).
 
@@ -948,16 +907,14 @@
 evidence into an invariant core, the attributes whose contribution to the
 identity direction is stable across ≥ N of N contexts, and a context
 coat, the attributes selected by the specific context, carrying
-contextual reinterpretation rather than identity per se (P3;
-rc.2 #4-core-and-coat-decomposition). Both are evidence. The core carries
+contextual reinterpretation rather than identity per se (P3). Both are evidence. The core carries
 identity; the coat carries treatment. The coat to core ratio is a
 characterisation, not a quality metric (P3, P1).
 
 ### Null-peer discrimination
 
 Before publication, discriminate an accepted Markov object from an
-incidental attribute cluster by null-peer comparison (P3, P6;
-rc.2 #5-null-peer-discrimination):
+incidental attribute cluster by null-peer comparison (P3, P6):
 
 - is the candidate's core size in a range that null peers also hit? Yes
   is expected and acceptable; size is not diagnostic;
@@ -972,8 +929,7 @@
 
 ### Overlay publication
 
-A published Markov-object overlay makes visible, at minimum (P6, P3;
-rc.2 #6-overlay-publication):
+A published Markov-object overlay makes visible, at minimum (P6, P3):
 
 - representation space: the declared space and attribute basis the
   direction is expressed in, versioned so a later re-fit is detectable;
@@ -999,8 +955,7 @@
 ### Storage shape
 
 The stored overlay is not a row in a table and not a membership list. It
-is a package attached to its entity cut (P4b, P6;
-rc.2 #7-storage-shape):
+is a package attached to its entity cut (P4b, P6):
 
 - the declared representation space and its version;
 - the geometric object (identity direction and projection support);
@@ -1021,8 +976,7 @@
 
 World-model construction is iterative. Builder projects may work a
 bounded source-object set repeatedly until the resulting attribute ledger
-is judged sufficiently saturated for publication (P2, P5;
-rc.2 #saturation-law). Sufficient saturation means: materially important
+is judged sufficiently saturated for publication (P2, P5). Sufficient saturation means: materially important
 attributes have traceable support; remaining gaps are explicit
 ambiguities rather than silent misses; and the resulting object cut is
 stable enough to publish and supersede later if needed. Sparse first
@@ -1032,8 +986,7 @@
 ### Composition law
 
 Do not build one central monolith first. Build local published domain
-artifacts and their entity cuts, then stitch them (P4a, P6;
-rc.2 #composition-law). Composition preserves fragment authority,
+artifacts and their entity cuts, then stitch them (P4a, P6). Composition preserves fragment authority,
 bounded-context meaning, treatment semantics, declared loss and
 ambiguity. Higher-order models are composed from published domain
 artifacts; they do not erase them (P4a, P4b). The preferred end state is
@@ -1045,7 +998,7 @@
 ### Projection law
 
 Projection is downstream convenience, not semantic authority; the
-semantic kernel remains primary (P6, P1; rc.2 #projection-law). All
+semantic kernel remains primary (P6, P1). All
 projections should remain traceable back to governing objects; evidence;
 treatments; covariance edges; adjoint mappings; and temporal reference
 artifacts where applicable. Tables, schemas, APIs, mapping documents and
@@ -1062,7 +1015,7 @@
 ### Control plane and data plane
 
 The world-model profile naturally separates semantic control from bulk
-execution (P0, P6; rc.2 #control-plane-and-data-plane). The semantic
+execution (P0, P6). The semantic
 control plane consists of published domain artifacts; composed world
 models; treatments, covariance edges and adjoint mappings; and epistemic
 overlays for correspondence, ranking and ambiguity. The high-volume data
@@ -1084,7 +1037,7 @@
 ### Proof law
 
 Adoption should not depend on winning the standardisation argument first
-(P2; rc.2 #proof-law). Preferred wedge:
+(P2). Preferred wedge:
 
 1. comprehend one bounded source slice;
 2. publish one fragment;
@@ -1108,8 +1061,7 @@
 Specifications are usually normative; world models are usually
 descriptive. A sufficiently well-formed world model can therefore project
 large parts of an application surface without requiring duplicated
-semantic re-authoring downstream (P2, P1;
-rc.2 #world-model-driven-development). Preferred relationship:
+semantic re-authoring downstream (P2, P1). Preferred relationship:
 
 `world model -> epistemic correspondence overlay -> deterministic compiled artifacts -> implementation`
 
@@ -1125,8 +1077,7 @@
 
 ### Output
 
-If the profile is working, the result is not just better metadata (P2;
-rc.2 #method-output). The result is:
+If the profile is working, the result is not just better metadata (P2). The result is:
 
 - published domain artifacts as the durable semantic publication units;
 - composed world models built from those published artifacts;
@@ -1144,22 +1095,18 @@
 
 ### Companion surfaces
 
-The companion surfaces of this profile are (P6;
-rc.2 #companion-surfaces): SPEC_METHOD, the constitutional specification
-method; RELEASE, the method for publishing immutable cuts and promoting
-version-line selectors for installed consumer bases; TICKETS, the method
-for turning discovery into bounded execution work; and
-`constraint_emergence_ontology`, at
-`markov_object_research/empirical_results.md`, the candidate empirical
-program on the Markov-object construct in a learned representation system
-(GPT-2 + SAEs). Experiments 08 onward report evidence consistent with the
-geometric-blanket reading; experiment 20 and its multi-layer successor
-tested the formal conditional-independence promotion gate and did not
-meet it. The program is bound at commit
-`2da7871bf48d3144e4e83d5e8a336671251a6c76`, document SHA-256
-`269b5c008bc9fa20283cef63bf2daca373af86b2cf495182753671a5b203b3dd`. It is
-research evidence, not constitutional authority; a later revision of that
-program does not amend this profile (P6, P3).
+The companion surfaces of this profile are local method owners (P6):
+
+- [SPEC_METHOD](SPEC_METHOD.md), the constitutional specification method;
+- [RELEASE](RELEASE.md), the method for publishing immutable cuts and
+  promoting version-line selectors for installed consumer bases;
+- [TICKETS](TICKETS.md), the method for turning discovery into bounded
+  execution work.
+
+Research evidence can support or challenge a hypothesis, but it does not
+amend this profile or replace its promotion gate. Changes to the working
+commitments follow [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)
+under their governing authority (P6, P3).
 
 ## 14. Results of this profile
 
@@ -1170,8 +1117,7 @@
 the value, so a `satisfied` for one predicate never counts toward another
 ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
 and no mapping raises a result's standing: nothing is coerced to
-`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
-material relation: this profile's verdicts decide publication of entity
+`satisfied` (P5, P6). Purpose and material relation: this profile's verdicts decide publication of entity
 cuts and overlays and enter conjunctions with the results of other
 members, which combine only in the core, so an inadmissible cut, an
 unverified direction or a failed gate run is never read as publishable
@@ -1244,112 +1190,3 @@
 §5's hypothesis standing, and candidate-class and formally closed are
 publication kinds; none of them is a result, and a gate run that fails
 does not falsify the construct.
-
-## 15. Source dispositions
-
-Rows of rc.2 WORLD_MODEL_METHOD.md received by this member. Anchors are
-into rc.2 WORLD_MODEL_METHOD.md; a locus is a section of this file unless
-another member is named. Every conserved row is restated in this
-member's own text; a route is provenance only. Generalisations recorded
-here: "WORLD_MODEL_METHOD.md" and "this method" are written "this
-profile"; "SPEC_METHOD.md", "RELEASE_METHOD.md" and "TICKET_METHOD.md" as
-SPEC_METHOD, RELEASE and TICKETS; "ODD_METHOD.md" as the graph-execution
-profile (PROFILES §2); "DESIGN_MODULE_METHOD.md" as DESIGN_MODULE;
-"GLOSSARY_GUIDE.md" as the GLOSSARY; "STDO basis" and "STDO release" as
-method basis and method release; the owner of the recursive product
-taxonomy, "SPEC_METHOD.md#recursive-product-taxonomy", as FOUNDATIONS §2
-Product lineage objects, which owns that bounded context now; the
-Builder Project owner "WORLD_MODEL_METHOD.md#builder-project" as §6
-Units. The predecessor's "must" is written in the indicative; every
-other modal keeps its force.
-
-Three clauses have no predecessor row and are new: the declared binding of
-FOUNDATIONS §2 Object and P3's boundary claim to the entity cut (lead);
-the refinements of the core result algebra (§14), which FOUNDATIONS §4
-Results requires of a profile with its own result vocabulary; and the
-family table (§1 Foundation to law), in the format of FOUNDATIONS §3
-Foundation to law (P1, P3, P5, P6).
-
-| Anchor | Disposition | Locus |
-|---|---|---|
-| #position | conserved; the lost-context premise, the eight enacting surfaces, the seven starting claims, inspectable versioned machine-reasonable truth; the family table under Foundation to law is new | §1 |
-| #method-role | conserved; the role split, primary surface, the owned bounded context, narrower Product contexts, graph-execution composition, the four imports with invalidation and the no-alias rule, the five "in particular" meanings; the import's owner is FOUNDATIONS §2 (generalisation); the import is a Semantic Import under PRODUCT_DEFINITION §5, which applies FOUNDATIONS §2 Imports between members between bounded contexts | §2 |
-| #builder-project-specialization-relation | conserved; all ten coordinates, stated against PRODUCT_DEFINITION §5's relation carrier | §2 Builder Project specialisation |
-| #constitutional-intents | conserved; the two intents, query and serving not constitutional, a later plane at "may" | §1 Constitutional intents |
-| #manifesto | conserved; the fifteen commitments and the not-world-model-driven condition | §1 Manifesto |
-| #what-a-world-model-is | conserved; descriptive before generative, the entity cut as primary unit and the shorthand rule, the eight "should make explicit" items, the five negations | §3 |
-| #theoretical-underpinnings-of-the-markov-object | conserved; load-bearing not borrowed, the definition, substrate neutrality across the four substrates, the propagation claim, recovery as practice | §4 |
-| #what-an-effective-blanket-actually-is | conserved; the set-theoretic reading rejected with its two grounds, the three geometric statements, candidate evidence and the failed promotion condition | §4 Effective blanket |
-| #four-working-refinements-indicated-by-the-empirical-program | conserved; the four refinements with their experiments, adoption as working reading, the pin rule, sharpening not weakening, not entity-cut admissibility | §4 Four working refinements |
-| #epistemic-status-of-the-construct | conserved; working vocabulary, candidate program, no completion prerequisite, working commitments, the promotion gate not met and not relocated, candidate-class overlays, entity cuts not inheriting the status, the "should default" publication kind; the formal object is FOUNDATIONS §5's hypothesis, pointed to | §4 Epistemic status; §14 |
-| #relation-to-design-module-method | conserved; the four "should prefer" preferences, not a prerequisite, the direction of the relation; DESIGN_MODULE §8 carries the analogues from its side | §4 Relation to the design profile |
-| #method-objectives | conserved; the eight "should" qualities and eight answerable questions | §3 Objectives |
-| #core-claims | not applicable: heading with no claim text (15 bytes); its nine children are disposed individually | §5 |
-| #source-systems-remain-sovereign | conserved | §5 |
-| #domains-are-functional-surfaces | conserved; the six functional coordinates | §5 |
-| #data-is-evidence-not-meaning-by-itself | conserved | §5 |
-| #world-models-externalize-expert-cognition | conserved | §5 |
-| #mappings-are-semantic-treatments | conserved; the five declarations of every treatment | §5 |
-| #fully-qualified-naming-is-mandatory | conserved; "mandatory" kept | §5 |
-| #value-lists-are-domain-artifacts-too | conserved | §5 |
-| #the-world-model-sits-above-apis-and-schemas | conserved | §5 |
-| #probability-belongs-in-the-epistemic-overlay | conserved; "should remain", the four overlay kinds, the five "may include" items, the substrate rationale, overlay not truth, the three distinct artifacts | §5 |
-| #single-truth-surface | conserved; the four layer constituents, the four supporting surfaces, no second truth surface | §3 Single truth surface |
-| #evidence-hierarchy | conserved; the five-level preferred hierarchy, code high-fidelity, behaviour broader, no code prerequisite | §3 Evidence hierarchy |
-| #method-units | not applicable: heading with no claim text (16 bytes); its seventeen children are disposed individually | §6 |
-| #app | conserved | §6, row App |
-| #builder-project | conserved; the concept identity, the definition, the directional specialisation and its non-equivalence | §6, row Builder Project |
-| #published-domain-artifact | conserved | §6, row Published Domain Artifact |
-| #fragment | conserved | §6, row Fragment |
-| #world-model-object | conserved; weaker than Markov Object, its uses, not the preferred published name | §6, row World Model Object |
-| #assurance | conserved | §6, row Assurance |
-| #attribute-ledger | conserved; the seven "may carry" entry kinds | §6, row Attribute Ledger |
-| #markov-object | conserved; the definition, immutable cut projected from the ledger, direction with evidence not columns, recovery not invention, entity cut with optional overlay, the three routes | §6 Markov Object |
-| #entity-cut | conserved; primary unit, lawful without direction, the eight published surfaces traced to ledger and assurance, convergence of looser candidates | §6 Entity Cut |
-| #markov-object-overlay | conserved; optional, admissible only with a declared space, the three additions, strengthens and its absence does not weaken | §6, row Markov-Object Overlay |
-| #treatment-surface | conserved | §6, row Treatment Surface |
-| #covariance-edge | conserved | §6, row Covariance Edge |
-| #adjoint-mapping | conserved | §6, row Adjoint Mapping |
-| #temporal-reference-artifact | conserved | §6, row Temporal Reference Artifact |
-| #composed-world-model | conserved | §6, row Composed World Model |
-| #projection | conserved | §6, row Projection |
-| #query-plane | conserved | §6, row Query Plane |
-| #method-flow | conserved; the profile proceeds through the stages | §7 |
-| #1-observe | conserved; the five surfaces | §7, stage 1 |
-| #2-trace | conserved; the "should" traceability to source span, field, locator, code path or record | §7, stage 2 |
-| #3-extract | conserved; the six intermediate surfaces, not yet the world model, the auditable path | §7, stage 3 |
-| #4-assure | conserved; the five "should make explicit" items | §7, stage 4 |
-| #5-ledger | conserved; append-only, new claims and later cuts, no in-place mutation | §7, stage 5 |
-| #6-bound | conserved; bounded contexts and coherent candidates, the two rejected modellings, the four boundary terms | §7, stage 6 |
-| #7-materialize | conserved; projection with enough context, sparse first publication under its three conditions | §7, stage 7 |
-| #8-relate | conserved | §7, stage 8 |
-| #9-publish | conserved; immutable cuts, no in-place mutation, Git and filesystem sufficient in the low-volume lane | §7, stage 9 |
-| #10-compose | conserved; recursive, inspectable, bounded, without erasing local authority | §7, stage 10 |
-| #11-align-optional | conserved; optional, the five "may produce" outputs, overlays not truth | §7, stage 11 |
-| #12-project | conserved; the eight outputs | §7, stage 12 |
-| #13-compile-optional | conserved; optional, the five "may include" examples, the three-part rule with "should run" | §7, stage 13 |
-| #14-serve-or-query-optional | conserved; optional, "if delivery needs justify it", filesystem-first or a later plane at "may" | §7, stage 14 |
-| #representation-law | conserved; prompt-sufficient, the eight "at minimum" surfaces, the blanket as surviving boundary, interventional not structural, the geometric form and the "should expose" overlay, semantic discharge under §9 | §8 Representation law |
-| #materialization-law | conserved; builder artifact, the four-part split, "should be versioned", the derivation chain, literal projection, many cuts per ledger state, the four-step recoverability and the three "should" prohibitions | §8 Materialisation law |
-| #publication-law | conserved; the four "should be" properties, Git and filesystem sufficient, a later database as query plane, the two ledgers distinct, both "should remain" append-only and replayable | §8 Publication law |
-| #attribute-ledger-law | conserved; immediate source, the six "should be" claim parts, the three "may be supported" evidence surfaces, one lawful claim record per fact | §8 Attribute ledger law |
-| #entity-cut-construction-law | conserved; recovered not invented, trawling then qualifying; the generic identity and boundary law is FOUNDATIONS §2 and P3, bound to the entity cut by this member's declared binding | §9; FOUNDATIONS §3 P3 |
-| #admissibility | conserved; the whole test with its eight surfaces and proportional altitude, not prescribing method, the three explicit values, no manufactured treatment, sparse first publication with the five entity kinds and the bound on altitude | §9 Admissibility; §14 |
-| #discrimination | conserved; the meaning, stronger claim stronger discrimination, the five non-mandatory techniques, adjoint round-trip as semantic analogue, interventional over declarative at "should say", interventional boundary and the weaker field-set claim at "should be read" | §9 Discrimination |
-| #publication | conserved; the eight surfaces visible and traceable with three values and the discrimination basis, immutable cuts and supersession, storage form as consumer realisation | §9 Publishing a cut |
-| #markov-object-construction-law | conserved; representation-substrate specialisation, its applicability and the three space kinds, not required otherwise, built and stored minimum, the space part of the overlay, no composition across spaces | §10 |
-| #1-paired-evidence-collection | conserved; at least one null peer, the three evidence items, distributed entries not the object | §10 Paired evidence collection |
-| #2-identity-direction-extraction | conserved; low-rank projection, the mean-offset formula, the three admissible supervised variants, principal-component and maximum-variance inadmissible, not a column | §10 Identity-direction extraction |
-| #3-verification-by-treatment | conserved; acceptance condition, at least one of the three verifications, unverified is candidate, publishing it violates the Representation law, the cut stays lawful, battery not a closed blanket; the mapping to the core result algebra is new (§14): a verification not run has no result, and publishing an unverified direction is `published_unverified` | §10 Verification by treatment; §14 |
-| #4-core-and-coat-decomposition | conserved; core across ≥ N of N contexts, coat, both evidence, ratio a characterisation | §10 Core and coat decomposition |
-| #5-null-peer-discrimination | conserved; the three questions with their expected answers, failure meaning not yet lawful | §10 Null-peer discrimination; §14 |
-| #6-overlay-publication | conserved; the seven "at minimum" items, immutable projection, revision supersedes, space change is supersession, no in-place mutation | §10 Overlay publication |
-| #7-storage-shape | conserved; not a row or list, the six package items, a lossy layout unlawful, derived planes no substitute | §10 Storage shape; §14 |
-| #saturation-law | conserved; iterative, repeated work at "may", the three saturation conditions, sparse lawful, silent unsupported attribute unlawful | §11 Saturation law; §14 |
-| #composition-law | conserved; no monolith first, local then stitch, the five preserved items, compose not erase, the preferred mesh, mesh topology product-local at "may", mesh law ratified at "should" only when stable | §11 Composition law |
-| #projection-law | conserved; convenience not authority, kernel primary, the six "should remain traceable" targets, publication forms, the preferred order, query and traversal at "may" | §11 Projection law |
-| #control-plane-and-data-plane | conserved; the four control-plane members, the data plane, the three carriers, plane not truth split, LLMs on the control plane with the four "should help" and the "should not" execution rule | §12 Control plane and data plane |
-| #proof-law | conserved; "should not depend", the five-step preferred wedge, incremental capture, the practical obligation, the "should also show" compilation proof | §12 Proof law |
-| #world-model-driven-development | conserved; parallel to spec-driven development, the two "usually", projection without re-authoring, the preferred and shorter relations, the four normative-spec cases, world model as substrate | §12 World-model-driven development |
-| #method-output | conserved; the ten results | §13 Output |
-| #companion-surfaces | conserved; the three method companions and the empirical program with its scope, findings, commit and document SHA-256 pin, research evidence not authority | §13 Companion surfaces |
--- specification_methodology/v3/build_tenants/claude/standards/ODD.md
+++ specification_methodology/v3/build_tenants/common/standards/ODD.md
@@ -6,9 +6,7 @@
 [PROFILES §1](PROFILES.md#1-the-boundary) and restates none of them. Inside
 its bounded context it uses its own terms freely: graph, node, asset,
 vector, edge, graph function, traversal, worksite, ledger, event log, GTL,
-ABG, F_D, F_P and F_H. A route written `rc.2 #anchor` is into
-`stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md` and is provenance
-only (P0, P1).
+ABG, F_D, F_P and F_H (P0, P1).
 
 Two definitions are used here and owned elsewhere. The a_c traversal record
 and the functor kinds are
@@ -146,7 +144,7 @@
 its own locus:
 
 - Row 1, nodes, vectors and typed assets: [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which asks first whether a boundary moves a typed asset from one state to another, and [DESIGN_MODULE Relationship to other members](DESIGN_MODULE.md#relationship-to-other-members); [§11.7](#117-manual-walkthrough-must-still-be-lawful), steps 1 and 2; [§11.7A](#117a-conforming-agentic-development), where admission enforces an artifact as a constructor enforces a typed asset under §11.1; [§17](#17-invocation-rule), step 5; [§19](#19-ramp-up-checklist), question 2; [§16](#16-failure-pattern), pattern 1.
-- Row 2, the bounded probabilistic step: [PROFILES §1](PROFILES.md#1-the-boundary), whose declared-binding rule takes its shape from the F_P and F_H specialisations §5 owns, and [PROFILES §2](PROFILES.md#2-graph-execution), which keeps the bounded-step binding and the worker's internal solution strategy outside the framework; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-09; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), which names A5 as the ODD specialisation of prompt construction; [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which keeps probabilistic worker boundaries out of imperative prompt or dispatch code; [§11.5B](#115b-execution-authority-audit) and [§11.7A](#117a-conforming-agentic-development), which read F_P and F_D at the audit and at the method layer.
+- Row 2, the bounded probabilistic step: [PROFILES §1](PROFILES.md#1-the-boundary), whose declared-binding rule takes its shape from the F_P and F_H specialisations §5 owns, and [PROFILES §2](PROFILES.md#2-graph-execution), which keeps the bounded-step binding and the worker's internal solution strategy outside the framework; [CONFORMANCE §1](CONFORMANCE.md#1-counterexample-cases), case C-09; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), which names A5 as the ODD specialisation of prompt construction; [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which keeps probabilistic worker boundaries out of imperative prompt or dispatch code; [§11.5B](#115b-execution-authority-audit) and [§11.7A](#117a-conforming-agentic-development), which read F_P and F_D at the audit and at the method layer.
 - Row 3, the bounded context: [PROFILES §1](PROFILES.md#1-the-boundary), which keeps the traversal record and the functor kinds as terms of AXIOMATIC_CALCULUS §5 apart from the profile's shorthands; [§11.5B](#115b-execution-authority-audit), which binds F_P and F_H to the source concepts of SPEC_METHOD §5 through §5 Probabilistic compute.
 - Row 4, graph functions and refinement: [PROFILES §2](PROFILES.md#2-graph-execution), which keeps the refinement binding with §11.8 as its specialised contract; [DESIGN_MODULE Atomic functions and higher-order composition](DESIGN_MODULE.md#atomic-functions-and-higher-order-composition), where a product under this profile binds its composition and effect algebra to GTL composition and ABG interpretation; [§11.7](#117-manual-walkthrough-must-still-be-lawful), step 2; [§17](#17-invocation-rule), steps 6 and 8; [§19](#19-ramp-up-checklist), question 3; [§16](#16-failure-pattern), patterns 2 and 7.
 - Row 5, published constructive carriers: [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which is not used to hide graph functions inside service methods, and [DESIGN_MODULE §11 Design review questions](DESIGN_MODULE.md#design-review-questions) 29 to 31; [UX §3](UX.md#3-product-truth-and-admitted-carriers), where a published graph function or lawful composition is an admitted carrier; [§9](#9-method-governance-and-audit), which asks which public graph functions carry the transition; [§17](#17-invocation-rule), steps 6 to 8; [§19](#19-ramp-up-checklist), questions 3 to 5; [§16](#16-failure-pattern), patterns 9 and 10.
@@ -192,10 +190,8 @@
   those surfaces. Whether a product is built correctly is decided by §11,
   and whether a move complies by the audit of §9.
 - §20 is a compression of this member and owns no determination (§20).
-- §21 records where each predecessor claim is carried and decides no
-  outcome ([FOUNDATIONS §3](FOUNDATIONS.md#foundation-to-law)).
-
-The table is new in this corpus. Purpose and material relation: an actor
+
+Purpose and material relation: an actor
 started on this member sees which rules follow from the foundations and
 which are choices, and who owns each choice, so no choice is presented as
 derived (P6, P1).
@@ -265,9 +261,8 @@
 
 Both the authoring library and an installed distribution contain three
 classes of document. Method members are the constitutional method
-surfaces; in the predecessor library they are the `*_METHOD.md` members,
-and in this corpus they are the members that [README](README.md#documents)
-names as method members: the tier 1 and tier 2 standards and, when a
+surfaces, the members that [README](README.md#documents) names as method
+members: the tier 1 and tier 2 standards and, when a
 project selects them, the tier 3 profiles. Guides (`*_GUIDE.md`) are operational guides and application standards
 that refine application of the method. Templates (`*_TEMPLATE.md`) are
 reusable starter forms and examples and are convenience artifacts only.
@@ -301,7 +296,7 @@
 fully determine the worker's internal solution path. One vector or edge
 traversal is the bounded unit of probabilistic compute (P0).
 
-Binding of the bounded step, new in this corpus. FOUNDATIONS P0 lets a
+Binding of the bounded step. FOUNDATIONS P0 lets a
 profile bind the bounded step to its own traversal unit and names
 [PROFILES §2](PROFILES.md#2-graph-execution), which indexes this profile,
 as the keeper of that binding. Direction: from the step of
@@ -378,7 +373,7 @@
 the graph function is the constructive realisation of that contract (P4a,
 P0).
 
-Binding of refinement, new in this corpus.
+Binding of refinement.
 [ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) generalises the
 refinement of one outer vector into an inner workflow to any realisation,
 lets a refinement carry an earlier output to a later step only through a
@@ -515,8 +510,7 @@
 result is non-compliance, the implementation should be repriced, repaired
 or rejected, not normalised by repetition (P6).
 
-Mapping of the audit outcome to the core result algebra, new in this
-corpus. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
+Mapping of the audit outcome to the core result algebra. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
 the outcome of every evaluation in the core. Material relation: a design,
 ticket or proof that consumes the audit reads incorporation as neither
 compliance nor failure. Each outcome maps for the predicate "the move
@@ -728,10 +722,8 @@
 admission authority is the graph-native specialisation of transformation
 admission completeness, whose admission semantics
 [ACTIVATION §4](ACTIVATION.md#complete-enclosing-relation-admission) owns;
-the software-design profile restates the predecessor rule in
-[DESIGN_MODULE, Transformation admission completeness](DESIGN_MODULE.md#transformation-admission-completeness-up-016)
-(provenance rc.2
-[STDO-UP-016](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)).
+the software-design profile applies that law in
+[DESIGN_MODULE, Transformation admission completeness](DESIGN_MODULE.md#transformation-admission-completeness-up-016).
 ABG's broader execution, supervision, retry and projection authority
 continues to derive from this profile and is not thereby reclassified as
 admission authority. `F_P` and `F_H` are the ODD projections of the
@@ -1073,9 +1065,7 @@
 edge, emit runtime events, mutate ledgers or decide re-entry. F_D, ABG and
 product admission own durable evidence and closure truth (P0, P6). An F_P
 worker must not be given an F_D-authored semantic extraction recipe when
-the edge requires F_P judgment (P0, P6; provenance rc.2
-authority_compressions/design_module_method.compressed.md, a claim no
-rc.2 body states).
+the edge requires F_P judgment (P0, P6).
 
 A6 Evidence before closure. No edge closes from raw artifact presence, a
 raw worker report, raw process success or a CLI summary. Closure is a fold
@@ -1119,8 +1109,7 @@
 Each disposition is replay-visible and must carry basis and reason refs
 sufficient to reproduce the decision (P5, P6).
 
-Mapping of the closure decision to the core result algebra, new in this
-corpus. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
+Mapping of the closure decision to the core result algebra. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
 every outcome in the core or in a refinement that maps each refined value
 to exactly one core value and adds no core value. Material relation: a
 composite over the edge joins each closure decision as one core value, so
@@ -1486,9 +1475,7 @@
 that follows. A derived surface or projected frame of the general method may
 orient the agent to source precedence, lawful re-entry and traceability;
 it must not be used to decide product-specific behaviour, which must come
-from the current product authority packet (P6, P1; provenance rc.2
-authority_compressions/spec_method.compressed.md, a claim no rc.2 body
-states).
+from the current product authority packet (P6, P1).
 
 The walkthrough proves at two levels. The work it produces must be lawful:
 correct change class, traceable, admitted. A point where the walkthrough
@@ -1539,8 +1526,7 @@
 
 Negative proof for an ODD or graph-native boundary exercises the supported
 Product authority path. It must not manufacture the refusal state, blocked
-event, gap or verdict that the system is supposed to derive (P6, P5;
-provenance rc.2 #117b-real-authority-path-negative-proof-stdo-up-010).
+event, gap or verdict that the system is supposed to derive (P6, P5).
 
 Closure-grade negative evidence identifies the supported entry and the
 governing authority; invalidates the real authority-bearing input;
@@ -1804,83 +1790,3 @@
 a source section differ, the source section decides
 ([ACTIVATION §2 Staleness of derived surfaces](ACTIVATION.md#staleness-of-derived-surfaces))
 (P1, P6).
-
-## 21. Source dispositions
-
-Rows of rc.2 ODD_METHOD.md received by this member, all 48 under
-STDO-UP-015. Anchors are into rc.2 ODD_METHOD.md; a locus is a section of
-this file. Every conserved row is restated in this member's own text at
-the predecessor's modal force; a route is provenance only. Formal content
-(code blocks and tables) is carried exactly and the prose around it is
-rewritten. Generalisations recorded here: rc.2 member file names are
-written as successor member names (ODD_METHOD as this profile, SPEC_METHOD,
-TICKETS, WORLD_MODEL, the software-design profile for DESIGN_MODULE_METHOD);
-imperatives ("do not", "declare") are written as indicative law or as
-"never", keeping their force; the predecessor's bold axiom titles are
-written as labelled paragraphs; American spellings are written British in
-prose and kept in identifiers (P6, P3).
-
-Seven clauses have no predecessor row and are new. Two are bindings that
-FOUNDATIONS P0 and ACTIVATION §4 assign to PROFILES §2, which indexes them
-in this profile: the binding of the bounded step of FOUNDATIONS P0 (§5
-Probabilistic compute) and the binding of the refinement of ACTIVATION §4
-(§5 Graph functions). The third is the opening note that roles are not
-functor kinds, which restates ACTIVATION §1 and AXIOMATIC_CALCULUS §5
-together. The fourth and fifth are the mappings of the A8 closure
-decisions (§11.5D) and of the §9 audit outcomes to the core result
-algebra, which FOUNDATIONS §4 Results requires of a profile with its own
-result vocabulary. The sixth is the family table (§1 Foundation to law),
-in the format of FOUNDATIONS §3 Foundation to law. The seventh is the
-statement in §20 that the canonical compression is a derived surface of
-this member under ACTIVATION §2 and owns no determination (P0, P1, P5, P6).
-
-| rc.2 anchor | Disposition | Locus |
-|---|---|---|
-| #1-position | conserved; the instruction written `using ODD, build this product`; its eight meanings, the paradigm equation, the three role expansions, the bounded-context URN, consumer binding and the two core jobs restated; the family table under Foundation to law is new | §1 |
-| #2-method-role | conserved; WORLD_MODEL_METHOD written as the world-model profile (WORLD_MODEL, tier 3) | §2 |
-| #3-method-composition | conserved | §3 |
-| #4-method-folder-semantics | conserved; the three classes and the rule that only method members are constitutional restated generically, the class named by its predecessor membership (`*_METHOD.md`) and in this corpus by the method members the standards README names (the tier 1 and tier 2 standards and, when a project selects them, the tier 3 profiles); the authoring path `specification/standards/` written generically, its successor path bound at packaging | §4 |
-| #5-graph-model | conserved | §5 |
-| #nodes | conserved; the ten example names kept as illustrative | §5 Nodes |
-| #vectors | conserved | §5 Vectors |
-| #probabilistic-compute | conserved; the three graph-native URNs, both directional specialisations with their preservation, exclusion and invalidation law; the source concepts' owner written SPEC_METHOD §5; kept distinct from the a_c functor kinds of AXIOMATIC_CALCULUS §5 | §5 Probabilistic compute |
-| #graph-functions | conserved; the three forms and the outer-contract rule | §5 Graph functions |
-| #traversal | conserved | §5 Traversal |
-| #6-product-boundary | conserved | §6 |
-| #7-self-host-boundary-rule | conserved | §7 |
-| #8-responsibility-layers-and-local-binding | conserved | §8 |
-| #9-method-governance-and-audit | conserved; "ODD_METHOD.md" written as this profile; the mapping of the three audit outcomes to the core result algebra is new | §9 |
-| #10-what-an-odd-product-is | conserved; the application boundary block carried exactly; the `reference_frame_bases` meaning routed to REFERENCE_FRAME | §10 |
-| #product-specification-software-development-topology | conserved | §10 Product specification |
-| #product-realization-software-development-topology | conserved | §10 Product realisation |
-| #abg | conserved; all thirteen ABG ownerships | §10 ABG |
-| #odd-product | conserved | §10 ODD product |
-| #query-and-service-layers | conserved | §10 Query and service layers |
-| #11-core-law | conserved; the all-clauses condition | §11 |
-| #111-typed-assets-and-nodes-are-explicit | conserved | §11.1 |
-| #112-graph-functions-are-the-primary-constructive-carrier | conserved | §11.2 |
-| #112a-outcome-first-realization-order | conserved | §11.2A |
-| #113-the-function-catalog-is-published | conserved; "at minimum" and "should" kept | §11.3 |
-| #114-the-gtl-module-is-the-operative-publication-surface | conserved | §11.4 |
-| #115-current-state-is-a-projection-over-constructive-history | conserved | §11.5 |
-| #115a-abg-owns-continuation-and-re-entry | conserved | §11.5A |
-| #115b-execution-authority-audit | conserved; the five-surface inventory carried exactly; UP-016's admission semantics are linked to their owner, ACTIVATION §4, and the predecessor rule to its restatement in the software-design profile, with the rc.2 route kept as provenance; the roles that F_P and F_H project are reached through the bindings of §5 Probabilistic compute to SPEC_METHOD §5 | §11.5B |
-| #115c-projection-source-coherence | conserved | §11.5C |
-| #115d-constructive-evaluation-and-yield-loop | conserved in full; the authority chain, the sixteen-object table, the four-function table, every axiom block, the constitutional equation and its where-clause carried exactly; A0 to A16 as labelled paragraphs; UP-013 routed to SPEC_METHOD §3; Design Module Method written as the software-design profile; the mapping of the closure decisions to the core result algebra is new, for the predicate "the edge's obligations are fulfilled on the exact basis", with `retry`, `repair`, `re-enter` and `block` split by cause into refined values, each mapped to exactly one core value; new: `evaluate_next`'s selection is stated to be no result of the core, while each typed no-action returns its own result for the selection predicate by cause and a closure decision it follows keeps its own value for the edge predicate; new: the closure decisions are distinguished from the dispositions of ACTIVATION §3, and the ground of `repair` is stated in this member | §11.5D |
-| #116-product-specific-semantics-sit-above-the-shared-carrier | conserved | §11.6 |
-| #117-manual-walkthrough-must-still-be-lawful | conserved; "§5.2 and §5.3" written as §5 Vectors and Graph functions | §11.7 |
-| #117a-conforming-agentic-development | conserved; SPEC_METHOD.md and TICKET_METHOD.md written as SPEC_METHOD and TICKETS; what a derived surface may decide referred to ACTIVATION §2 | §11.7A |
-| #117b-real-authority-path-negative-proof-stdo-up-010 | conserved in full, with the supported-relation block carried exactly; this section is UP-010's only successor home | §11.7B |
-| #118-cumulative-environment-law-is-mandatory | conserved; "mandatory", "should declare", "may require" and "structurally wrong" kept; profile law, not generalised into the core; §5 Graph functions declares this environment as the specialised contract through which ACTIVATION §4 lets a refinement carry earlier outputs | §11.8 |
-| #119-global-convergence-must-be-stable-under-zoom | conserved; "usually" kept | §11.9 |
-| #12-scenario-rule | conserved | §12 |
-| #13-installed-dev-rule | conserved | §13 |
-| #14-dogfooding-rule | conserved | §14 |
-| #15-release-boundary | conserved | §15 |
-| #16-failure-pattern | conserved; all fifteen patterns | §16 |
-| #17-invocation-rule | conserved; all fourteen steps and the three exclusions | §17 |
-| #18-cold-start-reading-order | conserved; "usually" kept | §18 |
-| #general-odd-product | conserved; nine steps with successor member names | §18 General ODD product |
-| #world-model-product | conserved; ten steps with successor member names | §18 World-model product |
-| #19-ramp-up-checklist | conserved; all fourteen questions | §19 |
-| #20-canonical-compression | conserved; stated to be a compression of this member under ACTIVATION §2 that owns no determination | §20 |
--- specification_methodology/v3/build_tenants/claude/standards/PROFILES.md
+++ specification_methodology/v3/build_tenants/common/standards/PROFILES.md
@@ -9,24 +9,21 @@
 ## 1. The boundary
 
 The core names no runtime, no carrier and no executor. Terms owned outside
-the core, by a profile, a realisation or an rc.2 member, never enter tier
-1 or 2 except in a disposition table: graph, edge, vector, ledger, event
+the core, by a profile or a realisation, never enter tier 1 or 2: graph, edge, vector, ledger, event
 log, worksite, HoG, Markov overlay, screen, entity cut, and the design
 profile's IACS and Prime. The traversal record and the functor kinds F_D,
 F_P and F_H are tier-1 calculus terms owned by AXIOMATIC_CALCULUS §5, and
-"module" is a generic term, as the predecessor's generic testing law uses
-it; neither is restricted here. A profile may bind a core mechanism to one of these;
+"module" is a generic term under [ASSURANCE](ASSURANCE.md); neither is
+restricted here. A profile may bind a core mechanism to one of these;
 the binding is declared in the profile with its direction, preserved
 meaning, narrowed scope and invalidation. In this member "binding" means
 that declared binding of a core mechanism; a Product's adoption binding is
 [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)'s,
 and a carrier binding to a typed contract is [UX §7](UX.md#7-carrier-binding)'s;
-the three are not interchanged. The declared-binding rule is new
-(P0 boundary, P1); its shape follows ODD's specialisations of F_P and F_H,
-which [ODD §5 Probabilistic compute](ODD.md#probabilistic-compute) owns in
-the graph-native context and carries as their provenance; the
-predecessor's section is rc.2
-[ODD probabilistic compute](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#probabilistic-compute).
+the three are not interchanged (P0 boundary, P1). A concrete application
+of the declared-binding rule is ODD's specialisation of F_P and F_H, which
+[ODD §5 Probabilistic compute](ODD.md#probabilistic-compute) owns in the
+graph-native context.
 
 Import rule. A profile imports the generic families of tiers 1 and 2 that
 its rules rest on, and owns only its own bindings: the terms and choices
@@ -43,7 +40,7 @@
 family's rules and choices keep their owners. A profile that refines
 another profile declares the refinement in its lead; the refined profile
 keeps its rules, and the refining profile owns only what it adds (P1, P6).
-The import rule is new in this corpus. Purpose and material relation:
+Purpose and material relation:
 each profile table cites the families it rests on without restating them,
 so no generic rule gains a second owner in a profile and no choice a
 profile adds is presented as following from the foundations (P6, P1).
@@ -54,14 +51,13 @@
 
 ## 2. Graph execution
 
-Graph execution is two tier-3 members, indexed here; each restates its
-predecessor in full in its own text and declares its bindings under §1
-(P0 boundary, P1):
+Graph execution is two tier-3 members, indexed here; each states its
+law in full and declares its bindings under §1 (P0 boundary, P1):
 
-| Member | Receives | Binds or adds |
-|---|---|---|
-| [ODD](ODD.md) | rc.2 ODD_METHOD, all 48 rows | the bounded step of FOUNDATIONS P0 to one vector or edge traversal and the graph-native F_P, F_D and F_H shorthands, with F_P and F_H as declared specialisations of SPEC_METHOD §5 ([§5 Probabilistic compute](ODD.md#probabilistic-compute)); the refinement of ACTIVATION §4 to graph functions, with the cumulative environment law of §11.8 declared as its specialised contract for carrying earlier outputs ([§5 Graph functions](ODD.md#graph-functions), [§11.8](ODD.md#118-cumulative-environment-law-is-mandatory)) |
-| [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md) | rc.2 TRAVERSAL_OCCURRENCE_PROFILE, all 26 rows, 25 conserved and 1 proposed superseded, pending the product owner | an optional closed model-family signature over one exact `a_c` basis of AXIOMATIC_CALCULUS for immutable occurrence histories over a mutable subject, with OP-001 to OP-007 |
+| Member | Binds or adds |
+|---|---|
+| [ODD](ODD.md) | the bounded step of FOUNDATIONS P0 to one vector or edge traversal and the graph-native F_P, F_D and F_H shorthands, with F_P and F_H as declared specialisations of SPEC_METHOD §5 ([§5 Probabilistic compute](ODD.md#probabilistic-compute)); the refinement of ACTIVATION §4 to graph functions, with the cumulative environment law of §11.8 declared as its specialised contract for carrying earlier outputs ([§5 Graph functions](ODD.md#graph-functions), [§11.8](ODD.md#118-cumulative-environment-law-is-mandatory)) |
+| [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md) | an optional closed model-family signature over one exact `a_c` basis of AXIOMATIC_CALCULUS for immutable occurrence histories over a mutable subject, with OP-001 to OP-007 |
 
 The ownership split of graph execution (runtime, product, service layers)
 is [ODD §10](ODD.md#10-what-an-odd-product-is); the worker's internal
@@ -132,22 +128,3 @@
 bind the responsibilities that configuration allocates under
 [ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation),
 not roles imported by spelling, as its lead declares (P1, P6).
-
-## 7. Source dispositions
-
-Each cell names where the rows of one rc.2 member receive their
-dispositions. Every row's disposition is one of the four values of
-[RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015); a
-row with none is unresolved, which blocks qualification of the claim it
-affects.
-
-| rc.2 member | Disposition |
-|---|---|
-| ODD_METHOD | conserved in full in ODD (all 48 rows; its §21), indexed in §2; the generic parts (bounded unit, refinement, loop structure) are generalised into ACTIVATION; the declared-binding rule of §1 is new |
-| TRAVERSAL_OCCURRENCE_PROFILE | 25 rows conserved and 1 proposed superseded, pending the product owner, disposed in TRAVERSAL_OCCURRENCE, Source dispositions; indexed in §2 |
-| baseline runtime bindings | disposed row by row in EXECUTIVE_BASELINE, with STDO_REFERENCE_FRAME_BASELINE; §6 is its index entry |
-| DESIGN_MODULE_METHOD | disposed row by row in DESIGN_MODULE, with 6A to 6C in ASSURANCE §14 to §16 and the core rule and non-goals in SPEC_METHOD §2; §3 is its index entry; the first-pass residual on the cost of the derivation chain is answered by DESIGN_MODULE §5 and §7 |
-| UX_METHOD | disposed row by row in UX; §4 is its index entry. The first-pass description of UX by reader and task obligations, operational projection and screen-level acceptance was candidate text with no source in UX_METHOD, so it is no predecessor claim; it is withdrawn |
-| WORLD_MODEL_METHOD | disposed row by row in WORLD_MODEL; §5 is its index entry; the generic identity and boundary law stays FOUNDATIONS §2 and P3 and IDENTITY, and the entity-cut law is WORLD_MODEL §9, bound to P3 by WORLD_MODEL's declared binding |
-| Authority compressions, schemas, templates | schemas and templates conserved under standards/schemas/ and standards/templates/; the ten compressions and the requirements template's bootstrap entrypoint have no disposition yet, so they are unresolved, pending the product owner's ruling on supersession by projected frames |
-| no rc.2 member | the import rule of §1 is new in this corpus and receives no predecessor claim |
```

</details>
