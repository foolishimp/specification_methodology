# Oracle: Expectations For A C3 Iteration 3 Candidate

Oracle-writing activation R0c. I wrote this from the common specification and the installed predecessor, before inspecting any candidate and without doing so. It is commentary only and accepts nothing.

## 1. Basis

Common specification at `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`, `specification_methodology/v3/specification/`, read with `git show`. SHA-256:

- PRODUCT.md `e859dfb6d84f3353ca7631e21bf3640b6e69e14848daba0e474c4a8e4c5cf9f1`
- INTENT.md `d668a54ddebd96ae22992b645cd720d993776450dfe2dfd58aa120aabc10329a`
- GOALS.md `82db6afb20a4203e86cd17f91b411f04c9e738d4e1f48b870b30ebb2ea93b84f`
- requirements/README.md `b04dad3be3fd6f4f2b9600a9ec2767681c8edd21cb6546bac34951229ab79fc8`
- requirements/A_C_DEPENDENCY.md `1095e3c5e63c25b12736de05121ae84cbee3095776cf924f90e4768d8d65c8b8`
- requirements/CAPABILITIES.md `26e2990fce28993f1a32abe7c10cff3b868f1bfd2cfd75bf2f23dfbfae7bbe8f`
- requirements/PRINCIPLES.md `009fca60d81e71586d9b3faf3f5cd932f902125fdfe8816c3d3b00cf15552fc7`
- conformance/README.md `f835e7b500101ee0b3d5ccc7a03a5f2bc03e861caa7f25a5498a14311ea79d7f`
- For structure only:
  - requirements/PREDECESSOR_CLAIMS.md `2b8e80c9623e746250b3c338d8afa08b6d17e033e658e4dc922965fa0b7f606a`. I used its header, rules, member table and declared totals. A few of its historical Claude-tenant cells were seen incidentally and not used.
  - REFERENCE_FRAME_BASIS.md `4e9344f3a5eafbe9e40623d545db25f2d3dd7d5ca1b9cd94536280d41a1d9fa2`.

The installed predecessor is `v2.5.1-rc.2`. Its manifest is `3d860ff4…2782`, which equals the pin. I read these standards:

- RELEASE_METHOD `582bc154…141c` (UP-015);
- REFERENCE_FRAME_METHOD `6e9148d7…67e7` (RF-012, Result Conjunction, Applicability);
- SPEC_METHOD `7f12d32e…8fb8a4` (UP-020);
- AXIOMATIC_CALCULUS `cbe2edb9…1f8d` (AC-007, AC-017, AC-018).

Each digest equals the inventory digest for that standard. I read nothing under `build_tenants/`, `.ai-workspace/comments/` or the tenant tickets.

Independence: a Claude-family activation wrote this oracle. A candidate may contain parts ported from the Claude tenant. Where the Independence rule makes it material, another nonauthor checks the expectations on those parts.

Keys. Files: PD = PRODUCT.md, RQ = requirements/README.md, ACD = A_C_DEPENDENCY.md, CAP = CAPABILITIES.md, PR = PRINCIPLES.md, CF = conformance/README.md, IN = INTENT.md, PC = PREDECESSOR_CLAIMS.md. Sections of PD: PD-FR = Foundational Reduction, with rN for pillar row N. Sections of RQ, followed by an item number: RQ-SD = Successor Disposition; RQ-SS = Standalone Successor; RQ-FR = Foundational Reduction; RQ-CS = Constraint Surfaces; RQ-BT = Bounded Transitions; RQ-BTB = Build-Tenant Binding; RQ-SO = Single Ownership; RQ-SRA = Single Result Algebra; RQ-CD = Categorical Demonstration. "crit N" is PD C3 acceptance criterion N, and "CF rN" is member-conformance row N.

Standing tags. [R] is the construction return (`candidate_ready`); at [R], marked pending supersessions and `unresolved` packaging rows are allowed. [M] is member acceptance. [C] is C3 closure. An [M] or [C] falsifier fails an [R] return only when that return claims the higher standing. E marks satisfying evidence and F marks a falsifier. Where an item has no E label, its opening statement is the satisfying evidence: the candidate's own text states and applies it at an owning locus.

## 2. Expectations

### (a) Pillars (PD#foundational-reduction; RQ reduction item 1)

A0 [R] (PD-FR; RQ-FR 1) For each contribution, the candidate names the deciding rules and consumers it governs. Premises, consequences, policies and implementation choices are kept separate. Finite resources alone supply no purpose, identity, authority or composition. F: the contribution appears only as a heading, a named calculus or a correspondence. F: a pillar is asserted to be an independent axiom without argument, or is derived from finite capacity alone.

A1 [R] (PD-FR r1) Specification and project structure. E: destination constraints; refinement from one WHAT to independent HOWs; separate owners for specification, design, work and commentary. F: commentary outranks the specification, or a realisation is treated as the WHAT.

A2 [R] (PD-FR r2; PR P3) World models, identity and Markov objects. E: boundaries, state and relations, each with evidence; sufficiency claimed separately. F: ordinary bounded modelling is said to establish a Markov property, or identity is conflated with content.

A3 [R] (PD-FR r3) Algebraic calculus. E: typed operations and laws, with each transformation stating what it preserves and when it applies. F: a transformation without either statement.

A4 [R] (PD-FR r4; RQ-FR 3) Functional design. E: contracts, invariants, and explicit failure and effect boundaries. Reuse keeps each domain's meaning and permissions. F: shared machinery transfers authority or evidence between domains.

A5 [R] (PD-FR r5; CF r6) Outcome-driven development. E: typed transitions with evaluation, continuation, recovery and termination. Operation kind, actor and mechanism are distinct. F: vocabulary only, or available only through the typed-graph profile.

A6 [R] (PD-FR r6) Information and interpretation. E: subject, representation and meaning are distinct, and each projection states what it preserves. F: structure is taken as meaning.

A7 [R] (PD-FR r7) Reference frames. E: task-sufficient acquisition under finite context and attention; bounded results; justified allocation. F: a frame without subject, authority or result.

A8 [R] (PD-FR r8; IN) Computational calculus and execution binding. E: operations, laws, effects and resource measures, bound to a human, machine or mixed environment, with the binding's satisfaction of those laws evidenced. It is distinct from the algebraic calculus (IN). F: either calculus is presented as the whole foundation, or the binding has no conformance duty.

A9 [R] (PD-FR r9; PR P6) Evidence, correction and authority. E: claims, observations and acceptance are distinct; correction is driven by counterexamples and traced to its cause; permission is distinct from capability. F: a passing check or review confers authority.

A10 [R] (PD-FR r10; PD responsibility note) Axiomatic calculus. E: a recoverable representation of constraints, dependencies, latitude and uncertainty that builds task surfaces. F: a_c is treated as a packaging check, or uncertainty is dropped.

### (b) Standalone successor (RQ#standalone-successor-requirement)

B1 [R] (RQ-SS 1; RQ preamble) Relation 1, material family. The specification defines a family of deciding contracts as "a group of related rules that decide outcomes", and a material family as "one whose outcomes matter to the product". For how this reading combines with the preamble's material determination, see Q1. E: the candidate states its grouping. For each material family it gives:

- the foundational premises;
- the consequences;
- the additional domain or policy choices, with their owners;
- the covered rules, the pillar contributions and the actual consumers bound to the argument.

F: a material deciding rule is in no family and has no exclusion reason. F: a material family lacks any of its three parts (premises, consequences, owned choices).

B2 [R] (RQ-SS 1; CF r2) Inherited rules. E: unchanged inherited deciding rules are covered, not only edited ones. F: edited-only coverage. F: a preamble or coarser grouping supplies a missing premise or policy.

B3 [R] (RQ-SS 1) Scope. F: a few-member demonstration is presented as a derivation of all members. F: file boundaries are given as the justification for a grouping.

B4 [R] (RQ-SS 2) Relation 2. E: the Spec Method and profiles apply the shared contracts in their deciding text at the entry points. F: a consumer decides by its own definition while citing the shared contract. F: a cross-reference is the only connection.

B5 [R] (RQ-SS 3) Relation 3. E: text owned by the candidate supplies every conserved determination. `stdo://` links are provenance only. F: a `conserved` locus is usable only through the predecessor.

B6 [R] (RQ-SS 4; RQ-FR 5) Relation 4, pass rule. E: for each claimed recurring determination:

- one shared law is used by the affected consumers;
- the removed determination, mechanism or reconciliation is named;
- the remaining distinctions are justified;
- permissions, obligations, failures and uncertainty are preserved.

F: reduction shown only by counts, diagrams, rewritten prose or a structural check. F: changed meaning without an accepted replacement.

B7 [R] (RQ-FR 5) Relation 4, deciding paths. E: each path is traced from a declared entry through the rules, bindings and acquired information to a permitted result. All materially affected entry and consumer paths are covered. Acquisition counts the material actually obtained, including dependencies, supplied context, repeated reads and boundaries. Grouped cases are justified. F: whole-corpus loading or file counts are used as cost. F: a claimed determination has no path.

B8 [R] (RQ-FR 5) Relation 4, baselines. E: two exact subjects:

- the predecessor at manifest `3d860ff4…`;
- the preceding candidate named in the admitted execution contract, or a record that none exists (the predecessor comparison is still required).

Tasks, inputs, authority and acquisition are comparable. F: an unnamed or floating baseline. F: one subject only. F: undisclosed differences in conditions.

B9 [R] (RQ-FR 5) Relation 4, discipline. E: dimensions and tradeoffs are declared before the comparison. Adverse changes are disclosed against both subjects. Each increase is justified, or the path is not claimed simpler. A supported elimination witness keeps its narrower standing even when the overall improvement is not established. F: dimensions are chosen post hoc. F: an unexplained increase beside a "simpler" verdict. F: one measure silently excuses another. F: a witness is inflated into an overall improvement, or a valid witness is discarded because the whole was not shown.

B10 [R/C] (RQ-FR close; PD Closure) Whole-candidate check. E [R]: complete accounting of shared owners and consumers across members, with member claims scoped to their cones. E [C]: an independent integrated assessment concludes reduction. F: the whole is inferred from members. F: two members decide one shared question differently.

B11 [R] (RQ-FR 6) Challenge cases (item 6). E: successful, refused and unresolved cases, including composition, failure preservation and recovery. Expectations are fixed independently before the trial, and limits are disclosed. F: author-written or post-hoc expectations. F: success-only cases.

B12 [R] (RQ-FR 3) Scope, force, triggers and exceptions are conserved (item 3). F: a conditional policy becomes unconditional in shared law. F: a reference loses a trigger or refers the work back to the consumer.

### (c) Constraint surfaces and a_c (RQ#constraint-surfaces-and-logic-compression; ACD)

C1 [R] (RQ-CS 2; ACD fixed theory) E: the candidate names its exact method subject (the candidate at a commit, including its own calculus statements). It separately names the calculus basis (rc.2 AXIOMATIC_CALCULUS `cbe2edb9…`) and the signature. F: only one of these is bound, or the subject floats. F: the successor calculus silently replaces the encoding basis.

C2 [R] (RQ-CS 2) E: premise, consequence, policy choice, observation and unresolved claim are distinguished. Shared premises are allowed. F: these are flattened. F: the candidate's law requires a tree-only encoding or an execution order. Using a tree encoding is not itself a defect.

C3 [R/C] (RQ-CS 3; ACD proof claims) Coverage. E: source-to-model dispositions cover every material owned determination with its dependencies, conditions, exceptions, choices and unresolved matters. Each residual keeps its source and acquisition. [R]: gaps are declared with scope. [C]: coverage is complete. F: a fragment is offered as the whole. F: coverage is counted by checker-accepted clauses.

C4 [R] (RQ-CS 3) E: each model element resolves to its current owning locus and basis. F: an element resolves to predecessor text or to a non-owning copy.

C5 [R] (RQ-CS 3) E: each residual or external predicate is marked as blocking its dependent work until the required premise is established. F: an unresolved premise or external predicate authorises work, or a missing premise yields a satisfied result.

C6 [R/M] (RQ-CS 5-6) Fidelity. E: independent permissible, prohibited and unresolved cases; a nonauthor review that reads the source first; approximations that state their adequacy relation and end-to-end bound. F: fidelity is claimed from a schema, a digest or a parse. F: "not required" becomes "prohibited", or a preference becomes an obligation.

C7 [R] (RQ-CS 6; ACD last) E: ordinary entry selects the current exact source, signature, program, maps and evidence boundary, with limits stated. Earlier models are labelled historical. F: an earlier model is reachable as current. F: the rc.2 STDO Representation, or tenant output presented as it, is used as the successor's interpretation.

C8 [R] (ACD relation, pins) No install is selected, so missing mechanical results are no defect. E: any claimed result binds the exact pins (tag `9bff233c…`, commit `9a9c4797…`, executable `5a2e0cb5…`, schema and output contract), a verified copy and a selected evaluation. F: an unverified run. F: "valid" read as fidelity, truth or acceptance.

C9 [R] (RQ-CS 4) E: projections carry inputs or acquisition routes, with the workspace as the basis for reacquisition. F: abstract rules stand in for observations or for a grant.

C10 [R] (RQ-CS 1) E: admissibility is constrained, not strategy. F: a single solution is imposed where several are permitted.

### (d) Single ownership and result algebra (RQ; PD#result-algebra)

D1 [R] (RQ-SO 1,3,7) One owning locus per determination. Other loci refer to it, or refine it with a mapping. F: two loci decide, or precedence replaces an owner.

D2 [R] (RQ-SO 2) Placement follows the responsibility table:

- Foundations own what holds for any method;
- the Spec Method owns what holds for this method;
- profiles own their bindings only;
- guides own their conventions;
- packaging owns formats and derives meaning.

F: a profile owns generic law. F: packaging defines a result meaning.

D3 [R] (RQ-SO 8) Generic law is usable without an optional profile. F: transition or recovery law exists only in the ODD or Traversal profile.

D4 [R] (RQ-SO 4) Frame copies name and match their owners. A derived view is no owner. F: a divergent "copy".

D5 [R] (RQ-SO 6) A ported part takes one owning locus. F: a ported clause coexists with a rival.

D6 [R] (RQ-SRA 1,6) The Foundations own one core algebra, unifying RF-012 and AC-007. Constraints, judgements, frames, stops, work steps and effects are stated in it or refine it. Conjunction and composition are defined once. F: a parallel outcome set, such as work variants, verdicts or refusals left unmapped. F: conjunction defined twice.

D7 [R] (RQ-SRA 2,4) Each refinement is stated at its owner. Each value, with its predicate and meaning conditions, maps to exactly one core value. The domain outcome travels with it, and missing conditions stay explicit. F: a value maps to zero or two core values. F: a bare "see core" where a map is owed.

D8 [R] (RQ-SRA 3) Standing never rises:

- failure never becomes satisfied;
- an undecidable result never becomes satisfied;
- "not performed" stays distinct from "cannot decide";
- an effect of unknown completion never becomes "no effect" or "completed".

F: any collapse of these distinctions.

D9 [R] (RQ-SRA 5) Availability, assessment and acceptance are separate. F: `candidate_ready` is read as fitness or acceptance.

D10 [R] (RQ-SRA close) A label that decides admission, compliance, closure or disposition returns through the core with its purpose stated. Assessment stays distinct from authority. F: a status field decides closure.

D11 [R] (RQ-SRA 7) A frame whose task returns a result carries the core algebra or its profile map. F: a result-returning frame carries neither.

### (e) Bounded transitions, recovery, acquisition (RQ#bounded-transitions-and-reference-frames; PD Limits)

E1 [R] (RQ-BT 1) A transition binds the current state, the destination constraints and the preservation obligations. A destination change follows its owner and proves nothing about the original destination. A stop keeps the outcome unresolved. F: completion by revising the destination.

E2 [R] (RQ-BT 2) Capacity pressure never licenses omission; refine the task, reassign it or stop. F: truncation to meet a budget.

E3 [R] (RQ-BT 3) Byte fit and attention adequacy are judged separately. F: fit is offered as adequacy.

E4 [R] (RQ-BT 4) Configuration is derived from operations, dependencies, capabilities and assurance. No role inventory or hierarchy is prescribed. Decomposition, communication, authority and evaluation dependency stay distinct. Names grant nothing, and adequacy is not optimality. F: Executive, Writer and Reviewer become a required role inventory. F: a peer configuration rejected by its label.

E5 [R] (RQ-BT 5) Recovery. E: the workspace is the truth surface and context is disposable. Resumption starts from the current state and keeps valid work. Contrary evidence reopens claims without silent rebinding. Unknown effects are resolved before dependent action. There is no universal reset or replay. F: a summary overrides the workspace. F: discarding context is treated as a reset.

E6 [R] (RQ-BT 5) Reuse checks changes to source, input, task, actor conditions and dependencies. F: reuse on unchanged hashes alone.

E7 [R] (PD Limits) Acquisition. E: declared routes. Supplied bytes, cumulative acquired bytes (with repeats) and the active retained bound are reported separately, with boundaries. F: a single "context" number, or unmeasured platform context. F: 30 KB plus 200 KB judged to fit 40 KB.

E8 [R] (RQ-BT close) A result binds its producer, subject, basis and evidence. F: plan membership authenticates a misbound judgement.

### (f) Build-tenant binding (RQ#build-tenant-binding-requirement; PD#build-tenant-binding, #source-project-construction)

F1 [R] (RQ-BTB 1-2) The candidate's Spec Method states the chain from the requirements calculus to a declared computational calculus to a concrete stack, human process or mix. F: the chain is absent, profile-only or software-only.

F2 [R] (RQ-BTB 2; CF r43) Author, actor and operation kind are distinct, and required human decisions stay human. F: automation replaces a required human decision, or independent assessments are merged.

F3 [R] (RQ-BTB 3) The binding names the operations, laws, effects, resource measures and assumptions material to conformance, with units and boundaries. F: obligations rely on effects or resources the binding does not cover.

F4 [R] (RQ-BTB 5-6) A calculus is reusable across environments. a_c selects no executor and proves no execution conformance. F: a new calculus per stack. F: a structural check offered as execution conformance.

F5 [R] (PD Source Project Construction) The tenant applies the binding to its own authoring process in its design and work records under the installed builder. The candidate's rule binds future consumers only. F: no such record. F: the candidate's rule claimed to govern its own construction.

### (g) Categorical demonstration (RQ#categorical-demonstration-standard; PD#categorical-construction)

G1 [R] (RQ-CD intro) The candidate carries items 1–5 as law for categorical claims (Q8). F: categorical vocabulary with no governing standard.

G2 [R] (RQ-CD 1,4) Each category, functor, equivalence or join gives objects, arrows, arrow equality, identities and associative composition. Functor laws are shown first. Otherwise the claim is labelled a hypothesis. F: a "functor" with no preservation shown.

G3 [R] (RQ-CD 2) Each layer states and discharges what it preserves. An approximate step gives its adequacy relation and an end-to-end bound. F: per-step tolerances are treated as composing.

G4 [R] (RQ-CD 3) A step is admissible only under laws declared for its subject; without them, only universally valid steps. F: an unlicensed rewrite.

G5 [R] (RQ-CD 5) Each claim names its evidence class. Conformance, equivalence and functorial preservation stay distinct. F: a structural check cited as proof.

G6 [R] (PD Categorical Construction; GOALS) The capability is unselected and the steel thread NOT_SELECTED. The sheaf account, grade algebra and second-domain generality are unresolved. The five layers are a reference design. F: any of these is presented as law, or a worked join as accepted.

### (h) Frontier and dispositions (PD Outcome, Frontier, #construction-authority; RQ#successor-disposition-requirement; PC)

H1 [R] (PC rules; PD Outcome) E: all 635 section rows (16 bodies), the 36 non-body members and the 19 auxiliary members are accounted for at PC granularity, with splits as child rows. F: a missing row, or a parent row standing for its children.

H2 [R/C] (RQ-SD; PD packaging row) Each row has exactly one UP-015 value. `unresolved` blocks qualification. At [R] it is tolerated for packaging rows and for rows outside the cones the return claims are ready, never inside a cone that is offered for acceptance. "reframed" is a note. F: two values on a row. F: a route used as a disposition. F: a row unresolved at [C].

H3 [R] (PD crit 1) Each `conserved` or `superseded` row names its owner and its necessary bindings, each resolving to candidate text. F: an unresolving locus, or a missing binding.

H4 [R] (RQ-SD; PD crit 3) A supersession names the claim, the replacement determination and its loci, and is marked proposed or accepted. An accepted one cites the ticket decision. F: only the old section is named. F: a proposed replacement is shown as accepted. F: a hash is cited as acceptance.

H5 [M] (PD Construction Authority) Who accepts a replacement, and when:

- the product owner accepts any replacement that changes predecessor meaning;
- the common pen records the decision and exact relations in the tenant ticket;
- each dependent `superseded` row cites that record before member acceptance;
- one decision may cover a named set.

None of these substitutes: a construction grant, general direction, a Reviewer finding, or the Executive's acceptance of the member. F: an uncited supersession in an accepted member. F: a review cited as the acceptance.

H6 [R] (RQ-SD; RQ-FR 3) A changed scope, force, trigger or exception makes a supersession. Relocation that preserves meaning stays conserved. F: a `conserved` heading with a new obligation.

H7 [R] (RQ-SD; PD crit 3) A removal names the owner's decision and reason. A "not applicable" row gives a bounded reason. F: a removal decided by a Writer or the Executive. F: an unbounded "n/a".

H8 [R] (PD Frontier) The frozen frontier holds proposals and evidence against its ticket subject. It cites the ticket and confers no acceptance. F: acceptance asserted without a ticket record.

H9 [R] (PD Frontier) The member list and the predecessor-to-successor member map are declared, and the map is labelled as navigation. F: the map is used as conservation evidence.

H10 [R] (PD Cross-Synthesis) A ported part is named in one cone, with its source (the peer at `31f28f90…`), its receiving owner and its disposition. F: no provenance, another commit, or a second owner.

H11 [R] (PD Frontier) U0 includes the open required evaluations, and excluded items stay open. F: a bounded view treated as disposal.

### (i) Criteria 1–6, whole check, actual use, independence (PD#c3-construction-contract)

I1 [R/M] (PD crit 1) Criterion 1 is H1–H3, with the same evidence and falsifiers.

I2 [R/M] (PD crit 2) Criterion 2. E [R]: the conserved meaning is present in full. E [M]: a nonauthor source comparison confirms it. F: a link, a label match or a partial paraphrase.

I3 [M] (PD crit 3) Criterion 3 is H4–H7, with the same evidence and falsifiers.

I4 [R/M] (PD crit 4, Audiences) Criterion 4.

- E: one frame per selected task. Each frame fits its limits, is sufficient, excludes irrelevant material and keeps its routes. It is built from a_c or a declared equivalent. Copies match their owners and views are faithful.
- E: a fresh actor with no unselected context and no auto-loaded repository instructions in any directory. It discloses its instructions and acquisitions and works standalone, with no predecessor rule supplying content. Expectations are independent and fixed in advance. The record names the exact frame, subject, task, instructions, acquired material and expectations.
- F: instructions leak the answer, or a CLAUDE.md or AGENTS.md file auto-loads.
- F: a trial in which predecessor rules supplied missing successor content is counted as standalone criterion-4 evidence. A trial that uses predecessor rules to perform construction is builder-process evidence, not a defect.
- F: an old trial is reused for a changed frame, or a corrected run is offered as the test of its own correction.

I5 [R/C] (PD Audiences and tasks) E: the selected tasks among the six listed each have a frame. The fresh-actor audience and the building actors start on frames. A human method owner can follow links through the candidate's own text. F: a selected task has no frame. F: the human route depends on the predecessor to supply successor content.

I6 [R/M] (PD crit 5) Criterion 5. E: the applicable rows of (j) hold under a source-first logical review that states coverage, expectations and open obligations. F: structural validity alone.

I7 [R/M] (PD crit 6) Criterion 6 is B6–B12 within the cone. In addition, every added obligation names its purpose and material relation, and work carriers and process change only where needed. F: an added obligation or process step with no stated purpose (CF r41).

I8 [M] (PD Construction Authority; RF Result Conjunction) Conjunction. E: one overall result plus six criterion judgments in the installed RF family, conjoined under the installed Result Conjunction. The Executive binds applicability; the Reviewer verifies it. A false condition excludes only its own obligation, with reason and source. Unknown applicability stays unresolved. F: acceptance with a missing, stale or falsified criterion. F: "N/A" without established absence.

I9 [M] (PD Independence) Independence. E: the Reviewer is a nonauthor, including of material repair wording. A different model family is the default; a same-family Reviewer is a declared exception with its reason and limits. Material facts are disclosed. F: the author reviews in a fresh context. F: a repair's contributor supplies acceptance evidence for it.

I10 [C] (PD Closure) E: every row is disposed and every member accepted. Independent assessment establishes integrated reduction, complete coverage and fidelity, and frame-use evidence. Changed dependencies reopen conclusions. The owner accepts. F: closure from member results, or with any required obligation unresolved.

I11 [R] (PD Limits) E: every activation declares its context bytes, wall time, spend and boundaries, reports them afterwards and names any unknown portions. F: a measure missing, or limits set post hoc.

I12 [R] (PD Outcome, Executive loop 4) E: the return covers all four Outcome bullets as a closed evaluation with its variant and exact coordinates, filed in the tenant's `qualification/`. F: filed in the ticket, or with no exact commit.

### (j) Conformance rows (CF), in table order

The citation for Jn is CF member-conformance row n. J53–J55 cite rows 1–3 of CF Construction And Integrated Closure. Rows are applied under criterion 5 [R/M]. J53–J55 are evaluated at their construction or closure decisions [M/C].

Member conformance:

- J1 Derivation or independence. E: premises shown, independence argued. F: asserted.
- J2 Inherited rules omitted. See B2.
- J3 Intro beside rival rules. E: consumers use the shared law. F: the rival still decides.
- J4 Shorter, same reconciliations. E: path comparison against both baselines. F: size as witness.
- J5 Unified rule with an exception. E: shared use; the exception kept and owned. F: the exception lost.
- J6 ODD as vocabulary. See A5.
- J7 One law, several clauses. E: each obligation evaluated. F: a bare link.
- J8 Exception deleted. E: a valid disposition or owner removal. F: silent deletion.
- J9 Rule replaced by a reference. E: trigger, force, adoption conditions and exceptions kept, with no circular referral. F: a lost trigger.
- J10 Generic rule in a profile. See D3.
- J11 Helper made public. E: the needed distinction is named. F: an owner by naming.
- J12 Markov by small interface. E: evidence, or left unresolved. F: unsupported.
- J13 a_c omits a condition, schema passes. E: fidelity fails. F: the pass is cited.
- J14 Fragment as whole. See C3.
- J15 Frame uses a projection. E: fidelity and sufficiency judged against the owner. F: encoding called a defect, or a changed obligation passes.
- J16 Unresolved read as free. E: stop, acquire or refine. F: permission granted.
- J17 Several solutions. E: all admitted. F: one imposed.
- J18 "Not required" read as "prohibited". E: a defect. F: excused by a digest.
- J19 Earlier model marked current. See C7.
- J20 Information versus representation. E: shape is not meaning. F: fidelity from structure.
- J21 Same identity, new content. E: state rechecked. F: reuse by identity.
- J22 Typed mismatch. E: made explicit. F: a join by shape.
- J23 A failed, B uncovered. E: A survives, B unresolved. F: masked or passed.
- J24 Misbound planned judgement. E: rejected. F: authenticated by plan membership.
- J25 Context too large for one actor. E: narrow, hand off or stop. F: an obligation dropped.
- J26 Fit with obscuring material. E: dependency kept, irrelevance excluded. F: size as adequacy.
- J27 Changed frame, or a leaked answer. E: narrower evidence. F: the old trial reused.
- J28 Author in a fresh context. E: not independent. F: accepted.
- J29 Items omitted from view. E: they stay open. F: disposed silently.
- J30 Discovery, or destination revised. E: the frontier may grow; a revision needs its owner. F: progress by count.
- J31 Direct authorised task. E: permitted, subject to any separately required assessment. F: an Executive mandated, or a required assessment skipped.
- J32 No central Executive. E: judged on merits. F: rejected by topology.
- J33 Redistribution under uncertain effects. E: obligations, effect resolution, authority and independence kept. F: an exemption.
- J34 "Optimal". E: objectives, constraints, scope and evidence. F: by familiarity.
- J35 Compact result hides a blocker. E: the coordinator acquires it. F: assumed favourable.
- J36 Dependency change. E: applicability rechecked. F: hash-only reuse.
- J37 Rules without context or authority. E: the frame binds subject, evidence, capability and effects. F: rules alone.
- J38 Stale summary. E: reacquire and correct. F: the summary wins.
- J39 Interrupted work. E: recover from the workspace. F: progress erased or an assessment invented.
- J40 Parse or map succeeds. E: the claim stays mechanical. F: semantic acceptance.
- J41 Process as law. E: purpose and relation given. F: unsupported overhead.
- J42 Software, human or mixed. E: calculus, binding and evidence for each. F: judged by executor kind.
- J43 Merged assessments or an automated decision. E: fails. F: passes on equal output.
- J44 One calculus, two environments, or one actor with several operation kinds. E: laws hold per binding. F: duplicate calculi, or identity grants authority.
- J45 a_c of a human process validates. E: no executor and no execution conformance follow. F: claimed.
- J46 Two loci decide. See D1.
- J47 Own result values. See D7–D8.
- J48 Label decides admission. See D10.
- J49 Changed heading, or old-section-only supersession. See H4, H6.
- J50 Frame returns a result. See D11.
- J51 Functor or join claimed. See G2.
- J52 Rewrite or refinement. See G3–G4.

Construction and integrated closure:

- J53 Local passes, cross-member contradiction. E: caught by the integrated assessment. F: closure from members.
- J54 Clear replacement, no owner decision. E: waits for the ticket record. F: review or grant treated as acceptance.
- J55 Five criteria satisfied, sixth missing, stale or falsified. E: withheld, components kept. F: an overall favourable verdict.

## 3. Negative expectations

A conforming candidate does not:

- N1 conserve by link, label or partial paraphrase, or depend on the predecessor remaining in force;
- N2 claim member, checkpoint, supersession or removal acceptance from its frontier, a return, the Executive's view or a review;
- N3 define outcomes outside the core, or raise standing by mapping;
- N4 present tenant a_c as the released STDO Representation, or claim unverified mechanical results;
- N5 change the 2.* line, `stack_release.json`, the cohort, identities or the common specification, or write outside its territory;
- N6 make categorical, Markov or optimality claims without their demonstration;
- N7 make a role inventory, a hierarchy, a universal budget, ticket-first work for all users or a fixed actor count into law (CAP; RQ frames item 4);
- N8 make Hello World, Data Mapper, sum-and-histogram specifics, the five layers, or ABG or HoG behaviour into method rules or product parts;
- N9 reduce by deleting obligations or by making conditional policy unconditional;
- N10 treat historical C1 or C2 verdicts, inventory columns or old trials as current standing;
- N11 add an obligation or a process step without its purpose;
- N12 let its own rule replace the installed builder for its own construction.

## 4. Ambiguities and readings

Q1 Material family. Relation 1 says "outcomes matter to the product"; the preamble says "affects meaning, permitted work or acceptance". Reading: a family is material if any of its determinations is. Every material deciding rule falls in some family or has a reasoned exclusion.

Q2 Preceding candidate. Item 5 binds "the preceding candidate named in that tenant's admitted execution contract", and several commits are plausible. Reading: the reviewer checks against the contract. A mismatch falsifies.

Q3 Core algebra versus RF-012. RF-012 lacks explicit values for "not performed" and "effect completion unknown". RQ item 3 requires both distinctions. Reading: the successor core may differ but must express both. A changed meaning of an RF-012 or AC-007 claim is a supersession needing owner acceptance; the common mandate to unify accepts no particular replacement. The builder's results stay in the installed family.

Q4 "Each selected task". Neither the selector nor the tasks required at closure are named. Reading: the execution contract selects them. Any of the six tasks left unselected across the whole candidate is uncovered scope, not a pass.

Q5 Criterion 6 locally versus wholly. Reading: a local claim may be satisfied while the whole remains open. The whole is decided only at [C].

Q6 Packaging rows may stay `unresolved` until closure, while criterion 1 requires one disposition per cone row. Reading: a member whose cone includes an unresolved packaging row cannot be accepted.

Q7 Standalone use versus the encoding basis. Construction encodes against rc.2, but the successor must stand without it. Reading: rc.2 is the lawful construction basis. The released basis and its acquisition are an open owner decision that precedes dependent acceptance, and the candidate does not claim them settled.

Q8 The capability is unselected, yet the standard governs "a categorical claim about the method, or a construction made with it". Reading: the candidate carries the standard. A missing capability contract or worked join is no defect at iteration 3.

Q9 Open owner decisions block per-member `accept` until review assignment and ported-part review are decided. Reading: claimed member acceptance overclaims unless the ticket records both decisions.

Q10 Conservation versus supersession. Reading: any change of scope, force, trigger, exception or permitted work is a supersession. "Reframed" covers wording and location only.

Q11 "The pillars determine the shared laws" sits against PD's statement that a pillar is no derivation claim. Reading: the pillars fix what the shared laws must carry. No deduction from them is required.

Q12 Frames are "generated from a_c … or by an equivalent the tenant declares". Reading: hand assembly is lawful when declared as the equivalent, provided its views are faithful.
