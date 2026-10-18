# Interpretation Set i3

The current interpretation of this candidate in `a_c`, first built at
iteration 3 and extended at iteration 5 with the construction and
assurance relations (group G14). It is a partial encoding: read
"Coverage" and "Where it is insufficient" before using it for any task.

## Coordinates

| Coordinate | Value |
|---|---|
| Method subject | the members under `standards/` at the current candidate's freeze commit, which the handoff names (refrozen at every member change since I5-05); statements are quoted from those bytes by the build tool, which refuses a quote that does not occur exactly once in its section. This set's source references name heading slugs under `stdo-3://build_tenants/claude/standards/` |
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
(P4a and the prohibition its paragraph states added at iteration 5), and,
since iteration 5, group G14: the
construction relation (ACTIVATION §1, 29 clauses), the construction
synthesis (FOUNDATIONS §3, 2 clauses), the assurance relations
(FOUNDATIONS §4: the owner paragraphs and the six subsections, 57
clauses) and one `uses` relation at ACTIVATION §7. Totals: 155 clauses, 5
frame indexes, no residuals. Each G14 clause carries one of the five kinds
of support of FOUNDATIONS §4 Formal representation (SIGNATURE, Kinds of
support): 80 `discharged-argument`, 9 `stated-formula`.
Every section that holds an encoded clause is only partly encoded.

Dispositions (`dispositions/`): every heading section of the eight
members of groups G1 to G4 (FOUNDATIONS, IDENTITY, PROFILES, ACTIVATION,
CONFORMANCE, EVALUATION, AXIOMATIC_CALCULUS, REFERENCE_FRAME) has exactly
one. Totals: 24 `encoded-in-part`, 8 `no determination` (source-disposition
sections), 183 `not-encoded-i3`; no section is fully `encoded`. Groups G5
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
surface only for the five task scopes below, and only for the clauses
they hold. For any other task, or any question these clauses do not
decide, acquire the deciding owner sections instead.

| Frame index | Task scope it serves | Not covered for that task |
|---|---|---|
| `result-algebra-and-conjunction` | combine results or refine result values | the Out-of-frame-or-indeterminate boundary, Predicates travel, Reported value and The declared rule of the conjunction are not encoded |
| `authority-kinds` | decide whether something grants authority | the proxy limit's list of what a proxy can never change; each member's domain instances |
| `reuse-and-invalidation` | decide whether a closed result may be reused | Transition evidence; domain triggers stated by members |
| `promotion-block` | decide whether a finding blocks current promotion | the purpose paragraph; the triage projection of EVALUATION §4 |
| `construction-and-assurance` | decide what a construction has established, and what an assertion, an agreement between derivations or a retained result supports | the examples and non-entailment arguments of ACTIVATION §1 and FOUNDATIONS §3; the family-table rows of both owners and the assurance family's instance premises (a) to (c); the consumers paragraphs; the Transitions, Intake and §7 text the construction relation refers to; the owner of an approximate relation's adequacy bound; the sentences "a universal soundness claim covers all admitted conclusions", "Shared derivations can be recorded once", "The formula supplies no missing likelihood or prior", "no exhaustive graph database is required" and "Selection alone produces no execution evidence" (named by the fidelity cases as uncovered); the quantified-assurance formulas are stated, not discharged |

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

- Coverage as above: the unencoded parts of 24 sections, 183 further
  sections of G1 to G4, and all of G5 to G13.
- Fidelity of group G14 and of the premise P4a:
  [fidelity/cases-i5.md](fidelity/cases-i5.md) (22 cases, written before
  the model was opened) and [fidelity/review-i5.md](fidelity/review-i5.md)
  (agree 14, disagree 7, cannot answer 1; 90 of 90 statements verbatim in
  their sections; 0 mismatches of the kind of support on the nine
  formulas; 7 force hardenings of non-requirements and non-entailments
  into `must-not`, the pattern the iteration 3 review also found; 5
  premise citations differing from the source's own). The disagreements
  and the uncovered P4a prohibition are repaired in this version as
  encoding decisions; the repaired clauses have not been re-read. Both
  files are same-family working evidence, not independent assessment.
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
`checker-commands.log` against a verified copy of the checker, which
`qualification/C3-ITER3/tools/run_ac.sh <checker> <out>` replays from any
copy of the tenant root. The record of one such reproduction from a clean
archive of a commit, with every output byte-identical and the controls
run from the clean root, is kept beside the iteration 5 returns
(`qualification/C3-ITER5/returns/ac_controls_clean_<commit>.json`).

## Artifacts

| File | SHA-256 |
|---|---|
| `axiomatic-program.json` | `5fea30ce62bbc8eea3b1904712d47ae0feb23ac0d8d4b49174dc8c1ea74b3b22` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` |
| `coverage.json` | `e31cca44bc799099d7c2e4897e6e61ce8a20476238c2ecf852aef813b478d4a5` |
| `consumers.json` | `a5ab74aa96038117a80bb3f86a20d0f6f9b275f08892784603a0fa197a5228ec` |
| `validation-report.json` | `0e8b39615de35777694f3540248e434b8b44f86ef8194822020da776238ca179` |
| `logical-constraint-map.json` | `af00f7fa4a6772cc8f1091e1d403cc6e9b4f252ec628499bcd21cf4e6b5828d5` |
| `projections/projection-authority-kinds-materialized.json` | `03c3b21b97092a9dd3a5756f642ad8710967b4123a61b95fbe72832e0b58efdf` |
| `projections/projection-authority-kinds-reference-only.json` | `17a6c9bed18b15c009e67bc5f572a26d6bbbf055633f697ce713bee8d6882633` |
| `projections/projection-construction-and-assurance-materialized.json` | `614601b32d67c01167997cc7bb205e1be7a67d8b2677e6458049ca3cb200c7f3` |
| `projections/projection-construction-and-assurance-reference-only.json` | `f65ee70bb9c41aa9a36dd9f4bf022e3fed81a3cf3470f4a9d828b519107adb92` |
| `projections/projection-promotion-block-materialized.json` | `a1ac86282ffb138c20bc43628d290b5b4b17c7fffa445882c903fd04ed95f34c` |
| `projections/projection-promotion-block-reference-only.json` | `8a103219a337c3036461ac309a52ea294534b9ccd52df57c7aa83f332c19ba1b` |
| `projections/projection-result-algebra-and-conjunction-materialized.json` | `12f2894ac79e5cfe9eeda7fdfac738824cc5e481e8c8c9854c346880cf236df6` |
| `projections/projection-result-algebra-and-conjunction-reference-only.json` | `c648f3da207cc3cab8b8759ca1a7a785ca46419b18cffb436820d4987f7383c5` |
| `projections/projection-reuse-and-invalidation-materialized.json` | `bd95ecb598a53d3bf8b4f772237db638ac9f8f5eae6e8bf6d4b3b4656c338fe3` |
| `projections/projection-reuse-and-invalidation-reference-only.json` | `beaf4d3cc0e851811f0cf21d7c8584628a15f4b1b862ba90bbda377010d4fe6b` |
