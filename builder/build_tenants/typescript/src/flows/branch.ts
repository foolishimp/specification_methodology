/**
 * The branch the folder is on, the active ticket and main (REQ-FLOW-001,
 * REQ-FLOW-003 step 1, REQ-FLOW-004 "Pull", REQ-FLOW-006, REQ-ALG-012; D239).
 *
 * A ticket is built in the workspace's own folder, on a branch of its own:
 * there is no second folder. When it is pulled, the ticket records the branch
 * the folder is on as the branch it left, which is main for it until it is
 * merged; the framework reads that name from the ticket, never again from the
 * folder. The active ticket is found by the branches the framework made for
 * tickets, local or remote, whichever branch the folder is on: a ticket whose
 * branch holds it in the active lane, or in the done lane before its merge,
 * and which lies in the active lane of the
 * branch it left; or, where it records none, as one an earlier release pulled,
 * of the branch the folder is on. Each is read from git by a name and a path,
 * never from a folder.
 *
 * While a ticket is active, a command that writes is refused unless the folder
 * is on the ticket's branch, and the refusal names both branches; a run takes
 * the branch up where it can: in a clone that has it only as a remote branch,
 * and for a ticket that records no branch it left. Where no ticket is active,
 * main is the branch the folder is on, and a run is refused where the folder
 * is on a branch the framework made for a ticket, or on none.
 *
 * @uses C13 C14 C17 H1 H2
 * @is REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-006 REQ-FLOW-007 REQ-ALG-010 REQ-ALG-012
 */
import { decide, each, end, sequence, using } from "../kit/calculus.js"
import { byName } from "../kit/order_by_name.js"
import { covers } from "../kit/place_containment.js"
import { Git } from "../services/git.js"
import type { Flow } from "../services/services.js"
import { committed } from "./commit.js"
import { note } from "./events.js"
import { Files } from "../services/files.js"
import { addLines, at, leftIn, LINES, lineOf, ticketPath, type Fault, type Lane, type Workspace } from "./workspace.js"

/** An active ticket, as its branch and the branch it left show it. */
export interface Active {
  readonly name: string
  /** The ticket's branch. */
  readonly line: string
  /** The branch it left, where it records one. */
  readonly left?: string
  /** Where the repository has the ticket's branch only as a remote branch, that branch's full name. */
  readonly remote?: string
  /** Where it has the branch left only as a remote branch, that branch's full name. */
  readonly leftRemote?: string
  /** The repository has no branch of the name the ticket records it left, local or remote. */
  readonly leftMissing?: true
}

/** The branch the folder is on, where it is on one; the active tickets, the first by name first; and the tickets in the active lane of the commit the folder is on that have no branch at all. */
export interface Placed {
  readonly on?: string
  readonly active: readonly Active[]
  readonly unbranched: readonly string[]
}

const HEADS = "refs/heads/"

/** The active tickets and the branch the folder is on, read from git alone (D239). */
export const placedOf = (root: string, on: string | undefined): Flow<Placed, Fault> =>
  using(Git, (git) =>
    decide(git.linesNamed(root, [LINES]), (local) =>
      decide(git.remoteLines(root, [LINES]), (remote) => {
        const ticketOf = (line: string): string | undefined => (line !== LINES && covers(LINES, line) ? line.slice(LINES.length + 1) : undefined)
        const names = byName(new Set([...local, ...remote.keys()].flatMap((l) => {
          const t = ticketOf(l)
          return t === undefined ? [] : [t]
        })))
        const refOf = (line: string): string => (local.includes(line) ? `${HEADS}${line}` : remote.get(line) ?? `${HEADS}${line}`)
        // On its branch the ticket lies in the active lane, or in the done lane where a run stopped between that move and the merge.
        const lanes = ["active", "done"] as const
        return decide(git.presentAt(root, names.flatMap((n) => lanes.map((lane) => [refOf(lineOf(n)), ticketPath(lane, n)] as const))), (onBranch) => {
          const inLane = names.flatMap((n, i) => {
            const lane = lanes.find((_, j) => onBranch.has(i * lanes.length + j))
            return lane === undefined ? [] : [[n, lane] as const]
          })
          return decide(each(inLane, ([n, lane]) => decide(git.textAt(root, refOf(lineOf(n)), ticketPath(lane, n)), (text) => end([n, leftIn(text ?? "")] as const))), (found) => {
            const lefts = [...new Set(found.flatMap(([, l]) => (l === undefined ? [] : [l])))]
            return decide(lefts.length === 0 ? end([] as readonly string[]) : git.linesNamed(root, lefts), (leftLocal) =>
              decide(lefts.length === 0 ? end(new Map<string, string>()) : git.remoteLines(root, lefts), (leftRemote) => {
                const leftRef = (l: string): string | undefined => (leftLocal.includes(l) ? `${HEADS}${l}` : leftRemote.get(l))
                const asked = found.map(([n, l]) => [l === undefined ? "HEAD" : leftRef(l) ?? `${HEADS}${l}`, ticketPath("active", n)] as const)
                return decide(git.presentAt(root, asked), (activeThere) =>
                  decide(git.tipOf(root, "HEAD"), (head) =>
                    decide(head === undefined ? end([] as readonly string[]) : git.namesAt(root, "HEAD", ticketPathFolder), (inHead) => {
                      const active = found.flatMap(([n, l], i): readonly Active[] => {
                        const missing = l !== undefined && leftRef(l) === undefined
                        if (!missing && !activeThere.has(i)) return []
                        return [{
                          name: n,
                          line: lineOf(n),
                          ...(l === undefined ? {} : { left: l }),
                          ...(local.includes(lineOf(n)) ? {} : { remote: refOf(lineOf(n)) }),
                          ...(l === undefined || leftLocal.includes(l) || leftRemote.get(l) === undefined ? {} : { leftRemote: leftRemote.get(l) ?? "" }),
                          ...(missing ? { leftMissing: true as const } : {})
                        }]
                      })
                      const unbranched = inHead.filter((f) => f.endsWith(".md")).map((f) => f.slice(0, -".md".length)).filter((n) => !names.includes(n))
                      return end({ ...(on === undefined ? {} : { on }), active, unbranched })
                    })))
              }))
          })
        })
      })))

/** The active lane's folder, which the commit the folder is on is read at. */
const ticketPathFolder = ticketPath("active", "x").slice(0, -"/x.md".length)

/** Main for the command: the branch the active ticket left, or, where none is active or it records none, the branch the folder is on (REQ-FLOW-001). */
export const mainOf = (placed: Placed): string | undefined => placed.active[0]?.left ?? placed.on

/** The words where a ticket is active and the folder is not on its branch, naming both (REQ-FLOW-001); none where it is, or none is active. */
export const elsewhere = (placed: Placed): string | undefined => {
  const a = placed.active[0]
  if (a === undefined || placed.on === a.line) return undefined
  return `The ticket ${a.name} is active and is built on its branch, ${a.line}, and the folder is ${placed.on === undefined ? "on no branch" : `on the branch ${placed.on}`}. A run and an answer are refused, and so is every command that writes in the workspace, until the folder is back on ${a.line}: git switch ${a.line}`
}

/** What a run's look at the branch gives: main, where it may go on, with the folder on the active ticket's branch where one is active; or why it is refused. */
export type TakenUp = { readonly main: string; readonly on: string } | { readonly refused: string }

/** The words where the ticket's branch is checked out in another working tree: that tree, with the command that removes it (REQ-FLOW-003 step 1). */
const heldIn = (line: string, elsewhere: string): string =>
  `The ticket's branch, ${line}, is checked out in another working tree, a folder in which git has checked out a branch: ${elsewhere}. A checkout an earlier release left is the user's to remove; remove it with git worktree remove ${elsewhere} (add --force where it holds work you do not want), then start a run again`

/** The words where git would not put the folder on a branch: the working tree that has it, with the command that removes it, or what git names (REQ-FLOW-003 step 1). */
const switchRefused = (line: string, s: { readonly refused: string; readonly elsewhere?: string }): string =>
  s.elsewhere !== undefined ? heldIn(line, s.elsewhere) : `git would not put the folder on the ticket's branch, ${line}: ${s.refused}`

/**
 * A run's look at the branch the folder is on (REQ-FLOW-003 step 1), before
 * anything is committed. Where a ticket is active and the folder is not on its
 * branch, the run is refused, naming both, but where it takes the branch up:
 * in a clone that has the ticket's branch only as a remote branch, it makes
 * the local branch from it, and the branch the ticket left in the same way,
 * and puts the folder on it; and for a ticket that records no branch it left,
 * it puts the folder on the ticket's branch and records there the branch the
 * folder was on as the one it left. It never begins the ticket again from
 * main. Where no ticket is active, the folder on a ticket's branch or on none
 * refuses the run (D239).
 */
export const takeUp = (root: string, placed: Placed, run: string): Flow<TakenUp, Fault> =>
  using(Git, (git) => {
    const a = placed.active[0]
    const on = placed.on
    if (a === undefined) {
      if (on === undefined) return end({ refused: "The folder is on no branch: its HEAD names a commit alone. No ticket is made active while it is. Put the folder on the branch you build on, git switch <branch>" })
      const ticket = covers(LINES, on) && on !== LINES ? on.slice(LINES.length + 1) : undefined
      if (ticket !== undefined) return end({ refused: `The folder is on the branch ${on}, which the framework made for the ticket ${ticket}, and no ticket is active. No ticket is made active while the folder is on such a branch. Put the folder on the branch you build on, git switch <branch>` })
      const none = placed.unbranched[0]
      if (none !== undefined) return end({ refused: `The ticket ${none} lies in the active lane, and the repository has no branch of it, ${lineOf(none)}, local or remote. The framework does not begin an active ticket again from main. Fetch its branch, or move the ticket back to the backlog and commit that` })
      return end({ main: on, on })
    }
    if (a.leftMissing === true) return end({ refused: `The ticket ${a.name} was pulled from the branch ${a.left ?? ""}, and the repository has no such branch, local or remote. Fetch it, then start a run again` })
    const fromRemote = (line: string, ref: string | undefined): Flow<void, Fault> =>
      ref === undefined ? end(undefined) : decide(git.tipOf(root, ref), (tip) => (tip === undefined ? end(undefined) : git.makeLine(root, line, tip)))
    const putOn: Flow<string | undefined, Fault> = sequence(
      a.remote === undefined ? end(undefined) : fromRemote(a.line, a.remote),
      decide(git.switchTo(root, a.line), (s) => end("switched" in s ? undefined : switchRefused(a.line, s)))
    )
    if (a.left === undefined) {
      if (on === undefined || on === a.line) {
        return end({ refused: `The ticket ${a.name} is active and records no branch it left, as one an earlier release pulled, and the folder is ${on === undefined ? "on no branch" : `on its branch, ${a.line}`}. Put the folder on the branch the ticket was pulled from, then start a run: the run records that branch in the ticket as the branch it left, and puts the folder on ${a.line}` })
      }
      const path = ticketPath("active", a.name)
      return decide(putOn, (refused): Flow<TakenUp, Fault> =>
        refused !== undefined ? end({ refused }) : sequence(
          addLines(root, path, [{ line: "left", branch: on }]),
          decide(committed({ folder: root, line: a.line }, `ticket ${a.name}: the branch it left, ${on}, recorded`, [path]), (commit) =>
            commit === undefined ? end(undefined) : note(root, { event: "commit made", run, ticket: a.name, commit, why: "the branch the ticket left, recorded" })),
          end({ main: on, on: a.line })
        ))
    }
    const left = a.left
    const withLeft: Flow<void, Fault> = fromRemote(left, a.leftRemote)
    if (on === a.line) return sequence(withLeft, end({ main: left, on: a.line }))
    // Where the ticket's branch is checked out in another working tree, the refusal names that tree too, and the command that removes it.
    if (a.remote === undefined) {
      return decide(git.heldElsewhere(root, a.line), (tree) => end({ refused: `${elsewhere(placed) ?? ""}${tree === undefined ? "" : `. ${heldIn(a.line, tree)}`}` }))
    }
    return sequence(withLeft, decide(putOn, (refused): Flow<TakenUp, Fault> => end(refused !== undefined ? { refused } : { main: left, on: a.line })))
  })

/**
 * Pulls a ticket (REQ-FLOW-004 step 1): records in it the branch the folder is
 * on, as the branch it leaves, moves it to the active lane and commits both on
 * that branch, its main; makes the ticket's branch from that commit, or takes
 * up the branch it already has, and puts the folder on it. A branch made from
 * the commit the folder is on moves HEAD alone, so no file is written. Gives
 * git's refusal in words, where it would not put the folder on the branch.
 */
export const pull = (ws: Workspace, ticket: string, run: string): Flow<string | undefined, Fault> =>
  using(Git, (git) => {
    const line = lineOf(ticket)
    return sequence(
      addLines(ws.root, ticketPath("backlog", ticket), [{ line: "left", branch: ws.main }]),
      move(ws, ws.main, ticket, "backlog", "active", run),
      decide(git.tipOf(ws.root, line), (had) =>
        decide(had !== undefined ? end(undefined) : decide(git.tipOf(ws.root, "HEAD"), (tip) => (tip === undefined ? end(undefined) : git.makeLine(ws.root, line, tip))), () =>
          decide(git.switchTo(ws.root, line), (s): Flow<string | undefined, Fault> =>
            "switched" in s
              ? sequence(note(ws.root, { event: "ticket pulled", run, ticket, main: ws.main, branch: line }), end(undefined))
              : end(switchRefused(line, s)))))
    )
  })

/** Moves a ticket from one lane to another in the workspace's folder, and commits that move and nothing else on `line`, the branch the folder is on: main when it is pulled, the ticket's branch before that is merged. The run's id names the entry of the commit. */
export const move = (ws: Workspace, line: string, ticket: string, from: Lane, to: Lane, run: string): Flow<void, Fault> =>
  using(Files, (files) =>
    sequence(
      files.move(at(ws.root, ticketPath(from, ticket)), at(ws.root, ticketPath(to, ticket))),
      decide(committed({ folder: ws.root, line }, `board: ${ticket} to ${to}`, [ticketPath(from, ticket), ticketPath(to, ticket)]), (commit) =>
        commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: `${ticket} moved to ${to}` }))
    ))
