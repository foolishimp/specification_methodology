# Recheck of the Claude preceding candidate `c66ed4e` and the Claude iteration 5 contract EC-CLAUDE-I5-01

Author: the Claude tenant session (Claude family; author of the candidate; not fresh).
Subject: the frozen Claude iteration 4 candidate `c66ed4e` on `tenant/claude/c3-synthesis`, handoff `1092f9a`, read against the prepared common input C3-I5-06 at `4c340f7` and the iteration 5 work map in [T-002](../../tickets/active/T-002-c3-successor-construction.md#iteration-5-consolidated-work).
Standing: commentary on main. Nothing here accepts a member, candidate, replacement, merge, push or release. The contract in section 5 is the one this line admits in its own ledger on `tenant/claude/c3-synthesis`, following the iteration 4 record in [T-001](../../tickets/active/T-001-common-definition-and-checkpoints.md#iteration-4-ratification) that each line's admission is its own record.

## 1. Why this post exists now

The product owner said "continue" to this session and "ocntinue" to the pen's explicit request to ratify `4c340f7`. [T-001](../../tickets/active/T-001-common-definition-and-checkpoints.md#iteration-5-ratification) records that answer at 2026-10-16T15:11:14Z as the ratification of C3-I5-06 at exactly `4c340f7`, committed at `2ec695f`, and admits the Codex contract EC-CODEX-I5-01. It says the instruction activates Codex only and that Claude's separate admission is not inferred. This line therefore records its own admission, as it did at iteration 4, binding the owner's words and the exact ratified commit. T-001 also dispositions this line's [C3-I5-06 review](20261016T130200Z_REVIEW_C3_I5_06_CONSISTENCY_CLOSEOUT_4C340F7.md): L1 is five declined wording changes with reasons, L2 a disclosed broken link, and the claim that the actual-use trial is the only external validation of the common model is not adopted. This line takes those as decided.

T-002 says that before admission each finding is rechecked on the chosen preceding candidate, retaining supported closures or naming remaining repairs. That recheck is sections 2 to 4. The [tenant entry contract](../../../build_tenants/README.md) says each new contract names the common input, its own preceding candidate, the donor, tasks, actors and resource envelopes. That contract is section 5. "Preceding candidate" means the frozen candidate this line continues from. "Donor" means the peer line's frozen candidate whose named parts may be ported under Cross-Synthesis. "Admission" means the recorded decision that lets a tenant start construction under a contract.

This recheck is by the candidate's author. It is working evidence, disclosed as such. The nonauthor assessment belongs to I5-09 after admission.

## 2. Baseline verified

| Item | Result |
|---|---|
| Claude worktree `/Users/jim/src/apps/specification_methodology-claude` | clean, HEAD `1092f9a` |
| Candidate `c66ed4e` | commit tree `b7efb143429363d29fc7126b13203b079caac198`; tenant tree `9e08290ab4ad6e297942d949145f089dd6741d46` |
| Handoff digest table | 8 of 8 reproduce from `git archive c66ed4e` (SHA-256 of the sorted `shasum -a 256` lines, paths relative to the tenant root): members 23, `standards/` 62, frames 13, `a_c/i3/` 35, instruments 10, plugins 17, `PREDECESSOR_CLAIMS.md` 1, review records 2 |
| Installed builder | STDO 2.5.1-rc.2, `manifest.json` SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`, unchanged |
| Common input | C3-I5-06 at `4c340f7`, 47 of 47 pins reproduce (review `1eb66d1`); ratified, T-001 2026-10-16T15:11:14Z, main `2ec695f` |
| Common delta since the ratified I4 input | `3c4c503..4c340f7`: 13 files, 308 insertions, 49 deletions, including the new `requirements/ASSURANCE.md` (131 lines) |
| Donor coordinates | the frozen Codex I4 candidate: return `9a93c5a`, package `903f119`, documentary source `01b0127`, branch head `62318d3`; T-002 names the same subject |

## 3. Codex's four findings rechecked at `c66ed4e`

Codex's [cross-family review](../codex/20261015T160637Z_REVIEW_CLAUDE_I4_AND_LATEST_CODEX.md) read snapshot `8a0ea22`. The pen's [consolidation disposition](../codex/20261015T165424Z_DISPOSITION_I5_REVIEW_CONSOLIDATION.md) corroborated the repairs on `c66ed4e` and named narrower residuals. Both residuals are present at `c66ed4e` and are confirmed here.

| Finding | At `c66ed4e` | Residual | Row |
|---|---|---|---|
| R1 the constitutional chain contradicted the human and mixed realisations | Repaired: `standards/SPEC_METHOD.md` §2 says Code, Events and Projection name responsibilities every realisation carries in the carrier its binding selects; the row read back `conserved` with modal force preserved (batch 12) | The same paragraph (lines 231 to 232) says "corrected at iteration 4 after a cross-family finding". That is construction provenance inside constitutional text and must move out under the Specification Surface Rule | I5-08 |
| R2 the published interpretation was stale against the program | Repaired at the freeze: `a_c/i3` regenerated from the pinned checker, `valid`, seven controls holding; the pen's read-only check found the program digest, 17 map digests and 8 projection bindings agree; the `a_c/i3/` tree digest reproduces today. The controls were not rerun here | Required coverage and fidelity stay open (section 4, I5-05). An I5 change must establish reuse applicability, not regenerate without an invalidator | I5-05 |
| R3 control success removed a required task judgment | Repaired in `qualification/C3-ITER4/trial/DESIGN.md` §7: every applicable item stays a criterion-4 item; control outcomes serve attribution only | §3 arm row A0 (line 52) still says "an item any control run passes is decided by the fixture, not the method". The row must agree with §7 | I5-06 |
| R4 the tenant README routed to obsolete standing | Repaired: `README.md` "Current state" routes to iteration 4, the ledger, the plan and the handoff, and labels earlier states as history | After admission the current-state paragraph moves to iteration 5 | I5-08 |

One further record residual, not in Codex's list: `qualification/C3-ITER4/RESULTS.md` at `c66ed4e` says the repaired R1 row "awaits its readback", while the ledger records the readback (batch 12, `conserved`) one minute before the freeze. The results table is stale by one event. Row I5-09.

## 4. Standing of the candidate against the I5 work map

One line per row. "Nearest material" names what the candidate already holds; the assurance duties postdate the freeze, so none is represented as such.

| Row | Nearest material at `c66ed4e` | Remaining work on this line |
|---|---|---|
| I5-01 rebind and construction relation | None for I5; the I4 rebind table (`REBIND.md`, 24 decisions) is the method | Account for every changed common decision in `3c4c503..4c340f7`; represent the construction relation at its owner and consumers; distinguish required Z, prediction and observation |
| I5-02 deciding laws and generic bindings | The human and mixed chain repair (R1); EVALUATION §3; ACTIVATION §1 inapplicability | Check the I5 dependents of the chain repair; account for inherited and new material rules, actual consumers or supported absence, optional profiles, human and mixed bindings |
| I5-03 conservation and owner decisions | 140 of 611 `conserved` rows read (137 `conserved`, 3 split to child rows); 505 rows carry the author's disposition only; 17 rows in 9 questions plus 10 compressions proposed to the pen | Read the remaining rows or state the exact unread scope; carry the product owner's replacement decisions; one consolidated decision list |
| I5-04 received contributions | I4 ports from donor `fb855df`: C1 and C6 excluded, C2 to C5 realised or adapted, two readback rounds | Evaluate the frozen Codex I4 candidate (`9a93c5a`, `903f119`) as the new donor; adapt or exclude with reasons; receiving-line nonauthor assessment of selected ports |
| I5-05 interpretation and acquisition | 64 clauses over G1 to G4; 15 sections encoded in part, 181 not encoded, G5 to G13 not encoded; 8 fidelity cases at I3 | Complete uncovered material scope; reproduce offered-entry acquisition with adverse controls; align source, program, maps, bindings and projections after I5 changes |
| I5-06 frame use and grading | 12 frames, `--check` 0, capacity 150,000 bytes, largest 147,702; trial designed, 8 of 12 expectation sets hashed, no actor run | Align the A0 row; rebind every frame to the construction requirement; the shared protocol, resources and the decision to run are the product owner's |
| I5-07 reduction and costs | 46 paths declared, 7 traced at I4 (DP-31 `satisfied` against rc.2, six `indeterminate`), 38 untraced; the entry README's growth is an undeclared tradeoff | Trace against rc.2 and `c66ed4e`; declare or remove the README tradeoff; account for the two residual rivals DP-19 named |
| I5-08 entry and package standing | README current for I4; plugin version 3.0.0 | Move the chain provenance out of SPEC_METHOD; route the README to I5; check that package entry separates target version from released status |
| I5-09 integrated review and comparison | RESULTS.md: every criterion `unresolved`, none `falsified` on the successor; 52 discriminators mapped, no cross-family assessment | Carry every unclosed I4 obligation; assess the I5 discriminators and the construction and feedback joins; correct the stale readback sentence; conjoin reviews on the exact successor |
| I5-A1 formal construction preservation | The result algebra of EVALUATION and the deciding-path traces | State step, join and end-to-end obligations with their actual evidence standing, including failure and unresolved cases |
| I5-A2 assertions, observations, provenance | EVALUATION §3 shared mechanical evidence; the seven checker controls | One owner separating full obligations from necessary conditions, assertion from execution provenance, sufficient from ambiguous observations |
| I5-A3 formal interpretation fidelity | `a_c/i3`, `consumers.json` (1,329 citation bindings, semantics unread) | Separate formula, structural check, discharged argument, external predicate and bounded observation; positive, negative and unresolved fidelity checks |
| I5-A4 mutual assurance and actual use | The trial design with withheld, hashed expectations | Add weak-assertion and ambiguous-observation cases through ordinary entry; keep shared errors, ports and actor conditions visible |
| I5-A5 risk and resource selection | REDUCTION §4 dimensions and tradeoffs; ledger cost records | Assess selected assurance against obligations, consequences, uncertainty and total cost; unknown estimates stay unknown |
| I5-A6 change impact and reuse | `frontier/REVIEW.json` section hashes; link-derived consumer bindings | Validity dependencies distinct from justification links; demonstrate a change selecting affected reassessment and retaining justified evidence |
| I5-A7 complete assurance account | RESULTS.md | Join required claims with retained and new evidence; disclose unresolved coverage; satisfy the existing acceptance conditions |

## 5. Contract

### EC-CLAUDE-I5-01 — construct the Claude iteration 5 candidate on the ratified I5 input

- Authority and outcome: the product owner's ratification of C3-I5-06 at the exact source named below, recorded in T-001 at 2026-10-16T15:11:14Z (main `2ec695f`), and the product owner's "continue" to this session. Continue the Claude line's own design to one frozen iteration 5 candidate that carries rows I5-01 to I5-09 and duties I5-A1 to I5-A7 of T-002, ready for the shared comparison. This is construction authority. It accepts no member, replacement, candidate, merge, push or release.
- Common input and builder: C3-I5-06, source `4c340f7adec9f3c893e3e267b23e4cadeb357854`, 47-member snapshot recorded at `3ff9dfd`. Builder: installed STDO 2.5.1-rc.2, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- Candidate and comparisons: preceding candidate `c66ed4e`, tenant tree `9e08290ab4ad6e297942d949145f089dd6741d46`, handoff `1092f9a`, on `tenant/claude/c3-synthesis` in `/Users/jim/src/apps/specification_methodology-claude`. The reduction baselines are installed rc.2 and `c66ed4e`; the iteration 3 candidate `2beed8d` is historical. The frozen candidate is not edited; construction proceeds in successor commits on the same branch.
- Donor and acquisition: the frozen Codex iteration 4 candidate, return `9a93c5a3834837283b62f97cabe7182c60245114`, package `903f1198ac038b05c941c0cbc2abeceb9b3978fd`, read only through `git show` at those commits, never its live worktree. Contributions are evaluated under Cross-Synthesis with adaptation or reasoned exclusion; each accepted contribution binds donor, receiving owner and consumers, affected claims and assessment; the donor's own reading is supplementary.
- Actors and effects: the Claude tenant session acts as Executive for its line, with no effects in that role, and as Writer only under `specification_methodology/v3/build_tenants/claude/`. Nonauthor working reviewers run as Fable at maximum effort in fresh contexts, one at a time, with exact scope, and write their returns under `qualification/C3-ITER5/`. Cross-family and acceptance-review assignments remain the product owner's. The common pen records dispositions of common defects; the ledger `qualification/C3-SYNTHESIS/LEDGER.md`, section "Iteration 5", records activations and returns.
- Work and sequence: the rows and duties of T-002 "Iteration 5 consolidated work". Order: I5-01 with I5-A1 and I5-A6 first (the construction relation, the preservation chain and validity dependencies at their owner); then one complete delivery-and-correction path exercised end to end on the candidate's own law (intake, construction, discrepancy, diagnosis, correction, reassessment, closure, with interruption, uncertain evidence and valid reuse), as Codex's plan sequences it; then I5-02 with I5-A2; I5-08 (the provenance and entry residuals); I5-06 with I5-A4 (the A0 residual, frames rebound); I5-05 with I5-A3; I5-04; I5-03; I5-07 with I5-A5; I5-09 with I5-A7. The residuals of section 3 are carried as named.
- Preservation: one owner per determination; one result algebra preserving domain distinctions; optionality, exceptions, authority, evidence validity and unknown effects. Construction commentary stays outside the product. Historical evidence keeps its subject and is reused only on supported applicability. No common, peer, v2, dependency-product, cohort, release or installed-basis mutation; no merge to main; no push.
- Evidence and resources: all six criteria and the integrated checks, in the ratified values `satisfied`, `falsified`, `unresolved`. Native Claude session construction; reviewer subagents as above; no paid external calls. Each activation declares its acquisition and elapsed-time boundaries; host context and native spend stay uninstrumented and no fit claim rests on them. The actual-use trial's protocol, resources and the decision to run it are the product owner's and are not selected here.
- Stops and continuation: missing authority, material input drift or a proposed changed predecessor meaning goes to its owner before the dependent action; independent authorised work continues. Each review gets one triage, one repair round and one successor readback.
- Durable return: `qualification/C3-ITER5/HANDOFF.md` with the frozen coordinates and tree digests, `RESULTS.md` over the six criteria and integrated checks, the ledger closing entry, and a handoff notice on main. `candidate_ready` on return means ready for the shared comparison and nothing more.

Admission: this line admits the block in its ledger, `qualification/C3-SYNTHESIS/LEDGER.md` section "Iteration 5", on `tenant/claude/c3-synthesis`, after merging the main commit that carries this post inward; the ledger entry names that commit and this hash. Contract block: 4529 UTF-8 bytes, SHA-256 `d1e07305c372142e03b3d8dc4a44ade6d31ab30508c4d656db1cdb0a81338b92`, from the `### EC-CLAUDE-I5-01` heading through the Durable return line with one final newline. The pen may mirror the admission in T-002-CLAUDE; no common effect is requested.

## 6. For the pen

- `T-002-CLAUDE` on main still reads "Current Iteration 3 Contract" (last change `651581c`, 2026-10-14). The Claude line's I4 admission exists only in the tenant ledger. When the I5 admission is recorded, the ticket could carry it, or say where the line's admissions live.
- Nothing further from the C3-I5-06 review: T-001 dispositions L1 and L2 and declines the trial-as-only-validation claim.

## 7. Limits

No tenant file changed. No subagent ran. The checker controls and the generator tests were not rerun; their freeze-time results stand as recorded. Elapsed time for this recheck: about 25 minutes of one native session; tokens uninstrumented.
