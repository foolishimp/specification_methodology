/**
 * Scenario S7, a session writes outside its vector: S1 under way with a
 * stand-in that, during the code step, changes an accepted requirement and
 * writes a scratch file in a place the graph does not name. S1's term is the
 * specification and then the build, so the code step is the build's (REQ-METHOD-006). The user asks where the
 * work stands when the run ends, then starts a run.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-005 REQ-ALG-008 REQ-METHOD-006
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const CHANGED = "# Requirements\n\n### REQ-HELLO-001 Say hello\n\nRun with no arguments, the program prints the line `hello, world!` and exits\nwith code 0.\n"
const SCRATCH = "notes the session kept for itself\n"
let ws: Workspace
let ticket = ""
let stopped: Said
let shown: Said
let next: Said
let nextFrom = 0
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  const fixtures = fixturesLike((f) => {
    write(join(f, "write-build", "work", "files", "specification", "requirements", "HELLO.md"), CHANGED)
    write(join(f, "write-build", "work", "files", "scratch", "notes.txt"), SCRATCH)
  })
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  stopped = await ws.run(fixtures)
  shown = await ws.show()
  nextFrom = ws.log().length
  next = await ws.run(fixtures)
  log = ws.log()
}, 180_000)

afterAll(clean)

describe("S7 A session writes outside its vector", () => {
  it("the code step did not close", () => {
    expect(log.some((e) => e.event === "vector closed" && e.vector === "write-build")).toBe(false)
    expect(shown.code).toBe(0)
  })

  it("the run stopped and named the changed requirement, and not the scratch file", () => {
    expect(stopped.code).toBe(1)
    expect(stopped.out).toContain("changed protected files: specification/requirements/HELLO.md")
    expect(stopped.out).not.toContain("scratch/notes.txt")
    expect(log.find((e) => e.event === "run ended" && e.ending === "stopped")?.vector).toBe("write-build")
  })

  it("neither file was put back: the framework puts nothing right (REQ-ALG-008 law 4)", () => {
    expect(readFileSync(ws.checkout(ticket, "specification", "requirements", "HELLO.md"), "utf8")).toBe(CHANGED)
    expect(readFileSync(ws.checkout(ticket, "scratch", "notes.txt"), "utf8")).toBe(SCRATCH)
  })

  it("the next run went on from the workspace as it was, and asked the user to accept the specification, which holds the requirements, again before any later step (REQ-ALG-008 law 4)", () => {
    expect(next.code).toBe(0)
    expect(next.out).toContain("waits for your answer on write-specification")
    const run = log.slice(nextFrom)
    expect(run.some((e) => e.event === "session started")).toBe(false)
    expect(run.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-specification"])
  })
})
