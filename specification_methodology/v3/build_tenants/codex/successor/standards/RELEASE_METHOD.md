# Release Method

This member owns release-specific identity, qualification, publication and
selection contracts. Given stable identity, fallible observation and bounded
authority, an acceptance claim requires one reacquirable subject and evidence
for its declared predicates. Exact-Cut Qualification and Acceptance Criteria
apply those consequences through the shared
[result algebra](FOUNDATIONS.md#result-algebra) and
[conjunction](FOUNDATIONS.md#result-conjunction). The immutable-cut policy,
Git ref profile and monotonic selector rule are additional release choices.
They are not inferred from finite capacity or successful construction.

The [transformation library](TRANSFORMATION_LIBRARY.md) supplies Evaluate,
Conjoin and Dispose responsibilities. Candidate preservation, acceptance,
publication and consumer adoption remain distinct decisions. Its version/ref
examples illustrate the declared release identities; each actual cut requires
its own authorised exact binding.
Result bindings below preserve core legal performance pairs, diagnostic
precedence, absent coverage and actual effects. They describe the existing
checks and decisions without adding an evaluation stage or evidence carrier.

## Release-Publication Context

`RELEASE_METHOD.md` owns the release-publication bounded context
`urn:stdo:bounded-context:release-publication` under the selected complete STDO
basis. It owns the identities and transitions used to qualify, publish, and
select released cuts, including the selector/adoption protocol below. It does
not own the consumer's Product meaning or its decision to adopt a cut; those
remain with the consumer's governing authority under Spec's Product binding.

## Position

Release process is distinct from live project specification.

Live specification defines the current constitutional truth of the project.
Release process defines how one published point-in-time cut is evaluated,
bounded, named, published, and made discoverable.

The product-local cut name is always:

```text
v<version>-rc.<n>
```

In a release source carrying one independently released project, that name may
also be the Git tag name. In a shared release source it is the suffix of the
project-qualified Git ref defined below. Equal product-local cut names do not
collapse releases owned by different projects.

The product-local version-line selector name is:

```text
v<version>
```

It denotes a mutable **Version-Line Selector**. The selector points to the
latest published immutable RC cut on that line, where latest means the greatest
positive RC ordinal published for that project and version line. It is
convenient discovery, not immutable identity and not sufficient as an exact
constitutional, dependency, evidence, or replay basis.

Release handling is downstream of intake triage. A bug, feature, regression,
or release blocker first receives its change class, lawful re-entry point,
affected scope, downstream proof obligations, and version-line disposition.
The existence of an RC window does not authorize untriaged mutation.

## Release Identities

This identity/publication family assumes [F2–F4 and F6](FOUNDATIONS.md#foundational-commitments)
with separately governed Products and observable release carriers. A claim
then needs its exact subject, compatible member/ref relations and actual grant
under [Contract application](TRANSFORMATION_LIBRARY.md#contract-application).
This member chooses immutable annotated cuts, qualified namespaces, subtree
identity, historical conservation and monotonic selectors. Product release
authorities assign namespaces and subjects; co-location cannot choose them.

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

## Project-Qualified Git Refs

`<project>` is one explicit Project Release Namespace. It matches
`[a-z0-9]+(?:[-_][a-z0-9]+)*`, contains no slash, is unique within the release
source, and remains stable for the continuing release line. It is assigned by
the Product release authority. A directory name, display name, definition
label, package name, or matching version cannot infer or reassign it.

A shared release source uses these exact ref shapes for every future
publication:

```text
RC branch:              refs/heads/rc/<project>/<version>
immutable RC cut tag:   refs/tags/<project>/v<version>-rc.<n>
version-line selector:  refs/tags/<project>/v<version>
release branch:         refs/heads/release/<project>/<version>
```

The short Git tag names are therefore `<project>/v<version>-rc.<n>` and
`<project>/v<version>`. A shared release source must not publish a future cut or
selector under the unqualified `v<version>-rc.<n>` or `v<version>` refs.

A single-project release source may retain the unqualified ref profile only
while it has exactly one independently released project and its release record
declares that profile. Adding a second independently released project requires
project-qualified refs before either project publishes another cut.

For the Specification Stack shared source, the allocated namespaces are
`specification_methodology`, `axiom_indexer`, and `stdo_representation`. These
keys distinguish release refs; they do not merge the three Products or imply a
dependency or composition relation.

## Project-Subtree Release Identity

In a shared release source, an immutable cut binds all of:

- the Project Release Namespace and owning Product authority;
- the exact qualified Git ref and annotated tag object;
- the peeled commit and repository-root tree;
- the normalized repository-relative Project Subtree root at that commit;
- the Git tree object at that exact Project Subtree root;
- the declared Product member inventory and release-scoped claim bytes; and
- the predecessor and successor dispositions required by this method.

The Project Subtree root is a locator inside the exact peeled commit, not
Product identity. Its canonical spelling is the slash-separated Git path from
the repository root, with no leading or trailing slash and no empty, `.`, or
`..` component; `.` alone denotes the repository root. Each non-root component
must name the exact tree entry bytes traversed at that commit. Moving a source
project changes this locator and its cut identity without reassigning the
Project Release Namespace. If the source project occupies the repository root,
its project-subtree tree equals the repository-root tree.

A tag over a monorepo commit does not make sibling subtrees Product members.
Unrelated sibling bytes remain carrier state outside the declared Product
subject. Conversely, a member inventory or payload digest without the
qualified ref, commit, Project Subtree root, and Project Subtree tree is not a
complete reacquirable release identity.

## Historical Ref And Public-URI Conservation

Project qualification is prospective. Existing unqualified refs retain their
names, objects, peels, and public links. A historical tag object may remain
reachable through an additional archival ref, but it is not recreated,
re-annotated, moved, or replaced. An immutable historical tag remains the same
object regardless of which preserving ref reaches it.

Product-local cut names and public logical release URIs also remain unchanged.
In particular, a logical STDO release remains
`stdo://releases/v<version>-rc.<n>/`; the project-qualified Git ref is transport
identity and is not inserted into that URI. Resolution binds the public logical
cut to its exact historical or project-qualified Git ref and fails closed if
one project-local coordinate names different tag objects.

When one version line spans the transition, latest means the greatest positive
RC ordinal across that project's preserved historical cuts and its qualified
future cuts. The first qualified publication creates the qualified selector.
The historical unqualified selector is preserved at its existing object and
ceases to be the current selector for the shared source; it is not force-moved
to imitate the qualified namespace.

## Phases

The release process has three phases:

1. mutable candidate construction;
2. immutable RC publication and monotonic version-line advancement; and
3. exact-cut qualification, acceptance, and explicit consumer adoption.

There is no second final cut after an accepted RC. Publication immediately
makes the new highest ordinal discoverable through the version-line selector;
acceptance remains a decision over the exact immutable RC rather than a second
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

Publication applies [Contract application](TRANSFORMATION_LIBRARY.md#contract-application)
to the granted remote operation, and evaluates `the declared cut and required
public ref relation exist at the selected remote` from that remote's state.
Its Currentness and Result conditions govern transport failure after dispatch:
local command success or failure cannot decide the remote effect. After
observation, complete or repair only the still-authorised missing relation;
never move an immutable published cut.

The publication, advancement, selector-resolution and cohort gates below each
bind their stated conditions as their exact predicate. `Refused`, `fails closed`
and `stops` preserve the domain reason: a demonstrated missing/incorrect ref,
nonmonotonic target, stale accepted plan, defeated lease or unsupported required
atomic transport falsifies that gate's admissibility predicate; unavailable
remote or deciding evidence leaves it `indeterminate`. An uninterpretable
governing subject/basis gives `invalid_basis`; evaluation outside its declared
scope/capability gives `out_of_frame`; established fulfillment of all conditions
gives `satisfied`. Missing reasons cannot justify satisfaction. A gate result
does not establish actual publication/adoption, and a refused call does not
prove `not_started` after possible dispatch. Preserve the core performance,
coverage and observed-effect coordinates at each selected boundary.

## Exact-Cut Qualification

Given F1–F4 and F6, evidence for a narrower or different subject cannot establish
this cut's claim, and a satisfied assessment cannot make an owner decision.
The shared [result/conjunction contract](FOUNDATIONS.md#result-conjunction)
supplies those consequences. Release policy separately chooses exact-cut review,
required operator checks and human acceptance; the Product declares its claim
set, external dependencies and any lawful narrowing. Supported alternative
realizations use those same claim conditions, not an assumed preferred build.

Qualification binds:

- the Project Release Namespace, qualified immutable RC ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree, and
  declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, assessment results, owner decisions and unresolved gaps; and
- the complete successor relation to the declared predecessor.

Evidence matches the claim. Source success does not prove packaged or installed
behavior; packaging equivalence does not prove semantic behavior; artifact
presence does not prove usability unless presence is the exact claim.

Each qualification item applies
[Contract application](TRANSFORMATION_LIBRARY.md#contract-application) to reliance
on its witness under the exact cut, claimed property and observation boundary
above. Evaluate that property using the shared Result condition, preserving the
item's original outcome and finer diagnostic. The release's declared required
claim set supplies the conjunction; its core result, performance and coverage
determine standing rather than a passed label or cached release summary.

For the item's claimed property, `passed` maps to `satisfied` only with
established performance and every required coverage/evidence condition on the
exact cut. `Failed` with admissible counterevidence is `falsified`; `skipped`,
`cached green` or any other raw label without deciding support is
`indeterminate`. Retain an established `invalid_basis` or `out_of_frame`
diagnosis and separately authenticated counterevidence under the core legal
pairs. Missing reasons, absent judgments, performance and effect observations
apply the [core result and conjunction law](FOUNDATIONS.md#result-conjunction);
the release labels supply no alternative rule for them.

An RC is accepted only when the required exact-cut review and operator checks
are complete and the human authority accepts that exact subject. If review
requires any qualifying-byte change, the review result remains attached to the old
RC and a higher RC is published. The selector already advertises the highest
published RC; acceptance does not move it, rewrite it, or create another final
carrier.

## Monotonic Version-Line Advancement

Version-line advancement makes the newly published highest RC for one Project
Release Namespace discoverable:

1. identify the exact new immutable RC tag, ordinal, and peeled commit;
2. confirm that no higher RC ordinal already exists on that line;
3. confirm the project-qualified selector is absent or currently resolves to a
   lower RC ordinal on the same project line;
4. atomically create or force-update the annotated
   `<project>/v<version>` selector to the new highest RC commit;
5. create or update `release/<project>/<version>` to the same commit when that
   optional carrier is used;
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

F2, F3 and F6 imply that discovery of current publication is neither an exact
consumer basis nor permission to change one. This family chooses separate
presentation and mutation, digest-bound plans and same-line downgrade refusal.
The actual consumer authority accepts the selected plan; supported retention of
an older immutable cut remains lawful through the exact-basis route below.

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

## Naming

The shared-source naming shape is:

- RC branch: `rc/<project>/<version>`;
- immutable RC tag: `<project>/v<version>-rc.<n>`;
- optional release branch: `release/<project>/<version>`; and
- mutable version-line selector tag: `<project>/v<version>`.

For example:

- candidate branch: `rc/stdo_representation/2.5.0`;
- first immutable cut: `stdo_representation/v2.5.0-rc.1`;
- second immutable cut: `stdo_representation/v2.5.0-rc.2`;
- latest-release branch: `release/stdo_representation/2.5.0`; and
- latest-published selector: `stdo_representation/v2.5.0`.

The unqualified profile remains lawful only under the single-project and
historical-conservation conditions above. Projects may choose another spelling
only in a release source whose ref policy proves collision freedom and preserves
the same project namespace, mutable carrier, immutable cut, and mutable selector
distinctions.

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

## Coordinated Release-Matched Asset Cohorts

Given F3, F4 and F6 and an explicitly declared cross-Product cohort, local member
success cannot establish the material joins of the cohort or merge its owners.
[Contract application](TRANSFORMATION_LIBRARY.md#contract-application) and core
conjunction supply that consequence. This family additionally chooses exact
version matching, the two-commit construction, atomic publication and ref leases.
The declaring authorities select the cohort; separately authorized recovery
owns any historical-backfill exception. Those policies are not universal
atomicity requirements for unrelated operations.

A Product authority may declare an explicit cross-Product **Release-Matched
Asset Cohort** when one source corpus and its required distributed or derived
assets must remain usable as one versioned set. The declaring relation names
every required Product and asset, the exact source dependency, its owning
authorities, the qualification boundary, and the publication transaction. Path
co-location, equal version text, or a common actor cannot infer the relation.

Every required member of one cohort uses one exact cohort version suffix
`<version>-rc.<n>`. Product-local cut names and refs render it as
`v<version>-rc.<n>`; embedded asset-version fields render the same suffix
without `v`. Qualification normalizes only that leading cut-name marker and
requires exact suffix equality. Equal versions establish release matching
only. They do not collapse Product identities, member inventories, tags,
acceptance judgments, or release authorities.

For a release-matched STDO stack, the closed cohort contains all of:

1. the exact STDO standards corpus cut;
2. the distributed `spec` plugin and host assets carried by that STDO cut;
3. the exact Axiom Indexer mechanics Product used to validate and project the
   index;
4. the exact STDO Representation Product; and
5. its released `a_c.STDO` axiomatic program and logical constraint map or
   equivalent semantic index, with the complete source-STDO member inventory,
   member digests, member-set digest, and exact cut identity used to derive it.

The cohort is incomplete when a required member is missing, stale, differently
versioned, built from another source cut, or unable to reproduce its declared
source-member and digest closure. A change to any source member covered by the
index invalidates the old derived candidate for the successor cohort. The
index is regenerated, mechanically validated, independently qualified where
required, and released under the same new cut name. A stale index may remain
immutable history; it cannot accompany the changed source as the current
cohort.

`Complete`/`incomplete` describes the declared cohort relation. Evaluation of
`every required cohort member and release/source relation holds` is `satisfied`
only with established complete coverage; an observed missing or incongruent
required member is `falsified`, and unobserved or unavailable closure evidence
is `indeterminate`, retaining core basis/scope diagnoses. An unknown required
set cannot become a proved empty cohort. This assessment and the later
remote-publication observation remain different predicates.

### Two-Commit Construction And One Publication Transaction

Exact installed-manifest identity includes the annotated STDO tag object, so a
same-commit carrier containing both that identity and derived child bytes would
be self-referential. A coordinated STDO cohort therefore uses this bounded
two-commit construction:

1. commit A freezes the exact STDO corpus, plugin, release record, and their
   qualification bytes;
2. the annotated STDO cut tag is created locally over commit A but is not
   pushed;
3. that exact local cut is installed and verified, producing the manifest
   identity used by every derived Product and index;
4. the Axiom Indexer, STDO Representation, semantic-index bytes, and cohort
   record are derived and frozen in commit B;
5. prepublication qualification evaluates commit B against the exact local
   STDO tag before child immutable tags are created;
6. annotated child cut tags and every Product-local RC branch, version-line
   selector, and optional release branch are prepared locally; and
7. a mandatory post-tag, pre-push gate re-runs qualification over every local
   annotated tag object and peel, selector, RC and release branch, normalized
   version mapping, target commit, and the exact closed ref set; it also fetches
   and binds the expected remote object ID or required absence for every
   destination ref; and
8. one transport transaction atomically publishes only that qualified carrier
   branch and
   complete Product ref set.

If the remote does not support atomic ref publication, publication refuses.
The process has no sequential-push fallback. Every immutable cut tag is
create-only and therefore requires bound remote absence. Every mutable carrier,
RC branch, selector, and release branch uses an explicit per-ref
compare-and-swap lease, such as `--force-with-lease=<ref>:<expected-oid>`, in
that same atomic transaction. A missing expected ref, unexpected existing tag,
or changed remote object ID stops publication; the operator refetches and
repeats complete content and local-ref-graph qualification before constructing
another push. A lease mismatch never falls back to an unguarded force, a
partial push, or an in-place expectation update.

Remote verification fails closed when any required cohort ref is absent,
lightweight, differently versioned, points to the wrong Product commit, or has
a selector or release branch that does not match its immutable cut.
Post-publication bookkeeping may use a later commit, but it cannot move any
immutable cohort tag.

### Qualification And Recovery

Prepublication content qualification binds the exact commit-A STDO tag and
manifest, commit-B source tree, all Product-local target refs, version markers,
Product member inventories, semantic-index bytes, and complete source-corpus
digest closure. It proves that the frozen candidate can be tagged without
changing a qualifying byte. After tag and mutable ref creation, local-ref-graph
qualification binds their annotated objects, peels, target commits, exact push
set, and every fetched remote expected object ID or required absence to that
unchanged content result. Post-publication qualification
verifies the same relation from remote refs and refuses a partial cohort.

On resumption, apply Contract application's Currentness condition to the exact
local and remote ref relations above and their frozen-subject evidence. The
complete remote relation, not a prior assumption of atomicity, determines the
publication effect. Remaining effects require the existing authorised recovery
relation; reacquiring context supplies no repository or remote-ref reset grant.

A historically published source cut may be the basis of a later same-version
backfill only when separately authorized recovery law names that exception.
Every recovered asset still binds the exact historical cut and same cut name,
and remote completeness remains mandatory. Recovery cannot move the historical
tag, add bytes to its Product subject, or be represented as an atomic cohort
that existed at the original publication. Normal successor publication uses
the atomic cohort process above.

Adding or changing this cohort law changes qualifying Release Method bytes. It
governs only a higher immutable RC that contains those bytes and cannot
retroactively make an earlier cut a coordinated cohort.

## Product Subject And Repository Carrier

Before qualification, the project declares:

- its Project Release Namespace and exact Project Subtree root;
- the exact Product member set or artifact constituting the release subject;
- the release-scoped claim surfaces describing that subject; and
- co-located mutable source-project fields excluded from both.

A repository commit carries those declared sets but does not make every
co-located file or sibling Project Subtree a Product member. The exact
Project Subtree tree and Product member inventory distinguish the subject from
the wider carrier. Once the immutable RC is published, no post-review carrier
delta is admitted into that cut. Publication-caused ticket or source-work
bookkeeping is recorded afterward on the continuing source branch and cannot
move the immutable RC tag.

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

Apply Contract application to reliance on qualification evidence and the actual
owner decision required above. Qualification, `the authorised owner accepted
this exact cut` and consumer adoption are three distinct predicates; their core
results retain their respective evidence, authority and actual performance.

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

This family assumes F1–F4 and F6 and a successor whose claims derive from an
identified predecessor. Naming, code similarity or patch absence cannot then
establish semantic preservation, and evidence cannot authorize removal. The
shared [preservation contract](TRANSFORMATION_LIBRARY.md#contract-application)
supplies those constraints. UP-015 chooses complete predecessor disposition and
watched-support-line policy. Product authority owns removal and acceptance of
changed meaning; the consumer chooses its comparison and durable record.

A successor identifies the exact predecessor immutable RC whose semantic claims
it evolves. That origin remains immutable for the candidate. Every predecessor
claim capable of affecting the successor receives one semantic disposition:

- **conserved** — the successor retains the claim;
- **superseded** — an accepted successor relation replaces it;
- **intentionally removed** — current Product authority removes it; or
- **not applicable** — it has no successor effect, with a bounded reason.

These are row dispositions, not interchangeable verdicts on retention. Bind
each semantic assessment to the predicate for its exact predecessor claim and
successor relation:

| Row disposition | Semantic predicate assessed | Required decision relation |
|---|---|---|
| `conserved` | the successor retains this predecessor claim's meaning | recording the conservation disposition under the bound mandate |
| `superseded` | the named successor relation replaces this predecessor claim | actual acceptance of that successor relation by its governing authority, plus the bound disposition |
| `intentionally removed` | this predecessor claim is excluded from the successor's governing claim set | actual removal by current Product authority; omission alone supplies no decision |
| `not applicable` | this predecessor claim has no effect on the declared successor scope | supported applicability determination and the bound disposition; scope cannot be silently narrowed |

On each named semantic predicate, established fulfillment maps to `satisfied`,
an admissible counterexample to `falsified`, and insufficient evidence or a
missing reason to `indeterminate`. An uninterpretable subject/governing basis
is `invalid_basis`; assessment outside scope/capability is `out_of_frame`.
Preserve the original row and cause, actual performance and absent coverage
under the [core result contract](FOUNDATIONS.md#result-algebra). Satisfaction
of removal or non-applicability is not a claim that predecessor meaning was
retained. Retention and replacement may be shown by any supported realization,
not only a familiar structure or byte-identical implementation.

For a row's claimed authorized disposition, the separate decision predicate is
`this disposition D on the exact claim and basis was made under its bound
mandate`. A supported lawful decision is
`satisfied`; a demonstrated absent/unauthorized decision is `falsified`;
unconfirmed authority, reason or decision is `indeterminate`, retaining core
basis/scope diagnoses. The table's required acceptance or removal decision is
an actual additional obligation where named, not a decision manufactured by
recording a row. Neither predicate overwrites the other, any known semantic
failure, or observed and uncertain effects.

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
