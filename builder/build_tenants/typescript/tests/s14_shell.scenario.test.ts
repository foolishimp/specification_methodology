/**
 * Scenario S14, cases 8 to 10: the further process is a shell, one of the
 * system's own programs, whose environment the system does not show
 * (REQ-FLOW-001: the framework knows a process of a session by its parent,
 * by its group and by its mark, the agent's own process first, and knows it
 * until it has ended; a process it cannot place it does not end, and names).
 * The agent the settings name is the script of `script_agent.ts`; its further
 * shell takes no notice of the terminate signal and writes into the ticket's
 * the workspace's folder every 30 ms. Case 8 as case 4 and as case 7 is here; as case 1, in
 * `s14_shell_time.scenario.test.ts`. A last case has a shell as the agent
 * itself, whose own process the framework knows from its start. Each case
 * waits for what it expects within a bound, and judges nothing after a fixed
 * pause.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007
 */
import { chmodSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, describe, expect, it } from "vitest"
import { alive, killAll, scriptAgent, strayLines, type Agent } from "./script_agent.js"
import { build, clean, S1_TICKET, temporary, until, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const cli = build()
const agents: Agent[] = []
const strays: number[] = []
afterAll(() => {
  for (const a of agents) killAll([...a.agents(), ...a.further()])
  killAll(strays)
  clean()
})

/** A governed product set up, its ticket written, and the script named as the agent; with `watched`, what the further process writes is compared as any file (S14). */
async function before(watched = false): Promise<{ readonly ws: Workspace; readonly agent: Agent; readonly ticket: string }> {
  const ws = new Workspace(cli)
  await ws.setup()
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  const agent = scriptAgent(ws, !watched)
  agents.push(agent)
  return { ws, agent, ticket }
}

const time = (e: LogEntry | undefined): number => (e === undefined ? Number.NaN : Date.parse(e.at))

/** The latest time the further process of the session of this number wrote into the workspace's folder. */
const lastWritten = (ws: Workspace, ticket: string, n: number): number => Math.max(...(strayLines(ws.path()).get(n) ?? []))

const tip = (ws: Workspace, ticket: string): string => ws.git(["rev-parse", `stdo/${ticket}`]).trim()

describe("S14 cases 8 to 10: the further process is a shell", () => {
  it("case 8, as case 4: the run receives the interrupt signal while the session is at work; the shell, which loses its parent while it is being ended, is still ended, and no process of the session is alive when the run has ended", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("shell-wait")
    const running = ws.start(["run", ws.root])
    await until(() => agent.further().length === 1 && strayLines(ws.path()).size === 1, 60)
    process.kill(running.pid, "SIGINT")
    const ran: Said = await running.ended
    const log = ws.log()
    expect(ran.code, ran.out).toBe(130)
    for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
    const stopped = log.filter((e) => e.event === "session processes ended")
    expect(stopped).toHaveLength(1)
    expect(stopped[0]?.processes).toBeGreaterThanOrEqual(2)
    expect(lastWritten(ws, ticket, 1)).toBeLessThanOrEqual(time(stopped[0]))
  }, 120_000)

  it("case 8, as case 7: the user kills the run while the session is at work, then starts a run; it ends the agent, known by its mark, and the shell, known by its parent, before anything else on the ticket", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("shell-wait")
    const running = ws.start(["run", ws.root])
    await until(() => agent.further().length === 1 && strayLines(ws.path()).size === 1, 60)
    running.kill()
    await running.ended
    const left = [...agent.agents(), ...agent.further()]
    for (const pid of left) expect(alive(pid), `process ${pid} after the kill`).toBe(true)
    const from = ws.log().length
    agent.does("fail")
    await ws.run("")
    const log = ws.log().slice(from)
    for (const pid of left) expect(alive(pid), `process ${pid}`).toBe(false)
    const events = log.map((e) => e.event)
    expect(events[0]).toBe("run started")
    expect(events[1], events.join(", ")).toBe("session processes ended")
    expect(log[1]?.processes).toBeGreaterThanOrEqual(2)
    expect(events.indexOf("run cut off")).toBeGreaterThan(1)
    expect(lastWritten(ws, ticket, 1)).toBeLessThanOrEqual(time(log[1]))
  }, 120_000)

  it("case 9: the script returns and leaves the shell behind in its own process group; the framework knows the shell by its group, ends it, counts it, and only then goes on", async () => {
    const { ws, agent, ticket } = await before(true)
    agent.does("shell-group,fail")
    const ran = await ws.run("")
    // The run goes on past the session: it names what the shell wrote into the workspace's folder, and judges and commits nothing of the step before the user has ruled (S14).
    expect(ran.out).toContain(`stray.txt (added)`)
    expect(ran.out).toContain("waits for your ruling on what changed")
    expect(ws.log().some((e) => e.event === "check run" || (e.event === "commit made" && String(e.why).startsWith("the result of the step")))).toBe(false)
    const log = ws.log()
    const shell = agent.further()[0] ?? -1
    expect(alive(shell), ran.out).toBe(false)
    const started = log.findIndex((e) => e.event === "session started")
    const stopped = log.findIndex((e, i) => i > started && e.event === "session processes ended")
    expect(stopped, log.map((e) => e.event).join(", ")).toBeGreaterThan(started)
    expect(log[stopped]?.processes).toBeGreaterThanOrEqual(1)
    expect(log[stopped + 1]?.event).toBe("session returned")
    expect(lastWritten(ws, ticket, 1)).toBeLessThanOrEqual(time(log[stopped]))
  }, 120_000)

  it("case 10: the script returns and leaves the shell in a session of its own, working in the workspace's folder; the framework cannot place it, ends no process, names it, and the run is cut off; nothing is committed, judged or started while it is alive; once the user ends it, a run goes on", async () => {
    const { ws, agent, ticket } = await before(true)
    agent.does("shell-place,fail")
    const first = await ws.run("")
    const shell = agent.further()[0] ?? -1
    strays.push(shell)
    const named = `the process ${shell}, started `
    expect(first.code, first.out).toBe(1)
    expect(first.out).toContain(named)
    expect(first.out).toContain(`running /bin/zsh ${join(agent.state, "further.zsh")}`)
    expect(first.out).toContain("cannot place")
    expect(first.out).toContain("End each process named here, then start a run again")
    expect(alive(shell)).toBe(true)
    // Nothing is added after the session's start, committed or judged while it may be alive.
    const log = ws.log()
    const at = log.map((e) => e.event).lastIndexOf("session started")
    expect(log.slice(at + 1)).toEqual([])
    const from = log[at]?.commit ?? ""
    expect(tip(ws, ticket)).toBe(from)
    // A run and an answer are refused while it is alive, and name it (REQ-FLOW-003 step 1, REQ-FLOW-006).
    const before2 = ws.log().length
    const second = await ws.run("")
    expect(second.code, second.out).toBe(2)
    expect(second.out).toContain(named)
    expect(second.out).toContain("running /bin/zsh")
    expect(second.out).toContain(`holds/${ticket}`)
    expect(ws.log().slice(before2).map((e) => e.event)).toEqual(["run started", "run ended"])
    const answered = await ws.answer("yes")
    expect(answered.code, answered.out).toBe(2)
    expect(answered.out).toContain(named)
    expect(answered.out).toContain("running /bin/zsh")
    expect(alive(shell)).toBe(true)
    expect(tip(ws, ticket)).toBe(from)
    // The user ends the shell; the run they start goes on: it notes that the run was cut off (REQ-FLOW-007), names what the shell wrote into the workspace's folder, and judges and commits nothing of the step before the user has ruled (S14).
    killAll([shell])
    await until(() => !alive(shell), 30)
    const from3 = ws.log().length
    const third = await ws.run("")
    expect(third.code, third.out).toBe(0)
    expect(ws.log().slice(from3).map((e) => e.event)).toEqual(["run started", "run cut off", "user asked", "run ended"])
    expect(third.out).toContain(`stray.txt (added)`)
    expect(third.out).toContain("waits for your ruling on what changed")
    expect(ws.log().slice(from3).some((e) => e.event === "commit made" || e.event === "check run")).toBe(false)
    expect(tip(ws, ticket)).toBe(from)
    // After the user's yes, the next run goes on to a session, and notes the cut-off no second time.
    await ws.answer("yes")
    const from4 = ws.log().length
    const fourth = await ws.run("")
    expect(ws.log().slice(from4).map((e) => e.event), fourth.out).toContain("session started")
    expect(ws.log().slice(from4).some((e) => e.event === "run cut off")).toBe(false)
    expect(ws.log().filter((e) => e.event === "run cut off")).toHaveLength(1)
  }, 180_000)

  it("the agent is itself a shell, whose environment the system does not show, and starts a further shell in a session of its own: the framework knows the agent's own process from its start, and the further shell by its parent, and ends both on the terminate signal", async () => {
    const ws = new Workspace(cli)
    await ws.setup()
    const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
    const state = temporary("stdo-builder-agent-")
    const script = join(state, "agent.zsh")
    writeFileSync(join(state, "further.zsh"), `trap '' TERM\nzmodload zsh/datetime\nwhile :; do print -r -- "1 $(( EPOCHREALTIME * 1000 ))" >> stray.txt; /bin/sleep 0.03; done\n`)
    writeFileSync(script, `print $$ > "$1/agent.pid"\n/usr/bin/perl -MPOSIX -e 'POSIX::setsid(); exec @ARGV' /bin/zsh "$1/further.zsh" &\nprint $! > "$1/further.pid"\nwhile :; do /bin/sleep 0.05; done\n`)
    chmodSync(script, 0o755)
    const settings = ws.path(".stdo-builder", "settings.json")
    const s = JSON.parse(readFileSync(settings, "utf8")) as { agents: Record<string, string[]>; work: string; evaluation: string }
    s.agents.shell = ["/bin/zsh", script, state]
    s.work = "shell"
    s.evaluation = "shell"
    writeFileSync(settings, `${JSON.stringify(s, null, 2)}\n`)
    const pidIn = (name: string): number => Number(readFileSync(join(state, name), "utf8"))
    const running = ws.start(["run", ws.root])
    await until(() => strayLines(ws.path()).size === 1, 60)
    const pids = [pidIn("agent.pid"), pidIn("further.pid")]
    strays.push(...pids)
    for (const pid of pids) expect(alive(pid), `process ${pid}`).toBe(true)
    process.kill(running.pid, "SIGTERM")
    const ran: Said = await running.ended
    expect(ran.code, ran.out).toBe(143)
    for (const pid of pids) expect(alive(pid), `process ${pid}`).toBe(false)
    const stopped = ws.log().filter((e) => e.event === "session processes ended")
    expect(stopped).toHaveLength(1)
    expect(stopped[0]?.processes).toBeGreaterThanOrEqual(2)
    expect(lastWritten(ws, ticket, 1)).toBeLessThanOrEqual(time(stopped[0]))
  }, 120_000)
})
