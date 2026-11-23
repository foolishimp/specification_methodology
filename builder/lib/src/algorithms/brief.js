/**
 * `brief`: what a session is given for a step, by name and by path only: the
 * activation packet of the reference frame the vector declares for that kind
 * of session (D88). It holds the minimum of the method's REFERENCE_FRAME
 * standard, section 11: the frame and its closed result, the subject and the
 * basis, the attention surface, the actor's authority and territory, the
 * evidence and relations, and the conditions to stop. Nothing in it is a line
 * of an asset; what it takes from the graph, such as a check's form, is the
 * graph's. Tickets are named by lane, so it does not grow with tickets done.
 *
 * Every packet but that of the session that inducts the ticket says that the
 * asset holds what the ticket's work needs and no part the ticket does not ask
 * for, and that such a part is a ground for no. A working packet also says
 * that every line the work and the findings do not require is left as it
 * stands, and what holds where the work removes or renames something; an
 * evaluating packet, that such a line changed since the content main holds is
 * a ground for no, and, at each node it judges, the commit that holds main's
 * content of it and the commands that give the lines the branch changed from
 * it, or that main holds none of it (D208). The packet for inducting the
 * ticket lists the entries of the registry its term may name, the induction's
 * own among them, each with the nodes it writes, what it rests on and what it
 * is for, and gives the check of the term in its form, with the nodes each node
 * depends on. Where the run has reached
 * an induction entry of the term, it names that entry's stretch, and the term
 * is written in the entry's place; it names the ticket the user confirmed by
 * the identity git holds it under, so a session after a failed attempt reads
 * the confirmed term there (REQ-METHOD-006, REQ-ALG-007).
 *
 * Of the method, a packet admits only the sections its frame names, and gives
 * where the release is installed only then (D103, D104).
 *
 * Both give what the graph says the asset must be: the results each node it
 * writes declares (for the first vector, the ticket's, which it declares), their
 * checks, and the checks of the other assets the vectors that take part write
 * that run or read one of them (D96, D98, D168, D181). The asset is every node the
 * vector writes, and what it rests on every node those depend on that it does
 * not write; an evaluation judges it against every node its verdict stands on
 * that the vector does not write (REQ-METHOD-006, D169).
 *
 * Both state the gap in one form (D177): for each node the session writes or
 * judges, the node as it stands, what is recorded at it, and what that was
 * given on that differs now, each with the identity git holds its content
 * under as it was. What the gap then is, REQ-ALG-007 states.
 *
 * @uses C1 C2 C5 C6 H1 H3 H6
 * @is REQ-ALG-007 REQ-METHOD-006
 */
import { withPaths } from "../kit/path_in_command.js";
import { covers } from "../kit/place_containment.js";
import { holdsWhiteSpace } from "../kit/white_space.js";
import { listing } from "../graph/registry.js";
import { ATTEMPTS, MINUTES, pathsOf } from "../graph/terms.js";
import { carries, nodesOf, vectorsOf } from "../graph/walk.js";
import { difference, paths as differing } from "../kit/map_difference.js";
import { factsOf, TICKET } from "./facts.js";
import { byPath } from "./identity.js";
import { takesPart } from "./next.js";
import { against, identityNow, recordAt, recordsOf, since, TERM } from "./passes.js";
import { guarded } from "./trespass.js";
import { declaredAt, placedOf } from "./well_formed.js";
/** A word of a command as a user would type it: quoted where it holds white space. */
const shown = (word) => (holdsWhiteSpace(word) ? `"${word}"` : word);
/** When a check says yes, in words, from what the graph declares of it and the paths of the assets. */
function yesWhen(run, places) {
    const at = (name) => (places.get(name) ?? [name]).join(", ");
    switch (run.kind) {
        case "command":
            return `\`${withPaths(run.argv, places).map(shown).join(" ")}\` exits with 0, run in this folder`;
        case "ticket_field": {
            const holds = run.is !== undefined ? `is ${run.is}` : run.is_not !== undefined ? `is not ${run.is_not}, or is not given` : "is given";
            return `the ticket's field ${run.field}, read from a line "- ${run.field}: value", ${holds}`;
        }
        case "ticket_kept":
            return "every line the user wrote in the ticket, as main holds it, is still in it";
        case "traced": {
            const others = run.others === undefined || run.others.length === 0
                ? ""
                : `; the names of the families ${run.others.join(", ")} in ${at(run.into)} are another product's, and are left out`;
            return `every name matching \`${run.pattern}\` that ${at(run.from)} states is named in ${at(run.into)}, unless the section that states it says \`${run.deferred}\`; and ${at(run.into)} names none that ${at(run.from)} does not state${others}`;
        }
    }
}
/** The check runs or reads the asset: a command names its place, a `traced` check reads from it or into it, or a check of the ticket reads the ticket (D96). */
function reads(run, asset) {
    switch (run.kind) {
        case "command":
            return run.argv.some((word) => word.includes(`{${asset}}`));
        case "traced":
            return run.from === asset || run.into === asset;
        case "ticket_field":
        case "ticket_kept":
            return asset === TICKET;
    }
}
/** The brief: of the evaluating session where it is asked for and the vector declares an evaluation, which is where a step starts one; else of the working session. */
export function brief(graph, vector, kind, snapshot, basis) {
    const nodes = nodesOf(graph.graph, graph.registry);
    const paths = new Map(nodes.map((n) => [n.name, pathsOf(n)]));
    const ticket = snapshot.ticket === "simplest" ? undefined : snapshot.ticket;
    const assetOf = (name) => ({ name, place: name === TICKET ? (ticket?.path ?? "") : (paths.get(name) ?? []).join(", ") });
    // What a vector writes: the nodes of its graph function; for the first vector, the ticket.
    const writes = (v) => (v.first === true ? [TICKET] : placedOf(graph, v).writes);
    const produced = writes(vector);
    const vectors = vectorsOf(graph.graph, graph.registry);
    const top = new Set(graph.graph.vectors);
    // Where the findings of a verdict are kept: those of the evaluation that writes it there.
    const findingsOf = (verdict) => vectors.find((v) => v.evaluation !== undefined && v.evaluation.verdict === verdict.at)?.evaluation?.findings;
    const saidOf = (by, g, at) => g === undefined ? [] : [{ by, says: g.says, ...(g.says === "yes" || at === undefined ? {} : { at }), ...(g.ticket === undefined ? {} : { ticket: g.ticket }), ...(g.commit === undefined ? {} : { commit: g.commit }) }];
    // What git holds a key's content under as it was: for the ticket its identity, for a node the identity at each of its paths that differs now (C1, C2); none for a declaration or the ticket without its term, which git keeps no content of.
    const wasOf = (key, id) => {
        if (key === TICKET)
            return [{ identity: id }];
        const node = nodes.find((n) => n.name === key);
        if (node === undefined)
            return [];
        const was = byPath(node, id);
        const differs = new Set(differing(difference(was, byPath(node, identityNow(key, snapshot)))));
        const several = pathsOf(node).length > 1;
        return [...was].filter(([path]) => differs.has(path)).map(([path, identity]) => (several ? { path, identity } : { identity }));
    };
    // The one form of the gap (D177): the node as it stands, what is recorded at it, and what the verdict, or else the answer, was given on that differs now.
    const standOf = (name) => {
        const at = name === TICKET ? vector.name : name;
        const verdict = recordAt(at, "evaluation", snapshot);
        const answer = recordAt(at, "decision", snapshot);
        const base = verdict ?? answer;
        return {
            name,
            there: name === TICKET ? ticket !== undefined : snapshot.identities.has(name),
            said: [...saidOf("evaluation", verdict, verdict === undefined ? undefined : findingsOf(verdict)), ...saidOf("user", answer, answer?.at)],
            ...(base === undefined ? {} : {
                since: since(graph, at, base.on, snapshot).map((key) => {
                    const was = base.on.get(key);
                    // The ticket as it was is read under the commit the resolution names, since git keeps no content of it without the framework's part (D203).
                    const shown = key === TICKET && base.commit !== undefined && snapshot.ticket !== "simplest" ? [{ identity: `${base.commit}:./${snapshot.ticket.path}` }] : undefined;
                    return { name: key, was: shown ?? (was === undefined ? [] : wasOf(key, was)) };
                })
            })
        };
    };
    const fenced = guarded(graph, vector, kind, basis.places);
    const kept = keptAt(recordsOf(graph, vector, "decision"), produced);
    const own = produced.map((name) => assetOf(name).place);
    const first = graph.graph.vectors.find((v) => v.first === true);
    // The checks the graph declares of an asset, those `keep` keeps, each in its form with the asset's place (REQ-GRAPH-002).
    const formsOf = (name, keep = () => true) => declaredAt(graph, name === TICKET ? (first?.name ?? "") : name).filter(keep).map((c) => ({ name: c.name, yes: yesWhen(c.run, paths) }));
    const checks = produced.flatMap((name) => formsOf(name));
    const shared = {
        vector: vector.name,
        basis,
        guarded: fenced.fixed.filter((place) => !fenced.free.some((free) => covers(free, place))),
        decision: vector.decision === undefined
            ? "none by the user"
            : `the user says yes or no to ${listed(produced)} once its checks pass${vector.evaluation === undefined ? "" : " and its verdict says yes"}${kept === undefined ? "" : `; the answer is ${kept}`}`,
        minutes: vector.minutes ?? MINUTES,
        // What must be true of each node it writes is that node's; the ticket's, which no node declares, the first vector's (D168).
        result: vector.first === true ? (vector.result ?? []) : produced.flatMap((name) => nodes.find((n) => n.name === name)?.result ?? []),
        checks,
        // The checks of the other assets the vectors that take part write that run or read one this vector writes, each in its form (D96).
        others: [...new Set(vectors.filter((v) => takesPart(graph, v, snapshot, top.has(v))).flatMap(writes))].filter((name) => !produced.includes(name))
            .flatMap((name) => formsOf(name, (c) => produced.some((p) => reads(c.run, p))).map((c) => ({ ...c, of: name })))
    };
    const evaluation = kind === "evaluation" ? vector.evaluation : undefined;
    if (evaluation !== undefined) {
        const frame = vector.frames?.evaluation;
        // The nodes it judges are those its verdict is recorded at (D164).
        const judged = recordsOf(graph, vector, "evaluation");
        return {
            kind: "evaluation",
            ...shared,
            ...(frame === undefined ? {} : { frame }),
            ...(ticket === undefined ? {} : { ticket: assetOf(TICKET), ...(ticket.ruled === true ? { ruled: true } : {}) }),
            write: fenced.free,
            judge: judged.map((name) => assetOf(name)),
            ...(snapshot.main === undefined ? {} : { main: judged.map((name) => ({ name, paths: paths.get(name) ?? [], ...(snapshot.main?.holds.includes(name) === true ? { commit: snapshot.main.commit } : {}) })) }),
            against: against(graph, vector).map((name) => assetOf(name)),
            stands: judged.map(standOf),
            findings: evaluation.findings,
            verdict: evaluation.verdict
        };
    }
    const facts = factsOf(snapshot, vector.name);
    // The ticket the user confirmed, by its identity: the session bound to a stretch rewrites the ticket it reads (REQ-METHOD-006).
    const yes = vector.first === true ? recordAt(vector.name, "decision", snapshot) : undefined;
    const confirmed = yes?.says === "yes" ? yes.on.get(TICKET) : undefined;
    const frame = vector.frames?.work;
    // The first vector has one outcome beside the ticket's checks: the ticket's term is well formed (REQ-METHOD-006). Where the run has
    // reached an induction entry of the term, the packet is bound to its stretch: the term written in its place obeys the law there.
    const inducts = carries(vector) ?? vector.name;
    const stretch = ticket?.inducting;
    const [enters, ends] = stretch === undefined ? ["the node the field enters names", "the node the field ends names"] : [stretch.enters, stretch.ends];
    // The edges the work is read by: each node with the nodes it depends on (REQ-GRAPH-003).
    const edges = nodes.filter((n) => (n.depends ?? []).length > 0).map((n) => `${n.name} on ${listed(n.depends ?? [])}`).join("; ");
    const composing = vector.first === true
        ? [{ name: TERM, yes: `the ticket's field term, read from a line "- term: value", is a reference to an entry of the registry listed here, or a sequence of such references, where a reference to ${inducts} is an induction entry that names its stretch, {"term": "reference", "name": "${inducts}", "enters": "<node>", "ends": "<node>"}, writes the work of that stretch, less than the work it lies in, and is never the term's first entry; ${stretch === undefined ? "" : `the term is the one the user confirmed with the induction entry over ${stretch.enters} to ${stretch.ends} alone replaced, and every other line of the ticket is as the user confirmed it; `}the term ${stretch === undefined ? "" : "in that entry's place "}composes: each entry rests on nodes an entry before it writes, or that are accepted as they now stand and written by no entry of the term, and no node is written twice; it writes exactly the work from ${enters} to ${ends}: those two nodes and every node that depends on the first and on which the second depends, where the nodes depend so: ${edges}; and the vector of its first entry declares an evaluation or a decision` }]
        : [];
    return {
        kind: "work",
        ...shared,
        ...(frame === undefined ? {} : { frame }),
        ...(ticket === undefined ? {} : { ticket: assetOf(TICKET), ...(ticket.ruled === true ? { ruled: true } : {}) }),
        write: [...own, ...fenced.free],
        produce: produced.map((name) => assetOf(name)),
        rests: placedOf(graph, vector).rests.map((name) => assetOf(name)),
        stands: produced.map(standOf),
        checks: [...shared.checks, ...composing],
        ...(facts.found === undefined ? {} : { found: facts.found }),
        ...(vector.evaluation === undefined ? {} : { judgedAgainst: against(graph, vector) }),
        ownTicket: vector.first === true,
        ...(vector.first === true ? { registry: listing(graph.registry, nodes) } : {}),
        ...(vector.first === true && stretch !== undefined ? { stretch } : {}),
        ...(vector.first === true && stretch !== undefined && confirmed !== undefined ? { confirmed } : {}),
        attempts: vector.attempts ?? ATTEMPTS
    };
}
/** What every packet but the induction's says the asset holds, and what is a ground for no (REQ-ALG-007). */
export const PROPORTION = "- work: the asset holds what the ticket's work needs and no part the ticket does not ask for; a part it does not ask for is a ground for no.";
/** What a working packet says of the lines the work does not require, and of what the work removes or renames (REQ-ALG-007, D208). */
export const UNCHANGED = {
    work: "- unchanged: every line the ticket's work and the findings do not require is left as it stands. Where the work removes or renames a file, a command, a record or a term, no file this session may write still mentions it as it was, and what this session prints names each file of an asset it may not write that does, which is left for that asset's step.",
    evaluation: "- unchanged: a line changed since the content last accepted, as main holds it (below), that the ticket's work and the findings do not require is a ground for no; the findings name each such line by its path and line, and copy none of it."
};
/** A node judged as main holds it, in one line: the commands that give the lines the branch changed from it, or that every line of it is the ticket's work (D208). */
const onMain = (m) => {
    const at = m.paths.map(shown).join(" ");
    return m.commit === undefined
        ? `- as main holds it, ${m.name}: main holds none of it, so every line of it is judged as the ticket's work.`
        : `- as main holds it, ${m.name}: the content last accepted, with what the user changed there by hand, is under the commit ${m.commit}; the lines the branch changed from it: \`git diff ${m.commit} -- ${at}\`, with each file git does not yet hold, every line of which the branch added: \`git ls-files --others --exclude-standard -- ${at}\`.`;
};
/** What every working packet says the work is, and every evaluating packet what is judged: the gap, whose one form the lines "as it stands" give (D177). */
const GAP = {
    work: "- gap: the work is the gap between each asset as it stands, below, and what its results require against what it rests on as it now is. What the gap does not concern stays as it stands.",
    evaluation: "- gap: each asset as it stands, below, is judged by its results against what it is judged against as it now is. A yes recorded at an asset held on what it was given on, so a gap can open only in what has changed since."
};
/** A node as it stands, in one line (D177). */
const stood = (s) => {
    const held = (r) => (r.commit === undefined ? "" : ` (in the ticket ${r.ticket ?? ""} on the commit ${r.commit})`);
    const said = s.said.map((r) => sayOf(r).replace(" to it", ` to it${held(r)}`));
    function sayOf(r) {
        return r.by === "evaluation"
            ? r.says === "yes" ? "the evaluation said yes to it" : r.says === "no" ? `the evaluation said no to it${r.at === undefined ? "" : `, with its findings at ${r.at}`}` : `the evaluation could not judge it${r.at === undefined ? "" : `, with why at ${r.at}`}`
            : r.says === "yes" ? "the user said yes to it" : `the user said no to it${r.at === undefined ? "" : `, with the reason at ${r.at}`}`;
    }
    const was = (c) => c.was.length === 0
        ? c.name
        : `${c.name} (${c.was.map((w) => `${w.path === undefined ? "" : `at ${w.path} `}as it was: \`git show ${w.identity}\``).join("; ")})`;
    const since = s.since === undefined ? [] : [s.since.length === 0 ? "nothing it was given on has changed since" : `changed since: ${listed(s.since.map(was))}`];
    return `- as it stands, ${s.name}: ${s.there ? "there" : "not there"}; ${[...(said.length === 0 ? ["nothing is recorded at it"] : said), ...since].join("; ")}.`;
};
/** Names joined as a person writes a list: "a, b and c". */
export const listed = (names) => names.length < 2 ? names.join("") : `${names.slice(0, -1).join(", ")} and ${names[names.length - 1] ?? ""}`;
/** Where the user's answer is kept, where that is not every node asked about: at the nodes a decision accepts, each for itself and the nodes it depends on (D164). */
export const keptAt = (at, asked) => at.length === asked.length ? undefined : `kept at ${listed(at)}, for ${at.length === 1 ? "it and the nodes it depends" : "each and the nodes each depends"} on`;
/** The brief as the lines a session reads: Markdown, under the six headings of the method's minimal activation binding. */
export function lines(b) {
    const asset = (a) => `${a.name} at ${a.place}`;
    const own = b.kind === "work" ? b.produce : b.judge;
    const named = listed(own.map((a) => a.name));
    const { places, release, limits } = b.basis;
    const work = b.kind === "work" ? b : undefined;
    const frame = b.frame === undefined ? "- frame: none declared in the graph for this session." : `- frame: ${b.frame.name}, revision ${b.frame.revision}.`;
    // The ticket is the context the session starts from, and its rulings bind the session; the packet names them and copies no line of either (REQ-ALG-007).
    const ticket = b.ticket === undefined ? [] : [`- ticket: ${b.ticket.place}, the context this session starts from${b.ruled === true ? "; the rulings in it bind this session" : ""}.`];
    const stands = b.stands.map(stood);
    // A frame that names no term of the method gets the release by its identity alone (D104). Where it names terms
    // and the release could not be found on this machine, the packet says so and points to no section of it (D100).
    const terms = b.frame?.method ?? [];
    const sections = release?.path === undefined ? [] : terms;
    const basis = [
        `- definition: ${places.definition}`,
        release === undefined
            ? "- method release: none named in the definition file."
            : terms.length === 0
                ? `- method release: ${release.uri}, manifest sha256 ${release.manifest}.`
                : release.path === undefined
                    ? `- method release: ${release.uri}, manifest sha256 ${release.manifest}. It could not be found on this machine, so judge by this packet alone.`
                    : `- method release: ${release.uri}, manifest sha256 ${release.manifest}, installed at "${release.path}"`,
        ...sections.map((m) => `- method term ${m.term}: section "${m.section}" of ${m.file} in the method release.`)
    ];
    const results = b.result.map((r) => `- result: ${r}`);
    const checks = b.checks.map((c) => `- check "${c.name}": yes where ${c.yes}.`);
    // The checks of other assets on this one grow with the graph, so they are one line (D88, D96).
    const others = b.others.length === 0
        ? []
        : [`- checks of other assets on ${named}: ${b.others.map((c) => `check "${c.name}" of ${c.of ?? ""}: yes where ${c.yes}.`).join(" ")}`];
    const write = `- write: ${listed(b.write)}. Work in this folder only.`;
    const limit = limits?.sessions !== undefined && limits.minutes !== undefined
        ? `at most ${limits.sessions} sessions and ${limits.minutes} minutes`
        : limits?.sessions !== undefined
            ? `at most ${limits.sessions} sessions`
            : limits?.minutes !== undefined
                ? `at most ${limits.minutes} minutes`
                : undefined;
    const fenced = `- must not change: ${b.guarded.join(", ")}; nor the tickets in ${listed(places.lanes)} that were there at the start${work?.ownTicket === true ? ", but for the ticket above" : ""}.`;
    // Of the method, the packet admits the sections it names and nothing else (D103).
    const exclusions = `- do not read: the framework's installation, ${places.graph}, ${places.registry}, ${places.settings} and the event log; nor anything of the method${sections.length === 0 ? "" : " but the sections named in this packet"}.`;
    const evidence = "- evidence: the files of this folder. The event log is no evidence.";
    const run = limit === undefined ? "- run: the settings set no limit on a run." : `- run: ${limit}, as the settings set.`;
    if (b.kind === "evaluation") {
        // What each verdict means, one line each (D98).
        return [
            `# Reference-Frame Activation: ${b.vector}, evaluating session`, "",
            "## Frame", frame,
            `- evaluation: judge ${named}${b.against.length === 0 ? "" : ` against ${listed(b.against.map((a) => a.name))}`}.`,
            `- verdict: write ${b.verdict} holding exactly {"verdict": "yes"}, {"verdict": "no"} or {"verdict": "cannot"}.`,
            `- yes means: ${named} ${own.length === 1 ? "is" : "are"} what the results below say ${own.length === 1 ? "it" : "they"} must be.`,
            `- no means: ${named} ${own.length === 1 ? "goes" : "go"} back to be written again, with the findings as the reason.`,
            "- cannot means: this session could not judge, and the findings say why. It stops the run for the user.",
            `- findings: write why at ${b.findings}.`,
            "- return: the session ends, and the framework reads the verdict. It stands only for the content this session judged.",
            PROPORTION, UNCHANGED.evaluation, GAP.evaluation, "",
            "## Subject And Basis", ...b.judge.map((a) => `- judge: ${asset(a)}`), ...ticket, ...basis, "",
            "## Attention Surface", ...results, ...stands, ...(b.main ?? []).map(onMain), ...b.against.map((a) => `- against: ${asset(a)}`), exclusions, "",
            "## Actor And Authority", write, fenced,
            "- may run: any command, in this folder. What a run leaves that git does not ignore counts as a change.",
            `- decision: ${b.decision}.`, "",
            "## Evidence And Relations", ...checks, ...others, evidence, "",
            "## Stop And Change", `- time: up to ${b.minutes} minutes.`, run, "- stop: where this session cannot judge, write cannot and stop."
        ];
    }
    return [
        `# Reference-Frame Activation: ${b.vector}, working session`, "",
        "## Frame", frame,
        `- evaluation: the checks below judge what this session leaves at ${named}. Each says yes, no, or cannot where it cannot be run.`,
        "- return: the session ends, and the framework runs the checks on what it left.",
        // The session that inducts the ticket chooses what its work is (REQ-METHOD-006).
        ...(b.ownTicket ? [] : [PROPORTION, UNCHANGED.work]), GAP.work, "",
        "## Subject And Basis", ...b.produce.map((a) => `- produce: ${asset(a)}`), ...ticket, ...basis, "",
        "## Attention Surface",
        ...results,
        ...stands,
        ...b.rests.map((a) => `- rests on: ${asset(a)}`),
        // The registry grows with the graph, so it is one line (D88).
        ...(b.registry === undefined ? [] : [`- registry: ${b.registry.map((e) => `${e.name} (writes ${e.writes.length === 0 ? "no node" : listed(e.writes)}; rests on ${e.rests.length === 0 ? "nothing" : listed(e.rests)}): ${e.purpose}`).join(" ")}`]),
        // An induction bound to a stretch writes the term for it in the place of the entry the run has reached (REQ-METHOD-006).
        ...(b.stretch === undefined ? [] : [`- stretch: the run has reached the induction entry over ${b.stretch.enters} to ${b.stretch.ends} in the term the user confirmed. Write the term for the work from ${b.stretch.enters} to ${b.stretch.ends} in its place: the field term is that term with this entry alone replaced, and every other line of the ticket is as the user confirmed it.${b.confirmed === undefined ? "" : ` The ticket as the user confirmed it is the blob ${b.confirmed} in git: \`git cat-file blob ${b.confirmed}\`.`}`]),
        ...(b.found === undefined ? [] : [`- last found: ${b.found}`]),
        exclusions, "",
        "## Actor And Authority",
        write,
        fenced,
        "- commits: the framework commits every file git does not ignore. What the work or its build leaves that is no part of the product, such as compiled output, is listed in the .gitignore at the top of this folder.",
        `- decision: ${b.decision}.`, "",
        "## Evidence And Relations",
        ...checks,
        ...others,
        ...(b.judgedAgainst === undefined ? [] : [`- judged: then an evaluating session judges ${named}${b.judgedAgainst.length === 0 ? "" : ` against ${listed(b.judgedAgainst)}`}.`]),
        evidence, "",
        "## Stop And Change",
        `- attempts: ${b.attempts}, each session of up to ${b.minutes} minutes.`,
        run,
        // What the session needs reaches the user through what it printed, which the framework keeps and names (D81, D97).
        `- stop: where the work needs a change this session may not make, say what change and why in what you print, and stop without writing ${listed(b.produce.map((a) => a.place))}.`
    ];
}
