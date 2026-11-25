/**
 * REQ-FLOW-005 step 1 and REQ-FLOW-006, on a built product: S1 is run whole,
 * with requirements of 100 lines. The user writes a ticket that changes one
 * line of them, and its induction gives the term the requirements and then
 * the build. The first step on each starts its working session: the user is
 * not asked and no evaluation is made before it. The question on the
 * requirements says that 1 line of their file changed and 99 remain as they
 * were, and that every other file is as it was.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-005 REQ-FLOW-006 REQ-VERIFY-002
 */
import { rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, inducted, s1Whole, since, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const REQUIREMENTS = ["specification", "requirements", "HELLO.md"] as const
const DESIGN = ["build_tenants", "main", "design", "DESIGN.md"] as const
const SAID = "Run with no arguments, the program prints the line `hello, world` and exits"
const CHANGED = "Run with no arguments, from any folder, the program prints the line `hello, world` and exits"

/** Requirements of 100 lines: S1's, then a note of 94 lines that names no requirement. */
const HUNDRED = [
  "# Requirements",
  "",
  "### REQ-HELLO-001 Say hello",
  "",
  SAID,
  "with code 0.",
  ...Array.from({ length: 94 }, (_, i) => `Note ${i + 1}: this line is no requirement, and no ticket here changes it.`)
].map((l) => `${l}\n`).join("")

/** The ticket, in the user's words. */
const TICKET = "Hello prints the same from any folder. Say so in the requirements, and in the design."
const DESIGNED = "# Design\n\nREQ-HELLO-001 is met by one POSIX shell script, `code/hello.sh`, which reads no file, so it prints\nthe line with `printf` from any folder and ends, so the shell exits with code 0.\n"

let ws: Workspace
let ticket = ""
let requirementsRun: Said
let buildRun: Said
let afterInduction: readonly LogEntry[] = []
let afterRequirements: readonly LogEntry[] = []

const sessionsIn = (log: readonly LogEntry[]): readonly string[] =>
  log.filter((e) => e.event === "session started" || e.event === "user asked").map((e) => `${e.vector ?? ""} ${e.kind ?? "asked"}`)

beforeAll(async () => {
  ws = new Workspace(build())
  await s1Whole(ws, fixturesLike((f) => write(join(f, "write-specification", "work", "files", ...REQUIREMENTS), HUNDRED)))
  // The ticket's sessions: the induction, the requirements and the build; a session no other fixed files are given for cannot be started.
  const fixtures = fixturesLike((f) => {
    for (const vector of ["write-specification", "write-intent", "write-product", "write-design", "write-tests", "write-code"]) rmSync(join(f, vector), { recursive: true, force: true })
    write(join(f, "induct-ticket", "work", "append"), inducted({ kind: "feature", klass: "requirement_reprice", enters: "requirements", ends: "code", scope: "the requirement's words, and the design", term: ["write-requirements", "write-build"] }))
    write(join(f, "write-requirements", "work", "files", ...REQUIREMENTS), HUNDRED.replace(SAID, CHANGED))
    write(join(f, "write-build", "work", "files", ...DESIGN), DESIGNED)
  })
  ticket = /The ticket (\S+) is written/.exec((await ws.ticket(TICKET)).out)?.[1] ?? ""
  await ws.run(fixtures)
  await ws.answer("yes")
  const fromInduction = ws.log().length
  requirementsRun = await ws.run(fixtures)
  afterInduction = since(ws.log(), fromInduction)
  await ws.answer("yes")
  const fromRequirements = ws.log().length
  buildRun = await ws.run(fixtures)
  afterRequirements = since(ws.log(), fromRequirements)
}, 360_000)

afterAll(clean)

describe("on a built product, under a ticket whose term is the requirements and then the build", () => {
  it("REQ-FLOW-005 step 1: the first step on the requirements starts its working session; the user is not asked before it", () => {
    expect(sessionsIn(afterInduction)).toEqual(["write-requirements work", "write-requirements asked"])
    expect(requirementsRun.code, requirementsRun.out).toBe(0)
    expect(requirementsRun.out).toContain("waits for your answer on write-requirements")
  })

  it("REQ-FLOW-005 step 1: the first step on the build starts its working session; no evaluation is made and the user is not asked before it", () => {
    expect(sessionsIn(afterRequirements)).toEqual(["write-build work", "write-build evaluation", "write-build asked"])
    expect(buildRun.code, buildRun.out).toBe(0)
    expect(buildRun.out).toContain("waits for your answer on write-build")
  })

  it("REQ-FLOW-005 step 1: the checklist shows that the work of each began, before the step's resolutions", () => {
    const text = ws.read(".ai-workspace", "tickets", "active", `${ticket}.md`) ?? ""
    for (const vector of ["write-requirements", "write-build"]) expect(text).toMatch(new RegExp(`^- framework: began ${vector} at [0-9a-f]{40}$`, "m"))
    expect(text.indexOf("began write-requirements")).toBeLessThan(text.indexOf("resolved user yes at requirements"))
    expect(text.indexOf("began write-build")).toBeLessThan(text.indexOf("resolved evaluation"))
  })

  it("REQ-FLOW-006: the question on the requirements says that 1 line of their file of 100 changed and 99 remain as they were, and that every other file is as it was", () => {
    expect(ws.git(["show", `main:${REQUIREMENTS.join("/")}`]).split("\n").filter((l, i, all) => i < all.length - 1 || l !== "")).toHaveLength(100)
    expect(requirementsRun.out).toContain(`In requirements, ${REQUIREMENTS.join("/")}: 1 line changed (1 added, 1 taken out), and 99 lines remain as they were.`)
    expect(requirementsRun.out).toContain("Every other file of requirements is as it was when main last held it.")
  })
})
