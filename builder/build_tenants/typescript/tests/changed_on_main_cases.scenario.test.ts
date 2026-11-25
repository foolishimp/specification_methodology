/**
 * What main, the branch the ticket left, gains with no session at work, and
 * while one works, beside the measured case (ticket 261125-083337-0fdf;
 * D257). Every session is started by the agent's command as a process of its
 * own: the fixture agent. Each workspace is a repository of its own under the
 * system's temporary folder.
 *
 * - While the induction's session works, main is moved by a commit that
 *   changes no file. Then, between two runs, with no session at work and no
 *   ruling awaited, the user commits a change on main.
 * - While the specification's session works, the user edits the active
 *   ticket on main, in a working tree of the user's own; then says yes.
 * - Inside a larger repository, the induction's working session commits on
 *   main a file of the workspace's folder, a changed file of the user's
 *   outside the folder and 25 files of its own outside it.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-008 REQ-FLOW-001 REQ-FLOW-004 REQ-FLOW-008 REQ-PARAM-001
 */
import { execFileSync } from "node:child_process"
import { appendFileSync, mkdirSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { build, clean, S1_FIXTURES, S1_TICKET, temporary, until, Workspace, write, type LogEntry, type Said } from "./scenario_driver.js"

const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]
const SESSION = "-c user.name=Session -c user.email=session@example.com"
const WITHIN = ["apps", "product"]

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
}

/** A workspace set up with a first ticket and the fixture agent; inside a larger repository, with one commit of `files` there, where `inside`. */
async function begun(cli: string, inside = false, files: readonly string[] = []): Promise<Case> {
  const ws = new Workspace(cli, undefined, inside ? WITHIN : [])
  if (inside) {
    const git = (args: readonly string[]): string => execFileSync("git", ["-C", ws.top, ...args], { encoding: "utf8", env: ws.env })
    for (const f of files) write(join(ws.top, f), `${f}\n`)
    git(["init", "-q", "-b", "main"])
    git(["add", "-A"])
    git([...USER, "commit", "-q", "-m", "the repository's own files"])
    mkdirSync(ws.root, { recursive: true })
  }
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent, ticket }
}

const branch = (c: Case): string => `stdo/${c.ticket}`
const takenIn = (c: Case): Promise<boolean> => c.ws.gitSays(["merge-base", "--is-ancestor", "main", branch(c)]).then((code) => code === 0)
const lineOf = (said: Said, start: string): string => said.out.split("\n").find((l) => l.startsWith(start)) ?? ""

let between: { c: Case; first: Said; second: Said; takenAfter: boolean; heldAfter: boolean }
let edited: { c: Case; asked: Said; takenAsked: boolean; after: Said; afterLog: readonly LogEntry[] }
let inside: { c: Case; said: Said; takenAfter: boolean }

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      const c = await begun(cli)
      // While the induction's session works, main is moved by a commit that changes no file.
      c.agent.first("induct-ticket.work", `git -C "$ROOT" branch -f main $(git -C "$ROOT" ${SESSION} commit-tree -p main -m "a commit that changes no file" "main^{tree}")\n`)
      const first = await c.ws.run("")
      await c.ws.answer("yes")
      // Between two runs, with no session at work and no ruling awaited, the user commits a change on main.
      c.ws.onMain(() => {
        writeFileSync(c.ws.path("between.md"), "committed by the user between two runs\n")
        c.ws.git(["add", "--", "between.md"])
        c.ws.git([...USER, "commit", "-q", "-m", "the user's commit on main between two runs"])
      })
      const second = await c.ws.run("")
      between = { c, first, second, takenAfter: await takenIn(c), heldAfter: (await c.ws.gitSays(["cat-file", "-e", `${branch(c)}:between.md`])) === 0 }
    })(),
    (async () => {
      const c = await begun(cli)
      await c.ws.run("")
      await c.ws.answer("yes")
      c.agent.gate("write-specification.work")
      const running = c.ws.start(["run", c.ws.root])
      await until(() => c.agent.waiting("write-specification.work"), 120)
      // While the session works, the user edits the active ticket on main, in a working tree of their own, removed after (D239).
      const tree = join(temporary("stdo-builder-main-"), "main")
      c.ws.git(["worktree", "add", "-q", tree, "main"])
      appendFileSync(join(tree, ".ai-workspace", "tickets", "active", `${c.ticket}.md`), "\nIt also prints a second line, goodbye.\n")
      execFileSync("git", ["-C", tree, ...USER, "commit", "-q", "-a", "-m", "the user edits the active ticket on main"], { env: c.ws.env })
      c.ws.git(["worktree", "remove", tree])
      c.agent.open("write-specification.work")
      const asked = await running.ended
      const takenAsked = await takenIn(c)
      await c.ws.answer("yes")
      const from = c.ws.log().length
      const after = await c.ws.run("")
      edited = { c, asked, takenAsked, after, afterLog: c.ws.log().slice(from) }
    })(),
    (async () => {
      const c = await begun(cli, true, ["x.txt"])
      c.agent.first("induct-ticket.work", `set -e
cd "$ROOT"
was=$(git symbolic-ref --short HEAD)
git checkout -q main
printf 'a file of the folder, on main\\n' > notes.md
printf 'x, changed on main while the session worked\\n' > ../../x.txt
for i in $(seq -w 1 25); do printf 'made\\n' > "../../z-made-$i.txt"; done
git add -- notes.md ../../x.txt ../../z-made-*.txt
git ${SESSION} commit -q -m "the session's commit on main"
git checkout -q "$was"
`)
      const said = await c.ws.run("")
      inside = { c, said, takenAfter: await takenIn(c) }
    })()
  ])
}, 900_000)

afterAll(clean)

describe("REQ-FLOW-001, REQ-FLOW-008: a move of main that changes no file, and what main gains while no session's identities are kept", () => {
  it("REQ-FLOW-001 acceptance: while a session works, main is moved by a commit that changes no file: the run names main, asks nothing on it, and its words are as they were", () => {
    const { first } = between
    expect(first.code, first.out).toBe(0)
    const line = lineOf(first, "While the session on induct-ticket worked, these changed among the repository's branches, tags and stash")
    expect(line, first.out).toBe("While the session on induct-ticket worked, these changed among the repository's branches, tags and stash; it may have been the session or you, and none holds the ticket: main (changed).")
    expect(first.out).toContain("waits for your answer on induct-ticket")
    expect(first.out).not.toContain("waits for your ruling")
    expect(first.out).not.toContain("committed on main")
  })

  it("REQ-FLOW-008 acceptance: between two runs, with no session at work and no ruling awaited, the user commits a change on main: the next run takes it in and asks nothing on what changed", () => {
    const { second, takenAfter, heldAfter } = between
    expect(second.code, second.out).toBe(0)
    expect(second.out).not.toContain("waits for your ruling")
    expect(second.out).toContain("waits for your answer on write-specification")
    expect(takenAfter).toBe(true)
    expect(heldAfter).toBe(true)
  })
})

describe("REQ-FLOW-004: the user edits the active ticket on main while a session works", () => {
  it("REQ-FLOW-004 acceptance: the run waits for the user's ruling and names the ticket as changed on main, and takes nothing of main in", () => {
    const { c, asked, takenAsked } = edited
    expect(asked.code, asked.out).toBe(0)
    expect(asked.out).toContain("The run waits for your ruling on what changed while the session on write-specification worked")
    expect(asked.out).toContain(`- .ai-workspace/tickets/active/${c.ticket}.md (changed on main)`)
    expect(takenAsked).toBe(false)
  })

  it("REQ-FLOW-004 acceptance, REQ-FLOW-008 acceptance: after the yes, main is taken in, with the edit, and the ticket is inducted again", async () => {
    const { c, after, afterLog } = edited
    expect(after.code, after.out).toBe(0)
    expect(await takenIn(c)).toBe(true)
    expect(afterLog.some((e) => e.event === "commit made" && e.why === "the user edited the active ticket on main"), JSON.stringify(afterLog)).toBe(true)
    expect(c.ws.git(["show", `${branch(c)}:.ai-workspace/tickets/active/${c.ticket}.md`])).toContain("It also prints a second line, goodbye.")
    expect(after.out).toContain("waits for your answer on induct-ticket")
  })
})

describe("REQ-FLOW-001, REQ-PARAM-001: inside a larger repository, what a session commits on main", () => {
  it("REQ-FLOW-001 acceptance: a working session commits on main a file of the workspace's folder and a changed file of the user's outside the folder: the run waits for the user's ruling on the first, and names the second as committed on main while the session worked", () => {
    const { said, takenAfter } = inside
    expect(said.code, said.out).toBe(0)
    expect(said.out).toContain("The run waits for your ruling on what changed while the session on induct-ticket worked")
    expect(said.out).toContain("- notes.md (added on main)")
    const line = lineOf(said, "While the session on induct-ticket worked, these were committed on main, the branch the ticket left, outside the workspace's folder")
    expect(line, said.out).toContain("x.txt (changed)")
    expect(line).toContain("it may have been the session or you, nothing is asked on them, and none of them holds the ticket")
    // Nothing is asked on a file outside the folder.
    const question = said.out.split("\n").filter((l) => l.startsWith("- "))
    expect(question.some((l) => l.includes("x.txt") || l.includes("z-made-")), question.join("\n")).toBe(false)
    expect(takenAfter).toBe(false)
  })

  it("REQ-PARAM-001, REQ-FLOW-001: of the files outside the folder committed on main while a session worked, 20 are named, with how many there are, counted apart from those committed on the ticket's branch", () => {
    const line = lineOf(inside.said, "While the session on induct-ticket worked, these were committed on main")
    expect(line.match(/z-made-\d+\.txt \(added\)/g), inside.said.out).toHaveLength(19)
    expect(line).toContain("20 named of 26")
    expect(inside.said.out).not.toContain("these files outside the workspace's folder were committed;")
  })
})
