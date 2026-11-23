/**
 * Scenario S5, a step that does not close: S1 under way with a stand-in whose
 * code step returns code that fails the tests. S1's term is the specification and then the build, so the code
 * is written in the build's step (REQ-METHOD-006). The user starts a run and,
 * when it ends, asks where the work stands. No evaluation is started while a
 * check of the build says no (D173).
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-005 REQ-ALG-009 REQ-ALG-012 REQ-METHOD-006
 */
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, S1_TICKET, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const FAILING = "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001.\nprintf 'hello\\n'\n"
let ws: Workspace
let ticket = ""
let ran: Said
let shown: Said
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  const fixtures = fixturesLike((f) => {
    write(join(f, "write-build", "work", "files", "build_tenants", "main", "code", "hello.sh"), FAILING)
  })
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  ran = await ws.run(fixtures)
  shown = await ws.show()
  log = ws.log()
}, 180_000)

afterAll(clean)

describe("S5 A step that does not close", () => {
  it("the code step's working session was started twice and failed the same checks both times", () => {
    const attempts = log.filter((e) => e.event === "session started" && e.vector === "write-build" && e.kind === "work")
    expect(attempts).toHaveLength(2)
    const failed = log.filter((e) => (e.event === "check run" && e.result !== "yes") && e.vector === "write-build").map((e) => e.check)
    expect(failed).toEqual(["the tests pass", "the tests pass"])
  })

  it("D173: no evaluation of the build was started while a check of it said no; the step went back to a working session, whose packet names what the checks found", () => {
    expect(log.filter((e) => e.event === "session started" && e.vector === "write-build").map((e) => e.kind)).toEqual(["work", "work"])
    expect(readFileSync(ws.checkout(ticket, ".stdo-builder", "local", "briefs", "write-build.work.md"), "utf8")).toContain(".stdo-builder/local/found/write-build.md")
  })

  it("the run then ended as stopped, and said which vector could not close and which check did not pass", () => {
    expect(ran.code).toBe(1)
    expect(ran.out).toContain("The run stopped")
    // Neither working session counts as an attempt: no evaluation said no (REQ-FLOW-005, REQ-PARAM-003).
    expect(ran.out).toContain("write-build could not close: the same number of checks failed twice in a row")
    // No verdict stands, since none is given over a check that says no (D173).
    expect(ran.out).toContain("What did not pass: the tests pass, verdict.")
    expect(log.at(-1)).toMatchObject({ event: "run ended", ending: "stopped", vector: "write-build" })
  })

  it("no session wrote a ticket", () => {
    const placed = readFileSync(join(S1_FIXTURES, "induct-ticket", "work", "append"), "utf8")
    // The framework's part of the ticket is the framework's (REQ-FLOW-001, REQ-FLOW-004); the rest is the user's words and the induction's.
    const written = ws.read(".stdo-builder", "local", "checkouts", ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
    expect((written ?? "").split("\n").filter((l) => !l.startsWith("- framework: ")).join("\n")).toBe(`${S1_TICKET}\n${placed}`)
    const tickets = ws.git(["-C", ws.checkout(ticket), "ls-files", ".ai-workspace"]).trim().split("\n")
    expect(tickets).toEqual([`.ai-workspace/tickets/active/${ticket}.md`])
  })

  it("the ticket is still active, and the framework gives its state as held up", () => {
    expect(ws.board()).toEqual({ backlog: [], active: [ticket], done: [] })
    expect(shown.code).toBe(0)
    expect(shown.out).toContain(`- ${ticket}: active, held up at write-build: the tests pass did not pass`)
  })

  it("the file the stand-in wrote is still there, unchanged", () => {
    expect(readFileSync(ws.checkout(ticket, "build_tenants", "main", "code", "hello.sh"), "utf8")).toBe(FAILING)
  })
})
