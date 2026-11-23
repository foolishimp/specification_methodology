/**
 * Item 5 of the ticket `261120-9636-findings-of-the-first-use-on-itself`: a
 * `traced` check leaves out the names of another product's requirements. The
 * stand-in's tests of S1 hold, beside S1's own, the requirements of a sample
 * product that a test builds, under a family S1's requirements do not have.
 * In three workspaces the user sets up, puts the method's graph back in place
 * with one change to the tests' check, and goes through S1 to the code, which
 * S1, by its term, writes in the build's step with the tests:
 *
 * - the check declares the sample product's family to be another product's:
 *   the sample's names do not make it say no, and the build waits only for
 *   the user's answer;
 * - the check declares nothing: the sample's names leave that vector open;
 * - the check declares S1's own family: the check cannot be run.
 *
 * The sample's names are put together when the test runs, so that this file
 * names no requirement Builder does not have.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-METHOD-005
 */
import { readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_TICKET, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

/** The sample product's family, and one of its names. */
const SAMPLE = "SAMPLE"
const SAMPLE_NAME = ["REQ", SAMPLE, "001"].join("-")
/** The family S1's requirements have. */
const OWN = "HELLO"

const SAMPLE_TESTS = join("write-build", "work", "files", "build_tenants", "main", "tests", "sample", "REQUIREMENTS.md")

interface TracedRun {
  kind?: string
  into?: string
  others?: readonly string[]
}

/** The name of the tests' `traced` check in a graph, and the graph with that check declaring `others`, where it is given. */
function withOthers(graph: unknown, others: readonly string[] | undefined): { readonly name: string; readonly graph: unknown } {
  let name = ""
  const walk = (x: unknown): void => {
    if (Array.isArray(x)) return x.forEach(walk)
    if (typeof x !== "object" || x === null) return
    const o = x as { name?: string; run?: TracedRun }
    if (o.run?.kind === "traced" && o.run.into === "tests") {
      name = o.name ?? ""
      if (others !== undefined) o.run.others = others
    }
    Object.values(o).forEach(walk)
  }
  walk(graph)
  return { name, graph }
}

interface Case {
  readonly check: string
  readonly said: readonly Said[]
  readonly last: Said
  readonly log: readonly LogEntry[]
}

/** Set-up; the graph changed by hand on main as the user does; then S1 to the code: the ticket, three runs and the two answers between them. */
async function s1ToCode(cli: string, fixtures: string, others: readonly string[] | undefined): Promise<Case> {
  const ws = new Workspace(cli)
  const said: Said[] = [await ws.setup()]
  const place = ws.path(".stdo-builder", "graph.json")
  const changed = withOthers(JSON.parse(readFileSync(place, "utf8")), others)
  writeFileSync(place, `${JSON.stringify(changed.graph, null, 2)}\n`)
  said.push(await ws.ticket(S1_TICKET))
  said.push(await ws.run(fixtures), await ws.answer("yes"), await ws.run(fixtures), await ws.answer("yes"))
  const last = await ws.run(fixtures)
  return { check: changed.name, said, last, log: ws.log() }
}

// S1's term is the specification and then the build: the tests are written and checked in the build's step (REQ-METHOD-006).
const ofTheCheck = (c: Case, passed: boolean): readonly LogEntry[] => c.log.filter((e) => e.event === "check run" && (e.result === "yes") === passed && e.vector === "write-build" && e.check === c.check)
const vectorEvents = (c: Case, event: string): readonly LogEntry[] => c.log.filter((e) => e.event === event && e.vector === "write-build")

let declared: Case
let undeclared: Case
let own: Case

beforeAll(async () => {
  const fixtures = fixturesLike((f) =>
    write(join(f, SAMPLE_TESTS), `# The requirements of a sample product that a test builds\n\n### ${SAMPLE_NAME} Say goodbye\n\nRun with no arguments, the sample prints goodbye.\n`)
  )
  const cli = build()
  ;[declared, undeclared, own] = await Promise.all([s1ToCode(cli, fixtures, [SAMPLE]), s1ToCode(cli, fixtures, undefined), s1ToCode(cli, fixtures, [OWN])])
}, 300_000)

afterAll(clean)

describe("a traced check leaves out another product's names (the ticket's item 5)", () => {
  it("the graph has the tests' traced check, and every command before the last run did as S1's", () => {
    for (const c of [declared, undeclared, own]) {
      expect(c.check).not.toBe("")
      expect(c.said.map((s) => s.code), c.said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0])
    }
  })

  it("declared to be another product's, the sample's names do not make the tests' check say no, and the build waits only for the user's answer", () => {
    expect(ofTheCheck(declared, false), declared.last.out).toEqual([])
    expect(ofTheCheck(declared, true).length).toBeGreaterThan(0)
    // The user is asked only when every other outcome of the build passes.
    expect(vectorEvents(declared, "user asked").length).toBeGreaterThan(0)
    expect(declared.last.code, declared.last.out).toBe(0)
    expect(declared.last.out).toContain("waits for your answer on write-build")
  })

  it("without the declaration, the sample's names leave the tests' vector open", () => {
    const said = ofTheCheck(undeclared, false)
    expect(said.length, undeclared.last.out).toBeGreaterThan(0)
    expect(said.every((e) => e.result === "no")).toBe(true)
    expect(vectorEvents(undeclared, "vector left open").length).toBeGreaterThan(0)
    expect(vectorEvents(undeclared, "vector closed")).toEqual([])
    expect(undeclared.last.code, undeclared.last.out).toBe(1)
  })

  it("a check that declares a family the requirements have to be another product's cannot be run", () => {
    const said = ofTheCheck(own, false)
    expect(said.length, own.last.out).toBeGreaterThan(0)
    expect(said.every((e) => e.result === "cannot")).toBe(true)
    expect(vectorEvents(own, "vector closed")).toEqual([])
    expect(own.last.code, own.last.out).toBe(1)
    expect(own.last.out).toContain("could not be run")
  })
})
