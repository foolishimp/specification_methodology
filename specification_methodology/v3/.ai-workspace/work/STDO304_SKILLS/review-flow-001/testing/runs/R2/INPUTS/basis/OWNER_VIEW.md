
Source: standards/EVALUATION.md; whole-member SHA256 b856cf04e2cf6ea0ba8b5f9de8b455a3a5f95cdb05fe7337f077f1b7547c7485; bytes [37254,46864); exact source section below.

## 3. Independent assessment

A constructor's self-review is construction output, not assessment. Where
promotion needs independent assessment, the assessor evaluates the exact
live subject, authority paths, proof and installed state, not the
constructor's summary (P6, and P0 with its premise that a step's output is
a candidate until evaluated; instance premise (c) of §1 Foundation to law).
This section decides what counts as independent assessment. Which
boundaries require it is a policy choice of the Spec Method, owned by
[TICKETS §7 Execution and verification authority separation](TICKETS.md#execution-and-verification-authority-separation-up-007);
a governing basis may add boundaries.

Protocol: where method qualification applies
([§7 Method self-qualification](#method-self-qualification)), the subject is
frozen by identity before material reference exposure; elsewhere it is
stabilised by an immutable identity or an equivalent exact-subject relation
sufficient for the claimed assessment. The assessor records its
expectations from the governing source before opening the candidate; it
reads the subject at that identity or relation, never a mutable working
tree; it makes no repair; it does not assess its
own authorship. Reusing the constructor's judgment does not satisfy
independence; shared mechanical evidence may be reused, judgment may not
(ACTIVATION §7). Binding a returned assessment to its producer, subject,
basis and evidence authenticates the result; it establishes neither the
assertion provenance of its expected answer nor the execution provenance
of its run, which
[FOUNDATIONS §4 Parallel derivation and mutual assurance](FOUNDATIONS.md#parallel-derivation-and-mutual-assurance)
requires separately (P6, P3). Membership in a plan authenticates nothing,
an unauthenticated result satisfies no required assessment, and a result
bound to another subject satisfies no planned assessment
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results));
no cryptographic or transport protocol is prescribed for the binding (P6). Any post-exposure revision is a declared intervention: it
is either a method constituent with its own qualification boundary or a new
qualification subject, and it cannot retroactively make the original
frozen construction pass. This law prescribes no actor type or count,
review-round count, engine, prompt or orchestration (P6).

Author identity is the party responsible for the content of a realised
subject. It is distinct from actor identity, whoever performs one
operation, which is an identity and not an authority
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds)).
Authorship is one of the conditions on
which the independence of an assessment rests; the evidence conditions are
the other (P6, P3).

Reporting a defect, supplying a counterexample or identifying behaviour
already required by governing law does not by itself author the realised
subject. Contributing wording, design or policy that is adopted into the
subject, including through directions for a particular repair, is authorship
of that contribution. A
reporter may assess a later repair only when the existing assessment grant,
authorship relation and evidence-independence conditions permit it; a
reporter gains no review authority from having found the defect. A person
who authored an adopted repair cannot supply its required independent
assessment by calling that authorship a finding (P6, P3).

Independence rests on authorship and on the evidence conditions above, not
on a new context. The assessor may read the same governing sources as the
constructor. A fresh context alone establishes no independence, and it
supplies no review authority the author lacks: an author that opens a
fresh context to review its own candidate is still its author, and its
review is self-review, which stays construction output and cannot be
relabelled as independent assessment (P6;
[TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007)). A contribution received from another author stays that
author's wherever it is carried, and that author's reading of it supplies
no independent acceptance of it (P6).

Independence across actor families is declared, not assumed. Whether two
activations of one model family are independent for a semantic judgment is a
policy the governing basis states for the claim; the default where it is not
stated is that they are not independent.

## 4. Review results

A review returns one core result
([FOUNDATIONS §4, Results](FOUNDATIONS.md#results)) for each declared
predicate it evaluated, with: the exact subject and basis, the evidence
consulted, the findings ranked by consequence, each finding's evidence and
the smallest bounded correction, the residual uncertainty, and the
invalidation conditions. A declared predicate the review planned and did
not evaluate has no result (FOUNDATIONS §4, Results). The review names it
as not performed and reports no core value for it, neither
`indeterminate` nor `falsified`, so that conjunction keeps it apart from
an undecided predicate and from required coverage that no planned
assessment addresses
([FOUNDATIONS §4, Conjunction of results](FOUNDATIONS.md#conjunction-of-results);
P5, P6). It may recommend a disposition
([ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition)), which is
evidence only and never a disposition; it does not apply one. A finding
without evidence a consumer can chase is commentary.

### Result and triage projection

Where a review returns findings with technical triage, the triage is the
assessor's evidence-bound assessment of each finding against the exact
evaluated claim and basis. Severity, the assessor's grade of consequence,
is evaluation evidence. Priority, the effect on the current promotion
boundary and the disposition are the decision owner's (ACTIVATION §1,
Roles and delegation; when a finding can block is
[§5, When a finding blocks promotion](#when-a-finding-blocks-promotion))
and stay distinct values even where a
Product-defined policy maps one to another. A recommended disposition
is evidence for the decision owner: it is not a disposition, a
priority or a boundary effect, and it is never adopted mechanically (P6,
RF-007). The fields of a triage are declared by the profile that adopts it, and
the scales it uses are bound by the adopting Product (P2, P6).

The projection of the finding-level triage payload is total over the core
values of [FOUNDATIONS §4, Results](FOUNDATIONS.md#results). A predicate
not performed has no result and so no triage payload; the payload class
`indeterminate` never stands for it. The payload classes `complete`,
`indeterminate` and `not_applicable` classify the triage only; they are
not new results, dispositions, priorities or lifecycle states (P5, P1).

| Core result | Finding and triage payload | Decision-owner consumption constraint |
|---|---|---|
| satisfied | an explicit no-finding state; triage `not_applicable`; evidence, residuals and invalidation stay present | priority and boundary effect are `not_applicable` to this result unless another exact consumed result supplies a finding |
| falsified | one or more exact findings; triage `complete` where supported, keeping `indeterminate` fields where evidence cannot close them | apply the Product-owned priority and boundary policy without mapping severity mechanically to a disposition |
| indeterminate | a partial finding or observation state; triage `indeterminate`; the exact evidence gaps and residual uncertainty | keep the uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or as a closed finding |
| out_of_frame | the evaluated claim needs an undeclared material relation or evaluator capability; triage `indeterminate`; the missing relation or capability and the exact reconfiguration pressure are named | refine or reconfigure a capable activation and keep the claim unresolved; do not consume the result as satisfaction or falsification |
| invalid_basis | a basis failure; triage `not_applicable`; invalidation evidence and basis-repair pressure | refuse to consume the result and return through the declared basis re-entry relation |

An adjacent observation outside the evaluated claim does not replace the
claim-relative result. The assessor returns it separately, with triage
`not_applicable` to that claim and the exact repricing or re-entry
pressure; the decision owner returns it to its declared owner without
creating a claim-relative block, or another review round, from its
severity alone (P6, P2).

The assessor returns to the decision owner, not to the constructor. It does
not edit the candidate, direct the repair or authorise continuation (P6,
§3).

Recording the assessment is a separate artifact effect. Where the activation
grants it, the assessor may write the exact named findings carrier under
[TICKETS §4 Review findings and bug items](TICKETS.md#review-findings-and-bug-items).
That grant adds no candidate-repair authority or acquisition route. A review
has covered its declared subject only when every planned predicate has been
evaluated or lawfully removed from that subject; a partial return preserves
the unperformed coverage. Closing the review activity does not satisfy a
falsified or unresolved work claim (P6, P5).

Purpose and material relation: every configuration keeps severity,
priority, boundary effect and disposition separate. The rule applies to any
assessor and decision owner; [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md)
binds its Reviewer and Executive instance (P6).


Source: standards/EXECUTIVE_BASELINE.md; whole-member SHA256 00cd728cf24b67511ad6dc58f4d10e147a444a551fdec242cd72e88417cf0801; bytes [95263,99896); exact source section below.

## 10. Derived Reviewer frame

(P6, P5)

| Frame element | Reviewer |
|---|---|
| evaluation family | Is this the exact claimed subject and basis? Does it satisfy the applicable method and project relations without competing authority, proof masking or an unevaluated composition boundary? For each finding, which evidence-bound severity and technical implications follow? |
| subject and basis | exact candidate, claim, governing method and project authority, scope, exclusions, evidence population, Product-selected severity scale, review carrier and declared independence conditions |
| material manifold | claimed relations; causal producers and consumers; authority seams; competing paths; failure, recovery, installed and reconstruction surfaces where claimed; test and fixture semantics; historical counterexamples; a finding's cause, blast radius, workaround, repair complexity, regression risk and uncertainty where supportable |
| coordinates | exact candidate, source basis, authority revision, configuration, dependency, evidence population, severity scale, installed subject, review time and Reviewer identity |
| governing invariants | RF-001 to RF-017; the execution relation (ACTIVATION §1 and §3); independence and traceability (EVALUATION §3); assurance boundary and qualification freeze (EVALUATION §1, §3 and §7); applicable Product, design, identity and release law |
| authority | bounded evaluation only; review access yields no construction, transformation, admission, publication, mutation, decision, disposition or next-activation authority |
| evidence | independently acquired live authority, candidate implementation, tests, artifacts, history, operational evidence, mutations, replay or reconstruction, and reproduced observations material to the claim and the technical triage |
| capability envelope | declared method, domain, implementation, assurance, technical-triage, tool, access, context, counterexample-search and independence competence |
| exclusions | editing the candidate, implementing a repair, assigning priority, disposing the release or MVP boundary, selecting the next action, substituting the Worker's summary, assurance-owned semantic reconstruction, flattening unbound evidence, silent scope expansion |
| result | one core result with findings, counterexamples, evidence-bound technical triage and residuals sufficient for the Executive to assign priority and apply the existing disposition where the basis is decidable |
| invalidation | a material change of candidate, authority, basis, evidence population, severity scale, dependency, configuration, scope or independence |

When independent review is required, and what makes a claimed review
traceable, are
[TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007),
with the further boundaries a governing basis adds; what counts as
independent is [EVALUATION §3](EVALUATION.md#3-independent-assessment);
EVALUATION §1, §3 and §7 decide the exact assurance boundary and the
qualification freeze. This profile adds no universal review round and no
new independence test (P6).

ACTIVATION §1 and §3 stay the owners of assessment and disposition. This
profile uses an activated Reviewer result as independent live-surface
evaluation input and, in the coordinated branch, the Executive as the
authorised assessor or proxy that applies the one existing disposition. It
creates no second verdict or disposition family (P6, P5).

The Reviewer may assess likely repair complexity and regression risk
without becoming the repair owner. Where cause, blast radius, workaround or
repair risk cannot be supported inside the activation, the result records
that uncertainty instead of manufacturing a complete triage (P5).

Tests are inside the Reviewer's manifold when their code, fixtures,
mutations, environment or interpretation can change the proof claim; a
passing result is not relied on in place of reviewing those semantics (P6,
EVALUATION §1).

Each finding binds a violated property, a supported entry or state, the
governing operating or threat model and a credible causal path. The same
conditions apply to retained guards and acceptance predicates as to new
findings. An excluded threat alone gives no retention claim; a proposed
wider threat model re-enters its owner. Internal location alone does not
establish trust, and hypothetical hostility alone does not establish
applicability. The actual untrusted-input, mutable-state, authority and
effect checks the supported model requires are retained. A suggested repair
becomes an obligation only through its proper owner (P6, P2, P5).


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

