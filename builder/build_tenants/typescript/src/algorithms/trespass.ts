/**
 * `trespass`: the protected files whose identity differs between a session's
 * start and its return. A file in a place that neither the graph nor the
 * definition file names is never returned.
 *
 * The protected files lie in two folders: the ticket's checkout, where the
 * session works, and the workspace's own folder, main's, which holds the
 * governing graph, its registry, the settings and the definition file the run
 * reads. All work on a ticket is done in its checkout (REQ-FLOW-004), so in
 * main's folder every file the graph or the definition file names is
 * protected, the vector's own asset, findings and verdict too. The ticket
 * lanes on main are not: the user may change the board there at any time
 * (REQ-FLOW-004).
 *
 * @uses C2 C1 C5 C6 H1
 * @is REQ-ALG-008
 */
import type { IdentityMap } from "../kit/content_addressing.js"
import { difference, paths } from "../kit/map_difference.js"
import { covers } from "../kit/place_containment.js"
import { pathsOf, type Vector } from "../graph/terms.js"
import { nodesOf, vectorsOf } from "../graph/walk.js"
import { placedOf, type WellFormed } from "./well_formed.js"

/** The places the definition file names for the framework's files and the ticket lanes. */
export interface FrameworkPlaces {
  /** The framework's own folder. */
  readonly folder: string
  readonly definition: string
  readonly settings: string
  readonly graph: string
  readonly registry: string
  /** The framework's own files that git holds: its ignore file and the reference-frame basis. */
  readonly own: readonly string[]
  /** The three ticket lanes. */
  readonly lanes: readonly string[]
}

export interface Session {
  readonly graph: WellFormed
  readonly vector: Vector
  readonly kind: "work" | "evaluation"
  readonly places: FrameworkPlaces
  /** The path of the branch's ticket, where there is one. */
  readonly ticket?: string
  /** The identity of each file at the session's start and at its return, by path (C1). */
  readonly start: IdentityMap
  readonly end: IdentityMap
  /** Which folder the identities are of: the ticket's checkout, where the session works, or main's own folder. */
  readonly side?: "checkout" | "main"
}

/** The file at the top of the checkout where what a build leaves is listed for git to ignore. A working session may write it (D99). */
const TOP_IGNORE = ".gitignore"

/**
 * The places a session must not change in one folder, beside the tickets: the
 * files the framework and the definition file name, every asset the vector
 * does not write and every verdict; and those it may write beside its own
 * asset, the findings and verdict of an evaluating session, or the top
 * `.gitignore` for a working session. `trespass` and `brief` both take them
 * from here, so a session that keeps to its brief does not trespass (D88,
 * D99).
 */
export function guarded(
  graph: WellFormed,
  vector: Vector,
  kind: "work" | "evaluation",
  places: FrameworkPlaces,
  side: "checkout" | "main" = "checkout"
): { readonly fixed: readonly string[]; readonly free: readonly string[] } {
  const onMain = side === "main"
  // A working session may write each node its vector writes.
  const own = new Set(placedOf(graph, vector).writes)
  const assets = nodesOf(graph.graph, graph.registry)
    .filter((n) => onMain || kind === "evaluation" || !own.has(n.name))
    .flatMap(pathsOf)
  const verdicts = vectorsOf(graph.graph, graph.registry).flatMap((v) => (v.evaluation === undefined ? [] : [v.evaluation.verdict]))
  return {
    fixed: [places.definition, places.settings, places.graph, places.registry, ...places.own, ...assets, ...verdicts],
    free: onMain ? [] : kind === "work" ? [TOP_IGNORE] : vector.evaluation === undefined ? [] : [vector.evaluation.findings, vector.evaluation.verdict]
  }
}

/** What the framework and an evaluating session write between two readings: its own folder, and what `guarded` leaves free to each evaluating session (CALCULUS L2). */
export function apart(graph: WellFormed, places: FrameworkPlaces): readonly string[] {
  return [places.folder, ...vectorsOf(graph.graph, graph.registry).flatMap((v) => guarded(graph, v, "evaluation", places).free)]
}

/** The key of the framework's part of the branch's ticket, beside the ticket's path, under which a snapshot holds the identity of that part alone (D202). */
export const PART = "#framework"

export function trespass(s: Session): readonly string[] {
  const { graph, vector, kind, places } = s
  const onMain = s.side === "main"
  const { fixed, free } = guarded(graph, vector, kind, places, s.side)
  const ownTicket = kind === "work" && vector.first === true ? s.ticket : undefined
  const tickets = new Set(
    onMain ? [] : [...s.start.keys()].filter((path) => path !== ownTicket && places.lanes.some((lane) => covers(lane, path)))
  )
  const isProtected = (path: string): boolean =>
    !free.some((place) => covers(place, path)) && (tickets.has(path) || fixed.some((place) => covers(place, path)))
  const only = (m: ReadonlyMap<string, string>): ReadonlyMap<string, string> =>
    new Map([...m].filter(([path]) => isProtected(path)))
  // Where the framework's part of the branch's ticket differs, the ticket is returned (REQ-ALG-008).
  return [...new Set(paths(difference(only(s.start), only(s.end))).map((path) => (path.endsWith(PART) ? path.slice(0, -PART.length) : path)))]
}
