# Product

## Product Boundary

The product is a specification methodology. It consists of the documents stating its rules for defining, building, checking and releasing a product, together with their formal interpretation in the axiomatic calculus, a_c. The [Intent](INTENT.md) states its purpose; [Method Structure](#method-structure) defines its parts. Each document of the method is a member.

The method's earlier releases are named STDO, short for Specification, Ticketing, Design and Outcome-Driven Development. The prefix remains in identifiers: a `stdo://` address names a file inside an installed release, which the installed toolchain resolves to the read-only copy on this machine, and rule IDs such as STDO-UP-015 name rules of that release.

The product succeeds the method's previous release, 2.5.1-rc.2. That release is installed read-only at `stdo://releases/v2.5.1-rc.2/` (manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`) and is the tool used to build this one.

A predecessor claim is a rule or statement in the previous release that could affect the new one. Every predecessor claim is listed in [requirements/PREDECESSOR_CLAIMS.md](requirements/PREDECESSOR_CLAIMS.md). Each receives exactly one disposition: `conserved`, `superseded`, `intentionally removed` or `not applicable`. The previous release's own rule [STDO-UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015) requires this before a successor is accepted.

Under the [standalone successor requirement](requirements/README.md#standalone-successor-requirement), the product establishes its foundational commitments and reconstructs the method on them. Restatement requires foundation-to-law, ownership-and-use, standalone conservation and demonstrated reduction. Unchanged text is permitted when those relationships hold. The new release is complete without the previous release in force. Its size follows the obligations it must express; retaining an old member's layout or adding an explanatory layer does not establish reduction.

Each rule has one owning section, under [Method Structure](#method-structure) and the [single ownership requirement](requirements/README.md#single-ownership-requirement).

The method distinguishes three accounts of a construction. They apply across the tiers:

- the algorithmic description: the steps;
- the informational interpretation: what the data means;
- the computational realisation: how people, machines or combinations of them carry it out in a declared execution environment.

A tier may need all three. A category, equivalence or functor is established only when its claim meets the categorical demonstration standard.

Each candidate supplies and owns its interpretation of the method in a_c. The calculus, interpretation and encoded carrier have distinct content identities and proof boundaries under the [a_c dependency contract](requirements/A_C_DEPENDENCY.md). The Axiom Indexer checker and the existing released STDO Representation are separately owned Products. A candidate's interpretation does not replace either Product or inherit its acceptance.

Runtimes that execute applications built with the method are outside the product. Examples are ABIogenesis (ABG), which runs typed graph programs and records what happened at run time, its executor HoG, which traverses those programs, and application workflow runtimes.

Example applications, such as Hello World and Data Mapper, are test subjects outside the product. So is the sum-and-histogram example used by the steel thread. Their particular features never become general method rules because they were used once.

The product changes nothing in the 2.* line: not its source project, its releases, its companion products or the selection of versions released together. The companion products are the Axiom Indexer; the STDO Representation, which publishes the method's canonical a_c map, linking each axiom to its source text; and the plugin, which carries the method's skills for coding agents.

Construction proceeds through numbered checkpoints, C0 to C3, described under [Checkpoints](#checkpoints). The two candidate build tenants are described under [Source Project Construction](#source-project-construction).

## Foundational Reduction

The method recovers the essential contributions of the following pillars and expresses their shared laws once. These are related accounts of the method, not a prescribed document list, a fixed sequence of work or a claim that each is an independent axiom.

| Pillar | Contribution the reconstruction must account for |
|---|---|
| Specification and project structure | Purpose and destination constraints; refinement from common WHAT to independent HOW realisations; ownership of specification, design, work and commentary. Project structure expresses those relations. |
| World models, identity and Markov objects | Objects, boundaries, state and material relations; the evidence supporting a boundary and a claim that its observed state is sufficient. Ordinary bounded modelling does not establish stronger Markov properties. |
| Algebraic calculus | Objects, typed operations and laws for composing and transforming them. A lawful transformation states what it preserves and the conditions under which it applies. |
| Functional design | Apply typed contracts, composition, invariant preservation and explicit failure and effect boundaries to decomposition. Reuse transformations while retaining each domain's meaning and permissions. |
| Outcome-driven development | Construction through typed transitions toward a selected outcome, with evaluation, continuation, recovery and termination. Operation kind, actor and execution mechanism remain distinct. |
| Information and interpretation | The relationship between a subject, its representations and their meaning; the distinctions a projection, translation or compression must preserve for its consumer. |
| Reference frames | Task-sufficient acquisition under finite context and attention; bounded results and justified allocations of work, information and authority. |
| Computational calculus and execution binding | Describe the operations and composition laws by which work is carried out, including effects and resource measures. Bind that calculus to a concrete human, machine or mixed environment and establish that the binding satisfies its laws. |
| Evidence, correction and authority | Claims distinguished from observations and acceptance; changes driven by counterexamples and traced to their cause; permission and ownership distinct from capability or a successful check. |
| Axiomatic calculus | Explicit, recoverable representation of the method's logical constraints, dependencies, permitted latitude and residual uncertainty, usable to construct the constraint surface for a task. |

The [reduction requirement](requirements/README.md#foundational-reduction-requirement) owns the evidence needed to show how these contributions govern the method's deciding rules. Its arguments identify their applicable [foundational premises](requirements/PRINCIPLES.md), additional domain premises and consuming rules. A pillar names a required contribution, not an additional axiom or a claim of derivation from finite capacity. The [constraint-surface requirement](requirements/README.md#constraint-surfaces-and-logic-compression) owns the relationship between prose, a_c, bounded acquisition and permissible work. Domain-specific policies retain their own premises and owners. Finite resources alone do not supply purpose, identity, authority or compatible composition.

## Construction And Context Management

The method describes a current state A and a destination Z defined by constraints. Several realised states may satisfy Z. A distinguishes material workspace state from each actor's account of it. The workspace is the continuing truth surface for construction; context is acquired from it under the [current-state and basis rule](requirements/README.md#bounded-transitions-and-reference-frames). Unknowns remain explicit. Intent, Product and Specification progressively define the destination. Construction, observation and evaluation change the current state and what is known about it.

When the work exceeds one activation's capacity, it proceeds through bounded transitions A → B → C → … . Each transition retains the applicable outer obligations. Composition depends on compatible contracts and discharged preservation obligations. Discovery may add obligations or invalidate a claim. An authorised change may revise the destination; it does not establish that the previous destination was reached. Progress is judged against the selected outcome and evidence, rather than the number of remaining items alone.

Finite context and finite attention drive context management. Context bounds what an activation can hold; attention bounds what it can use effectively for its selected task. A reference frame selects sufficient relevant material and the task contract within those limits. Time, spend and other resources constrain the selected execution binding as applicable. The [bounded-transition and frame requirement](requirements/README.md#bounded-transitions-and-reference-frames) owns these obligations.

Roles and coordination structures emerge from allocating required operations and information to actors. Task dependencies require exchanges and compatible results; actor fallibility and incomplete knowledge motivate the applicable checking and recovery. Limited context and attention bound each responsibility. These conditions constrain a configuration without uniquely determining it. Functional decomposition, communication, authority and evaluation dependency remain distinct relations.

A realisation may use a hierarchy, peer coordination or an arrangement that adapts as actors allocate work within their contracts. Its design relates that choice to the task, actor capabilities, communication costs and required assurance. Several configurations may be adequate; an optimality claim is relative to stated objectives, constraints and comparison scope. Operational profiles and build tenants own these choices. The [construction binding](#construction-authority) selects one configuration for building this release.

## Method Structure

The method has three tiers of method law. The [C3 responsibility table](#c3-construction-contract) identifies their obligations and predecessor coverage inputs. Guides and packaging have supporting responsibilities; the conventions and formats they own bind work within their declared scope.

| Tier | Responsibility |
|---|---|
| Foundations | Shared commitments and contracts for interpretation, purpose, identity, composition, finite context and attention, evidence, authority, results and reference frames. |
| Spec Method | Product definition, requirements, construction, assurance, change, re-entry and release, using the foundational contracts. |
| Profiles | Domain or operational specialisations that import the shared contracts and own their additional bindings. |

The Spec Method develops a product through four descriptions:

- Intent states why it exists and the outcomes it must achieve.
- Product defines what it is, its parts and boundaries.
- Specification states its required behaviour, constraints and checks.
- Realisation supplies design, implementation and evidence against the specification.

Each refinement preserves the obligations above it. A material constituent repeats this structure where it needs its own bounded account. Work records, triage and review connect changes to the earliest affected description.

Profiles include outcome-driven development of typed graph programs, user-interface construction from typed state and messages, and world modelling over authoritative source systems. Operational profiles specialise the reference-frame contract through task catalogues and justified coordination arrangements. Guides own writing, posting and glossary conventions; packaging carries the method's members and entry points.

The a_c interpretation represents the method's laws, results and declared maps as a recoverable logic compression, retaining premises, dependencies, consequences, policy choices and unresolved conditions. Reference-frame projections select the governing constraint surface and material for a task from their owners. Interpretation and projection apply across the tiers; neither creates a second rule owner or an execution grant. Their fidelity follows the constraint-surface requirement; task sufficiency is evaluated through criterion 4 of the [C3 contract](#c3-construction-contract).

## Build-Tenant Binding

A build tenant binds the common requirements calculus to a computational calculus grounded in a real-world execution environment. It owns the design, realisation and evidence for that binding. The [binding requirement](requirements/README.md#build-tenant-binding-requirement) governs its conformance.

The requirements calculus comprises the obligations, permitted outcomes and rules for refining and composing the construction. The computational calculus describes executable operations, their composition and permitted transformations, with the effects and resource behaviour relevant to those obligations. Its execution environment supplies the concrete means: a technology stack, a human process or a combination. A human process can use people, roles, documents, communication channels and decision procedures.

The common specification bounds the permitted realisations. Each tenant selects its computational calculus and execution binding within those bounds. The algorithmic, informational and computational accounts apply across this relation. Formal representation in a_c supports checking the relation; it does not select its executor. A tenant's author and the actors that carry out its realised process are separate coordinates.

## Product Identity And Lineage

| Coordinate | Binding |
|---|---|
| Product line | the Specification Methodology, whose 2.* source project is `specification_methodology/v2/` (`urn:stdo:product-definition:specification-methodology`) and whose release namespace is `specification_methodology` |
| Release | the next major release on that line; its release identities follow the installed RELEASE_METHOD, the previous release's rules for cutting and publishing releases, in the same namespace |
| Predecessor | `stdo://releases/v2.5.1-rc.2/`, immutable |
| Source project | `specification_methodology/v3/`, beside the 2.* source project, which it does not overwrite |
| Identifiers | `urn:stdo:product-definition:stdo-3`, `urn:stdo-3:bounded-context:method` and the `urn:stdo-3:` tenant identities are identifiers, not names. They do not change with the directory or the display name. |

[stdo_3.json](../stdo_3.json) is the machine-readable Product Definition that the installed release's tools read to locate this source project. It carries this identity in its product name and in a local axiom that points to this section. A local axiom is a rule this source project adds on top of the installed release's law. Its schema has no version field.

## Result Algebra

The Foundations own the method's single result algebra: one set of outcome values, and one way of combining them, in which every result is reported. The following are stated in it or as refinements of it:

- constraint checks;
- review judgements;
- reference-frame evaluations;
- stops;
- work steps;
- effects (changes made to files or systems).

No member, profile or frame defines its own parallel set of evaluation or decision outcomes. A refinement gives finer outcomes for one domain. Its owner binds the predicate and the conditions that determine each value's meaning, keeps the original domain outcome alongside the core value, and never raises the result's standing. Recorded states remain distinct from judgments about those states. The precise obligation is the [single result algebra requirement](requirements/README.md#single-result-algebra-requirement). The [conformance discriminators](conformance/README.md), the common test cases every member is checked against, check it in every member under acceptance criterion 5 of the [C3 Construction Contract](#c3-construction-contract).

## Categorical Construction

Categorical construction is a general capability of the method. The method defines categories of its own constructs and joins between categories, which are maps from one category to another. It permits a construction step only where declared laws allow it. Specification documents are the objects. Derivations and refinements are the arrows, and each states what it must preserve. A join of an algorithm category with a computation category is the acceptance instance for the capability. The [categorical demonstration standard](requirements/README.md#categorical-demonstration-standard) states what each categorical claim must show; a claim without it is a hypothesis.

[CAPABILITIES](requirements/CAPABILITIES.md) requires every capability to have an acceptance contract: the principles that require it (the working foundations in [PRINCIPLES](requirements/PRINCIPLES.md)), its scope, its observable outcome and its conformance expectations. This capability's contract is derived from the steel thread's evidence at step 3 below. It has not been selected yet: the product owner has not chosen it for current work.

Sequence:

1. The Intent and this Product state the categorical direction, the axiomatic representation of requirements, the [build-tenant binding](#build-tenant-binding) to computation and concrete execution, and the demonstration standard.
2. One thin end-to-end example, the steel thread, tests the direction under the installed previous release.
3. The method is corrected from the steel thread's evidence.
   - Each finding goes back to the section that actually owns its cause.
   - A failure counts against the method only when triangulation places the cause in the method. Triangulation tests the candidate causes from several reference frames over the same subject.
   - Corrected clauses are reviewed independently.
   - The standalone successor requirement, member acceptance and release obligations stay in force.
   - The steel thread supports its own join only. It is not evidence that the whole method works.
4. The full categorical product is built on the released method.

Steel thread. Its subject is the sum-and-histogram example. A list of numbers is split across partitions. The example computes their exact sum, and an approximate quantile (such as the 95th percentile) from histograms built per partition. It belongs to no project, it stays outside the method's own members, and it runs under the installed release. Its minimum contract:

1. A stated purpose and the meaning of the inputs and results. The exact law for the sum. For the approximate quantile: the adequacy relation (how close is close enough), the quantile convention, how the buckets cover the range, and the output rule. The failure outcomes that matter.
2. The actual objects and arrows of the example's categories, when two arrows are equal, identity and composition, and each specific map claimed. Each is related to the algorithmic, informational and computational accounts.
3. One exact rewrite that splits the input and combines the partial results (partition and reduction). One bounded approximation. Each has explicit conditions and an argument that the end-to-end result is adequate.
4. Execution and comparison:
   - an exact oracle, a reference computation specified independently of the one under test;
   - two concrete execution bindings, which are two ways of running the computation;
   - a comparison of returned meaning, required effects and diagnostics;
   - a refused-input case and an interrupted or uncertain-effect case, run beside normal completion.
5. Measured latency, bytes moved and memory over a declared workload, with the measurement boundaries stated. The context, time and spend limits of the run that executes it are recorded. Only the cost and generality claims those measurements support are made.
6. The steel thread's own chain from Intent through Product and Specification to Realisation. Each derivation step is an arrow whose preservation obligation is stated and discharged. A failed derivation is attributed under step 3 and counts against the method only when triangulation places the cause in the method.

Reference design. The [category-of-algorithms design](../.ai-workspace/comments/claude/assets/20261001T133903Z_STRATEGY_a-category-of-algorithms-with-computation.compressed.md) is a reference design and the steel thread's subject matter. It is read with the [corrections](../.ai-workspace/comments/claude/20261013T012745Z_STRATEGY_categorical_groundwork.md#corrections-to-the-attached-design) in the categorical groundwork strategy. Its five layers are not method rules. They are: the domain calculus (algorithms and their laws); the computational algebra (distributed operations and the cost grade on each arrow); the computational calculus (lawful plans and rewrites); the workload (volumes, arrival rates and service levels); and the binding to a technology stack and operational model.

Three further ideas from that design stay unresolved until a real example needs them and supports them:

- the sheaf account, which says which computations can be split across partitions and glued back;
- a universal grade algebra, which is one way of composing every cost measure on an arrow (latency, bytes moved, memory, width);
- generality across a second domain.

## Dependencies And Acceptance

[The a_c dependency contract](requirements/A_C_DEPENDENCY.md) fixes the exact a_c theory and the exact, unchangeable Axiom Indexer release used for mechanical checks. The neighbouring Axiom Indexer Product Definition only says where to find that product; it does not fix the version.

The [conformance discriminators](conformance/README.md#member-conformance) supply the applicable checks for each member. Their separate construction and integrated-closure section checks those decisions. None of the following shows that a member's meaning is acceptable now: passing syntax checks, valid maps, the number of documents, a local approval or an earlier passing run.

## Source Project Construction

This source project is where the next release is written. It owns one common WHAT: the specification in `specification/`, which states what the product must be.

Two build tenants supply the HOW, authored respectively by Codex and Claude. Each supplies its own candidate of the product as documents under `build_tenants/<tenant>/`, applying the [build-tenant binding requirement](requirements/README.md#build-tenant-binding-requirement). Author identity alone selects no execution environment for the method the candidate expresses.

For this document construction, each tenant applies the [build-tenant binding requirement](requirements/README.md#build-tenant-binding-requirement) to its own method-authoring process in its existing design and work records, under the installed builder. Its candidate also states the binding rule that future consumers must apply. The candidate's rule does not replace the builder governing its own construction.

Their organisation, wording and a_c encodings may differ. Their accepted outputs satisfy the same common contract and the same independently specified expectations. The method a tenant's documents express is distinct from this common specification, which governs how they are built. A tenant design does not replace this Product definition, and the common WHAT is not replaced by a merge of the tenants' work. Selecting or combining tenant candidates for a release is the product owner's decision.

### Construction Authority

The common construction pen edits the common specification and records. Common changes receive review independent of their author before the product owner accepts them. Checkpoint commits on main provide review visibility; they do not supply acceptance. A review result informs the product owner's decision. The [frame basis](REFERENCE_FRAME_BASIS.md) binds the actors and their activations under the installed 2.5.1-rc.2 release.

Work is done in activations. An activation binds a capable actor to a selected reference frame, its subject and admitted authority. This source project's task-based construction separates two attention needs: carrying out a bounded change and managing delivery across successive tasks. The Executive retains the longer-term outcome and uses a sufficient bounded view of worker results to decide what follows. It requests further bounded evaluation when a decision needs more information. Independent assessment provides the checking required by this construction contract. These needs explain the selected responsibilities below; their named arrangement is one configuration under the installed builder:

- an Executive frame selects the next work and disposes results within its decision grant, with no file or Git mutation;
- a Worker frame constructs a bounded result; the Writer frame used here specialises it for changes to documents and records in an exact granted territory;
- a Reviewer frame assesses a frozen subject against the applicable contract, with independently acquired evidence, no repair grant and no assessment of its own authorship.

These frames organise context and attention for their respective tasks. Their names confer no authority. The existing grants below and in each activation supply the permitted effects and decisions.

C3 disposition grant. The installed rule for agent-performed construction, [STDO-UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020), defines the outcomes a coordinator can give each delegated result. This grant states which of those outcomes the Executive may give in C3.

A member restatement supplies successor-owned determinations and the relationships required by the [standalone successor requirement](requirements/README.md#standalone-successor-requirement). Its frontier cone is the rows of PREDECESSOR_CLAIMS it covers, with their supported dispositions. One shared successor owner may cover claims from several predecessor members; a predecessor member may also map to several justified successor owners. The requirement permits unchanged text; neither relocation nor rewriting alone establishes its relationships.

The Executive activation named in the [frame basis](REFERENCE_FRAME_BASIS.md#activations-and-owners) may dispose of a member restatement within its grant in four ways:

- `local_repair`: fix it locally, because the restatement is defective while the rule it implements is sound;
- `re_enter`: send it back to an upstream stage that must change;
- `reject`;
- `accept` into the tenant's candidate, only on the satisfied conjunction below and when every row of the member's frontier cone is disposed.

All six member acceptance criteria are mandatory, evaluated over the member's declared cone. The Executive binds that scope and the applicability of conditional obligations before assessment; the Reviewer verifies the cited conditions against the actual subject under the installed [Applicability And Required Results](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#applicability-and-required-results) rule. A false applicability condition excludes only that obligation, with its reason and source recorded. It introduces no new result value and does not waive a criterion. Unknown applicability remains unresolved. A criterion with no applicable conditional obligation can be satisfied only after that absence is established; omitted selected tasks or unchecked scope do not establish it.

The Reviewer returns one closed evaluation of the member's conformance, with one overall result and supporting judgments for all six criteria. Overall and criterion results use the installed Reference Frame Method family: `satisfied`, `falsified`, `indeterminate`, `out_of_frame` or `invalid_basis`. The overall result is the conjunction of those judgments under the installed [Result Conjunction](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#result-conjunction). The Executive applies that same owner when combining required evaluations for the disposition. Member acceptance requires all six criteria satisfied on the same exact candidate and governing basis. Missing evaluation, unknown applicability, stale or wrong-subject evidence, authorship conflict or another non-satisfied required result withholds acceptance. Component findings remain available: a known failure is not erased because another obligation is unresolved.

The product owner accepts any replacement that changes predecessor meaning, including a predecessor requirement. A change to this common specification likewise requires its owning common decision. The common pen records each decision and its exact replacement relations in the affected tenant ticket, citing any shared owner decision. Each dependent `superseded` row cites that record before member acceptance. One owner decision may accept a named set of relations; it need not be repeated per row. A construction grant, accepted general direction or a Reviewer's conformance finding does not by itself accept particular changed meanings. Relocation that preserves meaning remains conservation. The Executive's member acceptance evaluates conformance to the selected contract and grants no additional authority to change that contract.

Acceptance of the C3 checkpoint, every merge to `main`, every `intentionally removed` disposition and the release decisions remain the product owner's. The Reviewer supplies severity as evidence. Priority, boundary effect (whether the result changes what may be promoted towards a release) and disposition are the Executive's decisions. The common pen, not the Executive activation, records each as a separate entry in the ticket, which is the work carrier.

[build_tenants/README.md](../build_tenants/README.md) states how a tenant starts work and returns results. A tenant's changes stay inside its grant, and a change it needs in common files is requested from the common pen. An Executive cannot write files or perform Git operations in that role.

### Development Isolation

These are local development rules for this source project. They govern how tenant work is kept apart and merged, and they change no installed rule and no release cut.

- Lineage. `main` is the sole lineage of this source project. The common
  WHAT (`specification/` and the Product Definition) and common work records
  are written on `main` by the common pen. An authorised Reviewer writes its
  own review under `.ai-workspace/comments/<reviewer>/`; this grants no
  change to the common definition, tickets or another reviewer's text. Frozen reviews are
  retained as written; a later review or response names its own subject.
- Tenant branches. Each build tenant works on a short-lived topic branch
  `tenant/<tenant>/<checkpoint>` cut from `main`, in its own git worktree,
  with a sparse checkout limited to `specification_methodology/v3/specification/`,
  `specification_methodology/v3/.ai-workspace/` and its own
  `specification_methodology/v3/build_tenants/<tenant>/`. The
  peer tenant's directory is not present in that worktree.
- Territory. A tenant commits only under its own `build_tenants/<tenant>/`.
  A needed common change is requested from the pen and reaches the tenant by
  merging `main` inward. A tenant does not edit tickets, common files or the
  peer tenant.
- Work carrier. The installed
  [Work-Carrier-To-Execution Rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)
  requires every run to execute under one run-scoped execution contract,
  derived from an existing ticket.
  - C3 work is carried by one upstream authority ticket and one tenant copy
    per build tenant under `.ai-workspace/tickets/`.
  - Each member activation runs under an execution contract derived from the
    tenant ticket. The pen drafts the contract on the Executive's selection,
    and the contract is admitted as a separate step: the pen records the
    Executive's decision to run it in the ticket, with the contract's
    identity and digest, before execution. It is not a further
    ticket.
  - The ticket has one writing owner, the common pen, acting as a Writer
    activation in common territory. Before the next activation starts, the
    pen records, each as the Executive decided it: the admitted contract, the
    closed Writer result, the Reviewer result, the triage, the Executive's
    disposition and the next authorised activation.
  - The Executive activation decides and holds no write grant to tickets,
    common files, candidates or worktrees.
  - The tenant Writer's return is written in its own territory
    (`build_tenants/<tenant>/qualification/`) and never in the ticket.
  - The ticket is the only record that can authorise an action. No Writer
    activation starts without one, and no disposition exists until the pen has recorded it.
- Inputs. Tenant worktrees use sparse-checkout cone mode. A declared shared
  input outside the cone is read from the snapshot's input commit with
  `git show <input-commit>:<path>`, never from a working tree. A
  file absent from the cone is neither licence to read elsewhere nor
  evidence that the declared input is absent.
- Snapshot. A checkpoint input snapshot names the input commit on `main`
  whose tree holds every member, and it records each member's hash as read
  from that commit. The ticket entry that records the snapshot is a later,
  descendant commit, so the record is not part of the snapshot it records.
- Review. The product owner authorises reviews between tenants. A reviewer
  reads the reviewed tenant's branch at a named commit, never its working
  tree, and writes the review under `.ai-workspace/comments/<reviewer>/`.
  Review authority grants no candidate or peer-tenant write access.
- Merge. A tenant branch merges to `main` only on the product owner's
  acceptance of the checkpoint review, or an explicit owner-directed variance
  recorded in the ticket. A visibility merge supplies no acceptance. The branch is deleted and its
  worktree removed after merge. An unmerged tenant branch is work in
  progress, not a lineage; `git worktree prune` runs only after merge.
- Porting reads. Porting is copying a part of the peer tenant's candidate
  into one's own. Each tenant's Writer and Reviewer activations may read the
  peer tenant's candidate at the commit named in
  [Cross-Synthesis](#cross-synthesis), for porting and comparison. Ported
  text is written only in the porting tenant's own territory.
- Release cuts. `rc/*` and `release/*` branches are governed by the installed
  RELEASE_METHOD and are not tenant branches.

### Cross-Synthesis

Each tenant line builds on its own candidate and takes named parts from the other.

| Line | Base | Takes named parts from |
|---|---|---|
| Claude | the Claude tenant candidate, `build_tenants/claude/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, with its frontier record | the Codex tenant candidate at the same commit |
| Codex | the Codex tenant candidate, `build_tenants/codex/` at the same commit, with its frontier record | the Claude tenant candidate at the same commit |

A frontier record is a tenant's record of where each predecessor claim is disposed.

A part of the peer candidate enters a line only as a named contribution inside one member's frontier cone. The Writer records where the part came from, the single section that owns it in the receiving line, and the disposition it supports. The Reviewer compares it with its source and with the previous release.

A ported part never creates a second owner for a rule. A rule moved unchanged to a new place stays `conserved`; `superseded` requires an accepted replacement relation. Both lines are bound by the [single result algebra](#result-algebra).

The parts proposed for porting are those nominated in two sets of reviews:

- the cross-assessments, in which each tenant reviewed the other's candidate ([Claude on Codex](../.ai-workspace/comments/claude/20261013T043048Z_REVIEW_CODEX_V3_CANDIDATE_CROSS_ASSESSMENT.md), [Codex on Claude](../.ai-workspace/comments/codex/20261013T043456Z_REVIEW_CLAUDE_V3_CANDIDATE_CROSS_ASSESSMENT.md));
- the direct comparisons ([Claude](../.ai-workspace/comments/claude/20261013T062917Z_REVIEW_V3_CANDIDATES_DIRECT_COMPARISON.md), [Codex](../.ai-workspace/comments/codex/20261013T064524Z_REVIEW_STDO_V3_DIRECT_COMPARISON_AND_PATH.md)).

Each line's Executive selects each part into the frontier cone of the member it belongs to.

### Checkpoints

Construction proceeds through checkpoints:

- C0, structure and bootstrap (setting up this source project and the instruction files that route agents to it): closed;
- C1, principles: closed;
- C2, capabilities and conformance: closed;
- C3: builds each tenant's candidate under the [C3 Construction Contract](#c3-construction-contract).

The state of the closed checkpoints is in [GOALS](GOALS.md).

In C3, members are restated under Executive coordination and evaluated independently. Their frames are tested by fresh actors in actual use, and their a_c checks are selected separately under the [a_c dependency contract](requirements/A_C_DEPENDENCY.md). Release, and adoption (a project choosing to install and use the release), are later explicit decisions over an exact accepted set of members and its dependencies.

### C3 Construction Contract

This section configures, for this source project, the installed 2.5.1-rc.2 Executive engagement: the previous release's procedure for coordinating agent work through an Executive. The governing process is:

- the [Complete Engagement Transition](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition), the step sequence from selecting the basis (the exact sources, versions and decisions the work is done against) to closing a result;
- [Executive attention and drift locks](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action), which keep the outcome and basis fixed;
- [STDO-UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020) dispositions;
- admission of execution contracts under TICKET_METHOD, the previous release's rules for tickets and execution contracts.

Where this section and the installed baseline (STDO_REFERENCE_FRAME_BASELINE, the previous release's catalogue of standard frames and its Executive procedure) differ, the baseline governs and this section is corrected. Work authority: [T-002](../.ai-workspace/tickets/active/T-002-c3-successor-construction.md).

Outcome. Each tenant produces a candidate of the product with:

- its foundational commitments and a standalone method reconstructed on them, accounting for every material predecessor claim under the [standalone successor](requirements/README.md#standalone-successor-requirement) and [reduction](requirements/README.md#foundational-reduction-requirement) requirements;
- for every row of [PREDECESSOR_CLAIMS.md](requirements/PREDECESSOR_CLAIMS.md), one UP-015 disposition, with the successor locus or loci needed to recover each conserved or superseded claim in the candidate's own text, the accepted successor relation for each superseded claim, the owner's decision and reason for each intentionally removed claim, and a bounded reason for each not-applicable claim;
- a current a_c interpretation with complete required coverage and independently assessed fidelity under the [constraint-surface requirement](requirements/README.md#constraint-surfaces-and-logic-compression);
- reference frames assembled from the candidate, as the unit every actor is started on, with their task-use evidence.

The previous release stays immutable and in force as the building tool until a release decision. It is not part of the new release. Its results and process govern this construction; the candidate's single result algebra governs the successor being built. Historical verdicts and work statuses retain their recorded basis and scope.

Frontier. The frontier is the work still open. PREDECESSOR_CLAIMS.md supplies the common claim inventory. Each tenant's frozen frontier records its proposed dispositions and evidence against the subject named by its ticket. Acceptance standing comes only from the decisions recorded in that ticket under [Construction Authority](#construction-authority); a frontier may cite those entries but cannot confer or revise acceptance. For that tenant the Executive manages `U0`: all unresolved claims and every required evaluation not closed on the current basis. Its active frame selects a sufficient bounded view of that frontier, applicable authority and closed results for the next decision. Excluded items retain their standing. Each tenant declares its own member list and a map from every predecessor member to the successor members that receive its content. The map is reviewed with the first member and is navigation derived from claim dispositions; it does not prove conservation.

Responsibility table. A tenant's organisation and wording are its own; the obligations of each responsibility are common:

| Responsibility | Owes | Predecessor coverage inputs |
|---|---|---|
| foundations | ontology (what kinds of things exist), principles with their standing, the single [result algebra](#result-algebra), the reference frame as a first-class object for [context and attention management](requirements/README.md#bounded-transitions-and-reference-frames), bounded activation, work state, evidence, authority and generic interpretation-fidelity law | AXIOMATIC_CALCULUS, REFERENCE_FRAME_METHOD, IDENTITY_METHOD, the generic law of SPEC_METHOD and RELEASE_METHOD |
| Spec Method | the chain Intent → Product → Specification → Realisation, requirements and design law, [build-tenant binding](requirements/README.md#build-tenant-binding-requirement), work carriers and triage, assurance and testing law, change classes (the kinds of change, each with the stage it re-enters at) and re-entry, release mechanics | SPEC_METHOD, TICKET_METHOD, DESIGN_MODULE_METHOD generic law, RELEASE_METHOD |
| profiles | domain or operational bindings that use the shared laws and state their additional necessary determinations; the predecessor claims they receive are accounted for through these bindings and shared owners | ODD_METHOD, TRAVERSAL_OCCURRENCE_PROFILE, UX_METHOD, WORLD_MODEL_METHOD, DESIGN_MODULE_METHOD realisation law, STDO_REFERENCE_FRAME_BASELINE frame catalogues and Executive law |
| guides | posting (how commentary posts are written), writing, glossary | POSTING_GUIDE, WRITING_GUIDE, GLOSSARY_GUIDE |
| packaging | manifest, schemas, templates, compressions (the shortened summaries of the standards) or their successor, bootstrap, plugin | the non-standard members; disposition may stay `unresolved` during construction and must close before C3 closure |

The coverage inputs identify predecessor material to account for, not exclusive destinations or a required file partition. The three tiers own generic laws, method laws and additional profile bindings respectively. Guides and packaging own their scoped conventions and formats while deriving method permissions and result meanings from the relevant method-law owners. A claim may need one owner and several consuming bindings. The tenant's required a_c interpretation covers those owners and bindings; it is not merely a packaging check.

The previous-release members named in the table: DESIGN_MODULE_METHOD is the discipline for designing implementation modules; ODD_METHOD is the outcome-driven development profile; TRAVERSAL_OCCURRENCE_PROFILE is an optional a_c profile for recording histories of an application over a subject that changes outside it.

Activation unit. Each tenant publishes reference frames assembled from its restated members, one per selected task, under the [bounded-transition and frame requirement](requirements/README.md#bounded-transitions-and-reference-frames). They contain the contract and material sufficient for that task and exclude irrelevant material, retaining material dependencies and declared acquisition routes. They are generated from the a_c form of the members (a_c projections) or by an equivalent the tenant declares. Exact copies match their owners; derived views meet the constraint-surface fidelity requirement. A frame whose task returns a result carries the core algebra or its refinement mapping. Every actor starts on a frame and its subject. Supplied context is measured in bytes before acquisition; further material acquired through declared routes is recorded with its measurement boundary. Criterion 4 evaluates whether the actor uses the resulting context adequately.

Audiences and tasks.

- Audiences:
  - a fresh model actor started on one frame against a declared subject;
  - a human method owner reading by following links;
  - the Writer, Reviewer and Executive actors building or assessing the new release itself.
- Assumed knowledge: none beyond the frame, its subject and material acquired through its declared routes and permitted tools. Criterion 4 qualifies standalone successor task use: predecessor rules cannot supply missing successor content during the trial. The installed builder governs preparation and assessment outside that actor's task context. A trial using predecessor rules to perform construction supplies separate builder-process evidence. Freshness excludes unselected private context and automatically loaded repository instructions regardless of working directory; supplied instructions and all acquired material are disclosed.
- Tasks:
  - do a bounded piece of work;
  - resume work another actor left;
  - review work;
  - decide acceptance or release;
  - apply a profile;
  - build or assess a member of the new release.

Executive loop.

1. The Executive's authority comes from this contract and the ticket.
2. It selects from the frontier the smallest set `M` of work whose prerequisites are done, normally one member or one declared frontier cone.
3. It starts one Writer per element of `M` with the UP-020 intake:
   - the exact outcome and checkpoint;
   - the rows in scope;
   - the governing invariants;
   - the grant and write territory;
   - the evidence required;
   - exclusions;
   - stop and re-entry conditions;
   - the context, wall-time and spend limits;
   - the exact bounded action.
4. The Writer returns a closed evaluation under the installed baseline, with its work-result variant:
   - `candidate_ready`, with exact artifact coordinates and a bounded account of the restated text, dispositions, interpretation, frames and measured activations;
   - `refused`;
   - `incomplete`;
   - `re_entry_requested`.
5. The Executive evaluates the bounded return and starts the Reviewer for every `candidate_ready`. The artifacts remain available to the relevant Writer or Reviewer frames; their bodies are not automatically loaded into Executive context. Independent review is required for every member.
6. It reads the Reviewer's closed result and applies the disposition grant above.
7. It has the common pen record the decision in the ticket, then starts the next already-authorised activation.

The Executive activation holds no write grant and never changes ticket, candidate, common or worktree files. If the same actor changes role, the pen records the change before the effect, and the actor is no longer Executive for that effect.

Acceptance criteria for one member restatement:

1. Every row of the member's frontier cone has exactly one UP-015 disposition. Each `conserved` or `superseded` row names all successor loci needed to recover the whole claim: its owning locus and any necessary domain or consumer bindings, each resolving to the required text.
2. For every `conserved` row, the Reviewer compares the source independently of the author and finds the claim's meaning present in the new release's own text. This is UP-015's semantic conservation, evidenced under the standalone successor requirement. A link to the source alone, a matching label, or a paraphrase that drops part of a rule fails.
3. Every `superseded` row names the successor relation accepted under [Construction Authority](#construction-authority), cites its ticket decision and names its carrying loci, showing what replaces that row's claim. Proposed replacements remain pending. Every `intentionally removed` row names the product owner's decision and reason. Every `not applicable` row gives a bounded reason, one that states the limits of what it covers.
4. Each selected task of the member has a frame that fits the declared limits, supplies sufficient relevant material and excludes irrelevant material. A fresh actor uses that frame, its subject and declared acquisition routes and tools correctly. Its work is judged against expectations specified independently of the author, without private validator knowledge or the author's memory. The evidence identifies the exact frame, subject, task, supplied instructions, acquired material and independent expectations. Reuse after a change requires evidence that the source, frame, task, actor conditions and material dependencies preserve the conclusion's applicability. Changed packets or tasks retain their own subjects. A corrected run is not an unchanged independent test of the correction. This establishes adequate context and attention for the tested conditions; byte fit alone does not.
5. The applicable [member-conformance discriminators](conformance/README.md#member-conformance) hold under source-first logical review. The affected a_c interpretation and acquired views preserve the owned determinations under the constraint-surface requirement. The review states coverage, independent expectations and unresolved obligations; structural validity alone establishes neither fidelity nor semantic conformance. Construction decisions and integrated closure are checked at their own boundaries.
6. The restatement meets the [reduction requirement](requirements/README.md#foundational-reduction-requirement) within its cone: shared laws govern the affected decisions, recurring independent determinations are contracted, and remaining material distinctions are justified. Applicable local deciding-path comparisons and counterexamples support that conclusion. The integrated assessment establishes cross-member coverage and the whole-candidate conclusion; its absence alone does not falsify a supported local claim. The restatement adds no new obligation without naming its purpose and material relation, and makes no needless change to work carriers or process. Prose size or structural validation alone does not satisfy this criterion.

Independence. The Reviewer does not assess its own authorship, including a material contribution to the subject or the repair under review. Reporting a defect, supplying a counterexample or identifying behavior already required by an owning rule does not itself author the repair; that Reviewer may recheck the defect. Authoring material wording, policy or design that is adopted in the repair is a contribution to the subject. Its author discloses that contribution and cannot supply independent acceptance evidence for it; another nonauthor covers the affected claim. Unaffected judgments retain their scope. Independently specified expectations do not come from the author of the behavior being assessed. Actor identity, model family, source contributions, supplied context and prior participation are disclosed where material to independence. A fresh context or another model name alone does not establish it. A different model family from the Writer is the default; a same-family nonauthor Reviewer is a declared exception, with its reason and limits in the activation record. Ported-source authorship retains the separate owner decision below.

Limits. Every activation declares its limits and measurement boundaries: context in bytes, wall time and spend. The context limit bounds the material concurrently retained in active actor context, including instructions, frame, subject and subsequently acquired material. Report supplied bytes, cumulative acquired bytes including repeated reads, and the measured or supported upper bound on active retained context separately. A 30 KB supplied frame plus 200 KB retained acquisition exceeds a 40 KB context limit; sequential acquisition fits only if each active context fits and the declared continuation preserves the material obligations. Unmeasured platform context or unsupported truncation cannot establish fit. Report wall time and spend after the activation. Attention is addressed through sufficient relevant frames and the actual-use evidence in criterion 4; it is not inferred from a byte or token count. This contract sets no universal budget. The Executive selects and records the limits for each activation, identifying unknown or uninstrumented portions.

Closure. C3 closes for a tenant when every frontier row is disposed, every member is accepted under the grant, and independent assessment establishes the integrated candidate's reduction, complete required interpretation coverage and fidelity, and required frame-use evidence. The reduction conclusion covers material shared owners and their consumers across member boundaries under the reduction requirement. Member results contribute only their supported scope; they cannot establish the whole by omission. Reuse preserves its applicability, and changed dependencies reopen affected conclusions. Any required obligation whose assessment remains unresolved prevents closure. The product owner accepts the checkpoint.

## Open Owner Decisions

- Acceptance-review assignments for each tenant in C3 remain owner decisions. Each ticket records its construction assignment. Construction and defect-review authority supply no per-member `accept` disposition until the required independent-review assignment and ported-part policy are resolved.
- Review of a ported part. By default a member is reviewed by the peer tenant's model family, which is the source author of any part ported from the peer. The [Independence](#c3-construction-contract) rule forbids a Reviewer assessing its own authorship. The product owner decides how a ported part is reviewed before the first frontier cone with a contribution is accepted.
- The steel thread: its selection, its work carrier, and its spend and time limits. The steel thread is step 2 of [Categorical Construction](#categorical-construction).
- Identity and packaging of the new release. The decisions cover whether the compressions are kept, superseded or removed; how identifiers for a_c concepts and for the Traversal Occurrence Profile are issued and accepted into use; and the released interpretation's encoding basis and its standalone acquisition. The successor does not depend on the previous release remaining in force. The relevant decision precedes any dependent member or C3 acceptance and, in all cases, a release-candidate cut.
- Candidate number and release-candidate cut, in the `specification_methodology` release namespace under RELEASE_METHOD. Decided before a release-candidate cut.
- Cohort relation: which versions of the companion products are released together with this one. Decided before a release-candidate cut. Existing Product identifiers and the current cohort are unchanged, and the installed 2.5.1-rc.2 release is the operative builder.
