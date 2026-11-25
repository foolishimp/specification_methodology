/**
 * What is committed outside the workspace's folder on a ticket's branch is
 * named to the user (ticket 261125-043021-2fed; D256). Every session is
 * started by the agent's command as a process of its own: the fixture agent.
 * Each workspace lies in a repository of its own under the system's temporary
 * folder.
 *
 * - A product inside a larger repository. The user has a changed file and an
 *   untracked file outside the folder, neither committed; the specification's
 *   working session gives `git add -A` and `git commit`. The build's working
 *   session writes a file outside the folder and commits it. Between two runs,
 *   with no session at work, the user commits one more file outside the folder
 *   on the ticket's branch. The ticket is then built to its end.
 * - A product inside a larger repository in which nothing is committed outside
 *   the folder, while a file there stays changed and not committed: built to
 *   its end, with its packets read.
 * - A product at the top of a repository: built to its end, with its packets
 *   read.
 * - A product inside a larger repository whose specification's working
 *   session puts the repository on a branch that has no commit yet, so git
 *   cannot compare the two commits.
 * - A product inside a larger repository whose induction's working session
 *   makes a tag, and writes 25 files outside the folder and commits them.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-FLOW-008 REQ-ALG-007 REQ-PARAM-001
 */
import { execFileSync } from "node:child_process"
import { mkdirSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { build, clean, S1_FIXTURES, S1_TICKET, Workspace, write, type Said } from "./scenario_driver.js"

const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]
/** The identity a session's own commits are made under. */
const SESSION = "-c user.name=Session -c user.email=session@example.com"
const WITHIN = ["apps", "product"]
/** The sentence every packet inside a larger repository holds (REQ-ALG-007). */
const LARGER = "- repository: this folder lies inside a larger git repository; the files outside this folder are the user's and no part of the step, and a git command given without a path acts on the whole repository."

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
  /** git at the repository's top. */
  readonly git: (args: readonly string[]) => string
}

/** A workspace set up with a first ticket and the fixture agent; inside a larger repository with one commit of its own files where `inside`. */
async function begun(cli: string, inside: boolean, files: readonly string[] = []): Promise<Case> {
  const ws = new Workspace(cli, undefined, inside ? WITHIN : [])
  const git = (args: readonly string[]): string => execFileSync("git", ["-C", ws.top, ...args], { encoding: "utf8", env: ws.env })
  if (inside) {
    for (const f of files) write(join(ws.top, f), `${f}\n`)
    git(["init", "-q", "-b", "main"])
    git(["add", "-A"])
    git([...USER, "commit", "-q", "-m", "the repository's own files"])
    mkdirSync(ws.root, { recursive: true })
  }
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent, ticket, git }
}

/** The line of a run's words that names what was committed outside the folder while the session on `vector` worked. */
const committedLine = (said: Said, vector: string): string =>
  said.out.split("\n").find((l) => l.startsWith(`While the session on ${vector} worked, these files outside the workspace's folder were committed`)) ?? ""

/** The line of the words that say the ticket is done that names what the merge took in outside the folder. */
const takenLine = (said: Said): string =>
  said.out.split("\n").find((l) => l.startsWith("The merge took these files outside the workspace's folder into")) ?? ""

/** S1 with the fixture agent: the induction, the specification, the build and the run that merges, with each answer yes; `between` is done before the run whose number it is given, from 1. */
async function toEnd(c: Case, between: (run: number) => void = () => {}): Promise<readonly Said[]> {
  const runs: Said[] = []
  for (let n = 1; n <= 4; n++) {
    between(n)
    const said = await c.ws.run("")
    runs.push(said)
    if (n < 4) await c.ws.answer("yes")
  }
  return runs
}

let measured: { c: Case; runs: readonly Said[] }
let none: { c: Case; runs: readonly Said[] }
let atTop: { c: Case; runs: readonly Said[] }
let cannot: { c: Case; said: Said }
let many: Said

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      const c = await begun(cli, true, ["x.txt", "kept.txt"])
      // The user has a changed file and an untracked file outside the folder, neither committed.
      writeFileSync(join(c.ws.top, "x.txt"), "x, changed by the user and not committed\n")
      writeFileSync(join(c.ws.top, "y.txt"), "y, untracked\n")
      // The specification's working session stages the whole repository and commits it.
      c.agent.does("write-specification.work", `git add -A\ngit ${SESSION} commit -q -m "the session's commit"\n`)
      // The build's working session writes a file outside the folder and commits it.
      c.agent.does("write-build.work", `printf 'made by the session\\n' > "$ROOT/../made.txt"\ngit add -- "$ROOT/../made.txt"\ngit ${SESSION} commit -q -m "the session's file outside the folder" -- "$ROOT/../made.txt"\n`)
      const runs = await toEnd(c, (n) => {
        // Between the run that asks on the build and the run that merges, with no session at work, the user commits a file outside the folder on the ticket's branch.
        if (n !== 4) return
        writeFileSync(join(c.ws.top, "w.txt"), "w, committed by the user between two runs\n")
        c.git(["add", "--", "w.txt"])
        c.git([...USER, "commit", "-q", "-m", "the user's commit outside the folder", "--", "w.txt"])
      })
      measured = { c, runs }
    })(),
    (async () => {
      const c = await begun(cli, true, ["x.txt"])
      // A file outside the folder stays changed and is never committed.
      writeFileSync(join(c.ws.top, "x.txt"), "x, changed and never committed\n")
      none = { c, runs: await toEnd(c) }
    })(),
    (async () => {
      const c = await begun(cli, false)
      atTop = { c, runs: await toEnd(c) }
    })(),
    (async () => {
      const c = await begun(cli, true, ["x.txt"])
      await c.ws.run("")
      await c.ws.answer("yes")
      // The session puts the repository on a branch with no commit: the commit it is on when the session is over cannot be compared.
      c.agent.does("write-specification.work", "git checkout -q --orphan a-branch-with-no-commit\n")
      cannot = { c, said: await c.ws.run("") }
    })(),
    (async () => {
      const c = await begun(cli, true, ["x.txt"])
      c.agent.does("induct-ticket.work", `git tag a-tag-made-while-it-worked\nfor i in $(seq 1 25); do printf 'made\\n' > "$ROOT/../made-$i.txt"; done\ngit add -- "$ROOT"/../made-*.txt\ngit ${SESSION} commit -q -m "25 files outside the folder" -- "$ROOT"/../made-*.txt\n`)
      many = await c.ws.run("")
    })()
  ])
}, 600_000)

afterAll(clean)

describe("REQ-FLOW-001: what was committed outside the folder while a session worked is named after it", () => {
  it("REQ-FLOW-001 acceptance, the measured case: the user's changed and untracked files, committed by a working session with git add -A, are named as committed while it worked, the first as changed and the second as added, with the merge that takes them into main; nothing is asked on them", () => {
    const said = measured.runs[1] ?? { code: -1, out: "" }
    expect(said.code, said.out).toBe(0)
    const line = committedLine(said, "write-specification")
    expect(line, said.out).toContain("x.txt (changed)")
    expect(line).toContain("y.txt (added)")
    expect(line).toContain("it may have been the session or you")
    expect(line).toContain("none of it holds the ticket")
    expect(line).toContain("the ticket's merge takes what was committed there into main, the branch the ticket left")
    expect(said.out).toContain("waits for your answer on write-specification")
    expect(said.out).not.toContain("waits for your ruling")
  })

  it("REQ-FLOW-001 acceptance: a working session writes a file outside the folder and commits it: the run names it as added, as committed while the session worked", () => {
    const said = measured.runs[2] ?? { code: -1, out: "" }
    expect(said.code, said.out).toBe(0)
    expect(committedLine(said, "write-build"), said.out).toContain("apps/made.txt (added)")
    expect(said.out).toContain("waits for your answer on write-build")
  })

  it("REQ-FLOW-001: a session that commits nothing outside the folder is named for nothing committed; a file left changed and not committed is not named as committed", () => {
    for (const said of none.runs) expect(said.out).not.toContain("were committed")
    expect(measured.runs[0]?.out ?? "").not.toContain("were committed")
  })

  it("REQ-FLOW-001: where git cannot compare the commit the folder was on when the session started with the one it is on when it is over, the run says it cannot tell what was committed outside the folder", () => {
    expect(cannot.said.out).toContain("While the session on write-specification worked, the framework cannot tell what was committed outside the workspace's folder")
    expect(cannot.said.out).toContain("a-branch-with-no-commit")
  })
})

describe("REQ-PARAM-001: the files committed outside the folder while a session worked are counted apart", () => {
  it("REQ-PARAM-001, REQ-FLOW-001: of 25 files committed outside the folder while a session worked, 20 are named, with how many there are, apart from what changed among the branches, tags and stash", () => {
    expect(many.code, many.out).toBe(0)
    const changed = many.out.split("\n").find((l) => l.startsWith("While the session on induct-ticket worked, these changed among")) ?? ""
    expect(changed, many.out).toContain("a-tag-made-while-it-worked (added)")
    expect(changed).not.toContain("named of")
    const line = committedLine(many, "induct-ticket")
    expect(line.match(/apps\/made-\d+\.txt \(added\)/g), many.out).toHaveLength(20)
    expect(line).toContain("20 named of 25")
  })
})

describe("REQ-FLOW-008 step 2: the words that say the ticket is done name what the merge took in outside the folder", () => {
  it("REQ-FLOW-008 acceptance: a ticket built to its end in which sessions committed files outside the folder: the words that say it is done name each of them as taken into the branch the ticket left", () => {
    const done = measured.runs[3] ?? { code: -1, out: "" }
    expect(done.code, done.out).toBe(0)
    expect(done.out).toContain(`The work on the ticket ${measured.c.ticket} is done`)
    const line = takenLine(done)
    expect(line, done.out).toContain("into main, the branch the ticket left")
    for (const named of ["x.txt (changed)", "y.txt (added)", "apps/made.txt (added)"]) expect(line).toContain(named)
    expect(line).not.toContain("kept.txt")
    expect(measured.c.git(["show", "main:y.txt"])).toBe("y, untracked\n")
  })

  it("REQ-FLOW-008 acceptance: between two runs, with no session at work, the user commits a file outside the folder on the ticket's branch: the words that say the ticket is done name it", () => {
    expect(takenLine(measured.runs[3] ?? { code: -1, out: "" })).toContain("w.txt (added)")
  })

  it("REQ-FLOW-008 acceptance: in a ticket where nothing was committed outside the folder, the words that say it is done name none; at the top of a repository, they are as they were", () => {
    for (const { c, runs } of [none, atTop]) {
      const done = runs[3] ?? { code: -1, out: "" }
      expect(done.code, done.out).toBe(0)
      expect(done.out).toContain(`The work on the ticket ${c.ticket} is done. It lies in the done lane and its branch is merged into main, the branch it left, at `)
      expect(takenLine(done)).toBe("")
      expect(done.out).not.toContain("outside the workspace's folder")
    }
    expect(none.c.git(["status", "--porcelain", "--", "x.txt"]).trim()).toBe("M x.txt")
  })
})

describe("REQ-ALG-007: the packet says what of a larger repository is the user's", () => {
  it("REQ-ALG-007 acceptance 13: inside a larger repository, a working packet and an evaluating packet each hold the sentence on the larger repository; at the top of a repository, neither does", () => {
    for (const at of ["write-build.work", "write-build.evaluation"]) {
      expect(none.c.agent.brief(at)?.split("\n"), at).toContain(LARGER)
      expect(atTop.c.agent.brief(at), at).toBeDefined()
      expect(atTop.c.agent.brief(at)).not.toContain("larger git repository")
    }
  })
})
