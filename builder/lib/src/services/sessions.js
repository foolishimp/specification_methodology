/**
 * The sessions service: the framework starts a session with its brief, in the
 * workspace's folder, and ends every process it knows to be of it at its
 * return, when its time is over, and when the run receives a signal
 * (REQ-FLOW-001, "Start and end a session" and "Fail"; REQ-FLOW-003;
 * REQ-FLOW-005). The supervised child knows them by their parent, their group
 * and the ticket's mark, from the agent's own process on (C12, D212, D222). A
 * session's end says how many of its processes were ended and, where one is
 * still alive or the framework finds one it cannot place, why: such a session
 * is not over, and the run goes no further (D221, D223). The session is given the path of its brief and
 * nothing else (REQ-ALG-007).
 *
 * This module holds the command binding: the settings file names a command for
 * each agent, and the framework starts it through the supervised child (C12)
 * in the workspace's folder, with the path of the brief. A session's end gives what it
 * printed, whether it returned or failed. The stand-in agent of the
 * scenarios is a second layer of the same service (`stand_in.ts`).
 *
 * @uses C12 C16 H6
 * @is REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-ALG-007 REQ-INTERFACE-001
 */
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { now } from "../kit/clock.js";
import { withPath } from "../kit/path_in_command.js";
import { bindSignals, goNoFurther, inherited, settled, supervise } from "../kit/supervised_child.js";
export class Sessions extends Context.Service()("stdo-builder/Sessions") {
}
export const commandSessions = Layer.effect(Sessions, Effect.gen(function* () {
    const context = yield* Effect.context();
    bindSignals();
    return Sessions.of({
        agentOf: (named) => named,
        goNoFurther,
        settled: () => Effect.sync(settled),
        within: () => Effect.sync(inherited),
        start: (call) => Effect.gen(function* () {
            // The brief's path goes where the command marks it, or last (H6).
            const [command = "", ...args] = withPath(call.agent.command, call.briefPath);
            const began = now().millis;
            const o = yield* supervise({ command, args, cwd: call.folder, deadline: call.minutes * 60_000, merged: true, mark: call.mark }).pipe(Effect.provideContext(context));
            const seconds = (now().millis - began) / 1000;
            if (o.outcome === "could not start")
                return { ended: "failed", seconds, why: `it could not start: ${o.why}`, printed: o.why };
            // How many processes of it were ended, and why not every one, where not every one could be (D213, D221).
            const processes = { ...(o.ended === undefined || o.ended === 0 ? {} : { processes: o.ended }), ...(o.unended === undefined ? {} : { unended: o.unended }), ...(o.table === undefined ? {} : { table: o.table }) };
            if (o.outcome === "cut off")
                return { ended: "cut off", signal: o.signal, printed: o.printed ?? "", ...processes };
            if (o.outcome !== "returned") {
                return { ended: "failed", seconds, why: o.outcome === "ran over" ? "it ran longer than allowed and was ended" : `it ${o.outcome}: ${o.why}`, printed: o.printed ?? "", ...processes };
            }
            if (o.code !== 0)
                return { ended: "failed", seconds, why: `it exited with ${o.code}`, printed: o.output, ...processes };
            return { ended: "returned", seconds, printed: o.output, ...processes };
        })
    });
}));
