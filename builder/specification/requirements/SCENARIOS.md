# Scenarios

Each scenario names what exists before it starts, what the user does, and what
must be true when it ends. The requirements name the scenarios that test them.
REQ-VERIFY says how a scenario is run and judged.

## S1 Set up and build the smallest product

- Before: the product installed from its release, and an empty folder. The
  user works from the command line.
- The user: sets up a governed product in the folder, writes a ticket of one
  paragraph saying what the product is to do, starts a run, and answers each
  question, starting a run again after each answer. While a session is at work
  the user asks for a second run.
- At the end: the second run was refused, since a run already worked on the
  only ticket. Every question the user was asked is
  one the graph declares. Every vector of the method's graph that takes part
  is closed. The workspace holds the intent, the product definition, the
  requirements, the design, the tests and code that passes them, and the
  user's answers. The ticket lies in the done lane on main, and its branch is
  merged. The event log names every step.

## S2 Interrupt and resume

- Before: S1 under way, with the code step running in a session that is a
  process of its own, apart from the framework's. The driver places a marker
  beside the files the session has written.
- The user: kills the framework and the session, then starts a run.
- At the end: as S1, apart from the one interrupted step. The marker is still
  there.

## S3 Go on without the event log

- Before: S1 stopped after the specification was accepted.
- The user: deletes the event log, asks where the work stands, then starts a
  run and goes on as in S1.
- At the end: the workspace is as S1 leaves it. Asked where the work stood,
  the framework gave the ticket's lane and what its ticket shows, and said the
  log was not found. The run said the log was not found. The new log starts at
  that run. It shows no session started on a vector that was closed, and the
  user was asked for nothing the workspace already records.

## S4 Three changes: to what is required, a fault in the code, and one by hand

- Before: the workspace S1 left. The driver records the content identity of
  every asset.
- The user: writes a ticket that changes one thing the product is required to
  do, and a second ticket that reports a fault the requirements already rule
  out. Starts runs, one at a time, and answers each question, until a run is
  refused with nothing to build. Then changes one accepted requirement by
  hand, starts a run and answers.
- At the end: the tickets were built one after the other. The first entered
  at the requirements, which the user accepted again; working sessions were
  started only on vectors that depend on them, and every other asset is
  byte-identical. The second entered at the code; no session was started on a
  vector that writes the intent, the product definition, the requirements or
  the design, and those assets are
  byte-identical. Both tickets lie in the done lane. Asked where the work
  stands, the framework names the assets each changed, and no others. After
  the change by hand, the user was asked to accept the requirements again, and
  no working session was started on a vector that does not depend on them.

## S5 A step that does not close

- Before: S1 under way, with a stand-in agent whose code step returns code
  that fails the tests.
- The user: starts a run and, when it ends, asks where the work stands.
- At the end: the code step's working session was started twice and failed
  the same checks both times.
  The run then ended as stopped, and said which vector could not close and
  which check did not pass. No session wrote a ticket. The ticket is still
  active, and the framework gives its state as held up. The file
  the stand-in wrote is still there, unchanged.

## S6 A second graph, the registry and an inner workflow

- Before: an empty folder; a graph of three nodes, with its registry, that is
  not the method's graph and has one vector carried out through an inner
  workflow; and a second copy of that graph which names a graph function that
  is not in its registry.
- The user: sets up a governed product, lists the registry, puts the second
  copy in place and starts a run, then puts the first in place and starts a
  run.
- At the end: the first run was refused before any step, with the reason. The
  second reached the three nodes. The framework was not changed.

## S7 A session writes outside its vector

- Before: S1 under way, with a stand-in agent that, during the code step,
  changes an accepted requirement and writes a scratch file in a place the
  graph does not name.
- The user: asks where the work stands when the run ends, says yes to what
  changed, then starts a run.
- At the end: the code step did not close. The run read no verdict, ran no
  check, committed nothing of the step and ended waiting for the user's
  ruling. It named the changed requirement as changed and the scratch file as
  added, and said that each changed while the session worked and that it may
  have been the session or the user. Asked where the work stood, the
  framework gave the same question. Neither file was put back. The next run
  committed both, and asked the user to accept the requirements again before
  any later step.

## S8 An existing system

- Before: a folder that holds a small working system, with an agent
  instruction file of its own and no specification. The driver records the
  content identity of every file.
- The user: sets up a governed product in the folder, starts a run and answers
  each question. Then writes a ticket that changes one thing the system does,
  starts a run and answers.
- At the end: no file of the system was moved, and its agent instruction file
  is as it was, with one block added. The intent and the product definition of
  what was there were written and accepted before any change was built. For
  the change, the requirements, the design and the tests of the part of the
  system it concerns were written, and the change was built. Every file the
  change does not concern is byte-identical, and what the system did before,
  other than the one thing, it still does.

## S9 Build again from the specification

- Before: the workspace S1 left.
- The user: deletes the code, starts a run and answers each question.
- At the end: the code is there again and passes the tests that passed before.
  The only vector a session was started on is the one that writes the code.
  The user was asked only to accept the built product. The run wrote the
  simplest ticket, which lies in the done lane on main.

## S10 Two agents

- Before: the workspace S1 left.
- The user: sets a second LLM agent for the evaluations, deletes the code,
  starts a run and answers each question.
- At the end: as S9. The event log shows the code written by the first agent
  and its evaluation made by the second. Nothing but the one setting and the
  code was changed by hand.

## S11 Two tickets at once

Tests REQ-FLOW-009, which is deferred.

- Before: the workspace S1 left.
- The user: writes two tickets, each changing a different thing the product is
  required to do. Starts a run and, while it is under way, a second. Answers
  each question, starting a run again after each answer.
- At the end: each ticket was built on a branch of its own. The one that
  finished first was merged first. For the other, the requirements, the design,
  the tests and the code were each judged again as merged, and the user
  accepted the merged requirements and the merged product. Main does both
  things and passes every check. Both tickets lie in the done lane on main,
  and they have different names. Asked where the work stands, the framework
  names what each ticket changed.

## S12 The life of one ticket

- Before: the workspace S1 left.
- The user: writes a ticket and starts a run. Says no at the confirmation,
  with a reason, starts a run and confirms. After accepting the requirements,
  edits the ticket and starts a run. Confirms, then puts the folder on main,
  deletes the ticket there, commits that and starts a run.
- At the end: after the no, the ticket was inducted again, and what was added
  to it answers the reason. After the edit, the user was asked to confirm again, and
  the requirements were built again. After the ticket was deleted, the run was
  refused with nothing to build. Main is as S1 left it, apart from the board.
  The ticket's branch is still there. At each point, asked where the work
  stands, the framework gave the ticket's state: in the backlog, waiting for
  the user, withdrawn.

## S13 A product inside a larger repository

- Before: the product installed from its release, and a git repository with
  files of its own and a second branch. Inside it, an empty folder that the
  repository does not ignore. Outside the folder, one file is changed and not
  committed, and another is changed and staged. The driver records the
  content identity of every file of the repository outside the folder, and
  the commit each branch is on.
- The user: sets up a governed product in the folder and goes on as in S1.
  While a session is at work, changes a file outside the folder by hand and
  commits it, which puts the commit on the ticket's branch; changes a second
  file there and leaves it uncommitted; makes a tag and a branch; and stashes
  a change to a third file there, alone. While a later session is at work,
  puts the folder on the branch they made; when the run has ended, puts it
  back on the ticket's branch and starts a run.
- At the end: set-up said that the product lies inside a larger repository,
  and named it. The run whose session was at work when the user did those
  things named the second file, the tag, the branch and the stash in its
  words, as changed while the session worked, and the first file as
  committed while the session worked, and asked nothing on them: none held
  the ticket. The run during whose session the folder was put on
  the other branch named both branches and went no further; the next run
  found the folder on the ticket's branch and went on. Within the folder, the
  workspace is as S1 leaves it. Outside the folder, every file is as the
  driver recorded it but two: the one the user committed, which the ticket's
  merge brought to main as the user committed it and the words that said the
  ticket was done named as taken in, and the second, which is still
  uncommitted. The two files left uncommitted before set-up are still
  uncommitted, and the staged one is still staged. The second branch is on
  the commit it was on. No commit the framework made, but the merge, changes
  a file outside the folder, and the merge brought into main what was
  committed on the ticket's branch, and nothing else. The ticket's branch is
  a branch of the repository, merged into main, and the folder is on main.

## S14 A session is over when the framework has ended it

- Before: a governed product set up and a ticket written, as in S1, in a new
  folder for each case below. The agent the settings name is a stand-in: a
  script, started as a process of its own, that starts a further process in
  a session of processes of its own. That process writes into the
  workspace's folder again and again until it is ended. It is a program whose
  environment the system shows. For the first case, the governing graph gives
  the session a short time.
- The user: starts a run. In each case one of these follows:
  1. the script runs longer than its time;
  2. the script returns and leaves the further process behind;
  3. the script exits with 1;
  4. while the session is at work, the user sends the run the interrupt
     signal;
  5. as 4, with the terminate signal;
  6. as 4, with the hang-up signal;
  7. while the session is at work, the user kills the run, then starts a run;
  8. as 1, 4 and 7, and the further process is a shell, one of the system's
     own programs, whose environment the system does not show;
  9. as 2, and the further process is such a shell, started in the script's
     own process group;
  10. as 2, and the further process is such a shell, started in a session of
      processes of its own, with the workspace's folder as its current
      folder. The user then ends the shell and starts a run;
  11. as 7, and before the user kills the run, the script changes the
      settings file and the governing graph and writes a file of its own in
      the workspace's folder.
- At the end: in cases 1 to 9, no process of the session is alive when the
  framework goes on: past the session in cases 1 to 3 and 9, when the run has
  ended in cases 4 to 6, and in case 7 before the next run does anything else
  on the ticket; in case 8 as in the case it repeats. Nothing such a process
  writes afterwards is in the workspace. In case 10 the framework cannot place
  the shell: it ends no process, the run is cut off and names the shell by its
  number, and nothing is committed, judged or started on the ticket while the
  shell is alive. The run the user starts after ending it goes on. In each
  case where a run goes on past the session, it names to the user what the
  further process wrote into the workspace's folder, and judges and commits
  nothing of the step before the user has ruled. In case 11, once the session's
  processes are ended, the next run commits nothing: it names the settings
  file and the governing graph as changed and the script's file as added,
  each as changed while the session worked, and ends waiting for the user's
  ruling. Main holds none of the three. The driver
  waits for each within a bound, and judges nothing after a fixed pause.
