/**
 * A command that works in a workspace reads git's version before anything
 * else, and where it reads as older than the version the product needs, it is
 * refused, changes nothing, and names in one sentence the version found and
 * the version needed (REQ-INTERFACE-001; REQ-PARAM-001, 2.38 or later). The
 * stand-in for an older git is a script named `git`, first on the PATH, that
 * answers `--version` with `git version 2.34.1` and passes every other command
 * on to the git the system has. Each of the seven commands is given on a
 * workspace whose ticket waits on the user's answer; set-up is given on a
 * folder not yet there too. With the script answering `2.38.0`, the commands
 * work, so the script passes the rest on.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-INTERFACE-001 REQ-PARAM-001
 */
import { chmodSync, existsSync, readdirSync, readFileSync, statSync } from "node:fs"
import { execFileSync } from "node:child_process"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, S1_FIXTURES, S1_TICKET, temporary, write, Workspace, type Said } from "./scenario_driver.js"

const cli = build()
afterAll(() => clean())

/** Every file under the folder, ignored ones and git's own among them, by its path from the folder, with what it holds; git's index and its other files git rewrites when it reads the folder are left out. */
const filesUnder = (folder: string): Map<string, string> =>
  new Map((readdirSync(folder, { recursive: true }) as string[])
    .filter((p) => statSync(join(folder, p)).isFile() && !/^\.git\/(index|FETCH_HEAD|ORIG_HEAD)$/.test(p) && !p.startsWith(".git/objects/"))
    .sort()
    .map((p) => [p, readFileSync(join(folder, p), "utf8")]))

/** A folder holding a `git` that answers `--version` with `version`, and passes every other command on to the system's own git. */
function olderGit(version: string, env: NodeJS.ProcessEnv): string {
  const real = execFileSync("sh", ["-c", "command -v git"], { encoding: "utf8", env }).trim()
  const bin = temporary("stdo-builder-git-stand-in-")
  write(join(bin, "git"), `#!/bin/sh\nif [ "$1" = "--version" ]; then echo "git version ${version}"; exit 0; fi\nexec "${real}" "$@"\n`)
  chmodSync(join(bin, "git"), 0o755)
  return bin
}

let ws: Workspace
let said = new Map<string, Said>()
let before = new Map<string, string>()
let after = new Map<string, string>()
let refsBefore = ""
let refsAfter = ""
let notThere = ""
let atNewer = new Map<string, Said>()

const COMMANDS = (root: string): Readonly<Record<string, readonly string[]>> => ({
  setup: ["setup", root, "--name", "Hello"],
  ticket: ["ticket", root, "another thing"],
  run: ["run", root, "--stand-in", S1_FIXTURES],
  answer: ["answer", root, "yes"],
  show: ["show", root],
  registry: ["registry", root],
  "record-release": ["record-release", root]
})

beforeAll(async () => {
  ws = new Workspace(cli)
  await ws.setup()
  await ws.ticket(S1_TICKET)
  // The run inducts the ticket and waits on the user's answer.
  await ws.run(S1_FIXTURES)
  const refs = (): string => `${ws.git(["for-each-ref"])}${ws.git(["symbolic-ref", "HEAD"])}${ws.git(["status", "--porcelain", "--ignored", "--untracked-files=all"])}`
  before = filesUnder(ws.root)
  refsBefore = refs()
  const path = ws.env.PATH ?? ""
  ws.env.PATH = `${olderGit("2.34.1", ws.env)}:${path}`
  for (const [name, args] of Object.entries(COMMANDS(ws.root))) said.set(name, await ws.command(args))
  notThere = join(temporary("stdo-builder-new-"), "product")
  said.set("setup, on a folder not yet there", await ws.command(["setup", notThere, "--name", "Hello"]))
  ws.env.PATH = path
  after = filesUnder(ws.root)
  refsAfter = refs()
  // A git of the version needed: the script passes every other command on, and the commands work.
  ws.env.PATH = `${olderGit("2.38.0", ws.env)}:${path}`
  for (const name of ["show", "registry"]) atNewer.set(name, await ws.command(COMMANDS(ws.root)[name] ?? []))
  ws.env.PATH = path
}, 300_000)

describe("a git older than the product needs", () => {
  for (const name of [...Object.keys(COMMANDS("")), "setup, on a folder not yet there"]) {
    it(`${name}: refused, naming in one sentence the version found and the version needed`, () => {
      const s = said.get(name)
      expect(s?.code, s?.out).toBe(2)
      const words = (s?.out ?? "").trim()
      expect(words.split("\n")).toHaveLength(1)
      expect(words).toContain("2.34.1")
      expect(words).toContain("2.38 or later")
      expect(words).toContain("nothing is changed")
    })
  }

  it("changes nothing: every file of the workspace, the event log among them, its branches and HEAD are as they were, and no folder is made", () => {
    expect([...after.keys()]).toEqual([...before.keys()])
    for (const [path, text] of before) expect(after.get(path), path).toBe(text)
    expect(refsAfter).toBe(refsBefore)
    expect(existsSync(notThere)).toBe(false)
  })

  it("a git that gives 2.38.0 is enough: the commands work, so the script passes every other command on", () => {
    for (const [name, s] of atNewer) expect(s.code, `${name}: ${s.out}`).toBe(0)
  })
})
