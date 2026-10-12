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

## W6 return, 2026-10-12T03:19:31Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry, parent ac3ec5f, on tenant/claude/c3-v3-m2 (the SHA cannot be inside its own commit; it is in the Executive-facing return)
FILES: standards/AXIOMATIC_CALCULUS.md (new, 49,325 bytes); standards/FOUNDATIONS.md (28,575; §6 three AC rows replaced by fourteen rows by anchor or identifier, nothing else changed); standards/ACTIVATION.md (25,733; §2 steps 1 and 2 now link the tenant AC-010 and AC-011 with the rc.2 route kept as provenance; §3 gains one sentence naming RF-012 and AC-007 as the two laws over the one algebra; §8 two rows reworded); standards/README.md (4,511; document table row, the understand route extended, one new route); frontier/PREDECESSOR_CLAIMS.md (84,059; 39 AC rows filled, every other line byte-identical, verified by diff: 39 insertions, 39 deletions, all table lines); qualification/RETURNS.md (this entry)
ROWS: conserved 38 | superseded 0 | not applicable 1 | unresolved 0 (of 39)
UNRESOLVED: none. The one not applicable row is #fundamental-laws, a heading with no claim text (20 bytes), children disposed individually.
PLACEMENT: all 39 rows land in AXIOMATIC_CALCULUS (§1 position, derivation provenance, scope; §2 signature; §3 five records; §4 AC-001 to AC-014; §5 traversals, AC-015, AC-016; §6 interpretation, AC-017 to AC-019; §7 layers, AC-020; §8 calculus identity; §9 application boundary, imports, exclusions; §10 conformance obligations; §11 the anchor | disposition | locus table). No row lands in another member. Cross-member relations, each pointing to the one definition: AC-007 is a law over constraints using the algebra of ACTIVATION §3 and adds nothing to its three-case boundary; AC-002, AC-005, AC-006, AC-009 and AC-014 are laws over the FOUNDATIONS §2 objects Object, Authority, Basis, Residual and Judgment; AC-008 and AC-011 point to their generic forms in FOUNDATIONS §4; AC-010 and AC-011 are applied by ACTIVATION §2; AC-013 is consumed by FOUNDATIONS §4 conservation accounting; AC-016 names P4a as its generic form; AC-018 and AC-019 name EVALUATION §2 as the generic form; AC-020 is applied by SPEC_METHOD §6; the functor-kind categorical obligation is consumed by FOUNDATIONS §4's formal fragment.
EXACT CALCULUS IDENTITY: the law and the record shape (AxiomaticCalculusBasis, JCS, sorted principle_refs, the urn:stdo:axiomatic-calculus-basis identity, id(a_c.X), id(a_c.X.C), the external judgments, the owning Product's grammar duty) are restated in full; a closing paragraph states that this edition's identity is bound at its own release under RELEASE and AC-020, that this authoring text is neither the identity-bearing release nor the identity-bearing source of the released calculus pinned by A_C_DEPENDENCY, and records the predecessor's coordinates (cut, manifest SHA-256, member SHA-256, concept identity unchanged) as provenance. The row is conserved; the disposition reason says the coordinates are a release artefact, not a claim of the section.
NEW CLAUSES (criterion 6): the binding-of-this-edition paragraph in §8 (purpose: the standalone successor requirement and A_C_DEPENDENCY's separation of tenant text from released identity; P3, P6); one sentence in §5 declaring Omega_v a refinement of the ACTIVATION §3 algebra with a total mapping (purpose: the design's rule that ACTIVATION §3 is the one algebra; P5); one sentence in §5 that the traversal record is this member's concept and a same-spelled term elsewhere is not imported by nominal equality (purpose: PROFILES §1 boundary; P3, P1). No profile term in the member outside the disposition table; "graph", "ODD", "GTL" and "world-model" are not used; where the predecessor named them the text is generalised and the disposition says so.
NON-CHANGES: a_c/, qualification cases, runs and instruments, reviews/, design/, the common specification/, tickets, the codex tenant; REFERENCE_FRAME.md, EVALUATION.md, SPEC_METHOD.md, CONFORMANCE.md, PROFILES.md untouched; every FOUNDATIONS and ACTIVATION row of other members untouched; no accepted principle changed; no definition added to FOUNDATIONS; the rc.2 cut not modified; no em-dash in any changed file (the frontier's two pre-exist in rows outside this cone); no heading deeper than ###; all AXIOMATIC_CALCULUS.md anchors referenced from the four edited files resolve (checked by generated anchor list).
RESIDUALS: (1) PROFILES §1 lists traversal, F_D, F_P and F_H among terms owned outside the core; under the accepted design the calculus is tier 1 and owns them, so PROFILES §1 drops those four at its own activation (step 8); outside this territory, not changed. (2) No RELEASE member exists yet; §8 names it in prose without a link; the AxiomaticCalculusBasis instance for this edition is issued at the release, never in this text. (3) EVALUATION §8 still lists AC-018 and AC-019 as "conserved; §2"; the frontier loci name AXIOMATIC_CALCULUS §6 with EVALUATION §2 as the generic form; harmonise at EVALUATION's next touch. (4) The a_c/ set program and its five frames do not yet encode the new member; the README route "load it into a model's context" names the existing frames; packaging step 10. (5) Lawful generalisations recorded in §11 and the frontier: derivation provenance (ODD, GTL to profile, realisation, carrier), exclusions (graph storage topology, world-model ontology to any storage topology, any domain ontology), AC-002 (graph position to position in any structure), §2 carrier list (graphs folded into any other representation). (6) The Reviewer family is not selected here; same-family review would be a declared exception.
MEASURED: input bytes read about 267,000 (design 12,275; PRODUCT 20,294; requirements README 2,310; A_C_DEPENDENCY 4,781; PRINCIPLES 43,417; FOUNDATIONS 26,739; ACTIVATION 25,211; REFERENCE_FRAME 42,981; EVALUATION 14,182; standards README 3,819; predecessor AXIOMATIC_CALCULUS 37,849; SPEC_METHOD §6, PROFILES §1, design README, frontier head and AC section, RETURNS entries W1 and W2c, headings and command output about 33,000; envelope 600 KB); wall 2026-10-12T03:08:29Z to 2026-10-12T03:19:31Z UTC
STOP BASIS: complete

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

## W2d return, 2026-10-12T03:26:02Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry (sha in the chat return); only standards/ACTIVATION.md, standards/REFERENCE_FRAME.md and qualification/RETURNS.md
REPAIRS:
1. REFERENCE_FRAME §10 reopen paragraph: "Stated plainly: a material revision of a frame produces a new frame revision coordinate. Every prior closed result bound to the previous revision of a materially revised frame is bound to a mismatched coordinate (RF-005) and is invalidated for reuse until it is re-checked against the new revision (RF-011; ACTIVATION §7)." and "A material revision does not select which of the results bound to the prior revision it reopens, and silence does not keep a result closed." Added: "A non-material revision, for example one that clarifies an activation or acquires evidence without changing any declaration, produces no new coordinate and reopens no result; the revision record states that the revision is non-material."
2. REFERENCE_FRAME §3 RF-011: "Material revision of the frame itself invalidates for reuse every result bound to the prior revision coordinate; §10 Revision actions states that rule."
3. Locus chosen: REFERENCE_FRAME §3 RF-012, where the universal quantifier lives. Added after the first sentence: "A performed evaluation returns a member; an evaluation not performed because a declared capability was not exercised owes the step's stop state, not a member (ACTIVATION §3, third case)." ACTIVATION §3 case 3 is unchanged.
4. ACTIVATION §3 closing: "The first two cases restate RF-012's members with the boundary made explicit, save the undefined-term clause of the first, which is a tightening because it decides a boundary the predecessor leaves open; the third is a tightening RF-012 does not name (P5, P6). The relation drawn is three-way: capability not declared; declared and exercised; declared and not exercised." The same section's opening parenthetical, which named the relation two-way ("declared and exercised versus not declared"), now reads "three-way: capability not declared, capability declared and exercised, capability declared and not exercised" so the section does not contradict itself.
5. ACTIVATION §8, RF-012 row: appended "; the tenant text carries labelled tightenings: undefined term, unexercised capability". REFERENCE_FRAME §15: #rf-012-closed-results "conserved; the tenant text carries a labelled tightening: unexercised capability owes stop state"; #diagnostic-order "conserved; the tenant text carries a labelled tightening: family inclusion, not membership"; #revision-actions "conserved; the tenant text carries a labelled tightening: prior results reopen by default". Disposition stays conserved on all three rows.
NON-CHANGES: every other sentence of both members, including the §10 "This restates what RF-005, RF-011 and the sentence above carry in combination" sentence and the whole of ACTIVATION §3 case 3; all other table rows; no file outside the three named; no em-dash introduced; no header deeper than ###; the predecessor was read only at RF-011, RF-012 and Revision Actions, and its wording there (material revision; every evaluation returns a member) is what the repairs track.
MEASURED: bytes read about 80,000 (ACTIVATION 25,211; REFERENCE_FRAME 42,981; predecessor excerpt about 1,900; RETURNS tail and headings about 2,800; command and diff output about 7,000); envelope 150 KB; wall 2026-10-12T03:23:39Z to 2026-10-12T03:26:02Z UTC

## W6b return, 2026-10-12T03:28:27Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry, parent a562db1, on tenant/claude/c3-v3-m2 (standards/AXIOMATIC_CALCULUS.md, frontier/PREDECESSOR_CLAIMS.md, qualification/RETURNS.md only; the SHA cannot be inside its own commit; it is in the Executive-facing return)
REPAIRS:
1. §11 notes, the three generalisations of "graph", mirrored in the frontier disposition cells: #derivation-provenance adds `"graph, runtime, ODD, or application shorthand" is generalised to a runtime, a profile, a realisation or an application, which include the graph case`; #core-signature adds `the carrier list "records, tables, graphs, terms" is generalised to records, tables, terms, clauses, code or any other representation, which includes graphs`; #ac-002-scoped-identity adds `"graph position" is generalised to position in any structure, which includes it`.
2. §11 #derivation-provenance adds `field correction: the predecessor says the resolved address array is recorded under derivation_basis.release_uri, this member says derivation_basis.principle_refs, the array field that the record shape in both editions actually declares for it (release_uri holds one URI); that is a correction that tightens the text to the record, not a change of law` (field names in code spans in the row; the frontier cell says "the locus" for "this member").
3. AC-007: "this law uses that definition and adds nothing to the algebra." (was "adds nothing to it"); the following "Where this member says that a condition refuses ..." sentence kept; the paragraph rewrapped, no other word changed.
4. §5, one sentence inserted after the Omega_v declaration: "The signature's stop contract constrains the kinds; the traversal record's `stop_states` declares, per traversal, which of `hold`, `gap` and `refusal` map to which non-satisfied core member."
NON-CHANGES: every other sentence of AXIOMATIC_CALCULUS.md as it was; every frontier row other than the three disposition cells; no other file; no em-dash in any changed hunk (checked); no heading deeper than ### (checked); the predecessor wording was verified against the rc.2 member bytes (SHA-256 cbe2edb9..., equal to the §8 coordinate): "graph, runtime, ODD, or application shorthand", "records, tables, graphs, terms, clauses, code, or another representation", "graph position", `derivation_basis.release_uri`.
MEASURED: bytes read about 59,000 (AXIOMATIC_CALCULUS 49,325; three frontier rows, predecessor slices, RETURNS tail and command output about 10,000; envelope 120 KB); wall 2026-10-12T03:25:52Z to 2026-10-12T03:28:27Z UTC
## W7b return, 2026-10-12T03:34:51Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry, parent a562db1, on tenant/claude/c3-v3-m3b (the SHA cannot be inside its own commit; it is in the Executive-facing return)
FILES: standards/PRODUCT_DEFINITION.md (new, 50,677 bytes); standards/ASSURANCE.md (new, 12,430 bytes); frontier/PREDECESSOR_CLAIMS.md (20 rows of the SPEC_METHOD section filled, 20 insertions and 20 deletions, every other line byte-identical); qualification/RETURNS.md (this entry appended)
ROWS: conserved 20 | superseded 0 | not applicable 0 | unresolved 0 (of 20)
UNRESOLVED: none
README ROWS NEEDED (standards/README.md, owned by the parallel Writer or the Executive). Documents table: "| [PRODUCT_DEFINITION.md](PRODUCT_DEFINITION.md) | 2 | how a project binds to the method: the overlay and layout independence, definition relations, constitutional-set sufficiency, installed release basis and toolchain manager, bounded-context semantic resolution, local constitutional binding, collective reference-frame basis, WHAT/HOW and carrier bindings, discovery and composition, semantic-resolution conformance cases, STDO-SURFACE-001, bootstrap |" and "| [ASSURANCE.md](ASSURANCE.md) | 2 | assurance and testing law: verification layers, testing strategy taxonomy, fixture portability, test authority, scenario bundles, installed dev proof, significant path coverage |". Routes: "| bootstrap a project onto the method, or bind its definition | [PRODUCT_DEFINITION §12](PRODUCT_DEFINITION.md#12-bootstrap), then [§2](PRODUCT_DEFINITION.md#2-required-definition-relations) and [§4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) |"; "| resolve a term or declare a cross-context relation | [PRODUCT_DEFINITION §5 and §6](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), then [§10](PRODUCT_DEFINITION.md#10-semantic-resolution-conformance-cases) for the cases |"; "| prove a requirement or classify a test lane | [ASSURANCE §2](ASSURANCE.md#2-testing-strategy-taxonomy), then [§3 to §6](ASSURANCE.md#3-test-authority) |"; and the "understand the method" route extended with PRODUCT_DEFINITION and ASSURANCE after SPEC_METHOD.
NEW CLAUSES (criterion 6): none. Pointers only: §9 names EVALUATION §2 for the structural versus semantic split of the discovery checks; §10 says CONFORMANCE may index the cases without redefining them; §8 names SPEC_METHOD §4 and TICKETS for carrier selection; §7 names REFERENCE_FRAME §11 and ACTIVATION §1 as the definitions of the packet and the step. No obligation added.
NON-CHANGES: SPEC_METHOD.md, FOUNDATIONS.md, ACTIVATION.md, EVALUATION.md, README.md, REFERENCE_FRAME.md, AXIOMATIC_CALCULUS.md, CONFORMANCE.md, PROFILES.md untouched; a_c/, qualification cases, runs and instruments, reviews/, design/, the common specification/, tickets, the codex tenant untouched; every frontier line outside the 20 rows byte-identical; no accepted principle changed; no definition added to tier 1; the rc.2 cut not modified; no em-dash in either new member; no heading deeper than ###; profile terms (graph) appear only inside the ASSURANCE dispositions table, recording a generalisation; every relative link target exists.
RESIDUALS: (1) Members named in prose without a link because they do not yet exist: IDENTITY (§1), RELEASE (opening, §4), GLOSSARY (§5), TICKETS (§8), DESIGN_MODULE (ASSURANCE §2), the Executive baseline (§7, ASSURANCE opening); link them at their activations, steps 4 to 9. (2) Four bounded contexts move owner from SPEC_METHOD to these members (product-definition-routing, semantic-resolution, build-tenancy to PRODUCT_DEFINITION; product-assurance to ASSURANCE); the parallel SPEC_METHOD Writer should not re-claim them; the current SPEC_METHOD §8 has no row for them, so no contradiction found. (3) The schemas and templates named (product-definition and installed-release-manifest schemas, PRODUCT_DEFINITION_TEMPLATE.json, PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md) exist only in the rc.2 cut until packaging step 10 produces the candidate's own; the law does not depend on their presence here. (4) Lawful generalisations recorded in both dispositions tables and the frontier: the Verification Layers example, IACS to the carrier inventory the design declares, the predecessor's mutable source path to the method's source workspace, "standard" to "member", predecessor member names to tenant member names. (5) ASSURANCE §7 reserves room for the baseline testing frames, DESIGN_MODULE 6A to 6C and TICKET test-case authority; none pre-empted. (6) The a_c/ set program and its frames do not encode the new members; packaging step 10. (7) The Reviewer family is not selected here; same-family review would be a declared exception.
MEASURED: input bytes read about 226,000 (design DOCUMENT_STRUCTURE 12,275; standards README 4,511; tenant SPEC_METHOD 11,530; requirements README 2,310; PRODUCT C3 section and headings about 6,200; PRINCIPLES §1 and §3 with headings about 20,000; AXIOMATIC_CALCULUS headings, §1, AC-012, §9 and §11 head about 9,000; REFERENCE_FRAME opening, §4 and §11 heads, §15 head about 8,000; RETURNS tail and headings about 4,000; frontier header and SPEC_METHOD section about 12,500; predecessor SPEC_METHOD cone 52,462 plus headings about 4,000; FOUNDATIONS 28,575; ACTIVATION 25,733; EVALUATION 14,182; injected CLAUDE.md bootstraps about 8,000; command output about 3,000; envelope 500 KB); wall 2026-10-12T03:22:56Z to 2026-10-12T03:34:51Z UTC
STOP BASIS: complete

## W7b2 return, 2026-10-12T03:43:25Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry, parent 3389aba, on tenant/claude/c3-v3-m3b (the SHA cannot be inside its own commit; it is in the Executive-facing return); only standards/PRODUCT_DEFINITION.md, standards/ASSURANCE.md and qualification/RETURNS.md
REPAIR 1 (PRODUCT_DEFINITION §5, per R7b1/R7b2): the parenthetical now reads "(P1, P6; these four kinds are related to the typed relations that AC-012, AXIOMATIC_CALCULUS §4, names, with Semantic Import defined here)"; AC-012 names override, disambiguation, equivalence, specialisation and translation, and Semantic Import is not among them, so the former "these are the typed relation kinds of AC-012 ... applied to terms" over-claimed; the §13 dispositions row already said "related to AC-012 ... without being redefined" and the prose now matches it; AXIOMATIC_CALCULUS untouched.
REPAIR 2 (ASSURANCE §4 and §5): option chosen is restoring the predecessor's "should" in the two clauses rather than a header-level mood rule, because a header sentence would speak for every clause of the member and the reviews examined only these two; §4 now reads "the proving surface should be a scenario bundle or an equivalent ordered set of test cases that exercises that behaviour through a coherent sequence rather than as disconnected fragments"; §5 now reads "That proof should prefer a fresh sandbox or equivalent isolated environment, an installed or built development artifact, and execution through the same declared entry, control and runtime surfaces the real product uses"; the latitude "or an equivalent ordered set" unchanged; no header sentence added.
NON-CHANGES: every other sentence of both members byte-identical (diff is 5 insertions and 4 deletions across the two files); no em-dash; no heading deeper than ###; no other file touched.
MEASURED: bytes read about 15,000 (PRODUCT_DEFINITION §5 region and greps about 2,500; ASSURANCE header and §4 to §5 about 3,200; AXIOMATIC_CALCULUS AC-012 about 900; RETURNS tail about 5,600; command and diff output about 3,000; envelope 80 KB); wall 2026-10-12T03:41:37Z to 2026-10-12T03:43:25Z UTC
## W7a return, 2026-10-12T03:39:43Z

RESULT: candidate_ready
COMMIT: 6e9042c (restatement) and the commit carrying this entry, on tenant/claude/c3-v3-m3a
FILES: standards/SPEC_METHOD.md 91,633 (rewritten; was 11,530); standards/FOUNDATIONS.md 34,548 (was 28,575); standards/ACTIVATION.md 44,532 (was 25,733); standards/EVALUATION.md 21,952 (was 14,182); standards/README.md 6,681 (was 4,511); frontier/PREDECESSOR_CLAIMS.md 89,982 (was 84,059; 59 lines changed, every other line byte-identical); qualification/RETURNS.md (this entry)
ROWS: conserved 58 | superseded 0 | not applicable 1 | unresolved 0 (of 59)
UNRESOLVED: none. The one not applicable row is the "Evidence Rules" heading (96 bytes, no claim beyond naming its three children, which are disposed individually; locus SPEC_METHOD §9).
PLACEMENT: SPEC_METHOD 43 rows (canonical compression, position, method identity, process constitution, manifesto, litmus, constitutional chain, sprint boundary, ambiguity governance, lifecycle sufficiency, change management, universal intake triage, computed classification, consistency gate, UP-013, core interface migration and its nine subsections, release version boundary, evidence rules heading, requirement categories, design rule, renewal path, trace closure with ownership, downstream closure and drift signals, live surface immutability, fundamental migration, transformation wave, legacy classification, requirement classification, specification surface rule, method, ADR conventions and folder convention); FOUNDATIONS 2 (probabilistic work boundary as §2 Work boundary and P0's boundary commitment; recursive product taxonomy as §2 Product lineage objects with the eight concept identities); ACTIVATION 10 (UP-014 in §6 with delivery priority in SPEC_METHOD §8; UP-020 in §1 with the six subsections across §1 Intake, Execution unit, Roles and delegation, §3 Disposition, §5 checkpoint and churn with the six falsifiers, §7 Transition evidence; UP-021 and standing structural qualification in §4 in full, ten forms); EVALUATION 4 (UP-001 §1; UP-008 §2 with the three bases; UP-022 in full across §1, §3, §6, §7 with its nine falsifiers; reconstruction litmus as generic layered sufficiency in §6, its five chain derivations and per-layer diagnoses in SPEC_METHOD §2).
NON-CHANGES: PRODUCT_DEFINITION.md and ASSURANCE.md not created or edited; the parallel cone's 20 rows untouched (still unresolved); a_c/, qualification cases, runs and instruments, reviews/, design/, the common specification/, tickets and the codex tenant untouched; REFERENCE_FRAME.md, AXIOMATIC_CALCULUS.md, CONFORMANCE.md, PROFILES.md untouched; no accepted principle changed; no definition removed from FOUNDATIONS; SPEC_METHOD §1, §3, §4 and §6 keep the roles other members cite (chain and derivation, UP-013, change management and re-entry, lineage and release), so AXIOMATIC_CALCULUS §1 and §7, FOUNDATIONS §6, CONFORMANCE C-08 and C-10 and the README routes still resolve; ACTIVATION and EVALUATION section numbers unchanged (every addition is a subsection or paragraph); no em-dash in any changed file; no heading deeper than ###; every successor anchor referenced from the six files and the 59 rows resolves (generated anchor list; rc.2 routes excluded as provenance); the rc.2 cut not modified.
RESIDUALS: (1) UP-012 not met: POSTING_GUIDE was not read; the first pass's "UP-012 conserved by reference" row is dropped from SPEC_METHOD §12, which now names the guides member as where that row is disposed (step 9). (2) SPEC_METHOD and README link PRODUCT_DEFINITION.md and ASSURANCE.md by the section headings the Executive supplied; they resolve only once the parallel Writer's files land, and the README rows are written from those headings, not from text. (3) Generalisations, recorded in SPEC_METHOD §12 and the frontier: "graph functions" to "published functions"; ambiguity governance's F_D, F_P, F_H to "a profile's runtime shorthands"; UP-014's "Ontology, IACS, Prime" to "a detailed algebra or semantic design view"; UP-013's "Prime" to "the prime law of a design profile"; Method's co_evolution_admissible(B) named without its symbol; "Executive" written "coordinating role" and "Product" written "the selected outcome" in tier 1; SPEC_METHOD §8 binds the generic terms back to the product outcome. (4) Method identity names the D and O owners as "the design profile member (PROFILES §3)" and "its profile member (PROFILES §2)" rather than by rc.2 file name, to keep profile names out of tier-2 prose; the pillar names S, T, D, O and the bounded-context identity are unchanged. (5) FOUNDATIONS §2 now owns the recursive-product-taxonomy bounded context (rc.2 placed it in SPEC_METHOD); the concept identities are unchanged; a one-line change if Jim prefers SPEC_METHOD to keep it. (6) Release criteria, immutable cut publication and selector advancement are carried by provenance in SPEC_METHOD §6 until RELEASE exists (step 6); likewise TICKETS for sprint and ticket mechanics, carrier selection and J/O continuity (step 4). (7) Counterexample localisation is cited to ASSURANCE per the member map; its row belongs to the baseline member (step 5). (8) The pre-existing ACTIVATION §4 and FOUNDATIONS §3 notes naming ODD graph functions as provenance are left as they were (not this cone). (9) The Reviewer family is not selected here; same-family review would be a declared exception.
MEASURED: input bytes read about 291,000 (design 12,275; first-pass SPEC_METHOD 11,530; standards README 4,511; requirements README 2,310; PRODUCT C3 contract 8,023; PRINCIPLES 43,417; frontier head and SPEC_METHOD section 13,562; FOUNDATIONS 28,575; ACTIVATION 25,733; EVALUATION 14,182; AXIOMATIC_CALCULUS head and §11 5,133; REFERENCE_FRAME §15 head and RF-001/002 1,263; predecessor SPEC_METHOD cone 105,470 of 157,952 by section; RETURNS tail, heading lists and command output about 15,000; envelope 800 KB); wall 2026-10-12T03:22:28Z to 2026-10-12T03:39:43Z
STOP BASIS: complete

## W7a2 return, 2026-10-12T06:52:00Z

RESULT: candidate_ready
COMMIT: the commit adding this entry (message prefix "W7a2"); files SPEC_METHOD.md, ACTIVATION.md, design/DOCUMENT_STRUCTURE.md, this file
REPAIRS:
1. The sentence sat in SPEC_METHOD §2 Constitutional chain, not §1. The whole sentence was removed, its leading clause too (no rc.2 predecessor for "own territory"); the paragraph now ends "(PRODUCT_DEFINITION §8). Conformance of a tenant is judged under EVALUATION §6; ...". §11 gains: "Tenant territory is imported from the same source, its Territory rule, and is not law of this method: a tenant commits only in its own territory; a needed common change is requested from the common WHAT's writing owner and reaches the tenant by merging the main lineage inward; a tenant does not edit tickets, common files or a peer tenant's realisation." The word "pen" no longer occurs in either standard.
2. §12 note adds: "graph" dropped from the consistency gate's reconciliation surfaces, which design and module cover (§4); "graph-native meaning" written "realisation meaning" in the method identity (§1); the sprint boundary's `UX_METHOD.md` written "a profile" (§4); the procedures' `GOALS.md`, `INTENT.md`, `PRODUCT.md` and `requirements/` written as surfaces and "installed STDO basis" as "installed basis" (§4); `REQ-*` and `INT-*` written "requirement identifiers" and "intent identifier" (§10); the overlay fields `what`, `how.build_tenants`, `how.build_tenants[].design` and `how.common` written in prose as WHAT bindings, build-tenant bindings, the tenant design surface and the common surface (§1, §2, §10).
3. §1 "modules, functions, build tenants" and §2 "module, function, runtime surface"; note: "graph functions" is written "functions" (§1, §2).
4. §5: "remain hard stops regardless of risk appetite. Typical hard-stop classes include: a violated invariant or guarantee; ...". Residual, not edited because it is outside the brief: the §12 row #ambiguity-governance-rule routes the hard stops to ACTIVATION §4. That conserved owner still states the list closed ("Some conditions are hard stops regardless of appetite: ...") and needs the same open marker; this is ticketable.
5. ACTIVATION §1: (a) "The restriction that a coordinating role mutates nothing remains applicable (P6, P3)." The conditional was dropped; no baseline locus is cited because PROFILES has no Executive section and EXECUTIVE_BASELINE is unbuilt. (b) "it may enter directly as constructor or Writer".
6. DOCUMENT_STRUCTURE: (a) row "SPEC_METHOD.md | ... ACTIVATION (UP-014, UP-020, UP-021; consumes the work boundary); FOUNDATIONS (work boundary, product taxonomy); ..."; (b) FOUNDATIONS row "ontology with the frame objects (§2), C (proposed as P0) ..."; REFERENCE_FRAME row "the frame law: RF-001 to RF-017; engagement; ..." (the object list was dropped to stay under budget); (c) "Two first-pass errors are retired: sizing the corpus to one activation, and counting a route to the rc.2 clause (FOUNDATIONS §1) as a disposition. The corpus is as large as the law requires and an activation reads a projected frame; a route is provenance under the standalone successor requirement."
ANCHORS: a scripted check found 251 member-§ references and 11 relative links resolving to headings in standards/ on this branch, including PRODUCT.md#development-isolation. The 5 name tails it flagged are prose or section titles, and all 5 resolve. Pending merge: PRODUCT_DEFINITION §1 (4), §5, §8 (3), §11, §12 (2); ASSURANCE §1, §3, §4; the file links PRODUCT_DEFINITION.md and ASSURANCE.md in the SPEC_METHOD head. Absent, unbuilt and not named in the brief: TICKETS (11 references), RELEASE (5) and EXECUTIVE_BASELINE (1), all cited by bare member name with no § anchor.
DESIGN BYTES: 12,277
NOTES: no em-dashes and no headers deeper than ### in the three files. Trailer conflict: a later harness reminder named "Claude Opus 5.5". The brief's Fable 5.1 lines were used because they match the running model.
MEASURED: bytes read about 70,000 (command output, sections and greps; no whole-file reads except the design map at 12,275); wall 2026-10-12T06:07:07Z to 2026-10-12T06:55:40Z. That is about 49 minutes, over the 25-minute envelope.
STOP BASIS: complete

## W11 return, 2026-10-12T07:14:37Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry (message prefix "W11: restate STDO_REFERENCE_FRAME_BASELINE"), parent 501e64c, on tenant/claude/c3-v3; the SHA cannot be inside its own commit and is in the Executive-facing return
FILES: standards/EXECUTIVE_BASELINE.md 105,646 (new); standards/ASSURANCE.md 58,591 (was 12,443; §7 to §13 added, dispositions renumbered §14); standards/EVALUATION.md 25,814 (was 21,952; §4 Result and triage projection, §8 rows); standards/README.md 7,763 (was 6,681; one document row, one route); frontier/PREDECESSOR_CLAIMS.md 98,745 (69 lines changed, all in the STDO_REFERENCE_FRAME_BASELINE section, every other line byte-identical); qualification/RETURNS.md (this entry)
ROWS: conserved 67 | superseded 0 | not applicable 2 | unresolved 0 (of 69). Not applicable: #profile-terms (17 bytes) and #product-owned-adoption-or-project-defined-configuration (59 bytes), both heading-only with children disposed individually.
PLACEMENT: EXECUTIVE_BASELINE 49 rows (§1 to §22, table of dispositions in §23); ASSURANCE 18 rows (testing frame, authoritative Product path, material combinatorial complexity, the testing frame set and its four frames, testing value, path erasure, evidence composition, subject acquisition, counterexample localisation, interface integration frame with its four subsections); EVALUATION 1 row (reviewer result and triage projection); canonical compression split EB §1 and ASSURANCE §7.
FIRST-PASS LOSSES RESTORED: twelve-family table (EB §11), four testing frame tables of eleven elements and the interface frame of twelve (ASSURANCE §7, §13), five drift locks as a table and the no-mutation rule (EB §6), severity, priority, frame result and boundary effect as four distinct values (EB §5, EVALUATION §4), promotion constraint projection with four rows (EB §12), failure classification with 28 rows (EB §20). Counts checked by script: 28 failure rows, 32 anti-patterns, 26 qualification items, 24 closure items, 8 handoff rows, 14 coverage rows, 5 triage rows, 4 claim boundaries, 10 interface cases, 8 testing-value terms.
MODAL RULE (coordinator, mid-task): applied before commit; corrected "enters directly" to "may enter directly", "mutates only" to "may mutate only", "can be written" to "may be represented", "Evidence relates" to "may relate", "stays reachable" to "may remain reachable", "exactly one of" to "one of", and removed "a fixed consequence"; "at least", "commonly", "normally", "often" and the "Minimum material content" header kept.
DEVIATION FROM BRIEF: testing frame, authoritative Product path and material combinatorial complexity are defined in ASSURANCE §7 (tier 2), not EXECUTIVE_BASELINE, because the tier-2 testing frames use them and tier 2 cannot import tier 3; EB §5 points to them. ASSURANCE and EVALUATION carry no Executive, Worker, Reviewer or family name outside their disposition tables (checked by script); the family relations to the testing and interface frames are EB §11.
NEW SENTENCES (criterion 6): EB preamble binds Worker, Reviewer and Executive to the constructor, assessor and coordinating role of ACTIVATION §1 (mapping, no obligation); EVALUATION §4 states that the recommended disposition is evidence, never a disposition, priority or boundary effect, reconciling §4's existing "recommends a disposition" with the predecessor's "no priority or disposition".
RESIDUALS: (1) Outside territory, stale: README's ASSURANCE row and the "prove a realisation" route still list §1 to §6; SPEC_METHOD §8 routes the Executive, Worker and Reviewer catalogue to PROFILES rather than EXECUTIVE_BASELINE; PROFILES' index lacks EXECUTIVE_BASELINE; ACTIVATION §1 says no baseline locus is cited because the member was unbuilt (EB §6 now exists). (2) Unbuilt members named without link: DESIGN_MODULE, IDENTITY, RELEASE, TICKETS. (3) Generalisations recorded in the tables: UP-007, UP-017 to UP-023, UP-001, UP-008, UP-022 written as their tenant sections or the design profile; IACS as the carrier inventory the design declares; "Ontology" as the design's ontology; the adoption block heading as "Executive Baseline Adoption Additions"; "Apply Steel-Thread Delivery" as SPEC_METHOD §8; family names in ASSURANCE written as concerns. (4) The interface frame URN is unchanged and resolves in REFERENCE_FRAME's context while its law sits in ASSURANCE; the reviewer should confirm that split. (5) a_c/ set program does not encode the new member (packaging step 10). (6) The Reviewer family is not selected here; same-family review would be a declared exception.
NON-CHANGES: FOUNDATIONS, REFERENCE_FRAME, ACTIVATION, AXIOMATIC_CALCULUS, SPEC_METHOD, PRODUCT_DEFINITION, CONFORMANCE, PROFILES, design/, a_c/, the common specification/ and the rc.2 cut untouched; no em-dash and no heading deeper than ### in any changed file; every relative link and anchor in the four standards files resolves (scripted); every frontier locus anchor generated from the actual headings.
MEASURED: input bytes read about 290,000 (predecessor 133,684 whole; DOCUMENT_STRUCTURE 12,277; tenant ASSURANCE 12,443; standards README 6,681; excerpts of ACTIVATION 20,348, REFERENCE_FRAME 23,540, FOUNDATIONS 6,496, EVALUATION 5,827, SPEC_METHOD, PRODUCT_DEFINITION and PROFILES 11,635, frontier 20,881; requirements README grep about 3,500; RETURNS tail about 11,000; heading lists, modal grep and command output about 22,000; envelope 600 KB); wall 2026-10-12T06:57:53Z to 2026-10-12T07:14:37Z UTC (first commit 07:11:25Z; repairs below amended into the same commit)
PRE-RETURN REPAIRS (advisor check, amended into this commit): (a) ASSURANCE §7 had made the testing set unconditional tier-2 law; the predecessor's condition "when this profile supports" is now carried as selection by the governing frame configuration (PRODUCT_DEFINITION §7) or admitted work authority, placement makes the set and §8 to §13 available and adopts nothing, and §13 says the same; recorded in the §14 row. Residual: making the set mandatory for every project would be Jim's decision. (b) EVALUATION §4 had written the triage policy as project-owned; restored to Product-owned and Product-defined, scales bound by the adopting Product. (c) Principle gate scripted over every prose paragraph of the new text: ten paragraphs lacked a P citation and now carry one (EB §7 twice, §7 notation, §12 steps 3 and 5B, §18 and §22 leads; ASSURANCE §7 fan-out, §10 and §12 leads); the remaining flags are line-wrap artefacts. Family names (Proof, Operator, Owner, Entity, Install, Effect, Design Component) are absent from ASSURANCE and EVALUATION prose.
## W9 return, 2026-10-12T06:57:10Z

RESULT: candidate_ready
COMMIT: 271b626 (restatement), d0b0632 (first return entry), afd8fe3 (reviewer-facing fixes) and the commit carrying this revision of the entry, on tenant/claude/c3-v3-m4
FILES: standards/TICKETS.md 72,314 (new); standards/SPEC_METHOD.md 92,203 (was 91,633; pointer links only, in §4 Change classes, Computed classification, Consistency gate, Sprint execution boundary, Carriers and the §12 table and closing paragraph); frontier/PREDECESSOR_CLAIMS.md 94,346 (was 89,982; 49 table lines changed, every other line byte-identical, verified by diff); qualification/RETURNS.md (this entry)
ROWS: conserved 46 | superseded 0 | not applicable 3 | unresolved 0 (of 49)
UNRESOLVED: none. Not applicable: #core-model (14 bytes), #sprint-rules (16), #ticket-rules (16), each a heading with no claim text whose children are disposed individually.
PLACEMENT: all 49 rows land in TICKETS: §1 work carriers (goals, ticket records, sprints, comments, execution contracts, UP-006); §2 default layout, bindings and projections, carrier substitution (future extensions); §3 sprint rules (record, manifest fields, status, admission, compliance escrow, close review); §4 ticket rules (record, multi-build-tenant independence, required fields, types, category, inside-out sequencing, change class, upward propagation check, triage metadata, status, lanes); §5 carrier selection with the table, execution contract admission, evaluation criteria and non-closure conditions, bounded-context term binding; §6 implementation migration (declaration and checklist, closure of a migration ticket, strategy requirements, recurring realisation and library declaration, multi-build-tenant review, review disambiguation, impacted interface checklist, break order and break-to-closure map, mixed-state negative proof); §7 UP-007, judgment continuity, condition-based closure, test case authority, UP-009; §8 the three shapes verbatim; §9 operating mode and relationships; §10 the anchor | disposition | locus table. Three rows also name the members where part of their determinations is defined once: the work-carrier row names ACTIVATION §1 Admission; the execution-contract-admission row names ACTIVATION §1 Admission and SPEC_METHOD §3; the implementation-migration-category row names SPEC_METHOD §7 Constitutional migration options. Test case authority anchor for ASSURANCE §3: TICKETS.md#test-case-authority.
README ROWS NEEDED: document table: | [TICKETS.md](TICKETS.md) | 2 | work carriers: 1 goals, tickets, sprints, comments, execution contracts, milestones (UP-006); 2 layout, bindings, carrier substitution; 3 sprint rules with compliance escrow and close review; 4 ticket rules with required fields, change class, upward propagation check, triage metadata, status and lanes; 5 carrier selection and the carrier side of admission, evaluation criteria, term binding; 6 implementation migration; 7 UP-007, judgment continuity, condition-based closure, test case authority, UP-009; 8 recommended shapes; 9 operating mode and relationships |. New route: | open, carry or close a piece of work | [TICKETS §5](TICKETS.md#carrier-selection) for the smallest lawful carrier and the carrier side of admission, [§4](TICKETS.md#4-ticket-rules) for the fields and the upward propagation check, [§7](TICKETS.md#condition-based-closure-and-reuse) for closure by condition |. Amend the triage route with "then [TICKETS §4](TICKETS.md#triage-metadata) for what the ticket records"; the migration route with "[TICKETS §6](TICKETS.md#6-implementation-migration) for the ticket's declaration and checklist"; the resume route with "[TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) for recorded judgment and owner rulings".
NON-CHANGES: FOUNDATIONS, ACTIVATION, EVALUATION, README, REFERENCE_FRAME, AXIOMATIC_CALCULUS, CONFORMANCE, PROFILES untouched; ASSURANCE and PRODUCT_DEFINITION not created; SPEC_METHOD outside §4 and the §12 table and closing paragraph untouched, no restructuring; a_c/, qualification cases, runs and instruments, reviews/, design/, common specification/, tickets and the codex tenant untouched; no accepted principle changed; no definition added to tier 1; ACTIVATION §1 admission not restated (TICKETS names the topics and points); no em-dash; no heading deeper than ###; every TICKETS link anchor and every locus of the 49 rows (54, across TICKETS, ACTIVATION and SPEC_METHOD) resolves by generated anchor list; no profile term (graph, ODD, GTL, world model, HoG, F_D, F_P, F_H, Executive, AssetSurface) in TICKETS outside §10; six of the seven rc.2 code blocks carried byte-identical, the seventh (test derivation chain) generalised.
RESIDUALS: (1) ACTIVATION §8 lists "TICKET judgment continuity | conserved; §7" and EVALUATION §3 says it "conserves UP-007"; the frontier loci for both rows are now TICKETS §7, with ACTIVATION §7 and EVALUATION §3 as generic forms; harmonise those notes at those members' next touch (outside territory). (2) SPEC_METHOD's intro still says TICKETS exists "only after" its activation and leaves TICKETS unlinked, as does §1 Method identity (T pillar); both lie outside §4, so they are unchanged. (3) PRODUCT_DEFINITION §1, §4, §5, §8 and ASSURANCE §3 are cited in plain text because those files are on another branch; ASSURANCE §3 should link TICKETS.md#test-case-authority. (4) Generalisations, recorded in TICKETS §10 and the frontier: escrow "public graph functions or AssetSurface contracts" to "public published-function or public carrier contracts", "UX interactions" to "user-interface interactions"; review question 8 "F_D-like" and "F_P-like" to "other deterministic checks" and "constructive or probabilistic path"; "graph function" and "graph-function" to "published function" in negative proof and test case authority; "Executive appointment" to "coordinating appointment"; rc.2 SPEC_METHOD what-how-and-work-carriers cited as PRODUCT_DEFINITION §8. Verbatim code blocks keep "Product", "UX" in the sprint example title, and American spellings. (5) Sentences for criterion 6 review, each derived and none new law: §5's carrier-side recording rule (the admitted result with its coordinates is recorded on the ticket or manifest when that is the bound result surface; from the record-before-return rule; an unsourced "referenced otherwise" clause was dropped in afd8fe3); §6's sentence that the checklist's second item is met by explicitly declaring absence (derived from rc.2's B-010 example, which adds "or explicitly declared absent"); §2's sentence that a generated board is a projection and a tracker a rebinding (derived from rc.2 Authority). (6) The a_c/ set program and frames do not encode TICKETS, and no projected frame exists for its tasks (criterion 4); this is packaging work outside territory. (7) Trailer: a mid-session system reminder named "Claude Opus 5.5"; the commit uses the activation's exact Fable 5.1 lines as instructed. (8) The Reviewer family is not selected here; same-family review would be a declared exception. (9) Wall envelope exceeded: 195 minutes against 150.
MEASURED: input bytes read about 349,000 (design DOCUMENT_STRUCTURE 12,275; PRINCIPLES 43,417; PRODUCT C3 lines about 8,000; requirements README 2,310; predecessor TICKET_METHOD 60,674; SPEC_METHOD 91,633; FOUNDATIONS about 34,500; ACTIVATION §1 and §5 to §8 about 28,000; EVALUATION §1 to §5 about 9,000; REFERENCE_FRAME head and §14 to §15 about 13,500; AXIOMATIC_CALCULUS §11 about 4,500; standards README 6,681; frontier head and TM section about 11,000; RETURNS tail about 8,000; command output about 15,000; envelope 700 KB); wall 2026-10-12T03:42:31Z to 2026-10-12T06:57:10Z
STOP BASIS: complete (wall envelope exceeded and reported)

## W9b return, 2026-10-12T07:13:06Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry, on tenant/claude/c3-v3-m4, parent a2c37ee
REPAIR 1 (modal force, 24 rows: 23 should or may, 1 recommended): §3 sprint naming "the filename should carry"; §3 escrow "The following may be eligible" and "The following may not be hidden"; §3 `remove` "should be backed out"; §4 ticket naming "the filename should carry"; §4 multi-tenant "Recommended examples" and "If a tenant-local duplicate exists, it should record"; §4 required fields "should also carry, at minimum"; §4 types "should be enough"; §4 spike "should terminate"; §4 lanes "should remain visible"; §5 admission "should treat" and "should be logged"; §5 evaluation criteria "should expose" and "should make ... visible"; §6 migration closure "may not remain silently authoritative"; §6 milestone "may continue within the bound" (the added "only" removed); §6 review disambiguation "should include" and "should be able to answer"; §6 impacted interface "should enumerate"; §6 mixed-state "should include"; §7 claimed review "may support"; §7 condition-based closure "may record"; §7 test case "should derive". The tenant's must-to-indicative convention is unchanged.
REPAIR 2: "the contract carries at minimum the states named in ACTIVATION §1 (drafted, admitted, rejected, superseded)".
REPAIR 3: "When a ticket is fixed and a mismatch appears between implementation behaviour and test expectation, review reconciles the mismatch in this order".
REPAIR 4: SPEC_METHOD §4 now reads "[TICKETS §4](TICKETS.md#change-class) records the class on the carrier."; the upward-walk substance stays in TICKETS §4 only.
REPAIR 5: TICKETS §2 "a tracker that holds tickets is lawful only as an explicit rebinding of the ticket authority by the product definition with no rival surface remaining".
REPAIR 6: TICKETS §8 sentence deleted; its citation moved into the preceding parenthetical "(§2; P3, P4b; rc.2 #recommended-ticket-shape)".
CHECKS: 30 relative links in TICKETS and SPEC_METHOD resolve (0 bad); no em-dash in added lines; no added line over 80 characters; §10 rows for #recommended-ticket-shape and #future-extensions remain consistent with the new text; the §6 checklist sentence already reads "at least this checklist", so the predecessor's minimum holds; the removed phrases have no hit in frontier/PREDECESSOR_CLAIMS.md or the SPEC_METHOD §12 table.
RESIDUAL: ACTIVATION §1 (line 89) states a closed set, "A contract is in one of the states drafted, admitted, rejected or superseded", and the TICKETS §10 row for #execution-contract-admission routes the states there; TICKETS §5 now states those as a minimum. The conflict sits in ACTIVATION, outside W9b territory, and needs routing by the Executive.
MEASURED: input bytes read about 65,000 (predecessor TICKET_METHOD targeted passages about 14,000; TICKETS targeted sections about 32,000; SPEC_METHOD W9 diff and §4 lines about 7,000; ACTIVATION §1 lines about 500; RETURNS tail about 2,000; command output about 10,000; envelope 200 KB); wall 2026-10-12T07:08:50Z to 2026-10-12T07:15:04Z
STOP BASIS: complete

## W12 return, 2026-10-12T07:36:20Z

RESULT: candidate_ready
COMMIT: the commit carrying this entry (message prefix "W12: restate RELEASE_METHOD and IDENTITY_METHOD"), on tenant/claude/c3-v3, parent 978d324 (the Executive's ASSURANCE repair landed on the branch during this activation; it touches only ASSURANCE.md and does not overlap this territory); the SHA is in the Executive-facing return
FILES: standards/RELEASE.md 36,121 (new, tier 2); standards/IDENTITY.md 20,297 (new, tier 1); standards/FOUNDATIONS.md 36,150 (was 34,548; §2 Release objects paragraph; §6 rows for UP-004 and UP-015 amended, two rows added); standards/EVALUATION.md 26,867 (was 25,814; §5 UP-015 as acceptance evidence; §8 UP-004 row amended, UP-015 row added); standards/README.md 9,477 (was 7,763; two document rows, the release route amended, two routes added); frontier/PREDECESSOR_CLAIMS.md 106,602 (45 table lines changed, every other line byte-identical, verified by diff); qualification/RETURNS.md 110,031 (this entry appended)
ROWS: conserved 39 | superseded 1 | not applicable 4 | unresolved 1 (of 45). RELEASE_METHOD 22 of 22 conserved. IDENTITY_METHOD 17 conserved, 1 superseded (#release-version-boundary), 4 not applicable (#core-law, #authority-split, #default-formats-and-overrides, #examples: heading lines only, children disposed), 1 unresolved.
UNRESOLVED: #defaults-from-a-bound-abg-realization, "member 7, DESIGN_MODULE": what a consumer-bound realisation of the ABG role publishes for its runtime surfaces and default ODD surface kinds used by default F_D helpers is realisation default; the row's identity-law determinations (starter conventions and convenience contracts, not doctrine, lawful only while overridable) are already restated in IDENTITY §7 Derived domain overrides.
PLACEMENT: RELEASE §1 context and position; §2 identities, qualified refs, subtree, historical conservation; §3 phases with candidate, publication (10 steps), qualification, advancement (7 steps, 4 refusals); §4 selector and adoption, with the plan object, hashing and commands pointed to PRODUCT_DEFINITION §4; §5 naming; §6 assets and Product subject; §7 cohorts, two-commit construction (8 steps), qualification and recovery; §8 acceptance (7 criteria) and external dependencies; §9 UP-015 in full (origin immutability, "one semantic disposition", the four dispositions as worded, the support-line paragraph); §10 both open questions; §11 table. FOUNDATIONS §2 Release objects defines candidate source, release subject and version-line selector beside the release cut, once; RELEASE §2 realises them. IDENTITY §1 to §12 restate every IDENTITY law; UP-004 in full in §6.
GENERALISATIONS (tier 1, recorded in IDENTITY §13): graph_function, asset_surface, graph_call written published_function, carrier_surface, function_call; "graph calls" as "function calls" and "frames" as "execution frames"; UP-004's "graph-native surfaces may project the relation as F_H" as a profile's own term (PROFILES), "may" kept; "bound ABG realization" and "consumer-bound realization of the ABG role" as runtime realisation. RELEASE (recorded in §11): "Release Method bytes" as "bytes of this member"; "must remain usable as one versioned set" as "need to remain usable", the declaration condition.
MODAL CHECK (scripted, predecessor against new text before the tables): RELEASE may 18/18, optional 6/6, never 4/4, cannot 10/10, must 3 to 0 (indicative); IDENTITY should 16/16, at minimum 2/2, at most 1/1, optional, useful, suitable 1/1 each, may 16/15 (the missing one is the unresolved row's "may publish"), must 17 to 0 (indicative). List counts checked: 7 identities, 4 ref shapes, 7 subtree bindings, 10 publication steps, 6 qualification bindings, 7 advancement steps, 4 refusals, 9 naming items, 6 assets, 4 subject declarations, 5 cohort members, 8 two-commit steps, 7 acceptance criteria, 7 minimum questions.
RESIDUALS: (1) Supersession for review: IDENTITY_METHOD #release-version-boundary calls the selector "latest-accepted"; RELEASE_METHOD, which that clause cites, makes it the highest-ordinal published cut and says acceptance never moves it. The row is superseded by RELEASE §1 (selector paragraph), §3 Exact-cut qualification and §8 Acceptance criteria; its other determinations are restated unchanged in IDENTITY §9. (1a) The brief names "identity versus content" and "rename and move rules" among the IDENTITY laws; no rc.2 IDENTITY_METHOD row carries a separate law for them and nothing was added. Where they already sit: rename, IDENTITY §2 Stability (a changed identity makes the relationship explicit, never silent reuse); move, RELEASE §2 Project-subtree release identity (moving a project changes the locator and cut identity, not the namespace); identity versus content, FOUNDATIONS §2 Object (identity survives admissible state and encoding change), AC-002 and AXIOMATIC_CALCULUS §8 (content-first identity). (2) Outside territory, now stale: SPEC_METHOD's lead (RELEASE "existing only after" activation), §1 Method identity ("RELEASE; until that member exists, §6") and §6 ("until that member exists this section carries them", and its UP-015 paragraph, which now duplicates RELEASE §9 and should become a pointer); AXIOMATIC_CALCULUS §8 "constructed at its own activation; until then SPEC_METHOD §6"; PRODUCT_DEFINITION's plain-text "(the RELEASE member)" and "(the IDENTITY member)"; EXECUTIVE_BASELINE's unlinked IDENTITY and RELEASE; FOUNDATIONS §1 and §2 still route UP-015, UP-004 and scoped identity to rc.2 rather than to RELEASE §9 and IDENTITY; EVALUATION §5's UP-004 link still routes to rc.2; README lacks the TICKETS document row. (3) RELEASE §4 restates the plan's bindings and drift rule beside PRODUCT_DEFINITION §4's definition because the selector row requires them; the reviewer should confirm that is pointing, not a second definition. (4) The a_c/ set program does not encode either member (packaging step 10). (5) Reviewer family not selected here.
NON-CHANGES: SPEC_METHOD, PRODUCT_DEFINITION, AXIOMATIC_CALCULUS, ACTIVATION, REFERENCE_FRAME, ASSURANCE, TICKETS, EXECUTIVE_BASELINE, CONFORMANCE, PROFILES, design/, a_c/, the common specification/ and the rc.2 cut untouched; frontier lines 419 and 422 (SPEC_METHOD rows) untouched; no em-dash, no heading deeper than ###, no prose line starting with "#"; every relative link and anchor in the five standards files resolves and every frontier locus anchor was generated from the actual headings (scripted); no profile term (graph, ODD, GTL, F_D, F_P, F_H, ABG, Executive, AssetSurface, Git, tag) in IDENTITY before its §13 table; every prose paragraph of both new members cites a principle (scripted).
MEASURED: input bytes read about 165,000 (predecessors 37,436 whole; DOCUMENT_STRUCTURE 12,277; requirements README 2,310; frontier header and the two sections about 11,500; standards README 7,763; FOUNDATIONS excerpts about 22,000; EVALUATION excerpts about 6,000; AXIOMATIC_CALCULUS §7 and §8 excerpts about 7,500; SPEC_METHOD §6 2,900; PRODUCT_DEFINITION §1 and §4 about 15,700; TICKETS head and §10 about 4,000; RETURNS tail about 13,000; heading lists and command output about 20,000; envelope 350 KB); wall 2026-10-12T07:24:25Z to 2026-10-12T07:38:43Z UTC (first commit 1c76e35 at 07:36:20Z; advisor repairs amended into the same commit)
STOP BASIS: complete
