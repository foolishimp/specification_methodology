/**
 * A session that removes what git ignores, or stashes it all, removes nothing
 * the framework needs to tell what it changed (the ticket's bug items 1a to
 * 1f and 2; REQ-ALG-008, REQ-FLOW-001, REQ-FLOW-003, REQ-FLOW-005,
 * REQ-FLOW-006, REQ-FLOW-007). Every session is started by the agent's
 * command as a process of its own, the fixture agent of `script_agent.ts`,
 * which writes S1's fixtures; each workspace, and the larger repository of
 * case d, is a repository of its own under the system's temporary folder, and
 * every cleaning is given there alone. Each case is a workspace of its own,
 * run side by side.
 *
 * The specification's working session, at a gate, has set the command of a
 * check in the graph to `true`, added a line to `AGENTS.md` and written a file
 * of its own outside every asset, the trio, with:
 *
 * - a: `git clean -fdx` in the workspace's folder as its first act; it
 *   returns (REQ-ALG-008 acceptance 9). Then e: with the ruling awaited, the
 *   user gives `git clean -fdX` and starts a run (REQ-FLOW-003).
 * - b: `git clean -fdX` as its last act; and `git stash --all` as its first
 *   act, the stash never taken back (REQ-ALG-008 acceptance 10).
 * - c: the session of a still at work when the run receives the interrupt
 *   signal, and when the run is killed; then a run (REQ-FLOW-003).
 * - d: the case a where the product is one folder of a larger repository and
 *   the cleaning is given at the repository's top (REQ-ALG-008 acceptance 11).
 * - f: the identities kept from the session's start are removed from where
 *   they lie, and the session returns; the user says yes, and a run follows
 *   (REQ-ALG-008 acceptance 12).
 * - 2: the session removes the event log (REQ-FLOW-003, REQ-FLOW-007).
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-008 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007
 */
import { execFileSync } from "node:child_process"
import { existsSync, mkdirSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { BY_HAND } from "../src/flows/commit.js"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { build, clean, S1_FIXTURES, S1_TICKET, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const AGENTS = "# Instructions for every agent\n\nKeep to the brief.\n"
const AT = "write-specification.work"
const OWN = "a-file-of-the-session.txt"
/** The three files the trio changes, as the question names them. */
const TRIO = [".stdo-builder/graph.json (changed)", "AGENTS.md (changed)", `${OWN} (added)`]
/** What the specification's step writes, which the question on the trio does not name, by path. */
const STEP = ["specification/INTENT.md", "specification/PRODUCT.md", "specification/requirements/HELLO.md"]
/** The sentence where the commit the session started from stands in for the identities from its start (REQ-FLOW-006 step 1, D255). */
const MISSING = "The identities taken at the start of the session on write-specification are missing, so the framework asks you about every file that differs from the commit the session started from."

/** Sets the command of every check of the graph that runs a command to `true`, adds a line to `AGENTS.md` and writes a file of no asset. */
const trio = [
  `${JSON.stringify(process.execPath)} -e 'const fs = require("fs"); const p = ".stdo-builder/graph.json"; const g = JSON.parse(fs.readFileSync(p, "utf8")); for (const n of g.nodes) for (const c of n.checks ?? []) if (c.run.kind === "command") c.run.argv = ["true"]; fs.writeFileSync(p, JSON.stringify(g, null, 2) + "\\n")'`,
  "echo 'a line the session added' >> AGENTS.md",
  `echo 'written while the session worked' > ${OWN}`
].join("\n")
const STASH = "git -c user.name=s -c user.email=s@s stash --all -q"

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
}

/** A product set up, in a repository of its own or, with `within`, in a folder of a larger one, the fixture agent named, `AGENTS.md` written, the ticket written, and the induction answered. */
async function begun(cli: string, within?: string): Promise<Case> {
  const ws = new Workspace(cli, undefined, within === undefined ? [] : [within])
  if (within !== undefined) {
    execFileSync("git", ["init", "-q", "-b", "main", ws.top], { env: ws.env })
    write(join(ws.top, "README"), "a larger repository\n")
    execFileSync("git", ["-C", ws.top, "add", "-A"], { env: ws.env })
    execFileSync("git", ["-C", ws.top, "commit", "-qm", "the repository's own file"], { env: ws.env })
    mkdirSync(ws.root, { recursive: true })
  }
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  writeFileSync(ws.path("AGENTS.md"), AGENTS)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  const first = await ws.run("")
  expect(first.out).toContain("waits for your answer on induct-ticket")
  await ws.answer("yes")
  return { ws, agent, ticket }
}

const tips = (c: Case): string => c.ws.git(["rev-parse", "main", `stdo/${c.ticket}`])
/** The files a question names, by the lines that name them, each with how it changed. */
const named = (out: string): readonly string[] => out.split("\n").flatMap((l) => (/^- .+ \((added|changed|removed)\)$/.test(l) ? [l.slice(2)] : [])).sort()
/** The same, by path alone. */
const paths = (out: string): readonly string[] => named(out).map((l) => l.replace(/ \((added|changed|removed)\)$/, ""))
/** The commits on main and on the ticket's branch since `tipsThen` whose message says they hold what the user changed by hand. */
const byHandSince = (c: Case, tipsThen: string): string => {
  const [main = "", branch = ""] = tipsThen.split("\n")
  return c.ws.git(["log", "--format=%H", "--fixed-strings", `--grep=${BY_HAND}`, `${main}..main`, `${branch}..stdo/${c.ticket}`]).trim()
}

/** The specification's session, started by a run, at its gate: the tips then, and the run. */
async function atGate(c: Case, first: string | undefined, then: string): Promise<{ readonly running: ReturnType<Workspace["start"]>; readonly tipsAtWork: string; readonly logBefore: readonly LogEntry[] }> {
  if (first !== undefined) c.agent.first(AT, first)
  c.agent.does(AT, then)
  c.agent.gate(AT)
  const logBefore = c.ws.log()
  const running = c.ws.start(["run", c.ws.root])
  await until(() => c.agent.waiting(AT), 60)
  return { running, tipsAtWork: tips(c), logBefore }
}

interface Returned { readonly c: Case; readonly waited: Said; readonly tipsAtWork: string; readonly tipsWaited: string; readonly logBefore: readonly LogEntry[] }

/** The session of `atGate` let go: it returns, and the run ends. */
async function returned(c: Case, first: string | undefined, then: string): Promise<Returned> {
  const g = await atGate(c, first, then)
  c.agent.open(AT)
  const waited = await g.running.ended
  return { c, waited, tipsAtWork: g.tipsAtWork, tipsWaited: tips(c), logBefore: g.logBefore }
}

interface Cut { readonly c: Case; readonly cut: Said; readonly next: Said; readonly from: number; readonly tipsAtWork: string; readonly tipsNext: string }

/** The session of case a, at work when the run is sent the signal or killed; then a run. */
async function cutOff(c: Case, how: "SIGINT" | "kill"): Promise<Cut> {
  const g = await atGate(c, "git clean -fdx -q\n", trio)
  if (how === "kill") g.running.kill()
  else process.kill(g.running.pid, "SIGINT")
  const cut = await g.running.ended
  const from = c.ws.log().length
  const next = await c.ws.run("")
  return { c, cut, next, from, tipsAtWork: g.tipsAtWork, tipsNext: tips(c) }
}

let a: Returned & { again: Said; tipsAgain: string }
let lastClean: Returned
let stash: Returned
let interrupted: Cut
let killed: Cut
let nested: Returned
let lost: Returned & { ruled: Said; next: Said }
let logGone: Returned

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      const r = await returned(await begun(cli), "git clean -fdx -q\n", trio)
      // e: a ruling is awaited; the user cleans what git ignores and starts a run.
      r.c.ws.git(["clean", "-fdX", "-q"])
      const again = await r.c.ws.run("")
      a = { ...r, again, tipsAgain: tips(r.c) }
    })(),
    (async () => {
      lastClean = await returned(await begun(cli), undefined, `${trio}\ngit clean -fdX -q\n`)
    })(),
    (async () => {
      stash = await returned(await begun(cli), `${STASH}\n`, trio)
    })(),
    (async () => {
      interrupted = await cutOff(await begun(cli), "SIGINT")
    })(),
    (async () => {
      killed = await cutOff(await begun(cli), "kill")
    })(),
    (async () => {
      nested = await returned(await begun(cli, "product"), "cd \"$(git rev-parse --show-toplevel)\" && git clean -fdx -q\n", trio)
    })(),
    (async () => {
      const c = await begun(cli)
      const r = await returned(c, undefined, `rm -f '${c.ws.notes("started", `${c.ticket}.json`)}'\n`)
      const ruled = await c.ws.answer("yes")
      const next = await c.ws.run("")
      lost = { ...r, ruled, next }
    })(),
    (async () => {
      const c = await begun(cli)
      logGone = await returned(c, undefined, "rm -f \"$ROOT/.stdo-builder/local/events.log\"\n")
    })()
  ])
}, 600_000)

afterAll(clean)

/** The run waits for a ruling that names the trio's three files and none of what the step writes, and commits nothing. */
function asksOnTheTrio(r: { readonly c: Case; readonly out: string; readonly code: number }, tipsBefore: string, tipsAfter: string): void {
  expect(r.code, r.out).toBe(0)
  expect(r.out).toContain("waits for your ruling on what changed while the session on write-specification worked")
  expect(named(r.out)).toEqual([...TRIO].sort())
  for (const p of STEP) expect(r.out).not.toContain(`${p} (`)
  // Neither sentence that says a commit stood in for the identities (REQ-FLOW-006 step 1).
  expect(r.out).not.toContain("are missing, so the framework asks you about every file")
  expect(tipsAfter).toBe(tipsBefore)
}

describe("bug item 1a: the session gives git clean -fdx in the workspace's folder as its first act (REQ-ALG-008 acceptance 9)", () => {
  it("the run asks for a ruling that names the three files and none of what the step writes, and commits nothing", () => {
    asksOnTheTrio({ c: a.c, ...a.waited }, a.tipsAtWork, a.tipsWaited)
  })

  it("the identities kept from the session's start lie under git's own directory for the workspace's folder, which the cleaning does not reach (REQ-FLOW-001)", () => {
    expect(a.c.ws.notes()).toContain(`${a.c.ws.git(["rev-parse", "--absolute-git-dir"]).trim()}/`)
    expect(existsSync(a.c.ws.path(".stdo-builder", "local", "started"))).toBe(false)
    expect(existsSync(a.c.ws.notes("started", `${a.c.ticket}.json`))).toBe(true)
  })
})

describe("bug item 1e: a ruling is awaited, and the user gives git clean -fdX and starts a run (REQ-FLOW-003)", () => {
  it("the run asks again, naming the same files, and commits nothing", () => {
    asksOnTheTrio({ c: a.c, ...a.again }, a.tipsWaited, a.tipsAgain)
    expect(named(a.again.out)).toEqual(named(a.waited.out))
  })
})

describe("bug item 1b: git clean -fdX as the session's last act, and git stash --all as its first (REQ-ALG-008 acceptance 10)", () => {
  it("with git clean -fdX last, the run asks for a ruling that names the three files and none of what the step writes, and commits nothing", () => {
    asksOnTheTrio({ c: lastClean.c, ...lastClean.waited }, lastClean.tipsAtWork, lastClean.tipsWaited)
  })

  it("with git stash --all first, the stash never taken back, the run asks the same, and names the stash as changed while the session worked", () => {
    asksOnTheTrio({ c: stash.c, ...stash.waited }, stash.tipsAtWork, stash.tipsWaited)
    expect(stash.waited.out).toContain("the stash (added)")
  })
})

describe("bug item 1c: the session of 1a is at work when the run receives the interrupt signal, or is killed (REQ-FLOW-003)", () => {
  for (const [label, get, code] of [["the interrupt signal", () => interrupted, 130], ["the run killed", () => killed, 128]] as const) {
    it(`${label}: the next run ends the session's processes, asks for the same ruling, and commits nothing as what the user changed by hand`, () => {
      const k = get()
      expect(k.cut.code, k.cut.out).toBe(code)
      asksOnTheTrio({ c: k.c, ...k.next }, k.tipsAtWork, k.tipsNext)
      const log = k.c.ws.log()
      expect(log.some((e) => e.event === "commit made" && e.why === "what the user left uncommitted")).toBe(false)
      expect(log.slice(k.from).some((e) => e.event === "run cut off" && e.ticket === k.c.ticket)).toBe(true)
      // The session's own process was ended: by the run that received the signal, or by the next one.
      expect(log.some((e) => e.event === "session processes ended" && e.ticket === k.c.ticket && (e.processes ?? 0) >= 1)).toBe(true)
    })
  }
})

describe("bug item 1d: the product is one folder of a larger repository, and the cleaning is given at the repository's top (REQ-ALG-008 acceptance 11)", () => {
  it("the run asks for a ruling that names the three files and none of what the step writes, and commits nothing", () => {
    asksOnTheTrio({ c: nested.c, ...nested.waited }, nested.tipsAtWork, nested.tipsWaited)
    expect(nested.c.ws.within.length).toBe(1)
  })
})

describe("bug item 1f: the identities kept from the session's start are removed from where they lie, and the session returns (REQ-ALG-008 acceptance 12, REQ-FLOW-005, REQ-FLOW-006)", () => {
  it("the run says that they are missing, puts every file that differs from the commit the session started from to the user, what the step writes among them, and commits nothing", () => {
    const { waited } = lost
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain(MISSING)
    expect(waited.out.split(MISSING)).toHaveLength(2)
    expect(waited.out).toContain("waits for your ruling on what changed while the session on write-specification worked")
    expect(paths(waited.out)).toEqual([...STEP].sort())
    expect(lost.tipsWaited).toBe(lost.tipsAtWork)
  })

  it("after the user's yes, they are committed with the step, and the work goes on", () => {
    const { ruled, next, c } = lost
    expect(ruled.code, ruled.out).toBe(0)
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("waits for your answer on write-specification")
    for (const p of STEP) expect(c.ws.git(["log", "-1", "--format=%s", `stdo/${c.ticket}`, "--", p]).trim()).toBe("the result of the step on write-specification")
    expect(byHandSince(c, lost.tipsAtWork)).toBe("")
  })
})

describe("bug item 2: a session removes the event log while the run works (REQ-FLOW-003, REQ-FLOW-007)", () => {
  it("the new log's first entry says that a new log was started, with the release in force, and the run says so once", () => {
    const { waited, c, logBefore } = logGone
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain("waits for your answer on write-specification")
    const log = c.ws.log()
    const run = log[0]?.run
    expect(log[0]?.event).toBe("new log started")
    expect(log[0]?.release).toBe(logBefore.find((e) => e.event === "run started")?.release)
    expect(log[0]?.release).toBeDefined()
    expect(log.filter((e) => e.event === "new log started")).toHaveLength(1)
    expect(log.at(-1)).toMatchObject({ event: "run ended", run })
    expect(waited.out.split("was not found")).toHaveLength(2)
    expect(waited.out).toContain("The event log this run was adding to was not found; this run started a new one, at .stdo-builder/local/events.log.")
  })

  it("so it is where a session cleans what git ignores: the new log begins with the entry, once", () => {
    for (const r of [lastClean, stash, nested]) {
      const log = r.c.ws.log()
      expect(log[0]?.event, JSON.stringify(log[0])).toBe("new log started")
      expect(log.filter((e) => e.event === "new log started")).toHaveLength(1)
      expect(r.waited.out.split("was not found")).toHaveLength(2)
    }
  })
})
