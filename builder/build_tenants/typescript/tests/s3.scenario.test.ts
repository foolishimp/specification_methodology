/**
 * Scenario S3, go on without the event log: S1 stopped after the
 * specification was accepted; the user deletes the event log, asks where the
 * work stands, then starts a run and goes on as in S1.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-003 REQ-FLOW-007 REQ-ALG-012
 */
import { rmSync } from "node:fs"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { answersOf, resolvedOnMain, build, clean, onMain, S1_ASKED, S1_ASSETS, S1_FIXTURES, s1ToRequirements, testsPass, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

let ws: Workspace
let ticket = ""
const said: Said[] = []
let shown: Said
let last: Said
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  ticket = (await s1ToRequirements(ws, S1_FIXTURES)).ticket
  rmSync(ws.path(".stdo-builder", "local", "events.log"))
  shown = await ws.show()
  said.push(await ws.run(S1_FIXTURES), await ws.answer("yes"), await ws.run(S1_FIXTURES))
  last = await ws.run(S1_FIXTURES)
  log = ws.log()
}, 180_000)

afterAll(clean)

describe("S3 Go on without the event log", () => {
  it("the workspace is as S1 leaves it", async () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0])
    const files = onMain(ws)
    for (const path of S1_ASSETS) expect(files, path).toContain(path)
    for (const name of answersOf(S1_ASKED)) expect(resolvedOnMain(ws, name).length, name).toBeGreaterThan(0)
    expect(testsPass(ws)).toBe(true)
    expect(ws.board()).toEqual({ backlog: [], active: [], done: [ticket] })
    expect(await ws.gitSays(["merge-base", "--is-ancestor", `stdo/${ticket}`, "main"])).toBe(0)
    expect(last.out).toContain("there is nothing to build")
  })

  it("asked where the work stood, the framework gave the ticket's lane and what its ticket shows, and said the log was not found", () => {
    expect(shown.code, shown.out).toBe(0)
    // The lane, and what the ticket shows: its confirmation stands and nothing is asked of the user, so a run finds what it waits on (REQ-ALG-012).
    expect(shown.out).toContain(`- ${ticket}: active`)
    expect(shown.out).not.toContain("to be inducted")
    expect(shown.out).not.toContain("waits for your answer")
    expect(shown.out).toContain("a run finds what it waits on")
    expect(shown.out).toContain("The event log was not found.")
  })

  it("the run said the log was not found", () => {
    expect(said[0]?.out).toMatch(/^The event log was not found; this run starts a new one/)
  })

  it("the new log starts at that run", () => {
    expect(log[0]?.event).toBe("run started")
    expect(log[0]?.why).toContain("the event log was not found")
  })

  it("it shows no session started on a vector that was closed", () => {
    const on = new Set(log.filter((e) => e.event === "session started").map((e) => e.vector))
    // S1's term is the specification and then the build: after the specification only the build's step is left (REQ-METHOD-006).
    expect([...on].sort()).toEqual(["write-build"])
  })

  it("the user was asked for nothing the workspace already records", () => {
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-build"])
  })
})
