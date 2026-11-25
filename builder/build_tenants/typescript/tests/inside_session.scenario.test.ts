/**
 * A command of the product given from inside a session, on the workspace that
 * session works for or on a folder inside it, is refused, says why and
 * changes nothing; given on a workspace of its own, it works, a run among
 * them, which starts sessions, holds its ticket and ends its sessions'
 * processes, as the product's own tests do (REQ-INTERFACE-001; finding G-3 of
 * the review of release 3.2.0). The session is the script of
 * `script_agent.ts`, started by the command the settings name. The folder
 * inside the workspace is a product the user set up there, `inner`, so each
 * command, were it not refused, would write there: a ticket, a log entry, a
 * run's branch, the settings, a folder set up inside it.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-INTERFACE-001 REQ-FLOW-001
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { alive, killAll, scriptAgent, type Agent } from "./script_agent.js"
import { build, clean, S1_TICKET, temporary, Workspace, write } from "./scenario_driver.js"

let given: { readonly args: readonly string[]; readonly code: number; readonly out: string }[] = []
let ws: Workspace
let other = ""
let agent: Agent
let settingsBefore = ""
let settingsAfter = ""
let innerSetUp = { code: -1, out: "" }
let innerBefore = new Map<string, string>()
let innerAfter = new Map<string, string>()
let innerStatusBefore = ""
let innerStatusAfter = ""

/** Every file under the folder, ignored ones among them, by its path from the folder, with what it holds. */
const filesUnder = (folder: string): Map<string, string> =>
  new Map((readdirSync(folder, { recursive: true }) as string[]).filter((p) => statSync(join(folder, p)).isFile()).sort().map((p) => [p, readFileSync(join(folder, p), "utf8")]))

beforeAll(async () => {
  ws = new Workspace(build())
  await ws.setup()
  // The user sets a second product up in a folder inside the workspace, whose sessions would start nothing, and commits that.
  innerSetUp = await ws.command(["setup", ws.path("inner"), "--name", "Inner"])
  const innerSettings = ws.path("inner", ".stdo-builder", "settings.json")
  const s = JSON.parse(readFileSync(innerSettings, "utf8")) as { agents: Record<string, string[]>; work: string; evaluation: string }
  s.agents.inert = [process.execPath, "-e", ""]
  s.work = "inert"
  s.evaluation = "inert"
  write(innerSettings, `${JSON.stringify(s, null, 2)}\n`)
  ws.git(["add", "--", "inner"])
  ws.git(["commit", "-q", "-m", "the inner product's sessions start nothing"])
  await ws.ticket(S1_TICKET)
  agent = scriptAgent(ws)
  other = join(temporary("stdo-builder-other-"), "other")
  write(join(agent.state, "other"), `${other}\n`)
  agent.does("inside")
  settingsBefore = ws.read(".stdo-builder", "settings.json") ?? ""
  innerBefore = filesUnder(ws.path("inner"))
  innerStatusBefore = ws.git(["status", "--porcelain", "--ignored", "--untracked-files=all", "--", "inner"])
  await ws.run("")
  given = JSON.parse(readFileSync(join(agent.state, "inside.json"), "utf8")) as typeof given
  settingsAfter = ws.read(".stdo-builder", "settings.json") ?? ""
  innerAfter = filesUnder(ws.path("inner"))
  innerStatusAfter = ws.git(["status", "--porcelain", "--ignored", "--untracked-files=all", "--", "inner"])
}, 240_000)

afterAll(() => {
  killAll([...agent.agents(), ...agent.further(), ...agent.inner()])
  clean()
})

describe("a command given from inside a session", () => {
  it("the user set a product up in a folder inside the workspace, with a log of its own", () => {
    expect(innerSetUp.code, innerSetUp.out).toBe(0)
    expect(innerBefore.has(join(".stdo-builder", "settings.json"))).toBe(true)
    expect(innerBefore.get(join(".stdo-builder", "local", "events.log"))).toContain("set-up")
  })

  it("on the workspace it works for, on the product inside it and on a folder inside that, each command is refused and says why", () => {
    const inside = given.filter((g) => !g.args.includes(other))
    // Each of the seven commands on the workspace, and each on the product set up inside it, with set-up of a folder inside that.
    expect(inside.map((g) => g.args[0])).toEqual(["ticket", "run", "answer", "show", "registry", "record-release", "setup", "ticket", "run", "answer", "show", "registry", "record-release", "setup", "setup"])
    expect(inside.slice(0, 7).every((g) => g.args[1] === ws.root)).toBe(true)
    expect(inside.slice(7, 14).every((g) => g.args[1] === ws.path("inner"))).toBe(true)
    expect(inside[14]?.args[1]).toBe(ws.path("inner", "deeper"))
    for (const g of inside) {
      expect(g.code, `${g.args.join(" ")}: ${g.out}`).toBe(2)
      expect(g.out).toContain("given from inside a session")
    }
  })

  it("changes nothing on the workspace: no ticket is written, no second log is started and the settings are as they were", () => {
    expect(settingsAfter).toBe(settingsBefore)
    const log = ws.log()
    expect(log.filter((e) => e.event === "ticket written")).toHaveLength(1)
    expect(log.filter((e) => e.event === "answer written" || e.event === "release recorded" || e.event === "set-up")).toHaveLength(1)
    expect(log.filter((e) => e.event === "run started")).toHaveLength(1)
    // The one ticket on the board is the user's.
    expect(ws.board().backlog.length + ws.board().active.length).toBe(1)
  })

  it("changes nothing in the folder inside it: its files, its log, its board and its settings are as they were, no run made a branch, and nothing is set up inside it", () => {
    expect([...innerAfter.keys()]).toEqual([...innerBefore.keys()])
    for (const [path, text] of innerBefore) expect(innerAfter.get(path), path).toBe(text)
    expect(innerStatusAfter).toBe(innerStatusBefore)
    expect(existsSync(ws.path("inner", ".ai-workspace", "tickets"))).toBe(false)
    expect(existsSync(ws.path("inner", "deeper"))).toBe(false)
    // The only ticket's branch is the workspace's own ticket's.
    const own = [...ws.board().backlog, ...ws.board().active].map((t) => `stdo/${t}`)
    const branches = ws.git(["for-each-ref", "--format=%(refname:short)", "refs/heads/stdo/"]).split("\n").filter((l) => l !== "")
    for (const b of branches) expect(own).toContain(b)
  })

  it("on a workspace of its own, the product's commands work from inside the session, a run among them", () => {
    const outside = given.filter((g) => g.args.includes(other))
    expect(outside.map((g) => g.args[0])).toEqual(["setup", "ticket", "run", "show"])
    // Set-up, the ticket and show work; the run is no refusal: it starts its sessions, whose agent writes no triage, and stops when they fail the same checks twice.
    expect(outside.map((g) => g.code), outside.map((g) => g.out).join("\n")).toEqual([0, 0, 1, 0])
    expect(outside[2]?.out).toContain("could not close")
  })

  it("the run on the other workspace ended its own sessions' processes, and not the session it was given from", () => {
    const inner = agent.inner()
    expect(inner.length).toBeGreaterThanOrEqual(1)
    for (const pid of inner) expect(alive(pid), `process ${pid}`).toBe(false)
    const log = readFileSync(join(other, ".stdo-builder", "local", "events.log"), "utf8").split("\n").filter((l) => l !== "").map((l) => JSON.parse(l) as { event: string; processes?: number })
    const ended = log.filter((e) => e.event === "session processes ended")
    expect(ended.length).toBe(inner.length)
    // The session it was given from went on, and wrote what it was given after that run.
    expect(given.at(-1)?.args).toEqual(["show", other])
  })
})
