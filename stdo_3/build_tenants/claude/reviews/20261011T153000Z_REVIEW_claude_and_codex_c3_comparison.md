# Claude and Codex STDO 3 builds: a comparison for Jim

State: closed author-side comparison, written in the Claude tenant under
Jim's authorisation ("when you finish you can post a review comparing codex
with claude work at the end"). The author of this comparison authored the
Claude build, so this is not an independent assessment of either tenant.
The Codex side was read source-first at one named commit; the Claude side
is the author's own work at the commits named in its
[review handoff](../qualification/REVIEW_HANDOFF.md). Nothing here accepts,
selects or merges anything.

## Frozen scope

| Subject | Commit | Read |
|---|---|---|
| Codex build | `67217a4` (2026-10-12 02:06 +1100), `tenant/codex/c1` | `git show` of named bodies; the Codex worktree was not opened |
| Claude build | `6bc1692` (T4 freeze) and the T4 runs commit named in `qualification/RETURNS.md` | own tenant |
| Common WHAT | `00be6b8` | both tenants bind it |

Codex's `qualification/BUILD_RETURN.md` at that commit is an active
completion plan started 2026-10-11T14:26Z under the same authorisation Jim
gave this tenant, with a three-hour envelope; its frontier table shows
Spec, profiles, qualification routes, fixtures, the Axiom Install, trials,
a_c mechanics and its own comparison as READY or WAITING. The Codex build
read here is therefore mid-flight, and its later commits are outside this
comparison. The Claude build read here is at its author's declared end.

## Expectations recorded before opening the Codex candidate

From the common sources at `80b46944f1c1` and `00be6b8`: the eight
capability questions (foundational derivation; one WHAT with distinct HOWs;
bounded work with a truthful stop; evidence and authority with failures
conserved; progress and recovery; method usability without private
knowledge; optional profiles; self-improvement at the right owner); the ten
conformance discriminators; the matrix's nine trials and its instruction to
declare caps and budgets, count context across every delegated actor and
keep acceptance criteria independent of the constructor. Comparison
predicate: for each, what each tenant has as law, as fixture, as run, and
as assessment; and at what observed cost.

## Shape of the two builds

| Concern | Claude (`6bc1692`) | Codex (`67217a4`) |
|---|---|---|
| Documents | seven files, 68,152 bytes: FOUNDATIONS, CALCULUS, EVALUATION (tier 1), SPEC_METHOD, CONFORMANCE (tier 2), PROFILES (tier 3), README route | twelve files, 69,151 bytes: FOUNDATIONS, SPEC_METHOD, WORK_METHOD, EVIDENCE_METHOD, QUALIFICATION_METHOD, SOURCE_INDEX, README, four profiles and their entry |
| Unit of law | sections carrying principle P0–P6 and an rc.2 route with one standing per clause (conserved, reframed, superseded, new); a source-dispositions table per document | numbered clauses F-01…, W-01…, E-01…, S-01…, K-01…, PR-01… with "Recovery Owners" sections pointing to the accepted C1 document's source recovery and to selected rc.2 anchors |
| rc.2 standing | checked by fresh step actors route by route before each freeze (T2: 29 routes, T3: 25 routes, repaired to all satisfied); the T1 review found four unfaithful points, repaired | recovered through C1's exact-source-recovery section (59 KB) and the SOURCE_INDEX; the independent corpus assessment checked 61 installed links resolve and judged no contradiction, without per-clause route judgments |
| Bounded step | CALCULUS §1–3: intake, closure, projection, fit measured in bytes before any read, five-member algebra, composite by declared conjunction | WORK W-01…W-07 and EVIDENCE E-02: bind, acquire with a five-step context operation, fit as a declared condition, the same five members, next action as a separate type |
| Composition and coverage | FOUNDATIONS §4: R minus C, union of failures, a known failure and an uncovered obligation survive every join; CALCULUS §4 faithful refinement | FOUNDATIONS F-03/F-04 and EVIDENCE E-04: the same R minus C rule, with an explicit distinction between an uncovered obligation and a missing planned slot |
| Work state and resumption | CALCULUS §5 and §7: work-state tuple, resumption, non-idempotence, restart argued, invalidators | WORK W-06/W-07 and WORK_RECORDS: the same content with an explicit "erasing retained work is a separate decision" |
| Profiles | PROFILES: boundary of the core, four profile bindings, all rc.2 profile members conserved by reference | profiles/: four profile documents with their own numbered clauses |
| a_c | four cumulative programs, the last over the whole set (130 symbols, 164 clauses, 6 residuals, five projected frames), validated with zero diagnostics against a byte-verified scratch copy of the pinned tag; no Install selected, left to Jim | an own-tenant Install of the pinned tag, extracted and verified member by member with a receipt; one small fixture interpretation (a wrong and a repaired program over six clauses of a cost-brief fixture) with maps and projections; the corpus itself not encoded at this commit |
| Fixtures and runs | T-01 (two fixtures, four runs), T-03-04 (two runs), T-05 (two runs), R-01 (five variants, two repeats): every reading step a fresh headless actor with its whole context measured and logged; constructors are fresh same-family contexts; the author did not repair or annotate any record | T1: construction of an operator handoff from a 1,420-byte source, two independent same-family assessments, an actual policy omission introduced, detected, repaired and reassessed under unchanged criteria, a planned interruption with fresh continuation, three acquisition-pressure profiles; T2–T6 fixtures frozen (cost brief D, receipt effect R, fresh reader G, finite tokens N, successor S) with two deployment-brief constructions and one fresh-reader run present at the commit |
| Assessment | none inside the tenant: EVALUATION §3 makes same-family activations not independent by default, so every run awaits Jim or the other tenant | inside the tenant: fresh non-author same-family assessors, declared as procedural independence; a corpus assessment returned GO for Jim's review; T1's FINAL_V2 closed the defect join |
| Cost reporting | step-actor tokens and list cost from the CLI per step; coordinator tokens as the harness reports them; wall by `date -u` | elapsed intervals, body bytes acquired with repeat counts, envelope overruns recorded; provider counters unavailable |
| Reviews of the peer | one, this document | one, `reviews/20261011T125957Z_REVIEW_CLAUDE_CODEX_BUILD.md` of Claude at `eca8cef`, which Jim relayed to this tenant and which it disposed in full |

## Where the two agree

The architecture is the same in substance, reached independently from the
same C1 basis: a finite actor's bounded step with declared intake and
grant; context acquired by exact identity with a fit test and a truthful
stop; one five-member result algebra conserving RF-012 and AC-007 without
claiming they are one domain; typed composition with R minus C and
surviving failures; resumption over current work state without blind
repetition of a possible effect; proportionality applied to the method's
own ceremony; profiles outside the core; fixtures never promoted to law;
the formal fragment carried from C1 with its non-faithfulness and nothing
stronger. Both tenants refuse to count a run as a pass and leave
acceptance, canonical selection, release and adoption to Jim. Neither
reads the other's working tree.

## Where they differ, and what each difference costs

1. **Law as routed clauses against law as recovered owners.** Claude's
   documents carry the rc.2 route and the standing of every clause inline
   and were checked by fresh actors before each freeze; the cost is seven
   dense files and a residual that the program cannot check conservation.
   Codex's documents are lighter and read as a method; the cost is that the
   rc.2 standing of a clause lives in C1's source-recovery section and the
   index, so a reader who needs the standing opens a 59 KB document. For a
   fresh actor doing work, Codex's entry is shorter; for an assessor judging
   conservation, Claude's is more direct.

2. **Independence policy.** Codex's assessments are inside its tenant by
   fresh same-family contexts, declared as procedural independence, and
   its own review of Claude calls family identity "an owner-policy premise
   to settle". Claude's corpus makes the default the opposite and therefore
   holds no assessment at all. The common question is open; until Jim
   fixes it, Codex has evidence that Claude cannot claim and Claude has a
   stricter claim that Codex has not tested. Whichever way the policy goes,
   both tenants' records are reusable: Codex's assessments as evidence or
   as judgment, Claude's runs as subjects.

3. **What a run is.** Claude's runs are instrumented: every actor's whole
   context is measured in bytes and logged before the actor exists, every
   output is digest-bound, and the structural check over the log is
   mechanical. That produced the one material finding against Claude's own
   fixtures (below). Codex's runs are narrative returns with body-byte
   accounting and Git-bound outputs; their contexts were not measured as
   actor contexts, which Codex says itself ("contractual acquisition
   behavior; native context-window stress is unproved"). Claude's
   instrument measures the thing the matrix asks for; Codex's fixtures
   exercise more of the method per run (a real defect, a repair, a lost
   receipt, a successor).

4. **The defect join.** Codex has done the construction, independent
   assessment, actual defect, repair and reassessment join on one small
   task, and retained the first reviewer's miss and the first fixture's
   failed isolation. Claude has not done that join as a fixture; its
   nearest evidence is the T1 review cycle on its own documents (four
   accepted findings, repaired, re-run) and the seeded failure in T-03-04,
   which is a judgment produced by a real actor on a seed, not a defect in
   a construction. Claude's conformance table names the case (C-10, T-07);
   it is not run.

5. **The a_c dependency.** Codex selected an own-tenant Install under the
   completion grant and verified it member by member before use; Claude
   verified the same seven members from the tag and used a scratch copy,
   recording that selection is Jim's. Codex's reading of A_C_DEPENDENCY
   ("verify the required target through the selected Install before
   mechanical use") is the more literal; Claude's results are candidate
   evidence until that selection. On the other side, Claude encoded the
   whole corpus (164 clauses, five frames) and Codex at this commit encoded
   six fixture clauses; Codex's corpus program is scheduled, not present.

6. **Cost accounting.** Claude reports tokens and list cost per step actor
   from the CLI and the harness's coordinator totals, with their
   definitions marked unverified where they are. Codex reports elapsed
   time and acquired bytes with repeat counts and says token counters are
   unavailable. Claude's figures are closer to what the matrix's F30 asks;
   Codex's byte accounting is more careful about repeated reads. Neither
   has a like-for-like task yet, so neither can claim contraction.

## Findings against the Claude build (author's own, ranked)

1. Every step actor of T-01 CASE-2, T-03-04 and T-05 received the
   workspace's three CLAUDE.md files in its context beside the measured
   bytes, because the headless CLI loads them from the actor process's
   working directory, which was inside the repository. Found at T4 by the
   calibration step (6,907 tokens inside against 2,247 outside). The
   judgments stand; the "whole context measured" claim of those fixtures
   is false by about 12 KB per step; each case records it and the
   instrument is repaired for R-01. Owner: the fixtures; the assessor
   should weigh it against E1 and E4 of those cases.
2. No assessment exists inside the tenant, by its own policy. Nothing is
   passed. Owner: Jim's independence policy and the assessor he names.
3. The a_c Install is not selected; all mechanical results are candidate
   evidence. Owner: Jim.
4. A fresh step actor on the whole FOUNDATIONS §3 judged AC-016
   out_of_frame and RF-010 indeterminate for P4a, where the paragraph-alone
   run judged both satisfied: a candidate finding against P4a's attribution
   of RF-010 and an observation that the route judgment is context
   sensitive. Owner: FOUNDATIONS P4a.
5. Two author errors in fixture descriptions (R_C "all ten satisfied";
   the P4a row of the T-05 draft) were caught by the constructors and
   corrected after the runs; the fixtures' declared seeds were incomplete.
   Owner: the case designs.
6. The two T-03-04 constructors triaged the same seeded defect into
   different change classes with reasons. Owner: SPEC_METHOD §4, which may
   need to say how a defect in a fixture copy of a standard is classed.

## Findings against the Codex build (read at `67217a4`, ranked)

1. The build is incomplete at the read commit: SPEC_METHOD, QUALIFICATION
   and the profiles are "candidate for review"; the T2–T6 fixtures are
   frozen but the deployment assessments, receipt and token branches,
   successor P1 assessment, the corpus a_c interpretation and Codex's own
   comparison are not present. The frontier table says so. Nothing here
   is a defect; it bounds what can be compared.
2. Same-family assessments are the only assessments; the corpus GO and
   the T1 FINAL_V2 rest on the procedural-independence declaration. Codex
   states the limit each time. Under Claude's default they are construction
   output; under Codex's they are judgments. Owner: Jim.
3. The rc.2 standing of a clause is not carried in the standards; the
   "Recovery Owners" paragraphs route to C1 and the index. A clause-level
   conservation check of the kind Claude's T1 review performed on Claude
   has not been performed on Codex's standards at this commit (the corpus
   assessment checked link resolution and contradiction, not per-route
   characterisation). Owner: Codex's qualification plan (T6 successor
   dispositions).
4. The a_c evidence at this commit is a six-clause fixture interpretation
   with a deliberately wrong variant; it demonstrates the mechanics and the
   fidelity separation on a toy, not the corpus. Owner: Codex's T5.
5. The T1 fixture's source is 1,420 bytes and its views are contractual
   byte envelopes; Codex says this is not native context stress. The
   matrix's cap-and-decomposition trial is therefore not yet run by Codex
   in the sense Claude's T-01 CASE-2 runs it. Owner: Codex's remaining
   cases (Q05–Q08 beyond T1's envelope).

## Coverage of the common discriminators

| Discriminator | Claude | Codex at `67217a4` |
|---|---|---|
| Derivation or independence argument | FOUNDATIONS §3 standings; residual that arguments are one sentence | C1 document; F-07 imports it |
| Information and representation differ | FOUNDATIONS §2, P1; R-01 variants (run) | F-01, S-02; D typed-join fixture (constructed, not assessed) |
| Identity unchanged while content changes | P3; T-05 invalidator checks (run) | F-04, W-06; R fixture (frozen) |
| Typed producers and consumers disagree | T-03-04 R_C refused on basis digest (run twice) | D typed join `rate = 6` (two briefs constructed; assessment pending) |
| Failed A and uncovered B; every slot authenticated | T-03-04 (run twice, including an altered slot) | E-04 law; D negative-conservation and omitted-slot variants (frozen) |
| Required coupled context cannot fit | T-01 CASE-2 (run twice, measured contexts) | T1 views A/B, refusal, unavailable, invalid (run; contractual) |
| Basis or evidence changes | T-05 applicability checks (run twice); T-03-04 R_C | R source-v2 (frozen); T1 EXPECTATIONS_V2 successor (run) |
| Interruption leaves authored progress | T-05 (run twice, real kill) | T1 continuation (run, planned stop) |
| A parse or map succeeds | a_c READMEs; R-01 E5 (run) | N wrong-but-valid program (constructed) |
| Carrier or process churn as new law | SPEC_METHOD §4 carrier by lifetime; R-01 E4 | S-09, K-04; G whole-path comparison (frozen) |

## Recommendation

Do not select a canonical tenant from either build's own evidence; both
tenants say the same. Three bounded steps would make the next decision
cheap:

1. Fix the independence policy for the C2 contract. If same-family
   non-author assessment is admitted with its limits declared, Codex's
   assessments become judgments and Claude's runs can be assessed by fresh
   Claude contexts tomorrow; if not, each tenant assesses the other's
   frozen runs at named commits.
2. Cross-assess at named commits under that policy: Codex over Claude's
   T-01 CASE-2, T-03-04, T-05 and R-01 against each case's expected
   distinctions; Claude over Codex's T1 chain and whatever of T2–T6 is
   frozen by then, against its EXPECTATIONS files.
3. Run one source-owned task through both tenants' lawful HOWs with the
   same cap, budget and assessor, as Codex's review also proposed. Claude's
   instrument can measure both tenants' actors; Codex's D fixture or
   Claude's R-01 task would serve.

The a_c dependency selection is on the path of both tenants' mechanical
claims and is Jim's alone.

## Effects and limits

This file is the only effect; it was written after the Claude build's
T4 freeze and after the Codex read, and is committed on `tenant/claude/c3`.
Codex bodies were read with `git show 67217a4:…`; no Codex working file,
assessment report, run body outside those listed in the shape table, or
later commit was consumed. The author's structural checks of Claude's logs
are mechanical; every judgment about Claude's own work above is an author's
and must not be reused as assessment. Claude's R-01 figures are in
`qualification/RETURNS.md` under the T4 return.
