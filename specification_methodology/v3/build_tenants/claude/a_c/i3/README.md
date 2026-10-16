# Interpretation Set i3

The current interpretation of this candidate in `a_c`, first built at
iteration 3 and extended at iteration 5 with the construction and
assurance relations (group G14). It is a partial encoding: read
"Coverage" and "Where it is insufficient" before using it for any task.

## Coordinates

| Coordinate | Value |
|---|---|
| Method subject | the members under `standards/` at the commit the ledger's I5-05 entry names; statements are quoted from those bytes by the build tool, which refuses a quote that does not occur exactly once in its section. This set's source references name heading slugs under `stdo-3://build_tenants/claude/standards/` |
| Calculus basis | `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md` (`calculus_ref`) |
| Signature | [SIGNATURE.md](SIGNATURE.md): vocabulary under `urn:stdo-3:claude:i3:vocabulary:` |

## Coverage

Encoded: the shared-owner determinations of the result algebra and its
conjunction, authority kinds, reuse and invalidation, the promotion block,
the step-result refinements (dispositions, construction availability,
effects, ambiguity outcomes), the AC-007 outcome maps, two RF §5 outcome
maps, in part boundaries (IDENTITY §2, two clauses) and constraint
surfaces (AXIOMATIC_CALCULUS §9, two clauses: its conditions of use,
including "Unresolved blocks", are not encoded), the commitments P0 to P6
(P4a added at iteration 5), and, since iteration 5, group G14: the
construction relation (ACTIVATION §1, 29 clauses), the construction
synthesis (FOUNDATIONS §3, 2 clauses), the assurance relations
(FOUNDATIONS §4: the owner paragraphs and the six subsections, 57
clauses) and one `uses` relation at ACTIVATION §7. Totals: 154 clauses, 5
frame indexes, no residuals. Each G14 clause carries one of the five kinds
of support of FOUNDATIONS §4 Formal representation (SIGNATURE, Kinds of
support): 80 `discharged-argument`, 9 `stated-formula`.
Every section that holds an encoded clause is only partly encoded.

Dispositions (`dispositions/`): every heading section of the eight
members of groups G1 to G4 (FOUNDATIONS, IDENTITY, PROFILES, ACTIVATION,
CONFORMANCE, EVALUATION, AXIOMATIC_CALCULUS, REFERENCE_FRAME) has exactly
one. Totals: 24 `encoded-in-part`, 8 `no determination` (source-disposition
sections), 181 `not-encoded-i3`; no section is fully `encoded`. Groups G5
to G13 (the other 15 members) are not encoded and have no disposition
files.

This is a narrowed scope, recorded as a ledger variance for the product
owner's token limit; the iteration 5 extension covers the nine sections
added at I5-01 and leaves the rest of that scope as it was. The missing
material coverage blocks C3 closure for
interpretation coverage (common conformance discriminator 14): this set
establishes only its covered scope and is not the whole method's
interpretation.

## Where it is insufficient

Under [ACTIVATION §2](../../standards/ACTIVATION.md#2-context-construction-under-an-envelope)
Acquisition, a constraint surface projected from this set is a derived
surface only for the four task scopes below, and only for the clauses
they hold. For any other task, or any question these clauses do not
decide, acquire the deciding owner sections instead.

| Frame index | Task scope it serves | Not covered for that task |
|---|---|---|
| `result-algebra-and-conjunction` | combine results or refine result values | the Out-of-frame-or-indeterminate boundary, Predicates travel, Reported value and The declared rule of the conjunction are not encoded |
| `authority-kinds` | decide whether something grants authority | the proxy limit's list of what a proxy can never change; each member's domain instances |
| `reuse-and-invalidation` | decide whether a closed result may be reused | Transition evidence; domain triggers stated by members |
| `promotion-block` | decide whether a finding blocks current promotion | the purpose paragraph; the triage projection of EVALUATION §4 |
| `construction-and-assurance` | decide what a construction has established, and what an assertion, an agreement between derivations or a retained result supports | the examples and non-entailment arguments of ACTIVATION §1 and FOUNDATIONS §3; the family-table rows of both owners; the consumers paragraphs; the Transitions, Intake and §7 text the construction relation refers to; the quantified-assurance formulas are stated, not discharged |

No published frame task is fully covered, so no frame index is made for
any of the frames in `standards/frames/`.

## Evidence boundary

- Tenant pre-check: `python3 -I a_c/i3/tools/assemble.py --check` exits
  0; `tools/test_assemble.py` passes 6 tests. This is not a checker result.
- Mechanical evaluation, selected by the product owner: the pinned Axiom
  Indexer `v2.5.1-rc.2` was materialised from the tag with `git show`
  into a scratch directory outside the repository and verified before use:
  tag `9bff233c…`, commit `9a9c4797…`, tree `3a553ceb…`, subtree
  `6dae168d…`, all seven member SHA-256 values equal to the release note,
  aggregate `55a2061b…`; the executable `build_tenants/core/code/ac.py`
  `5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`, the
  schema `43326dbab520bd2d56fbdf605211f66499de1969b13e2e0226868bd6af9777a7`
  and the output contract
  `c124264d1fc564a8a054bba46b5c188c4e770da51862b4c2122e3c616efb1b6b`. `validate` returned `valid` with 0
  diagnostics; 5 frame indexes were projected in both modes (10
  projections). A second run
  on the same bytes reproduced every output byte for byte. Commands and
  exit codes: [checker-commands.log](checker-commands.log).
- The result is structural validation only. It establishes neither
  fidelity to the source, nor truth, nor sufficiency for a task, nor
  acceptance. Statements are quoted verbatim from the settled source by
  `tools/build_fragments.py`; the encoding decisions are in
  `tools/spec.py`. Fidelity is assessed separately (`fidelity/`, when
  present).

## Known gaps

- Coverage as above: the unencoded parts of 24 sections, 181 further
  sections of G1 to G4, and all of G5 to G13.
- Fidelity of group G14 and of the premise P4a: the cases and the review
  for the 90 clauses added at iteration 5 are pending (I5-05); until they
  are written the group's fidelity is unassessed, and the review below
  covers only the 64 clauses it read.
- Fidelity: [fidelity/review.md](fidelity/review.md) found three defects
  in the frozen set (a dropped trigger, a dropped "by default", and "by
  itself" hardened into a prohibition). They are repaired in this version;
  the repairs have not been re-reviewed.
- No residuals are encoded, because no encoded owner section leaves its
  question open; open questions elsewhere are not represented.
- Standing of the commitments: P0 is encoded as `premise` with its
  recovered standing named as a qualification.

## Reproduce

The route needs the v3 common specification at the same commit beside the
tenant (`../../specification/`): the adverse controls read the expected
checker digests from `requirements/A_C_DEPENDENCY.md` and refuse without
it. A tenant-only archive runs the fragments, the assembly and the checker
but not the controls. From the tenant root: `python3 -I a_c/i3/tools/build_fragments.py --dispositions`,
then `python3 -I a_c/i3/tools/assemble.py`, then the checker commands of
`checker-commands.log` against a verified copy of the checker.

## Artifacts

| File | SHA-256 |
|---|---|
| `axiomatic-program.json` | `c732d5e3f5f011b871c4a67da061ca0939271ea7b5aac4bb752c07005c9c5d4b` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` |
| `coverage.json` | `aba91c31a2bd04c40e7a538e531a034ac0ac6a995d8b01b6fd75a819eba888f4` |
| `consumers.json` | `831b62efd1e8c32e7f29e9e45c8e875f04b7484a5c064fce00ef4f3855512052` |
| `validation-report.json` | `8f70934699a093ed65d6de6faf2b366f206fea6d12ad31f2f8a52ac71801f91c` |
| `logical-constraint-map.json` | `5fe4dbbd07a99e503d1c7d9d1af05da5ef22a793e4ce5abfcc75716b353aa64b` |
| `projections/projection-authority-kinds-materialized.json` | `3104ac4e04f820d5a3392369bcfb649068c74e04192371bdcacc5600d76ee65e` |
| `projections/projection-authority-kinds-reference-only.json` | `3ab61b26dc656d0077ea4e19cbfbe53d0579a619a72fc61d8f53a5ae75ffe6b5` |
| `projections/projection-construction-and-assurance-materialized.json` | `201c200a504254ae816f12755bf0ba28c901e4006a3f775ac17503737be2f58b` |
| `projections/projection-construction-and-assurance-reference-only.json` | `7c321f6fbf7a8db7ab2d62745ff88b3cdeee0def6e58961144036bf246a6a959` |
| `projections/projection-promotion-block-materialized.json` | `7cd3b5af918b6041faac62914f72daefe0d51893ccf107a6847799a00cbf9763` |
| `projections/projection-promotion-block-reference-only.json` | `c7a9e5d6d7e9926c87f9e24db10eb8f337e271a736a2b8357b897551d2a59f67` |
| `projections/projection-result-algebra-and-conjunction-materialized.json` | `adb12f126e10307a66b2bd39e8d66983cdc19811fd2604574c51261dc43ac681` |
| `projections/projection-result-algebra-and-conjunction-reference-only.json` | `5586ec972d5c1f9c254105d8df9fb1f7227acf725b3075c4e341cf97f1d50149` |
| `projections/projection-reuse-and-invalidation-materialized.json` | `51d8ad01fd2cf49f981ddf54e47d4c35d02697732a274eae5272e2bba766fb32` |
| `projections/projection-reuse-and-invalidation-reference-only.json` | `e799ce9be10775dd9c2a9d13a3cb18d5594b4dce38893bca44025f3223c23baf` |
