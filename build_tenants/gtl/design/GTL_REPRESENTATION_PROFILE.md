# GTL Representation Profile — STDO.gtl 0.8.0

Status: superseded pre-`a_c` design candidate; never accepted; retained as
design history

The active `a_c.STDO.GTL` mapping candidate is
[`GTL_AXIOM_INDEX_PROFILE.json`](GTL_AXIOM_INDEX_PROFILE.json). This document
preserves the prior five-family `P_B` mapping and its RC3 coordinates; it is not
an input to current construction.

Profile identity:
`urn:stdo-representation:gtl-profile:stdo-gtl:0.8.0`

Build-tenant identity: `urn:stdo-representation:build-tenant:gtl`

## Purpose

Define `stdo.gtl`, the canonical frozen-GTL encoding of the STDO Programmatic
Semantic Index for an external ODD `F_P[v_reason]` LLM traversal over a separately
supplied workspace. The index encodes the Source STDO Symbolic Axiomatic Program
as compact passive graph-and-constraint declarations while preserving exact
identity, basis, authority, bounded-context, scope, source-route, and refusal
coordinates.

`F_H[v_select]` selects and accepts the exact carrier-neutral algebra. Domain
HOW constructs, serializes, and measures exact bytes.
`F_D[v_carrier_admission]` evaluates the declared structural and identity
properties of those results and issues a separate admission judgment over their
unchanged identity and bytes. It does not transform, rewrite, reissue, or rename
the carrier. `F_P[v_reason]` consumes the index only when that judgment is
`admitted`. These are functor applications to exact declared traversals, not
names for the domain operations themselves.

This profile receives only the carrier-neutral `P_B` and Semantic Selection
Ledger already accepted under `F_H[v_select]`. It is not an input to
`F_P[v_compile]` and cannot cause the compiler to omit or alter Source STDO
meaning for GTL representability.
The payload is not a deterministic workspace assessor, frozen-GTL `GtlProgram`,
callable GTL workflow, vector database, HoG plan, ABG runtime, or qualification
bundle.

Acceptance binds this file's exact bytes and SHA-256. Any later change creates a
new profile candidate and does not inherit an earlier acceptance.

## Exact bases

### Source STDO

- installed URI: `stdo://releases/v2.4.3-rc.3/`
- installed-manifest SHA-256:
  `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`
- release commit: `eb87a20247beeb93de394523ebdf8faecfd71949`
- standards member-set SHA-256:
  `127a6fb213eb5e12bcf6180cb73016a003ccfda80651b476055f19a22ca10275`
- standards inventory: 47 regular files in installed-manifest order

### Frozen GTL

- repository: `https://github.com/foolishimp/abiogenesis.git`
- commit SHA-1: `8d7f965a3fae7d1acea6a9db298798480fd4cc2f`
- authority root: `specification/requirements/gtl/`
- authority-tree SHA-1: `21a44b1941a1055d6abd973937e65b83e359de1b`
- authority inventory: 33 regular files
- TypeScript tenant package: `@abiogenesis/typescript-tenant@5.0.0-dev.286`

The carrier-basis coordinate contains exactly:

```json
{
  "authority_inventory_count": 33,
  "authority_root": "specification/requirements/gtl/",
  "authority_tree_sha1": "21a44b1941a1055d6abd973937e65b83e359de1b",
  "commit_sha1": "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
  "repository": "https://github.com/foolishimp/abiogenesis.git"
}
```

Its RFC 8785 JCS/SHA-256 identity is:

```text
urn:stdo-representation:carrier-basis:gtl:sha256:
  b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703
```

Relevant immutable navigation routes are the
[language boundary](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-LANGUAGE.md),
[contract-law API](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-CONTRACT-LAW-API.md),
[Rule boundary](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-RULE.md), and
[Module boundary](https://github.com/foolishimp/abiogenesis/blob/8d7f965a3fae7d1acea6a9db298798480fd4cc2f/specification/requirements/gtl/REQ-L-GTL3-MODULE.md).
The complete 33-member authority tree remains operative.

## Frozen carrier contract

The serialized root is the frozen TypeScript `ModulePublication`, not the
legacy `Module { graphs[] }` shape:

```text
ModulePublication {
  kind: "module_publication"
  moduleRef: string
  moduleVersion: "5.0.0"
  owningProductId: string
  artifactDigest: Sha256
  productContentDigest: Sha256
  productManifestDigest: Sha256
  descriptorRef: string
  contributionManifestRef: string
  productSemanticsBinding: ProductSemanticsBinding
  contracts: [ContractDeclaration]
  evaluators: []
  rules: [RuleDeclaration]
  implementationBindings: []
  closureContracts: []
  programs: []
  graphFunctions: []
  contributions: [CatalogContribution]
}
```

The one Contract declares
`urn:stdo-representation:gtl-contract:programmatic-semantic-index:1` as an input
value of kind `stdo_programmatic_semantic_index_v1`. The one Rule has:

```text
name   = "stdo.programmatic-semantic-index.v1"
kind   = "stdo.programmatic_semantic_index"
config = CompactSemanticIndexConfig
tags   = []
```

The one CatalogContribution is a non-callable `node_type` contribution pointing
to that Contract and has empty Program membership. At least one contribution is
required by the frozen GTL validator. No GTL Node is claimed: frozen
`GtlNode` exists only inside a callable GraphFunction template, which this
Product excludes.

The empty callable, evaluator, implementation, closure, Program, and
GraphFunction inventories are positive Product-boundary claims. The external
host owns the complete ODD `F_P[v_reason]` traversal contract.

## Publication owner and cycle boundary

`ModulePublication.owningProductId`, its three Product digests, descriptor,
contribution manifest, package coordinates, and Product-semantics binding name
one immutable **GTL Tenant Toolchain Product** that publishes this carrier.
They do not name the later STDO Programmatic Semantic Index Product.

The toolchain Product basis shall be supplied as one verified immutable
`PublisherArtifactBasis`:

```text
PublisherArtifactBasis = {
  owning_product_id: absolute URI,
  artifact_digest: Sha256,
  product_content_digest: Sha256,
  product_manifest_digest: Sha256,
  descriptor_ref: absolute URI,
  contribution_manifest_ref: absolute URI,
  package_name: non-empty string,
  package_version: non-empty string,
  module_path: non-empty string,
  named_symbol: non-empty string
}
```

The named symbol is the toolchain's exported
`STDO_GTL_PRODUCT_SEMANTICS`. The output bytes incorporate the exact publisher
basis. Consequently, the later content-first STDO Programmatic Semantic Index
Product
identity covers it transitively without embedding its own final identity and
creating a cycle. A source-project path, mutable package, placeholder digest,
or the ABIogenesis Product identity cannot substitute for this publisher basis.

The evidence bundle carries the exact publisher artifact bytes and one
canonical publisher manifest with repository commit/tree, normalized
path-sorted content inventory, package and semantics-binding coordinates, and
the artifact/content digests. `product_content_digest` is SHA-256 over each
`path + NUL + sha256 + LF` inventory row. `product_manifest_digest` is SHA-256
of the exact RFC 8785 JCS manifest bytes, `artifact_digest` is SHA-256 of the
exact supplied artifact bytes, and:

```text
owning_product_id =
  "urn:stdo-representation:gtl-toolchain-product:sha256:" +
  hex(product_manifest_digest)
```

All four values are independently reproduced before construction. The
publisher manifest is not embedded in routine LLM context.

This profile claims frozen GTL publication validation, not ABIogenesis Product
catalog readiness. Catalog installation would additionally require an exact
installed Product descriptor and contribution manifest under that Product's
own admission process.

## Direct algebra mapping

The common programmatic index remains `P_B = (B, I_B, V_B, E_B, C_B)`.
Frozen GTL's open, passive Rule configuration carries one reversible compact
encoding:

| Common element | Carrier realization |
|---|---|
| `B` and pre-content Product coordinates | `config.m` metadata tuple |
| `I_B` | `config.i`, the sorted full-identity table |
| non-identity strings | `config.s`, a sorted, duplicate-free string table |
| `V_B` | `config.a`, atom tuples using identity and string indexes |
| `E_B` | `config.e`, typed semantic-edge tuples; never GTL GraphVector topology |
| `C_B` | `config.c`, passive constraint tuples; never GTL Evaluators |
| tuple and enumeration meaning | `config.l`, one embedded legend |

Encoding changes only representation. Decoding reproduces every exact common
record and its identity. There is no shared carrier-independent serialized IR:
the build plan and tuple encoding are GTL-tenant HOW, while the common algebra
remains constitutional WHAT.

## CompactSemanticIndexConfig

The Rule configuration contains exactly:

```text
CompactSemanticIndexConfig = {
  k: "stdo.programmatic_semantic_index",
  v: 1,
  m: MetadataTuple,
  l: Legend,
  s: string[],
  i: Identity[],
  a: AtomTuple[],
  e: EdgeTuple[],
  c: ConstraintTuple[]
}
```

`m` has these positional fields:

```text
[source_stdo_uri,
 source_stdo_manifest_sha256,
 standards_member_set_sha256,
 what_member_set_identity,
 build_tenant_identity,
 carrier_basis_identity,
 representation_profile_identity,
 representation_profile_sha256,
 project_reference_frame_basis_identity,
 project_reference_frame_basis_sha256,
 semantic_selection_ledger_identity,
 semantic_selection_ledger_sha256]
```

`i` contains every member of `I_B`, once, sorted by ascending unsigned UTF-16
code units. Every index reference is a non-negative index into `i`. `s`
contains every other repeated scalar used by an address, locator, label, or
statement, once under the same ordering. Every string-table reference is a
non-negative index into `s`.

The legend uses these tuple keys:

```text
z = [source_key, term, context, authority, scope]
o = [member_path, member_sha256, fragment]
a = [id, class, label, address, locators]
e = [id, address, source, relation, target, context, owner, scope,
     cross_context, locators]
c = [id, address, class, statement, applies_to, context, owner, scope,
     latitude, locators]
x = [class, source_context, target_context, preserved, changed, refusals,
     inverse, invalidations]
y = [functor_kind, decision_owner, re_entry]
```

The legend also embeds the ordered `ak`, `ck`, `xk`, and `fk` code tables copied
from the common AtomClass, ConstraintClass, CrossContext classification, and
declared-latitude function vocabularies. A class or function code is its
zero-based index in the applicable table. Nullable fields remain JSON `null`.

`SemanticAddress.selected_basis` is restored from the first two `m` fields for
every decoded record. `SourceLocator.basis_uri` is restored from the first `m`
field. No semantic field is dropped, guessed from a label, or inferred through
GTL nominal equality. The embedded legend is ordinary Product data and does not
extend GTL's ontology or validator.

## Canonical order and bytes

Before carrier construction:

- identity and string tables sort by unsigned UTF-16 code units;
- atom, edge, and constraint rows sort by their full record identities;
- every reference-set and locator set satisfies the common algebra order;
- exact Source STDO ordered relations retain ledger-declared source order; and
- the domain validator rejects duplicate, dangling, wrong-kind, cross-basis,
  out-of-range, missing, unknown, or non-reversible values.

The frozen GTL typed constructor canonicalizes `ModulePublication`; raw
admission canonicalizes the equivalent serialized value. The two canonical
values must be byte-identical before publication validation. The artifact is:

```text
canonical_index_bytes = RFC8785_JCS(raw_admitted_ModulePublication) + LF
program_content_identity = "sha256:" + sha256(canonical_index_bytes)
```

The final LF is byte `0x0a` and participates in the content identity of this
index encoding. The `program_content_identity` field names the encoded Source
STDO Symbolic Axiomatic Program; it is not a frozen-GTL `GtlProgram` identity.
A BOM, CR, leading byte, extra trailing byte, duplicate object name,
non-canonical escape, unsafe number, or alternate order refuses admission.
Frozen GTL's raw-admission subject digest addresses the canonical JSON value
without the framing LF; the build receipt records both identities explicitly.

The final STDO Programmatic Semantic Index Product coordinate and identity are
issued only after these bytes exist, under `PRODUCT.md#product-identity`.
Neither final
identity is embedded back into the carrier.

## Mandatory admission chain

One successful construction executes, in order:

```text
exact accepted build plan and semantic-selection evidence
  -> Product-owned typed TypeScript declaration
  -> frozen GTL modulePublication constructor
  -> exact canonical serialization
  -> frozen GTL rawAdmitValue(module_publication)
  -> frozen GTL rawAdmitValue(catalog_contribution)
  -> frozen GTL validatePublication
  -> domain decode/reference/identity checks
  -> canonical stdo.gtl bytes and receipt
```

The frozen validator is the only GTL validator. Tenant domain checks operate
after GTL admission and decide only this Product's compact record contract,
common identity law, basis equality, and reference-kind law. They neither
replace nor fork GTL validation.

The replayable conformance probe reacquires the exact frozen commit, verifies
the 33-member authority tree, builds its TypeScript package, compiles this
tenant against its published declarations, then runs positive and negative
admission tests. A locally compatible package, hand-written interface, or
successful JSON parse is insufficient.

## Construction inputs and authority gates

Production construction consumes:

1. exact Source STDO release and installed manifest;
2. exact current WHAT member-set identity;
3. this profile's accepted identity and SHA-256;
4. an accepted project Reference-Frame Basis;
5. the immutable Semantic Compilation Candidate and eligible Candidate Structure
   Result bound by an exact accepted Semantic Selection Ledger whose
   retained-reference union equals `I_B` and whose
   `representation_records_sha256` reproduces from the complete ID-sorted
   canonical build-plan record array;
6. the GTL Tenant Toolchain Product's verified publisher-artifact basis; and
7. tenant-owned build-plan records whose identities, locators, and reference
   kinds reproduce under the common law.

The CLI admits one JSON `GtlBuildPlan` containing exactly:

```text
GtlBuildPlan = {
  kind: "stdo-representation.gtl-build-plan",
  schema_version: 1,
  source_stdo: B,
  what_member_set_identity: Sha256,
  representation_profile_identity: this profile identity,
  representation_profile_sha256: Sha256,
  frame_basis_identity: absolute URI,
  frame_basis_sha256: Sha256,
  frame_admitting_authority_refs: URI-reference[],
  semantic_compilation_candidate_identity:
    SemanticCompilationCandidateIdentity,
  semantic_compilation_candidate_sha256: Sha256,
  candidate_structure_result_identity: CandidateStructureResultIdentity,
  candidate_structure_result_sha256: Sha256,
  semantic_selection_ledger_identity: SelectionLedgerIdentity,
  semantic_selection_ledger_sha256: Sha256,
  profile_acceptance_identity: AuthorityAcceptanceIdentity,
  frame_basis_acceptance_identity: AuthorityAcceptanceIdentity,
  selection_acceptance_identity: AuthorityAcceptanceIdentity,
  publisher: PublisherArtifactBasis,
  records: non-empty ProgramRecord[]
}
```

`frame_admitting_authority_refs` equals the complete applicable Product
Definition authority set byte-for-byte and in canonical order. The evidence
bundle supplies the exact installed manifest, profile and frame-basis bytes,
Semantic Compilation Candidate, Candidate Structure Result, canonical ledger,
three canonical acceptance records, canonical publisher manifest, and
publisher artifact bytes. Candidate and structure-result coordinates equal
those bound by the ledger. Digests or identities in the plan are locators to
those supplied bytes, not trusted assertions.

Each acceptance is an external, canonical `AuthorityAcceptanceRecord` binding
the unchanged subject, exact human or bounded-proxy authority and grant,
evidence, basis, decision, and time. Structural tooling may verify those record
relations; it cannot invent the actor, grant, or semantic decision.

The Semantic Selection Ledger's evaluated population equals all 47 installed
standards members in manifest order. Every retained atom, edge, and constraint
has exactly one retained selection owner, and its record-set digest binds every
field of those represented records rather than only their content-addressed
semantic identities. Omission and uncertainty remain external qualification
evidence and are not paid as routine LLM-context cost.

## ODD F_P consumption

The ordinary consumer relation remains:

```text
F_P[v_reason](stdo.gtl, workspace_input, intent, frame, capability_budget)
  -> probabilistic reasoning | hold | gap | refusal
```

The host also supplies the tuple legend primer when the model cannot reliably
recover it from `config.l`. The carrier contains no workspace bytes, model
configuration, prompt wrapper, response, usage price, transcript, GraphVector,
event, continuation, or runtime truth. Consumption grants no semantic,
decision, operation, acceptance, publication, release, or closure authority.

## Executive context projections

The complete `stdo.gtl` is the immutable parent Product. An authorized
Executive Context Assignment selects seed identities under
`REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md`. The tenant computes the exact least
closure in decoded common-record space and re-encodes only those rows, with
fresh minimal `i` and `s` tables and the unchanged basis/profile coordinates.

A projected carrier remains a frozen-GTL-admitted passive
`ModulePublication`, but it is a Context Packet artifact, not a new Product or
publication authority. Its external Context Projection Manifest binds parent
Product/content identity, assignment, included and omitted identity sets,
projected carrier digest, measurement, residuals, and source re-entry routes.
Repeating an assignment either reproduces the same bytes or returns the
declared hold. A token budget never removes a mandatory closure member.

## Measurements and observations

Qualification records exact byte count plus tokenizer identity, tokenizer
version, token count, price basis, and comparison-population identity for:

- all 47 raw Source STDO standards members;
- the released `stdo_compressed.md` prompt projection; and
- complete and role-projected `stdo.gtl` carriers.

Only like-for-like declared payloads support a reduction claim. Representative
and adversarial `F_P[v_reason]` observations may characterize usefulness, navigation,
holds, and failures; repeated observations do not become deterministic semantic
proof.

## Refusals

Construction or admission refuses at least:

- unverified, mutable, cross-cut, or mismatched Source STDO or GTL basis;
- an unaccepted profile, frame basis, or Semantic Selection Ledger;
- an unverified or placeholder publisher-artifact basis;
- a missing, reordered, duplicate, or digest-mismatched 47-member ledger
  population;
- a retained-reference union unequal to `I_B`;
- an unreproducible identity or generated source-key preimage;
- duplicate, dangling, wrong-kind, unlawful-null, cross-basis, or out-of-range
  reference;
- a non-reversible tuple or unknown legend, table, field, or code;
- semantic equivalence inferred only from spelling or graph shape;
- a semantic edge encoded as GTL GraphVector topology;
- callable Program, GraphFunction, evaluator, implementation, closure, HoG,
  ABG, event, continuation, or runtime-truth content;
- disagreement between typed declaration and raw admission;
- a second GTL parser, validator, or lowering surface; and
- non-canonical bytes or an unbound token/usefulness claim.

## Acceptance gate

This carrier grants no acceptance to itself. Without an external accepted
`AuthorityAcceptanceRecord`, it remains a proposal. Profile acceptance
authorizes only construction against these unchanged bytes and exact bases. It
does not pre-accept a Semantic Selection Ledger, toolchain Product, generated
index, projection, measurement, probabilistic observation, Product release,
or tag.
