# Common Realization Requirements

The authoritative calculus is
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`, SHA-256
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
These requirements select implementation obligations without redefining it.
Physical file layout and Graphify-specific record grammar belong to tenant HOW.

| ID | Required behavior |
|---|---|
| AC-R-001 | Bind the exact calculus, subject basis, signature, interpretation contract, semantic-selection ledger and content identity. Mutable locators alone do not establish identity. |
| AC-R-002 | Preserve all eight core populations as distinct families. Every local identity occurs exactly once. Empty populations are explicit and signature-permitted. Unknown fields, kinds and unsupported domains refuse within the declared checked fragment. |
| AC-R-003 | Preserve every record's content, context, owner, scope and basis. Typed references have explicit cardinality and target domains; local/external collisions, dangling references and wrong-family/sort targets refuse. |
| AC-R-004 | Retain the exact external-resolution coordinates separately from local populations. No inferred relationship, payload equality or same-spelled identifier supplies semantic identity or authority. |
| AC-R-005 | Preserve directed relation identity, distinct parallel relations, self-relations, qualifications, ordered content and repeated occurrences through representation and recovery. No carrier optimization silently merges or discards them. |
| AC-R-006 | A representation has an exact versioned profile and deterministic content identity. Recovering it preserves the complete declared model; malformed, stale, incomplete or contradictory representations refuse. |
| AC-R-007 | Distinguish a proposed-model view from the accepted-interpretation encoding relation. The latter requires an external accepted judgment with exact model identity/digest and declared decision contract, authority, evidence and provenance. A consistency check does not prove the judgment's legitimacy or semantic correctness. |
| AC-R-008 | Acquisition binds exact seeds and authored/signature-declared governing dependency roles. Compute complete finite closure, preserving constraints, governing conditions, latitude and residuals required by those exact roles. Cycles terminate. A budget cannot silently truncate required content. |
| AC-R-009 | A projection identifies the exact parent, selection, included/excluded records and external/unresolved boundaries. Discovery and provenance links remain inspectable without automatically becoming governing dependencies. A projection is not a complete replacement model or an acceptance decision. |
| AC-R-010 | Search and path results report their structural scope. Connectivity, ranking and extraction confidence do not establish implication, semantic truth, safe execution or authority. |
| AC-R-011 | Mechanical validation returns only the properties actually checked. F_P interpretation, F_D assessment, F_H adjudication and domain operations retain distinct identities and claims. Do not report full calculus admission from shape, digests, round trips or path traversal. |
| AC-R-012 | Declare unsupported operations and return an explicit refusal when requested. In particular, retaining transformation records does not establish AC-013 transformation execution or preservation proofs. |
| AC-R-013 | The realization is usable independently of v3, Axiom Indexer and STDO Representation. Its concrete stack, upstream identity, commands and qualification evidence are tenant-owned. |
| AC-R-014 | Qualify preservation with adversarial cases and an actual boundary trial. Measure discovery, context sufficiency, correction and total accepted-result cost before claiming efficiency improvement. |
| AC-R-015 | A tenant offering source-to-model creation declares its F_P authoring contract, exact input corpus and source coverage, preserves qualifications and residuals, and retains generation provenance. Discovery confidence, inferred graph links, shape checks and source processing do not by themselves establish normative relationships, semantic fidelity, completeness or acceptance. Existing authored models are not required inputs to that creation path. |

Interpretation fidelity, representation preservation, actual use, semantic
acceptance and release are separate deciding questions. Their evidence and
residuals remain explicit even when a mechanical check succeeds.

## Formalisation

[FR-001–FR-007](formalisation.md) govern tenants declaring formal definitions
and checked proofs. They require a source-linked mathematical interpretation,
explicit premises and trust boundaries, and a runnable first fragment for exact
declared closure, retained-record projection and budget refusal.
[T-011](../../.ai-workspace/tickets/active/T-011-lean-formalisation.md) selects
the independent Lean/Mathlib realization. These obligations are capability
specific; they do not retrospectively claim formal verification of Graphify.

[FR-008–FR-014](formalisation.md#reusable-formal-verification-gate) add the
reusable exact-subject gate selected by
[T-012](../../.ai-workspace/tickets/active/T-012-reusable-formal-gate.md): checked
versioned adapters for new subjects, actual supplied-view verification, portable
evidence and proof currentness, and optional required gating through ordinary
generation, context, preflight and dispatch. These are active construction
requirements; qualification requires the actual integrated path and independent
assessment, with existing semantic and operation authority retained separately.

## Deterministic support tools

The additional toolset supports F_P Executives, Workers and Reviewers under
STDO3.0-owned method contracts. It does not own another lifecycle, frame/packet
definition, applicability policy, result algebra or review/acceptance path.
The exact provisional contract derivation and the separate builder/consumer
basis roles are in the [source-owner map](fd-source-owner-map.md).

| Family | Category | Status and scope |
|---|---|---|
| [REQ-AC-FD-*](fd-support-tools.md) | Capability | Active: T-008's operative HOW and provisional public implementation; bounded implementation/review/technical integration complete, with qualification gaps retained. |
| [REQ-AC-FDV-*](fd-support-verification.md) | Verification | Active: qualification begun and partial for FDV-001/002; ordinary actor/variant gaps remain. FDV-003 accepted-result benefit is Deferred/unqualified. |

Active records operative work and begun qualification, not satisfaction or
acceptance. Earlier Deferred/design-pending wording is as-at T-007's historical
specification cut. [T-008](../../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation)
and its [handoff](../../.ai-workspace/qualification/t008/handoff-001/README.md)
record current evidence and remaining gaps without withdrawing the requested
Product outcome. These families apply to implementations declaring the
additional support capability and supplement, without rewriting, AC-R-001..015.
They do not retrospectively qualify existing scripts or frozen study artifacts.
The separate existing source-to-model F_P authoring capability remains intact.
Protocol, CLI/MCP, schemas, storage, providers and executors belong to tenant HOW.
