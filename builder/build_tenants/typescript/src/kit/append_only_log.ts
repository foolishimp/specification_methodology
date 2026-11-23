/**
 * Append-only log with a fold: entries are only added, each whole or not at
 * all, and a reader makes one pass over them keeping a running result.
 *
 * An entry is one line. It is added by one write at the end of the file, so
 * adding costs the same however long the log is. A last line with no end, left
 * by a writer that was stopped, is not a whole entry and is passed over.
 *
 * @carries C10
 */
import * as Effect from "effect/Effect"
import * as FileSystem from "effect/FileSystem"

/** The log could not be added to or read, and why. */
export class LogRefused {
  readonly _tag = "LogRefused"
  constructor(readonly file: string, readonly why: string) {}
}

const folderOf = (file: string): string => file.slice(0, Math.max(0, file.lastIndexOf("/")))

/** Adds one entry, which must not hold a line break. The log is started where there is none. */
export const append = (file: string, entry: string): Effect.Effect<void, LogRefused, FileSystem.FileSystem> =>
  Effect.gen(function*() {
    if (entry.includes("\n")) return yield* Effect.fail(new LogRefused(file, "an entry is one line"))
    const fs = yield* FileSystem.FileSystem
    yield* fs.makeDirectory(folderOf(file), { recursive: true })
    yield* fs.writeFileString(file, `${entry}\n`, { flag: "a" })
  }).pipe(Effect.mapError((e) => (e instanceof LogRefused ? e : new LogRefused(file, e.message))))

/** Whether there is a log at `file`. */
export const exists = (file: string): Effect.Effect<boolean, never, FileSystem.FileSystem> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    return yield* fs.exists(file).pipe(Effect.orElseSucceed(() => false))
  })

/** One pass over the whole entries, in the order added: `step` is given the running result and each entry. Undefined when there is no log. */
/** One step of a fold: the running result and the next entry give the next result. */
export type Step<R, E = string> = (running: R, entry: E) => R

export const fold = <R>(file: string, start: R, step: Step<R>): Effect.Effect<R | undefined, LogRefused, FileSystem.FileSystem> =>
  Effect.gen(function*() {
    const fs = yield* FileSystem.FileSystem
    if (!(yield* exists(file))) return undefined
    const text = yield* fs.readFileString(file).pipe(Effect.mapError((e) => new LogRefused(file, e.message)))
    const whole = text.slice(0, text.lastIndexOf("\n") + 1)
    let running = start
    for (const entry of whole.split("\n")) if (entry !== "") running = step(running, entry)
    return running
  })
