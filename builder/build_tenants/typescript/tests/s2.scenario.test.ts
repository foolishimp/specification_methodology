/**
 * Scenario S2, interrupt and resume: S1 under way with the code step running;
 * S1's term is the specification and then the build, so that is the build,
 * which writes the design, the tests and the code (REQ-METHOD-006). Its
 * working session is a process of its own, apart from the framework's: the
 * agent the settings name for it is a script that writes the stand-in's files
 * for that step and then waits. The driver places a marker beside the files
 * the session has written, kills the framework and the session, each by the
 * number of its process, and the user starts a run.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-007 REQ-METHOD-006
 */
import { readFileSync, rmSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { existsSync } from "node:fs"
import { answersOf, resolvedOnMain, build, clean, gated, onMain, S1_ASKED, S1_ASSETS, s1ToRequirements, temporary, testsPass, until, Workspace, write, wroteAll, type LogEntry, type Said } from "./scenario_driver.js"

const MARKER = "build_tenants/main/code/MARKER"
let ws: Workspace
let ticket = ""
let killedAt = 0
const said: Said[] = []
let last: Said
let log: LogEntry[] = []

beforeAll(async () => {
  ws = new Workspace(build())
  // The build's working session, once it has written its files, waits at a gate the driver never opens.
  const fixtures = gated(join(temporary("stdo-builder-gate-"), "never"))
  await ws.setup()
  // The build's working session is a process of its own: a script the settings name for it, which writes the stand-in's files for the step, notes its number and waits.
  const state = temporary("stdo-builder-s2-")
  const script = join(state, "build.mjs")
  writeFileSync(script, `
    import { cpSync, writeFileSync } from "node:fs"
    const [files, pid] = process.argv.slice(2)
    cpSync(files, process.cwd(), { recursive: true })
    writeFileSync(pid, String(process.pid))
    setInterval(() => {}, 1000)
  `)
  const settings = ws.path(".stdo-builder", "settings.json")
  const s = JSON.parse(readFileSync(settings, "utf8")) as { agents: Record<string, string[]>; vectors?: Record<string, { work?: string }> }
  s.agents.builder = [process.execPath, script, join(fixtures, "write-build", "work", "files"), join(state, "pid")]
  s.vectors = { ...s.vectors, "write-build": { work: "builder" } }
  writeFileSync(settings, `${JSON.stringify(s, null, 2)}\n`)
  // Set-up again changes nothing; the first run commits the settings as the user's change on main.
  const before = await s1ToRequirements(ws, fixtures)
  ticket = before.ticket
  const running = ws.start(["run", ws.root])
  // The kill waits until the session has written every file it writes.
  await until(() => wroteAll(fixtures, "write-build", "work", ws.path()) && existsSync(join(state, "pid")), 60)
  write(ws.path(MARKER), "placed by the driver\n")
  running.kill()
  await running.ended
  process.kill(Number(readFileSync(join(state, "pid"), "utf8")), "SIGKILL")
  killedAt = ws.log().length
  rmSync(join(fixtures, "write-build", "work", "gate"))
  said.push(await ws.run(fixtures), await ws.answer("yes"), await ws.run(fixtures))
  last = await ws.run(fixtures)
  log = ws.log()
}, 180_000)

afterAll(clean)

describe("S2 Interrupt and resume", () => {
  it("the run after the kill goes on from the interrupted step, starting no working session on it", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0])
    expect(said[0]?.out).toContain("waits for your answer on write-build")
    const after = log.slice(killedAt)
    expect(after.some((e) => e.event === "session started" && e.kind === "work")).toBe(false)
    expect(after.some((e) => e.event === "session started" && e.vector === "write-build" && e.kind === "evaluation")).toBe(true)
  })

  it("REQ-FLOW-007: the log holds that the interrupted run was cut off, added by the run after it", () => {
    const after = log.slice(killedAt)
    const next = after.findIndex((e) => e.event === "run started")
    expect(next, after.map((e) => e.event).join(", ")).toBeGreaterThanOrEqual(0)
    const run = after[next]?.run
    const cut = after.findIndex((e) => e.event === "run cut off")
    expect(cut, after.map((e) => e.event).join(", ")).toBeGreaterThan(next)
    expect(after[cut]?.ticket).toBe(ticket)
    expect(after[cut]?.run).toBe(run)
    // It is added before that run starts any session, and only once.
    const firstSession = after.findIndex((e) => e.event === "session started")
    expect(firstSession).toBeGreaterThan(cut)
    expect(log.filter((e) => e.event === "run cut off")).toHaveLength(1)
    expect(log.slice(0, killedAt).some((e) => e.event === "run cut off")).toBe(false)
  })

  it("as S1: every question asked is one the graph declares", () => {
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(S1_ASKED)
  })

  it("as S1: every vector that takes part is closed, and nothing is left to build", () => {
    // The steps S1 takes are closed on the branch; on main, where the six take part, they read the same acceptance (D164), and a run finds nothing to build.
    const closed = new Set(log.filter((e) => e.event === "vector closed" && e.ticket === ticket).map((e) => e.vector))
    for (const v of S1_ASKED) expect(closed.has(v), v).toBe(true)
    expect(last.out).toContain("there is nothing to build")
  })

  it("as S1: the workspace holds every asset, tests and code that passes them, and the answers", () => {
    const files = onMain(ws)
    for (const path of S1_ASSETS) expect(files, path).toContain(path)
    for (const name of answersOf(S1_ASKED)) expect(resolvedOnMain(ws, name).length, name).toBeGreaterThan(0)
    expect(testsPass(ws)).toBe(true)
  })

  it("as S1: the ticket lies in the done lane on main and its branch is merged", async () => {
    expect(ws.board()).toEqual({ backlog: [], active: [], done: [ticket] })
    expect(await ws.gitSays(["merge-base", "--is-ancestor", `stdo/${ticket}`, "main"])).toBe(0)
  })

  it("as S1, apart from the one interrupted step: the event log names every step", () => {
    const named = new Set(log.flatMap((e) => (e.commit === undefined ? [] : [e.commit])))
    for (const c of ws.git(["rev-list", "main"]).trim().split("\n")) expect(named.has(c), c).toBe(true)
    const started = log.filter((e) => e.event === "session started").length
    const ended = log.filter((e) => e.event === "session returned" || e.event === "session failed").length
    expect(ended).toBe(started - 1)
    expect(log.filter((e) => e.event === "run ended")).toHaveLength(log.filter((e) => e.event === "run started").length - 1)
  })

  it("the marker is still there", () => {
    expect(ws.git(["show", `main:${MARKER}`])).toBe("placed by the driver\n")
    expect(ws.read(MARKER)).toBe("placed by the driver\n")
  })
})
