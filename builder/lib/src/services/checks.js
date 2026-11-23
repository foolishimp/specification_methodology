/**
 * The checks service: the framework runs the checks the graph declares of an
 * asset against a checkout as it is now (REQ-FLOW-001, and the term "Check":
 * no language model, the same result on the same workspace). A command is
 * started through the supervised child (C12); a result is kept under the
 * identities of what the check reads, and used again only for exactly that
 * content (C4, CALCULUS L2). A check that cannot be run says so.
 *
 * Finding the names a `traced` check follows is the pattern search of H4. A
 * `traced` check leaves out of the names it finds in `into` those of each
 * family it declares to be another product's, and cannot be run where it so
 * declares a family the requirements have (D83).
 *
 * A check is not run again on content it has already judged, which keeps
 * the framework's own time for a step within REQ-PARAM-002.
 *
 * @uses C1 C2 C3 C4 C5 C12 C16 H1 H4 H5 H6
 * @is REQ-FLOW-001 REQ-FLOW-005 REQ-ALG-004 REQ-METHOD-005
 */
import { now } from "../kit/clock.js";
import * as Context from "effect/Context";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import { fieldsOf } from "../kit/field_lines.js";
import { difference } from "../kit/map_difference.js";
import { memo } from "../kit/memo.js";
import { formOf, namesIn } from "../kit/pattern_search.js";
import { withPaths } from "../kit/path_in_command.js";
import { covers } from "../kit/place_containment.js";
import { supervise } from "../kit/supervised_child.js";
import { covered } from "../graph/terms.js";
import { Files } from "./files.js";
export class Checks extends Context.Service()("stdo-builder/Checks") {
}
const tail = (text) => text.split("\n").slice(-40).join("\n");
/** The method's form of a requirement's name. */
const NAME = formOf("REQ-[A-Z]+-[0-9]+");
/** A family is written by its name alone: capital letters, and nothing else. */
const FAMILY = /^[A-Z]+$/;
/** A name's family: the part between `REQ-` and its number; none where the name is not of that form. */
const familyOf = (name) => {
    const rest = name.startsWith("REQ-") ? name.slice("REQ-".length) : undefined;
    const dash = rest?.lastIndexOf("-") ?? -1;
    return rest === undefined || dash <= 0 ? undefined : rest.slice(0, dash);
};
/**
 * The names `pattern` finds in the texts, each with the part that states it:
 * the section, from one heading to the next, whose heading names it, or else
 * the first section that names it.
 */
function stated(texts, form) {
    const byHeading = new Map();
    const anywhere = new Map();
    for (const text of texts) {
        for (const section of text.split(/\n(?=#)/)) {
            const heading = section.split("\n")[0] ?? "";
            if (heading.startsWith("#"))
                for (const name of namesIn(heading, form))
                    if (!byHeading.has(name))
                        byHeading.set(name, section);
            for (const name of namesIn(section, form))
                if (!anywhere.has(name))
                    anywhere.set(name, section);
        }
    }
    return new Map([...anywhere].map(([name, section]) => [name, byHeading.get(name) ?? section]));
}
export const checksLive = Layer.effect(Checks, Effect.gen(function* () {
    const files = yield* Files;
    const context = yield* Effect.context();
    const kept = memo();
    const textsUnder = (site, places) => Effect.forEach(covered(places, site.tree.files), (f) => files.read(`${site.checkout}/${f}`)).pipe(Effect.map((texts) => texts.map((t) => t ?? "")));
    const fresh = (check, site) => {
        const run = check.run;
        switch (run.kind) {
            case "command": {
                // A node's name in braces stands for the paths of its asset (REQ-GRAPH-003).
                const argv = withPaths(run.argv, site.places);
                const [command = "", ...args] = argv;
                return supervise({ command, args, cwd: site.checkout, deadline: site.minutes * 60_000, merged: true }).pipe(Effect.provideContext(context), Effect.map((o) => {
                    if (o.outcome === "returned") {
                        return o.code === 0
                            ? { result: "yes", found: `${argv.join(" ")} exited with 0`, detail: tail(o.output) }
                            : { result: "no", found: `${argv.join(" ")} exited with ${o.code}`, detail: tail(o.output) };
                    }
                    return { result: "cannot", found: `${argv.join(" ")} ${o.outcome}${o.outcome === "ran over" ? "" : `: ${o.why}`}` };
                }));
            }
            case "ticket_field":
                return Effect.gen(function* () {
                    const written = site.ticket === undefined ? "" : yield* files.read(`${site.checkout}/${site.ticket}`);
                    if (written === undefined)
                        return { result: "cannot", found: `no ticket at ${site.ticket}` };
                    const value = fieldsOf(written).get(run.field);
                    const holds = run.is !== undefined ? value === run.is : run.is_not !== undefined ? value !== run.is_not : value !== undefined;
                    return { result: holds ? "yes" : "no", found: `the ticket's ${run.field} is ${value ?? "not given"}` };
                });
            case "ticket_kept":
                return Effect.gen(function* () {
                    if (site.ticket === undefined)
                        return { result: "cannot", found: "there is no ticket of the branch" };
                    const onMain = yield* files.read(`${site.main}/${site.ticketOnMain ?? site.ticket}`);
                    const here = yield* files.read(`${site.checkout}/${site.ticket}`);
                    if (onMain === undefined || here === undefined)
                        return { result: "cannot", found: `main holds no ticket at ${site.ticketOnMain ?? site.ticket}, or the branch none at ${site.ticket}` };
                    // The user's lines are the keys of one map, the branch's of another: those only on main are lost (C2).
                    const linesOf = (text, all) => new Map(text.split("\n").filter((l) => all || l.trim() !== "").map((l) => [l, l]));
                    const lost = difference(linesOf(onMain, false), linesOf(here, true)).removed;
                    return lost.length === 0
                        ? { result: "yes", found: "every line the user wrote is in the ticket" }
                        : { result: "no", found: `${lost.length} line(s) the user wrote are no longer in the ticket` };
                });
            case "traced":
                return Effect.gen(function* () {
                    const form = formOf(run.pattern);
                    if (form === undefined)
                        return { result: "cannot", found: `'${run.pattern}' is not a pattern` };
                    const from = site.places.get(run.from);
                    const into = site.places.get(run.into);
                    if (from === undefined || into === undefined)
                        return { result: "cannot", found: "the graph names no such asset" };
                    const others = run.others ?? [];
                    const notFamily = others.find((f) => !FAMILY.test(f));
                    if (notFamily !== undefined)
                        return { result: "cannot", found: `'${notFamily}' is not a family` };
                    const fromTexts = yield* textsUnder(site, from);
                    // The families the requirements have, by the method's form of a name, whatever the check's own pattern leaves out.
                    const families = new Set(NAME === undefined || others.length === 0 ? [] : fromTexts.flatMap((t) => namesIn(t, NAME)).map(familyOf));
                    const own = others.find((f) => families.has(f));
                    if (own !== undefined) {
                        return { result: "cannot", found: `${from.join(", ")} states names of the family ${own}, which this check declares to be another product's` };
                    }
                    const statedIn = stated(fromTexts, form);
                    const named = new Set((yield* textsUnder(site, into)).flatMap((t) => namesIn(t, form)).filter((name) => !others.includes(familyOf(name) ?? "")));
                    const missing = [...statedIn].filter(([name, part]) => !part.includes(run.deferred) && !named.has(name)).map(([name]) => name);
                    const extra = [...named].filter((name) => !statedIn.has(name));
                    if (missing.length === 0 && extra.length === 0) {
                        return { result: "yes", found: `${into.join(", ")} names each of the ${statedIn.size} names ${from.join(", ")} states, and no other` };
                    }
                    const says = [
                        ...(missing.length === 0 ? [] : [`${into.join(", ")} does not name ${missing.join(", ")}`]),
                        ...(extra.length === 0 ? [] : [`${into.join(", ")} names ${extra.join(", ")}, which ${from.join(", ")} does not state`])
                    ];
                    return { result: "no", found: says.join("; ") };
                });
        }
    };
    // A check's key is what it reads: each path with its identity, beside what decides its answer (CALCULUS L2).
    const keyOf = (check, site) => {
        const run = check.run;
        const read = (paths) => paths.flatMap((p) => [p, site.tree.identities.get(p) ?? ""]);
        if (run.kind === "ticket_field")
            return [run.kind, run.field, run.is ?? "", run.is_not ?? "", ...read(site.ticket === undefined ? [] : [site.ticket])];
        if (run.kind === "traced")
            return [run.kind, run.pattern, run.deferred, ...(run.others ?? []), ...read(site.places.get(run.from) ?? []), "", ...read(site.places.get(run.into) ?? [])];
        // A command may read any file of the checkout: all of it but what lies apart, or all of it where it names a place apart.
        const argv = run.kind === "command" ? withPaths(run.argv, site.places) : [];
        return [run.kind, ...argv, "", site.apart.some((p) => argv.some((a) => covers(a, p) || covers(p, a))) ? site.tree.root : site.tree.beside ?? site.tree.root];
    };
    return Checks.of({
        run: (check, site) => {
            // How long it took, by the clock (C16), is given with what it found (REQ-FLOW-007).
            const timed = () => Effect.suspend(() => {
                const start = now().millis;
                return fresh(check, site).pipe(Effect.map((ran) => ({ ...ran, seconds: (now().millis - start) / 1000 })));
            });
            // What main holds of the ticket lies outside the checkout's identities, so that check is never kept.
            if (check.run.kind === "ticket_kept")
                return timed();
            const key = keyOf(check, site);
            const got = kept.lookup(key);
            if (got !== undefined)
                return Effect.succeed(got);
            return timed().pipe(Effect.tap((ran) => Effect.sync(() => kept.keep(key, ran))));
        }
    });
}));
