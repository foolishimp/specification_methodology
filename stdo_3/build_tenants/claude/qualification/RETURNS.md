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
