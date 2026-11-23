/**
 * Nothing is orphaned, and a requirement put off is not orphaned
 * (REQ-METHOD-005): every requirement is named in the design, in at least one
 * test and in the code, or is marked as deferred in the requirements the user
 * accepted; nothing in the design, the tests or the code names a requirement
 * that is not there.
 *
 * In two workspaces the user goes through S1 to the build, as S1 does, with
 * requirements of two: the first is S1's, and the second is named in the tests
 * alone, not in the design or the code.
 *
 * - The section of the second says it is Deferred: the design, the tests and
 *   the code are traced, nothing is orphaned and the build waits only for the
 *   user's answer. The tests name the second, which is there, so that is no
 *   ground for no.
 * - The section of the second does not say so: the second is orphaned in the
 *   design and in the code, whose checks say no, and the build does not close.
 *
 * @uses C14 C5 C6
 * @is REQ-METHOD-005 REQ-VERIFY-002
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, S1_TICKET, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const REQUIREMENTS = join("write-specification", "work", "files", "specification", "requirements", "HELLO.md")
const HELLO_TEST = join("write-build", "work", "files", "build_tenants", "main", "tests", "hello.test.sh")

/** S1's requirements with a second, whose section says Deferred where `deferred` is so. */
const requirements = (deferred: boolean): string =>
  `${readFileSync(join(S1_FIXTURES, REQUIREMENTS), "utf8")}\n### REQ-HELLO-002 Say goodbye\n\n${deferred ? "**Status**: Deferred.\n\n" : ""}Run with the argument bye, the program prints the line \`goodbye\`.\n`

/** S1's fixtures, with the requirements above and a test that names the second. */
const fixtures = (deferred: boolean): string =>
  fixturesLike((f) => {
    write(join(f, REQUIREMENTS), requirements(deferred))
    write(join(f, HELLO_TEST), `${readFileSync(join(S1_FIXTURES, HELLO_TEST), "utf8")}# REQ-HELLO-002 has no test while it is put off.\n`)
  })

interface Case {
  readonly said: readonly Said[]
  readonly last: Said
  readonly log: readonly LogEntry[]
  /** The names of the traced checks of the method's graph, by the node they read into. */
  readonly traced: ReadonlyMap<string, string>
}

/** The traced checks of a graph, by the node they read into. */
function tracedOf(graph: unknown): ReadonlyMap<string, string> {
  const out = new Map<string, string>()
  const walk = (x: unknown): void => {
    if (Array.isArray(x)) return x.forEach(walk)
    if (typeof x !== "object" || x === null) return
    const o = x as { name?: string; run?: { kind?: string; into?: string } }
    if (o.run?.kind === "traced" && o.run.into !== undefined && o.name !== undefined) out.set(o.run.into, o.name)
    Object.values(o).forEach(walk)
  }
  walk(graph)
  return out
}

/** Set-up, then S1 to the build: the ticket, three runs and the two answers between them. */
async function s1ToBuild(cli: string, deferred: boolean): Promise<Case> {
  const ws = new Workspace(cli)
  const said: Said[] = [await ws.setup()]
  const traced = tracedOf(JSON.parse(readFileSync(ws.path(".stdo-builder", "graph.json"), "utf8")))
  const fx = fixtures(deferred)
  said.push(await ws.ticket(S1_TICKET))
  said.push(await ws.run(fx), await ws.answer("yes"), await ws.run(fx), await ws.answer("yes"))
  const last = await ws.run(fx)
  return { said, last, log: ws.log(), traced }
}

const ofCheck = (c: Case, into: string, passed: boolean): readonly LogEntry[] =>
  c.log.filter((e) => e.event === "check run" && (e.result === "yes") === passed && e.vector === "write-build" && e.check === c.traced.get(into))

let deferred: Case
let due: Case

beforeAll(async () => {
  const cli = build()
  ;[deferred, due] = await Promise.all([s1ToBuild(cli, true), s1ToBuild(cli, false)])
}, 300_000)

afterAll(clean)

describe("REQ-METHOD-005 nothing is orphaned, and a requirement marked as deferred need not be traced", () => {
  it("the method's graph traces the design, the tests and the code, and every command before the build did as S1's", () => {
    for (const c of [deferred, due]) {
      expect([...c.traced.keys()].sort()).toEqual(["code", "design", "tests"])
      expect(c.said.map((s) => s.code), c.said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0])
    }
  })

  it("marked as deferred in the requirements the user accepted, a requirement the design and the code do not name leaves no check saying no, and the build waits only for the user's answer", () => {
    for (const into of ["design", "tests", "code"]) {
      expect(ofCheck(deferred, into, false), `${into}: ${deferred.last.out}`).toEqual([])
      expect(ofCheck(deferred, into, true).length, into).toBeGreaterThan(0)
    }
    expect(deferred.last.code, deferred.last.out).toBe(0)
    expect(deferred.last.out).toContain("waits for your answer on write-build")
  })

  it("a test that names a requirement put off names one that is there: the tests' check says yes", () => {
    expect(ofCheck(due, "tests", false), due.last.out).toEqual([])
    expect(ofCheck(due, "tests", true).length).toBeGreaterThan(0)
  })

  it("not marked as deferred, a requirement the design and the code do not name makes their checks say no, and the build does not close", () => {
    for (const into of ["design", "code"]) {
      const said = ofCheck(due, into, false)
      expect(said.length, `${into}: ${due.last.out}`).toBeGreaterThan(0)
      expect(said.every((e) => e.result === "no"), into).toBe(true)
    }
    expect(due.log.filter((e) => e.event === "vector closed" && e.vector === "write-build")).toEqual([])
    expect(due.log.filter((e) => e.event === "vector left open" && e.vector === "write-build").length).toBeGreaterThan(0)
    expect(due.last.code, due.last.out).toBe(1)
  })
})
