# STDO Representation Quickstart

This guide gets a new checkout to a verified STDO Representation development
state and explains the boundary for constructing and consuming `stdo.gtl`.
It is an onboarding map, not constitutional authority. The exact installed
STDO basis and the project surfaces listed in [README.md](README.md#authority)
remain authoritative.

## What You Can Do Today

From a clean checkout you can:

- verify the exact STDO release governing this project;
- validate the Product Definition and project constitution;
- rebuild the frozen GTL dependency from its immutable Git commit;
- compile and test the typed GTL carrier, raw-admission path, semantic-index
  encoding, and projection mechanics; and
- inspect the proposed Product, reference-frame basis, and GTL profile.

The repository contains one constructed but unreleased `stdo.gtl` candidate.
Its reference-frame basis, GTL profile, and Semantic Selection Ledger have exact
`F_H` construction-acceptance records. Product acceptance and release remain
separate and have not occurred.

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

This project is currently governed by `v2.4.3-rc.3`. Install the toolchain from
that immutable tag:

```sh
pipx install \
  "git+https://github.com/foolishimp/specification_methodology.git@v2.4.3-rc.3"
stdo --version
```

If `stdo` is already installed and available, do not reinstall it merely to
continue. The Product Definition, rather than the executable's installation
location, selects the exact governing release.

The complete manager onboarding guide is the
[STDO Quickstart for `v2.4.3-rc.3`](https://github.com/foolishimp/specification_methodology/blob/v2.4.3-rc.3/QUICKSTART.md).

## 3. Synchronize And Verify The Governing Basis

Install the exact basis already pinned by `stdo_representation.json`, then
verify it:

```sh
stdo sync --definition stdo_representation.json
stdo status --definition stdo_representation.json --verify
```

The verified result must identify:

- basis `stdo://releases/v2.4.3-rc.3/`;
- manifest SHA-256
  `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`;
- release commit `eb87a20247beeb93de394523ebdf8faecfd71949`; and
- 47 standards members with no failures.

Preview the agent bootstrap routing:

```sh
stdo bootstrap --definition stdo_representation.json --dry-run
```

In an unchanged checkout, both `AGENTS.md` and `CLAUDE.md` report
`action: unchanged`.

## 4. Run The Fast Project Checks

```sh
python3 scripts/check_constitution.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

These checks cover Product Definition routing, exact identity inputs,
constitutional structure, and negative mutations. They do not establish human
semantic acceptance or compression adequacy.

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
4. compiles this project's typed `ModulePublication` carrier; and
5. runs raw admission, frozen validation, and domain tests.

When a sibling ABIogenesis checkout is unavailable, the probe clones the
public repository into a temporary directory. To select an existing object
store explicitly:

```sh
python3 scripts/test_frozen_gtl_tenant.py \
  --abiogenesis-repository /path/to/abiogenesis
```

No Product artifact is published or retained by this probe.

## 6. Read The Product In Authority Order

Read these surfaces before changing the algebra or tenant:

1. [Goals](specification/GOALS.md)
2. [Intent](specification/INTENT.md)
3. [Product](specification/PRODUCT.md)
4. [Requirements](specification/requirements/README.md)
5. [Reference-Frame Basis](specification/REFERENCE_FRAME_BASIS.md)
6. [Frozen GTL Basis](build_tenants/gtl/design/GTL_BASIS.md)
7. [Proposed `stdo.gtl` Profile](build_tenants/gtl/design/GTL_REPRESENTATION_PROFILE.md)
8. [GTL Tenant Code](build_tenants/gtl/code/README.md)

The JSON [Product Definition](stdo_representation.json) locates those
authorities; it does not replace them.

## 7. Understand The Consumer Boundary

The intended path is:

```text
accepted Source STDO semantic selection
  -> canonical stdo.gtl programmatic semantic index
  -> accepted Executive Context Assignment
  -> least, role-bound Executive | Worker | Reviewer projection
  -> LLM F_P reasoning over separately supplied workspace evidence
```

`stdo.gtl` is passive graph and constraint data. It is not a frozen-GTL
`GtlProgram`, an LLM invocation, a vector database, an authority grant, or a
copy of the target workspace. A consuming host supplies workspace evidence,
intent, actor, frame assignment, token budget, and the `F_P` invocation.

The TypeScript package exposes `constructProjectionCandidate` for the exact
least-closure projection. A consumer-facing projection CLI and LLM host adapter
have not yet been published.

## 8. Inspect Or Reproduce The Constructed Candidate

A production build requires all of the following exact inputs:

- build plan and Source STDO manifest;
- accepted GTL profile bytes and acceptance record;
- accepted reference-frame basis bytes and acceptance record;
- accepted Semantic Selection Ledger and its acceptance record; and
- publisher Product manifest and immutable publisher artifact.

The retained candidate is under
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
exact construction inputs; it is not Product acceptance or a release record.

## Update To A Later STDO RC

The Product Definition follows the `2.4.3` version line. To inspect a later
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
removed Source STDO members must re-enter semantic selection and `F_H`
acceptance before a new index Product is constructed.

A new version line, such as `2.4.4`, requires a deliberate selector change.
The `2.4.3` channel never silently crosses that boundary.

## Common Stops

| Stop | Meaning |
|---|---|
| `stdo status` reports a manifest or member failure | The installed basis is not the exact selected release; do not continue. |
| Bootstrap dry-run proposes unexpected project-owned changes | Review the Product Definition targets before allowing mutation. |
| Frozen GTL commit, tree, or member count differs | The selected carrier basis was not reproduced. |
| Acceptance input is missing or its digest differs | Production construction is unauthorized and must fail closed. |
| A generated projection exceeds its declared token budget | Do not truncate it implicitly; revise the authorized assignment or selection. |
