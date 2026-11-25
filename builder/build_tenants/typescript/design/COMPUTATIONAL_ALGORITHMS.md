# Design: the computational algorithms and the bind

**Status**: Accepted.

The requirements state the product as business algorithms and flows, with
their parameters apart. This page is the next two layers: the computational
algorithms the build may use, and the three-way bind of business algorithm,
computational algorithm and stack.

## 1. The prescribed set

The build uses these computational algorithms and no others. A design or a
piece of code that needs one that is not listed stops, and the product owner
adds it to the set or does not. This section names no stack.

| | Computational algorithm | What it computes | Its law | Cost |
|---|---|---|---|---|
| C1 | Content addressing | The identity of a file is a hash of its content. The identity of a folder is a hash of the names and identities in it. A file git holds is read back by its identity | Equal identity, equal content | Follows the files that changed, not the files there are |
| C2 | Map difference | From two maps of path to identity: the paths added, removed and changed | Empty exactly when the maps are equal | One pass |
| C3 | Three-valued conjunction | Of results yes, no and cannot: cannot if any is cannot, else no if any is no, else yes | The order of the results makes no difference | One pass |
| C4 | Memo by content key | The result of a function with no effects, or of a check, which gives the same result on the same content (REQ-ALG-004), kept under the identities of all its inputs | Never read under any other key | One lookup |
| C5 | Structural recursion over terms, with a normal form | Every function of a graph follows the shape of its terms. Two rewrites give the normal form: a sequence inside a sequence is flattened, and a term that does nothing is dropped | The rewrites change neither the vectors nor their order | One pass over the terms |
| C6 | Name resolution with cycle refusal | Each name of a graph function is followed to its definition in the registry | A name that leads back to itself is refused | One pass over names and references |
| C7 | Dependency order | Items and the things they need and produce form a graph. The first item in declared order whose every need no other item left produces is taken next. The items left when none can be taken lie on a cycle of needs, or need what such an item produces | The same items give the same order, and each item comes after the producers of what it needs | One pass over the items left for each item taken |
| C8 | First-match rule list | Rules in a fixed order. The first whose condition holds gives the result | The order is part of the definition | One pass over the rules |
| C9 | Bounded loop with a measure | Repeat while a count strictly falls and a bound is not reached | It ends within the bound | The bound |
| C10 | Append-only log with a fold | Entries are only added, each whole or not at all. A reader makes one pass and keeps a running result | Earlier entries never change | Adding does not grow with the log. Reading is one pass |
| C11 | Exclusive hold bound to a process | At most one holder. The operating system releases it when the holder's process ends; a process given the holder's number again holds nothing (D216) | Nothing has to clean up after a killed holder | Constant |
| C12 | Supervised child with a deadline | Start a process and wait for its return or for the deadline, and end it at the deadline. A marked child is a session's agent: every process the framework knows to be of the session, by its parent, its group or its mark, from the agent's own process on, is ended at its return, at the deadline and on the run's signals, and a process it cannot place is looked for, before its outcome, which says how many were ended and, where the session is not over, why, naming each process (D212 to D214, D221 to D223) | Exactly one outcome: returned, could not start, stopped without returning, ran over, cut off | The child's own time, the rounds of ending its processes, and the readings of the process table until one tells of every process not known otherwise whether it holds the mark |
| C13 | Three-way merge from a common ancestor | Git's merge of two lines of work. Deferred: the assets changed on both sides are the intersection of two C2 results | It decides nothing about which side is right | Follows what changed |
| C14 | Lossless encoding | A value written as text and read back is equal to the value. One value has one written form | Reading refuses anything it does not know | One pass |
| C15 | Create if absent | Write a file only where there is none. Otherwise report it | Done twice, it changes nothing the second time | Constant for each file |
| C16 | The clock | The present time, read in one place | It enters no decision but a bound and the order of tickets by name, and no content identity but the simplest ticket's; `show` gives the time the line of the ticket or the entry of the log it read was written with (L9 of [the calculus page](CALCULUS.md), D204) | Constant |
| C17 | The combinators of the calculus | K5 to K8 of [the calculus page](CALCULUS.md), section 2: a sequence, a decision on what was read, a repeat under C9 and a hold through the hold service, with the terms that do nothing | A flow built from them and the services alone is one term of the calculus page, and keeps its laws | Nothing beyond the terms it combines |

C17 is the product owner's addition to the set, made by the induction of the
ticket `261120-e8b1-every-flow-goes-through-the-calculus`, which the product
owner answered yes. C7 orders what no term orders: the nodes, to find a
cycle of what they depend on; the vectors of an inner workflow; and the
vectors of a graph whose registry declares no default term. A ticket's term
and a registry's default give their own order, which composes only where it
respects the edges (D162). Over the order of the nodes, C7 gives in one pass
each node with every node it depends on, through any others (`needed`): its
law puts exactly those before the node in every order.

Six named helpers are allowed beside the set. Each has one implementation, in
the kit, and the rules of sections 3 and 6 hold for it as for an entry.

| | Helper | What it computes |
|---|---|---|
| H1 | Place containment | Whether a path is a given place or lies below it |
| H2 | Order by name | Names in the order of their characters |
| H3 | White-space test | Whether a name holds white space |
| H4 | Pattern search | The names of a given form in a text, for the check of traceability |
| H5 | Field lines | A ticket's fields, read from lines of the form `- field: value`, and a ticket without one field's lines |
| H6 | Placing a path in a command | The brief's path put where the agent's command marks it, or added at its end |

## 2. The bind

| Business algorithm or flow | Computational algorithms | Stack |
|---|---|---|
| `identity` | C1 | git, which already computes it |
| `well_formed` | C5, C6, C7, C14 | Plain functions. Effect's schema module reads the graph |
| `passes` | C2, C3, C7 | Plain function. The check runner, a service, keeps check results by C4 in a map |
| `open` | By `passes` | Plain function |
| `next` | C3 | Plain function over `open` |
| `brief` | C2 | Plain function |
| `trespass` | C1, C2 | Plain function over what differs between two identities of each folder, written as trees (D226) |
| `progress` | The measure of C9 | Plain function |
| `take_up` | C8 | Plain function |
| `done` | C3 | Plain function over `passes` |
| `stands` | C8, C10 | Plain function over one fold of the log |
| `collides` (deferred) | C13 | git |
| Set-up | C15, C14, C17 | A term of C17 over the file and git services |
| A run | `next` repeated under C9, C11, C17 | A term of C17 whose four endings are its results |
| A ticket | C8, C13, C17 | A term of C17 over the git service |
| A step | C12, C2, C3, C9, C17 | A term of C17 over the session, check and git services |
| A question and its answer | C14, C1, C17 | A term of C17 over the file service |
| The release that builds a product: set-up's record, a run's check and the command to record it | C1, C14, C15, C17 | Terms of C17 over the file service. The sha256 of the running release's manifest is C1's, by Effect's digest module (D197) |
| The event log | C10 | The log service |
| Merging | C13 | The git service |

The algorithms of the requirements are plain functions: they use nothing of
Effect. Only the flows are effect terms, and each is built from C17 and the
services alone.

## 3. One implementation of each, and the rest composed from it

The code has four layers. Each imports only from the layers above it in this
table.

| Layer | Holds | Rule |
|---|---|---|
| The kit | One module for each entry of section 1 | Exactly one implementation of each entry. Where git or Effect already supplies it, the module is the one place that wraps it. A kit module knows nothing of tickets, vectors or graphs |
| The algorithms | One module for each algorithm of the requirements | Composed from the kit. It implements no entry of section 1 itself |
| The flows | One module for each flow of the requirements | Composed from the algorithms, the kit and the services. Their effects are combined by C17 alone |
| The programs | The command-line program, and later the others | Pass commands to the library's public surface, and nothing else |

## 4. The parts of Effect that are used

Effect is pinned to one exact release of version 4.

| Part | Used for |
|---|---|
| The effect type, with typed failures | The effect entries of the kit, the services, and C17, through which each flow uses it. A flow imports nothing of Effect itself. A failure of a session, a check that cannot run and a file git cannot merge are distinct types |
| Services and layers | One service for each kind of effect the requirements allow (REQ-FLOW-001): sessions, checks, files, git, the event log, the hold. A flow can use no other. Each service is carried out by kit modules |
| A second layer for sessions | The stand-in agent of the scenarios, with no change to a flow |
| The schema module | C14: the graph, the registry, the settings, the tickets' fields and verdicts; and, read as any value, the definition file, what an agent prints and what the method's manager prints (D73, D89, D91) |
| The platform modules for files and processes | C12 and the file service |
| The command-line module | The command-line program |
| The Node platform layer and runtime | To run a flow from a program, and to carry the file and process services on Node |
| The stream module | In C12 alone: to read a child's output and give it input |
| The digest module | In C1 alone: the sha256 of the manifest of the release that is running (REQ-FLOW-010, D197) |

Of Node itself, beside its file and process modules: the process global, in
C11 for whether a holder's process lives, in C12 for a session's signals and
marks (D212 to D214), and in the command-line program for
the exit code.

Not used: fibers and concurrency, schedules, transactional memory and the
rest. A part is added here before it is used.

The library's public surface is plain functions that return promises. An
application that embeds the library does not need Effect.

## 5. How the parameters are met

| Parameter | Met by |
|---|---|
| 100,000 files in a workspace | C1 through git costs what changed. `trespass` asks git which paths differ between two trees of each folder (`diff-tree`), which reads names and identities alone; and, where main moved while a session's identities are kept, which differ between main's two commits, by one more `diff-tree` (D257) |
| 200 vectors in a graph | C5 and C6 are each one pass, C7 one pass over what is left for each item it takes, and `well_formed` places each vector once |
| 100,000 entries in the event log, with under a second of growth | A run only adds to the log (C10) and never reads it. `stands` reads it once |
| The framework's own time for a step, up to 10 seconds | C4: a check is not run again on content it has already judged |
| A brief of up to 100 lines | It holds references only (C2 gives which changed) |
| Git 2.38 or later, for every product | C13 reads `git --version` before anything else of a command (`versionOf`); `open` and `set-up` refuse an older one, changing nothing (D248) |

## 6. How the set is enforced

A rule on a page stops no agent. Each of these is a check the build runs,
with no language model, and a failing one leaves the code step open.

| Check | What it refuses |
|---|---|
| Each entry of section 1 is carried out by exactly one module, in the kit | A second implementation of an entry, anywhere |
| Every other module names the entries it uses and the algorithm or flow of the requirements it is | A module that names none, or names one that is not in the set |
| Each layer imports only from the layers above it in section 3 | An algorithm that reaches past the kit, and a program that holds logic of its own |
| Imports are limited to the product's own modules and the parts of Effect in section 4 | Any other library, and any part of Effect that is not listed |
| The algorithms of the requirements import nothing of Effect | An effect inside an algorithm |
| A flow's type names only the services of section 4, and a built-in of Node or a global is used only in the kit module listed for it | A flow that does anything the requirements' table of effects does not allow. The compiler refuses a service that is not named. The check refuses the rest |
| A flow imports nothing of Effect and no kit module whose value changes, and is written in C17's terms alone, as section 6 of the calculus page lists | A flow that sequences, decides or holds by anything but C17, repeats by a loop statement, or keeps a value in a variable or an object that changes |
| Each algorithm is tested by its value, worked out by hand (REQ-VERIFY-004) | A module that carries the right name and computes something else |

The self-test of the compliance script plants, one for one, a flow built with
Effect's generator, a flow with a loop statement, a flow that changes a value
after its declaration, a flow that imports C4, and a flow with each of the
three spellings of section 6 of the calculus page: `x .pipe (1)`,
`x["pipe"](1)` and `Array.prototype.push.call(xs, 1)`. Each is refused.

What these do not catch: a module that names the right entry, passes its
tests and still does more than the entry says, and what section 6 of the
calculus page leaves to the evaluation of the code. These are left to the
evaluation of the code, by a session that did not write it.

## Not on this page

- The method's graph written out as data.
- Where files are kept, when commits are made, and the format of a ticket's
  name.
- The exact module names of Effect version 4. They are fixed when the release
  is pinned, from its documentation.
