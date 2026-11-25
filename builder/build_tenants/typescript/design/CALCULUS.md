# Design: the computational calculus

**Status**: The rule is the product owner's, 20 November 2026: "all lawful
flows must go through the calculus", and "we will discover and update". Every
flow is built from the combinators of section 2, which one module of the kit
carries (C17 of the computational algorithms page). The build's checks refuse
a flow built any other way (section 6). A check reads the event log each
scenario leaves and refuses one the flow terms do not allow (section 8).
Section 9 lists where the code and the terms differed, and which side was
corrected. Section 10 writes the terms a ticket carries and their laws.
Section 11 states the gap in these terms.

The page of computational algorithms lists what the build may use. This page
says how the entries may be combined, what each combination keeps, and writes
each flow of the requirements as one combination. A flow that cannot be
written this way is not allowed.

## 1. Two kinds of term

A **pure term** computes a value and does nothing else. An **effect term**
reads or changes the world outside the program. Every entry of the prescribed
set is one or the other, except C4, which wraps one, and C17, which combines
them.

| Kind | Entries |
|---|---|
| Pure | C2 map difference, C3 conjunction, C5 recursion over terms, C6 name resolution, C8 rule list, the measure of C9, C14 encoding, and the six helpers |
| Effect | C1 content addressing (it reads files), C10 the log, C11 the hold, C12 the child process, C13 the merge, C15 create if absent, C16 the clock |
| Wrapper | C4 the memo, over a pure term or a check |
| Combinator | C17, which carries K5 to K8 of section 2 |

The clock is the one effect read by a plain call. A flow calls C16's `now()`
wherever it needs the time, as in the function `decide` gives, in a
`repeat`'s bound and in `note`, which stamps each entry. A term that calls it
reads the clock and is not pure, so L1 does not hold for it. The value goes
only where L9 lets it.

## 2. The combinators

There are eight ways to combine terms, and no others. `p` is a pure term and
`e` an effect term.

| | Written | Meaning | Built from |
|---|---|---|---|
| K1 | `p1 ; p2` | Apply `p2` to the value of `p1`. The result is pure | A plain function |
| K2 | `memo(t)` | The value of `t`, kept under the identities of what it reads (L2). `t` is a pure term, or a check, which gives the same result on the same content (REQ-ALG-004) | C4 |
| K3 | `all(p…)` | The three-valued conjunction of results | C3 |
| K4 | `first(rule…)` | The result of the first rule that holds | C8 |
| K5 | `e1 >> e2` | Do `e1`, then `e2`. It is associative, so `>>` over a finite list of terms, in the list's order, is K5 too | C17 `sequence`, `each` |
| K6 | `read >> decide(p) { case → e }` | Read the workspace, compute a pure value from what was read, and do the effect that value selects. What is read may also be the outcome of an effect term that K6 encloses: its value, or the fault it failed with | C17 `decide` |
| K7 | `repeat(e, measure, bound)` | Do `e` again while the measure falls and the bound is not reached. The measure may be left out, and the bound alone then ends it (C9's `within`, D51) | C9, in C17 `repeat` |
| K8 | `held(name, e)` | Do `e` while holding `name`. No other process does so at the same time | C11 through the hold service, in C17 `held` |

`note(event)` is the effect of adding one entry to the event log (C10). It
may follow any effect term. `end(value)` is the term that does nothing and
gives a value, and `fault(f)` the term that does nothing and fails with `f`.

C17 is one module of the kit, `src/kit/calculus.ts`. It is the one place a
flow reaches Effect. It gives:

| Function | What it is |
|---|---|
| `sequence(e…)` | K5 over the terms written |
| `each(values, x → e)` | K5 over a finite list, in its order |
| `decide(read, x → e)` | K6. `read` is an effect term, and the function from what it gave to the term to do is pure, but for the clock (section 1) |
| `outcome(e)` | The read of K6 that gives `e`'s value or its fault |
| `repeat(state, body, bound, measure?)` | K7. The body gives the state for the next round, or leaves with a value. The state is the only value carried from one round to the next |
| `held(hold, name, e)` | K8. `hold` is the hold service, which C17 knows only by its shape: a thing that does a term while holding a name, or says another holds it. C17 imports nothing of the services |
| `end(value)`, `fault(f)` | The two terms that do nothing |
| `using(service, s → e)` | The term `e` over one of the services of REQ-FLOW-001. It reads nothing but the clock (section 1), and decides nothing |

K1 to K4 are plain functions and are not part of C17.

## 3. The laws

| | Law | Guard rail or requirement it carries |
|---|---|---|
| L1 | A pure term given equal inputs gives an equal value | REQ-ALG laws of each algorithm |
| L2 | `memo(t)` equals `t`. Its key is what `t` reads, each place with its identity (C1). A check reads: for `ticket_field`, the ticket; for `traced`, the two assets it names; for a command, the workspace's folder but what lies apart, or all of it where its command names a place apart. Apart lie what the framework and an evaluating session write between readings: the framework's own folder, and the findings and verdict of each evaluation (`apart`). A check that reads past the folder, `ticket_kept`, which reads main's ticket by git, is not kept | REQ-ALG-004 |
| L3 | `all` gives the same value in any order, and says yes only where each of its terms does: where its pure terms already say other than yes, no effect term beside them can make it yes. So a reading does a check (L10) only where its value can change `passes` for the node it is declared of or for the step being decided (`counts`): a node's where the node is there, its records stand or the step's vector writes it, and each node it depends on is accepted or written by that vector; the ticket's where the user's confirmation stands or the step is on the first vector. One not done gives cannot and says it was not done (D18); it stops no step, is not logged as run and fails in no measure (`isDone`). `first` does not give the same value in any order: its order is part of its definition | REQ-ALG-004, REQ-ALG-010; the product definition, "The framework's own work for a step is small and does not grow with the history of the work" |
| L4 | In K6, the inputs of `p` are only what the user's command gave, what was read in that term or in a term enclosing it, and what the enclosing `repeat` carries. A `repeat` carries only the counts and measures for its bounds, and, for the ending's words, where the run is and where what failed sessions printed is kept (D75, D81). Nothing else passes from one step to the next, and nothing is read from the log | Guard rails 3 and 5; REQ-FLOW-003, "reads the workspace and not the event log" |
| L5 | Removing every `note` from a term changes no decision it takes and no file it writes outside the log | REQ-FLOW-007 |
| L6 | Every `repeat` ends within its bound. The round of `build` is bounded by the run's limit of minutes; where the settings set none, REQ-PARAM-003 sets none, and the round goes again only while main has moved. The `steps` of a workflow are bounded by `rounds(w)` (section 5). A round closes a vector, spends one of its attempts, leaves fewer outcomes failing than the working session before it, follows a session that did not fail with one that failed, or ends the steps, so they reach that bound only where a vector that closed in them opens again (D210). The `steps` of an inner workflow follow the graph's terms (C5), and C6 refuses a name that leads back to itself, so they end | REQ-PARAM-003 |
| L7 | Two terms held under one name never overlap, and a hold ends when its process ends | REQ-FLOW-003 |
| L8 | Create if absent, done twice, changes nothing the second time | REQ-FLOW-002 |
| L9 | A value of the clock enters only a bound, a `note`, a run's id, a ticket's name, the simplest ticket's `written` field and the time a `delivered` line of the ticket's checklist holds, which `show` gives (D35, D59, D204). The identities a record stands for are of the ticket without the framework's part, so that time reaches none of them. So it decides the order in which `take_up` takes tickets by name (H2), and reaches one content identity: that of the simplest ticket's text, which its name takes. It enters no other decision and no other identity. It is read by a plain call (section 1), in a flow or a service, and in no pure module | REQ-ALG-001 |
| L10 | A session and a check command are effect terms. Beside the workspace after it, a session gives its outcome (C12) and what it printed, and a check gives its result. These enter only the step they are in: its decisions on that session or check, the log, and the files of what was printed and found. No value passes from one session to the next | REQ-FLOW-005, "nothing passes from one session to the next except the workspace" |
| L11 | An effect term may be cut off after any effect. A run started on the workspace it left reaches the end the uncut term would have reached | REQ-FLOW-005, "the next attempt and the next run judge them as they stand"; scenarios S2 and S3 |
| L12 | `trespass` returns each file git does not ignore whose identity differs between a session's start and when it is over, in the workspace's folder, but what the step writes (`writes`); where the identities of a commit stood in for missing ones, the commit the session started from or, where a later run does not know it, the commit the folder is on, nothing counts as what it writes, and it says that the identities were missing (D241, D246, D255): for a working session the nodes its vector writes, the top `.gitignore` and, for the first vector's, the triage and the term of its ticket; for an evaluating session its findings and its verdict. Of the branch's ticket each part is compared apart. What the framework wrote in that time is not returned, nor a file the user said yes to, at the identity it had at the yes. It also returns, apart, each file of the folder that differs between the commit main, the branch the ticket left, was on at the session's start and the commit main is on now, none of them counted as what the step writes; where a commit's identities stood in, or the record names no commit of main, the commit where the ticket's branch and main last met stands in for main's (D257). Where anything is returned, the step ends asking the user to rule (`session`, section 5): no verdict is read, no check is run, nothing is committed, and nothing is put back. So a step that goes on has changed nothing but what its step writes, or what the user said yes to (D226) | REQ-ALG-008; guard rail 2 |

## 4. The business algorithms as pure terms

| Algorithm | Term |
|---|---|
| `well_formed` | `decode ; resolve names ; place each vector: the nodes it writes and the nodes it rests on` (C14 ; C6, over C5; section 10) |
| `passes` | `all(the checks of the nodes it writes, verdict, answer, nodes)`, each check done as L3 lets. The verdict and the answer are each read at the nodes the vector records them at, and stand exactly where nothing they were given on differs now: `since`, C2 over the identities at their standing keys as given and as now (`identitiesAt`). A key with no content has no identity and is in neither map, so it differs only where it is in one. Each node it writes is there, and each node it rests on is accepted (section 10, T6) |
| `open` | `not passes`, with C2 for what changed |
| `next` | `first of ⟦t⟧ open` (section 10, T4) |
| `brief` | C5 over the vector, with C2 for what changed |
| `trespass` | `difference(identities at the start, identities now)` (C2), less what the step writes, what the framework wrote and what the user said yes to |
| `progress` | the measure of C9 over two sets of check results |
| `take_up` | `first(rule…)` |
| `done` | `all(passes of every vector that takes part)` |
| `stands` | `first(rule…)` over one fold of the log and one reading of the board |

## 5. The flows as effect terms

`snapshot` is the reading of the workspace's folder: identities (C1) and check results,
each `memo(check)` in the check runner (C4, L2), and the identity of what
each accepting node declares, once for the command (D168). It does the
checks of the ticket and of the nodes in the order of the edges (C7), each
as L3 lets on what it read before them; `snapshot(v)`, a reading for a step
on `v`, does them for that step. Nothing keeps a reading: what a
later term needs of it is in the ticket's framework part or the log, and
`show` reads the ticket and the log (D204). `commit` makes no commit
where nothing changed, and is noted where it makes one, but in set-up, which
notes itself first. `end stopped` and `end waiting` name the vector of the
step they end in. Every command but set-up begins with `open`, which gives
the folder and the line it is on to the rest of the term. The library turns
the workspace the user names into a folder, gives the command's term its
services, runs it and puts its ending in words. It reads and decides nothing
itself.

```
gitOld   = read git's version (C13) >> decide(it reads as older than 2.38) {
             yes → end refused, changing nothing, naming the version found and the version needed (D248) }

open     = gitOld >> read the folder >> decide(it is there, lies in a repository, is set up, and is on a line) {
             no → end refused }   (the folder's place from the repository's top is read with it, D201)

set-up   = gitOld >> read the method at the place the library gives >> decide(it is there) { no → fault }
           >> repeat(read the parent, measure = the path's length, bound = its depth)
             to the nearest folder that is there
           >> read the repository that folder lies in >> decide(where the folder lies) {
             below its top → read whether the repository ignores the folder >> decide(it does) {
                               yes → end refused, naming the repository
                               no  → make the folder where it is not there >> set-up', naming the repository (D201) }
             in none       → make the folder >> make the repository >> set-up'
             its top       → set-up' }

set-up'  = read the line the folder is on >> decide(there is one) { no → fault }
           >> read what is running, from the manifest at the place the library gives (D197)
           >> create(definition, naming an existing system's places where there is one)
           >> install the method >> create(each framework file, the settings recording what is running)
           >> each agent file: read >> decide(what it holds) {
                nothing         → create(it)
                not the block   → add the block
                the block       → report it }
           >> decide(an existing system is there) { yes → create(the first ticket) }
           >> commit >> note(set-up) >> note(commit made, where it made one)

run      = decide(outcome(open >> read whether the log is there
                          >> note(run started, saying so where it is not))) {
             fault   → end refused (D75)
             refused → end refused
             noted   → decide(outcome(run')) {
                         fault in writing the log → end refused (D75)
                         fault                    → closing(refused) (D75)
                         ended                    → closing(its ending) } }

closing(x) = decide(outcome(note(run ended))) {
               noted → end x
               fault → end x, saying the log could not be written (D75) }

run'     = read the record in main's settings >> read what is running (D197)
           >> decide(the record is there and is what is running) { no → end refused }
           >> read main >> decide(well_formed) {
             no  → end refused
             yes → read the table of processes (C12) >> decide(it can be read) {
                     no → end refused, starting no session and ending nothing, saying in one sentence that `ps` was not found or could not read it, and what to install; naming no process (D249) }
                   >> each active ticket no live run holds: read whether its hold was left by a process that has ended (C11)
                     >> read the live processes it knows to be of its sessions, and, where the hold was left, those it cannot place (C12, D222, D223) >> decide(what was read) {
                       cannot tell              → end refused, cannot tell, ending nothing, naming why (D212); where the table cannot be read, in its one sentence, naming no process (D249)
                       none, hold free          → nothing
                       some, or the hold left   → end those it knows >> note(session processes ended, where it ended any)
                                                  >> decide(none it knows is left, and, where the hold was left, none it cannot place) {
                                                       no → end refused, naming the hold and each process } } (D215, D224)
                   >> each active ticket whose hold was left: decide(a record from a session's start is kept) {
                        yes → say it cannot tell what changed among the branches, tags and stash, nor, inside a larger repository, outside the folder } (D228)
                   >> each active ticket whose hold was left: note(run cut off) >> held(t, nothing) (D232)
                   >> read the branches, the active ticket and the branch it left, by git (D239) >> decide(where the folder is) {
                        on no branch, or on a ticket's branch, with no ticket active → end refused, naming it
                        not on the active ticket's branch → decide(the branch is only a remote one, or the ticket records no branch it left) {
                          yes → make the local branches from the remote ones; or record the branch the folder is on as the one it left >> commit
                                >> put the folder on the ticket's branch >> decide(git put it there) { no → end refused, naming the working tree that has it and how to remove it, or what git names }
                          no  → end refused, naming both branches }
                        on it, or no ticket active → main is the branch the ticket left, or the one the folder is on }
                   >> read the holds >> decide(a ticket is held) {
                     no → decide(how the record from a session's start on the active ticket stands, read under git's own directory (D245): `standing`) {
                            kept, and compared          → nothing
                            not to be read, naming a step the graph does not hold or what git no longer holds, or none where its run was cut off
                                                        → the commit the session started from stands in, as the record names it where it reads and git holds it, else the commit the folder is on, kept as that session's, with nothing counted as what its step writes (D241, D246, D255)
                            none, no run cut off        → the accepted limit: nothing to compare }
                          >> decide(a record is kept or stands in) {
                            yes → compare, the folder and main as it is now, before main is taken in (D257) >> decide(what differs, on which no yes was given) {
                              files → note(user asked, how many) >> end waiting, with the question, which says first, where the commit stood in, that the identities are missing (D246), and names the files changed on main apart (D257); nothing of main taken in
                              none  → nothing }
                                  >> commit what the step writes and each file of the folder the user said yes to, as the step's result, none of those changed on main >> settle (D227, D241, D257) }
                          >> commit what is still not committed, as the user's change by hand, completing a merge in progress where the folder is the repository's top, whosever it is (D47), and below the top only where it is the take-in's, leaving the user's own there as it is (D201, D240)
                             >> decide(unresolved, anywhere in the repository while the take-in's merge is in progress, else under the folder) {
                               files → decide(a ticket is active) {
                                         yes → end stopped, naming each file from the folder, or from the repository's top where it lies outside, and saying so and where to resolve it
                                         no  → end refused, naming them the same way } (D47, D240) } }
                   >> read main's board by git >> decide(take_up, with main taken as done) {
                     none, no ticket active and none named → read snapshot of main
                          >> decide(take_up, with done on main) { as below }
                     none     → end refused
                     simplest → create(the simplest ticket) >> commit >> build(it)
                     ticket   → build(it) }}

build(t) = read whether t's hold was left by a process that has ended (C11) >> decide(it was) { yes → note(run cut off) (D205; a hold `run'` did not see, D232) }
           >> decide(outcome(held(t,
             decide(t lies in the backlog) { yes → record the branch it leaves in t >> move it to the active lane >> commit on main
                                                  >> make its branch there >> put the folder on it >> decide(git did) { no → end refused }
                                                  >> note(ticket pulled, with main and the branch) (D239) }
             >> take-in(t, no session of the run started) >> read where the method release is installed (D89)
             >> repeat(round(t), bound = the run's limit of minutes)))) {
               another run holds t → end refused
               ended               → end }

take-in(t, s) = read the branch >> decide(it holds all of main) {
               yes → note(main taken in, already held, with main's name)
               no  → decide(the user edited t on main) { yes → read the framework's part of t >> take t as main has it >> commit }
                     >> merge main in, in the folder, wherever in the repository it moved (D240) >> decide(merged) {
                          conflict → add back the framework's part, where t was taken >> note(main taken in) >> end stopped, naming each file from the folder, or from the repository's top where it lies outside, and saying so
                          in the way → add back the framework's part, where t was taken >> commit >> decide(s: a session of the run started) {
                                       no  → end refused, naming each path main adds where a file or a folder git does not hold, or ignores, is there; nothing written over
                                       yes → end stopped, naming them } (D250)
                          refused  → add back the framework's part, where t was taken >> commit >> decide(s: a session of the run started) {
                                       no  → end refused, naming the files git would not write over
                                       yes → end stopped, naming them } (D240)
                          yes      → add back the framework's part, where t was taken, with `unbound` where a binding held >> commit (D202)
                                     >> note(main taken in) }}
             >> read t on main by git >> decide(t lies in the active lane on main) { no → end stopped }

round(t) = steps(⟦t⟧) >> read the branch >> decide(it holds all of main) {
             no  → take-in(t, whether a session of the run started) >> go round again
             yes → read the working trees by git >> decide(main is checked out in another working tree) {
                     yes → decide(a session of the run started) { no → end refused, naming it; yes → end stopped, naming it } (D240)
                     no  → decide(t lies in the active lane of the branch) { yes → move it to done >> commit }
                           >> merge into main: a commit of the branch's whole tree with both parents, main moved to it, the folder put on main; no file written (D240)
                           >> decide(merged) {
                                refused → decide(a session of the run started) { no → end refused, naming what git names; yes → end stopped, naming it }
                                yes     → note(ticket merged, with main's name) >> end done, naming main, and, inside a larger repository, each file outside the folder that differs between main before the merge and the merge's commit (D256) }}}

On a workflow, `done` holds where `next` gives none: both read one snapshot,
over the vectors that take part, and `next` gives none only where each of
them passes (T4). So `steps` leaves only where `done` holds.

steps(w) = repeat(vector(w), bound = rounds(w))

⟦t⟧ is the governing graph cut to the first vector and the vectors the
ticket's term denotes, in its order (section 10). A round steps on those and
no other. An induction entry of t is the first vector bound to its stretch.
Where the round reaches it, the step on the first vector is the same
`step(v)`: its brief binds the session to the stretch, and its check holds
the new term to t with that entry alone replaced (T5). The user is asked on
it, so the run ends waiting, and ⟦t⟧ never changes within a run. Where there
is no term to read, for the simplest ticket and on main, it is the registry's
default term. The one decision on which vectors take part is the term's, the
user's confirmation of the induction; the graph language has no condition
(D172).

vector(w) = read snapshot >> decide(next among the vectors of w) {
              none → leave, with the snapshot
              v    → step(v) >> decide(how it ended) {
                       closed            → again
                       asks              → end waiting
                       stopped, or ended → end
                       failed            → decide(the session before it on v in this run failed) { no → again; yes → end stopped }
                       open, judged no   → decide(within v's attempts) { yes → again, a new attempt; no → end stopped }
                       open              → decide(progress within the attempt) { yes → again; no → end stopped }}}

step(v)  = read snapshot(v) >> decide(a check it did cannot be run) { yes → end stopped }
           >> decide(a working session is needed: the first entry to v under the confirmed term, D209, or a check, a verdict or an answer says no, or a change) {
                yes → each part of v's function, in the order written (C5, C6): decide(the part) {
                        a session  → decide(a part ran before it) { yes → read snapshot (D165, D204) } >> session(work, v)
                        a workflow → steps(it) >> decide(how they ended) { ended → end } }}
           >> decide(v declares an evaluation; a part ran, or no verdict stands, or it says cannot) {
                yes → decide(a part ran) { yes → read snapshot(v) }
                      >> decide(v's asset is there, D97; and each check of v's nodes says yes, D173) {
                           yes → session(evaluation, v) >> read whether it wrote the verdict >> decide(it did) {
                                   yes → note(verdict read) >> decide(it says yes or no) {
                                           yes → commit >> at each node the verdict is recorded at, add its resolution to t >> commit (D164, D203) }
                                   no  → note(verdict not written) }}}
           >> read snapshot(v) >> write what the checks found >> each check it did: note(check run)
           >> decide(passes, asks the user) {
                a check it did cannot be run → commit >> note(vector left open) >> end stopped
                the verdict says cannot → commit >> note(vector left open) >> end stopped (D90)
                closed → commit >> add `delivered` to t's checklist >> commit (D202) >> note(vector closed) >> end closed
                ask    → commit >> add `delivered for the user's decision` to t's checklist >> commit >> note(user asked)
                         >> end asks, with the question; no file holds it (D204)
                open   → commit >> note(vector left open) >> end open }

session(k, v) = decide(a limit of the run is reached) { yes → commit, where a part of the step ran before it >> end stopped }
           >> write the brief >> decide(a working session bound to a stretch) { yes → add the binding to t's checklist >> commit (D204) }
           >> decide(a working session on the first entry to v) { yes → add `began` to t's checklist >> commit (D209) }
           >> note(session started) >> read, held by the run alone, the branches, tags and stash, and, inside a larger repository, what git lists outside the folder and the commit the folder is on (D228, D243)
           >> take and keep the identities of the folder, with the commit main is on (D227, D257)
           >> session(k), the processes it knows to be of it ended at its end, and those it cannot place looked for (D213, D222, D223)
           >> keep what it printed, in a file of its own (D218)
           >> note(session processes ended, where it ended any)
           >> decide(settled: a signal received from the session's start, or the session not over) {
                yes → go no further, leaving the hold, naming each process where the session is not over (D214, D221) }
           >> note(session returned or failed, with the cost and calls it printed, D91)
           >> read them again, and name what differs, as changed while the session worked, main among the branches, not said to hold no ticket where it changed a file of the folder (D257); and, inside a larger repository, each file outside the folder that differs between the commit the folder was on at the start and the one it is on now, as committed while the session worked, and, apart, each that differs between main's commit at the start and now, as committed on main, or that git cannot compare the two (D228, D243, D256, D257)
           >> decide(the folder is on the ticket's branch) { no → end stopped, naming the branch; nothing committed }
           >> read the record from the session's start (D245) >> decide(it is that session's, kept, and compares) {
                no → the commit the session started from, which `note(session started)` named, stands in, kept as that session's, with nothing counted as what its step writes; where git does not hold it, the stand-in cannot be compared, and the flow fails, with nothing written (D246, D255) }
           >> decide(trespass, its outcome) {
                files, in the folder or changed on main → note(user asked, with how many files) >> end asks the user to rule; nothing committed, judged or read, and nothing of main taken in (D226, D257)
                none   → settle the identities kept (D227)
                failed → commit >> end failed }

answer   = open >> read main >> decide(well_formed) { no → end refused }
           >> decide(the answer is no, with no reason) { yes → end refused }
           >> read the branches by git >> decide(the ticket is active) { no → end refused }
           >> decide(the folder is on its branch) { no → end refused, naming both branches } (D239)
           >> read the live processes of the ticket's sessions (C12) >> decide(none, and the framework can tell) { no → end refused } (D216; where the table cannot be read, in its one sentence, naming no process, D249)
           >> decide(outcome(held(ticket, letting go as it found the hold, so a hold a cut-off run left is left so (D232),
                decide(how the record from a session's start stands, as at the start of a run: `standing`) {
                  stands in → end refused, saying that a run asks on every file not committed; nothing is written (D246) }
                >> decide(identities kept from a session's start, and a file differs on which no yes was given) {
                  yes → add the user's ruling on what changed to the ticket, a yes with each file's identity now, and with each file changed on main, named apart, at the identity main gives it now (D257), a yes or a no with each line of the framework's part that changed while the session worked
                        >> note in the record the identity of the ruling's line and each file of a yes
                        >> note(answer written) >> commit that line alone >> end (D227, D230) }
                >> read the ticket >> read identities, and those under the commit of the last delivery for the user's decision (D204)
                >> decide(that delivery has no answer of the user after it, and nothing the answer would stand for differs now from that commit) {
                  no → end refused
                  v  → at each node v writes that the user's yes accepts, or under the first vector's name (D164): add the user's resolution to the ticket,
                       with the ruling where one is given >> note(answer written) >> commit
                       >> decide(the answer is yes) { yes → note(vector closed) } }))) {
                another run holds the ticket → end refused
                ended                        → end }

show     = open >> read main >> decide(well_formed) { no → end refused }
           >> read board >> read git's lines and merges
           >> each active ticket: read its ticket, and what git holds under the commit its confirmation names (D204) >> read what its branch changed
           >> each done ticket: read what its merge brought
           >> read log (one fold) >> stands

registry = open >> read main >> decide(well_formed) { no → end refused; yes → end(its registry) }

ticket   = open >> decide(words are given) { no → end refused }
           >> read the identity of its text, and the clock >> create(ticket file) >> note(ticket written)

record   = open >> read the settings >> read what is running (D197)
           >> decide(the settings read as an object) { no → end refused }
           >> decide(the record is what is running) { yes → end }
           >> write the settings, with the record in its place >> note(release recorded) >> end
```

Every run ends at exactly one `end`: done, waiting, stopped or refused. The
program prints what `show` and `registry` give.

Where a fault is decided (D75, D81). Each `repeat` of a run decides on the
outcome of its body. A fault met inside `steps` or `round` ends the run as
stopped, naming the vector of the state that repeat carries, with the places
of what failed sessions printed; where the state names no vector yet, the
run is refused. `run` decides on the outcome of all the rest, so only a fault
met outside every repeat reaches it, and it ends the run as refused: a fault
in `open`, in reading whether the log is there, in writing `run started`, or
in `run'` outside the round. The log holds nothing of a fault met before `run
started` is written, nor of one in writing the log. Any other is noted as
`run ended`. `run` decides on the outcome of writing `run ended` too. A fault
there leaves the ending the run reached, since the log changes no decision
(L5), and the log holds nothing of it. The ending is shown, and its words say
that the event log could not be written at its path and that the user puts
that right before the next run (D75). The run gives this beside its ending,
and the library puts it in words, as it does where the run started a new log. So `run`
fails with nothing, as D75 says. A step decides on the
outcome of what follows a session that failed, so a later fault in that step
loses no place. The state of a run,
its sessions and minutes, the attempts at each vector, the last vector and
the places, passes into `step` and into the `steps` of an inner workflow, and
comes back out with their ending. So the run's limits count the sessions of
inner workflows too (REQ-PARAM-003).

How `steps` ends. `rounds(w)` is the sum, over the vectors of `w`, of each
one's attempts and one more, times two rounds for each count of failing
outcomes its working sessions can pass through, and one round more for the
reading that finds none (D210). `steps` has no measure (K7): which vectors are open is read in each
round, from the snapshot, and is not carried. Inside a round, `vector` ends
the steps where a vector has used its attempts, where its working sessions
leave no fewer outcomes failing, or where two sessions on it fail in a row, and `session` ends them where
a limit of the run is reached. A round that closes a vector spends no
attempt, so the bound is what ends the steps where a vector that closed in
them opens again. Where it is reached, the run ends as stopped, naming the
vector of the state, with the words "the steps reached their bound".

Where a limit is read. A step reads both of the run's limits before a
session (D67). The round of `build` reads the limit of minutes before it goes
again. A limit reached ends the run as stopped, naming the limit, and the
last vector of the state where it names one. The round starts no session, so a limit of sessions does
not bound it: a run at its last session whose work is done is merged.

## 6. What this adds to the checks

The checks of the computational algorithms page establish that each module
names entries of the set. These establish the calculus:

| Check | Law | Built |
|---|---|---|
| A pure module imports no effect entry | L1 | As the algorithms' imports are checked |
| The log service has no reader in any flow but `show` | L4, L5 | Not by this ticket |
| A flow is written in the terms of C17 alone, and keeps no value in a variable or an object that changes | L4 | The check of the computational algorithms page, section 6, on how a flow is written |
| The clock is read only by the flows and the services, and by no pure module | L9 | As D59 confines it |

A flow, here, is every module of `src/flows/`. It imports nothing of Effect,
and no kit module whose value changes after it is made: C4 alone is one, and
only the check runner uses it. It has no generator, `async` or
`await`, promise, `.pipe`, loop statement, `let` or `var`, assignment after a
declaration, or call that changes an array, map, set or object in place. Each
of these is refused from a flow's imports or from one line of its text, where
the line names it, in each of these spellings: a name spaced, on that line,
from the `.` before it and from the `(` after it, as `x .pipe (1)`, and a
method that changes in place reached through `.call`, `.apply` or `.bind`,
as `Array.prototype.push.call(xs, 1)`. A member named by a string in
brackets and called, as `x["pipe"](1)`, is refused whatever the string,
since a flow needs none. Without them, a flow sequences, decides and holds
only through C17. It repeats only through `repeat` or by calling a flow
function again, and a value passes from one round to the next only as the
state of `repeat` or as an argument of that call.

What this does not catch, and is left to the evaluation of the code:

- A flow function that calls itself, directly or through others, outside
  `repeat`. The one lawful kind is the `steps` of an inner workflow, which
  ends (L6). Nothing read from a flow's text tells it from a call that repeats
  with no bound, and the flows need it, so the check does not refuse it.
- A conditional expression, in a pure term, that gives one effect term or
  another from a value no `decide` read.
- A member named by a value computed when the flow runs, as `x[name](1)`,
  and a method taken from its object under another name and called by that
  name. A line does not say what such a name holds.
- A name split from its `.` or its `(` by a line break, and an optional
  call, as `xs.push?.(1)`.
- A decision in the library. The library imports Effect to run a term, so the
  check of a flow cannot be put on it.

## 7. The scenarios traced through the terms

Each scenario was read against section 5, by hand. Section 8's check now runs
the log of each scenario against the terms.

| Scenario | The term and law that carry it | In the first draft |
|---|---|---|
| S1 smallest product | `set-up`, `ticket`, `run`, `answer`; the second run is refused by `take_up` under L7 | Covered |
| S2 interrupt and resume | L11, L7; `run'` notes the run cut off (D232), and `build` commits what the cut-off step left | The law was missing |
| S14 a session is over when the framework has ended it | `session(k)` over when every process it knows to be of it is ended and none it cannot place is found; the branch of `session` that goes no further, on a signal or a session not over; the left holds, the processes known and those it cannot place in `run'` (D212 to D215, D221 to D224) | Added with the ticket `261123-185201-a149` |
| S3 no event log | L5; `show` and `run` say the log is not there, and `run` starts one | That branch was missing |
| S4 three changes | `passes` holds an answer only on the identities it was given on; `show` names what each ticket changed from git | `show` did not read git |
| S5 a step that does not close | The `open` branch of `vector`, by `progress` within one attempt, and by the vector's attempts where its evaluation said no (D210) | One loop stood for two |
| S6 second graph, registry, inner workflow | `well_formed` refuses; `registry`; the workflow part of `step` | `registry` and inner terms were missing |
| S7 a session writes outside its vector | `decide(trespass)` in `session`; the comparison at the start of `run` and in `answer` (D227) | Covered |
| S8 an existing system | The first branch of `set-up`; the rest is the graph's data | That branch was missing |
| S9 build again | The `simplest` branch of `run` | That branch was missing |
| S10 two agents | No term: which agent is a setting read by `session` | Covered |
| S11 two tickets at once | Not covered. It is deferred with its requirement, and `collides` is not written as a term | Not covered |
| S12 the life of one ticket | `run` and `answer` again; `show` reads git for a withdrawn ticket's branch | `show` did not read git |

## 8. The check of the event log

The terms of section 5 allow some orders of `note` and refuse the rest. A
check in the tests reads the log each scenario leaves and refuses one they do
not allow. The scenario driver applies it to the log of every workspace it
makes, before it removes the workspace's folder, so a scenario whose log is
refused fails. A test of its own gives the check a log with one entry out of
order, and the check refuses it.

Every entry a run adds names the run by its id (`run`). Today only some of
them do; the code is corrected to name it in all. The entries that name no run
are set-up's, the answers', `ticket written` and `release recorded` (D205).
These never overlap: an answer holds its ticket, set-up writes before any
run, and `ticket` and `record` each add one entry. Two runs started in the same
millisecond share an id (D75), and the check refuses a log where they did. An
entry the check cannot read is passed over, as the log service passes over it
(REQ-FLOW-007).

A step's entries are those of a session, a check, a verdict not written, a
vector closed or left open, the user asked, and a commit made that names a
vector. The check reads the log in three parts.

1. The entries that name no run form a word of `{ set-up | answer }`.
2. The entries of one run that are not a step's form a word of `run`.
3. The step entries of one run that name one vector, taken in their order,
   form a word of `{ step }`. They lie after that run's first `main taken
   in`, and before its `ticket merged` or its `run ended`.
4. The sessions of one run on a ticket are those ⟦t⟧ gives, t the term in
   force: each is on the first vector or a vector t names, and those under
   one term follow its order, a vector repeated as its attempts need. A vector
   t names may have no session, since its asset may stand already. The term
   in force at a session is the one the ticket holds in the commit of its
   step, or the registry's default where it holds none, read in git by the
   workspace's own graph as `inForce` reads it (D129, D136). So a session
   before a substitution is held to the term confirmed with the induction
   entry, and one after it to the term that replaced it (T5).

```
set-up  = "set-up" [ "commit made" ] | "ticket written" | "release recorded"
answer  = "answer written" { "answer written" } [ "commit made" ] [ "vector closed" ]

run     = "run started" { "session processes ended" } [ "run cut off" ] [ "commit made" ] [ "user asked" ]
          [ "commit made" ] [ "commit made" ] [ "commit made" ] [ "run cut off" ] [ pull ] [ build ] "run ended"
pull    = [ "commit made" ] "ticket pulled"
build   = [ "commit made" ] ( take-in { take-in } [ last ] | [ "commit made" ] )
take-in = [ "commit made" ] "main taken in"
last    = "commit made" | merge
merge   = [ "commit made" ] "ticket merged"

step    = { session [ "verdict not written" | "verdict read" ] | "commit made" } [ judged ]
session = "session started" [ "session processes ended" ] ( "session returned" | "session failed" )
judged  = { "check run" } { "commit made" }
          ( "vector closed" | "vector left open" | "user asked" )
```

A commit with no closing entry is where git refuses what follows it, and the
run then ends as refused where no session of it started, and as stopped
otherwise (D240). In `take-in`, git would not take main in after the
branch took the user's edit of the ticket: as the run's first take-in, that
is the lone commit of `build`'s second branch, and later it is `last`. In
`round`, git would not merge the branch into main, after the ticket moved to
done: that is `last`.

Where the log a run was adding to is gone when the run next adds to it, the
run starts a new one whose first entry is that run's `new log started`, with
the release in force (D247). The rest of the run's word lies in the new log:
the check reads of such a run only that `new log started` is its first entry
there, and its only one.

A term may be cut off after any effect (L11). So the entries of a run may
also be the start of a word: a run killed at work, cut off by a signal, or
gone no further on a session it could not end, after its `session processes
ended` where it ended any (D214, D221), leaves no `run ended`, nor
does a run whose `run ended` could not be written, and a run that met a fault
ends with `run ended` straight after the start of a word (D75). A run that
met a fault before its `run started` was written leaves no entry. The last
step of each vector in a run may likewise be cut short, and so may the last
answer.

## 9. Where the code and the terms differed

1. Repaired by D80, then by D204. `answer` read a snapshot, which ran every
   check. It now reads the ticket and the identities, now and under the
   commit of the delivery it answers, and runs no check, as section 5 writes
   it. `show` reads the ticket and the log, and no record of a reading.
2. The memo is the check runner's. One map, held by the check service, keeps
   each check's result under the identities of what the check reads
   (`services/checks.ts`). The check that reads main's copy of the ticket
   reads past them and is not kept. A verdict or an answer is no memo: it
   stands by `since` (section 4). The page put C4 over a pure term alone,
   where REQ-ALG-004 lets a check's result be used again on the same content.
   The page is corrected: K2, L2, the reading of `snapshot` and the row of C4
   cover a check.
3. The terms of section 5 have been read line by line against the flows of
   `src/flows/`. Where they differed, this table says which side is
   corrected.

| Flow | Where they differed | Corrected |
|---|---|---|
| Every flow | The code sequences, decides and loops with Effect's generators, `while` and `if`, and keeps the run's state in variables it changes | The code: it is written in C17's terms alone (section 6) |
| Every flow | A session's outcome and what it printed are decided on and kept, where L10 said a session's only result is the workspace | The page: L10 says where they go |
| Every flow | A run's state carries where it is and where failed sessions' output is kept, beside its counts (D75, D81) | The page: L4 says what a `repeat` carries |
| `ticket`, `run` | A ticket's name and a run's id are made from the clock (D35). The simplest ticket's text holds the clock's `written` value, and its name takes the identity of that text (D59). So the clock orders tickets by name and reaches one content identity, where L9 and C16 said it entered no identity and no decision but a deadline | The page: L9 and C16 name both |
| Every command | The library finds the workspace, and refuses where there is none, where it is not set up in a repository, or where it is on no line. It refuses an answer where the graph is not `well_formed` and a ticket with no words, and reads the method set-up installs. These are decisions on what was read, made outside C17, and no term had them | Both. The page writes them as `open` and as branches of `answer`, `ticket` and `set-up`. The code moves them into `src/flows/`, and the library keeps only what section 5 gives it |
| `set-up` | The nearest folder there is is found first; a folder on no line is a fault; the first ticket is written after the framework files; an agent file is added to, not only created. The term noted the commit before `note(set-up)`; the code notes set-up first | The page |
| `run` | Main is not committed while another run holds a ticket (D57), and a merge left unresolved there refuses the run where no ticket is active (D47) | The page |
| `run'` | The term refused the run wherever a merge was left unresolved. The code stops it where a ticket is active, as D47 and REQ-FLOW-003's endings say, and refuses it only where none is | The page: `run'` decides on whether a ticket is active |
| `run'` | While main was taken in, git could leave a file unmerged outside the workspace's folder, and C13's commit looked for unmerged and marked files under the folder alone: the next run met git's refusal of `write-tree` as a fault, naming the file from the repository's top with no word saying so, and would have committed a file outside the folder staged with the lines that mark a conflict (D47) | The code: while the take-in's merge is in progress C13 looks in the whole repository and gives each file from the repository's top, and the run names it as `take-in` does (D240). The page: `run'`'s `unresolved` says so |
| `run'` | Below the top, the run's commit of what the user left uncommitted completed any merge in progress, a merge of the user's own among them, with both its parents, so it took in files outside the folder; and with no ticket active, a file outside the folder that the user's merge left unmerged refused the run | The code: below the top, C13 completes only the take-in's merge, whose second parent main holds; any other merge is left under way, the commit is of the folder's files alone with one parent, and its files are looked for under the folder (D201, D240). The page: `run'` says so |
| `run` | `take_up` reads main's snapshot only where nothing else gives a ticket (D38); the simplest ticket is committed | The page |
| `run` | A fault ends the run as refused, or stopped where a step has started (D75); no combinator expressed it. The term written for it left `open`, `run started` and the `run ended` of an ending that met no fault outside every `outcome`; the code followed it, and a fault there gave exit 4 | The page and D75. K6 reads an effect term's outcome, and `run` decides on the outcome of each (section 5). For a fault in writing `run ended`, D75 is corrected: the run keeps the ending it reached, as L5 asks, and its words say that the log could not be written. D75 gave the fault ending there, stopped at the last vector or refused, as the code did before the calculus build. Everywhere else the term is corrected towards D75. The code is corrected to follow the term |
| `build` | It pulls the ticket onto a branch of its own in the workspace's folder (D239), takes main in again where main moved by the time `done` says yes, and stops where the ticket left the active lane (D47, D48; REQ-FLOW-008) | The page |
| `build` | A run held by another is refused | The page |
| `take-in`, `round` | The term merged main in whatever main had changed. The code first asks whether the branch holds all of main, and where it does, notes `already held` and merges nothing; where it does not, main is taken in wherever in the repository it moved (REQ-FLOW-008 step 1, D240, which replaces D201's take-in of the folder alone) | The page |
| `take-in`, `round` | The term ended the run as stopped where git refused to take main in or to merge, and where main was checked out in another working tree. The code refuses the run where no session of it started, and stops it where one did (REQ-FLOW-008, REQ-FLOW-003, D240) | The page: `take-in` is given whether a session of the run started, and `round` decides on it |
| `round` | The term moved the ticket to the done lane before it looked at the other working trees. The code looks first, and where main is checked out in another, moves nothing and merges nothing, so main and both working trees are as they were (REQ-FLOW-008, D240) | The page |
| `take-in` | A file git could not merge outside the workspace's folder was named by its path from the repository's top with no word saying so, where every other path the run gives is from the folder (D49) | Both. The code: C13 gives each file from the repository's top, and the run names one outside the folder from there and says so, as for a refusal (D240). The page: `take-in`'s conflict says how each file is named |
| `session` | The term did not show the note the run holds before and after each session, of the branches, tags and stash and of what lies outside the folder, which the code takes (D228) | The page: `session` reads it before and after, and names what differs and what was committed outside the folder (D256) |
| `build` | The round that takes main in again reads no limit of the run. A run whose round goes again with no session passes the minutes the settings set (REQ-PARAM-003) | The code: the round is bounded by the run's limit of minutes, read before it goes again (section 5). L6 holds for it |
| `steps` | Its `repeat` carried neither the bound nor the measure the term named. It ended only through `vector`'s decisions and the limits `session` reads, and a round that closes a vector spends no attempt | Both. The term leaves the measure out (K7) and names the bound `rounds(w)`. The code gives the `repeat` of `steps` that bound, so L6 holds for it |
| `vector` | Inner terms run inside a step, as parts of its work, not in its place (D65); a failed session is tried again by the bound alone (D51) | The page; K7's measure may be left out |
| `step` | An outcome that cannot be run stops the step before any session, and again after the last reading (D38); a limit of the run stops it before a session (D67); a verdict not written is noted (D45) | The page |
| `answer` | It is refused before the hold where a no has no reason, the ticket is not active, the folder is not on its branch (D239), and where a run holds the ticket | The page |
| `show`, `registry` | Each is refused where the graph is not `well_formed`; printing is the program's | The page |
| Every run | Only the entries `run` adds itself name the run | The code (section 8) |
| Every flow | The check of how a flow is written passed `x .pipe (1)`, `x["pipe"](1)` and `Array.prototype.push.call(xs, 1)`, where section 6 said each refused form is refused from one line | Both. The code: the check refuses the three, and its self-test plants them. The page: section 6 says which spellings a line refuses, and names those it cannot |
| Every flow | A flow reads the clock by a plain call to C16's `now()`, as for a run's id, a ticket's name, the bound of `build`'s round, the limits `session` reads and the stamp `note` gives each entry. Section 1 put C16 among the effect terms, and the page did not say a plain call reads it | The page: section 1, `decide`, `using`, L9 and section 6 say so. The code's header of C16, which still said the clock enters no decision but a deadline, is corrected to L9 |

## 10. The terms a ticket carries

The induction writes on the ticket one term of the graph language
(REQ-GRAPH-001, REQ-METHOD-006): a reference to an entry of the registry, or
a sequence of terms. A reference to the first vector's graph function is an
induction entry, and names its stretch: the node it enters at and the node it
ends at, `ref n over a..b` (D140). It is read through the constructors (C14,
C5), so it is in normal form. In the governing graph G it denotes a list of
G's vectors:

```
⟦t₁ ; … ; tₙ⟧    = ⟦t₁⟧ ++ … ++ ⟦tₙ⟧    the empty sequence denotes the empty list
⟦ref n⟧          = [v]                  v the one vector of G whose graph function is ref n
⟦ref n⟧          = ⟦def n⟧              where no vector of G carries out n; def n from the registry (C6)
⟦ref n over a..b⟧ = [first over a..b]    the first vector, bound to the stretch from a to b
```

A session or a workflow that no vector of G carries out, a name the registry
does not list, a name that leads back to itself, a name two vectors carry out
and a stretch on a name no vector carries out denote nothing (`denoted`,
D121). A stretch is written only in a ticket's term: `well_formed` refuses
one in the graph or the registry (D140).

G is its nodes and its edges: each node declares once the nodes it depends on
(REQ-GRAPH-003), and nothing else states a dependency; no node depends on
itself, through any others (C7). What each node depends on, through any
others, is C7's `needed`, once for the graph (`below`). An entry of the
registry says only which nodes it writes, `W(e)`. What it rests on is
derived: `R(e) = deps(W(e)) \ W(e)` (`restsOn`). A vector carries out one
entry and has its `W` and `R`; the first vector writes none. A state is a set
of accepted nodes, and an entry is an arrow `e : S → S ∪ W(e)` from any state
`S ⊇ R(e)`. An induction entry over `a..b` writes the work of its stretch,

```
work(a, b) = {a, b} ∪ { n | n depends on a, and b depends on n }    (through any others)
```

and rests on what that depends on (`workOf`, D158).

Each node declares what must be true of it and what accepts it: an
evaluation's yes, the user's yes, both, or neither (REQ-GRAPH-003), and its
checks. A node is accepted on a workspace where it is there, its records
stand, its checks say yes, and every node it depends on is accepted, through
any others (`unaccepted`): its records are those of what it declares, each
standing for it as it is. A vector records its verdict at each node it writes
that an evaluation accepts, and its answer at each one the user's yes
accepts, each for that node, its declaration and the nodes it depends on. An
evaluation judges those nodes against the nodes they depend on that the
vector does not write (`against`, D169). So a vector declares an evaluation, or a decision, only
where a node it writes declares one, and a vector of G declares each that a
node it writes declares (`well_formed`). The acceptance of a node is read
alike whoever wrote it, and its record stands while that node, its
declaration (its results, what accepts it and what it depends on) and the
nodes it depends on are unchanged (D164, D168).

Laws:

- T1. Identity and associativity. `(r ; s) ; t` and `r ; (s ; t)` are one
  term, and the empty sequence, which writes nothing and rests on nothing, is
  the identity: `[] ; t` and `t ; []` are `t`. The constructor gives this
  normal form: it flattens inner sequences and drops empty ones. ⟦ ⟧ takes
  each sequence to `++`. Broken if a nested sequence denoted other vectors
  than its flat form: `T1` in `tests/graph.test.ts`.
- T2. Reference. Where no vector of G carries out `n`, `⟦ref n⟧ = ⟦def n⟧`,
  and `well_formed` holds `def n` to compose from `R(n)` and to write
  exactly `W(n)`, for every such entry (D155). Where one does, `⟦ref n⟧` is
  that vector, whatever `def n` is. Broken if an alias wrote other nodes than
  it declares: the T2 tests there, and the `registry` cases of
  `tests/cases/well_formed.json`.
- T3. Composition is the law. A list of entries `e₁ ; … ; eₖ` composes from a
  state `S` exactly when each node of `R(eᵢ)` is written by an entry before
  `eᵢ`, or else lies in `S` and is written by no entry of the list, and the
  `W(eᵢ)` are disjoint; it then takes `S` to `S ∪ ⋃ W(eᵢ)`. A ticket's term is well
  formed exactly when it composes from the nodes accepted on the workspace as
  it is, it writes exactly `work(enters, ends)` of the triage, and the vector
  of its first entry declares an evaluation or a decision (REQ-FLOW-004). An
  induction entry names a stretch whose work is smaller than the work it lies
  in and is never the term's first entry, and no other reference names one
  (`composes`, D152). A finding names an entry and a node:
  `X rests on A, which is neither accepted nor written before it`, once for
  each node, with why and where to enter. Why is the first node, through
  what `A` depends on, whose own records do not stand, looked for first past
  the nodes the term writes; where to enter is the nearest node on which both
  that node and the work depend, at which a term can begin and write only
  within the work, or, where there is none, a run with no ticket that accepts
  that node first (D166). The others: `X writes A, which an entry before it
  writes`; a node of the work no entry writes; or one an entry writes
  outside it (D160). So of the orders of one
  set of entries exactly those that respect the edges compose, and terms that
  write the same work are the choices the induction has for it: proportion
  is a choice among them. Broken if an order against the edges composed, or
  one that respects them did not: the 720 orders of the six in
  `tests/graph.test.ts`, of which the two that respect the edges compose.
- T4. Denotation and order. A run carries out the term in force and nothing
  else: the confirmed term, or the registry's default where the ticket
  carries none (D134). `round(t)` steps on ⟦t⟧ in its order (section 5), and
  the log's sessions are on vectors of ⟦t⟧, in its order (section 8). `next`
  is the first vector of ⟦t⟧ that is open, so every vector of
  ⟦t⟧ before it is closed; where no term gives an order, as in an inner
  workflow, the edges give one (C7, D162). A vector of ⟦t⟧ whose nodes
  already stand has no session. Broken if a session ran on a vector outside
  ⟦t⟧ or out of its order: the log check of `tests/event_log.test.ts` and the
  scenario driver.
- T5. Substitution. Let `t = p ; e ; q` be well formed, `e` an induction entry
  over `a..b`, and let `r` be well formed on the stretch: T3 with `a` for
  `enters` and `b` for `ends`, on the workspace as it is. Then `r` writes
  `work(a, b)`, as `e` does, and rests on nodes `p` writes or the workspace
  holds, so `t' = p ; r ; q` composes and writes what `t` writes, and
  `⟦t'⟧ = ⟦p⟧ ++ ⟦r⟧ ++ ⟦q⟧` (T1) is what the run steps on once the user
  confirms `t'` (T4). `r` may hold an induction entry only over a stretch
  whose work is strictly smaller than `work(a, b)`, by the same rule on `t`,
  so the nesting ends within the number of G's nodes. This is the only bound
  added; the session limit of a run bounds the sessions. Broken if a term
  lawful on its stretch broke the whole once put in the entry's place: the T5
  test of `tests/graph.test.ts`, over every stretch and every term of up to
  three entries, with the reverse control of a term put out of the entry's
  place; and each refusal of `substituted` in `tests/algorithms.test.ts`.
- T6. Acceptance is the node's, as this section states it. A vector passes
  where the checks of the nodes it writes pass, the verdict and the answer
  stand at the nodes it records them at, each node it writes is there and
  each node it rests on is accepted; for a vector of G, that is every node it
  writes accepted, since a vector of G records each record that a node it
  writes declares. An evaluation is not started while a check of a node its
  vector writes says no, so no verdict is given over a check that fails
  (D173). No vector is asked to end at a node.
  An edit leaves every node that depends on the edited one unaccepted at
  once; stepping through the default term, the vectors written again are
  those whose own records stand on the edited node: the intent, the product
  and the requirements for the intent; the product and the requirements for
  the product; the requirements, the design, the tests and the code for the
  requirements; the design and the code for the design; the tests and the
  code for the tests; the code for the code. Under the specification and the
  build as the default, that is the specification for an edit of any of its
  three, and the build for one of the design, the tests or the code (D164).
  A new declaration of a node leaves that node unaccepted, and those that
  depend on it, with its content as it was (D168). Broken if a node were
  accepted while one it depends on is not, or a vector were refused because
  no node it writes depends on all the others: the D164 tests of
  `tests/method.test.ts`, each with its reverse control; or if a node stayed
  accepted over a new declaration of it: the D168 tests of
  `tests/algorithms.test.ts` and `tests/redeclared.scenario.test.ts`; or if
  a vector of G passed while a node it writes is not accepted: the T6 test of
  `tests/algorithms.test.ts`, over every graph the tests hold and every
  workspace with one node, declaration or record changed, with the reverse
  control of a record taken away.

The run reaches an induction entry where the user's confirmation of the term
stands and the vector of every entry before it passes. The term's check then
says no, so the first vector is next, and its one session, on the
induction's packet, writes `t'` in place of `t` (D142). The packet names the
ticket the user confirmed by its blob in git (D153). The check holds the new
ticket to `t` with that entry alone replaced and every other line as
confirmed, and `r` to T3 on the stretch; the user confirms `t'` as they
confirmed `t` (D143). The stretch is bound before its session starts: the
framework adds the binding to the ticket's checklist and commits it, and the
binding ends at the first vector's next `delivered` line or at an `unbound`
line, so what a session that failed, or whose run was killed, left is held
to the substitution check as its own (D165, D204). A change to the ticket
that no session bound to the stretch made is the user's: it binds no
stretch, the term is held to T3 on the whole work, and the user confirms the
induction again (D151). The user's edit taken in from main ends a binding a
killed run left, by an `unbound` line (D202).
The confirmation stands on the ticket and on what the first vector declares
of it, so a new line there asks the user again (D175). It is that ticket's
alone: the first vector's resolution is read from the branch's ticket alone,
so one a merge carried in confirms nothing (D200, D203).

`tests/method.test.ts` tests the method's edges, what an edit of each node
reopens under either default, that acceptance of a node is read alike
whoever wrote it, in both directions, that it is recursive, and that no
vector is asked to end at a node. `tests/algorithms.test.ts` tests each
finding of `composes`, from the reviews' traces; `tests/induction.scenario.test.ts`
a nested induction built to the merge, each refusal of what takes an entry's
place, the user's edit of the term while the run waits at an entry (D151),
and the binding of a stretch whose session fails or whose run is killed,
and its end by the user's edit on main (D165, D202); `tests/s12.scenario.test.ts` the life of one ticket.

## 11. The gap

The product owner's model of the work is a gap between what the
specification requires and the workspace, closed one step at a time
(`builder/.ai-workspace/comments/claude/20261122T020012Z_INSIGHT_homeostasis_and_the_gap.md`,
commentary, sections 3 to 6). In the terms of this page:

- **The gap** is what `done` says no for: the vectors that take part and do
  not pass, on the workspace as it is (REQ-ALG-011). `Γ`, the nodes not
  accepted (section 10, `unaccepted`), is the gap at the nodes; at the
  ticket, it is what the first vector does not pass. Every reading reads
  both again, and nothing carries them (L4).
- **A step** is K6: it reads the workspace, decides on `passes` and what of
  it says no, and does the session, evaluation or question that selects
  (`step(v)`, section 5). On a closed gap it does nothing: `next` gives only
  an open vector, and a vector whose nodes stand has no session (T4). It
  writes only the nodes of its vector (L12), and its work is the gap of each
  of them, one form for an empty node, a node after a no and an accepted node
  under a change (D177).
- **A judgement stands** while nothing it was given on differs now (`since`,
  C2, section 4). So a gap at an accepted node opens only where an identity
  it was given on differs now.
- **Changes compose.** A step reads a change as the difference from the
  record to the workspace now (L2, L4), never a state between, so two changes
  made one after the other are read as one.
- **A run** is K7 over the gap. In the model the gap is its measure and falls
  to empty. As built, `steps` carries no measure and its bound ends it (L6):
  a closed step takes the nodes its vector writes out of `Γ` (T6), but a
  session that rewrote an accepted node of its own, or an edit between
  rounds, puts what depends on that node into `Γ`.
- **Intent, solutioning, action.** A ticket states a gap, and the simplest
  ticket is the gap the workspace itself shows, as after an edit by hand
  (`take_up`). The induction chooses a term that closes it (T3), and
  `round(t)` carries out ⟦t⟧ (T4). Where `done` says yes on main there is
  nothing to build. Runs repeated to that point are the model's homeostasis;
  whether a ticket or an edit opened the gap is not asked.
- **The cost of a step** follows the gap: a check is done only where its
  value can change `passes` (L3), and once for what it reads (L2). **Resumption** is L11.
