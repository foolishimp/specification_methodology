/**
 * QA-03, REQ-FLOW-004, REQ-METHOD-006: the induction closes only on a term
 * that composes. On the workspace S1 leaves, the user writes a new ticket and
 * the induction's session writes a term that begins with the build, though
 * the ticket enters at the intent. The induction does not close, the user is not asked
 * to confirm it, nothing is built and the ticket is not merged as done.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-004 REQ-FLOW-005 REQ-METHOD-006
 */
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, S1_FIXTURES, s1Whole, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

let ws: Workspace
let ticket = ""
let ran: Said
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  await s1Whole(ws, S1_FIXTURES)
  const written = await ws.ticket("Hello prints the line hello, builder instead.")
  ticket = /The ticket (\S+) is written/.exec(written.out)?.[1] ?? ""
  const backwards = fixturesLike((f) => {
    write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "intent_reprice", enters: "intent", ends: "code", scope: "the greeting", term: ["write-build", "write-specification"] }))
  })
  const from = ws.log().length
  ran = await ws.run(backwards)
  log = ws.log().slice(from)
}, 180_000)

afterAll(clean)

describe("QA-03, REQ-METHOD-006 acceptance 7: the induction does not close on a term that does not compose", () => {
  it("the induction is not closed, the user is not asked, and no other vector runs", () => {
    expect(ticket).not.toBe("")
    expect(log.some((e) => e.event === "vector closed" && e.ticket === ticket)).toBe(false)
    expect(log.some((e) => e.event === "user asked" && e.ticket === ticket)).toBe(false)
    expect(log.filter((e) => e.event === "session started").map((e) => e.vector)).toEqual(log.filter((e) => e.event === "session started").map(() => "induct-ticket"))
  })

  it("the run stops on the induction, saying why", () => {
    expect(ran.code, ran.out).toBe(1)
    expect(ran.out).toContain("induct-ticket could not close")
    expect(ran.out).toContain("the ticket's term composes")
    expect(ws.board().done).not.toContain(ticket)
  })
})
