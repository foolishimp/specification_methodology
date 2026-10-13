# Claude Tenant Design: Construction Binding

This file states how the Claude build tenant builds its own candidate. It
applies the common
[Build-Tenant Binding requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement)
(items 1 to 6) and item 4 of the
[Bounded Transitions And Reference Frames requirement](../../../specification/requirements/README.md#bounded-transitions-and-reference-frames)
to this tenant's construction. It is tenant HOW, not common WHAT, and not
accepted. The decisions and defaults in force for the current rebuild are
recorded in the [C3-SYNTHESIS ledger](../qualification/C3-SYNTHESIS/LEDGER.md);
this file is the design they apply.

Terms used here:

- The **requirements calculus** is the set of common obligations, permitted
  outcomes and rules for refining and composing the construction
  ([PRODUCT, Build-Tenant Binding](../../../specification/PRODUCT.md#build-tenant-binding)).
- The **computational calculus** is the set of executable operations, the
  laws by which they compose, their effects and the resources they consume.
- The **execution environment** is the concrete means that performs those
  operations: tools, processes and people.
- An **activation** binds one actor to one reference frame, an exact subject
  and admitted authority
  ([PRODUCT, Construction Authority](../../../specification/PRODUCT.md#construction-authority)).
- A **territory** is the exact set of files an activation may change.
- The **common pen** is the session that holds the right to edit the common
  files, tickets included. **T-002-CLAUDE** is this tenant's copy of the C3
  work ticket, which only the pen writes. The **tenant ledger** is
  [LEDGER](../qualification/C3-SYNTHESIS/LEDGER.md), this tenant's own
  record of the rebuild's decisions, role changes and returns.
- A **working check** is an assessment of a frozen subject by a fresh
  Claude context that did not write it, against expectations recorded from
  the sources before the subject is opened, with no repair grant. Section 1
  states why it never counts towards acceptance.
- **a_c** is the axiomatic-calculus representation of the members: a
  program of typed records with a map of their constraints, which the a_c
  checker validates for structure only.

The candidate's general law of build-tenant binding belongs to SPEC_METHOD
(decision D4 in [DOCUMENT_STRUCTURE](DOCUMENT_STRUCTURE.md#ownership-decisions)).
This file owns only this tenant's own binding.

## 1. Three coordinates kept apart

| Coordinate | What it identifies here |
|---|---|
| Author identity | Who is responsible for candidate text. The tenant, `urn:stdo-3:build-tenant:claude`, authors its candidate. A part ported from the peer keeps its source author, the Codex tenant, recorded per part in [CROSS_SYNTHESIS](CROSS_SYNTHESIS.md). |
| Actor identity | Who performs one activation: a Claude session, a Claude subagent context, a headless `claude -p` process, a Codex session, or the product owner. |
| Operation kind | What is done: select, set up, merge inward, write, commit, review, run, generate, encode, check, record or decide (section 3). |

None of the three determines the others. One actor may perform several
operation kinds, each under its own grant. A person performing an
operation does not by itself make that operation human adjudication: the
product owner relaying a Codex review is transport, while the product
owner accepting a checkpoint is adjudication. A fresh context of the
tenant's own model family is a different actor with the same author, so it
does not establish independent authorship
([conformance discriminator](../../../specification/conformance/README.md),
"An author opens a fresh context to review its own candidate").

**Independence in this rebuild.** The tenant is the author of its
candidate in the sense of that conformance row, whichever Writer
activation produced a given sentence. Every Claude context therefore
shares the author of every Claude-written subject, including a context
that did not write it. Every review of Claude-written text in this rebuild
is a working check:

- it is marked in its review file as a same-family working check, with its
  reason ([ledger default 2](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions));
- it does not meet the Independence paragraph of the
  [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract),
  whose first condition is that the Reviewer is never the author of the
  subject, and it is not the independent comparison that acceptance
  criterion 2 requires;
- its result is evidence for the Executive's `local_repair`, `re_enter` or
  `reject`, and never supports `accept`.

The activations the ledger calls same-family Reviewers are working checks
in this sense. That a context did not write the subject is an actor fact,
recorded with the check; it is not independence of authorship. Acceptance
reviews of this candidate are cross-family, by a Codex Reviewer, and the
Independence obligation stays open for every member until one returns. A
part ported from the Codex candidate has the Codex tenant as its source
author, so no planned Reviewer is independent of every sentence in a cone
that contains a port; [CROSS_SYNTHESIS](CROSS_SYNTHESIS.md#review-of-ported-text)
leaves that review to the product owner's decision.

## 2. Requirements calculus bound

This construction is bound to:

- the common specification at the input snapshot recorded in the
  [ledger](../qualification/C3-SYNTHESIS/LEDGER.md#basis);
- the [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract),
  including acceptance criteria 1 to 6, its Independence and Limits
  paragraphs, and the installed 2.5.1-rc.2 Executive engagement it
  configures;
- the 31 [conformance discriminators](../../../specification/conformance/README.md);
- [Development Isolation](../../../specification/PRODUCT.md#development-isolation)
  and [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis);
- the product owner's instruction, recorded verbatim in the
  [ledger](../qualification/C3-SYNTHESIS/LEDGER.md#owner-instruction),
  which admits this rebuild and is the basis of the declared variances in
  section 5.

The installed release `stdo://releases/v2.5.1-rc.2/` governs this
construction until a release decision. The candidate's own members, its
EXECUTIVE_BASELINE included, do not govern the work that builds them.

## 3. Computational calculus

### Operations

| Operation | Input | Output | Effect | Result values |
|---|---|---|---|---|
| Select | the frontier view, closed results, the ledger | the next set of activations, each with its intake | none on files | an Executive decision |
| Set up | the input commit on `main`; the branch and worktree names | the tenant branch, its git worktree and its sparse checkout | a new branch, a worktree directory and its sparse-checkout configuration, all outside `build_tenants/claude/`. Precondition: Development Isolation, Tenant branches | created, or refused with the git error |
| Merge inward | a commit on `main` that carries a common change | one merge commit on the tenant branch | common files under `specification/` and `.ai-workspace/` change on the tenant branch exactly as on `main`; no common file is authored. Precondition: Development Isolation, Territory ("reaches the tenant by merging `main` inward") | merged, or refused with the git error |
| Write | an intake, a territory, named inputs at named commits | changed files in the territory; a return file; a frontier delta | file changes inside the territory only | `candidate_ready`, `refused`, `incomplete`, `re_entry_requested` |
| Commit | the territory's working-tree changes | one commit on the tenant branch | a new commit | committed, or refused with the git error |
| Review | a subject frozen at a named commit; expectations recorded from the sources before the subject is opened | one closed result per criterion or check, with findings | one review file in the Reviewer's territory | `satisfied`, `falsified`, `indeterminate`, `out_of_frame`, `invalid_basis` |
| Run | one frame, one subject, one task card, a context cap | the actor's output and a measurement record | one new run directory | output, or refusal before start when the context exceeds the cap |
| Generate frames | the frame manifest and the members at their digests | verbatim frame files and updated digests | frame files and manifest in the frame territory | generated, or refusal on an absent, duplicated or ambiguous heading or section end |
| Encode | members at their digests | an a_c program, map and bindings | files under `a_c/` | authored program |
| Check | an a_c program and bindings | a validation report and projections | report files | structural pass or diagnostics |
| Record | an Executive decision or role change | one ledger entry | a ledger change inside the territory | `candidate_ready`, `refused`, `incomplete`, `re_entry_requested`, as for Write |
| Decide | a request with its evidence | a ruling in the product owner's words | none until recorded | the product owner's decision |

Write, Record and Review return the installed values shown, and the
installed release owns their meanings
([work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result),
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
the reference-frame law on closed results). Set up, Merge inward, Commit,
Run, Generate frames, Encode and Check return the outcome their tool
reports; the activation that performs them states that outcome inside its
own closed result.

### Composition laws

1. Sequence. Write, then Commit, then Review, then the Executive's
   disposition, then Record, before any activation that depends on the
   result starts. A Review reads only a committed subject, so the subject is
   frozen before the Reviewer sees it. Record writes the tenant ledger; the
   pen's entry in T-002-CLAUDE follows later (variance V1, section 5).
2. Concurrency. At most three activations run at once. Activations that
   run at the same time have disjoint territories: no file appears in two of
   them. Files that every member's work touches (the frontier copy, GLOSSARY,
   the standards README, cross-member links) are changed only by a serial
   integration activation that applies the deltas the others return.
3. Dependency. An activation starts only when each input it names is at a
   committed state named in its intake. If an input changes after the
   activation starts, its result is checked for applicability before the
   Executive relies on it.
4. Conjunction. A member is accepted only when every acceptance criterion
   has a closed `satisfied` result from a Reviewer who is not its author,
   which under section 1 is a cross-family Reviewer; for a cone that
   contains a ported part, only after the product owner's ruling on how
   ported parts are reviewed ([CROSS_SYNTHESIS](CROSS_SYNTHESIS.md#review-of-ported-text));
   and only by the Executive the product owner names (variance V3). A
   falsified, indeterminate or missing criterion keeps the member
   unaccepted. A working check never stands in for an acceptance review
   ([ledger default 2](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions)).
5. Recovery. Write and Commit are not assumed idempotent. After an
   interruption the Executive observes the worktree (`git status`,
   `git log`) and the return files before it reissues work. Uncommitted
   partial changes are either completed by the next activation on the same
   territory or discarded by an explicit instruction. A Run writes only its
   own new run directory, so it can be repeated.
6. Deterministic operations (Generate frames, Check, digest computation)
   are run again whenever an input changes. An earlier output is not reused
   across a changed input.

### Resources measured

| Resource | Unit | Boundary | Measurement | Record |
|---|---|---|---|---|
| Declared context | bytes | the intake text and every file the activation is told to read, at the named commits | `wc -c` before the activation reads | the activation's return or review file |
| Fresh-actor context | bytes and input tokens | the whole input of the headless process, framework overhead included | `qualification/instruments/bounded_step.py` measures bytes before start and logs host-reported tokens | the run directory |
| Wall time | minutes | from the activation's start, which the Executive logs in the ledger, to its closed result | UTC timestamps: `date -u` at start and at return, and the ledger's entries | the ledger and the return or review file |
| Spend | USD | one headless run | `total_cost_usd` as the host CLI reports it | the run directory |
| Human decisions | count; elapsed time in minutes | from the request to the product owner's ruling | the ledger's UTC timestamps | the ledger |
| Cross-session relays | count | each transfer between Claude and Codex sessions through the product owner | ledger entries | the ledger |

Two measurements are not available to this tenant:

- A Claude subagent receives context the host adds (system prompt, tool
  definitions and instruction files). That added context is not measurable
  from inside this tenant, so the declared-context measurement covers only
  the declared material. Only headless fresh-actor runs measure their whole
  context.
- Spend for the Executive session and for subagent activations is not
  reported to this tenant. It is recorded as `unavailable`, never estimated
  as measured. Wall time is recorded beside it and is not a spend figure.

Context size and adequate attention are different questions: bytes
measure the size of what was given; a fresh-actor run against expectations
specified independently of the author is the evidence of adequate use
(acceptance criterion 4).

### Limits for each activation kind

Every activation declares a context limit in bytes, a wall-time limit and
a spend limit, as the C3 Limits paragraph requires. The figures below are
defaults this design chooses; none is derived from a measurement. An
intake may set other figures, and each intake records the limits it sets.
An activation that reaches its wall-time limit returns `incomplete` with
its committed progress. A declared context over its limit is refused
before reading. Where a limit cannot stop the activation while it runs,
the measurement is compared with the limit afterwards and any excess is
recorded with the result.

| Activation kind | Context | Wall time | Spend | What is measured and recorded |
|---|---|---|---|---|
| Executive (this session) | 300,000 bytes of declared material per selection: the files read for that selection, drawn from return files, review files, the ledger, PLAN and this design; no member text | until the product owner's review, at most 12 hours from setup | USD 150 for the rebuild | bytes of the files read for each selection, by `wc -c`, named in its ledger entry. The session's whole context (host-added context, earlier turns, compaction) is not measurable and is recorded as not measured. Spend: `unavailable` |
| Executive acting as Writer (set up, merge inward, commit, record) | the files the effect changes and the ledger | 15 minutes per effect | counted in the Executive's limit | the role-change entry in the ledger, with UTC times |
| Writer (subagent) | 300,000 bytes of declared material | 45 minutes, the size in PLAN's activation conventions | USD 20 | declared bytes by `wc -c` before reading, in the return file; host-added context: not measured; start in the ledger and end by `date -u`; spend: `unavailable` |
| Working check (subagent) | 300,000 bytes of declared material | 45 minutes | USD 20 | as for a Writer, in the review file |
| Fresh actor (headless run) | the cap in its task card, at most 120,000 bytes of whole input | 10 minutes | USD 2 per run, and USD 15 for all runs of the rebuild, the upper end of PLAN's estimate for activation C6 | whole input in bytes before start and host-reported tokens, by `bounded_step.py`; duration from the run log; `total_cost_usd` after the run; all in the run directory |

Generate frames, Encode and Check run inside the Writer activation that
performs them and count against its limits. The product owner's
decisions are not activations of this tenant; this tenant sets them no
limit and records their elapsed time.

### Operational assumptions

- Open activations beyond the Executive's capacity to dispose of them
  delay delivery. The
  [T-002-CLAUDE](../../../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md)
  entry at 2026-10-12T06:49:31Z records that with six to eight
  activations open, minutes of reviewer work returned hours later, and one
  Writer wrote nothing in 3 h 20 min. The limit of three in composition
  law 2 is a choice: that record shows six to eight was too many, and it
  does not show that four or five would fail. Three keeps each return
  disposed before the next activation on a dependent input starts.
- A model actor's report of its own work is not evidence. The Executive
  checks files and commits, and Reviewers read the committed subject.
- Same-family actors share the tenant's authorship (section 1) and may
  share blind spots, so their judgments are working checks only.
- Instruction files load into a headless actor started inside a repository
  (`bounded_step.py` lines 21 to 24 record about 6,900 context tokens inside
  this repository against about 2,260 outside it). Fresh actors therefore
  run in an empty directory outside any repository.
- The a_c checker validates structure only. A passing check is not
  evidence of fidelity.
- The common specification may change on `main` during the rebuild. The
  ledger records the change and work continues on the snapshot until the
  product owner decides otherwise.

## 4. Execution environment

| Element | Binding |
|---|---|
| Executive | one Claude Code session on the tenant worktree, acting as Executive under the product owner's instruction until the product owner names the tenant's Executive (variance V3). It selects and disposes and changes no file while Executive. Set up, merge inward, commit and record are performed after a role change to Writer, recorded in the ledger ([ledger, Configuration](../qualification/C3-SYNTHESIS/LEDGER.md#configuration); variance V1). |
| Writers and working checks | fresh Claude subagent contexts started by the Executive, each with an exact territory inside `build_tenants/claude/` |
| Fresh actors | headless `claude -p` processes with no tools, no MCP servers (Model Context Protocol servers, which give a model external tools and data) and no session memory, started by `qualification/instruments/bounded_step.py` in an empty directory outside any repository |
| Repository | the git worktree `/Users/jim/src/apps/specification_methodology-claude` on branch `tenant/claude/c3-synthesis`, sparse to the common specification, `.ai-workspace/` and this tenant |
| Builder | the installed release at `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4…2782` |
| a_c checker | `axiom_indexer/build_tenants/core/code/ac.py` read with `git show` from tag `refs/tags/axiom_indexer/v2.5.1-rc.2` (commit `9a9c4797…`), SHA-256 `5a2e0cb5…6c8`, run from a scratch copy with `python3 -I`, as pinned by the [a_c dependency contract](../../../specification/requirements/A_C_DEPENDENCY.md#immutable-mechanical-subject) |
| Porting source | the Codex tenant candidate at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read with `git show` only |
| Common pen and cross-family review | Codex sessions, outside this tenant's actors; reached only through the product owner |
| Human process | the product owner: names the Executive and Reviewer actors; accepts the checkpoint; decides every `intentionally removed` disposition, every merge to `main`, how ported parts are reviewed, and other rulings; relays reviews between sessions. Member `accept` is the named Executive's disposition, not the product owner's. |

## 5. Conformance evidence

The binding addresses each obligation of the requirements calculus as
follows, with its evidence. The Independence obligation is open.

| Obligation | How the binding meets it | Evidence |
|---|---|---|
| Meaning and constraints | each member's restated text is assessed against acceptance criteria 1 to 6 and the 31 discriminators; each frame is tested in actual use | working-check review files, which are not acceptance evidence; cross-family acceptance review files when performed; run directories for criterion 4 |
| Authority | every authored file change lies in a declared territory; Set up and Merge inward have only the effects Development Isolation directs and author no common file; the Executive writes nothing while Executive; tickets and common files are written only by the common pen; ledger entries precede the pen's ticket entries under variance V1 | commits per territory; the ledger's role-change entries; the pen's transcription into T-002-CLAUDE |
| Independence | open. Working checks assess the tenant's own authorship (section 1), are marked as such with their reason, and never support `accept`. Acceptance needs a cross-family Reviewer's `satisfied` and, for a cone that contains a ported part, the product owner's ruling on how ported parts are reviewed | review files recording actor, family and the working-check marking; cross-family acceptance review files when performed |
| Required human decisions | naming the Executive and Reviewer actors, checkpoint acceptance, `intentionally removed`, merges, the review of ported parts and release stay with the product owner; member `accept` stays with the Executive the product owner names; no automated result substitutes for them | the ledger's verbatim rulings, transcribed by the pen |
| Failure and recovery | composition laws 3, 5 and 6 | return files with `incomplete` or `re_entry_requested`, and the Executive's recorded handling |
| Measurement | the resource table and the limits above | return files, review files, run directories and the ledger |

### Declared variances

Each variance departs from the common specification for this rebuild
only. Its basis is the product owner's instruction recorded verbatim in
the [ledger](../qualification/C3-SYNTHESIS/LEDGER.md#owner-instruction).
Each goes to the product owner with the handoff, and none changes a common
rule.

- **V1, ledger before ticket.** While the common pen is held by another
  session, this line's decisions and role changes are recorded first in
  the tenant ledger, and the pen transcribes them later into
  [T-002-CLAUDE](../../../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md).
  The next activation may start on the ledger entry, and activations run
  on the Executive's intake without a run-scoped execution contract drafted
  by the pen. This departs from Development Isolation, Work carrier (the
  pen records each disposition before the next activation starts, and no
  disposition exists until it has), and from step 7 of the Executive loop
  and the role-change rule of the C3 Construction Contract. Under the
  common specification the pen's ticket entry, not the ledger, is the
  record that can authorise an action. Nothing in the ledger is
  acceptance: no member `accept`, merge to `main` or common-file change
  rests on a ledger entry.
- **V2, unmeasured context and spend.** The C3 Limits paragraph requires
  each activation to report its context measured before reading and its
  spend afterwards. A subagent's whole context and the spend of subagent
  and Executive activations are not reported to this tenant (Resources
  measured), so those activations report declared bytes and `unavailable`
  instead.
- **V3, Executive and Reviewer actors not named.** Naming the Executive and
  Reviewer actors for each tenant is an open owner decision
  ([PRODUCT, Open Owner Decisions](../../../specification/PRODUCT.md#open-owner-decisions)),
  and under the common specification no execution contract leaves
  `drafted` until it is made. This session acts as Executive under the
  product owner's instruction; its dispositions are working dispositions,
  and it makes no member `accept`.

## 6. Reuse and representation

The computational calculus above does not depend on its executor. If a
person or another model family performs an operation, the execution
binding changes and the calculus does not, provided the binding keeps its
laws (Build-Tenant Binding requirement, item 5). An a_c encoding of the
members, or of this binding, does not select an executor and does not
establish that the construction conforms; structural validation checks
structure only (item 6).

## 7. Configuration and why it fits the task

The configuration is derived from the task, as the Bounded Transitions
requirement, item 4, asks, not from a fixed list of roles.

**Operations.** The rebuild changes or adds text in 23 members, takes six
parts from five items nominated in the Claude cross-assessment
([CROSS_SYNTHESIS](CROSS_SYNTHESIS.md)), regenerates frames, runs fresh
actors and checks every member against criteria 1 to 6 and the 31
discriminators.

**Dependencies.** The owners of results, conjunction and measurement must
change before the members that use them (step 2 before step 4). Families'
foundation-to-law tables need the revised premises (step 2 before step 3).
Frames are generated from settled text (steps 2 to 4 before step 5).
Shared files depend on every member's changes.

**Actor capabilities.** The standards total about 1.2 MB, with single
members up to about 140 KB (DESIGN_MODULE). One context cannot attend to
the whole corpus, so work is split by member section and by file. A
headless fresh actor has no tools, so it can test a frame only when the
frame and the subject are given to it whole.

**Required assurance.** Every member needs review independent of its
author against criteria 1 to 6, which under section 1 is cross-family
review; the product owner's decisions cannot be delegated.

**Allocation.**

| Responsibility | Allocated to | Why |
|---|---|---|
| Keep the outcome, the basis and the frontier; select and dispose | one Executive context | decisions across successive tasks need one longer-term view; worker results arrive as closed results, not working context |
| Change one territory | one Writer per territory | disjoint territories let concurrent effects combine without conflict |
| Change shared files | one serial integration Writer | the frontier copy, GLOSSARY, the standards README and cross-member links are touched by every member's work |
| Check a frozen subject | one working check per subject, by a fresh Claude context that did not write it | catches defects before cross-family acceptance; never counted as acceptance, because it assesses the tenant's own authorship (section 1) |
| Test a frame in use | one headless fresh actor per frame task | criterion 4 forbids private memory and author knowledge |
| Record decisions | a ledger-only Writer activation | the Executive holds no write grant ([ledger default 4](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions)); the pen transcribes the entries (variance V1) |
| Accept a member | the Executive the product owner names, on a cross-family Reviewer's `satisfied`, a disposed frontier cone and, for a cone that contains a ported part, the product owner's ruling on how ported parts are reviewed | the C3 disposition grant; no `accept` before that naming (variance V3) |
| Accept the checkpoint, remove, merge, release, rule on port review | the product owner | reserved human decisions |

**Information exchanges.** Activations exchange closed results through
files: return files, review files, run directories and commits. When the
Executive needs more information for a decision, it requests a bounded
evaluation instead of reading working context.

**Distinct relations.** Functional decomposition (members, families,
territories), communication (files within this tenant; the product owner
between Claude and Codex), authority (the product owner; the Executive's
disposition grant; each Writer's territory) and evaluation dependency (a
working check depends on a committed subject; acceptance depends on a
cross-family review) are kept as separate structures. The names Executive,
Writer and Reviewer are the installed baseline's frames as bound by the
[frame basis](../../../specification/REFERENCE_FRAME_BASIS.md); they confer
no authority.

**Alternatives considered.** One Writer for the whole line fails on
context and attention. A peer configuration with no Executive is lawful in
general, but the C3 contract configures the installed Executive
engagement for this construction. More than three concurrent activations
is not chosen; the limit of three is the choice stated under Operational
assumptions.

**Reconfiguration.** The Executive may split an activation that returns
`incomplete` or `re_entry_requested`, reduce concurrency, or change an
actor. Every reconfiguration keeps the material dependencies, the
outstanding obligations, any uncommitted effects and any effect whose
completion is unknown, the admitted authority and the required
independence.
