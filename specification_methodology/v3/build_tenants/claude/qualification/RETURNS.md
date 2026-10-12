# Claude Tenant Returns

Tenant-local return record. Under the rule that each tenant writes only inside
its own build tenant, returns after 2026-10-11T07:00Z are recorded here. The
ticket `stdo_3/.ai-workspace/tickets/backlog/T-001-CLAUDE-principles.md`
carries the earlier returns (initial author, first successor, Codex
cross-review disposition) and is not updated by this tenant; the common pen
may mirror this record there.

Builder basis for every entry: `stdo://releases/v2.5.1-rc.2/`, manifest
SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Common inputs: snapshot `C1-inputs-20261011-02`, 16 members.

## Candidate lineage

| Candidate | SHA-256 | Lines / words | Frozen | Standing |
|---|---|---|---|---|
| Initial | `329fe4228eb9d6e2a5f79bf597fa25a82d6a798a30146a93dd5773678c73d0bb` | 400 / 4,402 | 2026-10-11T05:58:13Z | superseded; Codex review `CHANGES REQUIRED` |
| First successor | `454770386c4cbe7c8aa2269afeafa3084a26ed0960774fae25e577a407f900a2` | 454 / 4,941 | 2026-10-11T06:48:18Z | superseded; two review items still open |
| Second successor | `28c9b1275ca23c53d80cf64afa45acf0d25ce8aa7daddd62b5c7aaf490b2b7ec` | 484 / 5,214 | 2026-10-11T07:48:06Z | current; not independently reviewed |

Each predecessor's bytes are retained in the activation scratchpad; the
repository holds only the current candidate at
`stdo_3/build_tenants/claude/design/PRINCIPLES.md`.

## Second successor return, 2026-10-11T07:48:06Z

Activation: Claude Writer, own tenant only, authorised by Jim ("go") after
the Codex posted review
`stdo_3/build_tenants/codex/reviews/20261011T072147Z_REVIEW_claude_c1_principles.md`
(SHA-256 `189aa62232dbbd7c530e05d4194523cbe05f3bf25e433eb7c8302fc4ddeb90af`,
92 lines), which binds the initial candidate `329fe422…d0bb`.

Disposition of that review's four findings against the first successor:

| Finding | State in first successor | Action here |
|---|---|---|
| 1. Cost fields as universal ritual | already applied (selected-by-claim) | none |
| 2. "Never semantically decidable" | already applied (AC-019 decision contract) | none |
| 3a. Contradictions against retired `-01` text | already applied (withdrawn) | none |
| 3b. ABG handoff and post-mortems described as tuple members | open | restated: the 504.8 MB figure and the post-mortem lessons are attributed to the Claude plan post and the two plan posts in the tuple, as indirectly reported historical observations; primary sources deferred to C2 and not reacquired |
| 4a. Sole-output premise | already applied (Pr2a, step-produced facts) | none |
| 4b. P1 and P6 independence asserted, not argued | open | non-entailment arguments added: P1 (vary only the interpretation contract with purpose, identity, evidence and authority fixed; RF-008 states the law); P6 (a finite actor satisfying C and P1–P5 can still accept a green label as acceptance or treat capability as permission; UP-022 and RF-006 are the separate commitments that forbid it) |

Changes to the candidate: header status and lineage; one paragraph after P1;
P6's standing paragraph; gap 3 attribution; the mechanisms paragraph's
attribution; one lineage bullet in the residuals. No other section changed.

Verification at freeze: 93 links resolve, 90 `stdo://` fragment-link
occurrences to 65 unique installed headings; no trailing whitespace; zero
occurrences of the stale "in the tuple" attributions; snapshot 16/16
unchanged at start (07:47:26Z) and at freeze. Bytes changed by this
activation: the candidate and this file only.

Resource observation: start 2026-10-11T07:47:26Z, end 07:48:06Z, 40 seconds
wall by `date -u`; generated-token counters unavailable on this host against
the 60,000 planning allowance.

Work result: `candidate_ready` / `satisfied` for the declared output. No
acceptance claimed. Independent review of this successor is Jim's to
authorise.

## Cross-review of the Codex tenant, 2026-10-11T06:53:37Z

Performed under the earlier grant, before the tenant-only rule. Closed result
and findings:
`stdo_3/build_tenants/codex/qualification/C1_REVIEW.md` (SHA-256
`40700da54763fdeac4103c2f3c0530e2266070ce6bcb57cd2c3a8d3eab9ba8be`), posted
verbatim in this tenant at
`../reviews/20261011T065337Z_REVIEW_codex_c1_principles.md` (SHA-256
`351e8e86f7927431f0475d02f34da2564a474fbba7702287ef764b027dcf46ef`). Subject
`52fbd93ad31476823d5bed7a991ee85b5d8e8e188037fcdb80ac052540051611`. Result:
`satisfied` on derivations, hypotheses, mechanisms, boundaries, prose and cost
reporting; `falsified` on source-recovery completeness for seven items;
recommended `local_repair`. 4 minutes 43 seconds wall.

## C3 build pass return, 2026-10-11T09:42:50Z

Activation: Claude Writer, own tenant only, on `tenant/claude/c3` cut from
`main` at `00be6b8` in the Claude sparse worktree, authorised by Jim
("ok build it out stdo 3.0"). Snapshot `C1-inputs-20261011-03` verified from
input commit `80b46944f1c1` at activation (16/16). Builder basis verified
valid.

Delivered: the tenant HOW (`design/DOCUMENT_STRUCTURE.md`) and a first
complete draft of the seven-file document set under `standards/`, 1031
lines in all. Every clause names its requiring principle and its rc.2
disposition (conserved, reframed, superseded, new) per UP-015 applied to the
corpus; each document ends with a source-dispositions table.

| File | SHA-256 | Lines |
|---|---|---|
| `standards/CALCULUS.md` | `879fb9dd7c8f59c866f2e9564e685dd57611bbeabd2806dc40d9b0ea5fb582ad` | 223 |
| `standards/CONFORMANCE.md` | `d588fdab7ee6f0875697e6e49493bf98a572e43ec6ccab38ee6c9ed2eecb8df2` | 65 |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` | 143 |
| `standards/FOUNDATIONS.md` | `5f5e7ab3b820657ec5992aa3eb9c0bc7a6f937dbe9ec0f36eb75014429efed80` | 214 |
| `standards/PROFILES.md` | `d84af888b321b096872c6db6910cf6c8980b733170ae82be9bda453a99446a41` | 83 |
| `standards/README.md` | `333f4924f379ea909d29dcdd7fecbb05c064fee718718c0d030154ba7d5249d2` | 38 |
| `standards/SPEC_METHOD.md` | `453970e8e879f36ad78e1c2e8b71a9791f7fac86397a6208602a823a00278851` | 173 |
| `design/DOCUMENT_STRUCTURE.md` | `dbba88c7a7f75ae60a3d0d0e21bcc63e54af44c4adf8cc3bf868aae943a0172d` | 92 |

Verification at freeze: 162 links resolve across the set and the tenant
README, including every `stdo://` fragment against the installed rc.2
headings; no trailing whitespace; profile-term boundary holds in tier 1 and
2 outside disposition tables and the hypotheses list. No a_c program, trial
or independent review exists for this draft; nothing here is executed
steel-thread work. Conformance cases are all `not run`.

Resource observation: declared allowance 150,000 generated tokens / 4 hours;
start 2026-10-11T09:35:30Z, end 2026-10-11T09:42:50Z, elapsed 7 min 20 s wall by `date -u`;
generated-token counters unavailable on this host.

Work result: `candidate_ready` / `satisfied` for the declared output. Next:
T1 (FOUNDATIONS, CALCULUS §1–3, EVALUATION §1–4) frozen as a thread
increment, a_c encoding, and the T-01 context-cap case run by an actor other
than the author under an authorised review.

## T1 thread return, 2026-10-11T11:28:41Z

Activation: Claude Writer, own tenant only, on `tenant/claude/c3`,
continuing the C3 activation on Jim's "continue". Start not stamped
separately; bounded below by the C3 return end, 2026-10-11T09:42:50Z.

Delivered, in two commits:

- `e984e48`: the T1 increment frozen at `cc1d29d` (FOUNDATIONS
  `5f5e7ab3…ed80`, CALCULUS `879fb9dd…82ad` §1–3, EVALUATION
  `fc063460…246d` §1–4); the pinned Axiom Indexer subject verified member by
  member from the tag commit's tree against its release record, seven of
  seven plus the inventory aggregate; the a_c.text program
  `urn:stdo-3:claude:program:a-c-text:t1` (74 symbols, 80 clauses, 8
  residuals; file `9dfa2e06…bd4c`, canonical `743e07fa…e0c0`) validated with
  zero diagnostics and its map; the bounded-activation frame projected in
  both modes; the T-01 case design (`cases/T-01/CASE.md` as read by the
  constructors `53cd9f6f…082a`; `fragment.py` `02c71289…3eda`). Record:
  `a_c/t1/README.md`.
- this commit: two T-01 constructor runs by fresh contexts of this model
  family, one per cap, each writing one record and nothing else:
  run A (160,000 bytes) `96fb0350…01ca`, composite satisfied, 22 of 22
  routes, 57,047 bytes charged, 9 min 23 s; run B (6,000 bytes)
  `16106f3f…2e58`, composite out_of_frame, existence 22 of 22, consistency
  19 of 22, three pairs measured over the cap and not read, escalation named,
  26,091 bytes charged, 12 min 23 s. CASE.md now carries the run table and a
  correction note (`27c7a1b7…d1da`).

Candidate findings the runs raised against the frozen documents, recorded
and not repaired, so the assessor sees the subject the constructors saw:

- one clause, two standings: P5 says it conserves RF-012 and AC-007 while
  CALCULUS §3 and §8 say the core algebra supersedes them; P4b says conserves
  and, in the same sentence, reframed. FOUNDATIONS §1 gives a clause one
  standing and says an undisposed standing blocks qualification. This is the
  first finding for the T1 successor.
- P4a's retained list omits "provenance", which AC-016 retains.
- CALCULUS §3 says RF-012 and AC-007 "name the same five outcomes"; AC-007
  names result conditions, not the five members.
- the case's "exceed 600,000 bytes" figure is wrong for the §3 route set
  (423,548 bytes); the discriminator's premise holds unchanged.

Rulings the runs request from the case owner: whether a resident tenant
paragraph is charged again per step (run B R-1; it decides two of the three
out_of_frame routes); the order among non-satisfied members for a composite
stop state (run B R-2); whether the step or human authority selects among
the fit options, since RF-014 vests it in human authority and CALCULUS §2
lists it as the step's own choice.

Encoding residuals (8, in the program): T1 boundary forward references;
'material' undefined; fit test not operationalised; independence arguments
one sentence each; formal fragment carried not constructed; indeterminate
versus out_of_frame boundary; judge of lawful compression unnamed; rc.2
routes outside the program basis.

Resource observation: the C3 allowance (150,000 generated tokens, 4 hours)
remains the declared one. Constructor spend as reported by the harness:
run A 164,925 tokens, 41 tool uses; run B 176,621 tokens, 27 tool uses;
the two ran in parallel, 12 min 23 s wall. The author's own generated-token
counter is unavailable on this host; wall for this pass is at most
1 h 45 min 51 s from the lower bound above to this stamp, including a
context compaction.

Verification at freeze: tenant gate green over 16 files, 271 links
including every `stdo://` fragment, no trailing whitespace; run records
are excluded from the gate as constructor output.

Work result: `candidate_ready` / `satisfied` for the declared T1 outputs.
T1 is not closed: closure needs an authorised independent assessment of
runs A and B under the case's five expected distinctions, an
author-independent fidelity judgment of the program, and Jim's rulings
above. Next after that: the T1 successor applying accepted findings, then
T2 (SPEC_METHOD, CALCULUS §4–7).

## T1.2 thread return, 2026-10-11T13:25:58Z

Activation: Claude Writer, own tenant only, on `tenant/claude/c3`, on
Jim's relay of the review of `eca8cef` (receipt processed
2026-10-11T13:06:07Z, which bounds the start).

Delivered, in two commits:

- `cee1157`: the received review recorded verbatim with per-finding
  dispositions under `qualification/received/`; all four findings and the
  three ruling narrowings accepted after source checks; FOUNDATIONS and
  CALCULUS repaired at source (one standing per clause, provenance in P4a,
  conjunctive step-produced-fact definition, material defined, context fit
  measured before any read, fit options combinable with selection vested
  in the step under its grant, compression preservation a claim,
  out_of_frame against indeterminate, composite by declared conjunction,
  formal fragment new with its interpretation); EVALUATION unchanged.
  T1.2 identified by digest (FOUNDATIONS `2f15c6c1…38a22`, CALCULUS
  `d708e76c…aee0c`, EVALUATION `fc063460…246d`). Program regenerated
  (75 symbols, 86 clauses, 5 residuals; file `f5d653e2…1f43`, canonical
  `c3f482ab…8d49`), validated with zero diagnostics against the same
  byte-verified pinned subject, both projections regenerated. Successor
  fixture `cases/T-01/CASE-2.md` with `step_actor.py` (a fresh headless
  actor per reading step, whole context measured and logged before the
  actor exists) and `STEP_CARD.md` (the judgment contract); caps reset
  against the measured single-step closure of 49,938 bytes: A2 20,000,
  B2 8,000.
- this commit: two CASE-2 runs by fresh coordinator contexts of this model
  family, step actors `claude-sonnet-5-5`, each writing one record beside
  the instrument's log and step files:
  A2 `584bc3d0…9219`, composite satisfied, 23 of 23 routes; closure refused
  at 49,948 bytes with no actor started; 8 actor steps, largest 12,996
  bytes; 70,046 bytes into step actors; 8 min 35 s.
  B2 `e2ca852b…5ecc`, composite out_of_frame; 20 satisfied, 3 out_of_frame
  (R12 10,352, R15 9,896, R21 9,145 bytes, refused before any actor, no
  lawful refinement under the card's section-as-unit contract, escalation
  to an envelope of at least 10,352 bytes named); 9 actor steps, largest
  7,765 bytes; 54,631 bytes into step actors; 9 min 38 s.

Author's structural check over both lifecycle logs (chronology of
measurement, refusal and start; input sizes; echoed byte counts; output
digests): no problems. Mechanical evidence only; not assessment.

Candidate findings carried, not repaired: the fixture's framework-overhead
figure is uncalibrated (constructors' regression 7,100–7,300 tokens per
step against 2,300 measured on a trivial input); the instrument's logged
output digest is over the raw result, not the file; P4b's "nine statements
become one obligation" is a paragraph-level claim no route step judges
(A2); route-level residuals from the step actors are listed in the records
(A2 nine, B2 eleven), none reported as a contradiction.

Resource observation: declared allowance per run 30 actor starts and 60
minutes; used 8 and 9 starts, under 10 minutes each. Step-actor spend from
the CLI usage records: A2 87,241 tokens (79,271 context, 7,970 output),
USD 0.3666 list; B2 89,542 tokens (81,084 context, 8,458 output), USD
0.3750 list. Coordinator spend as the harness reports it, definition
unverified: A2 150,541 tokens, 33 tool uses; B2 127,801 tokens, 30 tool
uses; the two ran in parallel, 9 min 38 s wall. The author's own
generated-token counter is unavailable on this host; wall for this pass is
at most 19 min 51 s from the receipt stamp to this stamp, after the
earlier verification and drafting that preceded the receipt stamp.

Verification at freeze: tenant gate green over 19 files, 284 links
including every `stdo://` fragment, no trailing whitespace; run
directories and `received/` verbatim text are excluded from the gate as
constructor and reviewer output respectively.

Work result: `candidate_ready` / `satisfied` for the declared T1.2
outputs. T1.2 is not closed: closure needs an authorised independent
assessment of runs A2 and B2 under CASE-2's five expected distinctions, an
author-independent fidelity judgment of the regenerated program, and Jim's
selection of the Axiom Indexer dependency use. Next after that: T2
(SPEC_METHOD, CALCULUS §4–7).

## T2 thread return, 2026-10-11T14:58:32Z

Activation: Claude Writer, own tenant only, on `tenant/claude/c3`, under
Jim's authorisation to complete STDO 3.0 ready for review ("i authorise you
finish the work to completetion"). Start bounded below by the T1.2 return
stamp, 2026-10-11T13:25:58Z.

Delivered, in two commits:

- `97f1259`: the T2 increment frozen (CALCULUS `b5fb31de…3821` with §1–3
  byte identical to T1.2; SPEC_METHOD `c30b9946…ddf4`; FOUNDATIONS and
  EVALUATION unchanged) after the author's pre-freeze route check: 29
  routes of SPEC_METHOD and CALCULUS §4–7 judged by fresh step actors
  through the new generic instrument (`qualification/instruments/`), first
  pass 19 satisfied, 3 out_of_frame, 2 indeterminate, five wording
  residuals; every non-satisfied route and residual repaired at source
  (UP-021 wording, graph functions, resumption against restart, allowance
  rule marked new, basis invalidator attribution, UP-013 "by itself",
  Universal Intake Triage cited, carrier default reframed only, Executive
  and non-widening attributed, Steel-Thread reframed, UP-015 qualifiers,
  RELEASE_METHOD anchors, AC-020 in its own words); second pass 28 of 29
  satisfied, third pass on §4 all satisfied. The T2 program
  `urn:stdo-3:claude:program:a-c-text:t2` (108 symbols, 135 clauses, 6
  residuals; file `bbc624e2…5524`, canonical `13338baa…7f8b`) validated
  with zero diagnostics; two frames projected (bounded-activation,
  composition-conservation). Case T-03-04 designed with its outer
  contract, the variant subject V and three result bundles produced by
  real step actors (11 starts, USD 0.62), with the seeded conditions
  declared in one place.
- this commit: two T-03-04 constructor runs by fresh coordinator contexts
  of this model family, each writing one record:
  A `bc31d8ea…0ea1`, zero actor starts: composite falsified; 18 routes
  covered and carried unchanged; failure set {R05} with the actor's quoted
  evidence; R minus C = {R16–R19 (B-P5 digest mismatch, the alteration
  located exactly), R21 (not executed)}; R_C refused on its basis digest;
  triage realization_refactor; stop state falsified; 8 min 8 s.
  B `e7e0c3be…1f33`, two actor starts of four allowed: the same join, then
  R16–R19 and R21 covered by two new authenticated steps on basis V
  (25,938 bytes, 23,607 context tokens, USD 0.107); R minus C empty after;
  R05 still carried; composite falsified; R_C refused; triage
  requirement_reprice; stop state satisfied (candidate_ready) with the
  composite falsified; 8 min 46 s.

Author's structural check over run B's lifecycle log: no problems.
Mechanical evidence only; not assessment.

Candidate findings carried, not repaired: the case design's claim that
R_C's actor judged all ten routes satisfied was wrong (R09 out_of_frame in
C-P4a), corrected in CASE.md after the runs; the rc.2 manifest digest
named in the contract is unverifiable under the constructor's grant; the
two constructors triaged the same defect into different change classes
with reasons, an observation about SPEC_METHOD §4 against a fixture copy
of a standard; a step actor's ROUTE line format varies (a tenant-section
prefix) without breaking authentication.

Resource observation: step actors, bundles plus run B, 13 starts, USD
0.73 list, all `claude-sonnet-5-5`. Coordinator spend as the harness
reports it, definition unverified: A 139,910 tokens, 18 tool uses; B
161,129 tokens, 23 tool uses; the two ran in parallel, 8 min 46 s wall.
The author's own generated-token counter is unavailable on this host.

Verification at freeze: tenant gate green over 24 files, 329 links
including every `stdo://` fragment, no trailing whitespace; run
directories, bundle output and received text excluded from the gate.

Work result: `candidate_ready` / `satisfied` for the declared T2 outputs.
T2 is not closed: closure needs an authorised independent assessment of
runs A and B under CASE.md's six expected distinctions and an
author-independent fidelity judgment of the T2 program. Next: T3
(EVALUATION §5–8, CONFORMANCE, PROFILES; case T-05).

## T3 thread return, 2026-10-11T15:16:40Z

Activation: Claude Writer, own tenant only, on `tenant/claude/c3`, under
the same authorisation as T2. Start bounded below by the T2 return stamp,
2026-10-11T14:58:32Z.

Delivered, in two commits:

- `c539daa`: the T3 increment frozen (EVALUATION `a9310f0c…a310` with
  §1–4 byte identical to T1.2; CONFORMANCE `2f6409b7…fc2d`; PROFILES
  `c83c9365…1865`; the T2 files unchanged) after the author's pre-freeze
  route check over EVALUATION §5–7 and PROFILES: first pass 14 satisfied,
  1 falsified, 1 out_of_frame, 1 indeterminate; repairs (proxy limits to
  UP-020, UP-022's comparison rule linked, the qualification protocol to
  UP-022, PROFILES §3 routed to its DESIGN_MODULE sections with the
  per-boundary exemption turned into a residual, §5 routes added); second
  pass 22 satisfied, 3 falsified on precise points (RF-013 scoping,
  UP-022's conditional withholding, ODD's ownership of F_P and F_H);
  repaired; third pass on the two sections all satisfied. The T3 program
  `urn:stdo-3:claude:program:a-c-text:t3` (127 symbols, 161 clauses, 7
  residuals; canonical `41afde44…082e`) validated with zero diagnostics;
  three frames projected. Case T-05 designed with a real interrupted work
  state (five steps completed by step actors, one natural refusal, one
  step killed six seconds after `actor_started`, USD 0.28) and the
  predecessor's draft. Case R-01 designed (card, task subject, five
  variants, operator).
- this commit: two T-05 constructor runs by fresh coordinator contexts of
  this model family, each copying the work state and continuing its
  lifecycle log in one file:
  A `d8d14bf9…9e26`: composite out_of_frame, 23 of 23 covered, 21
  satisfied, R09 out_of_frame and R10 indeterminate carried as the P4a
  actor judged; five steps reused after a recorded applicability check
  (section, card and instrument digests, every rc.2 block re-measured by
  dry run), none re-run; three draft claims disposed with evidence; P4b-2
  reconciled and closed as interrupted with its effect unknown before any
  repetition; three new steps; 7 min 41 s.
  B `0642f7dc…ba17`: the same shape with the prescribed reverse order
  (P6, P5, then the interrupted routes last); three new steps; 9 min 57 s.

Author's structural check over both logs: no problems; the fixture is
byte identical after both runs. Mechanical evidence only; not assessment.

Candidate findings carried, not repaired: the predecessor's draft carried
a third unsupported claim the case owner had not declared (the P4a row),
caught by both constructors and now corrected in CASE.md; a fresh step
actor on the whole FOUNDATIONS §3 judged AC-016 out_of_frame and RF-010
indeterminate for P4a where the T-01 A2 run, with the paragraph alone,
judged both satisfied, a candidate finding against P4a's attribution of
RF-010 and an observation about the context sensitivity of route
judgments; the instrument does not log its own digest.

Resource observation: step actors for the fixture and the two runs, 12
starts, USD 0.55 list, all `claude-sonnet-5-5`; pre-freeze checks 11
starts. Coordinator spend as the harness reports it, definition
unverified: A 132,455 tokens, 22 tool uses; B 163,979 tokens, 26 tool
uses; the two ran in parallel, 9 min 57 s wall. The author's own
generated-token counter is unavailable on this host.

Verification at freeze: tenant gate green over 30 files, 361 links
including every `stdo://` fragment, no trailing whitespace.

Work result: `candidate_ready` / `satisfied` for the declared T3 outputs.
T3 is not closed: closure needs an authorised independent assessment of
runs A and B under CASE.md's six expected distinctions and an
author-independent fidelity judgment of the T3 program. Next: T4.

## T4 thread return, 2026-10-11T15:30:00Z

Activation: Claude Writer, own tenant only, on `tenant/claude/c3`, under
the same authorisation. Start bounded below by the T3 return stamp.

Delivered, in two commits:

- `6bc1692`: README routes finalised (a resumption route added; the set
  program as the route into a model's context); CONFORMANCE statuses
  record what exists for every case; the set program
  `urn:stdo-3:claude:program:a-c-text:set` over all seven files (130
  symbols, 164 clauses, 6 residuals; canonical `df4701d9…dfad`) validated
  with zero diagnostics against the byte-verified pinned subject, five
  frames projected, one per README route; case R-01 ready; the review
  handoff `qualification/REVIEW_HANDOFF.md`; thread states in
  DOCUMENT_STRUCTURE.
- this commit: the R-01 recoverability trial run by the case owner as
  operator through `run_variants.py`: five variants (no method; the STDO 3
  route; the whole STDO 3 set; an author-selected rc.2 section set; the
  four rc.2 members a README reader would open) twice each, every variant
  one fresh headless step actor with its whole context measured and
  logged; eleven starts, no refusals, 4 min 13 s, USD 1.86 list, contexts
  from 3,551 to 129,631 tokens; no record reports claim K satisfied; the
  records are in the case's runs table, unjudged. A first run was stopped
  after six steps and kept as evidence: its calibration logged 6,907
  context tokens on a 235-byte input, which exposed that the headless CLI
  loads CLAUDE.md files from the actor's working directory and ancestors.
  The generic instrument is repaired (actor in an empty directory outside
  any repository; instrument digest logged in every measurement),
  calibration 2,248 tokens. The finding is recorded at the end of T-01
  CASE-2, T-03-04 and T-05: every step actor of those cases received the
  workspace's three CLAUDE.md files (about 12 KB) beside the measured
  context. The judgments stand; the "whole context measured" claim of
  those fixtures is false by that amount. Also in this commit: the
  received review's author identified as Codex (its
  `reviews/20261011T125957Z_REVIEW_CLAUDE_CODEX_BUILD.md` at `bfe4173`);
  the comparison review Jim authorised, written in this tenant from a
  source-first read of the Codex tenant at `67217a4`:
  `reviews/20261011T153000Z_REVIEW_claude_and_codex_c3_comparison.md`.

Candidate findings carried, not repaired: the CLAUDE.md contamination
above (material against E1 and E4 of the three earlier cases; the
assessor weighs it); the R-01 records give the same facts different
non-success members across variants (out_of_frame, indeterminate,
invalid_basis), an observation about the CALCULUS §3 boundary as read by
fresh actors; the V0 control records reach the same disposition (return
to the owner, claim not supported) without the algebra or any citation,
which bounds what the documents add on this task to vocabulary, intake
shape, fit measurement, citation and the handling of labels, and which
only the assessor can weigh.

Resource observation: step actors 11 starts USD 1.86 (run 002) plus the
abandoned run's six starts; pre-freeze and fixture production across T2–T4
about 60 starts; whole pass since the T1.2 return at most 2 h 5 min wall
by the return stamps, including four constructor runs in parallel pairs.
The author's own generated-token counter is unavailable on this host.

Verification at freeze: tenant gate green over 32 files, 388 links
including every `stdo://` fragment, no trailing whitespace.

Work result: `candidate_ready` / `satisfied` for the declared T4 outputs.
The C3 construction is complete to the author's declared outputs. Nothing
is closed: every run of every case awaits an authorised independent
assessment; every program awaits an author-independent fidelity judgment;
the Axiom Indexer dependency use awaits Jim's selection; the independence
policy and the C2 contract are Jim's; merge is on his acceptance.

## W1 return, 2026-10-12T01:53:57Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry on tenant/claude/c3-v3 (SHA in the Executive-facing return; it cannot be inside its own commit)
FILES: design/DOCUMENT_STRUCTURE.md (rewritten, 11,996 bytes); frontier/PREDECESSOR_CLAIMS.md (new, 76,568 bytes); qualification/RETURNS.md (this entry)
MEMBERS: tier 1 FOUNDATIONS, REFERENCE_FRAME*, ACTIVATION (CALCULUS renamed at member 1), AXIOMATIC_CALCULUS*, IDENTITY*, EVALUATION; tier 2 SPEC_METHOD, PRODUCT_DEFINITION*, TICKETS*, ASSURANCE*, RELEASE*, CONFORMANCE; tier 3 PROFILES (index and boundary), EXECUTIVE_BASELINE*, DESIGN_MODULE*, ODD*, TRAVERSAL_OCCURRENCE*, UX*, WORLD_MODEL*; guides POSTING_GUIDE*, WRITING_GUIDE*, GLOSSARY*; route README; packaging a_c/ (compressions' successor), standards/schemas/, standards/templates/, plugins/spec/, LICENSE, release/release-note.md (* new; 24 standards bodies)
MAP:
README.md -> README; RELEASE (installed cut, store, manifest)
AXIOMATIC_CALCULUS.md -> AXIOMATIC_CALCULUS
DESIGN_MODULE_METHOD.md -> DESIGN_MODULE; SPEC_METHOD (core rule, non-goals); ASSURANCE (6A to 6C)
GLOSSARY_GUIDE.md -> GLOSSARY
IDENTITY_METHOD.md -> IDENTITY; DESIGN_MODULE (bound-realisation defaults)
ODD_METHOD.md -> ODD; ACTIVATION (graph-function refinement, by note)
POSTING_GUIDE.md -> POSTING_GUIDE; SPEC_METHOD (UP-012)
REFERENCE_FRAME_METHOD.md -> REFERENCE_FRAME; FOUNDATIONS (ontology objects); ACTIVATION (engagement as the step); EVALUATION (qualification)
RELEASE_METHOD.md -> RELEASE; FOUNDATIONS (recursive product objects); EVALUATION (UP-015 as acceptance evidence)
SPEC_METHOD.md -> SPEC_METHOD; PRODUCT_DEFINITION (overlay, SURFACE-001, bootstrap); ACTIVATION (work boundary, UP-014/020/021); FOUNDATIONS (product taxonomy); EVALUATION (evidence rules, litmus); ASSURANCE (testing law)
STDO_REFERENCE_FRAME_BASELINE.md -> EXECUTIVE_BASELINE; ASSURANCE (testing frames, interface integration); EVALUATION (reviewer result, triage projection)
TICKET_METHOD.md -> TICKETS; SPEC_METHOD (change classes as the triage target)
TRAVERSAL_OCCURRENCE_PROFILE.md -> TRAVERSAL_OCCURRENCE
UX_METHOD.md -> UX
WORLD_MODEL_METHOD.md -> WORLD_MODEL
WRITING_GUIDE.md -> WRITING_GUIDE
compressions (10) -> a_c/ program, map and frames, proposed superseded by "projection from the set program"; stdo_bootstrap.md -> PRODUCT_DEFINITION and bootstrap templates
schemas (2) -> standards/schemas/ under PRODUCT_DEFINITION and RELEASE
templates (24) -> standards/templates/ under SPEC_METHOD, TICKETS, PRODUCT_DEFINITION, REFERENCE_FRAME
plugin (17) -> plugins/spec/, each skill re-routed to its successor frames
licence (1) -> LICENSE at the candidate root
release note (1) -> release/release-note.md at the RC cut under RELEASE
NON-CHANGES: design/PRINCIPLES.md; the seven first-pass standards/ files (FOUNDATIONS section 1 still defines conserved by route, fixed at member 1); a_c/, qualification cases, runs and instruments, reviews/; the common specification/ and tickets; the frontier copy differs from the common file only in its first heading and the inserted provenance paragraph (690 rows, all unresolved, 725 table lines carried; verified by diff).
RESIDUALS: (1) CALCULUS.md -> ACTIVATION.md rename is my decision to remove the name collision with AXIOMATIC_CALCULUS; a_c/set digests and case records cite CALCULUS.md as frozen history; confirm or veto before member 1. (2) PRODUCT_DEFINITION as its own tier-2 member for SPEC_METHOD's overlay, SURFACE-001 and bootstrap law (about 600 lines) rather than inside SPEC_METHOD; confirm. (3) The compressions' superseded relation "projection from the set program" needs Jim's acceptance before it is a valid disposition; those 10 rows stay unresolved until then. (4) The member map is reviewed with member 1 per the contract; the Reviewer family for member 1 is not selected here. (5) No gate script exists in the tenant; earlier "tenant gate" runs were ad hoc, so I ran link, heading-depth, whitespace and byte-diff checks by hand on the changed files only.
MEASURED: input bytes read about 115,000 (file reads plus command outputs, tallied per call; envelope 300 KB); wall 2026-10-12T01:39:43Z to 2026-10-12T01:53:57Z UTC
STOP BASIS: complete

## W2 return, 2026-10-12T02:12:13Z

RESULT: candidate_ready
COMMIT: 361f997 (step 1, rename CALCULUS.md to ACTIVATION.md) and the step-2 commit that carries this entry, both on tenant/claude/c3-v3
FILES: standards/REFERENCE_FRAME.md 40,908 (new); standards/FOUNDATIONS.md 26,694; standards/ACTIVATION.md 23,230 (renamed from CALCULUS.md); standards/EVALUATION.md 14,039; standards/README.md 3,819; standards/CONFORMANCE.md, PROFILES.md, SPEC_METHOD.md (link rename only, step 1); frontier/PREDECESSOR_CLAIMS.md 80441 (81 RF rows filled, no other line changed); qualification/RETURNS.md (this entry)
ROWS: conserved 75 | superseded 0 | not applicable 6 | unresolved 0 (of 81)
UNRESOLVED: none
NOT APPLICABLE: #definitions, #reference-frame-laws, #engagement, #workspace-coverage, #discovery-and-revision (heading-only rows of 14 to 26 bytes; each child disposed individually); #worked-binding-product-chain-drift-evaluation (non-normative by its own statement; its binding shape is conserved at REFERENCE_FRAME.md#minimal-activation-binding; subject is tier-2 matter)
PLACEMENT: 54 rows in REFERENCE_FRAME (§1 unit and scope, §2 core claims, §3 RF-001 to RF-017 and engagement atom, §4 frame set and selection, §5 functions, §6 conjunction, §7 relations, §8 coverage, §9 completeness, §10 revision, §11 packet and binding, §12 violations, §13 declarations, §14 closure, §15 dispositions); 18 in FOUNDATIONS §2 (Basis, Evidence, Authority and Material rows amended; new Frame objects table, Authority kinds, Disjointness and independence, The frame tuple); 7 in ACTIVATION (§1 Intake, Admission, Applicability; §2 Activation; §3 Evaluation; §4 Reconfiguration; §7 Closed result and reuse); 2 in EVALUATION §7 (Frame qualification, Method self-qualification with the nine-relation population table)
ALGEBRA: defined once in ACTIVATION §3; REFERENCE_FRAME RF-012 states the law and points there; the frame tuple's R points there; nothing defined twice
ADMISSION: ACTIVATION §1 Admission restates the drafting/admission distinction, the four contract states, execution only after deterministic admission or explicit human override, no admission inferred from the actor's own draft, carrier presence, lane or `active` label, the admitted-result coordinates, no authority creation by drafting or retaining, the durable result surface and refusal; provenance TICKET_METHOD #work-carrier-to-execution-rule and #execution-contract-admission; the carrier selection table is left to the TICKETS member
VOCABULARY: FOUNDATIONS §1 now carries the five UP-015 values with conserved defined as restated and a route as provenance only; §6's RF row is replaced by three rows and an anchor table; other members' "conserved by reference" rows are left with a note that each is rewritten at its member's activation
NON-CHANGES: design/ (PRINCIPLES.md unchanged; no restatement needed a principle changed); a_c/, qualification cases/runs/instruments, reviews/, common specification/, tickets, codex tenant; other members' rows in the three disposition tables except the CALCULUS to ACTIVATION name; the §3 commitments text; CALCULUS.md citations outside standards/ kept as frozen history; the bounded-context URN urn:stdo:bounded-context:reference-frame-evaluation carried unchanged; "Prime" generalised to "a semantic-contraction law an adopting method supplies", noted in REFERENCE_FRAME §15
RESIDUALS: (1) five heading-only rows are `not applicable`; if the Executive prefers `conserved` with the children's locus, it is one cell per row. (2) #worked-binding is `not applicable` rather than restated; a successor worked binding belongs to a qualification case; confirm. (3) Definitions of the frame objects live in FOUNDATIONS §2 and the laws over them in REFERENCE_FRAME §3; the DOCUMENT_STRUCTURE tier table lists "basis, manifold, envelope, frame, frame set, configuration, lens" under REFERENCE_FRAME, so the concurrent DOCUMENT_STRUCTURE repair should read definitions in FOUNDATIONS, laws in REFERENCE_FRAME. (4) ACTIVATION §7 is renamed "Closed result and reuse" (anchor changed; no link used the old anchor). (5) The a_c/set frames and README's route to them still cite CALCULUS.md; regenerate at AXIOMATIC_CALCULUS or packaging. (6) Step 1 touched CONFORMANCE, PROFILES and SPEC_METHOD for the name only.
MEASURED: input bytes read about 229,000 (file reads plus command outputs, tallied per call; envelope 600 KB); wall 2026-10-12T01:56:12Z to 2026-10-12T02:12:13Z UTC; spend counter unavailable on this host
STOP BASIS: complete

## W2b return, 2026-10-12T02:22:59Z

RESULT: candidate_ready
COMMIT: the commit that carries this entry, parent 09a8fe1, on tenant/claude/c3-v3; git show --stat confirms only the six named files changed
CORRECTIONS:
1. REFERENCE_FRAME.md RF-014: "When the material manifold exceeds an actor's capability envelope, human authority may select another actor, refine the frame, sequence activations or provide a lawful compression (RF-017); the selection is human authority's, exercised directly or in advance through the grant, and ACTIVATION §2 says which of these a step selects itself and which re-enter the grant's owner." Label "RF-014 Capability fit" kept.
2. FOUNDATIONS.md §2 Material row: "... change the admissible evidence, change who may perform a material operation, or change who may decide the evaluation or a material operation; ..."
3. frontier/PREDECESSOR_CLAIMS.md #reference-frame locus cell: `FOUNDATIONS.md#frame-objects; FOUNDATIONS.md#the-frame-tuple`; FOUNDATIONS.md §6 row: "| #reference-frame | conserved | §2 Frame objects; §2 The frame tuple |". Slug check over FOUNDATIONS.md headings: frame-objects PRESENT ("### Frame objects"), the-frame-tuple PRESENT ("### The frame tuple").
4. ACTIVATION.md §3: "... indeterminate is reserved for the case where the declared capability was exercised and the admissible evidence still cannot decide (P5, finite capacity and graceful total handling; the material relation drawn is the out_of_frame boundary, capability declared and exercised versus capability not declared)."
5. EVALUATION.md §7 Method self-qualification, one sentence appended to the paragraph: "The constructor, freeze, assessor, acceptance and release protocols are supplied by the governing authority; this member defines none of them."
6. ACTIVATION.md §7: "A closed result is reused by an unchanged consumer that checks exact applicability; ..." and "... invalidate the affected result before reliance, preserving its predecessor/successor relation and any demonstrably independent surviving results; ..."
NON-CHANGES: every other sentence in the five files; the tenant's P5 label is "Finite capacity and graceful total handling" (design/PRINCIPLES.md, read for the label only, unchanged), so correction 4 cites that label rather than "finite-attention and truthful-stop"; FOUNDATIONS §6's row already named both subsections in prose ("Frame objects and The frame tuple") and is changed only to the two-locus form so it agrees exactly with the frontier cell; no em-dash added; no heading deeper than ### in the four standards; predecessor read only at RF-014, the material-relation definition and Return A Closed Result.
MEASURED: bytes read about 41,000 (grep and sed ranges plus command output, tallied per call; envelope 200 KB); wall 2026-10-12T02:19:19Z to 2026-10-12T02:22:59Z UTC

## W3 return, 2026-10-12T02:44:51Z

RESULT: candidate_ready
COMMIT: 4633a0f (program, frames, fixture) and the commit that carries this entry (RETURNS.md only), both on tenant/claude/c3-v3, parent 1a68fd5
PROGRAM: a_c/set-2: symbols 209, clauses 263, residuals 6 (the six of set carried; none added, none retired); validation diagnostics 0; Axiom Indexer subject refs/tags/axiom_indexer/v2.5.1-rc.2 (tag 9bff233c, commit 9a9c4797), ac.py SHA-256 5a2e0cb503cf...e6c8 read from the tag with git show and matched against axiom_indexer/releases/v2.5.1.md at the same tag, run from a scratch copy with python3 -I; program canonical digest sha256:4cc36994c07d...aca01; the report's 107 resolved tenant sources carry exactly the 1a68fd5 standards digests
FRAMES (materialized bytes by wc -c after projection, before any actor read; reference-only variants also projected and listed in a_c/set-2/README.md):
bounded-activation | 137,713 | route "do a bounded piece of work"; T-01
composition-conservation | 155,385 | composition under an outer contract; T-03, T-04
work-state-restart | 159,525 | route "resume work someone else left"; T-05
recoverability | 170,335 | route "load it into a model's context"; R-01, R-02
review-and-acceptance | 138,512 | routes "review someone's work" and "decide acceptance or release"
frame-declaration-and-activation | 247,020 | REFERENCE_FRAME declare and activate tasks (minimal frame declaration, packet, binding, minimal evaluation result, laws, authority kinds, nine qualification tests); F-01 task A
coverage-and-revision | 208,066 | REFERENCE_FRAME audit_coverage and revise tasks (coverage tuple, inventory, ledger fields, seven statuses, interaction, authority, failure and high-risk coverage, operational full coverage, completeness boundary, nine signals, eight diagnostic questions, revision actions, frame relations, conjunction rule); F-01 task B
FIXTURE: qualification/cases/F-01/CASE.md, TASK-A.md (W-ledger-export: two builds, a replica move, three evidence items, three evaluations, owner's claim K; declare a frame for E1, activate, return a minimal evaluation result), TASK-B.md (W-notify: three-frame set, six evaluations: two closed, one basis advanced, one conflicted across two frames, two never activated; ledger with statuses, diagnostic order on the meeting signal, one revision action with what it reopens), plus CARD.md (455 bytes, routing only, no method content: the instrument requires --card and R-01's pattern carries one). Invocation per task: python3 -I qualification/instruments/bounded_step.py --cap 400000 --model sonnet --card CARD.md, one --block METHOD=<frame file> and one --block TASK=<task file>, run from the tenant root; the instrument starts the actor in an empty directory outside any repository (no CLAUDE.md). Dry-run measured at design time, no actor started: A 250,979 bytes, B 212,852 bytes, both under cap; components and digests logged. CASE.md names the subject (commit 1a68fd5 standards, program digest, the two frame file digests), the measured-context admissibility rule, and an Expectations section holding only the required sentence. EXPECTATIONS.md not created; no actor run.
NON-CHANGES: standards/, design/, frontier/, reviews/, the common specification, tickets and the codex tenant untouched; a_c/set, t1, t2, t3 frozen and unedited; set-2/bindings.json byte identical to set's (relative tenant basis); a_c/README.md gained one sentence pointing to set-2; nothing else in the tenant changed (git show --stat on both commits).
RESIDUALS: (1) no author-independent fidelity judgment of set-2 or its frames exists; the program, the frames and the fixture have one author. (2) standards/README.md's "load it into a model's context" route still points to a_c/set and its five frames; outside this territory; re-entry at the README member's Writer. (3) frame-declaration-and-activation is 247 KB, 62 percent of the R-01 cap; the projection format repeats each clause's arguments under clause_relations and adds source_routes, so roughly half the bytes are structure, and the reference-only mode (124 KB) carries no clause text; a smaller activation context needs a narrower clause selection or a projection mode the pinned tool lacks. (4) the six set residuals are carried unchanged; ACTIVATION section 2 still measures only the context dimension of the fit test. (5) the source-dispositions sections of every member are not encoded (rc.2 outside the program basis), as in set. (6) the derivation script that carried set forward to set-2 stays in scratch and is not committed; the program is the artefact and the README records every class of change.
MEASURED: bytes read about 275,000 (files 234 KB: the eight basis files, the eight standards, one 52 KB script dump of the set program's symbol and clause inventory; the rest command output, tallied per call), envelope 500 KB; wall 2026-10-12T02:24:15Z to 2026-10-12T02:44:51Z
STOP BASIS: complete

## W2c return, 2026-10-12T03:04:44Z

RESULT: candidate_ready
COMMIT: the commit that carries this entry, parent de075f1, on tenant/claude/c3-v3; git show --stat confirms only the three named files changed
REPAIRS:
1. ACTIVATION.md §3, the boundary paragraph after the no-coercion sentence, replaced by a three-case boundary: "out_of_frame when the claim requires a material relation or an evaluator capability that the activated frame does not declare. The result names the missing relation or capability, its owner where the subject gives one, and the reconfiguration pressure it creates ... A term the claim depends on and the frame leaves undefined is an undeclared material relation ... Whether the step exercised anything is irrelevant to this member; the ground is the missing declaration."; "indeterminate when every relation and capability the claim requires is declared and was exercised in the step, and the admissible evidence still cannot decide. The result names the evidence that would decide"; "A declared capability that the step did not exercise yields no Reference Frame Method result for the evaluation at all ... The step's stop state is `incomplete` under the construction availability refinement below, its work state (§5) carries the unexercised capability as a residual, and the actor says so rather than selecting a core member". Cases 1 and 2 are restatements of RF-012's members with the boundary explicit; case 3 is a labelled tightening (P5, P6); the undefined-term clause is labelled RF-003, P1. P5 label and RF-012 provenance kept; anchors added: #rf-012-closed-results, #reconfigure-when-necessary, #return-a-closed-result, #applicability-and-required-results.
2. REFERENCE_FRAME.md §10 Diagnostic order, one paragraph inserted after question 8 and before "The order prevents ...": "Question 1 is answered by family inclusion, not by set membership. An evaluation is within a frame's family when the question it decides is one the frame's declared evaluation family states, at the frame's declared coordinates (RF-001). Membership of the frame in the frame set, the frame's name, a role label or similar wording of the question does not place an evaluation in the frame's family; an activation of a frame on an evaluation outside its family answers question 1 no, whatever the frame's standing in the set." Labelled tightening (P2, P1; material relation drawn: evaluation-to-family inclusion; rc.2 #diagnostic-order, #evaluation, #rf-001-evaluation-relativity, #applicability-and-required-results). The eight questions and their order are unchanged.
3. REFERENCE_FRAME.md §10 Revision actions, one paragraph appended after the existing closing sentence: "Stated plainly: revising a frame produces a new frame revision coordinate. Every prior closed result bound to the previous revision is bound to a mismatched coordinate (RF-005) and is invalidated for reuse until it is re-checked against the new revision (RF-011; ACTIVATION §7). The revision record lists those results as reopened; a result leaves that list only by a recorded re-check that finds it demonstrably independent of the change, or by re-evaluation on the new revision. A revision does not select which of the results bound to the prior revision it reopens, and silence does not keep a result closed." Restatement of RF-005, RF-011 and rc.2 #revision-actions in combination (P3, P4b). §3 RF-011 gained one cross-reference sentence, "Revision of the frame itself invalidates for reuse every result bound to the prior revision coordinate; §10 Revision actions states that rule", with its label and provenance unchanged.
PREDECESSOR CHECK:
1. RF-012: the five members and their meanings stand unchanged in the §3 table; the compatible-extension rule stands in REFERENCE_FRAME RF-012; out_of_frame as undeclared relation or capability and indeterminate as admissible evidence unable to decide are both present. Return A Closed Result: the identified result fields and residual uncertainty stand in §7 and REFERENCE_FRAME §13; reuse by an unchanged consumer, role or conversation change invalidating nothing, invalidation before reliance with predecessor/successor relation and independent survivors, and independent judgment not satisfied by reuse all present in §7, unchanged. Applicability And Required Results: missing or ambiguous premise leaves applicability unresolved, not false; frame name, tool or listed family triggers no activation; absent, stale or wrong-subject required result cannot satisfy a dependent conjunction; qualification distinguishes true, false and unknown premises; all present in §1 Applicability, unchanged.
2. Diagnostic Order: the eight questions, their order and the closing sentence stand verbatim. Missing-Frame Signals: the nine signals stand, unchanged.
3. RF-011: an activated frame declares the topology changes capable of invalidating its coordinates or materiality judgment; a detected material mutation causes reevaluation, frame revision or recharting before reuse; both present. Revision Actions: the nine actions stand; every material revision changes frame identity or revision coordinates and states which prior activations, results and coverage claims require reevaluation, present verbatim. Return A Closed Result: demonstrably independent surviving results are preserved as the re-check's survival route, not removed.
NON-CHANGES: every other sentence of the two members; frames, fixtures, runs, frontier and design untouched; EXPECTATIONS.md not read; both Source dispositions tables unchanged (loci §3 and §10 unchanged); no em-dashes; no header deeper than ###.
MEASURED: bytes read about 104,000 (ACTIVATION 23,426; REFERENCE_FRAME 40,992; three run outputs 24,145; named predecessor sections and two definitions 7,004; headings, labels, RETURNS tail and command output about 8,500; envelope 200 KB); wall 2026-10-12T03:01:43Z to 2026-10-12T03:04:44Z UTC

## W5 return, 2026-10-12T03:21:32Z

RESULT: candidate_ready
COMMITS: phase 1 83075cd (set-3, re-projected frames, CASE.md subject revision 2, a_c/README.md sentence), phase 2 the commit that carries this entry (runs 003 and 004, RUNS.md, this file); both on tenant/claude/c3-v3, phase 1 parent ac3ec5f
PROGRAM: a_c/set-3: symbols 209 (unchanged), clauses 269 (263 carried, 2 rewritten in place: missing-capability-is-out-of-frame and rf-011-topology-mutation-forces-reevaluation-before-reuse; 6 added), residuals 6 (carried; none added or retired), diagnostics 0, 108 resolved sources whose 107 tenant digests are the ac3ec5f standards (ACTIVATION 7fa219fd, REFERENCE_FRAME 203b2123, six unchanged from set-2); canonical digest sha256:18f58f7e939b05bafa8d1957c12abc999b9733beb731c2f4f98438bfa13ea38f; map digest sha256:4050072c...0caf; Axiom Indexer ac.py 5a2e0cb5...e6c8 read from refs/tags/axiom_indexer/v2.5.1-rc.2 with git show, matched against axiom_indexer/releases/v2.5.1.md at the tag, run from a scratch copy with python3 -I. Clauses changed vs set-2: ACTIVATION section 3 boundary (the rewrite plus out-of-frame-result-names-the-missing-declaration, undefined-term-is-an-undeclared-material-relation, indeterminate-result-names-the-deciding-evidence, unexercised-declared-capability-yields-no-evaluation-result); REFERENCE_FRAME section 10 (question-one-is-answered-by-family-inclusion under #diagnostic-order, revision-reopens-every-result-bound-to-the-prior-revision under #revision-actions); RF-011's requirement literal extended by its one cross-reference sentence. Selection rule: a new clause joined every frame index carrying the clause it refines (the four section 3 clauses to five frames, family inclusion to coverage-and-revision, the reopen rule to coverage-and-revision and work-state-restart); scopes, frame refs, source refs, residual refs unchanged.
FRAMES (materialized, wc -c after projection and before any actor read; all seven regenerated in both modes by the recipe's one loop, listed in a_c/set-3/README.md):
frame-declaration-and-activation | 271,966 | 545c293146a9
coverage-and-revision | 223,594 | c4ec41584efb
RUNS (task | run id | measured bytes | matched dry run | exit | output bytes | spend USD list):
A | 20261012T031547Z-A-003 | 275,925 | yes | instrument 0, is_error false | 10,366 | 0.5612
A | 20261012T031631Z-A-004 | 275,925 | yes | instrument 0, is_error false | 7,682 | 0.5562
B | 20261012T031710Z-B-003 | 228,380 | yes | instrument 0, is_error false | 7,824 | 0.5054
B | 20261012T031824Z-B-004 | 228,380 | yes | instrument 0, is_error false | 9,448 | 0.5008
Per run, from lifecycle.jsonl: measured precedes actor_started; every component byte count and digest equals CASE.md subject revision 2 (card 237ea8f9, frames above, tasks 93b314b2 and 48b2ebd6, headers 115 and 104); actor cwd a fresh bounded-step-* directory under the system temporary directory, removed after the step, parent outside any git repository (git rev-parse fails there); model claude-sonnet-5-5; instrument f92ca26b; out.md bytes and SHA-256 equal actor_ended. Totals: 1,008,610 bytes measured, 466,098 context tokens, 27,423 output tokens, USD 2.1235 list; calibration 2,247 to 2,248 tokens and about USD 0.004 per run.
ANOMALIES: (1) both member frames grew: frame-declaration-and-activation 247,020 to 271,966 bytes (closure 82/79/2 to 86/86/2), coverage-and-revision 208,066 to 223,594 (78/58/2 to 81/62/2); task A's context is now 69 percent of the 400,000 cap. (2) review-and-acceptance carries no changed clause, yet its bytes and digest changed because every projection carries the program, map and resolved-source digests. (3) About 300 bytes of a set-2 run's actor output (the A-001 console.log tail) entered my context while I read that log's marker pattern; no judgment was made and no set-3 output was read. (4) The two-byte header discrepancy of runs 001 and 002 does not recur: the five-character step ids make every run equal its dry run to the byte.
NON-CHANGES: standards/, design/, frontier/, reviews/, the instrument, CARD.md, TASK-A.md, TASK-B.md, EXPECTATIONS.md (not read), a_c/set, set-2, t1, t2, t3 untouched; CASE.md changed only by the appended "Subject revision 2 (2026-10-12)" section; set-3/bindings.json byte identical to set-2's; the derivation and runner scripts stay in scratch, uncommitted; no author-independent fidelity judgment of set-3 exists; no run output was read or judged.
MEASURED: bytes read about 135,000 (files about 60 KB: set-2 README, bindings, CASE, both TASKs, RUNS, CARD, a_c README, one set-2 lifecycle.jsonl, the standards diff, the W3 and W2c returns, about 10 KB of ac.py excerpts; the rest jq and command output, tallied per call); envelope 400 KB; wall 2026-10-12T03:07:07Z to 2026-10-12T03:21:32Z UTC
