/**
 * The combinators of the calculus (design, CALCULUS.md section 2): K5 to K8,
 * a sequence, a decision on what was read, a repeat under C9 and a hold
 * through the hold service, with the two terms that do nothing. It is the one
 * place a flow reaches Effect. A flow built from these and the services alone
 * is one term of the calculus page.
 *
 * @carries C17
 */
import * as Effect from "effect/Effect";
import { goesOn } from "./bounded_loop.js";
/** The term that does nothing and gives `value`. */
export const end = (value) => Effect.succeed(value);
/** The term that does nothing and fails with `f`. */
export const fault = (f) => Effect.fail(f);
/** K5: the terms written, each after the one before; the value of the last. */
export const sequence = (...terms) => terms.reduce((done, next) => Effect.flatMap(done, () => next));
/** K5 over a finite list, in its order: the values of the terms, in that order. */
export const each = (values, term) => Effect.forEach(values, term);
/** K6: does `read`, then the term the pure function `then` selects from what it gave. */
export const decide = (read, then) => Effect.flatMap(read, then);
/** The read of K6 that gives `term`'s value or its fault. */
export const outcome = (term) => Effect.match(term, { onFailure: (f) => ({ fault: f }), onSuccess: (value) => ({ value }) });
/** The term over one of the services, given by its key, which is the term that gives the service: it reads nothing and decides nothing. */
export const using = (service, term) => Effect.flatMap(service, term);
/**
 * K7: does `body` on `state`, and again on each state it gives for the next
 * round, while the bound is not reached and, where a measure is given, the
 * measure strictly falls (C9). The state is the only value carried from one
 * round to the next.
 */
export const repeat = (state, body, bound, measure) => {
    const round = (s, made, before) => Effect.flatMap(body(s), (r) => {
        if ("leave" in r)
            return Effect.succeed(r.leave);
        const now = measure === undefined ? 0 : measure(r.again);
        const goes = goesOn(measure === undefined ? undefined : before, now, made + 1, bound.rounds ?? Number.POSITIVE_INFINITY) && bound.reached?.(r.again) !== true;
        return goes ? round(r.again, made + 1, now) : Effect.succeed(bound.leave(r.again));
    });
    return round(state, 0, measure === undefined ? undefined : measure(state));
};
/** K8: does `term` while holding `name`; "held" where another process holds it. */
export const held = (hold, name, term) => hold.holding(name, term);
