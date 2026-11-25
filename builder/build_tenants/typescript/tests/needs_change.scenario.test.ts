/**
 * REQ-FLOW-005, a working session whose work needs a change it may not make
 * (D97). S1 runs to the specification the user accepted. S1's term is the specification and then the build, so
 * the build's working session comes next (REQ-METHOD-006); it writes nothing,
 * and prints what change it needs and why, as its packet says. No evaluating
 * session is started on a build that is not there. The run stops when the
 * build cannot close, and names where what the last working session printed
 * is kept; the words are there.
 *
 * @uses C14 C5 C6
 * @is REQ-FLOW-005 REQ-ALG-007
 */
import { readFileSync, rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const NEEDS = "This work needs a change to the requirements: they give no exit code. 5be1d9."
const PRINTED = ".stdo-builder/local/printed/write-build.work."
let ws: Workspace
let ticket = ""
let ran: Said
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  const fixtures = fixturesLike((f) => {
    rmSync(join(f, "write-build", "work", "files"), { recursive: true })
    write(join(f, "write-build", "work", "print"), `${NEEDS}\n`)
  })
  ticket = (await s1ToRequirements(ws, fixtures)).ticket
  const from = ws.log().length
  ran = await ws.run(fixtures)
  log = ws.log().slice(from)
}, 180_000)

afterAll(clean)

describe("REQ-FLOW-005 a working session needs a change it may not make", () => {
  it("its packet tells it to say so in what it prints and to stop without writing its asset", () => {
    const brief = readFileSync(ws.path(".stdo-builder", "local", "briefs", "write-build.work.md"), "utf8")
    expect(brief).toContain("- stop: where the work needs a change this session may not make, say what change and why in what you print, and stop without writing build_tenants/main/design, build_tenants/main/tests and build_tenants/main/code.")
    expect(brief).not.toContain("backlog that says what and why")
  })

  it("no evaluating session is started on a build that is not there", () => {
    const started = log.filter((e) => e.event === "session started" && e.vector === "write-build").map((e) => e.kind)
    expect(started).toEqual(["work", "work"])
  })

  it("the run stops, and names where what the last working session printed is kept; the words are there", () => {
    expect(ran.code, ran.out).toBe(1)
    expect(ran.out).toContain("write-build could not close: the same number of checks failed twice in a row")
    // The last working session's own file, which its entry in the log names (D218).
    const own = log.filter((e) => e.event === "session returned" && e.vector === "write-build" && e.kind === "work").at(-1)?.printed ?? ""
    expect(own.startsWith(PRINTED)).toBe(true)
    const kept = `${own}`
    expect(ran.out).toContain(`What the last working session printed is kept at ${kept}.`)
    expect(readFileSync(ws.path(kept), "utf8")).toContain(NEEDS)
    expect(JSON.stringify(log)).not.toContain("5be1d9")
  })
})
