/**
 * A check is run only where its answer can change what the framework does
 * next, and its result is kept for what it reads (REQ-ALG-004 law 5, CALCULUS
 * L2 and L3, D180, D181). The workspace holds an existing system: the tests'
 * run.sh is on main before the first run, and each time it is run it adds a
 * line to a file outside the workspace, which says whether the code was
 * there. S1 is then run by hand: the ticket, the induction and its answer, the
 * specification and its answer. The code's check "the tests pass" is not run
 * while the code is not there, though its run.sh is in the ticket's checkout;
 * no answer runs a check (D80). The run that builds runs it once, after the
 * working session wrote the code: the evaluation's findings and verdict and
 * what the framework records are not what it reads, so the readings after the
 * evaluation use its result again. The run after the answer, a new process,
 * runs it once more before the merge.
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-004 REQ-PARAM-002
 */
import { existsSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, S1_TICKET, since, temporary, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const TESTS_RUN = join("build_tenants", "main", "tests", "run.sh")
const RUN_SH = join("write-build", "work", "files", TESTS_RUN)

let ws: Workspace
let ticket = ""
let counter = ""
const count = (line = "ran"): number => readFileSync(counter, "utf8").split("\n").filter((l) => l === line).length

const said: Said[] = []
let ranBeforeBuild = -1
let inCheckout = false
let before: readonly LogEntry[] = []
let atBuild: readonly LogEntry[] = []
let built: Said
let ranAtBuild = 0
let last: Said
let ranAtMerge = 0
let log: readonly LogEntry[] = []

beforeAll(async () => {
  counter = join(temporary("stdo-builder-count-"), "ran")
  writeFileSync(counter, "")
  // The tests' run.sh of S1, with one more line: it notes each time it is run, and whether the code was there.
  const counted = readFileSync(join(S1_FIXTURES, RUN_SH), "utf8")
    .replace("\nfailed=0\n", `\nif [ -f ../code/hello.sh ]; then echo ran >> '${counter}'; else echo 'ran without the code' >> '${counter}'; fi\nfailed=0\n`)
  const fixtures = fixturesLike((f) => write(join(f, RUN_SH), counted))
  ws = new Workspace(build())
  said.push(await ws.setup())
  // The existing system's tests, on main before any run.
  write(ws.path(TESTS_RUN), counted)
  said.push(await ws.ticket(S1_TICKET))
  ticket = /The ticket (\S+) is written/.exec(said[1]?.out ?? "")?.[1] ?? ""
  said.push(await ws.run(fixtures), await ws.answer("yes"), await ws.run(fixtures), await ws.answer("yes"))
  ranBeforeBuild = count()
  inCheckout = existsSync(ws.checkout(ticket, TESTS_RUN))
  const from = ws.log().length
  before = ws.log()
  built = await ws.run(fixtures)
  ranAtBuild = count()
  atBuild = since(ws.log(), from)
  await ws.answer("yes")
  last = await ws.run(fixtures)
  ranAtMerge = count()
  log = ws.log()
}, 240_000)

afterAll(clean)

describe("REQ-ALG-004 law 5: a check is run only where its answer can change what the framework does next, and once for what it reads (D180, D181)", () => {
  it("the runs up to the user's answer on the specification ask about the induction and then the specification", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0, 0, 0, 0])
    expect(said[2]?.out).toContain("waits for your answer on induct-ticket")
    expect(said[4]?.out).toContain("waits for your answer on write-specification")
  })

  it("while the code is not there, the tests' run.sh is in the ticket's checkout and is not run, before the build and in it", () => {
    expect(inCheckout).toBe(true)
    expect(ranBeforeBuild).toBe(0)
    expect(count("ran without the code")).toBe(0)
  })

  it("no check of the build or of the code is logged before the requirements are accepted", () => {
    expect(before.filter((e) => e.event === "check run" && (e.vector === "write-build" || e.vector === "write-code"))).toEqual([])
  })

  it("the run that builds runs the tests once, after the working session, and before it asks the user about the build", () => {
    expect(built.code, built.out).toBe(0)
    expect(built.out).toContain("waits for your answer on write-build")
    expect(ranAtBuild).toBe(1)
    const passed = atBuild.findIndex((e) => (e.event === "check run" && e.result === "yes") && e.vector === "write-build" && e.check === "the tests pass")
    const asked = atBuild.findIndex((e) => e.event === "user asked" && e.vector === "write-build")
    expect(passed).toBeGreaterThanOrEqual(0)
    expect(asked).toBeGreaterThan(passed)
  })

  it("after the answer, the run runs the tests once more before the ticket is merged", () => {
    expect(last.code, last.out).toBe(0)
    expect(ranAtMerge).toBe(2)
    expect(log.filter((e) => e.event === "ticket merged").map((e) => e.ticket)).toEqual([ticket])
  })
})
