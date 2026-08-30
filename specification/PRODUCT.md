# STDO Representation Product

Status: active source definition; thin `0.1.0` Product selected; no immutable
STDO Representation RC published or accepted.

## Product statement

STDO Representation is an exact Source STDO authoring map plus concise native
instructions for using it. An LLM reads Source STDO, authors `a_c.STDO`, invokes
the released Axiom Indexer validator, repairs diagnostics, and uses the resulting
logical constraint map to select reference frames and prepare bounded work.

The Product adds no local semantic compiler, GTL engine, prompt orchestrator,
or model runtime. Exact Axiom Indexer supplies all deterministic mechanics. The
LLM remains the semantic harness and supplies every frame, label, text value,
and ordering choice.

## Product shape

```text
exact Source STDO
  -> a_c.STDO Axiomatic Program
  -> logical constraint map
  -> native STDO Representation skill
  -> LLM-selected visible frame details and ordered sections
  -> Axiom Indexer pure join
  -> bounded Codex or Claude work with source re-entry
```

The program and map are derived from Source STDO. They do not replace or amend
it.

## Product terms

- **Source STDO** is the exact installed STDO `v2.5.0-rc.1` standards corpus.
- **Axiom Indexer Dependency** is exact accepted Axiom Indexer
  `v0.1.0-rc.1`, used without copying its Product members into this Product.
- **`a_c.STDO` Axiomatic Program** is the STDO-specific Axiom Indexer
  `a_c.text` authoring surface. It contains URI-identified symbols, clauses,
  and residuals grounded in Source STDO.
- **Logical Constraint Map** is the deterministic Axiom Indexer view
  instantiated from the unchanged valid program and invocation-local bindings.
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

The selected `0.1.0` Product contains exactly these eight repository entries:

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
- This Product owns the selected STDO authoring map, native use instructions,
  member set, and dogfood claim.
- The LLM owns probabilistic interpretation, frame selection, content, and
  revision within its supplied authority.
- External owners retain operation, decision, review, acceptance, publication,
  and runtime authority.

Loading a map or skill grants none of those authorities.

## Non-goals and exclusions

The `0.1.0` Product excludes:

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

## Current boundary

The exact Source STDO and accepted Axiom Indexer dependency exist. The thin
Product member bytes and digests are frozen in `releases/v0.1.0.md`. Project
frame basis revision 11 is accepted by exact digest and bound into the
operative Product Definition. Dogfood and qualification remain evidence over a
candidate until immutable RC publication and exact-cut acceptance close.

No STDO Representation RC, released `a_c.STDO`, GTL composition, or accepted
Product is currently claimed.
