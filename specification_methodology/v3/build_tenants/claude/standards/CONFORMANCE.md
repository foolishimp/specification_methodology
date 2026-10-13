# CONFORMANCE

Tier 2. Owns the cases this corpus must pass before it is qualified (§1 to
§4) and the coverage of the common discriminators by those cases and by
logical-review checks (§5). A discriminator is a situation whose expected
distinction separates a conforming corpus from a defective one. The common
discriminators are the 31 that the specification governing this corpus's
construction states for every candidate corpus; §5 states each of them in
this member's own text, and nothing here relies on that specification,
which is named only as provenance (`specification/conformance/README.md`
of the source project that constructs this corpus).

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
declared subject returns `out_of_frame`, which is recorded, not hidden.

Result values. The values `satisfied`, `falsified`, `out_of_frame` and
`invalid_basis` named in this member are core values of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). The values `re_enter`,
`re_entry_requested(authority)` and `completion_unknown` are refinements
that [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition)
defines and maps into that core. This member defines no result value
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
| T-03 Composition conservation | two valid bounded results under one outer contract | all inputs, constraints, judgments and evidence survive; an incompatible join is refused | fixture [T-03-04](../qualification/cases/T-03-04/CASE.md) run twice; not assessed |
| T-04 Failure and missing assessment | one observed failure plus one required obligation with no assessment | both states survive; the composite cannot report success or erase the unassessed obligation | fixture [T-03-04](../qualification/cases/T-03-04/CASE.md) run twice; not assessed |
| T-05 Compaction and actor change | pause, clear context, resume with a new actor | valid progress and basis recovered; unsupported completion claims and unnecessary restarts detected | fixture [T-05](../qualification/cases/T-05/CASE.md) run twice; not assessed |
| T-06 Changed governing requirement | one requirement revised after partial construction | affected claims reopened; unaffected results reused with explicit dependencies | not run |
| T-07 Defective acceptance oracle | a candidate passing structural checks but violating required behaviour | assessment detects the defect or reports its evidential limit; structural green is not acceptance | not run |
| T-08 Broader process use | a sourced decision analysis with uncertainty and stale evidence | facts, assumptions, judgments and authority stay distinct; the result is independently assessable | not run |

Trials declare a per-actor context cap and total-work budget before each
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
| CD-01 Configuration without a fixed role inventory (13, 14) | a task whose dependent operations are carried out by peer actors with no central coordinator, under responsibility names other than those of the executive configuration; during the work one actor hands another an operation whose external effect has unknown completion; an executive configuration installed to build a release is in use beside it | ACTIVATION §1 Configuration, §3 Effects, §5; EXECUTIVE_BASELINE §16 | the configuration is evaluated against the task, its dependencies, the actors' limits, the authority it applies and the required assurance, and its labels and topology neither accept nor reject it; the installed configuration keeps its own scope and is not the measure of the peer configuration; the handover keeps the outstanding obligations and the results that depend on them, resolves the effect's completion before the next dependent action, and keeps the admitted authority and the required independence; self-organisation exempts it from none of these | not run |
| CD-02 One set of requirements, several executors (23, 24) | one set of requirements realised by a software stack and by a mixed process of people and software; for one of them, a proposed faster execution plan merges two required independent assessments and replaces a required human decision with an automated result | SPEC_METHOD §11 rules 1, 2 and 4; EVALUATION §3 | each realisation is judged by the obligations of the requirements, with its computational calculus, execution binding and conformance evidence, and the kind of executor neither accepts nor rejects it; the faster plan's conformance for each weakened obligation is falsified, and matching outputs, lower cost or a faster run do not discharge the lost independence or authority | not run |
| CD-03 Stale summary against the current workspace (19) | a fresh actor with no private history resumes work from a retained summary that disagrees with the current workspace, including about whether an external effect occurred; resolving one disagreement needs an operation outside the actor's grant | ACTIVATION §5 The workspace and an actor's account, §3 Effects and Construction availability, §7 | the actor acquires the current subject and its authoritative inputs, corrects its account from current evidence, keeps the applicable work and continues within its grant, stopping with re_entry_requested(authority) for the disagreement outside it; the summary never overrules the workspace, discarding the prior context erases nothing in it, and a missing record of the effect leaves it completion_unknown, never absent | not run |

Purpose and material relation: a reading of the text can show that the
corpus states these distinctions, but only use shows that an actor
applying the corpus keeps them while it works (P6, P0).

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
governing specification lists them, with its expected distinction, the
member sections it exercises, and the cases or the logical-review check
that exercise it. A case is listed only where its subject instantiates the
discriminator's situation and its expected distinction, as this member
states it, tests the discriminator's; where it tests only part, the cell
also names the logical-review check for the rest. A check is named L with
the discriminator's number. Whatever its mapping, every discriminator is
read by logical review against every member; a case adds actual use and
replaces no part of that reading (P6). Check L-29 also reads each frame
whose task returns a result.

| No. | Discriminator | Expected distinction | Member sections | Exercised by |
|---|---|---|---|---|
| 1 | A derivation or independence argument is claimed | Each claimed derivation shows its premises. Claimed independence is argued, not assumed. | FOUNDATIONS §1, §3 Commitments and Foundation to law; EVALUATION §1 | L-01 premises shown |
| 2 | Information and its representation differ | Agreement in structure cannot establish identical meaning or semantic fidelity. | EVALUATION §2, §6 Equivalence ladder; AXIOMATIC_CALCULUS AC-017, AC-018 | L-02 structure is not meaning |
| 3 | Identity is unchanged while content changes | The current state, and whether an earlier observation still applies, are considered separately. | FOUNDATIONS §2 (Object); IDENTITY §2 Stability; REFERENCE_FRAME RF-005; ACTIVATION §7 | L-03 identity is not content |
| 4 | Typed producers and consumers disagree | The incompatible domain or precondition is made explicit. Fields of the same shape do not make a valid join. | FOUNDATIONS §4 Composition; AXIOMATIC_CALCULUS AC-004, AC-016 | T-03; L-04 for the explicit incompatible domain or precondition and for same-shape fields |
| 5 | Assessment A failed and required coverage B is uncovered | A's authenticated failure and its citations survive, and B stays unresolved. Every planned assessment's returned judgement is authenticated against its producer, subject, basis and supporting evidence. B is required coverage outside those assessments, not an omitted planned judgement. | FOUNDATIONS §4 Conjunction of results | T-04; L-05 for the authentication of each planned judgement and for B as uncovered coverage |
| 6 | A genuinely planned assessment carries a judgement from a different subject | Plan membership does not authenticate the returned judgement. The misbound result cannot satisfy the assessment obligation. | FOUNDATIONS §4 Conjunction of results (second input); EVALUATION §2; REFERENCE_FRAME RF-005 | L-06 plan membership authenticates nothing |
| 7 | The context a task needs is interdependent and does not fit one actor | Narrowing the task lawfully, handing it to another capable actor, or a truthful stop keeps the material obligations. | ACTIVATION §2 step 3, §4 Refinement; REFERENCE_FRAME RF-014 | T-01 |
| 8 | A frame fits its byte limit but irrelevant material obscures a required dependency | Size alone does not establish adequacy. The material dependency is kept, irrelevant material is excluded, and actual use is evaluated. | ACTIVATION §2 steps 2 and 3; EVALUATION §7 Frame qualification; REFERENCE_FRAME RF-003, RF-004 | L-08 fit is not attention; the actual use it calls for is the frame qualification of EVALUATION §7 |
| 9 | An author opens a fresh context to review its own candidate | A new context does not establish independent authorship or supply missing review authority. An independent reviewer may still share relevant common sources. | EVALUATION §3; ACTIVATION §1 Configuration (Reconfiguration) | L-09 a fresh context is not independence |
| 10 | A coordination frame omits frontier items, the known open work, from its current attention | Excluded work remains open; a bounded view cannot silently dispose of it. The next decision retains its material dependencies. | ACTIVATION §1 Transitions (Open work outside attention); REFERENCE_FRAME RF-015 | L-10 out of view stays open |
| 11 | A new observation exposes more obligations, or a destination is revised to make the current candidate pass | Discovery may increase the frontier while improving knowledge. Counts alone do not measure progress. A revised destination requires its owning decision and cannot establish that the original destination was reached. | ACTIVATION §1 Transitions (Discovery, Destination change, Completion, Progress), §5 (Progress) | L-11 discovery and destination change |
| 12 | One directly authorised task fits a sufficient frame | The generic method permits the direct activation, subject to any separately required assessment. It imposes no fixed role inventory or actor sequence. | ACTIVATION §1 Configuration (Allocation, Direct entry), Roles and delegation | L-12 direct entry |
| 13 | A peer configuration has no central coordinator such as an Executive, or a task uses responsibilities outside the three frames of the executive configuration | The configuration is evaluated against the task, its dependencies, the actors' limits, the authority and the required assurance. Different labels or topology neither reject nor accept it. An installed configuration selected to build a particular release keeps its own scope. | ACTIVATION §1 Configuration (Allocation, Evaluation of a configuration, Example); EXECUTIVE_BASELINE §16 | CD-01 |
| 14 | Actors redistribute work during execution, including work with effects of uncertain completion | The permitted reconfiguration retains outstanding obligations and result dependencies, resolves material effect uncertainty before dependent action, and preserves authority and required independence. Self-organisation supplies no exemption from these conditions. | ACTIVATION §1 Configuration (Reconfiguration), §3 Effects, §5 | CD-01 |
| 15 | An arrangement is called optimal because it is familiar, persistent or self-organised | Adequacy and optimality remain separate claims. An optimality claim needs stated objectives, constraints and comparison scope with supporting evidence. Different models or objectives can favour different configurations. | ACTIVATION §1 Configuration (Optimality) | L-15 optimality is a separate claim |
| 16 | A coordinator receives a compact task result that omits a blocker material to delivery | Small size is insufficient. The coordinator retains the longer-term outcome and acquires the information needed for the next decision through its permitted frame inputs. Missing information cannot be assumed favourable. | ACTIVATION §1 Configuration (Coordination across tasks), §7 | L-16 a compact result hides no blocker |
| 17 | A material dependency changes or a new observation invalidates an earlier claim | Affected applicability and validity are checked before reuse, including when the candidate's bytes are unchanged. Demonstrably independent supported work is kept. | ACTIVATION §7, §1 Transitions (Discovery); EVALUATION §2 | T-06; L-17 for unchanged bytes |
| 18 | A task packet contains relevant rules but lacks material context or authority | A rule packet alone is insufficient. The activated frame binds the contract, subject, evidence, capability and permitted effects required for the task. | REFERENCE_FRAME §11; ACTIVATION §1 Configuration (Distinct relations), §2 (Activation) | L-18 a rule packet is not an activation |
| 19 | A fresh actor has no private history, and a retained summary disagrees with the current workspace | The actor acquires the current subject and its authoritative inputs, corrects the stale account, retains applicable work and continues within its grant. Discarding context does not erase the workspace or prove an uncertain external effect absent. | ACTIVATION §5 The workspace and an actor's account, §3 Effects | CD-03 |
| 20 | An interruption leaves work partly written | Recovery uses the current workspace and the applicable work state. It does not erase progress or invent a completed assessment. | ACTIVATION §5 (Resumption; The workspace and an actor's account); FOUNDATIONS §4 Results (Not performed) | T-05; L-20 for partly written work |
| 21 | A parse or map succeeds | The claim stays mechanical until independently sufficient semantic and practical evidence exists. | EVALUATION §2, §7 (Derived guidance); AXIOMATIC_CALCULUS AC-018, AC-019 | T-07; L-21 for practical evidence |
| 22 | A change to work carriers or process is proposed as new law | The claimed obligation is justified by its purpose and material relation, or identified as unsupported overhead. | ACTIVATION §6; SPEC_METHOD §4; TICKETS §5 Carrier selection | L-22 new law states its purpose |
| 23 | The same requirements are realised by software, a human team or a mixed process | Each build tenant supplies its computational calculus, concrete execution binding and conformance evidence. The requirements decide fitness; the kind of executor alone neither rejects nor accepts the realisation. | SPEC_METHOD §11 rules 1, 2 and 4 | CD-02 |
| 24 | A faster execution plan merges two required independent assessments or substitutes an automated result for a required human decision | Matching outputs or lower cost cannot discharge the lost independence or authority obligation. The binding fails conformance. | SPEC_METHOD §11 rules 2 and 4; EVALUATION §3 | CD-02 |
| 25 | Two environments use one computational calculus, or one actor performs different kinds of operation | Each binding must satisfy the calculus's laws. Different stacks do not force duplicate calculi; actor identity does not determine operation kind or grant authority. | SPEC_METHOD §11 rules 2 and 5 | L-25 one calculus, several environments |
| 26 | An a_c model of a human process passes structural validation | The representation neither selects an automated executor nor establishes that the human process meets its requirements. Execution conformance needs its own applicable evidence. | SPEC_METHOD §11 rule 6; AXIOMATIC_CALCULUS AC-018 | L-26 a model selects no executor |
| 27 | Two loci in one corpus, places in its text that each decide a question, decide the same question | One is the owning locus. The other refers to it, or refines it with a mapping back to it. A frame's copy names its owner. No rule of precedence between loci substitutes for an owner. | FOUNDATIONS §2 Imports between members; PRODUCT_DEFINITION §11 | L-27 one owner per question |
| 28 | A member or profile defines its own result values | Each value maps to exactly one core result. Failure, undecidability, non-performance and unknown effect completion never map to a higher standing. The evaluated predicate and the domain outcome travel with the core value. | FOUNDATIONS §4 Results (Recording, Refinements, the rule that nothing raises standing); ACTIVATION §3; each member or profile that defines result values | L-28 refined values map once |
| 29 | A frame's task returns a result | The frame carries the core result algebra or its profile's mapping into it. | each frame whose task returns a result; REFERENCE_FRAME RF-012, §11; ACTIVATION §2 (Standalone scope) | L-29 result-returning frames carry the algebra |
| 30 | A functor or categorical join is claimed | Before the claim, objects, arrows, arrow equality, identity and composition are given and the functor laws are shown. Otherwise the claim is a hypothesis. | FOUNDATIONS §4 Formal fragment; EVALUATION §6 Equivalence ladder; AXIOMATIC_CALCULUS §5 | L-30 categorical claims carry their demonstration |
| 31 | A rewrite or refinement step is applied | The law that permits it is declared for the subject. An exact step preserves meaning. An approximate step states its adequacy relation and an end-to-end bound. | ACTIVATION §4 Refinement | L-31 steps are licensed |

Coverage. Eleven discriminators are exercised by cases: 4 (T-03), 5
(T-04), 7 (T-01), 13 and 14 (CD-01), 17 (T-06), 19 (CD-03), 20 (T-05), 21
(T-07), and 23 and 24 (CD-02). For 4, 5, 17, 20 and 21 the case tests
part of the expected distinction, and checks L-04, L-05, L-17, L-20 and
L-21 cover the rest. The other twenty are exercised by logical-review
checks only. No case has recorded a pass. Runs by fresh constructors exist for T-01, T-03, T-04 and T-05,
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
statement of the 31 common discriminators in §5 restates the
specification named in the header, as provenance; their mapping, the
logical-review checks and the cases of §4 are new. This member carries no
predecessor claim.
