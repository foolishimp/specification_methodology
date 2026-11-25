/**
 * Where the work stands, and the registry (REQ-ALG-012, REQ-GRAPH-005). The
 * flow reads the board on main, the branch the active ticket left, by git
 * (D239); the tickets' branches; for each active ticket what its file on its
 * branch shows (`shownBy`: the vector delivered for the user's decision with
 * no answer after it, its question and when it was asked, and whether a
 * confirmation in it stands), the files each ticket changed (C13: main
 * against its branch, or what its merge brought) and one fold of the event
 * log (C10), and hands them to `stands`, which says for each wait whether the
 * ticket or the log gave it (D204). It reads no other record. It still
 * answers while the folder is not on the active ticket's branch, and says so,
 * naming both.
 *
 * It writes nothing: no file, and nothing into git's index or store (D242).
 * It runs no check. What changed while a session worked is listed through the
 * index of identities without writing it, and every other identity, of the
 * graph's declarations and of the ticket's text, is git's of a text with
 * nothing stored (`hash-object` without `-w`). Its git calls read lines,
 * commits and trees alone. Each command begins with `open` and refuses a
 * graph that is not `well_formed` (design, CALCULUS.md section 5).
 *
 * @uses C3 C4 C8 C10 C13 C14 C17 H5
 * @is REQ-FLOW-001 REQ-ALG-012 REQ-GRAPH-005
 */
import { listing, type Listed } from "../graph/registry.js"
import { awaiting, bindingOf, declaration, TICKET, type Snapshot } from "../algorithms/facts.js"
import { recordsOf } from "../algorithms/passes.js"
import { logStep, startOfLog, stands, type Standing, type TicketShows, type TicketView } from "../algorithms/stands.js"
import { fieldsOf } from "../kit/field_lines.js"
import { hereOf, onCommit, type Here } from "./gather.js"
import { linesChanged, questionFor } from "./question.js"
import type { Reason } from "../algorithms/well_formed.js"
import { decide, each, end, using } from "../kit/calculus.js"
import { Files } from "../services/files.js"
import { Hold } from "../services/hold.js"
import { Git } from "../services/git.js"
import { EventLog } from "../services/log.js"
import type { Flow } from "../services/services.js"
import { elsewhere, mainOf, placedOf, type Placed } from "./branch.js"
import { logOf } from "./events.js"
import { changedQuestion, compare, keptFor } from "./changed.js"
import { at, boardAt, boardOf, foundPath, holdOf, lineOf, LINES, linesRead, nodes, open, openWorkspace, ticketPath, userPart, vectors, type Fault, type Opened, type Workspace } from "./workspace.js"

const PREFIX = lineOf("")

type OpenRefused = Exclude<Opened, { readonly root: string }>
type View = readonly [string, TicketView]

/** `open`, the branches read, then the workspace judged `well_formed`, then `then` on the workspace and the branches. */
const opening = <A>(folder: string, then: (ws: Workspace, placed: Placed) => Flow<A, Fault>): Flow<A | OpenRefused | { readonly refused: readonly Reason[] }, Fault> =>
  decide(open(folder), (opened): Flow<A | OpenRefused | { readonly refused: readonly Reason[] }, Fault> =>
    "refused" in opened ? end(opened) : decide(placedOf(opened.root, opened.on), (placed) =>
      decide(openWorkspace(opened.root, mainOf(placed) ?? "HEAD", opened.within, opened.on), (ws): Flow<A | { readonly refused: readonly Reason[] }, Fault> => ("refused" in ws ? end(ws) : then(ws, placed)))))

/**
 * What an active ticket shows, read from its file alone, in the folder where
 * the folder is on its branch, else from its branch by git (REQ-ALG-012,
 * D204): the vector delivered for the user's decision with no
 * answer after it, with its question and when it was asked; and whether a
 * confirmation in it stands, by the identities git holds under its commit
 * and of the ticket's text now (`hash-object`), so no index is written (D76).
 */
const shownBy = (ws: Workspace, onBranch: boolean, name: string): Flow<TicketShows | undefined, Fault> =>
  using(Files, (files) =>
    using(Git, (git) =>
      decide(onBranch ? hereOf(ws, name) : end<Here>({ folder: ws.root, line: lineOf(name), ticket: ticketPath("active", name), name }), (here) =>
        decide(here.ticket === undefined ? end(undefined) : onBranch ? files.read(at(ws.root, here.ticket)) : git.textAt(ws.root, here.line, here.ticket), (written): Flow<TicketShows | undefined, Fault> => {
          if (written === undefined || here.ticket === undefined) return end(undefined)
          const ticketPathHere = here.ticket
          return decide(linesRead(ws.root, written), (lines): Flow<TicketShows | undefined, Fault> => {
          const first = ws.graph.graph.vectors.find((v) => v.first === true)
          const names = (vector: string): readonly string[] => {
            const v = vectors(ws).find((w) => w.name === vector)
            return v === undefined ? [] : recordsOf(ws.graph, v, "decision")
          }
          const delivered = awaiting(lines, names)
          const v = delivered === undefined ? undefined : vectors(ws).find((w) => w.name === delivered.vector)
          const b = bindingOf(lines)
          const stretch = b !== undefined && v?.first === true && b.ended?.line === "delivered" ? { inducting: { enters: b.bound.enters, ends: b.bound.ends } } : {}
          const seen: Snapshot = { identities: new Map(), ticket: { path: ticketPathHere, identity: "", ...stretch }, vectors: new Map() }
          // The lines changed are counted up to the commit the delivery names, as the run counted them (D211).
          return decide(v === undefined || delivered === undefined ? end(undefined) : linesChanged(ws, ws.root, v, delivered.commit), (counted): Flow<TicketShows | undefined, Fault> => {
          const asked = v === undefined || delivered === undefined ? undefined : {
            vector: v.name,
            asset: v.first === true ? TICKET : names(v.name).join(", "),
            question: questionFor(ws, v, seen, written, undefined, counted),
            ...(delivered.when === undefined ? {} : { when: delivered.when })
          }
          const confirmation = first === undefined ? undefined : lines.findLast((l) => l.line === "resolved" && l.by === "user" && l.at === first.name)
          // What changed while a session worked, where its identities are kept, the folder is on the ticket's branch and no run holds the ticket, listed with nothing written (REQ-ALG-012, D227, D242).
          return decide(!onBranch ? end(undefined) : using(Hold, (hold) => decide(hold.held([holdOf(ws.notes, name)]), (held) => (held.length > 0 ? end(undefined) : keptFor(ws, name)))), (kept) => decide(kept === undefined ? end(undefined) : compare(ws, here, kept), (c): Flow<TicketShows | undefined, Fault> => {
          const ruling = kept === undefined || c === undefined || "missing" in c || c.changed.length === 0 ? undefined : { ruling: { vector: kept.vector, question: changedQuestion(kept.vector, c.changed, kept.stood, ws.main) } }
          if (ruling !== undefined) return end({ inducted: true, ...ruling })
          if (first === undefined || fieldsOf(written).get("simplest") === "yes") return end({ inducted: true, ...(asked === undefined ? {} : { asked }) })
          if (confirmation === undefined || confirmation.line !== "resolved" || confirmation.says !== "yes") return end({ inducted: false, ...(asked === undefined ? {} : { asked }) })
          return decide(onCommit(ws, ws.root, confirmation.commit, name), (then) =>
            decide(git.identityOfText(ws.root, userPart(written)), (whole) =>
              end({ inducted: then !== undefined && then.get(TICKET) === whole && then.get(declaration(first.name)) === ws.declared.get(declaration(first.name)), ...(asked === undefined ? {} : { asked }) })))
          }))
          })
          })
        }))))

export const show = (folder: string): Flow<Standing | OpenRefused | { readonly refused: readonly Reason[] }, Fault> =>
  opening(folder, (ws, placed): Flow<Standing, Fault> => {
    const { root, main } = ws
    const off = elsewhere(placed)
    return using(Git, (git) =>
        using(EventLog, (log) =>
          // The board as the folder holds it, with what the user wrote and did not commit; main's, where the folder is on another branch.
          decide(off === undefined ? boardOf(root) : boardAt(root, main), (board) =>
            decide(git.linesNamed(root, [LINES]), (lines) => {
              const branches = lines.filter((b) => b.startsWith(PREFIX)).map((b) => b.slice(PREFIX.length))
              const active = each(board.active, (t): Flow<View, Fault> => {
                const has = branches.includes(t.name)
                return decide(has ? shownBy(ws, ws.on === lineOf(t.name), t.name) : end(undefined), (shows) =>
                    decide(has ? git.changedLines(root, `${main}...${lineOf(t.name)}`) : end([]), (changes) =>
                      end<View>([t.name, { ...(shows === undefined ? {} : { ticket: shows }), changes }])))
              })
              return decide(git.mergesOn(root, main), (merges) =>
                decide(active, (activeViews) =>
                  decide(each(board.done, (t): Flow<View, Fault> =>
                    decide(branches.includes(t.name) ? git.tipOf(root, lineOf(t.name)) : end(undefined), (tip) => {
                      const merge = tip === undefined ? undefined : merges.find((m) => m.parents[1] === tip)
                      const first = merge?.parents[0]
                      return decide(merge === undefined || first === undefined ? end([]) : git.changedLines(root, first, merge.commit), (changes) => end<View>([t.name, { changes }]))
                    })), (doneViews) =>
                    decide(log.fold(logOf(root), startOfLog(), logStep), (logged) =>
                      end({ ...stands({ graph: ws.graph, board, branches, views: new Map<string, TicketView>([...activeViews, ...doneViews]), foundOf: foundPath, ...(logged === undefined ? {} : { log: logged }) }), within: ws.within, ...(off === undefined ? {} : { elsewhere: off }) })))))
            }))))
  })

/** The registry of the governing graph: each graph function by name, with the nodes it writes, what it rests on and what it is for. */
export const registryOf = (folder: string): Flow<readonly Listed[] | OpenRefused | { readonly refused: readonly Reason[] }, Fault> =>
  opening(folder, (ws) => end(listing(ws.graph.registry, nodes(ws))))
