/**
 * The hold service: while a run works on a ticket no second run takes that
 * ticket (REQ-FLOW-001, "Hold"). It is carried out by the exclusive hold bound
 * to a process (C11): a killed run leaves nothing that refuses the next, but
 * a process of its session still alive after the next run has tried to end
 * it, or a process the framework cannot place (C12, D215, D223).
 *
 * @uses C11 C12
 * @is REQ-FLOW-001 REQ-FLOW-003
 */
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { held, holding, keeping, left } from "../kit/exclusive_hold.js";
import { endMarked, marked, named, tableRead } from "../kit/supervised_child.js";
export class Hold extends Context.Service()("stdo-builder/Hold") {
}
export const holdLive = Layer.effect(Hold, Effect.gen(function* () {
    const context = yield* Effect.context();
    return Hold.of({
        holding: (file, body) => holding(file, body).pipe(Effect.provideContext(context)),
        keeping: (file, body) => keeping(file, body).pipe(Effect.provideContext(context)),
        held: (files) => held(files).pipe(Effect.provideContext(context)),
        left: (file) => left(file).pipe(Effect.provideContext(context)),
        alive: (sought) => marked(sought).pipe(Effect.map((f) => ({ alive: f.alive.map(named), unplaced: f.unplaced.map(named) })), Effect.catch((e) => Effect.succeed({ cannot: e.why, ...(e.table === undefined ? {} : { table: e.table }) })), Effect.provideContext(context)),
        table: () => tableRead().pipe(Effect.map((e) => (e === undefined ? undefined : { cannot: e.why, ...(e.table === undefined ? {} : { table: e.table }) })), Effect.provideContext(context)),
        end: (sought) => endMarked(sought).pipe(Effect.provideContext(context))
    });
}));
