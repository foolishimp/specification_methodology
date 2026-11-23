import { open } from "./open.js";
/**
 * The term in force on the snapshot's ticket: the vectors of the governing
 * graph it denotes, by name, in its order. The ticket's own term where it
 * carries one that reads; otherwise, for the simplest ticket, on main and for
 * a ticket not yet inducted, the registry's default term (REQ-METHOD-006).
 */
export function inForce(graph, snapshot) {
    return (snapshot.ticket === "simplest" ? undefined : snapshot.ticket.term) ?? graph.byDefault;
}
/**
 * Whether a vector takes part in the work on the snapshot's ticket
 * (REQ-ALG-006). The first vector for a ticket takes part for every ticket but
 * the simplest. A vector of an inner workflow (`top` false) takes part
 * wherever the vector that holds it is stepped on. Of the governing graph's
 * other vectors, those the term in force names take part, and no other.
 */
export function takesPart(graph, vector, snapshot, top = true) {
    if (vector.first === true)
        return snapshot.ticket !== "simplest";
    if (!top)
        return true;
    return inForce(graph, snapshot).includes(vector.name);
}
/**
 * The next vector of the well-formed graph, or of one of its inner workflows
 * (`within`), or undefined when none may run.
 */
export function next(graph, snapshot, within = graph.graph) {
    const top = within === graph.graph;
    const taking = within.vectors.filter((v) => takesPart(graph, v, snapshot, top));
    const first = taking.find((v) => v.first === true);
    if (first !== undefined && open(graph, first, snapshot))
        return first;
    const order = top ? inForce(graph, snapshot) : (graph.orders.get(within) ?? []);
    return order.flatMap((name) => taking.filter((v) => v.name === name)).find((v) => open(graph, v, snapshot));
}
