# Reference frame member-build-assess

Task: Build or assess one member of this corpus: state its family table in the required format with premises, consequences, choices and pillars, keep one owner per rule with rivals referring or refining, dispose its predecessor claims, and assess it against the common conformance discriminators without self-review standing in for independent review.

Purpose: The owning sections for the foundation-to-law table format and family index, authority kinds, imports between members, the core result algebra, independent assessment and review results, successor dispositions, and the coverage of the common conformance discriminators.

Binds:

- This task binds the construction relation: A is the exact subject and basis the activation binds, Z is the task's required outcome with the acceptance conditions the task states, and the actor's claims keep preservation, progress and outcome satisfaction distinct, returning `unresolved` for what its evidence cannot decide (ACTIVATION.md#construction-relation sha256=53bfd10350317b6f39c99879b98d9edf4b3639b4a999c8521b63d97020c1017e)
- An evaluation this task returns binds the assurance relations: the source obligation, the claimed predicate and its scope, the observation basis, the exact subject and its material dependencies; a pass is an observation until the oracle's fidelity is established (FOUNDATIONS.md#assurance-relations sha256=7f2c74584606617409e00702f74940c601148a9f926489eab093ffdaaecccdcf)

A `Binds:` item names an obligation the activation of this frame binds, with
the owning section and the digest of its member where it names one; the item
copies no section and owns no determination. A changed owner changes the digest.

Each excerpt below copies one owning section of a member of this method
byte for byte, except a `rows=k/n` excerpt (see below) and except that
each relative link destination is rebased
to resolve from this directory to the same target. Fenced code, inline
code and absolute and `stdo://` links are unchanged. The `Source:` line
before an excerpt names the member and the section's anchor, and gives
the SHA-256 of the whole owning member. The section digest recorded in
FRAME_INPUTS.json is over the owner's bytes, not over this copy. The
owning section decides; this frame owns no determination. An excerpt
whose `Source:` line says `rows=k/n` is a family table of which only
the k rows that cite a section this frame carries are copied, with the
table's preamble, header and every non-family table; the other rows
stay in the owning member and are not copied. The frame's
qualification, not this selection, decides whether the frame is
sufficient for its task.

Routes, in order:

1. [FOUNDATIONS.md#authority-kinds](../FOUNDATIONS.md#authority-kinds)
2. [FOUNDATIONS.md#imports-between-members](../FOUNDATIONS.md#imports-between-members)
3. [FOUNDATIONS.md#foundation-to-law](../FOUNDATIONS.md#foundation-to-law)
4. [FOUNDATIONS.md#results](../FOUNDATIONS.md#results)
5. [EVALUATION.md#3-independent-assessment](../EVALUATION.md#3-independent-assessment)
6. [EVALUATION.md#4-review-results](../EVALUATION.md#4-review-results)
7. [RELEASE.md#9-successor-baseline-conservation-stdo-up-015](../RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
8. [CONFORMANCE.md#5-coverage-of-the-common-discriminators](../CONFORMANCE.md#5-coverage-of-the-common-discriminators)
9. [EVALUATION.md#foundation-to-law-claims-evidence-assessment-and-acceptance](../EVALUATION.md#foundation-to-law-claims-evidence-assessment-and-acceptance)
10. [EVALUATION.md#foundation-to-law-conformance-equivalence-and-qualification](../EVALUATION.md#foundation-to-law-conformance-equivalence-and-qualification)
11. [RELEASE.md#foundation-to-law-release-and-successor-conservation](../RELEASE.md#foundation-to-law-release-and-successor-conservation)

Size of this frame: 81491 bytes.

Source: FOUNDATIONS.md#authority-kinds sha256=7f2c74584606617409e00702f74940c601148a9f926489eab093ffdaaecccdcf

### Authority kinds

Authority takes these kinds (P6): frame-set authority, the human authority
that declares or accepts a project frame set; semantic authority, the
owner of meaning for a material relation; evaluation authority, the role
permitted to perform an evaluation; operation authority, the owner-issued
grant to construct, transform, admit, publish or mutate a material subject
where an evaluation performs such an operation; decision authority, the
role permitted to accept, reject or otherwise dispose a result; and actor
identity, the human, agent, tool or process performing the work, which is
an identity and not an authority. These may coincide in a lawful case and
never collapse by default. A read-only evaluation declares no operation
authority; an effectful evaluation inherits the exact operation grant from
its existing owner, and the frame does not create that grant (P6, P3).

What creates no authority. Authority of any kind exists only by an
admitted grant or an explicit authority decision of its owner, with an
identifiable basis. None of the following mints, widens, transfers or
reconstructs semantic, evaluation, operation or decision authority (P6,
P3):

- actor identity, an actor's capability, its tools or its access;
- a name, label, display label, status label, role name, capability
  string, locator, file name or path;
- declaring, naming, selecting, activating or executing a frame, or
  occupying a role;
- implementation reachability, a reachable code path or an available
  operation;
- the shape of evidence or of a payload, or the availability of evidence
  inside a frame;
- a passing check, a successful step, a completed review or a count of
  any of them;
- copying, interpreting, encoding, evaluating, transporting, projecting,
  compressing, importing or acquiring material;
- drafting, admitting or retaining a work contract, beyond what its owner
  has admitted;
- composition, delegation, adapters, wrappers and registries, which may
  restrict admitted authority or carry it faithfully, and never widen its
  scope, add a role, increase its cardinality or change its kind.

Elevation, transfer, split, merge, proxy grant, revocation and retirement
each need an explicit authority decision with an identifiable basis. A
member that names an instance of this list for its own domain cites this
paragraph and adds only the instance.

Proxy limit. Human authority may act directly, or through an explicitly
admitted bounded proxy where the governing identity and authority law
permits it; proxy identity and human-authority identity stay distinct
(P6, P3). A proxy acts only inside its existing grant. It cannot change
the governing outcome's meaning, the requirements, the governing authority
or the accepted design; such a change re-enters at its owning relation.
Proxy authority does not make a constructor's self-review independent,
confers no unrelated runtime or domain authority, and does not replace
direct human acceptance where the governing product or release law
requires it. The contents of a proxy grant are
[IDENTITY §6](../IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)'s,
and the decisions a proxy may take inside a step are
[ACTIVATION §1 Roles and delegation](../ACTIVATION.md#roles-and-delegation)'s.

Purpose and material relation of the list and the proxy limit: each
member that names what cannot create authority decides the same question,
so one list keeps the answer the same in every member, and a capability,
a label or a passing check can never be read as a permission (P6).


Source: FOUNDATIONS.md#imports-between-members sha256=7f2c74584606617409e00702f74940c601148a9f926489eab093ffdaaecccdcf

### Imports between members

A member that uses a concept another member defines imports it and does
not define it again (P1, P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution`,
whose semantic import adopts the cited meaning unchanged). An import is
reference-only. Source and target meanings are identical owner-qualified
references, not new local definitions. Direction is from the named source
to the importing context; loss is none and no translation or ownership
transfer is asserted. An import provides no semantic, evaluation,
operation or decision authority (P6; Authority kinds, What creates no
authority). A use that changes, narrows or loses
the source meaning is not an import and is never declared as one.

An import declaration states, for each imported concept (P1, P3, P6):

- what is imported: the concept, under the name its owner gives it;
- its owner: the owning section of the member that defines it, which is a
  place in the text, not a semantic authority (Authority kinds above);
- the source context: the bounded context the owning member declares, or
  that member itself where it declares none;
- the target context and the member that owns it;
- the direction and the loss, which one sentence may state for all the
  concepts of one declaration.

An import takes one of two forms. A declaration states these contents
for each imported concept in one place; between members of this corpus it
rests on the authority of the Product that owns the corpus, so the
relation is owner-authorised (P6). A reference at the point of use
that names the owning section is also an import: it states what is
imported and its owner; its source context is the one the list above
names, its target is the using member's context, and its direction, loss
and lack of authority are those stated above. A concept another member
defines enters a bounded context only by one of these forms, never by
proximity or equal spelling (P1, P3).

An activation binds each member's distinct coordinates in its selected
complete governing basis; equal cut selection does not mean equal member
coordinates. Adoption is a target's taking an imported concept into use
under the conditions its source states, which are its adoption premises.
Lifecycle and adoption remain source-owned. A changed member,
selected basis, source declaration or adoption premise requires fresh
applicability before use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before
dependent reliance rather than interpreting it from equal spelling (P3,
P5). For an evaluation that depends on the imported concept, a missing
source meaning, adoption or authority binding is an undeclared material
relation, the ground of `out_of_frame` ([Results](../FOUNDATIONS.md#results), Out of frame
or indeterminate); a changed member or basis whose applicability is not
yet re-established is the ground of `invalid_basis` (§4 Results).

Purpose and material relation of the declaration's contents, its two
forms, a member as source context and the two grounds above: a concept
used outside its owning section keeps one meaning and one owner, so two
members cannot answer one question two ways, and using a concept grants
no authority over it (P1, P6).


Source: FOUNDATIONS.md#foundation-to-law sha256=7f2c74584606617409e00702f74940c601148a9f926489eab093ffdaaecccdcf

### Foundation to law

A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in five columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](../PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".
  A row never files the whole rule as the choice: the choice is only what
  the premises leave open.
- Pillar: the pillar contributions the row helps account for, by number.
  The pillars are the ten contributions that the Foundational Reduction of
  the Product that owns this corpus names, in its order: 1 specification
  and project structure; 2 world models, identity and Markov objects; 3
  algebraic calculus; 4 functional design; 5 outcome-driven development; 6
  information and interpretation; 7 reference frames; 8 computational
  calculus and execution binding; 9 evidence, correction and authority; 10
  axiomatic calculus. That Product owns the contributions and their
  wording. A Pillar cell is a trace, like the rest of the table: it is not
  a premise, adds no standing to the row, owns no choice, and does not
  claim that a pillar is an axiom or follows from finite capacity.

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table, the members or sections the table accounts for, and the pillar
contributions its table's rows name, which are the union of its rows'
Pillar cells. A row marked table pending names the section that is to
hold its table; until that table is written, the row names its members
and traces none of their rules. A Pillar cell marked pending names no
pillar: the family's table does not yet carry the Pillar column, and the
cell is filled from that table's rows when it does. The index decides
nothing: each rule is in its owning section, and each trace is in its
table (P1, P6).

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](../REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](../ACTIVATION.md#1-the-step) | ACTIVATION §1 including the construction relation, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 8, 9 |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](../FOUNDATIONS.md#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 | 3, 4, 6, 7, 9 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](../ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 | 2, 4, 5, 6, 7, 9 |
| F5 | Proportionality and cost | [ACTIVATION §6](../ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority | 1, 4, 5, 6, 7, 8, 9 |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](../EVALUATION.md#1-claims) | EVALUATION §1 to §5 | 1, 2, 3, 6, 7, 8, 9 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](../EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE | 1, 3, 4, 6, 7, 8, 9 |
| F8 | Identity | [IDENTITY §1](../IDENTITY.md#1-position) | IDENTITY | 1, 2, 6, 7, 8, 9 |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](../AXIOMATIC_CALCULUS.md#1-position) | AXIOMATIC_CALCULUS | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](../SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 | 1, 2, 3, 4, 5, 6, 8, 9 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](../SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 | 1, 2, 3, 4, 5, 6, 7, 9 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](../PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) | 1, 2, 4, 6, 7, 8, 9 |
| F13 | Work carriers | [TICKETS §5](../TICKETS.md#5-from-carrier-to-execution) | TICKETS; POSTING_GUIDE §2, §7, §9 | 1, 2, 3, 4, 6, 7, 8, 9 |
| F14 | Assurance and testing | [ASSURANCE §1](../ASSURANCE.md#1-verification-layers) | ASSURANCE | 1, 3, 4, 5, 6, 7, 8, 9 |
| F15 | Release and successor conservation | [RELEASE §1](../RELEASE.md#1-context-and-position) | RELEASE; FOUNDATIONS §2 Product lineage objects | 1, 2, 3, 6, 7, 8, 9 |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](../EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE | 1–9 |
| F17 | Software design | [DESIGN_MODULE §1](../DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE | 1, 2, 3, 4, 5, 6, 7, 9 |
| F18 | Outcome-driven development | [ODD §1](../ODD.md#1-position) | ODD | 1–9 |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](../TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F20 | UX | [UX §1](../UX.md#1-position) | UX | 1–9 |
| F21 | World model | [WORLD_MODEL §1](../WORLD_MODEL.md#1-position) | WORLD_MODEL | 1, 2, 3, 5, 6, 8, 9, 10 |
| F22 | Assurance relations | [FOUNDATIONS §4 Assurance relations](../FOUNDATIONS.md#assurance-relations) | FOUNDATIONS §4 Preservation through construction, Assertions and observation, Parallel derivation and mutual assurance, Quantified assurance, Change impact and evidence reuse, Formal representation | 2, 3, 4, 6, 7, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §3 Construction synthesis relates the commitments to the
  construction relation that ACTIVATION §1 states and decides no outcome of
  its own. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the family-import rule, which families a profile imports and how a row cites them under the import rule of §2, that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations, no consequence is filed
as a choice, and no partial trace is presented as a derivation of the
whole method (P6, P2). The Pillar column binds each argument to the
contributions it helps account for, so a contribution that no row names
is visible as unaccounted (P2).


Source: FOUNDATIONS.md#results sha256=7f2c74584606617409e00702f74940c601148a9f926489eab093ffdaaecccdcf

### Results

Every performed evaluation returns one value of the core result algebra,
directly or as a refined value mapped into it (P5):

| Value | Meaning |
|---|---|
| `satisfied` | the declared predicate holds on the exact basis |
| `falsified` | a declared counterexample defeats it |
| `indeterminate` | the available admissible evidence cannot decide it |
| `out_of_frame` | the evaluation requires an undeclared material relation or capability |
| `invalid_basis` | the subject or basis cannot support the evaluation |

This core is the only one. Results of constraints, judgments, frame
evaluations, stops, work steps and effects are stated in it or in a
refinement mapped into it, so that results from any members combine under
one rule ([Conjunction of results](../FOUNDATIONS.md#conjunction-of-results)). Purpose and
material relation: no combination can report success while a failure, an
undecided question, an unperformed evaluation or an uncertain effect
remains, and none of these can be mistaken for another (P5, P6).

Recording. A result records its core value together with the predicate
evaluated and the original domain outcome, which is the refined value
where a refinement produced it. A mapping into the core never owns domain
meaning: the member, profile or adopting Product that defines the refined
value keeps it, and a consumer that needs the domain distinction reads the
domain outcome, never the core value alone (P1, P6).

Standing. The standing of a result is what it establishes about its
predicate; it is distinct from the standing of a commitment (§1). Only
`satisfied` establishes the predicate. `falsified` establishes that the
predicate fails and names the counterexample. `indeterminate`,
`out_of_frame` and `invalid_basis` establish neither, and each names what
would decide: the evidence, the missing relation or capability with its
owner where the subject gives one, or the basis repair. By support for the
predicate, `satisfied` stands above each other value, and the other four
are not ordered among themselves.

No refinement or mapping raises a result's standing (P5, P6):

- a falsified or failed result never maps to a satisfied or successful one;
- a result that admissible evidence cannot decide never maps to
  `satisfied`;
- an evaluation that was not performed stays distinct from one whose
  evidence cannot decide: it has no
  [closed result](../ACTIVATION.md#7-closed-result-and-reuse), and it is never mapped
  to `indeterminate` or to any other core value;
- an effect whose completion is unknown never maps to no effect or to
  completed.

Not performed. An evaluation that is required or planned and was not
performed has no closed result; an actor cannot report an evaluation it
did not perform (P6). Nothing is coerced to success: a failed,
indeterminate, out-of-frame, out-of-scope or invalid-basis result follows
the declared result algebra and returns its own value under it, never
`satisfied`, and a missing result, being no result, enters every
conjunction over it as a gap: a planned assessment without a closed result
where an assessment was planned, and uncovered coverage where none was.
This
conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
whose five values the table restates unchanged, and
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
whose rule that a failed, missing, indeterminate, out-of-scope or
invalid-basis result follows the declared algebra rather than being
coerced to success is the sentence before; both are restated here once.
[REFERENCE_FRAME §3](../REFERENCE_FRAME.md#rf-012-closed-results) states
RF-012 as a law over frames and
[AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
states AC-007 as a law over constraints; each uses this core and neither
defines it again.

Refinements. A member, profile or adopting Product that needs finer
outcomes defines a refinement. The refinement names the question it
answers and the predicate its mapping is for, and maps every refined value
to exactly one core value. No outcome exists outside the core; a
refinement adds no core value and keeps the pressure of `indeterminate`,
`out_of_frame` and `invalid_basis` explicit. Where a refined value would
map to one of two core values according to its cause, the cause is part of
the refined value and each resulting value maps once (P5, P1). A further
refinement, by a member, profile, project or adopting Product, may split a
refined value by cause. The parent-value rule governs every such split:
each child value names its parent value and its cause and keeps its
parent's core value; a child that needs a different core value needs a
different parent value, which only the owner of the parent declares; and
no child takes `satisfied` from a parent that is not `satisfied`. No
further refinement raises a result's standing (P5, P6, P1). Purpose and
material relation: a consumer that reads a parent value reads the same
core value from each of its children, so a split by cause adds a domain
distinction and never changes what the parent establishes (P5, P6). The
refinements for admission, activation and steps are
[ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition); each other
member, profile and adopting Product states its mapping where it defines
its values.

Availability, assessment and acceptance are separate results, each with its
own predicate: that a step produced a candidate; that the candidate meets
its declared criteria; and that the
[decision owner](../ACTIVATION.md#roles-and-delegation) accepts it at its
boundary. A step having produced a candidate never maps to the candidate's
fitness or acceptance, and acceptance is never inferred from a successful
step (P6; [ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition),
[EVALUATION §4](../EVALUATION.md#4-review-results) and
[§5](../EVALUATION.md#5-acceptance)).

Out of frame or indeterminate. The boundary between these values is drawn
on what the activated frame declares and on what the step did with it (P5,
finite capacity and graceful total handling; the material relation drawn
is the three-way out_of_frame boundary: capability not declared, capability
declared and exercised, capability declared and not exercised; rc.2 RF
#rf-012-closed-results). Three cases; the first two name core values, and
the third names none:

- `out_of_frame` when the claim requires a material relation or an
  evaluator capability that the activated frame does not declare. The
  result names the missing relation or capability, its owner where the
  subject gives one, and the reconfiguration pressure it creates
  ([ACTIVATION §4](../ACTIVATION.md#4-totality-and-refinement); rc.2 RF
  #reconfigure-when-necessary). A term the claim depends on and the frame
  leaves undefined is an undeclared material relation: its meaning can
  alter the result and it enters through no declared input (rc.2 RF
  #material-relation, RF-003; P1). Whether the step exercised anything is
  irrelevant to this value; the ground is the missing declaration.
- `indeterminate` when the available admissible evidence cannot decide the
  claim (rc.2 RF-012). The result names the evidence that would decide, as
  its residual uncertainty (rc.2 RF #return-a-closed-result). Where the
  claim also depends on an undeclared relation or capability,
  `out_of_frame` and `indeterminate` each have a lawful ground; the result
  names the value it returns and that ground, and this boundary excludes
  neither (P5).
- no value of its own when the step did not exercise a declared capability
  the evaluation requires. A result is returned wherever a sufficient
  evaluation or an applicable judgment exists without that capability,
  identifying its evidence, verdict and residual uncertainty like any
  closed result (rc.2 RF #rf-012-closed-results, #return-a-closed-result):
  a counterexample found by what was exercised, as when source inspection
  falsifies A in a claim of A and B, returns `falsified`, and common
  agreement cannot discard it (rc.2 RF #result-conjunction). Where none
  exists because the capability was not exercised, the evaluation was not
  performed and has no result: the step's stop state carries it,
  `incomplete` under
  [construction availability](../ACTIVATION.md#construction-availability), and
  its work state ([ACTIVATION §5](../ACTIVATION.md#5-work-state-and-restart))
  carries the unexercised capability as a residual (P6). In either case
  the unexercised part, B above, has no result: in every conjunction over
  it, it is a planned assessment without a closed result, and the known
  failure A survives with it ([Conjunction of results](../FOUNDATIONS.md#conjunction-of-results)).
  The evaluation's result and the step's stop state answer different
  questions, so the step's stop value never becomes the evaluation's
  result.

Foundation to law for results and their combination (family F3). The
table covers every rule of §4 and the result grounds of §2 Imports
between members, in the format of
[Foundation to law](../FOUNDATIONS.md#foundation-to-law), which states the standing of its
consequences. Purpose and material relation: a reader of §4 sees which
commitments each result rule rests on and which choices it adds, with their
owners (P6, P2). Instance premises, which the commitments do not supply:
(i) an evaluation declares its predicate, subject and basis; (ii) results
of several evaluations, steps or members are combined into one decision;
(iii) members, profiles and adopting Products need outcomes finer than the
core.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P5 (derived from P0 and P6), P6 (independent); (i), (ii) | every performed evaluation returns one closed value of one algebra shared by every member, with a value for a claim that holds, one that fails, one the evidence cannot decide, one that needs a relation or capability the frame lacks, and one whose basis cannot support it | [Results](../FOUNDATIONS.md#results), the value table | the value names, and the division of P5's outcomes other than success into `indeterminate`, `out_of_frame` and `invalid_basis`, conserved from RF-012; owner: this section | 3, 9 |
| P6 (independent), P5 (derived from P0 and P6) | a result claims no more than it establishes: only `satisfied` establishes the predicate, and no refinement or mapping raises a result's standing | [Results](../FOUNDATIONS.md#results), Standing, and the rule that nothing raises standing; for the choice, [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Reported value | the order among the four other values within one combination; owner: the member or profile that applies the conjunction, in its declared rule | 9 |
| P1 (independent), P6 (independent); (iii) | a core value alone does not carry a refined value's domain meaning, so a result records its predicate and domain outcome, and the definer of a refined value keeps its meaning | [Results](../FOUNDATIONS.md#results), Recording | each refined value and its domain meaning; owner: the member, profile or adopting Product that defines it | 6, 3 |
| P6 (independent) | an evaluation that was not performed supports no claim, so it has no closed result and is never read as undecided | [Results](../FOUNDATIONS.md#results), Not performed, and the third item of the rule that nothing raises standing | recording non-performance as the absence of a closed result, not as a core value; owner: this section | 9 |
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](../FOUNDATIONS.md#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile, project or adopting Product that defines it | 3, 6 |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](../FOUNDATIONS.md#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](../EVALUATION.md#5-acceptance) names | 9 |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](../FOUNDATIONS.md#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](../ACTIVATION.md#construction-availability), construction availability | 7, 9 |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](../FOUNDATIONS.md#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none | 6 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none | 3, 9 |
| P3 (independent), P5 (derived from P0 and P6), P6 (independent); (i), (ii) | a result supports its predicate only on the basis it binds, so a component held only on another basis has, on the basis the composite requires, no performed evaluation and is a gap, while an evaluation performed on a basis that cannot support it decides its own predicate as `invalid_basis`; one component is never answered both ways | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Stale results | none | 3, 9 |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains; with every mandatory result `satisfied`, agreeing bases and no gap, a material counterexample to a mandatory constraint falsifies it whichever contributor found it, and without one its value is the one its declared rule gives over the mandatory results; a `falsified` result that is not mandatory stays in its record | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, how results that are not mandatory count, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P4a (independent), P4b (derived from P0 and P2) | composed steps exist only under typed composition; the composite carries both steps' step-produced facts, and its result for the outer predicate is the conjunction over the outer contract's obligations | [§4](../FOUNDATIONS.md#4-algebra) Composition; [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Composition of results; [RF-010](../REFERENCE_FRAME.md#rf-010-composition-on-demand), outside this member | whether a composition law is needed, under the conditions RF-010 states; owner: the governing evaluation | 3, 4 |
| P4b (derived from P0 and P2), P3 (independent) | every transformation records what it preserved, introduced and removed, its external witnesses and its residuals, so no fact is lost unrecorded | [§4](../FOUNDATIONS.md#4-algebra) Conservation accounting | the record's fields; owner: [AC-013](../AXIOMATIC_CALCULUS.md#ac-013-transformation) | 3 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P0 (recovered) | a reference stands for a body only where it supports the same consuming decision; otherwise the shortfall is a residual, never success, and no carrier or budget limit trims a required member | [§4](../FOUNDATIONS.md#4-algebra) Reference versus body | none | 6, 7 |
| P1 (independent), P6 (independent) | two values differ lawfully only through a declared relation; preference, probabilistic choice and human presence supply none | [§4](../FOUNDATIONS.md#4-algebra) Latitude | each latitude or transformation relation; owner: the owner of the contract that declares it | 3 |
| P3 (independent), P6 (independent) | similar computation proposes shared machinery and never decides identity or authority; each instance keeps its responsibility and binding | [§4](../FOUNDATIONS.md#4-algebra) Shared machinery | whether one implementation serves several instances; owner: the accepted design of the realisation that would share it, which [DESIGN_MODULE §5](../DESIGN_MODULE.md#capability-and-foundation-selection-up-023) refines for software design where that profile is selected | 4 |
| P6 (independent), P1 (independent) | a categorical claim is established only with its demonstration, and without it is a hypothesis | [§4](../FOUNDATIONS.md#4-algebra) Formal fragment | which categorical claims are made; owner: the member, profile or adopting Product that makes the claim | 3 |

RF-012 in [REFERENCE_FRAME §3](../REFERENCE_FRAME.md#rf-012-closed-results),
AC-007 in
[AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
and [EVALUATION §4](../EVALUATION.md#4-review-results) apply the first row's
algebra to frames, constraints and reviews and add no choice of their own
beyond any refinement they map under the fifth row;
[ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition) holds the
step's refinements of the fifth row and the stop state of the seventh.


Source: EVALUATION.md#3-independent-assessment sha256=509f52ea65403e506336d826e2ee328c41faa85c21833a232d2588ec9804f395

## 3. Independent assessment

A constructor's self-review is construction output, not assessment. Where
promotion needs independent assessment, the assessor evaluates the exact
live subject, authority paths, proof and installed state, not the
constructor's summary (P6, and P0 with its premise that a step's output is
a candidate until evaluated; instance premise (c) of §1 Foundation to law;
conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)).
This section decides what counts as independent assessment. Which
boundaries require it is a policy choice of the Spec Method, owned by
[TICKETS §7 Execution and verification authority separation](../TICKETS.md#execution-and-verification-authority-separation-up-007);
a governing basis may add boundaries.

Protocol: where method qualification applies
([§7 Method self-qualification](../EVALUATION.md#method-self-qualification)), the subject is
frozen by identity before material reference exposure; elsewhere it is
stabilised by an immutable identity or an equivalent exact-subject relation
sufficient for the claimed assessment. The assessor records its
expectations from the governing source before opening the candidate; it
reads the subject at that identity or relation, never a mutable working
tree; it makes no repair; it does not assess its
own authorship. Reusing the constructor's judgment does not satisfy
independence; shared mechanical evidence may be reused, judgment may not
(ACTIVATION §7). Any post-exposure revision is a declared intervention: it
is either a method constituent with its own qualification boundary or a new
qualification subject, and it cannot retroactively make the original
frozen construction pass. This law prescribes no actor type or count,
review-round count, engine, prompt or orchestration (UP-022).

Author identity is the party responsible for the content of a realised
subject. It is distinct from actor identity, whoever performs one
operation, which is an identity and not an authority
([FOUNDATIONS §2 Authority kinds](../FOUNDATIONS.md#authority-kinds)).
Authorship is one of the conditions on
which the independence of an assessment rests; the evidence conditions are
the other (P6, P3; provenance: the definition moves here from the build
binding terms of SPEC_METHOD §11, which refers to it).

Independence rests on authorship and on the evidence conditions above, not
on a new context. The assessor may read the same governing sources as the
constructor. A fresh context alone establishes no independence, and it
supplies no review authority the author lacks: an author that opens a
fresh context to review its own candidate is still its author, and its
review is self-review, which stays construction output and cannot be
relabelled as independent assessment (P6; UP-007 applied to a fresh
context). A contribution received from another author stays that
author's wherever it is carried, and that author's reading of it supplies
no independent acceptance of it (P6).

Independence across actor families is declared, not assumed. Whether two
activations of one model family are independent for a semantic judgment is a
policy the governing basis states for the claim; the default where it is not
stated is that they are not independent.


Source: EVALUATION.md#4-review-results sha256=509f52ea65403e506336d826e2ee328c41faa85c21833a232d2588ec9804f395

## 4. Review results

A review returns one core result
([FOUNDATIONS §4, Results](../FOUNDATIONS.md#results)) for each declared
predicate it evaluated, with: the exact subject and basis, the evidence
consulted, the findings ranked by consequence, each finding's evidence and
the smallest bounded correction, the residual uncertainty, and the
invalidation conditions. A declared predicate the review planned and did
not evaluate has no result (FOUNDATIONS §4, Results). The review names it
as not performed and reports no core value for it, neither
`indeterminate` nor `falsified`, so that conjunction keeps it apart from
an undecided predicate and from required coverage that no planned
assessment addresses
([FOUNDATIONS §4, Conjunction of results](../FOUNDATIONS.md#conjunction-of-results);
P5, P6). It may recommend a disposition
([ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition)), which is
evidence only and never a disposition; it does not apply one. A finding
without evidence a consumer can chase is commentary.

### Result and triage projection

Where a review returns findings with technical triage, the triage is the
assessor's evidence-bound assessment of each finding against the exact
evaluated claim and basis. Severity, the assessor's grade of consequence,
is evaluation evidence. Priority, the effect on the current promotion
boundary and the disposition are the decision owner's (ACTIVATION §1,
Roles and delegation; when a finding can block is
[§5, When a finding blocks promotion](../EVALUATION.md#when-a-finding-blocks-promotion))
and stay distinct values even where a
Product-defined policy maps one to another. A recommended disposition
is evidence for the decision owner: it is not a disposition, a
priority or a boundary effect, and it is never adopted mechanically (P6,
RF-007). The fields of a triage are declared by the profile that adopts it, and
the scales it uses are bound by the adopting Product (P2, P6; provenance
[reviewer result and triage projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection)).

The projection of the finding-level triage payload is total over the core
values of [FOUNDATIONS §4, Results](../FOUNDATIONS.md#results). A predicate
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

Purpose and material relation of this projection's generality: the
predecessor stated it for the Reviewer and the Executive only. Stating it
for any assessor and decision owner gives every configuration the same
separation of severity, priority, boundary effect and disposition, and
EXECUTIVE_BASELINE keeps the Reviewer and Executive instance (P6).


Source: RELEASE.md#9-successor-baseline-conservation-stdo-up-015 sha256=6901b148a0cca05ae85bab6439e9f0178f1a1fa904b49383d83445af57e6f93b

## 9. Successor baseline conservation (STDO-UP-015)

A successor identifies the exact predecessor immutable RC whose semantic
claims it evolves. That origin remains immutable for the candidate. Every
predecessor claim capable of affecting the successor receives one semantic
disposition (P4b, P3, P6;
rc.2 #successor-baseline-conservation-stdo-up-015):

- conserved: the successor retains the claim;
- superseded: an accepted successor relation replaces it;
- intentionally removed: current Product authority removes it; or
- not applicable: it has no successor effect, with a bounded reason.

An unresolved disposition blocks qualification of the affected claim.
Conservation is semantic: patch absence does not prove loss when a
successor-native realisation preserves behaviour, and naming or code
similarity does not prove conservation without relevant evidence (P6,
P1). The comparison that decides `conserved` is made on the same material
case, scope and authority: what must happen, what may happen, what is
prohibited, and what follows when a trigger, exception or required
premise is absent, in the owning text and in the consumer bindings that
apply it, with the counterexamples that would expose a changed decision.
Modal wording is judged by that meaning: indicative wording can state a
binding law, and rewriting "must" or "shall" is neither conservation nor
supersession by itself; an obligation stays obligatory, a preference
stays a preference, and every permitted exception and scope condition
survives, or the claim is not conserved. A statement that a whole
package's wording is equivalent establishes none of this for any claim
(P6, P1; the common successor disposition requirement, carried here as
the test this section applies). A `conserved` disposition recorded
before this test applied is re-evaluated under it before the affected
claim qualifies; until then its standing is `unresolved`.

Each disposition is a claim the successor makes about one predecessor
claim ([EVALUATION §1](../EVALUATION.md#1-claims)), not a result value; its
predicate is its value's wording above. It is distinct from the decision
owner's disposition of an assessed candidate
([ACTIVATION §3 Disposition](../ACTIVATION.md#disposition)), which is an
acceptance result. Qualification evaluates each
disposition on evidence and records a value of the core result algebra
([FOUNDATIONS §4 Results](../FOUNDATIONS.md#results)) with that predicate.
An unresolved disposition states no claim and so has no result: in the
qualification of the affected claim it is a planned assessment without a
closed result, which is why it blocks that qualification
([FOUNDATIONS §4 Conjunction of results](../FOUNDATIONS.md#conjunction-of-results),
Gaps). Purpose and material relation: a recorded disposition establishes
nothing until it is evaluated, so no disposition stands as a result (P6,
P5).

Where a maintenance or support line may affect retained claims, the
release basis identifies the watched source, observation boundary,
inclusion policy and successor candidate. Relevant changes receive
semantic disposition at material integration and exact-cut qualification.
The consumer owns its record, branch strategy, comparison and proof
mechanism (P4b, P6).

[EVALUATION §5](../EVALUATION.md#5-acceptance) states what acceptance
requires of the disposition record; it applies this section and is not
part of it (P4b, P6).


Source: CONFORMANCE.md#5-coverage-of-the-common-discriminators sha256=e8a3f3faa270a26515a39b4e3bbc8ece946f6ec48b11eadea682426966496f09

## 5. Coverage of the common discriminators

A logical-review check is a reviewer's reasoned reading: the reviewer
constructs a discriminator's situation against the text and finds whether
the text yields the expected distinction, or finds a counterexample or a
contradiction, without running anything (P6). Its result is a review result
under [EVALUATION §4](../EVALUATION.md#4-review-results), by a reviewer who
meets [EVALUATION §3](../EVALUATION.md#3-independent-assessment). A
structural or mechanical check of the text does not establish it
([EVALUATION §2](../EVALUATION.md#2-separation)), and it supplies no
actual-use evidence ([EVALUATION §7](../EVALUATION.md#frame-qualification)).

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
the one the [common conformance table](../../../../specification/conformance/README.md#member-conformance)
states; this member does not restate it.

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
pass ([FOUNDATIONS §4 Results](../FOUNDATIONS.md#results), Not performed), and
the logical review of its discriminators does not stand in for it. No
logical-review check is recorded for this revision: each is a planned
assessment without a closed result until a review records it
([FOUNDATIONS §4 Results](../FOUNDATIONS.md#results), Not performed).

Purpose and material relation: a reader sees, for each discriminator,
whether actual use or only a reasoned reading exercises it and which
sections it reads, so a discriminator mapped to a case that has not been
run and assessed is never counted as passed, and no mapping exempts a
member from logical review (P6, P2).


Source: EVALUATION.md#foundation-to-law-claims-evidence-assessment-and-acceptance sha256=509f52ea65403e506336d826e2ee328c41faa85c21833a232d2588ec9804f395 rows=7/17 selected by the anchors this frame carries

### Foundation to law: claims, evidence, assessment and acceptance

This family, claims, evidence, assessment and acceptance (F6 in the index
of [FOUNDATIONS §3 Foundation to law](../FOUNDATIONS.md#foundation-to-law)),
decides when a claim is supported, how it is assessed and who accepts it.
It covers §1 to §5 of this member. Its instance premises are: (a) claims
about exact subjects are relied on for promotion, closure or release; (b)
the evidence available is finite, and may observe a weaker or different
subject, or another basis, than the one claimed; (c) a constructing actor
may be probabilistic or otherwise fallible; (d) each boundary at which a
claim is relied on has a decision owner. They are conditions of the work
this family governs, not commitments, and do not follow from finite
capacity alone.
P0's premise that a step's output is a candidate until evaluated is cited
by name. The standing of the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](../FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated); instance premise c | By P6 assessment is a separate authority from construction, and by P0 and (c) a step's output is a fallible candidate until evaluated, so a constructor's self-review is construction output, not assessment; where promotion needs independent assessment, the assessor evaluates the exact live subject, authority paths, proof and installed state, not the constructor's summary | [§3](../EVALUATION.md#3-independent-assessment), first paragraph | the boundaries at which this method requires independent assessment: the Spec Method policy at [TICKETS, UP-007](../TICKETS.md#execution-and-verification-authority-separation-up-007); further boundaries: the governing basis of each promotion | 7, 9 |
| P6 (independent), P3 (independent); instance premise c | By P3 a judgment binds the exact subject it read, and by P6 and (c) the assessor's judgment must be its own, so assessment binds an exact subject: frozen by identity before material reference exposure where method qualification applies, and otherwise stabilised by an immutable identity or an equivalent exact-subject relation sufficient for the claim, never a mutable working tree; the assessor makes no repair and does not assess its own authorship. Shared mechanical evidence may be reused; the constructor's judgment may not. A revision after exposure is a declared intervention or a new qualification subject, and cannot make the original frozen construction pass retroactively | [§3](../EVALUATION.md#3-independent-assessment), Protocol | recording the assessor's expectations from the governing source before it opens the candidate: a policy choice of this section; actor type and count, review rounds, engine, prompt and orchestration: the governing authority, through the configuration of [ACTIVATION §1](../ACTIVATION.md#configuration); policies of this section: the assessor makes no repair, and a revision after exposure is a declared intervention or a new qualification subject; where the freeze applies: method qualification (§7) | 2, 7, 9 |
| P6 (independent); instance premise c | By P6 independence is a relation between the author and the assessor, and by (c) an author's judgment is fallible in a way that persists across its contexts, so independence rests on authorship and the evidence conditions, not on a new context, and the assessor may read the constructor's governing sources. An author that opens a fresh context to review its own candidate is still its author; its review stays self-review and cannot be relabelled as independent assessment. Independence across actor families is declared, not assumed | [§3](../EVALUATION.md#3-independent-assessment), the last two paragraphs | whether two activations of one model family are independent for a semantic judgment: the governing basis of the claim; the default where it is silent, that they are not: this section | 7, 9 |
| P6 (independent), P3 (independent); instance premise c | Self-review is construction output (P6), and identities are scoped by kind (P3), so the party whose self-review is excluded must be identified apart from whoever performs an operation: author identity, the party responsible for the content of a realised subject, is distinct from actor identity, and independence is judged against the author | [§3](../EVALUATION.md#3-independent-assessment), the author-identity paragraph | none | 2, 9 |
| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise) | By P6 a result must let its consumer check and dispose it, and by P5 an unevaluated predicate has no result, so a review result carries, for each predicate it evaluated, the exact subject and basis, the evidence consulted, the findings ranked by consequence with each finding's evidence and smallest bounded correction, the residual uncertainty and the invalidation conditions. A recommended disposition is evidence only and never a disposition, and the review applies none; a finding without evidence a consumer can chase is commentary | [§4](../EVALUATION.md#4-review-results), first paragraph | none | 3, 9 |
| P6 (independent), P3 (independent); instance premise d | By P6 and (d) a decision is the owner's, exercised directly or through a grant it admits, and by P3 a proxy's identity stays distinct from the human authority's, so a human decision may be exercised directly or through an explicitly admitted bounded proxy; a change a proxy cannot make, under FOUNDATIONS §2's proxy limit, re-enters at its owning relation | [§5](../EVALUATION.md#5-acceptance), the proxy sentences | what a proxy grant names: [IDENTITY §6](../IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004); what a proxy can never decide: [FOUNDATIONS §2 Authority kinds](../FOUNDATIONS.md#authority-kinds); whether a proxy is admitted, with its scope and exclusions: the human authority that grants it | 9 |
| P6 (independent), P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance premise a | By P4b and P3 a successor's predecessor claims persist and bind exact identities, and by P6 and (a) acceptance relies on qualified claims, so where the subject is a successor its acceptance evidence includes the successor disposition record. A claim whose disposition is unresolved cannot be qualified and so cannot be accepted; an intentionally removed disposition is a decision of the current Product authority, and its record is that decision | [§5](../EVALUATION.md#5-acceptance), second paragraph | the disposition values and how the record is evaluated: [RELEASE §9](../RELEASE.md#9-successor-baseline-conservation-stdo-up-015) (family F15); each removal: the current Product authority | 1, 9 |

The core result a review returns for each evaluated predicate, the rule
that a planned predicate not evaluated has no result, and the projection of
the triage payload over the core values (§4) apply the core result algebra;
they are traced in family F3 at
[FOUNDATIONS §4 Results](../FOUNDATIONS.md#results), and the rows above trace
what §4 decides about the review record, triage and returns.


Source: EVALUATION.md#foundation-to-law-conformance-equivalence-and-qualification sha256=509f52ea65403e506336d826e2ee328c41faa85c21833a232d2588ec9804f395 rows=1/12 selected by the anchors this frame carries

### Foundation to law: conformance, equivalence and qualification

This family, conformance, equivalence and qualification (F7 in the index of
[FOUNDATIONS §3 Foundation to law](../FOUNDATIONS.md#foundation-to-law)),
decides when a realisation, a frame or the method itself is shown fit for
what it claims. It covers §6 and §7 of this member and the
[CONFORMANCE](../CONFORMANCE.md) member; a rule in CONFORMANCE is marked
"outside this member" in the third column. Its instance premises are: (a)
one specification may have several realisations; (b) realisations, frames
and the method are made by fallible constructors and relied on by actors
who did not make them; (c) qualification evidence comes from a finite set
of cases, run by actors inside declared envelopes. They are conditions of
the work this family governs, not commitments, and do not follow from
finite capacity alone. P0's actor-change premise, that the actor of one
step need not be the actor of the next and may re-acquire declared sources
but not private memory, is cited by name. The standing of the consequences
below is stated in
[FOUNDATIONS §3 Foundation to law](../FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premise c | By P6 a pass is an assessor's verdict on evidence, and by P5 an evaluation not performed has no result, so a conformance case names its subject, the mechanism under test, an independently specified expected distinction and its status, and a status names what exists. A run is not a pass: only an assessment by an independent assessor records one. A case passes when the expected distinction is observed and no coerced success appears anywhere in the result; a case that cannot be run with its declared subject is a planned evaluation that was not performed, which has no result under [FOUNDATIONS §4 Results](../FOUNDATIONS.md#results), so it is recorded as not run, never hidden and never given a core value | [CONFORMANCE](../CONFORMANCE.md), preamble, outside this member | the cases, with their subjects and expected distinctions: CONFORMANCE, from the common conformance discriminators and the builder's history | 3, 9 |

§8 records dispositions and decides nothing. CONFORMANCE §1 to §4 list the
cases, which are the choices named in the last two rows, its §5 maps the
common discriminators to cases and logical-review checks, and its §6
records dispositions.


Source: RELEASE.md#foundation-to-law-release-and-successor-conservation sha256=6901b148a0cca05ae85bab6439e9f0178f1a1fa904b49383d83445af57e6f93b rows=2/12 selected by the anchors this frame carries

### Foundation to law: release and successor conservation

This family (F15 in the index of
[FOUNDATIONS §3 Foundation to law](../FOUNDATIONS.md#foundation-to-law))
decides how a product's releases are identified, published, qualified,
accepted and selected, and how a successor conserves its predecessor's
claims. Its instance premises, which the commitments do not supply, are
named in the rows as follows: recursive products, a released product may
build other products and the next version of itself; published cuts, a
project publishes point-in-time cuts of its product for review, replay and
adoption by consumers it does not control; mutable carriers, the carrier
that holds a release has movable names and may hold several independently
released projects; derived assets, some products are released with
derived or distributed assets that must match their source; external
services, some claims depend on services outside the carrier; successor
lines, a product evolves from a predecessor release whose claims may
affect it. The index also assigns to this family
[FOUNDATIONS §2 Product lineage objects](../FOUNDATIONS.md#product-lineage-objects);
the table traces that section in its first two rows, whose rule column
names it, and owns none of it. Each commitment's standing is written as
the table of commitments in FOUNDATIONS §3 states it.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P6 (independent); P1 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: successor lines | By P4b and P3 a successor evolves one exact, immutable predecessor whose established claims persist, so it names that predecessor, and every predecessor claim that can affect it receives one disposition. By P6 and P1 a disposition is a claim evaluated on evidence, so naming or code similarity does not prove conservation, and a missing patch does not prove loss when a successor-native realisation preserves behaviour; by P5 an unresolved disposition leaves a gap, so the affected claim cannot be qualified. | [§9](../RELEASE.md#9-successor-baseline-conservation-stdo-up-015) | the four disposition values: this member, restating UP-015; each removal: the current Product authority; the record of a successor's dispositions: that successor's construction | 1, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P6 (independent); instance: successor lines | By P4b a change on a support line persists into what the successor retains, and by P6 its effect needs a disposition by evidence, so where a maintenance or support line may affect retained claims, the release basis names its watched source, observation boundary, inclusion policy and successor candidate, and relevant changes receive a disposition at integration and at qualification. | [§9](../RELEASE.md#9-successor-baseline-conservation-stdo-up-015), the support-line paragraph | the record, branch strategy, comparison and proof mechanism: the consumer; a policy of this member: the four items the release basis names (watched source, observation boundary, inclusion policy, successor candidate) | 1, 9 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](../FOUNDATIONS.md#foundation-to-law).
The table accounts for §1 to §9 and for FOUNDATIONS §2 Product lineage
objects. §10 records open questions and decides nothing; §11 records
dispositions and decides nothing.

