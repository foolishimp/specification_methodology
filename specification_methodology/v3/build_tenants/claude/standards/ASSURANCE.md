# ASSURANCE

Tier 2. Owns the assurance and testing law of the method: the verification
layers of the chain, the testing strategy taxonomy with its two proof
authorities and its fixture and proof portability rule, test authority,
scenario bundles, installed dev proof, significant path coverage, the
product testing frame set, combinatorial coverage and testing value,
legitimate-path and technical-debt erasure, testing evidence composition,
assurance subject acquisition, counterexample localisation and the
end-to-end interface integration frame.
Consumes [FOUNDATIONS](FOUNDATIONS.md) (claim, evidence, judgment,
authority), [REFERENCE_FRAME](REFERENCE_FRAME.md) (the frame, its
declaration shape, conjunction and coverage),
[EVALUATION](EVALUATION.md) (claims, separation, independent
assessment, acceptance, conformance) and [ACTIVATION §3](ACTIVATION.md)
(the result algebra); adds no definition to tier 1. The particular
method's chain and change classes are [SPEC_METHOD](SPEC_METHOD.md); the
project's bindings are [PRODUCT_DEFINITION](PRODUCT_DEFINITION.md). Later
members add to this one without changing what is here: the design
profile's module-derived unit-proof law (its 6A to 6C) and the ticket law's
test-case authority each land in a section of their own when their member
is activated, and this text pre-empts neither. The testing frames and
interface-integration law received from the predecessor baseline profile
are §7 to §13; the profile that maps engagement roles and specialist
families onto them is [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md), tier 3,
and nothing here depends on it. Every clause names the principle that
requires it (P0 to P6, FOUNDATIONS §3). A route written `rc.2 #anchor` is
into `stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md`, and in §7 to
§13 a route written `provenance #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md`;
both are provenance only. Under the standalone successor requirement every
predecessor row received here is restated in full in this text, and
nothing here depends on that cut to be applied.

## 1. Verification layers

Each layer of the chain (SPEC_METHOD §1) preserves a distinct kind of truth
(P2, P6; rc.2 #verification-layers):

| Layer | What it preserves | Primary question answered |
|---|---|---|
| Requirements | invariant truth | what must be true? |
| Design | structural choice | how is that truth realised? |
| Scenarios | operational meaning | can the realised system actually do the claimed thing? |

Without scenarios a capability can appear covered because the words exist
in requirements and design. Scenarios force the sharper question: can the
product really do the thing? A requirement can name a reusable composable
unit and a design record can describe the types that realise it, but only
a scenario asks whether a user can build such a unit and apply it twice
(P6).

Scenarios are the product-owner layer: concrete, end-to-end use cases that
validate the chain from intent to realised behaviour. When a scenario
cannot be written, the capability is not yet real. When a scenario fails,
the gap is between the system's actual behaviour and its claimed
capability, not between the specification's words and its other words (P2,
P6).

Scenarios do not replace requirement categories. They primarily validate
capability claims and other behaviour with concrete operational meaning.
Constraints, governance rules and verification-infrastructure requirements
may require different evidence in addition to, or instead of, end-to-end
scenarios (P2).

## 2. Testing strategy taxonomy

This member owns the product-assurance bounded context,
`urn:stdo:bounded-context:product-assurance`, under the selected complete
STDO basis, and within it the Product-level test-authority taxonomy.
Module-derived unit-proof law stays owned by the design profile (the
DESIGN_MODULE member); the shared context does not merge the two authority
sources (P6; rc.2 #testing-strategy-taxonomy).

Every executable proof surface declares its authority source (P6). For
ticketed work the immediate proof authority is the admitted ticket and its
triage path: tests derive from the ticket's lawful re-entry point
(SPEC_METHOD §4) and from the governing constitutional or realisation-law
surfaces it cites; they never derive expected results from current
implementation behaviour (P6, P2).

Authority source is not execution breadth. A test may be small or broad,
fast or slow, deterministic or live, and still derives from one of two
primary authorities (P6, P1):

1. design or module conformance tests; and
2. UAT, or acceptance, tests.

Design or module conformance tests derive from realisation authority: the
governing design, module ownership, the carrier inventory the design
declares (the design profile's interface-and-carrier set or an
equivalent), structural carrier diagrams where present, and boundary-local
fail-closed law. They answer one question: did the implementation realise
the module or design boundary correctly? Unit tests are design or module
conformance tests. Module integration tests, negative tests and
fail-closed tests may also be, when their proof target is a designed module
boundary rather than a user scenario (P6).

UAT or acceptance tests derive from constitutional user or product
authority: requirements, acceptance criteria, declared scenarios or use
cases, and product-level release or qualification claims. They answer one
question: does the composed product satisfy the claimed requirement or
scenario? (P6, P2)

Under this method only sandbox tests, or an explicitly equivalent isolated
composed-product proof lane, may be called UAT or acceptance tests. A
sandbox test exercises the deployed, installed or otherwise runnable
product form through declared application, public, runtime or control
surfaces, and is driven by a requirement-sourced scenario or acceptance
case. Direct source-level unit tests, helper tests and module integration
tests may be valuable proof; they are not UAT and cannot close user
acceptance by themselves (P6; EVALUATION §1, the weaker property never
substitutes for the claimed one).

Sandbox UAT has two lawful execution modes (P6, P1):

- harnessed sandbox UAT exercises the full composed product path with a
  deterministic, fake, recorded or injected worker or result surface; and
- live sandbox UAT exercises the full composed product path with a real
  configured worker, tool, agent, service or other external probabilistic
  transport where the product depends on that live boundary.

Harnessed sandbox UAT proves composition, orchestration, control,
projection, archive and scenario wiring without relying on live
probabilistic execution; it is the lane for deterministic reproducibility.
Live sandbox UAT proves that the same scenario can cross the real external
probabilistic boundary and return evidence through the declared result,
evaluation, provenance and projection surfaces. Where a product or release
claim depends on live probabilistic compute, semantic green, unit green,
module-integration green and harnessed-sandbox green are necessary and not
sufficient for live acceptance (P6, P5).

Terminology (P1):

- `unit` names module or design conformance scope, not user acceptance;
- `integration` names execution breadth, not authority source;
- `sandbox` names composed-product acceptance execution;
- `harnessed`, `fake`, `recorded` or `deterministic` name non-live sandbox
  execution; and
- `live` is reserved for real external worker or transport execution; a
  status projection named "live" is not live UAT unless it crosses that
  real boundary.

A project that uses other local filenames or runner labels still maps each
executable lane back to this taxonomy before claiming closure (P1, P6).

### Fixture and proof portability

Required closure lanes are reproducible from the declared source boundary
(P3, P6; rc.2 #fixture-and-proof-portability-rule). A unit, semantic or
module-design conformance lane does not depend on an undeclared local path,
a sibling workspace, an operator home directory or a mutable external
fixture.

Where a proof needs external project evidence, one of these holds:

- a minimal fixture is checked into the source boundary;
- a fixture manifest declares the external source, version and
  acquisition or binding rule; or
- the test is classified as harnessed sandbox, live sandbox, reference
  comparison or optional local evidence rather than required semantic
  closure.

A missing external fixture fails with a governed diagnostic that names the
fixture authority and the lane; it never masquerades as a product semantic
failure (P5, P6).

## 3. Test authority

Every live requirement has written test-case authority (P6; rc.2
#test-authority-rule). That authority may include scenario bundles,
ordered test-case sequences, negative or control cases and other explicit
evidence cases appropriate to the kind of truth being proved; it exists in
written form and is traceable. No live requirement is fully proved on
informal operator confidence, ambient habit or an unlabelled test corpus
(P6; EVALUATION §5, green labels are not acceptance).

## 4. Scenario bundle

Features are not proved by isolated assertions alone. Where a requirement
claims meaningful system behaviour, the proving surface should be a scenario
bundle or an equivalent ordered set of test cases that exercises that
behaviour through a coherent sequence rather than as disconnected
fragments (P2, P6; rc.2 #scenario-bundle-rule).

A scenario bundle shows the feature or use-case boundary being exercised,
the test-case sequence that proves it, and the outcomes expected at each
significant step. It is the layer that makes operational meaning
inspectable (P6).

Declared scenarios and use cases are not downstream decoration. They put
pressure on feature intent and design decisions by forcing the project to
name the real operational boundary, sequence, actors, controls and
expected outcomes that matter. For that reason they are also the best
source for identifying the significant code and control paths the proving
surface must exercise (§6; P2).

## 5. Installed dev proof

Where a system has an installable or runnable development form, the
decisive proving lane runs against an installed development version as if
it were an independent project or an externalised target, not only against
the source tree in place (P6, P3; rc.2 #installed-dev-proof-rule). That
proof should prefer a fresh sandbox or equivalent isolated environment, an
installed or built development artifact, and execution through the same
declared entry, control and runtime surfaces the real product uses. Direct
source-level or unit-level checks may stay useful; they do not replace
installed-dev proof of the system under test (P6; SPEC_METHOD §6 for the
install and development-product roles).

## 6. Significant path coverage

The proving surface declares and exercises the significant paths for the
behaviour being claimed (P6, P2; rc.2 #significant-path-coverage-rule).
Exhaustive proof does not mean every possible branch in every file; it
means the project names the meaningful paths and proves them
intentionally. The significant paths usually include, where relevant:

- the intended success path;
- the fail-closed or rejection path;
- the boundary or control path;
- the integration, dispatch or transport path; and
- the recovery, retry or replay path.

If the significant paths are not declared, scenario coverage cannot be
judged. If they are declared and not exercised, the behaviour is not fully
proved (P6; EVALUATION §1, a claim's scope cannot exceed its evaluated
evidence).

## 7. Product testing frame set

### Terms

A testing frame is a frame (REFERENCE_FRAME §1) whose evaluation executes
or observes a declared subject to discriminate one exact claim through an
explicit oracle, evidence population, path boundary and falsification
condition. A test file, suite, runner, fixture, scenario label, coverage
percentage or actor does not become a testing frame by existing. A testing
frame's authority is bounded by the claim actually exercised; test count,
assertion count, source coverage, runtime duration and framework category
do not widen it (P6, P1; provenance rc.2 STDO_REFERENCE_FRAME_BASELINE
#testing-frame).

An authoritative Product path is the declared ordinary causal composition
from a supported user or public entry, through the exact selected
interfaces, owners, state transitions, effects, persistence and recovery
boundaries, to the outcome projection the Product claim requires.
Producing an expected output through a bypass, an obsolete executor, a
test-only seam, an undeclared fallback or a competing authority falsifies
path conformance even when the output value is equal (P6, P3; provenance
#authoritative-product-path).

Material combinatorial complexity is the claim-relative population of
independent dimensions and interactions whose combinations can change an
outcome, violate an invariant, select another authority path or expose a
failure. At unit altitude it includes module-owned laws, behaviour at the
public module contract included, with their algebraic operators,
calculation regimes, states, transitions, boundary classes and failure
cases. Cross-participant interface, Product, persistence, configuration and
user-role combinations belong to the integration, end-to-end or
user-acceptance frames; they are not mocked away and counted as unit
evidence (P2, P6; provenance #material-combinatorial-complexity).

### The set

Where the governing frame configuration (PRODUCT_DEFINITION §7) or the
admitted work authority selects testing frames for a Product promotion,
closure or release-assurance claim, testing is configured as a
claim-relative set of testing frames. Placement in this member makes the
set, and the law of §8 to §13 that serves it, available; it adopts nothing,
and each activation is decided by ACTIVATION §1 (Applicability). The kind
of runner does not select the frame; the evaluated claim, subject, path,
population, oracle and falsification boundary do (P6, P2; provenance
#derived-product-testing-frame-set). The ordinary configuration holds four
distinct frames:

- user acceptance evaluates the Product outcome from the user's supported
  frame;
- end to end evaluates the complete runnable causal realisation of that
  outcome;
- integration evaluates one material composition boundary and its
  interaction population; and
- unit evaluates one module-owned law; internal combinatorial complexity
  decides the proportional size and strategy of that evidence, not whether
  the law is eligible for unit proof.

They add no role, stage, authority or testing hierarchy. Their ordinary
evidence topology assigns each claim to its congruent frame (P6, P4a;
provenance #canonical-compression):

```text
Product and accepted design
  |- user-outcome claims -> user-acceptance frames
  |- runnable causal-path claims -> end-to-end frames
  |- composition-boundary claims -> integration frames
  `- module-owned laws -> unit frames

bound results -> declared conjunction -> Product or release disposition
```

The fan-out assigns claims to evidence; it is neither an authority
hierarchy nor a claim that one frame decomposes into another. Evidence
may relate through declared conjunction, translation, falsification and
re-entry (P4a; REFERENCE_FRAME §6). A broader frame cannot make a module-owned
law true, and any number of narrower green frames cannot establish an
unevaluated Product composition or user outcome (EVALUATION §1, the weaker
property never substitutes for the claimed one).

The frames may overlap, and one execution may supply evidence to several of
them; every result stays bound to its own claim. A label such as `UAT`,
`E2E`, `integration` or `unit` has no assurance value without the
corresponding frame declaration (P1, P6). Each frame below is given in the
shape of a frame declaration (REFERENCE_FRAME §13); "core result" is a
member of ACTIVATION §3.

### User-acceptance frame

(P6, P2; provenance #derived-user-acceptance-frame)

| Frame element | User acceptance |
|---|---|
| evaluation family | Can a declared user, with the user's admitted capability and information, obtain the exact Product-defined outcome through the supported ordinary Product surface? |
| subject and basis | the exact deployed, installed or otherwise runnable Product form the claim names; current Product, requirement, UX, identity, policy and acceptance authority; the declared user role, environment, and harnessed or live sandbox mode (§2) |
| material manifold | user goal, supported entry surfaces, permissions, inputs, Product configuration, ordinary dependencies, any declared external-worker or transport substitution boundary, user-visible state and outputs, refusal and recovery behaviour, and the acceptance interval |
| coordinates | exact Product and artifact identity, install, user role, capability, configuration, dependency realisation, harnessed or live mode, data, workspace, invocation, time, outcome and scenario identity |
| governing invariants | the applicable Product and requirement outcomes; supported-interface, identity, UX, safety, persistence and release law; RF-001 to RF-017; EVALUATION §1, §2, §3, §6 and §7 (proof target, evidence separation, assurance-boundary congruence, freeze and post-exposure revision, comparison, method qualification) |
| authority | bounded evaluation only; the frame mints no Product meaning or acceptance authority, and an automated actor does not become the human or Product acceptance owner |
| evidence | actual supported-surface requests and responses, user-visible projections, durable side effects where claimed, refusals, recovery observations, scenario records, exact-subject identity, and the declared live or substituted dependency identity |
| capability envelope | ability to operate the Product as the declared user would, perceive the material outcome and refusal surfaces, and distinguish hidden setup or unsupported assistance |
| exclusions | source imports, private APIs, direct Product-state injection, test-only endpoints, hidden administrator capability, undeclared fixtures or substitutes, a test double at a boundary claimed as real or live, compatibility bypasses, and internal success substituted for the user outcome |
| result | one core result bound to the exact user-outcome claim, with witnessed paths, counterexamples, residual user populations and invalidation conditions |
| invalidation | a material change of Product, supported interface, user role, capability, configuration, dependency or substitution mode, data contract, runnable subject, acceptance meaning or ordinary path |

User acceptance is the primary Product-outcome evidence frame when the
claim is that a user can use the Product. It may be automated only when the
automation faithfully occupies the declared user frame and gains no path or
capability that user lacks. Automation can execute acceptance evidence; it
cannot assume acceptance authority (P6; EVALUATION §5).

Where harnessed sandbox UAT is admitted (§2), a deterministic, fake,
recorded or injected external worker or transport limits the result to the
composed Product relations actually exercised; it does not prove that the
live external boundary works. When a Product or release claim depends on
real external compute or transport, live sandbox UAT is mandatory for that
claim; unit, integration, semantic and end-to-end evidence that uses the
substitute, and harnessed UAT green, are not sufficient (P6, P5).

### End-to-end frame

(P6, P3; provenance #derived-end-to-end-frame)

| Frame element | End to end |
|---|---|
| evaluation family | Does the exact Product subject realise the claimed outcome through the complete authoritative Product path, including every material interface, owner, state transition, effect, persistence, continuation, recovery and projection boundary? |
| subject and basis | the exact deployed, installed or otherwise runnable Product form, the composition design, the supported entry, the selected owner and dependency set, the ordinary runtime configuration and the Product claim |
| material manifold | the complete causal producers and consumers from entry to outcome; interface contracts; authority transitions; state, event, persistence, process, continuation, retry, recovery and projection relations; competing paths |
| coordinates | artifact and installed-tree identity, entry, operation, selected definition and owner, path and edge identities, process, event prefix, state, configuration, dependency, result, replay and scenario identity |
| governing invariants | Product and accepted-design composition law; exact-subject and assurance congruence; path singularity where required; lifecycle, authority, persistence, replay, recovery and release law |
| authority | bounded evaluation only; observation may expose internal evidence but may not bypass, repair, replace or reinterpret the Product path |
| evidence | supported entry invocation, the observed semantic path and authority edges, owner receipts, durable events, state transitions, outputs, replay or reconstruction where claimed, installed artifact identity, and negative-path observations |
| capability envelope | ability to execute and observe the complete Product path without changing it, to tell the authoritative path from rival paths, and to reproduce material state and failure relations |
| exclusions | source-only substitutes for runnable-Product claims, direct invocation below the supported entry, test doubles at claimed real boundaries, test-only routing, hidden retries or repair, omitted persistence or fresh-process boundaries, and equal output without path evidence |
| result | one core result bound to the exact end-to-end claim, with the exercised composition edges, unexercised material paths, counterexamples and residual combinations |
| invalidation | a material change of artifact, install, dependency, configuration, interface, owner, path, lifecycle, persistence, recovery, projection, test semantics or evidence population |

The expected output is necessary and not sufficient. Reaching it through a
forbidden or obsolete path falsifies the end-to-end claim. A test is not end
to end because it starts and finishes in one process, crosses many lines or
carries an end-to-end label (P6, P1).

### Integration frame

(P6, P4a; provenance #derived-integration-frame)

| Frame element | Integration |
|---|---|
| evaluation family | Do the actual participants at one declared material composition boundary satisfy their joint contract across the combinations of state, authority, configuration, timing, failure and recovery that can change the boundary result? |
| subject and basis | the exact interface or composition declaration, the actual participating implementations or exact substitutes the bounded claim admits, the governing Product, requirement and design law, and the interaction population |
| material manifold | both sides of the boundary, shared carriers, preconditions, postconditions, authority and ownership, ordering, state, configuration, failure, retry, recovery, translation and competing participants |
| coordinates | participant and version identities, interface and carrier revision, state, configuration, dependency, interaction case, input, output, failure and evidence identity |
| governing invariants | declared interface and composition law, complete participant admission, atomicity and reconstruction where applicable, and the exact assurance boundary (EVALUATION §1) |
| authority | bounded boundary evaluation only; no integration result establishes an unevaluated Product outcome or authorises a substitute participant |
| evidence | actual exchanges, admitted carriers, state transitions, contract verdicts, failures, retries, recovery observations, interaction combinations and participant identities |
| capability envelope | competence and access to exercise and observe the real composition seam, identify participant substitution and vary every material interaction dimension |
| exclusions | mocks or stubs that hide the claimed real contract, one-sided contract assertions, happy-path-only exchange, helper-call equivalence, flattened versions or states, and projection of a boundary result to the whole Product without a governing relation |
| result | one core result for the declared integration claim, with covered combinations, counterexamples, omitted interactions and invalidation conditions |
| invalidation | a material change of participant, interface, carrier, state, configuration, dependency, timing, failure, recovery or interaction population |

A substitute or test double may support a deliberately narrower claim only
when its equivalence boundary and exclusions are explicit. Its result
cannot be promoted to evidence that the real participant or Product
composition was exercised (P6, EVALUATION §1).

### Unit frame

(P6, P2; provenance #derived-unit-test-frame)

| Frame element | Unit |
|---|---|
| evaluation family | Does one module-owned law hold across its material combinations of algebraic operator, calculation regime, state, transition, public or private boundary class, and failure case? |
| subject and basis | one exact module boundary, the accepted ontology and design, the active carrier inventory the design declares, module-owned requirements and public contracts, the implementation, and a module-bounded decidable oracle |
| material manifold | module-owned public contracts, algebras, calculations, parsers, reducers, state machines, transition functions, combinators, admission predicates, conservation laws, invariants, numerical boundaries and failures |
| coordinates | module and implementation revision, owned law, operator or function family, module state, input class, boundary class, expected relation, generated case, mutation and result identity |
| governing invariants | the design profile's module-ownership and unit-proof law (DESIGN_MODULE); the accepted ontology, carrier inventory, domain, sequence, state, algorithm and error relations material to the module |
| authority | bounded local evidence only; a unit result has no Product, installed, integration, user-acceptance, architecture, path-selection or release authority |
| evidence | law-derived examples, equivalence classes, finite exhaustive cases where available, property-based or generative cases, metamorphic relations, calculation or algebra oracles, boundary cases and killed internal mutations |
| capability envelope | competence to derive an oracle independently from the owned law, identify the module-bounded combination population, and tell an invariant violation from an implementation restatement |
| exclusions | Product outcomes, cross-module composition, supported user paths, packaging or installation, real external participants, orchestration topology, mocked-away interface behaviour, incidental branches, private helper layout, assertion count, and source coverage used as broader assurance |
| result | one core result limited to the exact module-owned law and the module-bounded population, with counterexamples, residual combinations and invalidation conditions |
| invalidation | a material change of ontology, carrier inventory, module boundary, owned law, algorithm, state space, numerical regime, implementation, oracle, generator or module-bounded population |

Unit testing is deliberately module-bounded. Every coded module requires
the module-derived unit lane the design profile owns; public module
contracts are valid unit-proof subjects. Internal combinatorial complexity
decides the proportional size and strategy of that evidence. Its highest
discriminating value is often in algebras, calculations, transformations,
parsers, reducers, state machines, decision tables, admission predicates,
conservation relations and bounded algorithms with strong independently
derived oracles. A unit test whose oracle repeats the implementation, or
whose cases follow incidental code branches, gives weak or circular
evidence (P6, P2).

Modules whose material complexity lies mainly in composition,
orchestration, configuration, persistence, ownership or user interaction
need integration, end-to-end or user-acceptance evidence at that actual
boundary. Mocking those relations into a unit test does not turn their
complexity into unit evidence (P6).

This frame does not waive the module-derived unit lane. It binds the lane
to module-owned law and the smallest congruent evidence population. Low
internal combinatorial complexity justifies a small lane, not omission and
not hundreds of implementation-shaped tests. Unit-test volume has no
independent closure value (P2).

No Product, user-outcome, installed-path, cross-module composition or
release claim may be closed from unit evidence, whatever the test count,
assertion count, source coverage, mutation score, runtime or historical
pass rate. Treating unit green as broader assurance is a frame error (P6,
EVALUATION §1).

## 8. Combinatorial coverage and testing value

Testing value is indexed first by the material combinations a frame can
discriminate for its exact claim, not by test, assertion, file, line,
branch, mock, snapshot or runner count (P2, P6; provenance
#combinatorial-coverage-and-testing-value-index). For one claim, the
testing-value index considers at least:

1. congruence between the claim and the evaluated subject;
2. the number and materiality of independent claim dimensions;
3. the interaction strength actually covered among those dimensions;
4. the exactness of the authoritative path;
5. oracle independence and precision;
6. sensitivity to realistic faults, rival paths and historical failures;
7. observability, reconstruction and reproducibility of the result; and
8. explicit residual combinations and invalidation conditions.

No universal scalar is required. A project may define one only through
Product, requirement or accepted-design authority, and keeps the
underlying coverage coordinates rather than flattening them into a score
(P1, P6).

At unit altitude the relevant dimensions are module-bounded. Unit-testing
value normally rises with the internal combinatorial complexity of an
algebra, calculation, state machine, transition relation or other
module-owned closed domain, because local tests can cheaply discriminate
many meaningful combinations against a precise oracle (P2).

At integration, end-to-end and user-acceptance altitude, testing value can
be multiplicative rather than additive: each material interface composes
preconditions, postconditions, authority, state, configuration, failure and
recovery with every other traversed boundary. The value comes from the
interactions actually discriminated, not from touching many interfaces on
one sunny path (P4a, P2). Material Product factors commonly include:

- user role and capability;
- supported operation and Product composition;
- selected definition, owner, implementation and dependency;
- lifecycle and persisted state;
- configuration and version combination;
- process, continuation, retry, re-entry and recovery mode;
- success, refusal, malformed result, partial failure and competing-path
  case;
- fresh-process, replay, reconstruction and migration condition; and
- user-visible outcome and projection.

The activated frame declares the finite interaction population and why its
covering set is adequate. Pairwise or other covering-array reduction is
lawful only where the basis explains why the omitted higher-order
interactions cannot change the claim, or keeps them as residuals.
High-consequence authority, persistence, concurrency, recovery, migration
and historically failure-prone relations normally need explicit
higher-strength combinations (P5, P2; REFERENCE_FRAME §8, interaction and
failure coverage).

Source, line, branch and function coverage may diagnose whether code was
visited. They do not establish semantic combination coverage,
authoritative path selection, user-outcome coverage or the absence of a
rival path (P6, P1).

## 9. Legitimate path and technical-debt erasure

Every Product path claim needs two-sided evidence (P6, P3; provenance
#legitimate-path-and-technical-debt-erasure):

1. required-path reachability: each required authoritative composition has
   an exact witness in the deployed, installed or otherwise runnable
   Product form through the supported ordinary path; and
2. forbidden-path exclusion: each material superseded, duplicate,
   fallback, bypass or otherwise forbidden production path is absent,
   unreachable or refused at its declared boundary.

A successor passing does not prove the predecessor removed. Technical-debt
erasure evaluates two distinct, finite, subject-relative graphs (P3, P6):

1. production closure: the exact deployed, installed or otherwise runnable
   Product form and configuration, with its transitive imports, exports,
   package paths, configuration switches, registries, fallbacks, consumers,
   generated runtime artifacts, recovery paths and fresh-process
   reconstruction. No obsolete, bypass, fallback or rival production path
   may remain reachable inside this graph for the claimed scope; and
2. assurance/source closure: the source consumers, fixtures, proof
   scripts, generators, mutations and assurance tooling relied on for the
   claim. No obsolete assurance consumer may falsely supply closure
   evidence or reintroduce the removed production path into the Product
   graph.

A test-only seam is lawful when it is isolated from the Product
distribution, excluded from ordinary-path evidence and declared in the
assurance subject. Its presence outside the production graph is not a
production-path failure. A retained obsolete test or proof consumer stays
an assurance defect when it can falsely establish the claim or reintroduce
the removed path (P6).

Where proportionate and safe, assurance includes path-sensitive mutation or
sabotage (P5, P2):

- disabling the selected authoritative path prevents the Product scenario
  from succeeding;
- forcing or restoring a rival path causes refusal or a detected
  counterexample rather than silent success;
- corrupting a material interface or owner result is detected at the
  owning boundary; and
- removing an asserted obsolete path does not change the accepted Product
  outcome except through the declared deletion relation.

A Product outcome reached through a forbidden path is a falsified path
claim, not a passing Product test. A negative-path test that mutates the
exact subject without isolation, restoration and subject revalidation
invalidates its own assurance basis (P6, P3).

## 10. Testing evidence composition

One execution may provide several bound results. A supported user scenario
may supply user-acceptance evidence for the outcome, end-to-end evidence for
the runnable causal path, integration evidence for selected seams and unit
counterexamples for a module-owned algebra. Those claims stay distinct and
combine only through declared REFERENCE_FRAME §6 relations (P4a, P6;
provenance #testing-evidence-composition).

The default proof responsibilities are (P6, P2):

- user acceptance proves the outcome from the user's supported frame;
- end to end proves the complete authoritative runnable Product path;
- integration proves material participant composition; and
- unit proves module-owned laws, with evidence size and strategy
  proportional to their internal combinatorial complexity.

User acceptance alone may leave internal path singularity unevaluated.
End-to-end success alone may leave unselected user populations or
combinations unevaluated. Integration and unit results cannot stand in for
either broader claim. When the Product claim requires all of them, a
conflict or a missing result stays visible to the decision owner's
disposition and cannot be hidden by aggregate green status (P5, P6;
REFERENCE_FRAME §8, operational full coverage item 6).

## 11. Assurance subject acquisition and evaluation

Acquiring the assurance subject and evaluating it are distinct relations
(P6, P1; provenance #assurance-subject-acquisition-and-evaluation). Where a
claim depends on owner-issued Product, runtime, lifecycle, admission,
replay or projection truth, the testing frame acquires that truth through
the exact runnable owner surface, validator, projection, receipt or
reconstruction relation. A harness, fixture, expected-value builder, proof
script, assurance evaluator or assessor does not reconstruct a parallel
owner state from raw payloads, events, logs, filenames, labels or
implementation fragments and then evaluate that self-authored state as if
it were the Product subject.

After lawful acquisition, an independently derived oracle may evaluate the
governing claim. Generic assurance mechanics may compute bytes, digests,
ordering, equality, set membership, completeness and conjunction over
owner-issued evidence. Those mechanics stay evidence evaluators: they
cannot mint owner carriers, choose the current history, select the
authoritative path, interpret domain lifecycle or admission meaning, or
become a runtime fallback (P6; EVALUATION §2).

The rule does not require an evaluator to trust the implementation under
test as its semantic oracle; the oracle derives from Product, requirement
and accepted-design law. It requires the assurance subject to be the actual
owner-issued subject rather than a second implementation of the owner's
runtime meaning. If the required owner projection or observable seam is
absent, the result keeps a named assurance or design gap; the proof harness
does not fill it with rival semantics (P6, P5).

## 12. Counterexample localisation

A testing counterexample is returned to its earliest supported causal
frontier on the declared path. The frontier holds the causally minimal
violated owner relations or seam coordinates the evidence establishes;
earliest means minimal under the declared causal relation, not first in log
or clock order (P5, P6; provenance #counterexample-localization).

The localisation result represents exactly one of (P5, P1):

- one unique violated locus;
- a jointly established set of incomparable earliest violated loci whose
  combined violation is necessary to the supported causal explanation;
- unresolved alternative frontiers, when the evidence supports several
  possible causal explanations but cannot establish which occurred; or
- `indeterminate`, when the evidence cannot support a bounded frontier.

Localisation records the subject, basis, frontier form and members, causal
evidence, expected relations, the observed counterexample and the
downstream claims it invalidates. It does not collapse a jointly
established set into one arbitrary owner, and it does not report
unresolved alternatives as a joint cause (P5, P4b).

A localised frontier does not itself authorise broader test expansion,
compatibility repair, another controller or a reinterpretation of unchanged
upstream meaning. A resulting scope or design change follows the existing
re-entry relation (SPEC_METHOD §4; P6).

## 13. End-to-end interface integration frame

`urn:stdo:reference-frame:end-to-end-interface-integration:v1` is a
composite refinement whose identity resolves in
`urn:stdo:bounded-context:reference-frame-evaluation` (owned by
REFERENCE_FRAME) under the exact selected basis; its assurance law is
stated here. It relates the evaluation of public boundaries, design,
operators, owners and proof to the integration, end-to-end and
user-acceptance frames of §7. Like the set, it is available and is
activated only where the governing frame configuration or admitted work
authority selects it. It adds no fifth testing type, role or
universal activation gate (P2, P3; provenance
#derived-end-to-end-interface-integration-frame).

| Frame element | End-to-end interface integration |
|---|---|
| evaluation family | Does one outcome stay constructable, understandable and correctly realised across its material interface chain, with sufficient participant context and conserved meaning, authority and cause? |
| subject and basis | one Product outcome and an independently stated oracle; the governing requirements and design basis, exact source or workspace checkpoint, contracts and finite case population; for design claims, the declared participant roles, functional path, dependencies, configuration and capabilities; for claims over their realisation, the actual participants, callable selection, supported entry and exit, and the exact runnable artifact or install |
| material manifold | the producers, consumers, transformations and effect owners, as declared for design claims or actually selected for realised claims; at each material seam, the functional preconditions and postconditions, value and reference domains, lifecycle and time, supplied context, mutable subject, refusals, observations and user-visible result |
| coordinates and equality | distinct Product, artifact or install, workspace, observation, invocation, candidate, admitted result and evidence identities; exact revisions, domain, units, cardinality, ordering, empty, null or default meaning and validity interval; equal shape or output implies no equal meaning, provenance or authority |
| governing invariants | the selected Product, requirement, design and interface law; REFERENCE_FRAME declaration, conjunction and translation law; the claim boundaries and obligations below; the existing testing and assurance owners keep their laws |
| authority | existing owners keep semantic, operation, admission and reserved decision authority; the activation grants bounded evaluation, with construction only under its existing exact operation grant; the declared decision consumer disposes the closed result |
| evidence | source-linked contracts and both selected sides; for design claims, design relations and explicitly unresolved realisation facts; for claims over realised relations, the actual supplied request, context and response, callable and configuration identity, owner validation, effect and observation records and the ordinary caller's outcome; independently derived expected relations and disclosed substitution limits |
| capability envelope | competence in the outcome, functional composition, domain and lifecycle semantics, participant capabilities and causal diagnosis; sufficient access to the exact subject and evidence without altering a reviewed subject; required independence stays claim-relative |
| exclusions | hidden context or privilege, rival contract truth, inferred authority, undeclared substitutes, private or test-only paths for ordinary-path claims, candidate output treated as admission, fixture success treated as real user evidence, and unsupported whole-Product or all-future-case conclusions |
| result and relations | each activated claim returns a core result with its exact evidence, coverage, causal findings and residuals; shared evidence is referenced once; mandatory claims compose only through a declared same-basis or lawful-translation conjunction to the named decision consumer |
| invalidation | a material change of contract, domain, participant, prompt or context, capability, callable path, configuration, translation, relevant workspace observation, lifecycle, oracle or evidence population invalidates the affected conclusions; unchanged valid evidence and owner rulings stay reusable |
| qualification | the representative sensitivity and refusal cases below, bound to actual subjects, actor envelopes and independently stated expected relations; mechanical source checks supply no semantic or live-user qualification |

### Claim boundaries

(P6, P1; provenance #interface-integration-claim-boundaries)

| Claim | Evaluation and evidence boundary |
|---|---|
| contract sufficiency | Can each participant determine and perform its responsibility from the declared interface and the available context? Source-grounded design evaluation may establish this claim without an implemented runtime; unresolved realisability or actor-context questions stay explicit. |
| boundary congruence | Do the actual selected producers, transformations and consumers preserve the declared domains, meanings, lifecycle and authority? An actual-composition claim acquires both sides and their exchanges; design correspondence alone proves no implementation behaviour. |
| path realisation | Does the exact runnable subject use the authoritative entry-to-outcome path through its material state, effect and observation boundaries? Matching output through another path is insufficient. |
| user usability | Can the ordinary human, LLM or software caller obtain the selected outcome using only its declared context, access and supported surface? Internal success or validator-aware fixtures cannot establish this claim. |

The activation selects claims from the work's applicability (ACTIVATION §1)
and states the scope reason for each unselected claim. Design-only work
does not require unavailable runtime evidence and does not report runtime or
UAT satisfaction. An unknown material condition keeps its dependent claim
unresolved; omission cannot close it. A full end-to-end usability claim
needs all four distinct results and their explicit conjunction. Transport,
parse, admission, semantic satisfaction, operation completion and user
success are not interchangeable (P5, P6).

### Obligations

Existing truth surfaces are reused. The working record adds only missing
cross-interface relations; schemas, prompts, adapters, indexes and tests do
not become another contract owner (P6, P2; provenance
#interface-integration-obligations). For each material seam:

1. Bind the functional input domain, producer success postconditions,
   consumer preconditions, permitted effects, refusals and observable exit.
   Direct successful handoff requires the producer's guarantees to meet the
   consumer's preconditions. An interface may instead emit candidates:
   candidate output, later admission and semantic assessment stay distinct
   declared stages. A normal model refusal or an inadmissible candidate does
   not by itself falsify an adequately declared candidate interface; the
   exact promised outcome and refusal behaviour are evaluated (P4a, P5).
2. Make material actor obligations and domains available through the
   actual interface or context, or through an exact locator the actor can
   lawfully resolve. Bind the LLM role, instructions, supplied context,
   tools and model or transport configuration where material. Generic
   governance access does not replace the Product-specific contract or
   authorise inference of hidden validator rules. Existing deterministic
   owners compute the available facts and expose their owned relation to
   context and validation by reuse or a proven equivalent projection.
   Semantic actors judge meaning within that domain; reserved owner
   rulings, eligibility, authority and admission are not inferred from an
   actor response or a frame label (P0, P6, P1).
3. Preserve domain and temporal meaning through serialisation, parsing,
   normalisation and adaptation. A lawful translation binds source and
   target coordinates, preserved meaning, accepted loss, provenance,
   governing owner and refusal conditions. Distinguish proposed, admitted,
   assessed and completed states; active input from historical context;
   current validity from mere byte availability. Equal wire shape is no
   translation proof (P1, P3; REFERENCE_FRAME §6).
4. Observe the relevant current mutable workspace for each later
   operation, and bind that observation separately from immutable
   authority, artifacts, history and prior candidates. Changed support
   invalidates dependent conclusions; unaffected accepted work stays
   reusable. A snapshot does not replace the current subject, and a change
   of actor alone is no reason to repeat still-valid work (P3, P4b;
   ACTIVATION §7).
5. Follow the actual callable path and the existing effect owners through
   the selected exit and any required fresh observation. A hidden fallback,
   state injection, manually repaired output, private entry or undeclared
   retry cannot support an ordinary real-path claim. A pure function
   acquires no new event lifecycle because this frame evaluates it (P6,
   P3).
6. Preserve diagnostic cause through wrappers and projections. Apply §12:
   report the supported causal frontier, not merely the first log or clock
   occurrence. Keep the originating seam, bounded field or path, expected
   domain or basis, observed mismatch and evidence locator where available,
   with downstream symptoms, successful work and the declared continuation
   or block. Preserve joint causes, alternative frontiers and
   indeterminacy; do not invent a unique cause. Product redaction rules
   still govern sensitive content. Missing required diagnostic evidence
   stays a named gap. Return the smallest supported owner or re-entry;
   diagnosis grants no repair or retry (P5, P4b, P6).

Evidence acquisition follows §11: owner facts are acquired through existing
surfaces and evaluated with an independent contract-derived oracle.
Computed facts, contextual judgments and reserved owner rulings keep their
distinct owners and validity scopes (P6).

For an LLM-interface usability claim, clean-room LLM UAT is used, with the
ordinary supplied context and permitted tools and without private
implementation knowledge or fixture assistance. Expected outcomes are
recorded before responses are inspected. The sunny case and the ordinary
ambiguity and negative cases material to the claim are included.
Substitutes are disclosed; replayed or fabricated responses prove only
their stated narrower relation, not live-provider usability. Responses are
not edited, and nothing is silently retried until green. Live claims need
live evidence under §2, not a new universal live-provider requirement
during design (P6, P5; EVALUATION §3, expectations before exposure).

An early sunny thread can establish bounded evidence while the unexercised
claims stay open (the sequencing heuristic of SPEC_METHOD §8). This frame
adds no exhaustive-hardening prerequisite, scenario quota, controller,
runtime, generator, routine human approval, new ledger or automatic extra
agent. Existing authority selects proportionate assurance and any further
operation. The result returns the four claim dispositions, the exact
exercised subject and path, the supported mismatch, retained work,
substitutions, residuals and invalidators in the existing work carrier; it
is neither acceptance nor a grant of the next action (P2, P6; ACTIVATION
§6).

### Computational whole-path evaluation

For material computational composition or recurrence work, the selected
interface claims are composed with evaluations of the path's operators,
owners, reused foundations and proof, to evaluate one complete
producer-to-consumer path under the design profile's computational
realisation and recurrence law (DESIGN_MODULE). The evaluation binds fact
establishment, each consumer, validity and invalidation, effects, retained
alternatives and accumulated work. It evaluates equivalent computation
across different domain names without assuming semantic equivalence.
Qualification challenges the design's declared workload and operational
assumptions, and preserves the independent scope, freshness and effect
checks that serve distinct supported obligations (P4a, P1, P2; provenance
#computational-whole-path-evaluation).

An identifiable complete-path result and its evidence return to the
declared decision consumer; a collection of local successes cannot replace
that result. Design-only evidence establishes only the design claim; claims
about actual work need observations on the selected path. Valid unchanged
results are reused, and affected reassessment is activated on a material
change of path, basis or workload. This is a bounded composition of
existing frames, not a permanent actor, an extra frame family, a per-helper
review or a separate accounting ledger (P4b, P2).

### Qualification

These are representative source-contract discriminators: not an executed
trial, a universal test quota or whole-Product qualification. Each selected
case binds its own exact subject, oracle, evidence and claim scope (P6,
P5; provenance #interface-integration-qualification; EVALUATION §7).

| Case | Required discrimination |
|---|---|
| empty and non-empty eligible domains | Ordinary context makes both domains usable; a universal empty-value workaround cannot replace the governing domain. A hidden required rule defeats contract sufficiency even when the validator correctly refuses. |
| adequate candidate contract and rejected response | Legitimate refusal or admission filtering is told apart from an inadequate interface or a violated success guarantee; model variability alone is no frame failure. |
| same-response or historical-only reference | Eligibility and lifecycle come from the owning domain; available or equal-looking references are not automatically current admissible inputs. |
| individually valid but temporally mismatched carriers | Different observations or admission states can falsify boundary congruence despite matching shapes. |
| meaning-changing translation | Loss of units, default, identity or ordering is detected against the independent outcome oracle, even when both shapes validate. |
| fixture knows a hidden rule | Mechanical success leaves user usability unproved; it cannot hide missing ordinary actor context. |
| expected output through a forbidden path | Path realisation is falsified; equal output does not discharge the actual-path obligation. |
| changed workspace and reusable accepted work | Affected context and dependent evidence are refreshed while unaffected valid work is kept; history does not stand in for the current subject. |
| wrapped or ambiguous failure | The supported originating causal frontier and its uncertainty are kept, not replaced by a downstream symptom or an invented unique cause. |
| design-only sufficient contract | A bounded contract result can close while runtime and user claims stay unclaimed or unresolved according to their applicability; no runtime or UAT satisfaction is inferred. |

## 14. Source dispositions

Rows received by this member. In the first table anchors are into rc.2
SPEC_METHOD.md; in the second, into rc.2 STDO_REFERENCE_FRAME_BASELINE.md.
A locus is a section of this file. Every row is restated in this member's
own text; a route is provenance only. Rows of other predecessor members
that land here (the design profile's 6A to 6C, the ticket law's test-case
authority) are disposed at their members' activations and listed here
then.

| Anchor | Disposition | Locus |
|---|---|---|
| #verification-layers | conserved; the predecessor's example ("compositional graphs", "Fragment types", "a reusable discovery workflow") is generalised to a reusable composable unit, since the example named a profile's subject and the law does not depend on it | §1 |
| #testing-strategy-taxonomy | conserved in full: both authority sources, the sandbox-only rule for UAT, the harnessed and live modes, the necessary-not-sufficient rule and the terminology list; the owner of the product-assurance bounded context is this member rather than SPEC_METHOD; `DESIGN_MODULE_METHOD.md` is carried as the DESIGN_MODULE member and "IACS" as the carrier inventory the design declares | §2 |
| #fixture-and-proof-portability-rule | conserved | §2 Fixture and proof portability |
| #test-authority-rule | conserved | §3 |
| #scenario-bundle-rule | conserved | §4 |
| #installed-dev-proof-rule | conserved | §5 |
| #significant-path-coverage-rule | conserved | §6 |

| Anchor | Disposition | Locus |
|---|---|---|
| #canonical-compression | conserved in part here: the testing-frame evidence topology; the rest of the row is EXECUTIVE_BASELINE §1 | §7 The set |
| #testing-frame | conserved | §7 Terms |
| #authoritative-product-path | conserved | §7 Terms |
| #material-combinatorial-complexity | conserved | §7 Terms |
| #derived-product-testing-frame-set | conserved; the predecessor's condition "when this profile supports" is carried as selection by the governing frame configuration or work authority, so placement in tier 2 makes the set available and adopts nothing; the sentence relating the set to the profile's Proof family is EXECUTIVE_BASELINE §11 | §7 The set |
| #derived-user-acceptance-frame | conserved; eleven elements; "UP-001, UP-008 and UP-022" written as EVALUATION §1, §2, §3, §6 and §7, the full successor loci of those laws | §7 User-acceptance frame |
| #derived-end-to-end-frame | conserved; eleven elements | §7 End-to-end frame |
| #derived-integration-frame | conserved; eleven elements | §7 Integration frame |
| #derived-unit-test-frame | conserved; eleven elements; "IACS" written as the carrier inventory the design declares, and the design profile's unit-proof law named as DESIGN_MODULE | §7 Unit frame |
| #combinatorial-coverage-and-testing-value-index | conserved; the eight index terms and the nine Product factors | §8 |
| #legitimate-path-and-technical-debt-erasure | conserved | §9 |
| #testing-evidence-composition | conserved; "Executive disposition" written as the decision owner's disposition | §10 |
| #assurance-subject-acquisition-and-evaluation | conserved; "Reviewer" written as assessor | §11 |
| #counterexample-localization | conserved | §12 |
| #derived-end-to-end-interface-integration-frame | conserved; twelve elements; the frame identity is unchanged and still resolves in the reference-frame-evaluation context owned by REFERENCE_FRAME, its assurance law now stated in this member; the named families (Public Boundary, Design, Operator, Owner, Proof) are written as evaluations of those concerns, and their mapping is EXECUTIVE_BASELINE §11 | §13 |
| #interface-integration-claim-boundaries | conserved; four claims | §13 Claim boundaries |
| #interface-integration-obligations | conserved; six obligations; "Apply Steel-Thread Delivery" written as the sequencing heuristic of SPEC_METHOD §8 | §13 Obligations |
| #computational-whole-path-evaluation | conserved; the families Operator, Owner, Reuse/Foundation and Proof written as evaluations of operators, owners, reused foundations and proof, mapped in EXECUTIVE_BASELINE §11; "STDO-UP-019" written as the design profile's computational realisation law | §13 Computational whole-path evaluation |
| #interface-integration-qualification | conserved; ten cases | §13 Qualification |
