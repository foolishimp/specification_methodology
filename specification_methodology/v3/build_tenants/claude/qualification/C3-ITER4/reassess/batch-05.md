# I4-04 reading batch 05

Rows: 20. Members: ['SPEC_METHOD.md', 'STDO_REFERENCE_FRAME_BASELINE.md', 'TICKET_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001` at rc.2:

```text
Every load-bearing proof identifies the exact subject, intended property,
governing basis, relation between witness and claim, nearest weaker excluded
property, and falsification condition before selecting its witness. Without
those relations, the result is evidence discovery rather than closure-grade
proof.

Packaging, syntax, compilation, file presence, invocation, or local behavior
must not substitute for semantic, authority-bearing, installed, release, or
end-to-end proof merely because the weaker property is easier to measure.
```

Successor, `EVALUATION.md#1-claims`:

```text
A load-bearing claim names its exact subject, the property claimed, the
governing basis, the relation between witness and claim, the nearest weaker
property it excludes, and its falsifier, before a witness is selected.
Without these it is evidence discovery, not proof. Packaging, syntax,
compilation, presence, invocation or local behaviour never substitutes for a
semantic, authority-bearing, installed, release or end-to-end claim because
the weaker property is easier to measure (P6; conserves
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001)).

Boundary congruence. A checker, validator, harness, reviewer or other
assurance surface supporting promotion or closure binds the exact claimed
subject and its authoritative composition relation. Evidence over one file
or carrier proves only that boundary; it cannot establish a multi-file or
carrier-set claim. Cross-carrier satisfaction and conflict are decided at
the declared composite boundary (P3, P6). A claim of mechanical enforcement
names an executable or reproducible predicate and a witness reachable
through the declared ordinary assurance path; a planned or
specification-only harness is planned evidence, not observed verification,
and until both the predicate and such a witness are observed the claim
remains open or is explicitly downgraded to the planned property (P6;
conserves
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
first two paragraphs).

A claim's quantifier, population and scope cannot exceed its evaluated
evidence. Generalising a local defect or observation needs a declared
inference relation, the relevant comparable population, explicit
counterexample treatment and governing evidence. Later counterevidence
invalidates every dependent verdict until the claim-evidence relation is
superseded, withdrawn or requalified (UP-022). The quantifier rule and the
boundary rule are false if assurance observes a weaker or different
subject, if per-carrier evidence closes an unevaluated composite claim, if
mechanical enforcement lacks its predicate or a reachable witness, if
planned evidence is reported as observed verification, if a verdict outruns
its evaluated population or declared inference relation, or if dependent
verdicts survive material counterevidence without requalification.
```


### Row `SPEC_METHOD.md#renewal-path` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#renewal-path` at rc.2:

```text
Intent is not only top-down. The full homeostatic cycle includes a reverse path where real use cases generate new intent:

```
Current spec → real-world use case → gap analysis → new goals / intent
```

This is how the system stays alive instead of becoming a frozen constitution. The generative rule:

1. A real use case (scenario, deployment, external review) hits the current model
2. Gap analysis identifies what the constitution cannot express
3. If the gap is constitutional (not just a missing implementation), new goals and/or intent are written
4. The repriced surface then flows forward through the chain: product → requirements → design → code

New intents emerge from repeated, real use-case pressure against the current model — not from abstract speculation. The gap must be concrete before it becomes intent. Ad hoc coding pressure does not generate intent; explicit gap analysis does.

This flow is not a one-pass waterfall computation. It is a cumulative iteration:

- requirements and design are refined over time
- code is repeatedly re-derived against the current constitutional surface
- gaps discovered during implementation, testing, replay, or scenario work feed back into repricing

What must remain stable is the full direction of authority: goals govern intent, intent governs product, product governs requirements, requirements govern design, and requirements plus design govern code, even when the project advances through many iterations.

---
```

Successor, `SPEC_METHOD.md#renewal-path`:

```text
Intent is not only top-down. The full homeostatic cycle includes a reverse
path where real use cases generate new intent (P2; rc.2 #renewal-path):

```text
current specification → real-world use case → gap analysis → new goals or intent
```

The generative rule: a real use case (scenario, deployment, external review)
hits the current model; gap analysis identifies what the constitution cannot
express; if the gap is constitutional, not merely a missing implementation,
new goals or intent are written; the repriced surface then flows forward
through the chain, product to requirements to design to code. New intents
emerge from repeated, real use-case pressure against the current model, not
from abstract speculation; the gap is concrete before it becomes intent. Ad
hoc coding pressure does not generate intent; explicit gap analysis does.
This is how the system stays alive instead of becoming a frozen
constitution.

The flow is not a one-pass waterfall computation; it is cumulative
iteration: requirements and design are refined over time; code is
repeatedly re-derived against the current constitutional surface; gaps
discovered during implementation, testing, replay or scenario work feed
back into repricing. What stays stable is the full direction of authority:
goals govern intent, intent governs product, product governs requirements,
requirements govern design, and requirements plus design govern code,
through every iteration.
```


### Row `SPEC_METHOD.md#required-migration-protocol` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#required-migration-protocol` at rc.2:

```text
Every core interface migration must explicitly declare:

1. the exact affected migration scope
2. every explicitly excluded or disjoint Product or compatibility scope and its
   deterministic routing relation
3. the new authoritative contract
4. the superseded contract or surface
5. the authoritative closure law for the new contract
6. the full set of producers of the old and new contract
7. the full set of consumers of the old and new contract
8. every projection, report, status surface, and proof surface that derives from it

Every old path must then be classified as one of:

- `remove`
- `replace`
- `re-authorize`
- `temporary scaffolding`

Temporary scaffolding is lawful only if it is explicitly non-authoritative and
scheduled for removal before closure.
```

Successor, `SPEC_METHOD.md#required-migration-protocol`:

```text
Every core interface migration explicitly declares: the exact affected
migration scope; every explicitly excluded or disjoint product or
compatibility scope and its deterministic routing relation; the new
authoritative contract; the superseded contract or surface; the
authoritative closure law for the new contract; the full set of producers
of the old and new contract; the full set of consumers of the old and new
contract; and every projection, report, status surface and proof surface
that derives from it. Every old path is then classified as `remove`,
`replace`, `re-authorize` or `temporary scaffolding`. Temporary scaffolding
is lawful only if it is explicitly non-authoritative and scheduled for
removal before closure (P6, P4b; rc.2 #required-migration-protocol).
```


### Row `SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#shared-installed-release-basis-and-toolchain-manager` at rc.2:

```text
Within the product-definition-routing bounded context, an **Installed Release
Basis** is the pair:

```text
(immutable stdo://releases/<cut>/ URI, installed-manifest SHA-256)
```

The URI identifies one immutable annotated RC cut. The digest identifies the
deterministic installed-release manifest that binds its tag object, commit,
repository tree, standards subtree, exact standards inventory, member bytes,
and admitted auxiliary payloads. The manifest shape is owned by
`schemas/installed-release-manifest.schema.json`. It is transport and integrity
evidence, not a replacement constitution.

An **Adoption Plan** is the read-only, deterministic acceptance object binding
one current Product Definition's identity and bytes to its current basis and
one resolved immutable target's cut, annotated tag object, commit, tree, and
installed-manifest digest. Its SHA-256 is the operator-presentable acceptance
token; possession alone does not grant authority, while a mismatch proves that
the presented subject is no longer the subject being mutated. A **Fleet
Adoption Plan** binds an authorized fleet root and the complete ordered set of
per-definition plan digests under the same law.

Plan hashing uses the acceptance object only: local installation status and
machine-local install paths are excluded. Its canonical bytes are UTF-8 JSON
with recursively sorted object keys, two-space indentation, LF line endings,
and one final LF. Fleet order is deterministic discovery-path order. These
rules make a presented digest independently reproducible rather than an opaque
session token.

The **STDO Toolchain Manager** is the bounded executable realization that:

- installs each immutable cut once in a shared, versioned release store;
- resolves logical `stdo://releases/...` URIs to verified installed bytes;
- inventories and verifies complete installed distributions;
- synchronizes the exact basis already selected by a Product Definition;
- emits an exact digest-bound adoption plan from a mutable version-line
  selector and performs adoption only when that plan is explicitly accepted;
- manages the stable marker-bounded bootstrap in declared agent files; and
- applies those operations to an explicitly discovered fleet of Product
  Definitions.

The store may live at any machine-local path. Its registry maps logical release
URIs to installed paths and manifest digests, but owns neither Product
selection nor method meaning. A consumer repository therefore does not need a
project-local standards copy or a prescribed folder structure. Several Product
Definitions on one machine may select different installed cuts concurrently.
Every manager-owned component from the configured store root downward must be
a physical directory or regular file of its declared type. A symlink, junction,
reparse point, device, socket, or other redirection or special entry fails
closed. Verification inventories every filesystem entry type, including
directories, and rejects any entry not derived from the manifest's exact file
paths. It never follows an unmanifested alias.

`constitution.stdo.source.repository` identifies the transport source.
`constitution.stdo.selector` is a mutable `stdo://channels/<version>` discovery
selector whose Git alias semantics are owned by `RELEASE_METHOD.md`. Neither is
operative authority. `constitution.stdo.basis.uri` and
`constitution.stdo.basis.manifest_sha256` are the sole authored STDO selection
for that Product Definition.

The manager observes these command boundaries:

- `install` admits one explicitly named immutable RC cut without changing any
  Product Definition;
- `sync` installs and verifies only the exact basis already selected by the
  Product Definition and never consults its mutable selector;
- `adopt --dry-run` resolves the annotated selector and immutable RC, presents
  the target cut, tag object, commit, tree, manifest digest, current Product-
  Definition byte digest, and a deterministic adoption-plan digest without
  mutation;
- mutating `adopt` requires that exact prior plan digest as explicit
  acceptance, re-derives it before installation, installs only the bound target,
  rechecks the Product Definition bytes, and atomically changes only its basis
  and basis-relative schema locator; any drift refuses mutation;
- `status`, `verify`, `list`, `manifest`, and `resolve` are read-only with
  respect to Product Definitions; and
- fleet adoption emits and requires explicit acceptance of one aggregate plan
  digest over every per-definition plan; all fleet writes require explicit
  whole-selection authorization and do not infer composition or inheritance
  from directory nesting.

Missing cuts, moved immutable tags, tag-to-commit mismatch, manifest-digest
mismatch, missing, extra, or changed installed members, ambiguous Product
Definition discovery, unaccepted or stale adoption plans, URI escape, physical
store redirection, undeclared filesystem entry types, and malformed bootstrap
markers fail closed. Every `stdo:` schema locator is parsed before schema
loading under URI scheme case-insensitivity and must name the same immutable
cut as `constitution.stdo.basis`; spelling variation cannot cross that basis.
No cache, registry entry, source checkout, version alias, schema, or agent file
may silently replace the basis selected in the Product Definition.

`constitution.agent_bootstrap` does not embed another constitution. It names
one basis-qualified bootstrap entrypoint and the local instruction files whose
small discovery block the manager owns between explicit markers. Each target
is a portable relative path resolved against `product.source_project`; absolute
paths, parent traversal, redirected path components, and escape from that
boundary fail closed. A fleet additionally confines every resolved source
project to its explicitly authorized fleet root and preflights every target
before the first write. Exactly one correctly ordered marker span may be
replaced. Bytes before and after it, including trailing whitespace, remain
project-owned and byte-identical; appending a new span preserves all existing
bytes as an exact prefix. The bootstrap routes agents to the applicable Product
Definition, exact installed basis, and owning sources; it cannot restate or
override them.

Recursive fleet discovery prunes these exact directory names as VCS,
dependency, generated, cache, or managed-store internals:
`.git`, `.hg`, `.svn`, `.bzr`, `.venv`, `venv`, `node_modules`, `vendor`,
`site-packages`, `build`, `dist`, `out`, `target`, `.gradle`, `.tox`, `.nox`,
`.cache`, `.ruff_cache`, `.mypy_cache`, `.pytest_cache`, `__pycache__`,
`.genesis`, and `.stdo`. Discovered Product Definitions may not themselves be
symlinks. These exclusions are discovery law, not evidence that an excluded
tree lacks another independently governed Product.
```

Successor, `PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`:

```text
Within the product-definition-routing context an Installed Release Basis
is the pair (P3; rc.2
#shared-installed-release-basis-and-toolchain-manager):

```text
(immutable stdo://releases/<cut>/ URI, installed-manifest SHA-256)
```

The URI identifies one immutable annotated RC cut. The digest identifies
the deterministic installed-release manifest, which binds the cut's tag
object, commit, repository tree, standards subtree, exact standards
inventory, member bytes and admitted auxiliary payloads. The manifest shape
is owned by `schemas/installed-release-manifest.schema.json`. The manifest
is transport and integrity evidence, not a replacement constitution (P6).

An Adoption Plan is the read-only, deterministic acceptance object that
binds one current Product Definition's identity and bytes to its current
basis and to one resolved immutable target's cut, annotated tag object,
commit, tree and installed-manifest digest. Its SHA-256 is the
operator-presentable acceptance token. Possession of the token alone grants
no authority; a mismatch proves that the presented subject is no longer the
subject being mutated (P6, P3). A Fleet Adoption Plan binds an authorised
fleet root and the complete ordered set of per-definition plan digests
under the same law.

Plan hashing covers the acceptance object only: local installation status
and machine-local install paths are excluded. The canonical bytes are UTF-8
JSON with recursively sorted object keys, two-space indentation, LF line
endings and one final LF. Fleet order is deterministic discovery-path
order. These rules make a presented digest independently reproducible
rather than an opaque session token (P3, P6).

The STDO Toolchain Manager is the bounded executable realisation that (P2,
P3):

- installs each immutable cut once in a shared, versioned release store;
- resolves logical `stdo://releases/...` URIs to verified installed bytes;
- inventories and verifies complete installed distributions;
- synchronises the exact basis already selected by a Product Definition;
- emits an exact digest-bound adoption plan from a mutable version-line
  selector and performs adoption only when that plan is explicitly
  accepted;
- manages the stable marker-bounded bootstrap in declared agent files; and
- applies those operations to an explicitly discovered fleet of Product
  Definitions.

The store may live at any machine-local path. Its registry maps logical
release URIs to installed paths and manifest digests and owns neither
Product selection nor method meaning. A consumer repository therefore needs
no project-local standards copy and no prescribed folder structure, and
several Product Definitions on one machine may select different installed
cuts concurrently (P3, P6). Every manager-owned component from the
configured store root downward is a physical directory or regular file of
its declared type; a symlink, junction, reparse point, device, socket or
other redirection or special entry fails closed. Verification inventories
every filesystem entry type, directories included, rejects any entry not
derived from the manifest's exact file paths, and never follows an
unmanifested alias (P5, P3).

`constitution.stdo.source.repository` identifies the transport source.
`constitution.stdo.selector` is a mutable `stdo://channels/<version>`
discovery selector whose alias semantics are owned by the release law (the
[RELEASE](RELEASE.md) member). Neither is operative authority.
`constitution.stdo.basis.uri` and `constitution.stdo.basis.manifest_sha256`
are the sole authored STDO selection for that Product Definition (P6, P3).

The manager observes these command boundaries (P6, P5):

- `install` admits one explicitly named immutable RC cut without changing
  any Product Definition;
- `sync` installs and verifies only the exact basis already selected by
  the Product Definition and never consults its mutable selector;
- `adopt --dry-run` resolves the annotated selector and immutable RC, and
  presents the target cut, tag object, commit, tree, manifest digest,
  current Product-Definition byte digest and a deterministic
  adoption-plan digest, without mutation;
- mutating `adopt` requires that exact prior plan digest as explicit
  acceptance, re-derives it before installation, installs only the bound
  target, rechecks the Product Definition bytes, and atomically changes
  only its basis and its basis-relative schema locator; any drift refuses
  mutation;
- `status`, `verify`, `list`, `manifest` and `resolve` are read-only with
  respect to Product Definitions; and
- fleet adoption emits, and requires explicit acceptance of, one aggregate
  plan digest over every per-definition plan; all fleet writes require
  explicit whole-selection authorisation and infer no composition or
  inheritance from directory nesting.

Missing cuts, moved immutable tags, tag-to-commit mismatch, manifest-digest
mismatch, missing, extra or changed installed members, ambiguous Product
Definition discovery, unaccepted or stale adoption plans, URI escape,
physical store redirection, undeclared filesystem entry types and malformed
bootstrap markers fail closed (P5). Every `stdo:` schema locator is parsed
before schema loading under URI scheme case-insensitivity and names the
same immutable cut as `constitution.stdo.basis`; spelling variation cannot
cross that basis. No cache, registry entry, source checkout, version alias,
schema or agent file may silently replace the basis selected in the
Product Definition (P6, P3).

`constitution.agent_bootstrap` embeds no other constitution. It names one
basis-qualified bootstrap entrypoint and the local instruction files (such
as `AGENTS.md` or `CLAUDE.md` targets) whose small discovery block the
manager owns between explicit markers. Each target is a portable relative
path resolved against `product.source_project`; absolute paths, parent
traversal, redirected path components and escape from that boundary fail
closed. A fleet additionally confines every resolved source project to its
explicitly authorised fleet root and preflights every target before the
first write. Exactly one correctly ordered marker span may be replaced;
the bytes before and after it, trailing whitespace included, stay
project-owned and byte-identical, and appending a new span preserves all
existing bytes as an exact prefix. The bootstrap routes agents to the
applicable Product Definition, the exact installed basis and the owning
sources; it can neither restate nor override them (P6, P3, P5).

Recursive fleet discovery prunes these exact directory names as
version-control, dependency, generated, cache or managed-store internals:
`.git`, `.hg`, `.svn`, `.bzr`, `.venv`, `venv`, `node_modules`, `vendor`,
`site-packages`, `build`, `dist`, `out`, `target`, `.gradle`, `.tox`,
`.nox`, `.cache`, `.ruff_cache`, `.mypy_cache`, `.pytest_cache`,
`__pycache__`, `.genesis` and `.stdo`. A discovered Product Definition may
not itself be a symlink. These exclusions are discovery law, not evidence
that an excluded tree lacks another independently governed Product (P5,
P6).
```


### Row `SPEC_METHOD.md#significant-path-coverage-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#significant-path-coverage-rule` at rc.2:

```text
The proving surface must declare and exercise the significant paths for the
behavior being claimed.

Exhaustive proof does not mean every possible branch in every file. It means the
project names the meaningful paths and proves them intentionally.

The significant paths usually include, where relevant:

- intended success path
- fail-closed or rejection path
- boundary or control path
- integration, dispatch, or transport path
- recovery, retry, or replay path

If the significant paths are not declared, scenario coverage cannot be judged.
If they are declared but not exercised, the behavior is not fully proved.

---
```

Successor, `ASSURANCE.md#6-significant-path-coverage`:

```text
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
```


### Row `SPEC_METHOD.md#sprint-execution-boundary` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#sprint-execution-boundary` at rc.2:

```text
A sprint is a bounded execution-control surface.

It is not a new layer in the constitutional chain.

A sprint may batch work, coordinate tickets or iteration entries, price proof
cost, and force close review under existing Goals, Intent, Product Definition,
Requirements, and Design authority. It must not create, supersede, weaken, or
override that authority.

A lawful sprint states at least:

- the goal or work-wave it serves
- the upstream authority surfaces it depends on
- the scope it admits
- the product, requirement, design, runtime, data-contract, or governance
  boundaries it excludes
- the change classes it expects to contain
- the local proof or compliance debt, if any, that may be deferred during the
  sprint
- the closure trigger and closure law
- the paydown or repricing path for debt discovered at close

Sprints exist because proof cost is not uniform. For some work, especially
projection-surface and UX iteration, proving every micro-change before the next
change can cost more than making the bounded change visible and correcting it
at close. That optimization is lawful only when the deferred cost remains local,
visible, bounded, and repayable.

Deferred compliance inside a sprint is escrow, not acceptance. It cannot satisfy
method, release, or product closure until it is paid down, explicitly accepted
under the governing method, or repriced into the appropriate upstream surface.

A sprint may be recommended for close when any of these become true:

- its timebox expires
- the intended scope has been reached
- accumulated changed surface area makes continued iteration more expensive
  than review
- review uncertainty makes more work unsafe without reconciliation
- discovered gaps suggest the sprint boundary is no longer the right container

Sprint close is a forensic reconciliation event, not automatic approval. Close
review compares the accumulated work and evidence against the governing
authority, classifies each gap, accepts compliant work, opens paydown work for
local debt, and escalates any authority drift through the lawful change class.

If a sprint discovers a goal, intent, product, requirement, design, runtime,
data-contract, governance, or other product-truth change, the sprint manifest
does not authorize landing that change. The work must be split, escalated,
repriced, or carried as explicit paydown according to the governing method.

`TICKET_METHOD.md` defines the sprint and ticket mechanics. Domain refinements,
such as `UX_METHOD.md`, may define when sprint compliance escrow is an
appropriate cost optimization for that domain.

---
```

Successor, `SPEC_METHOD.md#sprint-execution-boundary`:

```text
A sprint is a bounded execution-control surface, not a new layer in the
constitutional chain (P6, P2; rc.2 #sprint-execution-boundary). It may
batch work, coordinate tickets or iteration entries, price proof cost and
force close review under existing goals, intent, product definition,
requirements and design authority; it does not create, supersede, weaken
or override that authority.

A lawful sprint states at least: the goal or work wave it serves; the
upstream authority surfaces it depends on; the scope it admits; the
product, requirement, design, runtime, data-contract or governance
boundaries it excludes; the change classes it expects to contain; the
local proof or compliance debt, if any, that may be deferred during the
sprint; the closure trigger and closure law; and the paydown or repricing
path for debt discovered at close.

Sprints exist because proof cost is not uniform. For some work, especially
projection-surface and user-interface iteration, proving every micro-change
before the next change can cost more than making the bounded change visible
and correcting it at close. That optimisation is lawful only when the
deferred cost remains local, visible, bounded and repayable. Deferred
compliance inside a sprint is escrow, not acceptance: it satisfies no
method, release or product closure until it is paid down, explicitly
accepted under the governing method, or repriced into the appropriate
upstream surface.

A sprint may be recommended for close when its timebox expires, its
intended scope has been reached, accumulated changed surface area makes
continued iteration more expensive than review, review uncertainty makes
more work unsafe without reconciliation, or discovered gaps suggest the
sprint boundary is no longer the right container. Sprint close is a
forensic reconciliation event, not automatic approval: close review
compares the accumulated work and evidence against the governing
authority, classifies each gap, accepts compliant work, opens paydown work
for local debt, and escalates any authority drift through the lawful
change class. If a sprint discovers a goal, intent, product, requirement,
design, runtime, data-contract, governance or other product-truth change,
the sprint manifest does not authorise landing it; the work is split,
escalated, repriced or carried as explicit paydown.
[TICKETS §3](TICKETS.md#3-sprint-rules) defines the sprint mechanics,
including compliance escrow, and §4 the ticket mechanics; a profile may
define when sprint compliance escrow is an appropriate cost optimisation
for its domain (PROFILES).
```


### Row `SPEC_METHOD.md#test-authority-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#test-authority-rule` at rc.2:

```text
Every live requirement must have written testcase authority.

That authority may include scenario bundles, ordered testcase sequences, negative
or control cases, and other explicit evidence cases as appropriate to the kind of
truth being proved, but it must exist in written form and be traceable.

No live requirement is considered fully proved if it relies only on informal
operator confidence, ambient habit, or an unlabeled test corpus.

---
```

Successor, `ASSURANCE.md#3-test-authority`:

```text
Every live requirement has written test-case authority (P6; rc.2
#test-authority-rule). That authority may include scenario bundles,
ordered test-case sequences, negative or control cases and other explicit
evidence cases appropriate to the kind of truth being proved; it exists in
written form and is traceable. No live requirement is fully proved on
informal operator confidence, ambient habit or an unlabelled test corpus
(P6; EVALUATION §5, green labels are not acceptance). The derivation of
each test case from admitted work authority is
[TICKETS §7 Test case authority](TICKETS.md#test-case-authority).
```


### Row `SPEC_METHOD.md#testing-strategy-taxonomy` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#testing-strategy-taxonomy` at rc.2:

```text
`SPEC_METHOD.md` owns the product-assurance bounded context
`urn:stdo:bounded-context:product-assurance` under the selected complete STDO
basis. This section owns the Product-level test-authority taxonomy.
`DESIGN_MODULE_METHOD.md` retains ownership of module-derived unit-proof law;
the shared context does not merge those authority sources.

Every executable proof surface must declare its authority source.

For ticketed work, the immediate proof authority is the admitted ticket and its
triage path. Tests derive from the ticket's lawful re-entry point and the
governing constitutional or realization-law surfaces it cites; they do not
derive expected results from current implementation behavior.

Authority source is not the same thing as execution breadth. A test may be
small or broad, fast or slow, deterministic or live, but it still derives from
one of two primary authorities:

1. **Design/module conformance tests**
2. **UAT / acceptance tests**

Design/module conformance tests derive from realization authority:

- governing design
- module ownership
- IACS or equivalent carrier inventory
- structural carrier diagrams when present
- boundary-local fail-closed law

They answer:

- did the implementation realize the module or design boundary correctly?

Unit tests are design/module conformance tests. Module integration tests,
negative tests, and fail-closed tests may also be design/module conformance
tests when their proof target is a designed module boundary rather than a user
scenario.

UAT / acceptance tests derive from constitutional user or product authority:

- requirements
- acceptance criteria
- declared scenarios or use cases
- product-level release or qualification claims

They answer:

- does the composed product satisfy the claimed requirement or scenario?

Under this method, only sandbox tests or an explicitly equivalent isolated
composed-product proof lane may be called UAT / acceptance tests.

A sandbox test must exercise the deployed, installed, or otherwise runnable
product form through declared application, public, runtime, or control surfaces.
It must be driven by a requirement-sourced scenario or acceptance case. Direct
source-level unit tests, helper tests, and module integration tests may be
valuable proof, but they are not UAT and cannot close user acceptance by
themselves.

Sandbox UAT has two lawful execution modes:

- **Harnessed sandbox UAT**: exercises the full composed product path with a
  deterministic, fake, recorded, or injected worker/result surface.
- **Live sandbox UAT**: exercises the full composed product path with a real
  configured worker, tool, agent, service, or other external probabilistic
  transport where the product depends on that live boundary.

Harnessed sandbox UAT proves composition, orchestration, control, projection,
archive, and scenario wiring without relying on live probabilistic execution.
It is the right lane for deterministic reproducibility.

Live sandbox UAT proves that the same scenario can cross the real external
probabilistic boundary and return evidence through the declared result,
evaluation, provenance, and projection surfaces. Where a product or release
claim depends on live probabilistic compute, semantic green, unit green, module
integration green, and harnessed sandbox green are necessary but not sufficient
for live acceptance.

Terminology rules:

- `unit` names module/design conformance scope, not user acceptance.
- `integration` names execution breadth, not authority source.
- `sandbox` names composed-product acceptance execution.
- `harnessed`, `fake`, `recorded`, or `deterministic` name non-live sandbox
  execution.
- `live` is reserved for real external worker or transport execution. A status
  projection named "live" is not live UAT unless it crosses that real boundary.

If a project uses different local filenames or runner labels, the local test
surface must still map each executable lane back to this taxonomy before
claiming closure.
```

Successor, `ASSURANCE.md#2-testing-strategy-taxonomy`:

```text
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
declares (the design profile's irreducible architectural carrier set,
[DESIGN_MODULE §6](DESIGN_MODULE.md#irreducible-architectural-carrier-set),
or an equivalent), structural carrier diagrams where present, and boundary-local
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
```


### Row `SPEC_METHOD.md#transformation-wave-rule` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#transformation-wave-rule` at rc.2:

```text
Refactor and migration should be understood as a transformation wave over
mutable implementation surfaces.

While the wave is in flight:

- temporary mixed-state implementation may exist only below the current break
  boundary and only as explicitly non-authoritative plumbing
- transitional adapters or scaffolds may exist only when they are named,
  bounded, and outside the acceptance path
- refactor state may still carry traces of the prior operative model, but never
  as competing or ambiguous dual authority over the same request, fact,
  identity, state, or projection

Explicitly specified, deterministically routed, non-overlapping Product or
compatibility scopes are not competing authority under this rule. They may
coexist while the enclosing migration remains visibly open.

When the wave lands across its declared affected scope:

- only the new current operative surface remains live for that scope
- prior operative paths for that scope are erased from the live product
- the path taken to get there survives only in version control, event history, and superseded records
- mixed old/new operative models are not a stable end state

The only lawful exception is an explicit compatibility feature.

If compatibility is retained, it must be:

- named as current product behavior
- justified in the specification
- bounded in scope
- tested as an intentional feature

Otherwise the correct action is deletion, not passive preservation.

---
```

Successor, `SPEC_METHOD.md#transformation-wave`:

```text
Refactor and migration should be understood as a transformation wave over
mutable
implementation surfaces (P3, P6; rc.2 #transformation-wave-rule). While
the wave is in flight: temporary mixed-state implementation may exist only
below the current break boundary and only as explicitly non-authoritative
plumbing; transitional adapters or scaffolds may exist only when they are
named, bounded and outside the acceptance path; refactor state may still
carry traces of the prior operative model, never as competing or ambiguous
dual authority over the same request, fact, identity, state or projection.
Explicitly specified, deterministically routed, non-overlapping product or
compatibility scopes are not competing authority under this rule; they may
coexist while the enclosing migration remains visibly open.

When the wave lands across its declared affected scope: only the new
current operative surface remains live for that scope; prior operative
paths for that scope are erased from the live product; the path taken to
get there survives only in version control, event history and superseded
records; mixed old and new operative models are not a stable end state. The
only lawful exception is an explicit compatibility feature, which is named
as current product behaviour, justified in the specification, bounded in
scope and tested as an intentional feature. Otherwise the correct action is
deletion, not passive preservation.
```


### Row `SPEC_METHOD.md#transition-evidence-and-proof-cadence` (modal; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#transition-evidence-and-proof-cadence` at rc.2:

```text
A reviewable transition identifies the exact candidate, affected relations,
changed realization paths, authority paths added or removed, retained and open
seams, focused proof, any required integration proof, explicit non-changes, and
the assessor disposition. Consumers choose the representation. Transition
evidence is a read model and does not become specification, design, or
admission authority.

Construction uses the cheapest focused proof capable of falsifying the active
relation. Expensive whole-candidate qualification occurs at a declared
candidate boundary rather than after every local edit, unless the affected
risk makes whole-candidate proof necessary.

A durable or reconstructable authority claim is not established solely by a
same-process proof when loss of incidental process state is a material
counterexample. Proof must destroy or exclude the incidental authority and
compare reconstructed semantic outcomes.
```

Successor, `ACTIVATION.md#transition-evidence`:

```text
A reviewable transition identifies the exact candidate, the affected
relations, the changed realisation paths, the authority paths added or
removed, the retained and open seams, the focused proof, any required
integration proof, the explicit non-changes, and the decision owner's
disposition or the assessor's recommended disposition (§3). Consumers
choose the representation. Transition evidence is a read
model; it does not become specification, design or admission authority
(P6, P4b; provenance rc.2 SPEC_METHOD
#transition-evidence-and-proof-cadence).

Construction uses the cheapest focused proof capable of falsifying the
active relation. Expensive whole-candidate qualification occurs at a
declared candidate boundary rather than after every local edit, unless the
affected risk makes whole-candidate proof necessary (§6). A durable or
reconstructable authority claim is not established solely by a same-process
proof when loss of incidental process state is a material counterexample:
the proof destroys or excludes the incidental authority and compares the
reconstructed semantic outcomes (P5, P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#2-executive-activates-worker` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#2-executive-activates-worker` at rc.2:

```text
In the coordinated branch, Executive applies `REFERENCE_FRAME_METHOD.md`
activation to the `STDO-UP-020` sufficient execution intake. The activation identifies:

- selected complete STDO and project authority;
- exact governed outcome and checkpoint;
- affected causal relation set and governing invariants;
- selected computational relations and specialist frames;
- testing claims, exact subjects, frame topology, material combination
  populations, ordinary paths, oracles, and forbidden-path exclusions where
  testing evidence is required;
- Worker authority, capability envelope, and the exact inherited operation
  grant, subject, and write territory where mutation is authorized;
- evidence and qualification obligations;
- exclusions, prohibited competing paths, stop conditions, and re-entry
  conditions; and
- the exact bounded action already authorized.

If activation detects a known capability, authority, subject, basis, or
topology mismatch, it returns `activation_refusal` directly to Executive. No
Worker frame is active, no Worker evaluation occurs, and Executive must not
manufacture a Worker result to represent the failed activation.
```

Successor, `EXECUTIVE_BASELINE.md#2-executive-activates-worker`:

```text
In the coordinated branch the Executive applies `activate` (REFERENCE_FRAME
§5) to the sufficient execution intake of ACTIVATION §1. The packet is
REFERENCE_FRAME §11; for this step it identifies (P0, P6; rc.2
#2-executive-activates-worker):

- the selected complete method and project authority;
- the exact governed outcome and checkpoint;
- the affected causal relation set and the governing invariants;
- the selected computational relations and specialist frames;
- where testing evidence is required: the testing claims, exact subjects,
  frame topology, material combination populations, ordinary paths,
  oracles and forbidden-path exclusions (ASSURANCE §7 to §9);
- the Worker's authority and capability envelope, and, where mutation is
  authorised, the exact inherited operation grant, subject and write
  territory;
- the evidence and qualification obligations;
- exclusions, prohibited competing paths, stop conditions and re-entry
  conditions; and
- the exact bounded action already authorised.

If activation detects a known capability, authority, subject, basis or
topology mismatch, it returns `activation_refusal` directly to the
Executive, with the cause and core value REFERENCE_FRAME §5 gives it. No
Worker frame is active, no Worker evaluation occurs, and the
Executive does not manufacture a Worker result to represent the failed
activation (P5, P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#closure` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#closure` at rc.2:

```text
Evaluate only the obligations applicable to the exact selected outcome and
engagement branch. A listed frame or available testing family does not make
its claim applicable. Every applicable obligation must be satisfied with valid
evidence and required J/O, with no active non-closure condition under
`TICKET_METHOD.md#condition-based-closure-and-reuse`. A closed indeterminate
result or a review event does not satisfy an unresolved obligation.

A project has applied this baseline to one outcome when:

1. existing project authority admits and projects the exact frame basis;
2. the complete selected STDO and Reference Frame Method remain the governing
   sources;
3. Executive, Worker, and Reviewer are available finite evaluation frames,
   activated only where applicable, not hierarchy or actor identities;
4. activation refusal remains distinct from Worker results, and every Worker
   result maps exclusively from one closed Reference Frame Method result and
   returns to its declared consumer, first to Executive in the coordinated
   branch;
5. existing work authority determines whether an exact candidate requires
   independent review; the coordinated Executive activates Reviewer where
   required, while the sufficient direct branch adds no such activation;
6. required Reviewer assessment binds the exact subject, evidence population,
   verdict, evidence-bound technical triage, and independence conditions;
7. an activated Executive consumes closed results and technical triage against
   the complete Product view and current MVP or release mandate, keeps severity, priority,
   frame result, and boundary effect distinct, and applies only the existing
   `STDO-UP-020` disposition and continuation relation;
8. specialist frames and result relations cover every known material
   evaluation and interaction or retain an explicit residual;
9. frame, basis, capability, evidence, and topology change can invalidate and
   rechart the configuration;
10. every material operation carries its existing owner's exact grant;
11. no new execution authority, local constitutional layer, actor topology,
    runtime, or universal completeness claim is inferred from the profile;
12. every material Product testing claim is assigned to an exact
    user-acceptance, end-to-end, integration, unit, or explicitly declared
    alternative frame rather than inferred from a suite label;
13. a user-outcome claim binds the declared user capability, exact Product
    subject, supported ordinary surface, environment, and observable outcome;
14. an end-to-end claim binds the exact deployed, installed, or otherwise
    runnable Product form and records the required authoritative causal path
    rather than accepting output equality through an unknown or forbidden path;
15. material interface and Product factors have a declared combinatorial
    population, adequate interaction strength, exercised scenario matrix, and
    explicit residual combinations;
16. unit-test evidence proves module-owned laws, including public module
    contracts, and its volume and strategy are proportional to useful
    discrimination of the module-bounded population rather than implementation
    size;
17. required paths have positive runnable-Product witnesses; the production
    closure excludes obsolete, rival, fallback, and bypass paths; and the
    assurance/source closure cannot falsely supply evidence or reintroduce a
    removed production path, while declared isolated test-only seams remain
    outside ordinary-path claims;
18. source or code coverage, test count, and aggregate green status do not
    substitute for Product, installed, path, composition, or user-frame proof;
19. test fixtures, mutations, sabotage, proof capture, and assurance tooling
    preserve or revalidate the exact subject they claim to evaluate;
20. owner-issued Product and runtime truth is acquired through the exact owner
    surface and evaluated by a separately derived oracle without a rival
    assurance-owned semantic interpreter;
21. counterexamples return a causally minimal supported frontier represented as
    one unique locus, a jointly established incomparable set, unresolved
    alternative frontiers, or `indeterminate` evidence;
22. every Product, Product Composition, Design, Design Component, Public
    Boundary, Entity, Operator, Owner, Effect, Reuse/Foundation, Install, and
    Proof family material to the outcome has an exact declaration or
    acquisition path, while every non-material or uncovered family has an
    authority-bound disposition;
23. every material cross-frame seam preserves or lawfully translates identity,
    coordinate and basis, carried value or evidence, lifecycle scope,
    authority, and provenance; and
24. no consumer-specific architecture, renamed local topology, runtime object,
    or component roster is inferred from the generic specialist set.

A project-defined frame configuration closes against
`REFERENCE_FRAME_METHOD.md`, the selected complete STDO cut, and its cited
existing project authorities. It need not claim conformance to this optional
baseline profile.
```

Successor, `EXECUTIVE_BASELINE.md#22-closure`:

```text
Only the obligations applicable to the exact selected outcome and
engagement branch are evaluated. A listed frame or an available testing
family does not make its claim applicable (ACTIVATION §1, Applicability).
The closure condition is
[TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse),
which this profile applies to the selected branch and does not restate: a
work item closes by that condition, not by a reviewer's approval
([EVALUATION §5](EVALUATION.md#5-acceptance)). Applied here, a closed
`indeterminate` result or a review event does not satisfy an unresolved
obligation, because `indeterminate` never maps to `satisfied`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) and a review's
occurrence is not the closing event (P5, P6; rc.2 #closure).

A project has applied this baseline to one outcome when (P6, P2):

1. existing project authority admits and projects the exact frame basis;
2. the complete selected method, REFERENCE_FRAME included, stays the
   governing source;
3. Executive, Worker and Reviewer are available finite evaluation frames,
   activated only where applicable, not a hierarchy or actor identities;
4. activation refusal stays distinct from Worker results, and every Worker
   result is one work-result value selected by its cause, maps to exactly
   one core value as ACTIVATION §3 states, and returns to its declared
   consumer, first to the Executive in the coordinated branch;
5. existing work authority decides whether an exact candidate requires
   independent review; the coordinated Executive activates the Reviewer
   where required, and the sufficient direct branch adds no such
   activation;
6. required Reviewer assessment binds the exact subject, evidence
   population, verdict, evidence-bound technical triage and independence
   conditions;
7. an activated Executive consumes closed results and technical triage
   against the complete Product view and the current MVP or release
   mandate, keeps severity, priority, frame result and boundary effect
   distinct, and applies only the existing disposition and continuation
   relation;
8. specialist frames and result relations cover every known material
   evaluation and interaction or keep an explicit residual;
9. frame, basis, capability, evidence and topology change can invalidate
   and rechart the configuration;
10. every material operation carries its existing owner's exact grant;
11. no new execution authority, local constitutional layer, actor topology,
    runtime or universal completeness claim is inferred from the profile;
12. every material Product testing claim is assigned to an exact
    user-acceptance, end-to-end, integration, unit or explicitly declared
    alternative frame rather than inferred from a suite label;
13. a user-outcome claim binds the declared user capability, the exact
    Product subject, the supported ordinary surface, the environment and
    the observable outcome;
14. an end-to-end claim binds the exact deployed, installed or otherwise
    runnable Product form and records the required authoritative causal
    path, rather than accepting equal output through an unknown or
    forbidden path;
15. material interface and Product factors have a declared combinatorial
    population, adequate interaction strength, an exercised scenario matrix
    and explicit residual combinations;
16. unit evidence proves module-owned laws, public module contracts
    included, with volume and strategy proportional to useful
    discrimination of the module-bounded population rather than to
    implementation size;
17. required paths have positive runnable-Product witnesses; the
    production closure excludes obsolete, rival, fallback and bypass paths;
    the assurance/source closure cannot falsely supply evidence or
    reintroduce a removed production path; and declared isolated test-only
    seams stay outside ordinary-path claims;
18. source or code coverage, test count and aggregate green status do not
    stand in for Product, installed, path, composition or user-frame proof;
19. test fixtures, mutations, sabotage, proof capture and assurance tooling
    preserve or revalidate the exact subject they claim to evaluate;
20. owner-issued Product and runtime truth is acquired through the exact
    owner surface and evaluated by a separately derived oracle, without a
    rival assurance-owned semantic interpreter;
21. counterexamples return a causally minimal supported frontier
    represented as one unique locus, a jointly established incomparable
    set, unresolved alternative frontiers, or `indeterminate`;
22. every one of the twelve families material to the outcome has an exact
    declaration or acquisition path, and every non-material or uncovered
    family has an authority-bound disposition;
23. every material cross-frame seam preserves or lawfully translates
    identity, coordinate and basis, carried value or evidence, lifecycle
    scope, authority and provenance; and
24. no consumer-specific architecture, renamed local topology, runtime
    object or component roster is inferred from the generic set.

A project-defined frame configuration closes against REFERENCE_FRAME, the
selected complete method cut and its cited existing project authorities. It
need not claim conformance to this optional profile (P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#combinatorial-coverage-and-testing-value-index` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#combinatorial-coverage-and-testing-value-index` at rc.2:

```text
Testing value is indexed first by the material combinations a frame can
discriminate for its exact claim. It is not indexed by test, assertion, file,
line, branch, mock, snapshot, or runner count.

For one claim, the testing-value index considers at least:

1. congruence between the claim and evaluated subject;
2. the number and materiality of independent claim dimensions;
3. the interaction strength actually covered among those dimensions;
4. authoritative-path exactness;
5. oracle independence and precision;
6. sensitivity to realistic faults, rival paths, and historical failures;
7. observability, reconstruction, and reproducibility of the result; and
8. explicit residual combinations and invalidation conditions.

No universal scalar is required. A project may define one only through Product,
requirement, or accepted-design authority and must retain the underlying
coverage coordinates rather than flattening them into a score.

At unit altitude, the relevant dimensions are module-bounded. Unit-testing
value normally rises with the internal combinatorial complexity of an algebra,
calculation, state machine, transition relation, or other module-owned closed
domain because local tests can cheaply discriminate many meaningful
combinations against a precise oracle.

At integration, end-to-end, and user-acceptance altitude, testing value can be
multiplicative rather than additive: each material interface composes
preconditions, postconditions, authority, state, configuration, failure, and
recovery with every other traversed boundary. The evidence value comes from
the interactions actually discriminated, not from merely touching many
interfaces on one sunny path.

Material Product factors commonly include:

- user role and capability;
- supported operation and Product composition;
- selected definition, owner, implementation, and dependency;
- lifecycle and persisted state;
- configuration and version combination;
- process, continuation, retry, re-entry, and recovery mode;
- success, refusal, malformed result, partial failure, and competing-path case;
- fresh-process, replay, reconstruction, and migration condition; and
- user-visible outcome and projection.

The activated frame declares the finite interaction population and why its
covering set is adequate. Pairwise or other covering-array reduction is lawful
only where the basis explains why omitted higher-order interactions cannot
change the claim or retains them as residuals. High-consequence authority,
persistence, concurrency, recovery, migration, and historically failure-prone
relations normally require explicit higher-strength combinations.

Source, line, branch, and function coverage may diagnose whether code was
visited. They do not establish semantic combination coverage, authoritative
path selection, user-outcome coverage, or the absence of a rival path.
```

Successor, `ASSURANCE.md#8-combinatorial-coverage-and-testing-value`:

```text
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
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#define-a-project-configuration` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#define-a-project-configuration` at rc.2:

```text
A project may define different frames, names, overlaps, sequences, and actor
bindings. The defining Product, requirement, Goals, or accepted-design
authority records:

- exact method and project basis;
- known evaluation inventory;
- each frame declaration and capability envelope;
- semantic, evaluation, operation where material, and decision authority;
- intentional overlap, separately activated evaluations, and required
  assurance independence;
- conjunction, translation, and composition actually used;
- mapping to applicable STDO construction, assessment, disposition, identity,
  and release obligations;
- coverage and residual uncertainty; and
- re-entry, invalidation, and revision conditions.

The project configuration need not preserve the labels Executive, Worker, and
Reviewer or map one local frame to each label. It must preserve every applicable
STDO relation and identify how its evaluations cover the claims it makes.

A local axioms document may carry this accepted configuration. Its authority is
the cited Goals, Product, requirement, or accepted-design decision, not the
document category.
```

Successor, `EXECUTIVE_BASELINE.md#define-a-project-configuration`:

```text
A project may define different frames, names, overlaps, sequences and actor
bindings. The defining Product, requirement, Goals or accepted-design
authority records (P6, P2; rc.2 #define-a-project-configuration;
REFERENCE_FRAME §4):

- the exact method and project basis;
- the known evaluation inventory;
- each frame declaration and capability envelope;
- semantic, evaluation, operation where material, and decision authority;
- intentional overlap, separately activated evaluations and required
  assurance independence;
- the conjunction, translation and composition actually used;
- the explanation of the allocation, with its material resource limits and
  failure assumptions, that ACTIVATION §1 Configuration requires of every
  configuration;
- the mapping to the applicable construction, assessment, disposition,
  identity and release obligations;
- coverage and residual uncertainty; and
- re-entry, invalidation and revision conditions.

A project configuration need not keep the labels Executive, Worker and
Reviewer or map one local frame to each. It keeps every applicable method
relation and identifies how its evaluations cover the claims it makes. It
is evaluated against its task, its dependencies, its actors' limits, the
authority it applies and the required assurance, as ACTIVATION §1
Configuration states, never by its labels, its topology or its difference
from this profile. A local axioms document may carry the accepted
configuration; its authority is the cited Goals, Product, requirement or
accepted-design decision, not the document's category (P6, P1).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` at rc.2:

```text
Executive is the profile frame for three inseparable duties over one governed
outcome:

1. **attention management** maintains the exact outcome and basis, Product-role
   map, evaluation inventory, dependency relation, unresolved frontier, actor
   envelopes, current MVP or release mandate, applicable triage policy, and
   residual boundary, then selects the smallest
   dependency-ready activation set sufficient for the next decision within the
   finite actor envelopes;
2. **evaluation orchestration** activates capable Workers, Reviewers, or
   specialists, preserves their exact subjects and bases, and consumes only
   closed results or declared translations; and
3. **authorized action selection** assigns priority, determines the effect on
   the current promotion boundary, applies an existing disposition, and issues
   only the next already-authorized activation or action.

Executive does not contain the complete workspace, perform every evaluation,
or acquire Product meaning, implementation, mutation, acceptance, publication,
or other operation authority from the role. A material effect remains owned by
the actor carrying its exact operation grant.

An actor occupying Executive must not modify candidate, Product or worktree
bytes or perform an implementation effect. Filesystem or tool access and an
edit being small, test-only, reversible or apparently obvious supply no
exception. Mutation requires a separately activated Worker or Writer relation
with the exact operation grant, subject and write territory. A same-actor role
transition is explicit and recorded in the existing work carrier before the
effect; the actor is no longer acting as Executive for that effect. Recording
or delegating after an Executive edit cannot authorize it retroactively.

The attention cycle is:

```text
U0 = every known material evaluation not closed on the current basis

while U is non-empty:
  select a finite dependency-ready subset M that fits the assigned actors
  activate each member of M against the exact outcome and basis
  keep assurance-independent evaluations free of unclosed peer results
  when no other authorized decision is ready:
    await decision-relevant input under Event-Driven Executive Attention
  record every closed result, technical triage, residual, and invalidation condition
  apply only declared conjunctions or translations
  assign priority and boundary effect only under the current Product mandate
  invalidate affected results when the subject or basis changes
  update U from coverage, dependencies, conflicts, and discovered materiality

stop only when every mandatory evaluation is closed, or governing authority
has explicitly retained every remaining residual consistently with the claim
```

This relation requires no scheduler or frame engine. `M` may contain parallel
activations. Recursion follows declared evaluation dependencies and bounded
refinements; it does not nest or join undifferentiated copies of every frame.
The Executive retains the frontier and closed-result ledger in attention, not
the undocumented working context of every evaluator.

Severity supplied by Reviewer is evaluation evidence. Priority, current-boundary
effect, `STDO-UP-020` disposition, and subsequent action are Executive decisions.
They remain distinct ledger entries even when a Product-defined policy maps one
to another.

Every result returns to Executive, a declared conjunction, or another frame
through an explicit `D` relation. No lateral handoff, child completion, model
response, tool output, or shared actor implicitly activates another frame or
authorizes continuation. A consumer receives the closed result and its source
routes, not the child's hidden reasoning context.
```

Successor, `EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action`:

```text

```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#generic-specialist-frame-family` (modal; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#generic-specialist-frame-family` at rc.2:

```text
A **generic specialist-frame family** is a reusable evaluation-family
archetype in this profile. It identifies a recurring distinction that a
project must either instantiate it where material, have capable authority
establish it as non-material for the governed outcome, or retain it as an
explicit coverage residual.

The family does not select a concrete carrier, component, actor, architecture,
owner, or implementation. One project may instantiate several frames in one
family. One declared frame may cover several families only when its evaluation
and result relations preserve every material distinction rather than flattening
them behind one broad label.
```

Successor, `EXECUTIVE_BASELINE.md#generic-specialist-frame-family`:

```text
A generic specialist-frame family is a reusable evaluation-family archetype
of this profile (§11). It names a recurring distinction that a project
either instantiates where material, has capable authority establish as
non-material for the governed outcome, or keeps as an explicit coverage
residual (P2, P6; rc.2 #generic-specialist-frame-family).

A family selects no concrete carrier, component, actor, architecture, owner
or implementation. One project may instantiate several frames in one
family. One declared frame may cover several families only when its
evaluation and result relations preserve every material distinction instead
of flattening them behind one broad label (P1, RF-008).
```


### Row `TICKET_METHOD.md#authority` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#authority` at rc.2:

```text
- `ticketing.goals` locates the epic layer
- `ticketing.sprints.root`, when present, is the bounded execution-batch and
  sprint-close review layer
- `ticketing.tickets.lanes.backlog`, `.active`, and `.completed` locate the
  ticket authority
- `ticketing.comments.root` locates the discussion and publication layer

The paths shown in the default layout are the bindings supplied by
`stdo_default.json`. The definition locates these carriers but does not own
their ticket or comment content.

There is no separate mandatory `ACTIVE_TASKS.md` in this model.

If a project later wants a board view, it may generate one from the bound
ticket authority. That board is a projection only and must not become the
source of truth unless the Product Definition Overlay explicitly rebinds the
ticket authority to that carrier and no rival remains.

---
```

Successor, `TICKETS.md#bindings-and-projections`:

```text
The bindings (P6, P3; rc.2 #authority): `ticketing.goals` locates the epic
layer; `ticketing.sprints.root`, when present, is the bounded
execution-batch and sprint-close review layer;
`ticketing.tickets.lanes.backlog`, `.active` and `.completed` locate the
ticket authority; `ticketing.comments.root` locates the discussion and
publication layer. The paths of the default layout are the bindings
supplied by `stdo_default.json`. The definition locates these carriers and
does not own their ticket or comment content.

There is no separate mandatory `ACTIVE_TASKS.md` in this model. A project
that wants a board view may generate one from the bound ticket authority;
that board is a projection only and does not become the source of truth
unless the product definition explicitly rebinds the ticket authority to
that carrier and no rival remains (§7).
```


### Row `TICKET_METHOD.md#change-class` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#change-class` at rc.2:

```text
Ticket type and change class are orthogonal.

- ticket type answers: what kind of work record is this?
- change class answers: where does this change lawfully re-enter the
  constitutional chain?

Tickets must record the `change_class` declared by intake triage, using the
change classes from `SPEC_METHOD.md`.

Common pairings are:

- `feature` with `goal_reprice`, `intent_reprice`, `product_reprice`,
  `requirement_reprice`, or `design_reframe`
- `bug` with `requirement_reprice`, `design_reframe`, or
  `realization_refactor`
- `chore` with `design_reframe` or `realization_refactor`
- `spike` as exploratory work that still carries the current triage class and
  should terminate either in a more specific downstream ticket or in an
  explicit decision that no further substantive change is required

Ticket category and change class are also orthogonal.

- `change_class` governs lawful constitutional re-entry
- `ticket_category` governs ticket execution and closure discipline

So a ticket may be:

- `type: bug`
- `ticket_category: implementation_migration`
- `change_class: design_reframe`

without contradiction.
```

Successor, `TICKETS.md#change-class`:

```text
Ticket type and change class are orthogonal: type answers what kind of
work record this is; change class answers where the change lawfully
re-enters the constitutional chain. A ticket records the `change_class`
declared by intake triage, using the classes of
[SPEC_METHOD §4](SPEC_METHOD.md#change-classes) (P4b, P2; rc.2
#change-class).

Common pairings: `feature` with `goal_reprice`, `intent_reprice`,
`product_reprice`, `requirement_reprice` or `design_reframe`; `bug` with
`requirement_reprice`, `design_reframe` or `realization_refactor`; `chore`
with `design_reframe` or `realization_refactor`; `spike` as exploratory
work that still carries the current triage class and should terminate
either in a more specific downstream ticket or in an explicit decision
that no further substantive change is required.

Ticket category and change class are also orthogonal: `change_class`
governs lawful constitutional re-entry; `ticket_category` governs ticket
execution and closure discipline. A ticket may therefore be `type: bug`,
`ticket_category: implementation_migration`, `change_class: design_reframe`
without contradiction (P3).
```


### Row `TICKET_METHOD.md#execution-contract-admission` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#execution-contract-admission` at rc.2:

```text
The runtime execution flow should treat the ticket, sprint entry, or drafted
work contract as an admission candidate, not as automatic truth.

Minimum expected states are:

- `drafted`
- `admitted`
- `rejected`
- `superseded`

An admitted execution contract should be:

- logged in runtime/event truth
- available to prompt assembly
- available to later closure checking

The system must not allow the model to silently self-certify its own execution
basis without deterministic admission or explicit human override.

Execution-contract admission validates a proposed contract against its cited
Product outcome, prerequisite, or experiment basis; it does not admit that
growth basis. Admission or renewal of the basis belongs to the authority owning
the selected Goals work wave, or its explicitly bounded proxy, and remains
durably legible in existing Goals or ticket authority. Drafting, admitting, or
retaining an active execution contract cannot create or renew authority that
the owning work-wave authority has not admitted.
```

Successor, `TICKETS.md#execution-contract-admission`:

```text
The runtime execution flow should treat a ticket, a sprint entry or a
drafted work contract as an admission candidate, never as automatic truth;
the contract carries at minimum the states named in ACTIVATION §1
(drafted, admitted, rejected, superseded). An admitted execution contract
should be logged in runtime and event truth, available to prompt assembly,
and available to later closure checking, so that execution and closure
read the same admitted basis (P6,
P4b; rc.2 #execution-contract-admission). The refusal of self-certification
is ACTIVATION §1.

Admission validates a contract against its cited product outcome,
prerequisite or experiment basis and does not admit that basis (ACTIVATION
§1). Admission or renewal of the basis belongs to the authority owning the
selected goals work wave, or its explicitly bounded proxy, and stays
durably legible in the existing goals or ticket authority
([SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation)). A ticket's
`active` status, its lane, or an admitted or retained contract is therefore
never the admission of a growth basis (P6, P2).
```

Successor, `ACTIVATION.md#admission`:

```text
Drafting a step's contract and admitting it are distinct relations, even
inside one invocation that drafts, validates, admits and executes; no
separate turn, carrier or approval ceremony is implied by the distinction.
A contract carries at minimum the states drafted, admitted, rejected and
superseded ([TICKETS §5](TICKETS.md#execution-contract-admission)).
Execution begins only after deterministic admission or an
explicit human override of the exact contract. The drafting actor never
infers admission from its own draft, from the presence of a carrier
(ticket, sprint entry, work contract), from lane placement or from an
`active` label. The admitted result identifies the admission mechanism and
its authority, the exact contract identity or digest, the decision and the
evidence, including any human override; absent those coordinates the
contract stays drafted or rejected, and prose asserting admission is not
admission evidence (P6; the actor cannot self-certify its own execution
basis). Admission validates the contract against its cited outcome,
prerequisite or experiment basis; it does not admit that basis, and
drafting, admitting or retaining a contract creates or renews no authority
its owner has not admitted (P6, P2;
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). Only an admitted contract activates a step: no
result, child completion, tool output, model response, shared actor or
lateral handoff activates another step or authorises continuation by
itself, and a profile that routes results names its instances of this
rule. Purpose and material relation: a profile and a template each stated
this list for one configuration, so the generic rule had no owner (P6).
The admitted contract names one
durable result and evidence surface; every result, withheld closure and
residual obligation is recorded there before return, a conversation return
alone is not durable evidence, and if no such surface is authorised and
available, admission refuses (P4b). Absent or rejected admission returns
the missing work authority without execution, as `admission_refused` with
its cause ([§3 Admission and activation](#admission-and-activation)).
Provenance:
[work-carrier-to-execution rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)
and
[execution contract admission](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-contract-admission);
the selection of the carrier (ticket, sprint entry, run-scoped contract)
is tier-2 law in the [TICKETS](TICKETS.md) member, which disposes those rows.
```

Successor, `SPEC_METHOD.md#3-outcome-conservation`:

```text
Every product-outcome-bearing work wave identifies one explicitly selected,
unresolved, directly verifiable product-defined outcome and declares the
acceptance interval for that instance. Product-progress claims and
promotion onto the supported product path are judged against that same
outcome (P2; rc.2 #product-outcome-conservation-stdo-up-013; FOUNDATIONS §2
Outcome U is the generic object).

Evidence distinguishes material advance, prerequisite readiness,
preservation and regression. The four refine the progress
categories of [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)
(Progress) for a product outcome: material advance is progress there,
accepted material movement toward the selected product outcome, and only
material advance projects product progress; prerequisite readiness is
its prerequisite work, which names the product obligation it enables and
here also remains bounded; preservation is its preservation and repeated
proof, useful evidence, not progress; regression maps to evidence that
is not new progress, and this member adds one need to it: the promotion
block in the last paragraph of this section. Churn and the revision of the forecast are
ACTIVATION §5's, unchanged here.

The exact bound outcome instance stops selecting later product-progress
work when the owning authority accepts it; its witnesses remain regression
and preservation evidence. Acceptance exhausts only that instance and its
declared acceptance interval; it does not discharge an enduring guarantee,
a recurring obligation or a broader product family beyond the accepted
instance. Further work against the accepted instance is preservation, a
named bounded prerequisite for another admitted outcome, or a new change
requiring lawful repricing; it is not additional progress against the
accepted instance (EVALUATION §5).

Selecting the next unresolved outcome already defined by the product is a
goals and work-sequencing decision. Changing an outcome's meaning or scope,
or introducing a new product outcome, requires lawful re-entry at the
product (§4).

Evidence evaluates and constrains its bound product claim. Completion of a
proof surface, matrix, coverage ledger, inventory, design-method artifact,
test suite or other evidence surface cannot by itself select, enlarge or
replace the product outcome. If an assurance capability is explicitly
defined as product behaviour, delivery of that capability is judged as
product progress; its evidence still does not author the claim. The same
artifact may be product output for one claim and evidence for another only
when those roles are declared separately (P6).

Within a product-outcome-bearing work wave, material realisation growth
derives its authority from the selected unresolved product outcome, an
admitted named bounded prerequisite to it, or an admitted named bounded
experiment whose stated observation discriminates a stated decision for it.
A prerequisite or experiment authorises only its declared provisional
bound; it does not select or enlarge the product outcome, authorise
downstream work, confer promotion or closure, or waive applicable design,
safety, authority or release law, including the prime law of a design
profile where one applies.

Admission or renewal of a prerequisite or experiment belongs to the
authority owning the selected work wave, or its explicitly bounded proxy,
and is recorded in the existing durable goals or ticket authority. The
admitted basis states its provisional bound and its exhaustion or
falsification condition. Satisfaction of an experiment's stated
decision-discriminating observation exhausts that experiment. Drafting or
validating a ticket or execution contract, retaining active status, or
holding a prior admission cannot create, extend or renew the basis
(ACTIVATION §1, Admission).

Acceptance of the selected outcome, discharge of an admitted prerequisite,
or resolution of an admitted experiment's stated decision exhausts that
basis. A basis or bound also ends when another admitted terminal condition
is reached or it is rejected, withdrawn, superseded, repriced away or
falsified by evidence. Ended authority cannot be renewed by repair,
continuation, evidence, active ticket or run state, or prior admission;
further material work requires a new admission by the owning authority or
its explicitly bounded proxy (P6).

Retention as supported product behaviour, required evidence, regression
protection or bounded donor material confers no further growth authority.
Consumers own deletion, archival, quarantine and salvage mechanics. Salvage
carries only the explicitly re-adopted semantics; it inherits neither the
enclosing work's authority, dependencies or completion claim nor its power
to select further work.

A regression or unresolved gap blocks further promotion on the affected
path until repaired, repriced or accepted by the owning authority. It does
not globally serialise independent work: parallel work may proceed under
its own admitted basis and cannot be laundered into the governed outcome's
progress claim. Outcome success is necessary delivery evidence, not
complete product or release closure (§6).
```


### Row `TICKET_METHOD.md#future-extensions` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#future-extensions` at rc.2:

```text
This minimal method can later grow into:

- a generated active board
- ticket dependency checks
- links from tickets to scenario, requirement, or ADR surfaces
- external sync with a real ticketing system
- message-board integration through a standard tool-protocol capability

The durable local-file model remains the default and must remain valid when
selected. Another carrier is not required to reproduce its folders, but it must
preserve the same ticket authority and refusal laws.
```

Successor, `TICKETS.md#carrier-substitution`:

```text
The durable local-file model is the default and remains valid whenever it
is selected. Another carrier is not required to reproduce its folders, but
it preserves the same ticket authority and refusal laws (§3 and §4, one
durable record). Growth the model admits includes a generated active board,
ticket dependency checks, links from tickets to scenario, requirement or
ADR surfaces, external sync with a real ticketing system, and message-board
integration through a standard tool-protocol capability. Under the bindings
above, a generated board is a projection, and a tracker that holds tickets
is lawful only as an explicit rebinding of the ticket authority by the
product definition with no rival surface remaining, so neither growth
changes the authority or refusal laws (P2, P6; rc.2 #future-extensions).
```
