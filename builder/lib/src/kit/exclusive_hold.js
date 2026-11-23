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
 * the files below, so the greatest number never goes back. This reading of
 * C11 is recorded in DECISIONS.md (D32, D50): the operating system does not
 * remove the file, it ends the process the file names.
 *
 * @carries C11
 * @uses C15
 */
import * as Effect from "effect/Effect";
import * as FileSystem from "effect/FileSystem";
import { createIfAbsent } from "./create_if_absent.js";
/** The process with this number runs. */
function runs(pid) {
    if (!Number.isInteger(pid) || pid <= 0)
        return false;
    try {
        process.kill(pid, 0);
        return true;
    }
    catch (error) {
        return error.code === "EPERM";
    }
}
const folderOf = (file) => file.slice(0, Math.max(0, file.lastIndexOf("/")));
const nameOf = (file) => file.slice(file.lastIndexOf("/") + 1);
const numbered = (file, n) => (n === 0 ? file : `${file}.${n}`);
/** The numbers of the hold's files there are now, greatest last. */
const numbers = (file) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    const name = nameOf(file);
    const names = yield* fs.readDirectory(folderOf(file)).pipe(Effect.orElseSucceed(() => []));
    return names
        .flatMap((n) => (n === name ? [0] : n.startsWith(`${name}.`) && /^[0-9]+$/.test(n.slice(name.length + 1)) ? [Number(n.slice(name.length + 1))] : []))
        .sort((a, b) => a - b);
});
/** The process the file of number `n` names, where it runs. */
const holderAt = (file, n) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    const text = yield* fs.readFileString(numbered(file, n)).pipe(Effect.orElseSucceed(() => ""));
    const pid = Number(text.trim());
    return runs(pid) ? pid : undefined;
});
/** The process that holds `file`, where one does: the one the greatest file names. */
const holderOf = (file) => Effect.gen(function* () {
    const top = (yield* numbers(file)).at(-1);
    return top === undefined ? undefined : yield* holderAt(file, top);
});
/** Makes the file of number `n`, whole, saying `says` (C15); false where it is there already. */
const make = (file, n, says) => createIfAbsent(numbered(file, n), `${says}\n`).pipe(Effect.map((made) => made === "written"), Effect.orElseSucceed(() => false));
/** Removes the hold's files numbered below `n`. */
const removeBelow = (file, n) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    for (const m of yield* numbers(file))
        if (m < n)
            yield* fs.remove(numbered(file, m), { force: true }).pipe(Effect.ignore);
});
/** Takes the hold; the number of the file that holds it, or undefined where another process holds it. */
const take = (file) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    const top = (yield* numbers(file)).at(-1);
    if (top !== undefined && (yield* holderAt(file, top)) !== undefined)
        return undefined;
    const mine = top === undefined ? 1 : top + 1;
    if (!(yield* make(file, mine, String(process.pid))))
        return undefined;
    // A taker whose view was old has made a number below the greatest: it lets go.
    if (((yield* numbers(file)).at(-1) ?? mine) > mine) {
        yield* fs.remove(numbered(file, mine), { force: true }).pipe(Effect.ignore);
        return undefined;
    }
    yield* removeBelow(file, mine);
    return mine;
});
/** Lets go: the next number says free, then the files below it go. */
const release = (file, mine) => Effect.gen(function* () {
    if (yield* make(file, mine + 1, "free"))
        yield* removeBelow(file, mine + 1);
});
/** Runs `body` while holding `file`, and lets go after. "held" when another process holds it. */
export const holding = (file, body) => Effect.gen(function* () {
    const mine = yield* take(file);
    if (mine === undefined)
        return "held";
    return yield* body.pipe(Effect.map((done) => ({ done })), Effect.ensuring(release(file, mine)));
});
/** Whether the hold was left by a process that has ended: its greatest file names a process, not free, that no longer runs (REQ-FLOW-007, a run cut off). */
export const left = (file) => Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;
    const top = (yield* numbers(file)).at(-1);
    if (top === undefined)
        return false;
    const text = yield* fs.readFileString(numbered(file, top)).pipe(Effect.orElseSucceed(() => "free"));
    return text.trim() !== "free" && (yield* holderAt(file, top)) === undefined;
});
/** Of the files named, those a running process holds. */
export const held = (files) => Effect.gen(function* () {
    const out = [];
    for (const file of files)
        if ((yield* holderOf(file)) !== undefined)
            out.push(file);
    return out;
});
