/**
 * Supervised child with a deadline: start a process, wait for its return or
 * for the deadline, and end it at the deadline. Each start has exactly one
 * outcome: it returned (with its exit code and what it printed), it could not
 * start, it stopped without returning, it ran over, or the run that started it
 * was cut off by a signal; the last three with what it printed until then.
 * This is the one module that starts a process; it wraps Effect's process
 * module.
 *
 * A child given a mark is a session's agent (D212). It is started as the
 * leader of a session of processes of its own, with the mark, a variable of
 * its environment that every process started from it inherits. The framework
 * reads the live processes from the process table (`ps`), and knows a process
 * to be of the session in three ways: by its parent, by its group and by its
 * mark. The agent's own process, by its number and when it started, is the
 * first it knows, and what it has once known it knows until that process has
 * ended (D222). When the agent's own process ends, at its deadline, and when
 * the run receives the interrupt, the terminate or the hang-up signal, every
 * process it knows to be of the session is ended (D213). Then it looks for a
 * process it cannot place: one that started after the session did, has no
 * parent left alive, is of the session in none of the three ways, shows no
 * environment, and has its current folder in the folder the session works in.
 * It ends no such process, and names it (D223). The outcome comes with how
 * many were ended and, where the session is not over, why, naming each
 * process. What it printed is read until its own process ends and every
 * process of it is ended, and then for at most a moment more, so a process
 * that keeps its output open does not hold it. A signal received from the
 * start of a session until the caller has recorded its end is kept, and the
 * caller asks for it (`settled`); none is dropped (D214).
 *
 * @carries C12
 * @uses H1
 */
import * as Effect from "effect/Effect"
import * as ChildProcess from "effect/process/ChildProcess"
import * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import * as Stream from "effect/Stream"
import { covers } from "./place_containment.js"

/** A variable of the environment that marks every process of one session: its name and its value (D212). */
export interface Mark {
  readonly name: string
  readonly value: string
}

export interface Child {
  readonly command: string
  readonly args: readonly string[]
  /** The folder the child starts in. */
  readonly cwd: string
  /** How long it may run, in milliseconds. */
  readonly deadline: number
  /** Text, or bytes, given on its standard input. Without it the child's input is closed. */
  readonly input?: string | Uint8Array
  /** Added to the environment it inherits; a name set to undefined is taken out. */
  readonly env?: Readonly<Record<string, string | undefined>>
  /** Its output and its errors as one text, in the order printed. Otherwise the output alone, and the errors apart. */
  readonly merged?: boolean
  /** The mark of a session: the child is a session's agent, and every process of the session is ended with it. */
  readonly mark?: Mark
}

/** What the child printed before it was ended, where it printed anything: its output, then its errors where they are apart. */
export interface Printed {
  readonly printed?: string
}

/** How many processes of a session were ended; and, where the session is not over, why: each process still alive after every round, each the framework cannot place, or what it cannot tell (D213, D223); with, where the table of processes could not be read, how, and then `unended` names no process (D249). */
export interface Ended {
  readonly ended: number
  readonly unended?: string
  readonly table?: Unread
}

/** For a session's agent, how many processes of the session were ended and, where it is not over, why. */
type EndedOf = Partial<Ended>

export type Outcome =
  | ({ readonly outcome: "returned"; readonly code: number; readonly output: string; readonly errors: string } & EndedOf)
  | { readonly outcome: "could not start"; readonly why: string }
  | ({ readonly outcome: "stopped without returning"; readonly why: string } & Printed & EndedOf)
  | ({ readonly outcome: "ran over" } & Printed & EndedOf)
  | ({ readonly outcome: "cut off"; readonly signal: Signal; readonly why: string } & Printed & EndedOf)

type Spawner = ChildProcessSpawner.ChildProcessSpawner

/** The signals on which a run is cut off (REQ-FLOW-003), with the exit code each gives. */
export const SIGNALS = { SIGINT: 130, SIGTERM: 143, SIGHUP: 129 } as const
export type Signal = keyof typeof SIGNALS

const encoder = new TextEncoder()

/** How long a process of a session has after the terminate signal before it is killed; how long output is read after the end. */
const GRACE = 2000
/** The most times the process table is read while a session's processes are ended: each time ends those it knows. */
const ROUNDS = 20
/** The most readings of the process table, one after another, until one tells of every process whether it holds the mark (D212). */
const READINGS = 20
/** In one reading, the most times the processes `ps` could not read are read again, alone (D212). */
const AGAIN = 5

/** One live process, as one reading of the process table gives it (D212). */
export interface Process {
  readonly pid: number
  readonly ppid: number
  /** Its process group (D222). */
  readonly pgid: number
  /** When it started, as `ps` gives it in the C locale; with the number, it tells one process from another given the same number. */
  readonly start: string
  /** What the table gives after when it started: in the reading with the environment, its command and then its environment. */
  readonly line: string
  /** Its command, as the reading without the environment gives it, where that reading has it with the same start; its line otherwise. */
  readonly command: string
  /** Its environment, entries `name=value`, each after a space: what the line with it holds after the command the line without it gives, where the two agree; not known where they do not, or where `ps` could read neither. */
  readonly env?: string
}

/** How the table of processes could not be read: `ps` was not found, or it could not read the table (D249). */
export type Unread = "not found" | "unread"

/**
 * Where the table of processes cannot be read, the one sentence every refusal
 * and every cut-off for it gives: that `ps` was not found or could not read
 * the table, and what to install. It names no process (REQ-FLOW-001, D249).
 */
const psSentence = (table: Unread, how?: string): string =>
  table === "not found"
    ? "`ps` was not found, so the framework cannot read the table of processes: install it; on Debian and Ubuntu it comes with the package procps."
    : `\`ps\` could not read the table of processes${how === undefined ? "" : ` (${how})`}, so the framework cannot tell which processes are a session's: install a \`ps\` that reads it; on Debian and Ubuntu it comes with the package procps.`

/** The framework cannot tell which processes are of a session: the process table, or the current folders of processes, could not be read; and why, with how the table could not be read where that is why. */
export class CannotTell {
  readonly _tag = "CannotTell"
  constructor(readonly why: string, readonly table?: Unread) {}
}

const LINE = /^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+\s+\S+\s+\S+\s+\S+\s+\S+)\s?(.*)$/
/** What `ps` gives where it could read neither a process's command nor its environment, as while the process starts a new program: its short name alone, in brackets, after the spaces of its column. */
const UNREAD = /^\s*\([^=]*\)$/

/** The table as `ps` gives it in the C locale; with each process's environment after its command, where asked; of the processes of these numbers alone, where given, of which none may be left. */
const table = (environment: boolean, only?: readonly number[]): Effect.Effect<readonly Process[], CannotTell, Spawner> =>
  Effect.gen(function*() {
    const flag = !environment ? [] : process.platform === "darwin" ? ["-E"] : ["e"]
    const which = only === undefined ? ["-A"] : ["-p", only.join(",")]
    const o = yield* supervise({ command: "ps", args: [...which, "-ww", ...flag, "-o", "pid=,ppid=,pgid=,stat=,lstart=,command="], cwd: "/", deadline: 30_000, env: { LC_ALL: "C" } })
    // Of the numbers given, none is left: `ps` exits with 1 and prints nothing.
    if (only !== undefined && o.outcome === "returned" && o.code === 1 && o.output.trim() === "") return []
    if (o.outcome !== "returned" || o.code !== 0) {
      // `ps` that cannot be started for want of the program is not found; any other failure is a table it could not read (D249).
      const missing = o.outcome === "could not start" && /NotFound|ENOENT/.test(o.why)
      const how = o.outcome === "returned" ? `it exited with ${o.code}` : o.outcome === "could not start" ? "it could not be started" : o.outcome === "ran over" ? "it ran over" : "it stopped without returning"
      return yield* Effect.fail(missing ? new CannotTell(psSentence("not found"), "not found") : new CannotTell(psSentence("unread", how), "unread"))
    }
    return o.output.split("\n").flatMap((l) => {
      const m = LINE.exec(l)
      // A zombie, or a process trying to exit (`E`), is no live process.
      if (m === null || /^Z|E/.test(m[4] ?? "")) return []
      const line = m[6] ?? ""
      return [{ pid: Number(m[1]), ppid: Number(m[2]), pgid: Number(m[3]), start: (m[5] ?? "").split(/\s+/).join(" "), line, command: line }]
    })
  })

/**
 * One reading of the live processes: the table is read without the environment
 * and then with it, so a process's environment is what its second line holds
 * after the command its first line gives (D212). Where the two do not agree, as
 * for a process that started a new program or began between the two, or where
 * `ps` could read neither, its environment is not known, and the process is
 * given with its second line alone; it is not passed over. A zombie, or a
 * process trying to exit, is no live process.
 */
export const processes = (): Effect.Effect<readonly Process[], CannotTell, Spawner> =>
  Effect.gen(function*() {
    const commands = new Map((yield* table(false)).map((p) => [p.pid, p]))
    let all = (yield* table(true)).map((p): Process => {
      const plain = commands.get(p.pid)
      const same = plain !== undefined && plain.start === p.start
      const agree = same && !UNREAD.test(p.line) && (p.line === plain.line || p.line.startsWith(`${plain.line} `))
      const command = same ? plain.line : p.line
      return agree ? { ...p, command, env: p.line.slice(plain.line.length) } : { ...p, command }
    })
    // A process `ps` could not read is read again alone, up to `AGAIN` times: a line read then holds all its environment; one that has ended is left out (D212).
    for (let n = 0; n < AGAIN; n++) {
      const unread = all.filter((p) => p.env === undefined && UNREAD.test(p.line))
      if (unread.length === 0) break
      const now = new Map((yield* table(true, unread.map((p) => p.pid))).map((p) => [p.pid, p]))
      all = all.flatMap((p) => {
        if (p.env !== undefined || !UNREAD.test(p.line)) return [p]
        const q = now.get(p.pid)
        return q === undefined || q.start !== p.start ? [] : [{ ...p, ppid: q.ppid, pgid: q.pgid, line: q.line }]
      })
    }
    return all
  })

/** Whether the table of processes can be read: none where it can, and otherwise why, in the one sentence `psSentence` gives (REQ-FLOW-003 step 1, D249). */
export const tableRead = (): Effect.Effect<CannotTell | undefined, never, Spawner> =>
  Effect.match(table(false), { onFailure: (e) => e, onSuccess: () => undefined })

/** When the process of this number started, where one runs; undefined where none does. */
export const startOf = (pid: number): Effect.Effect<string | undefined, CannotTell, Spawner> =>
  Effect.map(table(false), (all) => all.find((p) => p.pid === pid)?.start)

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
const two = (n: number): string => String(n).padStart(2, "0")

/** A time of the process table, as `ps` gives it in the C locale (`Mon Nov 23 20:10:11 2026`), as a key that sorts by time, to the second, in local time; undefined where it is not of that form (D216). */
export const startKey = (start: string): string | undefined => {
  const [, month = "", day = "", time = "", year = ""] = start.split(" ")
  const m = MONTHS.indexOf(month)
  return m < 0 || !/^[0-9]+$/.test(day) || !/^[0-9]{2}:[0-9]{2}:[0-9]{2}$/.test(time) || !/^[0-9]{4}$/.test(year) ? undefined : `${year}${two(m + 1)}${two(Number(day))}${time.replaceAll(":", "")}`
}

/** What the framework looks for of one session (D222). */
export interface Sought {
  readonly mark: Mark
  /** The folder the session works in, where the framework looks for a process it cannot place. */
  readonly folder?: string
  /** When the session, or the run cut off on its ticket, started, as a key (`startKey`): a process it cannot place started no earlier. Without it, none is looked for. */
  readonly since?: string
  /** The agent's own process, where the framework started it: its number and, where it was read, when it started. */
  readonly agent?: { readonly pid: number; readonly start?: string }
}

/** What the framework knows of one session's processes, as it reads them (D222): each process by its number, with when it started, and the groups they are in or led. It adds to them, and forgets a process only by its number being given to another. */
interface Known {
  readonly processes: Map<number, string>
  readonly groups: Set<number>
}

/** What it knows from the start: the agent's own process, and the group it leads, since it is started as the leader of a session of processes of its own. */
const knownFrom = (sought: Sought): Known => ({
  processes: new Map(sought.agent?.start === undefined ? [] : [[sought.agent.pid, sought.agent.start]]),
  groups: new Set(sought.agent === undefined ? [] : [sought.agent.pid])
})

/** Of one reading, the processes of the session, and those whose environment it does not show while it may hold the mark. */
interface Placed {
  readonly all: readonly Process[]
  readonly of: ReadonlyMap<number, Process>
  readonly untold: readonly Process[]
  /** This process and those it was started from, by number: never of a session. */
  readonly ours: ReadonlySet<number>
}

/**
 * Of one reading, the processes the framework knows to be of the session, in
 * three ways, until no more is found (D222): by what it knows already, the
 * same number with the same start; by its parent, which is of the session; by
 * its group, a group a process of the session is in or led, while a process is
 * in it; and by its mark, the entry `name=value` whole in the environment the
 * table shows, after a space and up to a space or the end. The same text in a
 * command, or a value that only begins with the mark's, is no mark (D212).
 * Each it finds it knows from then on. Never this process or one it was
 * started from, and never its group or theirs: a session's agent leads a
 * session of processes of its own. And those it cannot tell by the mark
 * (`untold`), for the table to be read again: a process of none of the three
 * ways whose environment is not known, where its line holds the entry; or
 * where `ps` could not read it, read again, unless its parent is in the
 * reading with an environment the table shows, without the entry.
 */
const place = (all: readonly Process[], known: Known, mark: Mark, self: number = process.pid): Placed => {
  const entry = ` ${mark.name}=${mark.value} `
  const holds = (text: string): boolean => ` ${text} `.includes(entry)
  const byNumber = new Map(all.map((p) => [p.pid, p]))
  const ours = new Set<number>([self])
  const ourGroups = new Set<number>()
  for (let p = byNumber.get(self); p !== undefined && p.pid > 1; p = byNumber.get(p.ppid)) {
    ours.add(p.pid)
    ourGroups.add(p.pgid)
  }
  const others = all.filter((p) => !ours.has(p.pid))
  // A group is known while a process is in it: once none is, its number may be given again.
  const live = new Set(all.map((p) => p.pgid))
  for (const g of [...known.groups]) if (!live.has(g) || ourGroups.has(g)) known.groups.delete(g)
  const of = new Map(others.filter((p) => known.processes.get(p.pid) === p.start).map((p) => [p.pid, p]))
  for (let added = true; added;) {
    added = false
    for (const p of of.values()) {
      for (const g of [p.pgid, p.pid]) if (!ourGroups.has(g) && !known.groups.has(g)) known.groups.add(g)
    }
    for (const p of others) {
      if (of.has(p.pid)) continue
      if (of.has(p.ppid) || known.groups.has(p.pgid) || (p.env !== undefined && holds(p.env))) {
        of.set(p.pid, p)
        added = true
      }
    }
  }
  for (const p of of.values()) known.processes.set(p.pid, p.start)
  // The last resort for a process `ps` could not read, again and again: where its parent shows an environment without the entry, it is taken to have none (D212).
  const shown = (pid: number): boolean => (byNumber.get(pid)?.env ?? "").trim() !== ""
  const untold = others.filter((p) => !of.has(p.pid) && p.env === undefined && (holds(p.line) || (UNREAD.test(p.line) && !shown(p.ppid))))
  return { all, of, untold, ours }
}

/**
 * The session's live processes, from the first of up to `READINGS` readings
 * that tells of every process of none of the three ways whether it holds the
 * mark. Where none does, the last reading is taken: a process it still does
 * not tell is not of the session by its mark, and may be one the framework
 * cannot place (D212, D223). A process is named by its command, and `ps`
 * cannot read the command of a process at the moment it starts a new program:
 * the command is then the one the last reading that could read it gave (D225).
 */
const reading = (sought: Sought, known: Known): Effect.Effect<Placed, CannotTell, Spawner> =>
  Effect.gen(function*() {
    // The command each reading gave of a process, by its number and start, where `ps` could read it (D225).
    const commands = new Map<string, string>()
    const read = Effect.map(processes(), (all) => {
      for (const p of all) if (!UNREAD.test(p.command)) commands.set(`${p.pid} ${p.start}`, p.command)
      return all
    })
    let last = place(yield* read, known, sought.mark)
    for (let n = 1; n < READINGS && last.untold.length > 0; n++) last = place(yield* read, known, sought.mark)
    // A process `ps` could not read in the reading taken is named by the command the last reading that could read it gave.
    const told = (p: Process): Process => (UNREAD.test(p.command) ? { ...p, command: commands.get(`${p.pid} ${p.start}`) ?? p.command } : p)
    return { ...last, all: last.all.map(told), of: new Map([...last.of].map(([pid, p]): [number, Process] => [pid, told(p)])) }
  })

/** The real path of a folder, as `pwd -P` in it gives it; the folder as given, where it cannot be read. */
const realPath = (folder: string): Effect.Effect<string, never, Spawner> =>
  Effect.map(supervise({ command: "pwd", args: ["-P"], cwd: folder, deadline: 30_000 }), (o) => (o.outcome === "returned" && o.code === 0 && o.output.trim() !== "" ? o.output.trim() : folder))

/**
 * The current folder of each process of these numbers, where it can be read
 * (D223): on Linux, what `/proc` gives; elsewhere, what `lsof` gives. A
 * process whose folder is not read is read again, up to `AGAIN` times in all,
 * as one that starts a new program at that moment may not be read; one whose
 * folder cannot be read, as one of another user's, or one that has ended, is
 * left out. Where `lsof` cannot be started, the framework cannot tell.
 */
const foldersOf = (pids: readonly number[]): Effect.Effect<ReadonlyMap<number, string>, CannotTell, Spawner> =>
  Effect.gen(function*() {
    const out = new Map<number, string>()
    for (let n = 0; n < AGAIN; n++) {
      const left = pids.filter((pid) => !out.has(pid))
      if (left.length === 0) break
      if (process.platform === "linux") {
        for (const pid of left) {
          const o = yield* supervise({ command: "readlink", args: [`/proc/${pid}/cwd`], cwd: "/", deadline: 30_000 })
          if (o.outcome === "returned" && o.code === 0 && o.output.trim() !== "") out.set(pid, o.output.trim())
        }
        continue
      }
      // `lsof` exits with 1 where it could not read some of the processes, and gives those it could.
      const o = yield* supervise({ command: "/usr/sbin/lsof", args: ["-a", "-d", "cwd", "-p", left.join(","), "-Fpn"], cwd: "/", deadline: 30_000, env: { LC_ALL: "C" } })
      if (o.outcome !== "returned") return yield* Effect.fail(new CannotTell(`the current folders of processes could not be read: lsof ${o.outcome === "could not start" ? `could not start: ${o.why}` : o.outcome}`))
      let at: number | undefined
      for (const l of o.output.split("\n")) {
        if (l.startsWith("p")) at = Number(l.slice(1))
        else if (l.startsWith("n") && at !== undefined) out.set(at, l.slice(1))
      }
    }
    return out
  })

/**
 * Of one reading, the processes the framework cannot place (REQ-FLOW-001,
 * D223): none of the session in any of the three ways; started no earlier
 * than the session or the cut-off run, to the second; with no parent left
 * alive, its parent the first process or not in the reading, or one that
 * started after it, given the number again, or, on Linux, where an orphan may
 * be given to a reaper that is not the first process, one not of the session
 * that started before the session did; showing no environment, an empty
 * one or one not known; and with its current folder in the folder the session
 * works in, by its real path. Its folder is read only of those that pass the
 * other tests. None where the framework is given no start or no folder.
 */
const unplaced = (placed: Placed, sought: Sought): Effect.Effect<readonly Process[], CannotTell, Spawner> =>
  Effect.gen(function*() {
    const { since, folder } = sought
    if (since === undefined || folder === undefined) return []
    const byNumber = new Map(placed.all.map((p) => [p.pid, p]))
    const keyOf = (p: Process): string => startKey(p.start) ?? ""
    const orphaned = (p: Process): boolean => {
      const parent = byNumber.get(p.ppid)
      return p.ppid <= 1 || parent === undefined || keyOf(parent) > keyOf(p) || (process.platform === "linux" && keyOf(parent) < since)
    }
    const candidates = placed.all.filter((p) =>
      p.pid > 1 && !placed.ours.has(p.pid) && !placed.of.has(p.pid) && (p.env === undefined || p.env.trim() === "") && keyOf(p) >= since && orphaned(p)
    )
    if (candidates.length === 0) return []
    const real = yield* realPath(folder)
    const folders = yield* foldersOf(candidates.map((p) => p.pid))
    return candidates.filter((p) => {
      const cwd = folders.get(p.pid)
      return cwd !== undefined && (covers(real, cwd) || covers(folder, cwd))
    })
  })

/** A process named to the user: by its number, when it started and its command (REQ-FLOW-001). */
export const named = (p: Process): string => `the process ${p.pid}, started ${p.start}, running ${p.command.trim()}`

const listed = (ps: readonly Process[]): string => ps.map(named).join("; and ")

/** The words that a session is not over: each process still alive after every round, and each the framework cannot place, named (D213, D223). */
const notOver = (alive: readonly Process[], unknown: readonly Process[], folder: string | undefined): string =>
  [
    ...(alive.length === 0 ? [] : [`${listed(alive)}: ${alive.length === 1 ? "it is" : "these are"} of the session and still alive after ${ROUNDS} rounds of ending ${alive.length === 1 ? "it" : "them"}`]),
    ...(unknown.length === 0 ? [] : [`the framework cannot place ${listed(unknown)}: ${unknown.length === 1 ? "it" : "each"} started after the session did, has no parent left alive, is of the session by neither its parent, its group nor its mark, shows no environment, and works in ${folder ?? "the session's folder"}; it is not ended`])
  ].join("; and ")

/** What the framework finds of a session, ending nothing (REQ-FLOW-003 step 1, REQ-FLOW-006): the processes it knows to be of it that are alive, and those it cannot place (D222, D223). */
export interface Found {
  readonly alive: readonly Process[]
  readonly unplaced: readonly Process[]
}

/** The live processes the framework knows to be of the session, by its mark and from there by their parents and groups, and those it cannot place; or why it cannot tell (D222, D223). */
export const marked = (sought: Sought): Effect.Effect<Found, CannotTell, Spawner> =>
  Effect.gen(function*() {
    const placed = yield* reading(sought, knownFrom(sought))
    const unknown = yield* unplaced(placed, sought)
    return { alive: [...placed.of.values()], unplaced: unknown }
  })

const signal = (pid: number, s: "SIGTERM" | "SIGKILL"): void => {
  try {
    process.kill(pid, s)
  } catch {
    // It ended already.
  }
}

/**
 * Ends every live process the framework knows to be of the session: the
 * terminate signal, then, after a grace, the kill signal, and the table read
 * again until none is left (D213). A process it has once known it ends until
 * it has ended, whether or not a later reading finds it in any of the three
 * ways, and counts it only when it is gone: no reading has it, by its number
 * and start (D222). Then it looks for a process it cannot place, which it
 * does not end (D223). It never fails: it gives how many it ended and, where
 * a process it knows is still alive after every round, it finds one it cannot
 * place, or it cannot tell, why, naming each; so the count of those it did end
 * is never lost, nor one counted that may be alive.
 */
export const endMarked = (sought: Sought): Effect.Effect<Ended, never, Spawner> =>
  Effect.gen(function*() {
    const known = knownFrom(sought)
    const sent = new Map<number, string>()
    const gone = new Set<number>()
    const seen = (all: readonly Process[]): void => {
      const live = new Map(all.map((p) => [p.pid, p.start]))
      for (const [pid, start] of sent) if (live.get(pid) !== start) gone.add(pid)
    }
    const read = Effect.match(reading(sought, known), { onFailure: (e) => ({ cannot: e }) as const, onSuccess: (placed) => ({ placed }) as const })
    // Every process it knows, alive in the reading by its number and start.
    const knownIn = (placed: Placed): readonly Process[] => placed.all.filter((p) => !placed.ours.has(p.pid) && known.processes.get(p.pid) === p.start)
    // Where the table cannot be read, the words are the one sentence, and name no process (D249).
    const cannot = (e: CannotTell): Ended => ({ ended: gone.size, unended: e.why, ...(e.table === undefined ? {} : { table: e.table }) })
    for (let round = 0; round < ROUNDS; round++) {
      const now = yield* read
      if ("cannot" in now) return cannot(now.cannot)
      seen(now.placed.all)
      const targets = knownIn(now.placed)
      if (targets.length === 0) break
      for (const p of targets) {
        sent.set(p.pid, p.start)
        signal(p.pid, "SIGTERM")
      }
      let left = targets
      for (let waited = 0; left.length > 0 && waited < GRACE; waited += 50) {
        yield* Effect.sleep(50)
        const again = yield* Effect.match(table(false, left.map((p) => p.pid)), { onFailure: (e) => ({ cannot: e }) as const, onSuccess: (all) => ({ all }) as const })
        if ("cannot" in again) return cannot(again.cannot)
        const live = new Map(again.all.map((p) => [p.pid, p.start]))
        left = left.filter((p) => live.get(p.pid) === p.start)
      }
      for (const p of left) signal(p.pid, "SIGKILL")
    }
    const last = yield* read
    if ("cannot" in last) return cannot(last.cannot)
    seen(last.placed.all)
    const still = knownIn(last.placed)
    const unknown = yield* Effect.match(unplaced(last.placed, sought), { onFailure: (e) => ({ cannot: e }) as const, onSuccess: (ps) => ({ ps }) as const })
    if ("cannot" in unknown) {
      return unknown.cannot.table !== undefined ? cannot(unknown.cannot) : cannot(new CannotTell([...(still.length === 0 ? [] : [notOver(still, [], sought.folder)]), unknown.cannot.why].join("; and ")))
    }
    return still.length === 0 && unknown.ps.length === 0 ? { ended: gone.size } : { ended: gone.size, unended: notOver(still, unknown.ps, sought.folder) }
  })

/** A marked child at work, which a signal cuts off. */
interface AtWork {
  cut?: Signal
}

/** The session at work, from just before its start until the caller has recorded its end (D214). */
let atWork: AtWork | undefined
let bound = false
/** The first signal the run received. */
let cutBy: Signal | undefined

/**
 * Binds the run's signals (REQ-FLOW-003), once in a process: on the
 * interrupt, the terminate or the hang-up signal, the session at work, from
 * just before its start until the caller has recorded its end, is cut off:
 * its supervision ends every process it knows to be of it, and the caller, asking
 * `settled`, goes no further. Where none is at work, the process ends at once
 * with the first signal's exit code, as a killed run does, and goes no
 * further. No signal is dropped (D214).
 */
export const bindSignals = (): void => {
  if (bound) return
  bound = true
  for (const s of Object.keys(SIGNALS) as Signal[]) {
    process.on(s, () => {
      cutBy ??= s
      if (atWork === undefined) process.exit(SIGNALS[cutBy])
      atWork.cut ??= s
    })
  }
}

/** The session's end is recorded: the signal the run received from its start, where it received one, after which the run goes no further (D214). */
export const settled = (): Signal | undefined => {
  atWork = undefined
  return cutBy
}

/** The prefix of the name of every mark (D212). */
export const MARK = "STDO_BUILDER_SESSION_"

/** The workspaces of the sessions this process was started from, by the marks it inherited, each value read back from its written form (D212, D217). */
export const inherited = (): readonly string[] =>
  Object.entries(process.env).flatMap(([name, value]) => {
    if (!name.startsWith(MARK) || value === undefined || value === "") return []
    try {
      return [decodeURIComponent(value)]
    } catch {
      return [value]
    }
  })

/**
 * Ends this process: the run goes no further (REQ-FLOW-003). With the exit
 * code of the signal it was cut off by, or 1 where its session is not over;
 * it first says why, where there are words (D214, D221).
 */
export const goNoFurther = (s: Signal | undefined, words?: string): Effect.Effect<never> =>
  Effect.sync(() => {
    if (words !== undefined) process.stderr.write(`${words}\n`)
    return process.exit(s === undefined ? 1 : SIGNALS[s])
  })

/**
 * Starts the child and waits for its one outcome. It never fails: every way it
 * can end is an outcome. What the child prints is read as it comes, into texts
 * kept outside the part the deadline cuts off, so a child that stops without
 * returning, or is ended at its deadline, still gives what it printed until then.
 */
export const supervise = (child: Child): Effect.Effect<Outcome, never, Spawner> =>
  Effect.gen(function*() {
    const read = { output: "", errors: "" }
    const printed = (): Printed => {
      const text = `${read.output}${read.errors}`
      return text === "" ? {} : { printed: text }
    }
    const spawner = yield* ChildProcessSpawner.ChildProcessSpawner
    const mark = child.mark
    const command = ChildProcess.make(child.command, [...child.args], {
      cwd: child.cwd,
      env: mark === undefined ? { ...child.env } : { ...child.env, [mark.name]: mark.value },
      extendEnv: true,
      // A session's agent leads a session of processes of its own, so the group it leads holds no process that is not of the session (D222).
      ...(mark === undefined ? {} : { detached: true }),
      stdin: child.input === undefined ? "ignore" : { stream: Stream.make(typeof child.input === "string" ? encoder.encode(child.input) : child.input) },
      forceKillAfter: GRACE
    })
    // A marked child is at work from before it is started, so a signal in the moment of its start is kept (D214).
    const work: AtWork = {}
    if (mark !== undefined) atWork = work
    // Once the child's own process has ended and its session's processes are ended: and how long what it printed is read after that, none for an unmarked child cut at its deadline.
    const state = { over: false, grace: GRACE }
    type Ending = { readonly exit: number } | { readonly stopped: string } | { readonly over: true } | { readonly cut: Signal }
    const body = Effect.gen(function*() {
      // A program that cannot be found can reach here as a defect of the platform rather than a failure.
      const handle = yield* spawner.spawn(command).pipe(
        Effect.mapError((error): Outcome => ({ outcome: "could not start", why: error.message })),
        Effect.catchDefect((defect) => Effect.fail<Outcome>({ outcome: "could not start", why: String(defect) }))
      )
      // The agent's own process is the first the framework knows of the session, by its number and when it started, read at once; the session began then, or, where the agent has ended already, no later than this run did (D222, D223).
      const pid = Number(handle.pid)
      const starts = mark === undefined ? new Map<number, string>() : new Map((yield* Effect.orElseSucceed(table(false, [pid, process.pid]), (): readonly Process[] => [])).map((p) => [p.pid, p.start]))
      const began = starts.get(pid)
      const since = startKey(began ?? starts.get(process.pid) ?? "")
      // A session's processes are ended, however its agent's own process ended; the outcome carries how many, and why the session is not over, where it is not.
      const endAll = (): Effect.Effect<EndedOf, never, Spawner> =>
        mark === undefined ? Effect.succeed({}) : endMarked({ mark, folder: child.cwd, ...(since === undefined ? {} : { since }), agent: { pid, ...(began === undefined ? {} : { start: began }) } })
      const into = (s: typeof handle.all, kept: "output" | "errors") =>
        Stream.runForEach(Stream.decodeText(s), (text) => Effect.sync(() => void (read[kept] += text))).pipe(Effect.ignore)
      const reading = Effect.all(child.merged === true ? [into(handle.all, "output")] : [into(handle.stdout, "output"), into(handle.stderr, "errors")], { concurrency: "unbounded", discard: true })
      // Once the child's own process has ended and its session's processes are ended, what it printed is read for a moment more at most.
      const drained = Effect.raceFirst(reading, Effect.gen(function*() {
        while (!state.over) yield* Effect.sleep(20)
        yield* Effect.sleep(state.grace)
      }))
      const own: Effect.Effect<Ending> = handle.exitCode.pipe(
        Effect.map((n): Ending => ({ exit: Number(n) })),
        Effect.catch((error) => Effect.succeed<Ending>({ stopped: error.message }))
      )
      const deadline = Effect.as(Effect.sleep(child.deadline), { over: true } as Ending)
      const cut = Effect.gen(function*() {
        while (work.cut === undefined) yield* Effect.sleep(50)
        return { cut: work.cut } as Ending
      })
      const ending = mark === undefined ? Effect.raceFirst(own, deadline) : Effect.raceFirst(own, Effect.raceFirst(deadline, cut))
      const [, [first, ended]] = yield* Effect.all([
        drained,
        Effect.gen(function*() {
          const how = yield* ending
          const ended = yield* endAll()
          if (mark === undefined && !("exit" in how)) state.grace = 0
          state.over = true
          return [how, ended] as const
        })
      ], { concurrency: "unbounded" })
      // A signal received at any moment of the session cuts it off, whatever its own process did (D214).
      const how: Ending = work.cut !== undefined && !("cut" in first) ? { cut: work.cut } : first
      if ("cut" in how) return { outcome: "cut off", signal: how.cut, why: `the run received the ${how.cut} signal`, ...printed(), ...ended } satisfies Outcome as Outcome
      if ("exit" in how) return { outcome: "returned", code: how.exit, output: read.output, errors: read.errors, ...ended } satisfies Outcome as Outcome
      if ("stopped" in how) return { outcome: "stopped without returning", why: how.stopped, ...printed(), ...ended } satisfies Outcome as Outcome
      return { outcome: "ran over", ...printed(), ...ended } satisfies Outcome as Outcome
    })
    return yield* body.pipe(
      Effect.scoped,
      Effect.catch((outcome: Outcome) => Effect.succeed(outcome))
    )
  })
