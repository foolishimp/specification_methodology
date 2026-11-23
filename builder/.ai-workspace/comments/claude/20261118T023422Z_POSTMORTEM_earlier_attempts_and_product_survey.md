# Post-mortem of the earlier attempts, and a survey of equivalent products

**Type:** POSTMORTEM. Commentary for the product owner, not law.
**Author:** claude (Fable 5.2) · 18 November 2026
**Purpose:** the grounds for the second round of the STDO Builder requirements.

## What was read

- **The owner's typed prompts** to Claude and Codex, February to November 2026.
  The three prompt histories hold about 26,000 entries. A filter for words of
  intent and failure kept 7,506 of them, and a stricter one 2,981. Three
  readers went through every one of those and took the 180 strongest
  statements of intent, 179 reports of failure and 90 statements that bear on
  an open decision. A script checked each quotation against its source line.
- **The repositories** from c4h (December 2024) to odd_glc, and twenty
  post-mortems and lessons files written at the time.
- **Equivalent products**, from my own knowledge, checked against the current
  public record and against the four products cloned on this machine.

Limits. Before February 2026 there are no prompts, only repositories. The
counts below are of the statements selected, not of all prompts. My September
post-mortem, the one earlier synthesis of this record, was deleted in the
mothball of 18 November; this is built again from the sources. The extracts
stay outside the repository. Only short quotations of the owner's own words
appear here, with his spelling.

## 1. The attempts

| Attempt | Dates | Size at its end | Where the truth of the work lived | How it ended |
|---|---|---|---|---|
| c4h | Dec 2024 to May 2025 | 11,400 lines | The target project's files, with a lineage file per agent | Stopped; no record of why |
| ai_sdlc_method | Oct 2025 to Mar 2026 | 200,400 lines, 749 Markdown files | A Markdown specification and an event log | Superseded: it "cannot be re-derived from first principles" |
| abiogenesis 0 to 2 | Mar to Apr 2026 | 34,900 lines | The event log: "Assets are not stored — they are derived by reading the event stream." | Continued as version 3 |
| genesis_sdlc | Mar to Apr 2026 | 34,400 lines | The event log: "Recovery is replay." | Replaced for its "migration baggage" |
| odd_sdlc | Apr to Jun 2026 | 154,500 lines | The specification, and the runtime's typed records | Superseded by odd_glc |
| abiogenesis 3 | Apr to Jun 2026 | 117,000 lines | The event stream and a payload ledger | Twelve release candidates of 3.9, then renumbered 4.0 |
| odd_glc | Jun to Sep 2026 | 4,100 lines | The runtime's records; its goals page records one run that closed at 1.24 GB | The owner's ruling: "the product revisions are wrong" |
| abiogenesis 4 to 5 | Jun to Nov 2026 | 151,100 lines, measured on 18 November before the mothball | The runtime's ledger and event log | Mothballed on 18 November 2026 |

Two things hold across most of the table. Most successors began as a clean
restart, kept the same core and added a layer above it; the abiogenesis
versions are the exception, each continuing the same repository. And from March
2026 the attempts kept the truth of the work in an event record and rebuilt
their state from it. odd_sdlc is a part exception: it resumed by running its
start command again over the workspace, on a runtime that kept an event
record.

## 2. What the owner asked for throughout

| | His words | Date |
|---|---|---|
| A deterministic framework holds control and the agent does the work | "the frame work IS the executor and the LLM slave to it" | 31 Aug |
| | "once control is passed to ABG it remains in ABG until it exits" | 11 Jun |
| The framework governs and does not say how | "its the gate keeper but doesnt say how things are to be done" | 30 May |
| | "i dont want to write my own claude cde" | 23 Mar |
| The agent is given references | "we just need to pass them references that they can access" | 29 Mar |
| The specification is the truth, and the product can be built again from it | "i can rebuild the system just from the intents" | 20 Mar |
| One current truth; history belongs to git | "git is for history - no.1 rule" | 4 Apr |
| Proof is a live run from end to end on a clean install, as a user | "the only real test is deployment and the full life cycle testing" | 16 Mar |
| The author is not the judge | "i dont trust it because its context is what caused the problem" | 24 Jul |
| | "independent assurance of the UAT.integration tests which are derived from spec and design, not code" | 21 Mar |
| Nothing is orphaned | "if the req is live then it needs to appear in code" | 26 Mar |
| A change is an amendment, entered at the right level | "a rebuild only of the dependencides on the requirement change" | 19 Apr |
| | "reentry with a ticket and a cold start are both a triage for proportionality and an entry at the appropriate level in a graph" | 17 Jun |
| Weight in proportion; waste is a defect | "abg bloat is very very bad" | 21 Mar |
| | "finding waste is a p1 or p2 bug so it must be resolved" | 16 Sep |
| It can be seen what happened | "the purpose of the system is to know what happened, thats auditing" | 20 Sep |
| It is used on itself | "mvp means i can eat my own dog food" | 30 Aug |
| It serves a user who cannot inspect the engineering | "non technical users can make changes to the specification the automation can then reliably build their amendments to an existing system" | 11 Nov |

## 3. What the owner changed his mind about

**The event record.** In February: "i think modelling event sourcing is the
methodology". In April: "true event sourcing is not possible, the purpose of
event sourcing in an F_P world is to allow forensic analysis". In May: "The
Workspace is the stateful reality", in a message that still lists an "immutable
event log" and "the ledgers" among the system's truths. In September: "restarting is just from the
current state of the worksapce which is mutable, there is nothing to
reconstruct". In October: "even without an eventlog, mutable state is in
workspace, you can restart". In November: "proof, evidence, everything exists
in the work space".

The code and the specifications kept the February position through every
restart. On 31 August he wrote: "i had to abandon last version of abg because
we made a huge mistake that workspace was not being treated as mutable". The
approved intent of STDO Builder is the first to put the workspace first.

**Who judges.** Deterministic ledgers until May. Then the agent's own reading:
"eval.F_P over the workspace is they highest level of truth" (24 May). Then an
independent reviewer (October), at release boundaries (November).

**Who picks the next step.** "optimal path choice … can be derived in the
moment" (24 April). Then "there should not be an outer loop" (11 June) and
"graph entry beyonnd current traversal is F_H only" (12 September). Then an
executive that "chooses the appropriate graph functions" (11 November), and six
days later "the control harness is explicity deterministic over the llm agent".

**Where new work comes from.** In February the system was to raise its own
intent from what it observed. By June a gap becomes a ticket that is triaged.

## 4. How the builds failed

Counts are of the 179 selected reports.

| Cause | Feb–Mar | Apr–May | Jun–Nov | All | In his words |
|---|---|---|---|---|---|
| An agent lost or rewrote what he had decided | 10 | 16 | 9 | 35 | "why are there excuses in my intent" |
| The agent, or code around the framework, took control | 9 | 10 | 5 | 24 | "we went straight to code and didnt create the assets" |
| Work was called done on something other than the real work | 6 | 8 | 6 | 20 | "they SAID they converged" |
| A copy or a second record was treated as the truth | 9 | 3 | 8 | 20 | "oh no we are building a 2ndary engine again!!" |
| Weight, slowness and token cost | 5 | 6 | 9 | 20 | "why is this so much slower than running claude directly" |
| A request became a rewrite | 5 | 5 | 9 | 19 | "all i wanted to do was add a catalog capabilityt to 4.6 and instead i have 3 weeks of churn" |
| Reviews and tickets passed work that had drifted | 2 | 7 | 9 | 18 | "why have your reviews allowed this drift?" |
| A decision to start again | 8 | 3 | 4 | 15 | "i regret not starting from scratch" |

The remaining eight are faults of tooling (five) and unclassed (three). The
three periods are of two, two and six months, and each count is of the sixty or
so reports selected for that period, so the columns are not rates.

## 5. Three patterns under the causes

**Most restarts kept the premise and added a layer.** The engine, then a
software-lifecycle package over it, then a general lifecycle framework, then a
manager, then an executive. The premise they kept is the one the owner dropped
in April: state rebuilt from an event record.

**Remedies often added weight.** The assistants wrote thirteen post-mortems
between July and September. Several fixes added a gate, a role or a record, and
later post-mortems name some of those additions as causes. Other remedies took
weight away: a limit on work in progress, one gate in place of several, "A
finding blocks its exact claim." Codex, 24 July: "STDO acted
as a correctness amplifier. Once the Product destination and work ordering
drifted, the method made the wrong work more exhaustive, more reviewed, more
evidenced, and harder to stop." In one week there were 84 self-reviews and 219
commentary posts.

**"Done" was judged on something other than the real work, in at least five of
the eight attempts.**
c4h: no merge errors. ai_sdlc_method: "delta=0 via skips ≠ converged".
abiogenesis 1: the test harness issued the assessment itself. odd_sdlc: it
accepted Markdown as code, and built 7 source files where the reference build
had about 105. abiogenesis 5: "Green count increased while product reachability
remained zero."

## 6. The field

Three kinds of product do something like this.

- **Specification kits** (Spec Kit, Kiro, BMAD, OpenSpec, Superpowers). The
  method is files and prompts in the repository, and the agent drives.
- **Orchestration runtimes** (LangGraph, Temporal, CrewAI Flows). A
  deterministic controller drives, and the truth is the runtime's own state or
  history, which it replays.
- **Build systems and reconcilers** (Make, Bazel, Kubernetes controllers).
  They read the files as they are now and act on the difference. They are not
  LLM products, and they are the nearest to the owner's model.

A paper of September 2026 (Consort) sorts the ways a method is enforced on an
agent into three: persuasion by prompts, structure by specifications, and
"controls the agent cannot edit". STDO Builder is of the third kind. That paper
reports no results yet.

What the leading products now do, beside the owner's words:

| Practice | Who | The owner |
|---|---|---|
| A lighter entry for a small change | Spec Kit's bug-fix entry; Kiro's quick and bug-fix specifications | "a triage for proportionality" (17 Jun) |
| A commit for each finished task | Anthropic's published harness; Superpowers | Not asked for as such. He asked for one snapshot commit before a clean-up (20 Mar) and for history to live in git (4 Apr) |
| A reviewing session told not to trust the author's report | Superpowers | "i dont trust it because its context is what caused the problem" (24 Jul) |
| Tests the working agent may not edit | Anthropic's harness; Consort | "why are you rewriting tests" (28 Apr) |
| A limit on spend | Claude Code; paperclip | Not his remedy. Waste is a defect to repair: "finding waste is a p1 or p2 bug so it must be resolved" (16 Sep) |

What none of the products examined does:

- tie an approval to the exact content approved, or notice that the content
  changed afterwards;
- check its own record against the files. LangGraph and Temporal replay their
  record. Claude Code documents how its checkpoints part from the files.

The published criticism matches the owner's. On volume: one small feature
produced "8 files and 1,300 lines of text" (Marmelab, November 2025). On many
agents: every multi-agent arrangement tested made strictly sequential tasks
worse by 39 to 70 per cent (Google Research, December 2025).

Limits of the survey: thirty web requests, some claims taken from search
summaries, and nothing confirmed for Codex on four of eight questions.

## 7. What it says about how STDO Builder itself is built

What it puts into the requirements, one requirement at a time, is in the guide
beside this file, `20261118T040741Z_GUIDE_specification_round_two.md`. The
points below are proposed in the goals and in the page on how work is done.

- The smallest end-to-end scenario is built first, and every later change keeps
  it working.
- One ticket is in work at a time.
- Progress is what a user can now do with the installed product. A count of
  tests, tickets or reviews is not progress.
- A new rule, role or record names what it protects and what it costs.
- Nothing from a scenario's sample product enters the specification.
