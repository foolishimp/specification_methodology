/**
 * The graph language: terms made only by their constructors, in normal form
 * and unchangeable; every declaration of a vector read and written back
 * without loss; the files a node covers; the registry; traversal code
 * that names nothing of the method's graph; and the laws of the terms a
 * ticket carries (design, CALCULUS.md section 10).
 *
 * @uses C5 C6 C14
 * @is REQ-GRAPH-001 REQ-GRAPH-002 REQ-GRAPH-003 REQ-GRAPH-004 REQ-GRAPH-005 REQ-GRAPH-006 REQ-METHOD-006
 */
import { readdirSync, readFileSync } from "node:fs"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { describe, expect, it } from "vitest"
import { placedOf, well_formed } from "../src/algorithms/well_formed.js"
import { definitionOf, systemPlaces } from "../src/flows/setup.js"
import { placesNamedIn } from "../src/flows/workspace.js"
import { listing } from "../src/graph/registry.js"
import { covered, pathsOf, reference, sequence, session, TermRefused, workflow, type Term, type Workflow } from "../src/graph/terms.js"
import { RELEASE } from "../src/library/library.js"
import { denoted, inPlace, nodesOf, vectorsOf } from "../src/graph/walk.js"
import { composes } from "../src/algorithms/passes.js"
import { next } from "../src/algorithms/next.js"
import type { Snapshot } from "../src/algorithms/facts.js"
import { acceptedOn, built, confirmed as confirmedOn } from "./built_workspace.js"
import { readGraph, readRegistry, readTerm, writeGraph, writeRegistry, writeTerm } from "../src/graph/written.js"

const root = join(dirname(fileURLToPath(import.meta.url)), "..")
const text = (...path: string[]): string => readFileSync(join(root, ...path), "utf8")

function graphOf(written: string): Workflow {
  const g = readGraph(written)
  if ("faults" in g) throw new Error(JSON.stringify(g.faults))
  return g.graph
}

const everything = {
  term: "workflow",
  nodes: [
    { name: "ask", place: "in/ask.md", result: ["The ask is written by the user."], given: true },
    {
      name: "answer",
      place: "out/answer",
      result: ["The answer answers the ask.", "It is short."],
      checks: [
        { name: "runs", run: { kind: "command", argv: ["sh", "check.sh", "--all"] } },
        { name: "kept", run: { kind: "ticket_kept" } },
        { name: "urgent", run: { kind: "ticket_field", field: "urgent", is: "yes" } },
        { name: "traced", run: { kind: "traced", pattern: "ASK-[0-9]+", from: "ask", into: "answer", deferred: "Later" } }
      ],
      depends: ["ask"],
      accepted: ["evaluation", "decision"]
    }
  ],
  vectors: [
    { name: "take", first: true, result: ["The ticket says where it enters."], checks: [{ name: "enters", run: { kind: "ticket_field", field: "enters" } }], decision: {}, function: { term: "session" } },
    {
      name: "make",
      evaluation: { findings: "reviews/answer/findings.md", verdict: "reviews/answer/verdict.json" },
      decision: {},
      attempts: 2,
      minutes: 15,
      frames: {
        work: { name: "make-answer", revision: 2, method: [{ term: "ask", file: "standards/ASK.md", section: "Kinds of ask" }] },
        evaluation: { name: "judge-answer", revision: 1 }
      },
      function: { term: "sequence", terms: [{ term: "session" }, { term: "reference", name: "tidy" }] }
    }
  ]
}

describe("REQ-GRAPH-001 a graph function is a term", () => {
  it("a term is made only by its constructor and cannot be changed", () => {
    const w = workflow([{ name: "a", place: "a", result: ["made"] }], [])
    expect(Object.isFrozen(w)).toBe(true)
    expect(Object.isFrozen(w.nodes[0])).toBe(true)
    expect(() => {
      ;(w as { term: string }).term = "session"
    }).toThrow()
  })
  it("a sequence inside a sequence is flattened, and a term that does nothing is dropped", () => {
    const s = sequence([sequence([session(), session()]), sequence([]), workflow([], []), session()])
    expect(s.terms.map((t) => t.term)).toEqual(["session", "session", "session"])
  })
  it("the normal form changes neither the vectors nor their order", () => {
    const nested = {
      ...everything,
      vectors: [
        everything.vectors[0],
        {
          ...everything.vectors[1],
          function: {
            term: "sequence",
            terms: [
              { term: "sequence", terms: [] },
              { term: "workflow", nodes: [], vectors: [{ name: "inner-a", function: { term: "session" } }] },
              { term: "sequence", terms: [{ term: "workflow", nodes: [], vectors: [{ name: "inner-b", function: { term: "session" } }] }] }
            ]
          }
        }
      ]
    }
    const g = graphOf(JSON.stringify(nested))
    const fn = g.vectors[1]?.function
    expect(fn?.term === "sequence" && fn.terms.map((t) => t.term)).toEqual(["workflow", "workflow"])
    const reg = readRegistry('{"entries":[]}')
    if ("faults" in reg) throw new Error("registry")
    expect(vectorsOf(g, reg.registry).map((v) => v.name)).toEqual(["take", "make", "inner-a", "inner-b"])
  })
  it("a constructor refuses what is not a term of the language", () => {
    expect(() => workflow([{ name: "a b", place: "a", result: ["s"] }], [])).toThrow(TermRefused)
    expect(() => workflow([{ name: "a", place: "../a", result: ["s"] }], [])).toThrow(TermRefused)
    expect(() => workflow([{ name: "a", place: "a", result: ["s"] }, { name: "a", place: "b", result: ["s"] }], [])).toThrow(TermRefused)
    expect(() =>
      workflow([], [{ name: "a v", function: session() }])
    ).toThrow(TermRefused)
  })
})

describe("REQ-GRAPH-002 what a vector declares", () => {
  it("acceptance: a graph that declares each of these for a vector is read and written back without loss", () => {
    const g = graphOf(JSON.stringify(everything))
    const written = writeGraph(g)
    expect(JSON.parse(written)).toEqual(everything)
    expect(writeGraph(graphOf(written))).toBe(written)
    const make = g.vectors[1]
    expect(make && Object.keys(make)).toEqual([
      "name", "evaluation", "decision", "attempts", "minutes", "frames", "function"
    ])
  })

  it("D168, D181: what must be true of an asset and its checks are its node's: a vector other than the first that declares results or checks of its own is refused on reading; the first keeps the ticket's, which no node declares", () => {
    const make = everything.vectors[1]
    const g = readGraph(JSON.stringify({ ...everything, vectors: [everything.vectors[0], { ...make, result: ["The answer is short."] }] }))
    expect("faults" in g && g.faults).toEqual([{ fault: "terms", where: "vector 'make'", says: "declares what must be true of its result: each node it writes declares that of itself" }])
    const checked = readGraph(JSON.stringify({ ...everything, vectors: [everything.vectors[0], { ...make, checks: [{ name: "short", run: { kind: "ticket_kept" } }] }] }))
    expect("faults" in checked && checked.faults).toEqual([{ fault: "checks", where: "vector 'make'", says: "declares checks: each node it writes declares its own" }])
    expect(graphOf(JSON.stringify(everything)).vectors[0]?.result).toEqual(["The ticket says where it enters."])
    expect(graphOf(JSON.stringify(everything)).nodes[1]?.result).toEqual(["The answer answers the ask.", "It is short."])
  })

  it("D169: what an evaluation judges against is derived from the edges, not declared: a graph whose evaluation names what it is judged against is refused on reading", () => {
    const make = everything.vectors[1]
    const g = readGraph(JSON.stringify({ ...everything, vectors: [everything.vectors[0], { ...make, evaluation: { against: ["ask"], findings: "reviews/answer/findings.md", verdict: "reviews/answer/verdict.json" } }] }))
    expect("faults" in g).toBe(true)
  })

  it("acceptance: a frame for the evaluating session of a vector that declares no evaluation is refused", () => {
    const take = everything.vectors[0]
    const framed = { ...everything, vectors: [{ ...take, frames: { evaluation: { name: "judge-ticket", revision: 1 } } }, everything.vectors[1]] }
    const g = readGraph(JSON.stringify(framed))
    expect("faults" in g && g.faults).toEqual([{ fault: "terms", where: "vector 'take'", says: "declares a frame for an evaluating session, and no evaluation" }])
  })

  it("a frame's name is a name, its method files are places in the release, and its terms and sections have words", () => {
    const make = everything.vectors[1]
    const withFrame = (frames: unknown) => readGraph(JSON.stringify({ ...everything, vectors: [everything.vectors[0], { ...make, frames }] }))
    expect("faults" in withFrame({ work: { name: "make answer", revision: 1 } })).toBe(true)
    expect("faults" in withFrame({ work: { name: "make", revision: 1, method: [{ term: "ask", file: "../ASK.md", section: "Kinds" }] } })).toBe(true)
    expect("faults" in withFrame({ work: { name: "make", revision: 1, method: [{ term: " ", file: "ASK.md", section: "Kinds" }] } })).toBe(true)
    expect("faults" in withFrame({ work: { name: "make", revision: 1, method: [{ term: "ask", file: "ASK.md", section: "" }] } })).toBe(true)
    expect("faults" in withFrame({ work: { name: "make", revision: 0 } })).toBe(true)
    expect("graph" in withFrame({ work: { name: "make", revision: 1 } })).toBe(true)
  })
})

describe("REQ-GRAPH-003 an asset is declared by where it is in the workspace", () => {
  it("acceptance: for each node, the files in the workspace that it covers", () => {
    const files = [
      "specification/requirements/A.md",
      "specification/requirements.md",
      "specification/requirements/sub/B.md",
      "specification/INTENT.md"
    ]
    expect(covered(["specification/requirements"], files)).toEqual([
      "specification/requirements/A.md",
      "specification/requirements/sub/B.md"
    ])
    expect(covered(["specification/INTENT.md"], files)).toEqual(["specification/INTENT.md"])
    // Every node has a place of its own.
    expect("faults" in readGraph(JSON.stringify({ term: "workflow", nodes: [{ name: "build", result: [] }], vectors: [] }))).toBe(true)
  })

  it("acceptance: the same graph, over two definition files that give different paths to the code, covers the files each one names", () => {
    const files = ["README.md", "bin/hello", "tests/run.sh", "build_tenants/main/code/hello.sh", "build_tenants/main/tests/run.sh", "src/x.ts"]
    const codeOver = (definition: string): readonly string[] => {
      const v = well_formed(text("src", "method", "graph.json"), text("src", "method", "registry.json"), placesNamedIn(definition))
      if (!("yes" in v)) throw new Error(JSON.stringify(v.no))
      const code = nodesOf(v.yes.graph, v.yes.registry).find((n) => n.name === "code")
      return code === undefined ? [] : covered(pathsOf(code), files)
    }
    // A new product's definition file, and one over an existing system whose code is a file and a folder at the top.
    expect(codeOver(definitionOf("Hello", "hello", RELEASE, undefined))).toEqual(["build_tenants/main/code/hello.sh"])
    expect(codeOver(definitionOf("Hello", "hello", RELEASE, systemPlaces(["README.md", "bin", "tests"])))).toEqual(["README.md", "bin/hello"])
  })

  it("a definition file the method accepts, in a form set-up does not write, gives its names their paths (D73)", () => {
    // Builder's own definition file: its axioms and overrides are records, which set-up's own form does not hold.
    const own = text("..", "..", "stdo_builder.json")
    expect(placesNamedIn(own).get("code")).toEqual(["build_tenants/typescript/src", "build_tenants/typescript/scripts", "build_tenants/typescript/packaging"])
    expect(placesNamedIn(own).get("tests")).toEqual(["build_tenants/typescript/tests"])
    expect("yes" in well_formed(text("src", "method", "graph.json"), text("src", "method", "registry.json"), placesNamedIn(own))).toBe(true)
  })

  it("a place that is a name the definition file gives no path is refused, with the reason", () => {
    const v = well_formed(text("src", "method", "graph.json"), text("src", "method", "registry.json"), new Map())
    expect("no" in v && v.no.map((r) => r.rule)).toEqual(["places"])
  })
})

describe("REQ-GRAPH-004 a graph is data", () => {
  it("acceptance: the code that traverses a graph names no node, vector or asset of the method's graph", () => {
    const g = graphOf(text("src", "method", "graph.json"))
    const reg = readRegistry(text("src", "method", "registry.json"))
    if ("faults" in reg) throw new Error("registry")
    const names = new Set([
      ...nodesOf(g, reg.registry).flatMap((n) => [n.name, n.place]),
      ...vectorsOf(g, reg.registry).map((v) => v.name),
      ...reg.registry.entries.map((e) => e.name)
    ])
    for (const layer of ["kit", "graph", "algorithms"]) {
      for (const file of readdirSync(join(root, "src", layer)).filter((f) => f.endsWith(".ts"))) {
        const source = text("src", layer, file)
        for (const m of source.matchAll(/"([^"\\\n]*)"|'([^'\\\n]*)'|`([^`\\$\n]*)`/g)) {
          const literal = m[1] ?? m[2] ?? m[3] ?? ""
          expect(names.has(literal), `${layer}/${file} names "${literal}"`).toBe(false)
        }
      }
    }
  })
})

describe("REQ-GRAPH-005 every named graph function is listed in the registry", () => {
  it("acceptance: no two entries have the same name", () => {
    const r = readRegistry(
      '{"entries":[{"name":"a","writes":[],"purpose":"One.","definition":{"term":"session"}},{"name":"a","writes":[],"purpose":"Two.","definition":{"term":"session"}}]}'
    )
    expect("faults" in r && r.faults.map((f) => f.fault)).toEqual(["registry"])
  })
  it("acceptance: from the list alone, a person can say what each graph function is for", () => {
    const blank = readRegistry('{"entries":[{"name":"a","writes":[],"purpose":" ","definition":{"term":"session"}}]}')
    expect("faults" in blank).toBe(true)
    const r = readRegistry(text("src", "method", "registry.json"))
    if ("faults" in r) throw new Error("registry")
    const listed = listing(r.registry, graphOf(text("src", "method", "graph.json")).nodes)
    // What each entry rests on is derived from the nodes it writes: the build rests on the requirements, the specification on nothing but the ticket.
    expect(listed.filter((e) => ["write-specification", "write-build"].includes(e.name)).map((e) => [e.name, e.rests])).toEqual([["write-specification", []], ["write-build", ["requirements"]]])
    for (const entry of listed) {
      expect(Object.keys(entry)).toEqual(["name", "writes", "rests", "purpose"])
      expect(entry.purpose.endsWith(".")).toBe(true)
    }
    expect(writeRegistry(r.registry)).toBe(text("src", "method", "registry.json"))
  })
  it("acceptance: an entry that writes what is no node of the governing graph is refused", () => {
    const registry = JSON.parse(text("src", "method", "registry.json")) as { entries: { name: string }[] }
    const wrong = { ...registry, entries: registry.entries.map((e) => (e.name === "induct-ticket" ? { ...e, writes: ["the ticket"] } : e)) }
    const v = well_formed(text("src", "method", "graph.json"), JSON.stringify(wrong))
    expect("no" in v && v.no).toEqual([{ rule: "registry", where: "registry entry 'induct-ticket'", says: "writes 'the ticket', which is no node of the graph" }])
  })
  it("the registry's default term is read and written with it, and one that denotes nothing, or names the first vector, is refused", () => {
    const registry = JSON.parse(text("src", "method", "registry.json")) as Record<string, unknown>
    const withDefault = (d: unknown) => well_formed(text("src", "method", "graph.json"), JSON.stringify({ ...registry, default: d }))
    expect("no" in withDefault({ term: "reference", name: "write-everything" }) && withDefault({ term: "reference", name: "write-everything" })).toEqual({ no: [{ rule: "terms", where: "the registry's default term", says: "write-everything is not in the registry" }] })
    const first = withDefault({ term: "reference", name: "induct-ticket" })
    expect("no" in first && first.no.map((r) => r.where)).toEqual(["the registry's default term"])
    const r = readRegistry(text("src", "method", "registry.json"))
    expect("registry" in r && r.registry.default?.term).toBe("sequence")
  })
  it("a graph holds a reference to a named graph function, never a copy of it", () => {
    const g = graphOf(text("src", "method", "graph.json"))
    for (const v of g.vectors) expect(v.function.term).toBe("reference")
  })
})

describe("REQ-GRAPH-006 what is run in a vector's place", () => {
  const r = readRegistry(JSON.stringify({
    entries: [
      { name: "one", writes: ["x"], purpose: "One session.", definition: { term: "session" } },
      { name: "alias", writes: ["x"], purpose: "Another name for one.", definition: { term: "reference", name: "one" } },
      { name: "steps", writes: ["x"], purpose: "A workflow of no vectors' own here.", definition: { term: "workflow", nodes: [], vectors: [{ name: "inner", function: { term: "reference", name: "one" } }] } }
    ]
  }))
  if ("faults" in r) throw new Error(JSON.stringify(r.faults))
  const reg = r.registry
  const termOf = (written: unknown) => {
    const g = readGraph(JSON.stringify({ term: "workflow", nodes: [{ name: "x", place: "x", result: ["s"] }], vectors: [{ name: "v", function: written }] }))
    if ("faults" in g) throw new Error(JSON.stringify(g.faults))
    const v = g.graph.vectors[0]
    if (v === undefined) throw new Error("no vector")
    return v.function
  }
  it("a session, or a reference to one through any number of names, is one session", () => {
    expect(inPlace(termOf({ term: "session" }), reg).map((t) => t.term)).toEqual(["session"])
    expect(inPlace(termOf({ term: "reference", name: "alias" }), reg).map((t) => t.term)).toEqual(["session"])
  })
  it("a sequence is its terms in the order written, inner sequences flattened; a workflow is itself, not what is inside it", () => {
    const got = inPlace(termOf({ term: "sequence", terms: [{ term: "reference", name: "one" }, { term: "sequence", terms: [{ term: "reference", name: "steps" }, { term: "session" }] }] }), reg)
    expect(got.map((t) => t.term)).toEqual(["session", "workflow", "session"])
    const w = got[1]
    expect(w?.term === "workflow" ? w.vectors.map((v) => v.name) : []).toEqual(["inner"])
  })
})

describe("the laws of the terms a ticket carries (REQ-METHOD-006; CALCULUS.md section 10)", () => {
  const graphText = text("src", "method", "graph.json")
  const registryText = text("src", "method", "registry.json")
  // The method's registry with one entry more: a name for the specification and then the build, which no vector carries out.
  const aliased = JSON.stringify({
    ...(JSON.parse(registryText) as object),
    entries: [
      ...(JSON.parse(registryText) as { entries: unknown[] }).entries,
      { name: "write-whole", writes: ["intent", "product", "requirements", "design", "tests", "code"], purpose: "The specification and then the build.", definition: { term: "sequence", terms: [{ term: "reference", name: "write-specification" }, { term: "reference", name: "write-build" }] } }
    ]
  })
  const v = well_formed(graphText, aliased)
  if (!("yes" in v)) throw new Error(JSON.stringify(v.no))
  const method = v.yes
  const names = (t: Term): readonly string[] => {
    const d = denoted(t, method.graph, method.registry)
    return "entries" in d ? d.entries.map((x) => x.v.name) : [d.why]
  }
  const [a, b, c] = ["write-requirements", "write-design", "write-code"].map((n) => reference(n)) as [Term, Term, Term]

  it("T1: sequence is associative, and the empty sequence is its identity, up to the normal form the constructor gives", () => {
    expect(sequence([sequence([a, b]), c])).toEqual(sequence([a, sequence([b, c])]))
    expect(sequence([sequence([]), a])).toEqual(sequence([a]))
    expect(sequence([a, sequence([])])).toEqual(sequence([a]))
  })
  it("a term reads back from its one written line as the term it was, an induction entry with its stretch", () => {
    const t = sequence([a, b, c])
    expect(readTerm(writeTerm(t))).toEqual({ term: t })
    const entry = reference("induct-ticket", { enters: "design", ends: "code" })
    expect(writeTerm(entry)).toBe('{"term":"reference","name":"induct-ticket","enters":"design","ends":"code"}')
    expect(readTerm(writeTerm(sequence([a, entry])))).toEqual({ term: sequence([a, entry]) })
  })
  it("an induction entry denotes the first vector, bound to its stretch; a stretch on a reference no vector carries out denotes nothing", () => {
    const d = denoted(sequence([a, reference("induct-ticket", { enters: "design", ends: "code" })]), method.graph, method.registry)
    expect("entries" in d ? d.entries.map((e) => [e.v.name, e.stretch]) : d).toEqual([["write-requirements", undefined], ["induct-ticket", { enters: "design", ends: "code" }]])
    expect(names(reference("write-whole", { enters: "intent", ends: "code" }))).toEqual(["write-whole names a stretch, and is carried out by no vector of the graph"])
    expect(() => reference("induct-ticket", { enters: "design" })).toThrow(TermRefused)
  })
  it("T1: the denotation of a sequence is the denotations of its terms one after the other", () => {
    expect(names(sequence([sequence([a, b]), c]))).toEqual([...names(a), ...names(b), ...names(c)])
    expect(names(sequence([]))).toEqual([])
  })
  it("T2: a reference means the term it names where no vector of the graph carries it out: then it denotes its definition", () => {
    expect(names(reference("write-whole"))).toEqual(["write-specification", "write-build"])
    expect(names(sequence([reference("write-whole")]))).toEqual(names(sequence([reference("write-specification"), reference("write-build")])))
  })
  it("T2's condition: a reference to an entry a vector carries out denotes that vector, not its definition, which is a session", () => {
    expect(names(reference("write-specification"))).toEqual(["write-specification"])
    expect(names(session())).toEqual(["the term holds a session that no vector of the graph carries out"])
  })
  const ticket = { path: ".ai-workspace/tickets/active/261121-a.md", identity: "t1", asked: "a1", enters: "intent" }
  const empty: Snapshot = { identities: new Map(), ticket, vectors: new Map() }
  const fields = (order: readonly string[], enters = "intent", ends = "code") => new Map([["term", writeTerm(sequence(order.map((n) => reference(n))))], ["enters", enters], ["ends", ends]])
  const orders = (rest: readonly string[]): readonly (readonly string[])[] =>
    rest.length === 0 ? [[]] : rest.flatMap((n) => orders(rest.filter((m) => m !== n)).map((o) => [n, ...o]))
  const SIX = ["write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]
  /** The fields the term's check reads, for a term over the work from `enters` to `ends`. */
  const termFields = (t: Term, enters = "intent", ends = "code") => new Map([["term", writeTerm(t)], ["enters", enters], ["ends", ends]])
  /** The induction confirmed on the ticket whose identity is given. */
  const confirmed = (s: Snapshot, identity: string): Snapshot => confirmedOn(method, s, identity)

  /** What each of the six writes, and what it rests on, by name. */
  const arrows = new Map(method.graph.vectors.map((x) => [x.name, placedOf(method, x)]))
  /** Each entry comes after the entries that write what it rests on. */
  const respects = (order: readonly string[]): boolean =>
    order.every((n, i) => (arrows.get(n)?.rests ?? []).every((r) => order.slice(0, i).some((m) => arrows.get(m)?.writes.includes(r))))
  it("T3: of the 720 orders of the six from the intent to the code, on an empty workspace and on a built one, exactly those that respect the edges compose: the tests come before the design or after it", () => {
    const lawful = orders(SIX).filter(respects)
    expect(lawful).toEqual([SIX, ["write-intent", "write-product", "write-requirements", "write-tests", "write-design", "write-code"]])
    for (const workspace of [empty, built(method, ticket)]) {
      const composing = orders(SIX).filter((order) => composes(method, fields(order), workspace).result === "yes")
      expect(composing).toEqual(lawful)
    }
  })
  it("T3 on a built workspace: the terms that compose on what is accepted and write exactly the work from where it enters to where it ends are well formed", () => {
    const at = (enters: string) => built(method, { ...ticket, enters })
    for (const [term, enters, ends] of [
      [["write-requirements", "write-build"], "requirements", "code"],
      [["write-requirements", "write-design", "write-tests", "write-code"], "requirements", "code"],
      [["write-requirements", "write-tests", "write-design", "write-code"], "requirements", "code"],
      // A change that enters at the design and ends at the code writes the design and the code, and rests on the tests as they are (D161).
      [["write-design", "write-code"], "design", "code"],
      [["write-tests", "write-code"], "tests", "code"],
      [["write-design"], "design", "design"],
      [["write-code"], "code", "code"],
      [["write-whole"], "intent", "code"],
      [["write-intent", "write-product", "write-requirements"], "intent", "requirements"],
      [["write-product", "write-requirements"], "product", "requirements"]
    ] as const) expect(composes(method, fields(term, enters, ends), at(enters)), term.join(" ")).toEqual({ result: "yes" })
  })
  it("T3 on a built workspace: terms that do not compose, or do not run from where the work starts to where it ends, are refused", () => {
    const at = (enters: string) => built(method, { ...ticket, enters })
    for (const [term, enters, ends] of [
      [["write-requirements", "write-code"], "requirements", "code"],
      [["write-intent", "write-design"], "intent", "design"],
      [["write-code", "write-requirements"], "requirements", "code"],
      [["write-code", "write-intent"], "intent", "code"],
      [["write-code", "write-tests"], "tests", "code"],
      [["write-specification", "write-build"], "intent", "design"],
      [["write-whole"], "intent", "requirements"],
      // The build writes the tests, which the work from the design to the code does not hold (D161).
      [["write-build"], "design", "code"],
      [["write-design", "write-tests", "write-code"], "design", "code"],
      [["write-intent", "write-intent"], "intent", "intent"]
    ] as const) expect(composes(method, fields(term, enters, ends), at(enters)).result, term.join(" ")).toBe("no")
    // An entry that needs a node written only after it: the finding names the entry and the node, once.
    expect(composes(method, fields(["write-code", "write-tests"], "tests"), at("tests")).found).toBe("write-code rests on tests, which is neither accepted nor written before it")
    expect(composes(method, fields(["write-intent", "write-intent"], "intent", "intent"), at("intent")).found).toBe("write-intent writes intent, which an entry before it writes")
    // A term that composes and does not write the work, or writes beyond it, is refused by what it misses or what lies outside.
    expect(composes(method, fields(["write-requirements", "write-code"], "requirements"), at("requirements")).found?.split("; ").filter((f) => f.startsWith("no entry"))).toEqual([
      "no entry of the term writes design, which the work from requirements to code covers",
      "no entry of the term writes tests, which the work from requirements to code covers"
    ])
    expect(composes(method, fields(["write-build"], "design"), at("design")).found).toBe("write-build writes tests, which lies outside the work from design to code")
    expect(composes(method, fields(["write-code"], "code", "intent"), at("code")).found).toBe("the work ends at intent, which neither is code nor depends on it")
  })
  it("T5: a term well formed on an induction entry's stretch, put in the entry's place, leaves the whole term well formed, and the run steps on what the whole then denotes", () => {
    // A workspace on which the entries before every stretch stand: built, and accepted after the ticket was inducted.
    const workspace = acceptedOn(method, built(method, ticket))
    const order = ["intent", "product", "requirements", "design", "tests", "code"]
    const single = new Map(SIX.map((name, i) => [order[i] ?? "", name]))
    /** Every node a node depends on, directly or through others. */
    const below = (n: string): readonly string[] => {
      const direct = method.graph.nodes.find((x) => x.name === n)?.depends ?? []
      return [...new Set([...direct, ...direct.flatMap(below)])]
    }
    /** The work from `a` to `b`: those two and every node that depends on the first and on which the second depends. */
    const work = (a: string, b: string): readonly string[] => order.filter((n) => n === a || n === b || (below(b).includes(n) && below(n).includes(a)))
    // Every stretch of the graph: its end is where it enters or depends on it. An induction entry is never a term's first entry (R2), so none enters at the intent.
    const stretches = order.flatMap((a) => order.filter((b) => b === a || below(b).includes(a)).map((b) => [a, b] as const)).filter(([a]) => a !== "intent")
    const entries = ["write-specification", "write-build", "write-whole", ...SIX]
    let held = 0
    for (const [s, e] of stretches) {
      const inside = work(s, e)
      // Before the entry, the single writers of every node the stretch rests on; after it, those of every other node.
      const before = order.filter((n) => !inside.includes(n) && inside.some((m) => below(m).includes(n)))
      const after = order.filter((n) => !inside.includes(n) && !before.includes(n))
      const entry = reference("induct-ticket", { enters: s, ends: e })
      const outer = sequence([...before.map((n) => reference(single.get(n) ?? "")), entry, ...after.map((n) => reference(single.get(n) ?? ""))])
      expect(composes(method, termFields(outer), workspace), `${s} to ${e}`).toEqual({ result: "yes" })
      // Every term of at most three entries, and of at most two where one is an induction entry over a stretch whose work lies inside this one; one that begins with an induction entry is refused on its own (R2).
      const inner = stretches.filter(([a, b]) => !(a === s && b === e) && work(a, b).every((n) => inside.includes(n))).map(([a, b]) => reference("induct-ticket", { enters: a, ends: b }))
      const plain = entries.map((n) => reference(n))
      const candidates = [
        ...plain.map((x) => [x]),
        ...plain.flatMap((x) => plain.map((y) => [x, y])),
        ...plain.flatMap((x) => plain.flatMap((y) => plain.map((z) => [x, y, z]))),
        ...inner.map((x) => [x]),
        ...[...plain, ...inner].flatMap((x) => [...plain, ...inner].map((y) => [x, y]))
      ]
      for (const parts of candidates) {
        const r = sequence(parts)
        if (composes(method, termFields(r, s, e), workspace).result !== "yes") continue
        held++
        const whole = sequence([...before.map((n) => reference(single.get(n) ?? "")), r, ...after.map((n) => reference(single.get(n) ?? ""))])
        const shown = writeTerm(whole)
        expect(composes(method, termFields(whole), workspace), shown).toEqual({ result: "yes" })
        // The framework's check of the substitution says the same, on the ticket changed since the user confirmed the outer term.
        expect(composes(method, termFields(whole), confirmed(workspace, "t0"), { fields: termFields(outer), asked: "a1" }), shown).toEqual({ result: "yes" })
        // What the whole denotes is the entries before, those of the term put in, and those after, in that order (T1).
        expect(names(whole), shown).toEqual([...before.flatMap((n) => names(reference(single.get(n) ?? ""))), ...names(r), ...after.flatMap((n) => names(reference(single.get(n) ?? "")))])
      }
      // The reverse control: the same term put at the end, out of the entry's place, breaks the whole wherever a node after the stretch depends on it.
      if (after.length > 0) {
        const r = sequence(inside.map((n) => reference(single.get(n) ?? "")))
        expect(composes(method, termFields(sequence([...[...before, ...after].map((n): Term => reference(single.get(n) ?? "")), r])), workspace).result, `${s} to ${e} at the end`).toBe("no")
      }
    }
    expect(held).toBeGreaterThan(stretches.length)
  })
  it("T5: after the substitution the run steps on what the new term denotes: next is the first vector of the term put in the entry's place", () => {
    const up = confirmed(acceptedOn(method, built(method, ticket, { design: null, tests: null, code: null })), "t1")
    const four = ["write-intent", "write-product", "write-requirements"].map((n) => reference(n))
    for (const [inner, first] of [
      [[reference("write-build")], "write-build"],
      [["write-design", "write-tests", "write-code"].map((n) => reference(n)), "write-design"],
      [[reference("write-design"), reference("induct-ticket", { enters: "tests", ends: "code" })], "write-design"]
    ] as const) {
      const whole = sequence([...four, ...inner])
      const s: Snapshot = { ...up, ticket: { ...ticket, term: names(whole) } }
      const at: Snapshot = { ...s, vectors: new Map([...s.vectors].map(([n, f]) => [n, n === "induct-ticket" ? { ...f, composes: composes(method, termFields(whole), s) } : f])) }
      expect(next(method, at)?.name, writeTerm(whole)).toBe(first)
    }
  })
  it("T3 on a built workspace: a node an entry rests on is accepted only where the records it declares stand for it and every node it depends on is accepted, not where it is merely there", () => {
    const changed = built(method, { ...ticket, enters: "design" }, { requirements: "requirements-2" })
    expect(changed.identities.has("requirements")).toBe(true)
    // The tests rest on the requirements too, so they stand no longer either: each node is said once, at the first entry that rests on it.
    expect(composes(method, fields(["write-design", "write-code"], "design"), changed).found).toBe([
      "write-design rests on requirements, which is neither accepted nor written before it: the user has not accepted requirements as it now stands; enter at requirements",
      "write-code rests on tests, which is neither accepted nor written before it: the user has not accepted requirements as it now stands; enter at requirements"
    ].join("; "))
    // Where a node it depends on is not accepted either, the work enters there.
    const deeper = composes(method, fields(["write-design", "write-code"], "design"), built(method, { ...ticket, enters: "design" }, { product: "product-2", requirements: "requirements-2" })).found
    expect(deeper?.split("; ")[0]).toBe("write-design rests on requirements, which is neither accepted nor written before it: the user has not accepted product as it now stands")
    expect(deeper?.split("; ")[1]).toBe("enter at product")
    expect(composes(method, fields(["write-requirements", "write-build"], "requirements"), built(method, { ...ticket, enters: "requirements" }, { requirements: "requirements-2" }))).toEqual({ result: "yes" })
  })
})
