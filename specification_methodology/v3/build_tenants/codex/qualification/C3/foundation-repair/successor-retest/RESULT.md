# Next actions for the three work states in STATES.json (read-only interpretation of the candidate method)

**Main finding:** the method itself says it can't authorize any of these actions. The Host verified the construction basis `stdo://releases/v2.5.1-rc.2/` (manifest `3d860ff4…2782`). METHOD_ROOT is unreleased candidate source, and the stdo-work skill says "a mutable candidate is no fallback" (`plugins/spec/skills/stdo-work/SKILL.md` §Acquire, lines 31–32). The standards README agrees: "A mutable source head or moving selector cannot replace it" (`standards/README.md` lines 77–80). So every recommendation below is my reading of what the candidate text would require. None of it grants permission to act or claims anything is complete.

## Blockers that apply to all three states

- **No Project Reference-Frame Basis (the per-project rules for this responsibility) was supplied.** The skill says to return the missing binding before any dependent action (SKILL.md lines 20–26). The work/recovery view supplies none ("An absent basis remains unresolved", `frames/WORK_RECOVERY.md` lines 26–28).
- **No record shows the work contract was admitted.** There is no admitting mechanism, contract digest, decision or evidence, and no Product-bound durable result/evidence surface. Without these, admission must refuse or stop (SKILL.md §Establish steps 2–3, lines 86–96). A conversation return is not durable evidence (line 115–116).
- **Strictly, the method's first output in every state is that missing authority.** The actions below are what would be lawful *once* those bindings exist and "original work grant" can be taken as the admitted grant.

## State 1: `uncertain-effect`

- **Next action:** read publication status using the original operation identity `publication-17-4` (for content `revision-4`). The contract lists this as an allowed effect. Basis: "Neither historical intent nor a timeout proves completion or grants a safe repeat. Observe/reconcile…" (WORK_RECOVERY.md line 45). Also: "an unknown effect state cannot be silently treated as no effect" (Computed Classification, lines 291–294).
- **Don't:** republish, or edit the report yet. The state gives no evidence that either is independent of the uncertain effect. Wider effects are withheld "where independence is unproved" (lines 44, 300–301), and idempotence has not been established for this operation (line 45).
- **Keep:** section A complete with its evidence, reusable only for `revision-4` (Condition-Based Closure, lines 419–424). Keep section B as an open obligation, the missing independent assessment, and the attempt coordinates `worker-17/attempt-4`.
- **Unsupported claims:** "published", "not published", "complete" and "candidate ready".
- **After the observation:**
  - *Not published:* repairing B is the next permitted step. Then the exact new revision needs independent assessment before publishing.
  - *Published:* an inadequate, unassessed revision is live. That breaks the contract's required assurance, so it goes back to the owner.
  - *Indeterminate:* return unresolved.

## State 2: `known-failure`

- **Facts that settle it:** an authentic receipt shows `revision-4` was published. The independent assessor (`independent-assessor-22`) returned **falsified**, citing "report/B: missing required limitation". The worker's "candidate_ready" summary is a constructor's report and can't override that: "a constructor's report substitutes for required independent live evidence" is listed as a falsifier (STDO-UP-020, lines 217–222; STDO-UP-007, lines 352–359). "Transport has recovered" says nothing about whether the content is adequate.
- **Next action:**
  1. Keep the falsified verdict and the receipt.
  2. Tell the owner that an inadequate revision was published, which violates "independent assessment … before publication".
  3. Under the existing edit grant, add the missing limitation to B as a new revision (a `local_repair` — the contract is unchanged; the candidate is defective, lines 159–161 and 276–283).
- **Don't:** republish `revision-4`, or treat this as completed.
- **Judgment, not a ruling:** whether publishing a repaired revision still fits "publish one adequate revision" is my judgment. So is whether `revision-4` needs to be withdrawn or superseded. The contract doesn't list withdrawal as an effect, so both are owner decisions (O). Publishing again would also require a fresh independent assessment of the exact new revision.

## State 3: `revoked-grant`

- **Next action:** only observe publication status via `publication-17-4`. The read/observe grant is still in force. Then return to the owner with what was observed.
- **Don't:** edit or publish, even though the worker still technically can. A frame does not create authority from "available capability [or] implementation reachability" (RF-006, lines 324–327).
- **Keep:** the uncertain effect, B incomplete, A's evidence, and the attempt coordinates. Closure is withheld.
- **Open issue:** recording the result durably may itself need write authority, which was revoked. If so, durable recording isn't available, and the owner must re-grant or choose how to proceed. Any further work needs a new owner grant.

## How far I read

I read `TASK.md`, `STATES.json`, `stdo-work/SKILL.md`, `references/PRODUCT_BASIS.md`, `standards/README.md` and `frames/WORK_RECOVERY.md`, which totals well under the byte allowance.

I did not read the full `SPEC_METHOD.md`, `TICKET_METHOD.md`, the definitions of the premises F1–F6, or `STDO_REFERENCE_FRAME_BASELINE.md`. I couldn't check the frame's SHA-256 pins against their source files, because that would mean running commands. The released v2.5.1-rc.2 material is outside the available roots, so I couldn't confirm that its clauses match the candidate's.
