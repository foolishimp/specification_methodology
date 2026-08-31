# STDO Representation Product

Status: active source definition for release-matched `2.5.0`; bootstrap
`v0.1.0-rc.1` remains an accepted immutable historical Product.

## Product statement

STDO Representation 2.5.0 is the canonical `a_c.STDO` semantic compression of
exact Source STDO 2.5.0, the deterministic logical constraint index over that
compression, and concise native instructions for using both. An LLM reads
Source STDO, authors the compression, invokes the released Axiom Indexer
validator, repairs diagnostics, and uses the index to select reference frames
and prepare bounded work.

The Product adds no local semantic compiler, GTL engine, prompt orchestrator,
or model runtime. Exact Axiom Indexer supplies all deterministic mechanics. The
LLM remains the semantic harness and supplies every frame, label, text value,
and ordering choice.

## Product shape

```text
exact Source STDO 2.5.0
  -> a_c.STDO 2.5.0 Axiomatic Program (semantic compression)
  -> Logical Constraint Map (deterministic index over the program)
  -> native STDO Representation skill
  -> LLM-selected visible frame details and ordered sections
  -> Axiom Indexer pure join
  -> bounded Codex or Claude work with source re-entry
```

The program and map are derived from Source STDO. They do not replace or amend
it.

## Product terms

- **Represented STDO Version** is semantic version line `2.5.0`; its exact
  represented cut is immutable STDO `v2.5.0-rc.1`.
- **Source STDO** is that exact installed standards corpus and remains semantic
  authority.
- **Axiom Indexer Dependency** is exact accepted Axiom Indexer
  `v0.1.0-rc.1`, used without copying its Product members into this Product.
- **Shared-Source Release Profile** is this Product's local specialization of
  the installed Release Method's alternate-spelling permission. It owns only
  Git transport spelling and additional source-subtree reacquisition evidence.
- **`a_c.STDO` Axiomatic Program** is the canonical semantic compression
  selected for the exact represented cut. It contains URI-identified symbols,
  clauses, and residuals grounded in Source STDO.
- **Logical Constraint Map** is the deterministic Axiom Indexer index
  instantiated from the unchanged valid compression and invocation-local
  bindings. It adds no semantic interpretation.
- **Source Route** is a logical URI from a program item or residual to exact
  Source STDO. A physical path is an invocation binding, not semantic identity.
- **Reference Frame Selection** is the LLM's explicit choice of material frame
  URIs for one task. The Product does not claim automatic applicability.
- **Frame Details** are the visible URI, purpose, and source route for every
  selected frame.
- **Ordered Sections** are the exact caller-authored
  `{label: string, text: string}` rows passed to the Axiom Indexer joiner.
- **Native Skill** is the canonical concise instruction bundle discovered by
  Codex and Claude through their repository-native skill paths.
- **Target Instruction Reference** contains presentation guidance for one
  native environment or model family. It may change ordering or tool-call
  presentation, never Source STDO meaning.
- **Working Candidate** is an unpromoted program, map, skill, or request used
  for validation and dogfood.
- **Released Product** is the exact immutable member set accepted under the
  installed STDO Release Method. Repository proximity does not make other bytes
  Product members.

## Version relation

STDO Representation inherits the semantic version of the represented STDO
Product line:

```text
representation_version = represented_stdo_version
2.5.0 = semantic_version(stdo://releases/v2.5.0-rc.1/)
```

This equality identifies what is represented; it does not collapse release
cuts. STDO Representation has its own RC ordinal, member identities, review,
acceptance, and Product-owned shared-source Git refs. Axiom Indexer remains independently
versioned. A new represented STDO version requires a new Representation version;
an implementation-only Representation correction may publish a higher RC on
the same matched version line.

## Shared-source release profile

Installed STDO `v2.5.0-rc.1` permits a project to choose alternate Git spelling
when it preserves the mutable carrier, immutable cut, and mutable selector
distinctions. The Product owner selects this local profile:

```text
local_release_key = stdo_representation
RC branch = refs/heads/rc/stdo_representation/2.5.0
immutable RC = refs/tags/stdo_representation/v2.5.0-rc.<n>
version-line selector = refs/tags/stdo_representation/v2.5.0
release branch = refs/heads/release/stdo_representation/2.5.0
source_subtree_root = stdo_representation/
```

This profile is a Product-local axiom, not imported mutable Specification
Methodology law. Exact-cut identity remains the installed Release Method's
annotated tag object, peeled commit, repository tree, declared Product member
inventory, release claims, and predecessor relation. The source-subtree root
and tree are additional carrier and reacquisition evidence only. They never
become Product identity and never make sibling bytes Product members.

`a_c.STDO` does not claim a complete admitted `M_b`, the full
`I/O/E/C/L/X/V/T/J` population, a total semantic interpretation, or a lossless
replacement for the corpus.

## Exact dependency bases

### Source STDO

```text
release_uri:
  stdo://releases/v2.5.0-rc.1/
installed_manifest_sha256:
  3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338
standards_member_set_sha256:
  87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5
axiomatic_calculus_sha256:
  cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d
```

### Axiom Indexer

```text
release_tag: v0.1.0-rc.1
annotated_tag_object: e7afc8a42a7123aebe91cb7582cb037b1aae612d
peeled_commit: dc3e00998da36dae6ac7b76b340431a85096c83c
repository_tree: 8c9ad5f5e99a60c18fb8c1802471753afb226272
product_member_inventory_sha256:
  7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6
```

The dependency contributes URI resolution, released program validation,
logical-map instantiation, exact diagnostics, and ordered string joining. This
Product does not widen those claims.

## Axiom Indexer Product dependency relation

STDO Representation is the source Product and exact Axiom Indexer
`v0.1.0-rc.1` is its mechanical Product dependency. The relation is owned by
`urn:stdo-representation:authority:product-owner` and is limited to mechanical
validation, logical constraint index materialization, diagnostics, URI
resolution, and exact joining under the contracts below. It imports no Axiom
Indexer Product member and transfers no semantic, acceptance, publication, or
runtime authority.

The relation begins only when the target Product Definition resolves to
`urn:stdo:product-definition:axiom-indexer` and the exact release coordinates
in [Exact dependency bases](#exact-dependency-bases) verify. Its governing
contracts are [Imported validation boundary](requirements/REQ-P-CANDIDATE-VALIDATION.md#imported-validation-boundary)
and [Frame-use relation](requirements/REQ-P-NATIVE-FRAME-USE.md#frame-use-relation).
It is invalidated by target-definition, release, member-inventory, contract, or
result drift. Mutable sibling source never substitutes for the selected Install.

## Authoring and validation relation

```text
LLMAuthor(
  exact Source STDO,
  exact Axiom Indexer output contract,
  selected authoring frames
) -> a_c.STDO* | hold | residual

AxiomValidate(a_c.STDO*, invocation_bindings)
  -> valid + logical constraint map | diagnostics
```

The LLM owns interpretation and repair. The validator checks only its released
mechanical contract: shape, absolute and unique URIs, URI-set ordering,
reference closure, source grounding and resolution, residual re-entry, and
deterministic map identity. It never authors or repairs meaning.

An invocation-local Binding Set maps logical prefixes to physical installed
resources. Because those paths vary by installation, a concrete `bindings.json`
is runtime configuration or retained evidence, not a portable Product member.

Program or map validity does not prove semantic truth, completeness, fidelity,
unique interpretation, frame applicability, usefulness, or acceptance. An LLM
Reviewer compares material claims and omissions with exact Source STDO.

## Native frame-use relation

```text
LLMSelect(
  logical_constraint_map,
  task,
  role,
  evidence_boundary
) -> selected_frame_refs + ordered_sections | hold

AxiomJoin(ordered_sections) -> exact_request_bytes | refusal
```

The LLM selects the frames and writes all section bytes. Each request exposes:

- task and intended result;
- role and responsibility;
- authority and permitted-effect boundary;
- selected frame URI, purpose, and source route;
- material constraints, dependencies, evidence, and residuals;
- stop conditions; and
- return relation.

The joiner emits `label + "\n" + text` for each row, separates rows with two
newline characters, and adds no terminal newline. It does no selection,
resolution, interpretation, rewriting, budgeting, truncation, or invocation.

## Native agent projection

One canonical skill is carried at `skills/stdo-representation/`. Relative
repository symlinks expose it to Codex and Claude. The common skill owns the
semantic use sequence. `references/codex.md` and `references/claude.md` own only
target-specific instruction presentation. `agents/openai.yaml` supplies Codex
metadata.

The native skill instructs an LLM to:

1. verify the exact dependency and map identities;
2. load the logical map before broad Source STDO prose;
3. select and show material frame details;
4. re-enter exact source when required;
5. invoke Axiom Indexer validation or join directly;
6. preserve Executive, Worker, and Reviewer boundaries; and
7. return residuals and unresolved diagnostics honestly.

The skill is an instruction surface, not generated GTL, a hidden prompt
template, or a grant of external authority.

## Engagement roles

- **Executive** binds the task and evidence boundary, selects frames and target
  role, writes the ordered context, and disposes returned results.
- **Worker** performs one bounded construction, invokes declared validators,
  and returns its result, diagnostics, residuals, or stop to Executive.
- **Reviewer** evaluates an exact subject under an explicit evidence boundary,
  does not repair while retaining Reviewer status, and returns findings to
  Executive.

The native instructions preserve these relations. This release does not claim
that code validates role independence or computes a deterministic role packet.

## Product member set

The selected `2.5.0` Product contains exactly these eight repository entries:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/
  axiomatic-program.json
  logical-constraint-map.json
skills/stdo-representation/
  SKILL.md
  agents/openai.yaml
  references/codex.md
  references/claude.md
.agents/skills/stdo-representation
.claude/skills/stdo-representation
```

The last two entries are symlinks to `../../skills/stdo-representation`.
Member digests and the aggregate inventory identity are assigned only after the
exact bytes and symlink targets are frozen. No digest is inferred from an
intended path.

Source specification, README files, runtime bindings, validation reports,
dogfood results, tickets, decisions, release records, and historical prototypes
are authority, configuration, evidence, or history. They are not Product
members unless a later release record explicitly reprices the member set.

## Identity and provenance

- Source identity binds the exact installed STDO release and member set.
- Dependency identity binds the annotated Axiom Indexer tag object, peeled
  commit, tree, and released member inventory.
- Program identity is the released Axiom Indexer canonical-value digest of the
  exact Axiomatic Program.
- Map identity binds the exact program and resolved source evidence produced by
  the exact dependency.
- Skill identity binds its exact file inventory and target-specific references.
- Joined-request identity is the digest of exact output bytes for exact ordered
  input rows.

Provider process provenance is optional unless an observation claims one exact
invocation occurrence. It does not enter program, map, skill, or request
identity.

## Dogfood and proof boundary

Release evidence shall retain:

- exact program, invocation bindings, validation result, and logical map;
- representative URI, reference, source-route, and residual refusal cases;
- fresh Codex and Claude native discovery and map-first use;
- bounded Source STDO re-entry and material constraint recovery;
- Executive-selected visible frame details, ordered input rows, and exact
  joined request bytes;
- an independent source comparison naming omissions and regressions; and
- residual uncertainty about tasks and models not observed.

Green validation proves only its declared mechanical laws. Lower token count,
one favorable response, or artifact presence does not establish usefulness.

## Product disposition authority

`urn:stdo-representation:authority:product-owner` owns acceptance of the exact
project frame set, release scope, candidate disposition, and immutable RC
subject. Frame-set acceptance binds the exact declaration digest. Product
acceptance binds the annotated immutable RC tag object, peeled commit, tree,
eight-member inventory, and claim bytes. Proposal, validation, dogfood,
publication, or tag visibility performs neither decision.

## Authority boundary

- Source STDO owns STDO meaning and role definitions.
- Axiom Indexer owns its released program, validation, map, and join contracts.
- This Product owns the selected STDO semantic compression, its logical
  constraint index, native use instructions, member set, and dogfood claim.
- The LLM owns probabilistic interpretation, frame selection, content, and
  revision within its supplied authority.
- External owners retain operation, decision, review, acceptance, publication,
  and runtime authority.

Loading a map or skill grants none of those authorities.

## Non-goals and exclusions

The `2.5.0` Product excludes:

- the retained semantic-compilation and full-model prototypes;
- the retained GTL codecs, profiles, carrier artifacts, and frozen tenant;
- the JSON Schema placeholder tenant;
- a complete admitted `a_c` model or lossless semantic carrier;
- GTL overlays, GraphFunctions, automatic closure, or carrier admission;
- deterministic assignment packets, tokenizer budgets, renderers, or skill
  generators;
- ABG runtime, events, lineage, continuation, correction, or projection;
- semantic acceptance inferred from validation or use; and
- provider attestation as a prerequisite for ordinary use.

Those repository bytes remain historical evidence. They gain no current
Product status by remaining present.

## Product success

The Product succeeds when fresh Codex and Claude agents prefer the map-first
native workflow for real work, preserve material constraints and source
recovery, make selected frames inspectable, and use bounded source re-entry
without hidden orchestration. A material regression against direct Source STDO
prose holds release for the smallest owning reprice.

## Historical and current boundary

The accepted bootstrap Product is annotated immutable historical tag
`v0.1.0-rc.1`, tag object
`46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`, peeled commit
`b127ee9a0362f85d4875ae59664ecfcd13028d9c`, tree
`15f9beb360836386ce9607dd31e30d0c8b5cd830`, and eight-member inventory
`316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`.
The exact-cut review and Product-owner decision accept only release claims
`STDO-REP-0.1-C01` through `STDO-REP-0.1-C05` at their declared boundaries. It
is not retargeted or renamed.

The active source project is preparing STDO Representation `2.5.0` under its
Product-owned shared-source release profile. Until that exact cut is published, independently
qualified, and accepted, `2.5.0` is a candidate and the bootstrap cut remains
the latest accepted Representation Product.

No GTL composition, complete admitted `M_b`, provider attestation, automatic
frame selection, ABG runtime, or semantic-completeness claim is made.
