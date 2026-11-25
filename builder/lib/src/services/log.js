/**
 * The event log service: the framework adds one entry at a time to the one
 * event log of the governed product (REQ-FLOW-001, "Add to the event log"), and
 * a person, through `stands`, reads it in one pass. It is carried out by the
 * append-only log (C10); each entry is written and read in its one written
 * form (C14). An entry it cannot read is passed over and left in place.
 *
 * For the one command it serves, it keeps which logs it has added to, so it
 * can say where one of them is gone when it is next added to, and how many
 * times it started one anew so (REQ-FLOW-003, REQ-FLOW-007, D247).
 *
 * @uses C10 C14
 * @is REQ-FLOW-007
 */
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { append, exists, fold } from "../kit/append_only_log.js";
import { list, number, optional, read, record, text, writeLine } from "../kit/lossless_encoding.js";
const EntryShape = record({
    at: text,
    event: text,
    run: optional(text),
    ticket: optional(text),
    vector: optional(text),
    kind: optional(text),
    agent: optional(text),
    check: optional(text),
    result: optional(text),
    seconds: optional(number),
    cost: optional(text),
    unit: optional(text),
    calls: optional(number),
    ending: optional(text),
    why: optional(text),
    path: optional(text),
    commit: optional(text),
    files: optional(list(text)),
    release: optional(text),
    command: optional(list(text)),
    printed: optional(text),
    findings: optional(text),
    processes: optional(number),
    named: optional(number),
    main: optional(text),
    branch: optional(text)
});
/** The log could not be added to, and why. */
export class LogRefused {
    why;
    _tag = "LogRefused";
    constructor(why) {
        this.why = why;
    }
}
export class EventLog extends Context.Service()("stdo-builder/EventLog") {
}
export const eventLogLive = Layer.effect(EventLog, Effect.gen(function* () {
    const context = yield* Effect.context();
    // The logs this command added to, and how many times it found each gone (D247).
    const added = new Set();
    const anew = new Map();
    return EventLog.of({
        append: (file, entry) => append(file, writeLine(EntryShape, entry)).pipe(Effect.mapError((e) => new LogRefused(e.why)), Effect.provideContext(context), Effect.tap(() => Effect.sync(() => added.add(file)))),
        exists: (file) => exists(file).pipe(Effect.provideContext(context)),
        gone: (file) => exists(file).pipe(Effect.provideContext(context), Effect.map((there) => added.has(file) && !there), Effect.tap((lost) => Effect.sync(() => (lost ? anew.set(file, (anew.get(file) ?? 0) + 1) : anew)))),
        startedAnew: (file) => Effect.sync(() => anew.get(file) ?? 0),
        fold: (file, start, step) => fold(file, start, (running, line) => {
            const got = read(EntryShape, line);
            return "value" in got ? step(running, got.value) : running;
        }).pipe(Effect.mapError((e) => new LogRefused(e.why)), Effect.provideContext(context))
    });
}));
