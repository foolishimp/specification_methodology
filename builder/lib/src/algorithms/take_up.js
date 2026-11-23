/**
 * `take_up`: the ticket a run works on, by rules in a fixed order: an active
 * ticket no run holds; else, under the limit, the first in the backlog; else,
 * where nothing is active and main is not done, the simplest ticket; else
 * none, with which of these held. Names are taken in the order of their
 * characters.
 *
 * @uses C8 C5 C6 H2
 * @is REQ-ALG-010
 */
import { firstMatch } from "../kit/first_match.js";
import { firstByName } from "../kit/order_by_name.js";
import { vectorsOf } from "../graph/walk.js";
export function take_up(input) {
    const { board, limit, mainDone, named } = input;
    const hasFirst = vectorsOf(input.graph.graph, input.graph.registry).some((v) => v.first === true);
    const eligible = (t) => (hasFirst || t.simplest === true) && (named === undefined || t.name === named);
    const free = board.active.filter((t) => eligible(t) && !input.held.includes(t.name));
    const waiting = board.backlog.filter(eligible);
    const underLimit = board.active.length < limit;
    const rules = [
        { holds: () => free.length > 0, gives: () => ({ take: "ticket", name: firstByName(free, (t) => t.name)?.name ?? "", lane: "active" }) },
        { holds: () => underLimit && waiting.length > 0, gives: () => ({ take: "ticket", name: firstByName(waiting, (t) => t.name)?.name ?? "", lane: "backlog" }) },
        { holds: () => named === undefined && board.active.length === 0 && !mainDone, gives: () => ({ take: "simplest" }) }
    ];
    return firstMatch(rules, null, () => {
        const why = board.active.some(eligible) ? "held" : waiting.length > 0 ? "limit" : "nothing";
        const passedOver = !hasFirst && [...board.active, ...board.backlog].some((t) => t.simplest !== true);
        return passedOver
            ? { take: "none", why, note: "only the simplest ticket is taken up: the graph declares no first vector for a ticket" }
            : { take: "none", why };
    });
}
