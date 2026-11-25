/**
 * Where the identities taken at a session's start cannot serve, the commit the
 * session started from stands in for them, so what a session committed of its
 * own is asked about (ticket 261125-014851-46cb; REQ-ALG-008, its last four
 * acceptance lines; REQ-FLOW-003 step 1, REQ-FLOW-005 step 3, REQ-FLOW-006
 * step 1). Every session is started by the agent's command as a process of
 * its own, the fixture agent of `script_agent.ts`, which writes S1's fixtures;
 * each workspace is a repository of its own under the system's temporary
 * folder, and every commit, `git gc` and `git prune` a session gives is given
 * there alone. Each case is a workspace of its own, run side by side.
 *
 * - gc: the build's evaluating session adds a line to `AGENTS.md`, which its
 *   step does not write, gives `git add -A .` and `git commit` in the
 *   workspace's folder, then `git gc --prune=now`.
 * - prune: the same, with `git prune --expire=now` in place of the gc.
 * - killed: the same as gc, and the run is killed while that session works,
 *   after it has committed and pruned; then a run.
 * - removed: the specification's working session writes a file its step does
 *   not write, commits what it changed, and the record of its start is then
 *   removed from git's own directory.
 * - amended: the build's evaluating session adds a line to `AGENTS.md`, puts
 *   what it changed into the commit it started from with `git commit
 *   --amend`, then gives `git reflog expire --expire=now --all` and `git gc
 *   --prune=now`, so git no longer holds the commit the session started from.
 *   The run that started it knows that commit and no other stands in: the
 *   stand-in cannot be compared, and the flow fails (REQ-ALG-008, its law
 *   that the framework never goes on without the user's ruling; ticket item 3).
 *
 * @uses C14 C5 C6
 * @is REQ-ALG-008 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-006
 */
import { readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { build, clean, S1_FIXTURES, S1_TICKET, until, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const AGENTS = "# Instructions for every agent\n\nKeep to the brief.\n"
const EVALUATION = "write-build.evaluation"
const WORK = "write-specification.work"
const OWN = "notes-of-the-session.txt"
/** The one sentence where the commit the session started from stands in (REQ-FLOW-006 step 1). */
const startedFrom = (vector: string): string =>
  `The identities taken at the start of the session on ${vector} are missing, so the framework asks you about every file that differs from the commit the session started from.`
const COMMIT = "git add -A . && git -c user.name=s -c user.email=s@s commit -qm \"the session's own commit\""

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
}

/** A product set up, the fixture agent named, `AGENTS.md` written, and the ticket written. */
async function begun(cli: string): Promise<Case> {
  const ws = new Workspace(cli)
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  writeFileSync(ws.path("AGENTS.md"), AGENTS)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent, ticket }
}

/** S1 driven by the fixture agent up to the user's yes on the specification. */
async function toBuild(c: Case): Promise<void> {
  for (let i = 0; i < 2; i++) {
    const ran = await c.ws.run("")
    expect(ran.out).toContain("waits for your answer")
    await c.ws.answer("yes")
  }
}

/** A shell line that writes to `<state>/start-tree` whether git still holds the tree kept at the session's start, as the record names it. */
const treeHeld = (c: Case): string => {
  const record = c.ws.notes("started", `${c.ticket}.json`)
  const read = `${JSON.stringify(process.execPath)} -e 'process.stdout.write(JSON.parse(require("fs").readFileSync(process.argv[1], "utf8")).tree)' '${record}'`
  return `t=$(${read})\nif git cat-file -e "$t^{tree}" 2>/dev/null; then echo held; else echo gone; fi > '${join(c.agent.state, "start-tree")}'\n`
}

/** A shell line that writes to `<state>/start-commit` whether git still holds the commit the session started from, as the record names it. */
const commitHeld = (c: Case): string => {
  const record = c.ws.notes("started", `${c.ticket}.json`)
  const read = `${JSON.stringify(process.execPath)} -e 'process.stdout.write(JSON.parse(require("fs").readFileSync(process.argv[1], "utf8")).commit)' '${record}'`
  return `s=$(${read})\nif git cat-file -e "$s^{commit}" 2>/dev/null; then echo held; else echo gone; fi > '${join(c.agent.state, "start-commit")}'\n`
}

/** The evaluating session's script: a line added to `AGENTS.md`, what it changed committed in the folder, and git's store cleaned by `clean`. */
const evaluating = (c: Case, cleanStore: string): string =>
  `echo 'a line the evaluation added' >> AGENTS.md\n${COMMIT}\n${cleanStore}\n${treeHeld(c)}`

/** The evaluating session's script where what it changed goes into the commit it started from, and git's store is cleaned of that commit. */
const amending = (c: Case): string =>
  `echo 'a line the evaluation added' >> AGENTS.md\ngit add -A . && git -c user.name=s -c user.email=s@s commit -q --amend -m "the session's own commit"\ngit reflog expire --expire=now --all\ngit gc --prune=now --quiet\n${commitHeld(c)}`

/** The entries of the log after the last `session started` of this kind. */
const afterStart = (log: readonly LogEntry[], kind: "work" | "evaluation"): readonly LogEntry[] => {
  const i = log.map((e) => e.event === "session started" && e.kind === kind).lastIndexOf(true)
  return i < 0 ? [] : log.slice(i + 1)
}

/** The message of the ticket's branch's tip: the session's own commit, where the framework committed nothing after it. */
const tipMessage = (c: Case): string => c.ws.git(["log", "-1", "--format=%s", `stdo/${c.ticket}`]).trim()

interface Asked { readonly c: Case; readonly asked: Said; readonly log: readonly LogEntry[] }

let gc: Asked
let pruned: Asked
let killed: Asked & { readonly cut: Said }
let removed: Asked
let amended: Asked

/** The build's evaluating session gives `cleanStore` after its commit; the run that started it ends. */
async function evaluatedThen(cli: string, cleanStore: string): Promise<Asked> {
  const c = await begun(cli)
  c.agent.does(EVALUATION, evaluating(c, cleanStore))
  await toBuild(c)
  const asked = await c.ws.run("")
  return { c, asked, log: c.ws.log() }
}

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      gc = await evaluatedThen(cli, "git gc --prune=now --quiet")
    })(),
    (async () => {
      pruned = await evaluatedThen(cli, "git prune --expire=now")
    })(),
    (async () => {
      const c = await begun(cli)
      c.agent.does(EVALUATION, evaluating(c, "git gc --prune=now --quiet"))
      c.agent.gate(EVALUATION)
      await toBuild(c)
      const running = c.ws.start(["run", c.ws.root])
      await until(() => c.agent.waiting(EVALUATION), 120)
      running.kill()
      const cut = await running.ended
      const from = c.ws.log().length
      const asked = await c.ws.run("")
      killed = { c, cut, asked, log: c.ws.log().slice(from) }
    })(),
    (async () => {
      const c = await begun(cli)
      c.agent.does(WORK, `echo 'what the session noted' > ${OWN}\n${COMMIT}\nrm -f '${c.ws.notes("started", `${c.ticket}.json`)}'\n`)
      const first = await c.ws.run("")
      expect(first.out).toContain("waits for your answer on induct-ticket")
      await c.ws.answer("yes")
      const asked = await c.ws.run("")
      removed = { c, asked, log: c.ws.log() }
    })(),
    (async () => {
      const c = await begun(cli)
      c.agent.does(EVALUATION, amending(c))
      await toBuild(c)
      const asked = await c.ws.run("")
      amended = { c, asked, log: c.ws.log() }
    })()
  ])
}, 600_000)

afterAll(clean)

/** The run asks for a ruling that names `AGENTS.md`, in the sentence of the commit the session started from, reads no verdict and commits nothing of the step. */
function asksOnAgents(a: Asked): void {
  const { c, asked } = a
  expect(asked.code, asked.out).toBe(0)
  expect(asked.out).toContain("waits for your ruling on what changed while the session on write-build worked")
  expect(asked.out).toContain("AGENTS.md (changed)")
  expect(asked.out).toContain(startedFrom("write-build"))
  expect(asked.out).not.toContain("waits for your answer on write-build")
  const after = afterStart(a.log, "evaluation")
  expect(after.some((e) => e.event === "verdict read" || e.event === "check run" || e.event === "commit made")).toBe(false)
  expect(after.some((e) => e.event === "user asked")).toBe(true)
  expect(tipMessage(c)).toBe("the session's own commit")
  expect(c.ws.git(["show", "main:AGENTS.md"])).toBe(AGENTS)
}

describe("an evaluating session changes a file its step does not write, commits what it changed and gives git gc --prune=now (REQ-ALG-008 acceptance 13, REQ-FLOW-005 step 3)", () => {
  it("the tree kept at the session's start is one git no longer holds", () => {
    expect(readFileSync(join(gc.c.agent.state, "start-tree"), "utf8").trim()).toBe("gone")
  })

  it("the run asks for a ruling that names the file, reads no verdict and commits nothing of the step", () => {
    asksOnAgents(gc)
  })
})

describe("the same, with git prune --expire=now in place of the gc (REQ-ALG-008 acceptance 14)", () => {
  it("the tree kept at the session's start is one git no longer holds", () => {
    expect(readFileSync(join(pruned.c.agent.state, "start-tree"), "utf8").trim()).toBe("gone")
  })

  it("the run asks for a ruling that names the file, reads no verdict and commits nothing of the step", () => {
    asksOnAgents(pruned)
  })
})

describe("the same, where the run is killed while that session works, after the session has committed and pruned (REQ-ALG-008 acceptance 15, REQ-FLOW-003 step 1)", () => {
  it("the run is cut off, after the tree kept at the session's start was pruned", () => {
    expect(killed.cut.code, killed.cut.out).toBe(128)
    expect(readFileSync(join(killed.c.agent.state, "start-tree"), "utf8").trim()).toBe("gone")
  })

  it("the next run asks, naming the file, reads no verdict and commits nothing of the step", () => {
    const { c, asked, log } = killed
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("waits for your ruling on what changed while the session on write-build worked")
    expect(asked.out).toContain("AGENTS.md (changed)")
    expect(asked.out).toContain(startedFrom("write-build"))
    expect(log.some((e) => e.event === "run cut off")).toBe(true)
    expect(log.some((e) => e.event === "verdict read" || e.event === "commit made" || e.event === "session started")).toBe(false)
    expect(tipMessage(c)).toBe("the session's own commit")
  })
})

describe("a working session commits a file its step does not write, and the record of its start is then removed from git's own directory (REQ-ALG-008 acceptance 16, REQ-FLOW-005 step 3)", () => {
  it("the run that started it still asks, naming the file, and commits nothing of the step", () => {
    const { c, asked } = removed
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("waits for your ruling on what changed while the session on write-specification worked")
    expect(asked.out).toContain(`${OWN} (added)`)
    expect(asked.out).toContain(startedFrom("write-specification"))
    expect(asked.out).not.toContain("waits for your answer on write-specification")
    const after = afterStart(removed.log, "work")
    expect(after.some((e) => e.event === "commit made" || e.event === "verdict read" || e.event === "check run")).toBe(false)
    expect(tipMessage(c)).toBe("the session's own commit")
    expect(c.ws.git(["show", `stdo/${c.ticket}:${OWN}`])).toBe("what the session noted\n")
  })
})

describe("an evaluating session amends the commit it started from and git no longer holds it: the run that started it lets no other commit stand in (REQ-ALG-008, REQ-FLOW-005 step 3)", () => {
  it("git no longer holds the commit the session started from", () => {
    expect(readFileSync(join(amended.c.agent.state, "start-commit"), "utf8").trim()).toBe("gone")
  })

  it("the flow fails and the run stops: no verdict is read, no check run, nothing of the step committed, and no stand-in of the commit the folder is on is kept", () => {
    const { c, asked } = amended
    expect(asked.code, asked.out).toBe(1)
    expect(asked.out).toContain(`The run stopped on the ticket ${c.ticket}, at write-build`)
    expect(asked.out).toContain("the framework cannot compare the workspace's folder with the commit the session started from, which stands in for the identities taken at the start of the session on write-build")
    expect(asked.out).not.toContain("waits for your answer on write-build")
    const after = afterStart(amended.log, "evaluation")
    expect(after.some((e) => e.event === "verdict read" || e.event === "check run" || e.event === "commit made")).toBe(false)
    expect(tipMessage(c)).toBe("the session's own commit")
    expect(readFileSync(c.ws.notes("started", `${c.ticket}.json`), "utf8")).not.toContain("stood")
  })
})
