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

The candidate's general law of build-tenant binding belongs to SPEC_METHOD
(decision D4 in [DOCUMENT_STRUCTURE](DOCUMENT_STRUCTURE.md#ownership-decisions)).
This file owns only this tenant's own binding.

## 1. Three coordinates kept apart

| Coordinate | What it identifies here |
|---|---|
| Author identity | Who is responsible for candidate text. The tenant, `urn:stdo-3:build-tenant:claude`, authors its candidate. A part ported from the peer keeps its source author, the Codex tenant, recorded per part in [CROSS_SYNTHESIS](CROSS_SYNTHESIS.md). |
| Actor identity | Who performs one activation: a Claude session, a Claude subagent context, a headless `claude -p` process, a Codex session, or the product owner. |
| Operation kind | What is done: select, write, commit, review, run, check, generate, record or decide (section 3). |

None of the three determines the others. One actor may perform several
operation kinds, each under its own grant. A person performing an
operation does not by itself make that operation human adjudication: the
product owner relaying a Codex review is transport, while the product
owner accepting a checkpoint is adjudication. A fresh context of the
tenant's own model family is a different actor with the same author, so it
does not establish independent authorship
([conformance discriminator](../../../specification/conformance/README.md),
"An author opens a fresh context to review its own candidate").

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
  and [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis).

The installed release `stdo://releases/v2.5.1-rc.2/` governs this
construction until a release decision. The candidate's own members, its
EXECUTIVE_BASELINE included, do not govern the work that builds them.

## 3. Computational calculus

### Operations

| Operation | Input | Output | Effect | Result values |
|---|---|---|---|---|
| Select | the frontier view, closed results, the ledger | the next set of activations, each with its intake | none on files | an Executive decision |
| Write | an intake, a territory, named inputs at named commits | changed files in the territory; a return file; a frontier delta | file changes inside the territory only | `candidate_ready`, `refused`, `incomplete`, `re_entry_requested` |
| Commit | the territory's working-tree changes | one commit on the tenant branch | a new commit | committed, or refused with the git error |
| Review | a subject frozen at a named commit; expectations recorded from the sources before the subject is opened | one closed result per criterion or check, with findings | one review file in the Reviewer's territory | `satisfied`, `falsified`, `indeterminate`, `out_of_frame`, `invalid_basis` |
| Run | one frame, one subject, one task card, a context cap | the actor's output and a measurement record | one new run directory | output, or refusal before start when the context exceeds the cap |
| Generate frames | the frame manifest and the members at their digests | verbatim frame files and updated digests | frame files and manifest in the frame territory | generated, or refusal on an absent or ambiguous heading |
| Encode | members at their digests | an a_c program, map and bindings | files under `a_c/` | authored program |
| Check | an a_c program and bindings | a validation report and projections | report files | structural pass or diagnostics |
| Record | an Executive decision | one ledger entry | a ledger change | recorded |
| Decide | a request with its evidence | a ruling in the product owner's words | none until recorded | the product owner's decision |

Writers, Reviewers and the ledger Writer return the result values shown.
The installed release owns those values' meanings
([work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result),
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results)).

### Composition laws

1. Sequence. Write, then Commit, then Review, then the Executive's
   disposition, then Record, before any activation that depends on the
   result starts. A Review reads only a committed subject, so the subject is
   frozen before the Reviewer sees it.
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
   has a closed `satisfied` result from a Reviewer who is not its author. A
   falsified, indeterminate or missing criterion keeps the member
   unaccepted. A same-family working check never stands in for an
   acceptance review ([ledger default 2](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions)).
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
| Declared context | bytes | the intake text and every file the activation is told to read, at the named commits | `wc -c` before the activation reads | the activation's return file |
| Fresh-actor context | bytes and input tokens | the whole input of the headless process, framework overhead included | `qualification/instruments/bounded_step.py` measures bytes before start and logs host-reported tokens | the run directory |
| Wall time | seconds | from the activation's start to its closed result | `date -u` at start and at return | the return file |
| Spend | USD | one headless run | `total_cost_usd` as the host CLI reports it | the run directory |
| Human decisions | count and elapsed time | from the request to the product owner's ruling | ledger timestamps | the ledger |
| Cross-session relays | count | each transfer between Claude and Codex sessions through the product owner | ledger entries | the ledger |

Two limits on these measurements are known and stated rather than hidden:

- A Claude subagent receives context the host adds (system prompt, tool
  definitions and instruction files). That added context is not measurable
  from inside this tenant, so the declared-context measurement covers only
  the declared material. Only headless fresh-actor runs measure their whole
  context.
- Spend for the Executive session and for subagent activations is not
  reported to this tenant. It is recorded as unavailable, never estimated
  as measured.

For each activation the Executive declares a context limit in bytes, a
wall-time limit and, for headless runs, a spend limit, as the C3 Limits
paragraph requires. Context size and adequate attention are different
questions: bytes measure the size of what was given; a fresh-actor run
against expectations specified independently of the author is the evidence
of adequate use (acceptance criterion 4).

### Operational assumptions

- Concurrency degrades delivery. In the first pass, six to eight open
  activations returned minutes of reviewer work hours later, and one Writer
  wrote nothing in 3 h 20 min
  ([T-002-CLAUDE, 2026-10-12T06:49:31Z](../../../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md)).
  This is the reason for composition law 2's limit of three.
- A model actor's report of its own work is not evidence. The Executive
  checks files and commits, and Reviewers read the committed subject.
- Same-family actors may share blind spots, so their judgments are working
  checks only.
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
| Executive | one Claude Code session on the tenant worktree; it selects and disposes and changes no file while Executive. Git setup, commits and ledger entries are performed after a recorded role change to Writer ([ledger, Configuration](../qualification/C3-SYNTHESIS/LEDGER.md#configuration)). |
| Writers and Reviewers | fresh Claude subagent contexts started by the Executive, each with an exact territory inside `build_tenants/claude/` |
| Fresh actors | headless `claude -p` processes with no tools, no MCP servers and no session memory, started by `qualification/instruments/bounded_step.py` in an empty directory outside any repository |
| Repository | the git worktree `/Users/jim/src/apps/specification_methodology-claude` on branch `tenant/claude/c3-synthesis`, sparse to the common specification, `.ai-workspace/` and this tenant |
| Builder | the installed release at `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4…2782` |
| a_c checker | `axiom_indexer/build_tenants/core/code/ac.py` read with `git show` from tag `refs/tags/axiom_indexer/v2.5.1-rc.2` (commit `9a9c4797…`), SHA-256 `5a2e0cb5…6c8`, run from a scratch copy with `python3 -I`, as pinned by the [a_c dependency contract](../../../specification/requirements/A_C_DEPENDENCY.md#immutable-mechanical-subject) |
| Porting source | the Codex tenant candidate at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read with `git show` only |
| Common pen and cross-family review | Codex sessions, outside this tenant's actors; reached only through the product owner |
| Human process | the product owner: decides member and checkpoint acceptance, every `intentionally removed` disposition, merges and rulings; relays reviews between sessions |

## 5. Conformance evidence

The binding satisfies the requirements calculus through these relations,
each with its evidence:

| Obligation | How the binding meets it | Evidence |
|---|---|---|
| Authority | every effect lies in a declared territory; the Executive writes nothing while Executive; tickets and common files are written only by the common pen | commits per territory; the ledger's role-change entries |
| Independence | a Reviewer never assesses its own authorship; same-family results are marked as working checks; acceptance reviews are cross-family | review files with the actor and family recorded |
| Required human decisions | acceptance, `intentionally removed`, merges and release stay with the product owner; no automated result substitutes for them | the ledger's verbatim rulings |
| Failure and recovery | composition laws 3, 5 and 6 | return files with `incomplete` or `re_entry_requested`, and the Executive's recorded handling |
| Measurement | the resource table above | return files and run directories |

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

**Operations.** The rebuild changes or adds text in 23 members, ports five
named parts, regenerates frames, runs fresh actors and checks every member
against criteria 1 to 6 and the 31 discriminators.

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

**Required assurance.** Every member needs independent review against
criteria 1 to 6; acceptance reviews are cross-family; the product owner's
decisions cannot be delegated.

**Allocation.**

| Responsibility | Allocated to | Why |
|---|---|---|
| Keep the outcome, the basis and the frontier; select and dispose | one Executive context | decisions across successive tasks need one longer-term view; worker results arrive as closed results, not working context |
| Change one territory | one Writer per territory | disjoint territories let concurrent effects combine without conflict |
| Change shared files | one serial integration Writer | the frontier copy, GLOSSARY, the standards README and cross-member links are touched by every member's work |
| Check a frozen subject | one Reviewer per subject, same family during construction | catches defects before cross-family acceptance; never counted as acceptance |
| Test a frame in use | one headless fresh actor per frame task | criterion 4 forbids private memory and author knowledge |
| Record decisions | a ledger-only Writer activation | the Executive holds no write grant ([ledger default 4](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions)) |
| Accept, remove, merge, release | the product owner | reserved human decisions |

**Information exchanges.** Activations exchange closed results through
files: return files, review files, run directories and commits. When the
Executive needs more information for a decision, it requests a bounded
evaluation instead of reading working context.

**Distinct relations.** Functional decomposition (members, families,
territories), communication (files within this tenant; the product owner
between Claude and Codex), authority (the product owner; the Executive's
disposition grant; each Writer's territory) and evaluation dependency (a
Reviewer depends on a committed subject; acceptance depends on a
cross-family review) are kept as separate structures. The names Executive,
Writer and Reviewer are the installed baseline's frames as bound by the
[frame basis](../../../specification/REFERENCE_FRAME_BASIS.md); they confer
no authority.

**Alternatives considered.** One Writer for the whole line fails on
context and attention. A peer configuration with no Executive is lawful in
general, but the C3 contract configures the installed Executive
engagement for this construction. More than three concurrent activations
is excluded by the first-pass failure recorded above.

**Reconfiguration.** The Executive may split an activation that returns
`incomplete` or `re_entry_requested`, reduce concurrency, or change an
actor. Every reconfiguration keeps the outstanding obligations, any
uncommitted effects, the admitted authority and the required independence.
