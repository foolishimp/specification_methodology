/**
 * The framework reads the table of processes with `ps` (REQ-FLOW-001). Where
 * `ps` cannot be started, a run is refused before any step, starts no session
 * and commits nothing, and says in one sentence that `ps` was not found, and
 * what to install; an answer is then refused in the same words; neither names
 * a process (REQ-FLOW-003 step 1, REQ-FLOW-006). The machine with no `ps` is a
 * PATH that holds a link to every program of the system's PATH but `ps`, as a
 * clean Debian machine has no `ps` until the package procps is installed.
 *
 * - The first run on a workspace, with a ticket in the backlog: refused before
 *   the ticket is pulled.
 * - With `ps` there again, a run inducts the ticket and waits on the user's
 *   answer. Without it, the answer is refused, and so is the next run, in the
 *   same sentence.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-006
 */
import { existsSync, readdirSync, symlinkSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, temporary, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const cli = build()
afterAll(() => clean())

/** A folder of links to every program on `path` but `ps`, the first of each name, as a PATH of its own. */
function withoutPs(path: string): string {
  const bin = temporary("stdo-builder-no-ps-")
  const linked = new Set<string>(["ps"])
  for (const dir of path.split(":")) {
    if (dir === "" || !existsSync(dir)) continue
    let names: string[] = []
    try {
      names = readdirSync(dir)
    } catch {
      continue
    }
    for (const name of names) {
      if (linked.has(name)) continue
      linked.add(name)
      symlinkSync(join(dir, name), join(bin, name))
    }
  }
  return bin
}

/** The one sentence that `ps` was not found, as the words give it. */
const sentence = (words: string): string | undefined => /`ps` was not found[^.]*\./.exec(words)?.[0]

/** Whether the words name a process, as the framework names one: by its number and when it started. */
const namesAProcess = (words: string): boolean => /the process \d+, started/.test(words)

let ws: Workspace
let first: Said
let firstLog: readonly LogEntry[] = []
let headBefore = ""
let headAfter = ""
let inBacklog = false
let branchesAfter = ""
let answered: Said
let ran: Said
let ranLog: readonly LogEntry[] = []
let tipBefore = ""
let tipAfter = ""

beforeAll(async () => {
  ws = new Workspace(cli)
  await ws.setup()
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  const path = ws.env.PATH ?? ""
  const noPs = withoutPs(path)
  headBefore = ws.git(["rev-parse", "HEAD"])
  let from = ws.log().length
  ws.env.PATH = noPs
  first = await ws.run(S1_FIXTURES)
  ws.env.PATH = path
  firstLog = ws.log().slice(from)
  headAfter = ws.git(["rev-parse", "HEAD"])
  inBacklog = ws.read(".ai-workspace", "tickets", "backlog", `${ticket}.md`) !== undefined
  branchesAfter = ws.git(["branch", "--list", "stdo/*"]).trim()
  // With `ps` there, the run inducts the ticket and waits on the user's answer.
  await ws.run(S1_FIXTURES)
  tipBefore = ws.git(["rev-parse", `stdo/${ticket}`])
  ws.env.PATH = noPs
  answered = await ws.answer("yes")
  from = ws.log().length
  ran = await ws.run(S1_FIXTURES)
  ws.env.PATH = path
  ranLog = ws.log().slice(from)
  tipAfter = ws.git(["rev-parse", `stdo/${ticket}`])
}, 300_000)

describe("where ps cannot be started", () => {
  it("the first run is refused before any step, saying in one sentence that ps was not found and what to install", () => {
    expect(first.code, first.out).toBe(2)
    expect(first.out).toContain("The run is refused before any step")
    expect(sentence(first.out), first.out).toBeDefined()
    expect(sentence(first.out)).toContain("procps")
    expect(namesAProcess(first.out)).toBe(false)
  })

  it("it starts no session, pulls no ticket and commits nothing", () => {
    expect(firstLog.map((e) => e.event)).toEqual(["run started", "run ended"])
    expect(headAfter).toBe(headBefore)
    expect(inBacklog).toBe(true)
    expect(branchesAfter).toBe("")
  })

  it("an answer is refused in the same words, writes nothing and names no process", () => {
    expect(answered.code, answered.out).toBe(2)
    expect(sentence(answered.out)).toBe(sentence(first.out))
    expect(namesAProcess(answered.out)).toBe(false)
  })

  it("the next run, with a ticket active, is refused in the same words, starts no session, commits nothing and names no process", () => {
    expect(ran.code, ran.out).toBe(2)
    expect(sentence(ran.out)).toBe(sentence(first.out))
    expect(namesAProcess(ran.out)).toBe(false)
    expect(ranLog.map((e) => e.event)).toEqual(["run started", "run ended"])
    expect(tipAfter).toBe(tipBefore)
  })
})
