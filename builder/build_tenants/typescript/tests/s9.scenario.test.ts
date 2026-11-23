/**
 * Scenario S9, build again from the specification: the workspace S1 left; the
 * user deletes the code, starts a run and answers each question. The
 * stand-in's code this time differs from the first by a comment, as a new
 * session's would.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-003 REQ-FLOW-004 REQ-ALG-010
 */
import { rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1Whole, testsPass, ticketFields, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

let ws: Workspace
let first = ""
let from = 0
const said: Said[] = []
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  first = (await s1Whole(ws, S1_FIXTURES)).ticket
  rmSync(ws.path("build_tenants", "main", "code"), { recursive: true })
  const again = fixturesLike((f) => {
    write(join(f, "write-code", "work", "files", "build_tenants", "main", "code", "hello.sh"), "#!/bin/sh\n# Hello, built again. Carries out REQ-HELLO-001.\nprintf 'hello, world\\n'\n")
  })
  from = ws.log().length
  said.push(await ws.run(again), await ws.answer("yes"), await ws.run(again))
  log = ws.log().slice(from)
}, 180_000)

afterAll(clean)

describe("S9 Build again from the specification", () => {
  it("the code is there again and passes the tests that passed before", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0])
    expect(ws.git(["ls-tree", "-r", "--name-only", "main", "build_tenants/main/code"]).trim()).toBe("build_tenants/main/code/hello.sh")
    expect(ws.git(["diff", "--quiet", `stdo/${first}`, "main", "--", "build_tenants/main/tests"])).toBe("")
    expect(testsPass(ws)).toBe(true)
  })

  it("the only vector a session was started on is the one that writes the code", () => {
    const on = new Set(log.filter((e) => e.event === "session started").map((e) => e.vector))
    expect([...on]).toEqual(["write-code"])
  })

  it("the user was asked only to accept the built product", () => {
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-code"])
  })

  it("the run wrote the simplest ticket, which lies in the done lane on main", () => {
    const board = ws.board()
    expect(board.backlog).toEqual([])
    expect(board.active).toEqual([])
    expect(board.done).toHaveLength(2)
    const simplest = board.done.filter((t) => t !== first)
    expect(simplest).toHaveLength(1)
    expect(ticketFields(ws.git(["show", `main:.ai-workspace/tickets/completed/${simplest[0]}.md`])).get("simplest")).toBe("yes")
    expect(log.some((e) => e.event === "commit made" && e.why === "the simplest ticket written" && e.ticket === simplest[0])).toBe(true)
  })
})
