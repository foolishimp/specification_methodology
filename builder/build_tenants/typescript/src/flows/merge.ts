/**
 * Merging a ticket's work (REQ-FLOW-008), by git's three-way merge (C13).
 * Main is taken into the ticket's branch at the start of each run on it, and
 * again where main has moved by the time `done` says yes. Main that has moved
 * only outside the workspace's folder is held already, and is not taken in
 * (D201). When `done` says yes
 * on a branch that holds all of main, the ticket moves to the done lane on the
 * branch and the branch is merged into main. Where git cannot merge a file by
 * itself, the merge is left as git leaves it and the run stops, naming the
 * file. Nothing is reverted and no branch is deleted.
 *
 * @uses C13 C14 C15 C17
 * @is REQ-FLOW-008
 */
import { decide, end, sequence, using } from "../kit/calculus.js"
import { bindingOf, type TicketLine } from "../algorithms/facts.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import type { Flow } from "../services/services.js"
import { committed } from "./commit.js"
import { note } from "./events.js"
import { move } from "./ticket.js"
import { addLines, at, boardOf, checkoutPlace, laneOfTicket, lineOf, ticketLines, ticketPath, type Fault, type Workspace } from "./workspace.js"

export type Taken = { readonly taken: "yes" } | { readonly stopped: string; readonly files?: readonly string[] }

/**
 * Takes main into the ticket's branch, in its checkout. Where the user edited
 * the active ticket on main since the branch last took main in, the branch
 * first takes the ticket as main has it, by git, and commits it: the
 * induction the branch added is no longer on it, so the ticket is inducted
 * and confirmed again (REQ-FLOW-004), and the user's edit never meets the
 * induction in a conflict. The change is the user's, so no stretch is under
 * way: after the merge the framework's lines the branch's ticket held are
 * added back, with `unbound at <commit>` where a binding held, as a run killed
 * while a session bound to a stretch was at work left it (REQ-FLOW-004,
 * D202). The run's id names each entry.
 */
export const takeMainIn = (ws: Workspace, checkout: string, ticket: string, run: string): Flow<Taken, Fault> =>
  using(Git, (git) => {
    const path = ticketPath("active", ticket)
    const active = (folder: string): Flow<boolean> => decide(boardOf(folder), (board) => end(laneOfTicket(board, ticket) === "active"))
    const edited: Flow<boolean, Fault> = decide(git.changedLines(checkout, `HEAD...${ws.main}`), (changes): Flow<boolean, Fault> =>
      !changes.some((c) => c.path === path) ? end(false) : decide(active(ws.root), (onMain) => (onMain ? active(checkout) : end(false))))
    // The framework's lines the branch's ticket holds, kept across the take-in of the user's edit (D202).
    const kept: Flow<string | undefined> = using(Files, (files) => files.read(at(checkout, path)))
    const takeTicket: Flow<void, Fault> = sequence(
      git.takeFrom(checkout, ws.main, path),
      decide(committed({ folder: checkout, line: lineOf(ticket) }, `board: ${ticket} as the user edited it on ${ws.main}; it is inducted again`, [path]), (commit) =>
        commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: "the user edited the active ticket on main" }))
    )
    /** After the merge, the branch's framework lines are added back, with the end of a binding that held, and committed (D202). */
    const restore = (before: string | undefined, merged: boolean): Flow<void, Fault> => {
      const lines = before === undefined ? [] : ticketLines(before)
      const b = bindingOf(lines)
      return lines.length === 0 ? end(undefined) : decide(git.tipOf(checkout, lineOf(ticket)), (tip) =>
        sequence(
          addLines(checkout, path, [...lines, ...(b !== undefined && b.ended === undefined && tip !== undefined ? [{ line: "unbound", commit: tip } satisfies TicketLine] : [])]),
          merged
            ? decide(committed({ folder: checkout, line: lineOf(ticket) }, `ticket ${ticket}: the framework's part kept after the user's edit`, [path]), (commit) =>
              commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: "the framework's part of the ticket, kept after the user's edit" }))
            : end(undefined)
        ))
    }
    const already: Flow<Taken, Fault> = sequence(note(ws.root, { event: "main taken in", run, ticket, result: "already held", files: [] }), end({ taken: "yes" as const }))
    return decide(git.holdsAll(checkout, ws.main), (holds): Flow<Taken, Fault> => holds ? already : decide(edited, (yes) =>
      decide(yes ? kept : end(undefined), (before) =>
      sequence(
        yes ? takeTicket : end(undefined),
        decide(git.merge(checkout, lineOf(ticket), ws.main, `merge ${ws.main} into ${lineOf(ticket)}`, true), (m): Flow<Taken, Fault> => {
          if (m.merged === "conflict") {
            return sequence(
              yes ? restore(before, false) : end(undefined),
              note(ws.root, { event: "main taken in", run, ticket, result: "conflict", files: m.files }),
              end({
                stopped: `git could not merge ${m.files.join(", ")} by itself when main was taken into the ticket's branch. Resolve ${m.files.length === 1 ? "it" : "them"} in the ticket's checkout, ${checkoutPlace(ticket, ws.within)}, and commit there`,
                files: m.files.map((f) => `${checkoutPlace(ticket, ws.within)}/${f}`)
              })
            )
          }
          if (m.merged === "refused") return end({ stopped: `git would not take main into the ticket's branch: ${m.why}` })
          return sequence(yes ? restore(before, true) : end(undefined), note(ws.root, { event: "main taken in", run, ticket, result: m.changed ? "merged" : "already held", files: [] }), end({ taken: "yes" as const }))
        })
      ))))
  })

export type Merged = { readonly merged: string } | { readonly stopped: string; readonly files?: readonly string[] }

/** Moves the ticket to the done lane on its branch and merges the branch into main, leaving what the user has not committed outside what the merge changes as it is (D201). */
export const mergeIntoMain = (ws: Workspace, checkout: string, ticket: string, run: string): Flow<Merged, Fault> =>
  using(Git, (git) =>
    sequence(
      // A run stopped after this move, or main returned to a commit before the merge, leaves the ticket done on the branch already.
      decide(boardOf(checkout), (board) => (laneOfTicket(board, ticket) === "active" ? move(ws, checkout, ticket, "active", "done", run) : end(undefined))),
      decide(git.mergeInto(ws.root, ws.main, lineOf(ticket), `merge ${lineOf(ticket)}: ${ticket} is done`), (m): Flow<Merged, Fault> => {
        if (m.merged === "conflict") return end({ stopped: `git could not merge ${m.files.join(", ")} by itself into main`, files: m.files })
        if (m.merged === "refused") return end({ stopped: `git would not merge the ticket's branch into main: ${m.why}` })
        return decide(git.tipOf(ws.root, "HEAD"), (tip) => sequence(note(ws.root, { event: "ticket merged", run, ticket, commit: tip ?? "" }), end({ merged: tip ?? "" })))
      })
    ))
