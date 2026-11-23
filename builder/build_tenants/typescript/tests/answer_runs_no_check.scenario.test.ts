/**
 * Item 2 of the ticket `261120-9636-findings-of-the-first-use-on-itself`: the
 * answer runs no check. S1 is run to where it waits for the user's answer on
 * the code. The tests' run.sh, which the code's check "the tests pass" runs,
 * adds a line to a file outside the workspace each time it is run.
 *
 * The user then changes the code by hand and answers. The answer is not on the
 * content its question was asked on, so it is refused and nothing is written.
 * The next run asks again. The user answers yes, and the answer is written in
 * the ticket in its checkout, as a `resolved user` line that names a commit
 * (REQ-FLOW-006 step 3, D202). Neither
 * answer runs the tests' run.sh. The run after it ends with the work done.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-006
 */
import { existsSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1ToRequirements, temporary, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const RUN_SH = join("write-build", "work", "files", "build_tenants", "main", "tests", "run.sh")
// The build records its answer at each node it writes that the user's yes accepts: the code alone (D164).
/** The user's resolution at the code, as the ticket's framework part holds it (D202). */
const resolvedAt = (file: string): { says: string; on?: string } | undefined => {
  const line = (existsSync(file) ? readFileSync(file, "utf8") : "").split("\n").findLast((l) => l.startsWith("- framework: resolved user ") && l.includes(" at code on "))
  const m = line === undefined ? undefined : /^- framework: resolved user (yes|no) at code on (\w+)/.exec(line)
  return m === null || m === undefined ? undefined : { says: m[1] ?? "", on: m[2] ?? "" }
}
const CODE = join("build_tenants", "main", "code", "hello.sh")

let ws: Workspace
let ticket = ""
let counter = ""
const count = (): number => readFileSync(counter, "utf8").split("\n").filter((l) => l === "ran").length

let asked: Said
let ranAtQuestion = 0
let refused: Said
let ranAfterRefused = 0
let answerAfterRefused = false
let tipBefore = ""
let tipAfterRefused = ""
let askedAgain: Said
let ranBeforeAnswer = 0
let answered: Said
let ranAfterAnswer = 0
let answer: { says?: string; on?: string } = {}
let last: Said
let log: readonly LogEntry[] = []

beforeAll(async () => {
  counter = join(temporary("stdo-builder-count-"), "ran")
  writeFileSync(counter, "")
  // The tests' run.sh of S1, with one more line: it notes each time it is run.
  const fixtures = fixturesLike((f) =>
    write(join(f, RUN_SH), readFileSync(join(S1_FIXTURES, RUN_SH), "utf8").replace("\nfailed=0\n", `\necho ran >> '${counter}'\nfailed=0\n`))
  )
  ws = new Workspace(build())
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  const tip = (): string => ws.git(["-C", ws.checkout(ticket), "rev-parse", "HEAD"]).trim()

  asked = await ws.run(fixtures)
  ranAtQuestion = count()

  // The user changes the code by hand after the question, and answers.
  const code = ws.checkout(ticket, CODE)
  writeFileSync(code, `${readFileSync(code, "utf8")}# changed by hand after the question\n`)
  tipBefore = tip()
  refused = await ws.answer("yes")
  ranAfterRefused = count()
  answerAfterRefused = resolvedAt(ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)) !== undefined
  tipAfterRefused = tip()

  askedAgain = await ws.run(fixtures)
  ranBeforeAnswer = count()
  answered = await ws.answer("yes")
  ranAfterAnswer = count()
  answer = resolvedAt(ws.checkout(ticket, ".ai-workspace", "tickets", "active", `${ticket}.md`)) ?? {}
  last = await ws.run(fixtures)
  log = ws.log()
}, 240_000)

afterAll(clean)

describe("the answer runs no check (the ticket's item 2)", () => {
  it("the run waits for the answer on the code, and ran the tests' run.sh", () => {
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("waits for your answer on write-build")
    expect(ranAtQuestion).toBeGreaterThan(0)
  })

  it("an answer on content changed since the question is refused, and writes and commits nothing", () => {
    expect(refused.code, refused.out).toBe(2)
    expect(answerAfterRefused).toBe(false)
    expect(tipAfterRefused).toBe(tipBefore)
    // One answer, written in the ticket that holds it as the user's resolution (REQ-FLOW-006, REQ-FLOW-007).
    expect(log.filter((e) => e.event === "answer written" && e.ticket === ticket && e.vector === "write-build").map((e) => e.path)).toEqual([join(".ai-workspace", "tickets", "active", `${ticket}.md`)])
  })

  it("the refused answer does not run the tests' run.sh", () => {
    expect(ranAfterRefused).toBe(ranAtQuestion)
  })

  it("the next run asks the user again", () => {
    expect(askedAgain.code, askedAgain.out).toBe(0)
    expect(askedAgain.out).toContain("waits for your answer on write-build")
  })

  it("the answer does not run the tests' run.sh", () => {
    expect(answered.code, answered.out).toBe(0)
    expect(ranAfterAnswer).toBe(ranBeforeAnswer)
  })

  it("the answer is written in the ticket in its checkout, as the user's resolution, naming a commit", () => {
    expect(answer.says).toBe("yes")
    expect((answer.on ?? "").length).toBeGreaterThan(0)
  })

  it("with the answer written, the next run ends with the work done", () => {
    expect(last.code, last.out).toBe(0)
    expect(log.filter((e) => e.event === "ticket merged").map((e) => e.ticket)).toEqual([ticket])
    expect(ws.board().done).toContain(ticket)
  })
})
