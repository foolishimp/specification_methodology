# Expectations: review of the C3-I4-01 common specification at `5d2b257`

Written and committed before opening the subject. This is Stage 1 step 4
of the iteration 4 plan (`20261015T042323Z_PROMPT_I4_STAGED_PLAN.md`,
revision 4 at `fa8e172`).

## Subject and baseline

- Subject: the common specification `specification_methodology/v3/specification/`
  at the frozen commit `5d2b257`, read against the closed I3 input `1fce537`.
- Recording: `51ccfd6` (T-002 snapshot, handoff). I will check the recording
  against the frozen commit, not against the working tree.
- Also in scope, because the handoff routes to them: the T-001 and T-002
  ticket changes, `build_tenants/README.md`, `v3/AGENTS.md`, `v3/CLAUDE.md`,
  and Codex's divergence classification post `20261015T054112Z_…`.

## Opened before these expectations

Only Codex's handoff `comments/codex/20261015T054313Z_HANDOFF_C3_I4_01_COMMON_SPECIFICATION.md`,
the `git log` and `diff --stat` of the two commits, and texts I authored
(the staged plan, my two I3 review posts). Not opened: the specification
diff, the ticket diffs, the routing files, the divergence post, Codex's
expectations post.

## Standing

Cross-family, nonauthor of the common text, interested party twice over:
I built the competing Claude candidate, and I authored the port-review
and comparison policy (D4, D6, Stage 3) that the proposal adopts. My
reading of those adopted policies is not independent acceptance of them;
the product owner ratifies them. Budget: bounded reads, one mechanical
check, no subagent.

## What I expect to find

- **E1 Classification.** Each of the ten divergences of the plan carries
  a class and a reason. Expected: 1 gap plus owner decision; 2 owner
  decision; 3 gap; 4 permitted design choice; 5 gap plus owner decision;
  6 gap; 7 partly answered, Claude rebind defect; 8 permitted design
  choice; 9 owner decision plus the binding question; 10 owner decisions.
  Every reserved owner decision is named with the point at which it is
  decided, at ratification or before admission, not left floating.
- **E2 Conservation and modal force.** One operational test, stated once,
  comparing the permitted and required decisions with force, triggers,
  conditions and exceptions; indicative wording admissible as binding;
  no blanket convention counted as equivalence. Two assessors applying
  it to the same row would reach the same class.
- **E3 Owed evidence and work items.** The evidence every candidate owes
  in Stage 2 is named: six criteria, 52 discriminators, J53 to J55,
  conservation record, interpretation coverage, frames by task coverage,
  reduction, actual use. The nine work items name a tenant and a done
  condition each, and together cover CX-03 to CX-09, the Claude handoff
  gaps, the ports, and the evidence.
- **E4 Port authorship.** Received contributions retain authorship; the
  acceptance-bearing assessment is by a receiving-line nonauthor; donor
  reading of its own contribution is supplementary; a repair requires
  readback of changed material and affected dependencies on the
  successor. Same meaning as D4 and Stage 3, no new machinery.
- **E5 Comparison.** Eligibility on all six criteria and the integrated
  checks; missing evidence blocks and qualifies nothing; missing is
  distinct from falsified; the no-qualified-choice outcome exists;
  ranking by non-blocking residuals over comparable coverage, then the
  owner's reasoned preference.
- **E6 Agreement.** Product, requirements, conformance, frame basis, the
  routing files and both tickets say the same thing about ratification
  (an owner act on an exact commit), admission (recorded in the ticket
  against the signed commit), the three stages, and where candidates and
  donors are named (the ticket, not Product). No history or proposal
  narration in live law.
- **E7 Writing.** Every new term defined at first use; exact modal force;
  the role, not the person's name, in specification text; no markers of
  provisional standing in active surfaces.
- **E8 Smallest change.** No HOW in WHAT: no file count, capacity figure
  or result representation imposed; the ten pillars, the 52
  discriminators and the three integrated checks keep their meaning;
  nothing a tenant depends on is removed except the historical table.
- **E9 Verification.** The 19 recorded member hashes reproduce from
  `5d2b257`. Links in the changed files resolve. I will rerun the hash
  check; the link pass I will rerun only if cheap, else record it as not
  rerun.
- **E10 Process.** Stage 1 steps 1 and 2 of the plan did not precede step
  3: no divergence list from Claude, and no Codex review of the Claude
  candidate `2beed8d`. Expected: the tickets carry that review as owed
  before Claude's Stage 2 admission, since Claude's repair list depends
  on it; otherwise this is a finding.

## Verdict form

`no blocking defect`, or `blocking defects` each with the smallest
repair; non-blocking findings listed; every expectation E1 to E10 marked
met, not met or not checked. Nothing is accepted here. Ratification is
the product owner's act.
