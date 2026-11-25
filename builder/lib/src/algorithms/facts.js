/** The key under which the branch's ticket's identity is kept. It has a space, so it is never a node's name. */
export const TICKET = "the ticket";
/**
 * The key under which the identity of the branch's ticket without its term is
 * kept: what an answer or verdict at the vector the ticket enters by stands
 * for, so a term that changes at an induction entry opens none of them (D141).
 */
export const ASKED = "the ticket but its term";
/**
 * The key under which the identity of what a node declares of itself is kept:
 * what must be true of it, what accepts it and what it depends on (C14, C1); or
 * of what the first vector declares of the ticket, under its name. A verdict
 * or an answer kept there stands on it too, so a change to what acceptance
 * there means reopens it (D168, D175). It has a space, so it is never a node's
 * name.
 */
export const declaration = (node) => `the declaration of ${node}`;
const noFacts = {};
export function factsOf(snapshot, vector) {
    return snapshot.vectors.get(vector) ?? noFacts;
}
/**
 * The framework's part of a ticket (REQ-FLOW-001, REQ-FLOW-004; D202): every
 * line of the field `framework`, wherever it lies. The branch it left
 * (`left`), the checklist (`began`, `delivered`, `bound`, `unbound`), the
 * resolutions (`resolved`), the rulings (`ruling`) and the rulings on what
 * changed (`changed`).
 */
export const FRAMEWORK = "framework";
const DECISION = "for the user's decision";
/** The key of a ruling's entry naming, by its identity, a line of the framework's part that changed while a session worked (D230). */
export const NOT_THE_USERS = "not the user's answer";
/** The words of one line of the framework's part, after its field. */
export function lineText(l) {
    switch (l.line) {
        case "left":
            return `left ${l.branch}`;
        case "began":
            return `began ${l.vector} at ${l.commit}`;
        case "delivered":
            return `delivered ${l.vector}${l.decision === true ? ` ${DECISION}` : ""} at ${l.commit}${l.when === undefined ? "" : ` (${l.when})`}`;
        case "bound":
            return `bound ${l.vector} over ${l.enters} to ${l.ends} at ${l.commit}`;
        case "unbound":
            return `unbound at ${l.commit}`;
        case "resolved":
            return [
                `resolved ${l.by} ${l.says} at ${l.at} on ${l.commit}`,
                ...(l.verdict === undefined ? [] : [`verdict ${l.verdict}`]),
                ...(l.findings === undefined ? [] : [`findings ${l.findings}`]),
                ...(l.reason === undefined ? [] : [`reason ${oneLine(l.reason)}`])
            ].join("; ");
        case "ruling":
            return `ruling on ${l.commit}: ${oneLine(l.words)}`;
        case "changed": {
            const entries = [...l.files.map((f) => `${f.key} ${f.identity === "" ? "none" : f.identity}`), ...(l.foreign ?? []).map((id) => `${NOT_THE_USERS} ${id}`)];
            return `ruled ${l.says} on what changed at ${l.vector}${entries.length === 0 ? "" : `: ${entries.join("; ")}`}`;
        }
    }
}
/** Words put on one line, as a line of the ticket holds them. */
const oneLine = (words) => words.split("\n").map((w) => w.trim()).filter((w) => w !== "").join(" ");
/** One line's words read back; none where they are not of a form above, which is then passed over. */
export function readLine(words) {
    const [head = "", ...rest] = words.split("; ");
    const w = head.split(" ");
    const after = (key) => rest.find((p) => p.startsWith(`${key} `))?.slice(key.length + 1);
    if (w[0] === "delivered" && w.length >= 4) {
        const decision = head.includes(` ${DECISION} `);
        const i = w.indexOf("at");
        const when = w[i + 2];
        return { line: "delivered", vector: w[1] ?? "", commit: w[i + 1] ?? "", ...(decision ? { decision: true } : {}), ...(when === undefined ? {} : { when: when.slice(1, -1) }) };
    }
    if (w[0] === "left" && w.length === 2 && w[1] !== "")
        return { line: "left", branch: w[1] ?? "" };
    if (w[0] === "began" && w.length === 4 && w[2] === "at")
        return { line: "began", vector: w[1] ?? "", commit: w[3] ?? "" };
    if (w[0] === "bound" && w.length === 8)
        return { line: "bound", vector: w[1] ?? "", enters: w[3] ?? "", ends: w[5] ?? "", commit: w[7] ?? "" };
    if (w[0] === "unbound" && w.length === 3)
        return { line: "unbound", commit: w[2] ?? "" };
    if (w[0] === "resolved" && w.length === 7 && (w[1] === "evaluation" || w[1] === "user") && (w[2] === "yes" || w[2] === "no")) {
        const verdict = after("verdict");
        const findings = after("findings");
        const reason = after("reason");
        return { line: "resolved", by: w[1], says: w[2], at: w[4] ?? "", commit: w[6] ?? "", ...(verdict === undefined ? {} : { verdict }), ...(findings === undefined ? {} : { findings }), ...(reason === undefined ? {} : { reason }) };
    }
    if (w[0] === "ruled" && (w[1] === "yes" || w[1] === "no") && w[2] === "on" && w[3] === "what" && w[4] === "changed" && w[5] === "at" && w.length >= 7) {
        const colon = words.indexOf(": ");
        const entries = colon < 0 ? [] : words.slice(colon + 2).split("; ").flatMap((entry) => {
            const space = entry.lastIndexOf(" ");
            const identity = entry.slice(space + 1);
            return space < 0 ? [] : [{ key: entry.slice(0, space), identity: identity === "none" ? "" : identity }];
        });
        const files = entries.filter((e) => e.key !== NOT_THE_USERS);
        const foreign = entries.filter((e) => e.key === NOT_THE_USERS).map((e) => e.identity);
        return { line: "changed", says: w[1], vector: (w[6] ?? "").replace(/:$/, ""), files, ...(foreign.length === 0 ? {} : { foreign }) };
    }
    if (w[0] === "ruling" && w[1] === "on" && w.length >= 3) {
        const colon = words.indexOf(": ");
        return { line: "ruling", commit: (w[2] ?? "").replace(/:$/, ""), words: colon < 0 ? "" : words.slice(colon + 2) };
    }
    return undefined;
}
/** The binding of a session to a stretch, as the checklist shows it: the last `bound` line, and the line that ended it, if one has (REQ-FLOW-004). */
export function bindingOf(lines) {
    const at = lines.findLastIndex((l) => l.line === "bound");
    const bound = lines[at];
    if (bound === undefined || bound.line !== "bound")
        return undefined;
    const ended = lines.slice(at + 1).find((l) => l.line === "unbound" || (l.line === "delivered" && l.vector === bound.vector));
    return { bound, ...(ended === undefined ? {} : { ended }) };
}
/**
 * The vector whose work the checklist shows delivered for the user's decision
 * with no answer of the user after it, with the commit that delivery names
 * (REQ-FLOW-006 step 3). `names` gives the names a vector's answer is kept
 * under.
 */
export function awaiting(lines, names) {
    let waiting;
    for (const l of lines) {
        if (l.line === "delivered" && l.decision === true)
            waiting = l;
        else if (waiting !== undefined && l.line === "resolved" && l.by === "user" && names(waiting.vector).includes(l.at))
            waiting = undefined;
    }
    return waiting;
}
/** The names the checklist and the resolutions of a ticket name: each vector whose work began or was delivered, and each name a resolution is at (REQ-FLOW-005 step 1). */
export const workedIn = (lines) => [...new Set(lines.flatMap((l) => (l.line === "began" || l.line === "delivered" ? [l.vector] : l.line === "resolved" ? [l.at] : [])))];
