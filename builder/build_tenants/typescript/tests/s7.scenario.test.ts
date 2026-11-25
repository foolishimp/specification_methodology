/**
 * Scenario S7, a session writes outside its vector: S1 under way with a
 * stand-in that, during the code step, changes an accepted requirement and
 * writes a scratch file in a place the graph does not name. S1's term is the
 * specification and then the build, so the code step is the build's (REQ-METHOD-006). The user asks where the
 * work stands when the run ends, says yes to what changed, then starts a run.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007 REQ-ALG-008 REQ-ALG-012 REQ-METHOD-006
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const CHANGED = "# Requirements\n\n### REQ-HELLO-001 Say hello\n\nRun with no arguments, the program prints the line `hello, world!` and exits\nwith code 0.\n"
const SCRATCH = "notes the session kept for itself\n"
let ws: Workspace
let ticket = ""
let waited: Said
let shown: Said
let ruled: Said
let next: Said
let fromWaited = 0
let nextFrom = 0
let log: LogEntry[] = []
let headBefore = ""

beforeAll(async () => {
  ws = new Workspace(build())
  const fixtures = fixturesLike((f) => {
    write(join(f, "write-build", "work", "files", "specification", "requirements", "HELLO.md"), CHANGED)
    write(join(f, "write-build", "work", "files", "scratch", "notes.txt"), SCRATCH)
  })
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  fromWaited = ws.log().length
  headBefore = ws.git(["rev-parse", `stdo/${ticket}`]).trim()
  waited = await ws.run(fixtures)
  shown = await ws.show()
  ruled = await ws.answer("yes")
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

  it("the run read no verdict, ran no check, committed nothing of the step and ended waiting for the user's ruling (REQ-FLOW-005 step 3)", () => {
    expect(waited.code).toBe(0)
    expect(waited.out).toContain("waits for your ruling on what changed while the session on write-build worked")
    const run = log.slice(fromWaited, nextFrom)
    expect(run.some((e) => e.event === "verdict read")).toBe(false)
    expect(run.some((e) => e.event === "check run")).toBe(false)
    expect(run.filter((e) => e.event === "commit made").map((e) => e.why)).not.toContain("the result of the step: the user is asked")
    expect(run.some((e) => e.event === "commit made" && String(e.why).startsWith("the result of the step"))).toBe(false)
    expect(run.find((e) => e.event === "run ended")?.ending).toBe("waiting")
  })

  it("it named the changed requirement as changed and the scratch file as added, each as changed while the session worked, by the session or the user (REQ-FLOW-006)", () => {
    expect(waited.out).toMatch(/specification\/requirements\/HELLO\.md \(changed\)/)
    expect(waited.out).toMatch(/scratch\/notes\.txt \(added\)/)
    expect(waited.out).toContain("changed while the session worked; it may have been the session or you")
    expect(waited.out).not.toContain("the session changed")
  })

  it("asked where the work stood, the framework gave the same question (REQ-ALG-012)", () => {
    expect(shown.out).toContain("waits for your ruling on what changed while the session on write-build worked")
    expect(shown.out).toContain("scratch/notes.txt (added)")
    expect(shown.out).toContain("specification/requirements/HELLO.md (changed)")
    expect(ruled.code).toBe(0)
  })

  it("neither file was put back: the framework puts nothing right (REQ-ALG-008 law 4)", () => {
    expect(readFileSync(ws.path("specification", "requirements", "HELLO.md"), "utf8")).toBe(CHANGED)
    expect(readFileSync(ws.path("scratch", "notes.txt"), "utf8")).toBe(SCRATCH)
  })

  it("the next run committed both, and asked the user to accept the specification, which holds the requirements, again before any later step", () => {
    expect(next.code).toBe(0)
    const tip = `stdo/${ticket}`
    expect(ws.git(["show", `${tip}:./specification/requirements/HELLO.md`])).toBe(CHANGED)
    expect(ws.git(["show", `${tip}:./scratch/notes.txt`])).toBe(SCRATCH)
    expect(ws.git(["rev-parse", tip]).trim()).not.toBe(headBefore)
    expect(next.out).toContain("waits for your answer on write-specification")
    const run = log.slice(nextFrom)
    expect(run.some((e) => e.event === "session started")).toBe(false)
    expect(run.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-specification"])
  })

  it("the log holds that the user was asked on what changed, with how many files were named, and names none of them (REQ-FLOW-007)", () => {
    const asked = log.slice(fromWaited, nextFrom).filter((e) => e.event === "user asked")
    expect(asked.map((e) => e.named)).toEqual([2])
    expect(JSON.stringify(asked)).not.toContain("notes.txt")
    expect(JSON.stringify(asked)).not.toContain("HELLO.md")
  })
})
