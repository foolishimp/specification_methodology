/**
 * The method's graph as shipped: well formed, written in its one form, and
 * declaring what REQ-METHOD-001 to 005 require of it. These are checks of the
 * graph's declarations; how a run follows them is in the algorithms' cases.
 * The method's graph and registry also give the graph functions a ticket's
 * term may name (REQ-METHOD-006); how a run interprets a term is in
 * `induction.scenario.test.ts`.
 *
 * @uses C5 C6 C14
 * @is REQ-METHOD-001 REQ-METHOD-002 REQ-METHOD-003 REQ-METHOD-004 REQ-METHOD-005 REQ-METHOD-006 REQ-GRAPH-001 REQ-GRAPH-002 REQ-GRAPH-003
 */
import { execFileSync } from "node:child_process"
import { readFileSync } from "node:fs"
import { homedir } from "node:os"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { describe, expect, it } from "vitest"
import { done } from "../src/algorithms/done.js"
import { next } from "../src/algorithms/next.js"
import { open } from "../src/algorithms/open.js"
import { against, composes, identitiesAt, passes, recordsOf } from "../src/algorithms/passes.js"
import { checksOf, placedOf, well_formed, type WellFormed } from "../src/algorithms/well_formed.js"
import { definitionOf } from "../src/flows/setup.js"
import { placesNamedIn } from "../src/flows/workspace.js"
import { pathsOf, type Vector } from "../src/graph/terms.js"
import { RELEASE } from "../src/library/library.js"
import { nodesOf } from "../src/graph/walk.js"
import { readGraph, writeGraph } from "../src/graph/written.js"
import { built, fieldsOf, inducted } from "./built_workspace.js"

const root = join(dirname(fileURLToPath(import.meta.url)), "..")
const graphText = readFileSync(join(root, "src", "method", "graph.json"), "utf8")
const registryText = readFileSync(join(root, "src", "method", "registry.json"), "utf8")
const verdict = well_formed(graphText, registryText)
if (!("yes" in verdict)) throw new Error(`the method's graph is not well formed: ${JSON.stringify(verdict.no)}`)
const method = verdict.yes
const vector = (name: string): Vector => {
  const v = method.graph.vectors.find((x) => x.name === name)
  if (v === undefined) throw new Error(name)
  return v
}
/** What the vector writes, and what it rests on. */
const arrow = (name: string): readonly (readonly string[])[] => [placedOf(method, vector(name)).writes, placedOf(method, vector(name)).rests]

describe("the method's graph", () => {
  it("is well formed with its registry, written in the terms of the graph language (REQ-GRAPH-001)", () => {
    expect("yes" in verdict).toBe(true)
  })
  it("survives a write and a read back unchanged, byte for byte", () => {
    const written = writeGraph(method.graph)
    expect(written).toBe(graphText)
    const again = readGraph(written)
    expect("graph" in again && again.graph).toEqual(method.graph)
  })
})

describe("REQ-METHOD-001 the method's graph", () => {
  it("its six nodes and the nodes each depends on are the method's edges, and each vector writes nodes and rests on what they depend on", () => {
    expect(method.graph.nodes.map((n) => [n.name, n.depends ?? []])).toEqual([
      ["intent", []], ["product", ["intent"]], ["requirements", ["intent", "product"]],
      ["design", ["requirements"]], ["tests", ["requirements"]], ["code", ["requirements", "design", "tests"]]
    ])
    expect(method.graph.vectors.map((v) => [v.name, ...arrow(v.name)])).toEqual([
      ["induct-ticket", [], []], ["write-specification", ["intent", "product", "requirements"], []], ["write-build", ["design", "tests", "code"], ["requirements"]],
      ["write-intent", ["intent"], []], ["write-product", ["product"], ["intent"]], ["write-requirements", ["requirements"], ["intent", "product"]],
      ["write-design", ["design"], ["requirements"]], ["write-tests", ["tests"], ["requirements"]], ["write-code", ["code"], ["requirements", "design", "tests"]]
    ])
  })
  it("builds the design, the tests and the code in a build tenant, as the definition file set-up writes for a new product declares", () => {
    const placed = well_formed(graphText, registryText, placesNamedIn(definitionOf("Hello", "hello", RELEASE, undefined)))
    if (!("yes" in placed)) throw new Error(JSON.stringify(placed.no))
    const places = new Map(nodesOf(placed.yes.graph, placed.yes.registry).map((n) => [n.name, pathsOf(n)]))
    for (const name of ["design", "tests", "code"]) expect(places.get(name)).toEqual([`build_tenants/main/${name}`])
  })
  it("acceptance: every vector of the graph declares the frame of each of its sessions", () => {
    for (const v of method.graph.vectors) {
      expect(v.frames?.work, `${v.name} work`).toMatchObject({ name: v.name, revision: 1 })
      if (v.evaluation === undefined) expect(v.frames?.evaluation, v.name).toBeUndefined()
      else expect(v.frames?.evaluation, `${v.name} evaluation`).toMatchObject({ name: v.name.replace("write-", "judge-"), revision: 1 })
    }
  })
})

/** Where the method keeps the release set-up selects, as its manager says. */
const installedRelease = (): string => {
  const said = execFileSync("stdo", ["resolve", RELEASE.uri], { encoding: "utf8", env: { ...process.env, PATH: `${join(homedir(), ".local", "bin")}:${process.env.PATH ?? ""}` } })
  return (JSON.parse(said) as { path: string }).path
}

describe("REQ-METHOD-002 the first vector for a ticket inducts it", () => {
  it("there is one first vector, and its checks ask the ticket for its triage and its term, and keep the user's words", () => {
    const firsts = method.graph.vectors.filter((v) => v.first === true)
    expect(firsts.map((v) => v.name)).toEqual(["induct-ticket"])
    const fields = checksOf(method, vector("induct-ticket")).flatMap((c) => (c.run.kind === "ticket_field" ? [c.run.field] : []))
    expect(fields).toEqual(["kind", "class", "enters", "ends", "scope", "term"])
    expect(checksOf(method, vector("induct-ticket")).some((c) => c.run.kind === "ticket_kept")).toBe(true)
  })
  it("acceptance: the file and the section the frame names for the kind, the class and the triage are there in the method release the product selects", () => {
    const named = vector("induct-ticket").frames?.work?.method ?? []
    expect(named.map((m) => m.term)).toEqual(["kind", "class", "triage"])
    const release = installedRelease()
    for (const m of named) {
      const headings = readFileSync(join(release, m.file), "utf8").split("\n").filter((l) => /^#+ /.test(l)).map((l) => l.replace(/^#+ /, "").trim())
      expect(headings, `${m.file}: ${m.section}`).toContain(m.section)
    }
  })
})

describe("REQ-METHOD-003 what is wanted is agreed before it is designed", () => {
  it("the specification, and each of the intent, the product definition and the requirements, end in the user's decision, asked whatever the ticket says", () => {
    for (const name of ["write-specification", "write-intent", "write-product", "write-requirements"]) expect(vector(name).decision, name).toEqual({})
  })
  it("neither the design nor the tests are written before the user has accepted the requirements as they stand: on a built product whose requirements changed after the answer, no term enters below them and `next` gives neither", () => {
    const placed = well_formed(graphText, registryText, placesNamedIn(definitionOf("Hello", "hello", RELEASE, undefined)))
    if (!("yes" in placed)) throw new Error(JSON.stringify(placed.no))
    const graph = placed.yes
    const ticket = (enters: string) => ({ path: ".ai-workspace/tickets/active/261121-a.md", identity: "t1", asked: "a1", enters })
    const changed = (enters: string) => built(graph, ticket(enters), { requirements: "requirements-2" })
    const below = (name: string | undefined) => ["write-design", "write-tests", "write-build"].includes(name ?? "")
    // The build writes the tests and the design, which no work below the requirements holds both of: it follows a requirements writer.
    for (const [term, enters] of [[["write-design", "write-code"], "design"], [["write-tests", "write-code"], "tests"], [["write-build"], "design"]] as const) {
      const got = composes(graph, fieldsOf(term, enters, "code"), changed(enters))
      expect(got.result, term.join(" ")).toBe("no")
      expect(got.found, term.join(" ")).toContain("enter at requirements")
      expect(next(graph, inducted(graph, changed(enters), term, enters, "code"))?.name, term.join(" ")).toBe("induct-ticket")
    }
    // Entering at the requirements, or with no ticket, the requirements are asked for again first.
    expect(next(graph, inducted(graph, changed("requirements"), ["write-requirements", "write-build"], "requirements", "code"))?.name).toBe("write-requirements")
    expect(below(next(graph, built(graph, "simplest", { requirements: "requirements-2" }))?.name)).toBe(false)
    expect(next(graph, built(graph, "simplest", { requirements: "requirements-2" }))?.name).toBe("write-requirements")
    // Once the user accepts them as they stand, the same term composes and the design is next.
    expect(next(graph, inducted(graph, built(graph, ticket("design")), ["write-design", "write-code"], "design", "code"))?.name).toBe("write-design")
  })
})

describe("REQ-METHOD-004 the author of an asset is never its only judge", () => {
  it("acceptance: the vector that writes the tests rests on the accepted requirements alone: neither the design nor the code is among what it rests on", () => {
    expect(placedOf(method, vector("write-tests")).rests).toEqual(["requirements"])
  })
  it("D169: the design and the tests are each evaluated against the accepted requirements, and the built product against them, the design and the tests: what the node judged depends on", () => {
    for (const name of ["write-design", "write-tests"]) expect(against(method, vector(name))).toEqual(["requirements"])
    expect(against(method, vector("write-code"))).toEqual(["requirements", "design", "tests"])
  })
  it("the code rests on the requirements, the design and the tests, and ends in the user's decision", () => {
    expect(placedOf(method, vector("write-code")).rests).toEqual(["requirements", "design", "tests"])
    expect(vector("write-code").decision).toEqual({})
  })
})

describe("REQ-METHOD-005 nothing is orphaned", () => {
  it("the design, the tests and the code each have a check that traces the requirements into them", () => {
    for (const [name, into] of [["write-design", "design"], ["write-tests", "tests"], ["write-code", "code"]] as const) {
      const traced = checksOf(method, vector(name)).find((c) => c.run.kind === "traced")?.run
      expect(traced).toMatchObject({ kind: "traced", from: "requirements", into })
    }
  })
})

describe("REQ-METHOD-006 induction chooses the graph functions", () => {
  it("each vector carries out the graph function of the registry of its name; the specification writes the intent, the product definition and the requirements, and the build the design, the tests and the code", () => {
    for (const v of method.graph.vectors) expect(v.function, v.name).toEqual({ term: "reference", name: v.name })
    expect(placedOf(method, vector("write-specification")).writes).toEqual(["intent", "product", "requirements"])
    expect(placedOf(method, vector("write-build")).writes).toEqual(["design", "tests", "code"])
  })

  it("REQ-METHOD-006 acceptance 15, D164: acceptance of a node is acceptance of that node whoever wrote it: on main, a product the specification and the build wrote is done under the six, and one the six wrote is done under the specification and the build", () => {
    expect(done(method, built(method, "simplest", {}, ["write-specification", "write-build"]))).toEqual({ done: "yes" })
    expect(next(method, built(method, "simplest", {}, ["write-specification", "write-build"]))).toBeUndefined()
    const registry = JSON.parse(registryText) as Record<string, unknown>
    const whole = well_formed(graphText, JSON.stringify({ ...registry, default: { term: "sequence", terms: [{ term: "reference", name: "write-specification" }, { term: "reference", name: "write-build" }] } }))
    if (!("yes" in whole)) throw new Error(JSON.stringify(whole.no))
    expect(whole.yes.byDefault).toEqual(["write-specification", "write-build"])
    expect(done(whole.yes, built(whole.yes, "simplest", {}, method.byDefault))).toEqual({ done: "yes" })
    expect(next(whole.yes, built(whole.yes, "simplest", {}, method.byDefault))).toBeUndefined()
    // A change to the design reopens the build, as it reopens the design and the code of the six.
    expect(next(whole.yes, built(whole.yes, "simplest", { design: "design-2" }, method.byDefault))?.name).toBe("write-build")
  })

  /**
   * The vectors of the default term an edit of `node` reopens: stepping through the term in its order, each
   * that does not pass is accepted again on the content as it is, its records written where it records them,
   * before the next is read. The sessions change nothing, so what reopens is what the edit leaves stale.
   */
  const reopened = (graph: WellFormed, node: string, by: readonly string[]): readonly string[] => {
    let s = built(graph, "simplest", { [node]: `${node}-2` }, by)
    const again: string[] = []
    for (const name of graph.byDefault) {
      const v = graph.graph.vectors.find((x) => x.name === name) as Vector
      if (passes(graph, v, s).result === "yes") continue
      again.push(name)
      const records = new Map(s.records)
      for (const kind of ["evaluation", "decision"] as const) {
        for (const at of recordsOf(graph, v, kind)) {
          records.set(at, { ...records.get(at), [kind === "evaluation" ? "verdict" : "answer"]: { says: "yes", on: identitiesAt(graph, at, s) } })
        }
      }
      s = { ...s, records }
    }
    return again
  }

  it("D164: a node is accepted only where every node it depends on is, so an edit leaves open at once every vector that writes what depends on the edited node", () => {
    const s = built(method, "simplest", { intent: "intent-2" }, method.byDefault)
    expect(method.byDefault.filter((name) => open(method, vector(name), s))).toEqual(method.byDefault)
  })

  it("D164: an acceptance stands on the node and the nodes it depends on, so an edit reopens, in the default term's order, what depends on the edited node directly or through others whose content the edit changes, and no more", () => {
    expect(reopened(method, "intent", method.byDefault)).toEqual(["write-intent", "write-product", "write-requirements"])
    expect(reopened(method, "product", method.byDefault)).toEqual(["write-product", "write-requirements"])
    expect(reopened(method, "requirements", method.byDefault)).toEqual(["write-requirements", "write-design", "write-tests", "write-code"])
    expect(reopened(method, "design", method.byDefault)).toEqual(["write-design", "write-code"])
    expect(reopened(method, "tests", method.byDefault)).toEqual(["write-tests", "write-code"])
    expect(reopened(method, "code", method.byDefault)).toEqual(["write-code"])
  })

  it("D164: under the specification and then the build as the default, an edit of the intent, the product definition or the requirements reopens the specification, and of the design, the tests or the code the build; whichever grain built the product", () => {
    const registry = JSON.parse(registryText) as Record<string, unknown>
    const two = well_formed(graphText, JSON.stringify({ ...registry, default: { term: "sequence", terms: [{ term: "reference", name: "write-specification" }, { term: "reference", name: "write-build" }] } }))
    if (!("yes" in two)) throw new Error(JSON.stringify(two.no))
    for (const by of [two.yes.byDefault, method.byDefault]) {
      expect(reopened(two.yes, "intent", by), by.join(" ")).toEqual(["write-specification"])
      expect(reopened(two.yes, "requirements", by), by.join(" ")).toEqual(["write-specification", "write-build"])
      expect(reopened(two.yes, "design", by), by.join(" ")).toEqual(["write-build"])
      expect(reopened(two.yes, "code", by), by.join(" ")).toEqual(["write-build"])
    }
    for (const node of ["intent", "requirements", "tests"]) expect(reopened(method, node, two.yes.byDefault)).toEqual(reopened(method, node, method.byDefault))
  })

  it("REQ-GRAPH-003: the user's yes accepts the intent, the product definition and the requirements; an evaluation's yes the design and the tests; both the code", () => {
    expect(new Map(method.graph.nodes.map((n) => [n.name, n.accepted ?? []]))).toEqual(new Map([
      ["intent", ["decision"]], ["product", ["decision"]], ["requirements", ["decision"]],
      ["design", ["evaluation"]], ["tests", ["evaluation"]], ["code", ["evaluation", "decision"]]
    ]))
  })

  it("REQ-GRAPH-002 acceptance 2: a vector that writes the code and ends in no decision is refused, and so is one that writes only the design and ends in one", () => {
    const g = JSON.parse(graphText) as { vectors: { name: string; decision?: unknown }[] }
    const decision = g.vectors.find((v) => v.name === "write-code")?.decision
    const changed = (name: string, f: (v: { name: string; decision?: unknown }) => object): string =>
      JSON.stringify({ ...g, vectors: g.vectors.map((v) => (v.name === name ? f(v) : v)) })
    const refused = (text: string): string => {
      const v = well_formed(text, registryText)
      return "no" in v ? v.no.map((r) => `${r.where} ${r.says}`).join("; ") : ""
    }
    expect(refused(changed("write-code", ({ decision: _, ...rest }) => rest))).toContain("vector 'write-code' writes code, which a decision accepts, and declares none")
    expect(refused(changed("write-design", (v) => ({ ...v, decision })))).toContain("vector 'write-design' declares a decision, and no node it writes is accepted by one")
  })

  // The method's graph with each edge stated once: the requirements depend on the product definition alone, and the code on the design and the tests.
  const reducedText = (): string => {
    const g = JSON.parse(graphText) as { nodes: { name: string; depends?: string[] }[] }
    return JSON.stringify({ ...g, nodes: g.nodes.map((n) => (n.name === "requirements" ? { ...n, depends: ["product"] } : n.name === "code" ? { ...n, depends: ["design", "tests"] } : n)) })
  }
  const reduced = (): WellFormed => {
    const v = well_formed(reducedText(), registryText)
    if (!("yes" in v)) throw new Error(JSON.stringify(v.no))
    return v.yes
  }

  it("D164: no vector is asked for a node it ends at: the graph with each edge stated once is well formed, and so is an entry whose nodes do not depend on one another", () => {
    expect("yes" in well_formed(reducedText(), registryText)).toBe(true)
    const g = JSON.parse(graphText) as { vectors: { name: string }[] }
    const r = JSON.parse(registryText) as { entries: unknown[] }
    const design = g.vectors.find((v) => v.name === "write-design")
    const both = well_formed(
      JSON.stringify({ ...g, vectors: [...g.vectors, { ...design, name: "write-design-and-tests", function: { term: "reference", name: "write-design-and-tests" } }] }),
      JSON.stringify({ ...r, entries: [...r.entries, { name: "write-design-and-tests", writes: ["design", "tests"], purpose: "Writes the design and the tests: it fits a test.", definition: { term: "session" } }] })
    )
    expect("yes" in both, JSON.stringify("no" in both ? both.no : [])).toBe(true)
  })

  it("D164: the requirements depend on the intent, and the code on the requirements, so that an edit of the intent reopens the requirements, and one of the requirements the code: with each edge stated once, neither is reopened", () => {
    expect(reopened(reduced(), "intent", method.byDefault)).toEqual(["write-intent", "write-product"])
    expect(reopened(reduced(), "requirements", method.byDefault)).toEqual(["write-requirements", "write-design", "write-tests"])
  })

  it("D164: acceptance is recursive: where the user said no to the intent, with no content changed, every vector that writes what depends on it is open, and a design ticket does not compose", () => {
    const s = built(method, "simplest", {}, method.byDefault)
    const intent = s.records?.get("intent")?.answer
    if (intent === undefined) throw new Error("no answer at the intent")
    const refused = { ...s, records: new Map([...(s.records ?? []), ["intent", { answer: { ...intent, says: "no" as const } }]]) }
    expect(method.byDefault.filter((name) => open(method, vector(name), refused))).toEqual(method.byDefault)
    // On the graph with each edge stated once, the design rests on the requirements alone, whose own answer stands: an edit of the intent still holds it.
    const ticket = { path: ".ai-workspace/tickets/active/t.md", identity: "t1", asked: "a1", enters: "design" }
    const edited = built(reduced(), ticket, { intent: "intent-2" })
    const why = "which is neither accepted nor written before it: the user has not accepted intent as it now stands; enter at intent"
    expect(composes(reduced(), fieldsOf(["write-design", "write-code"], "design", "code"), edited)).toEqual({
      result: "no",
      found: `write-design rests on requirements, ${why}; write-code rests on tests, ${why}`
    })
    expect(next(reduced(), inducted(reduced(), edited, ["write-design", "write-code"], "design", "code"))?.name).toBe("induct-ticket")
  })

  it("the purpose of each entry a term may name says when it fits, and none is a mode of another; the induction's says small work never needs one", () => {
    for (const e of method.registry.entries) {
      expect(e.purpose, e.name).toContain("fits")
      if (e.name === "induct-ticket") expect(e.purpose).toContain("Small work never needs one.")
      else expect(e.purpose, e.name).not.toMatch(/small/i)
    }
  })

  it("the registry's default term, which the simplest ticket, main and a ticket with no term are built by, is the six single-asset functions, each after those that write what it rests on", () => {
    expect(method.byDefault).toEqual(["write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"])
  })

  it("D168: only the first vector declares results of its own; what must be true of each other asset is its node's, and none clips the work to where the ticket ends", () => {
    for (const v of method.graph.vectors) expect(v.result === undefined, v.name).toBe(v.first !== true)
    for (const n of method.graph.nodes) {
      expect(n.result.length, n.name).toBeGreaterThan(0)
      expect(n.result.some((r) => /enters|ends|left as it is/.test(r)), n.name).toBe(false)
    }
  })

  it("the specification ends in the user's one decision and has no evaluation and no check", () => {
    expect(vector("write-specification").decision).toEqual({})
    expect(vector("write-specification").evaluation).toBeUndefined()
    expect(checksOf(method, vector("write-specification"))).toEqual([])
  })

  it("the build rests on the requirements, runs the checks of the design, the tests and the code, as the vectors that write each alone do, and has one evaluation and the user's decision", () => {
    const build = vector("write-build")
    expect(arrow("write-build")).toEqual([["design", "tests", "code"], ["requirements"]])
    expect(checksOf(method, build)).toEqual(["write-design", "write-tests", "write-code"].flatMap((name) => checksOf(method, vector(name))))
    expect(against(method, build)).toEqual(["requirements"])
    expect(build.decision).toEqual({})
    expect(build.frames).toEqual({ work: { name: "write-build", revision: 1 }, evaluation: { name: "judge-build", revision: 1 } })
  })

  it("the one evaluation judges, among its grounds, whether the tests exercise the product as a user would and were not bent to fit the code: a result of the tests, whichever vector writes them (D168)", () => {
    const tests = method.graph.nodes.find((n) => n.name === "tests")
    expect(tests?.result.some((r) => r.includes("as a user of it would") && r.includes("not bent to fit the code"))).toBe(true)
  })
})
