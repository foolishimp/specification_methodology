/**
 * Where a node's resolution is read, and what it stands on (REQ-ALG-004,
 * D203), driven through the command-line program with the stand-in agent, as
 * scenario S1 is. A resolution whose commit git does not hold counts as
 * absent, and the user is asked again. A no in the branch's ticket outranks
 * the yes of a done ticket on the same content.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-004 REQ-FLOW-004
 */
import { readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, resolvedOnMain, S1_FIXTURES, s1ToRequirements, s1Whole, write, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

afterAll(clean)

/** A commit git does not hold. */
const NOT_HELD = "e".repeat(40)

/** The sessions started, in order, as `<vector> <kind>`. */
const sessionsIn = (log: readonly LogEntry[]): readonly string[] =>
  log.filter((e) => e.event === "session started").map((e) => `${e.vector ?? ""} ${e.kind ?? ""}`)

/** The ticket in its checkout, with `change` made to it by hand. */
const byHand = (ws: Workspace, ticket: string, change: (text: string) => string): void => {
  const path = ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)
  write(path, change(readFileSync(path, "utf8")))
}

describe("REQ-ALG-004 acceptance 6: a resolution whose commit git no longer holds counts as absent, and the user is asked again", () => {
  let ws: Workspace
  let again: Said
  let log: readonly LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(build())
    const { ticket } = await s1ToRequirements(ws, S1_FIXTURES)
    // The user's yes to the requirements now names a commit git does not hold.
    byHand(ws, ticket, (text) => text.replace(/^(- framework: resolved user yes at requirements on )[0-9a-f]{40}$/m, `$1${NOT_HELD}`))
    const from = ws.log().length
    again = await ws.run(S1_FIXTURES)
    log = ws.log().slice(from)
  }, 180_000)

  it("the run asks the user again on the specification, and builds nothing that rests on it", () => {
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("waits for your answer on write-specification")
    expect(sessionsIn(log).some((s) => s.startsWith("write-build "))).toBe(false)
  })
})

describe("REQ-ALG-004 acceptance 5: the user says yes to the requirements in one ticket, and no to the same content in the next: the requirements are not accepted", () => {
  let ws: Workspace
  let later = ""
  let ran: Said
  let confirmed: Said
  let log: readonly LogEntry[] = []

  beforeAll(async () => {
    ws = new Workspace(build())
    await s1Whole(ws, S1_FIXTURES)
    const yes = resolvedOnMain(ws, "requirements")[0]
    later = /The ticket (\S+) is written/.exec((await ws.ticket("Hello's code says nothing of where it reads from. Say so in its comment.")).out)?.[1] ?? ""
    // The induction at the code and the code alone; no other session has files, so any other fails.
    const fixtures = fixturesLike((f) => {
      for (const vector of ["write-specification", "write-build"]) rmSync(join(f, vector), { recursive: true, force: true })
      write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "bug", klass: "realization_refactor", enters: "code", ends: "code", scope: "the greeting's code", term: ["write-code"] }))
    })
    await ws.run(fixtures)
    confirmed = await ws.answer("yes")
    // In the next ticket, the user's no to the requirements, on the content the done ticket's yes was given on.
    byHand(ws, later, (text) => `${text}- framework: resolved user no at requirements on ${yes?.commit ?? ""}; reason not as I want it\n`)
    const from = ws.log().length
    ran = await ws.run(fixtures)
    log = ws.log().slice(from)
  }, 240_000)

  it("the done ticket said yes to the requirements on that content", () => {
    expect(resolvedOnMain(ws, "requirements").length).toBeGreaterThan(0)
    expect(later).not.toBe("")
  })

  it("the requirements are not accepted: the code, which rests on them, is not built and the user is not asked on it", () => {
    expect(sessionsIn(log).some((s) => s.startsWith("write-code "))).toBe(false)
    expect(ran.out).not.toContain("waits for your answer on write-code")
    expect(confirmed.code, confirmed.out).toBe(0)
    expect(ran.out).toContain("at induct-ticket")
    expect(readFileSync(ws.checkout(later, ".stdo-builder", "local", "found", "induct-ticket.md"), "utf8")).toContain("the user has not accepted requirements as it now stands")
  })
})
