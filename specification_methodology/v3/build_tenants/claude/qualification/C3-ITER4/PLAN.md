# Iteration 4 Plan, Claude Line

Activation plan for the Claude line's iteration 4 (I4) under the ratified
common input C3-I4-03. It is written by the Executive in the main session.
It claims nothing accepted. Every term it uses is defined in the
[I3 plan](../C3-ITER3/PLAN.md), whose conventions (section 3) apply
unchanged unless a line below says otherwise.

## 1. Basis

| Coordinate | Value |
|---|---|
| Common input | C3-I4-03: common specification at `3c4c503d291e7cb19ba21333ba6caf6167be77c9` on `main`, recorded at `a960032`, merged inward at `7c60f32` (spec and entry files byte-identical to `3c4c503`) |
| Ratification | the product owner, 2026-10-15, in session: "ive approved i4, this means that the build tenants may proceed". The common pen records the exact-commit ratification in T-001 and the Claude-line admission in T-002-CLAUDE; both records were pending when this plan was written |
| Preceding candidate | `2beed8d` on `tenant/claude/c3-synthesis`, handoff `96ccdcc` (I3) |
| Donor | the Codex candidate at handoff `fb855df`, package `d490dd6`, read only through `git show` at those commits |
| Comparison subjects for reduction | the installed `v2.5.1-rc.2` (manifest `3d860ff4…2782`) and the preceding candidate `2beed8d` |
| Work list | T-002 "Iteration 4 staging", Claude column, I4-01 to I4-09 |
| Staged plan | `comments/claude/20261015T042323Z_PROMPT_I4_STAGED_PLAN.md` at `fa8e172`, Stage 2, decisions D3 to D9; where it differs from the ratified text, the ratified text governs |
| Checker | the pinned Axiom Indexer `v2.5.1-rc.2`, structural validation only (owner decision, I3) |

## 2. Work items

Each item names its class under Cross-Synthesis (defect, permitted choice,
gap decided in common text, or owner decision) and what this line does.

| Item | Class | What this line does | Return |
|---|---|---|---|
| I4-01 Rebind | gap decided | Bind `3c4c503`; account for every common decision changed since `355aa86` | [REBIND](REBIND.md): effect or reasoned no-change per decision |
| I4-02 Foundation and ownership | evidence gap | Source-first assessment of the family tables not sampled by WC-2, in particular EXECUTIVE_BASELINE, DESIGN_MODULE and ODD, and the shared-owner and consumer joins; categorical claims bound to a declared demonstration or marked unresolved | `reviews/FAMILY.md` by a nonauthor Sonnet reviewer; repairs |
| I4-03 Ports | gap decided | Evaluate C1 to C6 against the donor; select, adapt or exclude with a reason; one receiving owner each; nonauthor readback of every port, including the six I3 ports never compared with their source | [ports.md](ports.md) |
| I4-04 Conservation | defect (evidence) | Re-assess by both texts the rows judged from deltas at I3; record the modal-force judgment of every row whose predecessor "must" or "shall" is written in the indicative, under the ratified test; supply the pen one list of proposed replacements by question | `reassess/` and a post to the pen |
| I4-05 Interpretation | evidence gap | Extend `a_c/i3` towards the required coverage (every material owned determination); fidelity cases per member for criterion 5; checker run; report uncovered scope exactly | `a_c/i4/` or extended `i3/`, fidelity record |
| I4-06 Frames and actual use | defect (frames); owner decision (criterion 4) | Task-coverage map for the frames; family-table rows and result maps (TO1); F5 `kind` label; active-context fit rule; criterion 4 only under D5 | frames, `paths/`, trial record if funded |
| I4-07 Reduction | defect (rebind) | Preceding candidate becomes `2beed8d`; results per path as `satisfied`, `indeterminate` or `falsified`; trace the remaining declared paths or justify groupings | `REDUCTION.md`, `paths/DESK-TRACES.md` |
| I4-08 Package and routing | defect | Stale standing text after rebind; design records that still name `31f28f9`, the I3 input or the undecided port policy; identity and packaging limits kept | the edited files, listed in the ledger |
| I4-09 Review | evidence gap | Discriminator self-map on the successor; satisfied, falsified, unresolved per criterion per member; one nonauthor working review, expectations first, including the I3-8r repairs and every port; repair; readback; freeze; handoff | `reviews/`, `HANDOFF.md` |

Order: I4-01, I4-08 (text), I4-03, I4-04, I4-02, I4-06, I4-07, I4-05, I4-09.
Items that run out of budget are recorded as unresolved with their exact
uncovered scope; nothing is sampled silently.

## 3. Conventions added for I4

- Every activation declares three separate facts about its actor: model
  family, authorship of the subject, and freshness of task context. The
  Codex line's part in the donor material is disclosed wherever a port is
  assessed.
- A nonauthor reviewer of this candidate is Claude-family. It reads the
  donor only at the frozen commit and only for the port it assesses.
- Results use the ratified three values for obligations: `satisfied`,
  `falsified`, `unresolved`. A missing assessment is `unresolved`, never
  `falsified`.
- The shared head-to-head protocol is the pen's. This line builds no
  expectation of it into any frame.

## 4. Budget

D8: sequential work in the main session; at most one Sonnet subagent at a
time with an exact file and line scope; no parallel agents. Variances are
recorded in the ledger as they occur.

## 5. Open owner decisions carried

- D5: criterion 4 for this line. Until decided, criterion 4 is
  `unresolved` and the candidate is ineligible for a qualified choice.
- The proposed replacement relations (15 rows and 10 compressions at I3,
  plus any from I4), to be decided from the pen's consolidated list.
- The UX compliance-test replacement; UX applies the stricter reading
  under the ambiguity rule, which is not acceptance of a replacement.
- Identity and packaging of the released interpretation.
