# STDO Builder: instructions for users

STDO Builder lets you set up a product under a defined method of work and have
an LLM agent build it. You say what you want in a ticket; the framework walks
the method's graph one step at a time, starts the agent on each step, checks
the result against the folder as it is, and asks you where the graph calls
for your decision.

If you have not used the product before, read the getting-started guide,
`GETTING_STARTED.md`, beside this page, first. It takes one small product from
nothing to a change, with the commands and what the product printed. This page
gives the details.

You need:

- Node.js 24 or later on your PATH;
- git 2.38 or later on your PATH, for every product;
- `ps` on your PATH, which reads the table of processes; on Debian and Ubuntu
  it comes with the package procps, which a clean machine may lack;
- the method's release manager, `stdo`, on your PATH: set-up uses it to
  install and verify the method release the product is built under;
- an LLM agent that runs from the command line. By default this is `claude`
  (Claude Code). Another is named in the settings file (below).

## Install

The release is a folder, `stdo-builder-<version>`. Its installation page,
`INSTALL.md`, says what installing needs and does. Install it into a folder of
your choice with one command:

```
sh <release>/install.sh <folder>
```

Before it writes anything, the install checks every file of the release
against the release's manifest, `manifest.json`. Where a file is missing or
differs, or the release holds a file the manifest does not name, it says which
and installs nothing.

The command `stdo-builder` is then in `<folder>/bin`. Put that folder on your
PATH, as the install says, so that you can type `stdo-builder` alone:

```
export PATH="<folder>/bin:$PATH"
```

Installing writes nothing outside `<folder>`.

## Set up a product

```
stdo-builder setup <workspace> --name "<a name for the product>"
```

The workspace is the folder that holds the product: an empty folder, or one
that holds an existing system, which is left where it is. It may be in no git
repository, the top folder of one, or a folder inside a larger git repository.
Set-up puts a folder in no repository under git, installs and verifies the
method release, and writes:

- the definition file, `stdo_<name>.json`, and
  `specification/REFERENCE_FRAME_BASIS.md`;
- `.stdo-builder/settings.json`, `.stdo-builder/graph.json` and
  `.stdo-builder/registry.json`: which agent works, which release of STDO
  Builder builds the product (the one that set it up), and the method's graph;
- a block of the product's commands in `AGENTS.md` and `CLAUDE.md`, so that an
  agent started in the folder can run them for you.

### Inside a larger git repository

Where the folder lies below the top of a larger git repository, set-up says so
and names that repository by its top folder. The workspace is still the one
folder. Each file the framework writes, each commit it makes but a ticket's
merges, and each identity it reads concern only files under it. A ticket's
merges are the two below: main taken into the ticket's branch, and the
ticket's branch merged into main. Each carries whatever was committed on its
branch anywhere in the repository. It leaves every other file of the
repository as it is, and what you have not committed or have staged elsewhere
in it, save what you have staged when a run completes the one merge below, and
changes none of the repository's other branches.

- A repository has one folder checked out on one branch. While a ticket is
  active, the repository is on the ticket's branch, so a commit of yours
  anywhere in it, inside the folder or outside, goes on that branch, and
  reaches main when the ticket is merged: the merge carries the branch's whole
  tree. Main that moved outside the folder is taken into the ticket's branch
  too; what main gained in the folder while a session worked is put to you
  first, as "What changed while a session worked" says.
- A session's git commands act on the whole repository, as yours do: a
  session that commits with `git add -A` commits what you have not committed
  outside the folder. After each session the run names each file outside the
  folder that was committed while it worked, whether by the session or by
  you, and says that the ticket's merge takes it into the branch the ticket
  left; and, apart, each file outside the folder committed on that branch
  while it worked. When the ticket is merged, the words that say it is done
  name each file outside the folder the merge took into that branch. None of
  them holds the ticket, and you are asked nothing on them.
- Two products in one repository share that one checked-out branch: while the
  repository is on a ticket's branch of one, a run of the other is refused,
  naming that branch, until the repository is back on a branch of its own.
- Main changes a file outside the folder in which you have work not
  committed, or adds one where you have a file git ignores: main is not taken
  in, and the run names the file. Commit it or put it aside, then start a run
  again.
- A merge of your own under way in the repository when a run starts stays
  yours: the run commits only what you changed in the folder, and leaves the
  merge for you to commit. The one merge a run completes is main taken into
  the ticket's branch, once you have resolved what git could not merge. It
  completes it as `git commit` would, from the repository's own index, so a
  file you have staged elsewhere in the repository at that time is in that
  merge: commit the merge yourself first, or unstage what is not to go with
  it.
- Git keeps the history and the branches where it keeps them for the whole
  repository.

Where the repository ignores the folder, set-up is refused and changes nothing:
set the product up in a folder the repository does not ignore, in a folder in
no repository, or in the top folder of one.

A file that is there already is left as it is. Set-up asks for nothing else.

## Write a ticket

```
stdo-builder ticket <workspace> "<what you want, in your own words>"
```

A ticket is one file in `.ai-workspace/tickets/backlog/`. The first step of a
run inducts it: it adds the method's triage of the change and the steps that
carry the work out, from where the work enters to where it ends: two for a new
product of a few commands, one for each asset for larger work. It keeps your
words as you wrote them. You confirm that.

A step may instead be an induction entry, for a later stretch whose steps are
best chosen once the work before it is accepted; it is never the first step.
When the run reaches it, the induction writes the steps for that stretch in
its place and changes nothing else of the ticket, and you confirm the ticket
again.

You do not need a ticket to rebuild what the specification already says: a run
with no ticket waiting builds the workspace to its specification as it stands.

## Start a run

```
stdo-builder run <workspace>
```

A run works on one ticket and goes on without you until it ends, in one of
four ways, which it tells you in plain words with what you can do next:

- done: the ticket lies in `.ai-workspace/tickets/completed/` and its branch
  is merged into the branch it left, which the run names;
- waiting for your answer, or for your ruling on what changed while a
  session worked;
- stopped: it names the step and why;
- refused before any step: it says why, for example that a run is already at
  work, that there is nothing to build, or that another release of STDO
  Builder is recorded as the one that builds the product.

Where a session failed in the run, the run names where what it printed is
kept: a file for each session, under `.stdo-builder/local/printed/`, which
that session's entry in the event log names.

A session is every process the agent's start leads to. The framework knows a
process to be of the session by its parent, by its process group, or by a
mark in its environment, starting from the agent's own process. When the
agent's own process ends, when the session's time is over, and when the run
receives the interrupt, the terminate or the hang-up signal (Ctrl-C, `kill`,
a closed terminal), the run ends every process it knows to be of the session
before it goes on, and the event log holds how many it ended. On a signal the
run then goes no further: it is cut off, which is none of the four endings,
and exits with 130, 143 or 129.

The system does not show the environment of its own programs, a shell among
them. A process that has left its parent, is in no group with a process of
the session, shows no environment, and works in the workspace's folder is one
the framework cannot place: a job of your own started there is one. It does
not end it, and names it by its number,
when it started and its command. Where such a process is there, or one of the
session's is still alive after the run has tried to end it, the session is not
over: the run commits, judges and starts nothing more, names each process,
exits with 1 and is cut off too. End each process it names, then start a run
again. Where the run cannot read the process table with `ps` when the session
would be over, the session is not over either: the run is cut off in the same
way, says in one sentence that `ps` was not found or could not read the table
and what to install, and names no process; install it, then start a run
again. Where a run was
killed or cut off, the next run ends what is left of its session before
anything else on the ticket, and is refused while one of those processes, or
one it cannot place, is still alive. An answer ends no process, and is
refused while one is alive; end it, then answer.

One kind of process of a session the framework does not find: one that has
left its parent, is in no group with a process of the session, and shows an
environment without the mark, wherever it works, or shows none and works
outside the workspace's folder. Nothing the system gives a program without
privileges finds it, and the framework cannot tell it from a job of your own.
What it writes in the folder before its step is settled is put to you, as
"What changed while a session worked" says; what it writes after that, the
next run takes as your change by hand.

A command of STDO Builder given from inside a session it started, on that
session's workspace or a folder inside it, is refused and changes nothing:
the framework runs that workspace's commands itself. On any other workspace
the commands work as ever.

### One folder, a branch for each ticket

All work on a ticket is done in the workspace's own folder, on a branch of its
own, `stdo/<ticket>`. When a run pulls a ticket, the ticket records the branch
the folder was on as the branch it left, `- framework: left <branch>`; that
branch is main for the ticket until it is merged into it, and into no other.
The run makes the ticket's branch there and puts the folder on it. Only one
run works on a ticket at a time.

The cost of one folder: while a ticket is active, the folder is on its branch.
What you change by hand there, and commit, is on the ticket's branch and
reaches main when the ticket is merged. To change main itself, other than to
withdraw or put back the ticket (below), put the folder on main (`git switch
main`), commit, and put it back (`git switch stdo/<ticket>`): the next run
takes main in. Done while a session works, or while your ruling on what
changed is awaited, each file of the folder your commit changes is put to you
first, and main is taken in after your yes. While the folder is on another
branch, a run, an answer, `ticket` and `record-release` are refused, naming
both branches; `show` still answers and says so. A run on a folder on no
branch, or on a ticket's branch with no ticket active, is refused.

The files git ignores in the folder are yours too: local settings,
dependencies, what a build left. A session works among them: it can read
them, and what it removes of them is removed, and the framework, which
compares only what git does not ignore, names nothing of it. A check runs in
the folder as it is, with the files git ignores there, so what passes in your
folder may rest on one of them that no commit holds. The event log lies among
them too: a cleaning of the folder removes it, and the next run starts a new
one.

A clone that has the ticket's branch only as a remote branch: the run makes
the local branch from it, and the branch the ticket left in the same way, and
goes on with the ticket; it never begins it again from main.

Where the ticket's branch is checked out in another working tree — a working
tree is a folder in which git has checked out a branch, such as a checkout an
earlier release left under `.stdo-builder/local/checkouts/` — git will not put
the folder on it, and the run is refused and names that working tree. Remove it
with `git worktree remove <path>` (add `--force` where it holds work you do
not want). The merge is refused in the same way while the branch the ticket
left is checked out in another working tree. A done ticket's branch is no
longer needed; remove it with `git branch -d stdo/<ticket>`.

### What changed while a session worked

When a session is over, the run compares every file git does not ignore in
the workspace's folder with what was there when the session started. Where a file differs that the step does not write,
and the framework did not write, the run judges and commits nothing of the
step: it waits, and asks you to rule. The question names each file by its path
from the workspace's folder, with whether it was added, changed or removed. It may have been the session or you; the framework cannot
tell which. A yes: each file named stands as it then is, the framework commits
it with the step, and whatever rests on it is judged or accepted again. A no:
put back what is not to stand. The framework puts nothing back in either case.
The next run compares again and asks again while a file differs that you gave
no yes to, or that changed after your yes.

The comparison does not reach three cases, which are limits of this release:

- a folder in the workspace that is a git repository of its own, as `git
  clone` or `git init` there leaves: none of its files is compared or asked
  about, and the framework commits a pointer to its commit, which a clone of
  the product cannot follow;
- a file that a session takes out of git's index and has git ignore: it is
  removed from the ticket's branch, and so from main, with no question, and
  stays in the folder;
- a change of a file's mode alone: it is committed with no question.

The run also compares main, the branch the ticket left, as it is now with the
commit it was on when the session started. Each file of the workspace's folder
that differs there, by a commit of the session's or of yours, is put to you in
the same question, named apart from the files that differ in the folder, as
changed on main, by its path from the workspace's folder and whether it was
added, changed or removed there. None of them counts as what the step writes:
the step's own work, committed on main, is asked about too. Until you have
said yes to each, as main then holds it, nothing of main is taken into the
ticket's branch, and nothing of the step is judged or committed. A yes: main
stands as it then is, and the run takes it into the ticket's branch; the
framework commits none of those files with the step, and whatever rests on
them is judged or accepted again. A no: put main back, to the commit it was on
or by a commit on main that undoes the change, such as `git revert` gives; the
framework puts nothing back and takes nothing of main in, and the next run,
finding nothing that differs there, goes on. `git reflog show main` lists the
commits main has been on, the latest first. Inside a larger repository, a
session's commit on main can take in work you had not committed outside the
folder; then that commit alone holds it. Take it out, `git show
<commit>:<path>` with the path the run names, before you put main back. Where
main moves again and a file there differs from what you said yes to, you are
asked again. A move of main that changes no file is named, as below, and asks
nothing. What main gains while no session's identities are kept, as between
two runs when no ruling is awaited, a commit of yours on main or an edit of a
ticket there among it, the next run takes in with no question. A withdrawal or
a putting back of the ticket asks nothing either, and main is taken into the
ticket's branch only when a run pulls it again.

What you change by hand in the folder and leave uncommitted, a run commits as
your change, on the branch the folder is on, when it starts. Where the
identities from a session's start are kept and its ticket is active, it
compares first, and commits nothing until you have ruled; then it commits what
the step writes and the files you said yes to as the step's result, and the
rest as your change by hand.

The identities taken at a session's start, with each yes you gave on what
changed, and the hold a run keeps on a ticket lie in a folder of the
framework's own under git's own directory for the workspace's folder, the one
`git rev-parse --absolute-git-dir` gives there: `stdo-builder/` in it, with a
folder for each workspace. `git clean`, `git stash --all` and git's other
commands do not reach them, so where a session cleans the workspace's folder,
the comparison still finds what changed. That holds for the comparison and
for nothing else: what a cleaning costs you is said under "One folder, a
branch for each ticket". The framework's other files stay under
`.stdo-builder/local/`, where git ignores them; the comparison needs none of
them.

Where the identities from a session's start are missing, cannot be read, name
a step the graph no longer holds or name what git no longer holds, after the
session or when a run starts, the commit the session started from stands in
for them, with nothing counted as what the step writes: each file that
differs from that commit, whether committed since or not committed, is put to
you, so what a session committed of its own is asked about too, and the
question says in one sentence that the identities are missing. An answer
given while that is so is refused, and writes nothing: start a run, which
asks. The run that started the session knows that commit; a later run reads
it from the record kept at the session's start. This has a limit,
which is accepted: where that record is gone, cannot be read or names a
commit git no longer holds, the commit the folder is on stands in instead,
each file not committed in the folder is put to you, and what a session
committed of its own on the ticket's branch is not asked about. Wherever a
commit stands in for the identities, in either way, or where the record
names no commit of main, as a record an earlier release wrote names none, the
commit where the ticket's branch and main last met stands in for the commit
main was on: each file of the folder that main holds otherwise than that
commit is put to you, named apart as changed on main, before main is taken
in, so what a session committed of its own on main is asked about too. Where
both the hold and the identities are removed from git's directory before a
run starts, that run cannot know that a session worked, and commits what is
not committed as your change by hand.

The run also notes the repository's branches, tags and stash, but the
ticket's own branch, before and after each session; and, inside a larger
repository, what git lists as changed or untracked outside the workspace's
folder. What differs it names as changed while the session worked, at most 20
for each session, with how many there are. Main is named among them as any
other branch. None of it holds the ticket, save main where it changed a file
of the folder: each such file is put to you, as above, and the run's words
then say so of main. After a run cut off while its session worked, the next
run says it cannot tell what changed among them.

Inside a larger repository, a session's git commands act on the whole
repository, so a session that commits with `git add -A` commits what you have
not committed outside the folder. After each session the run names, apart,
each file outside the folder that differs between the commit the folder was
on when the session started and the one it is on when it is over, as
committed while the session worked, at most 20 with how many there are, and
says that the ticket's merge takes what was committed there into the branch
the ticket left; where git cannot compare the two commits, it says it cannot
tell what was committed there. A file you only commit while a session works
is named so. Apart again, it names each file outside the folder that differs
between the commit main was on when the session started and the one main is
on when it is over, as committed on main while the session worked, by whether
it was added, changed or removed, at most 20 with how many there are; nothing
is asked on them, and none of them holds the ticket; where git cannot compare
main's two commits, it says it cannot tell what was committed on main there.
When the ticket is merged, the words that say it is done name each file
outside the folder the merge took in, at most 20 with how many there are.

## Answer a question

When a run waits, it prints the question as it ends; `stdo-builder show` gives
it again. No file keeps it. It says what is being decided, the files it rests
on, and what follows from each answer. Read the files it names, then:

```
stdo-builder answer <workspace> yes
stdo-builder answer <workspace> no --reason "<why>"
stdo-builder answer <workspace> no --reason "<why>" --ruling "<what binds>"
```

A no comes with your reason. With either answer you may give a ruling: it binds
every later session on the ticket. Then start a run again. An answer stands for
the files as they were when you gave it; if they change, you are asked again.
An answer given after the files changed since the question is refused: start a
run, and you are asked again.

## What the ticket holds

The ticket is the work order. Your words are yours; the induction's session adds
the triage and the term. As the work goes on, the framework adds lines that
start `- framework: `: the checklist of where the work of a step began and
what has been delivered, each yes or no
of an evaluation or of yours, with your reason, and each ruling, each with the
commit it was given on. Those lines are the framework's part. It names findings
and what a session printed by path, and copies none of them. Editing your part
of an active ticket has it inducted again; an edit of the framework's part is
read as it stands.

## See where the work stands

```
stdo-builder show <workspace>
```

For each ticket: its lane, and for an active one what it waits on (your
answer, to be inducted, held up at a step and why, in build, or ready to merge);
the parts of the product it changed, with how many lines; how its last run
ended and the sessions it took. Whether an active ticket waits on your answer
or on its induction is read from the ticket; the rest is read from the event
log. `show` says which it read, with when that was written, and runs no check,
so a change made since then shows once a run reads the workspace again.
Without the event log it says so, and for a ticket that waits on neither your
answer nor its induction it says that a run finds what it waits on. The event
log is at `.stdo-builder/local/events.log`; it says what the framework did,
and is never the proof of the work. The proof is the folder itself.

## List the registry

```
stdo-builder registry <workspace>
```

The graph functions the graph may use, each with the parts it writes, the
parts it rests on and what it is for. You may put another graph and registry in place
of the method's, in `.stdo-builder/graph.json` and
`.stdo-builder/registry.json`; a run refuses a graph that is not well formed,
and says why.

## Record the release that builds the product

```
stdo-builder record-release <workspace>
```

The settings record which release of STDO Builder builds the product: its
version and the sha256 of its manifest, or `"unreleased build"` for a build
that is no release. Set-up records the release that set the product up, and
setting up again does not change it. A run by any other release, or where
nothing is recorded, is refused before any step: it says what is recorded and
what is running. Only a run is refused; the other commands work as before.

Before you install and record a new release, finish or put back every active
ticket with the release that pulled it: a release does not read the hold or
the identities that an earlier release kept in another place, so a ruling
awaited across the change is not asked again, and the next run commits what is
not committed as your change by hand.

To have the release you now run build the product, for example after you
install a new one, give this command with it. It writes that release in place
of the one recorded, changes nothing else, and commits nothing: the next run
commits it as your change by hand, on the branch the folder is on. You may
also edit the record by hand; it is
read as it stands.

## When a run stops

- A step could not close: its evaluation said no as many times as the graph
  allows attempts, its working sessions did not leave fewer checks failing
  each time, or two sessions on it failed in a row. The run names
  the checks that did not pass and where what they found is kept. Change what
  needs changing, by hand or by editing the ticket to give direction, and
  start a run again. Nothing is undone for you, and nothing is put back.
- The folder was found on a branch that is not the ticket's after a session:
  the run names that branch and stops, and nothing of the step is judged or
  committed. A run started while the folder is on such a branch is refused,
  naming both. Put the folder back on the ticket's branch, `git switch
  stdo/<ticket>`, and start a run again.

A file that changed while a session worked, outside what its step writes,
does not stop a run: the run waits for your ruling on it, as above. One case
does: a symbolic link to a folder, or one whose target is not there, that
appears while a session works stops the run with git's own words, and each
run and answer after it is refused until you remove the link or have git
ignore it.
- git could not merge a file: resolve it where the run says, commit there,
  and start a run again.

To withdraw a ticket, delete its file on main. To put one back, move it to the
backlog. The commits on a withdrawn or put-back ticket's branch stay on that
branch, and the framework brings none of them to main; bring what you want
of them to main with git. To change what you asked, edit the ticket on main; to change its
steps, edit them in the ticket's file that the question names. Either change
is yours, and you are asked to confirm the whole ticket again. Where the
ticket no longer passes the induction's checks, its steps among them, the
induction runs again first, and the question says so. An edit on main made
while a session works, or while your ruling on what changed is awaited, is put
to you first, as any file main gains then; after your yes main is taken in,
and what this section says of it holds.

Withdraw a ticket or put it back only when no session works on it and no
ruling on what changed is awaited, and leave the folder on main. Done while a
session works, the question names the ticket's file as changed on main. At
either time your answer is refused, since no ticket is active, and so is each
run until the folder is on the branch you build on. What the session wrote
lies uncommitted in the folder; `git switch` carries it to main, and the next
run commits it there as your change by hand, with no question and no word of
it. Before you switch, set it aside (`git stash -u`) or remove it; where a run
has committed it, undo that commit on main with `git revert`. Where a session
moved the ticket's file on main, or moved main back, put main back to the
commit it was on, as above: the ticket is active again, and the run goes on.

## The settings

`.stdo-builder/settings.json` says which agent does each step's work and each
evaluation:

```
{
  "definition": "stdo_<name>.json",
  "builder": { "version": "<version>", "manifest_sha256": "<sha256 of its manifest.json>" },
  "agents": {
    "claude": [
      "claude", "-p",
      "Read the activation packet at {brief}, and do the work it binds in this folder.",
      "--permission-mode", "acceptEdits",
      "--tools", "Bash,Read,Write,Edit,Glob,Grep",
      "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep",
      "--output-format", "json"
    ]
  },
  "work": "claude",
  "evaluation": "claude",
  "reports": { "claude": { "cost": "total_cost_usd", "calls": "num_turns", "unit": "USD" } }
}
```

`builder` is the release of STDO Builder that builds the product (see
"Record the release that builds the product"). `agents` gives each agent's command; `{brief}` is replaced by the path of the
brief the framework writes for the session, or the path is added at the end.
`work` and `evaluation` name the agent for all work and for all evaluations;
`vectors` may name another for one step, as
`"vectors": { "write-code": { "evaluation": "other" } }`. An agent named with
no command in `agents` is started by its name. In the default command,
`--tools` makes only the six tools it names available to the session, so the
session has no tool that starts a further agent, and `--allowedTools` lets the same
six run without asking, since no one is there to answer. `--tools` names the
agent's built-in tools: the tools of your own MCP servers stay as your own
configuration gives them. The command is yours to change. `reports` names, for an agent,
the fields of what it prints that give its cost, its calls and the unit of
the cost; the event log keeps them for each session, `show` adds them up and
says that the calls are the agent's own report, and no step depends on them.

A run has no limit unless the settings set one. `"limits": { "sessions": 10 }`
lets one run start at most ten sessions, and `"limits": { "minutes": 120 }`
start none after two hours; a run that reaches a limit ends as stopped, and
the next run goes on from there.

## Trying it without an agent: the stand-in

A run can be made with a stand-in agent that writes fixed files and calls no
language model:

```
stdo-builder run <workspace> --stand-in <fixtures>
```

The fixtures folder holds, for each step and kind of session
(`work` or `evaluation`), a folder `<fixtures>/<step>/<kind>/` with:

- `files/...`: files written into the workspace's folder at the same paths;
- `append`: text added to the end of the file the step writes (for the
  induction, the ticket);
- `seconds`: how long the session goes on after writing;
- `gate`: the path of a file the session waits for before it returns;
- `print`: the text the session prints;
- `fails`: the session fails after it has written and printed.

A step and kind with no folder is a session that cannot be started.

## What the commands exit with

0: done, or waiting for your answer or your ruling on what changed. 1:
stopped. 2: refused, or the command was not given what it needs. 4: the
workspace could not be read or written.

## Use it as a library

The command `stdo-builder` is a thin program over a library, which the
release carries and names as its entry. An application of your own may hold
the library instead of running the command. Make the installed folder,
`<folder>/lib/stdo-builder/<release>`, a dependency of your application under
the name `stdo-builder`, for example as `node_modules/stdo-builder`, and
import it:

```
import { setup, ticket, run, answer, show, registry, recordRelease } from "stdo-builder"

const said = await setup("<workspace>", { name: "<a name for the product>" })
console.log(said.words)
```

There is one function for each command. Each names the workspace by its path
or a `file:` URI, and gives a promise of `{ exitCode, words, result }`: the
exit code the command gives, what it prints, and the same result as data.

- `setup(workspace, { name, release })`: set up a product. `release` is the
  method release, `{ uri, manifest }`; where it is not given, `RELEASE`, also
  exported, is used.
- `ticket(workspace, words)`: write a ticket in your own words.
- `run(workspace, { ticket, standIn })`: start a run. `ticket` names the
  ticket to work on; `standIn` is a fixtures folder, as `--stand-in` gives.
- `answer(workspace, "yes" | "no", { reason, ruling, ticket })`: answer the
  question a run waits on, with the reason of a no and a ruling.
- `show(workspace)`: where the work stands.
- `registry(workspace)`: list the registry.
- `recordRelease(workspace)`: record the release that runs it as the one that
  builds the product.

Each gives the same result as the command, on the same workspace.
