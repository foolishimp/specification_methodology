/**
 * The one runner for the algorithms' cases (REQ-VERIFY-004). Each case file
 * under `cases/` states inputs and the output worked out by hand from the
 * requirement, and names the law or acceptance line it covers. The runner
 * refuses a law or acceptance line of the requirements with no case, named
 * skip or named test elsewhere, runs every case twice (the same inputs give the same output), and
 * checks that no input was changed.
 *
 * @uses C3 C4 C14
 * @is REQ-VERIFY-004
 */
import { readdirSync, readFileSync } from "node:fs"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { describe, expect, it } from "vitest"
import { brief, lines } from "../src/algorithms/brief.js"
import { done } from "../src/algorithms/done.js"
import { declaration, TICKET, type Board, type BranchTicket, type Given, type LogEntry, type Recorded, type Snapshot, type VectorFacts } from "../src/algorithms/facts.js"
import { byPath, identity } from "../src/algorithms/identity.js"
import { next, takesPart } from "../src/algorithms/next.js"
import { changed, open } from "../src/algorithms/open.js"
import { against, asksUser, composes, inducting, passes, recordsOf, since, standingKeys, TERM, unaccepted, type Outcome } from "../src/algorithms/passes.js"
import { progress } from "../src/algorithms/progress.js"
import { logStep, startOfLog, stands, type TicketView } from "../src/algorithms/stands.js"
import { take_up } from "../src/algorithms/take_up.js"
import { trespass, type FrameworkPlaces } from "../src/algorithms/trespass.js"
import { checksOf, placedOf, well_formed, type WellFormed } from "../src/algorithms/well_formed.js"
import type { Node, Vector, Workflow } from "../src/graph/terms.js"
import { inPlace, vectorsOf } from "../src/graph/walk.js"
import { declarationsOf } from "../src/flows/workspace.js"
import { acceptedOn, built, confirmed, inducted } from "./built_workspace.js"

type J = any

const root = join(dirname(fileURLToPath(import.meta.url)), "..")
const text = (...path: string[]): string => readFileSync(join(root, ...path), "utf8")

/** The paths the definition file set-up writes for a new product gives the method's named places (REQ-GRAPH-003). */
export const NEW_PRODUCT: ReadonlyMap<string, readonly string[]> = new Map([
  ["design", ["build_tenants/main/design"]],
  ["code", ["build_tenants/main/code"]],
  ["tests", ["build_tenants/main/tests"]]
])

/** A fixture's graph; with `named`, its places that are names take the paths given (REQ-GRAPH-003). */
function fixture(name: string, named?: Record<string, readonly string[]>): WellFormed {
  const [g, r] = name === "method"
    ? [text("src", "method", "graph.json"), text("src", "method", "registry.json")]
    : [text("tests", "graphs", `${name}.graph.json`), text("tests", "graphs", `${name}.registry.json`)]
  const v = well_formed(g, r, named !== undefined ? new Map(Object.entries(named)) : name === "method" ? NEW_PRODUCT : undefined)
  if (!("yes" in v)) throw new Error(`fixture ${name} is not well formed: ${JSON.stringify(v.no)}`)
  return v.yes
}

function vectorOf(graph: WellFormed, name: string): Vector {
  const v = vectorsOf(graph.graph, graph.registry).find((x) => x.name === name)
  if (v === undefined) throw new Error(`no vector ${name}`)
  return v
}

const given = (j: J): Given | undefined =>
  j === undefined
    ? undefined
    : {
      says: j.says,
      on: new Map(Object.entries(j.on)),
      ...(j.at === undefined ? {} : { at: j.at }),
      // A resolution names the ticket that holds it and the commit it was given on (REQ-ALG-004, REQ-ALG-007).
      ...(j.commit === undefined ? {} : { commit: j.commit }),
      ...(j.ticket === undefined ? {} : { ticket: j.ticket })
    }

const resultOf = (r: J): J => (typeof r === "string" ? { result: r } : r)

function factsOf(j: J): VectorFacts {
  return {
    ...(j.composes === undefined ? {} : { composes: typeof j.composes === "string" ? { result: j.composes } : j.composes }),
    ...(j.found === undefined ? {} : { found: j.found })
  } as VectorFacts
}

function recordedOf(j: J): Recorded {
  const verdict = given(j.verdict)
  const answer = given(j.answer)
  return { ...(verdict === undefined ? {} : { verdict }), ...(answer === undefined ? {} : { answer }) }
}

function snapshotOf(j: J): Snapshot {
  return {
    identities: new Map(Object.entries(j.identities ?? {})),
    ticket: j.ticket === "simplest"
      ? "simplest"
      : {
        path: j.ticket.path,
        identity: j.ticket.identity,
        ...(j.ticket.asked === undefined ? {} : { asked: j.ticket.asked }),
        ...(j.ticket.enters === undefined ? {} : { enters: j.ticket.enters }),
        ...(j.ticket.term === undefined ? {} : { term: j.ticket.term }),
        ...(j.ticket.inducting === undefined ? {} : { inducting: j.ticket.inducting }),
        ...(j.ticket.ruled === true ? { ruled: true as const } : {})
      },
    ...(j.checks === undefined ? {} : { checks: new Map(Object.entries(j.checks).map(([n, r]: [string, J]) => [n, resultOf(r)])) }),
    vectors: new Map(Object.entries(j.vectors ?? {}).map(([n, f]) => [n, factsOf(f)])),
    ...(j.records === undefined ? {} : { records: new Map(Object.entries(j.records).map(([n, r]) => [n, recordedOf(r)])) })
  }
}

const outcomesOf = (results: readonly string[]): Outcome[] =>
  results.map((result, i) => ({ source: "check", name: `check ${i}`, result }) as Outcome)

interface Adapter {
  readonly prepare: (given: J) => J
  readonly call: (inputs: J) => J
  readonly compare: (actual: J, expected: J) => void
}

const equal = (actual: J, expected: J): void => {
  expect(actual).toEqual(expected)
}

const adapters: Record<string, Adapter> = {
  identity: {
    prepare: (g) => ({ asset: { ...g.asset, result: [] } as Node, tree: new Map(Object.entries(g.tree)) }),
    // The identity, and what it gives back for each path of the asset: `byPath` is the inverse of `identity`.
    call: ({ asset, tree }) => {
      const id = identity(asset, tree)
      return { identity: id ?? null, byPath: Object.fromEntries(byPath(asset, id)) }
    },
    compare: equal
  },
  well_formed: {
    prepare: (g) => {
      if (g.fixture !== undefined) {
        const [gp, rp] = g.fixture === "method"
          ? [["src", "method", "graph.json"], ["src", "method", "registry.json"]]
          : [["tests", "graphs", `${g.fixture}.graph.json`], ["tests", "graphs", `${g.fixture}.registry.json`]]
        return { graph: text(...gp), registry: text(...rp) }
      }
      return { graph: g.graphText ?? JSON.stringify(g.graph), registry: JSON.stringify(g.registry) }
    },
    call: ({ graph, registry }) => {
      const v = well_formed(graph, registry)
      return "yes" in v ? { yes: true } : { no: v.no.map(({ rule, where }) => ({ rule, where })), traversable: "yes" in v }
    },
    compare: (actual, expected) => {
      if (expected.yes === true) return equal(actual, expected)
      // A graph that is not well formed gives nothing to traverse (REQ-ALG-002 law 1).
      equal(actual, { ...expected, traversable: false })
    }
  },
  passes: {
    prepare: (g) => {
      const graph = fixture(g.fixture)
      return { graph, vector: vectorOf(graph, g.vector), snapshot: snapshotOf(g.snapshot) }
    },
    call: ({ graph, vector, snapshot }) => passes(graph, vector, snapshot),
    compare: (actual, expected) => {
      expect(actual.result).toBe(expected.result)
      expect(actual.outcomes).toHaveLength(expected.outcomes.length)
      expected.outcomes.forEach((o: J, i: number) => expect(actual.outcomes[i]).toMatchObject(o))
    }
  },
  open: {
    prepare: (g) => {
      const graph = fixture(g.fixture)
      return { graph, vector: vectorOf(graph, g.vector), snapshot: snapshotOf(g.snapshot) }
    },
    call: ({ graph, vector, snapshot }) => ({ open: open(graph, vector, snapshot), changed: changed(graph, vector, snapshot) }),
    compare: equal
  },
  next: {
    prepare: (g) => {
      const graph = fixture(g.fixture)
      const within = g.within === undefined ? graph.graph : (inPlace(vectorOf(graph, g.within).function, graph.registry).find((t) => t.term === "workflow") as Workflow)
      return { graph, within, snapshot: snapshotOf(g.snapshot) }
    },
    call: ({ graph, within, snapshot }) => next(graph, snapshot, within)?.name ?? null,
    compare: equal
  },
  done: {
    prepare: (g) => ({ graph: fixture(g.fixture), snapshot: snapshotOf(g.snapshot) }),
    call: ({ graph, snapshot }) => {
      const d = done(graph, snapshot)
      return d.done === "yes" ? d : { done: "no", saysNo: d.saysNo.map((s) => ({ vector: s.vector, outcomes: s.outcomes.map((o) => o.name) })) }
    },
    compare: equal
  },
  brief: {
    prepare: (g) => {
      const graph = fixture(g.fixture, g.named)
      return { graph, vector: vectorOf(graph, g.vector), kind: g.kind, snapshot: snapshotOf(g.snapshot), basis: g.basis }
    },
    call: ({ graph, vector, kind, snapshot, basis }) => {
      const b = brief(graph, vector, kind, snapshot, basis)
      return { brief: b, lines: lines(b) }
    },
    compare: (actual, expected) => {
      if (expected.brief !== undefined) equal(actual.brief, expected.brief)
      if (expected.lines !== undefined) equal(actual.lines, expected.lines)
    }
  },
  trespass: {
    prepare: (g) => {
      const graph = fixture(g.fixture)
      return {
        graph,
        vector: vectorOf(graph, g.vector),
        kind: g.kind,
        places: g.places as FrameworkPlaces,
        ...(g.ticket === undefined ? {} : { ticket: g.ticket }),
        ...(g.side === undefined ? {} : { side: g.side }),
        start: new Map(Object.entries(g.start)),
        end: new Map(Object.entries(g.end))
      }
    },
    call: (inputs) => trespass(inputs),
    compare: equal
  },
  progress: {
    prepare: (g) => ({ before: g.before === null ? undefined : outcomesOf(g.before), now: outcomesOf(g.now) }),
    call: ({ before, now }) => progress(before, now),
    compare: equal
  },
  take_up: {
    prepare: (g) => ({
      board: g.board as Board,
      held: g.held,
      ...(g.named === undefined ? {} : { named: g.named }),
      graph: fixture(g.fixture),
      mainDone: g.mainDone,
      limit: g.limit
    }),
    call: (inputs) => take_up(inputs),
    compare: equal
  },
  stands: {
    prepare: (g) => {
      const views = new Map<string, TicketView>(
        Object.entries(g.views).map(([name, v]: [string, J]) => [
          name,
          // What the ticket shows, read from it alone (REQ-ALG-012).
          { changes: v.changes ?? [], ...(v.ticket === undefined ? {} : { ticket: v.ticket }) }
        ])
      )
      // The one pass over the log is the event log's reader (C10); here the runner makes it.
      const log = g.log === null ? undefined : (g.log as LogEntry[]).reduce(logStep, startOfLog())
      const found = g.found as string | undefined
      return {
        graph: fixture(g.fixture),
        board: g.board as Board,
        branches: g.branches,
        views,
        ...(log === undefined ? {} : { log }),
        ...(found === undefined ? {} : { foundOf: (vector: string) => found.replace("{vector}", vector) })
      }
    },
    call: (inputs) => stands(inputs),
    compare: equal
  }
}

/** A plain form of any input or output, to tell whether it changed. */
const plain = (value: unknown): string =>
  JSON.stringify(value, (_key, v: unknown) => (v instanceof Map ? [...v.entries()] : v))

const caseFiles = readdirSync(join(root, "tests", "cases")).filter((f) => f.endsWith(".json")).sort()
const files = caseFiles.map((f) => ({ file: f, data: JSON.parse(text("tests", "cases", f)) as J }))

for (const { file, data } of files) {
  describe(`${data.algorithm} (${data.requirement})`, () => {
    const adapter = adapters[data.algorithm]
    it("has a runner", () => {
      expect(adapter, file).toBeDefined()
    })
    if (adapter === undefined) return
    for (const c of data.cases as J[]) {
      it(`${c.says} [${c.covers.join("; ")}]`, () => {
        const inputs = adapter.prepare({ ...data.shared, ...c.given })
        const before = plain(inputs)
        const first = adapter.call(inputs)
        const second = adapter.call(inputs)
        expect(plain(second)).toBe(plain(first))
        expect(plain(inputs)).toBe(before)
        adapter.compare(JSON.parse(plain(first)), c.expect)
      })
    }
    for (const s of (data.skips ?? []) as J[]) it.skip(`${s.covers.join("; ")}: ${s.why}`, () => {})
    // A line shown by a test elsewhere: that test names each line it covers.
    for (const e of (data.elsewhere ?? []) as J[]) {
      it(`${e.covers.join("; ")}: ${e.says} (${e.in})`, () => {
        for (const tag of e.covers as string[]) expect(text("tests", e.in), `${e.in} names no test of ${tag}`).toContain(tag)
      })
    }
  })
}

describe("REQ-METHOD-006 the ticket's term is well formed, as the first vector's own check (CALCULUS.md T3)", () => {
  const method = fixture("method")
  const seq = (...names: readonly string[]): string => JSON.stringify({ term: "sequence", terms: names.map((name) => ({ term: "reference", name })) })
  const on = (term: string | undefined, enters = "intent", ends = "code"): ReadonlyMap<string, string> =>
    new Map([...(term === undefined ? [] : [["term", term] as const]), ["enters", enters], ["ends", ends]])
  const ticket = (enters: string): BranchTicket => ({ path: "tickets/active/261121-a.md", identity: "t1", asked: "a1", enters })
  /** A workspace with nothing in it. */
  const empty = (enters = "intent"): Snapshot => ({ identities: new Map(), ticket: ticket(enters), vectors: new Map() })
  /** A workspace built and accepted, then changed as given. */
  const whole = (enters: string, changes: Readonly<Record<string, string | null>> = {}): Snapshot => built(method, ticket(enters), changes)
  const no = (found: string) => ({ result: "no", found })
  const found = (...each: readonly string[]) => no(each.join("; "))
  const covers = (span: string, ...nodes: readonly string[]): readonly string[] => nodes.map((n) => `no entry of the term writes ${n}, which the work from ${span} covers`)
  const needs = (entry: string, node: string, why?: string): string => `${entry} rests on ${node}, which is neither accepted nor written before it${why === undefined ? "" : `: ${why}`}`

  it("the specification and then the build, on an empty workspace: yes", () => {
    expect(composes(method, on(seq("write-specification", "write-build")), empty())).toEqual({ result: "yes" })
  })
  it("the six single-asset functions, each after those that write what it rests on, on an empty workspace: yes, the tests before the design or after it", () => {
    expect(composes(method, on(seq("write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code")), empty())).toEqual({ result: "yes" })
    expect(composes(method, on(seq("write-intent", "write-product", "write-requirements", "write-tests", "write-design", "write-code")), empty())).toEqual({ result: "yes" })
  })
  it("the code alone on a built product, entering and ending at the code; one reference, not in a sequence: yes", () => {
    expect(composes(method, on('{"term": "reference", "name": "write-code"}', "code"), whole("code"))).toEqual({ result: "yes" })
  })
  it("the specification alone, ending at the requirements: yes", () => {
    expect(composes(method, on(seq("write-specification"), "intent", "requirements"), empty())).toEqual({ result: "yes" })
  })
  it("fine and coarse entries mixed: the requirements and then the build, on a built product, entering at the requirements: yes", () => {
    expect(composes(method, on(seq("write-requirements", "write-build"), "requirements"), whole("requirements"))).toEqual({ result: "yes" })
  })
  it("D161: from the design to the code on a built product, the design and then the code: yes, and the tests stand as they are; the build alone, or the tests between, write the tests, which lie outside that work: no", () => {
    expect(composes(method, on(seq("write-design", "write-code"), "design"), whole("design"))).toEqual({ result: "yes" })
    expect(composes(method, on(seq("write-build"), "design"), whole("design"))).toEqual(no("write-build writes tests, which lies outside the work from design to code"))
    expect(composes(method, on(seq("write-design", "write-tests", "write-code"), "design"), whole("design"))).toEqual(no("write-tests writes tests, which lies outside the work from design to code"))
  })
  it("the specification and then the design, from the intent to the design: yes, each node once", () => {
    expect(composes(method, on(seq("write-specification", "write-design"), "intent", "design"), empty())).toEqual({ result: "yes" })
  })

  // Every finding names an entry or the work, and a node: one an entry rests on that is neither accepted nor written before it, one written twice, one of the work no entry writes, or one outside the work (T3).
  // A node is accepted only where every node it depends on is (REQ-ALG-004): once the ticket reopens the requirements, the design and the tests no longer hold either.
  it("a term that does not write the work: the requirements and then the code; the intent and then the design; the requirements, the design and the code", () => {
    const reopened = "the user has not accepted requirements as it now stands; enter at requirements"
    expect(composes(method, on(seq("write-requirements", "write-code"), "requirements"), whole("requirements"))).toEqual(found(
      needs("write-code", "design", reopened), needs("write-code", "tests", reopened), ...covers("requirements to code", "design", "tests")
    ))
    expect(composes(method, on(seq("write-intent", "write-design"), "intent", "design"), whole("intent"))).toEqual(found(
      needs("write-design", "requirements", "the user has not accepted intent as it now stands; enter at intent"), ...covers("intent to design", "product", "requirements")
    ))
    expect(composes(method, on(seq("write-requirements", "write-design", "write-code"), "requirements"), whole("requirements"))).toEqual(found(needs("write-code", "tests", reopened), ...covers("requirements to code", "tests")))
  })
  it("a term against the edges does not compose: the code before the tests, the build before the specification, the code before the five it rests on", () => {
    expect(composes(method, on(seq("write-code", "write-tests"), "tests"), whole("tests"))).toEqual(no(needs("write-code", "tests")))
    expect(composes(method, on(seq("write-build", "write-specification")), empty())).toEqual(no(needs("write-build", "requirements")))
    expect(composes(method, on(seq("write-code", "write-intent", "write-product", "write-requirements", "write-design", "write-tests")), whole("intent"))).toEqual(found(needs("write-code", "requirements"), needs("write-code", "design"), needs("write-code", "tests")))
  })
  it("enters and ends are held to the whole term: a work that ends at a node that does not depend on where it enters, and a term that writes past where the work ends", () => {
    expect(composes(method, on(seq("write-code", "write-requirements"), "code", "requirements"), whole("code"))).toEqual(found("the work ends at requirements, which neither is code nor depends on it", needs("write-code", "requirements")))
    expect(composes(method, on(seq("write-code", "write-intent"), "code", "intent"), whole("code"))).toEqual(no("the work ends at intent, which neither is code nor depends on it"))
    expect(composes(method, on(seq("write-specification", "write-build"), "intent", "design"), empty())).toEqual(found("write-build writes tests, which lies outside the work from intent to design", "write-build writes code, which lies outside the work from intent to design"))
    expect(composes(method, on(seq("write-build"), "tests"), whole("tests", { tests: null, code: null }))).toEqual(no("write-build writes design, which lies outside the work from tests to code"))
  })
  it("no clipping: the specification ending at the product definition, and a term that stops short of where the work ends", () => {
    expect(composes(method, on(seq("write-specification"), "intent", "product"), empty())).toEqual(no("write-specification writes requirements, which lies outside the work from intent to product"))
    expect(composes(method, on(seq("write-specification")), empty())).toEqual(found(...covers("intent to code", "design", "tests", "code")))
  })
  it("a node written twice does not compose: no", () => {
    expect(composes(method, on(seq("write-intent", "write-intent", "write-product"), "intent", "product"), empty())).toEqual(no("write-intent writes intent, which an entry before it writes"))
  })
  it("a term that does not write the node the ticket enters at: no", () => {
    expect(composes(method, on(seq("write-code"), "requirements"), whole("requirements"))).toEqual(found(
      ...["requirements", "design", "tests"].map((n) => needs("write-code", n, "the user has not accepted requirements as it now stands; enter at requirements")),
      ...covers("requirements to code", "requirements", "design", "tests")
    ))
  })
  it("a ticket entering at a node the graph does not have: no", () => {
    expect(composes(method, on(seq("write-specification", "write-build"), "specification"), empty()).found).toBe("no node of the graph is specification")
  })

  it("rule (b): the design is not written before the requirements are accepted; a finding names the node to enter at", () => {
    const term = on(seq("write-design", "write-code"), "design")
    const reopened = "the user has not accepted requirements as it now stands; enter at requirements"
    // The tests rest on the requirements too, so they no longer stand either.
    expect(composes(method, term, whole("design", { requirements: "requirements-2" }))).toEqual(found(needs("write-design", "requirements", reopened), needs("write-code", "tests", reopened)))
    expect(composes(method, on(seq("write-build"), "design"), whole("design", { requirements: "requirements-2" }))).toEqual(found(needs("write-build", "requirements", reopened), "write-build writes tests, which lies outside the work from design to code"))
    expect(composes(method, on(seq("write-design"), "design", "design"), empty("design"))).toEqual(no(needs("write-design", "requirements", "intent is not in the workspace; enter at intent")))
    expect(composes(method, term, whole("design"))).toEqual({ result: "yes" })
  })
  it("rule (b): presence is not enough; the code alone rests on tests whose verdict stands, and the first node, through what each depends on, that is not accepted is where to enter", () => {
    expect(composes(method, on(seq("write-code"), "code"), whole("code", { tests: "tests-2" }))).toEqual(no(needs("write-code", "tests", "no verdict of yes stands for tests as it now is; enter at tests")))
    const reopened = "the user has not accepted requirements as it now stands; enter at requirements"
    expect(composes(method, on(seq("write-code"), "code"), whole("code", { requirements: "requirements-2", tests: "tests-2" }))).toEqual(found(
      needs("write-code", "requirements", reopened), needs("write-code", "design", reopened), needs("write-code", "tests", reopened)
    ))
  })
  // The node to enter at is the nearest on which both the node not accepted and the work depend, so the ticket's work can reach both (R3).
  it("rule (b) holds every node the work rests on: the tests and then the code, the design changed after its acceptance; the design and then the code, the tests changed; each is entered at the requirements", () => {
    const term = on(seq("write-tests", "write-code"), "tests")
    expect(composes(method, term, whole("tests", { design: "design-2" }))).toEqual(no(needs("write-code", "design", "no verdict of yes stands for design as it now is; enter at requirements")))
    expect(composes(method, on(seq("write-design", "write-code"), "design"), whole("design", { tests: "tests-2" }))).toEqual(no(needs("write-code", "tests", "no verdict of yes stands for tests as it now is; enter at requirements")))
  })
  it("R3: on a design ticket whose tests the user edited by hand, only a term from the requirements, which reaches both the tests and the design, composes", () => {
    const edited = (enters: string): Snapshot => whole(enters, { tests: "tests-2" })
    expect(composes(method, on(seq("write-design", "write-code"), "design"), edited("design"))).toEqual(no(needs("write-code", "tests", "no verdict of yes stands for tests as it now is; enter at requirements")))
    expect(composes(method, on(seq("write-design", "write-tests", "write-code"), "design"), edited("design"))).toEqual(no("write-tests writes tests, which lies outside the work from design to code"))
    expect(composes(method, on(seq("write-tests", "write-design", "write-code"), "tests"), edited("tests"))).toEqual(no("write-design writes design, which lies outside the work from tests to code"))
    expect(composes(method, on(seq("write-requirements", "write-design", "write-tests", "write-code"), "requirements"), edited("requirements"))).toEqual({ result: "yes" })
  })
  it("R3: where a node of the specification is edited by hand and only the specification writes it, the work is entered where that graph function writes", () => {
    // The method's graph with the specification, the requirements and the build: no graph function writes the product definition alone.
    const graph = JSON.parse(text("src", "method", "graph.json")) as { vectors: { name: string }[] }
    const registry = JSON.parse(text("src", "method", "registry.json")) as { entries: { name: string }[] }
    const keep = ["induct-ticket", "write-specification", "write-requirements", "write-build"]
    const v = well_formed(
      JSON.stringify({ ...graph, vectors: graph.vectors.filter((x) => keep.includes(x.name)) }),
      JSON.stringify({ ...registry, entries: registry.entries.filter((e) => keep.includes(e.name)), default: JSON.parse(seq("write-specification", "write-build")) })
    )
    if (!("yes" in v)) throw new Error(JSON.stringify(v.no))
    const product = built(v.yes, ticket("requirements"), { product: "product-2" }, ["write-specification", "write-build"])
    const reopened = needs("write-requirements", "product", "the user has not accepted product as it now stands; enter at intent")
    expect(composes(v.yes, on(seq("write-requirements"), "requirements", "requirements"), product)).toEqual(no(reopened))
    expect(composes(v.yes, on(seq("write-requirements", "write-build"), "requirements"), product)).toEqual(no(reopened))
  })
  it("R3: where no graph function a ticket may begin with writes a node on which both the node not accepted and the work depend, a run with no ticket accepts that node first", () => {
    const small = fixture("small")
    // The draft is written by a vector with no evaluation and no decision, and the brief is given: no ticket enters at either.
    const s: Snapshot = { identities: new Map([["brief", "b1"]]), ticket: ticket("final"), vectors: new Map() }
    expect(composes(small, on(seq("finish"), "final", "final"), s)).toEqual(found(
      "finish rests on draft, which is neither accepted nor written before it: draft is not in the workspace; no ticket enters where both draft and this work are reached, so a run with no ticket accepts draft first",
      "finish writes notes, which lies outside the work from final to final"
    ))
  })
  it("rule (b) holds every entry: the same term, the design standing: yes", () => {
    expect(composes(method, on(seq("write-tests", "write-code"), "tests"), whole("tests"))).toEqual({ result: "yes" })
  })

  it("a name the registry does not list, a session of its own and a term that does not read: no", () => {
    expect(composes(method, on(seq("write-everything")), empty())).toEqual(no("write-everything is not in the registry"))
    expect(composes(method, on('{"term": "session"}'), empty())).toEqual(no("the term holds a session that no vector of the graph carries out"))
    expect(composes(method, on("write-specification, write-build"), empty()).found).toMatch(/^the ticket's term does not read: /)
    expect(composes(method, on(undefined), empty())).toEqual(no("the ticket gives no term"))
  })

  // A term with induction entries: each names its stretch, and writes the work of it (REQ-METHOD-006; CALCULUS.md T3, T5).
  const induct = (enters: string, ends: string) => ({ term: "reference", name: "induct-ticket", enters, ends })
  const of = (...entries: readonly (string | object)[]): string =>
    JSON.stringify({ term: "sequence", terms: entries.map((e) => (typeof e === "string" ? { term: "reference", name: e } : e)) })
  const TWO = ["write-intent", "write-product"] as const
  const FOUR = ["write-intent", "write-product", "write-requirements"] as const
  /** The induction confirmed on the ticket whose identity is given, its checks passing. */
  const confirmedOn = (s: Snapshot, identity: string): Snapshot => confirmed(method, s, identity)
  /** Built up to the product definition, which the user accepted after the ticket was inducted; no requirements, design, tests or code. */
  const toProduct = (identity = "t1"): Snapshot =>
    confirmedOn(acceptedOn(method, built(method, ticket("intent"), { requirements: null, design: null, tests: null, code: null })), identity)
  /** The ticket as the user confirmed it, with the outer term, where the session bound to its stretch has changed it since: its text without its term is the one the acceptances at the entry stand on. */
  const was = (fields: ReadonlyMap<string, string>) => ({ fields, asked: "a1" })
  const outer = was(on(of(...TWO, induct("requirements", "code"))))

  it("an induction entry writes the work of its stretch and rests on what that depends on: the intent and the product and then the stretch from the requirements; the requirements and the tests and then the stretch from the design to the code: yes", () => {
    expect(composes(method, on(of(...TWO, induct("requirements", "code"))), empty())).toEqual({ result: "yes" })
    expect(composes(method, on(of(...FOUR, "write-tests", induct("design", "code"))), empty())).toEqual({ result: "yes" })
    expect(composes(method, on(of("write-specification", "write-tests", induct("design", "code"))), empty())).toEqual({ result: "yes" })
  })
  it("an induction entry is held to the law as any entry: a gap, a node twice, a stretch past where the work ends, and one that leaves out a node the work covers", () => {
    expect(composes(method, on(of("write-intent", induct("requirements", "code"))), empty())).toEqual(found(needs("induct-ticket", "product", "product is not in the workspace; enter at intent"), ...covers("intent to code", "product")))
    expect(composes(method, on(of(...FOUR, induct("requirements", "code"))), empty())).toEqual(no("induct-ticket writes requirements, which an entry before it writes"))
    expect(composes(method, on(of(...TWO, induct("requirements", "code")), "intent", "requirements"), empty())).toEqual(found(...["design", "tests", "code"].map((n) => `induct-ticket writes ${n}, which lies outside the work from intent to requirements`)))
    // The work from the design to the code holds no tests: after the requirements, a stretch from the design needs the tests before it.
    expect(composes(method, on(of(...FOUR, induct("design", "code"))), empty())).toEqual(found(needs("induct-ticket", "tests", "tests is not in the workspace; enter at intent"), ...covers("intent to code", "tests")))
  })
  it("acceptance 13: the induction without a stretch, a stretch on another entry, a stretch over the whole work and one that is no stretch of the graph: no", () => {
    expect(composes(method, on(seq("induct-ticket", "write-specification", "write-build")), empty()).found).toMatch(
      /^the term names induct-ticket, the graph function of the first vector for a ticket, with no stretch: an induction entry names the node it enters at and the node it ends at/
    )
    expect(composes(method, on(of("write-specification", { term: "reference", name: "write-build", enters: "design", ends: "code" })), empty())).toEqual(no("write-build names a stretch, and only an induction entry names one"))
    expect(composes(method, on(of(induct("intent", "code"))), empty()).found).toMatch(/^the induction entry over intent to code is the whole of the work from intent to code; a term for it is chosen now/)
    expect(composes(method, on(of("write-specification", induct("code", "design"))), empty()).found).toMatch(/^the induction entry over code to design names no stretch of the graph: design neither is code nor depends on it/)
    expect(composes(method, on(of(induct("specification", "code")), "intent", "code"), empty()).found).toMatch(/^the induction entry over specification to code names no stretch of the graph: /)
  })
  it("reached: the confirmation stands and every entry before the induction entry passes; the term then says no, so the induction runs again, bound to the stretch", () => {
    const term = on(of(...TWO, induct("requirements", "code")))
    const reached = toProduct()
    expect(composes(method, term, reached)).toEqual(no("the run has reached the induction entry over requirements to code: a term for that stretch is to take its place"))
    expect(inducting(method, term, reached)).toEqual({ enters: "requirements", ends: "code" })
    // Not reached: the product definition is not accepted as it now stands, or the induction is not confirmed yet.
    const short = acceptedOn(method, built(method, ticket("intent"), { product: "product-2", requirements: null, design: null, tests: null, code: null }))
    expect(composes(method, term, confirmedOn(short, "t1"))).toEqual({ result: "yes" })
    expect(inducting(method, term, confirmedOn(short, "t1"))).toBeUndefined()
    expect(composes(method, term, acceptedOn(method, built(method, ticket("intent"), { requirements: null, design: null, tests: null, code: null })))).toEqual({ result: "yes" })
  })
  it("R2: an induction entry is never the term's first entry, on the whole work or on a stretch: no, with the finding", () => {
    const begins = "the term begins with the induction entry over intent to product: an induction entry fits only a later stretch, once the entries before it are accepted"
    expect(composes(method, on(of(induct("intent", "product"), "write-requirements"), "intent", "requirements"), empty())).toEqual(no(begins))
    expect(composes(method, on(of(induct("intent", "product"), "write-requirements"), "intent", "requirements"), confirmedOn(empty(), "t1"))).toEqual(no(begins))
    expect(composes(method, on(of(induct("intent", "code"))), empty()).found).toContain("the term begins with the induction entry over intent to code")
    // In an entry's place too: the term put there starts no stretch of its own.
    expect(composes(method, on(of(...TWO, induct("requirements", "tests"), "write-design", "write-code")), toProduct("t0"), outer)).toEqual(no("the term begins with the induction entry over requirements to tests: an induction entry fits only a later stretch, once the entries before it are accepted"))
  })
  it("substitution: the confirmed term with exactly the entry replaced, by a term that obeys the law on its stretch: yes; the whole term then obeys it (T5)", () => {
    const changed = toProduct("t0")
    for (const inner of [["write-requirements", "write-build"], ["write-requirements", "write-design", "write-tests", "write-code"], ["write-requirements", "write-tests", "write-design", "write-code"]]) {
      expect(composes(method, on(of(...TWO, ...inner)), changed, outer), inner.join(" ")).toEqual({ result: "yes" })
      expect(composes(method, on(of(...TWO, ...inner)), empty()), inner.join(" ")).toEqual({ result: "yes" })
    }
    expect(inducting(method, on(of(...TWO, "write-requirements", "write-build")), changed, outer)).toEqual({ enters: "requirements", ends: "code" })
  })
  it("substitution: a term in the entry's place that breaks the law on the stretch is a no, with its finding", () => {
    expect(composes(method, on(of(...TWO, "write-requirements", "write-design", "write-code")), toProduct("t0"), outer)).toEqual(found(needs("write-code", "tests", "tests is not in the workspace; enter at requirements"), ...covers("requirements to code", "tests")))
    expect(composes(method, on(of(...TWO, "write-code", "write-requirements", "write-design", "write-tests")), toProduct("t0"), outer).found).toMatch(/^write-code rests on requirements, which is neither accepted nor written before it/)
  })
  it("substitution: a new term that changes anything else of the confirmed term is refused, naming the ticket the user confirmed by the commit that holds it (R3)", () => {
    const refused = no("the term is not the one the user confirmed with the induction entry over requirements to code alone replaced; the ticket the user confirmed is held by the commit t0 in git")
    expect(composes(method, on(of("write-specification", "write-build")), toProduct("t0"), outer)).toEqual(refused)
    expect(composes(method, on(of("write-intent", "write-requirements", "write-build")), toProduct("t0"), outer)).toEqual(refused)
  })
  it("R1, E6: the session bound to the stretch changes a line other than the term: a no for that session, with the finding, also where its term is a lawful substitution", () => {
    const confirmed = was(new Map([...on(of(...TWO, induct("requirements", "code"))), ["kind", "feature"]]))
    const moved = toProduct("t0")
    const now: Snapshot = moved.ticket === "simplest" ? moved : { ...moved, ticket: { ...moved.ticket, asked: "a2" } }
    const line = "a line of the ticket other than its term is not as the user confirmed it, and the session writes only the term in the entry's place; the ticket the user confirmed is held by the commit t0 in git"
    // The changed line also reopens the entry at the intent (D141), so a node the stretch rests on no longer stands; the stretch stays under way.
    const lawful = new Map([...on(of(...TWO, "write-requirements", "write-build")), ["kind", "fault"]])
    const kind = composes(method, lawful, now, confirmed)
    expect(kind.result).toBe("no")
    expect(kind.found?.endsWith(line)).toBe(true)
    expect(inducting(method, lawful, now, confirmed)).toEqual({ enters: "requirements", ends: "code" })
    // E6: the kind changed and a whole new term written: both are found, and the stretch is still the one under way.
    const e6 = new Map([...on(of("write-specification", "write-build")), ["kind", "fault"]])
    expect(composes(method, e6, now, confirmed)).toEqual(no(`the term is not the one the user confirmed with the induction entry over requirements to code alone replaced; the ticket the user confirmed is held by the commit t0 in git; ${line}`))
    expect(inducting(method, e6, now, confirmed)).toEqual({ enters: "requirements", ends: "code" })
    // The user is not asked: the term's check says no.
    const v = vectorOf(method, "induct-ticket")
    const at: Snapshot = { ...now, vectors: new Map([...now.vectors].map(([n, f]) => [n, n === v.name ? { ...f, composes: composes(method, e6, now, confirmed) } : f])) }
    expect(asksUser(method, v, at)).toBe(false)
  })
  it("R1, E3b: a change no session bound to a stretch made is the user's: the whole ticket is held to the law, bound to no stretch, and the user is asked, with no session where its term holds", () => {
    const moved = toProduct("t0")
    const v = vectorOf(method, "induct-ticket")
    const judged = (fields: ReadonlyMap<string, string>): Snapshot => ({ ...moved, vectors: new Map([...moved.vectors].map(([n, f]) => [n, n === v.name ? { ...f, composes: composes(method, fields, moved) } : f])) })
    // The user's term changes the entries before the stretch: it is held as the whole ticket's, which it is, and no stretch is under way.
    const users = on(of("write-specification", "write-build"))
    expect(composes(method, users, moved)).toEqual({ result: "yes" })
    expect(inducting(method, users, moved)).toBeUndefined()
    expect(asksUser(method, v, judged(users))).toBe(true)
    // A user's term that does not hold is a no on the whole work, so the induction runs again, bound to no stretch.
    expect(composes(method, on(of("write-intent", "write-code")), moved).found).toMatch(/^write-code rests on requirements, which is neither accepted nor written before it/)
    expect(inducting(method, on(of("write-intent", "write-code")), moved)).toBeUndefined()
  })
  it("substitution: an induction entry in the entry's place only over a stretch strictly smaller than the one it fills", () => {
    expect(composes(method, on(of(...TWO, induct("requirements", "code"))), toProduct("t0"), outer).found).toMatch(/^the induction entry over requirements to code is the whole of the work from requirements to code; a term for it is chosen now/)
    expect(composes(method, on(of(...TWO, induct("product", "code"))), toProduct("t0"), outer).result).toBe("no")
    expect(composes(method, on(of(...TWO, "write-requirements", "write-tests", induct("design", "code"))), toProduct("t0"), outer)).toEqual({ result: "yes" })
  })
  it("a ticket enters only by a vector that declares an evaluation or a decision (REQ-FLOW-004)", () => {
    const bare = { ...vectorOf(method, "write-code"), evaluation: undefined, decision: undefined } as unknown as Vector
    const graph = { ...method, graph: { ...method.graph, vectors: method.graph.vectors.map((v) => (v.name === "write-code" ? bare : v)) } } as unknown as WellFormed
    expect(composes(graph, on(seq("write-code"), "code"), whole("code"))).toEqual(no("write-code, by which the ticket enters, declares neither an evaluation nor a decision"))
  })
  it("the induction does not pass while its term does not compose, though every declared check and the answer do", () => {
    const v = vectorOf(method, "induct-ticket")
    const facts: VectorFacts = { composes: composes(method, on(seq("write-everything")), empty()) }
    const got = passes(method, v, {
      identities: new Map(),
      ticket: { path: "tickets/active/261121-a.md", identity: "t1", enters: "intent" },
      checks: new Map(checksOf(method, v).map((c) => [c.name, { result: "yes" }])),
      vectors: new Map([["induct-ticket", facts]]),
      records: new Map([["induct-ticket", { answer: { says: "yes", on: new Map([["the ticket", "t1"]]) } }]])
    })
    expect(got.result).toBe("no")
    expect(got.outcomes.filter((o) => o.result !== "yes")).toEqual([{ source: "check", name: TERM, result: "no", found: "write-everything is not in the registry" }])
  })

  it("on a term of the design whose requirements changed after they were accepted, the induction is next and the design never is", () => {
    const term = ["write-design", "write-code"]
    expect(next(method, inducted(method, whole("design", { requirements: "requirements-2" }), term, "design", "code"))?.name).toBe("induct-ticket")
    expect(next(method, inducted(method, whole("design"), term, "design", "code"))?.name).toBe("write-design")
    // The simplest ticket on the same workspace asks for the requirements again before anything below them.
    expect(next(method, built(method, "simplest", { requirements: "requirements-2" }))?.name).toBe("write-requirements")
  })
  it("the default is the registry's data: declared as the specification and the build, the simplest ticket and a ticket with no term are built by those two", () => {
    const registry = JSON.parse(text("src", "method", "registry.json")) as Record<string, unknown>
    const coarse = { term: "sequence", terms: [{ term: "reference", name: "write-specification" }, { term: "reference", name: "write-build" }] }
    const v = well_formed(text("src", "method", "graph.json"), JSON.stringify({ ...registry, default: coarse }), NEW_PRODUCT)
    if (!("yes" in v)) throw new Error(JSON.stringify(v.no))
    const graph = v.yes
    expect(graph.byDefault).toEqual(["write-specification", "write-build"])
    for (const t of ["simplest", ticket("intent")] as const) {
      const s: Snapshot = { identities: new Map(), ticket: t, vectors: new Map() }
      expect(takesPart(graph, vectorOf(graph, "write-specification"), s)).toBe(true)
      expect(takesPart(graph, vectorOf(graph, "write-build"), s)).toBe(true)
      expect(takesPart(graph, vectorOf(graph, "write-intent"), s)).toBe(false)
    }
    expect(next(graph, { identities: new Map(), ticket: "simplest", vectors: new Map() })?.name).toBe("write-specification")
  })
  it("the simplest ticket, main and a ticket with no readable term take part by the one default term, read as an inducted ticket's is", () => {
    const noTerm = { identities: new Map(), ticket: ticket("intent"), vectors: new Map() } satisfies Snapshot
    const simplest = { identities: new Map(), ticket: "simplest", vectors: new Map() } satisfies Snapshot
    const named = { identities: new Map(), ticket: { ...ticket("intent"), term: method.byDefault }, vectors: new Map() } satisfies Snapshot
    expect(method.byDefault).toEqual(["write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"])
    for (const v of method.graph.vectors.filter((x) => x.first !== true)) {
      expect(takesPart(method, v, noTerm), v.name).toBe(method.byDefault.includes(v.name))
      expect(takesPart(method, v, simplest), v.name).toBe(takesPart(method, v, named))
    }
  })
})

describe("acceptance stands on what it means and on what it judges against (D168, D169; the review of 21 November)", () => {
  type Kind = "evaluation" | "decision"
  const node = (name: string, depends: readonly string[] = [], accepted: readonly Kind[] = ["decision"]): Node =>
    ({ name, place: `${name}.md`, result: [`${name} is as asked.`], ...(depends.length === 0 ? {} : { depends }), ...(accepted.length === 0 ? {} : { accepted }) })
  const given = (name: string): Node => ({ name, place: `${name}.md`, result: [`${name} is given.`], given: true })
  /** The graph of the nodes given, each written by a vector of its own that declares what its node's acceptance asks for, with its registry. */
  const example = (nodes: readonly Node[]): WellFormed => {
    const written = nodes.filter((n) => n.given !== true)
    const vectors = written.map((n) => ({
      name: `write-${n.name}`,
      ...((n.accepted ?? []).includes("evaluation") ? { evaluation: { findings: `reviews/${n.name}/findings.md`, verdict: `reviews/${n.name}/verdict.json` } } : {}),
      ...((n.accepted ?? []).includes("decision") ? { decision: {} } : {}),
      function: { term: "reference", name: `write-${n.name}` }
    }))
    const registry = { entries: written.map((n) => ({ name: `write-${n.name}`, writes: [n.name], purpose: `Writes ${n.name}.`, definition: { term: "session" } })) }
    const v = well_formed(JSON.stringify({ term: "workflow", nodes, vectors }), JSON.stringify(registry))
    if (!("yes" in v)) throw new Error(JSON.stringify(v.no))
    return v.yes
  }
  const results = (g: WellFormed, s: Snapshot): readonly string[] => g.graph.vectors.map((v) => passes(g, v, s).result)

  it("the review's chain A to B to C to D, each accepted by the user: with A changed and B, C and D as they were, no node past A is accepted, and a ticket whose term is write-D alone does not compose, naming A; with A as it was, it composes", () => {
    const graph = example([node("A"), node("B", ["A"]), node("C", ["B"]), node("D", ["C"])])
    const ticket: BranchTicket = { path: "tickets/active/261122-d.md", identity: "t1", asked: "a1", enters: "D" }
    const fields = new Map([["term", JSON.stringify({ term: "reference", name: "write-D" })], ["enters", "D"], ["ends", "D"]])
    const asWas = acceptedOn(graph, built(graph, ticket))
    expect(results(graph, asWas)).toEqual(["yes", "yes", "yes", "yes"])
    expect(composes(graph, fields, asWas)).toEqual({ result: "yes" })
    const changed = acceptedOn(graph, built(graph, ticket, { A: "A-2" }))
    expect(results(graph, changed)).toEqual(["no", "no", "no", "no"])
    expect(composes(graph, fields, changed)).toEqual({ result: "no", found: "write-D rests on C, which is neither accepted nor written before it: the user has not accepted A as it now stands; enter at A" })
  })

  it("D168: a record at a node stands on what the node declares of itself: with the content as it was, a new declaration of the code reopens the code alone, and the six read as closed what the specification and the build accepted", () => {
    const method = fixture("method")
    const byTwo = built(method, "simplest", {}, ["write-specification", "write-build"])
    expect(done(method, byTwo)).toEqual({ done: "yes" })
    const redeclared = built(method, "simplest", { [declaration("code")]: "declared-code-2" }, ["write-specification", "write-build"])
    const d = done(method, redeclared)
    expect(d.done === "no" && d.saysNo.map((v) => v.vector)).toEqual(["write-code"])
    expect(next(method, redeclared)?.name).toBe("write-code")
    expect(passes(method, vectorOf(method, "write-code"), redeclared).outcomes.filter((o) => o.result !== "yes").map((o) => o.source)).toEqual(["verdict", "answer"])
    // The reverse control: the nodes whose declaration is as it was stay accepted.
    for (const v of ["write-design", "write-tests", "write-requirements"]) expect(passes(method, vectorOf(method, v), redeclared).result, v).toBe("yes")
  })

  it("D169, the review's policy case: what an evaluation judges against is what its verdict stands on, so a node it reads is an edge and a change to it reopens the verdict; the reverse control, the same graph without the edge, neither reads it nor reopens", () => {
    const graph = example([given("source"), given("policy"), node("result", ["source", "policy"], ["evaluation"])])
    const v = vectorOf(graph, "write-result")
    expect(against(graph, v)).toEqual(["source", "policy"])
    expect(passes(graph, v, built(graph, "simplest")).result).toBe("yes")
    expect(passes(graph, v, built(graph, "simplest", { policy: "policy-2" })).result).toBe("no")
    const without = example([given("source"), given("policy"), node("result", ["source"], ["evaluation"])])
    const w = vectorOf(without, "write-result")
    expect(against(without, w)).toEqual(["source"])
    expect(passes(without, w, built(without, "simplest", { policy: "policy-2" })).result).toBe("yes")
  })

  /** The method's graph, the test graphs and the well-formed graphs of the cases. */
  const everyGraph = (): readonly WellFormed[] => {
    const cases = (files.find((f) => f.file === "well_formed.json")?.data.cases ?? []) as J[]
    const inline = cases.filter((c) => c.expect.yes === true && c.given.graph !== undefined).map((c) => well_formed(JSON.stringify(c.given.graph), JSON.stringify(c.given.registry)))
    return [fixture("method"), fixture("small"), fixture("s6"), ...inline.flatMap((v) => ("yes" in v ? [v.yes] : []))]
  }

  it("T6: for a vector of the governing graph, yes is every node it writes accepted: wherever `passes` says yes, on a built workspace and on each with one node, its declaration or its record changed, none of its nodes is unaccepted; the reverse control, one record taken away at a node it writes, says no (D173)", () => {
    let held = 0
    let controls = 0
    for (const g of everyGraph()) {
      const whole = built(g, "simplest")
      const keys = [...whole.identities.keys()]
      const without = (at: string, field: "verdict" | "answer"): Snapshot => ({ ...whole, records: new Map([...(whole.records ?? [])].map(([n, r]) => [n, n === at ? { ...r, [field]: undefined } : r])) })
      const states = [whole, ...keys.flatMap((k) => [built(g, "simplest", { [k]: `${k}-2` }), built(g, "simplest", { [k]: null })]), ...[...(whole.records?.keys() ?? [])].flatMap((n) => [without(n, "verdict"), without(n, "answer")])]
      for (const s of states) {
        for (const v of g.graph.vectors.filter((x) => x.first !== true && passes(g, x, s).result === "yes")) {
          for (const n of placedOf(g, v).writes) expect(unaccepted(g, n, s), `${v.name} passes, and ${n} is not accepted`).toBeUndefined()
          held += 1
        }
      }
      for (const v of g.graph.vectors.filter((x) => x.first !== true && passes(g, x, whole).result === "yes")) {
        for (const [kind, field] of [["evaluation", "verdict"], ["decision", "answer"]] as const) {
          for (const n of recordsOf(g, v, kind)) {
            expect(passes(g, v, without(n, field)).result, `${v.name} without the ${field} at ${n}`).toBe("no")
            controls += 1
          }
        }
      }
    }
    expect(held).toBeGreaterThan(20)
    expect(controls).toBeGreaterThan(5)
  })

  it("D185: a record stands exactly where `since` finds nothing it was given on that differs now; a key with no content has no identity, so a record without it stands while it is still absent, as an empty identity is, and not once it is there; the reverse control, a record on content now gone, does not stand", () => {
    const method = fixture("method")
    const first = vectorOf(method, "induct-ticket").name
    const s = (identity: string): Snapshot => ({ identities: new Map([[declaration(first), "d1"]]), ticket: { path: "t.md", identity }, vectors: new Map() })
    const without = new Map([[declaration(first), "d1"]])
    expect(since(method, first, without, s(""))).toEqual([])
    expect(since(method, first, without, s("t1"))).toEqual([TICKET])
    expect(since(method, first, new Map([[TICKET, "t1"], [declaration(first), "d1"]]), s(""))).toEqual([TICKET])
  })

  it("D175: the user's confirmation of the induction stands on what the first vector declares of the ticket: a result line added gives another declaration, and with the ticket as it was the confirmation no longer stands, so the user is asked again; the reverse control, the declaration as it was, stands", () => {
    const method = fixture("method")
    const first = vectorOf(method, "induct-ticket")
    const ticket: BranchTicket = { path: ".ai-workspace/tickets/active/261122-c.md", identity: "t1", asked: "a1", enters: "code" }
    const s = inducted(method, acceptedOn(method, built(method, ticket)), ["write-code"], "code", "code")
    expect(standingKeys(method, first.name, s)).toEqual([TICKET, declaration(first.name)])
    expect(passes(method, first, s).result).toBe("yes")
    expect(asksUser(method, first, s)).toBe(false)
    // The review's P2: one line added to what the first vector declares of the ticket.
    const graph = JSON.parse(text("src", "method", "graph.json"))
    graph.vectors[0].result.push("The term names write-tests wherever it names write-code.")
    const longer = well_formed(JSON.stringify(graph), text("src", "method", "registry.json"), NEW_PRODUCT)
    if (!("yes" in longer)) throw new Error(JSON.stringify(longer.no))
    const of = (g: WellFormed) => new Map(declarationsOf(g)).get(declaration(first.name))
    expect(of(longer.yes)).not.toBe(of(method))
    for (const n of ["intent", "code"]) expect(new Map(declarationsOf(longer.yes)).get(declaration(n))).toBe(new Map(declarationsOf(method)).get(declaration(n)))
    const redeclared: Snapshot = { ...s, identities: new Map([...s.identities, [declaration(first.name), "declared-induct-ticket-2"]]) }
    expect(passes(longer.yes, vectorOf(longer.yes, first.name), redeclared).result).toBe("no")
    expect(asksUser(longer.yes, vectorOf(longer.yes, first.name), redeclared)).toBe(true)
  })

  it("D169: for every vector that declares an evaluation, in the method's graph, the test graphs and the well-formed graphs of the cases, it is judged against no node it writes and only nodes its verdict stands on", () => {
    const graphs = everyGraph()
    const none: Snapshot = { identities: new Map(), ticket: "simplest", vectors: new Map() }
    let judged = 0
    for (const g of graphs) {
      for (const v of vectorsOf(g.graph, g.registry).filter((x) => x.evaluation !== undefined)) {
        const on = new Set(recordsOf(g, v, "evaluation").flatMap((n) => standingKeys(g, n, none)))
        for (const n of against(g, v)) expect(on.has(n), `${v.name} is judged against ${n}`).toBe(true)
        judged += against(g, v).length
      }
    }
    expect(judged).toBeGreaterThan(5)
  })
})

describe("every law and acceptance line of the algorithms has a case or a named skip", () => {
  const spec = text("..", "..", "specification", "requirements", "ALGORITHMS.md").split("\n")
  const lines: string[] = []
  let section: string | undefined
  let mode: "law" | "acceptance" | undefined
  const count = { law: 0, acceptance: 0 }
  for (const line of spec) {
    const heading = /^### (REQ-ALG-\d+)/.exec(line)
    if (heading !== null) {
      section = heading[1]
      mode = undefined
      count.law = 0
      count.acceptance = 0
    } else if (line === "Laws:") mode = "law"
    else if (line === "Acceptance:") mode = "acceptance"
    else if (mode !== undefined && line.startsWith("- ")) lines.push(`${section} ${mode} ${++count[mode]}`)
    else if (line.trim() !== "" && !line.startsWith("  ")) mode = undefined
  }
  const deferred = new Set(["REQ-ALG-013"])
  const covered = new Set(files.flatMap(({ data }) => [...data.cases, ...(data.skips ?? []), ...(data.elsewhere ?? [])].flatMap((c: J) => c.covers as string[])))
  const due = lines.filter((tag) => !deferred.has(tag.split(" ")[0] ?? ""))
  it("reads the laws and acceptance lines", () => {
    expect(due.length).toBeGreaterThan(20)
  })
  for (const tag of due) {
    it(tag, () => {
      expect(covered.has(tag), `no case or named skip covers ${tag}`).toBe(true)
    })
  }
})
