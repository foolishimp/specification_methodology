# Triage of the second review of the 3.2.1 candidate (build 3.2.1-rc.7)

**Release 3.2.1 is not cut.** The second review's verdict is no. One finding of severity 2 is open, Q-1, and the review rule lets no phase close with one open. The report is `builder/.ai-workspace/comments/fable/20261124T210537Z_REVIEW_3.2.1_candidate_2.md`. Severity runs from 1, the worst, to 5. Every severity below is the reviewer's and is not changed.

What the review confirmed: finding V-1 of the first review is repaired; tickets Z, X and Y do what they state; the four tickets brought in no defect of severity 1 or 2 and their work breaks no guard rail. Q-1 was already there on the first candidate. It has been open since a session works in the user's own folder.

## Each finding, and what happens with it

| Finding | Severity | What it is | What happens |
|---|---|---|---|
| Q-1 | 2 | A session that puts the folder on main and commits there gets what it changed outside its step into the ticket, judged and merged, with no ruling asked. Main is the branch the ticket left. | **Repaired before the cut**, by one ticket. Its rule: what the branch a ticket left gained while a session worked is put to the user, who rules before any of it is taken into the ticket's branch. Then a new candidate, my trials again, and a fresh reviewer's check of this repair alone, since it touches guard rail 1. |
| Q-2 | 3 | A git repository of its own that a session leaves in the folder is never put to the user. The framework commits a pointer to it that no clone can follow. | **Put off to 3.2.2.** The repair is that the framework commits exactly what it compared. That changes the code under every commit the framework makes, and closes Q-6 and the change of a file's mode as well: too wide for a repair round. It is bounded: it needs a session that makes or clones a repository inside the folder, and nothing of the user's is lost. Stated as a limit in the instructions, by the Q-1 ticket, and in the release's note. |
| Q-3 | 3 | The release's note, and one sentence of the instructions, promise what Q-1 and Q-2 show the product does not do. | The note's two sentences are bounded at the cut. For main they become true by Q-1's repair. The instructions' sentence is bounded by the Q-1 ticket, which states the three cases the comparison does not reach. |
| Q-4 | 4 | The note says the framework knows every process of a session. It does not, and the instructions say which it misses. | The note's sentence is corrected at the cut. |
| Q-5 | 4 | A symbolic link to a folder, or one whose target is not there, that appears while a session works stops the run with git's own words. No page says so. | The instructions say so, with the way round, by the Q-1 ticket. The behaviour is put off to 3.2.2 with Q-2's repair: the stop errs on the safe side. |
| Q-6 | 4 | A file a session takes out of git's index and has git ignore is removed from the ticket's branch and from main with no question. | **Put off to 3.2.2**, with Q-2: the same repair. Stated as a limit in the instructions and in the note. |
| Q-7 | 5 | A session's changes to git's settings, hooks and exclusions are named by no run. | Put off to 3.2.2, with the push that is not named. Named in the note. |
| Q-8 | 5 | Nine small things in the note and the pages. | a, b and c are in the note: corrected at the cut. d to i go to 3.2.2. |

Three more things the reviewer graded or remarked:

- **The loss of an ignored file on a disk that folds case** (my Y-1). The reviewer grades it 4; I had 5. The reviewer's grade stands. It is put off to 3.2.2 and named in the note, as before.
- **The limit of ticket Z** (a session that rewrites the commit it started from, expires git's reflog and prunes). The reviewer grades it 3, as I did. It is put off to 3.2.2; the ticket's words are drafted. Two remarks go with it: the stop's own words tell the user to start the run that lets the change through, and git shows the rewritten commit under the framework's name.
- **Ticket X.** The run says what the ticket's merge will take in from outside the folder. It does not say what to do if that is not wanted. To 3.2.2, with the other words.

Left to the owner, as before: that the framework's notes on a session lie under git's own directory, which inside a larger repository is outside the workspace's folder; and that a cleaning of the folder removes the event log.

## Why one more road was found, and what stops the next

Four findings in a row were roads to one consequence: what a session changes outside its step reaches main with no ruling. They are V-1 (a cleaning of the folder), the finding behind ticket Z (a session's own commit and a prune), the one behind ticket X (a commit outside the folder) and Q-1 (a commit on main). Each was found by trial, one at a time.

I have now listed every way content reaches a ticket's branch or main, and what guards each:

1. The framework's own commit of the folder after a session. Guarded by the comparison with the session's start. The comparison and the commit read the folder by two different listings, and where the two disagree a change passes: Q-2, Q-6 and a change of mode.
2. A session's own commit on the ticket's branch. Guarded since ticket Z, but for its stated limit.
3. A session's commit on main, by any means: a checkout, a second working tree, a fetch into main, a branch moved by hand. Then main is taken into the ticket's branch. **Not guarded: Q-1.** The repair guards the take-in, so it covers every one of these means.
4. A session's commit on any other branch. No act of the framework carries it further.
5. The ticket's merge into main. It carries only what 1 to 3 let onto the ticket's branch.

After Q-1's repair the open roads are the stated limits: Q-2, Q-6, a change of mode, the files git ignores, a process that has left its parent, and the limit of ticket Z. The first three close at their root with one rule in 3.2.2: the framework commits exactly what it compared. My trials of the new candidate try each means under 3.

## Changes to the release's note at the cut

- Rule 1: "knows every process" becomes what the product does (Q-4).
- Rule 2 and the sentence "so what a session commits is asked about too": bounded, and the three cases the comparison does not reach are named (Q-3).
- "The instructions say this in full" goes (Q-8 a). "The event log lies among them" is said plainly (Q-8 b). The sentence on this review is replaced by its result (Q-8 c).
- Added under what to know of: Q-2, Q-6, Q-7.
- Two additions of my own, found while the review ran. The bundle of 3.2.0 carried the history page and this one does not: the committed page says 3.2.0 is not yet published, and the changed copy in the owner's folder is another session's. And a process a run names is given as `ps` prints it, which for a process that has rewritten its own title can carry entries of its environment, into the terminal and the event log.
