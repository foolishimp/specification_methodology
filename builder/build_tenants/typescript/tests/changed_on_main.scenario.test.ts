/**
 * What main, the branch the ticket left, gains while a session works is put
 * to the user before any of it is taken into the ticket's branch (ticket
 * 261125-083337-0fdf; D257). Every session is started by the agent's command
 * as a process of its own: the fixture agent. Each workspace is a repository
 * of its own under the system's temporary folder, and the product the
 * scenario driver builds is the one the user would run.
 *
 * - The measured case: the build's working session sets the command of the
 *   graph's check "the tests pass" to `true`, adds a line to `AGENTS.md` and
 *   writes a file of its own, commits the three on main with `git checkout
 *   main`, `git add` and `git commit`, puts the folder back on the ticket's
 *   branch and returns. The user then says yes.
 * - The same, where the session leaves the folder on main; after the user's
 *   yes, main is moved again by a commit that changes one of the three.
 * - The same, where the user says no and leaves main as it is, then puts main
 *   back to the commit it was on; and where the user says no and undoes the
 *   commit with `git revert` on main.
 * - A run killed while the build's session works, after the session has
 *   committed a file on main; and an evaluating session that commits a file
 *   on main and returns on the ticket's branch.
 * - The same killed run, where the record of the session's start then names
 *   no commit of main, as a record an earlier release wrote names none; and
 *   where the record is then removed, so the commit the folder is on stands
 *   in: the commit where the ticket's branch and main last met stands in for
 *   the commit main was on.
 * - A ruling of an earlier release: the induction's session writes two files
 *   of the folder outside what its step writes, the user says yes, and the
 *   ruling's line in the ticket and the record of the session's start are
 *   then given the names an earlier release gave the two files, beginning
 *   `checkout:` and `main:`.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-008 REQ-ALG-012 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-008
 */
import { execFileSync } from "node:child_process"
import { appendFileSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { lineText, readLine, type TicketLine } from "../src/algorithms/facts.js"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { build, clean, S1_FIXTURES, S1_TICKET, temporary, until, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]
const SESSION = "-c user.name=Session -c user.email=session@example.com"
/** The line the session adds to `AGENTS.md` on main. */
const LINE = "A line the session added on main."

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
}

async function begun(cli: string): Promise<Case> {
  const ws = new Workspace(cli)
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent, ticket }
}

/**
 * The session's script: on main, by `git checkout`, the graph's check "the
 * tests pass" set to `true`, a line added to `AGENTS.md` and a file of its
 * own, `notes.md`, committed; then back on the branch the folder was on,
 * unless `stay`.
 */
const threeOnMain = (stay = false): string => `set -e
cd "$ROOT"
was=$(git symbolic-ref --short HEAD)
git checkout -q main
perl -0pi -e 's/"argv": \\[\\s*"sh",\\s*"\\{tests\\}\\/run\\.sh"\\s*\\]/"argv": ["true"]/' .stdo-builder/graph.json
printf '\\n${LINE}\\n' >> AGENTS.md
printf 'a file of the session\\n' > notes.md
git add -- .stdo-builder/graph.json AGENTS.md notes.md
git ${SESSION} commit -q -m "the session's commit on main"
${stay ? "" : `git checkout -q "$was"\n`}`

/** A script that commits one file of the folder, `name`, on main, and puts the folder back. */
const oneOnMain = (name: string): string => `set -e
cd "$ROOT"
was=$(git symbolic-ref --short HEAD)
git checkout -q main
printf 'committed on main while the session worked\\n' > ${name}
git add -- ${name}
git ${SESSION} commit -q -m "${name} on main"
git checkout -q "$was"
`

/** The three as the question names them. */
const THREE = [".stdo-builder/graph.json (changed on main)", "AGENTS.md (changed on main)", "notes.md (added on main)"]

const branch = (c: Case): string => `stdo/${c.ticket}`
/** Whether main's commit is in the ticket's branch: whether main was taken in. */
const takenIn = (c: Case): Promise<boolean> => c.ws.gitSays(["merge-base", "--is-ancestor", "main", branch(c)]).then((code) => code === 0)
/** Whether a commit holds a file. */
const holds = (c: Case, rev: string, path: string): Promise<boolean> => c.ws.gitSays(["cat-file", "-e", `${rev}:${path}`]).then((code) => code === 0)
const textAt = (c: Case, rev: string, path: string): string => c.ws.git(["show", `${rev}:${path}`])
/** The rulings on what changed the ticket holds on its branch. */
const rulings = (c: Case): readonly string[] =>
  textAt(c, branch(c), `.ai-workspace/tickets/active/${c.ticket}.md`).split("\n").filter((l) => l.startsWith("- framework: ruled "))

/** Commits on main, in a working tree of the user's own that is removed after, so the folder stays on the ticket's branch (D239). */
function onMainElsewhere(c: Case, change: (tree: string) => void, message: string): void {
  const tree = join(temporary("stdo-builder-main-"), "main")
  c.ws.git(["worktree", "add", "-q", tree, "main"])
  try {
    change(tree)
    execFileSync("git", ["-C", tree, "add", "-A"], { env: c.ws.env })
    execFileSync("git", ["-C", tree, ...USER, "commit", "-q", "-m", message], { env: c.ws.env })
  } finally {
    c.ws.git(["worktree", "remove", "--force", tree])
  }
}

/** The runs to the build's session, each answer yes: the induction and the specification. */
async function toBuild(c: Case): Promise<void> {
  await c.ws.run("")
  await c.ws.answer("yes")
  await c.ws.run("")
  await c.ws.answer("yes")
}

/** Runs and answers yes until the ticket is done, or six runs are made. */
async function toEnd(c: Case): Promise<Said> {
  let said = await c.ws.run("")
  for (let n = 0; n < 6 && said.out.includes("waits for your answer"); n++) {
    await c.ws.answer("yes")
    said = await c.ws.run("")
  }
  return said
}

let measured: { c: Case; asked: Said; takenAsked: boolean; shown: Said; mainThen: string; branchThen: string; mainBefore: string; yes: Said; after: Said; afterLog: readonly LogEntry[] }
let stayed: { c: Case; stopped: Said; asked: Said; takenBefore: boolean; again: Said }
let reset: { c: Case; asked: Said; waited: Said; takenWaiting: boolean; goes: Said; done: Said }
let reverted: { c: Case; goes: Said; done: Said }
let killed: { c: Case; said: Said }
let evaluated: { c: Case; said: Said; log: readonly LogEntry[] }
let earlier: { c: Case; said: Said }
let lost: { c: Case; said: Said }
let earlierRuling: { c: Case; asked: Said; renamed: string; after: Said }

/** The line of the framework's part, as `lineText` gives it, of the ticket's ruling yes on what changed at `vector`. */
const rulingLine = (text: string, vector: string): string =>
  (text.split("\n").find((l) => l.startsWith(`- framework: ruled yes on what changed at ${vector}: `)) ?? "").replace(/^- framework: /, "")
const identityOf = (c: Case, text: string): string => execFileSync("git", ["-C", c.ws.root, "hash-object", "--stdin"], { input: text, encoding: "utf8", env: c.ws.env }).trim()

/** A run killed while the build's session works, after it committed `name` on main; then `after` is done to the record of the session's start, and the next run is made. */
async function killedOnMain(c: Case, name: string, after: (record: string) => void): Promise<Said> {
  await toBuild(c)
  c.agent.first("write-build.work", oneOnMain(name))
  c.agent.gate("write-build.work")
  const running = c.ws.start(["run", c.ws.root])
  await until(() => c.agent.waiting("write-build.work"), 120)
  running.kill()
  await running.ended
  c.agent.open("write-build.work")
  after(c.ws.notes("started", `${c.ticket}.json`))
  return c.ws.run("")
}

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      const c = await begun(cli)
      await toBuild(c)
      c.agent.first("write-build.work", threeOnMain())
      const mainBefore = c.ws.git(["rev-parse", "main"]).trim()
      const asked = await c.ws.run("")
      const mainThen = c.ws.git(["rev-parse", "main"]).trim()
      const branchThen = c.ws.git(["rev-parse", branch(c)]).trim()
      const takenAsked = await takenIn(c)
      const shown = await c.ws.show()
      const yes = await c.ws.answer("yes")
      const from = c.ws.log().length
      const after = await c.ws.run("")
      measured = { c, asked, takenAsked, shown, mainThen, branchThen, mainBefore, yes, after, afterLog: c.ws.log().slice(from) }
    })(),
    (async () => {
      const c = await begun(cli)
      await toBuild(c)
      c.agent.first("write-build.work", threeOnMain(true))
      const stopped = await c.ws.run("")
      c.ws.git(["switch", "-q", branch(c)])
      const asked = await c.ws.run("")
      const takenBefore = await takenIn(c)
      await c.ws.answer("yes")
      // After the yes, main is moved again by a commit that changes one of the three.
      onMainElsewhere(c, (tree) => appendFileSync(join(tree, "notes.md"), "changed again by the user\n"), "notes.md changed again")
      const again = await c.ws.run("")
      stayed = { c, stopped, asked, takenBefore, again }
    })(),
    (async () => {
      const c = await begun(cli)
      await toBuild(c)
      const was = c.ws.git(["rev-parse", "main"]).trim()
      c.agent.first("write-build.work", threeOnMain())
      const asked = await c.ws.run("")
      await c.ws.answer("no", "these are not to stand")
      const waited = await c.ws.run("")
      const takenWaiting = await takenIn(c)
      // The user puts main back to the commit it was on when the session started.
      c.ws.git(["branch", "-f", "main", was])
      const goes = await c.ws.run("")
      const done = await toEnd(c)
      reset = { c, asked, waited, takenWaiting, goes, done }
    })(),
    (async () => {
      const c = await begun(cli)
      await toBuild(c)
      c.agent.first("write-build.work", threeOnMain())
      await c.ws.run("")
      await c.ws.answer("no", "these are not to stand")
      // The user undoes the session's commit with git revert on main.
      const tree = join(temporary("stdo-builder-main-"), "main")
      c.ws.git(["worktree", "add", "-q", tree, "main"])
      execFileSync("git", ["-C", tree, ...USER, "revert", "--no-edit", "HEAD"], { env: c.ws.env, stdio: "pipe" })
      c.ws.git(["worktree", "remove", tree])
      const goes = await c.ws.run("")
      const done = await toEnd(c)
      reverted = { c, goes, done }
    })(),
    (async () => {
      const c = await begun(cli)
      await toBuild(c)
      c.agent.first("write-build.work", oneOnMain("killed.md"))
      c.agent.gate("write-build.work")
      const running = c.ws.start(["run", c.ws.root])
      await until(() => c.agent.waiting("write-build.work"), 120)
      running.kill()
      await running.ended
      c.agent.open("write-build.work")
      killed = { c, said: await c.ws.run("") }
    })(),
    (async () => {
      const c = await begun(cli)
      await toBuild(c)
      c.agent.first("write-build.evaluation", oneOnMain("evaluated.md"))
      const from = c.ws.log().length
      const said = await c.ws.run("")
      evaluated = { c, said, log: c.ws.log().slice(from) }
    })(),
    (async () => {
      const c = await begun(cli)
      // The record names no commit of main, as a record an earlier release wrote names none.
      const said = await killedOnMain(c, "earlier.md", (record) => {
        const { main: _main, ...rest } = JSON.parse(readFileSync(record, "utf8")) as Record<string, unknown>
        writeFileSync(record, `${JSON.stringify(rest)}\n`)
      })
      earlier = { c, said }
    })(),
    (async () => {
      const c = await begun(cli)
      const said = await killedOnMain(c, "lost.md", (record) => rmSync(record, { force: true }))
      lost = { c, said }
    })(),
    (async () => {
      const c = await begun(cli)
      // The induction's session writes two files of the folder its step does not write, and commits neither.
      c.agent.first("induct-ticket.work", `printf 'one\\n' > "$ROOT/one.md"\nprintf 'two\\n' > "$ROOT/two.md"\n`)
      const asked = await c.ws.run("")
      await c.ws.answer("yes")
      // The ruling's line and the record are given the names an earlier release gave the two files: `checkout:` and `main:` before the path.
      const path = c.ws.path(".ai-workspace", "tickets", "active", `${c.ticket}.md`)
      const text = readFileSync(path, "utf8")
      const was = rulingLine(text, "induct-ticket")
      const line = readLine(was)
      const earlierName = (key: string): string => (key === "one.md" ? "checkout:one.md" : key === "two.md" ? "main:two.md" : key)
      const renamed = line?.line === "changed" ? lineText({ ...line, files: line.files.map((f) => ({ ...f, key: earlierName(f.key) })) }) : ""
      writeFileSync(path, text.replace(was, renamed))
      const recordPath = c.ws.notes("started", `${c.ticket}.json`)
      const record = JSON.parse(readFileSync(recordPath, "utf8")) as { own?: string[]; yes?: Record<string, string> } & Record<string, unknown>
      const own = (record.own ?? []).map((id) => (id === identityOf(c, was) ? identityOf(c, renamed) : id))
      const yes = Object.fromEntries(Object.entries(record.yes ?? {}).map(([k, id]) => [earlierName(k), id]))
      writeFileSync(recordPath, `${JSON.stringify({ ...record, own, yes })}\n`)
      const after = await c.ws.run("")
      earlierRuling = { c, asked, renamed, after }
    })()
  ])
}, 900_000)

afterAll(clean)

describe("REQ-ALG-008, REQ-FLOW-001: what main gains while a session works is put to the user, and nothing of it is taken in before the yes", () => {
  it("REQ-ALG-008 acceptance: a working session sets the command of a check in the graph to true, adds a line to AGENTS.md and writes a file of its own, commits the three on main, puts the folder back on the ticket's branch and returns: the run ends waiting for the user's ruling and names the three as changed on main", () => {
    const { asked } = measured
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("The run waits for your ruling on what changed while the session on write-build worked")
    expect(asked.out).toContain("these files of the workspace's folder changed on main, the branch the ticket left")
    for (const named of THREE) expect(asked.out).toContain(`- ${named}`)
    expect(asked.out).toContain("it may have been the session or you")
    expect(asked.out).toContain("A yes: for the files changed on main, main stands as it then is, and the run takes it into the ticket's branch")
    expect(asked.out).toContain("put main back for the files changed there; the framework takes nothing of main in")
    // The step's own work, in the folder, is no part of what is asked.
    expect(asked.out).not.toContain("While the session on write-build worked, these files changed outside what its step writes")
  })

  it("REQ-ALG-008 acceptance, REQ-FLOW-001 acceptance: the ticket's branch holds none of the three, and no commit the framework made holds them; main is as the session left it", async () => {
    const { c, mainThen, mainBefore } = measured
    expect(measured.takenAsked).toBe(false)
    expect(await holds(c, measured.branchThen, "notes.md")).toBe(false)
    expect(textAt(c, measured.branchThen, "AGENTS.md")).not.toContain(LINE)
    expect(textAt(c, measured.branchThen, ".stdo-builder/graph.json")).not.toContain('"argv": ["true"]')
    expect(c.ws.git(["log", "--format=%s", `${mainBefore}..${mainThen}`]).trim()).toBe("the session's commit on main")
    expect(c.ws.git(["log", "--format=%H", measured.branchThen, "--", "notes.md"]).trim()).toBe("")
  })

  it("REQ-FLOW-001: main is named among the branches, and the run's words do not say of main that it does not hold the ticket", () => {
    const line = measured.asked.out.split("\n").find((l) => l.startsWith("While the session on write-build worked, these changed among the repository's branches, tags and stash")) ?? ""
    expect(line, measured.asked.out).toContain("main (changed)")
    expect(line).toContain("none holds the ticket but main, the branch the ticket left")
    expect(line).not.toMatch(/and none holds the ticket: /)
  })

  it("REQ-ALG-012 acceptance: while a ruling is awaited, show gives the same question, file by file, the files changed on main named apart", () => {
    const { shown } = measured
    expect(shown.code, shown.out).toBe(0)
    for (const named of THREE) expect(shown.out).toContain(`- ${named}`)
    expect(shown.out).toContain("these files of the workspace's folder changed on main, the branch the ticket left")
  })

  it("REQ-ALG-008 acceptance, REQ-FLOW-006: after the user's yes, the next run takes main in; the ticket holds one ruling on what changed, which names the three apart from the folder's files; and what rests on them is judged or asked again", async () => {
    const { c, yes, after, afterLog } = measured
    expect(yes.code, yes.out).toBe(0)
    expect(after.code, after.out).toBe(0)
    expect(await takenIn(c)).toBe(true)
    expect(afterLog.some((e) => e.event === "main taken in" && e.result === "merged"), JSON.stringify(afterLog)).toBe(true)
    const lines = rulings(c)
    expect(lines).toHaveLength(1)
    for (const key of ["left:.stdo-builder/graph.json", "left:AGENTS.md", "left:notes.md"]) expect(lines[0]).toContain(`${key} `)
    expect(after.out).not.toContain("waits for your ruling")
    expect(after.out).toContain("waits for your answer on write-build")
    expect(textAt(c, branch(c), "AGENTS.md")).toContain(LINE)
  })
})

describe("REQ-FLOW-005, REQ-FLOW-003: the session leaves the folder on main, a run is killed, an evaluating session commits on main", () => {
  it("REQ-FLOW-005 acceptance: a working session commits on main files its step does not write and returns with the folder on main: the run stops as for any other branch; after the user puts the folder back, the next run waits for the ruling, naming those files as changed on main, and takes nothing of main in", () => {
    const { stopped, asked, takenBefore } = stayed
    expect(stopped.code, stopped.out).toBe(1)
    expect(stopped.out).toContain("the workspace's folder is on the branch main, which is not the ticket's")
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("waits for your ruling")
    for (const named of THREE) expect(asked.out).toContain(`- ${named}`)
    expect(takenBefore).toBe(false)
  })

  it("REQ-FLOW-003 acceptance: a run is killed while its session works, after the session has committed a file on main: the next run waits for the user's ruling and names the file as changed on main", async () => {
    const { c, said } = killed
    expect(said.code, said.out).toBe(0)
    expect(said.out).toContain("waits for your ruling")
    expect(said.out).toContain("- killed.md (added on main)")
    expect(await takenIn(c)).toBe(false)
  })

  it("REQ-FLOW-005 acceptance: an evaluating session commits a file on main and returns with the folder on the ticket's branch: the run names the file as changed on main, reads no verdict and waits for the user's ruling", async () => {
    const { c, said, log } = evaluated
    expect(said.code, said.out).toBe(0)
    expect(said.out).toContain("The run waits for your ruling on what changed while the session on write-build worked")
    expect(said.out).toContain("- evaluated.md (added on main)")
    const started = log.findIndex((e) => e.event === "session started" && e.kind === "evaluation")
    expect(started, JSON.stringify(log)).toBeGreaterThanOrEqual(0)
    expect(log.slice(started).some((e) => e.event === "verdict read" || e.event === "check run")).toBe(false)
    expect(await takenIn(c)).toBe(false)
  })
})

describe("REQ-ALG-008: the commit where the ticket's branch and main last met stands in for the commit main was on", () => {
  it("REQ-ALG-008: the record of the session's start names no commit of main, as a record an earlier release wrote names none: the next run waits for the user's ruling and names the file committed on main, and takes nothing of main in", async () => {
    const { c, said } = earlier
    expect(said.code, said.out).toBe(0)
    expect(said.out).toContain("waits for your ruling")
    expect(said.out).toContain("- earlier.md (added on main)")
    expect(await takenIn(c)).toBe(false)
  })

  it("REQ-ALG-008, REQ-FLOW-006: the record of the session's start is gone, so the commit the folder is on stands in: the question says the identities are missing, names the file committed on main, and nothing of main is taken in", async () => {
    const { c, said } = lost
    expect(said.code, said.out).toBe(0)
    expect(said.out).toContain("waits for your ruling")
    expect(said.out).toContain("The identities taken at the start of the session on write-build are missing")
    expect(said.out).toContain("- lost.md (added on main)")
    expect(await takenIn(c)).toBe(false)
  })
})

describe("REQ-FLOW-006: what a no and a yes mean for the files changed on main", () => {
  it("REQ-FLOW-006 acceptance: the user says no to files changed on main and leaves main as it is: the next run waits again and takes nothing of main in", () => {
    const { asked, waited, takenWaiting } = reset
    for (const named of THREE) expect(asked.out).toContain(`- ${named}`)
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain("waits for your ruling")
    for (const named of THREE) expect(waited.out).toContain(`- ${named}`)
    expect(takenWaiting).toBe(false)
  })

  it("REQ-FLOW-006 acceptance: the user says no and puts main back to the commit it was on when the session started: the next run asks nothing on what changed, the ticket is built to its end, and main holds none of those files", async () => {
    const { c, goes, done } = reset
    expect(goes.code, goes.out).toBe(0)
    expect(goes.out).not.toContain("waits for your ruling")
    expect(done.code, done.out).toBe(0)
    expect(done.out).toContain(`The work on the ticket ${c.ticket} is done`)
    expect(await holds(c, "main", "notes.md")).toBe(false)
    expect(textAt(c, "main", "AGENTS.md")).not.toContain(LINE)
    expect(textAt(c, "main", ".stdo-builder/graph.json")).not.toContain('"argv": ["true"]')
  })

  it("REQ-FLOW-006 acceptance: the same where the user undoes them with git revert on main", async () => {
    const { c, goes, done } = reverted
    expect(goes.code, goes.out).toBe(0)
    expect(goes.out).not.toContain("waits for your ruling")
    expect(done.code, done.out).toBe(0)
    expect(done.out).toContain(`The work on the ticket ${c.ticket} is done`)
    expect(await holds(c, "main", "notes.md")).toBe(false)
    expect(textAt(c, "main", "AGENTS.md")).not.toContain(LINE)
    expect(textAt(c, "main", ".stdo-builder/graph.json")).not.toContain('"argv": ["true"]')
  })

  it("REQ-FLOW-006 acceptance: the user says yes to files changed on main, and main is then moved again by a commit that changes one of them: the next run asks again, and names that file", async () => {
    const { c, again } = stayed
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("waits for your ruling")
    expect(again.out).toContain("- notes.md (added on main)")
    expect(again.out).not.toContain("- AGENTS.md (changed on main)")
    expect(again.out).not.toContain("- .stdo-builder/graph.json (changed on main)")
    expect(await takenIn(c)).toBe(false)
  })
})

describe("REQ-FLOW-004: the ruling names a file changed on main apart from a file of the folder", () => {
  it("REQ-FLOW-004: a ruling line naming a file of the folder, a file changed on main of the same path and a file removed on main is read back as it was written, each told apart", () => {
    const line: TicketLine = {
      line: "changed",
      says: "yes",
      vector: "write-build",
      files: [
        { key: "AGENTS.md", identity: "a".repeat(40) },
        { key: "left:AGENTS.md", identity: "b".repeat(40) },
        { key: "left:gone.md", identity: "" }
      ]
    }
    const text = lineText(line)
    expect(text).toBe(`ruled yes on what changed at write-build: AGENTS.md ${"a".repeat(40)}; left:AGENTS.md ${"b".repeat(40)}; left:gone.md none`)
    expect(readLine(text)).toEqual(line)
  })

  it("REQ-FLOW-004: a ruling of an earlier release, whose names begin checkout: and main:, is read as naming the files of the folder at the paths that follow: the next run asks nothing on them and commits both as the step's result", async () => {
    const { c, asked, renamed, after } = earlierRuling
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("The run waits for your ruling on what changed while the session on induct-ticket worked")
    for (const f of ["one.md", "two.md"]) expect(asked.out).toContain(`- ${f} (added)`)
    expect(renamed).toContain("checkout:one.md ")
    expect(renamed).toContain("main:two.md ")
    expect(after.code, after.out).toBe(0)
    expect(after.out).not.toContain("waits for your ruling")
    expect(after.out).not.toContain("changed on main")
    expect(after.out).toContain("waits for your answer on induct-ticket")
    for (const f of ["one.md", "two.md"]) {
      expect(await holds(c, branch(c), f), f).toBe(true)
      expect(c.ws.git(["log", "--format=%s", branch(c), "--", f]).trim(), f).toBe("the result of the step on induct-ticket")
    }
  })
})
