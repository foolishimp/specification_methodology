/**
 * Main is not taken in where a path it adds is there already in the user's
 * folder, as a file or a folder, or a folder on the way to it is there as a
 * file, inside the workspace's folder or outside it (REQ-FLOW-008). Git
 * ignores each such thing here, so git's own take-in would write over it with
 * no word, and none of it is in a commit. In each case a ticket waits on the
 * user's answer on its induction; main then gains a commit, made in a working
 * tree of its own that is removed before the run, so the user's folder is
 * not touched; the user answers yes, and the run that follows is refused
 * before any step, names the path, takes nothing in, and leaves the user's
 * file or folder as it was:
 *
 * - main adds `local.cfg`; the user has a file `local.cfg`;
 * - main adds a file `out`; the user has a folder `out/` with a file in it;
 * - main adds `cfg/local.json`; the user has a file `cfg`;
 * - the workspace lies below the top of a larger repository, and main adds
 *   `local.cfg` at the repository's top, where the user has one.
 *
 * Once the user has moved it aside, the next run takes main in.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-FLOW-008 REQ-FLOW-003
 */
import { execFileSync } from "node:child_process"
import { existsSync, mkdirSync, readFileSync, renameSync, statSync } from "node:fs"
import { join } from "node:path"
import { afterAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, temporary, write, Workspace, type Said } from "./scenario_driver.js"

const cli = build()
afterAll(() => clean())

const USER = ["-c", "user.name=User", "-c", "user.email=user@example.com"]

interface Case {
  /** The paths main adds, from the repository's top, with what each holds. */
  readonly adds: Readonly<Record<string, string>>
  /** The user's own things in the way, from the repository's top: a file with its text, or a folder with one file in it. */
  readonly mine: { readonly path: string; readonly file?: string; readonly folder?: { readonly name: string; readonly text: string } }
  /** The path the run names, as it names it. */
  readonly named: string
  /** The workspace's folder below the repository's top, where it lies inside a larger repository. */
  readonly within?: readonly string[]
}

interface Seen {
  readonly ws: Workspace
  readonly ticket: string
  readonly refused: Said
  readonly sessionsAfter: number
  readonly takenIn: boolean
  readonly mineAfter: string
  readonly mineBefore: string
  readonly tipBefore: string
  readonly tipAfter: string
  readonly then: Said
  readonly takenInThen: boolean
}

/** What the user's thing in the way holds: a file's text, or a folder's one file's text, with what it is. */
const kept = (path: string): string => {
  if (!existsSync(path)) return "gone"
  const s = statSync(path)
  if (s.isFile()) return `file: ${readFileSync(path, "utf8")}`
  return `folder: ${readFileSync(join(path, "kept.txt"), "utf8")}`
}

async function seen(c: Case): Promise<Seen> {
  const ws = new Workspace(cli, undefined, c.within ?? [])
  const top = ws.top
  const git = (args: readonly string[]): string => execFileSync("git", ["-C", top, ...args], { encoding: "utf8", env: ws.env, stdio: ["ignore", "pipe", "pipe"] })
  if (c.within !== undefined) {
    git(["init", "-q", "-b", "main"])
    write(join(top, "README"), "a larger repository\n")
    git(["add", "-A"])
    git([...USER, "commit", "-qm", "the repository's own file"])
    mkdirSync(ws.root, { recursive: true })
  }
  await ws.setup()
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  // The run inducts the ticket and waits for the user's answer.
  await ws.run(S1_FIXTURES)
  // Main gains a commit that adds the paths, made in a working tree of its own, which is removed before the run.
  const other = join(temporary("stdo-builder-main-"), "main")
  git(["worktree", "add", "-q", other, "main"])
  for (const [path, text] of Object.entries(c.adds)) write(join(other, path), text)
  execFileSync("git", ["-C", other, ...USER, "add", "-A"], { env: ws.env })
  execFileSync("git", ["-C", other, ...USER, "commit", "-qm", "main adds what the user has, ignored"], { env: ws.env })
  git(["worktree", "remove", "--force", other])
  // The user's own thing, which git ignores, in the folder.
  const exclude = git(["rev-parse", "--path-format=absolute", "--git-path", "info/exclude"]).trim()
  write(exclude, `${c.mine.path}\n`)
  const mine = join(top, c.mine.path)
  if (c.mine.file !== undefined) write(mine, c.mine.file)
  if (c.mine.folder !== undefined) write(join(mine, c.mine.folder.name), c.mine.folder.text)
  const mineBefore = kept(mine)
  await ws.answer("yes")
  const tipBefore = git(["rev-parse", `stdo/${ticket}`]).trim()
  const from = ws.log().length
  const refused = await ws.run(S1_FIXTURES)
  const after = ws.log().slice(from)
  const takenIn = (): boolean => {
    try {
      git(["merge-base", "--is-ancestor", "main", `stdo/${ticket}`])
      return true
    } catch {
      return false
    }
  }
  const seenThen = {
    refused,
    sessionsAfter: after.filter((e) => e.event === "session started").length,
    takenIn: takenIn(),
    mineAfter: kept(mine),
    tipAfter: git(["rev-parse", `stdo/${ticket}`]).trim()
  }
  // The user moves the thing aside; the next run takes main in.
  renameSync(mine, `${mine}.aside`)
  const then = await ws.run(S1_FIXTURES)
  return { ws, ticket, mineBefore, tipBefore, ...seenThen, then, takenInThen: takenIn() }
}

const CASES: Readonly<Record<string, Case>> = {
  "main adds a file local.cfg where the user has a file local.cfg that git ignores": {
    adds: { "local.cfg": "main's settings\n" },
    mine: { path: "local.cfg", file: "the user's own settings\n" },
    named: "local.cfg"
  },
  "main adds a file out where the user has a folder out/ that git ignores, with a file in it": {
    adds: { out: "main's out\n" },
    mine: { path: "out", folder: { name: "kept.txt", text: "what the user's build left\n" } },
    named: "out"
  },
  "main adds cfg/local.json where the user has a file cfg that git ignores": {
    adds: { "cfg/local.json": "{}\n" },
    mine: { path: "cfg", file: "the user's cfg\n" },
    named: "cfg"
  },
  "the workspace lies inside a larger repository, and main adds local.cfg at its top, outside the workspace's folder, where the user has one that git ignores": {
    adds: { "local.cfg": "main's settings\n" },
    mine: { path: "local.cfg", file: "the user's own settings\n" },
    named: "local.cfg",
    within: ["product"]
  }
}

describe("main is not taken in over what the user has and git does not hold", () => {
  const all = Promise.all(Object.entries(CASES).map(async ([name, c]) => [name, await seen(c)] as const)).then((pairs) => new Map(pairs))
  for (const [name, c] of Object.entries(CASES)) {
    it(name, async () => {
      const s = (await all).get(name)
      if (s === undefined) throw new Error(name)
      // The run is refused before any step, starts no session, and names the path.
      expect(s.refused.code, s.refused.out).toBe(2)
      expect(s.refused.out).toContain("The run is refused before any step")
      expect(s.refused.out).toContain(c.named)
      expect(s.refused.out).toContain("git ignores")
      expect(s.sessionsAfter).toBe(0)
      // Main is not taken in: the ticket's branch is where it was, and does not hold main.
      expect(s.takenIn).toBe(false)
      expect(s.tipAfter).toBe(s.tipBefore)
      // The user's file or folder is as it was.
      expect(s.mineAfter).toBe(s.mineBefore)
      // Once it is moved aside, the next run takes main in.
      expect(s.takenInThen, s.then.out).toBe(true)
    }, 300_000)
  }
})
