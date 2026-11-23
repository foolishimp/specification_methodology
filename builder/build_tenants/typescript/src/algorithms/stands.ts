/**
 * `stands`: where the work stands, in the graph's own names. For each ticket
 * on the board its lane and, if active, what it waits on, as its ticket shows
 * or else as the event log shows, with when that was written (D204); the tickets
 * withdrawn; the assets each ticket changed; and, from one fold of the event
 * log, how each ticket's last run ended and its sessions, with the cost and
 * the calls each reported and their sums. A cost is given with its unit, and
 * costs are summed only where they share one (D102). A cost that is a number,
 * and the sum, are given to the cent; the sum is of the costs as reported
 * (D195). Nothing is kept.
 *
 * @uses C8 C10 C3 C5 C6 H1
 * @is REQ-ALG-012
 */
import type { Step } from "../kit/append_only_log.js"
import { firstMatch, type Rule } from "../kit/first_match.js"
import { covered, pathsOf, type Vector, type Workflow } from "../graph/terms.js"
import { inPlace, nodesOf } from "../graph/walk.js"
import { done } from "./done.js"
import { factsOf, TICKET, type Board, type Given, type LogEntry, type Snapshot } from "./facts.js"
import { next } from "./next.js"
import { asksUser, isDone, passes, recordsOf, standsFor } from "./passes.js"
import type { WellFormed } from "./well_formed.js"

/** What an active ticket waits on, and what it was read from: the ticket, or the event log, with when that was written (D204). Without the log, the rest is what a run finds. */
export type Waits =
  | { readonly on: "answer"; readonly vector: string; readonly asset: string; readonly question?: string; readonly from: "ticket"; readonly when?: string }
  | { readonly on: "induction"; readonly from: "ticket" }
  | { readonly on: "held up"; readonly vector: string; readonly checks: readonly string[]; readonly found?: string; readonly from: "log"; readonly when?: string }
  | { readonly on: "work"; readonly vector: string; readonly from: "log"; readonly when?: string }
  | { readonly on: "merge"; readonly from: "log"; readonly when?: string }
  | { readonly on: "unknown" }

export interface SessionSeen {
  readonly vector: string
  readonly kind: string
  readonly agent?: string
  readonly ended: "returned" | "failed" | "under way"
  readonly seconds?: number
  /** What the agent reported the session cost (D91), and its unit as the settings name it (D102). The fold keeps it as reported; `stands` gives one that is a number to the cent, and any other as reported (D195). */
  readonly cost?: string
  readonly unit?: string
  /** How many calls the agent reported the session made. */
  readonly calls?: number
}

export interface TicketRuns {
  readonly last?: { readonly ending: string; readonly why: string }
  readonly sessions: readonly SessionSeen[]
  /** Working sessions started, by vector. */
  readonly attempts: Readonly<Record<string, number>>
  /** The sum of the costs its sessions reported that are plain numbers, where one did and all of them have the same unit, or none, given to the cent (D195); and that unit. */
  readonly cost?: string
  readonly unit?: string
  /** The sum of the calls its sessions reported, where one did. */
  readonly calls?: number
}

/** The running result of one fold of the log. The pass over the log is the event log's reader (C10). */
export type LogFold = Map<string, { last?: { ending: string; why: string; at?: string }; step?: { vector: string; failing: string[] }; sessions: SessionSeen[]; attempts: Record<string, number> }>

export function startOfLog(): LogFold {
  return new Map()
}

/** One step of the fold. An entry it does not know is passed over and left as it is. */
export const logStep: Step<LogFold, LogEntry> = (fold, entry) => {
  const ticket = entry.ticket
  if (ticket === undefined) return fold
  const runs = fold.get(ticket) ?? { sessions: [], attempts: {} }
  fold.set(ticket, runs)
  if (entry.event === "run ended" && entry.ending !== undefined) {
    runs.last = { ending: entry.ending, why: entry.why ?? "", ...(entry.at === undefined ? {} : { at: entry.at }) }
  } else if ((entry.event === "check run" || entry.event === "check passed" || entry.event === "check did not pass") && entry.vector !== undefined && entry.check !== undefined) {
    // The last step's vector, and the checks that did not say yes in it.
    if (runs.step?.vector !== entry.vector) runs.step = { vector: entry.vector, failing: [] }
    if (entry.result !== "yes" && !runs.step.failing.includes(entry.check)) runs.step.failing.push(entry.check)
  } else if (entry.event === "verdict read" && entry.vector !== undefined) {
    // A verdict that does not say yes is among what said no in the step (D204).
    if (runs.step?.vector !== entry.vector) runs.step = { vector: entry.vector, failing: [] }
    if (entry.result !== "yes" && !runs.step.failing.includes("verdict")) runs.step.failing.push("verdict")
  } else if ((entry.event === "vector closed" || entry.event === "vector left open") && entry.vector !== undefined) {
    if (runs.step?.vector !== entry.vector) runs.step = { vector: entry.vector, failing: [] }
  } else if (entry.event === "session started" && entry.vector !== undefined && entry.kind !== undefined) {
    if (runs.step?.vector !== entry.vector) runs.step = { vector: entry.vector, failing: [] }
    runs.sessions.push({ vector: entry.vector, kind: entry.kind, ended: "under way", ...(entry.agent === undefined ? {} : { agent: entry.agent }) })
    if (entry.kind === "work") runs.attempts[entry.vector] = (runs.attempts[entry.vector] ?? 0) + 1
  } else if ((entry.event === "session returned" || entry.event === "session failed") && entry.vector !== undefined) {
    const at = runs.sessions.findLastIndex((s) => s.vector === entry.vector && s.kind === entry.kind && s.ended === "under way")
    const seen = runs.sessions[at]
    if (seen !== undefined) {
      runs.sessions[at] = {
        ...seen,
        ended: entry.event === "session returned" ? "returned" : "failed",
        ...(entry.seconds === undefined ? {} : { seconds: entry.seconds }),
        ...(entry.cost === undefined ? {} : { cost: entry.cost }),
        ...(entry.unit === undefined ? {} : { unit: entry.unit }),
        ...(entry.calls === undefined ? {} : { calls: entry.calls })
      }
    }
  }
  return fold
}

/** What an active ticket shows, read from it alone (REQ-ALG-012, D204). */
export interface TicketShows {
  /** The vector whose work its checklist shows delivered for the user's decision with no answer of the user after it: the asset asked on, the question, and when it was asked. */
  readonly asked?: { readonly vector: string; readonly asset: string; readonly question?: string; readonly when?: string }
  /** Whether a confirmation of its induction in it stands (REQ-ALG-004), or it needs none. */
  readonly inducted: boolean
}

export interface TicketView {
  /** For an active ticket with a checkout, what its ticket shows. */
  readonly ticket?: TicketShows
  /** The files the ticket changed and how many lines of each: main against its branch, or what its merge brought. */
  readonly changes: readonly { readonly path: string; readonly lines: number }[]
}

export interface StandsInput {
  readonly graph: WellFormed
  readonly board: Board
  /** The names of the tickets that have a branch. */
  readonly branches: readonly string[]
  readonly views: ReadonlyMap<string, TicketView>
  /** One fold of the event log, or undefined when the log was not found. */
  readonly log?: LogFold
  /** Where what the checks of a vector last found is kept. */
  readonly foundOf?: (vector: string) => string
}

export interface TicketStands {
  readonly name: string
  readonly lane: "backlog" | "active" | "done"
  /** For an active ticket, what it waits on, as the ticket or the event log shows it. */
  readonly waits?: Waits
  readonly changed: readonly { readonly asset: string; readonly lines: number }[]
  readonly runs?: TicketRuns
}

export interface Standing {
  readonly tickets: readonly TicketStands[]
  /** The workspace's folder from the top of its repository, which `show` adds, so a path in a ticket's checkout is named where it is (D201). */
  readonly within?: string
  readonly withdrawn: readonly string[]
  readonly log: "found" | "not found"
}

/** A cost as reported, where it is a plain number: text that reads as a finite number (D91). An older cost such as `0.40 USD` is none. */
function plainNumber(cost: string | undefined): number | undefined {
  if (cost === undefined || cost.trim() === "") return undefined
  const n = Number(cost)
  return Number.isFinite(n) ? n : undefined
}

/** A cost as given: two places after the decimal point, rounded to the nearest (D195). */
const toCent = (n: number): string => n.toFixed(2)

/** A session as `stands` gives it: a cost that is a plain number to the cent, any other as reported (D195). */
function given(session: SessionSeen): SessionSeen {
  const n = plainNumber(session.cost)
  return n === undefined ? session : { ...session, cost: toCent(n) }
}

/** The sums of what a ticket's sessions reported: the costs that are plain numbers, where they share one unit or none (D102), summed as reported and the sum given to the cent (D195); and the calls (D91). Neither enters a decision. */
function spent(sessions: readonly SessionSeen[]): { readonly cost?: string; readonly unit?: string; readonly calls?: number } {
  const priced = sessions.flatMap((s) => {
    const n = plainNumber(s.cost)
    return n === undefined ? [] : [{ n, unit: s.unit }]
  })
  const units = new Set(priced.map((p) => p.unit))
  const [unit] = units
  const calls = sessions.flatMap((s) => (s.calls === undefined ? [] : [s.calls]))
  return {
    ...(priced.length === 0 || units.size > 1 ? {} : { cost: toCent(priced.reduce((sum, p) => sum + p.n, 0)), ...(unit === undefined ? {} : { unit }) }),
    ...(calls.length === 0 ? {} : { calls: calls.reduce((sum, c) => sum + c, 0) })
  }
}

/**
 * What an active ticket waits on: the user's answer, or its induction, as the
 * ticket shows; otherwise as the event log shows the last run on it: held up
 * where it ended stopped, to be merged where it ended done, and otherwise in
 * build at the vector of its last step. Without the log, what a run finds.
 */
function waitsOf(shows: TicketShows | undefined, runs: LogFold extends Map<string, infer R> ? R | undefined : never, logFound: boolean, foundOf: ((vector: string) => string) | undefined): Waits {
  if (shows?.asked !== undefined) {
    const a = shows.asked
    return { on: "answer", vector: a.vector, asset: a.asset, from: "ticket", ...(a.question === undefined ? {} : { question: a.question }), ...(a.when === undefined ? {} : { when: a.when }) }
  }
  if (shows !== undefined && !shows.inducted) return { on: "induction", from: "ticket" }
  const step = runs?.step
  const last = runs?.last
  const when = last?.at === undefined ? {} : { when: last.at }
  if (!logFound || step === undefined) return { on: "unknown" }
  if (last?.ending === "stopped") return { on: "held up", vector: step.vector, checks: step.failing, ...(foundOf === undefined ? {} : { found: foundOf(step.vector) }), from: "log", ...when }
  if (last?.ending === "done") return { on: "merge", from: "log", ...when }
  return { on: "work", vector: step.vector, from: "log", ...when }
}

export function stands(input: StandsInput): Standing {
  const nodes = nodesOf(input.graph.graph, input.graph.registry)
  const lanes = [["backlog", input.board.backlog], ["active", input.board.active], ["done", input.board.done]] as const
  const onBoard = new Set<string>()
  const tickets: TicketStands[] = []
  for (const [lane, list] of lanes) {
    for (const t of list) {
      onBoard.add(t.name)
      const view = input.views.get(t.name)
      const changed = nodes.flatMap((node) => {
        const touched = covered(pathsOf(node), (view?.changes ?? []).map((c) => c.path))
        return touched.length === 0 ? [] : [{ asset: node.name, lines: (view?.changes ?? []).filter((c) => touched.includes(c.path)).reduce((sum, c) => sum + c.lines, 0) }]
      })
      const runs = input.log?.get(t.name)
      tickets.push({
        name: t.name,
        lane,
        ...(lane === "active" ? { waits: waitsOf(view?.ticket, input.log?.get(t.name), input.log !== undefined, input.foundOf) } : {}),
        changed,
        ...(runs === undefined ? {} : { runs: { ...(runs.last === undefined ? {} : { last: runs.last }), sessions: runs.sessions.map(given), attempts: runs.attempts, ...spent(runs.sessions) } })
      })
    }
  }
  return {
    tickets,
    withdrawn: input.branches.filter((b) => !onBoard.has(b)),
    log: input.log === undefined ? "not found" : "found"
  }
}
