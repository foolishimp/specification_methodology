/**
 * `passes`: the checks of the nodes the vector writes on the workspace, with
 * what each found. Yes only when every one passes, the verdict and the answer
 * at the nodes it writes stand, each node it writes is there and each node it
 * rests on is accepted. So where it says yes, every node it writes is accepted
 * (CALCULUS T6). A verdict or an answer stands only where `since` finds
 * nothing it was given on that differs now (C2); otherwise it counts as
 * absent: requirements changed after the user's yes are not accepted
 * (REQ-METHOD-003). A verdict that says the evaluation cannot judge gives cannot (D90).
 * A check is done where `counts` says, and one not done gives cannot and says
 * so (CALCULUS L3; D18).
 *
 * Acceptance is the node's, as REQ-ALG-004 and CALCULUS section 10 state it
 * (`unaccepted`); a record stands for a node while it, what it declares and
 * the nodes it depends on are as they were. A vector's verdict and answer are recorded at each
 * node it writes that declares them, so the acceptance of a node is read alike
 * whoever wrote it (D164, D168). What an evaluation judges against is derived
 * from the same edges (`against`, D169).
 *
 * The user's yes to the first vector for a ticket stands on the ticket and on
 * what that vector declares of it (D175). It has one outcome besides the
 * ticket's checks:
 * the ticket's term composes (`composes`, REQ-METHOD-006). It reads the
 * acceptance of the nodes the work rests on, and `passes` of the entries
 * before an induction entry of the term. A change to the ticket since the
 * user confirmed it is the user's, and the whole ticket is held to the law,
 * unless the session bound to a stretch of the confirmed term made it; that
 * session may change nothing but the entry's place (REQ-FLOW-004).
 *
 * @uses C2 C3 C5 C6 C7 C14
 * @is REQ-ALG-004 REQ-METHOD-006 REQ-FLOW-004 REQ-METHOD-003
 */
import { difference, paths } from "../kit/map_difference.js"
import { all, type Tri } from "../kit/three_valued.js"
import { restsOn, type Acceptance, type Stretch, type Vector } from "../graph/terms.js"
import { carries, denoted, nodesOf, type Denoted, type TermEntry } from "../graph/walk.js"
import { readTerm } from "../graph/written.js"
import { ASKED, declaration, factsOf, TICKET, type CheckResult, type Given, type Recorded, type Snapshot } from "./facts.js"
import { arrowOf, below, beyond, breaks, checksOf, declaredAt, placedOf, type Arrow, type WellFormed } from "./well_formed.js"

export interface Outcome {
  /** A check of what it writes, the evaluation's verdict, the user's answer, or a node it writes or rests on. */
  readonly source: "check" | "verdict" | "answer" | "node"
  readonly name: string
  readonly result: Tri
  readonly found?: string
}

export interface Passes {
  readonly result: Tri
  readonly outcomes: readonly Outcome[]
}

/** The outcome the first vector for a ticket has besides the ticket's checks (REQ-METHOD-006). */
export const TERM = "the ticket's term composes"

/** The ticket's term, read through the constructors (C14, C5), and what it denotes in the governing graph; or why it denotes nothing. */
function termIn(graph: WellFormed, written: string | undefined): Denoted {
  if (written === undefined || written.trim() === "") return { why: "the ticket gives no term" }
  const read = readTerm(written)
  if ("faults" in read) return { why: `the ticket's term does not read: ${read.faults.map((f) => `${f.where}: ${f.says}`).join("; ")}` }
  return denoted(read.term, graph.graph, graph.registry)
}

/** The vectors the ticket's term names, by name, in its order; none where it does not read or denotes nothing. */
export function termOf(graph: WellFormed, written: string | undefined): readonly string[] | undefined {
  const d = termIn(graph, written)
  return "why" in d ? undefined : d.entries.map((e) => e.v.name)
}

/** The ticket's term as the user reads it: each entry's graph function, an induction entry with its stretch; none where it does not read. */
export function shownTerm(graph: WellFormed, written: string | undefined): readonly string[] | undefined {
  const d = termIn(graph, written)
  return "why" in d ? undefined : d.entries.map((e) => `${carries(e.v) ?? e.v.name}${e.stretch === undefined ? "" : ` over ${e.stretch.enters} to ${e.stretch.ends}`}`)
}

/** The nodes of the graph, inner workflows included, each with the nodes it depends on, by name. */
const dependsOf = (graph: WellFormed): ReadonlyMap<string, readonly string[]> =>
  new Map(nodesOf(graph.graph, graph.registry).map((n) => [n.name, n.depends ?? []]))

/**
 * The work from `enters` to `ends`, which a term over it writes: those two
 * nodes and every node that depends on the first and on which the second
 * depends, directly or through others, in the order the nodes are declared;
 * none where `ends` neither is `enters` nor depends on it (REQ-METHOD-006).
 */
function workOf(graph: WellFormed, enters: string, ends: string): readonly string[] | undefined {
  const under = below(graph, ends)
  if (enters !== ends && !under.has(enters)) return undefined
  return nodesOf(graph.graph, graph.registry).map((n) => n.name)
    .filter((n) => n === enters || n === ends || (under.has(n) && below(graph, n).has(enters)))
}

/** One entry of a term, with the nodes it writes and those it rests on: a vector's; for an induction entry, the work of its stretch. */
interface Step extends Arrow {
  readonly v: Vector
  readonly stretch?: Stretch
}

function stepsOf(graph: WellFormed, entries: readonly TermEntry[]): readonly Step[] {
  const nodes = nodesOf(graph.graph, graph.registry)
  return entries.map(({ v, stretch }) => {
    if (stretch === undefined) return { ...arrowOf(graph, v), v }
    // A stretch on an entry other than an induction entry is refused by the law; the entry writes what its vector writes.
    if (v.first !== true) return { ...arrowOf(graph, v), v, stretch }
    const writes = workOf(graph, stretch.enters, stretch.ends) ?? []
    return { name: carries(v) ?? v.name, v, stretch, writes, rests: restsOn(nodes, writes) }
  })
}

/** What a node declares accepts it: an evaluation's yes, the user's yes, both, or neither (REQ-GRAPH-003). */
const acceptedBy = (graph: WellFormed, node: string): readonly Acceptance[] =>
  nodesOf(graph.graph, graph.registry).find((n) => n.name === node)?.accepted ?? []

/** The field a record of each kind is kept in. */
const fieldOf = (kind: Acceptance): keyof Recorded => (kind === "evaluation" ? "verdict" : "answer")

/** Why a node's records do not hold for it as it is: it is not there, or a record of what it declares does not stand for it with a yes; none where they hold. */
function recordsWhy(graph: WellFormed, node: string, snapshot: Snapshot): string | undefined {
  if (!snapshot.identities.has(node)) return `${node} is not in the workspace`
  const kinds = acceptedBy(graph, node)
  if (kinds.includes("evaluation") && standing(graph, node, "evaluation", snapshot)?.says !== "yes") return `no verdict of yes stands for ${node} as it now is`
  if (kinds.includes("decision") && standing(graph, node, "decision", snapshot)?.says !== "yes") return `the user has not accepted ${node} as it now stands`
  return undefined
}

/** What a check not done gives beside cannot (CALCULUS L3; D18). */
const NOT_DONE = "not done: no answer of it can change what is done next"

/** Where a reading may do checks, in the order of the edges (C7): the ticket, under the first vector's name, where it is `among` the vectors that take part; then the nodes those write and what they depend on. */
export function checkOrder(graph: WellFormed, among: readonly Vector[]): readonly string[] {
  const read = new Set(among.flatMap((v) => placedOf(graph, v).writes).flatMap((n) => [n, ...below(graph, n)]))
  return [...among.filter((v) => v.first === true).map((v) => v.name), ...[...graph.below.keys()].filter((n) => read.has(n))]
}

/** Whether a reading does the checks declared of `at`, on what it read before them in `checkOrder`, for the step on `stepping` where there is one: CALCULUS L3. On the first entry to a vector its working session starts whatever a check says, so none is done (D209). */
export function counts(graph: WellFormed, at: string, snapshot: Snapshot, stepping?: Vector): boolean {
  if (stepping !== undefined && firstEntry(graph, stepping, snapshot)) return false
  if (graph.graph.vectors.some((v) => v.first === true && v.name === at)) return stepping?.name === at || standing(graph, at, "decision", snapshot)?.says === "yes"
  const own = (n: string): boolean => stepping !== undefined && placedOf(graph, stepping).writes.includes(n)
  return snapshot.identities.has(at) && (own(at) || recordsWhy(graph, at, snapshot) === undefined) &&
    (dependsOf(graph).get(at) ?? []).every((d) => own(d) || unaccepted(graph, d, snapshot) === undefined)
}

/**
 * Why a node is not accepted on the workspace as it is, and the node where
 * that begins, `at`: of the node and every node it depends on, through any
 * others, the first in the order of the edges (C7) whose own declaration does
 * not hold. None where the node is accepted (CALCULUS section 10). A term's
 * law looks first past the nodes the term writes (`written`), so the reason it
 * gives is one the term does not already mend.
 */
export function unaccepted(graph: WellFormed, node: string, snapshot: Snapshot, written: ReadonlySet<string> = new Set()): { readonly why: string; readonly at: string } | undefined {
  // Its own declaration: its records, then its checks.
  const own = (n: string): string | undefined => {
    const check = declaredAt(graph, n).find((c) => snapshot.checks?.get(c.name)?.result !== "yes")
    return recordsWhy(graph, n, snapshot) ?? (check && `the check "${check.name}" of ${n} says ${snapshot.checks?.get(check.name)?.result ?? "nothing: it was not done"}`)
  }
  const up = [...graph.below.keys()].filter((n) => n === node || below(graph, node).has(n))
  const at = up.find((n) => !written.has(n) && own(n) !== undefined) ?? up.find((n) => written.has(n) && own(n) !== undefined)
  return at === undefined ? undefined : { why: own(at) ?? "", at }
}

/**
 * The node a ticket enters at where `node` is not accepted and its work enters
 * at `enters` and ends at `ends`: the nearest node on which both `node` and
 * `enters` depend, or that is one of them, at which a vector of the governing
 * graph can be the term's first entry, writing that node, declaring an
 * evaluation or a decision, and writing nothing outside the work from there to
 * `ends`. None where there is no such node (REQ-METHOD-006).
 */
function enterAt(graph: WellFormed, node: string, enters: string | undefined, ends: string | undefined): string | undefined {
  const names = nodesOf(graph.graph, graph.registry).map((n) => n.name)
  const upTo = (n: string): ReadonlySet<string> => new Set([n, ...below(graph, n)])
  const from = upTo(node)
  const work = enters !== undefined && names.includes(enters) ? upTo(enters) : new Set(names)
  const known = ends !== undefined && names.includes(ends)
  const can = names.filter((x) => from.has(x) && work.has(x) && graph.graph.vectors.some((v) => {
    if (v.first === true || (v.evaluation === undefined && v.decision === undefined)) return false
    const writes = placedOf(graph, v).writes
    const within = known ? workOf(graph, x, ends) : undefined
    return writes.includes(x) && (!known || (within !== undefined && writes.every((n) => within.includes(n))))
  }))
  return can.find((x) => !can.some((y) => y !== x && below(graph, y).has(x)))
}

/**
 * The law of a term over the work it fills, from `enters` to `ends`, and every
 * finding where it does not hold (REQ-METHOD-006; CALCULUS.md section 10, T3):
 * the ticket's term over the triage's work, or a term in an induction entry's
 * place over that entry's stretch. Each entry is carried out by one vector of
 * the graph and writes its nodes; one of the first vector's is an induction
 * entry, which names its stretch and writes the work of it, less than the work
 * it lies in, and no other entry names one. The term composes: each entry
 * rests on nodes an entry before it writes, or that are accepted on the
 * workspace as it is and written by no entry of the term, and no node is
 * written twice. It writes exactly the work. The vector of its first entry
 * declares an evaluation or a decision (REQ-FLOW-004).
 */
function law(graph: WellFormed, steps: readonly Step[], enters: string | undefined, ends: string | undefined, snapshot: Snapshot): readonly string[] {
  const nodes = new Map(graph.graph.nodes.map((n) => [n.name, n]))
  const named = (field: string, node: string | undefined): readonly string[] =>
    node === undefined
      ? [`the ticket names no node at which the work ${field}`]
      : nodes.get(node) === undefined
      ? [`no node of the graph is ${node}`]
      : nodes.get(node)?.given === true
      ? [`${node} is given, and no graph function writes it`]
      : []
  const faults = [...named("enters", enters), ...named("ends", ends)]
  const work = faults.length === 0 && enters !== undefined && ends !== undefined ? workOf(graph, enters, ends) : undefined
  const span = `the work from ${enters ?? ""} to ${ends ?? ""}`
  const head = steps[0]
  const over = (s: Stretch): string => `the induction entry over ${s.enters} to ${s.ends}`
  const written = new Set(steps.flatMap((s) => s.writes))
  const held = (n: string): string | undefined => {
    const not = unaccepted(graph, n, snapshot, written)
    if (not === undefined) return undefined
    const at = enterAt(graph, not.at, enters, ends)
    return at === undefined
      ? `${not.why}; no ticket enters where both ${not.at} and this work are reached, so a run with no ticket accepts ${not.at} first`
      : `${not.why}; enter at ${at}`
  }
  const exactly = work === undefined ? undefined : beyond(steps, work)
  return [
    ...(head === undefined ? ["the term names no graph function"] : []),
    ...steps.filter((s) => s.v.first === true && s.stretch === undefined).map((s) => `the term names ${s.name}, the graph function of the first vector for a ticket, with no stretch: an induction entry names the node it enters at and the node it ends at`),
    ...steps.filter((s) => s.v.first !== true && s.stretch !== undefined).map((s) => `${s.name} names a stretch, and only an induction entry names one`),
    ...steps.flatMap((s) => {
      if (s.v.first !== true || s.stretch === undefined) return []
      return s.writes.length === 0
        ? [`${over(s.stretch)} names no stretch of the graph: ${s.stretch.ends} neither is ${s.stretch.enters} nor depends on it`]
        : work !== undefined && s.writes.length === work.length && s.writes.every((n) => work.includes(n))
        ? [`${over(s.stretch)} is the whole of ${span}; a term for it is chosen now`]
        : []
    }),
    ...faults,
    ...(faults.length === 0 && work === undefined ? [`the work ends at ${ends ?? ""}, which neither is ${enters ?? ""} nor depends on it`] : []),
    ...breaks(steps, held),
    ...(exactly?.missing ?? []).map((n) => `no entry of the term writes ${n}, which ${span} covers`),
    ...(exactly?.extra ?? []).map(([name, n]) => `${name} writes ${n}, which lies outside ${span}`),
    ...(head?.stretch === undefined ? [] : [`the term begins with ${over(head.stretch)}: an induction entry fits only a later stretch, once the entries before it are accepted`]),
    ...(head !== undefined && head.v.evaluation === undefined && head.v.decision === undefined
      ? [`${head.v.name}, by which the ticket enters, declares neither an evaluation nor a decision`]
      : [])
  ]
}

/** The first vector for a ticket, and the user's confirmation of the induction where one is written. The snapshot holds an answer there only where it names this ticket, so one a merge carried in from another ticket is none (REQ-FLOW-004, D200). */
const confirmation = (graph: WellFormed, snapshot: Snapshot): { readonly first: Vector; readonly given: Given } | undefined => {
  const first = graph.graph.vectors.find((v) => v.first === true)
  const given = first === undefined ? undefined : snapshot.records?.get(first.name)?.answer
  return first === undefined || given?.says !== "yes" ? undefined : { first, given }
}

/**
 * The identity of the ticket as the user last confirmed its induction, where
 * the ticket has changed since: git holds that ticket's text under it (C1),
 * and a term in the place of an induction entry is held to the term then
 * confirmed (REQ-METHOD-006).
 */
export function confirmedOn(graph: WellFormed, snapshot: Snapshot): string | undefined {
  const c = confirmation(graph, snapshot)
  if (c === undefined || snapshot.ticket === "simplest") return undefined
  const on = c.given.on.get(TICKET)
  return on === undefined || on === snapshot.ticket.identity ? undefined : c.given.commit
}

/**
 * The ticket as the user last confirmed its induction, where the session
 * bound to a stretch of its term has changed it since: its fields, and the
 * identity of its text without its term (D141), which `gather` reads by the
 * identity the confirmation holds (C1). A change no such session made is the
 * user's, and is given no `Confirmed` (REQ-FLOW-004).
 */
export interface Confirmed {
  readonly fields: ReadonlyMap<string, string>
  readonly asked: string
}

/** Where the induction of a stretch is under way: the entry the run has reached, at `at` in the confirmed term `steps`; `changed` where the session bound to it has changed the ticket since that confirmation, which git holds as `confirmed`. */
interface Inducting {
  readonly stretch: Stretch
  readonly at: number
  readonly steps: readonly Step[]
  readonly changed: boolean
  readonly confirmed: string
}

/**
 * The induction entry of the confirmed term the run has reached: the entries
 * before it each pass on the workspace as it is. Once the session bound to its
 * stretch has changed the ticket, the stretch stays under way, whatever that
 * change reopened. Where the ticket has changed since the confirmation and no
 * such session made the change, the change is the user's, and none is under
 * way: the whole ticket is held to the law and confirmed again (REQ-FLOW-004).
 */
function inductingIn(graph: WellFormed, fields: ReadonlyMap<string, string>, snapshot: Snapshot, confirmed: Confirmed | undefined): Inducting | undefined {
  const c = confirmation(graph, snapshot)
  const on = c?.given.on.get(TICKET)
  if (c === undefined || on === undefined || snapshot.ticket === "simplest") return undefined
  const changed = standing(graph, c.first.name, "decision", snapshot) === undefined
  if (changed && confirmed === undefined) return undefined
  const d = termIn(graph, (changed ? confirmed?.fields : fields)?.get("term"))
  if ("why" in d) return undefined
  const steps = stepsOf(graph, d.entries)
  const at = steps.findIndex((s) => s.stretch !== undefined)
  const stretch = steps[at]?.stretch
  const reached = changed || steps.slice(0, at).every((s) => passes(graph, s.v, snapshot).result === "yes")
  // An induction entry is never a term's first, so one at the head is no stretch to reach: the term's law refuses it.
  return stretch === undefined || at === 0 || !reached ? undefined : { stretch, at, steps, changed, confirmed: c.given.commit ?? on }
}

/**
 * The stretch of the induction entry of the confirmed term that the run has
 * reached, or whose place the session bound to it is filling; `confirmed` the
 * ticket as the user last confirmed it, where that session has changed it
 * since. The induction's packet is bound to it (REQ-ALG-007).
 */
export function inducting(graph: WellFormed, fields: ReadonlyMap<string, string>, snapshot: Snapshot, confirmed?: Confirmed): Stretch | undefined {
  return inductingIn(graph, fields, snapshot, confirmed)?.stretch
}

/**
 * What the induction's checks found where the ticket had changed since the
 * user confirmed its induction, no session bound to a stretch made the
 * change, and a check of the first vector, its term's among them, said no:
 * the induction then runs again on the whole ticket, and the question says so
 * (REQ-FLOW-004). None otherwise.
 */
export function overturned(graph: WellFormed, snapshot: Snapshot): string | undefined {
  const c = confirmation(graph, snapshot)
  if (c === undefined || snapshot.ticket === "simplest" || snapshot.ticket.inducting !== undefined) return undefined
  if (standing(graph, c.first.name, "decision", snapshot) !== undefined) return undefined
  const failed = passes(graph, c.first, snapshot).outcomes.filter((o) => o.source === "check" && o.result === "no")
  return failed.length === 0 ? undefined : failed.map((o) => (o.found === undefined ? o.name : `${o.name} (${o.found})`)).join("; ")
}

/**
 * Whether the term a ticket carries is well formed, and every reason it is
 * not (REQ-METHOD-006; CALCULUS.md section 10, T3 and T5). `confirmed` is
 * the ticket as the user last confirmed its induction, where the session
 * bound to a stretch has changed it since (REQ-FLOW-004).
 *
 * Where the confirmation stands and the run has reached an induction entry of
 * the term, it says no, so that the induction runs again, bound to that
 * entry's stretch. Where the session so bound has changed the ticket since,
 * the new term is the confirmed one with exactly that entry replaced, by a
 * term that obeys the law on the entry's stretch (T5), and
 * every other line of the ticket is as the user confirmed it. Otherwise the
 * term obeys the law on the work from the triage's `enters` to its `ends`.
 */
export function composes(graph: WellFormed, fields: ReadonlyMap<string, string>, snapshot: Snapshot, confirmed?: Confirmed): CheckResult {
  const d = termIn(graph, fields.get("term"))
  if ("why" in d) return { result: "no", found: d.why }
  const steps = stepsOf(graph, d.entries)
  const at = inductingIn(graph, fields, snapshot, confirmed)
  const why: readonly string[] = at === undefined
    ? law(graph, steps, fields.get("enters"), fields.get("ends"), snapshot)
    : !at.changed
    ? [`the run has reached the induction entry over ${at.stretch.enters} to ${at.stretch.ends}: a term for that stretch is to take its place`]
    : substituted(graph, at, steps, snapshot, confirmed)
  return why.length === 0 ? { result: "yes" } : { result: "no", found: why.join("; ") }
}

/**
 * The findings on what the session bound to the induction entry `at` of the
 * confirmed term wrote in the ticket (REQ-METHOD-006, T5): the term is the
 * confirmed one with that entry alone replaced, the term in its place obeys
 * the law on the stretch, and no other line changed. Each finding names the
 * ticket the user confirmed by the identity git holds it under.
 */
function substituted(graph: WellFormed, at: Inducting, steps: readonly Step[], snapshot: Snapshot, confirmed: Confirmed | undefined): readonly string[] {
  const before = at.steps.slice(0, at.at)
  const after = at.steps.slice(at.at + 1)
  const same = (a: Step | undefined, b: Step | undefined): boolean =>
    a !== undefined && b !== undefined && a.v === b.v && a.stretch?.enters === b.stretch?.enters && a.stretch?.ends === b.stretch?.ends
  const kept = steps.length >= before.length + after.length &&
    before.every((s, i) => same(s, steps[i])) && after.every((s, i) => same(s, steps[steps.length - after.length + i]))
  const blob = `the ticket the user confirmed is held by the commit ${at.confirmed} in git`
  const lines = snapshot.ticket !== "simplest" && confirmed !== undefined && confirmed.asked !== snapshot.ticket.asked
    ? [`a line of the ticket other than its term is not as the user confirmed it, and the session writes only the term in the entry's place; ${blob}`]
    : []
  return [
    ...(kept
      ? law(graph, steps.slice(before.length, steps.length - after.length), at.stretch.enters, at.stretch.ends, snapshot)
      : [`the term is not the one the user confirmed with the induction entry over ${at.stretch.enters} to ${at.stretch.ends} alone replaced; ${blob}`]),
    ...lines
  ]
}

/** The identity of an asset by node name, of the branch's ticket under TICKET, or of that ticket without its term under ASKED, now. */
export function identityNow(key: string, snapshot: Snapshot): string | undefined {
  if (key === TICKET) return snapshot.ticket === "simplest" ? undefined : snapshot.ticket.identity
  if (key === ASKED) return snapshot.ticket === "simplest" ? undefined : snapshot.ticket.asked
  return snapshot.identities.get(key)
}

/**
 * The names a vector's verdict (`evaluation`) or answer (`decision`) is
 * recorded under, where it declares that kind: each node it writes that
 * declares it too; for the first vector, which writes no node, its own name
 * (D164).
 */
export function recordsOf(graph: WellFormed, v: Vector, kind: Acceptance): readonly string[] {
  if ((kind === "evaluation" ? v.evaluation : v.decision) === undefined) return []
  if (v.first === true) return [v.name]
  return placedOf(graph, v).writes.filter((n) => acceptedBy(graph, n).includes(kind))
}

/**
 * What a record kept under `at` stands for: under the first vector's name, the
 * ticket and what that vector declares of it; at a node, that node, what it
 * declares of itself, the nodes it depends on and, where the ticket enters at
 * it, the ticket without its term (D141, D168, D175).
 */
export function standingKeys(graph: WellFormed, at: string, snapshot: Snapshot): readonly string[] {
  if (graph.graph.vectors.some((v) => v.first === true && v.name === at)) return [TICKET, declaration(at)]
  const enters = snapshot.ticket === "simplest" ? undefined : snapshot.ticket.enters
  return [at, declaration(at), ...(dependsOf(graph).get(at) ?? []), ...(enters === at ? [ASKED] : [])]
}

/**
 * What a vector's evaluation judges the nodes it writes against: every node
 * its verdict stands on that it does not write, the nodes those it records the
 * verdict at depend on, in the order the nodes are declared; none where it
 * declares no evaluation (REQ-GRAPH-002, D169).
 */
export function against(graph: WellFormed, v: Vector): readonly string[] {
  const deps = dependsOf(graph)
  const on = new Set(recordsOf(graph, v, "evaluation").flatMap((n) => deps.get(n) ?? []))
  const writes = placedOf(graph, v).writes
  return nodesOf(graph.graph, graph.registry).map((n) => n.name).filter((n) => on.has(n) && !writes.includes(n))
}

/**
 * The identities at the standing keys of a record kept under `at`, by key: as
 * `identityOf` gives them, by default as they are now. A key with no content
 * has no identity, and so no entry; "" is none (CALCULUS section 4).
 */
export function identitiesAt(graph: WellFormed, at: string, snapshot: Snapshot, identityOf = (key: string): string | undefined => identityNow(key, snapshot)): ReadonlyMap<string, string> {
  return new Map(standingKeys(graph, at, snapshot).flatMap((key) => {
    const id = identityOf(key)
    return id === undefined || id === "" ? [] : [[key, id] as const]
  }))
}

/** What a record kept under `at`, given on `on`, stands on whose identity now differs (C2), in the order of its standing keys: empty exactly where it stands (CALCULUS section 4). */
export function since(graph: WellFormed, at: string, on: ReadonlyMap<string, string>, snapshot: Snapshot): readonly string[] {
  const differs = new Set(paths(difference(identitiesAt(graph, at, snapshot, (key) => on.get(key)), identitiesAt(graph, at, snapshot))))
  return standingKeys(graph, at, snapshot).filter((key) => differs.has(key))
}

/** The record of `kind` kept under `at`, as written, whether or not it stands. */
export const recordAt = (at: string, kind: Acceptance, snapshot: Snapshot): Given | undefined => snapshot.records?.get(at)?.[fieldOf(kind)]

/** The record of `kind` kept under `at`, where it stands for the content as it is now; otherwise undefined. */
function standing(graph: WellFormed, at: string, kind: Acceptance, snapshot: Snapshot): Given | undefined {
  const given = recordAt(at, kind, snapshot)
  return given === undefined || since(graph, at, given.on, snapshot).length > 0 ? undefined : given
}

/**
 * The vector's own verdict or answer, where it stands under every name it is
 * recorded under: what it says there is no where one says no, cannot where
 * one cannot judge, and otherwise yes. Undefined where one does not stand.
 */
export function standsFor(graph: WellFormed, v: Vector, kind: Acceptance, snapshot: Snapshot): Given | undefined {
  const got = recordsOf(graph, v, kind).map((at) => standing(graph, at, kind, snapshot))
  const [one] = got
  if (one === undefined || got.some((g) => g === undefined)) return undefined
  const says = got.some((g) => g?.says === "no") ? "no" : got.some((g) => g?.says === "cannot") ? "cannot" : "yes"
  return { ...one, says }
}

function judged(source: "verdict" | "answer", given: Given | undefined, at: string | undefined): Outcome {
  if (given === undefined) return { source, name: source, result: "no", found: `no ${source} stands for the content as it is now` }
  return {
    source,
    name: source,
    result: given.says === "yes" ? "yes" : given.says === "cannot" ? "cannot" : "no",
    found: given.at ?? at ?? `the ${source} says ${given.says}`
  }
}

/** The user is asked on this vector: it declares a decision, no answer stands, and every other outcome passes (REQ-FLOW-006). */
export function asksUser(graph: WellFormed, vector: Vector, snapshot: Snapshot): boolean {
  if (vector.decision === undefined || standsFor(graph, vector, "decision", snapshot) !== undefined) return false
  return passes(graph, vector, snapshot).outcomes.every((o) => o.source === "answer" || o.result === "yes")
}

/** Whether the reading did what the outcome says: all but a check not done, which is neither yes nor no, is not logged as run and fails nothing (CALCULUS L3; guard rail 6). */
export const isDone = (o: Outcome): boolean => o.found !== NOT_DONE

/** The checks a step stops on: those the reading did that could not be run (REQ-FLOW-005). */
export const cannotRun = (p: Passes): readonly Outcome[] => p.outcomes.filter((o) => o.source === "check" && o.result === "cannot" && isDone(o))

export function passes(graph: WellFormed, vector: Vector, snapshot: Snapshot): Passes {
  const checked = (name: string, got: CheckResult | undefined): Outcome => got === undefined
    ? { source: "check", name, result: "cannot", found: NOT_DONE }
    : { source: "check", name, result: got.result, ...(got.found === undefined ? {} : { found: got.found }) }
  const outcomes: Outcome[] = checksOf(graph, vector).map((c) => checked(c.name, snapshot.checks?.get(c.name)))
  if (vector.first === true && snapshot.ticket !== "simplest") outcomes.push(checked(TERM, factsOf(snapshot, vector.name).composes))
  if (vector.evaluation !== undefined) outcomes.push(judged("verdict", standsFor(graph, vector, "evaluation", snapshot), vector.evaluation.verdict))
  if (vector.decision !== undefined) outcomes.push(judged("answer", standsFor(graph, vector, "decision", snapshot), undefined))
  // Each node it writes is there, and each node it rests on is accepted: named where it is not (REQ-ALG-004).
  for (const n of placedOf(graph, vector).writes.filter((x) => !snapshot.identities.has(x))) outcomes.push({ source: "node", name: n, result: "no", found: `${n} is not in the workspace` })
  for (const n of placedOf(graph, vector).rests) {
    const not = unaccepted(graph, n, snapshot)
    if (not !== undefined) outcomes.push({ source: "node", name: n, result: "no", found: not.why })
  }
  return { result: all(outcomes.map((o) => o.result)), outcomes }
}

/**
 * The first entry to a vector under the ticket's confirmed term (REQ-FLOW-005
 * step 1, D209): the confirmation of the induction stands, the term names the
 * vector, and the ticket's checklist and resolutions name neither the vector
 * nor a name it records at. Its working session then starts with no question
 * and no evaluation before it. The first vector, an inner vector and every
 * vector of the simplest ticket are judged first, as is a vector after any
 * work under the ticket.
 */
export function firstEntry(graph: WellFormed, v: Vector, snapshot: Snapshot): boolean {
  const ticket = snapshot.ticket
  const first = graph.graph.vectors.find((w) => w.first === true)
  if (ticket === "simplest" || first === undefined || v.first === true || !(ticket.term ?? []).includes(v.name)) return false
  if (standing(graph, first.name, "decision", snapshot)?.says !== "yes") return false
  const worked = new Set(ticket.worked ?? [])
  return ![v.name, ...recordsOf(graph, v, "evaluation"), ...recordsOf(graph, v, "decision")].some((n) => worked.has(n))
}
