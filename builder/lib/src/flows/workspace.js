/**
 * The workspace as the flows see it: where the framework keeps its files, the
 * written forms of those files, the governing graph as it stands on main, the
 * settings, and the board. Every place is a path relative to a checkout.
 *
 * Under git, travelling with a branch: the definition file, the settings, the
 * graph and its registry, and the tickets, whose framework's part holds the
 * checklist, the resolutions and the rulings (D202). In the workspace and
 * outside the history, under `.stdo-builder/local/`: the event log, what the
 * checks found, the briefs, what the sessions printed, the holds, git's index
 * of identities and the tickets' checkouts.
 *
 * The settings name, for each agent, the fields of what it prints that report
 * a session's cost and its calls, and the cost's unit (D91, D102). The definition file names the method
 * release by its identity (D89). The settings also record which release of
 * this product builds the governed product, read as it stands, and what is
 * running is read from the manifest at the place the library gives
 * (REQ-FLOW-010, D197).
 *
 * Every command but set-up begins with `open`: the folder the user named is
 * there, lies in a repository, at its top or below it (D201), is set up, and
 * is on a line
 * (design, CALCULUS.md section 5).
 *
 * @uses C14 C5 C6 C3 C4 C13 C16 C17 H5 H1
 * @is REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-004 REQ-FLOW-007 REQ-FLOW-010 REQ-INTERFACE-002 REQ-ALG-012
 */
import { decide, each, end, using } from "../kit/calculus.js";
import { fieldsOf, valuesOf, withoutField } from "../kit/field_lines.js";
import { anything, count, list, literal, names, oneOf, optional, read, record, text, write, writeLine } from "../kit/lossless_encoding.js";
import { namedPlaces, pathsOf } from "../graph/terms.js";
import { covers } from "../kit/place_containment.js";
import { nodesOf, vectorsOf } from "../graph/walk.js";
import { writeDeclaration } from "../graph/written.js";
import { declaration, FRAMEWORK, lineText, readLine } from "../algorithms/facts.js";
import { well_formed } from "../algorithms/well_formed.js";
import { Files } from "../services/files.js";
import { Git } from "../services/git.js";
export const OWN = ".stdo-builder";
export const LOCAL = `${OWN}/local`;
export const PLACES = {
    settings: `${OWN}/settings.json`,
    graph: `${OWN}/graph.json`,
    registry: `${OWN}/registry.json`,
    ignore: `${OWN}/.gitignore`,
    frame: "specification/REFERENCE_FRAME_BASIS.md",
    log: `${LOCAL}/events.log`,
    found: `${LOCAL}/found`,
    briefs: `${LOCAL}/briefs`,
    /** What the last session of each vector and kind printed, in the ticket's checkout (D81). */
    printed: `${LOCAL}/printed`,
    holds: `${LOCAL}/holds`,
    index: `${LOCAL}/identity.index`,
    /** Where a commit that cannot stage in the folder's own index stages, in the folder committed (C13, D201). */
    commitIndex: `${LOCAL}/commit.index`,
    checkouts: `${LOCAL}/checkouts`,
    agentFiles: ["AGENTS.md", "CLAUDE.md"],
    lanes: {
        backlog: ".ai-workspace/tickets/backlog",
        active: ".ai-workspace/tickets/active",
        done: ".ai-workspace/tickets/completed"
    }
};
/** What git keeps out of the history: the framework's local folder. */
export const IGNORE = "local/\n";
export const at = (folder, path) => `${folder}/${path}`;
/** The framework's prefix: every ticket's branch lies below it. */
export const LINES = "stdo";
/** A ticket's branch, and where its checkout is. */
export const lineOf = (ticket) => `${LINES}/${ticket}`;
/** Where git makes a ticket's checkout in the workspace's own folder. */
export const checkoutTop = (ticket) => `${PLACES.checkouts}/${ticket}`;
/**
 * Where the workspace lies in a ticket's checkout, from the workspace's own
 * folder: the path the user opens it by. `within` is the workspace's folder
 * from the top of its repository, empty at the top; the checkout holds that
 * folder alone, at that place in it (D201).
 */
export const checkoutPlace = (ticket, within) => `${checkoutTop(ticket)}${within === "" ? "" : `/${within}`}`;
export const checkoutOf = (root, ticket, within) => at(root, checkoutPlace(ticket, within));
/** A path of a ticket's checkout as the user opens it from the workspace's folder; a path of main's, where there is no ticket, as it is. */
export const seenFrom = (ticket, path, within) => (ticket === undefined ? path : `${checkoutPlace(ticket, within)}/${path}`);
export const ticketPath = (lane, ticket) => `${PLACES.lanes[lane]}/${ticket}.md`;
export const holdOf = (root, ticket) => at(root, `${PLACES.holds}/${ticket}`);
export const foundPath = (vector) => `${PLACES.found}/${vector}.md`;
export const printedPath = (vector, kind) => `${PLACES.printed}/${vector}.${kind}.txt`;
export const SettingsShape = record({
    definition: text,
    builder: optional(anything),
    agents: names(list(text)),
    work: text,
    evaluation: text,
    vectors: optional(names(record({ work: optional(text), evaluation: optional(text) }))),
    limits: optional(record({ sessions: optional(count), minutes: optional(count) })),
    reports: optional(names(record({ cost: optional(text), calls: optional(text), unit: optional(text) })))
});
/** The tools of the default agent's session: the agent's own, for reading, writing and running commands, and none that starts another agent (D198). */
const TOOLS = "Bash,Read,Write,Edit,Glob,Grep";
/**
 * The settings set-up writes, which work as they are (REQ-FLOW-002 step 5).
 * The default command makes only the tools it names available to the session
 * (`--tools`), so one session is one start of the agent, and lets the same
 * tools run without asking, since no one answers a session's question
 * (`--allowedTools`). The user owns the command and may change it (D198).
 */
export const defaultSettings = (definition, builder) => ({
    definition,
    builder,
    agents: {
        claude: [
            "claude",
            "-p",
            "Read the activation packet at {brief}, and do the work it binds in this folder.",
            "--permission-mode",
            "acceptEdits",
            "--tools",
            TOOLS,
            "--allowedTools",
            TOOLS,
            "--output-format",
            "json"
        ]
    },
    work: "claude",
    evaluation: "claude",
    // The agent reports its cost in US dollars, as its field's name says (D102).
    reports: { claude: { cost: "total_cost_usd", calls: "num_turns", unit: "USD" } }
});
// ---- The release of this product that builds the governed product (REQ-FLOW-010)
/** Said of a build of this product that is no release, in the record and of what is running (D197). */
export const UNRELEASED = "unreleased build";
const BuilderShape = oneOf([literal(UNRELEASED), record({ version: text, manifest_sha256: text })]);
/** The field of a value read as any value, where it is an object that has it. */
const fieldOf = (value, name) => typeof value === "object" && value !== null && !Array.isArray(value) ? new Map(Object.entries(value)).get(name) : undefined;
/** The record the settings' text holds, read as it stands: none where the text does not read as data or holds no record (D197). */
export const recordedIn = (settings) => {
    const got = read(anything, settings);
    const value = "value" in got ? fieldOf(got.value, "builder") : undefined;
    if (value === undefined)
        return { none: true };
    const builder = read(BuilderShape, write(anything, value));
    return "value" in builder ? { builder: builder.value } : { written: writeLine(anything, value) };
};
/** The release a record names, in words for the event log: its version and the sha256 of its manifest, `unreleased build`, or that none is recorded (REQ-FLOW-007, D205). */
export const releaseWords = (recorded) => "builder" in recorded ? (typeof recorded.builder === "string" ? recorded.builder : `${recorded.builder.version} ${recorded.builder.manifest_sha256}`) : "none" in recorded ? "none recorded" : recorded.written;
/** Whether two are the same release, or both a build that is no release: compared in their one form (D197). */
export const sameBuilder = (a, b) => typeof a === "string" || typeof b === "string" ? a === b : a.version === b.version && a.manifest_sha256 === b.manifest_sha256;
/** Whether what is recorded is what is running, so a run is not refused for its release (REQ-FLOW-010). */
export const builds = (recorded, running) => "builder" in recorded && sameBuilder(recorded.builder, running);
/** The profile and the product a manifest of a release of this product names (REQ-INTERFACE-004). */
const PROFILE = "stdo-builder.release-package/1";
const PRODUCT = "stdo-builder";
/**
 * What is running, from the manifest at the place the library gives: the
 * release it names, where a manifest of a release of this product is there,
 * with the sha256 of its bytes (C1); an unreleased build where none is (D197).
 */
export const running = (manifest) => using(Files, (files) => decide(files.hashed(manifest), (got) => {
    const parsed = got === undefined ? undefined : read(anything, got.text);
    const value = parsed !== undefined && "value" in parsed ? parsed.value : undefined;
    const version = fieldOf(value, "version");
    return end(got !== undefined && fieldOf(value, "profile") === PROFILE && fieldOf(value, "product") === PRODUCT && typeof version === "string"
        ? { version, manifest_sha256: got.sha256 }
        : UNRELEASED);
}));
/** The agent the settings give a vector's session of this kind, with the fields that report its cost and its calls, where they name any. */
export function agentFor(settings, vector, kind) {
    const name = settings.vectors?.[vector]?.[kind] ?? settings[kind];
    const reports = settings.reports?.[name];
    return { name, command: settings.agents[name] ?? [name], ...(reports === undefined ? {} : { reports }) };
}
/** The fields of a text that reads as one object, read as any value (C14); undefined for any other text. */
const objectIn = (written) => {
    const got = read(anything, written);
    return "value" in got && typeof got.value === "object" && got.value !== null && !Array.isArray(got.value) ? new Map(Object.entries(got.value)) : undefined;
};
/**
 * What a session's agent reported of its cost and its calls, from what it
 * printed, read as any value (C14): the cost as the field's number or text, the
 * calls as a whole number at or above zero. The output is read as one object,
 * or else its last line that reads as one, since what an agent prints holds its
 * errors too. Output with no object, or one that lacks a field, reports nothing
 * of it (D91). A cost read is given with the unit the settings name (D102).
 */
export function reported(reports, printed) {
    const value = reports === undefined
        ? new Map()
        : objectIn(printed) ?? printed.split("\n").filter((line) => line.trim().startsWith("{")).map(objectIn).findLast((m) => m !== undefined) ?? new Map();
    const cost = reports?.cost === undefined ? undefined : value.get(reports.cost);
    const calls = reports?.calls === undefined ? undefined : value.get(reports.calls);
    const costed = typeof cost === "number" && Number.isFinite(cost) ? String(cost) : typeof cost === "string" ? cost : undefined;
    return {
        ...(costed === undefined ? {} : { cost: costed, ...(reports?.unit === undefined ? {} : { unit: reports.unit }) }),
        ...(typeof calls === "number" && Number.isInteger(calls) && calls >= 0 ? { calls } : {})
    };
}
// ---- The definition file
const Ref = record({ basis: text, uri: text });
/** The definition file the method requires, in the one form set-up writes it. */
export const DefinitionShape = record({
    $schema: text,
    kind: literal("stdo.product-definition"),
    product: record({ definition_id: text, name: text, source_project: text, bounded_context: record({ id: text, definition: text }) }),
    constitution: record({
        stdo: record({ source: record({ repository: text }), selector: text, basis: record({ uri: text, manifest_sha256: text }) }),
        additional_authorities: list(text),
        entrypoints: list(Ref),
        agent_bootstrap: record({ entrypoint: text, targets: list(text) })
    }),
    local_constitution: record({ axioms: list(text), overrides: list(text), disambiguations: list(text) }),
    reference_frame_bases: list(record({ uri: text, authority: list(text), applies_to: list(text) })),
    what: record({ intent: text, product: text, specification: list(text) }),
    how: record({ common: list(text), build_tenants: list(record({ id: text, root: text, design: list(text), implementation: list(text) })) }),
    ticketing: record({
        goals: text,
        tickets: record({ root: text, lanes: record({ backlog: text, active: text, completed: text }) }),
        comments: record({ root: text }),
        sprints: optional(record({ root: text }))
    }),
    composition: list(text)
});
// ---- Verdicts and the identities they were given on
/** A verdict says yes, no, or that the evaluation cannot judge (D90). */
export const VerdictShape = record({ verdict: oneOf([literal("yes"), literal("no"), literal("cannot")]) });
// ---- The framework's part of a ticket (D202)
/** The framework's lines of a ticket's text, read back in order; a line of another form is passed over. */
export const ticketLines = (written) => valuesOf(written, FRAMEWORK).flatMap((words) => {
    const l = readLine(words);
    return l === undefined ? [] : [l];
});
/** A ticket's text without the framework's part: what the ticket's identities are of (REQ-ALG-004). */
export const userPart = (written) => withoutField(written, FRAMEWORK);
/** The text of the framework's lines of a ticket, as written, in order: what `trespass` compares (REQ-ALG-008). */
export const frameworkPart = (written) => valuesOf(written, FRAMEWORK).join("\n");
/** Adds lines to the framework's part of the ticket at `path` in `folder`, at its end. */
export const addLines = (folder, path, lines) => using(Files, (files) => decide(files.read(at(folder, path)), (written) => {
    const text = written ?? "";
    const added = lines.map((l) => `- ${FRAMEWORK}: ${lineText(l)}\n`).join("");
    return lines.length === 0 ? end(undefined) : files.write(at(folder, path), `${text}${text === "" || text.endsWith("\n") ? "" : "\n"}${added}`);
}));
const refusedAt = (refused, folder) => ({ refused, folder });
/**
 * `open` (design, CALCULUS.md section 5): reads the folder the user named and
 * decides whether it is there, lies in a repository, is set up, and is on a
 * line. It gives the folder with every link followed, the line it is on and
 * its place from the repository's top, or why it is refused. A folder below
 * the top of a larger repository is a workspace where it is set up (D201).
 */
export const open = (folder) => using(Files, (files) => using(Git, (git) => decide(files.exists(folder), (there) => !there
    ? end(refusedAt("absent", folder))
    : decide(files.real(folder), (root) => decide(git.topOf(root), (top) => decide(top === undefined ? end(undefined) : files.real(top), (realTop) => decide(files.exists(at(root, PLACES.settings)), (setUp) => realTop === undefined || !covers(realTop, root) || !setUp
        ? end(refusedAt("not set up", root))
        : decide(git.currentLine(root), (main) => end(main === undefined ? refusedAt("no line", root) : { root, main, within: realTop === root ? "" : root.slice(realTop.length + 1) })))))))));
/** The settings and the governing graph as main has them, with the identity of what each node declares of itself (D168), or why they cannot be used. */
export const openWorkspace = (root, main, within) => using(Files, (files) => decide(each([PLACES.settings, PLACES.graph, PLACES.registry], (place) => files.read(at(root, place))), ([settingsText, graphText, registryText]) => {
    if (settingsText === undefined || graphText === undefined || registryText === undefined) {
        return end({ refused: [{ rule: "terms", where: OWN, says: "the workspace is not set up: the settings, the graph or the registry is missing" }] });
    }
    const settings = read(SettingsShape, settingsText);
    if ("refused" in settings) {
        return end({ refused: settings.refused.map((r) => ({ rule: "terms", where: `${PLACES.settings} ${r.at.join(".")}`, says: r.says })) });
    }
    return decide(files.read(at(root, settings.value.definition)), (definition) => {
        const verdict = well_formed(graphText, registryText, placesNamedIn(definition ?? ""));
        const release = releaseNamedIn(definition ?? "");
        if ("no" in verdict)
            return end({ refused: verdict.no });
        const graph = verdict.yes;
        return using(Git, (git) => decide(each(declarationsOf(graph), ([key, written]) => decide(git.identityOfText(root, written), (id) => end([key, id]))), (declared) => decide(each([[PLACES.graph, graphText], [PLACES.registry, registryText], [settings.value.definition, definition ?? ""]], ([path, text]) => decide(git.identityOfText(root, text), (id) => end([path, id]))), (basis) => end({ root, main, within, settings: settings.value, graph, declared: new Map(declared), basis: new Map(basis), ...(release === undefined ? {} : { release }) }))));
    });
}));
/**
 * What each node that declares what accepts it declares of itself, and what
 * the first vector declares of the ticket, by `declaration`, in their one
 * written form: a record is kept only there, so only those are read (D168,
 * D175).
 */
export const declarationsOf = (graph) => [
    ...nodesOf(graph.graph, graph.registry).filter((n) => (n.accepted ?? []).length > 0).map((n) => [declaration(n.name), writeDeclaration(n)]),
    ...graph.graph.vectors.filter((v) => v.first === true)
        .map((v) => [declaration(v.name), writeDeclaration({ result: v.result ?? [], ...(v.decision === undefined ? {} : { accepted: ["decision"] }) })])
];
export const nodes = (ws) => nodesOf(ws.graph.graph, ws.graph.registry);
export const vectors = (ws) => vectorsOf(ws.graph.graph, ws.graph.registry);
/** The paths of each node's asset, by the node's name. */
export const placesOf = (ws) => new Map(nodes(ws).map((n) => [n.name, pathsOf(n)]));
/**
 * The paths the definition file gives each name a place may be (REQ-GRAPH-003); none where it cannot be read.
 * The file is the method's, and the method's own tool checks its form: any definition it accepts is read here (D73).
 */
export const placesNamedIn = (definition) => {
    const got = read(anything, definition);
    return "value" in got ? namedPlaces(got.value) : new Map();
};
/** The method release the definition file selects: `constitution.stdo.basis`, its `uri` and `manifest_sha256`, read as any value (D73, D89); none where it names none. */
const releaseNamedIn = (definition) => {
    const got = read(anything, definition);
    const basis = fieldOf(fieldOf(fieldOf("value" in got ? got.value : undefined, "constitution"), "stdo"), "basis");
    const uri = fieldOf(basis, "uri");
    const manifest = fieldOf(basis, "manifest_sha256");
    return typeof uri === "string" && typeof manifest === "string" ? { uri, manifest } : undefined;
};
/** The places `trespass` protects that are the framework's and the method's, not the graph's: those of its own files that git holds. */
export const frameworkPlaces = (ws) => ({
    folder: OWN,
    definition: ws.settings.definition,
    settings: PLACES.settings,
    graph: PLACES.graph,
    registry: PLACES.registry,
    own: [PLACES.ignore, PLACES.frame],
    lanes: Object.values(PLACES.lanes)
});
/** Every place `trespass` can protect, which the graph or the definition file names: the places whose files a trespass snapshot holds. */
export const watchedPlaces = (ws) => {
    const p = frameworkPlaces(ws);
    return [
        p.definition, p.settings, p.graph, p.registry, ...p.own, ...p.lanes,
        ...nodes(ws).flatMap(pathsOf),
        ...vectors(ws).flatMap((v) => (v.evaluation === undefined ? [] : [v.evaluation.verdict]))
    ];
};
// ---- The board
/** The tickets of one lane of a checkout, by name, each read for whether it is the simplest ticket. */
const laneOf = (folder, lane) => using(Files, (files) => decide(files.list(at(folder, PLACES.lanes[lane])), (listed) => each(listed.filter((file) => file.endsWith(".md")).map((file) => file.slice(0, -".md".length)), (name) => decide(files.read(at(folder, ticketPath(lane, name))), (written) => end(fieldsOf(written ?? "").get("simplest") === "yes" ? { name, simplest: true } : { name })))));
/** The three ticket lanes as a checkout has them; for the board, main's. */
export const boardOf = (folder) => decide(each(["backlog", "active", "done"], (lane) => laneOf(folder, lane)), (lanes) => end({ backlog: lanes[0] ?? [], active: lanes[1] ?? [], done: lanes[2] ?? [] }));
/** The lane a ticket lies in, in a checkout, or undefined. */
export const laneOfTicket = (board, ticket) => board.active.some((t) => t.name === ticket) ? "active" : board.backlog.some((t) => t.name === ticket) ? "backlog" : board.done.some((t) => t.name === ticket) ? "done" : undefined;
