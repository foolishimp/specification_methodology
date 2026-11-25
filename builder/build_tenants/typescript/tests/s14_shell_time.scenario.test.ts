/**
 * Scenario S14, case 8 as case 1: the governing graph gives the induction's
 * session one minute, and the script runs longer than its time; its further
 * process is a shell in a session of processes of its own, whose environment
 * the system does not show, and which takes no notice of the terminate
 * signal. When its time is over the framework ends every process it knows to
 * be of the session: the shell, known by its parent, is still ended once the
 * script has ended, and only then does the framework go on.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-005 REQ-FLOW-007 REQ-PARAM-003
 */
import { readFileSync, writeFileSync } from "node:fs"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { alive, killAll, scriptAgent, strayLines, type Agent } from "./script_agent.js"
import { build, clean, S1_TICKET, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

let ws: Workspace
let agent: Agent | undefined
let ticket = ""
let ran: Said
let log: readonly LogEntry[] = []

/** Gives the vector of this name one minute for each session, in the graph's written form. */
const oneMinute = (value: unknown, name: string): unknown =>
  Array.isArray(value) ? value.map((v) => oneMinute(v, name))
    : typeof value === "object" && value !== null
    ? Object.fromEntries([...Object.entries(value).map(([k, v]) => [k, oneMinute(v, name)]), ...((value as { name?: unknown }).name === name && "function" in value ? [["minutes", 1]] : [])])
    : value

beforeAll(async () => {
  ws = new Workspace(build())
  await ws.setup()
  ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  const graph = ws.path(".stdo-builder", "graph.json")
  writeFileSync(graph, `${JSON.stringify(oneMinute(JSON.parse(readFileSync(graph, "utf8")), "induct-ticket"), null, 2)}\n`)
  agent = scriptAgent(ws)
  agent.does("shell-over,fail")
  ran = await ws.run("")
  log = ws.log()
}, 240_000)

afterAll(() => {
  if (agent !== undefined) killAll([...agent.agents(), ...agent.further()])
  clean()
})

describe("S14 case 8, as case 1: the script runs longer than its time, and its further process is a shell", () => {
  it("the session fails as having run longer than allowed, and no process of it is alive past it, the shell among them", () => {
    const failed = log.find((e) => e.event === "session failed")
    expect(failed?.why, ran.out).toContain("ran longer than allowed")
    for (const pid of [...(agent?.agents() ?? []), ...(agent?.further() ?? [])]) expect(alive(pid), `process ${pid}`).toBe(false)
    const stopped = log.findIndex((e) => e.event === "session processes ended")
    expect(stopped).toBeGreaterThan(-1)
    expect(log[stopped]?.processes).toBeGreaterThanOrEqual(2)
    expect(log[stopped + 1]?.event).toBe("session failed")
    expect(Math.max(...(strayLines(ws.path()).get(1) ?? []))).toBeLessThanOrEqual(Date.parse(log[stopped]?.at ?? ""))
  })

  it("the run goes on past the session: it names what the further process wrote into the workspace's folder, and judges and commits nothing of the step before the user has ruled (S14)", () => {
    expect(ran.code, ran.out).toBe(0)
    expect(ran.out).toContain("waits for your ruling on what changed while the session on induct-ticket worked")
    expect(ran.out).toContain(`stray.txt (added)`)
    expect(log.some((e) => e.event === "check run" || e.event === "verdict read")).toBe(false)
    expect(log.some((e) => e.event === "commit made" && String(e.why).startsWith("the result of the step"))).toBe(false)
  })
})
