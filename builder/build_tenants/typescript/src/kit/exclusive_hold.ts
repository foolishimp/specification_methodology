/**
 * Exclusive hold bound to a process: at most one holder of a name at a time,
 * and a hold whose holder's process has ended counts as released, so nothing
 * has to clean up after a killed holder.
 *
 * A hold is a run of numbered files beside the name: `<name>` itself is
 * number 0, then `<name>.1`, `<name>.2` and on. The file with the greatest
 * number says who holds it: the number of a process, or `free`. Each file is
 * made only where there is none, and whole (C15), so no reader sees one half
 * made. A taker reads the greatest
 * file; where its process no longer runs, or it is free, the taker makes the
 * next number. Two takers that read the same greatest file both try to make
 * the same next number, and only one can. A taker whose view was old makes a
 * number below the greatest; it reads again after making it, sees a greater
 * one and lets go. Release makes the next number `free` before it removes
 * the files below, so the greatest number never goes back; `keeping` makes it
 * say what the file it took over said, so a hold left by a process that has
 * ended is left so (D232). This reading of
 * C11 is recorded in DECISIONS.md (D32, D50): the operating system does not
 * remove the file, it ends the process the file names. A file names the
 * holder's number and when it started, read from the process table (C12), so
 * another process given the same number holds nothing; a file of a release
 * before that, which names the number alone, is held only by a process that
 * started no later than the file was written (D216).
 *
 * @carries C11
 * @uses C12 C15
 */
import * as Effect from "effect/Effect"
import * as FileSystem from "effect/FileSystem"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { createIfAbsent } from "./create_if_absent.js"
import { startKey, startOf } from "./supervised_child.js"

type Fs = FileSystem.FileSystem | ChildProcessSpawner.ChildProcessSpawner

/** The process with this number runs. */
function runs(pid: number): boolean {
  if (!Number.isInteger(pid) || pid <= 0) return false
  try {
    process.kill(pid, 0)
    return true
  } catch (error) {
    return (error as { code?: string }).code === "EPERM"
  }
}

const folderOf = (file: string): string => file.slice(0, Math.max(0, file.lastIndexOf("/")))
const nameOf = (file: string): string => file.slice(file.lastIndexOf("/") + 1)
const numbered = (file: string, n: number): string => (n === 0 ? file : `${file}.${n}`)

/** The numbers of the hold's files there are now, greatest last. */
const numbers = (file: string): Effect.Effect<readonly number[], never, Fs> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    const name = nameOf(file)
    const names = yield* fs.readDirectory(folderOf(file)).pipe(Effect.orElseSucceed((): readonly string[] => []))
    return names
      .flatMap((n) => (n === name ? [0] : n.startsWith(`${name}.`) && /^[0-9]+$/.test(n.slice(name.length + 1)) ? [Number(n.slice(name.length + 1))] : []))
      .sort((a, b) => a - b)
  })

/** The process that holds a hold: its number and, where it was recorded, when it started (D216). */
export interface Holder {
  readonly pid: number
  readonly start?: string
}

const two = (n: number): string => String(n).padStart(2, "0")

/** When the file was last written, as a key of the same form as C12's `startKey`; undefined where it cannot be read. */
const keyOfWritten = (file: string): Effect.Effect<string | undefined, never, Fs> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    const info = yield* fs.stat(file).pipe(Effect.orElseSucceed(() => undefined))
    const at = info?.mtime
    if (at === undefined || at._tag !== "Some") return undefined
    const t = at.value
    return `${t.getFullYear()}${two(t.getMonth() + 1)}${two(t.getDate())}${two(t.getHours())}${two(t.getMinutes())}${two(t.getSeconds())}`
  })

/**
 * The process the file of number `n` names, where it runs. A file names the
 * process's number and when it started; a live process of that number that
 * started at another time is another process, given the number again, and
 * holds nothing. A file that names a number alone, as a release before D216
 * wrote it, is held by a live process of that number only where it started no
 * later than the file was written. Where the process table cannot be read, or
 * the file says `unknown`, the live process is taken to hold it, since the
 * framework cannot tell (D216).
 */
const holderAt = (file: string, n: number): Effect.Effect<Holder | undefined, never, Fs> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    const text = yield* fs.readFileString(numbered(file, n)).pipe(Effect.orElseSucceed(() => ""))
    const [first = "", ...rest] = text.trim().split(" ")
    const pid = Number(first)
    const start = rest.join(" ")
    if (!runs(pid)) return undefined
    if (start === "unknown") return { pid }
    const read = yield* startOf(pid).pipe(Effect.map((now) => ({ now })), Effect.orElseSucceed(() => undefined))
    if (read === undefined) return { pid }
    const now = read.now
    if (now === undefined) return undefined
    if (start !== "") return now === start ? { pid, start } : undefined
    const started = startKey(now)
    const written = yield* keyOfWritten(numbered(file, n))
    return started === undefined || written === undefined || started <= written ? { pid, start: now } : undefined
  })

/** The process that holds `file`, where one does: the one the greatest file names. */
const holderOf = (file: string): Effect.Effect<Holder | undefined, never, Fs> =>
  Effect.gen(function*() {
    const top = (yield* numbers(file)).at(-1)
    return top === undefined ? undefined : yield* holderAt(file, top)
  })

/** Makes the file of number `n`, whole, saying `says` (C15); false where it is there already. */
const make = (file: string, n: number, says: string): Effect.Effect<boolean, never, Fs> =>
  createIfAbsent(numbered(file, n), `${says}\n`).pipe(
    Effect.map((made) => made === "written"),
    Effect.orElseSucceed(() => false)
  )

/** Removes the hold's files numbered below `n`. */
const removeBelow = (file: string, n: number): Effect.Effect<void, never, Fs> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    for (const m of yield* numbers(file)) if (m < n) yield* fs.remove(numbered(file, m), { force: true }).pipe(Effect.ignore)
  })

/** Takes the hold; the number of the file that holds it, with what the greatest file said before it, or undefined where another process holds it. */
const take = (file: string): Effect.Effect<{ readonly mine: number; readonly was: string } | undefined, never, Fs> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    const top = (yield* numbers(file)).at(-1)
    if (top !== undefined && (yield* holderAt(file, top)) !== undefined) return undefined
    // What the greatest file said: free, or a process that has ended, which left the hold (D232).
    const was = top === undefined ? "free" : (yield* fs.readFileString(numbered(file, top)).pipe(Effect.orElseSucceed(() => "free"))).trim()
    const mine = top === undefined ? 1 : top + 1
    // Where the process table cannot be read, the file says the start is unknown, and a live process of its number holds it (D216).
    const start = yield* startOf(process.pid).pipe(Effect.orElseSucceed(() => undefined))
    if (!(yield* make(file, mine, `${process.pid} ${start ?? "unknown"}`))) return undefined
    // A taker whose view was old has made a number below the greatest: it lets go.
    if (((yield* numbers(file)).at(-1) ?? mine) > mine) {
      yield* fs.remove(numbered(file, mine), { force: true }).pipe(Effect.ignore)
      return undefined
    }
    yield* removeBelow(file, mine)
    return { mine, was }
  })

/** Lets go: the next number says `says`, free unless it is said otherwise, then the files below it go. */
const release = (file: string, mine: number, says = "free"): Effect.Effect<void, never, Fs> =>
  Effect.gen(function*() {
    if (yield* make(file, mine + 1, says)) yield* removeBelow(file, mine + 1)
  })

/** Runs `body` while holding `file`, and lets go after, free, or, with `keep`, as it found it. Where another process holds it, that process, where one is found. */
const holdingAs = <A, E, R>(file: string, body: Effect.Effect<A, E, R>, keep: boolean): Effect.Effect<{ readonly done: A } | { readonly heldBy?: Holder }, E, R | Fs> =>
  Effect.gen(function*() {
    const taken = yield* take(file)
    if (taken === undefined) {
      const by = yield* holderOf(file)
      return by === undefined ? {} : { heldBy: by }
    }
    return yield* body.pipe(
      Effect.map((done) => ({ done })),
      Effect.ensuring(release(file, taken.mine, keep && taken.was !== "" ? taken.was : "free"))
    )
  })

/** Runs `body` while holding `file`, and lets go after. Where another process holds it, that process, where one is found. */
export const holding = <A, E, R>(file: string, body: Effect.Effect<A, E, R>): Effect.Effect<{ readonly done: A } | { readonly heldBy?: Holder }, E, R | Fs> =>
  holdingAs(file, body, false)

/**
 * As `holding`, but it lets go as it found the hold: where the greatest file
 * named a process that had ended, the next number names that process again,
 * as that file did, so `left` still finds the run that left the hold, and
 * when it started (D232).
 */
export const keeping = <A, E, R>(file: string, body: Effect.Effect<A, E, R>): Effect.Effect<{ readonly done: A } | { readonly heldBy?: Holder }, E, R | Fs> =>
  holdingAs(file, body, true)

/** The run that left a hold: its process, which has ended, and when it started, as a key of C12's `startKey`, where the file names it; otherwise when the file was written, which is when the run took the hold (D223). */
export interface Left {
  readonly pid: number
  readonly since?: string
}

/** Where the hold was left by a process that has ended, that process: its greatest file names a process, not free, that no longer runs (REQ-FLOW-007, a run cut off). */
export const left = (file: string): Effect.Effect<Left | undefined, never, Fs> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    const top = (yield* numbers(file)).at(-1)
    if (top === undefined) return undefined
    const text = yield* fs.readFileString(numbered(file, top)).pipe(Effect.orElseSucceed(() => "free"))
    if (text.trim() === "free" || (yield* holderAt(file, top)) !== undefined) return undefined
    const [first = "", ...rest] = text.trim().split(" ")
    const since = startKey(rest.join(" ")) ?? (yield* keyOfWritten(numbered(file, top)))
    return { pid: Number(first), ...(since === undefined ? {} : { since }) }
  })

/** Of the files named, those a running process holds, each with that process. */
export const held = (files: readonly string[]): Effect.Effect<readonly { readonly file: string; readonly by: Holder }[], never, Fs> =>
  Effect.gen(function*() {
    const out: { readonly file: string; readonly by: Holder }[] = []
    for (const file of files) {
      const by = yield* holderOf(file)
      if (by !== undefined) out.push({ file, by })
    }
    return out
  })
