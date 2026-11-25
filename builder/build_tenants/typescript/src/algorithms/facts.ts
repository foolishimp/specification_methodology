/**
 * The facts of the workspace that the algorithms read, given to them as plain
 * data: a snapshot of the workspace's folder, the board, and the event log's entries.
 * The flows gather these facts; the algorithms only read them.
 *
 * @uses C3
 * @is REQ-ALG-004 REQ-ALG-005 REQ-ALG-006 REQ-ALG-010 REQ-ALG-012 REQ-FLOW-004
 */
import type { Tri } from "../kit/three_valued.js"

/** The key under which the branch's ticket's identity is kept. It has a space, so it is never a node's name. */
export const TICKET = "the ticket"

/**
 * The key under which the identity of the branch's ticket without its term is
 * kept: what an answer or verdict at the vector the ticket enters by stands
 * for, so a term that changes at an induction entry opens none of them (D141).
 */
export const ASKED = "the ticket but its term"

/**
 * The key under which the identity of what a node declares of itself is kept:
 * what must be true of it, what accepts it and what it depends on (C14, C1); or
 * of what the first vector declares of the ticket, under its name. A verdict
 * or an answer kept there stands on it too, so a change to what acceptance
 * there means reopens it (D168, D175). It has a space, so it is never a node's
 * name.
 */
export const declaration = (node: string): string => `the declaration of ${node}`

export interface CheckResult {
  readonly result: Tri
  /** Where what the check found is kept, or a short statement of it. */
  readonly found?: string
  /** What its command printed, its last lines, as the reading ran it; no record keeps it. */
  readonly detail?: string
  /** How long it took when it ran, in seconds (REQ-FLOW-007). */
  readonly seconds?: number
}

/** A verdict or an answer, as written, with the content identities it was given on. A verdict may say that the evaluation cannot judge (D90); an answer says yes or no. */
export interface Given {
  readonly says: "yes" | "no" | "cannot"
  /** By node name, the ticket under TICKET or ASKED, and a node's declaration under `declaration`. */
  readonly on: ReadonlyMap<string, string>
  /** Where it is written: the verdict's place, or the ticket that holds it. */
  readonly at?: string
  /** The commit it names, under which git holds what it was given on (REQ-ALG-004). */
  readonly commit?: string
  /** For a resolution, the ticket that holds it (REQ-ALG-007). */
  readonly ticket?: string
}

/** What is recorded at a node, or under the first vector's name: the verdict of an evaluation and the user's answer, each where one is written. */
export interface Recorded {
  readonly verdict?: Given
  readonly answer?: Given
}

export interface VectorFacts {
  /** Where what the checks last found is kept. */
  readonly found?: string
  /** For the first vector: whether the ticket's term composes (`composes`). */
  readonly composes?: CheckResult
}

export interface BranchTicket {
  readonly path: string
  readonly identity: string
  /** The node at which the work enters, once the ticket is inducted. */
  readonly enters?: string
  /** The vectors of the governing graph the ticket's term names, by name, in its order, where the term reads (REQ-METHOD-006). */
  readonly term?: readonly string[]
  /** The identity of the ticket without its term lines (ASKED). */
  readonly asked?: string
  /**
   * The stretch of the induction entry of the term the run has reached, or whose place the session bound to
   * it is filling (REQ-METHOD-006). Nothing keeps it: a working session of the first vector is bound to it by a
   * `bound` line of the ticket's checklist (`session`, `step.ts`), and from that line the next reading finds
   * whether a change to the ticket is that session's (`boundNow`, `gather.ts`; REQ-FLOW-004, D204).
   */
  readonly inducting?: { readonly enters: string; readonly ends: string }
  /** Whether the ticket holds a ruling of the user, which binds every later session (REQ-FLOW-004). */
  readonly ruled?: true
  /** The names the ticket's checklist and resolutions name: each vector whose work began or was delivered, and each name a resolution is at (REQ-FLOW-005 step 1, D209). */
  readonly worked?: readonly string[]
}

/** The workspace's folder as it is now. */
export interface Snapshot {
  /** The content identity of each asset, by node name, and of what each node that declares what accepts it declares of itself, and the first vector of the ticket, under `declaration`. An asset that is not there has none. */
  readonly identities: ReadonlyMap<string, string>
  /** The branch's ticket. On main, and for the simplest ticket, "simplest". */
  readonly ticket: "simplest" | BranchTicket
  /** Each check's result on the workspace as it is now, by name, where the reading did it (CALCULUS L3). A check missing here was not done. */
  readonly checks?: ReadonlyMap<string, CheckResult>
  readonly vectors: ReadonlyMap<string, VectorFacts>
  /** What is recorded at each node, and under the first vector's name; none where nothing is. */
  readonly records?: ReadonlyMap<string, Recorded>
  /**
   * Main as the branch holds it, for an evaluating brief: the commit where the two last met, and the nodes main holds there (REQ-ALG-007, D208);
   * and, by node, each commit on the branch since then that holds the user's change by hand there (D244).
   */
  readonly main?: { readonly commit: string; readonly holds: readonly string[]; readonly byHand?: ReadonlyMap<string, readonly string[]> }
}

const noFacts: VectorFacts = {}

export function factsOf(snapshot: Snapshot, vector: string): VectorFacts {
  return snapshot.vectors.get(vector) ?? noFacts
}

export interface TicketOnBoard {
  readonly name: string
  /** The simplest ticket: build the workspace to the specification as it stands. */
  readonly simplest?: true
}

/** The three ticket lanes as main has them. */
export interface Board {
  readonly backlog: readonly TicketOnBoard[]
  readonly active: readonly TicketOnBoard[]
  readonly done: readonly TicketOnBoard[]
}

/** One entry of the event log, with the fields `stands` reads. Other events and fields are passed over. */
export interface LogEntry {
  readonly at?: string
  readonly event: string
  readonly check?: string
  readonly result?: string
  readonly ticket?: string
  readonly vector?: string
  readonly kind?: string
  readonly agent?: string
  readonly seconds?: number
  readonly cost?: string
  readonly unit?: string
  readonly calls?: number
  readonly ending?: string
  readonly why?: string
}

/**
 * The framework's part of a ticket (REQ-FLOW-001, REQ-FLOW-004; D202): every
 * line of the field `framework`, wherever it lies. The branch it left
 * (`left`), the checklist (`began`, `delivered`, `bound`, `unbound`), the
 * resolutions (`resolved`), the rulings (`ruling`) and the rulings on what
 * changed (`changed`).
 */
export const FRAMEWORK = "framework"

export type TicketLine =
  /** The branch the folder was on when the ticket was pulled: main for the ticket until it is merged (REQ-FLOW-001, REQ-FLOW-004; D239). */
  | { readonly line: "left"; readonly branch: string }
  | { readonly line: "began"; readonly vector: string; readonly commit: string }
  | { readonly line: "delivered"; readonly vector: string; readonly commit: string; readonly decision?: true; readonly when?: string }
  | { readonly line: "bound"; readonly vector: string; readonly enters: string; readonly ends: string; readonly commit: string }
  | { readonly line: "unbound"; readonly commit: string }
  | { readonly line: "resolved"; readonly by: "evaluation" | "user"; readonly says: "yes" | "no"; readonly at: string; readonly commit: string; readonly verdict?: string; readonly findings?: string; readonly reason?: string }
  | { readonly line: "ruling"; readonly commit: string; readonly words: string }
  /** The user's ruling on what changed while a session worked at the vector: a yes names each file it was given on, by its path in the workspace, with its identity then, and each line of the framework's part that changed while the session worked, by its identity, which is never read as the user's answer (REQ-FLOW-004, D227, D230). */
  | { readonly line: "changed"; readonly says: "yes" | "no"; readonly vector: string; readonly files: readonly { readonly key: string; readonly identity: string }[]; readonly foreign?: readonly string[] }

const DECISION = "for the user's decision"
/** The key of a ruling's entry naming, by its identity, a line of the framework's part that changed while a session worked (D230). */
export const NOT_THE_USERS = "not the user's answer"

/** The words of one line of the framework's part, after its field. */
export function lineText(l: TicketLine): string {
  switch (l.line) {
    case "left":
      return `left ${l.branch}`
    case "began":
      return `began ${l.vector} at ${l.commit}`
    case "delivered":
      return `delivered ${l.vector}${l.decision === true ? ` ${DECISION}` : ""} at ${l.commit}${l.when === undefined ? "" : ` (${l.when})`}`
    case "bound":
      return `bound ${l.vector} over ${l.enters} to ${l.ends} at ${l.commit}`
    case "unbound":
      return `unbound at ${l.commit}`
    case "resolved":
      return [
        `resolved ${l.by} ${l.says} at ${l.at} on ${l.commit}`,
        ...(l.verdict === undefined ? [] : [`verdict ${l.verdict}`]),
        ...(l.findings === undefined ? [] : [`findings ${l.findings}`]),
        ...(l.reason === undefined ? [] : [`reason ${oneLine(l.reason)}`])
      ].join("; ")
    case "ruling":
      return `ruling on ${l.commit}: ${oneLine(l.words)}`
    case "changed": {
      const entries = [...l.files.map((f) => `${f.key} ${f.identity === "" ? "none" : f.identity}`), ...(l.foreign ?? []).map((id) => `${NOT_THE_USERS} ${id}`)]
      return `ruled ${l.says} on what changed at ${l.vector}${entries.length === 0 ? "" : `: ${entries.join("; ")}`}`
    }
  }
}

/** Words put on one line, as a line of the ticket holds them. */
const oneLine = (words: string): string => words.split("\n").map((w) => w.trim()).filter((w) => w !== "").join(" ")

/** One line's words read back; none where they are not of a form above, which is then passed over. */
export function readLine(words: string): TicketLine | undefined {
  const [head = "", ...rest] = words.split("; ")
  const w = head.split(" ")
  const after = (key: string): string | undefined => rest.find((p) => p.startsWith(`${key} `))?.slice(key.length + 1)
  if (w[0] === "delivered" && w.length >= 4) {
    const decision = head.includes(` ${DECISION} `)
    const i = w.indexOf("at")
    const when = w[i + 2]
    return { line: "delivered", vector: w[1] ?? "", commit: w[i + 1] ?? "", ...(decision ? { decision: true as const } : {}), ...(when === undefined ? {} : { when: when.slice(1, -1) }) }
  }
  if (w[0] === "left" && w.length === 2 && w[1] !== "") return { line: "left", branch: w[1] ?? "" }
  if (w[0] === "began" && w.length === 4 && w[2] === "at") return { line: "began", vector: w[1] ?? "", commit: w[3] ?? "" }
  if (w[0] === "bound" && w.length === 8) return { line: "bound", vector: w[1] ?? "", enters: w[3] ?? "", ends: w[5] ?? "", commit: w[7] ?? "" }
  if (w[0] === "unbound" && w.length === 3) return { line: "unbound", commit: w[2] ?? "" }
  if (w[0] === "resolved" && w.length === 7 && (w[1] === "evaluation" || w[1] === "user") && (w[2] === "yes" || w[2] === "no")) {
    const verdict = after("verdict")
    const findings = after("findings")
    const reason = after("reason")
    return { line: "resolved", by: w[1], says: w[2], at: w[4] ?? "", commit: w[6] ?? "", ...(verdict === undefined ? {} : { verdict }), ...(findings === undefined ? {} : { findings }), ...(reason === undefined ? {} : { reason }) }
  }
  if (w[0] === "ruled" && (w[1] === "yes" || w[1] === "no") && w[2] === "on" && w[3] === "what" && w[4] === "changed" && w[5] === "at" && w.length >= 7) {
    const colon = words.indexOf(": ")
    const entries = colon < 0 ? [] : words.slice(colon + 2).split("; ").flatMap((entry) => {
      const space = entry.lastIndexOf(" ")
      const identity = entry.slice(space + 1)
      return space < 0 ? [] : [{ key: entry.slice(0, space), identity: identity === "none" ? "" : identity }]
    })
    const files = entries.filter((e) => e.key !== NOT_THE_USERS)
    const foreign = entries.filter((e) => e.key === NOT_THE_USERS).map((e) => e.identity)
    return { line: "changed", says: w[1], vector: (w[6] ?? "").replace(/:$/, ""), files, ...(foreign.length === 0 ? {} : { foreign }) }
  }
  if (w[0] === "ruling" && w[1] === "on" && w.length >= 3) {
    const colon = words.indexOf(": ")
    return { line: "ruling", commit: (w[2] ?? "").replace(/:$/, ""), words: colon < 0 ? "" : words.slice(colon + 2) }
  }
  return undefined
}

/** The binding of a session to a stretch, as the checklist shows it: the last `bound` line, and the line that ended it, if one has (REQ-FLOW-004). */
export function bindingOf(lines: readonly TicketLine[]): { readonly bound: Extract<TicketLine, { line: "bound" }>; readonly ended?: TicketLine } | undefined {
  const at = lines.findLastIndex((l) => l.line === "bound")
  const bound = lines[at]
  if (bound === undefined || bound.line !== "bound") return undefined
  const ended = lines.slice(at + 1).find((l) => l.line === "unbound" || (l.line === "delivered" && l.vector === bound.vector))
  return { bound, ...(ended === undefined ? {} : { ended }) }
}

/**
 * The vector whose work the checklist shows delivered for the user's decision
 * with no answer of the user after it, with the commit that delivery names
 * (REQ-FLOW-006 step 3). `names` gives the names a vector's answer is kept
 * under.
 */
export function awaiting(lines: readonly TicketLine[], names: (vector: string) => readonly string[]): Extract<TicketLine, { line: "delivered" }> | undefined {
  let waiting: Extract<TicketLine, { line: "delivered" }> | undefined
  for (const l of lines) {
    if (l.line === "delivered" && l.decision === true) waiting = l
    else if (waiting !== undefined && l.line === "resolved" && l.by === "user" && names(waiting.vector).includes(l.at)) waiting = undefined
  }
  return waiting
}

/** The names the checklist and the resolutions of a ticket name: each vector whose work began or was delivered, and each name a resolution is at (REQ-FLOW-005 step 1). */
export const workedIn = (lines: readonly TicketLine[]): readonly string[] =>
  [...new Set(lines.flatMap((l) => (l.line === "began" || l.line === "delivered" ? [l.vector] : l.line === "resolved" ? [l.at] : [])))]
