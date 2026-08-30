# STDO Representation Quickstart

This guide gets a new checkout to a verified STDO Representation development
state and explains the boundary for constructing and consuming `stdo.gtl`.
It is an onboarding map, not constitutional authority. The exact installed
STDO basis and the project surfaces listed in [README.md](README.md#authority)
remain authoritative.

## What You Can Do Today

From a clean checkout you can:

- verify the exact STDO release governing this project;
- validate the project constitution and observe the Product Definition's exact
  fail-closed frame-acceptance gate;
- rebuild the frozen GTL dependency from its immutable Git commit;
- compile and test the historical `0.7.0` typed GTL carrier, raw-admission path,
  semantic-index encoding, and projection mechanics; and
- inspect the proposed Product, reference-frame basis, and GTL profile.

The repository retains one constructed, independently reproduced `stdo.gtl`
from the preceding WHAT basis. Its reference-frame basis, GTL profile, and
Semantic Selection Ledger have exact `F_H` construction-acceptance records for
that basis. Product re-entry has made it ineligible for current Product
acceptance or release; renewed acceptance and construction remain open.

## Prerequisites

- Git
- Python 3.11 or newer
- [`pipx`](https://pipx.pypa.io/) or another isolated Python application
  installer
- Node.js 20 or newer and npm, for the full frozen-GTL conformance probe

## 1. Clone The Project

```sh
git clone https://github.com/foolishimp/stdo_representation.git
cd stdo_representation
```

## 2. Install The Exact STDO Toolchain

This project is currently governed by `v2.5.0-rc.1`. Install the toolchain from
that immutable tag:

```sh
pipx install \
  "git+https://github.com/foolishimp/specification_methodology.git@v2.5.0-rc.1"
stdo --version
```

If `stdo` is already installed and available, do not reinstall it merely to
continue. The Product Definition, rather than the executable's installation
location, selects the exact governing release.

The complete manager onboarding guide is the
[STDO Quickstart for `v2.5.0-rc.1`](https://github.com/foolishimp/specification_methodology/blob/v2.5.0-rc.1/QUICKSTART.md).

## 3. Synchronize And Verify The Governing Basis

Install and verify the immutable release directly. Product Definition routing
remains intentionally unavailable until the frame-basis gate opens:

```sh
stdo install v2.5.0-rc.1 \
  --manifest-sha256 3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338
stdo verify v2.5.0-rc.1
```

The verified result must identify:

- basis `stdo://releases/v2.5.0-rc.1/`;
- manifest SHA-256
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`;
- release commit `ca6694314c4e9a56d3facae3eef06fe2792104c9`; and
- 51 standards members with no failures.

The operative Product Definition deliberately has
`reference_frame_bases = []` until the unchanged project frame-basis proposal
receives external `F_H` acceptance. Therefore these commands must fail on that
single non-empty-list gate:

```sh
stdo status --definition stdo_representation.json --verify
stdo bootstrap --definition stdo_representation.json --dry-run
```

Any different validation failure is a separate stop.

## 4. Run The Fast Project Checks

```sh
python3 scripts/check_constitution.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

These project-local staging checks cover the intended Product Definition
routing, exact identity inputs, constitutional structure, and negative
mutations. They do not establish Product Definition conformance while the frame
list is empty, human semantic acceptance, or compression adequacy.

## 5. Verify The Frozen GTL Tenant

Run the complete carrier probe:

```sh
python3 scripts/test_frozen_gtl_tenant.py
```

The probe:

1. resolves frozen GTL commit
   `8d7f965a3fae7d1acea6a9db298798480fd4cc2f`;
2. verifies authority tree `21a44b1941a1055d6abd973937e65b83e359de1b`
   and its 33 members;
3. archives and builds the immutable GTL TypeScript tenant;
4. compiles this project's historical `0.7.0` typed `ModulePublication`
   carrier; and
5. runs raw admission, frozen validation, and domain tests.

When a sibling ABIogenesis checkout is unavailable, the probe clones the
public repository into a temporary directory. To select an existing object
store explicitly:

```sh
python3 scripts/test_frozen_gtl_tenant.py \
  --abiogenesis-repository /path/to/abiogenesis
```

No Product artifact is published or retained by this probe. It validates frozen
carrier mechanics, not the active-WHAT axiom-index compilation and selection
path.

## 6. Read The Product In Authority Order

Read these surfaces before changing the algebra or tenant:

1. [Goals](specification/GOALS.md)
2. [Intent](specification/INTENT.md)
3. [Product](specification/PRODUCT.md)
4. [Requirements](specification/requirements/README.md)
5. [Reference-Frame Basis](specification/REFERENCE_FRAME_BASIS.md)
6. [Frozen GTL Basis](build_tenants/gtl/design/GTL_BASIS.md)
7. [Current axiom-index GTL Profile Candidate](build_tenants/gtl/design/GTL_AXIOM_INDEX_PROFILE.json)
8. [GTL Tenant Code](build_tenants/gtl/code/README.md)

The JSON [Product Definition](stdo_representation.json) locates those
authorities; it does not replace them.

## 7. Understand The Consumer Boundary

The intended path is:

```text
exact Source STDO member population
  + exact a_c basis and Sigma_STDO
  -> F_P[v_compile] immutable semantic proposal
  -> deterministic ConstructCandidate invocation/provenance envelope
  -> F_D[v_candidate_structure] structural result
  -> F_H[v_select] unchanged-model Semantic Selection Ledger | rework | rejected
  -> F_H[v_accept_interpretation] accepted a_c.STDO | rejected
  -> GTL carrier construction, then separate F_D carrier admission
  -> admitted stdo.gtl programmatic semantic index
  -> accepted Executive Context Assignment
  -> least, role-bound Executive | Worker | Reviewer projection
  -> LLM F_P[v_reason] reasoning over separately supplied workspace evidence
```

`stdo.gtl` is passive graph and constraint data. It is not a frozen-GTL
`GtlProgram`, an LLM invocation, a vector database, an authority grant, or a
copy of the target workspace. A consuming host supplies workspace evidence,
intent, actor, frame assignment, token budget, and the `F_P[v_reason]`
invocation contract.

The TypeScript package exposes `constructProjectionCandidate` for the exact
least-closure projection. A consumer-facing projection CLI and LLM host adapter
have not yet been published.

## 8. Run An Exploratory Whole-Index Probe

Until the role-projection CLI and host adapter are published, the retained
pre-reprice index can be supplied to a model for an exploratory observation
against its exact prior basis. Attaching bytes does not let an Executive assign
a Reviewer frame and must not be represented as the current Product. A probe
may attach:

- [`stdo.gtl`](build_tenants/gtl/representation/products/stdo-2.4.3-rc.3/product/stdo.gtl);
- the target workspace's Product Definition and active ticket; and
- the exact diff or files to review.

The index is a compact tuple carrier. Its semantic payload is in
`rules[0].config`:

| Key | Meaning |
|---|---|
| `l` | Tuple schemas and class tables |
| `s` | Shared string table |
| `i` | Shared identity table |
| `a` | Semantic atoms |
| `e` | Typed semantic edges |
| `c` | Passive constraints |

Integer identity references resolve through `i`; integer text references
resolve through `s`. Give the attached files to the LLM with a prompt such as:

```text
Explore this exact workspace change as a non-authoritative model observation.

STDO_INDEX is the governing Programmatic Semantic Index, not workspace
evidence and not a replacement for Source STDO.

Decode rules[0].config as follows:
- l = tuple schemas and class tables
- s = shared string table
- i = shared identity table
- a = semantic atoms
- e = typed semantic edges
- c = passive constraints
- integer identity references resolve through i
- integer text references resolve through s

Review intent:
Determine whether the supplied change preserves the declared Product,
authority, public-boundary, and proof relations.

Perspectives requested for exploration only:
- Product
- Public Boundary
- Owner
- Proof

Rules:
1. Resolve governing concepts by identity, bounded context, owner, and basis.
2. Follow declared edges and applicable constraints; do not infer authority
   from spelling or proximity.
3. Treat workspace files and the diff as evidence, never STDO authority.
4. When the index is insufficient, return the exact SourceLocator requiring
   re-entry into Source STDO.
5. Do not claim an Executive assignment, Reviewer activation, acceptance,
   disposition, or continuation authority.
6. Return exactly one exploratory observation:
   potential_falsifier | no_counterexample_observed | indeterminate
7. Include governing record identities, source routes, evidence examined,
   counterexamples, residual uncertainty, and the return route.
```

A compact response can then take this shape:

```text
Observation: potential_falsifier
Governing constraints: <constraint identities and source routes>
Evidence: <workspace observations and counterexample>
Residual uncertainty: <anything the supplied evidence could not resolve>
Source re-entry: stdo://releases/v2.4.3-rc.3/standards/<member>#<anchor>
Possible re-entry for an authorized Executive to consider:
<Product | Requirement | Design | Ticket>.
```

This bare model call is exploratory probabilistic processing. It is **not** an
Executive Context Assignment, Reviewer activation, Context Packet, claimed ODD
`F_P[v_reason]` traversal, qualified Product observation, or authority-bearing
disposition. It grants no authority to edit, accept, release, or continue the
workspace. A qualified role-bound call requires the complete assignment,
projection manifest, activation, grant, capability envelope, gates,
provenance, and stop coordinates defined by the Product.

The retained historical whole index is 153,986 bytes. Future role-bound projections will
replace it with the exact least closure for the accepted assignment and token
budget. Do not imitate projection by manually trimming the index: that can
silently remove a governing dependency or constraint.

## 9. Inspect Or Reproduce The Historical Construction

The historical construction required all of the following exact inputs:

- build plan and Source STDO manifest;
- accepted GTL profile bytes and acceptance record;
- accepted reference-frame basis bytes and acceptance record;
- accepted Semantic Selection Ledger and its historical construction-acceptance
  record under that prior WHAT; and
- publisher Product manifest and immutable publisher artifact.

The retained prior-WHAT construction is under
`build_tenants/gtl/representation/products/stdo-2.4.3-rc.3/`. Its exact
authorization and build plan can reproduce it into any new output directory:

```sh
python3 scripts/finalize_stdo_gtl_product.py \
  --candidate-directory build_tenants/gtl/representation/candidates/stdo-2.4.3-rc.3 \
  --authorization build_tenants/gtl/representation/candidates/stdo-2.4.3-rc.3/construction-authorization.json \
  --output-directory /new/empty/path/stdo-2.4.3-rc.3
```

The output directory must not already exist. The finalizer reconstructs the
same authorization, acceptance records, build plan, `stdo.gtl`, receipt, and
construction summary or refuses. The retained authorization accepts only the
exact historical construction inputs; it is not Product acceptance or a
release record and cannot authorize a current-WHAT candidate.

Future candidate coordinates must include both the WHAT member-set identity and
the immutable Semantic Compilation Candidate identity. They must be created at
a new path and must never overwrite or ambiguously reuse the historical
`candidates/stdo-2.4.3-rc.3` or `products/stdo-2.4.3-rc.3` directories.
The legacy `prepare_stdo_gtl_candidate.py` now checks its three historical
digests and refuses on the active WHAT before writing anything.

## Update To A Later STDO RC

The Product Definition follows the `2.5.0` version line. To inspect a later
published RC without changing the project:

```sh
stdo adopt --definition stdo_representation.json --dry-run
```

Review the exact target cut, tag object, commit, tree, manifest, and
`plan_sha256`. Accept only that plan in a separate invocation:

```sh
stdo adopt --definition stdo_representation.json \
  --accept-plan-sha256 <plan_sha256>
```

Then rerun synchronization, verification, bootstrap preview, and both project
check suites. Adoption updates the governing basis; it does **not** declare
changed STDO semantics conserved or regenerate `stdo.gtl`. Changed, added, and
removed Source STDO members must re-enter `F_P[v_compile]` semantic compilation
and `F_H[v_select]` acceptance before a new index Product is constructed.

A new version line, such as `2.6.0` or `3.0.0`, requires a deliberate selector
change. The `2.5.0` channel never silently crosses that boundary.

## Common Stops

| Stop | Meaning |
|---|---|
| `stdo status`, `sync`, or bootstrap reports `reference_frame_bases: [] should be non-empty` | Expected current gate: the proposed project frame basis has not been accepted. |
| `stdo status` reports a manifest or member failure | The installed basis is not the exact selected release; do not continue. |
| Bootstrap dry-run proposes unexpected project-owned changes | Review the Product Definition targets before allowing mutation. |
| Frozen GTL commit, tree, or member count differs | The selected carrier basis was not reproduced. |
| Acceptance input is missing or its digest differs | Production construction is unauthorized and must fail closed. |
| A generated projection exceeds its declared token budget | Do not truncate it implicitly; revise the authorized assignment or selection. |
