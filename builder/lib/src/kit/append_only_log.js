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
import * as Effect from "effect/Effect";
import * as FileSystem from "effect/FileSystem";
/** The log could not be added to or read, and why. */
export class LogRefused {
    file;
    why;
    _tag = "LogRefused";
    constructor(file, why) {
        this.file = file;
        this.why = why;
    }
}
const folderOf = (file) => file.slice(0, Math.max(0, file.lastIndexOf("/")));
/** Adds one entry, which must not hold a line break. The log is started where there is none. */
export const append = (file, entry) => Effect.gen(function* () {
    if (entry.includes("\n"))
        return yield* Effect.fail(new LogRefused(file, "an entry is one line"));
    const fs = yield* FileSystem.FileSystem;
    yield* fs.makeDirectory(folderOf(file), { recursive: true });
    yield* fs.writeFileString(file, `${entry}\n`, { flag: "a" });
}).pipe(Effect.mapError((e) => (e instanceof LogRefused ? e : new LogRefused(file, e.message))));
/** Whether there is a log at `file`. */
export const exists = (file) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    return yield* fs.exists(file).pipe(Effect.orElseSucceed(() => false));
});
export const fold = (file, start, step) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    if (!(yield* exists(file)))
        return undefined;
    const text = yield* fs.readFileString(file).pipe(Effect.mapError((e) => new LogRefused(file, e.message)));
    const whole = text.slice(0, text.lastIndexOf("\n") + 1);
    let running = start;
    for (const entry of whole.split("\n"))
        if (entry !== "")
            running = step(running, entry);
    return running;
});
