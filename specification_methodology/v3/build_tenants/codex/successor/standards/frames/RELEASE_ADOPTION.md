# Release and Adoption Frame

Scope: Assess immutable publication, exact-cut qualification, successor dispositions and consumer adoption as distinct claims. This frame supplies no publishing or adoption grant.

Bind this scope to the exact subject, selected governing basis, actor, capability
envelope, required coverage and existing grant before use. Any missing material
relation remains unresolved. The excerpts below are derived acquisition views of
the named owners; those owners retain authority. Section text is retained, with
relative links relocated to the same targets. A source digest binds the entire
owner, not proof that this selection suffices for another task.











Source: [RELEASE_METHOD.md — Release Identities](../RELEASE_METHOD.md#release-identities); SHA256 `26f48744f6344f11237f78ddc8a7012f0d85abf20043fcf1a8b84942bfb19373`.

## Release Identities

The release-publication context distinguishes:

- **Project Release Namespace** — a stable repository-local key assigned by the
  Product release authority to one independently released source project;
- **Project Subtree** — the exact repository-relative source-project root and
  Git tree object selected for one cut;
- **Candidate Source** — mutable source-project state constructing a possible
  successor;
- **RC Branch** — a mutable project-qualified carrier for the current candidate
  window;
- **Immutable RC Cut** — an annotated project-qualified Git tag plus its exact
  Product release subject, naming one published candidate and, once accepted,
  one released Product;
- **Version-Line Selector** — the mutable project-qualified tag alias naming
  the highest-ordinal published immutable RC cut for that project and version
  line; and
- **Release Branch** — an optional mutable project-qualified convenience
  carrier aligned to the same latest-published commit as the selector.

Equal version text does not collapse these identities. Branches and the
version-line selector may move. An immutable RC tag never moves.


Source: [RELEASE_METHOD.md — Immutable RC Publication](../RELEASE_METHOD.md#immutable-rc-publication); SHA256 `26f48744f6344f11237f78ddc8a7012f0d85abf20043fcf1a8b84942bfb19373`.

## Immutable RC Publication

A published RC cut exists to provide one exact subject for review, replay, and
possible acceptance. To publish it, the project:

1. confirms the triaged scope and lawful constitutional re-entry;
2. declares the exact Product release subject and release-scoped claim set;
3. reconciles the release note and other release-facing assets to that subject;
4. runs the proportionate pre-RC qualification and operator checks;
5. commits the exact carrier;
6. resolves and records the exact Project Release Namespace, Project Subtree
   root, and Project Subtree tree;
7. creates one annotated immutable `<project>/v<version>-rc.<n>` tag and an
   annotated `<project>/v<version>` selector tag over that same commit in a
   shared release source;
8. atomically pushes the carrier, RC branch, immutable RC tag, selector, and
   optional release branch where the transport supports it;
9. verifies remotely that the immutable tag, selector, and release branch
   resolve to the highest published RC commit; and
10. records enough ref, subtree, identity, and inventory evidence to reacquire
    the cut without trusting a mutable checkout.

Each published RC tag is immutable. Further work increments `<n>` on the same
version line when the intended line remains applicable. It does not require a
minor-version increment merely because review found a bounded repair. A
published higher RC without matching selector advancement is an invalid,
fail-closed release state; it never authorizes resolution of the older cut as
the version-line latest.


Source: [RELEASE_METHOD.md — Exact-Cut Qualification](../RELEASE_METHOD.md#exact-cut-qualification); SHA256 `26f48744f6344f11237f78ddc8a7012f0d85abf20043fcf1a8b84942bfb19373`.

## Exact-Cut Qualification

Qualification binds:

- the Project Release Namespace, qualified immutable RC ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree, and
  declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, owner verdicts, and unresolved gaps; and
- the complete successor relation to the declared predecessor.

Evidence matches the claim. Source success does not prove packaged or installed
behavior; packaging equivalence does not prove semantic behavior; artifact
presence does not prove usability unless presence is the exact claim.

An RC is accepted only when the required exact-cut review and operator checks
are complete and the human authority accepts that exact subject. If review
requires any qualifying-byte change, the verdict remains attached to the old
RC and a higher RC is published. The selector already advertises the highest
published RC; acceptance does not move it, rewrite it, or create another final
carrier.


Source: [RELEASE_METHOD.md — Selector And Consumer Adoption](../RELEASE_METHOD.md#selector-and-consumer-adoption); SHA256 `26f48744f6344f11237f78ddc8a7012f0d85abf20043fcf1a8b84942bfb19373`.

## Selector And Consumer Adoption

The version-line selector answers only:

> Which highest-ordinal published immutable RC cut currently exists on this
> version line?

It never answers:

> Which exact STDO cut governs this consumer?

A Product Definition may retain `stdo://channels/<version>` as its discovery
selector, but its operative basis is the exact
`stdo://releases/v<version>-rc.<n>/` URI and installed-manifest digest. Moving
the Git version-line selector does not update any consumer. Adoption is a
separate explicit Product-Definition transition that resolves, presents,
installs, verifies, and pins the selected immutable RC. Resolution requires an
annotated selector with a distinct peeled commit; absence of a peeled selector
ref fails closed and cannot be interpreted as a lightweight selector whose tag
object is its commit.

Channel resolution enumerates the published RC tags for the selected Project
Release Namespace, including preserved unqualified historical cuts during a
namespace transition, selects the greatest positive ordinal, requires that cut
and the current selector to be annotated tags peeling to the same commit, and
fails closed when the selector lags or points elsewhere. Channel adoption also
refuses a same-line target whose ordinal is below the Product Definition's
current exact basis. A consumer that intentionally retains an older cut names
that immutable RC URI and digest explicitly and uses exact-basis operations
such as `sync`; it does not express that choice through the latest-version
channel.

Presentation and mutation are separate invocations. The read-only plan binds
the current Product Definition bytes and basis to the target immutable cut,
annotated tag object, peeled commit, tree, and installed-manifest digest, then
emits a deterministic plan digest. Mutation requires that exact digest as the
operator's acceptance and re-derives it before changing any Product Definition.
Selector, target, manifest, or definition drift invalidates the acceptance. A
fleet uses the same law with one aggregate digest over all exact per-definition
plans; planning inside a mutating invocation is not external presentation and
cannot authorize itself.

This split lets operators refer to `v<version>` for the latest published RC
without repeatedly incrementing the version line, while every governed project
retains reproducible exact-cut authority and changes only through explicit
adoption.


Source: [RELEASE_METHOD.md — Successor Baseline Conservation (`STDO-UP-015`)](../RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015); SHA256 `26f48744f6344f11237f78ddc8a7012f0d85abf20043fcf1a8b84942bfb19373`.

## Successor Baseline Conservation (`STDO-UP-015`)

A successor identifies the exact predecessor immutable RC whose semantic claims
it evolves. That origin remains immutable for the candidate. Every predecessor
claim capable of affecting the successor receives one semantic disposition:

- **conserved** — the successor retains the claim;
- **superseded** — an accepted successor relation replaces it;
- **intentionally removed** — current Product authority removes it; or
- **not applicable** — it has no successor effect, with a bounded reason.

An unresolved disposition blocks qualification of the affected claim.
Conservation is semantic: patch absence does not prove loss when a
successor-native realization preserves behavior, and naming or code similarity
does not prove conservation without relevant evidence.

Where a maintenance or support line may affect retained claims, the release
basis identifies the watched source, observation boundary, inclusion policy,
and successor candidate. Relevant changes receive semantic disposition at
material integration and exact-cut qualification. The consumer owns its record,
branch strategy, comparison, and proof mechanism.


Source: [SPEC_METHOD.md — Explicit Complete Consumer Update](../SPEC_METHOD.md#explicit-complete-consumer-update); SHA256 `5b088f10f0c3ecac1a87bcd0b4c566a20a9a76a06fda80742e9267b96250b3a1`.

#### Explicit Complete Consumer Update

A **Complete Consumer Update Plan** binds one explicitly selected Product
Definition and the complete companion population of one exact upstream
release-matched cohort to the consumer bindings selected by the invocation's
owner. The Product Definition continues to own composition; the upstream
cohort and each Product's release record own release and member identity.
An invocation selection and its derived plan/result are operation evidence,
not another persistent dependency declaration, registry or lock. The caller
must select every native route and derived context for the claimed update
scope; directory proximity or an empty discovery result cannot supply that
selection. An empty derived-context population means the owner selected none,
not that the manager established the absence of semantic context.

The separate `cohort-update` operation presents the whole plan without consumer
effects. Unlike the basis-only Adoption Plan above, its acceptance object also
binds physical effect destinations and binding preimages, exact selected
cohort bytes, companion annotated tags/commits/subtrees and inventories,
replacement dependency locators, native routes, and declared derived-source
observations. It uses the same canonical JSON hashing rule. Already-installed
status supplies no additional authority and does not change the digest.
Mutation requires explicit acceptance of this exact plan and rederives it;
possession of its digest alone grants no operation authority. Existing
`adopt`, `sync` and fleet contracts retain their narrower boundaries.

The complete operation verifies the selected cohort's dependency closure and
each exact companion's definition, release record and admitted members before
reliance. It stages absent immutable installs, verifies existing installs
without repairing them in place, and preflights every consumer target. Only
the selected basis/schema, existing composition locators/contracts and selected
native/install links may change. Historical installs and unrelated consumer
content remain available and unchanged. It creates no consumer-local checker
and changes no Product meaning or local semantic map.

For each selected derived context, missing, ambiguous, changed or unavailable
program/map/source evidence holds the complete update before consumer effects.
Its source owner must perform any necessary semantic re-entry; the manager
cannot mechanically relabel an older map as current. Exact source freshness is
integrity evidence, not semantic conformance or an independent semantic verdict.
After immutable staging the manager rechecks the consumer preimages and source
evidence. It reports completion only after verifying every selected resulting
binding and companion. Refusal before consumer effects retains prior state;
a caught application failure restores the affected consumer preimages and
does not report completion. Newly staged immutable installs may remain unused.
The operation requires an exclusive consumer write scope during application.
It does not claim a crash-atomic transaction across independent filesystem
paths: abrupt process/host loss or unavailable rollback storage requires
recovery from the presented preimages before claiming the complete relation.


Source: [REFERENCE_FRAME_METHOD.md — RF-005 Exact Basis And Coordinates](../REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates); SHA256 `44bb25eacd05550240d31ef318dc2c23db2b8a147ba1b8daa342f688d343e488`.

### RF-005 Exact Basis And Coordinates

Every result binds its exact subject, basis, coordinates, and evidence scope.
A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or
requires reactivation. Apparent equality does not substitute for declared
coordinate equality.


Source: [REFERENCE_FRAME_METHOD.md — RF-006 Authority Conservation](../REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation); SHA256 `44bb25eacd05550240d31ef318dc2c23db2b8a147ba1b8daa342f688d343e488`.

### RF-006 Authority Conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer, or reconstruct semantic, evaluation, operation, or decision authority
from actor identity, available capability, evidence shape, implementation
reachability, or frame selection.


Source: [REFERENCE_FRAME_METHOD.md — RF-012 Closed Results](../REFERENCE_FRAME_METHOD.md#rf-012-closed-results); SHA256 `44bb25eacd05550240d31ef318dc2c23db2b8a147ba1b8daa342f688d343e488`.

### RF-012 Closed Results

Every evaluation returns a member of its declared result algebra. The baseline
result family is:

- `satisfied`: the declared predicate holds on the exact basis;
- `falsified`: a declared counterexample defeats it;
- `indeterminate`: available admissible evidence cannot decide it;
- `out_of_frame`: the evaluation requires an undeclared material relation or
  capability; or
- `invalid_basis`: the subject or basis cannot support the evaluation.

An externally owned compatible extension may refine this algebra while
preserving explicit indeterminate, out-of-frame, and invalid-basis pressure.
