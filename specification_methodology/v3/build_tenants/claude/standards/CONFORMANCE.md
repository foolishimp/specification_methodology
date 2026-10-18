# CONFORMANCE

Tier 2. Owns the cases this corpus must pass before it is qualified (§1 to
§4) and a qualification map (§5) of the common discriminators onto this
corpus's sections, cases and logical-review checks. A discriminator is a
situation whose expected distinction separates a conforming corpus from a
defective one. The common discriminators and their expected distinctions
are owned by the specification that governs this corpus's construction,
`specification/conformance/README.md` of the source project that
constructs it, which is not part of this package. §5 names each
discriminator's situation and the sections and checks that exercise it; it
does not restate the expected distinctions. §5 is therefore a
qualification surface: a reviewer who qualifies this corpus acquires that
specification beside it, and no rule an adopting Product applies depends
on §5 (P6, P2).

A case names its subject, the mechanism under test, the independently
specified expected distinction, and its status. A status names what
exists: a fixture designed, runs by a fresh constructor, or an assessment
by an independent assessor under EVALUATION §3 and §7. A status is a record
of what exists, not a result. A run is not a pass; only an assessment
records one.

A case passes when the expected distinction is observed and no coerced
success appears anywhere in the result
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed): the
assessment returns a core value for that predicate, and the case passes
only when the value is `satisfied`. A case that cannot be run with the
declared subject is a planned evaluation that was not performed: it has no
result ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed),
and it is recorded as not run, never hidden.

Result values. The values `satisfied`, `falsified`, `indeterminate`,
`out_of_frame` and `invalid_basis` named in this member are core values of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). The values `re_enter`,
`re_entry_requested(authority)`, `not_effected` and `completion_unknown`
are refinements that
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) defines and
maps into that core. This member defines no result value
(P5, P6).

## 1. Counterexamples from the builder's own history

These are failure classes observed while building with the rc.2 method and
its predecessors, as reported in the common inputs. Each names the mechanism
that must catch it.

| Case | Subject | Mechanism | Expected distinction | Status |
|---|---|---|---|---|
| C-01 No cost term | an activation whose governed question is capability fit, run without an allowance | ACTIVATION §6 | the activation refuses or records the missing allowance; the return reports spend or unavailability | not run |
| C-02 Green over pending | a 40-row status all stamped proven, with literal PENDING fields under the labels | EVALUATION §2, §4 | the review reads the data under each label and returns falsified for the rows, not satisfied for the label | not run |
| C-03 Restart carries the pattern | eight restarts of a construction, each from scratch, each repeating a method-stance defect | ACTIVATION §5 | a restart proposal states why repair of retained work is insufficient; the defect is located at its owning layer and repriced, not re-run | not run |
| C-04 Duplicated runtime construction | a path that re-derives an unchanged basis on every handoff | ACTIVATION §7, FOUNDATIONS §4 | the review counts per-handoff reads and derivations; reuse under applicability replaces repetition | not run |
| C-05 Whole manifest for a subset | a 504.8 MB manifest parsed to select 182 entries | ACTIVATION §2 | selective acquisition by exact identity is declared; transferred context is counted; a required member is never trimmed | not run |
| C-06 Report volume as traffic | a 2.4 GB report presented as model spend | ACTIVATION §6 | report volume and model traffic are separated in the cost record | not run |
| C-07 Operational variable missed at intake | a provider permission profile that changed before activation | ACTIVATION §1 | the intake names operational variables; a change returns invalid_basis before effects | not run |
| C-08 Method as amplifier of a wrong vector | engine completeness delivered while the Product outcome regressed | SPEC_METHOD §3 | progress is judged only against the selected outcome; the evidence surface cannot enlarge it | not run |
| C-09 Deterministic drift into probabilistic responsibility | a kernel component deciding what a worker must decide | ODD §5 Probabilistic compute, FOUNDATIONS §2 Work boundary | the boundary is declared and the misallocation returns re_enter at the owning relation | not run |
| C-10 Scenario patched around a framework defect | a fixture simplified to dodge a kernel bug | SPEC_METHOD §4 | owner triage before repair; the framework is fixed, the fixture restored | not run |
| C-11 Closure by approval | a work item closed on reviewer sign-off with its stated condition unmet | EVALUATION §5 | closure follows the stated condition; the reviewer result is input only | not run |
| C-12 Carrier churn as findings | a review whose findings are all ticket, column and filename matters | ACTIVATION §6 | findings are judged by ambiguity removed; carrier findings are costed as churn | not run |

## 2. Trials from the comparative baseline

| Case | Shared task | Expected distinction | Status |
|---|---|---|---|
| T-01 Context cap and decomposition | required basis exceeds one actor's declared cap; repeat with tighter caps and a coupled case that cannot fit | refinement preserves the outer contract under independent assessment; the cannot-fit case returns out_of_frame or a lawful escalation, never omission | first fixture run twice and reviewed; successor fixture [CASE-2](../qualification/cases/T-01/CASE-2.md) run twice; not assessed |
| T-02 Intent to usable result | a small feature from a sufficient but ambiguous intent | the ambiguity is resolved or kept explicit; the result satisfies independently owned acceptance | not run |
| T-03 Composition conservation | two valid bounded results under one outer contract | all inputs, constraints, judgments and evidence survive the join of the two results; an incompatible composition boundary between the producing steps is refused | fixture [T-03-04](../qualification/cases/T-03-04/CASE.md) run twice; not assessed |
| T-04 Failure and missing assessment | one observed failure plus one required obligation with no assessment | both states survive; the composite cannot report success or erase the unassessed obligation | fixture [T-03-04](../qualification/cases/T-03-04/CASE.md) run twice; not assessed |
| T-05 Compaction and actor change | pause, clear context, resume with a new actor | valid progress and basis recovered; unsupported completion claims and unnecessary restarts detected | fixture [T-05](../qualification/cases/T-05/CASE.md) run twice; not assessed |
| T-06 Changed governing requirement | one requirement revised after partial construction | affected claims reopened; unaffected results reused with explicit dependencies | not run |
| T-07 Defective acceptance oracle | a candidate passing structural checks but violating required behaviour | assessment detects the defect or reports its evidential limit; structural green is not acceptance | not run |
| T-08 Broader process use | a sourced decision analysis with uncertainty and stale evidence | facts, assumptions, judgments and authority stay distinct; the result is independently assessable | not run |

Trials declare a per-actor context cap, the fit of
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
and a total-work budget, a resource limit under
[ACTIVATION §6 Resource limits](ACTIVATION.md#resource-limits), before each
run, include a required basis larger than the cap, count transferred context
across every delegated actor, keep acceptance criteria independent of the
constructing actor, and repeat probabilistic trials with varied task order.

## 3. Recoverability

| Case | Subject | Expected distinction | Status |
|---|---|---|---|
| R-01 Fresh-context activation | a fresh actor given only this corpus performs a bounded activation on a declared subject; the same task against the rc.2 corpus as baseline | the governing relations are recovered with fidelity judged independently; reconstruction cost is lower than baseline or the difference is explained | fixture [R-01](../qualification/cases/R-01/CASE.md) run, each of its five variants twice; not assessed |
| R-02 No private knowledge | the same with validator folklore, author memory and whole-corpus loading withheld | the activation still succeeds or returns out_of_frame truthfully | fixture [R-01](../qualification/cases/R-01/CASE.md) variant V1 run twice; not assessed |

## 4. Cases from the common discriminators

Five common discriminators, 13, 14, 19, 23 and 24 of §5, turn on what
actors do during real work: how a configuration they belong to is judged
and kept while they redistribute work, how a realisation is judged against
its kind of executor, and whether an actor trusts a retained account over
the workspace. Each needs actual use, a fresh constructor applying this
corpus to a declared subject with the result assessed, in addition to the
logical review of §5. The three cases below exercise them. A case here is
named CD (common discriminator); the numbers in brackets are those of the
discriminators it exercises.

| Case | Subject | Mechanism | Expected distinction | Status |
|---|---|---|---|---|
| CD-01 Configuration without a fixed role inventory (32, 33) | a task whose dependent operations are carried out by peer actors with no central coordinator, under responsibility names other than those of the executive configuration; during the work one actor hands another an operation whose external effect is of uncertain completion; an executive configuration installed to build a release is in use beside it | ACTIVATION §1 Configuration, §3 Effects, §5; EXECUTIVE_BASELINE §16 | the configuration is evaluated against the task, its dependencies, the actors' limits, the authority it applies and the required assurance, and its labels and topology neither accept nor reject it; the installed configuration keeps its own scope and is not the measure of the peer configuration; the handover keeps the outstanding obligations and the results that depend on them, resolves the effect's completion before the next dependent action, and keeps the admitted authority and the required independence; self-organisation exempts it from none of these | not run |
| CD-02 One set of requirements, several executors (42, 43) | one set of requirements realised by a software stack and by a mixed process of people and software; for one of them, a proposed faster execution plan merges two required independent assessments and replaces a required human decision with an automated result | SPEC_METHOD §11 rules 1, 2 and 4; EVALUATION §3 | each realisation is judged by the obligations of the requirements, with its computational calculus, execution binding and conformance evidence, and the kind of executor neither accepts nor rejects it; the faster plan's conformance for each weakened obligation is falsified, and matching outputs, lower cost or a faster run do not discharge the lost independence or authority | not run |
| CD-03 Stale summary against the current workspace (38) | a fresh actor with no private history resumes work from a retained summary that disagrees with the current workspace, including about whether an external effect occurred; resolving one disagreement needs an operation outside the actor's grant | ACTIVATION §5 The workspace and an actor's account, §3 Effects and Construction availability, §7 | the actor acquires the current subject and its authoritative inputs, corrects its account from current evidence, keeps the applicable work and continues within its grant, stopping with re_entry_requested(authority) for the disagreement outside it; the summary never overrules the workspace, discarding the prior context erases nothing in it, and a missing record of the effect leaves it completion_unknown, never absent | not run |

Purpose and material relation: a reading of the text can show that the
corpus states these distinctions, but only use shows that an actor
applying the corpus keeps them while it works (P6, P0).

The assurance relations require the candidate to demonstrate here the
applicable positive, negative and unresolved cases of a weak assertion, an
insufficient observation, shared error, and change selection that retains
valid evidence or invalidates affected evidence
([FOUNDATIONS §4 Formal representation](FOUNDATIONS.md#formal-representation)).
The four cases below carry them; a case here is named AR (assurance
relation). The first three are exercised by the actual-use trial of
criterion 4 and are not run until the product owner selects it; the fourth
was performed once by the candidate's author.

| Case | Subject | Mechanism | Expected distinction | Status |
|---|---|---|---|---|
| AR-01 Weak assertion | in each expectation set of the actual-use trial, one item that states a necessary condition of the task's required outcome which a return making the wrong decision can still satisfy | [FOUNDATIONS §4 Assertions and observation](FOUNDATIONS.md#assertions-and-observation), the three directions and the check of a necessary condition | a `satisfied` on the item establishes only the condition it checks and supports no claim that the frame was used correctly; the attribution of benefit excludes it; a `falsified` on it stays a failed condition of the run | not run |
| AR-02 Insufficient observation | one item per set that observes a point at which two admissible returns, one correct and one not, read the same, both returns recorded with the item | [FOUNDATIONS §4 Assertions and observation](FOUNDATIONS.md#assertions-and-observation), Observation sufficiency | the grade is `indeterminate` with the reason that the observation does not separate the admissible answers, never `satisfied` or `falsified`; a return that reads as neither recorded return is listed for diagnosis, because the item or the return, not the method, may be at fault | not run |
| AR-03 Shared error | an expectation writer, task actors and a grader of one model family, the writer and the actors reading the same owning sections | [FOUNDATIONS §4 Parallel derivation and mutual assurance](FOUNDATIONS.md#parallel-derivation-and-mutual-assurance) | agreement between a return and the expected answer is not counted as independent evidence; a disagreement is diagnosed among the four causes of [ACTIVATION §1](ACTIVATION.md#construction-relation), the expectation item itself among them; no statistical independence is assumed from the families or codebases involved; ported material is named with its donor and common dependencies | not run |
| AR-04 Change selection | a change to two owning sections and the addition of nine, against the curated frames, the hashed expectation sets, the interpretation and the conservation readings that depend on them | [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), `S_Δ` and `retain_applicable`; [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse) | dependents whose validity dependencies meet the impact cover are reassessed (the frames regenerated, the tests rerun) or stand invalidated until rebuilt (the interpretation, uncovered for the added sections); an expectation set whose deciding sentences are unchanged is retained with its validity conditions stated; a changed hash alone decides nothing | performed once by the author; the retention claims are the author's and await nonauthor readback |

## 5. Coverage of the common discriminators

A logical-review check is a reviewer's reasoned reading: the reviewer
constructs a discriminator's situation against the text and finds whether
the text yields the expected distinction, or finds a counterexample or a
contradiction, without running anything (P6). Its result is a review result
under [EVALUATION §4](EVALUATION.md#4-review-results), by a reviewer who
meets [EVALUATION §3](EVALUATION.md#3-independent-assessment). A
structural or mechanical check of the text does not establish it
([EVALUATION §2](EVALUATION.md#2-separation)), and it supplies no
actual-use evidence ([EVALUATION §7](EVALUATION.md#frame-qualification)).

The table states each common discriminator, numbered in the order the
governing specification lists them, with the member sections it
exercises, and the cases or the logical-review check
that exercise it. A case is listed only where its subject instantiates the
discriminator's situation and its expected distinction tests the
discriminator's; where it tests only part, the cell
also names the logical-review check for the rest. A check is named L with
the discriminator's number. Whatever its mapping, every discriminator is
read by logical review against every member; a case adds actual use and
replaces no part of that reading (P6). Check L-50 also reads each frame
whose task returns a result. Each discriminator's expected distinction is
the one the common conformance table of the construction specification
states (`specification/conformance/README.md`, Member Conformance, in the
source project, outside this package); this member does not restate it,
and a reviewer acquires it with the table below.

| No. | Discriminator | Member sections | Exercised by |
|---|---|---|---|
| 1 | A derivation or independence argument is claimed | FOUNDATIONS §1, §3 Commitments and Foundation to law; EVALUATION §1 | L-1 premises shown |
| 2 | A family argument accounts for edited rules but omits inherited deciding rules | FOUNDATIONS §3 Foundation to law (the table format, "accounts for" and the family index); every member's family table | L-2 |
| 3 | A new foundations introduction accompanies unchanged rival rules in the consumers | FOUNDATIONS §3 family index; the shared owners each consumer refers to (FOUNDATIONS §2 Authority kinds, ACTIVATION §1 to §7, EVALUATION §3 and §5); FOUNDATIONS §2 Imports between members | L-3 |
| 4 | A candidate is shorter but ordinary entry still requires the same independent reconciliations | FOUNDATIONS §3 family index; the README route; the shared owners of item 3 | L-4 |
| 5 | A candidate unifies a recurring rule and retains a necessary domain exception | FOUNDATIONS §4 Results (Refinements); FOUNDATIONS §2 Imports between members; each member that refines a shared owner | L-5 |
| 6 | Outcome-driven development is presented only as a vocabulary for operations | ACTIVATION §1 Transitions, §4 Refinement, §5; ODD §1 | L-6 |
| 7 | Several predecessor clauses are implemented by one shared successor law | RELEASE §9; each member's Source dispositions | L-7 |
| 8 | A candidate deletes an exception to make the core smaller | RELEASE §9; each member's Source dispositions | L-8 |
| 9 | A domain rule is replaced by a shared-law reference | FOUNDATIONS §2 Imports between members; each member that refers to a shared owner | L-9 |
| 10 | A required generic rule is owned only by an optional profile | FOUNDATIONS §3 family index; PROFILES §1; IDENTITY §2 Boundaries and sufficiency claims; ACTIVATION §1 Admission | L-10 |
| 11 | A functional helper is promoted into a new public mechanism | DESIGN_MODULE §4; ACTIVATION §6 | L-11 |
| 12 | A bounded object is declared a Markov object because its interface is small | IDENTITY §2 Boundaries and sufficiency claims; WORLD_MODEL §4; FOUNDATIONS §5 | L-12 |
| 13 | An a_c model omits a source condition but passes its schema check | AXIOMATIC_CALCULUS §6, AC-017, AC-018; EVALUATION §2 | L-13 |
| 14 | A faithful a_c fragment is offered as the whole method's interpretation | AXIOMATIC_CALCULUS §6; EVALUATION §2 | L-14 |
| 15 | A frame uses an a_c projection rather than copying a clause verbatim | AXIOMATIC_CALCULUS §9 Constraint surfaces; ACTIVATION §2 Acquisition | L-15 |
| 16 | A compressed constraint surface treats an unresolved premise as unrestricted freedom | AXIOMATIC_CALCULUS §9 Constraint surfaces, AC-009; ACTIVATION §1 Applicability | L-16 |
| 17 | A task has several solutions inside the same constraint surface | AXIOMATIC_CALCULUS §9 Constraint surfaces, AC-008 | L-17 |
| 18 | A projection changes “not required” into “prohibited”, or preference into obligation | EVALUATION §7 Derived guidance; AXIOMATIC_CALCULUS AC-008, §9 | L-18 |
| 19 | Ordinary entry points to an earlier formal interpretation marked current | PRODUCT_DEFINITION §11; ACTIVATION §2 Staleness of derived surfaces; the README route | L-19 |
| 20 | Information and its representation differ | EVALUATION §2, §6 Equivalence ladder; AXIOMATIC_CALCULUS AC-017, AC-018 | L-20 structure is not meaning |
| 21 | Identity is unchanged while content changes | FOUNDATIONS §2 (Object); IDENTITY §2 Stability; REFERENCE_FRAME RF-005; ACTIVATION §7 | L-21 identity is not content |
| 22 | Typed producers and consumers disagree | FOUNDATIONS §4 Composition; AXIOMATIC_CALCULUS AC-004, AC-016 | T-03; L-22 for the explicit incompatible domain or precondition and for same-shape fields |
| 23 | Assessment A failed and required coverage B is uncovered | FOUNDATIONS §4 Conjunction of results | T-04; L-23 for the authentication of each planned judgement and for B as uncovered coverage |
| 24 | A genuinely planned assessment carries a judgement from a different subject | FOUNDATIONS §4 Conjunction of results (second input); EVALUATION §2; REFERENCE_FRAME RF-005 | L-24 plan membership authenticates nothing |
| 25 | The context a task needs is interdependent and does not fit one actor | ACTIVATION §2 step 3, §4 Refinement; REFERENCE_FRAME RF-014 | T-01 |
| 26 | A frame fits its byte limit but irrelevant material obscures a required dependency | ACTIVATION §2 steps 2 and 3; EVALUATION §7 Frame qualification; REFERENCE_FRAME RF-003, RF-004 | L-26 fit is not attention; the actual use it calls for is the frame qualification of EVALUATION §7 |
| 27 | A frame or task changes after its trial, or actor instructions supply the expected answer | EVALUATION §7 Frame qualification (Adequate attention), §3 Protocol | L-27 |
| 28 | An author opens a fresh context to review its own candidate | EVALUATION §3, including authorship of a received contribution; ACTIVATION §1 Configuration (Reconfiguration) | L-28 a fresh context is not independence; a contributor's reading of its contribution is not independent acceptance |
| 29 | A coordination frame omits frontier items from its current attention | ACTIVATION §1 Transitions (Open work outside attention); REFERENCE_FRAME RF-015 | L-29 out of view stays open |
| 30 | A new observation exposes more obligations, or a destination is revised to make the current candidate pass | ACTIVATION §1 Transitions (Discovery, Destination change, Completion, Progress), §5 (Progress) | L-30 discovery and destination change |
| 31 | One directly authorised task fits a sufficient frame | ACTIVATION §1 Configuration (Allocation, Direct entry), Roles and delegation | L-31 direct entry |
| 32 | A peer configuration has no central Executive, or a task uses responsibilities outside the familiar three roles | ACTIVATION §1 Configuration (Allocation, Evaluation of a configuration, Example); EXECUTIVE_BASELINE §16 | CD-01 |
| 33 | Actors redistribute work during execution, including work with effects of uncertain completion | ACTIVATION §1 Configuration (Reconfiguration), §3 Effects, §5 | CD-01 |
| 34 | An arrangement is called optimal because it is familiar, persistent or self-organised | ACTIVATION §1 Configuration (Optimality) | L-34 optimality is a separate claim |
| 35 | A coordinator receives a compact task result that omits a blocker material to delivery | ACTIVATION §1 Configuration (Coordination across tasks), §7 | L-35 a compact result hides no blocker |
| 36 | A material dependency changes or a new observation invalidates an earlier claim | ACTIVATION §7, §1 Transitions (Discovery); EVALUATION §2; REFERENCE_FRAME §10 Revision actions | T-06; L-36 for unchanged bytes and for a frame revision that changes no declaration: harmless explanatory metadata leaves a closed result reusable after the consumer's exact applicability check; newly admitted evidence bearing on a closed result, or a recorded activation found outside its frame's family, reopens that result and the coverage claims that consumed it before reliance, while demonstrably independent results survive |
| 37 | A task packet contains relevant rules but lacks material context or authority | REFERENCE_FRAME §11; ACTIVATION §1 Configuration (Distinct relations), §2 (Activation) | L-37 a rule packet is not an activation |
| 38 | A fresh actor has no private history, and a retained summary disagrees with the current workspace | ACTIVATION §5 The workspace and an actor's account, §3 Effects | CD-03 |
| 39 | An interruption leaves work partly written | ACTIVATION §5 (Resumption; The workspace and an actor's account); FOUNDATIONS §4 Results (Not performed) | T-05; L-39 for partly written work |
| 40 | A parse or map succeeds | EVALUATION §2, §7 (Derived guidance); AXIOMATIC_CALCULUS AC-018, AC-019 | T-07; L-40 for practical evidence |
| 41 | A change to work carriers or process is proposed as new law | ACTIVATION §6; SPEC_METHOD §4; TICKETS §5 Carrier selection | L-41 new law states its purpose |
| 42 | The same requirements are realised by software, a human team or a mixed process | SPEC_METHOD §11 rules 1, 2 and 4 | CD-02 |
| 43 | A faster execution plan merges two required independent assessments or substitutes an automated result for a required human decision | SPEC_METHOD §11 rules 2 and 4; EVALUATION §3 | CD-02 |
| 44 | Two environments use one computational calculus, or one actor performs different kinds of operation | SPEC_METHOD §11 rules 2 and 5 | L-44 one calculus, several environments |
| 45 | An a_c model of a human process passes structural validation | SPEC_METHOD §11 rule 6; AXIOMATIC_CALCULUS AC-018 | L-45 a model selects no executor |
| 46 | Two loci in one candidate decide the same question | FOUNDATIONS §2 Imports between members; PRODUCT_DEFINITION §11 | L-46 one owner per question |
| 47 | A member or profile defines its own result values | FOUNDATIONS §4 Results (Recording, Refinements, the rule that nothing raises standing); ACTIVATION §3; each member or profile that defines result values | L-47 refined values map once, including two effects: one whose declared outcome requires five updates by 12:00, where at 12:01 the evidence establishes three and not whether the effect has ended, is `not_effected` (`falsified`) with the two missing updates as counterexample and the unestablished end as a residual; one whose response was lost with no counterexample observed is `completion_unknown` (`indeterminate`); neither is repeated before reconciliation |
| 48 | A lifecycle label or classification is used to decide admission, compliance or closure | FOUNDATIONS §4 Results (Recording, Refinements); ACTIVATION §3 Disposition; TICKETS §3; SPEC_METHOD §2 Requirement categories and classification | L-48 |
| 49 | A conserved heading now carries a different obligation, or a superseded row names only the old section | RELEASE §9, the comparison test on required and permitted decisions, modal force, triggers, scope and exceptions; each member's Source dispositions | L-49; an indicative rewrite is judged by its meaning |
| 50 | A frame's task returns a result | each frame whose task returns a result; REFERENCE_FRAME RF-012, §11; ACTIVATION §2 (Standalone scope) | L-50 result-returning frames carry the algebra |
| 51 | A functor or categorical join is claimed | FOUNDATIONS §4 Formal fragment; EVALUATION §6 Equivalence ladder; AXIOMATIC_CALCULUS §5 | L-51 categorical claims carry their demonstration |
| 52 | A rewrite or refinement step is applied | ACTIVATION §4 Refinement | L-52 steps are licensed |

The construction and integrated closure checks of the common conformance
table are not member predicates. The integrated working assessment reads
them over the whole candidate, and the cross-family acceptance review
evaluates them before closure:

| No. | Check | Read by |
|---|---|---|
| J53 | Each member passes its local checks while two members still decide the same shared question differently | the integrated assessment (L-J53) |
| J54 | A member reviewer agrees that a proposed replacement is clear, but no owner decision accepts its changed meaning | the integrated assessment (L-J54) |
| J55 | Five member criteria are satisfied and the sixth is missing, stale or falsified | the integrated assessment (L-J55), and the decision owner at member acceptance, who applies the installed builder's result conjunction; ACTIVATION §1 Applicability, under which a supported inapplicability of a conditional obligation is recorded separately and waives no criterion |

Coverage. Eleven of the 52 discriminators are exercised by cases: 22
(T-03), 23 (T-04), 25 (T-01), 32 and 33 (CD-01), 36 (T-06), 38 (CD-03),
39 (T-05), 40 (T-07), and 42 and 43 (CD-02). For 22, 23, 36, 39 and 40
the case tests part of the expected distinction, and checks L-22, L-23,
L-36, L-39 and L-40 cover the rest. The other 41 are exercised by
logical-review checks only, and the three closure checks J53 to J55 by
the integrated assessment. No case has recorded a pass. Runs by fresh constructors exist for T-01, T-03, T-04 and T-05,
and for R-01 and R-02, which exercise no discriminator; each run bound an
earlier revision of this corpus and none has been assessed, so none is
actual-use evidence for this revision (EVALUATION §7). T-06, T-07, CD-01, CD-02 and CD-03 have not
been run. A case that has not been run on this revision and assessed has no
result for it: it is a planned assessment without a closed result, never a
pass ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed), and
the logical review of its discriminators does not stand in for it. No
logical-review check is recorded for this revision: each is a planned
assessment without a closed result until a review records it
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed).

### Universal-construction and assurance discriminators

The construction specification adds, beside the member discriminators
above, nine universal-construction discriminators and twelve assurance
discriminators, with their expected distinctions in the same file and not
restated here, assessed under criterion 5 within a member's declared
responsibility. Each is numbered UC-n or AS-n in the order the governing
specification lists it. A logical-review check L-UCn or L-ASn is a planned
assessment without a closed result until a review records it; a case is
exercised only when it has been run and assessed; the finite oracle named
for three of them is mechanical evidence on a finite model and establishes
neither fidelity nor semantic conformance
([EVALUATION §2](EVALUATION.md#2-separation)).

| No. | Discriminator | Member sections | Exercised by |
|---|---|---|---|
| UC-1 | Internal tasks pass while a required end-to-end feature fails | ACTIVATION §1 Composition boundaries; FOUNDATIONS §4 Preservation through construction; EVALUATION §1 | L-UC1 |
| UC-2 | Every selected operation is lawful but the result fails the chosen outcome constraints | ACTIVATION §1 Binding A and Z (lawfulness establishes neither delivery nor optimality); SPEC_METHOD §11 | L-UC2 |
| UC-3 | A report called a bug could concern implementation, requirements or missing observations | ACTIVATION §1 Feedback and diagnosis; SPEC_METHOD §4 Universal intake triage | L-UC3 |
| UC-4 | A requirement is weakened until the current realisation passes | ACTIVATION §1 Transitions, Destination change, and Evaluation and completion; SPEC_METHOD §4 change classes; FOUNDATIONS §4 Parallel derivation and mutual assurance (corrections preserve counterexamples) | L-UC4 |
| UC-5 | A predictive model agrees with observations while the required outcome is absent, or predicts incorrectly while the outcome holds | ACTIVATION §1 Three accounts of the subject; Feedback and diagnosis | L-UC5 |
| UC-6 | A strategy is selected solely by its name, or a cheaper plan loses required assurance | ACTIVATION §1 Strategy; FOUNDATIONS §4 Quantified assurance (no waiver by a cheaper plan); EXECUTIVE_BASELINE Steel-thread delivery | L-UC6 |
| UC-7 | Every recursive step preserves an invariant but the process does not deliver | ACTIVATION §1 Preservation, progress and completion; FOUNDATIONS §3 Construction synthesis | L-UC7 |
| UC-8 | A limit is exhausted, an observation exposes more work, or an ongoing maintenance loop continues | ACTIVATION §1 Preservation, progress and completion, and Transitions (Stops); ACTIVATION §6 | L-UC8 |
| UC-9 | A restart or later disturbance contradicts a cached successful result | ACTIVATION §5 The workspace and an actor's account; ACTIVATION §7; case CD-03 | CD-03 (not run); L-UC9 |
| AS-1 | Every local check passes, but a postcondition does not establish the next precondition or the final property does not imply Z | FOUNDATIONS §4 Preservation through construction | L-AS1 |
| AS-2 | A histogram has the right keys but incorrect counts; a key-only test passes | FOUNDATIONS §4 Assertions and observation (a check of a necessary condition); case AR-01 | AR-01 (not run); L-AS2 |
| AS-3 | Two admissible states have identical acquired observations but opposite truth values for the asserted obligation | FOUNDATIONS §4 Assertions and observation, Observation sufficiency; case AR-02; the finite oracle instance `assurance` | AR-02 (not run); the finite oracle (mechanical); L-AS3 |
| AS-4 | A test copies its expected answer from the implementation and cites the requirement's digest | FOUNDATIONS §4 Parallel derivation and mutual assurance (an implementation-derived decision supplies no independent justification) | L-AS4 |
| AS-5 | A human or probabilistic checker can soundly return satisfied or indeterminate on the same observations | FOUNDATIONS §4 Assertions and observation (a universal soundness claim covers all admitted conclusions) | L-AS5 |
| AS-6 | Two implementations or reviewers agree through the same wrong interpretation, fixture or received contribution | FOUNDATIONS §4 Parallel derivation and mutual assurance; case AR-03 | AR-03 (not run); L-AS6 |
| AS-7 | Miss rates are multiplied without conditional independence, or an injected-defect score is reported as whole-product correctness probability | FOUNDATIONS §4 Quantified assurance; the finite oracle instance `assurance` | the finite oracle (mechanical); L-AS7 |
| AS-8 | Finite successful examples or a schema-valid formula are called a proof of a universal preservation law | FOUNDATIONS §4 Formal representation; AXIOMATIC_CALCULUS §9 Constraint surfaces, condition 1 | L-AS8 |
| AS-9 | A governing requirement changes but expected answers and acceptance evidence are silently retained | FOUNDATIONS §4 Change impact and evidence reuse; ACTIVATION §7; case AR-04 | AR-04 (performed once by the author); L-AS9 |
| AS-10 | An implementation or environment dependency changes but the only selection relation is requirement-to-test provenance | FOUNDATIONS §4 Change impact and evidence reuse (a requirements-to-test link is no impact model); the finite oracle instance `assurance` | the finite oracle (mechanical); L-AS10 |
| AS-11 | A local repair has supported isolation from an unchanged obligation and its evidence conditions | FOUNDATIONS §4 Change impact and evidence reuse (retention) | L-AS11 |
| AS-12 | Selection is cheap but omits a material obligation, or selection overhead exceeds the saved execution | FOUNDATIONS §4 Change impact and evidence reuse (cost); FOUNDATIONS §4 Quantified assurance | L-AS12 |

Coverage of these 21: four are mapped to cases (AR-01, AR-02, AR-03,
CD-03, none run; AR-04 performed once by the author), three to the finite
oracle beside their logical review, and all 21 to a logical-review check;
no logical-review check is recorded for this revision.

Purpose and material relation: a reader sees, for each discriminator,
whether actual use or only a reasoned reading exercises it and which
sections it reads, so a discriminator mapped to a case that has not been
run and assessed is never counted as passed, and no mapping exempts a
member from logical review (P6, P2).

## 6. Source dispositions

This section records dispositions and decides nothing. The comparative
baseline's eight trials are conserved as §2. The builder-history
counterexamples are new, derived from the common inputs; their primary
sources are reacquired when a case is designed for execution. The
situations of the common discriminators in §5 (52 member discriminators,
three of the seven integrated-closure discriminators, J53 to J55, and the
21 universal-construction and assurance discriminators) are named from
the construction specification in the header, whose expected distinctions
§5 does not restate; their mapping, the logical-review checks and the
cases of §4 are new. This member carries no
predecessor claim.
