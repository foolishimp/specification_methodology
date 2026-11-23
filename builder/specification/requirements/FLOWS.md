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
| Write an asset | A working session | The assets its vector writes; for the first vector's session, the triage and the term in the branch's ticket. Elsewhere in the workspace it does as it needs, and it may add a ticket to the backlog |
| Write a verdict | An evaluating session | Its findings and its verdict, where the vector declares |
| Write the set-up files | The framework | What REQ-FLOW-002 lists, once. Afterwards, at the user's command, the record of the release that builds the product (REQ-FLOW-010) |
| Start and end a session | The framework | It starts one with its brief, and ends one that runs longer than allowed |
| Write its own files | The framework | What its checks found |
| Write its part of a ticket | The framework | In the branch's ticket: the checklist, the resolutions and the rulings (REQ-FLOW-004). It only adds to that part |
| Keep what a session printed | The framework | When a session returns or fails, what it printed, or why it could not be started, as one of its own files. The last of each vector and kind of session is kept |
| Move a ticket | The framework | From lane to lane. It also writes the simplest ticket, and names a ticket |
| Open a branch | The framework | For a ticket it pulls: a branch from main, and a checkout of that branch |
| Commit | The framework | On a ticket's branch: the result of each step, each answer, and what a line of its part of the ticket names, before the line names it. On main: a move on the board, and what the user left uncommitted in the workspace when a run starts |
| Merge | The framework | Main into a ticket's branch, and a ticket's branch into main (REQ-FLOW-008) |
| Add to the event log | The framework | One entry (REQ-FLOW-007) |
| Hold | The framework | While a run works on a ticket no second run takes that ticket |
| Wait | The framework | The run ends as waiting for the user |
| Fail | A session | It cannot be started, stops without returning, or runs longer than allowed. It may be tried again |

A ticket has three parts, and each has one writer. The user's words are the
user's. The triage and the term are the first vector's session's. The
checklist, the resolutions and the rulings are the framework's part. The
framework writes no line of the first two, and no session writes the third
(REQ-ALG-008). The user may change any part by hand (REQ-FLOW-004), and the
framework reads its part as it stands.

The tickets, and the resolutions in them, are under git: a ticket travels
with its branch and reaches main by its merge. What the checks found, what
the sessions printed and the event log are in the workspace and outside the
history. A run that ends after a session failed names where what that session
printed is kept.

Main is the line the workspace's own checkout is on, at the folder the user
named, whatever its name. The workspace may lie inside a larger git repository, below its top
folder (REQ-FLOW-002). It is still one workspace: that folder. Every effect
then concerns only files under it: each file the framework writes, each commit
and merge it makes and each identity it reads. A ticket's branch and main are
the repository's, since git has no other. The framework leaves every other
file of the repository as it is, and what the user has not committed elsewhere
in it, and changes none of the repository's other branches. Main that has
moved only outside the folder has not changed for the product. A product in a
repository of its own is the case where the folder is the repository's top.

Laws:

- The framework never reverts, resets or rewrites anything, puts no file back,
  deletes no branch and sends the history nowhere. What the agent or the user
  does with the history is theirs: the framework works from the workspace as
  it then is.
- The framework adds to main in three ways only: a move on the board, what the
  user changed by hand in the workspace or by the command to record the
  release, and the merge of a ticket on whose branch `done` said yes.
- The framework keeps nothing outside the workspace. Inside a larger
  repository, git keeps the history, the branches and the record of each
  checkout where it keeps them for the whole repository.
- The framework makes no copy of the workspace or of any part of it. A branch
  and its checkout are made by git and by nothing else, and work moves between
  a branch and main only by a merge.
- Runs share nothing but the workspace.
- Only a session uses a language model.
- Nothing a killed run leaves behind refuses the next run.

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
- Scenario S13 ends as it should.
- After scenario S1, each verdict and each answer is a resolution in the
  ticket. No other file of the framework's holds one, or the content
  identities one was given on, and no file holds a record of a run's reading
  of a ticket or a question.

From: intent, guard rails 1, 2, 4, 6 and 7; product definition, "The agent
writes the product's assets and the framework writes its own files", the term
"Ticket" and "There is one event log"; the user, in tickets 261123-001543-eae1
and 261123-021212-4e94.

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

1. Where no record of the release is there, or the record is not what is
   running, the run is refused (REQ-FLOW-010).
   Then a graph that is not `well_formed` is refused; where the graph or its
   registry is, the refusal names where the installed release keeps the
   method's own. Then what is not yet committed on main is committed.
2. `take_up` gives the ticket. None: the run is refused, and says which holds:
   a run already works on every active ticket, the limit is reached, or there
   is nothing to build.
3. The framework holds the ticket, pulls it if it lies in the backlog
   (REQ-FLOW-004), and takes main into its branch (REQ-FLOW-008).
4. `next` gives the vector, in the ticket's checkout. None: go to step 6.
5. One step is made on that vector (REQ-FLOW-005). Then step 4 again.
6. The ticket is merged (REQ-FLOW-008), and the run ends with the work done:
   where `next` gives none, no vector that takes part is open, so `done` says
   yes in the checkout.

A run ends in exactly one of four ways:

1. the work is done: the ticket is merged, and main is what its specification
   says;
2. it is waiting for the user's answer;
3. it has stopped, and states the vector and the reason: a check that could
   not be run, a vector that could not close, a protected file that changed, a
   file git could not merge, or a limit the user set;
4. it was refused before any step, and states why.

Laws:

- Where the framework cannot do what the graph declares, it stops and says so,
  and does nothing else in its place.
- Each ending is shown to the user in plain words, with what the user can do
  next.
- A run reads the workspace and not the event log. Where the log is missing it
  says so, and starts one.

Acceptance:

- A run started on the workspace scenario S1 leaves starts no session and is
  refused: there is nothing to build.
- Scenarios S2 and S3 end as they should.

From: product definition, "Build" and "Resume"; intent, outcomes 1 and 4.

### REQ-FLOW-004 A ticket

A ticket is a work order: it says how the workspace is to be amended. The user
writes one in their own words, as a file in the backlog, on main. The three
ticket lanes are a board: backlog, active and done. The framework pulls from
the backlog, and never chooses what is put there.

1. **Pull.** The framework moves the ticket to the active lane on main, and
   opens a branch for it, or takes up the branch it already has. All work on
   the ticket is done in the checkout of that branch.
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
5. **Merge.** When `done` says yes in the checkout, the ticket moves to the
   done lane on its branch, and the branch is merged into main
   (REQ-FLOW-008).

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

Where what a line names is not yet committed, the framework commits it first.
The ticket names each finding, each difference and what a session printed by
its path, and holds none of them: the detail is in git. A session starts from
the ticket. Its brief names the ticket, and the rulings in it as binding on
the session (REQ-ALG-007).

What the user may do on main, at any time. A run under way on the ticket
learns of it when main is next taken in (REQ-FLOW-008):

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

To induct a ticket again is to hold the whole ticket, as it now is, to the
checks of its first induction, and to ask the user to confirm it as it then
is. The first vector's session runs where the user said no or the ticket does
not pass those checks; otherwise no session runs. A change to an active
ticket outside the framework's part, that the framework finds before it
starts a session, is the user's, and the ticket is inducted again; a change a
session makes is that session's work (REQ-METHOD-006).

Before it starts a session bound to a stretch, the framework adds the binding
to the checklist and commits it. The binding ends when the user is asked to
confirm the term the session wrote, or when the framework takes the user's
edit of the ticket in from main; the checklist shows each. A change to the
ticket while the binding holds is that session's work, whether it returned,
failed or its run was cut off, and so is the ticket as the user was then
asked to confirm it. Any other change since the user's confirmation is the
user's. Where the session then runs on the user's change, the question says
so: the user's edit is never overwritten without the user being told.

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

From: product definition, "Ask" and the term "Ticket"; the user, in tickets
261122-232152-1198, 261123-021212-4e94 and 261123-100659-a0d5.

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
2. A working session is started, in the ticket's checkout, with its `brief`.
   It is a new session, of the agent the settings file names for this vector.
   Where the vector's graph function is not a single session, its inner terms
   are run in its place: `next` is asked among them until none is open.
3. On its return, `trespass` is asked. Any file returned: the step does not
   close, and the run ends as stopped, naming the files. The framework puts
   nothing back. The next run goes on from the workspace as it is.
4. Where the vector declares an evaluation, its asset is there and every
   check of the assets it writes says yes, it is made in a new session, of
   the agent the settings file names for it, with its `brief`. Its verdict says yes, no, or that it cannot judge, with why in
   its findings. On its return `trespass` is asked, as in step 3. The
   framework reads the verdict. A yes or a no it adds to the ticket as the
   evaluation's resolution, with the commit that holds what it was given on
   (REQ-FLOW-004). A verdict that it cannot judge is no resolution.
5. `passes` is asked, and the framework writes what the checks found.
6. Where the vector declares a decision by the user, no answer stands and
   every other check passes, the user is asked (REQ-FLOW-006).
7. The result of the step is committed, whether or not the vector closed, and
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

- Nothing passes from one session to the next except the workspace.
- A session works in the ticket's checkout itself, reached by its URI, never
  in a copy of it. The framework sets no limit on how a session reaches it.
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
- An evaluating session that changes the asset it judges stops the run.
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
- Scenarios S5, S7 and S10 end as they should.

From: product definition, the terms "Step", "Session" and "Evaluation", and
"Change"; intent, guard rails 2, 3 and 7; the user, in ticket
261123-100659-a0d5.

### REQ-FLOW-006 A question and its answer

1. The framework asks the user, and the run ends as waiting. The question says
   in plain words what is being decided, what it rests on and what follows from
   each answer. For each file of the nodes the vector writes that changed
   since the content last accepted, as main holds it (REQ-ALG-007), it says
   how many of its lines changed and how many remain as they were, and it
   says that every other file is as it was; where main holds none of a node,
   it says that the node is new. It is given in the run's ending, and `stands` gives what is
   asked (REQ-ALG-012). No file holds it.
2. The user answers with the product's command for that, and starts a run
   again. With the answer, the user may give a ruling.
3. The framework adds the answer to the ticket as the user's resolution, with
   the ruling where there is one, and commits it (REQ-FLOW-004). The answer is
   for the vector whose work the checklist shows delivered for the user's
   decision with no answer of the user after it, and it is given on the
   commit that delivery names.

Laws:

- The answer runs no check, and reads neither the event log nor any record
  but the ticket. Where the ticket shows nothing delivered for an answer, or
  the content the answer would stand for (REQ-ALG-004) differs now from that
  commit's, the answer is refused, and says that a run asks again.
- When that content changes, the answer no longer stands, and the user is
  asked again.
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

From: product definition, the term "User" and the term "Ticket"; intent,
purpose and guard rails 3 and 4; the user, in tickets 261120-9636,
261123-021212-4e94 and 261123-100659-a0d5.

### REQ-FLOW-007 The event log

Each governed product has one event log, in the workspace. Every run adds to
it, whichever ticket it works on. The framework adds an entry for:

- set-up; a ticket written; the release recorded (REQ-FLOW-010);
- a ticket pulled or merged; main taken into a branch, with the assets that
  collided;
- a run started, with the release in force, and how it ended;
- a run cut off, which the next run on the ticket adds where it finds the
  hold the cut-off run left. A session that run started and that neither
  returned nor failed was cut off with it;
- a session started, by vector, kind and agent, with the agent's command as
  it was run and the commit the session starts from;
- a session returned or failed, with how long it took, where what it printed
  is kept and, where the agent reports them, its cost and the number of its
  calls;
- a check run, by name, with whether it passed, said no or could not be run,
  and how long it took;
- a verdict read, with what it says and where its findings are;
- a vector closed or left open; the user asked;
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
- A run adds nothing between the start of its session and that session's
  return.
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
- After any number of runs, the earlier content of the log is unchanged at the
  start of the later log.

From: intent, model and guard rails 5 and 6; product definition, "There is
one event log" and "the log lacks an event or a detail"; the user, in ticket
261123-021212-4e94.

### REQ-FLOW-008 Merging a ticket's work

1. Main is taken into the ticket's branch at the start of each run on the
   ticket, and again where main has moved by the time `done` says yes. Main
   that has moved only outside the workspace's folder is not taken in
   (REQ-FLOW-001). Where the ticket then no longer lies in the active lane,
   the run ends as stopped and says so.
2. When `done` says yes on a branch that holds all of main under the
   workspace's folder, the ticket moves to the done lane on the branch, and
   the branch is merged into main.
3. Where git cannot merge a file by itself, the run ends as stopped and names
   the file.

Laws:

- Ticket files do not collide: each has a name of its own, and a branch moves
  no ticket but its own.
- What a done ticket changed can be read from the history.
- Inside a larger repository, a ticket's branch and its merge change no file
  outside the workspace's folder: after the merge, each such file on main is
  as main had it before.

Acceptance:

- After any merge the framework made of a ticket whose term ends at the code,
  `done` says yes on main. Where the term ends at a node on which the code
  depends, the next run takes up the simplest ticket and builds what is
  missing.
- A ticket the user edits on main while it is being built is merged with the
  edit in it.
- Inside a larger repository, a file outside the workspace's folder is
  changed and committed on main while a ticket is active. The next run does
  not take main into the ticket's branch, and after the merge that file is on
  main as the user committed it.

From: product definition, "Each is built on a branch of its own and merged
into main when its work is done"; the user, in ticket 261123-001543-eae1.

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
- Runs share nothing but the workspace.

Acceptance:

- Scenario S11 ends as it should.

From: product definition, "Several tickets may be active at once, up to a
limit the user sets".

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
  left uncommitted on main.
- A run where no record is there, or where the record is not what is running,
  is refused first (REQ-FLOW-003, step 1). It says what is recorded, or that
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
requirements; product definition, "Set up" and "it does not guard its own
records against the user"; intent, guard rail 3.
