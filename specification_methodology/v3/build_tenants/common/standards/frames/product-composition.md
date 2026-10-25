# Reference frame product-composition

Task: Bind one recursive Product composition, its standalone constituent outcome, exact edge authority and permitted sufficient actor context; assess joins, replacement and continuation without transferring grants.

Purpose: PRODUCT_DEFINITION section9 owns the clauses. This projection covers the composition owner and binds required shared laws; it does not establish full task sufficiency or acceptance.

Binds:

- Use the shared preservation and licensing contract for any replacement or refinement. ([../ACTIVATION.md#refinement](../ACTIVATION.md#refinement); member sha256=56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d; section sha256=5b33a40f42b5f4449224ffe67bd387dc329f62207e3bf2bea3dc5ceda0810e1d)
- Retain the distinctions required by the actual decision/continuation under its fixed conditions; permission is not adequacy. ([../FOUNDATIONS.md#assurance-relations](../FOUNDATIONS.md#assurance-relations); member sha256=92fe2f3c09a59b4e9a732463a41d4a45d7efd693648159621e03c75f7127eac5; section sha256=09932548f56a2af56c4fb0140aa7adf1859bcf42680d174b2bbb78e30531690b)
- Reassess material changed reliance while retaining original evidence and established applicability. ([../FOUNDATIONS.md#change-impact-and-evidence-reuse](../FOUNDATIONS.md#change-impact-and-evidence-reuse); member sha256=92fe2f3c09a59b4e9a732463a41d4a45d7efd693648159621e03c75f7127eac5; section sha256=e989bf4b8c0dd996e5545f18db94f8ba275d14485697c0b046429746ed3bfbc6)

A `Binds:` item names an obligation the activation of this frame binds, with
a link to the owning section, the digest of its member and the digest of that
section, or of the span of sections it names, where it names one; the item
copies no section and owns no determination, and where no route of this frame
carries the section the item is a paraphrase of it.

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

1. [PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition](../PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition)

Size of this frame: 15977 bytes.

Source: PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition sha256=7394f9d046e34f0ced33372dd0bd1d8983cfbab5453ebc8997d65d4e7a43a567

## 9. Recursive discovery and explicit composition

Tools discover `stdo_*.json` recursively within the selected workspace
boundary: definitions at the workspace root and definitions at arbitrarily
deep nested project roots (P3).

For a requested Product scope exactly one applicable definition is
selected; zero or several unresolved definitions fail closed, and a
symlinked definition is refused (P6, P5).

Directory nesting creates no implicit inheritance, ownership, composition
or constitutional override. Parent and child definitions stay independent
until `composition` explicitly relates them. Each composition entry records
(P6, P3):

- `product_definition`: the current locator for the target definition;
- `target_definition_id`: the stable identity expected from the target's
  `product.definition_id`;
- `relation`: the authority defining the directed composition kind, the
  source and target roles, owner, scope, lifecycle and invalidation
  conditions; and
- `contracts`: one or more exact interface, capability, identity,
  lifecycle, data, evidence or other governing contract references
  consumed by that relation.

Resolution verifies both the locator and the expected identity. Moving a
definition requires a locator update and does not change its identity.
Replacing the content at the same locator with another definition identity
fails closed. When an edge binds exact immutable Product or release
versions, the cited relation and contracts also carry and verify those
identities; the mutable definition identity cannot substitute for them
(P3, P5).

A conforming discovered set satisfies all of the following (P3, P6, P1):

- every definition validates against its selected released schema;
- every required URI and fragment resolves under the declared workspace
  and resolver boundary;
- every `product.definition_id` is unique;
- every build-tenant identity is unique within its overlay;
- every governed scope has a resolvable applicable reference-frame basis,
  and overlapping basis bindings are reconciled by their cited authority;
- every local disambiguation binds one exact term, target context,
  complete material candidate set, selected concept, authority, basis and
  scope; `resolves_to` is a member of `disambiguates`; and its referenced
  resolution carrier is congruent with those bindings;
- every material cross-context term seam resolves through an explicit
  import, disambiguation, translation or equivalence relation rather than
  nominal match;
- every composition target resolves to another product definition whose
  `product.definition_id` equals `target_definition_id`, and every
  relation and non-empty contract set resolves; and
- no two carriers claim authority for the same Product, tenant, ticket
  state or constitutional relation.

Portable Draft 2020-12 JSON Schema validation establishes structural shape.
The schema's `uri` and `uri-reference` formats are annotations unless the
declared validator implements format assertion. Conformance therefore
performs an explicit RFC 3986 URI and URI-reference syntax check with an
assertion-capable validator, followed separately by resolution, fragment
existence, selected-release identity, uniqueness across files,
constitutional sufficiency, semantic-resolution and cross-context-relation
completeness, and authority-congruence checks. The structural subset and
the semantic subset of these checks are distinct claims (EVALUATION §2;
P1, P6).

### Product composition contract

The following clauses apply the shared authority, identity, context,
preservation and change laws to Product composition. They define no second
admission or result algebra. A Product may consume, coordinate or assess
another Product through its declared relation; these roles are neither a closed
nor disjoint kind taxonomy, and none confers authority (P6, P3).

[The contract template](../templates/PRODUCT_COMPOSITION_CONTRACT_TEMPLATE.md)
projects these coordinates; [the recursive example](../examples/PRODUCT_COMPOSITION.md)
works them through a shared leaf and an independently enterable composite.
[CONFORMANCE](../CONFORMANCE.md#product-composition-discriminators) names their
positive and adverse discriminators. These artifacts apply this owner (P1, P6).

### PC-01 — Recursive Product boundaries

A Product identifies one coherent WHAT and its owning authority. Alternative
realizations of that WHAT are build tenants. A decomposition into Products names
which distinct outcomes and authorities each constituent owns, and which outer
outcome the composition owns.

Under the identity and ownership laws (P3, P6), within a declared decomposition scope, a leaf has no further constituent Product
boundary exposed by that decomposition. It may contain modules and declared
external dependencies. A composite relates two or more constituent capabilities
or an outer capability to its constituent capability; its own capability may in
turn be consumed as a constituent. The same definition, contract and authority
laws apply at every depth. Shared constituents keep one identity and their
separately bound uses; a hierarchy view may show several references to one leaf.

Decomposition, capability/data dependency, inspection permission, authority and
work prerequisites are distinct relations. A directory tree establishes none of
them. A named composition view states its root, participating identities,
selected boundaries and relation kinds rather than treating all reachable edges
as one hierarchy.

### PC-02 — Independent entry and the integrated outcome

A Product offered as a standalone constituent must be enterable through its own
Product Definition and a Product-authorized applicable frame basis, with the
dependency closure and capabilities its contract declares. Entry must not require
an enclosing composition's activation unless that enclosing capability is itself
an explicit prerequisite. Such a prerequisite is disclosed as a limit on the
standalone claim. Shared or externally located frame documents are permitted
where adoption, scope and availability are established; file ownership alone is
not the deciding test.

Standalone does not imply dependency-free, separately deployable or able to
supply every host itself. The claim names which construction, evaluation or use
can be performed independently and its required inputs. The composition owner
separately establishes interface compatibility, material joins and its complete
outcome. Successful constituent checks do not establish that outer predicate.

### PC-03 — The edge's contract and authority record

For each directed relation, the `relation` authority and referenced `contracts`
state, directly or by exact reference:

1. Source and target Product identities and roles; the consumed capability,
   outcome, purpose, selected basis and currentness policy.
2. The existing owners and grants for each material operation: acquisition,
   disclosure, use, execution, mutation, assessment and disposition. A kind or
   role label records no grant by itself.
3. Admissible inputs and exports; material assumptions, effects, failures,
   obligations and evidence; restrictions on implementation material and derived
   information where applicable.
4. The acting principals or binding rule, task/phase scope, permitted delegation,
   return consumer, stop/refusal conditions and revocation/invalidation route.

These coordinates may be supplied by source-linked prose. The relation locates
and constrains lawfully granted authority; it cannot manufacture the target's
permission or the source's admission. Missing material authority or an unresolved
conflict withholds the dependent action. The execution-scoped activation remains
the place where a particular actor, input, effect and return are bound.

### PC-04 — Recursive authority and information eligibility

A permitted A → B use does not entail A's access to B's dependencies. Neither
A → B plus B → C nor two routes to a shared leaf imply a union of their grants.
Each onward acquisition, disclosure or delegated effect needs authority for that
actor, purpose and path, including any permitted onward use of returned material.
Existing delegation may authorize a chain explicitly; its scope cannot expand
silently at a recursive step.

A provider may encapsulate internal dependencies behind an adequate contract.
Consumers need not flatten every implementation dependency into a direct edge.
Where an outer claim materially relies on a far-side contract, assumption,
evidence item or acquisition, that reliance and its applicable authority must be
preserved through the boundary. Unknown impact is not evidence of encapsulation.

Durable Product consumption and bounded authorized inspection are different
relations. A Reviewer or diagnostic Worker may inspect a larger causal cone under
an explicit access grant without thereby adopting those internals as a runtime
dependency or gaining a write grant. If findings become a continuing construction
constraint or dependency, their producer, applicability and governing relation
must be retained.

### PC-05 — Context construction and clean-room conditions

An actor's selected context must satisfy both permission and adequacy for its
engagement. Permission covers the source information and permitted derivations,
not only paths or filenames. The boundary identifies eligible source classes,
exports and tool outputs, material provenance, intended use, later acquisitions
and the effect of prior exposure. An allowed file location or a fresh summary
does not sanitize prohibited information.

A target owner may authorize an export, but clean-room eligibility additionally
requires that the engagement's information policy admits that export and its
provenance. The actual delivered/acquired material must be recorded to the extent
required by the claim. An uncertain or prohibited exposure follows the declared
hold/re-entry rule; it cannot be repaired by deleting its receipt or relabeling
the same actor fresh. Prior actor knowledge and external acquisition channels are
part of the declared limits.

Adequacy retains the distinctions required for the task's decisions and
continuations, including unresolved obligations, result standing, currentness and
authority. If the permitted material is insufficient, acquire an authorized
extension, narrow the task with the owner, use a suitable actor or return the
unresolved outcome. Permission is not evidence of sufficiency, and a budget is
not permission to omit a deciding condition. This applies [FOUNDATIONS Observation sufficiency](../FOUNDATIONS.md#assurance-relations)
and its scoped preservation law; it supplies no general optimal context selector (P1, P2, P6).

### PC-06 — Readiness, cycles and replacement

Work selects a dependency-ready frontier at the required subjects and revisions.
A cycle in declared Product relationships need not be a cycle in the selected
work. A cycle of current prerequisite claims requires an executable resolution:
for example an admitted prior revision, explicit seed, staged contract or bounded
iteration with its continuation/stop conditions. Naming a lead alone does not
supply a missing prerequisite or establish convergence.

Replacing a constituent or refining it into further Products preserves the
consumer's material contract: meaning, preconditions, effects, failures,
authority, lifecycle, evidence and subsequent obligations. A semantic change
requires an authorized successor relation and affected reassessment. The [ACTIVATION refinement contract](../ACTIVATION.md#refinement) governs this
preservation. Matching signatures, labels or a sample output is insufficient (P4a, P6). New capabilities may be
added without silently widening existing consumers' duties or grants.

### PC-07 — Change, evidence and reliance

Each cross-boundary use binds the actual selected sources and material execution
basis, including uncommitted bytes where relevant. A moving selection identifies
how advancement is detected and which reliance must be reassessed. Git is one
possible carrier, not a mandatory identity system.

Changes and new counterexamples propagate through material assertion, execution
and evidence-use dependencies under [FOUNDATIONS Change impact and evidence reuse](../FOUNDATIONS.md#change-impact-and-evidence-reuse). Historical
evidence remains about its original subject. Reuse on a changed subject needs an
established applicability or preservation relation; rereading alone does not
establish it. A new release does not invalidate a still-selected older release,
and a changed hash alone establishes neither semantic incompatibility nor
continued validity. Unknown impact holds the dependent assurance or widens
assessment; it does not require unrelated work to restart.

