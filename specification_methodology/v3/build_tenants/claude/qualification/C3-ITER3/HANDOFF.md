# Iteration 3 Handoff, Claude Line

This is the closing record of the Claude line's iteration 3 under contract
`EC-CLAUDE-I3-01` (T-002-CLAUDE, admitted at `651581c`). The common input
is `C3-I3-R2-01`, and the common specification on the branch equals
`355aa86`. It is for the product owner and for the reviewer the product
owner assigns. Every check named here is same-family working evidence
from the Claude line. Nothing here is accepted, and nothing claims
acceptance.

## Candidate

| Coordinate | Value |
|---|---|
| Branch | `tenant/claude/c3-synthesis` (worktree `specification_methodology-claude`), not merged, not pushed |
| Frozen candidate (I3-8f) | commit `2beed8d`. The earlier freeze `416bdb5` (I3-6) is the subject of the final review; `2beed8d` repairs that review's findings |
| Source settlement | `3ab7ef9` (I3-4d); member text changed after it only through step 7, and once by recorded variance (`standards/README.md`, I3-5v) |
| Ledger | `qualification/C3-SYNTHESIS/LEDGER.md`, section "Iteration 3" |

Digests at `2beed8d`: SHA-256 of the sorted `shasum -a 256` lines of each tree's files.

| Tree | SHA-256 |
|---|---|
| 23 members `standards/*.md` | `7e8349f90797d16f18c90150e57d9ca0ed551dbee3252fe9acf6fab0fe0583ec` |
| all of `standards/` | `4f5c5c1de4cf6c80790497fb7686b1242e60e1e85a1246a4d7cb46b3fa041910` |
| `standards/frames/` | `3b5913a2d5591083e8dc68099e4707676ec6be1cc1513a37a40fc5f38b79275a` |
| `a_c/i3/` | `b316f78f167cc96363433317b3889c54ae758b0b7fabadaa1912647ec34e7762` |
| `qualification/instruments/` | `e79af6eced91ca77a93f29e8f405efddc17f76ceb138b59d2e4b5930fbfc7bd6` |
| `plugins/` | `5e73f8e3b36c85bbd5ced9e19f0630e9f4f7761fa6b4a1fb669398a1c1f14d7f` |
| `frontier/PREDECESSOR_CLAIMS.md` | `c8cd19a0a08ac57a30cba1e41fcc4d769f57e0e05549fcb1023a3a388be317f6` |

## What changed in this iteration

- **Shared owners.** Each shared rule has one owner. The rival loci refer to it, or refine it with a map back to it (design `REDUCTION.md` §3, 34 clusters). New or settled owners:
  - EVALUATION §5 `When a finding blocks promotion`;
  - ACTIVATION §2 `Staleness of derived surfaces`, and ACTIVATION §6 resource limits;
  - ACTIVATION §1 `Admission`, for "only an admitted contract activates a step";
  - IDENTITY §2 `Boundaries and sufficiency claims`, pillar 2's generic law, which WORLD_MODEL refines;
  - AXIOMATIC_CALCULUS §9 `Constraint surfaces`, pillar 10;
  - SPEC_METHOD §10 for the ADR lifecycle rules.
- **Family tables.** All 21 families now argue in the form "By … so …", label their policy choices with owners, and carry a Pillar column. The FOUNDATIONS §3 index has every Pillar cell.
- **Consumers.** The plugins, templates, UX, WORLD_MODEL, PROFILES, TICKETS, RELEASE and ASSURANCE cite their owners instead of restating them. GLOSSARY §17 lists the labels that have several senses.
- **CONFORMANCE** maps all 52 common discriminators and the 3 closure checks.
- **Frontier.** Rebound to the `355aa86` inventory. A script finds all 707 keyed rows present exactly once, plus 9 tenant child rows. Every row has a disposition. Every supersession is marked proposed and pending the product owner.
- **Interpretation** `a_c/i3/`, narrowed by variance:
  - 64 clauses, each quoted verbatim, covering the shared-owner determinations of groups G1 to G4;
  - 15 sections `encoded-in-part`, 181 `not-encoded-i3`; G5 to G13 not encoded.
- **Checker.** The pinned Axiom Indexer `v2.5.1-rc.2` was verified against its tag, its seven member digests and its aggregate. It returned `valid` with 0 diagnostics. Four frame indexes were projected in both modes, and every output reproduced byte for byte. This is structural validation only.
- **Frames.** 12 frames, including the new `acceptance-release` and `member-build-assess`. `--check` exits 0. The finite check `--check` exits 0.

## Working results (same family)

| Check | Subject | Result |
|---|---|---|
| WC-1 (`reviews/WC-1.md`) | step 1 | `local_repair`; repaired in I3-2r |
| WC-2 (`reviews/WC-2.md`, non-author) | step 2 | `local_repair`: 1 High, 3 Medium, 8 Low; repaired in I3-3r. Table check: 71 of 204 rows sampled, 62 real, 9 weak, 0 hollow |
| FINAL (`reviews/FINAL.md`, non-author) | freeze `416bdb5` against ORACLE | `local_repair`: 0 High, 4 Medium, 7 Low. FR-01, FR-03 to FR-06, FR-08 to FR-11 repaired in I3-8r. FR-02 and FR-07 go to the product owner (below). Closure checks: no proposal is presented as accepted (J54); J53 and J55 need the integrated and cross-family reviews |
| Fidelity (`a_c/i3/fidelity/`) | `a_c/i3` at `416bdb5` | 8 cases: 3 faithful, 3 defects, 2 not encoded. The 3 defects were repaired in I3-8r, but the repairs have not been re-reviewed |
| Desk traces (`paths/DESK-TRACES.md`) | DP-43 only | against S0: "not established" (S0's route never reaches the owner); against S1: "simpler to determine and apply", on condition that the shall-to-indicative convention is accepted (FR-02) |

## Gaps the product owner should know

- **Criterion 4 (actual use) is unevidenced.** The product owner chose no paid fresh-actor trials, so no fresh actor used the frames or the method. Desk traces and reviews do not stand in for actual use.
- **Desk traces.** The declared sample was 8 paths. Only DP-43 was traced; the reviewer ran out of budget. DP-01, -07, -13, -19, -25, -31, -37 and the other 38 paths were not traced. No reduction verdict exists for them.
- **Row re-assessment (I3-4a, I3-4b).** WC-2 read both texts for about 30 of about 75 changed rows and judged the rest from the deltas. Those rows are partly evidenced.
- **Interpretation coverage.** The partial coverage blocks C3 closure for interpretation coverage (conformance discriminator 14). The fidelity repairs are unreviewed.
- **Frames.** Frames do not yet carry the family-table rows and result maps that their sections need (tradeoff TO1). The F5 `kind` label is not done.
- **Variances recorded in the ledger:**
  - activations acquired more than the 300 KB default, and both reviewers went over their budgets;
  - one read-only extraction subagent was used besides the two reviewers;
  - the README paragraph was changed after settlement;
  - the finite result file was stale at the first freeze.

## Open decisions for the product owner

1. **Sign-off on the common specification.** Still open; carried as a known gap.
2. **Changes to accepted conditions and the pillar list.** Still open; carried as known gaps.
3. **Replacement relations.** Each stays a proposed `superseded`, pending the product owner:
   - BASE: `#work-result-disjointness-and-incomplete-pairing`, `#derived-worker-frame-result`, `#3-worker-returns-to-executive-mapping`, `#profile-qualification-obligation-5`, `#closure-condition-4-mapping`;
   - BASE child rows: `#executive-drift-locks-stale-held-result`, `#derived-generic-specialist-frame-set-seam-result`, `#missing-frame-and-re-entry-application-order`;
   - SPEC: `#proportional-disposition-returning-party`, new in step 7;
   - DESIGN_MODULE: `#15-adoption-guidance`;
   - UX: `#1a-constitutional-authority-rule`, `#13-adoption-guidance`;
   - WRITING_GUIDE: `#current-surface-writing`;
   - IDENTITY: `#release-version-boundary`;
   - TRAVERSAL: `#closed-profile-signature-fourteen-members`;
   - the ten authority compressions, unresolved, with a proposed supersession by projection.
4. **Modal-force convention (FR-02, FR-07).** The corpus writes the predecessor's "must" and "shall" in the indicative. Does that conserve modal force, or does each conversion need a proposed replacement?
5. **UX compliance-test conflict.** Which of the two UX compliance tests governs. UX §15 applies the stricter one until the product owner rules.
6. **Earlier owner points (PLAN §7).** MT-9, MT-2, B21, occ-24, and the ported-part review policy for the six named ports (`ports.md`).
7. **Step 4 scope.** Whether to fund the rest of the encoding (G5 to G13, and the unencoded parts of G1 to G4) and its fidelity review.

## Still needed before any acceptance claim

- **A cross-family review** of the frozen candidate, requested through the product owner with the exact commit. It must also include:
  - the integrated assessment, closure checks J53 to J55, over REDUCTION §3 and §4;
  - a re-review of the step 7 repairs.
- **Desk traces** of the remaining declared paths, or a decision to accept the narrower evidence.
- **Actual-use evidence** for criterion 4, if the product owner wants criterion 4 evidenced.
- **The product owner's decisions** listed above.
