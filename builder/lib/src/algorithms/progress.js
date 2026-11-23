/**
 * `progress`: yes when fewer checks fail now than failed after the last
 * working session of the attempt. The first working session of an attempt
 * counts as progress (D210). A check done that could not
 * be run counts as failing; one not done is neither, and is not given here
 * (`isDone`, CALCULUS L3).
 *
 * @uses C9 C3
 * @is REQ-ALG-009
 */
import { falls } from "../kit/bounded_loop.js";
const failing = (outcomes) => outcomes.filter((o) => o.result !== "yes").length;
const measure = (outcomes) => (outcomes === undefined ? undefined : failing(outcomes));
/** `before` is undefined at the first working session of an attempt. */
export function progress(before, now) {
    return falls(measure(before), failing(now));
}
