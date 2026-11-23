/**
 * The terms of the graph language (a session, a sequence, a workflow and a
 * reference), what a node and a vector declare, and the constructors that are
 * the only way to make a term. A term that exists has been checked, is in
 * normal form and cannot be changed.
 *
 * @uses C5 H1 H3
 * @is REQ-GRAPH-001 REQ-GRAPH-002 REQ-GRAPH-003
 */
import { covers } from "../kit/place_containment.js"
import { normal, type Shape } from "../kit/term_recursion.js"
import { holdsWhiteSpace } from "../kit/white_space.js"

declare const made: unique symbol
/** Only this module's constructors give a value this mark. */
interface Made {
  readonly [made]: true
}

/** What accepts a node: an evaluation's yes, or the user's yes, which a decision asks for (REQ-GRAPH-003). */
export type Acceptance = "evaluation" | "decision"

/**
 * A node names an asset by its place in the workspace, what must be true of
 * it and its checks, the nodes it depends on: those its asset is made from, and
 * what accepts it. Nothing else in a graph states a dependency, and nothing
 * else states what must be true of an asset or checks it (REQ-GRAPH-003).
 */
export interface Node {
  readonly name: string
  /** A path, or `#` and a name that the definition file gives one or more paths to. */
  readonly place: string
  /** What must be true of its asset, whichever vector writes it: its results, one sentence each. */
  readonly result: readonly string[]
  /** The checks of its asset, whichever vector writes it; none where it is left out. */
  readonly checks?: readonly Check[]
  /** The nodes it depends on, by name; none where it is left out. */
  readonly depends?: readonly string[]
  /** A given asset is one no vector writes, such as a ticket the user writes. */
  readonly given?: true
  /** What accepts it, each once; neither where it is left out. */
  readonly accepted?: readonly Acceptance[]
  /** Where the place is a name: the paths the definition file gives it. */
  readonly paths?: readonly string[]
}

/** The paths of a node's asset: those its name gives it, or its place (REQ-GRAPH-003). */
export function pathsOf(node: Node): readonly string[] {
  return node.paths ?? [node.place]
}

/**
 * What a graph function that writes `writes` rests on: every node those nodes
 * depend on that it does not write itself, in the order the nodes are declared
 * (REQ-GRAPH-005).
 */
export function restsOn(nodes: readonly Node[], writes: readonly string[]): readonly string[] {
  const needed = new Set(nodes.filter((n) => writes.includes(n.name)).flatMap((n) => n.depends ?? []))
  return nodes.map((n) => n.name).filter((name) => needed.has(name) && !writes.includes(name))
}

/**
 * The paths a definition file gives each name: every reference in it whose
 * fragment is the name, as a path from the workspace's folder: `./bin/#x`
 * gives the name x the path bin.
 */
export function namedPlaces(definition: unknown): ReadonlyMap<string, readonly string[]> {
  const named = new Map<string, string[]>()
  const visit = (value: unknown): void => {
    if (typeof value === "object" && value !== null) for (const inner of Object.values(value)) visit(inner)
    if (typeof value !== "string") return
    const at = value.indexOf("#")
    const path = value.slice(0, Math.max(0, at)).replace(/^\.\//, "").replace(/\/$/, "")
    if (at > 0 && isPlace(path)) named.set(value.slice(at + 1), [...(named.get(value.slice(at + 1)) ?? []), path])
  }
  visit(definition)
  return named
}

/** A node whose place is a name, with the paths `named` gives it; any other node as it is. */
export function placed(node: Node, named: ReadonlyMap<string, readonly string[]> | undefined): Node {
  if (named === undefined || !node.place.startsWith("#")) return node
  const paths = named.get(node.place.slice(1)) ?? []
  if (paths.length === 0) throw new TermRefused("places", `node '${node.name}'`, `the definition file gives '${node.place}' no path`)
  return { ...node, paths }
}

/** What runs a check. The kinds are the graph language's whole set. */
export type Run =
  /** A command, run in the checkout; yes when it exits with zero. */
  | { readonly kind: "command"; readonly argv: readonly string[] }
  /** A field of the branch's ticket: present; or equal to `is`; or not equal to `is_not` (absent counts as not equal). */
  | { readonly kind: "ticket_field"; readonly field: string; readonly is?: string; readonly is_not?: string }
  /** Every line the user wrote in the branch's ticket, as main holds it, is still in it. */
  | { readonly kind: "ticket_kept" }
  /**
   * Every name matching `pattern` in the asset `from` is named in the asset `into`, unless the part of
   * `from` that states it says `deferred`; and `into` names none that `from` does not state. The names in
   * `into` of a family in `others`, each written by its name alone, as `HELLO`, are another product's and
   * are left out (D83).
   */
  | {
    readonly kind: "traced"
    readonly pattern: string
    readonly from: string
    readonly into: string
    readonly deferred: string
    readonly others?: readonly string[]
  }

export interface Check {
  readonly name: string
  readonly run: Run
}

/** What it judges against is not declared: it is every node its verdict stands on that the vector does not write (`against`, REQ-GRAPH-002). */
export interface Evaluation {
  /** Where the evaluating session writes its findings. */
  readonly findings: string
  /** Where the evaluating session writes its verdict. */
  readonly verdict: string
}

/** A decision by the user, which is always asked: it declares nothing more (REQ-GRAPH-002). */
export type Decision = Readonly<Record<string, never>>

/** A term of the method a session needs: the file of the method release that states it, and the words of the section's heading. */
export interface MethodTerm {
  readonly term: string
  readonly file: string
  readonly section: string
}

/**
 * The reference frame a session is activated on, as the vector declares it:
 * its name, its revision and the terms of the method its session needs. The
 * rest of the frame is what the vector already declares (REQ-GRAPH-002, D86).
 */
export interface Frame {
  readonly name: string
  readonly revision: number
  readonly method?: readonly MethodTerm[]
}

/** The frame of a vector's working session and, where it declares an evaluation, of its evaluating session. */
export interface Frames {
  readonly work?: Frame
  readonly evaluation?: Frame
}

/** The attempts at a vector, and the minutes of each of its sessions, where it declares none (REQ-PARAM-003, D94). */
export const ATTEMPTS = 3
export const MINUTES = 60

/**
 * What a vector declares (REQ-GRAPH-002). It writes the nodes the graph
 * function of the registry it carries out writes, which its `function` names.
 * What must be true of them, and their checks, are theirs: each node declares
 * them.
 */
export interface Vector {
  readonly name: string
  /** The first vector for a ticket. Its asset is the branch's ticket. */
  readonly first?: true
  /** Only on the first vector: what must be true of the ticket, its asset, which no node declares, and the ticket's checks. */
  readonly result?: readonly string[]
  readonly checks?: readonly Check[]
  readonly evaluation?: Evaluation
  readonly decision?: Decision
  readonly attempts?: number
  readonly minutes?: number
  /** The reference frames its sessions are activated on. */
  readonly frames?: Frames
  readonly function: Term
}

export interface Session extends Made {
  readonly term: "session"
}
export interface Sequence extends Made {
  readonly term: "sequence"
  readonly terms: readonly Term[]
}
export interface Workflow extends Made {
  readonly term: "workflow"
  readonly nodes: readonly Node[]
  readonly vectors: readonly Vector[]
}
/** The stretch an induction entry of a ticket's term inducts: the node its work enters at and the node it ends at (REQ-METHOD-006). */
export interface Stretch {
  readonly enters: string
  readonly ends: string
}

export interface Reference extends Made {
  readonly term: "reference"
  readonly name: string
  /** In a ticket's term, on a reference to the first vector's graph function: the stretch it inducts. */
  readonly enters?: string
  readonly ends?: string
}

/** The stretch a reference names, where it names one. */
export function stretchOf(term: Reference): Stretch | undefined {
  return term.enters === undefined || term.ends === undefined ? undefined : { enters: term.enters, ends: term.ends }
}
export type Term = Session | Sequence | Workflow | Reference

/** Why a term could not be made: the kind of fault, where it is, and what it says. */
export class TermRefused extends Error {
  constructor(
    readonly fault: "terms" | "checks" | "places" | "registry",
    readonly where: string,
    readonly says: string
  ) {
    super(`${where}: ${says}`)
  }
}

function freeze<T>(value: T): T {
  if (typeof value === "object" && value !== null && !Object.isFrozen(value)) {
    for (const inner of Object.values(value)) freeze(inner)
    Object.freeze(value)
  }
  return value
}

/** A name of a node, a vector or a graph function: at least one character, and no white space. */
export function isName(name: string): boolean {
  return name !== "" && !holdsWhiteSpace(name)
}

/** A place is a path relative to the workspace: parts joined by "/", none empty, "." or "..". A path does not start with `#`. */
function isPlace(place: string): boolean {
  return !place.startsWith("#") && place.split("/").every((part) => part !== "" && part !== "." && part !== "..")
}

/** One of two places lies inside the other. */
export function nests(a: string, b: string): boolean {
  return covers(a, b) || covers(b, a)
}

/** The files of the workspace that an asset at `paths` covers (REQ-GRAPH-003). */
export function covered(paths: readonly string[], files: readonly string[]): readonly string[] {
  return files.filter((file) => paths.some((path) => covers(path, file)))
}

function makeSequence(terms: readonly Term[]): Sequence {
  return freeze({ term: "sequence", terms: [...terms] }) as unknown as Sequence
}

function makeWorkflow(nodes: readonly Node[], vectors: readonly Vector[]): Workflow {
  return freeze({ term: "workflow", nodes: [...nodes], vectors: [...vectors] }) as unknown as Workflow
}

/** The shape of terms for the structural recursion, without following references. */
export const termShape: Shape<Term> = {
  parts: (term) =>
    term.term === "sequence" ? term.terms : term.term === "workflow" ? term.vectors.map((v) => v.function) : [],
  rebuild: (term, parts) => {
    if (term.term === "sequence") {
      return parts.length === term.terms.length && parts.every((p, i) => p === term.terms[i]) ? term : makeSequence(parts)
    }
    if (term.term === "workflow") {
      if (parts.every((p, i) => p === term.vectors[i]?.function)) return term
      return makeWorkflow(term.nodes, term.vectors.map((v, i) => ({ ...v, function: parts[i] ?? v.function })))
    }
    return term
  },
  isSequence: (term) => term.term === "sequence",
  isInert: (term) =>
    (term.term === "sequence" && term.terms.length === 0) || (term.term === "workflow" && term.vectors.length === 0)
}

export function session(): Session {
  return freeze({ term: "session" }) as Session
}

/** A sequence, in normal form: inner sequences flattened and terms that do nothing dropped. */
export function sequence(terms: readonly Term[]): Sequence {
  return normal(termShape, makeSequence(terms)) as Sequence
}

/** A reference; with a stretch, both its nodes named, an induction entry of a ticket's term (REQ-METHOD-006). */
export function reference(name: string, stretch: { readonly enters?: string | undefined; readonly ends?: string | undefined } = {}): Reference {
  if (!isName(name)) throw new TermRefused("terms", `reference '${name}'`, "is not a name")
  const { enters, ends } = stretch
  if ((enters === undefined) !== (ends === undefined)) throw new TermRefused("terms", `reference '${name}'`, "names where its stretch enters or where it ends, and not both")
  if (enters === undefined || ends === undefined) return freeze({ term: "reference", name }) as Reference
  for (const node of [enters, ends]) if (!isName(node)) throw new TermRefused("terms", `reference '${name}'`, `'${node}' is not a name`)
  return freeze({ term: "reference", name, enters, ends }) as Reference
}

function checkOf(check: Check, where: string): Check {
  if (check.name.trim() === "") throw new TermRefused("checks", where, "has no name")
  const run = check.run
  if (run.kind === "ticket_field" && run.is !== undefined && run.is_not !== undefined) {
    throw new TermRefused("checks", `${where} '${check.name}'`, "says both is and is_not")
  }
  if (run.kind === "command" && run.argv.length === 0) {
    throw new TermRefused("checks", `${where} '${check.name}'`, "names no command")
  }
  return check
}

function vectorOf(v: Vector): Vector {
  const where = `vector '${v.name}'`
  if (!isName(v.name)) throw new TermRefused("terms", where, `'${v.name}' is not a name`)
  if (v.result !== undefined && v.first !== true) throw new TermRefused("terms", where, "declares what must be true of its result: each node it writes declares that of itself")
  if (v.checks !== undefined && v.first !== true) throw new TermRefused("checks", where, "declares checks: each node it writes declares its own")
  for (const check of v.checks ?? []) checkOf(check, `check of ${where}`)
  if (v.evaluation !== undefined) {
    for (const place of [v.evaluation.findings, v.evaluation.verdict]) {
      if (!isPlace(place)) throw new TermRefused("places", where, `'${place}' is not a place in the workspace`)
    }
  }
  if (v.frames?.evaluation !== undefined && v.evaluation === undefined) {
    throw new TermRefused("terms", where, "declares a frame for an evaluating session, and no evaluation")
  }
  for (const frame of [v.frames?.work, v.frames?.evaluation]) if (frame !== undefined) frameOf(frame, where)
  return v
}

function frameOf(frame: Frame, where: string): Frame {
  if (!isName(frame.name)) throw new TermRefused("terms", where, `the frame '${frame.name}' is not a name`)
  if (!Number.isInteger(frame.revision) || frame.revision < 1) throw new TermRefused("terms", where, `the frame '${frame.name}' has no revision above zero`)
  for (const m of frame.method ?? []) {
    if (m.term.trim() === "" || m.section.trim() === "") throw new TermRefused("terms", where, `the frame '${frame.name}' names a term of the method with no words`)
    if (!isPlace(m.file)) throw new TermRefused("terms", where, `the frame '${frame.name}' names '${m.file}', which is not a place in the method release`)
  }
  return frame
}

/** A workflow: nodes and the vectors between them, each vector with its own graph function. */
export function workflow(nodes: readonly Node[], vectors: readonly Vector[]): Workflow {
  const nodeNames = new Set<string>()
  for (const node of nodes) {
    if (!isName(node.name)) throw new TermRefused("terms", `node '${node.name}'`, "is not a name")
    if (nodeNames.has(node.name)) throw new TermRefused("terms", `node '${node.name}'`, "is declared twice")
    nodeNames.add(node.name)
    if (!(isPlace(node.place) || (node.place.startsWith("#") && isName(node.place.slice(1))))) {
      throw new TermRefused("places", `node '${node.name}'`, `'${node.place}' is not a place in the workspace`)
    }
    for (const name of node.depends ?? []) if (!isName(name)) throw new TermRefused("terms", `node '${node.name}'`, `depends on '${name}', which is not a name`)
    const accepted = node.accepted ?? []
    if (new Set(accepted).size < accepted.length) throw new TermRefused("terms", `node '${node.name}'`, "declares what accepts it twice")
    if (node.given === true && accepted.length > 0) throw new TermRefused("terms", `node '${node.name}'`, "is given, and declares what accepts it, which no vector records")
    for (const check of node.checks ?? []) checkOf(check, `check of node '${node.name}'`)
  }
  const vectorNames = new Set<string>()
  for (const v of vectors) {
    if (vectorNames.has(v.name)) throw new TermRefused("terms", `vector '${v.name}'`, "is declared twice")
    vectorNames.add(v.name)
    vectorOf(v)
  }
  return makeWorkflow(nodes, vectors)
}
