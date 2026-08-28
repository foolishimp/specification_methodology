import {
  ATOM_CLASSES,
  BUILD_TENANT_IDENTITY,
  CARRIER_BASIS_IDENTITY,
  CONSTRAINT_CLASSES,
  CROSS_CONTEXT_CLASSES,
  LATITUDE_FUNCTIONS,
  type CompactSemanticIndexConfig,
  type GtlBuildPlan,
  type ProgramRecord,
  type SemanticAddress,
  type SourceLocator,
} from "./contracts.js";
import { compareUnicodeCodeUnits, type JsonValue } from "./canonical.js";

function recordStrings(record: ProgramRecord): readonly string[] {
  const address = record.semantic_address;
  const strings = [
    address.source_key,
    address.term,
    address.bounded_context,
    address.owning_authority,
    address.governed_scope,
    ...record.source_locators.flatMap((locator) => [
      locator.member_path,
      locator.member_sha256,
      ...(locator.fragment === null ? [] : [locator.fragment]),
    ]),
  ];
  if (record.kind === "atom") strings.push(record.label);
  if (record.kind === "constraint") strings.push(record.statement);
  return strings;
}

export function encodeSemanticIndex(plan: GtlBuildPlan): CompactSemanticIndexConfig {
  const identities = plan.records
    .map((record) => record.id)
    .sort(compareUnicodeCodeUnits);
  const identityIndex = new Map(identities.map((identity, index) => [identity, index]));
  const strings = [...new Set(plan.records.flatMap(recordStrings))].sort(compareUnicodeCodeUnits);
  const stringIndex = new Map(strings.map((value, index) => [value, index]));
  const si = (value: string): number => {
    const index = stringIndex.get(value);
    if (index === undefined) throw new TypeError(`unindexed string ${value}`);
    return index;
  };
  const ii = (value: string): number => {
    const index = identityIndex.get(value);
    if (index === undefined) throw new TypeError(`unindexed identity ${value}`);
    return index;
  };
  const address = (value: SemanticAddress): JsonValue => [
    si(value.source_key),
    si(value.term),
    si(value.bounded_context),
    si(value.owning_authority),
    si(value.governed_scope),
  ];
  const locator = (value: SourceLocator): JsonValue => [
    si(value.member_path),
    si(value.member_sha256),
    value.fragment === null ? null : si(value.fragment),
  ];
  const sortedRecords = [...plan.records].sort((left, right) =>
    compareUnicodeCodeUnits(left.id, right.id),
  );
  const atoms: JsonValue[] = [];
  const edges: JsonValue[] = [];
  const constraints: JsonValue[] = [];
  for (const record of sortedRecords) {
    if (record.kind === "atom") {
      atoms.push([
        ii(record.id),
        ATOM_CLASSES.indexOf(record.atom_class),
        si(record.label),
        address(record.semantic_address),
        record.source_locators.map(locator),
      ]);
    } else if (record.kind === "edge") {
      const cross = record.cross_context === null
        ? null
        : [
          CROSS_CONTEXT_CLASSES.indexOf(record.cross_context.classification),
          ii(record.cross_context.source_context_ref),
          ii(record.cross_context.target_context_ref),
          record.cross_context.preserved_meaning_refs.map(ii),
          record.cross_context.changed_meaning_refs.map(ii),
          record.cross_context.refusal_refs.map(ii),
          record.cross_context.inverse_ref === null ? null : ii(record.cross_context.inverse_ref),
          record.cross_context.invalidation_refs.map(ii),
        ];
      edges.push([
        ii(record.id),
        address(record.semantic_address),
        ii(record.source_ref),
        ii(record.relation_kind_ref),
        ii(record.target_ref),
        record.context_ref === null ? null : ii(record.context_ref),
        record.owner_ref === null ? null : ii(record.owner_ref),
        record.scope_ref === null ? null : ii(record.scope_ref),
        cross,
        record.source_locators.map(locator),
      ]);
    } else {
      constraints.push([
        ii(record.id),
        address(record.semantic_address),
        CONSTRAINT_CLASSES.indexOf(record.constraint_class),
        si(record.statement),
        record.applies_to_refs.map(ii),
        record.context_ref === null ? null : ii(record.context_ref),
        record.owner_ref === null ? null : ii(record.owner_ref),
        record.scope_ref === null ? null : ii(record.scope_ref),
        record.declared_latitude === null
          ? null
          : [
            LATITUDE_FUNCTIONS.indexOf(record.declared_latitude.function_ref),
            ii(record.declared_latitude.decision_owner_ref),
            ii(record.declared_latitude.re_entry_ref),
          ],
        record.source_locators.map(locator),
      ]);
    }
  }
  return {
    k: "stdo.programmatic_semantic_index",
    v: 1,
    m: [
      plan.source_stdo.release_uri,
      plan.source_stdo.installed_manifest_sha256,
      plan.source_stdo.standards_member_set_sha256,
      plan.what_member_set_identity,
      BUILD_TENANT_IDENTITY,
      CARRIER_BASIS_IDENTITY,
      plan.representation_profile_identity,
      plan.representation_profile_sha256,
      plan.frame_basis_identity,
      plan.frame_basis_sha256,
      plan.semantic_selection_ledger_identity,
      plan.semantic_selection_ledger_sha256,
    ],
    l: {
      m: ["source_uri", "manifest_sha256", "member_set_sha256", "what_sha256", "tenant", "carrier", "profile", "profile_sha256", "frame_basis", "frame_basis_sha256", "selection", "selection_sha256"],
      z: ["source_key", "term", "context", "authority", "scope"],
      o: ["member_path", "member_sha256", "fragment"],
      a: ["id", "class", "label", "address", "locators"],
      e: ["id", "address", "source", "relation", "target", "context", "owner", "scope", "cross_context", "locators"],
      c: ["id", "address", "class", "statement", "applies_to", "context", "owner", "scope", "latitude", "locators"],
      x: ["class", "source_context", "target_context", "preserved", "changed", "refusals", "inverse", "invalidations"],
      y: ["function", "decision_owner", "re_entry"],
      ak: ATOM_CLASSES,
      ck: CONSTRAINT_CLASSES,
      xk: CROSS_CONTEXT_CLASSES,
      fk: LATITUDE_FUNCTIONS,
    },
    s: strings,
    i: identities,
    a: atoms,
    e: edges,
    c: constraints,
  };
}
