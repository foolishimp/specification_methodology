# GTL Tenant Code

This TypeScript package implements the historical `STDO.gtl 0.7.0` carrier and
the active Axiom Index GTL profile candidate. The active encoder requires the
exact STDO `v2.5.0-rc.1` calculus basis, all eight `a_c` populations,
`ResolutionSet_M`, accepted-program and selection-ledger bytes, the exact F_D
result, and an external F_H judgment. Its tests synthesize that acceptance only
to exercise the gate; they accept no repository artifact and create no current
carrier candidate. The `0.7.0` implementation:

- validates the closed common atom, edge, and constraint identities;
- encodes them reversibly into compact indexed tuple tables;
- constructs the exact frozen GTL `ModulePublication` typed declaration;
- passes the equivalent raw carrier through frozen GTL admission and its sole
  publication validator; and
- emits canonical `stdo.gtl` bytes and a content-first Product candidate
  receipt.

It does not select Source STDO semantics, accept a profile or ledger, authorize
an Executive assignment, invoke an LLM, or create HoG/ABG execution.

Run the exact-basis conformance suite from the repository root:

```sh
python3 scripts/test_frozen_gtl_tenant.py
```

The probe uses the sibling ABIogenesis repository when present; otherwise it
clones the public repository into a temporary directory. To select a local
object store explicitly:

```sh
python3 scripts/test_frozen_gtl_tenant.py \
  --abiogenesis-repository /path/to/abiogenesis
```

The probe archives the immutable GTL commit rather than compiling mutable
checkout bytes.

For historical `0.7.0` inputs only, after the profile, frame basis, and Semantic
Selection Ledger have exact acceptance records, the compiled CLI constructs
into a new directory atomically:

```sh
stdo-gtl build \
  --plan build-plan.json \
  --source-manifest manifest.json \
  --profile ../design/GTL_REPRESENTATION_PROFILE.md \
  --frame-basis ../../../specification/REFERENCE_FRAME_BASIS.md \
  --selection-ledger semantic-selection-ledger.json \
  --profile-acceptance profile-acceptance.json \
  --frame-basis-acceptance frame-basis-acceptance.json \
  --selection-acceptance selection-acceptance.json \
  --publisher-manifest gtl-toolchain-product.json \
  --publisher-artifact gtl-toolchain-product.tgz \
  --output-directory candidate
```

The command is not an active-WHAT construction path. The destination must not
already exist. Success creates only `stdo.gtl` and
`build-receipt.json`. The package API also exposes the exact least-context
closure and role-bound projection-candidate constructor; a projection remains
non-admitted until its exact tokenizer measurement and Context Projection
Manifest are completed.
