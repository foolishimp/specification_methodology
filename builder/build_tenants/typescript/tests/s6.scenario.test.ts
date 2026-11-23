/**
 * Scenario S6, a second graph, the registry and an inner workflow: in an empty
 * folder the user sets up a governed product, lists the registry, puts in
 * place a second copy of a graph of three nodes that names a graph function
 * not in its registry and starts a run, whose refusal names where the release
 * keeps the method's own graph and registry (D176), then puts the first copy
 * in place and starts a run. One vector of the graph is carried out through an
 * inner workflow, a graph function of the registry (REQ-FLOW-005 step 2). Each line
 * of "At the end" is one test; REQ-GRAPH-006's acceptance is shown on the
 * same graph.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-GRAPH-004 REQ-GRAPH-005 REQ-GRAPH-006 REQ-FLOW-003 REQ-FLOW-005 REQ-ALG-002
 */
import { createHash } from "node:crypto"
import { cpSync, readdirSync, readFileSync, rmSync } from "node:fs"
import { dirname, join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, onMain, temporary, tenant, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const GRAPHS = join(tenant, "tests", "graphs")
const S6_FIXTURES = join(tenant, "tests", "fixtures", "stand-in", "s6")
const METHOD_REGISTRY = JSON.parse(readFileSync(join(tenant, "src", "method", "registry.json"), "utf8")) as { entries: { name: string; purpose: string }[] }
const S6_REGISTRY = JSON.parse(readFileSync(join(GRAPHS, "s6.registry.json"), "utf8")) as { entries: { name: string; purpose: string }[] }

/** The content identity of the built framework: every file of the build, by path and content. */
const frameworkIdentity = (cli: string): string => {
  const root = dirname(dirname(dirname(cli)))
  const hash = createHash("sha256")
  for (const f of readdirSync(root, { recursive: true }).map(String).sort()) {
    const path = join(root, f)
    try {
      hash.update(`${f}\n`).update(readFileSync(path))
    } catch {
      // A folder.
    }
  }
  return hash.digest("hex")
}

/** Puts a graph and its registry in place on main, by hand, as the user does. */
const putInPlace = (ws: Workspace, graph: string): void => {
  cpSync(join(GRAPHS, graph), ws.path(".stdo-builder", "graph.json"))
  cpSync(join(GRAPHS, "s6.registry.json"), ws.path(".stdo-builder", "registry.json"))
}

let cli = ""
let framework = ""
let ws: Workspace
let listed: Said
let listedAfter: Said
let firstRun: Said
let shownRefused: Said
let secondRun: Said
let log: readonly LogEntry[] = []
let fromFirst = 0
let fromSecond = 0

beforeAll(async () => {
  cli = build()
  framework = frameworkIdentity(cli)
  ws = new Workspace(cli)
  expect((await ws.setup()).code).toBe(0)
  listed = await ws.command(["registry", ws.root])
  putInPlace(ws, "s6-unlisted.graph.json")
  fromFirst = ws.log().length
  firstRun = await ws.run(S6_FIXTURES)
  shownRefused = await ws.show()
  putInPlace(ws, "s6.graph.json")
  fromSecond = ws.log().length
  secondRun = await ws.run(S6_FIXTURES)
  listedAfter = await ws.command(["registry", ws.root])
  log = ws.log()
}, 180_000)

afterAll(clean)

describe("S6 A second graph, the registry and an inner workflow", () => {
  it("the user lists the registry and can read each entry: its name and what it is for", () => {
    expect(listed.code, listed.out).toBe(0)
    for (const e of METHOD_REGISTRY.entries) expect(listed.out).toContain(`- ${e.name}: ${e.purpose}`)
    expect(listedAfter.code, listedAfter.out).toBe(0)
    expect(listedAfter.out).toContain(`The registry holds ${S6_REGISTRY.entries.length} graph functions`)
    for (const e of S6_REGISTRY.entries) expect(listedAfter.out).toContain(`- ${e.name}: ${e.purpose}`)
  })

  it("the first run was refused before any step, with the reason", () => {
    expect(firstRun.code, firstRun.out).toBe(2)
    expect(firstRun.out).toContain("The run is refused before any step: the governing graph is not well formed")
    expect(firstRun.out).toContain("reference 'outline-it': names a graph function that is not in the registry")
    const during = log.slice(fromFirst, fromSecond)
    expect(during.filter((e) => e.event === "run ended").map((e) => [e.ending, e.why])).toEqual([["refused", "not well formed"]])
    expect(during.filter((e) => e.event === "session started" || e.event === "commit made" || e.event === "ticket pulled")).toEqual([])
  })

  it("D176: the refusal names where the release keeps the method's own graph and registry, on a run and on show", () => {
    const method = join(dirname(dirname(cli)), "method")
    const named = `The method's own graph and registry of this release are at ${join(method, "graph.json")} and ${join(method, "registry.json")}; to work by them, put them in place at .stdo-builder/graph.json and .stdo-builder/registry.json.`
    expect(firstRun.out).toContain(named)
    expect(shownRefused.code, shownRefused.out).toBe(2)
    expect(shownRefused.out).toContain(named)
    for (const f of ["graph.json", "registry.json"]) expect(readFileSync(join(method, f), "utf8"), f).toBe(readFileSync(join(tenant, "src", "method", f), "utf8"))
  })

  it("the second reached the three nodes", () => {
    expect(secondRun.code, secondRun.out).toBe(0)
    expect(secondRun.out).toContain("is done")
    const files = onMain(ws)
    for (const path of ["plan.md", "drafts/draft.md", "text.md"]) expect(files, path).toContain(path)
    const after = log.slice(fromSecond)
    const closed = after.filter((e) => e.event === "vector closed").map((e) => e.vector)
    expect(closed).toEqual(["make-plan", "write-draft", "polish-draft", "make-text"])
  })

  it("the inner workflow was run in its vector's place, and each of its steps appears in the event log as any other (REQ-GRAPH-006)", () => {
    const after = log.slice(fromSecond)
    expect(after.filter((e) => e.event === "session started").map((e) => [e.vector, e.kind])).toEqual([["make-plan", "work"], ["write-draft", "work"], ["polish-draft", "work"]])
    for (const v of ["write-draft", "polish-draft"]) {
      expect(after.some((e) => e.event === "session returned" && e.vector === v), v).toBe(true)
      expect(after.some((e) => e.event === "commit made" && e.vector === v), v).toBe(true)
    }
    // The draft declares no check; the text, which the polish writes, does.
    expect(after.some((e) => (e.event === "check run" && e.result === "yes") && e.vector === "polish-draft")).toBe(true)
    // The outer vector is closed by the checks of the nodes it writes, after its inner vectors.
    const outer = after.findIndex((e) => (e.event === "check run" && e.result === "yes") && e.vector === "make-text" && e.check === "the text says it follows the plan")
    const inner = after.findIndex((e) => e.event === "vector closed" && e.vector === "polish-draft")
    expect(outer).toBeGreaterThan(inner)
  })

  it("the framework was not changed", () => {
    expect(frameworkIdentity(cli)).toBe(framework)
  })
})

/** A workspace with the S6 graph in place, and the S6 fixtures as `change` leaves them; the run on it. */
async function s6With(change: (fixtures: string) => void): Promise<{ readonly ran: Said; readonly log: readonly LogEntry[] }> {
  const w = new Workspace(cli)
  await w.setup()
  putInPlace(w, "s6.graph.json")
  const fixtures = join(temporary("stdo-builder-fx-"), "fixtures")
  cpSync(S6_FIXTURES, fixtures, { recursive: true })
  change(fixtures)
  const from = w.log().length
  const ran = await w.run(fixtures)
  return { ran, log: w.log().slice(from) }
}

describe("REQ-GRAPH-006 an outer vector is closed only by the nodes it writes", () => {
  let unpolished: { readonly ran: Said; readonly log: readonly LogEntry[] }
  let undrafted: { readonly ran: Said; readonly log: readonly LogEntry[] }
  beforeAll(async () => {
    unpolished = await s6With((f) => write(join(f, "polish-draft", "work", "files", "text.md"), "# Text\n\nThe product is a greeter, for people at a terminal.\n"))
    undrafted = await s6With((f) => rmSync(join(f, "write-draft"), { recursive: true }))
  }, 180_000)

  it("where a check of a node the outer vector writes says no, the inner vector that writes the node does not close, and neither does the outer vector", () => {
    expect(unpolished.ran.code, unpolished.ran.out).toBe(1)
    expect(unpolished.ran.out).toContain("at polish-draft: polish-draft could not close: the same number of checks failed twice in a row")
    expect(unpolished.ran.out).toContain("What did not pass: the text says it follows the plan.")
    const closed = unpolished.log.filter((e) => e.event === "vector closed").map((e) => e.vector)
    expect(closed).toEqual(["make-plan", "write-draft"])
    expect(unpolished.log.filter((e) => e.event === "vector left open").map((e) => e.vector)).toEqual(["polish-draft", "polish-draft"])
  })

  it("an inner vector that cannot close stops the run, which names the inner vector", () => {
    expect(undrafted.ran.code, undrafted.ran.out).toBe(1)
    expect(undrafted.ran.out).toContain("The run stopped on the ticket")
    expect(undrafted.ran.out).toContain(", at write-draft: the session on write-draft failed twice in a row")
    expect(undrafted.log.filter((e) => e.event === "session failed").map((e) => e.vector)).toEqual(["write-draft", "write-draft"])
    expect(undrafted.log.at(-1)).toMatchObject({ event: "run ended", ending: "stopped", vector: "write-draft" })
  })
})
