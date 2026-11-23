/**
 * `well_formed`: a governing graph and its registry, as written, are well
 * formed, or the reasons they are not. Only a well-formed graph is ever
 * traversed: the other algorithms take what this one gives.
 *
 * A graph is its nodes and the nodes each depends on, and each node declares
 * what must be true of it, its checks and what accepts it; only the first
 * vector, whose asset is the ticket, declares results and checks of its own,
 * which reading refuses on any other (C5). No two checks share a name. Every vector carries out a graph function of the registry,
 * which names the nodes it writes; what it rests on is every node those depend
 * on that it does not write (`restsOn`). A vector records its verdict and its
 * answer at each node it writes that declares them, so it declares an
 * evaluation or a decision only where a node it writes declares one, and a
 * vector of the governing graph declares each that a node it writes declares:
 * in the method's graph, whose nodes of the specification each declare the
 * user's decision, each vector that writes one ends in it (REQ-METHOD-003).
 * Entries compose exactly where each rests on nodes written before it or held
 * at the start, and none writes a node twice. Where no term gives an order, as
 * in an inner workflow, the edges give one (C7) (REQ-METHOD-006; CALCULUS.md
 * section 10).
 *
 * @uses C5 C6 C7 C14
 * @is REQ-ALG-002 REQ-METHOD-003
 */
import { needed, ordered, type Dependencies } from "../kit/dependency_order.js"
import type { Registry } from "../graph/registry.js"
import { nests, pathsOf, restsOn, type Check, type Node, type Term, type Vector, type Workflow } from "../graph/terms.js"
import { carries, denoted, inPlace, nodesOf, resolution, stretched, workflows, type TermEntry } from "../graph/walk.js"
import { readGraph, readRegistry, type Fault } from "../graph/written.js"

/**
 * The conditions: `writes` every vector carries out a graph function of the registry, it writes at least
 * one node and no given one, the first vector writes none, a vector
 * declares an evaluation, or a decision, only where a node it writes declares one, and a vector of the
 * governing graph declares each that a node it writes declares; `places` no asset's place lies inside
 * another's; `checks` every check says what runs it, and no two checks of the graph share a name; `registry` every graph function named is in the
 * registry, each entry writes nodes of the graph, and the definition of each entry no vector carries out
 * denotes vectors of the graph that compose from what it rests on and write exactly what it writes
 * (REQ-GRAPH-005); `terms` every term is one the language has, every node a node depends on is declared, no
 * two nodes and no two vectors of the graph, inner workflows included, share a name, no reference in the
 * graph or the registry names a stretch, the registry's default term denotes vectors of the graph other
 * than the first and composes, and the vectors of each inner workflow compose from what the vector holding
 * it rests on and write exactly what it writes; `first` at most one first vector for a ticket; `cycle` no
 * name leads back to itself, and no node depends on itself.
 */
export type Rule = "writes" | "places" | "checks" | "registry" | "terms" | "first" | "cycle"

export interface Reason {
  readonly rule: Rule
  readonly where: string
  readonly says: string
}

/** What a vector writes, and what it rests on. */
export interface Placed {
  /** The nodes it writes: those of the graph function it carries out. */
  readonly writes: readonly string[]
  /** What it rests on: every node those depend on that it does not write. */
  readonly rests: readonly string[]
}

declare const made: unique symbol
/** A graph and its registry that are well formed. Only `well_formed` makes one. */
export interface WellFormed {
  readonly [made]: true
  readonly graph: Workflow
  readonly registry: Registry
  /**
   * The vectors of the graph the registry's default term denotes, by name, in its order: what a ticket that
   * carries no term is built by (REQ-METHOD-006). Where the registry declares none, every vector of the
   * graph but the first, in the order the edges give (C7).
   */
  readonly byDefault: readonly string[]
  /** Each vector of the graph's workflows, by name, with what it writes and what it rests on. */
  readonly placed: ReadonlyMap<string, Placed>
  /** The vectors of each inner workflow, by name, in the order the edges give (C7). */
  readonly orders: ReadonlyMap<Workflow, readonly string[]>
  /** Each node, inner workflows' included, in the order of the edges, with every node it depends on, through any others (C7's `needed`). */
  readonly below: ReadonlyMap<string, ReadonlySet<string>>
}

export type Verdict = { readonly yes: WellFormed } | { readonly no: readonly Reason[] }

/** What the vector writes, and what it rests on. */
export function placedOf(graph: WellFormed, v: Vector): Placed {
  return graph.placed.get(v.name) ?? { writes: [], rests: [] }
}

const NONE: ReadonlySet<string> = new Set()

/** Every node a node depends on, through any others (C7). */
export const below = (graph: WellFormed, node: string): ReadonlySet<string> => graph.below.get(node) ?? NONE

/** The checks the graph declares of `at`: of a node, or, under the first vector's name, of the ticket, which that vector declares (REQ-GRAPH-003). */
export const declaredAt = (graph: WellFormed, at: string): readonly Check[] =>
  graph.graph.vectors.find((v) => v.first === true && v.name === at)?.checks ?? nodesOf(graph.graph, graph.registry).find((n) => n.name === at)?.checks ?? []

/** A vector's checks, which it does not declare: those of the nodes it writes; for the first vector, the ticket's (REQ-GRAPH-002). */
export const checksOf = (graph: WellFormed, v: Vector): readonly Check[] => (v.first === true ? [v.name] : placedOf(graph, v).writes).flatMap((at) => declaredAt(graph, at))

/** A term's entry: its name, the nodes it writes and the nodes it rests on. */
export interface Arrow {
  readonly name: string
  readonly writes: readonly string[]
  readonly rests: readonly string[]
}

/** The entry of a term that a vector of the graph carries out, by its graph function's name. */
export const arrowOf = (graph: WellFormed, v: Vector): Arrow => ({ name: carries(v) ?? v.name, writes: placedOf(graph, v).writes, rests: placedOf(graph, v).rests })

/**
 * Every place where a list of entries does not compose (CALCULUS.md section
 * 10, T3): an entry rests on a node that no entry before it writes and that
 * the state it starts from does not hold, an entry of the list writing it at
 * or after that one included, said once for each node, at the first entry
 * that rests on it; or it writes a node an entry before it writes.
 * `held` says why the state does not hold a node no entry writes, or gives
 * undefined where it holds it.
 */
export function breaks(arrows: readonly Arrow[], held: (node: string) => string | undefined): readonly string[] {
  const all = new Set(arrows.flatMap((a) => a.writes))
  const before = new Set<string>()
  const said = new Set<string>()
  const found: string[] = []
  for (const a of arrows) {
    for (const n of a.rests.filter((r) => !before.has(r) && !said.has(r))) {
      const why = all.has(n) ? "" : held(n)
      if (why === undefined) continue
      said.add(n)
      found.push(`${a.name} rests on ${n}, which is neither accepted nor written before it${why === "" ? "" : `: ${why}`}`)
    }
    for (const n of a.writes.filter((w) => before.has(w))) found.push(`${a.name} writes ${n}, which an entry before it writes`)
    for (const n of a.writes) before.add(n)
  }
  return found
}

/** Where a list of entries does not write exactly `nodes`: each node of them no entry writes, and each entry with a node it writes beyond them. */
export function beyond(arrows: readonly Arrow[], nodes: readonly string[]): { readonly missing: readonly string[]; readonly extra: readonly (readonly [string, string])[] } {
  const written = new Set(arrows.flatMap((a) => a.writes))
  return {
    missing: nodes.filter((n) => !written.has(n)),
    extra: arrows.flatMap((a) => a.writes.filter((n) => !nodes.includes(n)).map((n) => [a.name, n] as const))
  }
}

const reasonOf = (fault: Fault): Reason => ({ rule: fault.fault, where: fault.where, says: fault.says })

/** `named`: the paths the definition file gives each name a place may be (REQ-GRAPH-003). */
export function well_formed(graphText: string, registryText: string, named?: ReadonlyMap<string, readonly string[]>): Verdict {
  const g = readGraph(graphText, named)
  const r = readRegistry(registryText, named)
  const read: Reason[] = []
  if ("faults" in g) read.push(...g.faults.map(reasonOf))
  if ("faults" in r) read.push(...r.faults.map(reasonOf))
  if ("faults" in g || "faults" in r) return { no: read }
  const graph = g.graph
  const reg = r.registry

  const resolved = resolution(graph, reg)
  const names: Reason[] = [
    ...resolved.unknown.map((name): Reason => ({
      rule: "registry",
      where: `reference '${name}'`,
      says: "names a graph function that is not in the registry"
    })),
    ...resolved.cyclic.map((name): Reason => ({
      rule: "cycle",
      where: `graph function '${name}'`,
      says: "leads back to itself"
    }))
  ]
  if (names.length > 0) return { no: names }

  const held = workflows(graph, reg)
  const nodes: Node[] = held.flatMap((w) => w.nodes)
  const vectors: Vector[] = held.flatMap((w) => w.vectors)
  const reasons: Reason[] = []

  // One name, one term in the whole graph, inner workflows included: a node's names its asset; a check's keys its result in a reading, the
  // log and what was found; a vector's keys its attempts, records, packets and log entries (D154).
  const twice = (names: readonly string[]): readonly string[] => [...new Set(names.filter((n, i) => names.indexOf(n) !== i))]
  for (const n of twice(nodes.map((x) => x.name))) reasons.push({ rule: "terms", where: `node '${n}'`, says: "is declared twice" })
  for (const n of twice([...nodes, ...vectors].flatMap((x) => x.checks ?? []).map((c) => c.name))) reasons.push({ rule: "checks", where: `check '${n}'`, says: "is declared twice in the graph, inner workflows included" })
  for (const n of twice(vectors.map((v) => v.name))) reasons.push({ rule: "terms", where: `vector '${n}'`, says: "is declared twice in the graph, inner workflows included" })
  const byName = new Map(nodes.map((n) => [n.name, n] as const).reverse())

  // The edges: every node a node depends on is declared, and no node depends on itself, directly or through others (C7).
  for (const node of nodes) {
    for (const d of (node.depends ?? []).filter((x) => !byName.has(x))) reasons.push({ rule: "terms", where: `node '${node.name}'`, says: `depends on '${d}', which no node declares` })
  }
  const edges: Dependencies<Node> = { needs: (n) => n.depends ?? [], produces: (n) => [n.name] }
  const { order: byEdges, left: looped } = ordered(nodes, edges)
  if (looped.length > 0) {
    reasons.push({ rule: "cycle", where: looped.map((n) => `node '${n.name}'`).join(", "), says: "depend on themselves, directly or through other nodes, or on a node that does" })
    return { no: reasons }
  }
  const under = new Map([...needed(byEdges, edges)].map(([n, ns]) => [n.name, new Set([...ns].map((x) => x.name))] as const))
  const given = (name: string): boolean => byName.get(name)?.given === true

  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const a = nodes[i]
      const b = nodes[j]
      if (a !== undefined && b !== undefined && a.name !== b.name && pathsOf(a).some((p) => pathsOf(b).some((q) => nests(p, q)))) {
        reasons.push({
          rule: "places",
          where: `nodes '${a.name}' and '${b.name}'`,
          says: `'${pathsOf(a).join(", ")}' and '${pathsOf(b).join(", ")}': one lies inside the other`
        })
      }
    }
  }

  const firsts = vectors.filter((v) => v.first === true)
  if (firsts.length > 1) {
    reasons.push({
      rule: "first",
      where: firsts.map((v) => `vector '${v.name}'`).join(", "),
      says: `${firsts.length} vectors are the first vector for a ticket; a graph has at most one`
    })
  }

  // Each entry writes nodes of the graph (REQ-GRAPH-005).
  for (const entry of reg.entries) {
    for (const n of entry.writes.filter((x) => !byName.has(x))) {
      reasons.push({ rule: "registry", where: `registry entry '${entry.name}'`, says: `writes '${n}', which is no node of the graph` })
    }
  }

  // What each vector writes and what it rests on; the vectors of an inner workflow compose from what the vector holding it rests on, and write what it writes.
  const entries = new Map(reg.entries.map((e) => [e.name, e]))
  const placed = new Map<string, Placed>()
  const orders = new Map<Workflow, readonly string[]>()
  const arrowIn = (v: Vector): Arrow => ({ name: carries(v) ?? v.name, writes: placed.get(v.name)?.writes ?? [], rests: placed.get(v.name)?.rests ?? [] })
  /** The state a list of entries starts from holds `start` and every given node. */
  const from = (start: readonly string[]) => (n: string): string | undefined => (start.includes(n) || given(n) ? undefined : "")
  const kinds = [["evaluation", "an evaluation"], ["decision", "a decision"]] as const
  // `inner`: the workflow is held by a vector, whose declaration covers the nodes it writes.
  const place = (w: Workflow, inner: boolean): void => {
    for (const v of w.vectors) {
      const where = `vector '${v.name}'`
      const entry = v.function.term === "reference" ? entries.get(v.function.name) : undefined
      if (entry === undefined) {
        reasons.push({ rule: "writes", where, says: "carries out no graph function of the registry by its name, so it writes no node" })
        continue
      }
      const writes = entry.writes.filter((n) => byName.has(n))
      const rests = restsOn(nodes, writes)
      if (v.first === true && writes.length > 0) reasons.push({ rule: "writes", where, says: "is the first vector for a ticket, which writes no node: its asset is the ticket" })
      else if (v.first !== true && writes.length === 0) reasons.push({ rule: "writes", where, says: "writes no node" })
      for (const node of writes.filter(given)) reasons.push({ rule: "writes", where, says: `writes ${node}, which is given` })
      // A vector records its verdict and its answer at each node it writes that declares them (REQ-GRAPH-003).
      for (const [kind, an] of v.first === true ? [] : kinds) {
        const declared = kind === "evaluation" ? v.evaluation !== undefined : v.decision !== undefined
        const at = writes.filter((n) => byName.get(n)?.accepted?.includes(kind) === true)
        if (declared && at.length === 0) reasons.push({ rule: "writes", where, says: `declares ${an}, and no node it writes is accepted by one, so it would be recorded nowhere` })
        if (!declared && !inner && at.length > 0) reasons.push({ rule: "writes", where, says: `writes ${at.join(", ")}, which ${an} accepts, and declares none` })
      }
      const p: Placed = { writes, rests }
      placed.set(v.name, p)
      for (const held of inPlace(v.function, reg)) {
        if (held.term !== "workflow" || held.vectors.length === 0) continue
        place(held, true)
        const { order, left } = ordered(held.vectors, { needs: (x) => placed.get(x.name)?.rests ?? [], produces: (x) => placed.get(x.name)?.writes ?? [] })
        orders.set(held, order.map((x) => x.name))
        const arrows = order.map(arrowIn)
        const exactly = beyond(arrows, writes)
        const off = [
          ...(left.length === 0 ? [] : [`its vectors ${left.map((x) => x.name).join(", ")} rest on what one another write`]),
          ...breaks(arrows, from(rests)),
          ...exactly.missing.map((n) => `no vector of it writes ${n}, which ${v.name} writes`),
          ...exactly.extra.map(([name, n]) => `its vector ${name} writes ${n}, which ${v.name} does not write`)
        ]
        for (const says of off) reasons.push({ rule: "terms", where: `the inner workflow of ${where}`, says })
      }
    }
  }
  place(graph, false)
  const entryArrow = (e: TermEntry): Arrow => arrowIn(e.v)

  // A stretch is written only on an induction entry of a ticket's term (REQ-METHOD-006).
  const terms: readonly (readonly [string, Term])[] = [
    ["the graph", graph],
    ...reg.entries.map((e) => [`registry entry '${e.name}'`, e.definition] as const),
    ...(reg.default === undefined ? [] : [["the registry's default term", reg.default] as const])
  ]
  for (const [where, t] of terms) {
    for (const name of stretched(t)) reasons.push({ rule: "terms", where, says: `the reference to '${name}' names a stretch, which only an induction entry of a ticket's term names` })
  }

  // An entry no vector carries out means its definition: what that denotes composes from what the entry rests on and writes what it writes (T2).
  for (const entry of reg.entries) {
    if (vectors.some((v) => carries(v) === entry.name)) continue
    const where = `registry entry '${entry.name}'`
    const d = denoted(entry.definition, graph, reg)
    if ("why" in d) {
      reasons.push({ rule: "registry", where, says: `no vector carries it out, and its definition denotes nothing: ${d.why}` })
      continue
    }
    if (d.entries.length === 0) {
      reasons.push({ rule: "registry", where, says: `no vector carries it out, and its definition is empty, so it writes none of ${entry.writes.join(", ")}` })
      continue
    }
    const arrows = d.entries.map(entryArrow)
    const exactly = beyond(arrows, entry.writes)
    const off = [
      ...breaks(arrows, from(restsOn(nodes, entry.writes))),
      ...exactly.missing.map((n) => `writes ${n}, which no entry of its definition writes`),
      ...exactly.extra.map(([name, n]) => `its definition's ${name} writes ${n}, which it does not write`)
    ]
    for (const says of off) reasons.push({ rule: "registry", where, says })
  }

  // The default term: the registry's, or every vector of the graph but the first in the order the edges give (C7). It composes from the given nodes.
  const derived = ordered(graph.vectors.filter((v) => v.first !== true), { needs: (x) => placed.get(x.name)?.rests ?? [], produces: (x) => placed.get(x.name)?.writes ?? [] })
  const byDefault = reg.default === undefined ? { entries: derived.order.map((v) => ({ v })) } : denoted(reg.default, graph, reg)
  const whereDefault = reg.default === undefined ? "the vectors of the graph, its default term" : "the registry's default term"
  if ("why" in byDefault) reasons.push({ rule: "terms", where: whereDefault, says: byDefault.why })
  else if (byDefault.entries.some((e) => e.v.first === true)) {
    reasons.push({ rule: "terms", where: whereDefault, says: "names the first vector for a ticket, which a ticket that carries no term does not take" })
  } else {
    const loop = reg.default === undefined && derived.left.length > 0 ? [`the vectors ${derived.left.map((x) => x.name).join(", ")} rest on what one another write`] : []
    for (const says of [...loop, ...breaks(byDefault.entries.map(entryArrow), from([]))]) reasons.push({ rule: "terms", where: whereDefault, says })
  }

  if (reasons.length > 0 || "why" in byDefault) return { no: reasons }
  return { yes: Object.freeze({ graph, registry: reg, byDefault: Object.freeze(byDefault.entries.map((e) => e.v.name)), placed, orders, below: under }) as unknown as WellFormed }
}
