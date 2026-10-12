# Declared Trial Inputs: STDO 2.4.1 Amendment Qualification

- prepared_at: 2026-08-17T03:40:22Z
- input_owner: STDO 2.4.1 authoring Worker
- input_status: declared_inputs_without_reference_outcomes
- predecessor: `v2.4.0` at
  `e05984c4f3b75525e6d962f6b9d72bbedd8e271a`
- candidate_standards_aggregate:
  `0f46a3d583f321da0445331566ef878e11e19e16e71c54fb9a8e66c5fff4ce91`
- candidate_product_sha256:
  `aa1eb79808be2b82acc59d58b27965dbbce3d14135c11084461b7191493cf066`
- candidate_release_note_sha256:
  `7756e23f34ccd06280549ebb81fb1cdd0a8b77da291516ddd46f16a511ca27ea`
- intended_consumer: fresh capable constructor distinct from the authoring
  Worker
- prohibited_use: expected-output, answer-key, ABIogenesis-local law, or prior
  review-verdict substitution

## Input Boundary

These inputs exercise only the two `2.4.1` amendment populations:

1. Design Module Method `STDO-UP-023` capability and foundation selection; and
2. the optional STDO baseline's claim-relative Product-testing configuration.

They provide a synthetic Product, actors, evidence, candidate observations,
testing claims, paths, mutations, and evaluation requests. They do not provide
the constructor's foundation selection, testing-frame set, result algebra,
coverage verdict, counterexample localization, or release decision.

The constructor derives those outputs from the candidate
`DESIGN_MODULE_METHOD.md`, `STDO_REFERENCE_FRAME_BASELINE.md`, and their cited
governing basis. It records ambiguity, refusal, or residual uncertainty rather
than asking the authoring Worker for an intended answer. The constructor does
not edit the candidate or authorize release.

## Synthetic Product

### Identity And Outcome

- Product: `ATLAS-7`, a runnable command-line Product that turns admitted route
  declarations into one signed route-atlas bundle.
- exact runnable subject: `ATLAS-7@install-44`;
- Product checkpoint: `AT-B0`;
- supported user: `route-editor`;
- supported entry: `atlas build routes.yaml --output atlas.bundle`;
- Product outcome: a route editor can obtain the exact admitted atlas bundle,
  or a typed refusal, through the supported entry;
- ordinary path:

```text
CLI request
  -> route declaration admission
  -> route semantic validation
  -> deterministic graph traversal
  -> canonical bundle construction
  -> signature validation
  -> publication-store admission
  -> user-visible receipt
```

### Existing Owners

| Owner | Existing authority |
|---|---|
| `AT-PRODUCT` | owns Product outcome, supported entry, bundle membership, and acceptance conditions |
| `AT-ROUTE` | owns route identity, edge meaning, admissibility, and route-semantic refusal |
| `AT-BUILD` | owns deterministic traversal and canonical bundle construction from admitted route carriers |
| `AT-SECURITY` | owns signing-policy meaning and signature validation |
| `AT-STORE` | owns publication-store admission and durable receipt projection |
| `AT-DESIGN` | owns the exact design-basis foundation tradeoff and its declared priorities and risk tolerances |
| `AT-RELEASE` | owns Product/release disposition and publication |

No library, source file, test, harness, actor, or frame gains authority from its
name, implementation language, provenance, or reuse status.

### Material Authority-Bearing Role

Accepted design assigns relation `ROUTE-VALIDATE-R3` this exact tuple:

- owner: `AT-ROUTE`;
- role kind: semantic validator;
- subject: admitted `RouteSet@AT-B0`;
- scope: route identity, edge endpoint existence, and declared direction;
- basis: `AT-PRODUCT-7 + ROUTE-SCHEMA-3 + AT-B0`;
- lifecycle: validate after route admission and before traversal;
- refusals: missing endpoint, duplicate route identity, unsupported direction;
  and
- excluded meaning: traversal order, signing policy, store admission, release
  disposition, and Product acceptance.

An external foundation may be assigned to realize this role. The relation and
owner tuple above do not change merely because the realization is reused code.

## Foundation-Selection Inputs

### Required Capability

The design needs deterministic traversal over an immutable directed multigraph,
including stable successor ordering, cycle detection, bounded path enumeration,
and explicit failure values. The Product-labelled working phrase is
`ATLAS route graph engine in route_core.ts`. The constructor must derive the
capability statement used for comparison.

### Candidate Categories And Discovery Record At `DISC-7`

Discovery cutoff is `2026-08-17T02:00:00Z`; relevant versions are fixed below.

| Category | Sources or collections searched | Applicability | Material exclusions | Predecessor/incumbent status | Discovered candidates | Residual unknowns |
|---|---|---|---|---|---|---|
| admitted project | accepted dependency register and current source inventory | candidate must accept immutable carriers and deterministic ordering | mutable registry-backed engines | incumbent `LOCAL-G1` is local code, not an admitted foundation | `LOCAL-G1` | no other admitted foundation recorded at cutoff |
| language/runtime/standard | runtime `R20` standard-library index | graph mechanics available without hidden global state | non-deterministic iteration surfaces | no predecessor | `NATIVE-G2` composition | performance above 5 million edges not measured; Product maximum is 100,000 |
| immutable lineage | `ATLAS-6` release manifest and source archive | exact Apache-2.0 lineage and current schema compatibility required | unversioned development snapshots | `LINEAGE-G3` realized the predecessor | `LINEAGE-G3` | predecessor has no parallel traversal evidence |
| maintained external | approved registry index, security advisory feed, license index, and maintainer release pages | Apache-2.0-compatible, maintained in last 18 months, immutable-carrier API, supported runtime | copyleft license, native binary requirement, network service dependency | none incumbent | `FOUNDATION-G4`, `FOUNDATION-G5` | one registry with no deterministic-order metadata is recorded as excluded pending evidence |
| bounded local | accepted design plus bounded implementation estimate | no new semantic owner and deletion plan required | open-ended framework construction | incumbent `LOCAL-G1` | `LOCAL-G1-R2` | concurrency proof estimate is uncertain |

### Material Candidate Evidence At `EVID-7`

| Dimension | `NATIVE-G2` | `LINEAGE-G3` | `FOUNDATION-G4` | `FOUNDATION-G5` | `LOCAL-G1-R2` |
|---|---|---|---|---|---|
| functional/constructability fit | requires 180 lines of lawful composition; all required operations constructible | lacks bounded path enumeration | exact fit through immutable API | exact fit except stable successor ordering requires a 25-line adapter | exact fit claimed by design |
| authority posture | mechanics only unless explicitly assigned a role | predecessor mixed validation and traversal but tuple can be separated | mechanics plus optional explicitly assigned validator role | mechanics only | local implementation currently mixes `AT-ROUTE` refusal with traversal |
| integration/migration/deletion | moderate integration; predecessor deletion complete | lowest migration, but missing operation | low integration; full predecessor deletion path recorded | moderate adapter and migration | highest new-code and deletion cost |
| license/security/supply chain | runtime license; runtime security process | Apache-2.0; no current advisory | Apache-2.0; signed release; no current advisory | Apache-2.0; signed release; one resolved advisory | local license; internal review only |
| runtime/operations | 42 ms at Product maximum | not measured at Product maximum | 34 ms at Product maximum | 29 ms at Product maximum | 61 ms at Product maximum |
| determinism/failure/recovery | deterministic with explicit local error algebra | cycle failure aborts without typed locus | deterministic with typed cycle and bound failures | deterministic after adapter; adapter failure proof present | deterministic happy path; recovery evidence unknown |
| proof/assurance | property proof required for composition | missing parallel and path-bound proof | upstream property suite plus local role/basis proof | upstream suite plus adapter-order proof | complete new proof population required |
| exit/reversibility | runtime-coupled but no external package | lineage-owned | interface-local replacement; deletion recipe present | adapter must be deleted on exit | all code locally removable |

`FOUNDATION-G4` and `FOUNDATION-G5` remain materially different: G4 has lower
integration/proof burden and G5 has lower measured runtime. `AT-DESIGN` declares
these exact priorities for `ATLAS-7@AT-B0`:

1. authority and Product-contract fit are hard constraints;
2. deterministic failure and recovery evidence outrank runtime below the
   accepted 75 ms ceiling;
3. proof, integration, and deletion burden outrank feature breadth; and
4. supply-chain evidence must be current at the discovery cutoff.

No priority is declared between two candidates that remain equal under those
conditions.

### Foundation-Selection Cases

- `F-01`: determine whether the required traversal capability triggers
  `STDO-UP-023`, state its normalized capability, and separate mechanics from
  `ROUTE-VALIDATE-R3`.
- `F-02`: apply proportionality to a private helper that joins two already
  admitted display strings and cannot affect authority, Product behavior,
  lifecycle cost, or accepted design.
- `F-03`: evaluate the bounded discovery record at `DISC-7`, including the
  excluded registry entry and each residual unknown.
- `F-04`: remove the maintained-external row without `not_applicable`, a named
  gap, or reason, then attempt selection.
- `F-05`: compare all lawful compositions at `EVID-7`; identify eliminations,
  dominance relations that are actually supported, material unknowns, and the
  undominated frontier.
- `F-06`: use the declared `AT-DESIGN` priorities and risk tolerances to
  disposition the frontier. Repeat with those priorities withheld.
- `F-07`: change `FOUNDATION-G4` to GPL-only while Product requires an
  Apache-2.0-compatible distribution.
- `F-08`: assign `FOUNDATION-G4` to realize `ROUTE-VALIDATE-R3` with the exact
  declared tuple and direct owner-issued inputs and refusals.
- `F-09`: change that assignment so the foundation selects signing policy,
  admits publication, and remints validation owner as `FOUNDATION-G4`.
- `F-10`: after selection, discover `FOUNDATION-G6`, which meets the recorded
  applicability criteria and is no worse on every material dimension than the
  selected composition while strictly reducing proof and exit cost.
- `F-11`: during integration, discover a material generic canonical-ordering
  subproblem that was absent from every evaluated composition.
- `F-12`: attempt to select `LINEAGE-G3` solely because it is the predecessor,
  and separately attempt to select `LOCAL-G1-R2` solely because it is local.

## Claim-Relative Product-Testing Inputs

### Claims And Evidence

| Claim | Evidence input |
|---|---|
| `CL-U1` | a `route-editor` invokes the supported CLI on `ATLAS-7@install-44` and receives the exact admitted bundle and durable receipt |
| `CL-U2` | the same scenario replaces the Product-claimed live signing service with `SIGN-FAKE`, a deterministic harness substitute |
| `CL-E1` | the installed Product executes every ordinary-path owner edge from CLI through store receipt with exact identities and owner-issued projections |
| `CL-E2` | obsolete `legacy-build` bypasses `AT-BUILD`, produces equal bundle bytes, and remains reachable from the supported CLI under one configuration |
| `CL-I1` | the `AT-BUILD -> AT-SECURITY` boundary is exercised across graph kind, cycle state, signature policy, and retry state |
| `CL-I2` | a substitute signer is used and the result is claimed only for request/response serialization, not live signing-policy conformance |
| `CL-N1` | coded module `receipt_format` owns a public formatting contract with two branches and no internal combinatorial complexity |
| `CL-N2` | coded module `route_traversal` owns cycle, ordering, path-bound, and refusal laws with a large combinatorial population |

The declared interaction population for `CL-I1` is:

- graph kind: acyclic, single cycle, disconnected;
- cycle state: absent, admitted refusal, malformed evidence;
- signature policy: current, stale;
- retry state: first attempt, recovered retry, exhausted;
- required strength: all pairs plus the declared three-way interaction
  `(single cycle, stale policy, recovered retry)`; and
- residual: four-way interactions not exercised unless another law or history
  makes one material.

### Path And Closure Evidence

- `PATH-POS`: one exact runnable witness traverses the complete ordinary path
  and records owner-issued receipts at each material edge.
- `PATH-NEG`: mutations separately prove that the obsolete CLI route,
  `legacy-build`, a fallback signer, and direct store injection are unreachable
  or fail closed in the production closure.
- `SRC-OLD`: one obsolete proof fixture still imports `legacy-build` and can
  manufacture an aggregate green result without executing the installed
  Product.
- `TEST-SEAM`: one declared in-memory store seam exists only in an integration
  fixture, is excluded from Product distribution, and is never used as
  ordinary-path or installed-Product evidence.
- `MUT-1`: a negative test corrupts a copied bundle in an isolated temporary
  subject and retains the original exact install identity.
- `MUT-2`: another negative test edits the only installed bundle in place and
  continues claiming evidence about the pre-mutation install identity without
  restoration or revalidation.

### Assurance Acquisition Inputs

`AT-STORE` exports `projectAdmittedReceipt(store, prefix)` and `AT-BUILD`
exports `projectBuildLineage(candidate)`. Both return owner-issued typed
projections on an exact basis.

- `AQ-1`: assurance acquires those projections and applies an independently
  Product-law-derived oracle for equality, completeness, and path membership.
- `AQ-2`: a Governor-like proof script ignores both projections, reads raw log
  lines, reconstructs current store prefix and build meaning, and grades its
  own reconstruction.
- `AQ-3`: the Product claim requires signing-policy status, but no owner-issued
  observable seam exists for that status.

### Causal Counterexample Inputs

The declared causal graph uses owner edges, not log order.

- `CF-1`: exact evidence establishes one malformed route-admission carrier as
  the sole causally minimal violated relation; every later failure derives from
  it.
- `CF-2`: publication required both an invalid signature acceptance and a
  wrong-store admission. The two violations are incomparable in causal order,
  both are established, and both are necessary to explain the observed
  published subject.
- `CF-3`: the receipt is absent; evidence supports either store refusal before
  admission or transport loss after admission, but cannot establish which
  frontier occurred.
- `CF-4`: only a user-visible timeout is observed; no bounded owner-edge
  evidence exists.

### Testing-Frame Cases

- `T-01`: derive the testing frame declaration for each `CL-*` claim from its
  subject, path, population, oracle, evidence, and falsification condition,
  without treating the labels as authority.
- `T-02`: determine what `CL-U1` and `CL-U2` can each prove and whether either
  can close a claim that live signing works.
- `T-03`: evaluate `CL-E1` and `CL-E2`, including equal output through the
  obsolete path.
- `T-04`: evaluate the claim altitude of `CL-I1` and `CL-I2`, the declared
  interaction strength, and the residual population.
- `T-05`: determine the required unit-proof lane for `CL-N1` and `CL-N2` and
  what internal combinatorial complexity changes.
- `T-06`: bind the distinct UAT, E2E, integration, and unit results through a
  declared conjunction for Product/release disposition without allowing one
  lane to mint another lane's claim.
- `T-07`: evaluate production closure and assurance/source closure using
  `PATH-POS`, `PATH-NEG`, `SRC-OLD`, and `TEST-SEAM`.
- `T-08`: evaluate subject preservation for `MUT-1` and `MUT-2`.
- `T-09`: evaluate assurance acquisition and oracle separation for `AQ-1`,
  `AQ-2`, and `AQ-3`.
- `T-10`: localize `CF-1..CF-4` using the permitted causal-frontier forms and
  identify the evidence and downstream claims invalidated by each result.
- `T-11`: state the residual testing population and invalidation conditions for
  the complete frame set.

## Constructor Output Contract

Return one self-contained, digest-bound trial record that includes:

1. constructor identity plus non-authorship, no-reference-outcome exposure, and
   configuration-separation declarations;
2. exact candidate and input identities;
3. a row for every `F-01..F-12` and `T-01..T-11` case naming the relation,
   subject/basis, observed result, evidence, residual, and invalidation;
4. the normalized capability, relation/mechanics factoring, bounded discovery
   disposition, candidate evidence ledger, supported dominance relations,
   undominated frontier, and tradeoff-owner disposition;
5. the four claim-relative testing frames, their overlaps and conjunction, and
   the two closure graphs;
6. all four causal-frontier result forms;
7. any `indeterminate`, `out_of_frame`, `invalid_basis`, refusal, or residual
   population rather than a manufactured favorable answer;
8. reconstruction instructions; and
9. one closed `candidate_ready`, `incomplete`, `refused`, or
   `re_entry_requested` result returned to Executive.

The constructor evaluates constructability and sufficiency of the changed
method populations. It does not perform independent release review, apply an
Executive disposition, edit candidate bytes, tag, push, or publish.
