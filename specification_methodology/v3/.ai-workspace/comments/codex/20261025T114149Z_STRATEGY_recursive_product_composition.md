# STRATEGY: Recursive Product composition and governed context

**Author:** Codex, Writer `/root/composition_proposal_writer`  
**Date:** 2026-10-25  
**Addresses:** STDO 3.0.1 Product composition; the downstream decomposition use case; STDO Skills → a_c  
**Status:** Open — amendment proposal for review

## Summary

Make independently governed Products usable as leaves and as recursively composed
capabilities. Each Product owns a coherent outcome and can be entered through its
own definition and admitted frame basis, given its declared dependencies. A
composite owns the integrated outcome. Its edges carry the contracts and authority
conditions for crossing constituent boundaries, including the information that
may enter each actor's context.

Use the existing `composition` carrier and its `relation` and `contracts` fields.
The first useful addition is a precise Product-level application of existing
STDO authority, basis, preservation and evidence laws. A new scheduler, Product
kind enum or universal graph database is unnecessary for this proposal.

The concrete package is:

- [Draft Skills → a_c relation](../../../../../stdo_skills/.ai-workspace/comments/codex/20261025T114149Z_STRATEGY_a_c_support_dependency.md): actual Product identities, supported
  operations, selected provider cut, actor boundaries and adoption conditions.
- [Proposed edge](../../work/PRODUCT_COMPOSITION_PROPOSAL_01/PROPOSED_SKILLS_AC_EDGE.json): the existing four-field schema, based explicitly on
  `stdo_skills/stdo_skills.json`; it is not inserted into the live definition.
- [Recursive worked example](../../work/PRODUCT_COMPOSITION_PROPOSAL_01/RECURSIVE_EXAMPLE.md): a composite, an independently enterable
  intermediate Product, two leaves, sharing, replacement and context exclusions.
- [Acceptance cases](../../work/PRODUCT_COMPOSITION_PROPOSAL_01/ACCEPTANCE_CASES.md): deciding predicates, positive and adverse cases,
  owning implementation boundaries and present evidence.
- [Source custody](../../work/PRODUCT_COMPOSITION_PROPOSAL_01/SOURCE-CUSTODY.json), [retained downstream input](../../work/PRODUCT_COMPOSITION_PROPOSAL_01/inputs/STDO_PRODUCT_COMPOSITION_GAP_SANITIZED.md) and
  [retained tool-probe results](../../work/PRODUCT_COMPOSITION_PROPOSAL_01/retained-tool-probe/results.json).

The baseline being extended is the proper published immutable
`stdo://releases/v3.0.1-rc.1/`, native commit
`fe4941f56a52ed3697a2b516d8d68948b0ea65d9`, manifest
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
The v3 source project's builder remains its selected `v2.5.1-rc.2`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
This package changes neither installation, operative Product Definition nor
accepted requirement. A successor version is not selected here.

## The concrete gap

The downstream requirement is to construct substantial outcomes from reusable,
standalone projects, then refine or replace their parts without reconstructing
the whole governance arrangement. Directory recursion alone cannot provide that.
The method needs a clear account of the local outcome, the composed outcome and
the authorized information crossing each edge.

Our own Skills Product demonstrates a small existing declaration gap:
[Product](../../../../../stdo_skills/specification/PRODUCT.md) and SK-04 consume
a_c's native support operations, while
[its definition](../../../../../stdo_skills/stdo_skills.json) has an empty
`composition` array. This is a missing durable relation, not evidence that every
skill invocation fails. The methodology pin is a different relation; Codex and
Claude are two realizations of one Skills Product.

There is also a separate implementation defect. The retained independent probe
ran the installed toolchain 0.1.5's actual `stdo fleet verify` over a valid control
and four single-defect variants. A wrong target identity, missing target
file, missing relation anchor and missing contract all returned exit 0,
`valid: true` and no failures. The deciding path verifies definitions individually
but never traverses their composition edges. These are already required §9
checks. The result does not justify saying that no tool checks any edge:
`cohort_update` performs its own selected identity checks.

## Existing owners and the proposed delta

| Current owner in the exact 3.0.1 cut | Already established | Addition proposed here |
|---|---|---|
| PRODUCT_DEFINITION §§1, 7, 9, 12 | Distinct WHAT; tenants; Product-owned frame adoption; explicit recursive discovery; edge identity, contracts, authority and resolution | A concrete leaf/composite account; independent entry; a reusable edge-contract profile; recursive reliance and context examples |
| FOUNDATIONS, Basis and Change impact and evidence reuse | Exact or moving basis; material dependencies; historical evidence and justified reuse | Product-level bindings and falsifiers, not a new invalidation algebra |
| FOUNDATIONS, Observation sufficiency | Required decisions and continuations must survive a representation under stated conditions | Apply it to permission-filtered actor contexts; retain currentness and obligations |
| ACTIVATION §§1, 4, 7 | Authorized execution, consumer interpretation, transformation/refinement obligations | Apply those contracts to provider replacement and boundary crossings |
| REFERENCE_FRAME RF-009; EXECUTIVE_BASELINE §§6, 9–11 | Decomposition, communication, authority and evaluation are distinct; scoped causal-cone inspection | Explain recursive Product selection and separately authorized inspection |
| GLOSSARY | Indexes source-owned meanings | Add navigation to Product composition, leaf and composite; no second semantic owner |

The governing sources are pinned in SOURCE-CUSTODY. The proposal's PC clauses
below would be owned by PRODUCT_DEFINITION §9, with §7/§12 and the profile/template
consumers referring to that owner. Repeated foundations should remain references
to their existing law.

## Proposed clauses

### PC-01 — Recursive Product boundaries

A Product identifies one coherent WHAT and its owning authority. Alternative
realizations of that WHAT are build tenants. A decomposition into Products names
which distinct outcomes and authorities each constituent owns, and which outer
outcome the composition owns.

Within a declared decomposition scope, a leaf has no further constituent Product
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
not permission to omit a deciding condition. This applies FOUNDATIONS' scoped
preservation law; it supplies no general optimal context selector.

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
requires an authorized successor relation and affected reassessment. Matching
signatures, labels or a sample output is insufficient. New capabilities may be
added without silently widening existing consumers' duties or grants.

### PC-07 — Change, evidence and reliance

Each cross-boundary use binds the actual selected sources and material execution
basis, including uncommitted bytes where relevant. A moving selection identifies
how advancement is detected and which reliance must be reassessed. Git is one
possible carrier, not a mandatory identity system.

Changes and new counterexamples propagate through material assertion, execution
and evidence-use dependencies under FOUNDATIONS' existing impact law. Historical
evidence remains about its original subject. Reuse on a changed subject needs an
established applicability or preservation relation; rereading alone does not
establish it. A new release does not invalidate a still-selected older release,
and a changed hash alone establishes neither semantic incompatibility nor
continued validity. Unknown impact holds the dependent assurance or widens
assessment; it does not require unrelated work to restart.

## Disposition of the downstream R1–R9

| Input | Disposition and reason |
|---|---|
| R1 base kinds | Use `consumes`, `coordinates` and `assesses` as optional examples, not a closed or disjoint taxonomy. PC-03 defines the required meaning; a kind cannot supply permissions. |
| R2 no edge/no read | Replace the universal restriction with PC-04. Declare durable consumption and separately bind authorized causal-cone inspection. Both obey information eligibility. |
| R3 pure orchestrator | Keep as a selectable local profile. A composite may own runtime behavior, state and integrated results; it cannot appropriate constituent meaning. Counts alone often lose deciding distinctions. |
| R4 standalone | Adopt the scoped independent-entry obligation in PC-02. Test adopted authority and actual dependency closure, not merely which directory stores the frame. |
| R5 source revision | Apply existing Basis law through PC-07, including actual bytes and moving-source observation. Do not require Git or mistake a commit for dirty working bytes. |
| R6 blanket staleness | Apply material invalidation and justified reuse. Preserve old evidence and exact old selections; neither universal invalidation nor reread-as-proof is sound. |
| R7 graph vs order | Adopt the distinction, broaden composition beyond reads, and require an executable cycle resolution. A named lead is insufficient. |
| R8 tool checks | Repair the demonstrated `fleet verify` omission against existing law. No kind-refinement check without a separately adopted kind contract. |
| R9 glossary | Add an index to PRODUCT_DEFINITION's single owner, distinguishing this sense from result, activation, traversal and module composition. |

The external workspace's specific Products and failed standalone entries remain
reported observations in the supplied sanitized input. Only the local Skills
relation and retained synthetic tool probe are independently grounded here.

## Bounded delivery sequence

| Step | Owning Product and concrete deliverable | Exit evidence |
|---|---|---|
| 1. Review this package | STDO v3; clauses, real relation and recursive case | Source-first nonauthor review of meaning and counterexamples; owner disposition of the proposed amendment |
| 2. Restore existing verification | STDO manager's owning source scope; target/identity/URI/fragment/contract resolution on declared resolver boundaries | Valid control plus isolated broken-edge cases, nested/shared targets, supported URI modes, cycles and bounded failure; no unrequested network or filesystem expansion |
| 3. Adopt the real dependency | Skills and a_c owners; select the exact supported contract and promote the draft edge/relation | Resolved identity/basis, exact grants and compatible operation path; a declaration alone claims no successful invocation |
| 4. Add scoped context support | a_c requirements/design first; bind owner-authorized declarations to current source/preflight/context mechanisms | Source-bound permissions and exposure evidence on the actual path; unauthorized traversal, summaries and host bypasses handled under the declared capability claim |
| 5. Integrate method and consumers | STDO successor source, reference-frame/example/template consumers, a_c/Graphify representation and each skill tenant | Clauses conserved or explicitly changed; source-matched representations, exact carrier recovery plus semantic review; actor tasks preserve decisions and refusals |
| 6. Select and release the successor | Existing release owners and tools | Exact accepted subject, compatibility decision, package/install checks and published immutable release; version chosen from the demonstrated change |

Only this proposal package is constructed by the present instruction. Steps 2–6
are the proposed subsequent execution plan. Existing Claude Q05 and 3.0.1
representation obligations retain their recorded standing; this package neither
reruns nor closes them.

The manager owns mechanical relationship resolution, a_c owns its supported
computational acquisition/preflight/evidence operations, and skills guide F_P
actors. An F_P actor interprets source-owned authority and selects material
context; a deterministic tool checks a declared finite binding. The declaration
must not be silently inferred from arbitrary prose and treated as admitted.
Graphify can support discovery and navigation without owning any grant.

For an enforced clean-room claim, the actual host must restrict unmediated
filesystem, shell, network, index and inherited-context paths as selected by the
threat model. Today's a_c cooperative local process contract provides no OS
confinement. Logged mediated acquisitions support their scoped exposure claim,
not a proof that no other acquisition occurred.

## Review and release boundary

This is a draft amendment with a worked design witness. The acceptance matrix
states what later implementation must demonstrate; its expected outcomes are not
reported as executed results. Mechanical package checks and frozen review inputs
are retained alongside the source custody. Product-owner ratification, implementation
acceptance and release remain separate decisions over their exact subjects.
