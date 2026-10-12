# STDO 3 Standards (Claude tenant realisation)

Status: the Claude tenant's STDO 3 candidate, under construction member by
member on the order of [DOCUMENT_STRUCTURE](../design/DOCUMENT_STRUCTURE.md);
the first pass (steel threads T1 to T4) is its starting text. Not
released, not installed, not common WHAT. Builder basis
`stdo://releases/v2.5.1-rc.2/`.

STDO 3 is a specification methodology for construction and evaluation by
actors with finite context, attention, time and capability. Its core
statement: interpret a scoped subject; select a purpose and governing
contract; transform within admitted authority while conserving its material
relations; evaluate the resulting claims; continue, recover or conclude from
current state under explicit uncertainty.

## Routes

| You want to | Read, in order |
|---|---|
| understand the method | [FOUNDATIONS](FOUNDATIONS.md) → [REFERENCE_FRAME](REFERENCE_FRAME.md) → [ACTIVATION](ACTIVATION.md) → [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md) → [SPEC_METHOD](SPEC_METHOD.md) |
| bind one project to the method | [SPEC_METHOD §1](SPEC_METHOD.md) for the process constitution and its surfaces, then [PRODUCT_DEFINITION](PRODUCT_DEFINITION.md) for the definition overlay, its required relations, bounded-context resolution, the one constitutional surface and bootstrap |
| triage a report, select its change class and re-enter | [SPEC_METHOD §4](SPEC_METHOD.md) for the front door, the six determinations, the computed classification and the classes, [SPEC_METHOD §5](SPEC_METHOD.md) for the ambiguity it must record, then [TICKETS §4](TICKETS.md#triage-metadata) for what the ticket records |
| migrate a core interface or reset a constitutional line | [SPEC_METHOD §7](SPEC_METHOD.md), then [TICKETS §6](TICKETS.md#6-implementation-migration) for the ticket's declaration and checklist |
| prove a realisation | [EVALUATION §1–2](EVALUATION.md) for what a proof names, then [ASSURANCE](ASSURANCE.md) for verification layers, the testing taxonomy, test authority, scenario bundles, installed proof and path coverage |
| interpret a subject as a model, project a frame from it, or encode an accepted model | [AXIOMATIC_CALCULUS §2–4](AXIOMATIC_CALCULUS.md) for the signature, records and laws, [§6–8](AXIOMATIC_CALCULUS.md#6-interpretation-and-models) for interpretation, the three layers and identity, then [EVALUATION §2](EVALUATION.md) for the structural and semantic split of its review |
| do a bounded piece of work | [ACTIVATION §1–3](ACTIVATION.md) for the step, its admission and its result algebra, [REFERENCE_FRAME §11](REFERENCE_FRAME.md) for the packet you are activated on, then [SPEC_METHOD §4](SPEC_METHOD.md) for where your change re-enters |
| declare, audit or revise a project's frame set | [REFERENCE_FRAME §4, §8 and §10](REFERENCE_FRAME.md), then [EVALUATION §7](EVALUATION.md) to qualify a frame |
| resume work someone else left | [ACTIVATION §5 and §7](ACTIVATION.md) for work state, resumption and reuse, [TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) for recorded judgment and owner rulings, then the [T-05 case](../qualification/cases/T-05/CASE.md) for a worked resumption |
| open, carry or close a piece of work | [TICKETS §5](TICKETS.md#carrier-selection) for the smallest lawful carrier and the carrier side of admission, [§4](TICKETS.md#4-ticket-rules) for the fields and the upward propagation check, [§7](TICKETS.md#condition-based-closure-and-reuse) for closure by condition |
| review someone's work | [EVALUATION](EVALUATION.md), then the [CONFORMANCE](CONFORMANCE.md) case nearest your subject |
| decide acceptance or release | [EVALUATION §5](EVALUATION.md), [SPEC_METHOD §6](SPEC_METHOD.md), then [RELEASE §8](RELEASE.md#8-acceptance) for acceptance of an exact cut and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015) for the successor dispositions |
| cut, publish, qualify or select a release | [RELEASE §1 to §3](RELEASE.md) for the identities, refs, phases and publication steps, [§4](RELEASE.md#4-selector-and-consumer-adoption) for the selector and adoption, then [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) for the consumer basis |
| define, parse or audit an identity | [IDENTITY §2 to §4](IDENTITY.md) for the core law and hierarchy, [§8](IDENTITY.md#8-parsing) for parsing, [§10](IDENTITY.md#10-minimum-questions) for the minimum questions, [§6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004) for authority identity |
| coordinate work as Executive, Worker or Reviewer, or adopt the baseline profile | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) for direct versus coordinated entry, [§6](EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action) and [§12](EXECUTIVE_BASELINE.md#12-complete-engagement-transition) for the Executive's duties and the transition, then [§16](EXECUTIVE_BASELINE.md#16-adoption-or-project-defined-configuration) to adopt or replace it |
| design or review a software realisation boundary | [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design) for ontology-first derivation, proportional sequencing and the decision-complete gate, [§6](DESIGN_MODULE.md#6-prime-law) and [§7](DESIGN_MODULE.md#7-ontology-and-three-view-design-gate) for Prime, the carrier set and the three-view gate, [§11](DESIGN_MODULE.md#11-review) for the review questions, then [ASSURANCE §14 to §16](ASSURANCE.md#14-design-to-module-evidence-route) for module evidence, unit tests and lifecycle confirmation |
| apply the method to code, graphs, UX or world models | [PROFILES](PROFILES.md); for a UX surface [UX §4](UX.md#4-process-model), [§8](UX.md#8-continuation-and-replay) and [§12](UX.md#12-adoption); for a world model [WORLD_MODEL §7](WORLD_MODEL.md#7-flow), [§9](WORLD_MODEL.md#9-entity-cut-construction) and [§10](WORLD_MODEL.md#10-markov-object-overlay-construction) |
| build a graph-native ODD product | [ODD §17](ODD.md#17-invocation-rule), then [§18](ODD.md#18-cold-start-reading-order) |
| model immutable occurrence histories over a mutable subject | [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md#authority-and-adoption) |
| write or revise a specification artifact | [WRITING_GUIDE](WRITING_GUIDE.md), then [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) for the layer a sentence belongs to |
| publish analysis, a review, a handoff or a proposed change | [POSTING_GUIDE](POSTING_GUIDE.md), then [SPEC_METHOD §6](SPEC_METHOD.md#shared-method-adoption-and-propagation-stdo-up-012) for how a reusable method change is adopted |
| find the clause that owns a term | [GLOSSARY](GLOSSARY.md), then [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) to resolve the occurrence |
| load it into a model's context | the current set program under [../a_c/set-4/](../a_c/set-4/README.md), a partial encoding over thirteen members at `978d324` with four projected frames (transformation and judgment, triage and re-entry, carrier and admission, executive disposition): it carries set-3's encoding of FOUNDATIONS, REFERENCE_FRAME, ACTIVATION, EVALUATION, SPEC_METHOD, CONFORMANCE, PROFILES and README, adds parts of AXIOMATIC_CALCULUS, SPEC_METHOD, TICKETS, EXECUTIVE_BASELINE and ASSURANCE, and encodes nothing of PRODUCT_DEFINITION or of the members added after `978d324`; [../a_c/set-3/](../a_c/set-3/README.md) and the earlier sets are history |

## Documents

| File | Tier | Owns |
|---|---|---|
| [FOUNDATIONS.md](FOUNDATIONS.md) | 1 | ontology including the frame objects, commitments, algebra, hypotheses, the UP-015 disposition vocabulary |
| [REFERENCE_FRAME.md](REFERENCE_FRAME.md) | 1 | the reference frame as a first-class object: laws RF-001 to RF-017, frame sets, method functions, conjunction, relations, coverage, revision, the activation packet, declarations |
| [ACTIVATION.md](ACTIVATION.md) | 1 | the bounded step: intake, admission, applicability, context construction, the single result algebra, totality, refinement, work state, cost, closed result and reuse |
| [AXIOMATIC_CALCULUS.md](AXIOMATIC_CALCULUS.md) | 1 | the a_c theory: signature, typed records, laws AC-001 to AC-020, traversals and functor kinds, interpretation and models, the three layers, the law of calculus identity, exclusions, conformance obligations |
| [IDENTITY.md](IDENTITY.md) | 1 | identity law: scoped identity with uniqueness, type and stability, readable and opaque identity, hierarchy, engine-owned and domain-owned identity, authority identity and conservation (UP-004), domain overrides and their publication, parsing, the release version boundary, minimum questions, examples, consequence for implementations |
| [EVALUATION.md](EVALUATION.md) | 1 | claims, evidence, assessment, acceptance, conformance, qualification of frames and of the method |
| [SPEC_METHOD.md](SPEC_METHOD.md) | 2 | the particular method: position, process constitution and method identity; the constitutional chain, manifesto, litmus tests, renewal path, specification surfaces, requirement categories and classification, trace closure, live-surface immutability, lifecycle sufficiency; outcome conservation; change management with universal intake triage, change classes, computed classification, consistency gate, sprint boundary, carriers and procedures; ambiguity governance; lineage and the release version boundary; core-interface, fundamental and wave migration; bounded execution and delivery priority; ADR conventions |
| [PRODUCT_DEFINITION.md](PRODUCT_DEFINITION.md) | 2 | how one project binds to the method: 1 overlay and layout independence; 2 required definition relations; 3 constitutional-set sufficiency; 4 shared installed release basis and toolchain manager; 5 bounded-context semantic resolution; 6 local constitutional binding; 7 collective reference-frame basis; 8 WHAT, HOW and work carriers; 9 recursive discovery and explicit composition; 10 semantic-resolution conformance cases; 11 one constitutional surface and version boundary; 12 bootstrap |
| [ASSURANCE.md](ASSURANCE.md) | 2 | testing and proof law: 1 verification layers; 2 testing strategy taxonomy with fixture and proof portability; 3 test authority; 4 scenario bundle; 5 installed dev proof; 6 significant path coverage; 7 product testing frame set; 8 combinatorial coverage and testing value; 9 legitimate path and technical-debt erasure; 10 testing evidence composition; 11 assurance subject acquisition and evaluation; 12 counterexample localisation; 13 end-to-end interface integration frame; 14 design-to-module evidence route; 15 module-derived unit tests; 16 module lifecycle confirmation |
| [TICKETS.md](TICKETS.md) | 2 | work carriers: 1 goals, tickets, sprints, comments, execution contracts, milestones (UP-006); 2 layout, bindings, carrier substitution; 3 sprint rules with compliance escrow and close review; 4 ticket rules with required fields, change class, upward propagation check, triage metadata, status and lanes; 5 carrier selection and the carrier side of admission, evaluation criteria, term binding; 6 implementation migration; 7 UP-007, judgment continuity, condition-based closure, test case authority, UP-009; 8 recommended shapes; 9 operating mode and relationships |
| [RELEASE.md](RELEASE.md) | 2 | release publication: 1 context and position; 2 release identities, project-qualified refs, project subtree, historical ref conservation; 3 phases, candidate construction, immutable RC publication, exact-cut qualification, monotonic advancement; 4 selector and consumer adoption; 5 naming; 6 release-scoped assets and the Product subject; 7 release-matched asset cohorts; 8 acceptance and external dependencies; 9 successor baseline conservation (UP-015); 10 open questions |
| [CONFORMANCE.md](CONFORMANCE.md) | 2 | cases the method must pass |
| [PROFILES.md](PROFILES.md) | 3 | profile imports and the core boundary |
| [EXECUTIVE_BASELINE.md](EXECUTIVE_BASELINE.md) | 3 | the optional Executive, Worker and Reviewer profile: canonical compression, authority boundary, engagement applicability, profile terms, Executive attention with its drift locks and no-mutation rule, the derived Executive, Worker and Reviewer frames, steel-thread delivery, the twelve generic specialist families, the engagement transition with the promotion constraint projection, handoff and coverage application, adoption or project configuration, actor binding, profile qualification, failure classification, anti-patterns, closure |
| [DESIGN_MODULE.md](DESIGN_MODULE.md) | 3 | the optional software-design profile: purpose, position and graph-execution alignment; boundary closure evaluators and ingress collapse; functional bias and Python typing; ontology-first design with proportional design sequencing, decision-complete symbolic design, bounded frame conservation (UP-017), native constructability (UP-002), capability and foundation selection (UP-023), entity, authority, transformation-admission (UP-016) and function completeness, Prime atoms, whole-family contraction and root conservation (UP-003), ontology projection; Prime law with governance cost (UP-005), the carrier set, promotion and inflation; the three-view gate with invariant reconstruction (UP-018) and computational realisation (UP-019); theoretical framing; module taxonomy; realisation rules; review questions and checklist; adoption, relations and identity defaults |
| [ODD.md](ODD.md) | 3 | the Outcome-Driven Development profile: position, method role and composition, library classes, graph model with probabilistic compute and the graph-native F_P, F_D and F_H, product and self-host boundaries, responsibility layers, governance, what an ODD product is, core law 11.1 to 11.9 with the execution-authority audit, the constructive evaluation and yield loop (A0 to A16), UP-010 and the cumulative environment law, scenario, installed-dev, dogfooding, release boundary, failure pattern, invocation, reading order, ramp-up |
| [TRAVERSAL_OCCURRENCE.md](TRAVERSAL_OCCURRENCE.md) | 3 | the optional a_c traversal occurrence profile over mutable subjects: imported calculus boundary, closed sorts and reference domains, event kinds, relation families, constraint, judgment, residual and stop kinds, occurrence identity, admission cut, causality and lineage, effect relation, frontier and projection, OP-001 to OP-007, adoption, exact profile identity, exclusions, conformance |
| [UX.md](UX.md) | 3 | the optional UX profile: Elm process model, carrier boundary, state transitions, effect membrane, carrier binding, continuation and Msg-replay proof, view shape, type sharing, accessibility minimum, adoption with scaffold law and sprint escrow, failure patterns, review questions, result mapping |
| [WORLD_MODEL.md](WORLD_MODEL.md) | 3 | the optional world-model profile: position, imports and Builder Project, Markov-object construct at candidate status, core claims, units, flow, representation and ledger laws, entity cut construction, overlay construction, saturation, composition, projection, planes, proof, output, result mapping |
| [POSTING_GUIDE.md](POSTING_GUIDE.md) | guide | the commentary layer: a post's purposes and boundary, location binding, carrier identity, categories, structure, discussion state, posting rules and ratification |
| [WRITING_GUIDE.md](WRITING_GUIDE.md) | guide | writing discipline: core rule, style rules, habits to remove, good and bad prose, tone by authority layer, specification artifact practice, layer checks, current-surface writing |
| [GLOSSARY.md](GLOSSARY.md) | guide | the non-deciding locator index: index contract, locator law, rows by bounded context |

The constitutional method members of this corpus are its tier 1 and tier 2
standards and, when a project selects them, its tier 3 profiles (P6, P3).

Each clause names the principle that requires it (P0 to P6, defined in
FOUNDATIONS §3) and, where it restates or supersedes an rc.2 clause, may
carry that clause's route as provenance; a route is never the disposition
(FOUNDATIONS §1). Every predecessor row's disposition and locus are in the
tenant [frontier](../frontier/PREDECESSOR_CLAIMS.md). The corpus is
applicable without the rc.2 cut, which remains the operative builder of
this construction until STDO 3 is released.

## Library and installed basis

One complete immutable released RC cut of this standards tree is the
constitutional member set of the selectable STDO Product. The release may
also carry subordinate executable and interaction tooling (P6, P3;
provenance rc.2 README #standards-library). A cut carries (P3, P2):

- the constitutional members of tiers 1 and 2 above;
- the carrier-neutral [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md), whose
  a_c theory stays separate from interpreted subject models and carrier
  encodings ([AC-020](AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation));
- the application-neutral traversal occurrence profile
  [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md), which instantiates
  one closed model-family signature under an exact a_c basis without
  changing the calculus or selecting a consumer, and whose adoption stays
  optional;
- derived application profiles such as
  [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md);
- the companion guides [POSTING_GUIDE](POSTING_GUIDE.md) and
  [WRITING_GUIDE](WRITING_GUIDE.md);
- the non-deciding semantic locator index [GLOSSARY](GLOSSARY.md), whose
  rows point to context-declaring owning clauses and never define a shared
  default;
- compact read models for activations that need a compact method basis;
  their carrier awaits the ruling on the rc.2 compression rows, and the
  current candidate is the set program under
  [../a_c/set-4/](../a_c/set-4/README.md);
- normative interoperability schemas under `schemas/`, among them the
  layout-neutral product definition overlay and the deterministic
  installed-release manifest; and
- starter templates under `templates/`: the single per-product product
  definition template, project specification templates, the project
  reference-frame basis template and agent bootstrap templates.

The STDO toolchain manager installs each complete immutable cut once in a
shared versioned store and resolves logical release URIs, so a product
definition names its basis by logical URI and manifest digest and carries
no machine-local path
([PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager))
(P3, P6). A project-local copy stays possible when it is explicitly bound
and verified; it is not the default
([PRODUCT_DEFINITION §12](PRODUCT_DEFINITION.md#12-bootstrap)) (P6, P3).
Installed bytes take their authority from the exact RC cut, the product
definition's basis URI, the manifest digest and the member inventory
([PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager),
[RELEASE §3](RELEASE.md#exact-cut-qualification)) (P3, P6). Neither the
mutable authoring head nor the moving version-line selector silently
replaces that consumer basis
([RELEASE §4](RELEASE.md#4-selector-and-consumer-adoption)) (P6, P3).

## Source dispositions

The row of rc.2 README.md, received by this member. A route is provenance
only. Generalisations recorded here: "this tree" is this tenant's
standards tree; the predecessor's companion governance and operating
surfaces RELEASE_METHOD, TICKET_METHOD and DESIGN_MODULE_METHOD are tier 2
and tier 3 members here (RELEASE, TICKETS, DESIGN_MODULE), so the
companion item names the two guides; the predecessor's constitutional
method surfaces ODD_METHOD and WORLD_MODEL_METHOD are tier 3 profiles here
(ODD, WORLD_MODEL), constitutional members when a project selects them;
the compressed read models under `authority_compressions/` are restated as
a member kind only, their carrier staying unresolved at the compression
rows pending Jim's ruling; the installed cut, store and manifest claims are owned by
PRODUCT_DEFINITION §4 and §12, as the member map records,
which RELEASE §1 consumes, and are restated above with those owners
named.

| Anchor | Disposition | Locus |
|---|---|---|
| #standards-library | conserved; the cut as the constitutional member set, subordinate tooling at "may", the nine member kinds with the calculus separation, the traversal profile's neutrality and optional adoption, the non-deciding index, compact read models as a member kind (their carrier unresolved at the compression rows), schemas and templates with their named members, the shared versioned store, logical URIs and no machine-local paths, the non-default project-local copy, the four authority sources and the two non-replacements | Library and installed basis; PRODUCT_DEFINITION §4, §12; RELEASE §3, §4 |
