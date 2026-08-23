# Release Method

## Release-Publication Context

`RELEASE_METHOD.md` owns the release-publication bounded context
`urn:stdo:bounded-context:release-publication` under the selected complete STDO
basis. It owns the identities and transitions used to qualify, publish, and
select released cuts. It does not own Product meaning or consumer adoption.

## Position

Release process is distinct from live project specification.

Live specification defines the current constitutional truth of the project.
Release process defines how one published point-in-time cut is evaluated,
bounded, named, published, and made discoverable.

The exact operative release identity is always an immutable RC cut tag:

```text
v<version>-rc.<n>
```

The unqualified version tag:

```text
v<version>
```

is a mutable **Version-Line Selector**. It points to the latest published
immutable RC cut on that line, where latest means the greatest positive RC
ordinal present in the release source. It is convenient discovery, not
immutable identity and not sufficient as an exact constitutional, dependency,
evidence, or replay basis.

Release handling is downstream of intake triage. A bug, feature, regression,
or release blocker first receives its change class, lawful re-entry point,
affected scope, downstream proof obligations, and version-line disposition.
The existence of an RC window does not authorize untriaged mutation.

## Release Identities

The release-publication context distinguishes:

- **Candidate Source** — mutable source-project state constructing a possible
  successor;
- **RC Branch** — a mutable carrier such as `rc/<version>` for the current
  candidate window;
- **Immutable RC Cut** — an annotated `v<version>-rc.<n>` tag naming one exact
  published candidate and, once accepted, one released Product;
- **Version-Line Selector** — the mutable `v<version>` tag alias naming the
  highest-ordinal published immutable RC cut on that version line; and
- **Release Branch** — an optional mutable convenience carrier such as
  `release/<version>` aligned to the same latest-published commit as the
  selector.

Equal version text does not collapse these identities. Branches and the
version-line selector may move. An immutable RC tag never moves.

## Phases

The release process has three phases:

1. mutable candidate construction;
2. immutable RC publication and monotonic version-line advancement; and
3. exact-cut qualification, acceptance, and explicit consumer adoption.

There is no second final cut after an accepted RC. Publication immediately
makes the new highest ordinal discoverable through the version-line selector;
acceptance remains a verdict over the exact immutable RC rather than a second
carrier. If any byte capable of affecting the Product or a release-scoped claim
changes, the project publishes and reviews a higher immutable RC cut instead.

## Mutable Candidate Construction

During candidate construction:

- bounded fixes are allowed after intake triage;
- qualification and operator review may continue;
- release notes may remain draft until RC publication;
- the RC branch may move; and
- mutable source is explicitly non-operative for released consumers.

The intended Product boundary, release-scoped claims, excluded source-project
state, and qualification basis become explicit before RC publication. A
material scope change is repriced instead of being silently absorbed.

## Immutable RC Publication

A published RC cut exists to provide one exact subject for review, replay, and
possible acceptance. To publish it, the project:

1. confirms the triaged scope and lawful constitutional re-entry;
2. declares the exact Product release subject and release-scoped claim set;
3. reconciles the release note and other release-facing assets to that subject;
4. runs the proportionate pre-RC qualification and operator checks;
5. commits the exact carrier;
6. creates one annotated immutable `v<version>-rc.<n>` tag and an annotated
   `v<version>` selector tag over that same commit;
7. atomically pushes the carrier, RC branch, immutable RC tag, selector, and
   optional release branch where the transport supports it;
8. verifies remotely that the immutable tag, selector, and release branch
   resolve to the highest published RC commit; and
9. records enough identity and inventory evidence to reacquire the cut without
   trusting a mutable checkout.

Each published RC tag is immutable. Further work increments `<n>` on the same
version line when the intended line remains applicable. It does not require a
minor-version increment merely because review found a bounded repair. A
published higher RC without matching selector advancement is an invalid,
fail-closed release state; it never authorizes resolution of the older cut as
the version-line latest.

## Exact-Cut Qualification

Qualification binds:

- the immutable RC tag object, peeled commit, repository tree, and declared
  Product member set;
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

## Monotonic Version-Line Advancement

Version-line advancement makes the newly published highest RC discoverable:

1. identify the exact new immutable RC tag, ordinal, and peeled commit;
2. confirm that no higher RC ordinal already exists on that line;
3. confirm `v<version>` is absent or currently resolves to a lower RC ordinal
   on the same line;
4. atomically create or force-update the annotated `v<version>` selector to the
   new highest RC commit;
5. create or update `release/<version>` to the same commit when that optional
   carrier is used;
6. push the carrier, RC branch, immutable RC tag, selector, and optional release
   branch atomically where the transport supports it; and
7. verify remotely that the selector peels to the highest RC commit and that
   the matching immutable annotated RC tag exists.

Advancement is refused when the target has no matching immutable annotated RC
tag, any higher ordinal already exists, the selector would move to a lower RC,
or the selector and release branch would not align to the same highest commit.

Forward movement is strictly monotonic by RC ordinal. A later defect is
repaired through a higher immutable RC, not by moving an old RC tag or rolling
the selector backward. The selector is therefore equivalent to
`v<version>-rc.latest`, while every concrete RC tag remains addressable.

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

Channel resolution enumerates the published RC tags, selects the greatest
positive ordinal, requires that cut and the version-line selector to be
annotated tags peeling to the same commit, and fails closed when the selector
lags or points elsewhere. Channel adoption also refuses a same-line target
whose ordinal is below the Product Definition's current exact basis. A consumer
that intentionally retains an older cut names that immutable RC URI and digest
explicitly and uses exact-basis operations such as `sync`; it does not express
that choice through the latest-version channel.

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

## Naming

The default naming shape is:

- RC branch: `rc/<version>`;
- immutable RC tag: `v<version>-rc.<n>`;
- optional release branch: `release/<version>`; and
- mutable version-line selector tag: `v<version>`.

For example:

- candidate branch: `rc/2.4.3`;
- first immutable cut: `v2.4.3-rc.1`;
- second immutable cut: `v2.4.3-rc.2`;
- latest-release branch: `release/2.4.3`; and
- latest-published selector: `v2.4.3`.

Projects may choose another spelling only when they preserve the same mutable
carrier, immutable cut, and mutable selector distinctions.

## Release-Scoped Assets

An immutable RC cut may carry release-scoped surfaces such as:

- release notes;
- release and installed-distribution manifests;
- dependency declarations;
- package or installed-carrier metadata;
- qualification receipts; and
- branch and tag identity declarations.

Before RC publication, each used surface is reconciled to the exact RC subject.
After publication, changing one of those bytes creates a different candidate
and therefore requires a higher RC tag. The version-line selector has no
content-reconciliation phase because it adds no new Product bytes.

Version-line branding does not belong in live present-tense Product or
requirements surfaces merely to signal recency. Exact version and RC identity
belong in release-scoped carriers and consumer basis bindings.

## Product Subject And Repository Carrier

Before qualification, the project declares:

- the exact Product member set or artifact constituting the release subject;
- the release-scoped claim surfaces describing that subject; and
- co-located mutable source-project fields excluded from both.

A repository commit carries those declared sets but does not make every
co-located file a Product member. Once the immutable RC is published, no
post-review carrier delta is admitted into that cut. Publication-caused ticket
or source-work bookkeeping is recorded afterward on the continuing source
branch and cannot move the immutable RC tag.

## Acceptance Criteria

An RC may be accepted when:

- pre-RC qualification passed for the declared subject;
- independent exact-cut review passed where required;
- required operator review is complete;
- the intended release scope and successor relation are stable;
- release-scoped assets accurately describe the exact cut;
- all release-blocking gaps are closed or the claimed scope is explicitly
  narrowed; and
- the human Product authority accepted the exact immutable RC identity.

Acceptance attaches to that immutable RC identity. It neither advances nor
rolls back the version-line selector. Consumer adoption separately evaluates
the exact latest target presented by the channel and mutates only after its
digest-bound plan is accepted.

## External Qualification Dependencies

Some claims depend on external backends, transports, or operator-facing
services outside the local carrier. Such a dependency may remain out of Product
for carrier and migration classification while still blocking the dependent
release claim.

A clean skip caused by an unhealthy external dependency may preserve correct
Product classification, but it cannot establish that the dependent capability
passed. The claim is either qualified against a healthy dependency or narrowed
before acceptance.

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

## Open Questions

- What exact qualification bundle is mandatory for each Product class?
- What version-line compatibility rule requires a new `<version>` rather than a
  higher RC ordinal?
