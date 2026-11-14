## 2. Release identities

The release-publication context distinguishes (P3):

- Project Release Namespace: a stable repository-local key assigned by
  the Product release authority to one independently released source
  project;
- Project Subtree: the exact repository-relative source-project root and
  Git tree object selected for one cut;
- Candidate Source: the candidate source of FOUNDATIONS §2, the mutable
  source-project state constructing a possible successor;
- RC Branch: a mutable project-qualified carrier for the current
  candidate window;
- Immutable Release Cut: an annotated project-qualified Git tag plus its
  exact Product release subject (FOUNDATIONS §2), under the selected RC or
  stable profile; publication, qualification and acceptance retain their
  respective meanings; it realises the release cut;
- Version-Line Selector: the mutable project-qualified tag alias naming
  the highest-ordinal published immutable RC cut for that project and
  version line; it realises the version-line selector of FOUNDATIONS §2;
  and
- Release Branch: an optional mutable project-qualified convenience
  carrier aligned to the same latest-published commit as the selector.

Equal version text does not collapse these identities. Branches and the
version-line selector may move. An immutable release tag never moves (P3).

### Project-qualified Git refs

`<project>` is one explicit Project Release Namespace. It matches
`[a-z0-9]+(?:[-_][a-z0-9]+)*`, contains no slash, is unique within the
release source, and remains stable for the continuing release line. It is
assigned by the Product release authority. A directory name, display name,
definition label, package name or matching version cannot infer or
reassign it (P3, P6).

A shared release source uses these exact ref shapes for an RC-profile
publication (P3):

```text
RC branch:              refs/heads/rc/<project>/<version>
immutable RC cut tag:   refs/tags/<project>/v<version>-rc.<n>
version-line selector:  refs/tags/<project>/v<version>
release branch:         refs/heads/release/<project>/<version>
```

The short Git tag names are therefore `<project>/v<version>-rc.<n>` and
`<project>/v<version>`. A shared release source does not publish a future
cut or selector under the unqualified `v<version>-rc.<n>` or `v<version>`
refs (P3).

A single-project release source may retain the unqualified ref profile
only while it has exactly one independently released project and its
release record declares that profile. Adding a second independently
released project requires project-qualified refs before either project
publishes another cut (P3).

For the Specification Stack shared source, the allocated namespaces are
`specification_methodology`, `axiom_indexer` and `stdo_representation`.
These keys distinguish release refs; they do not merge the three Products
or imply a dependency or composition relation (P3, P6).

### Stable cuts

The `stable-v1` profile publishes an immutable release directly as
`refs/tags/<project>/v<major>.<minor>.<patch>`. Each numeric component is a
nonnegative decimal integer, with no leading zero except the single digit
`0`. The tag is annotated, targets a commit and contains exactly one
standalone annotation line (P3):

```text
STDO-Release-Profile: stable-v1
```

Its exact release declaration names the same stable cut, declared payload,
source selection and predecessor. The installed manifest records
`release.profile = "stable-v1"` alongside the complete identity of
[Project-subtree release identity](#project-subtree-release-identity).
An RC manifest retains its prior shape; adding stable support must not
change the canonical bytes of a historical release manifest (P3, P4b).

The stable coordinate is available only on a fresh version line with no
same-version RC tag in either the historical or project-qualified namespace
and no historical unqualified bare-version tag. The stable tag itself is
create-only. A same-line collision or a missing, duplicated or different
profile marker refuses stable acquisition; bare spelling or annotation alone
cannot turn an RC selector into an immutable cut (P3, P5).

There is no separate version-line selector or RC branch for this profile.
A channel `stdo://channels/<major>.<minor>.<patch>` may discover that exact
immutable stable tag; its cut ordinal is absent (`null`), and resolution
must verify the stable profile and complete identity. That channel route
creates neither another tag nor mutable alias semantics. Consumer adoption
still follows §4 (P3, P6).

A published stable tag never moves. Any change to its qualifying bytes
requires a new version and a new immutable cut, not an RC added to the
already stable line. Historical RC lines keep their selector semantics,
refs, objects, peels and URIs; this profile neither finalises nor renames
them. An RC-labelled published release remains a proper release (P3, P4b).

### Project-subtree release identity

In a shared release source, an immutable cut binds all of (P3):

- the Project Release Namespace and owning Product authority;
- the exact qualified Git ref and annotated tag object;
- the peeled commit and repository-root tree;
- the normalised repository-relative Project Subtree root at that commit;
- the Git tree object at that exact Project Subtree root;
- the declared Product member inventory and release-scoped claim bytes;
  and
- the predecessor and successor dispositions required by §9.

The Project Subtree root is a locator inside the exact peeled commit, not
Product identity. Its canonical spelling is the slash-separated Git path
from the repository root, with no leading or trailing slash and no empty,
`.` or `..` component; `.` alone denotes the repository root. Each
non-root component names the exact tree entry bytes traversed at that
commit. Moving a source project changes this locator and its cut identity
without reassigning the Project Release Namespace. If the source project
occupies the repository root, its project-subtree tree equals the
repository-root tree (P3).

A tag over a monorepo commit does not make sibling subtrees Product
members. Unrelated sibling bytes remain carrier state outside the declared
Product subject. Conversely, a member inventory or payload digest without
the qualified ref, commit, Project Subtree root and Project Subtree tree is
not a complete reacquirable release identity (P3, P6).

### Historical ref and public-URI conservation

Project qualification is prospective. Existing unqualified refs retain
their names, objects, peels and public links. A historical tag object may
remain reachable through an additional archival ref, but it is not
recreated, re-annotated, moved or replaced. An immutable historical tag
remains the same object regardless of which preserving ref reaches it
(P3, P4b).

Product-local cut names and public logical release URIs also remain
unchanged. An RC logical STDO release remains
`stdo://releases/v<version>-rc.<n>/`; a stable release uses
`stdo://releases/v<major>.<minor>.<patch>/`. The project-qualified Git ref is
transport identity and is not inserted into that URI. Resolution binds
the public logical cut to its exact historical or project-qualified Git
ref and fails closed if one project-local coordinate names different tag
objects (P3, P5).

When one version line spans the transition, latest means the greatest
positive RC ordinal across that project's preserved historical cuts and
its qualified future cuts. The first qualified publication creates the
qualified selector. The historical unqualified selector is preserved at
its existing object and ceases to be the current selector for the shared
source; it is not force-moved to imitate the qualified namespace (P3).


## 3. Phases

The release process has three phases (P0, P3, P6):

1. mutable candidate construction;
2. immutable publication under the selected profile, with RC selector
   advancement only for an RC line; and
3. exact-cut qualification, acceptance and explicit consumer adoption.

An accepted RC needs no second final cut. RC publication immediately makes
the new highest ordinal discoverable through its selector. Stable publication
makes its one exact tag discoverable under the stable profile. Acceptance is
a verdict over the exact immutable subject, not a second carrier. A change
to qualifying bytes requires a higher RC on an applicable RC line or a new
version after a stable cut (P3, P6).

### Mutable candidate construction

During candidate construction (P0, P6):

- bounded fixes are allowed after intake triage;
- qualification and operator review may continue;
- release notes may remain draft until publication;
- the candidate branch may move; and
- mutable source is explicitly non-operative for released consumers.

The intended Product boundary, release-scoped claims, excluded
source-project state and qualification basis become explicit before
publication. A material scope change is repriced instead of being silently
absorbed (P2, P6).

### Immutable RC publication

A published RC cut exists to provide one exact subject for review, replay
and possible acceptance. To publish it, the project (P3, P5, P6):

1. confirms the triaged scope and lawful constitutional re-entry;
2. declares the exact Product release subject and release-scoped claim
   set;
3. reconciles the release note and other release-facing assets to that
   subject;
4. runs the proportionate pre-RC qualification and operator checks;
5. commits the exact carrier;
6. resolves and records the exact Project Release Namespace, Project
   Subtree root and Project Subtree tree;
7. creates one annotated immutable `<project>/v<version>-rc.<n>` tag and
   an annotated `<project>/v<version>` selector tag over that same commit
   in a shared release source;
8. atomically pushes the carrier, RC branch, immutable RC tag, selector
   and optional release branch where the transport supports it;
9. verifies remotely that the immutable tag, selector and release branch
   resolve to the highest published RC commit; and
10. records enough ref, subtree, identity and inventory evidence to
    reacquire the cut without trusting a mutable checkout.

Each published RC tag is immutable. Further work increments `<n>` on the
same version line when the intended line remains applicable. It does not
require a minor-version increment merely because review found a bounded
repair. A published higher RC without matching selector advancement is an
invalid, fail-closed release state; it never authorises resolution of the
older cut as the version-line latest (P3, P5).

### Immutable stable publication

Stable publication applies the same scope, source reconciliation, proportionate
checks, exact carrier, subtree and inventory obligations as RC publication.
It instead creates one stable-v1 annotated tag and any explicitly selected
release branch, with no RC branch or separate selector. Before publication,
verify the fresh-line conditions of [Stable cuts](#stable-cuts), bind remote
absence for the immutable tag and bind every mutable destination's expected
object. Publish the selected refs atomically where supported; a changed
expectation stops publication for reconciliation. Read back the remote tag
object, commit, subtree and declared assets. The release is publicly classified
as a normal published release; release-host flags do not replace exact identity
or qualification evidence (P3, P5, P6).

### Exact-cut qualification

Qualification binds (P6, P3):

- the Project Release Namespace, qualified immutable release ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree,
  and declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, owner verdicts and unresolved gaps; and
- the complete successor relation to the declared predecessor (§9).

Evidence matches the claim. Source success does not prove packaged or
installed behaviour; packaging equivalence does not prove semantic
behaviour; artifact presence does not prove usability unless presence is
the exact claim (P6, P1; EVALUATION §1 is the generic claim law).

A cut is accepted only when the required exact-cut review and operator
checks are complete and the human authority accepts that exact subject. If
review requires a qualifying-byte change, the verdict stays on its original
subject and the applicable successor rule is used. Acceptance does not move
an immutable tag or create another final carrier (P6, P3).

### Monotonic version-line advancement

On an RC-profile line, version-line advancement makes the newly published highest RC for one
Project Release Namespace discoverable (P3, P5):

1. identify the exact new immutable RC tag, ordinal and peeled commit;
2. confirm that no higher RC ordinal already exists on that line;
3. confirm the project-qualified selector is absent or currently resolves
   to a lower RC ordinal on the same project line;
4. atomically create or force-update the annotated `<project>/v<version>`
   selector to the new highest RC commit;
5. create or update `release/<project>/<version>` to the same commit when
   that optional carrier is used;
6. push the carrier, RC branch, immutable RC tag, selector and optional
   release branch atomically where the transport supports it; and
7. verify remotely that the selector peels to the highest RC commit and
   that the matching immutable annotated RC tag exists.

Advancement is refused when the target has no matching immutable annotated
RC tag, any higher ordinal already exists, the selector would move to a
lower RC, or the selector and release branch would not align to the same
highest commit (P5).

Forward movement is strictly monotonic by RC ordinal. A later defect is
repaired through a higher immutable RC, not by moving an old RC tag or
rolling the selector backward. The selector is therefore equivalent to
`v<version>-rc.latest`, while every concrete RC tag remains addressable
(P3).


## 6. Release-scoped assets and the Product subject

### Release-scoped assets

An immutable release cut may carry release-scoped surfaces such as (P3, P6):

- release notes;
- release and installed-distribution manifests;
- dependency declarations;
- package or installed-carrier metadata;
- qualification receipts; and
- branch and tag identity declarations.

Before publication, each used surface is reconciled to the exact cut
subject. After publication, changing one of those bytes requires the
applicable immutable successor: a higher RC or a new version after stable. The
version-line selector has no content-reconciliation phase because it adds
no new Product bytes (P3).

Exact version and cut identity belong in release-scoped carriers and
consumer basis bindings (P3). How a live constitutional surface, Product
and requirements surfaces included, uses version labels is the
[SPEC_METHOD §2 Specification surface rule](SPEC_METHOD.md#specification-surface-rule).

### Product subject and repository carrier

Before qualification, the project declares (P3, P6):

- its Project Release Namespace and exact Project Subtree root;
- the exact Product member set or artifact constituting the release
  subject;
- the release-scoped claim surfaces describing that subject; and
- co-located mutable source-project fields excluded from both.

A repository commit carries those declared sets but does not make every
co-located file or sibling Project Subtree a Product member. The exact
Project Subtree tree and Product member inventory distinguish the subject
from the wider carrier. Once the immutable cut is published, no post-review
carrier delta is admitted into that cut. Publication-caused ticket or
source-work bookkeeping is recorded afterward on the continuing source
branch and cannot move the immutable cut tag (P3, P6).


## 7. Coordinated release-matched asset cohorts

A Product authority may declare an explicit cross-Product Release-Matched
Asset Cohort when one source corpus and its required distributed or
derived assets need to remain usable as one versioned set. The declaring
relation names every required Product and asset, the exact source
dependency, its owning authorities, the qualification boundary and the
publication transaction. Path co-location, equal version text or a common
actor cannot infer the relation (P3, P6).

For the existing RC-profile cohort, every required member uses one exact version suffix
`<version>-rc.<n>`. Product-local cut names and refs render it as
`v<version>-rc.<n>`; embedded asset-version fields render the same suffix
without `v`. Qualification normalises only that leading cut-name marker
and requires exact suffix equality. Equal versions establish release
matching only. They do not collapse Product identities, member
inventories, tags, acceptance judgments or release authorities (P3, P6).

For a release-matched STDO stack, the closed cohort contains all of (P3,
P4b):

1. the exact STDO standards corpus cut;
2. the distributed `spec` plugin and host assets carried by that STDO cut;
3. the exact Axiom Indexer mechanics Product used to validate and project
   the index;
4. the exact STDO Representation Product; and
5. its released `a_c.STDO` axiomatic program and logical constraint map
   or equivalent semantic index, with the complete source-STDO member
   inventory, member digests, member-set digest and exact cut identity
   used to derive it.

The cohort is incomplete when a required member is missing, stale,
differently versioned, built from another source cut, or unable to
reproduce its declared source-member and digest closure. A change to any
source member covered by the index invalidates the old derived candidate
for the successor cohort. The index is regenerated, mechanically
validated, independently qualified where required, and released under the
same new cut name. A stale index may remain immutable history; it cannot
accompany the changed source as the current cohort (P3, P5, P6).

### Two-commit construction and one publication transaction

Exact installed-manifest identity includes the annotated STDO tag object,
so a same-commit carrier containing both that identity and derived child
bytes would be self-referential. A coordinated STDO cohort therefore uses
this bounded two-commit construction (P3, P5):

1. commit A freezes the exact STDO corpus, plugin, release record and
   their qualification bytes;
2. the annotated STDO cut tag is created locally over commit A but is not
   pushed;
3. that exact local cut is installed and verified, producing the manifest
   identity used by every derived Product and index;
4. the Axiom Indexer, STDO Representation, semantic-index bytes and cohort
   record are derived and frozen in commit B;
5. prepublication qualification evaluates commit B against the exact
   local STDO tag before child immutable tags are created;
6. annotated child cut tags and every Product-local RC branch,
   version-line selector and optional release branch are prepared
   locally;
7. a mandatory post-tag, pre-push gate re-runs qualification over every
   local annotated tag object and peel, selector, RC and release branch,
   normalised version mapping, target commit and the exact closed ref
   set; it also fetches and binds the expected remote object ID or
   required absence for every destination ref; and
8. one transport transaction atomically publishes only that qualified
   carrier branch and complete Product ref set.

If the remote does not support atomic ref publication, publication
refuses. The process has no sequential-push fallback. Every immutable cut
tag is create-only and therefore requires bound remote absence. Every
mutable carrier, RC branch, selector and release branch uses an explicit
per-ref compare-and-swap lease, such as
`--force-with-lease=<ref>:<expected-oid>`, in that same atomic
transaction. A missing expected ref, unexpected existing tag or changed
remote object ID stops publication; the operator refetches and repeats
complete content and local-ref-graph qualification before constructing
another push. A lease mismatch never falls back to an unguarded force, a
partial push or an in-place expectation update (P5, P3).

Remote verification fails closed when any required cohort ref is absent,
lightweight, differently versioned, points to the wrong Product commit, or
has a selector or release branch that does not match its immutable cut.
Post-publication bookkeeping may use a later commit, but it cannot move
any immutable cohort tag (P5, P3).

### Qualification and recovery

Prepublication content qualification binds the exact commit-A STDO tag
and manifest, commit-B source tree, all Product-local target refs, version
markers, Product member inventories, semantic-index bytes and complete
source-corpus digest closure. It proves that the frozen candidate can be
tagged without changing a qualifying byte. After tag and mutable ref
creation, local-ref-graph qualification binds their annotated objects,
peels, target commits, exact push set, and every fetched remote expected
object ID or required absence to that unchanged content result.
Post-publication qualification verifies the same relation from remote refs
and refuses a partial cohort (P6, P3, P5).

A historically published source cut may be the basis of a later
same-version backfill only when separately authorised recovery law names
that exception. Every recovered asset still binds the exact historical cut
and same cut name, and remote completeness remains mandatory. Recovery
cannot move the historical tag, add bytes to its Product subject, or be
represented as an atomic cohort that existed at the original publication.
Normal successor publication uses the atomic cohort process above (P3,
P6).

Adding or changing this cohort law changes qualifying bytes of this
member. It governs only an immutable successor that contains those bytes
and cannot retroactively make an earlier cut a coordinated cohort (P3).


## 8. Acceptance

### Acceptance criteria

A release cut may be accepted when (P6, P3):

- proportionate prepublication qualification passed for the declared subject;
- independent exact-cut review passed where required;
- required operator review is complete;
- the intended release scope and successor relation are stable;
- release-scoped assets accurately describe the exact cut;
- all release-blocking gaps, including the findings that block promotion
  under [EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
  are closed or the claimed scope is explicitly narrowed; and
- the human Product authority accepted the exact immutable cut identity.

Each criterion is a mandatory gate in the sense of
[FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse):
it applies irrespective of any selection of checks after a change, and
retained evidence satisfies it only under the validity conditions stated
there (P6).

Acceptance attaches to that immutable cut identity. It neither advances
nor rolls back the version-line selector. Consumer adoption separately
evaluates the exact latest target presented by the channel and mutates
only after its digest-bound plan is accepted (P6, P3; EVALUATION §5 is
the generic acceptance law).

### External qualification dependencies

Some claims depend on external backends, transports or operator-facing
services outside the local carrier. Such a dependency may remain out of
Product for carrier and migration classification while still blocking the
dependent release claim (P6, P5).

A clean skip caused by an unhealthy external dependency is an evaluation
not performed, which has no result
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). It may
preserve correct Product classification, but it cannot establish that the
dependent capability passed. The claim is either qualified against a
healthy dependency or narrowed before acceptance (P6, P5).


## 9. Successor baseline conservation (STDO-UP-015)

A successor identifies the exact predecessor immutable cut whose semantic
claims it evolves. That origin remains immutable for the candidate. Every
predecessor claim capable of affecting the successor receives one semantic
disposition (P4b, P3, P6):

- conserved: the successor retains the claim;
- superseded: an accepted successor relation replaces it;
- intentionally removed: current Product authority removes it; or
- not applicable: it has no successor effect, with a bounded reason.

Evidence for a disposition is retained or reassessed under
[FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse):
a `conserved` reading made on an earlier successor text applies to a later
one only where the owning text and the consumer bindings that carry it
are unchanged, or the change is shown not to affect the claim (P3, P6).

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
(P6, P1). A `conserved` disposition recorded
before this test applied is re-evaluated under it before the affected
claim qualifies; until then its standing is `unresolved`.

Each disposition is a claim the successor makes about one predecessor
claim ([EVALUATION §1](EVALUATION.md#1-claims)), not a result value; its
predicate is its value's wording above. It is distinct from the decision
owner's disposition of an assessed candidate
([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)), which is an
acceptance result. Qualification evaluates each
disposition on evidence and records a value of the core result algebra
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) with that predicate.
An unresolved disposition states no claim and so has no result: in the
qualification of the affected claim it is a planned assessment without a
closed result, which is why it blocks that qualification
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps). Purpose and material relation: a recorded disposition establishes
nothing until it is evaluated, so no disposition stands as a result (P6,
P5).

Where a maintenance or support line may affect retained claims, the
release basis identifies the watched source, observation boundary,
inclusion policy and successor candidate. Relevant changes receive
semantic disposition at material integration and exact-cut qualification.
The consumer owns its record, branch strategy, comparison and proof
mechanism (P4b, P6).

[EVALUATION §5](EVALUATION.md#5-acceptance) states what acceptance
requires of the disposition record; it applies this section and is not
part of it (P4b, P6).

### Deterministic-kind migration

A successor that adopts the total deterministic kind of
[AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds)
preserves each existing evaluation operation's unchanged subject, admissible
reads, witness/log outputs, permitted writes, stops/results, authority and
invalidation conditions. That profile alone does not
establish the new kind's totality, closed dependencies or declared outcomes.
The old deterministic evaluation/proof definition supplies no general
termination argument. Assess each proposed use against this relation (P3, P6):

| Evidence and declared migration status | Successor disposition |
|---|---|
| Establishes the new totality, closed-dependency and outcome contract | Map to common F_D plus the unchanged operation profile and exact traversal binding. Preserve the evidence and grants. |
| New-kind eligibility is unestablished, and the owner has identified the missing evidence or a separately declared bounded successor and its remediation obligation | Keep that identified migration pending. The legacy operation retains only its lawful standing on its exact old basis while it remains applicable; it gains no successor F_D standing. A narrower domain or fuel-bounded implementation has its own contract, identity, exhaustion outcomes and affected preservation evidence; it does not retrospectively prove the old operation total or preserve every old continuation. |
| New-kind eligibility is unestablished and no supported remediation or successor classification has been selected | Retain the exact legacy meaning and evidence with an explicit unresolved successor-classification obligation until its owner disposes it. The legacy operation retains only its lawful standing on its exact old basis while applicable. Grant neither new F_D standing nor an automatic F_P label; the affected successor claim stays open. |

An old deterministic evaluator with unestablished termination or an
undeclared material dependency takes the second or third row, even if it
preserves the judged subject: the second row requires an identified evidence
gap/remediation or selected bounded successor; absent that, the third records
the unresolved classification. Evidence alone need not choose the owner's
remediation. This relation imposes no general decision procedure for totality.
These eligibility/remediation cases are not additional semantic dispositions
under this section. Generic role descriptions and schematic traversal contracts are not concrete
operations with an implementation to qualify; their use still binds the
kind and operation contracts when instantiated.

ODD admission and closure retain their named operation owners under
[AXIOMATIC_CALCULUS §5's authority boundary](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds).
Exhaustion
retains the evaluated predicate and its signature/traversal stop mapping,
as [the conformance examples](examples/DETERMINISTIC_CONTRACTS.md) distinguish.

Immutable consumers keep their selected edition's meaning. New consumers
explicitly select the complete successor and operation profiles. A stable
concept URN is not its immutable calculus edition
([AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity)). Migration
records the old release, manifest, member and clauses and the applicable row
above. Current URN lookup never reinterprets history. A versioned import or
alias records its justified supersession and grants no broader permission.
Disposition and qualification retain the separate obligations of this
section; unresolved mappings block the affected successor claim.

Broadening operation purpose while strengthening totality, dependency and
evidence requirements is a substantive semantic change. A patch-shaped
version label by itself promises no compatibility. The release's version
assessment identifies the selected predecessor, affected consumer mappings
and remaining obligations. This relation settles no general version-line
policy and waives no acceptance gate.

