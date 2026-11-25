/**
 * A session that returns breaks a row of failed sessions (REQ-FLOW-005, "unless
 * the session before it on the vector in this run failed too"; finding C-11 of
 * the review of release 3.2.0). S1 up to the build, then a run whose agent is
 * the script of `script_agent.ts`: the build's first working session fails;
 * the second writes the stand-in's files and returns; the evaluation fails.
 * That is no second failure in a row, so the evaluation is made again; it
 * fails again, and the run stops there.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-005
 */
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { scriptAgent } from "./script_agent.js"
import { build, clean, S1_FIXTURES, s1ToRequirements, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

let ran: Said
let log: readonly LogEntry[] = []

beforeAll(async () => {
  const ws = new Workspace(build())
  await s1ToRequirements(ws, S1_FIXTURES)
  const from = ws.log().length
  const agent = scriptAgent(ws, true)
  write(join(agent.state, "copy"), `${join(S1_FIXTURES, "write-build", "work", "files")}\n`)
  agent.does("fail,copy,fail")
  ran = await ws.run("")
  log = ws.log().slice(from)
}, 180_000)

afterAll(clean)

describe("C-11: a session that returned between two failures", () => {
  it("does not stop the run as failed twice in a row; the next failure after it does", () => {
    const sessions = log.filter((e) => e.event === "session started" && e.vector === "write-build").map((e) => e.kind)
    expect(sessions, ran.out).toEqual(["work", "work", "evaluation", "evaluation"])
    expect(ran.out).toContain("failed twice in a row")
  })
})
