/**
 * A session is not over where a process the framework knows to be of it is
 * still alive after it has tried to end it, or it finds one it cannot place
 * (REQ-FLOW-005; REQ-FLOW-003 step 1; REQ-FLOW-006). The agent is the script
 * of `script_agent.ts`. Each case in a new folder:
 *
 * - its further process outlives every round of ending it;
 * - the process table cannot be read when the session returns, through a
 *   `ps` the driver puts first on the framework's path: the run is cut off,
 *   saying in one sentence that `ps` could not read the table and what to
 *   install, and names no process; the answer and the next run are refused
 *   in the same sentence, and end nothing and start nothing (REQ-FLOW-001);
 * - a process with the ticket's mark is alive while the ticket's hold is free:
 *   the answer is refused, naming it, and the run ends it and goes on;
 * - its further process starts a new program in its place again and again, so
 *   no reading of the process table shows its environment; it has no parent
 *   left and works in the workspace's folder: the framework cannot place it, ends it
 *   not, and names it, at the session's end, in the answer and in the next
 *   run.
 *
 * Where the session is not over the run is cut off, or refused, naming each
 * process, and nothing is committed, judged or started on the ticket until
 * none is alive. Each waits within a bound, and judges nothing after a fixed
 * pause.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007
 */
import { spawn, type ChildProcess } from "node:child_process"
import { afterAll, describe, expect, it } from "vitest"
import { alive, killAll, scriptAgent, type Agent } from "./script_agent.js"
import { build, clean, S1_TICKET, until, Workspace, type LogEntry } from "./scenario_driver.js"

const cli = build()
const agents: Agent[] = []
const others: ChildProcess[] = []
afterAll(() => {
  for (const a of agents) killAll([...a.agents(), ...a.further(), ...a.chain()])
  for (const c of others) c.kill("SIGKILL")
  clean()
})

/** A governed product set up, its ticket written, and the script named as the agent. */
async function before(): Promise<{ readonly ws: Workspace; readonly agent: Agent; readonly ticket: string }> {
  const ws = new Workspace(cli)
  await ws.setup()
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  const agent = scriptAgent(ws, true)
  agents.push(agent)
  return { ws, agent, ticket }
}

/** The entries after the last `session started`, and the commit that session started from. */
function afterLastStart(log: readonly LogEntry[]): { readonly after: readonly LogEntry[]; readonly from: string } {
  const at = log.map((e) => e.event).lastIndexOf("session started")
  return { after: log.slice(at + 1), from: log[at]?.commit ?? "" }
}

const tip = (ws: Workspace, ticket: string): string => ws.git(["rev-parse", `stdo/${ticket}`]).trim()

describe("a session whose processes cannot all be ended is not over", () => {
  it("its further process outlives every round: the run goes no further, and the next run, which cannot end it either, starts nothing", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("survive,fail")
    const first = await ws.run("")
    const log = ws.log()
    expect(first.code, first.out).toBe(1)
    expect(first.out).toContain("its working session is not over")
    expect(first.out).toContain("still alive after 20 rounds")
    expect(first.out).toContain("End each process named here, then start a run again")
    const { after, from } = afterLastStart(log)
    // The count of those it did end is kept; nothing else is added, committed or judged (REQ-FLOW-007).
    expect(after.map((e) => e.event)).toEqual(["session processes ended"])
    expect(after[0]?.processes).toBeGreaterThanOrEqual(1)
    expect(tip(ws, ticket)).toBe(from)
    const chain = agent.chain()
    expect(alive(chain.at(-1) ?? -1)).toBe(true)
    // The next run finds the hold the run left, and cannot end the process either: it starts nothing, and names the hold and the process.
    const at = ws.log().length
    const second = await ws.run("")
    const next = ws.log().slice(at)
    expect(second.code, second.out).toBe(2)
    expect(second.out).toContain(`holds/${ticket}`)
    expect(second.out).toContain("is not over")
    expect(second.out).toContain("still alive after 20 rounds")
    expect(next.map((e) => e.event)).toEqual(["run started", "session processes ended", "run ended"])
    expect(tip(ws, ticket)).toBe(from)
    // The user ends the chain; the next run goes on, and notes that the run was cut off.
    killAll(agent.chain())
    await until(() => agent.chain().every((p) => !alive(p)), 30)
    const from3 = ws.log().length
    const third = await ws.run("")
    const events = ws.log().slice(from3).map((e) => e.event)
    expect(events, third.out).toContain("run cut off")
    expect(events).toContain("session started")
    for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
  }, 180_000)

  it("the process table cannot be read when the session returns: the run goes no further, saying so in one sentence that names no process; the answer and the next run are refused in the same sentence, end nothing and start nothing", async () => {
    const { ws, agent, ticket } = await before()
    ws.env.PATH = `${agent.bin}:${ws.env.PATH ?? ""}`
    agent.does("unread,fail")
    const first = await ws.run("")
    expect(first.code, first.out).toBe(1)
    expect(first.out).toContain("its working session is not over")
    const sentence = /`ps` could not read the table of processes[^.]*\./.exec(first.out)?.[0]
    expect(sentence, first.out).toContain("procps")
    // Where it found none, it names no process, and asks the user to end none (REQ-FLOW-005).
    expect(first.out).not.toMatch(/the process \d+, started/)
    expect(first.out).not.toContain("End each process named here")
    const { after, from } = afterLastStart(ws.log())
    expect(after).toEqual([])
    expect(tip(ws, ticket)).toBe(from)
    const further = agent.further()[0] ?? -1
    expect(alive(further)).toBe(true)
    // The answer is refused in the same sentence, and names no process (REQ-FLOW-006).
    const answered = await ws.answer("yes")
    expect(answered.code, answered.out).toBe(2)
    expect(answered.out).toContain(sentence)
    expect(answered.out).not.toMatch(/the process \d+, started/)
    // So is the next run, which reads the table before anything else and before any session: it ends nothing and starts nothing (REQ-FLOW-003 step 1).
    const at = ws.log().length
    const second = await ws.run("")
    expect(second.code, second.out).toBe(2)
    expect(second.out).toContain(sentence)
    expect(second.out).not.toMatch(/the process \d+, started/)
    expect(ws.log().slice(at).map((e) => e.event)).toEqual(["run started", "run ended"])
    expect(alive(further)).toBe(true)
    expect(tip(ws, ticket)).toBe(from)
    // Once the table can be read, the next run ends the session's process before anything else on the ticket.
    agent.readable()
    const from3 = ws.log().length
    await ws.run("")
    const log3 = ws.log().slice(from3)
    expect(log3[1]?.event).toBe("session processes ended")
    expect(log3[1]?.processes).toBeGreaterThanOrEqual(1)
    expect(log3.map((e) => e.event)).toContain("run cut off")
    expect(alive(further)).toBe(false)
  }, 180_000)

  it("a process with the ticket's mark is alive while its hold is free: the answer is refused, naming it; the run ends it before anything else on the ticket, and goes on", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("fail")
    await ws.run("")
    for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
    const marked = spawn(process.execPath, ["-e", "setInterval(() => {}, 1000)"], {
      env: { ...process.env, [`STDO_BUILDER_SESSION_${ticket.replace(/[^A-Za-z0-9]/g, "_")}`]: encodeURIComponent(ws.root) },
      stdio: "ignore"
    })
    others.push(marked)
    const pid = marked.pid ?? -1
    await until(() => alive(pid), 30)
    const answered = await ws.answer("yes")
    expect(answered.code, answered.out).toBe(2)
    expect(answered.out).toContain(`the process ${pid}, started `)
    expect(alive(pid)).toBe(true)
    const from = ws.log().length
    await ws.run("")
    const log = ws.log().slice(from)
    expect(alive(pid)).toBe(false)
    expect(log[1]?.event, log.map((e) => e.event).join(", ")).toBe("session processes ended")
    expect(log[1]?.ticket).toBe(ticket)
    expect(log[1]?.processes).toBe(1)
    expect(log.map((e) => e.event)).toContain("session started")
  }, 180_000)

  it("its further process starts a new program in its place again and again, with no parent left, in the workspace's folder: the framework cannot place it; the run is cut off, and the answer and the next run name it and start nothing", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("reexec,fail")
    const first = await ws.run("")
    const further = agent.further()[0] ?? -1
    const named = `the process ${further}, started `
    expect(first.code, first.out).toBe(1)
    expect(first.out).toContain("its working session is not over")
    expect(first.out).toContain("cannot place")
    expect(first.out).toContain(named)
    expect(first.out).toContain("reexec.cjs")
    // Nothing is added after the session's start, committed or judged while it may be alive (REQ-FLOW-005, REQ-FLOW-007).
    const { after, from } = afterLastStart(ws.log())
    expect(after).toEqual([])
    expect(tip(ws, ticket)).toBe(from)
    expect(alive(further)).toBe(true)
    // The answer cannot place it either, and names it (REQ-FLOW-006).
    const answered = await ws.answer("yes")
    expect(answered.code, answered.out).toBe(2)
    expect(answered.out).toContain("cannot place")
    expect(answered.out).toContain(named)
    expect(answered.out).toContain("reexec.cjs")
    // Nor can the next run: it ends nothing and starts nothing, and names the hold and the process (REQ-FLOW-003 step 1).
    const at = ws.log().length
    const second = await ws.run("")
    expect(second.code, second.out).toBe(2)
    expect(second.out).toContain("cannot place")
    expect(second.out).toContain(`holds/${ticket}`)
    expect(second.out).toContain(named)
    expect(second.out).toContain("reexec.cjs")
    expect(ws.log().slice(at).map((e) => e.event)).toEqual(["run started", "run ended"])
    expect(alive(further)).toBe(true)
    expect(tip(ws, ticket)).toBe(from)
    // The user ends it; the next run goes on, and notes that the run was cut off.
    killAll([further])
    await until(() => !alive(further), 30)
    const from3 = ws.log().length
    const third = await ws.run("")
    const events = ws.log().slice(from3).map((e) => e.event)
    expect(events, third.out).toContain("run cut off")
    expect(events).toContain("session started")
  }, 180_000)
})
