/**
 * REQ-FLOW-005, an evaluation that cannot judge (D90). S1 runs to the
 * specification the user accepted. S1's term is the specification and then
 * the build (REQ-METHOD-006): the build's evaluating session then writes a verdict that says it cannot judge,
 * with why in its findings. The run stops and names where the findings are,
 * and the log holds none of the evaluator's words. The next run makes the
 * evaluation again, and starts no new working session on the build, whose
 * checks pass.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-005 REQ-FLOW-007 REQ-ALG-004
 */
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const WHY = "The requirements name a terminal the design cannot reach: 7c41e2."
const FINDINGS = "build_tenants/main/evaluations/build/findings.md"
let ws: Workspace
let ticket = ""
let first: Said
let again: Said
let firstLog: LogEntry[] = []
let againLog: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  const cannot = fixturesLike((f) => {
    const evaluations = join(f, "write-build", "evaluation", "files", "build_tenants", "main", "evaluations", "build")
    write(join(evaluations, "verdict.json"), "{\"verdict\": \"cannot\"}\n")
    write(join(evaluations, "findings.md"), `# Findings on the build\n\n${WHY}\n`)
  })
  ticket = (await s1ToRequirements(ws, cannot)).ticket
  const from = ws.log().length
  first = await ws.run(cannot)
  const middle = ws.log().length
  firstLog = ws.log().slice(from, middle)
  again = await ws.run(cannot)
  againLog = ws.log().slice(middle)
}, 180_000)

afterAll(clean)

describe("REQ-FLOW-005 an evaluating session says that it cannot judge", () => {
  it("the run stops and names where its findings are", () => {
    expect(first.code, first.out).toBe(1)
    expect(first.out).toContain(`the evaluation of write-build cannot judge; why is in its findings at .stdo-builder/local/checkouts/${ticket}/${FINDINGS}`)
    expect(firstLog.some((e) => e.event === "vector closed" && e.vector === "write-build")).toBe(false)
    expect(firstLog.some((e) => e.event === "user asked")).toBe(false)
  })

  it("the event log holds none of the evaluator's words", () => {
    expect(JSON.stringify(firstLog)).not.toContain("7c41e2")
  })

  it("the next run makes the evaluation again, with no new working session on the build", () => {
    const started = againLog.filter((e) => e.event === "session started" && e.vector === "write-build").map((e) => e.kind)
    expect(started).toEqual(["evaluation"])
    expect(again.code, again.out).toBe(1)
    expect(again.out).toContain("the evaluation of write-build cannot judge")
  })
})
