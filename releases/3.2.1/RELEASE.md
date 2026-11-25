# STDO Builder 3.2.1, with the method's standards

This bundle holds release 3.2.1 of STDO Builder, in `builder/`, whose own note is `builder/RELEASE_NOTE.md`.
Beside it, in `standards/`, it holds release v3.1.0-rc.3 of the method's standards, `stdo://releases/v3.1.0-rc.3/`,
manifest sha256 2b3a7391dfb731219e64240199fe2e1b2736b9d5a44d030602fe7f07dd6c7a9a: the release set-up installs where the user names none.
To install it, read `INSTALL.md`.

## Licences

- STDO Builder's own files, in `builder/` but for `builder/lib/node_modules/` and `builder/licenses/`, and the files of this bundle at its top: the Apache License 2.0, in `LICENSE`.
- The method's standards, in `standards/`: the Apache License 2.0, in `standards/LICENSE`.

Each library STDO Builder's release ships keeps its own licence, which the release holds beside it in
`builder/licenses/<package>/`:

- @effect/platform-node 4.1.4, licence MIT
- @effect/platform-node-shared 4.1.4, licence MIT
- effect 4.1.4, licence MIT
- undici 8.12.4, licence MIT
- ws 8.23.0, licence MIT

## Put off

The requirement files mark these as put off, each in its own section:

- REQ-ALG-013 `collides : {branch, main, graph} → assets`: Deferred, with REQ-FLOW-009.
- REQ-FLOW-009 Several tickets at once: Deferred. It is built after the first build, as a ticket.
- REQ-INTERFACE-001 One library, instanced in four ways: Active for the library, the command-line program and an application of the user's own. The program that serves the commands as tools over the Model Context Protocol and the service with an API are Deferred: the user put them off on 23 November 2026, in ticket 261124-055459-1851.
- REQ-INTERFACE-002 A workspace is named by a URI: Active for a workspace on a mounted file system. A workspace reached through a service is Deferred: it is built after the first build, as a ticket.
- REQ-VERIFY-002 A scenario is driven by a user, on the installed product: Deferred: the user put it off on 23 November 2026, in ticket 261124-055459-1851.
- REQ-VERIFY-003 A scenario is judged from the workspace it leaves: Deferred: the user put it off on 23 November 2026, in ticket 261124-055459-1851.

## From the person who cut this release

Release 3.2.0 was reviewed in full on 23 November 2026. The verdict was no: 65 findings, four of them of severity 2 on a scale where 1 is the worst. Do not use 3.2.0 on real work. This release repairs those four and the findings that go with them. It does so by five rules.

1. A session is over when the framework has ended it. The framework knows a process to be of a session it started by its parent, by its process group or by a mark in its environment, and ends each one it knows when the session returns, is cut off or runs out of time. A process it cannot place is named to the user, and the run is cut off. One kind of process it does not find; the instructions say which, and what follows from that.
2. What changed while a session worked is put to the user. Each file that git does not ignore and that differs in the folder outside what the step writes is asked about, and the user rules before anything of the step is judged or committed. So is each file of the folder that main, the branch the ticket left, gained in that time, by a session or by you, before any of it is taken into the ticket's branch. What else changed among the repository's branches, tags and stash is named. Inside a larger repository, so is what changed outside the folder, and what was committed there: on the ticket's branch, which the ticket's merge takes into main and names again when it does, and on main. The limits of this rule are listed under "Not repaired here".
3. Where the framework cannot tell what changed while a session worked, it asks. Its notes on a session lie under git's own directory, which no cleaning of the folder reaches. Where they cannot serve all the same, the commit the session started from stands in for them, and every file that differs from it is put to the user.
4. A ticket is built in the workspace's own folder, on a branch of its own. There is no second folder. The ticket records the branch it left, and is merged into that branch and into no other.
5. A release is cut by one command, which says only what it has read or checked. The bundle carries the method's standards as release v3.1.0-rc.3, the exact cut of the public 3.1.0 line; 3.2.0 carried the earlier rc.2. The download installs where tar keeps every member as a file, as on Linux.

Two reviews of this release's own candidate said no, on 24 and 25 November 2026, and two more gaps were found by trial between them. Each is repaired here.

- A session that cleaned the folder removed the framework's notes with it, and what it had changed outside its step was committed with no question. The third rule repairs it.
- A session that changed a file outside its step, committed the change itself and pruned git's store got it to main with no question. The commit the session started from now stands in, so what a session commits on the ticket's branch is asked about too.
- A session that put the folder on main and committed there got what it had changed into the ticket when main was next taken in, with no question. What main gains in the folder while a session works is now asked about before any of it is taken in.
- Inside a larger repository, a session that gave `git add -A` and `git commit` committed what you had not committed outside the product's folder, and the ticket's merge took it into main with nothing said. The run now names it, the merge names it again, and each session is told that the folder lies inside a larger repository.
- The pages held sentences that the product did not bear out. Each is put right, in the product or in the page. The product now refuses an older git, and a machine without `ps`, before it starts anything. It refuses to take main into a ticket's branch where main adds a path at which you have a file or a folder that git ignores, which git's own merge would write over with no word.

The third of these repairs was the last made, and a fresh reviewer checked it alone on 25 November 2026. The repair holds. The verdict was still no, for sentences the repair had added to the instructions, which did not say what the product does; they are put right. That check also found one more gap, of lesser weight, which is not repaired here: it is the first under "Know of these" below.

The reports, and what was done with each finding, are in `builder/.ai-workspace/comments/` of the source: `fable/20261124T075040Z_REVIEW_3.2.1_candidate.md` and `claude/20261124T080500Z_TRIAGE_review_of_3.2.1_candidate.md` for the first review, `fable/20261124T210537Z_REVIEW_3.2.1_candidate_2.md` and `claude/20261124T213314Z_TRIAGE_second_review_of_3.2.1_candidate.md` for the second. The check of that one repair is `fable/20261125T030203Z_REVIEW_3.2.1_repair_of_Q-1.md`; what was done with its four findings is written in the ticket, `builder/.ai-workspace/tickets/completed/261125-083337-0fdf-what-the-branch-a.md`.

What it needs. Node.js 24 or later; git 2.38 or later, for every product; the program `ps`, which on Debian and Ubuntu comes with the package procps; the method's release manager `stdo`; and an agent that runs from the command line.

What one folder costs. While a ticket is active the folder is on the ticket's branch. Inside a larger repository the whole repository is on it. Whatever is committed there meanwhile, by anyone, reaches main when the ticket is merged. Two products in one repository cannot each hold an active ticket at the same time. A session works among the files that git ignores in the folder, your local settings and dependencies among them: it can read them, and what it removes is removed. The event log is one of the files git ignores, so a cleaning of the folder removes it, and the next run starts a new one. Inside a larger repository a session's git commands act on the whole of it: `git reset --hard` given by a session loses what you have not committed outside the folder too, and the run can only name the files afterwards. And where a session commits on main work of yours that you had not committed, that commit alone holds it: before you say no to it and move main back, take your work out of the commit.

Coming from 3.2.0. Finish or put back every active ticket with 3.2.0 before you install this release. A checkout that 3.2.0 left under `.stdo-builder/local/checkouts/` is yours to remove, with `git worktree remove <path>`.

Not repaired here. Two groups of findings wait for the next release. The first is what a step does first: after a change by hand, a cut-off session or an evaluation's no, the framework sometimes starts a session where it should ask the user. The second is what the user is told, and small repairs. Know of these before you rely on the release:

- Withdraw a ticket or put it back only when no session works on it and no ruling on what changed is awaited. At another time the ruling cannot be given: the answer is refused, and so is each run until the folder is on the branch the ticket left. Putting it there carries what the session left uncommitted, and the next run commits it there as your change by hand, with no question. Set it aside first (`git stash -u`), or undo that commit with `git revert`.
- Three changes the comparison does not reach, each committed with no question. A folder that is a git repository of its own, as `git clone` inside the workspace leaves: the framework commits a pointer to it, which a clone of your product cannot follow, and none of its files. A file that a session takes out of git's index and has git ignore: it leaves the ticket's branch, and so main, and stays in your folder. And a change of a file's mode alone.
- A symbolic link to a folder, or one whose target is not there, that appears while a session works stops the run with git's own words, until you remove the link or have git ignore it.
- Where a session rewrites the commit it started from, expires git's reflog and prunes, the run stops and says it cannot compare; the run after it goes on, and what that session changed outside its step is not asked about.
- A session that pushes to your remote is not named. Nor is one that changes git's own settings for your repository, leaves a hook there or adds an exclusion.
- On a disk that folds case, as macOS has by default, where main adds a file whose name differs only in case from a file of yours that git ignores, main is taken in and your file is written over, as git's own merge would.
- Where a run names a process, it gives the command line as `ps` prints it. For a process that has rewritten its own title that can carry entries of the process's environment, a secret among them, and the words go to the terminal and into the event log.

Where each of the 65 findings goes is written in `builder/.ai-workspace/comments/claude/20261123T075500Z_TRIAGE_full_review_of_3.2.0.md` of the source.

The history page that 3.2.0 carried is not in this bundle: it says that 3.2.0 is not yet published, and is not yet brought up to this release. It is in the public repository, as `history.html`.

Set-up fetches the method's standards from the public repository, so a machine with no network cannot set a product up. The standards inside the bundle are for reading.
