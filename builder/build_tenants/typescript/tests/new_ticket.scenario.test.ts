/**
 * A new ticket after an earlier one was confirmed and merged (REQ-FLOW-004,
 * its last acceptance line), driven through the command-line program with the
 * stand-in agent, as scenario S1 is. S1's ticket is confirmed and merged; the
 * user then writes a new ticket, a fault in the code, and starts a run. The
 * user has confirmed nothing on the new ticket: its first question does not
 * say that the ticket changed after the user confirmed it, and its
 * induction's packet records nothing of the ticket (REQ-ALG-007). Once the
 * user confirms it, the run builds by its term and does not ask again.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-004 REQ-ALG-007 REQ-FLOW-006 REQ-VERIFY-002 REQ-ALG-004
 */
import { readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, S1_FIXTURES, s1Whole, write, Workspace, type LogEntry, type Said, resolvedOnMain } from "./scenario_driver.js"

afterAll(clean)

/** The new ticket, in the user's words: a fault in the code. */
const FAULT = "Hello's code says nothing of where it reads from. Say in its comment that it reads no file, so it prints the same from any folder."

const FIXED = "#!/bin/sh\n# Hello. Carries out REQ-HELLO-001. It reads no file, so it prints the same from any folder.\nprintf 'hello, world\\n'\n"

/** The induction at the code and the code alone; only these sessions have fixed files, so any other fails. */
const faultFixtures = (): string =>
  fixturesLike((f) => {
    for (const vector of ["induct-ticket", "write-specification", "write-build", "write-intent", "write-product", "write-requirements", "write-design", "write-tests", "write-code"]) {
      for (const kind of ["work", "evaluation"]) if (!["induct-ticket/work", "write-code/work", "write-code/evaluation"].includes(`${vector}/${kind}`)) rmSync(join(f, vector, kind), { recursive: true, force: true })
    }
    write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "bug", klass: "realization_refactor", enters: "code", ends: "code", scope: "the greeting's code", term: ["write-code"] }))
    write(join(f, "write-code", "work", "files", "build_tenants", "main", "code", "hello.sh"), FIXED)
  })

/** The sessions started, in order, as `<vector> <kind>`. */
const sessionsIn = (log: readonly LogEntry[]): readonly string[] =>
  log.filter((e) => e.event === "session started").map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)

describe("REQ-FLOW-004: a ticket is confirmed and merged, and a new ticket is then written and pulled", () => {
  let ws: Workspace
  let earlier = ""
  let ticket = ""
  let first: Said
  let firstLog: readonly LogEntry[] = []
  let packet: readonly string[] = []
  let answered: Said
  let next: Said
  let nextLog: readonly LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(build())
    const whole = await s1Whole(ws, S1_FIXTURES)
    earlier = whole.ticket
    ticket = /The ticket (\S+) is written/.exec((await ws.ticket(FAULT)).out)?.[1] ?? ""
    const fixtures = faultFixtures()
    const from = ws.log().length
    first = await ws.run(fixtures)
    firstLog = ws.log().slice(from)
    packet = readFileSync(ws.path(".stdo-builder", "local", "briefs", "induct-ticket.work.md"), "utf8").split("\n")
    answered = await ws.answer("yes")
    const again = ws.log().length
    next = await ws.run(fixtures)
    nextLog = ws.log().slice(again)
  }, 240_000)

  it("the earlier ticket was confirmed and merged, and the new one is another ticket", () => {
    expect(ws.git(["ls-tree", "--name-only", "main", ".ai-workspace/tickets/completed/"])).toContain(`${earlier}.md`)
    expect(resolvedOnMain(ws, "induct-ticket").length).toBeGreaterThan(0)
    expect(ticket).not.toBe("")
    expect(ticket).not.toBe(earlier)
  })

  it("the first run on the new ticket inducts it in one session and asks the user to confirm it", () => {
    expect(first.code, first.out).toBe(0)
    expect(sessionsIn(firstLog)).toEqual(["induct-ticket work"])
    expect(first.out).toContain("waits for your answer on induct-ticket")
    expect(first.out).toContain("Is the ticket inducted as you want it?")
  })

  it("the first question on the new ticket does not say that the ticket changed after the user confirmed it", () => {
    expect(first.out).not.toContain("The ticket changed after you confirmed it")
    expect(first.out).not.toContain("The induction ran again")
  })

  it("REQ-ALG-007: the induction's packet records nothing of the new ticket: the user has said nothing on it", () => {
    const line = packet.find((l) => l.startsWith("- as it stands, the ticket:")) ?? ""
    expect(line).toBe("- as it stands, the ticket: there; nothing is recorded at it.")
  })

  it("REQ-FLOW-006: the user's yes is the confirmation of the new ticket: the next run builds by its term, and does not ask about the induction again", () => {
    expect(answered.code, answered.out).toBe(0)
    expect(next.code, next.out).toBe(0)
    expect(sessionsIn(nextLog)).toEqual(["write-code work", "write-code evaluation"])
    expect(next.out).toContain("waits for your answer on write-code")
    expect(next.out).not.toContain("Is the ticket inducted as you want it?")
  })

  it("REQ-ALG-004 acceptance 4: the new ticket, which changes the code alone, finds the intent, the product definition, the requirements, the design and the tests accepted by the resolutions of the done ticket", () => {
    for (const name of ["intent", "product", "requirements"]) expect(resolvedOnMain(ws, name).map((r) => r.ticket), name).toEqual([`.ai-workspace/tickets/completed/${earlier}.md`])
    for (const name of ["design", "tests"]) expect(resolvedOnMain(ws, name, "evaluation").map((r) => r.ticket), name).toEqual([`.ai-workspace/tickets/completed/${earlier}.md`])
    // No session ran on what the done ticket's resolutions accept, and the user was asked on the code alone.
    expect(sessionsIn(nextLog).every((s) => s.startsWith("write-code "))).toBe(true)
    expect(nextLog.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-code"])
  })
})
