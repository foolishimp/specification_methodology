/**
 * Scenario S14, a session is over when the framework has ended it: cases 2 to
 * 7 and 11, and case 11 run on to the user's yes, each in a new folder. The agent the settings name is the script of
 * `script_agent.ts`, whose further process, in a session of processes of its
 * own, keeps the session's output open and writes into the workspace's folder
 * until it is ended. Each case waits for what it expects within a bound, and
 * judges nothing after a fixed pause. Case 1 is `s14_time.scenario.test.ts`.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-007 REQ-PARAM-001
 */
import { existsSync, readFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, describe, expect, it } from "vitest"
import { alive, killAll, scriptAgent, strayLines, type Agent } from "./script_agent.js"
import { build, clean, S1_TICKET, until, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const cli = build()
afterAll(clean)

/** A governed product set up, its ticket written, and the script named as the agent. */
async function before(): Promise<{ readonly ws: Workspace; readonly agent: Agent; readonly ticket: string }> {
  const ws = new Workspace(cli)
  await ws.setup()
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent: scriptAgent(ws), ticket }
}

const time = (e: LogEntry | undefined): number => (e === undefined ? Number.NaN : Date.parse(e.at))

/** Each session's further process wrote nothing after the entry that ends that session. */
function nothingAfter(ws: Workspace, ticket: string, log: readonly LogEntry[]): void {
  const ends = log.filter((e) => e.event === "session returned" || e.event === "session failed")
  for (const [n, times] of strayLines(ws.path())) {
    const end = ends[n - 1]
    expect(end, `the session ${n} has no end in the log`).toBeDefined()
    expect(Math.max(...times)).toBeLessThanOrEqual(time(end))
  }
}

describe("S14 a session is over when the framework has ended it", () => {
  for (const [label, how] of [["2, the script returns and leaves the further process behind", "return"], ["3, the script exits with 1", "fail"]] as const) {
    it(`case ${label}: no process of a session is alive past it, and nothing it writes afterwards is in the workspace`, async () => {
      const { ws, agent, ticket } = await before()
      agent.does(how)
      const ran = await ws.run("")
      const log = ws.log()
      // What the further process wrote into the folder is named to the user, and nothing of the step is judged or committed before the user has ruled (S14, REQ-FLOW-005 step 3).
      expect(ran.code, ran.out).toBe(0)
      expect(ran.out).toContain("waits for your ruling on what changed")
      expect(ran.out).toContain(`stray.txt (added)`)
      expect(log.some((e) => e.event === "check run" || e.event === "verdict read")).toBe(false)
      expect(log.filter((e) => e.event === "session started").length).toBe(agent.agents().length)
      for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
      nothingAfter(ws, ticket, log)
      // The further process kept the output open; the session still ended as the script did (G-11).
      const ended = log.filter((e) => e.event === "session returned" || e.event === "session failed")
      expect(ended.every((e) => e.event === (how === "return" ? "session returned" : "session failed")), ended.map((e) => e.why).join("; ")).toBe(true)
      // REQ-FLOW-007: each time the framework ended processes, the log holds how many.
      const stopped = log.filter((e) => e.event === "session processes ended")
      expect(stopped.length).toBe(ended.length)
      for (const e of stopped) expect(e.processes).toBeGreaterThanOrEqual(1)
      // Each session printed a line of its own, the number of its further process, kept in a file of its own that its entry names (REQ-FLOW-001; C-13).
      const further = agent.further()
      ended.forEach((e, i) => {
        const text = readFileSync(join(ws.path(), e.printed ?? ""), "utf8")
        further.forEach((pid, j) => expect(text.includes(`further process ${pid}`), `${e.printed} and ${pid}`).toBe(i === j))
      })
    }, 120_000)
  }

  for (const [n, signal, code] of [[4, "SIGINT", 130], [5, "SIGTERM", 143], [6, "SIGHUP", 129]] as const) {
    it(`case ${n}: the run receives the ${signal} signal while the session is at work; no process of it is alive when the run has ended`, async () => {
      const { ws, agent, ticket } = await before()
      agent.does("wait")
      const running = ws.start(["run", ws.root])
      await until(() => agent.further().length === 1 && strayLines(ws.path()).size === 1, 60)
      if (signal === "SIGINT") {
        // While the run holds the ticket, a second run and an answer are each refused, naming the hold's file and its process (REQ-FLOW-001; G-13).
        for (const refused of [await ws.run(""), await ws.answer("yes")]) {
          expect(refused.code, refused.out).toBe(2)
          expect(refused.out).toContain(`holds/${ticket}`)
          expect(refused.out).toContain(String(running.pid))
        }
      }
      process.kill(running.pid, signal)
      const ran: Said = await running.ended
      const log = ws.log()
      expect(ran.code, ran.out).toBe(code)
      for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
      const stopped = log.filter((e) => e.event === "session processes ended")
      expect(stopped).toHaveLength(1)
      expect(stopped[0]?.processes).toBeGreaterThanOrEqual(2)
      expect(stopped[0]?.why).toContain(signal)
      // The run went no further: it ended nowhere, and its hold is left for the next run.
      expect(log.at(-1)?.event).toBe("session processes ended")
      for (const times of strayLines(ws.path()).values()) expect(Math.max(...times)).toBeLessThanOrEqual(time(stopped[0]))
    }, 120_000)
  }

  it("as case 4, the signal received after the script has returned, while the processes of its session are being ended: the run goes no further, whatever the session's outcome", async () => {
    const { ws, agent } = await before()
    // The further process takes no notice of the terminate signal, so ending it takes the grace before the kill signal.
    agent.does("ignore")
    const running = ws.start(["run", ws.root])
    await until(() => agent.agents().length === 1 && agent.further().length === 1 && !alive(agent.agents()[0] ?? -1) && alive(agent.further()[0] ?? -1), 60)
    process.kill(running.pid, "SIGINT")
    const ran: Said = await running.ended
    const log = ws.log()
    expect(ran.code, ran.out).toBe(130)
    expect(log.at(-1)?.event).toBe("session processes ended")
    expect(log.at(-1)?.why).toContain("SIGINT")
    expect(log.some((e) => e.event === "session returned" || e.event === "session failed")).toBe(false)
    for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
  }, 120_000)

  it("case 7: the user kills the run while the session is at work, then starts a run; it ends the session's processes before anything else on the ticket", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("wait")
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
    const ended = events.indexOf("session processes ended")
    expect(events[0]).toBe("run started")
    expect(ended, events.join(", ")).toBe(1)
    expect(log[ended]?.ticket).toBe(ticket)
    expect(log[ended]?.processes).toBeGreaterThanOrEqual(2)
    // Once the session's processes are ended, the next run notes that the run was cut off (REQ-FLOW-007), compares before it commits anything, names what the further process wrote and waits for the user's ruling (REQ-FLOW-003 step 1).
    expect(events.slice(ended + 1, ended + 4)).toEqual(["run cut off", "user asked", "run ended"])
    expect(log[ended + 1]?.ticket).toBe(ticket)
    expect(log.some((e) => e.event === "commit made")).toBe(false)
    expect(Math.max(...(strayLines(ws.path()).get(1) ?? []))).toBeLessThanOrEqual(time(log[ended]))
  }, 120_000)

  it("case 11: as case 7, and before the kill the script changed the settings file and the governing graph and wrote a file, in the workspace's folder; the next run commits nothing, names the three and waits for the user's ruling (C-1)", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("trespass")
    const running = ws.start(["run", ws.root])
    await until(() => existsSync(join(agent.state, "trespassed")) && agent.further().length === 1 && strayLines(ws.path()).size === 1, 60)
    running.kill()
    await running.ended
    const tipsBefore = ws.git(["rev-parse", "main", `stdo/${ticket}`])
    const from = ws.log().length
    agent.does("fail")
    const next = await ws.run("")
    const log = ws.log().slice(from)
    for (const pid of [...agent.agents(), ...agent.further()]) expect(alive(pid), `process ${pid}`).toBe(false)
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("waits for your ruling on what changed while the session on induct-ticket worked")
    expect(next.out).toContain(`.stdo-builder/settings.json (changed)`)
    expect(next.out).toContain(`.stdo-builder/graph.json (changed)`)
    expect(next.out).toContain("a-file-the-session-wrote.txt (added)")
    expect(next.out).toContain("it may have been the session or you")
    // REQ-FLOW-003: the note of the branches, tags and stash was held by the cut-off run alone.
    expect(next.out).toContain("cannot tell what changed then among the repository's branches, tags and stash")
    expect(log.map((e) => e.event)).toEqual(["run started", "session processes ended", "run cut off", "user asked", "run ended"])
    expect(ws.git(["rev-parse", "main", `stdo/${ticket}`])).toBe(tipsBefore)
    // Main holds none of the three.
    expect(ws.git(["ls-tree", "-r", "--name-only", "main"])).not.toContain("a-file-the-session-wrote.txt")
    for (const f of ["settings.json", "graph.json"]) expect(readFileSync(ws.path(".stdo-builder", f), "utf8")).toBe(`${ws.git(["show", `main:.stdo-builder/${f}`])}\n`)
  }, 120_000)

  it("REQ-FLOW-007: as case 11, then a run without the ruling, then the user's yes and a run: the log holds that the run was cut off once, added by the run after the kill", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("trespass")
    const running = ws.start(["run", ws.root])
    await until(() => existsSync(join(agent.state, "trespassed")) && agent.further().length === 1 && strayLines(ws.path()).size === 1, 60)
    running.kill()
    await running.ended
    const killedAt = ws.log().length
    agent.does("fail")
    const next = await ws.run("")
    expect(next.out).toContain("waits for your ruling on what changed")
    const nextRun = ws.log()[killedAt]?.run
    // A run without the ruling asks again, and notes no second cut-off.
    const from2 = ws.log().length
    const again = await ws.run("")
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("waits for your ruling on what changed")
    expect(ws.log().slice(from2).map((e) => e.event)).toEqual(["run started", "user asked", "run ended"])
    // After the user's yes, the next run goes on, and notes no cut-off either.
    const yes = await ws.answer("yes")
    expect(yes.code, yes.out).toBe(0)
    const from3 = ws.log().length
    const third = await ws.run("")
    const log3 = ws.log().slice(from3)
    expect(log3.map((e) => e.event), third.out).toContain("session started")
    expect(log3.some((e) => e.event === "run cut off")).toBe(false)
    const cut = ws.log().filter((e) => e.event === "run cut off")
    expect(cut).toHaveLength(1)
    expect(cut[0]?.run).toBe(nextRun)
    expect(cut[0]?.ticket).toBe(ticket)
  }, 180_000)

  it("REQ-FLOW-007, REQ-FLOW-003: as case 11, but the user ends the session's processes and says yes to what changed before any run: the run after the answer notes the cut-off, once, and says it cannot tell what changed among the branches, tags and stash", async () => {
    const { ws, agent, ticket } = await before()
    agent.does("trespass")
    const running = ws.start(["run", ws.root])
    await until(() => existsSync(join(agent.state, "trespassed")) && agent.further().length === 1 && strayLines(ws.path()).size === 1, 60)
    running.kill()
    await running.ended
    const left = [...agent.agents(), ...agent.further()]
    killAll(left)
    await until(() => left.every((pid) => !alive(pid)), 30)
    agent.does("fail")
    const yes = await ws.answer("yes")
    expect(yes.code, yes.out).toBe(0)
    const from = ws.log().length
    const next = await ws.run("")
    expect(next.out).toContain("cannot tell what changed then among the repository's branches, tags and stash")
    const log = ws.log().slice(from)
    expect(log.slice(0, 2).map((e) => e.event), next.out).toEqual(["run started", "run cut off"])
    expect(log[1]?.ticket).toBe(ticket)
    expect(ws.log().filter((e) => e.event === "run cut off")).toHaveLength(1)
  }, 180_000)
})
