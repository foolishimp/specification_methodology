/**
 * The review of 21 November, BDR-01: acceptance does not survive a change to
 * what acceptance means. On the workspace S1 left, the user first changes only
 * the revision of the code's evaluating frame in the workspace's graph and
 * starts a run: the frame is not what the node declares, so nothing is open
 * and the run is refused with nothing to build (D168). Then the user adds a
 * result to the code node, with no byte of the product changed, and starts a
 * run: the code's verdict and the user's answer no longer stand, so the run
 * judges the code again and asks the user, and opens neither the design nor
 * the tests. The stand-in has the code's evaluation alone; a session the
 * framework should not start finds no fixed files, fails, and shows in the
 * log.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-004 REQ-GRAPH-003
 */
import { rmSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, onMain, S1_ASSETS, S1_FIXTURES, s1Whole, since, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const CLAUSE = "The code prints nothing on standard error."
const GRAPH = [".stdo-builder", "graph.json"] as const

/** The graph in the workspace, changed by `change` and written back in its one form. */
const changeGraph = (ws: Workspace, change: (g: { nodes: { name: string; result: string[] }[]; vectors: { name: string; frames?: { evaluation?: { revision: number } } }[] }) => void): void => {
  const g = JSON.parse(ws.read(...GRAPH) ?? "") as Parameters<typeof change>[0]
  change(g)
  writeFileSync(ws.path(...GRAPH), `${JSON.stringify(g, null, 2)}\n`)
}

/** The product's assets on main, by path, with git's identity of each. */
const product = (ws: Workspace): ReadonlyMap<string, string> => new Map(S1_ASSETS.map((p) => [p, ws.git(["rev-parse", `main:${p}`]).trim()]))

let ws: Workspace
let before: ReadonlyMap<string, string>
let afterFrame: Said
let asked: Said
let answered: Said
let merged: Said
let idle: Said
let log: readonly LogEntry[] = []
let frameFrom = 0
let clauseFrom = 0

beforeAll(async () => {
  ws = new Workspace(build())
  await s1Whole(ws, S1_FIXTURES)
  before = product(ws)
  const codeEvaluation = fixturesLike((f) => {
    for (const vector of ["induct-ticket", "write-specification", "write-build", "write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]) {
      for (const kind of ["work", "evaluation"]) if (`${vector}/${kind}` !== "write-code/evaluation") rmSync(join(f, vector, kind), { recursive: true, force: true })
    }
  })
  frameFrom = ws.log().length
  changeGraph(ws, (g) => {
    const frame = g.vectors.find((v) => v.name === "write-code")?.frames?.evaluation
    if (frame === undefined) throw new Error("write-code declares no evaluating frame")
    frame.revision += 1
  })
  afterFrame = await ws.run(codeEvaluation)
  clauseFrom = ws.log().length
  changeGraph(ws, (g) => {
    g.nodes.find((n) => n.name === "code")?.result.push(CLAUSE)
  })
  asked = await ws.run(codeEvaluation)
  answered = await ws.answer("yes")
  merged = await ws.run(codeEvaluation)
  idle = await ws.run(codeEvaluation)
  log = ws.log()
}, 300_000)

afterAll(clean)

const sessions = (entries: readonly LogEntry[]) => entries.filter((e) => e.event === "session started").map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)

describe("acceptance stands on what the node declares (BDR-01, D168)", () => {
  it("the control: a new revision of the code's evaluating frame alone opens nothing, and the run is refused with nothing to build", () => {
    expect(afterFrame.code, afterFrame.out).toBe(2)
    expect(afterFrame.out).toContain("there is nothing to build")
    expect(sessions(log.slice(frameFrom, clauseFrom))).toEqual([])
  })

  it("a result added to the code, with no byte of the product changed: the run does not end with nothing to build; it judges the code again and asks the user", () => {
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).not.toContain("there is nothing to build")
    expect(asked.out).toContain("waits for your answer on write-code")
    expect(sessions(since(log, clauseFrom))).toEqual(["write-code evaluation"])
    expect(log.filter((e) => e.event === "session failed")).toEqual([])
  })

  it("the design and the tests are not reopened: the user is asked of the code alone, and no session is started on them", () => {
    const after = since(log, clauseFrom)
    expect(after.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-code"])
    expect(after.some((e) => e.event === "session started" && (e.vector === "write-design" || e.vector === "write-tests"))).toBe(false)
  })

  it("the user's yes closes it: the next run merges, the one after has nothing to build, and the product's bytes are as S1 left them", () => {
    expect(answered.code, answered.out).toBe(0)
    expect(merged.code, merged.out).toBe(0)
    expect(idle.code, idle.out).toBe(2)
    expect(idle.out).toContain("there is nothing to build")
    expect(product(ws)).toEqual(before)
    expect(onMain(ws)).toEqual(expect.arrayContaining([...S1_ASSETS]))
  })
})
