/**
 * QA-02, REQ-ALG-004 and REQ-METHOD-004: a verdict counts only where the
 * evaluating session of this step wrote it. On the workspace S1 leaves, the
 * user deletes the design and starts a run. The working session writes a new
 * design, other than the first; the evaluating session writes nothing. S1's
 * verdict was given on the first design and must not stand for the new one,
 * so the design's vector stays open and the run stops on it.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-004 REQ-FLOW-005
 */
import { rmSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1Whole, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const DESIGN = "# Design\n\nREQ-HELLO-001 is met by one shell script, `code/hello.sh`, written again,\nwhich prints the line and exits with code 0.\n"
let ws: Workspace
let ran: Said
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  await s1Whole(ws, S1_FIXTURES)
  rmSync(ws.path("build_tenants", "main", "design"), { recursive: true })
  const silent = fixturesLike((f) => {
    write(join(f, "write-design", "work", "files", "build_tenants", "main", "design", "DESIGN.md"), DESIGN)
    rmSync(join(f, "write-design", "evaluation", "files"), { recursive: true })
  })
  const from = ws.log().length
  ran = await ws.run(silent)
  log = ws.log().slice(from)
}, 180_000)

afterAll(clean)

describe("QA-02 a verdict counts only where this step's evaluating session wrote it", () => {
  it("the evaluating session was started on the new design and wrote nothing", () => {
    expect(log.filter((e) => e.event === "session started" && e.vector === "write-design").map((e) => e.kind)).toEqual(["work", "evaluation", "evaluation"])
  })

  it("the design's vector is not closed by S1's verdict, and the run stops on it", () => {
    expect(log.some((e) => e.event === "vector closed" && e.vector === "write-design")).toBe(false)
    expect(ran.code, ran.out).toBe(1)
    expect(ran.out).toContain("write-design could not close: the same number of checks failed twice in a row")
    expect(ran.out).toContain("What did not pass: verdict.")
    expect(log.some((e) => e.event === "session started" && e.vector === "write-code")).toBe(false)
  })
})
