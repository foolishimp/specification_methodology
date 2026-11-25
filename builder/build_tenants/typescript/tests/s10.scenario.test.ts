/**
 * Scenario S10, two agents: the workspace S1 left; the user sets a second
 * agent for the evaluations, deletes the code, starts a run and answers each
 * question. The stand-in stands in for both, and the log names which agent the
 * settings gave each session. The stand-in's code differs from the first by a
 * comment, as a new session's would (D41).
 *
 * Beside it, REQ-PARAM-003's acceptance: a run the settings limit to three
 * sessions ends as stopped after the third. S1's term is the specification and then the build (REQ-METHOD-006),
 * so the run writes the build, its evaluation says no, and the build is
 * written again: the third session.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-005 REQ-PARAM-003
 */
import { readFileSync, rmSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, fixturesLike, S1_FIXTURES, s1ToRequirements, s1Whole, testsPass, ticketFields, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const SETTINGS = [".stdo-builder", "settings.json"] as const

let cli = ""
let ws: Workspace
let first = ""
let mainBefore = ""
const said: Said[] = []
let log: LogEntry[] = []

beforeAll(async () => {
  cli = build()
  ws = new Workspace(cli)
  first = (await s1Whole(ws, S1_FIXTURES)).ticket
  mainBefore = ws.git(["rev-parse", "main"]).trim()
  // The one setting: the agent for the evaluations.
  const settings = JSON.parse(readFileSync(ws.path(...SETTINGS), "utf8")) as Record<string, unknown>
  writeFileSync(ws.path(...SETTINGS), `${JSON.stringify({ ...settings, evaluation: "codex" }, null, 2)}\n`)
  rmSync(ws.path("build_tenants", "main", "code"), { recursive: true })
  const again = fixturesLike((f) => {
    write(join(f, "write-code", "work", "files", "build_tenants", "main", "code", "hello.sh"), "#!/bin/sh\n# Hello, built again. Carries out REQ-HELLO-001.\nprintf 'hello, world\\n'\n")
  })
  const from = ws.log().length
  said.push(await ws.run(again), await ws.answer("yes"), await ws.run(again))
  log = ws.log().slice(from)
}, 180_000)

afterAll(clean)

describe("S10 Two agents", () => {
  it("as S9: the code is there again and passes the tests that passed before", () => {
    expect(said.map((s) => s.code), said.map((s) => s.out).join("\n---\n")).toEqual([0, 0, 0])
    expect(ws.git(["ls-tree", "-r", "--name-only", "main", "build_tenants/main/code"]).trim()).toBe("build_tenants/main/code/hello.sh")
    expect(ws.git(["diff", "--quiet", `stdo/${first}`, "main", "--", "build_tenants/main/tests"])).toBe("")
    expect(testsPass(ws)).toBe(true)
  })

  it("as S9: the only vector a session was started on is the one that writes the code, and the user was asked only to accept the built product", () => {
    expect([...new Set(log.filter((e) => e.event === "session started").map((e) => e.vector))]).toEqual(["write-code"])
    expect(log.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-code"])
  })

  it("as S9: the run wrote the simplest ticket, which lies in the done lane on main", () => {
    const board = ws.board()
    expect(board.backlog).toEqual([])
    expect(board.active).toEqual([])
    const simplest = board.done.filter((t) => t !== first)
    expect(simplest).toHaveLength(1)
    expect(ticketFields(ws.git(["show", `main:.ai-workspace/tickets/completed/${simplest[0]}.md`])).get("simplest")).toBe("yes")
  })

  it("the event log shows the code written by the first agent and its evaluation made by the second", () => {
    const started = log.filter((e) => e.event === "session started" && e.vector === "write-code")
    expect(started.map((e) => [e.kind, e.agent])).toEqual([["work", "stand-in for claude"], ["evaluation", "stand-in for codex"]])
  })

  it("nothing but the one setting and the code was changed by hand", () => {
    const byHand = log.filter((e) => e.event === "commit made" && e.why === "what the user left uncommitted").map((e) => e.commit ?? "")
    expect(byHand).toHaveLength(1)
    expect(ws.git(["rev-parse", `${byHand[0]}^`]).trim()).toBe(mainBefore)
    const changed = ws.git(["diff", "--name-only", mainBefore, byHand[0] ?? ""]).trim().split("\n")
    expect(changed).toEqual(["build_tenants/main/code/hello.sh", ".stdo-builder/settings.json"].sort())
    const settings = ws.git(["diff", "--unified=0", mainBefore, byHand[0] ?? "", "--", ".stdo-builder/settings.json"]).split("\n").filter((l) => /^[-+] /.test(l))
    // The settings name the fields each agent reports after the evaluation's agent, so its line ends with a comma (D91).
    expect(settings).toEqual(['-  "evaluation": "claude",', '+  "evaluation": "codex",'])
  })
})

describe("REQ-PARAM-003 limits on a step and on a run", () => {
  let limited: Said
  let started: readonly LogEntry[] = []
  beforeAll(async () => {
    const w = new Workspace(cli)
    const no = fixturesLike((f) => write(join(f, "write-build", "evaluation", "files", "build_tenants", "main", "evaluations", "build", "verdict.json"), '{"verdict": "no"}\n'))
    await s1ToRequirements(w, no)
    const settings = JSON.parse(readFileSync(w.path(...SETTINGS), "utf8")) as Record<string, unknown>
    writeFileSync(w.path(...SETTINGS), `${JSON.stringify({ ...settings, limits: { sessions: 3 } }, null, 2)}\n`)
    const from = w.log().length
    limited = await w.run(no)
    started = w.log().slice(from).filter((e) => e.event === "session started")
  }, 180_000)

  it("a run limited to three sessions ends as stopped after the third", () => {
    expect(limited.code, limited.out).toBe(1)
    expect(limited.out).toContain("the run reached the limit the settings set, 3 sessions")
    expect(started.map((e) => [e.vector, e.kind])).toEqual([["write-build", "work"], ["write-build", "evaluation"], ["write-build", "work"]])
  })
})
