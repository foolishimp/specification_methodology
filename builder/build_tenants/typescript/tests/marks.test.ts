/**
 * C12, the processes of a session (REQ-FLOW-001): the framework knows a
 * process to be of the session by its parent, by its group and by its mark,
 * the agent's own process first, and what it has once known it knows until
 * that process has ended. It ends only a process it knows. A process it
 * cannot place, one that started after the session did, has no parent left
 * alive, is of the session in none of the three ways, shows no environment
 * and works in the session's folder, it does not end, and names. A shell is
 * one of the system's own programs, whose environment the system does not
 * show (D212, D222, D223).
 *
 * Every process these tests start as a session's would be is started as the
 * leader of a session of processes of its own, as the framework starts an
 * agent. Each waits within a bound, and judges nothing after a fixed pause.
 *
 * @uses C12
 * @is REQ-FLOW-001 REQ-FLOW-005
 */
import * as NodeServices from "@effect/platform-node/NodeServices"
import * as Effect from "effect/Effect"
import { execFileSync, spawn, type ChildProcess } from "node:child_process"
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, describe, expect, it } from "vitest"
import { endMarked, marked, startKey, type Sought } from "../src/kit/supervised_child.js"
import { clean, temporary, until } from "./scenario_driver.js"

const started: ChildProcess[] = []
const kin: number[] = []

afterAll(() => {
  for (const c of started) c.kill("SIGKILL")
  for (const pid of kin) {
    try {
      process.kill(pid, "SIGKILL")
    } catch {
      // It ended.
    }
  }
  clean()
})

/** The environment of this process, without the marks it inherited. */
const unmarked = (): NodeJS.ProcessEnv => {
  const plain = { ...process.env }
  for (const k of Object.keys(plain)) if (k.startsWith("STDO_BUILDER_SESSION_")) delete plain[k]
  return plain
}

/** Starts a process as the leader of a session of processes of its own, as the framework starts an agent. */
const leader = (command: string, args: readonly string[], env: NodeJS.ProcessEnv, cwd?: string): ChildProcess => {
  const c = spawn(command, [...args], { env, stdio: "ignore", detached: true, ...(cwd === undefined ? {} : { cwd }) })
  started.push(c)
  return c
}

const sleeper = (args: readonly string[], env: NodeJS.ProcessEnv): ChildProcess => leader(process.execPath, ["-e", "setInterval(() => {}, 1000)", ...args], env)

/** When the process of this number started, as `ps` gives it in the C locale. */
const startOf = (pid: number): string =>
  execFileSync("ps", ["-o", "lstart=", "-p", String(pid)], { encoding: "utf8", env: { ...process.env, LC_ALL: "C" } }).trim().split(/\s+/).join(" ")

/** Whether the process of this number is alive: a zombie is not. */
const alive = (pid: number): boolean => {
  try {
    return !execFileSync("ps", ["-o", "stat=", "-p", String(pid)], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim().startsWith("Z")
  } catch {
    return false
  }
}

/** The number a file holds, once it holds one. */
const numberIn = async (file: string): Promise<number> => {
  await until(() => existsSync(file) && /^[0-9]+\s*$/.test(readFileSync(file, "utf8")), 30)
  const pid = Number(readFileSync(file, "utf8"))
  kin.push(pid)
  return pid
}

/** What `marked` finds, by number: the processes it knows to be alive, and those it cannot place; or why it cannot tell. */
const found = (sought: Sought): Promise<{ readonly alive: ReadonlySet<number>; readonly unplaced: ReadonlySet<number> } | { readonly cannot: string }> =>
  Effect.runPromise(
    Effect.match(marked(sought), {
      onFailure: (e) => ({ cannot: e.why }),
      onSuccess: (f) => ({ alive: new Set(f.alive.map((p) => p.pid)), unplaced: new Set(f.unplaced.map((p) => p.pid)) })
    }).pipe(Effect.provide(NodeServices.layer))
  )

const ending = (sought: Sought) => Effect.runPromise(endMarked(sought).pipe(Effect.provide(NodeServices.layer)))

/** A process that starts a new program in its place, itself with a new argument, again and again: its command changes, its number and start stay. */
const RE_EXEC = `process.execve(process.execPath, [process.execPath, __filename, String(Number(process.argv[2] ?? "0") + 1)], process.env)
`

/** A shell script, run by a shell, whose environment the system does not show: it writes its number to `<state>/<name>` and waits, taking no notice of the terminate signal. Its path. */
const SHELL_WAITS = (state: string, name: string): string => {
  const script = join(state, `${name}.zsh`)
  writeFileSync(script, `trap '' TERM\nprint $$ > ${JSON.stringify(join(state, name))}\nwhile :; do /bin/sleep 0.05; done\n`)
  return script
}

const mark = (state: string) => ({ name: "STDO_BUILDER_SESSION_marks_test", value: encodeURIComponent(join(state, "ws")) })

describe("C12 the processes of a session (D212, D222, D223)", () => {
  it("by its mark, and by its parent: a process whose environment holds the mark's entry whole, and its child that cleared its environment; no process of another workspace's mark, nor one whose command holds the entry as text", { timeout: 60_000 }, async () => {
    const state = temporary("stdo-builder-marks-")
    const m = mark(state)
    const kinFile = join(state, "kin")
    const own = leader(process.execPath, ["-e", `
      const { spawn } = require("node:child_process")
      const c = spawn(process.execPath, ["-e", "setInterval(() => {}, 1000)"], { env: {}, stdio: "ignore", detached: true })
      require("node:fs").writeFileSync(${JSON.stringify(kinFile)}, String(c.pid))
      setInterval(() => {}, 1000)
    `], { ...unmarked(), [m.name]: m.value })
    const other = sleeper([], { ...unmarked(), [m.name]: `${m.value}-other` })
    const said = sleeper([`${m.name}=${m.value}`], unmarked())
    const child = await numberIn(kinFile)
    const seen = await found({ mark: m })
    expect(seen).toEqual({ alive: new Set([own.pid, child]), unplaced: new Set() })
    expect(other.pid).toBeDefined()
    expect(said.pid).toBeDefined()
  })

  it("the agent's own process, by its number and when it started, though the system shows no environment for it; and by its parent, a shell in a session of its own that it started", { timeout: 60_000 }, async () => {
    const state = temporary("stdo-builder-marks-")
    const m = mark(state)
    // The agent is a shell, which starts a further shell as the leader of a session of processes of its own.
    const agent = leader("/bin/zsh", ["-c", `/usr/bin/perl -MPOSIX -e 'POSIX::setsid(); exec @ARGV' /bin/zsh ${SHELL_WAITS(state, "further")} & while :; do /bin/sleep 0.05; done`], { ...unmarked(), [m.name]: m.value })
    const further = await numberIn(join(state, "further"))
    const pid = agent.pid ?? -1
    // Neither shows the mark: without the agent's own process, neither is known.
    const without = await found({ mark: m })
    expect(without).toEqual({ alive: new Set(), unplaced: new Set() })
    const seen = await found({ mark: m, agent: { pid, start: startOf(pid) } })
    expect("alive" in seen && seen.alive.has(pid) && seen.alive.has(further)).toBe(true)
  })

  it("what it has once known it knows until that process has ended: the further shell, which takes no notice of the terminate signal and loses its parent while it is being ended, is still ended, and counted when it is gone", { timeout: 60_000 }, async () => {
    const state = temporary("stdo-builder-marks-")
    const m = mark(state)
    const agent = leader("/bin/zsh", ["-c", `/usr/bin/perl -MPOSIX -e 'POSIX::setsid(); exec @ARGV' /bin/zsh ${SHELL_WAITS(state, "further")} & while :; do /bin/sleep 0.05; done`], unmarked())
    const further = await numberIn(join(state, "further"))
    const pid = agent.pid ?? -1
    const e = await ending({ mark: m, agent: { pid, start: startOf(pid) } })
    expect(e.unended).toBeUndefined()
    expect(e.ended).toBeGreaterThanOrEqual(2)
    expect(alive(pid)).toBe(false)
    expect(alive(further)).toBe(false)
  })

  it("by its group: a shell left in the group the agent led, after the agent has ended, is known and ended; the group of the framework's own process never is", { timeout: 60_000 }, async () => {
    const state = temporary("stdo-builder-marks-")
    const m = mark(state)
    // The agent leads its group, starts a shell in it, and ends: the shell has no parent left, and shows no environment.
    const agent = leader("/bin/zsh", ["-c", `/bin/zsh ${SHELL_WAITS(state, "left")} &!`], unmarked())
    const left = await numberIn(join(state, "left"))
    const pid = agent.pid ?? -1
    await until(() => !alive(pid), 30)
    const seen = await found({ mark: m, agent: { pid } })
    expect("alive" in seen && seen.alive.has(left)).toBe(true)
    expect(seen).toHaveProperty("unplaced", new Set())
    const e = await ending({ mark: m, agent: { pid } })
    expect(e.unended).toBeUndefined()
    expect(e.ended).toBeGreaterThanOrEqual(1)
    expect(alive(left)).toBe(false)
    // An agent in the group of this test's own process: that group is never taken as the session's, so no other process of it is found.
    const near = spawn(process.execPath, ["-e", "setInterval(() => {}, 1000)"], { env: unmarked(), stdio: "ignore" })
    started.push(near)
    const nearPid = near.pid ?? -1
    await until(() => alive(nearPid), 30)
    const ours = await found({ mark: m, agent: { pid: nearPid, start: startOf(nearPid) } })
    expect(ours).toEqual({ alive: new Set([nearPid]), unplaced: new Set() })
  })

  it("a process it cannot place: a shell in a session of its own, whose parent has ended, working in the session's folder, started after the session did; not one working elsewhere, nor one that started before", { timeout: 60_000 }, async () => {
    const state = temporary("stdo-builder-marks-")
    const m = mark(state)
    const folder = join(state, "checkout")
    const elsewhere = join(state, "elsewhere")
    mkdirSync(join(folder, "inner"), { recursive: true })
    mkdirSync(elsewhere)
    const since = startKey(startOf(process.pid)) ?? ""
    const start = (cwd: string, name: string): ChildProcess =>
      leader("/bin/zsh", ["-c", `/usr/bin/perl -MPOSIX -e 'POSIX::setsid(); exec @ARGV' /bin/zsh ${SHELL_WAITS(state, name)} &!`], { ...unmarked(), [m.name]: m.value }, cwd)
    start(join(folder, "inner"), "in")
    start(elsewhere, "out")
    const inside = await numberIn(join(state, "in"))
    const outside = await numberIn(join(state, "out"))
    const seen = await found({ mark: m, folder, since })
    expect(seen).toEqual({ alive: new Set(), unplaced: new Set([inside]) })
    // One that started before the session is not one it cannot place.
    expect(await found({ mark: m, folder, since: "29991231000000" })).toEqual({ alive: new Set(), unplaced: new Set() })
    // It ends none of them, and names the one it cannot place by its number, when it started and its command.
    const e = await ending({ mark: m, folder, since })
    expect(e.ended).toBe(0)
    expect(e.unended).toContain(`the process ${inside}, started ${startOf(inside)}, running /bin/zsh`)
    expect(e.unended).not.toContain(String(outside))
    expect(alive(inside)).toBe(true)
    expect(alive(outside)).toBe(true)
  })

  it("a process whose command changes between any two lines the framework reads of it, left behind in the session's folder, shows no environment it can read: it cannot place it, and names it", { timeout: 90_000 }, async () => {
    const state = temporary("stdo-builder-marks-")
    const m = mark(state)
    const folder = join(state, "checkout")
    mkdirSync(folder)
    writeFileSync(join(state, "reexec.cjs"), RE_EXEC)
    const since = startKey(startOf(process.pid)) ?? ""
    const at = join(state, "left")
    leader(process.execPath, ["-e", `
      const { spawn } = require("node:child_process")
      const c = spawn(process.execPath, [${JSON.stringify(join(state, "reexec.cjs"))}, "0"], { detached: true, stdio: "ignore" })
      c.unref()
      require("node:fs").writeFileSync(${JSON.stringify(at)}, String(c.pid))
    `], { ...unmarked(), [m.name]: m.value }, folder)
    const left = await numberIn(at)
    const seen = await found({ mark: m, folder, since })
    expect(seen).toEqual({ alive: new Set(), unplaced: new Set([left]) })
  })
})
