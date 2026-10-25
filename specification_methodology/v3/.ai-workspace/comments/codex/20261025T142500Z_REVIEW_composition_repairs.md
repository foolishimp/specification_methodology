# Review — targeted composition repair readbacks

Author: `/root/composition_source_review`, independent nonauthor Reviewer.

Date: 2026-10-26 (Australia/Sydney).

Addresses: manager M1 in
[the manager review](20261025T140000Z_REVIEW_composition_manager.md) and
representation M1 in
[the method/representation review](20261025T141000Z_REVIEW_composition_method_representation.md).

Status: **closed; both findings are discharged for the exact successors below.**
No new defect was identified within these two targeted predicates. The original
reviews remain historical records of their original subjects. This readback is
same-family nonauthor evidence, not owner acceptance, release approval, complete
method qualification or a new broad review.

## Frozen subjects and verified scope

| Subject | Successor index SHA-256 |
|---|---|
| [Manager repair 1](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/manager/CANDIDATE-repair1.json) | `cc6c338c944069734d762a56b2bcea552c5158f81c79c0ff745fd0f8aacc7b90` |
| [Common/representation repair 1](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/common/CANDIDATE-repair1.json) | `49782c5a616cb4c12ad2ef95d28d6fd7f5a60546d329cd37a8380f998f9728bd` |

All manager index members matched: eight source/test/document files and nine
evidence files. All 113 common successor members matched their declared lengths
and digests. The manager delta is confined to `composition.py`, its composition
tests, README and toolchain design. `references.py`, the CLI, cohort implementation
and Product Definition module match the original reviewed identities. The common
delta consists of the declared interpretation and derived/provenance records;
the native owner and frames remain at the original common freeze. No builder or
installed release change is part of either repair.

## Manager M1 — discharged

The deciding source is
[`composition.py:95`](../../../../v2/src/stdo_toolchain/composition.py:95), SHA-256
`af60451743604db9f24e2182b6eaf088ec79c5a70885811e3d674b2f38536d74`.
The replacement scanner distinguishes escaped punctuation from actual tags,
pairs maximal equal-width backtick runs across line endings, keeps inline spans
within paragraph/block boundaries, and consumes raw tags atomically. Paragraph
continuations preserve an indented inline-span delimiter. The actual fragment
path calls that scanner before HTML anchor extraction at line 135. The shared
heading-slug implementation is unchanged.

I compared the repair to its preserved reviewed preimage and read the focused
negative and real-anchor cases at
[`test_composition.py:174`](../../../../v2/tests/test_composition.py:174), current
SHA-256 `7c817048252817e8dfd60f84b655be6e5e3fb626908681d68e4d0b22b97c3835`.
The Writer's final evidence binds this source and records 20 composition tests,
including ten literal/escape/code negatives and eleven actual-anchor positives.
The earlier 31 cohort tests concern the unchanged cohort/slug implementation;
they were not relabelled as a fresh final-source run, and I did not repeat them.

I independently replayed the original exact definition/relation bytes through
the successor public CLI, using isolated copies of the retained control and
`PYTHONPATH` selecting `v2/src`. Two real-anchor counterfactuals check that the
repair did not simply reject HTML anchors:

| Case | Actual exit | Actual result |
|---|---:|---|
| Original control | 0 | `valid: true`; relation resolved |
| Original escaped `<a>` markup | 1 | `valid: false`; relation `missing_fragment` |
| Original multiline inline-code anchor text | 1 | `valid: false`; relation `missing_fragment` |
| Actual HTML anchor with the same target fragment | 0 | `valid: true`; relation resolved |
| Actual anchor after a closed multiline code span | 0 | `valid: true`; relation resolved |

The two false-positive paths from M1 now fail at the required relation and
aggregate result; valid counterfactuals still succeed. The independent command,
input digests and complete reports are retained in
[`manager-M1-independent-replay.json`](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/reviews/repair-readback/manager-M1-independent-replay.json),
SHA-256 `b17eb182d589e4a8dbba12099419b06cee59670f0574a79feb12e6ae3fb81a98`.
Temporary fixture copies were removed. This closes the reported literal-anchor
failure class within the declared bounded fragment convention; it does not
claim a general Markdown renderer or exhaustive Markdown conformance.

## Representation M1 — discharged

The repaired author answer at
[`AUTHOR_ANSWER.json:375`](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/representation/AUTHOR_ANSWER.json:375)
has SHA-256 `af9a7a8bf3677cddf10ef4d2cbea8d9afb49cd8b57e1e9c7f3a89ac0281e25a3`.
It explicitly permits an optional direct-edge inventory of public constituent
contracts despite available adequate encapsulation, with targets, purposes and
grants separately established. Its prohibited variation now concerns inferred
or unioned grants and omission of material far-side reliance and authority.

That matches the unchanged owner at
[`PRODUCT_DEFINITION.md:924`](../../../build_tenants/common/standards/PRODUCT_DEFINITION.md:924):
adequate encapsulation is permitted, flattening is not mandatory, and material
far-side reliance remains accountable. A lawful optional inventory is no longer
rejected as unnecessary. Reachability still supplies no grant, and choosing
encapsulation does not excuse omission of a material assumption or evidence-use
dependency. I read the three source-selected cases in
[`DISCRIMINATOR.md`](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/representation/repair1/DISCRIMINATOR.md)
as semantic counterexamples, not executed policy tests.

Comparison with `PRE_REPAIR.zip` confirmed that only the PC-04 latitude record's
allowed/forbidden variations changed within the 24-record semantic population.
All 15 archived entries match the original frozen identities. The current native
owner remains SHA-256
`7394f9d046e34f0ced33372dd0bd1d8983cfbab5453ebc8997d65d4e7a43a567`;
source sections, coverage and interpretation contract are unchanged. No source-law
amendment was introduced to rationalize the former interpretation error.

The current
[`MODEL.json`](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/representation/MODEL.json)
file SHA-256 is `e0118acc7525fe17a3fc9e9f72e774cf5bfc0abea10d6614d692292620262b1c`.
Both retained recovered models equal it as JSON values, with canonical digest
`451532d247c3804538880a96fa0a29161bd6104fa3d314f14e9a8b8d3bf62119`.
This is value recovery, not raw serialization-byte identity. Authoring provenance
and derived evidence are refreshed. The unsupported prohibition is absent from
the actual semantic record, rather than merely explained away in a note.

## Limits and closure

This pass inspected the two changed subsets, retained preimages, exact successor
identities and focused evidence. It added only the five isolated manager CLI
observations above; no full suite, broad build, actor trial or general review was
repeated. The original reviews' other limits remain: bounded mechanical
resolution is not grant/semantic acceptance, and a 24-record representation does
not complete the earlier whole-method interpretation or execute its predicates.

a_c/Skills runtime code remains outside this readback. Only this authorized
review and its focused evidence were written. No candidate repair, Git operation,
installed release change or global installation was performed. Both M1 findings
are closed on these successors; owner acceptance and the separately scoped
runtime review remain separate decisions.
