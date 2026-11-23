/**
 * The sessions service: the framework starts a session with its brief, in the
 * ticket's checkout, and ends one that runs longer than allowed (REQ-FLOW-001,
 * "Start and end a session" and "Fail"). The session is given the path of its
 * brief and nothing else (REQ-ALG-007).
 *
 * This module holds the command binding: the settings file names a command for
 * each agent, and the framework starts it through the supervised child (C12)
 * in the checkout, with the path of the brief. A session's end gives what it
 * printed, whether it returned or failed. The stand-in agent of the
 * scenarios is a second layer of the same service (`stand_in.ts`).
 *
 * @uses C12 C16 H6
 * @is REQ-FLOW-001 REQ-FLOW-005 REQ-ALG-007
 */
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { now } from "../kit/clock.js";
import { withPath } from "../kit/path_in_command.js";
import { supervise } from "../kit/supervised_child.js";
export class Sessions extends Context.Service()("stdo-builder/Sessions") {
}
export const commandSessions = Layer.effect(Sessions, Effect.gen(function* () {
    const context = yield* Effect.context();
    return Sessions.of({
        agentOf: (named) => named,
        start: (call) => Effect.gen(function* () {
            // The brief's path goes where the command marks it, or last (H6).
            const [command = "", ...args] = withPath(call.agent.command, call.briefPath);
            const began = now().millis;
            const o = yield* supervise({ command, args, cwd: call.checkout, deadline: call.minutes * 60_000, merged: true }).pipe(Effect.provideContext(context));
            const seconds = (now().millis - began) / 1000;
            if (o.outcome === "could not start")
                return { ended: "failed", seconds, why: `it could not start: ${o.why}`, printed: o.why };
            if (o.outcome !== "returned") {
                return { ended: "failed", seconds, why: o.outcome === "ran over" ? "it ran longer than allowed and was ended" : `it ${o.outcome}: ${o.why}`, printed: o.printed ?? "" };
            }
            if (o.code !== 0)
                return { ended: "failed", seconds, why: `it exited with ${o.code}`, printed: o.output };
            return { ended: "returned", seconds, printed: o.output };
        })
    });
}));
