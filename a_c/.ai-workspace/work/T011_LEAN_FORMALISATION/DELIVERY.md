# T-011 Lean formalisation delivery

The independent Lean/Mathlib tenant is implemented. Its
[final independent review](review/20261027_FINAL_REVIEW.md) is **satisfied for
FR-001–FR-007**, with no findings or required repairs. The bounded delivery
proves exact declared dependency closure, retained-record projection and
insufficient-budget refusal. Work remains **uncommitted and unpushed on `main`**.
No owner acceptance or release is issued.

Start with the [usable tenant README](../../../build_tenants/lean/README.md).
The private toolchain is present in this checkout. From the repository root:

```sh
cd a_c/build_tenants/lean
python3 -B scripts/check.py
```

For a fresh checkout, follow the README's prerequisites and run
`python3 -B scripts/bootstrap.py` first. Bootstrap installs the pinned compiler
privately in the tenant. Apple Silicon macOS is the exercised platform; the
first compiler download is about 570 MB. The full check writes its report under
`.lake/check/` and includes roughly a minute of fresh kernel replay here.

The source adapter runs without Lean:

```sh
python3 -B scripts/import_fixture.py --seed 4 --budget 6
python3 -B scripts/import_fixture.py --seed 4 --budget 5
python3 -B scripts/import_fixture.py --toy --seed 1 --budget 9
```

The first command returns six complete records; the second refuses with exit 2.
The third exercises the application-neutral all-family fixture. The full check
additionally builds and replays the Lean proofs, executes the actual projection
operation and compares returned content to the source.

The [implementation record](implementation/README.md) and
[independent public-path report](review/full-path-001/report.json) retain the
performed evidence: 32 adapter tests, both published-subject carrier recoveries,
46 concrete selectors, 46 actual projections, 46 underbudget refusals and 204
deciding theorem reports. Independent controls cover changed payloads, missing
dependencies, altered authority/residuals and disconnected cycles. The 32-record
published STDO 3.0.2 supplement is subject data under the unchanged installed
v2.5.1-rc.2 builder; the separate 14-record toy populates all eight families.

| Exact subject/evidence | SHA-256 |
|---|---|
| [29-file tenant source manifest](implementation/SOURCE_MANIFEST.json) | `3d231e3fb56053a9dc6eca789c57ec42e395e0c6a7d68cfe71f5efa019203e2e` |
| [Implementation closed return](implementation/CLOSED.json) | `d060009721ef82e04607df730631e561bf54ac268adfa99774265282574aa535` |
| [Independent review closed return](review/CLOSED.json) | `d2ccc3ee74d4ac4e7fce366483720733c8d67936674679d0156039438605a308` |
| [Independent public-path report](review/full-path-001/report.json) | `8b002e3821e99cd88bae0ccf07794d2e99818ba4e5b38d919fc3e3b45c672061` |

The [preserved common-source manifest](final-status/PRESERVED_REVIEWED_SOURCE.json)
locates all eleven exact reviewed contract subjects before README/Goals/ticket
status updates. Prior returns and all 29 tenant files retain their reviewed
bytes. The [final-status record](final-status/CLOSED.json) binds this handoff
and verifies the unchanged normative source, implementation and review evidence.

The [proof boundary](../../../build_tenants/lean/design/BOUNDARIES.md) retains
the exact limits: Lean's kernel and `propext`, `Classical.choice`, `Quot.sound`
remain trusted; Python parsing, hashing, schema mapping and generation are
unproved bridges; compiler/runtime/serialization are tested rather than proved
correct. Conserved source strings do not prove source fidelity, semantic
dependency sufficiency or authority legitimacy. Whole-calculus validity,
arbitrary predicates/transformation execution, efficiency, semantic/carrier
admission, Product acceptance and release are outside this delivery.
