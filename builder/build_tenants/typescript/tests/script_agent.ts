/**
 * The stand-in of scenario S14 (REQ-VERIFY-002): an agent the settings name,
 * a script started as a process of its own, that starts a further process in
 * a session of processes of its own, which keeps the session's output open
 * and writes into the workspace's folder again and again until it is ended.
 * What the script then does is read, at each start, from `<state>/case`:
 * `over` (it waits until it is ended, on its first start), `return`, `fail`
 * (it exits with 1), `wait` (it waits until it is ended), `trespass` (it changes the settings file and the governing graph and writes a file, in the workspace's folder, and waits until it is ended, S14 case 11), `inside` (it gives
 * the product's commands on the workspace, on the product set up at `inner`
 * inside it and on a folder inside that, then on a workspace of its own, and
 * returns), `survive` (it returns, and its
 * further process, at each terminate signal, starts one more in its place and
 * ends, so it outlives every round of ending it), `ignore` (it returns, and
 * its further process takes no notice of the terminate signal), `reexec` (it
 * returns, and its further process starts a new program in its place, itself
 * with a new argument, again and again, so its command changes between any
 * two lines the framework reads of it) or `unread` (it makes the process
 * table unreadable to the framework, through the `ps` the driver puts first
 * on its path, and returns). With `shell-` before `over`, `wait`, `group` or
 * `place`, its further process is a shell, one of the system's own programs,
 * whose environment the system does not show, that takes no notice of the
 * terminate signal (S14 cases 8 to 10): for `over` and `wait`, in a session of
 * processes of its own, and the script does as for `over` and `wait`; for
 * `group`, in the script's own process group, and the script returns; for
 * `place`, in a session of processes of its own, working in the
 * workspace's folder, and the script returns. The script and its
 * further processes write their numbers to the state folder, outside the
 * workspace, so the driver ends nothing by a pattern and judges by those
 * numbers alone.
 *
 * @uses C14
 * @is REQ-VERIFY-002 REQ-FLOW-001 REQ-FLOW-005
 */
import { execFileSync } from "node:child_process"
import { chmodSync, existsSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { temporary, Workspace, write } from "./scenario_driver.js"

const SCRIPT = `
import { spawn, execFileSync } from "node:child_process"
import { appendFileSync, cpSync, existsSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
const [state, cli] = process.argv.slice(2)
let n = 1
while (existsSync(join(state, "agent." + n + ".pid"))) n++
writeFileSync(join(state, "agent." + n + ".pid"), String(process.pid))
const list = readFileSync(join(state, "case"), "utf8").trim().split(",")
const how = list[Math.min(n, list.length) - 1]
const loop = (how === "ignore" ? "process.on('SIGTERM', () => {}); " : "") + "const { appendFileSync } = require('node:fs'); setInterval(() => appendFileSync('stray.txt', '" + n + " ' + Date.now() + '\\\\n'), 30)"
const shell = how.startsWith("shell-")
const further = shell
  ? spawn("/bin/zsh", [join(state, "further.zsh"), String(n)], { detached: how !== "shell-group", stdio: ["ignore", "inherit", "inherit"] })
  : spawn(process.execPath, how === "survive" ? [join(state, "survivor.cjs"), join(state, "chain")] : how === "reexec" ? [join(state, "reexec.cjs"), "0"] : ["-e", loop], { detached: true, stdio: ["ignore", "inherit", "inherit"] })
writeFileSync(join(state, "further." + n + ".pid"), String(further.pid))
further.unref()
console.log("the script started its further process " + further.pid)
if (how === "copy") { cpSync(readFileSync(join(state, "copy"), "utf8").trim(), process.cwd(), { recursive: true }); process.exit(0) }
const forever = () => setInterval(() => {}, 1000)
if (how === "over" || how === "shell-over") { if (n === 1) forever(); else process.exit(0) }
else if (how === "trespass") {
  appendFileSync(join(".stdo-builder", "settings.json"), "\\n")
  appendFileSync(join(".stdo-builder", "graph.json"), "\\n")
  writeFileSync(join(readFileSync(join(state, "root"), "utf8").trim(), "a-file-the-session-wrote.txt"), "written while the session worked\\n")
  writeFileSync(join(state, "trespassed"), "")
  forever()
}
else if (how === "wait" || how === "shell-wait") forever()
else if (how === "shell-group" || how === "shell-place") process.exit(0)
else if (how === "fail") process.exit(1)
else if (how === "unread") { writeFileSync(join(state, "unread"), ""); process.exit(0) }
else if (how === "inside") {
  const root = readFileSync(join(state, "root"), "utf8").trim()
  const other = readFileSync(join(state, "other"), "utf8").trim()
  const said = (args) => { try { return { code: 0, out: execFileSync(process.execPath, [cli, ...args], { encoding: "utf8" }) } } catch (e) { return { code: e.status, out: String(e.stdout) } } }
  const inner = join(root, "inner")
  const given = [
    ["ticket", root, "a ticket a session writes"], ["run", root], ["answer", root, "yes"], ["show", root], ["registry", root], ["record-release", root], ["setup", root, "--name", "Again"],
    ["ticket", inner, "a ticket a session writes"], ["run", inner], ["answer", inner, "yes"], ["show", inner], ["registry", inner], ["record-release", inner], ["setup", inner, "--name", "Again"], ["setup", join(inner, "deeper"), "--name", "Deeper"],
    ["setup", other, "--name", "Other"], ["ticket", other, "a ticket of another workspace"]
  ].map((args) => ({ args, ...said(args) }))
  // The other workspace's agent is a script whose further process stays behind: a run there starts sessions, holds its ticket and ends their processes.
  const settings = join(other, ".stdo-builder", "settings.json")
  const s = JSON.parse(readFileSync(settings, "utf8"))
  s.agents.inner = [process.execPath, join(state, "inner.cjs"), join(state, "inner.pids")]
  s.work = "inner"
  s.evaluation = "inner"
  writeFileSync(settings, JSON.stringify(s, null, 2) + "\\n")
  given.push({ args: ["run", other], ...said(["run", other]) }, { args: ["show", other], ...said(["show", other]) })
  writeFileSync(join(state, "inside.json"), JSON.stringify(given))
  process.exit(0)
}
`

/** The further process of `survive`: at each terminate signal it starts one more in its place, which inherits its environment, and ends; each notes its number. */
const SURVIVOR = `
const { spawn } = require("node:child_process")
const { appendFileSync } = require("node:fs")
const chain = process.argv[2]
appendFileSync(chain, process.pid + "\\n")
process.on("SIGTERM", () => {
  const g = Number(process.env.STDO_TEST_GENERATION || "0")
  if (g < 200) spawn(process.execPath, [__filename, chain], { detached: true, stdio: "ignore", env: { ...process.env, STDO_TEST_GENERATION: String(g + 1) } }).unref()
  process.exit(0)
})
setInterval(() => {}, 1000)
`

/** The further process of `reexec`: it starts a new program in its place, itself with a new argument, again and again; its number stays. */
const REEXEC = `process.execve(process.execPath, [process.execPath, __filename, String(Number(process.argv[2] ?? "0") + 1)], process.env)
`

/** The further process of the `shell-` cases: a shell that takes no notice of the terminate signal and writes into the folder it works in, the session's number and the time to the thousandth of a second, every 30 ms. */
const FURTHER_SHELL = `trap '' TERM
zmodload zsh/datetime
while :; do print -r -- "$1 $(( EPOCHREALTIME * 1000 ))" >> stray.txt; /bin/sleep 0.03; done
`

/** The agent of the other workspace of `inside`: it starts a further process that stays behind, notes its number and returns. */
const INNER = `
const { spawn } = require("node:child_process")
const { appendFileSync } = require("node:fs")
const c = spawn(process.execPath, ["-e", "setInterval(() => {}, 1000)"], { detached: true, stdio: "ignore" })
c.unref()
appendFileSync(process.argv[2], c.pid + "\\n")
`

export interface Agent {
  /** The folder, outside the workspace, of the script and of the numbers its processes write. */
  readonly state: string
  /** Sets what the script does at its next start. */
  readonly does: (how: string) => void
  /** The numbers of the script's processes and of its further processes, in the order they started. */
  readonly agents: () => readonly number[]
  readonly further: () => readonly number[]
  /** The numbers of the processes of `survive`'s chain, and of the other workspace's further processes in `inside`, in the order they started. */
  readonly chain: () => readonly number[]
  readonly inner: () => readonly number[]
  /** A folder that holds a `ps` that cannot read the table once the script has run `unread`, and runs the system's own until then: put first on the framework's path. */
  readonly bin: string
  /** Makes the table readable again. */
  readonly readable: () => void
}

/**
 * Writes the script and names it in the workspace's settings, on main, as the
 * agent of every session. Where `unwatched`, the repository ignores what the
 * further processes write, so a case whose subject is not the ruling on what
 * changed (REQ-FLOW-006) is not stopped by it.
 */
export function scriptAgent(ws: Workspace, unwatched = false): Agent {
  const state = temporary("stdo-builder-agent-")
  if (unwatched) {
    const exclude = execFileSync("git", ["rev-parse", "--path-format=absolute", "--git-path", "info/exclude"], { cwd: ws.root, encoding: "utf8" }).trim()
    write(exclude, `${existsSync(exclude) ? readFileSync(exclude, "utf8") : ""}stray.txt\n`)
  }
  write(join(state, "agent.mjs"), SCRIPT)
  write(join(state, "survivor.cjs"), SURVIVOR)
  write(join(state, "inner.cjs"), INNER)
  write(join(state, "reexec.cjs"), REEXEC)
  write(join(state, "further.zsh"), FURTHER_SHELL)
  write(join(state, "root"), `${ws.root}\n`)
  const bin = join(state, "bin")
  write(join(bin, "ps"), `#!/bin/sh\nif [ -e "${join(state, "unread")}" ]; then echo "ps: the table cannot be read" >&2; exit 1; fi\nexec /bin/ps "$@"\n`)
  chmodSync(join(bin, "ps"), 0o755)
  const settings = ws.path(".stdo-builder", "settings.json")
  const s = JSON.parse(readFileSync(settings, "utf8")) as { agents: Record<string, string[]>; work: string; evaluation: string }
  s.agents.script = [process.execPath, join(state, "agent.mjs"), state, ws.cli]
  s.work = "script"
  s.evaluation = "script"
  writeFileSync(settings, `${JSON.stringify(s, null, 2)}\n`)
  const pids = (kind: string) =>
    readdirSync(state).filter((f) => f.startsWith(`${kind}.`) && f.endsWith(".pid")).sort((a, b) => Number(a.split(".")[1]) - Number(b.split(".")[1])).map((f) => Number(readFileSync(join(state, f), "utf8")))
  const listed = (file: string) => (existsSync(join(state, file)) ? readFileSync(join(state, file), "utf8").split("\n").filter((l) => l !== "").map(Number) : [])
  return {
    state,
    does: (how) => write(join(state, "case"), `${how}\n`),
    agents: () => pids("agent"),
    further: () => pids("further"),
    chain: () => listed("chain"),
    inner: () => listed("inner.pids"),
    bin,
    readable: () => rmSync(join(state, "unread"), { force: true })
  }
}

/**
 * The agent of the bug items' tests (D231): a script the settings name for
 * every session, started by the framework with the brief's path as a process
 * of its own. It reads the vector and the kind from the brief's name and
 * writes the fixtures of that vector and kind into the workspace's folder, as
 * the stand-in does: each file of `files/`, `append` added to the place the
 * brief says it produces, `print` printed and `fails` an exit with 1. Where the
 * test has set it, it first does once what `<state>/first.<vector>.<kind>.sh`
 * says, before it writes anything, as its first act. Where the
 * test has set them, it then does once what `<state>/do.<vector>.<kind>.sh`
 * says, a shell script run in the folder with `ROOT` the workspace's folder,
 * and waits at `<state>/gate.<vector>.<kind>` until the test writes
 * `<state>/open.<vector>.<kind>`, having written `<state>/at.<vector>.<kind>`.
 * It keeps a copy of each brief in the state folder. It starts no further
 * process.
 */
const FIXTURE = `
import { execFileSync } from "node:child_process"
import { appendFileSync, cpSync, existsSync, readFileSync, renameSync, writeFileSync } from "node:fs"
import { basename, join } from "node:path"
const [state, fixtures, brief] = process.argv.slice(2)
const [vector, kind] = basename(brief).replace(/\\.md$/, "").split(".")
const name = vector + "." + kind
const text = readFileSync(brief, "utf8")
appendFileSync(join(state, "sessions"), name + "\\n")
writeFileSync(join(state, "brief." + name + ".md"), text)
const once = (script) => {
  if (!existsSync(script)) return
  renameSync(script, script + ".done")
  execFileSync("/bin/sh", [script + ".done"], { stdio: "inherit", env: { ...process.env, ROOT: readFileSync(join(state, "root"), "utf8").trim() } })
}
once(join(state, "first." + name + ".sh"))
const here = join(fixtures, vector, kind)
if (!existsSync(here)) { console.log("no fixtures for " + name); process.exit(1) }
if (existsSync(join(here, "files"))) cpSync(join(here, "files"), process.cwd(), { recursive: true })
const produce = /^- produce: .* at (\\S+)/m.exec(text)?.[1]
if (existsSync(join(here, "append")) && kind === "work" && produce !== undefined) appendFileSync(produce, readFileSync(join(here, "append"), "utf8"))
once(join(state, "do." + name + ".sh"))
if (existsSync(join(state, "gate." + name))) {
  writeFileSync(join(state, "at." + name), "")
  const until = Date.now() + 5 * 60_000
  while (!existsSync(join(state, "open." + name)) && Date.now() < until) execFileSync("/bin/sleep", ["0.1"])
}
if (existsSync(join(here, "print"))) process.stdout.write(readFileSync(join(here, "print"), "utf8"))
process.exit(existsSync(join(here, "fails")) ? 1 : 0)
`

export interface Fixed {
  readonly state: string
  /** Sets a shell script the session of this vector and kind runs once, as its first act, before it writes anything, in the folder, with `ROOT` the workspace's folder. */
  readonly first: (at: string, script: string) => void
  /** Sets a shell script the session of this vector and kind runs once, in the folder, with `ROOT` the workspace's folder. */
  readonly does: (at: string, script: string) => void
  /** Sets a gate at the session of this vector and kind; `at` holds once it waits there, and `open` lets it go on. */
  readonly gate: (at: string) => void
  readonly waiting: (at: string) => boolean
  readonly open: (at: string) => void
  /** The sessions started, by `<vector>.<kind>`, in order. */
  readonly sessions: () => readonly string[]
  /** The brief the session of this vector and kind was given last. */
  readonly brief: (at: string) => string | undefined
}

/** Writes the fixture agent and names it in the workspace's settings, on main, as the agent of every session (D231). */
export function fixtureAgent(ws: Workspace, fixtures: string): Fixed {
  const state = temporary("stdo-builder-fixed-")
  write(join(state, "agent.mjs"), FIXTURE)
  write(join(state, "root"), `${ws.root}\n`)
  const settings = ws.path(".stdo-builder", "settings.json")
  const s = JSON.parse(readFileSync(settings, "utf8")) as { agents: Record<string, string[]>; work: string; evaluation: string }
  s.agents.fixed = [process.execPath, join(state, "agent.mjs"), state, fixtures]
  s.work = "fixed"
  s.evaluation = "fixed"
  writeFileSync(settings, `${JSON.stringify(s, null, 2)}\n`)
  const read = (f: string): string | undefined => (existsSync(join(state, f)) ? readFileSync(join(state, f), "utf8") : undefined)
  return {
    state,
    first: (at, script) => write(join(state, `first.${at}.sh`), script),
    does: (at, script) => write(join(state, `do.${at}.sh`), script),
    gate: (at) => write(join(state, `gate.${at}`), ""),
    waiting: (at) => existsSync(join(state, `at.${at}`)),
    open: (at) => write(join(state, `open.${at}`), ""),
    sessions: () => (read("sessions") ?? "").split("\n").filter((l) => l !== ""),
    brief: (at) => read(`brief.${at}.md`)
  }
}

/** Kills each process of these numbers that is alive. */
export function killAll(pids: readonly number[]): void {
  for (const pid of pids) {
    try {
      process.kill(pid, "SIGKILL")
    } catch {
      // It ended.
    }
  }
}

/** Whether the process of this number is alive: a zombie is not. */
export function alive(pid: number): boolean {
  try {
    return !execFileSync("ps", ["-o", "stat=", "-p", String(pid)], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim().startsWith("Z")
  } catch {
    return false
  }
}

/** The lines the further processes wrote into the folder: by the session's number, the times they were written. */
export function strayLines(folder: string): ReadonlyMap<number, readonly number[]> {
  const file = join(folder, "stray.txt")
  const out = new Map<number, number[]>()
  if (!existsSync(file)) return out
  for (const l of readFileSync(file, "utf8").split("\n")) {
    const [n, t] = l.split(" ").map(Number)
    if (n !== undefined && t !== undefined && Number.isFinite(n) && Number.isFinite(t)) out.set(n, [...(out.get(n) ?? []), t])
  }
  return out
}
