
Source: standards/EVALUATION.md; whole-member SHA256 b856cf04e2cf6ea0ba8b5f9de8b455a3a5f95cdb05fe7337f077f1b7547c7485; bytes [46864,53352); exact source section below.

## 5. Acceptance

Acceptance is the decision owner's disposition over an unchanged subject;
recording it cannot widen it, and it exhausts only the instance and interval
it names (P6, P2).
A work item closes by the condition it stated, not by a reviewer's approval;
a reviewer result is an input to closure, never the closure. Green labels,
document counts, review counts and historical outcomes are not acceptance.
A human decision may be exercised directly or through an explicitly admitted
bounded proxy. What a proxy grant names is
[IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)'s,
and what a proxy can never decide is
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds)';
for acceptance, a change a proxy cannot make re-enters at its owning
relation ([ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)).

Where the subject is a successor, its acceptance evidence includes the
successor disposition record of [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
(STDO-UP-015), which states the law: the exact predecessor immutable cut
the successor evolves, and one semantic disposition for every predecessor
claim capable of affecting the successor. A claim whose disposition is
unresolved cannot be qualified and so cannot be accepted; how the record
is evaluated is [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015).
An intentionally removed disposition is a decision of the current Product
authority, and its record is that decision (P6, P3, P4b).

### Landing, closure and release

Landing makes an exact candidate available at an authorized checkpoint or
integration destination. It is an operation under its existing grant, not
acceptance of the candidate's claims. Work closure applies the stated closing
condition; release applies the separately selected publication and acceptance
conditions of [RELEASE](RELEASE.md). Record these as separate decisions (P6,
P3).

Review supplies QA evidence for those decisions. A pending review does not by
itself hold landing: an admitted candidate may land after its bounded work
and fix pass, while review of that exact candidate runs beside subsequent
authorized work. A required review holds the closure or acceptance claim that
depends on its complete report. A governing landing condition, applicable hard
stop or missing operation authority still prevents landing; availability is
no waiver. [EXECUTIVE_BASELINE §12](EXECUTIVE_BASELINE.md#qa-cadence-and-repair-rechecks)
binds the optional profile's repair/recheck cadence (P6, P2).

Permitted downstream work may consume a landed candidate before its review
reports, carrying its exact identity, unresolved conditions and dependency
links. This is provisional use, not admitted truth. A later material finding
invalidates the affected dependent results under
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); unrelated valid results
remain reusable. Repair and re-evaluation follow those dependencies before
further reliance (P4b, P6).

### Declared Product acceptance gates

A Product-owned frame basis, or a work contract explicitly delegated that
choice by the basis, may declare a gated handoff between two Products. It
names both Product identities, the directed relation, exact candidate/claim,
required review and coverage, acceptance conditions and decision owner. Until
that review has covered its declared subject and the acceptance conditions
are satisfied, the downstream Product cannot accept the candidate as an
admitted input or close claims dependent on that acceptance. Authorized
provisional work and repair may continue under the preceding section (P6,
P2).

The gate's declaration is explicit; co-location, a dependency or this available
mechanism creates none. Existing user-acceptance, release/go-live and other
Product boundaries retain their own conditions. This member declares no
particular Product gate or extra capture-review hold on landing (P6).

### When a finding blocks promotion

A finding is a defect a review reports against the exact claim it
evaluated (§4). Blocking current promotion is the decision owner's act
over that finding (§4, Result and triage projection). This section is the
one statement of when a finding can block; profiles and work carriers
refer to it and add only their domain triggers.

A review verdict is bounded by the exact reviewed claim and its applicable
hard stops ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)). A
finding can block current promotion only when it:

1. falsifies that claim;
2. exposes competing or ambiguous authority on the claim's acceptance
   path;
3. violates applicable active authority, safety or retained accepted
   behaviour; or
4. establishes a material architectural decision with durable
   consequences that forecloses an admitted Product outcome.

These conditions are necessary. Which of them suffice is decided as
follows:

| Consumed condition | Effect on the current promotion boundary |
|---|---|
| a valid falsification of a mandatory claim governed by a non-waivable hard stop | the boundary blocks, whatever the assigned priority or the decision cutoff |
| any other finding meeting one of the four conditions | the decision owner decides blocking from the exact affected claim, the governed outcome or decision the work serves ([ACTIVATION §1, Intake](ACTIVATION.md#intake)), the applicable hard stops and the Product-owned cutoff policy; below that cutoff no block follows mechanically, and an accepted residual is retained explicitly |
| a finding meeting none of the four conditions | it does not block |
| an observation outside the exact reviewed claim | repricing or re-entry input, returned as §4 states: by itself it does not widen the reviewed subject, block its bounded claim, or require a new ticket, artifact, review round or implementation increment |

Severity selects neither priority nor a block mechanically, and priority
neither erases severity nor waives a hard stop. The decision cutoff is the
adopting Product's policy; this member sets no cutoff (P6, P2). This law
applies at any promotion boundary; [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md#promotion-constraint-projection)
binds the Executive instance. Purpose and material relation: one owner
gives every review consumer the same blocking condition. A bounded review
does not block on observations outside its claim, while a non-waivable hard
stop still blocks.


Source: standards/EXECUTIVE_BASELINE.md; whole-member SHA256 00cd728cf24b67511ad6dc58f4d10e147a444a551fdec242cd72e88417cf0801; bytes [57457,63010); exact source section below.

### Technical triage, severity, priority and boundary effect

Technical triage is the Reviewer's assessment of one finding against the
exact evaluated claim and basis. Where admissible evidence and the actor's
capability envelope support it, the triage records (P6, P5):

- the affected claim and the observed failure;
- severity on the Product-selected severity scale;
- causal assessment and confidence, the confidence being a quantified
  claim under [FOUNDATIONS §4 Quantified assurance](FOUNDATIONS.md#quantified-assurance);
- blast radius and the affected users, paths or relations;
- an available workaround or containment;
- repair complexity, regression risk and material dependencies; and
- residual uncertainty and the evidence that would reduce it.

Missing causal or repair evidence stays explicit. Where the missing
relation can change the evaluation, the Reviewer returns `indeterminate` or
`out_of_frame` pressure (FOUNDATIONS §4 Results); it does not invent precision and
does not send work sideways to the Worker (P5).

Severity grades the consequence if the finding manifests. Priority orders
the response relative to the complete Product outcome, likelihood and
exposure, the current MVP or release mandate, reversibility, dependencies,
cost of delay and available capacity. The Reviewer grades severity; the
Executive assigns priority (P6, P2).

The Product-owned Project Reference-Frame Basis binds the severity scale,
the priority scale and the current-boundary decision cutoff, and names
which conditions of the governed outcome are hard stops. What a hard stop
is, its classes, and that it holds whatever the priority, cutoff or risk
appetite, so that no decision waives it, are
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) Hard stops,
whose classes are typical, not closed; the basis names its own
non-waivable hard stops, each holding as that section states. "Non-waivable hard stop" in this
profile and in EVALUATION §5 means such a stop. This profile imposes no
universal numeric scale. Severity, priority, the frame result
(FOUNDATIONS §4 Results) and the current-boundary effect are four distinct
values. When a finding can block a promotion boundary is
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
and none of the four values alone decides it (P6, P1).

Current-boundary effect is the Executive's recorded determination of what
one finding does to the current promotion boundary: it blocks it, requires
narrowing it, or may remain an explicit residual. It is a decision
projection, a state this profile declares, not a result and not a
disposition (§8): it maps to no core value of its own and decides nothing
by itself. Where it is "blocks", a condition of EVALUATION §5 holds; the
decision it records returns through the core only through the one
existing disposition the Executive then applies (ACTIVATION §3,
Disposition). Purpose and material relation: the record keeps the
Executive's reading of each finding apart from severity, priority and the
disposition, so a consumer can see why a boundary was held, narrowed or
promoted with a residual, and no field other than the disposition decides
acceptance (P6, P2). A hard stop or a falsified mandatory claim cannot be
waived by lowering priority. An observation outside the exact claim
boundary cannot open another review round because it carries a severe
label (P6, P2). How each result member projects the triage payload and
constrains its consumption is EVALUATION §4 (Result and triage
projection).

#### Proportional triage assistance

When the cause and consequence are sufficiently clear, the Executive decides
priority and ownership directly. Where finding volume would overwhelm its
bounded attention, it may activate a triage Worker to group causes, identify
duplicates and propose priorities and responsible owners from the admitted
findings. The assistant neither grades nor changes Reviewer severity and
decides no priority or disposition. The Executive consumes its evidence and
records its own decision; unsupported cause relations stay uncertain. The
assistant adds no read authority, and this profile requires no extra actor
for a small or clear result (P6, P2).

#### Optional P0–P5 response policy

An adopting Product may explicitly select the following response policy in its
frame basis. The labels have no numeric meaning outside that adoption; the
Product supplies its ordering/assignment criteria and any finer distinctions.
This is priority policy, not a Reviewer severity scale (P6, P2).

| Selected priority | Response and boundary effect |
|---|---|
| P0–P2 | Include in the next bounded fix pass; hold the affected outcome's closure and release, not candidate landing merely because of this priority. |
| P3–P5 | Repair before release/go-live; hold that release, while bounded work may close with the item durably retained or transferred with its disposition. |

This policy never waives applicable hard stops, mandatory claims, acceptance
conditions, access restrictions or operation grants. Those owners may require
an earlier hold at any priority. A P3–P5 item may outlive a local work claim's
closure only when that claim does not require the unfixed behaviour; assigning
that priority cannot satisfy a false mandatory claim. No review-to-work ratio or additional
capture-review landing hold is selected by adopting this example. Durable
items and their actual verification state are owned by
[TICKETS §4](TICKETS.md#review-findings-and-bug-items).


Source: standards/EXECUTIVE_BASELINE.md; whole-member SHA256 00cd728cf24b67511ad6dc58f4d10e147a444a551fdec242cd72e88417cf0801; bytes [121244,124142); exact source section below.

### QA cadence and repair rechecks

Landing, closure, release and explicit Product gates have one owner,
[EVALUATION §5](EVALUATION.md#landing-closure-and-release). For this profile,
an admitted step lands its candidate after its selected work and fix pass.
Where review is required or selected, one bounded QA review covers that exact
declared subject and may run beside the next authorized step. It is not a
standing permission for another review of every local change. The Executive
records review size and its reason in the existing work carrier; any ratio is
Product-selected, and none is imposed here (P6, P2).

Sizing does not shrink a declared claim. Preserve the exact evaluated
population and conjunction; a sample supports its stated scope and leaves
uncovered required coverage explicit. A budget or ratio cannot turn that
residual into a completed whole-subject review (P6, P5).

Each test-reproducible repair binds a reproduction that fails on the faulty
subject and passes on the repaired subject, with the full suite declared for
that repair scope passing. A repair without a reproduction states that gap and
requires the independent recheck below; a green total does not fill the gap.
Tests may verify a repair without becoming independent assessment. A fix pass
closes on that evidence and its other applicable conditions unless independent
recheck is required by one of these conditions (P6, P5):

1. the candidate reaches a boundary whose governing basis requires or claims
   independent review, including any Product, release, qualification, risk or
   admitted-work addition;
2. the pass repairs a hard stop or a capture whose source-fidelity claim is
   material to the outcome;
3. a repair has no reproducing test; or
4. a selected review left part of its declared subject uncovered.

For a required recheck, activate one fresh Reviewer for the bounded fix pass,
with its affected claims, prior findings, reproductions and remaining coverage.
Fresh means a new bounded assessment activation with the independence of
EVALUATION §3, not independence inferred from a new context or actor name.
Partitioning follows the declared conjunction, not extra serial rounds. The
covered fixes remain unresolved for the dependent closure claim until that
report arrives and the required predicates are satisfied; tests alone cannot
substitute for this required review. A later material finding is a new input
to the next bounded disposition, not an unbounded review loop (P6, P2).

The Executive preserves Reviewer severity, assigns priority under the selected
policy and hands the linked items to the lawful repair Writer. Pending review
alone holds no landing. An open required review holds its dependent closure,
and release retains all its selected conditions. Downstream use and later
invalidation follow EVALUATION §5; access and artifact-effect grants remain
unchanged (P6).


Source: standards/TICKETS.md; whole-member SHA256 86fefd277ab513b3f22d8e827967d18c4a7ee41558a6daf896c9ad60c9240e67; bytes [29096,31828); exact source section below.

### Review findings and bug items

When findings from a review need a durable work carrier, record one linked bug
report for that review, with one entry per finding: stable identity, original
Reviewer severity and triage, exact subject/basis, violated claim, location and
chaseable evidence. Link it to the work item that issued the review. With no
findings, create no bug report. A sufficient existing direct-work carrier may
carry the same relations without a redundant ticket (P3, P2).

The Reviewer may record this report only when its activation grants the exact
artifact identity/path and effects. Otherwise it returns the findings and a
lawful Writer records them. Recording creates no repair, priority, admission or
closure authority. Keep the report within its evidence/read and visibility
restrictions: findings derived from a withheld capture are withheld from the
same recipients, including any report projection that reveals them. The
Product may bind a recognizable report naming pattern and exclusion route to
its actual access mechanism; a filename or separate lane alone enforces
nothing and grants no additional read (P6).

After Executive or other authorized decision-owner triage, the reviewed work
item carries a linked Bug items section. Each item records its identity,
original severity, assigned priority and reason, cause group, responsible owner,
source report/finding, disposition and state. The report remains the technical
finding source; the item is the decision and repair ledger. An actor/session
index, where used, points the Reviewer to its report and the triage/repair work
to the reviewed work item's ledger, rather than duplicating that truth (P3).

| Item state | Required trace |
|---|---|
| open | Finding and triage/disposition, with unresolved work named. |
| fixed | Exact repaired subject (commit or equivalent immutable identity) and repair evidence; not yet a claim of verification. |
| verified | The satisfied repair predicate and exact evidence; identify tests and, when required, the independent recheck/report. Tests alone are not labelled independent review. |

These are carrier states, not core evaluation results or acceptance. A required
recheck keeps its affected items unverified until the required result is
available and applicable. A test-verified fix needs no invented Reviewer when
the governing basis requires none; the optional Executive cadence is
[EXECUTIVE_BASELINE §12](EXECUTIVE_BASELINE.md#qa-cadence-and-repair-rechecks).
Retained or deferred findings stay linked until their selected boundary, or
transfer with owner, disposition and destination when the work item closes.
Changing priority does not erase the original severity or the obligation (P6,
P4b).


Source: standards/ACTIVATION.md; whole-member SHA256 56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d; bytes [137016,141073); exact source section below.

## 7. Closed result and reuse

A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context need not be
transferred when the closed result and its provenance are sufficient for
the consuming decision; it may still be attached, for audit or otherwise,
without changing the result. Independent evaluations may share valid
mechanical evidence under the declared independence conditions of
[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that
permission (P4b, P0).

The sufficiency of a handed-off result or reference for subsequent decisions
is [FOUNDATIONS §4 Observation sufficiency](FOUNDATIONS.md#assertions-and-observation)'s
consumer-relative claim. Reuse preserves the material standing and
continuation distinctions, including unassessed versus indeterminate; a
role change alone requires no full-history scan or new representation.

The selection of affected results after a change and the conditions for
retaining evidence on a new subject are
[FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse);
this section applies them to closed results and handoffs, and the three
invalidators below are kinds of change Δ, and a closed result is affected
when its dependencies `D*(t)` meet the impact cover `I(Δ)` (P3, P6).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. Invalidation withdraws the result from direct reliance; whether
its evidence is retained on the new basis is decided by `retain_applicable`
of FOUNDATIONS §4 Change impact and evidence reuse, and the changed
coordinate alone establishes neither that the claim fails nor that it
holds. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

A changed source, task or actor condition is a changed basis where the
basis binds it, and otherwise a material input change; a role change that
alters a required actor condition is such a change, while a role,
conversation or resumption change that alters none of these invalidates
nothing (P3, P6).

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. [TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity)
uses the same evidence invalidator. Naming these kinds once gives every
consumer the same triggers. The
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.

