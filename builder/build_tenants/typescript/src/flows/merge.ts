/**
 * Merging a ticket's work (REQ-FLOW-008), by git's three-way merge (C13), in
 * the workspace's own folder, which is on the ticket's branch (D240). Main is
 * the branch the ticket left, as the ticket records it. Main is taken into
 * the ticket's branch at the start of each run on it, and again where main has
 * moved by the time `done` says yes; the merge is of the whole tree, so main
 * that moved only outside the workspace's folder is taken in as well. When
 * `done` says yes on a branch that holds all of main, the ticket moves to the
 * done lane on the branch and main is moved to a merge of the branch's whole
 * tree with both as parents, and the folder put on main, with no file written.
 * Where git cannot merge a file by itself, the merge is left as git leaves it
 * and the run stops, naming the file. Nothing is reverted and no branch is
 * deleted.
 *
 * @uses C13 C14 C15 C17 H1
 * @is REQ-FLOW-008 REQ-FLOW-007 REQ-ALG-004
 */
import { decide, end, sequence, using } from "../kit/calculus.js"
import { covers } from "../kit/place_containment.js"
import { bindingOf, lineText, type TicketLine } from "../algorithms/facts.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import type { Flow } from "../services/services.js"
import { move } from "./branch.js"
import { outsideFiles, topOf } from "./changed.js"
import { committed, namedFrom } from "./commit.js"
import { note } from "./events.js"
import { addLines, at, frameworkPart, lineOf, ticketLines, ticketPath, type Fault, type Workspace } from "./workspace.js"

/** Main taken in, or why not: `refused` where git refused and took nothing in, as against a file it could not merge (REQ-FLOW-008). */
export type Taken = { readonly taken: "yes" } | { readonly stopped: string; readonly files?: readonly string[]; readonly refused?: true }

/** Files git names from the repository's top, by their path in the workspace where they lie in its folder; else from the repository's top, and said so. */
export const fromTop = (ws: Workspace, files: readonly string[]): readonly string[] => namedFrom(ws.within, files)

/** Where the user resolves files git could not merge, each given from the repository's top: in the workspace's folder, or where git left them in the repository where one lies outside it (D240). */
export const resolveWhere = (ws: Workspace, files: readonly string[]): string => {
  const them = files.length === 1 ? "it" : "them"
  const outside = ws.within !== "" && files.some((f) => !covers(ws.within, f))
  return `Resolve ${them} ${outside ? `where git left ${them} in the repository, and commit in the workspace's folder` : "in the workspace's folder, and commit there"}`
}

/**
 * Takes main into the ticket's branch, in the workspace's folder. Where the
 * user edited the active ticket on main since the branch last took main in,
 * the branch first takes the ticket as main has it, by git, and commits it:
 * the induction the branch added is no longer on it, so the ticket is
 * inducted and confirmed again (REQ-FLOW-004), and the user's edit never meets
 * the induction in a conflict. The change is the user's, so no stretch is
 * under way: after the merge the framework's lines the branch's ticket held
 * are added back, with `unbound at <commit>` where a binding held, as a run
 * killed while a session bound to a stretch was at work left it
 * (REQ-FLOW-004, D202). Where git will not write over what the user has not
 * committed or not added in a file main changed, nothing is taken in, and the
 * files are named (D240). The run's id names each entry, with main's name.
 */
export const takeMainIn = (ws: Workspace, ticket: string, run: string): Flow<Taken, Fault> =>
  using(Git, (git) => {
    const path = ticketPath("active", ticket)
    const line = lineOf(ticket)
    const edited: Flow<boolean, Fault> = decide(git.changedLines(ws.root, `HEAD...${ws.main}`), (changes): Flow<boolean, Fault> =>
      !changes.some((c) => c.path === path) ? end(false) : decide(git.textAt(ws.root, ws.main, path), (onMain) =>
        onMain === undefined ? end(false) : using(Files, (files) => files.exists(at(ws.root, path)))))
    // The framework's lines the branch's ticket holds, kept across the take-in of the user's edit (D202).
    const kept: Flow<string | undefined> = using(Files, (files) => files.read(at(ws.root, path)))
    const takeTicket: Flow<void, Fault> = sequence(
      git.takeFrom(ws.root, ws.main, path),
      decide(committed({ folder: ws.root, line }, `board: ${ticket} as the user edited it on ${ws.main}; it is inducted again`, [path]), (commit) =>
        commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: "the user edited the active ticket on main" }))
    )
    /**
     * After the merge, the branch's framework lines are added back, with the end of a binding that held, and committed (D202); a line the
     * ticket as main has it holds already, as the branch it left, is not added twice.
     */
    const restore = (before: string | undefined, merged: boolean): Flow<void, Fault> => {
      const lines = before === undefined ? [] : ticketLines(before)
      const b = bindingOf(lines)
      return lines.length === 0 ? end(undefined) : decide(git.tipOf(ws.root, line), (tip) =>
        decide(using(Files, (files) => files.read(at(ws.root, path))), (now) => sequence(
          addLines(ws.root, path, [
            ...lines.filter((l) => !new Set(frameworkPart(now ?? "").split("\n")).has(lineText(l))),
            ...(b !== undefined && b.ended === undefined && tip !== undefined ? [{ line: "unbound", commit: tip } satisfies TicketLine] : [])
          ]),
          merged
            ? decide(committed({ folder: ws.root, line }, `ticket ${ticket}: the framework's part kept after the user's edit`, [path]), (commit) =>
              commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: "the framework's part of the ticket, kept after the user's edit" }))
            : end(undefined)
        )))
    }
    const already: Flow<Taken, Fault> = sequence(note(ws.root, { event: "main taken in", run, ticket, main: ws.main, result: "already held", files: [] }), end({ taken: "yes" as const }))
    return decide(git.holdsAll(ws.root, ws.main), (holds): Flow<Taken, Fault> => holds ? already : decide(edited, (yes) =>
      decide(yes ? kept : end(undefined), (before) =>
      sequence(
        yes ? takeTicket : end(undefined),
        decide(git.takeInto(ws.root, line, ws.main, `merge ${ws.main} into ${line}`), (m): Flow<Taken, Fault> => {
          if (m.merged === "conflict") {
            // Each file by its path in the workspace, or from the repository's top where it lies outside the folder, and said so (D49, D240).
            const files = fromTop(ws, m.files)
            return sequence(
              yes ? restore(before, false) : end(undefined),
              note(ws.root, { event: "main taken in", run, ticket, main: ws.main, result: "conflict", files }),
              end({
                stopped: `git could not merge ${files.join(", ")} by itself when ${ws.main} was taken into the ticket's branch. ${resolveWhere(ws, m.files)}`,
                files
              })
            )
          }
          // A path main adds that is there already, a file or a folder git does not hold, ignored or not: nothing is taken in, and each is named, as for work not committed (REQ-FLOW-008, D250).
          if (m.merged === "refused" && m.inTheWay !== undefined) {
            const files = fromTop(ws, m.inTheWay)
            return sequence(
              yes ? restore(before, true) : end(undefined),
              end({ stopped: `${ws.main} is not taken into the ticket's branch, so that nothing of yours is written over: ${ws.main} adds ${files.length === 1 ? "a path" : "paths"} where you have a file or a folder that git does not hold, or that git ignores and would write over with no word, and none of it is in a commit: ${files.join(", ")}. Move it aside, then start a run again`, files, refused: true as const })
            )
          }
          if (m.merged === "refused") {
            const files = fromTop(ws, m.files ?? [])
            return sequence(
              yes ? restore(before, true) : end(undefined),
              end(files.length > 0
                ? { stopped: `git would not take ${ws.main} into the ticket's branch: ${ws.main} changed ${files.length === 1 ? "a file" : "files"} in which you have work not committed or not added: ${files.join(", ")}. Commit it or put it aside, then start a run again`, files, refused: true as const }
                : { stopped: `git would not take ${ws.main} into the ticket's branch: ${m.why}`, refused: true as const })
            )
          }
          return sequence(yes ? restore(before, true) : end(undefined), note(ws.root, { event: "main taken in", run, ticket, main: ws.main, result: m.changed ? "merged" : "already held", files: [] }), end({ taken: "yes" as const }))
        })
      ))))
  })

/**
 * The ticket merged, with, inside a larger repository, each file outside the
 * workspace's folder the merge took in, by its path from the repository's top
 * and what happened to it; or why not: `refused` where nothing was merged
 * because git refused or the branch left is checked out elsewhere
 * (REQ-FLOW-008).
 */
export type Merged = { readonly merged: string; readonly into: string; readonly outside?: readonly string[] } | { readonly stopped: string; readonly files?: readonly string[]; readonly refused?: true }

/**
 * Moves the ticket to the done lane on its branch and merges the branch into
 * main, the branch the ticket left and no other: main is moved to a commit of
 * the branch's whole tree with both as parents, and the folder is put on it,
 * with no file written (D240). Where main is checked out in another working
 * tree, nothing is done, the ticket not moved either, and the working tree is
 * named. Inside a larger repository, the files outside the folder the merge
 * took in are read from the commit main was on before the merge and the
 * merge's commit, by their names alone, and not from what was noted after
 * each session (REQ-FLOW-008 step 2, D256).
 */
export const mergeIntoMain = (ws: Workspace, ticket: string, run: string): Flow<Merged, Fault> =>
  using(Git, (git) =>
    using(Files, (files) => {
      const heldIn = (tree: string): Merged => ({
        stopped: `The branch the ticket left, ${ws.main}, is checked out in another working tree, a folder in which git has checked out a branch: ${tree}. Nothing is merged while it is. Put that working tree on another branch, or remove it with git worktree remove ${tree}, then start a run again`,
        refused: true
      })
      // What the merge took in outside the workspace's folder: none to read at the top of a repository (D256).
      const takenIn = (before: string | undefined, tip: string | undefined): Flow<readonly string[], Fault> =>
        ws.within === "" || before === undefined || tip === undefined
          ? end([])
          : decide(git.committedOutside(topOf(ws), ws.within, before, tip), (taken) => end(outsideFiles(taken)))
      // Where the branch left is checked out in another working tree, nothing is done: the ticket is not moved, so both working trees are as they were.
      return decide(git.heldElsewhere(ws.root, ws.main), (tree): Flow<Merged, Fault> => tree !== undefined ? end(heldIn(tree)) : sequence(
        // A run stopped after this move, or main returned to a commit before the merge, leaves the ticket done on the branch already.
        decide(files.exists(at(ws.root, ticketPath("active", ticket))), (active) => (active ? move(ws, lineOf(ticket), ticket, "active", "done", run) : end(undefined))),
        decide(git.tipOf(ws.root, `refs/heads/${ws.main}`), (before) =>
          decide(git.mergeInto(ws.root, ws.main, lineOf(ticket), `merge ${lineOf(ticket)}: ${ticket} is done`), (m): Flow<Merged, Fault> => {
            if (m.merged === "refused") return end(m.elsewhere !== undefined ? heldIn(m.elsewhere) : { stopped: `git would not merge the ticket's branch into ${ws.main}: ${m.why}`, refused: true })
            return decide(git.tipOf(ws.root, "HEAD"), (tip) =>
              sequence(
                note(ws.root, { event: "ticket merged", run, ticket, main: ws.main, commit: tip ?? "" }),
                decide(takenIn(before, tip), (outside) => end({ merged: tip ?? "", into: ws.main, ...(outside.length === 0 ? {} : { outside }) }))
              ))
          }))
      ))
    }))
