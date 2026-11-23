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

- Node.js 24 or later, and git, on your PATH;
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
folder. Everything the framework does for the product concerns only files under
it: each file it writes, each commit and merge it makes and each identity it
reads. It leaves every other file of the repository as it is, and what you have
not committed or have staged elsewhere in it, and changes none of the
repository's other branches.

- Main is the branch the repository's own folder has checked out, whatever its
  name. A ticket's branch is a branch of the repository, made from main and
  merged into it.
- A ticket's checkout, under `.stdo-builder/local/checkouts/<ticket>/`, holds
  the folder alone, at its place from the repository's top: for a folder
  `apps/product`, the ticket's workspace is
  `.stdo-builder/local/checkouts/<ticket>/apps/product/`. The agent works there.
- Where main has moved only outside the folder, nothing is taken into the
  ticket's branch, and it is no change to the product.
- A file you commit outside the folder on a ticket's branch stays on that
  branch: the merge into main takes the folder alone, and outside it main keeps
  its own files.
- Git keeps the history, the branches and the record of each checkout where it
  keeps them for the whole repository.
- It needs git 2.38 or later.

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
  is merged into main;
- waiting for your answer;
- stopped: it names the step and why;
- refused before any step: it says why, for example that a run is already at
  work, that there is nothing to build, or that another release of STDO
  Builder is recorded as the one that builds the product.

Where a session failed in the run, the run names where what it printed is
kept: the last of each step and kind of session, under
`.stdo-builder/local/printed/` in the ticket's checkout.

All work on a ticket is done on a branch of its own, `stdo/<ticket>`, in a
checkout at `.stdo-builder/local/checkouts/<ticket>/`. Open that folder to see
the work while it is under way. Only one run works on a ticket at a time.

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

To have the release you now run build the product, for example after you
install a new one, give this command with it. It writes that release in place
of the one recorded, changes nothing else, and commits nothing: the next run
commits it as your change on main. You may also edit the record by hand; it is
read as it stands.

## When a run stops

- A step could not close: its evaluation said no as many times as the graph
  allows attempts, its working sessions did not leave fewer checks failing
  each time, or two sessions on it failed in a row. The run names
  the checks that did not pass and where what they found is kept. Change what
  needs changing, by hand or by editing the ticket to give direction, and
  start a run again. Nothing is undone for you, and nothing is put back.
- A session changed files it may not: the run names them. Nothing is put
  back. Put any of them right if you want, and start a run again; it goes on
  from the workspace as it is.
- git could not merge a file: resolve it where the run says, commit there,
  and start a run again.

To withdraw a ticket, delete its file on main. To put one back, move it to the
backlog. To change what you asked, edit the ticket on main; to change its
steps, edit them in the ticket's file that the question names. Either change
is yours, and you are asked to confirm the whole ticket again. Where the
ticket no longer passes the induction's checks, its steps among them, the
induction runs again first, and the question says so.

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

- `files/...`: files written into the ticket's checkout at the same paths;
- `append`: text added to the end of the file the step writes (for the
  induction, the ticket);
- `seconds`: how long the session goes on after writing;
- `gate`: the path of a file the session waits for before it returns;
- `print`: the text the session prints;
- `fails`: the session fails after it has written and printed.

A step and kind with no folder is a session that cannot be started.

## What the commands exit with

0: done, or waiting for your answer. 1: stopped. 2: refused, or the command
was not given what it needs. 4: the workspace could not be read or written.

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
