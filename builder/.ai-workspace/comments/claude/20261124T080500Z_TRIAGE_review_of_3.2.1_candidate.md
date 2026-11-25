# Triage of the review of the 3.2.1 candidate

Commentary, not law. Author: Claude, as Executive. Date: 24 November 2026.

Subject: the report `../fable/20261124T075040Z_REVIEW_3.2.1_candidate.md`, by
a fresh reviewer at maximum effort, on build 3.2.1-rc.4 (source `873aaebeb`).
Triage under "Review findings" of `specification/REFERENCE_FRAME_BASIS.md`.
Severity is the reviewer's grade, from 1, the highest, to 5, and is not
changed here.

**Verdict: no. 3.2.1 is not cut.**

The four findings of severity 2 of release 3.2.0 (C-1, G-1, R-1, R-2) are each
repaired as found: the reviewer saw each go wrong on 3.2.0 and go right on the
candidate. The claim fails on one new finding of severity 2, V-1, and on pages
that say what the product does not do.

## Words

- **Workspace**: the folder that holds the product being built.
- **Session**: one start of the agent on one step of a ticket.
- **Ruling**: the user's yes or no on what changed while a session worked,
  outside what its step writes.
- **The framework's notes on a session**: two files it writes when a session
  starts. One names the state of the folder at that moment, so it can tell
  afterwards what changed. The other, the hold, says that a run is at work on
  the ticket; a hold left behind is how the next run knows that a run was cut
  off.

## 1. V-1, and why it was missed

The framework keeps its notes on a session in `.stdo-builder/local/`, a
folder git ignores. Since ticket W the session works in the folder that holds
them. A session that removes what git ignores, as `git clean -fdx` does for a
clean build, removes the notes too. The framework then cannot tell what the
session changed, says one sentence ("cannot tell … and goes on"), and commits
all of it. Where the run is also interrupted, the next run says nothing and
commits it as "what the user changed by hand".

I ran the reviewer's trial again myself. Without the clean, the run asks for a
ruling and commits nothing. With the clean, the session's three changes
outside its step (the graph's check set to `true`, a line in `AGENTS.md`, a
stray file) reached main with no ruling.

Why it was missed. The fault is mine, in two steps.

1. My words for ticket P accepted this as a limit: "Where they are missing,
   the framework cannot tell what the session changed, says so, and goes on."
   That was safe then: a session worked in a folder apart and could not reach
   the notes.
2. Ticket W put the session in the folder that holds the notes. I did not
   read P's accepted limits again against that change, and my trial of W had
   no case of a session that cleans.

## 2. Findings

Priority: **1** is repaired before the cut of 3.2.1. All items are open.

| Id | Sev | Finding | Pri | Goes to |
|---|---|---|---|---|
| V-1 | 2 | A session that removes the files git ignores removes the framework's notes on it; what it changed outside its step is committed and merged with no ruling | 1 | Ticket V |
| V-2 | 3 | The install page says git 2.31 is enough; the product needs 2.38, and the refusal on an older git does not name the cause | 1 | Ticket Y |
| V-3 | 4 | A session's process that sheds its parent, its group and the mark is neither ended nor named, wherever it works; the requirement states only the kind that works outside the folder | 1 | Ticket Y, in the words: the framework cannot tell such a process from a job of the user's own |
| V-4 | 4 | Taking main in writes over a file of the user's that git ignores, with no word | 1 | Ticket Y: the run refuses and names the file, as the page says |
| V-5 | 5 | A command not given what it needs exits 1; the page says 2 | 1 | Ticket Y |
| T3 | 5 | Already recorded by me: a file the user staged outside the folder is in the commit that completes a merge of main the user resolved; the page says it is left | 1 | Ticket Y, in the words |
| U-8 | 5 | Already recorded by me: the bundle's install exits 6 where its page says 2 | 1 | Ticket Y |

The reviewer judged none of my recorded items for tickets E and U to be of
severity 1 or 2.

## 3. The repair

Two tickets, each one rule, built with the candidate itself. Then a fresh
reviewer checks the repair of V-1 again, because it touches guard rail 1.

**Ticket V. Where the framework cannot tell what changed while a session
worked, it asks; it never goes on.** Two parts.

1. The framework's notes on a session lie under git's own directory of the
   repository, where no cleaning reaches. Measured on this machine with git
   2.50.1: a file there is left alone by `git clean -fdx`, `git clean -fdX`,
   `git stash -a`, `git gc --prune=now`, `git repack -ad`, `git prune`,
   `git reset --hard`, `git maintenance run` and `git worktree prune`;
   `git fsck` and `git status` say nothing of it; a clone does not carry it.
   `git stash -a` and both cleans empty `.stdo-builder/local/`.
2. Where the notes are missing all the same, the commit the folder is on
   stands in for them and every file not committed is put to the user. This
   is already the rule for a run that was cut off (REQ-FLOW-003, step 1).

**Ticket Y. A page of the release says only what the product does.** The six
items of priority 1 above after V-1, the paragraph on coming from release
3.2.0, and one sentence the pages lack: a session works in the user's own
folder, so what it removes there is removed, the files git ignores among
them.

## 4. For the product owner

1. **Ticket V puts two small files of the framework under the repository's
   `.git/`.** For a product inside a larger repository that is outside the
   workspace's folder, so the requirement's law "The framework keeps nothing
   outside the workspace" now names this one exception. No sentence of the
   intent or of the product definition is touched: the two files are notes,
   and no proof (guard rail 4). It is my decision, and yours to overrule. The
   other way keeps everything in the folder and asks you about every
   uncommitted file after any cleaning; it is weaker where a session both
   commits its own changes and cleans.
2. **The event log lies in the same ignored folder.** A clean by a session or
   by you removes it, and the run starts a new one. No decision of the
   framework rests on the log, so this is a loss of history and not a hole
   like V-1. The reviewer leaves to you whether it breaks guard rail 6 ("is
   only added to"). The intent's model says the log is "kept in the
   workspace", so it cannot follow the notes into git's directory. Within the
   intent there are two ways: leave it where it is and say in the pages that
   a cleaning removes it, or commit it, which is your open decision on
   whether the log travels with the repository. Ticket V makes the run say so
   when the log it was adding to is gone; ticket Y says the first in the
   pages. (Corrected at 19:37: I first recommended moving the log beside the
   notes, against that sentence of the intent.)
3. **One folder exposes your ignored files to a session.** Before ticket W a
   session worked in a folder apart, which held none of them. Now a session's
   `git clean -fdx` removes your `.env` or your `node_modules`, and the
   framework, which compares only what git does not ignore, names nothing.
   A session can read them too. This follows from one folder. Ticket Y says
   it in the pages and tells each session that such files are not its own to
   remove.
4. **Linux, run by me on 24 November in a clean Debian container.** With
   `ps` installed the candidate installs from the download, walks the
   getting-started guide to its end and passes the session-process cases as
   on macOS. A minimal image has no `ps`, and no page names it as needed:
   there the first run spends its session and is then cut off with a raw
   error. Finding L-1, mine, severity 3. It goes into ticket Y: the pages
   name `ps`, and a run is refused before any session where it cannot read
   the process table.

## 5. What the review did not cover

By the reviewer's own account: the tenant's whole check (it passed on
`ed87712e9`, 814 tests), the release command, a session of a real agent, a
real older git (V-2 rests on a stand-in), Linux, the upgrade from 3.2.0 with
a ticket under way, a product in a linked working tree or with submodules.
It read twelve source files in full and the tests and design pages not at
all. I ran a real agent end to end on the candidate (a hello product inside a
larger repository, ticket to merge). The run on a clean Linux machine is done
once on this candidate (section 4, item 4) and is to be repeated on the final
one.
