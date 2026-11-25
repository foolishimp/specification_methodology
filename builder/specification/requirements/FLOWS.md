# The product's process flows

**Family**: REQ-FLOW-*
**Status**: Active
**Category**: Capability

Each requirement here is one flow: what happens, in what order, and how it
ends. A flow uses the [algorithms](ALGORITHMS.md) to decide, and has effects.
REQ-FLOW-001 lists every effect a flow may have. A flow has no other.

### REQ-FLOW-001 The effects

| Effect | Who | What |
|---|---|---|
| Write an asset | A working session | The assets its vector writes and the `.gitignore` at the top of the workspace's folder; for the first vector's session, the triage and the term in the branch's ticket. Anything else that differs when it is over is put to the user (REQ-ALG-008) |
| Write a verdict | An evaluating session | Its findings and its verdict, where the vector declares |
| Write the set-up files | The framework | What REQ-FLOW-002 lists, once. Afterwards, at the user's command, the record of the release that builds the product (REQ-FLOW-010) |
| Start and end a session | The framework | It starts one with its brief, and ends every process it knows to be of it (below), when REQ-FLOW-003 and REQ-FLOW-005 say |
| Write its own files | The framework | What its checks found; and the identities taken at a session's start, with the commit main is on then, or standing in for them, as identities, with each yes the user gave on what changed, until its step's result is committed (REQ-ALG-008, REQ-FLOW-003), the identities and each yes in git's own directory (below) |
| Write its part of a ticket | The framework | In the ticket, when it is pulled, the branch it left; in the branch's ticket, the checklist, the resolutions, the rulings and the rulings on what changed (REQ-FLOW-004). It only adds to that part |
| Keep what a session printed | The framework | When a session returns or fails, what it printed, or why it could not be started, as one of its own files: a file for each session, which the session's entry in the event log names |
| Move a ticket | The framework | From lane to lane. It also writes the simplest ticket, and names a ticket |
| Open a branch | The framework | For a ticket it pulls: the ticket's branch, made from the commit that moves the ticket to the active lane, and the folder put on it. For a ticket it takes up (REQ-FLOW-003, step 1): the folder put on its branch and, in a clone, a local branch made from a remote one. It makes no checkout and prunes none |
| Commit | The framework | Files under the workspace's folder alone, on the branch the folder is on. On a ticket's branch: the result of each step, with the files the user said yes to (REQ-FLOW-006), each answer, what a line of its part of the ticket names, before the line names it, and the move to the done lane. On main: the move to the active lane, with the branch the ticket leaves. When a run starts: what the user left uncommitted in the folder, once it is told from what a session left (REQ-FLOW-003, step 1); where the identities that tell it are missing, nothing is committed as the user's change by hand |
| Merge | The framework | Main into a ticket's branch, in the folder; and a ticket's branch into main, which moves main and puts the folder on it, and writes no file (REQ-FLOW-008) |
| Add to the event log | The framework | One entry (REQ-FLOW-007) |
| Hold | The framework | While a run works on a ticket no second run takes that ticket. A run or an answer refused for a hold names the hold's file and the process the hold names. The hold's file lies in git's own directory (below) |
| Wait | The framework | The run ends as waiting for the user: for an answer, or for the user's ruling on what changed while a session worked (REQ-FLOW-006) |
| Fail | A session | It cannot be started, stops without returning, or runs longer than allowed. It may be tried again |

The processes of a session are the agent's own process and every process
started from it, in whatever process group or session of processes each then
is. The framework ends only a process it knows to be of the session. It reads
which processes are alive from the system's table of processes, and it knows
a process to be of the session in one of three ways:

- by its parent: the process that started it is alive, and is one the
  framework knows to be of the session. The agent's own process is the first
  it knows;
- by its group: it is in a process group with a process the framework knows
  to be of the session, or in a group that such a process led. The framework
  starts the agent's own process as the leader of a session of processes of
  its own, so such a group holds no process that is not of the session;
- by its mark: the framework starts the agent with a mark in its environment,
  which every process started from it inherits, and the environment the
  system shows for the process holds that mark.

A process it has once known to be of the session it knows until that process
has ended.

It reads the table of processes with `ps`. Where it cannot, each refusal and
each cut-off for that says in one sentence that `ps` was not found or could not
be read, and what to install, and names no process where it found none
(REQ-FLOW-003, step 1, REQ-FLOW-005 and REQ-FLOW-006).

The system does not show the environment of every process. On macOS it shows
none for the system's own programs, a shell among them. So there is a process
the framework cannot place: one that started after the session did, has no
parent left alive, is of the session in none of the three ways, shows no
environment, and has its current folder in the workspace's folder, where the
session works. Of such a process the framework cannot tell whether it is of
the session: a job of the user's own that fits all of this is one too. It
does not end it. It names it to the user, by its number, when it started and
its command, and goes no further on the ticket (REQ-FLOW-005).

One kind of process of a session the framework does not find: a process that
has left its parent, is in no group with a process the framework knows, shows
an environment without the mark, wherever its current folder is, or shows no
environment and has its current folder outside the workspace's folder.
Nothing the system gives a program without privileges finds it, and the
framework cannot tell it from a job of the user's own. What it writes in the
folder before its step is settled, by the comparison at the session's end and
the user's ruling where one is asked (REQ-FLOW-005, step 3), is put to the
user; what it writes after that is taken at the next run as the user's change
by hand (REQ-FLOW-003, step 1).

A ticket has three parts, and each has one writer. The user's words are the
user's. The triage and the term are the first vector's session's. The branch
it left, the checklist, the resolutions, the rulings and the rulings on what
changed are the framework's part. The
framework writes no line of the first two, and no session writes the third
(REQ-ALG-008). The user may change any part by hand (REQ-FLOW-004), and the
framework reads its part as it stands.

The tickets, and the resolutions in them, are under git: a ticket travels
with its branch and reaches main by its merge. What the checks found, what
the sessions printed and the event log are in the workspace and outside the
history. A run that ends after a session failed names where what that session
printed is kept.

The hold, and the identities taken at a session's start with each yes the
user gave on what changed, lie apart from the framework's other files: in a
folder of its own under git's own directory for the workspace's folder, the
one `git rev-parse --absolute-git-dir` gives there, which git's commands that
clean the folder or stash what it holds do not reach. Each workspace keeps its
own folder there, so two products in one repository do not read each other's.
They are the framework's notes, and no proof or evidence of the work. The
framework's other files stay in the workspace, where git ignores them, the
packets and the note of a ticket the user wrote with the product's command
among them. The comparison (REQ-ALG-008) needs none of them: where a session
removes any of them, their loss may lead to a question to the user, never
to a commit with none. That holds for the comparison and for nothing else:
what a cleaning of the folder costs the user is said below.

A ticket is built in the workspace's own folder, the folder the user named,
on a branch of its own: there is no second folder. The branch the folder is
on when the ticket is pulled is main for that ticket until it is merged. The
ticket records its name (REQ-FLOW-004), and the framework reads it from the
ticket, and never again from the folder. Where no ticket is active, main is
the branch the folder is on. A ticket is active while it lies in the active
lane of the branch it left, and one that records none, as one an earlier
release pulled, while it lies in the active lane of the branch the folder is
on; the framework finds it by the branches it made for tickets, whichever
branch the folder is on. While a ticket is active, the folder stays on its
branch, so what the user changes in the folder meanwhile is on that branch,
and reaches main when the ticket is merged. A command that writes in the
workspace is then refused unless the folder is on the ticket's branch, save
where a run takes that branch up (REQ-FLOW-003, step 1), and the refusal
names both branches; `show` still answers, and says the same (REQ-ALG-012).

Since a ticket is built in the workspace's own folder, a session works among
the user's own files that git ignores there: local settings, dependencies,
what a build left. A session can read them, and what it removes of them is
removed; the framework, which compares only what git does not ignore
(REQ-ALG-008), names nothing. A check runs in the folder as it is, with the
files git ignores there, so what passes in the user's folder may rest on one
of them that no commit holds. The event log lies among them too: a cleaning
of the folder removes it, and the next run starts a new one (REQ-FLOW-003).

The workspace may lie inside a larger git repository, below its top
folder (REQ-FLOW-002). It is still one workspace: that folder. Each file the
framework writes, each commit it makes but a ticket's merge, and each
identity it reads concern only files under it. A ticket's branch and main are
the repository's, since git has no other, and the repository's folder has one
branch checked out: whatever is committed there while a ticket is active, by
the user or by anyone else who works in it, is on the ticket's branch, and
the ticket's merge brings it into main (REQ-FLOW-008). So two products in one
repository cannot each hold an active ticket at once (REQ-FLOW-003, step 1).
The framework leaves every other file of the repository as it is, and what
the user has not committed elsewhere in it, save what the user has staged
there when a run completes a merge (REQ-FLOW-008, step 3), and changes none
of the repository's other branches. A product in a repository of its own is the
case where the folder is the repository's top.

Before and after each session, the framework also notes the repository's
branches, tags and stash, each by its name and the commit it is on, but for
the ticket's own branch, on which a session may commit its step's work
(REQ-ALG-008). Inside a larger repository, it also notes each file outside
the workspace's folder that git lists as changed or untracked, with whether
it is there, its size and its time of change. It reads the content of no
file there. What differs, but for what the framework itself did in that
time, the run names in its words, saying that it changed while the session
worked. It names a file outside the folder by what happened to it: added
where it was not there and is, removed where it was there and is not, and
changed where it is there both times and is not as it was; never by whether
it entered or left git's list alone. A file the user edits there is changed,
and one the user only commits is named as committed (below). Where
more things differ outside the workspace's folder or among the branches,
tags and stash than REQ-PARAM-001 lets a run name, the run names that many
and says how many there are. Inside a larger repository, the run also
names, in the same place, each file outside the workspace's folder that
differs between the commit the folder was on when the session started and
the commit it is on when the session is over, as committed while the
session worked, by what happened to it: added, changed or removed. It says
that it may have been the session or the user, that none of it holds the
ticket, and that the ticket's merge takes what was committed there into the
branch the ticket left (REQ-FLOW-008). Of those files it names at most as
many as REQ-PARAM-001 lets a run name, says how many there are, and reads
the content of none. It also names there each file outside the workspace's
folder that differs between the commit main was on when the session started
(REQ-ALG-008) and the commit main is on when the session is over, as
committed on main while the session worked, by what happened to it: added,
changed or removed. Of those it names at most as many as REQ-PARAM-001 lets a
run name, says how many there are, and reads the content of none; it asks
nothing on them, and none of them holds the ticket. Where
git cannot compare two such commits, the run says in the same place that it
cannot tell what was committed outside the folder while the session worked.
Main is named among the branches as any other. Where a file of the
workspace's folder differs between those two commits of main, that file is
put to the user (REQ-ALG-008), and the run's words do not say of main that it
does not hold the ticket. None of the rest holds the ticket: other work goes
on in the repository, and no commit the framework makes but a ticket's merge
takes in a file outside the folder. The note is held by the run alone, in no file:
after a run cut off while its session worked, the next run says that it
cannot tell what changed among the branches, tags and stash, nor, inside a
larger repository, outside the workspace's folder.

Laws:

- The framework never reverts, resets or rewrites anything, puts no file back,
  deletes no branch and sends the history nowhere. What the agent or the user
  does with the history is theirs: the framework works from the workspace as
  it then is.
- The framework adds to main in three ways only: the move of a ticket to the
  active lane, what the user left uncommitted in the folder while no ticket
  is active, the record of the release among it, and the merge of a ticket on
  whose branch `done` said yes.
- The framework keeps nothing outside the workspace but the hold and the
  identities, in git's own directory (above). Inside a larger
  repository, git keeps the history and the branches where it keeps them for
  the whole repository.
- The framework makes no copy of the workspace or of any part of it, and no
  second folder: it makes no checkout and prunes none. A checkout an earlier
  release made is the user's to remove (REQ-INTERFACE-003). A branch is made
  by git and by nothing else, and work moves between a branch and main only
  by a merge.
- Runs share nothing but the workspace, and the hold and the identities in
  git's own directory.
- Only a session uses a language model.
- Nothing a killed run leaves behind refuses the next run, save a process of
  that run's session that is still alive after the framework has tried to end
  it, a process the framework cannot place, or the folder left on a branch
  that is not the ticket's (REQ-FLOW-003). What changed while that session
  worked is put to the user.

Acceptance:

- With a stand-in agent that only writes fixed files, a run completes with no
  call to a language model.
- The user goes back to an earlier commit. The next run builds from the
  workspace as it is, and the event log has lost no entry.
- A session that undoes its own work with git, back to the commit it started
  from, does not stop the run.
- A session prints a line and fails, and the run ends. The run names where
  what that session printed is kept. The line is there, in the workspace, and
  is neither in the event log nor in the history.
- A session prints a line and fails, and the next session on the same vector,
  of the same kind, prints another. Each line is in a file of its own, and
  each session's entry in the event log names that session's file.
- While a run holds the ticket, a second run and an answer are each refused,
  and each refusal names the hold's file and the process the hold names.
- Scenario S13 ends as it should.
- After scenario S1, each verdict and each answer is a resolution in the
  ticket. No other file of the framework's holds one, or the content
  identities one was given on, and no file holds a record of a run's reading
  of a ticket or a question.
- A session changes a file of the workspace outside what its step writes:
  the framework makes no commit, on the ticket's branch or on main, that
  holds that change before the user says yes to it.
- In a repository of its own, while a session works, a tag and a branch are
  made and main is moved by a commit that changes no file: the run names the
  three and asks nothing on them.
- A ticket is built and merged: every session of it was started in the
  workspace's own folder, and the repository has no working tree it did not
  have before.
- The user has a working tree of their own of the repository, whose folder is
  away while a ticket is built and merged: when the folder is back, git still
  knows it as a working tree.
- Inside a larger repository, while a session works, the user changes a file
  outside the folder that git did not list, and commits a second that git
  listed as changed: the run names the first as changed, and the second as
  committed while the session worked.
- Inside a larger repository, the user has a changed file and an untracked
  file outside the folder, neither committed. A working session gives
  `git add -A` and `git commit`: the run names both as committed while the
  session worked, the first as changed and the second as added, and says
  that the ticket's merge takes them into the branch the ticket left.
- Inside a larger repository, a working session writes a file outside the
  folder and commits it: the run names it as added, as committed while the
  session worked.
- Inside a larger repository, a working session commits on main a file of
  the workspace's folder and a changed file of the user's outside the folder:
  the run waits for the user's ruling on the first, and names the second as
  committed on main while the session worked.
- Two products lie in one repository. While one holds an active ticket, a run
  of the other is refused and names the branch the folder is on.

From: intent, model, "in one workspace: the folder that holds the product
being built", and guard rails 1, 2, 4, 6 and 7; product definition, "The agent
writes the product's assets and the framework writes its own files", the term
"Ticket" and "There is one event log"; the owner, on 18 November 2026, "git,
no copies!"; the user, in tickets 261123-001543-eae1, 261123-021212-4e94,
261123-185201-a149, 261124-001024-40f8, 261124-091541-a64b,
261124-190535-753f, 261124-220448-c7ab, 261125-043021-2fed and
261125-083337-0fdf.

### REQ-FLOW-002 Set-up

The user names a workspace by its URI, a name for the product and a method
release. Set-up asks for nothing else.

Where the workspace lies inside a git repository whose top folder is above it,
set-up says that the product lies inside a larger repository, and names that
repository by its top folder (REQ-FLOW-001). Where that repository ignores the
workspace's folder, set-up is refused before it writes anything. It names the
repository, says that the repository ignores the folder, and says that the
user may set the product up in a folder the repository does not ignore, in a
folder that is in no repository, or in the top folder of one. A workspace that
is in no repository, is the top folder of one, or lies inside one that does
not ignore it, is set up. Set-up then:

1. puts the workspace under git, if it is in no repository;
2. installs the method release where the method keeps its releases, and
   verifies it;
3. writes the definition file the method requires: it selects the release by
   its exact identity, and names the places for the goals, the intent, the
   product definition, the requirements, the three ticket lanes and a build
   tenant, the folder that holds one build of the product;
4. writes the page that says how work on the product is done and accepted: by
   this product, under the governing graph;
5. writes the settings file: which LLM agent does each vector's work and each
   evaluation, and for each agent which fields of what it prints report its
   cost and its calls; and the record of the release that builds the product
   (REQ-FLOW-010). Its defaults work as they are;
6. puts the governing graph and its registry in the workspace. By default it
   is the method's graph, and the user may put another in its place;
7. writes the product's commands into the agent instruction files the
   definition file names: to write a ticket, start a run, give an answer, show where the work
   stands, list the registry and record the release that builds the product.
   It writes nothing else there;
8. where it finds a system with no specification, writes a first ticket: to
   write the intent and the product definition of what is there, for the user
   to accept;
9. commits what it wrote, and adds its events to the event log.

Laws:

- A file that was there before is not changed, moved or deleted. Two
  exceptions: set-up adds to an event log, and adds its own block to an agent
  instruction file. Where another file it would write exists, it reports that
  and does not overwrite it.
- Over an existing system, the definition file names the places where that
  system's code, tests and design already are, and the graph's nodes take
  their places from it (REQ-GRAPH-003).
- Run again on a workspace already set up, it changes nothing but the event
  log.
- It writes only in the workspace, apart from step 2 and what git keeps of its
  commit in a larger repository (REQ-FLOW-001).

Acceptance:

- The method's own verification of the definition file passes.
- Scenario S1 runs with the settings as set-up wrote them.
- An agent started in the workspace and asked in plain words to start a run
  does so with no other instruction.
- Scenarios S8 and S13 end as they should.
- Set-up in a folder that lies inside a larger git repository says so and
  names that repository. Every file of the repository outside the folder,
  what the user has not committed there and the repository's other branches
  are as they were.
- Set-up in a folder that a larger git repository ignores is refused, names
  that repository, and leaves the folder and the repository as they were.

From: product definition, "Set up"; intent, model, "in one workspace: the
folder that holds the product being built", guard rails 2 and 4 and outcome 5;
the user, in ticket 261123-001543-eae1.

### REQ-FLOW-003 A run

The user starts a run by naming the workspace, and may name a ticket. A run
works on one ticket, and goes on without the user until it ends.

1. Once git's version is read (REQ-INTERFACE-001), where no record of the
   release is there, or the record is not what is
   running, the run is refused (REQ-FLOW-010).
   Then a graph that is not `well_formed` is refused; where the graph or its
   registry is, the refusal names where the installed release keeps the
   method's own. Then the framework reads the table of processes, before it
   starts any session; where it cannot, it starts nothing, and the run is
   refused in the words REQ-FLOW-001 gives. Then, where it finds the hold a cut-off run left, or a
   process alive that it knows to be of a session on the ticket, the
   framework ends every process it knows to be of that session
   (REQ-FLOW-001), before anything else is done on that ticket. Where one of
   them is still alive after that, or it finds a process it cannot place that
   started after the cut-off run did, it starts nothing, and the run is
   refused and names each such process. Then, where a run was cut off while
   its session worked, the run says that it cannot tell what changed among
   the branches, tags and stash, nor, inside a larger repository, outside the
   workspace's folder (REQ-FLOW-001).

   Then, before anything is committed, the branch the folder is on is looked
   at (REQ-FLOW-001). Where a ticket is active and the folder is not on its
   branch, the run is refused and names both branches, but in two cases,
   where the run takes the ticket's branch up and puts the folder on it. In a
   clone, where the repository has the ticket's branch only as a remote
   branch, the run makes the local branch from it, and takes up the branch
   the ticket left in the same way; where the repository has no such branch
   at all, the run is refused and says so. It never begins the ticket again
   from main. And where the active ticket records no branch it left, as one
   an earlier release pulled, the run puts the folder on the ticket's branch
   and records there, in the ticket, the branch the folder was on as the one
   it left; where the folder is on the ticket's own branch already, the run
   is refused and says to put the folder on the branch the ticket left. Where
   git refuses to put the folder on a branch, the run is refused and names
   what git names.
   Where the ticket's branch is checked out in another working tree, such as
   a checkout an earlier release left, the refusal names that working tree
   and gives the command that removes it. Where no ticket is active and the
   folder is on a branch the framework made for a ticket, or on no branch, no
   ticket is made active: the run is refused, and names the branch or says
   that the folder is on none.

   Then, in the folder, what a session left is told from what the user left
   by the identities kept from that session's start and what its step writes
   (REQ-ALG-008), and by nothing else. Where a run was cut off while its
   session worked and that session's identities are missing, or where the
   identities kept from a session's start cannot be read, name a step the
   graph does not hold or name what git no longer holds, the identities
   of the commit the session started from stand in their place, read from
   the record kept at its start (REQ-ALG-008): so each file that differs from
   that commit, committed since or not committed, is put to the user. Where
   that record is gone, cannot be read or names a commit git does not hold,
   the identities of the commit the folder is on stand in, and each file not
   committed is put to the user. Where the framework keeps such identities,
   as after a run cut off while its session worked, it compares, with main
   as it is now, before main is taken in (step 3). Where a file differs, in
   the folder or on main (REQ-ALG-008), on which no yes was given, the run
   asks the user (REQ-FLOW-006), takes nothing of main in and ends as
   waiting. Otherwise what is not
   committed of what that step writes, and each file the user said yes to, is
   committed as that step's result, and the identities are let go. Then what
   is still not committed in the folder is the user's change by hand, and is
   committed as that.
2. `take_up` gives the ticket. None: the run is refused, and says which holds:
   a run already works on every active ticket (REQ-FLOW-001, "Hold"), the
   limit is reached, or there is nothing to build.
3. The framework holds the ticket, pulls it if it lies in the backlog
   (REQ-FLOW-004), and takes main into its branch (REQ-FLOW-008).
4. `next` gives the vector, on the ticket's branch. None: go to step 6.
5. One step is made on that vector (REQ-FLOW-005). Then step 4 again.
6. The ticket is merged (REQ-FLOW-008), and the run ends with the work done:
   where `next` gives none, no vector that takes part is open, so `done` says
   yes on the ticket's branch.

A run ends in exactly one of four ways:

1. the work is done: the ticket is merged into the branch it left, which the
   run names, with, inside a larger repository, each file outside the
   workspace's folder that the merge took in there (REQ-FLOW-008, step 2),
   and that branch is what its specification says;
2. it is waiting for the user's answer, or for the user's ruling on what
   changed while a session worked;
3. it has stopped, and states the vector and the reason: a check that could
   not be run, a vector that could not close, the folder found on a branch
   that is not the ticket's, a file git could not merge, a refusal to
   take main in or to merge after a step was made (REQ-FLOW-008), or a limit
   the user set;
4. it was refused before any step, and states why.

Laws:

- Where the framework cannot do what the graph declares, it stops and says so,
  and does nothing else in its place.
- Each ending is shown to the user in plain words, with what the user can do
  next.
- A run reads the workspace and not the event log. Where the log is missing it
  says so, and starts one. So it does, too, where the log it was adding to is
  gone when it next adds to it: it says once that the log was not found and
  that it starts a new one.
- A run is cut off, which is none of the four endings, in two cases. When it
  receives the interrupt, the terminate or the hang-up signal, it ends every
  process it knows to be of the session at work, where there is one
  (REQ-FLOW-001), and goes no further. And where its session is not over
  (REQ-FLOW-005), it says what it found and goes no further. A run that is
  cut off leaves its hold, and the next run on the ticket adds to the event
  log that it was cut off (REQ-FLOW-007).

Acceptance:

- A run started on the workspace scenario S1 leaves starts no session and is
  refused: there is nothing to build.
- Scenarios S2, S3 and S14 end as they should.
- While a ticket is active, the user puts the folder on a branch of their own
  and commits there: a run and an answer are each refused, name both
  branches, and start and commit nothing; `show` answers, and says the same.
  After the user has put the folder back, the next run goes on, and the
  ticket is merged into the branch it left, once, and into no other.
- A run is killed while its session works: the next run says that it cannot
  tell what changed among the branches, tags and stash. Inside a larger
  repository, it also says that it cannot tell what changed outside the
  workspace's folder.
- A run is killed while its session works, after the session has committed
  a file on main: the next run waits for the user's ruling and names the file
  as changed on main.
- A run is killed while its session works, after the session has written
  part of its asset and the user has changed a file the step does not write.
  The next run commits neither as the user's change by hand: it asks the user
  on the user's file alone, and after the user's yes commits both as that
  step's result. With that session's identities removed, the next run asks
  the user on both files, and commits neither as the user's change by hand.
- The working session of REQ-ALG-008's acceptance that gives `git clean -fdx`
  as its first act is still at work when the run receives the interrupt
  signal; and again when the run is killed. The next run ends the session's processes where
  any is alive, asks for the same ruling, and commits nothing as what the user
  changed by hand.
- A ruling on what changed is awaited. The user gives `git clean -fdX` and
  starts a run: the run asks again, naming the same files, and commits
  nothing.
- A session removes the event log while the run works. When the run next
  adds to it, it says, once, that the log was not found and that it starts a
  new one.
- In a clone of a workspace whose active ticket waits for the user's answer,
  and which has the ticket's branch only as a remote branch, a run makes the
  local branch from it, puts the folder on it and asks the same question. It
  starts no session to induct the ticket and makes no branch from main.
  Where the clone has no such branch at all, the run is refused and says so.
- With the folder on no branch, a run is refused, says so, and makes no
  ticket active.
- A checkout an earlier release left holds the active ticket's branch: the
  run is refused, names that checkout and gives the command that removes it.
  After the user has removed it, the next run goes on.
- Where `ps` cannot be started, a run is refused before any step, starts no
  session and commits nothing, and says in one sentence that `ps` was not
  found or could not be read, and what to install. An answer is then refused
  in the same words. Neither names a process.

From: product definition, "Build" and "Resume"; intent, guard rails 1 and 3
and outcomes 1 and 4; the user, in tickets 261123-185201-a149,
261124-001024-40f8, 261124-091541-a64b, 261124-190535-753f,
261124-220448-c7ab, 261125-014851-46cb, 261125-043021-2fed and
261125-083337-0fdf.

### REQ-FLOW-004 A ticket

A ticket is a work order: it says how the workspace is to be amended. The user
writes one in their own words, as a file in the backlog, in the folder
(REQ-FLOW-001). The three ticket lanes are a board: backlog, active and
done. The framework pulls from
the backlog, and never chooses what is put there. A ticket that appears in a
lane while a session works, other than by the product's command, is named to
the user with what changed then (REQ-ALG-008), and is not taken up as the
user's words until the user has ruled on it.

1. **Pull.** The framework records in the ticket the branch the folder is on,
   as the branch it leaves, moves the ticket to the active lane and commits
   both on that branch, its main. It makes the ticket's branch from that
   commit, or takes up the branch it already has, and puts the folder on it.
   Where git refuses that, the run is refused and names what git names, as
   REQ-FLOW-003 step 1 says. All work on the ticket is done in the
   workspace's own folder, on that branch.
2. **Induct.** The first vector for a ticket, which the graph declares, runs.
   Its session adds to the ticket the method's triage of the change and the
   term of graph functions that carries the work out (REQ-METHOD-006); or that
   the ticket cannot be inducted, and why. It changes none of the user's
   words, and nothing of the framework's part (REQ-FLOW-001).
3. **Confirm.** The user confirms the ticket as inducted (REQ-FLOW-006).
4. **Build.** The run builds by the confirmed term: the vectors it names, in
   its order, and no other (REQ-ALG-006). Where it reaches an induction entry
   of the term, the first vector runs for that entry's stretch alone, and the
   user confirms the term it writes in the entry's place (REQ-METHOD-006).
5. **Merge.** When `done` says yes on the ticket's branch, the ticket moves to
   the done lane on that branch, and the branch is merged into the branch it
   left (REQ-FLOW-008).

The simplest ticket skips steps 2 and 3: it names no change, so there is
nothing to settle, and it is built by the method's default term
(REQ-METHOD-006). The framework writes it in the backlog and pulls it. A user
who has changed an asset by hand starts a run, and that is the ticket.

A ticket is one file, and it is the only record of the ticket. Its name is
given by the product's command for a new ticket, or when it is pulled. Names
need no shared counter, so two tickets written on two branches do not take the
same name, and they sort by when the ticket was written.

As the work goes on, the framework adds to the ticket, in its part
(REQ-FLOW-001):

- **The branch it left**: when it is pulled, the name of the branch the
  folder is on, which is main for the ticket until it is merged.
- **The checklist** of what has been delivered: a line each time the work of a
  vector that takes part is delivered, with the commit that holds it. A
  vector that declares a decision by the user is delivered when the user is
  asked; any other, when it closes. The checklist also shows each binding of
  a session to a stretch, and its end (below), and where the work of a
  vector began (REQ-FLOW-005, step 1).
- **The resolutions**: each yes or no of an evaluation or of the user, at the
  vector it was given at, with the commit that holds what it was given on. An
  evaluation's names where its verdict and its findings are. The user's no
  holds the user's reason.
- **The rulings**: each ruling the user gives with an answer
  (REQ-FLOW-006). A ruling binds every later session of the ticket.
- **The rulings on what changed**: each yes or no the user gives on what
  changed while a session worked (REQ-FLOW-006), at the vector of that
  session's step. A yes names each file it was given on by its path, with the
  content identity the file then had. A file changed on main (REQ-ALG-008)
  it names apart from a file of the folder, with the identity main then gave
  it, by a name that begins neither `main:` nor `checkout:`: a name a ruling
  of an earlier release gave that begins so is read as the path that follows
  it, a file of the folder. Such a ruling is no resolution and binds no
  session.

Where what a line names is not yet committed, the framework commits it first;
the files a ruling on what changed names are the exception: they are
committed with the step (REQ-FLOW-003, step 1), and those changed on main
are taken in with main (REQ-FLOW-008).
The ticket names each finding, each difference and what a session printed by
its path, and holds none of them: the detail is in git. A session starts from
the ticket. Its brief names the ticket, and the rulings in it as binding on
the session (REQ-ALG-007).

What the user may do, at any time. The user puts a ticket back or withdraws
it on main: with the folder on the branch the ticket left, the user commits
the move there. The user edits an active ticket in the folder, on its
branch, or on main; a run under way on the ticket learns of an edit on main
when main is next taken in (REQ-FLOW-008):

- **Put a ticket back.** The user moves it to the backlog. It waits like any
  other. Its branch stays, and when it is pulled again the work goes on from
  there.
- **Withdraw a ticket.** The user deletes its file. No run takes it. Its
  branch stays as it is, and nothing of it reaches main.
- **Edit an active ticket.** Where the edit lies outside the framework's
  part, the confirmation no longer stands: the ticket is inducted again. An
  edit of the framework's part is read as it stands.
- **Say no at the confirmation, with a reason.** The ticket is inducted
  again, and the session's brief names the reason. Where a ticket cannot be
  inducted, the user edits it or withdraws it.

Where the user puts a ticket back, withdraws it or edits it on main while a
session's identities are kept (REQ-ALG-008), that commit is among what
changed while the session worked, as any other on main: the run asks the user
on each file it changed in the folder (REQ-FLOW-006), and main is taken in
only after the yes. What this flow and REQ-FLOW-008 say of the move or the
edit then holds. Done while no session's identities are kept, no question is
asked: an edit is taken in when main next is, and of a move, what this flow
says above holds.

To induct a ticket again is to hold the whole ticket, as it now is, to the
checks of its first induction, and to ask the user to confirm it as it then
is. The first vector's session runs where the user said no or the ticket does
not pass those checks; otherwise no session runs. A change to an active
ticket outside the framework's part, that the framework finds before it
starts a session, is the user's, and the ticket is inducted again; a change a
session makes is that session's work (REQ-METHOD-006).

Before it starts a session bound to a stretch, the framework adds the binding
to the checklist and commits it. The binding ends when the user is asked to
confirm the term the session wrote, or when the framework commits the user's
edit of the ticket from the folder (REQ-FLOW-003, step 1) or takes it in from
main; the checklist shows each. A change to the
ticket while the binding holds is that session's work, whether it returned,
failed or its run was cut off, and so is the ticket as the user was then
asked to confirm it. Any other change since the user's confirmation is the
user's, and so is a change taken in from main after the user's yes on what
changed (REQ-FLOW-006), though it was made while the binding held. Where the
session then runs on the user's change, the question says so: the user's
edit is never overwritten without the user being told.

Laws:

- One ticket is active at a time, until REQ-FLOW-009 is in force.
- The lane a ticket lies in is its only status; what it waits on is worked
  out when asked (REQ-ALG-012). Its checklist opens and closes no vector
  (REQ-ALG-005).
- A ticket enters only by a vector that declares an evaluation or a decision
  by the user.
- A branch moves no ticket but its own.
- Going back to a node that the ticket's node depends on is the user's
  decision alone.
- Under a graph that declares no first vector for a ticket, only the simplest
  ticket is taken up, and the framework says so.
- The framework is never given a list of what changed.
- A line of the framework's part that changed while a session worked is never
  read as the user's answer, whatever the user rules on what changed.

Acceptance:

- Scenario S1 starts from a ticket of one paragraph and nothing else.
- After step 2, every word the user wrote is still in the ticket, unchanged.
- Scenarios S4, S9 and S12 end as they should.
- A session bound to a stretch writes the ticket and then fails, or its run is
  cut off before what it wrote is judged: the next reading holds what it left
  to the check of the stretch's term, as that session's work.
- A ticket is confirmed and merged, and a new ticket is then written and
  pulled: the first question on the new ticket does not say that the ticket
  changed after the user confirmed it.
- After each step, the ticket holds the lines of the checklist and the
  resolutions the step gave, each with its commit, and no finding, no
  difference and no line a session printed.
- The framework adds lines to its part of a confirmed ticket: the
  confirmation still stands, and the user is not asked to confirm it again.
- A session adds a ticket to the backlog: the run names it as added and
  waits for the user's ruling, and no run takes it up before the user has
  ruled.
- A session writes lines of the framework's part into the ticket, one of them
  a yes of the user: the run names the ticket and waits for the user's
  ruling. After the user's yes, that line is not read as the user's answer,
  and the user is asked at its vector when the run reaches it.
- A ticket is pulled: it names the branch the folder was on as the branch it
  left, and the folder is then on the ticket's branch, made from the commit
  that moved the ticket to the active lane on that branch.
- While a session works, the user edits the active ticket on main: the run
  waits for the user's ruling and names the ticket as changed on main. After
  the yes, main is taken in and the ticket is inducted again.

From: product definition, "Ask" and the term "Ticket"; the user, in tickets
261122-232152-1198, 261123-021212-4e94, 261123-100659-a0d5,
261124-001024-40f8, 261124-091541-a64b and 261125-083337-0fdf.

### REQ-FLOW-005 A step

One attempt at one vector.

1. Where the ticket's confirmed term names the vector, the ticket holds no
   resolution at it and its checklist shows none of its work begun or
   delivered, the framework adds to the checklist that the vector's work
   began, commits that, and starts the working session (step 2). Otherwise,
   where the vector's asset is already there, `passes` is asked first, and
   where the vector declares an evaluation whose verdict no longer stands, or
   says that it cannot judge, it is made again (step 4). A working session follows only where a check says
   no, a verdict says no, the user's answer says no, the ticket is `changed`,
   or an asset is `changed` and the vector declares no evaluation. An answer
   that is missing is not a lack: step 6 asks for it.
2. A working session is started in the workspace's own folder, on the
   ticket's branch, with its `brief`.
   It is a new session, of the agent the settings file names for this vector.
   Where the vector's graph function is not a single session, its inner terms
   are run in its place: `next` is asked among them until none is open.
3. When the session is over (below), however it ended, the framework looks
   at the branch the folder is on: where it is not the ticket's, the run
   names both branches and ends as stopped, and goes no further on the ticket
   until the user has put the folder back on it. Then `trespass` is
   asked. Where the identities from the session's start are missing, those
   of the commit the session started from stand in for them (REQ-ALG-008), so
   each file that differs from that commit, committed since or not committed,
   is returned, what the step writes among them. Where it returns any file,
   in the folder or changed on main, the run asks the user to rule on what
   changed (REQ-FLOW-006), takes nothing of main in and ends as waiting. The
   framework puts nothing back. The run also names what differs among the
   branches, tags and stash and, inside a larger repository, outside the
   workspace's folder, changed, or committed on the ticket's branch or on
   main, while the session worked (REQ-FLOW-001), which, save main where a
   file of the folder differs there, does not hold the ticket.
4. Where the vector declares an evaluation, its asset is there and every
   check of the assets it writes says yes, it is made in a new session, of
   the agent the settings file names for it, with its `brief`. Its verdict says yes, no, or that it cannot judge, with why in
   its findings. When that session is over, the folder's branch is looked at
   and `trespass` asked, as in step 3. Where `trespass` returns any file, the
   verdict is not read: after the user's ruling, the evaluation is made again
   by a new session. Otherwise the
   framework reads the verdict. A yes or a no it adds to the ticket as the
   evaluation's resolution, with the commit that holds what it was given on
   (REQ-FLOW-004). A verdict that it cannot judge is no resolution.
5. `passes` is asked, and the framework writes what the checks found.
6. Where the vector declares a decision by the user, no answer stands and
   every other check passes, the user is asked (REQ-FLOW-006).
7. The result of the step is committed, whether or not the vector closed,
   with the files the user said yes to, and not while the user's ruling on
   what changed is awaited; and
   the framework adds to the event log.

Where the step does not close:

- A check could not be run. The run ends as stopped.
- The evaluation says it cannot judge. The run ends as stopped, and names
  where its findings are.
- A check said no, so no evaluation was made. The working session is made
  again in the same attempt, over the workspace as it stands, while
  `progress` says yes.
- A session failed. It is made again in the same attempt, unless the session
  before it on the vector in this run failed too.
- The evaluation said no. That is one attempt, and the step is made again,
  over the workspace as it stands, while the attempts the graph allows are
  not used up. A new run counts afresh.
- So, with no limit set on the run, sessions that reach no evaluation still
  end: fewer checks must fail each time, and no two fail in a row.
- When no further attempt is made, the run ends as stopped. It names the
  vector, the checks that said no and where what they found is kept and, where
  a working session worked in the last attempt, where what it printed is kept.
  The ticket stays active. The user may edit it to give direction, start a
  run again, or withdraw it (REQ-FLOW-004).

Laws:

- A session is over when the framework has ended every process it knows to
  be of it, and finds none it cannot place (REQ-FLOW-001). The framework ends
  them at the session's return, which is the end of the agent's own process,
  and when its time is over (REQ-PARAM-003).
- Where a process it knows to be of the session is still alive after the
  framework has tried to end it, or it finds a process it cannot place, the
  session is not over. The framework then commits nothing, judges nothing
  and starts nothing on the ticket. The run names each such process and says
  what the user can do: end it, then start a run again. The run is cut off
  (REQ-FLOW-003).
- Where the framework cannot read the table of processes when a session would
  be over, the session is not over either, and the run is cut off: it says so
  in the words REQ-FLOW-001 gives, and names no process where it found none.
- While a process the framework knows to be of a session on a ticket is
  alive, or one it cannot place, the framework starts no session on that
  ticket, judges nothing on it and commits nothing on it.
- Until the user has ruled on what changed while a session worked
  (REQ-FLOW-006), the framework judges nothing on the ticket, commits nothing
  on it, starts no session on it and merges nothing: it reads no verdict, runs
  no check, does not commit what the step itself wrote and takes nothing of
  main into the ticket's branch.
- Nothing passes from one session to the next except the workspace.
- A session works in the workspace's own folder, reached by its URI, never in
  a copy of it or in a second folder. The framework sets no limit on how a
  session reaches it.
- A change leaves every asset it does not concern exactly as it was.
- Files a session wrote in a step that did not close, or that was interrupted,
  stay as they are. The next attempt and the next run judge them as they stand.
- Changing which agent does a vector needs no change to the graph, the
  registry or the framework.

Acceptance:

- On a built product, under a ticket whose term is the requirements and then
  the build, the first step on each starts its working session: the user is
  not asked and no evaluation is made before it.
- A step is interrupted after its asset was complete. The next run starts no
  working session on that vector.
- A requirement changed by hand that the design already meets starts no
  working session on the design.
- Two working sessions in a row that fail the same checks end the run as
  stopped, and neither counts as an attempt.
- With one attempt allowed, a working session leaves a check failing and the
  next leaves none: the evaluation is made.
- An evaluation says no as many times as the graph allows attempts: the run
  ends as stopped.
- With no limit set on the run, an agent that cannot be started: the run ends
  as stopped at its second failure.
- An evaluating session that changes the asset it judges: the run names the
  asset's files, reads no verdict and waits for the user's ruling. After it,
  the evaluation is made again by a new session.
- An evaluating session adds a line to a file that is part of no asset, such
  as the agent instruction file: the run names that file and waits for the
  user's ruling, and nothing of the step is committed or merged before the
  user has ruled.
- An evaluating session commits a file on main and returns with the folder
  on the ticket's branch: the run names the file as changed on main, reads no
  verdict and waits for the user's ruling.
- A working session commits on main files its step does not write and
  returns with the folder on main: the run stops as for any other branch.
  After the user puts the folder back on the ticket's branch, the next run
  waits for the user's ruling, naming those files as changed on main, and
  takes nothing of main in.
- A working session writes nothing and prints what change it needs. No
  evaluating session is started, and the run that stops names where what it
  printed is kept.
- A requirement is changed by hand. The next run asks the user to accept it
  before any session rewrites it.
- An evaluating session says it cannot judge. The run stops and names where
  its findings are. The next run makes the evaluation again.
- A check of an asset the vector writes says no, and the asset is there. No
  evaluating session is started, and the next working session's packet names
  what the checks found.
- An evaluation says yes or no: the ticket holds that resolution, and git
  gives, under the commit it names, the content the evaluation judged.
- Scenarios S5, S7, S10 and S14 end as they should.

From: product definition, the terms "Step", "Session" and "Evaluation", and
"Change"; intent, guard rails 1, 2, 3 and 7; the user, in tickets
261123-100659-a0d5, 261123-185201-a149, 261124-001024-40f8,
261124-091541-a64b, 261124-190535-753f, 261124-220448-c7ab,
261125-014851-46cb, 261125-043021-2fed and 261125-083337-0fdf.

### REQ-FLOW-006 A question and its answer

1. The framework asks the user, and the run ends as waiting. The question says
   in plain words what is being decided, what it rests on and what follows from
   each answer. For each file of the nodes the vector writes that changed
   since the content last accepted, as main holds it (REQ-ALG-007), it says
   how many of its lines changed and how many remain as they were, and it
   says that every other file is as it was; where main holds none of a node,
   it says that the node is new. It is given in the run's ending, and `stands` gives what is
   asked (REQ-ALG-012). No file holds it.
   The question on what changed while a session worked (REQ-ALG-008) names
   each file by its path in the workspace, and whether it was added, changed
   or removed. Each file changed on main it names apart from the files that
   differ in the folder, as changed on main, the branch the ticket left, by
   its path in the workspace and whether it was added, changed or removed
   there. It says that each changed
   while the session worked and that it may have been the session or the
   user, and never that the session changed it. Where the identities of a
   commit stand in for those of the
   session's start (REQ-ALG-008), it says in one sentence that those are
   missing and that it therefore asks about every file that differs from the
   commit the session started from; where the commit the folder is on stands
   in, the sentence says instead that it asks about every file not committed. It
   says what each answer means. A yes: each file that then
   differs in the folder stands as it then is; the framework commits them
   with the step, and whatever rests on them is judged or accepted again, as
   after any change by hand. For the files changed on main, main stands as it
   then is, and the run takes it into the ticket's branch (REQ-FLOW-008); the
   framework commits none of them with the step. A no: the user puts back
   what is not to stand, in the folder, and puts main back for the files
   changed there; the framework takes nothing of main in. The
   framework puts nothing back, in either case. The next run compares again,
   and asks again while a file differs on which no yes was given.
2. The user answers with the product's command for that, and starts a run
   again. With the answer, the user may give a ruling.
3. The framework adds the answer to the ticket as the user's resolution, with
   the ruling where there is one, and commits it (REQ-FLOW-004). The answer is
   for the vector whose work the checklist shows delivered for the user's
   decision with no answer of the user after it, and it is given on the
   commit that delivery names. Where a file differs from the identities kept
   from a session's start, in the folder or on main (REQ-ALG-008), on which
   no yes was given, the answer is instead the user's ruling on what changed:
   it is for that session's step, and a yes is given on each file that then
   differs, as it then is, and on each file changed on main, as main then
   holds it. The framework
   adds it to the ticket as a ruling on what changed and commits that line,
   and nothing it is given on.

Laws:

- The answer runs no check, and reads neither the event log nor any record
  but the ticket, and the hold and the identities kept from a session's start
  where REQ-FLOW-001 says they lie. Where a run's start would put the
  commit's identities in place of a session's (REQ-FLOW-003, step 1), the
  answer is refused, and says that a run asks the user on every file not
  committed. While a run holds the ticket (REQ-FLOW-001,
  "Hold"), the answer is refused, and so it is while the folder is not on
  the ticket's branch (REQ-FLOW-001). It is refused too while a process the
  framework knows to be of a session on the ticket is alive, or one it cannot
  place: the answer looks as the start of a run does (REQ-FLOW-003, step 1),
  ends no process, and names each one it finds. Where it cannot read the
  table of processes, it is refused in the words REQ-FLOW-001 gives, and
  names no process. Where no file differs on
  which a ruling on what changed is wanted, the answer is for a delivery. It
  is then refused where the ticket shows nothing delivered for an answer, or
  the content the answer would stand for (REQ-ALG-004) differs now from that
  commit's, and says that a run asks again.
- When that content changes, the answer no longer stands, and the user is
  asked again. So too where main, taken into the ticket's branch, changed a
  file of that node since the answer, whatever the file then holds
  (REQ-ALG-004).
- An answer of no comes with the user's reason, and the brief of the next
  attempt names it.
- A ruling binds as REQ-FLOW-004 says. It changes no resolution.
- A session's answer is never taken in place of the user's.

Acceptance:

- A run does not pass a vector that declares a decision unless the workspace
  holds the user's answer.
- In scenario S1, a person who has not read the framework's source answers each
  question from the question and the asset it names.
- An answer runs no check, the tests' command among them.
- The asset asked on is changed after the question and before the answer: the
  answer is refused, and the next run asks again.
- A ruling given with an answer is named in the brief of every later session
  on the ticket.
- A ticket changes one line of a requirements file of 100 lines: the question
  on the requirements says of that file that 1 line changed and 99 remain as
  they were, and that every other file is as it was. In scenario S1, the
  question on the specification says that each of its nodes is new.
- While a session works, the user changes a file outside what the step
  writes: the run names it in words that say it changed while the session
  worked and that it may have been the session or the user, and waits for
  the user's ruling.
- The user says yes to what changed and starts a run: the run commits each
  file named, as it was at the yes, with the step, asks nothing more on them,
  and judges or asks again on what rests on them, as after a change by hand.
- The user says no, puts one file back and leaves another as it is: the next
  run commits nothing on the ticket, names the other alone and waits again.
- The user says no to files changed on main and puts main back to the commit
  it was on when the session started: the next run asks nothing on what
  changed, the ticket is built to its end, and main holds none of those
  files. The same where the user undoes them with `git revert` on main.
- The user says no to files changed on main and leaves main as it is: the
  next run waits again and takes nothing of main in.
- The user says yes to files changed on main, and main is then moved again by
  a commit that changes one of them: the next run asks again, and names that
  file.

From: product definition, the term "User" and the term "Ticket"; intent,
purpose and guard rails 1, 2, 3 and 4; the user, in tickets 261120-9636,
261123-021212-4e94, 261123-100659-a0d5, 261123-185201-a149,
261124-001024-40f8, 261124-091541-a64b, 261124-190535-753f,
261124-220448-c7ab, 261125-014851-46cb and 261125-083337-0fdf.

### REQ-FLOW-007 The event log

Each governed product has one event log, in the workspace. Every run adds to
it, whichever ticket it works on. The framework adds an entry for:

- set-up; a ticket written; the release recorded (REQ-FLOW-010);
- a ticket pulled, with the branch it left and its own; a ticket merged,
  with the branch it was merged into; main taken into a ticket's branch, with
  main's name and the assets that collided;
- a run started, with the release in force, and how it ended;
- a new log started, where the log a run was adding to is gone when it next
  adds to it (REQ-FLOW-003), with the release in force;
- a run cut off, which the next run on the ticket adds where it finds the
  hold the cut-off run left. A session that run started and that neither
  returned nor failed was cut off with it: its processes were ended by that
  run on a signal or by the next run, or the session was not over
  (REQ-FLOW-003);
- a session started, by vector, kind and agent, with the agent's command as
  it was run and the commit the session starts from;
- a session returned or failed, with how long it took, the file of its own
  that holds what it printed and, where the agent reports them, its cost and
  the number of its calls;
- the processes of a session ended, each time the framework ends them, with
  how many;
- a check run, by name, with whether it passed, said no or could not be run,
  and how long it took;
- a verdict read, with what it says and where its findings are;
- a vector closed or left open; the user asked; the user asked on what
  changed while a session worked, with how many files were named, and not
  which;
- an answer written, with what it says, the ticket that holds it and, for a
  no, that the reason is there;
- a commit made, with the commit and what it holds: the result of a step, by
  vector, an answer or a move on the board.

Laws:

- Entries are only added. None is changed or removed, and one the framework
  cannot read is left in place.
- The framework takes no decision from the log. It is there for a person to
  see what happened.
- An entry names nodes, vectors, checks, files and commits by name, path,
  content identity or the commit's identity. It holds no content of an asset,
  nothing a check found and none of a session's output other than the cost
  and the calls reported and what a verdict says. Which fields of an agent's
  output report the cost and the calls is a setting of that agent
  (REQ-FLOW-002). The agent's command it holds is the command as the settings
  give it and the framework ran it.
- Between the start of its session and the moment that session is over
  (REQ-FLOW-005), a run adds only how many of the session's processes it
  ended, and that a new log was started where the log is gone. Where the
  session is not over, it adds nothing after that.
- The framework keeps no other record of its own events.

Acceptance:

- From the log alone, a person can say which steps ran, in what order, how
  each ended and why each vector was closed or left open.
- From the log and the workspace, a person can say for each run the release
  in force; for each session the agent's command, the commit it started from,
  where what it printed is kept and the commit that holds its step's result;
  how long each check took; and for each verdict and answer what it said and
  where its findings or its reason are.
- After scenario S2, the log holds that the interrupted run was cut off,
  added by the run after it.
- After each case of scenario S14, the log holds each time the framework
  ended processes of the session, with how many.
- After any number of runs, the earlier content of the log is unchanged at the
  start of the later log.
- After scenario S7, the log holds that the user was asked on what changed,
  with how many files were named, and names none of them.
- A session removes the event log while the run works: the new log's first
  entry says that a new log was started, with the release in force.

From: intent, model and guard rails 5 and 6; product definition, "There is
one event log" and "the log lacks an event or a detail"; the user, in tickets
261123-021212-4e94, 261123-185201-a149, 261124-001024-40f8,
261124-091541-a64b and 261124-190535-753f.

### REQ-FLOW-008 Merging a ticket's work

Main is the branch the ticket left (REQ-FLOW-001).

1. Main is taken into the ticket's branch, in the folder, at the start of
   each run on the ticket, and again where main has moved by the time `done`
   says yes, wherever in the repository it moved. While a session's
   identities are kept, the comparison with main comes first (REQ-FLOW-003,
   step 1): where a file of the folder differs on main (REQ-ALG-008), main is
   taken in only once the user has said yes to each such file as main then
   holds it (REQ-FLOW-006). What main gains while no session's identities are
   kept, a commit of the user's between two runs among it, is taken in with
   no question. Where the ticket then no
   longer lies in the active lane, the run ends as stopped and says so.
2. When `done` says yes on a branch that holds all of main, the ticket moves
   to the done lane on the branch, and the branch is merged into main. Main
   is then an ancestor of the branch, so the merged content is the branch's
   own. The framework makes the merge commit from the branch's whole tree,
   with main and the branch as its parents, moves main to it and puts the
   folder on main, with git's `commit-tree`, `update-ref` and `symbolic-ref`
   alone. No file is written and no file's time changes, and what the user
   has uncommitted, staged or untracked is as it was. Inside a larger
   repository, the words that say the ticket is done (REQ-FLOW-003) then name
   each file outside the workspace's folder that the merge took into main:
   each that differs between the commit main was on before the merge and the
   merge's commit. They are read from those two commits, and not from what
   was noted after each session, so a file committed on the ticket's branch
   while no session was at work is named too. The run names at most as many
   as REQ-PARAM-001 lets a run name, says how many there are, and reads the
   content of none. Where the merge took in none, and at the top of a
   repository, those words name no file outside the folder.
3. Where git cannot merge a file by itself as main is taken in, the run ends
   as stopped and names the file. The user decides between the two, in the
   folder. The next run then completes that merge as `git commit` would, from
   the repository's own index: a file the user has staged elsewhere in the
   repository at that time is in that commit.

Where git refuses to take main in because the user has uncommitted or
untracked work in a file main changed or added, the run names those files
and takes nothing in. Before main is taken in, where a file the take-in adds
is there already in the repository's folder, as a file or as a folder, or a
folder on the way to it is there as a file, inside the workspace's folder or
outside it, the run names each such path and takes nothing in, and the
user's files are as they were: where git ignores such a file, git's own
take-in would write over it with no word, and none of it is in a commit. Where the branch the ticket left is checked out in
another working tree of the repository when the ticket is to be merged, the
run names that working tree and merges nothing. In each case the run is
refused where it has made no step, and stops otherwise (REQ-FLOW-003).

Laws:

- Ticket files do not collide: each has a name of its own, and a branch moves
  no ticket but its own.
- What a done ticket changed can be read from the history.
- A ticket is merged into the branch it left, and into no other.
- The merge brings into main what was committed on the ticket's branch, and
  nothing else: inside a larger repository, that is what was committed on it
  anywhere in the repository (REQ-FLOW-001), and the run names what it took
  in outside the workspace's folder (step 2). The framework's other commits
  take in files of the workspace's folder alone.
- Where main, taken in, changed a file of a node since the user answered on
  that node, the answer no longer stands (REQ-ALG-004), and the user is asked
  again before the ticket is merged. The framework never decides which of two
  colliding changes is right.

Acceptance:

- After any merge the framework made of a ticket whose term ends at the code,
  `done` says yes on main. Where the term ends at a node on which the code
  depends, the next run takes up the simplest ticket and builds what is
  missing.
- A ticket the user edits on main while it is being built is merged with the
  edit in it, after the user's yes where the edit was made while a session
  worked.
- Between two runs, with no session at work and no ruling awaited, the user
  commits a change on main: the next run takes it in and asks nothing on
  what changed.
- Inside a larger repository, while a ticket is active, the user commits a
  change to a file outside the workspace's folder on main, and to a second on
  the ticket's branch. The next run takes main into the ticket's branch, and
  after the merge both are on main as the user committed them.
- Inside a larger repository, a ticket is built to its end in which one
  working session committed the user's changed and untracked files outside
  the workspace's folder, and another wrote a file there and committed it:
  the words that say the ticket is done name each of those files as taken
  into the branch the ticket left. In a ticket where nothing was committed
  outside the folder, they name none.
- Inside a larger repository, between two runs on a ticket, with no session
  at work, the user commits a file outside the workspace's folder on the
  ticket's branch: the words that say the ticket is done name it.
- The user says yes to the code. A commit on main then changes a file of the
  code, and after main is taken in a working session writes that file back
  as it was at the yes: the user is asked on the code again, and the ticket
  is not merged before the user answers.
- A ticket is merged: no file is written and no file's time changes, a file
  the user left uncommitted, one staged and one untracked are as they were,
  and the folder is on main.
- When a ticket is to be merged, the branch it left is checked out in another
  working tree: the run names that working tree, and main and both working
  trees are as they were.
- Main has changed a file outside the workspace's folder in which the user
  has uncommitted work: the run names that file and takes nothing in, and the
  file is as the user left it.
- Main adds a file `local.cfg` where the user has a file `local.cfg` that git
  ignores; main adds a file `out` where the user has a folder `out/` that git
  ignores, with a file in it; main adds `cfg/local.json` where the user has a
  file `cfg` that git ignores. In each case main is not taken in, the run is
  refused and names the path, and the user's file or folder is as it was.

From: product definition, "Each is built on a branch of its own and merged
into main when its work is done"; intent, guard rails 1, 2 and 3; the user,
in tickets 261123-001543-eae1, 261124-091541-a64b, 261124-220448-c7ab,
261125-043021-2fed and 261125-083337-0fdf.

### REQ-FLOW-009 Several tickets at once

**Status**: Deferred. It is built after the first build, as a ticket.

Several tickets are active at once, up to a limit the user sets
(REQ-PARAM-001), each on its own branch. A run started while another is under
way takes the next ticket. Their work meets on main.

1. Each time main is taken into a branch, `collides` is asked.
2. Every vector that writes an asset it returns is open, because no verdict
   or answer was given on the merged content. The merged asset is judged
   first, as any asset that is already there (REQ-FLOW-005, step 1): by its
   checks, by its evaluation and, where the vector declares a decision, by the
   user. The brief of any session on it names both tickets, and where each
   side's content is in the history.
3. Where git cannot merge a file of an asset by itself, the asset is built
   again by a working session, whatever its checks say.

Laws:

- The first ticket to finish is merged first. No asset is locked, and no
  ticket is put before another.
- The framework never decides which of two colliding changes is right.
- Runs share nothing but the workspace, and the hold and the identities in
  git's own directory (REQ-FLOW-001).

Acceptance:

- Scenario S11 ends as it should.

From: product definition, "Several tickets may be active at once, up to a
limit the user sets"; the user, in ticket 261124-190535-753f.

### REQ-FLOW-010 The release that builds a product

The settings file records which release of this product builds the governed
product: the release's version and the sha256 of its manifest
(REQ-INTERFACE-004). Where the product runs from a build that is no release,
the record says that it is an unreleased build. What is running is stated in
the same form, and compared with the record in that form.

- Set-up writes the record from what is running (REQ-FLOW-002, step 5).
- The user's command to record the release writes it from what is running,
  in place of the record there was. It changes nothing else and commits
  nothing: the next run commits it as the user's, with what else the user
  left uncommitted in the folder (REQ-FLOW-003, step 1).
- A run where no record is there, or where the record is not what is running,
  is refused first, once git's version is read (REQ-FLOW-003, step 1). It says what is recorded, or that
  nothing is, and what is running, and names the command to record the
  release.

Laws:

- The framework writes the record only at set-up and by that command.
  Set-up run again does not change it.
- A record the user edits by hand is read as it stands.
- Only a run is refused for its release.

Acceptance:

- Set-up from a release records that release's version and the sha256 of its
  manifest. Set-up from a build that is no release records an unreleased
  build, and a run from such a build is not refused for its release.
- A run by another release than the one recorded, and a run where nothing is
  recorded, each start no session, commit nothing and are refused, saying
  what is recorded, or that nothing is, and what is running.
- After the user gives the command to record the release, a run by the
  release that gave it is not refused for its release.
- In scenario S1, the settings file records the release the product was
  installed from, and no run is refused for its release.

From: the user, in ticket 261122-220203-6a87 and in the answer on its
requirements, and in tickets 261124-091541-a64b and 261124-220448-c7ab;
product definition, "Set up"
and "it does not guard its own records against the user"; intent, guard
rail 3.
