# Guide to the specification draft, round two

**Type:** GUIDE. Commentary for the product owner's review, not law.
**Author:** claude (Fable 5.2) · 18 November 2026
**Subject:** `builder/specification/`, requirements at commit `f4a47b98f`.
Replaces the guide of 17 November.

**This round proposes changes to the product definition.** They are in three
commits that touch nothing else, `05615ef4e`, `8b409e774` and `8a3bbf21f`, for
the owner to accept or undo. The intent is unchanged. Nothing is accepted on
the owner's behalf.

## What happened

1. I read a year of the owner's prompts and the earlier attempts back to c4h,
   and surveyed equivalent products. The result is the post-mortem beside this
   guide.
2. From it I drafted round two: 54 requirements and 10 scenarios.
3. An independent reviewer (Claude Opus 5.5, a fresh agent that wrote none of
   it) tested the draft against the intent and the owner's words. Verdict:
   **No, not ready.** 29 findings, and scenario S1 could not pass as written.
4. I reworked the draft. A second fresh reviewer checked the rework only.
   Verdict: **No** again. Of the first 25 findings, 13 were closed, 9 closed in
   part and 3 not closed, and it had 6 new ones.
5. I reworked it a second time: 49 requirements and 10 scenarios. **This
   second rework has not been reviewed.** I walked scenario S1 through it
   myself, and ran the method's own verification on a definition file written
   as set-up would write it.

Both reviews are in `builder/.ai-workspace/comments/opus/`.

## What there is to read

| Page | Words | State |
|---|---|---|
| `INTENT.md` | 395 | Approved by the owner; unchanged |
| `PRODUCT.md` | 967 | Proposed changes; see the next section |
| `GOALS.md` | 157 | Proposed: goal 3 reworded; goal 4, "Use it on itself", added |
| `REFERENCE_FRAME_BASIS.md` | 409 | Proposed: a new section, "Progress and weight" |
| `requirements/`, 12 families | 6,585 | Draft |
| `requirements/SCENARIOS.md` | 1,112 | Draft |

With the index page the requirements are 7,899 words. Round one was 5,169.
That growth is a cost. The next two sections show what the added words carry,
and "What could go" names what I would cut first.

## Changes proposed to the product page

| Change | Why |
|---|---|
| "Ticket" replaces "Request", and asking is a step of its own. A ticket lies in one of the method's three lanes | His words of 17 June on triage, in the table below |
| The first step for a ticket settles the node where it enters and whether it is small work; the user confirms | The same, and his words of 17 May on proportion |
| Work that cannot be closed comes back to the user as a ticket | His words of 14 June, below |
| An evaluation is a judgement of an asset by a session that did not produce it | His words of 6 June, below |
| New terms: session, step, content identity. A graph function is a declared way of carrying out a vector, not a program the framework runs | The requirements depend on them |
| Every session is a new one; one ticket at a time; the agent and the framework each write only their own files; the framework's own work is small | The commonest causes in the post-mortem |
| One person, on their own machine; the framework does not guard its records against the user | "this is not verification or assurance, this is if china hacks me?" (21 Sep) |
| Set-up may be over an existing system; "Show" also says what a ticket changed and what it cost | His words of 21 August, below; the rewrites in the post-mortem |

## The owner's words, and the requirement that carries each

| The owner's words | Date | Requirement |
|---|---|---|
| "when I say, start -- i expect to run at maxiumum autonomy to completion" | 24 Apr | BUILD-001 |
| "we just need to pass them references that they can access" | 29 Mar | AGENT-001 |
| "i dont trust it because its context is what caused the problem" | 24 Jul | AGENT-002, METHOD-004 |
| "choose custom llms on each vector" | 26 Feb | AGENT-003 |
| "system artifacats only go through ABG, the only other legitimate writer is the transformer over the worksurface" | 26 May | AGENT-005 |
| "sufficient autonomy to allow it to manage its workspace" | 24 May | AGENT-005 |
| "reentry with a ticket and a cold start are both a triage for proportionality and an entry at the appropriate level in a graph" | 17 Jun | CHANGE-001, CHANGE-003 |
| "i want the change to be detected at an engine level" | 16 Mar | CHANGE-002 |
| "maintain lineage IN the assets" | 26 May | CHANGE-002 |
| "a rebuild only of the dependencides on the requirement change" | 19 Apr | CHANGE-005 |
| "two F_P traversal paths 1. the transformation, 2. the evaluation" | 6 Jun | BUILD-006 |
| "its really dependent if its getting into churn or making incremental progress" | 7 Oct | BUILD-007 |
| "i have no context to make a judgement" | 25 Oct | BUILD-008 |
| "declare a work around or tell me, but don't silently shift to alternate functionality" | 5 May | BUILD-009 |
| "git is for history - no.1 rule" | 4 Apr | BUILD-010 |
| "the framework does not have an opinion on this" | 2 Nov | BUILD-010 |
| "long framework durations between llm calls that are just framework spinning" | 6 Nov | BUILD-011 |
| "even without an eventlog, mutable state is in workspace, you can restart" | 8 Oct | RESUME-003, LOG-001 |
| "fill in the template as an overlay, rather than forcing a restructure" | 21 Aug | SETUP-004, SETUP-008 |
| "context commands in agent.md and claude.md on how to start abg" | 1 May | SETUP-007 |
| "the amount of detail is not proportional" | 17 May | METHOD-003 |
| "independent assurance of the UAT.integration tests which are derived from spec and design, not code" | 21 Mar | METHOD-004 |
| "if the req is live then it needs to appear in code" | 26 Mar | METHOD-005 |
| "i want a failure, i want new tickets, i want it to retry lawfully" | 14 Jun | METHOD-006 |
| "the test harness is supposed to only start the traversal and not do anything else" | 20 May | VERIFY-002 |
| "if i was to ask to delete the code i should be able to recover it" | 4 Apr | Scenario S9 |

## Decisions that are the owner's

Of the eight decisions in the first guide, the owner's own words now answer
six: what ties a result to exact content, who judges, what the agent may write,
ticketing, the agent instruction files, and an existing system. The table above
shows the words. The rows below remain. Each default is mine. The first two
shape the most.

| Default | Where | His words for it | Against it, or silent |
|---|---|---|---|
| **The ticket is a thing the framework knows.** The framework takes tickets one at a time, in the order of their names, and moves each through the method's three lanes. The graph declares only the step that settles where a ticket enters | CHANGE-003, CHANGE-006 | "a triage for proportionality and an entry at the appropriate level in a graph" (17 Jun); "effectively single threaded" (14 Aug) | The intent: "The graph carries the method", and ticketing is part of the method. I first put the ticket's whole life in the graph. The second check showed the graph language cannot say it without growing a great deal |
| **Besides its log, the framework writes three things in the workspace:** what its checks found, the user's answers, and the content identity each rests on. They can re-open a vector and can never close one | CHANGE-002, BUILD-006, BUILD-008 | Guard rail 4; "maintain lineage IN the assets" and his per-edge manifest (26 May) | The intent: "The framework's own record is a log of its events" |
| Every check is run again before a run reports the work done | BUILD-009 | Guard rail 3; "they SAID they converged" | "inprinciple we should not be rechecking unchanged code" (28 Oct). It costs one pass of the checks for each finished run |
| The framework commits to git when a vector closes and when an answer is recorded. It never rewrites history and has no say over what the agent or the user does with it | BUILD-010 | "git is for history - no.1 rule" (4 Apr); "the framework does not have an opinion on this" (2 Nov) | He has not said who commits |
| No session chooses the next vector | BUILD-004 | "there should not be an outer loop" (11 Jun); "explicity deterministic over the llm agent" (17 Nov) | "optimal path choice" that "can be derived in the moment" (24 Apr); an executive that "chooses the appropriate graph functions" (11 Nov) |
| A run stops when a session has changed an asset that is not its own, or the framework's files. Elsewhere in the workspace the session is free, and it may add a ticket | AGENT-005 | The two rows for AGENT-005 above | His words name the two writers; the stop is mine |
| The lane a ticket lies in is its status. The method's status and updated-at fields are not written | METHOD-002 | The method itself: a ticket marked completed "cannot stand in" for a result | The method's ticket record requires both fields. Keeping them means the framework writes inside a file that is not its own |
| What "small work" buys: one acceptance of the whole specification, in place of three | METHOD-003 | "a triage for proportionality" (17 Jun) | The measure is mine |
| Set-up writes only the product's commands into the agent instruction files, and not the method's own block for agents | SETUP-007 | "context commands in agent.md and claude.md on how to start abg" (1 May); guard rail 7 | The method writes that block into every governed product. It tells an agent to "use Executive" and to "Fail closed" when a frame basis is missing, and every session would read it |
| The framework's own work between two sessions takes at most ten seconds | BUILD-011 | "long framework durations between llm calls that are just framework spinning" (6 Nov) | The number is mine |
| Left out: consensus among agents, a room of mixed agents, an executive agent, parallel streams of work | Nowhere | The approved intent has one agent and guard rail 1; "ABG, but without all the baggage" (18 Nov) | He asked for each: "one of my key features" (12 Jul); "i want to be able to open a room" (21 Apr); "independent work streams" (28 May); the executive (11 Nov) |
| The product is used on itself after the first build | Goal 4 | "mvp means i can eat my own dog food" (30 Aug) | "it was going down a rewrite rabbit hole" (12 Jul) |

## The requirements since round one

- **New:** SETUP-007 to 009, BUILD-011, AGENT-005, CHANGE-005 and 006,
  METHOD-005 and 006.
- **Removed or merged:** CHANGE-004 and AGENT-004 (into AGENT-005 and
  BUILD-007), BUILD-003 (into BUILD-001), SETUP-006 (into SETUP-005),
  REGISTRY-002, HOG-002, LOG-004, SHOW-002.
- **Changed in meaning:** BUILD-006 to 010, CHANGE-001 to 003, RESUME-003,
  LOG-001 and 002, GRAPH-001 and 002, METHOD-002 to 004, SETUP-002 and 004,
  SHOW-001, VERIFY-002.
- **New scenarios:** S8 an existing system, S9 build again from the
  specification, S10 two agents.

## What I did with the two reviews

| Review | Findings | Done |
|---|---|---|
| First, of round two | 29: 6 against a guard rail or the owner's words, 11 contradictions or undefined terms, 2 unchecked acceptances, 5 asked for and missing, 4 beyond his words, 1 on volume | All changed in the text, but for the ruling on what was left out. The largest: the event log now decides nothing |
| Second, of the rework | 3 of the first 25 still open, and 6 new | The 6 new changed in the text. The largest: checks decide whether a vector is closed, and what the framework writes can only re-open one. The first two rows of the table above come from this review |

The first review also found over-claims in the post-mortem, which I corrected:
three patterns stated as holding for every attempt, three quotations used for
more than they say, and one comparison of counts.

## What could go

If the set is too long, I would cut in this order, and each cut loses the thing
named: the ten-second bound and the limits on a run (BUILD-011); "nothing is
orphaned" (METHOD-005); the ticket for a failure (METHOD-006); the shorter path
for small work (one sentence each in CHANGE-003 and METHOD-003); scenario S10.

## Limits

- The author and both reviewers are Claude models. A reader of the same family
  shares blind spots.
- Two reviews each said No. I fixed what each found and stopped there: a third
  round would cost what the second did, and the questions that remain are the
  owner's.
- No loan is examined and there is no design. The graph language must say two
  new things, a condition on a vector and the vector that runs when one cannot
  close, and that is untested.
- My post-mortem of September was lost in the mothball of 18 November, by my
  error. The new one is built again from the sources.
