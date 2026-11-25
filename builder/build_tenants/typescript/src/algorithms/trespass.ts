/**
 * `trespass`: what changed while a session worked, outside what its step
 * writes (D226). The identities of every file git does not ignore are taken
 * at the session's start, in the workspace's folder, where the session works,
 * and again when it is over; each file whose identity differs, but those the
 * step writes, is returned with whether it was added, changed or removed. Of the branch's ticket each part is compared
 * apart: the user's words, the triage and the term, and the framework's part.
 * What the framework itself wrote in that time is not returned, a ticket the
 * user writes with the product's command among it; nor a file the user said
 * yes to, where its identity is the one it had at the yes. Where the
 * identities from the start are missing, cannot be read, name a step the graph
 * does not hold or name what git no longer holds, the identities of the
 * commit the session started from stand in their place, or, where that is not
 * known, those of the commit the folder is on, with nothing counted as what
 * the step writes, so each file that differs from that commit is returned; and
 * it says that the identities were missing (D241, D246, D255).
 *
 * It also returns, apart, each file of the workspace's folder that differs
 * between the commit main, the branch the ticket left, was on at the
 * session's start and the commit main is on now, whatever the file: none of
 * them counts as what the step writes; nor one the user said yes to, where
 * main gives it now the identity it had at the yes (D257).
 *
 * @uses C2 C1 C5 C6 H1
 * @is REQ-ALG-008
 */
import type { IdentityMap } from "../kit/content_addressing.js"
import { difference } from "../kit/map_difference.js"
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

/** One file that changed while a session worked, by its path in the workspace; `on` where it changed on main, the branch the ticket left, and not in the folder (D257). */
export interface Changed {
  readonly path: string
  readonly how: "added" | "changed" | "removed"
  readonly on?: "main"
}

/** The key a yes and a ruling give a file changed on main, before its path in the workspace: no key of a file of the folder begins so, nor one a ruling of an earlier release gave, which began `main:` or `checkout:` (REQ-FLOW-004, D257). */
export const LEFT = "left:"

export interface Session {
  readonly graph: WellFormed
  readonly vector: Vector
  readonly kind: "work" | "evaluation"
  readonly places: FrameworkPlaces
  /** The path of the branch's ticket, where there is one. */
  readonly ticket?: string
  /** The identities of a commit, the one the session started from or the one the folder is on, stood in for the missing ones: nothing counts as what the step writes (D241, D246, D255). */
  readonly stood?: true
  /**
   * The identity at the session's start, or at the commit that stands in for
   * it, and now of each file that differs in the workspace's folder, by path
   * (C1); the parts of the branch's ticket under `<ticket>#words`,
   * `<ticket>#triage` and `<ticket>#framework`.
   */
  readonly start: IdentityMap
  readonly end: IdentityMap
  /** Files the framework itself wrote in that time, by path, with the identity it left (D227). */
  readonly framework?: IdentityMap
  /** Files the user said yes to, by path, with the identity each had at the yes, where the ticket and the framework's record agree (REQ-FLOW-006); a file changed on main by `LEFT` and its path, with the identity main gave it. */
  readonly yes?: IdentityMap
  /** The identity, by path in the workspace, of each file of the folder that differs between the commit main was on at the session's start, or the one that stands in for it, and the commit main is on now: in the first, and in the second (D257). */
  readonly main?: { readonly start: IdentityMap; readonly end: IdentityMap }
}

/** The file at the top of the workspace's folder where what a build leaves is listed for git to ignore. A working session may write it (D99). */
const TOP_IGNORE = ".gitignore"

/** The keys of the parts of the branch's ticket, beside its path (D202, D226). */
export const PART = "#framework"
export const WORDS = "#words"
export const TRIAGE = "#triage"

/**
 * What a step writes, in the workspace's folder (REQ-ALG-008): for a working
 * session the nodes its vector writes and the top `.gitignore`, and for the
 * first vector's session the triage and the term of the branch's ticket; for
 * an evaluating session its findings and its verdict, and nothing else.
 * `brief` names the same places, so a session that keeps to its packet
 * changes nothing that is named to the user (D88, D99).
 */
export function writes(graph: WellFormed, vector: Vector, kind: "work" | "evaluation", ticket?: string): readonly string[] {
  if (kind === "evaluation") return vector.evaluation === undefined ? [] : [vector.evaluation.findings, vector.evaluation.verdict]
  const own = new Set(placedOf(graph, vector).writes)
  const assets = nodesOf(graph.graph, graph.registry).filter((n) => own.has(n.name)).flatMap(pathsOf)
  return [...assets, TOP_IGNORE, ...(vector.first === true && ticket !== undefined ? [`${ticket}${TRIAGE}`] : [])]
}

/** What the framework and an evaluating session write between two readings: its own folder, and the findings and verdict of each evaluation (CALCULUS L2). */
export function apart(graph: WellFormed, places: FrameworkPlaces): readonly string[] {
  return [places.folder, ...vectorsOf(graph.graph, graph.registry).flatMap((v) => (v.evaluation === undefined ? [] : [v.evaluation.findings, v.evaluation.verdict]))]
}

/** The files whose identity differs, as added, changed or removed (C2). */
const differing = (start: IdentityMap, end: IdentityMap): readonly Changed[] => {
  const d = difference(start, end)
  return [
    ...d.added.map((path) => ({ path, how: "added" as const })),
    ...d.changed.map((path) => ({ path, how: "changed" as const })),
    ...d.removed.map((path) => ({ path, how: "removed" as const }))
  ]
}

/** What `trespass` returns: each file that changed in the folder, those changed on main apart, and whether the identities from the session's start were missing, so the commit's stood in (REQ-ALG-008). */
export interface Trespassed {
  readonly files: readonly Changed[]
  readonly main: readonly Changed[]
  readonly missing: boolean
}

/**
 * Each file that changed while the session worked, outside what its step
 * writes, and whether the identities from its start were missing. Where they
 * were, the commit's stand in, and nothing counts as what the step writes.
 * The branch's ticket is returned once, by its path, where a part of it the
 * step does not write differs.
 */
export function trespass(s: Session): Trespassed {
  const free = s.stood === true ? [] : writes(s.graph, s.vector, s.kind, s.ticket)
  const left = (path: string, now: string | undefined): boolean =>
    (now !== undefined && s.framework?.get(path) === now) || s.yes?.get(path) === (now ?? "")
  const inFolder = differing(s.start, s.end).filter((c) => {
    // The ticket's whole file is compared by its parts (D202, D226).
    if (s.ticket !== undefined && c.path === s.ticket && s.start.has(`${s.ticket}${PART}`)) return false
    if (free.some((place) => covers(place, c.path) || place === c.path)) return false
    return !left(c.path, s.end.get(c.path))
  })
  const ticketPart = s.ticket === undefined ? [] : inFolder.filter((c) => c.path.startsWith(`${s.ticket}#`))
  const files = inFolder.filter((c) => s.ticket === undefined || !c.path.startsWith(`${s.ticket}#`))
  const ticket: readonly Changed[] = ticketPart.length === 0 || s.ticket === undefined ? [] : [{ path: s.ticket, how: "changed" }]
  // What main gained counts as no part of what the step writes, whatever the file; a yes counts at the identity main gave the file then (D257).
  const main = s.main === undefined ? [] : differing(s.main.start, s.main.end)
    .filter((c) => s.yes?.get(`${LEFT}${c.path}`) !== (s.main?.end.get(c.path) ?? ""))
    .map((c): Changed => ({ ...c, on: "main" }))
  return { files: [...ticket, ...files], main, missing: s.stood === true }
}
