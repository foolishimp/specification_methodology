/**
 * A run (REQ-FLOW-003): it works on one ticket and goes on without the user
 * until it ends, in exactly one of four ways, which are its typed results:
 * the work is done, it waits for the user, it has stopped, or it was refused
 * before any step.
 *
 * Where the settings record no release of this product, or one that is not
 * what is running, the run is refused first, and commits nothing
 * (REQ-FLOW-010). Then a graph that is not `well_formed` is refused, and what
 * is not yet committed on main is committed. `take_up` gives the ticket; the run holds it (C11),
 * pulls it if it lies in the backlog, and takes main into its branch (C13).
 * It asks the method's manager, once, where the method release the
 * definition file selects is installed, for the sessions' packets (D89).
 * Then, in the ticket's checkout, the steps are made on the governing graph
 * (`steps`, under C9). When no vector may run, `done` holds, for `next` and
 * `done` read one snapshot over the vectors that take part, and the ticket is
 * merged (CALCULUS section 5, round). The run
 * reads the workspace and never the event log; where the log is missing it
 * says so and starts one.
 *
 * At its outermost bound a run turns every fault it meets into an ending, so
 * its type fails with nothing (D75): refused where no step has started, and
 * stopped, naming the step's vector, where one has. The why says what failed
 * and what the user does next, and the ending is logged as every other is;
 * where the fault is in writing the log, the log holds nothing of it. Where
 * the fault is in writing `run ended`, the run keeps the ending it reached,
 * since the log changes no decision, and says the log could not be written.
 *
 * Every ending of a run in which a session failed names where what that
 * session printed is kept (D81).
 *
 * The run is the terms `run` and `closing` of the calculus page (section 5):
 * `open`, the log read and `run started`, decided on by their outcome; then
 * `run'`, decided on by its outcome; then `run ended`, decided on by its
 * outcome. The round of `build` is a `repeat` bounded by the run's limit of
 * minutes, read before it goes again. Every entry the run adds names it by its
 * id.
 *
 * @uses C3 C4 C5 C6 C8 C9 C11 C13 C14 C16 C17
 * @is REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-005 REQ-FLOW-008 REQ-FLOW-010
 */
import type { Release } from "../algorithms/brief.js"
import { done } from "../algorithms/done.js"
import type { Board } from "../algorithms/facts.js"
import { take_up, type TakeUp } from "../algorithms/take_up.js"
import { decide, end, held, outcome, repeat, sequence, using, type Round } from "../kit/calculus.js"
import { now } from "../kit/clock.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import { Hold } from "../services/hold.js"
import type { Flow, Services } from "../services/services.js"
import { commitOf, committed } from "./commit.js"
import { logFound, note } from "./events.js"
import { gather, hereOf } from "./gather.js"
import { mergeIntoMain, takeMainIn } from "./merge.js"
import { faultEnding, minutesReached, steps, type Ending, type RunState } from "./step.js"
import { move, writeSimplest } from "./ticket.js"
import { at, boardOf, builds, checkoutOf, checkoutPlace, checkoutTop, holdOf, laneOfTicket, lineOf, open, openWorkspace, PLACES, recordedIn, releaseWords, running, ticketPath, type Fault, type Opened, type Workspace } from "./workspace.js"

/** The limit on active tickets while REQ-FLOW-009 is not in force (REQ-PARAM-001). */
const LIMIT = 1

export type { Ending }

export interface Ran {
  readonly ending: Ending
  /** Said when the event log was not found and a new one was started. */
  readonly logStarted: boolean
  /** Said when the run's `run ended` could not be written to the event log; the run keeps the ending it reached (D75). */
  readonly logUnwritten?: true
  /** Where what each session that failed in this run printed is kept, from the workspace's folder, once each; its ending names them (D81). */
  readonly printed: readonly string[]
}

/** What the command `run` gives: why `open` refused it, or how the run ended. */
export type RunGiven = Ran | Exclude<Opened, { readonly root: string }>

/** How `run'` ended, with the places of what failed sessions printed. */
interface Built {
  readonly ending: Ending
  readonly printed: readonly string[]
}

const built = (ending: Ending, printed?: readonly string[]): Built => ({ ending, printed: printed ?? [] })

/** What the ticket and the run are, read in the terms that enclose `build`, with the method release once the run has found where it is installed (D89). */
interface Building {
  readonly ws: Workspace
  readonly ticket: string
  readonly run: string
  readonly checkout: string
  readonly release?: Release
}

/** The method release the definition file selects, with where its manager keeps it, where it says (D89). Where it cannot say, the release is named by its identity alone. */
const releaseOf = (ws: Workspace): Flow<Release | undefined> => {
  const release = ws.release
  if (release === undefined) return end(undefined)
  return using(Files, (files) => decide(files.methodAt(release.uri, ws.root), (path) => end(path === undefined ? release : { ...release, path })))
}

/** `take-in`: main taken into the ticket's branch, and the ticket read in the active lane on main; the ending where either stops the run. */
const takeIn = (b: Building): Flow<Ending | undefined, Fault> =>
  decide(takeMainIn(b.ws, b.checkout, b.ticket, b.run), (taken): Flow<Ending | undefined, Fault> =>
    "stopped" in taken
      ? end({ ending: "stopped", ticket: b.ticket, why: taken.stopped, ...(taken.files === undefined ? {} : { files: taken.files }) })
      : decide(boardOf(b.ws.root), (board) =>
        end(laneOfTicket(board, b.ticket) !== "active" ? { ending: "stopped", ticket: b.ticket, why: `the ticket ${b.ticket} no longer lies in the active lane on main` } : undefined)))

/** One round of `build`: the steps on the governing graph, until none may run, where `done` holds; main taken in again where it moved, or the ticket merged. */
const round = (b: Building, here: Parameters<typeof steps>[0]["here"]) => (state: RunState): Flow<Round<RunState, Built>> =>
  decide(steps({ ws: b.ws, here, ticket: b.ticket, run: b.run, ...(b.release === undefined ? {} : { release: b.release }) }, b.ws.graph.graph, state), ({ traversed, state: after }): Flow<Round<RunState, Built>> => {
    if ("ended" in traversed) return end({ leave: built(traversed.ended, after.failed) })
    const merging: Flow<Round<RunState, Built>, Fault> = using(Git, (git) =>
      decide(git.holdsAll(b.checkout, b.ws.main), (holds): Flow<Round<RunState, Built>, Fault> =>
        !holds
          ? decide(takeIn(b), (stopped) => end(stopped === undefined ? { again: after } : { leave: built(stopped, after.failed) }))
          : decide(mergeIntoMain(b.ws, b.checkout, b.ticket, b.run), (m) =>
            end({
              leave: built(
                "stopped" in m ? { ending: "stopped", ticket: b.ticket, why: m.stopped, ...(m.files === undefined ? {} : { files: m.files }) } : { ending: "done", ticket: b.ticket, merged: m.merged },
                after.failed
              )
            }))))
    return decide(outcome(merging), (o) => end("fault" in o ? { leave: built(faultEnding(b.ws.root, o.fault, b.ticket, after.vector), after.failed) } : o.value))
  })

/** `build(t)`: the ticket held, pulled where it lies in the backlog, its checkout made, what an interrupted step left committed, main taken in, and the rounds. */
const build = (ws: Workspace, ticket: string, lane: "active" | "backlog", run: string): Flow<Built, Fault> => {
  const checkout = checkoutOf(ws.root, ticket, ws.within)
  const b: Building = { ws, ticket, run, checkout }
  const inHold: Flow<Built, Fault> = using(Git, (git) =>
    sequence(
      lane === "backlog" ? sequence(move(ws, ws.root, ticket, "backlog", "active", run), note(ws.root, { event: "ticket pulled", run, ticket })) : end(undefined),
      git.checkoutOf(ws.root, lineOf(ticket), ws.main, at(ws.root, checkoutTop(ticket))),
      // What an interrupted step left in the checkout is the result of that step: it is committed, not changed.
      // A merge git could not make is the user's to resolve: the run stays stopped, and commits nothing, until they have.
      decide(commitOf({ folder: checkout, line: lineOf(ticket) }, "the result of an interrupted step"), (left): Flow<Built, Fault> => {
        if ("unresolved" in left) {
          const { unresolved } = left
          return end(built({
            ending: "stopped",
            ticket,
            why: `git could not merge ${unresolved.join(", ")}, and the merge is not resolved. Resolve ${unresolved.length === 1 ? "it" : "them"} in the ticket's checkout, ${checkoutPlace(ticket, ws.within)}, and commit there`,
            files: unresolved.map((f) => `${checkoutPlace(ticket, ws.within)}/${f}`)
          }))
        }
        return sequence(
          left.commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit: left.commit, why: "what an interrupted step left" }),
          decide(takeIn(b), (stopped): Flow<Built, Fault> =>
            stopped !== undefined
              ? end(built(stopped))
              : decide(hereOf(ws, ticket), (here) => decide(releaseOf(ws), (release) => {
                const state: RunState = { attempts: new Map(), began: now().millis, sessions: 0, failed: [] }
                return repeat<RunState, Built, never, Services>(state, round({ ...b, ...(release === undefined ? {} : { release }) }, here), {
                  reached: (st) => minutesReached(ws, st) !== undefined,
                  leave: (st) => built({ ending: "stopped", ticket, ...(st.vector === undefined ? {} : { vector: st.vector }), why: minutesReached(ws, st) ?? "" }, st.failed)
                })
              })))
        )
      })
    ))
  // A hold left by a run whose process ended says that run was cut off, with any session it started that neither returned nor failed (REQ-FLOW-007).
  return using(Hold, (hold) =>
    decide(hold.left(holdOf(ws.root, ticket)), (left) =>
      sequence(
        left ? note(ws.root, { event: "run cut off", run: b.run, ticket, why: "this run found the hold the cut-off run left; a session it started that neither returned nor failed was cut off with it" }) : end(undefined),
        decide(held(hold, holdOf(ws.root, ticket), inHold), (h) => end(h === "held" ? built({ ending: "refused", why: "held" }) : h.done)))))
}

/**
 * The release check of `run'` (REQ-FLOW-010): the record the settings on main
 * hold, as it stands, and what is running, from the manifest at the place the
 * library gives. The ending where the record is not there or is not what is
 * running; nothing where it is.
 */
const releaseRefused = (root: string, manifest: string): Flow<Ending | undefined> =>
  using(Files, (files) =>
    decide(files.read(at(root, PLACES.settings)), (settings) =>
      decide(running(manifest), (now) => {
        const recorded = recordedIn(settings ?? "")
        return end(builds(recorded, now) ? undefined : { ending: "refused", why: "release", release: { recorded, running: now } })
      })))

/** `run'`: refused where the release recorded is not what is running; then main read and judged, what the user left on main committed where no run holds a ticket, the ticket taken up, and built. */
const runOn = (root: string, main: string, within: string, named: string | undefined, run: string, manifest: string): Flow<Built, Fault> =>
  decide(releaseRefused(root, manifest), (refused): Flow<Built, Fault> => refused !== undefined ? end(built(refused)) : runOnMain(root, main, within, named, run))

/** `run'` past the release check: main read and judged, what the user left on main committed where no run holds a ticket, the ticket taken up, and built. */
const runOnMain = (root: string, main: string, within: string, named: string | undefined, run: string): Flow<Built, Fault> =>
  decide(openWorkspace(root, main, within), (opened): Flow<Built, Fault> => {
    if ("refused" in opened) {
      return end(built({ ending: "refused", why: opened.refused.some((r) => r.where === ".stdo-builder") ? "not set up" : "not well formed", reasons: opened.refused }))
    }
    const ws = opened
    return using(Hold, (hold) => {
      const heldNow = (board: Board): Flow<readonly string[]> =>
        decide(hold.held(board.active.map((t) => holdOf(root, t.name))), (files) => end(board.active.filter((t) => files.includes(holdOf(root, t.name))).map((t) => t.name)))
      // While another run holds a ticket, its session may be at work, and what lies in main's folder is judged at its return: nothing of main's is committed until then.
      const commitMain: Flow<Ending | undefined, Fault> = decide(decide(boardOf(root), heldNow), (heldAtStart): Flow<Ending | undefined, Fault> =>
        heldAtStart.length > 0
          ? end(undefined)
          : decide(commitOf({ folder: root, line: main }, "what the user changed by hand on main"), (onMain): Flow<Ending | undefined, Fault> =>
            "unresolved" in onMain
              ? end({ ending: "refused", why: "unresolved", files: onMain.unresolved })
              : onMain.commit === undefined
              ? end(undefined)
              : sequence(note(root, { event: "commit made", run, commit: onMain.commit, why: "what the user left uncommitted on main" }), end(undefined))))
      return decide(commitMain, (refused): Flow<Built, Fault> =>
        refused !== undefined ? end(built(refused)) : decide(boardOf(root), (board) =>
          decide(heldNow(board), (heldBy): Flow<Built, Fault> => {
            const input = { board, held: heldBy, graph: ws.graph, limit: LIMIT, ...(named === undefined ? {} : { named }) }
            const first = take_up({ ...input, mainDone: true })
            // Only where the first two rules give nothing does the third rule of take_up turn on what done says on main.
            const taken: Flow<TakeUp, Fault> = first.take === "none" && board.active.length === 0 && named === undefined
              ? decide(gather(ws, { folder: root, line: main }), (g) => end(take_up({ ...input, mainDone: done(ws.graph, g).done === "yes" })))
              : end(first)
            return decide(taken, (t): Flow<Built, Fault> => {
              if (t.take === "none") return end(built({ ending: "refused", why: t.why }))
              if (t.take !== "simplest") return build(ws, t.name, t.lane, run)
              return decide(writeSimplest(root), (ticket) =>
                sequence(
                  decide(committed({ folder: root, line: main }, `board: the simplest ticket ${ticket}`, [ticketPath("backlog", ticket)]), (commit) =>
                    commit === undefined ? end(undefined) : note(root, { event: "commit made", run, ticket, commit, why: "the simplest ticket written" })),
                  build(ws, ticket, "backlog", run)
                ))
            })
          })))
    })
  })

/** The entry of the run's ending, as every ending is logged. */
const ended = (root: string, run: string, ending: Ending): Flow<void, Fault> =>
  note(root, {
    event: "run ended",
    run,
    ending: ending.ending,
    ...("ticket" in ending ? { ticket: ending.ticket } : {}),
    ...("vector" in ending && ending.vector !== undefined ? { vector: ending.vector } : {}),
    why: ending.ending === "refused" ? (ending.fault ?? ending.why) : ending.ending === "stopped" ? ending.why : ending.ending === "waiting" ? "the user is asked" : "the ticket is merged"
  })

/**
 * `closing(x)`: `run ended` written, and the run ends as it reached. Where it
 * cannot be written, the run keeps that ending, since the log changes no
 * decision (L5), and says the log could not be written (D75).
 */
const closing = (root: string, run: string, ran: Ran): Flow<Ran> =>
  decide(outcome(ended(root, run, ran.ending)), (o) => end("fault" in o ? { ...ran, logUnwritten: true as const } : ran))

/** The run refused for a fault met outside every repeat (D75). */
const refusedFor = (root: string, f: Fault, logStarted: boolean): Ran => ({ ending: faultEnding(root, f, undefined, undefined), logStarted, printed: [] })

/**
 * A run on the workspace in `folder`, on the ticket the user names or the one
 * `take_up` gives, by the release whose manifest would be at `manifest`. It
 * fails with nothing (D75).
 */
export const run = (folder: string, named: string | undefined, manifest: string): Flow<RunGiven> =>
  decide(outcome(open(folder)), (o): Flow<RunGiven> => {
    // `open` writes nothing to the log, so its fault names its own path, and the folder named stands for the root.
    if ("fault" in o) return end(refusedFor(folder, o.fault, false))
    const opened = o.value
    if ("refused" in opened) return end(opened)
    const { root, main, within } = opened
    const runId = now().written
    const started: Flow<boolean, Fault> = decide(logFound(root), (found) =>
      using(Files, (files) =>
        decide(files.read(at(root, PLACES.settings)), (settings) =>
          sequence(
            note(root, { event: "run started", run: runId, release: releaseWords(recordedIn(settings ?? "")), ...(named === undefined ? {} : { ticket: named }), ...(found ? {} : { why: "the event log was not found; this run starts a new one" }) }),
            end(!found)
          ))))
    return decide(outcome(started), (s): Flow<RunGiven> => {
      // A fault before `run started` is written ends the run as refused, and the log holds nothing of it.
      if ("fault" in s) return end(refusedFor(root, s.fault, false))
      const logStarted = s.value
      return decide(outcome(runOn(root, main, within, named, runId, manifest)), (r): Flow<RunGiven> =>
        "fault" in r
          // A fault met outside every repeat ends the run as refused; where it is in writing the log, the log holds nothing of it.
          ? r.fault._tag === "LogRefused" ? end(refusedFor(root, r.fault, logStarted)) : closing(root, runId, refusedFor(root, r.fault, logStarted))
          : closing(root, runId, { ending: r.value.ending, logStarted, printed: r.value.printed }))
    })
  })
