module
public import AC.GateProof
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
def str0 : String := "urn:a-c:toy:object:c"

def str1 : String := "urn:a-c:toy:context"

def str2 : String := "urn:a-c:toy:author"

def str3 : String := "[\"urn:a-c:toy:scope\"]"

def str4 : String := "urn:a-c:toy:basis"

def str5 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:object:c\",\"owner\":\"urn:a-c:toy:author\",\"scope\":[\"urn:a-c:toy:scope\"],\"sort\":\"urn:a-c:toy:sort:statement\",\"value\":{\"arguments\":[],\"text\":\"C is a provenance-only discovery lead; acquiring A does not require C.\"}}"

def record0 : Record := { key := 0, family := .objects, identity := str0, context := str1, owner := str2, scope := str3, basis := str4, payload := str5 }

def str6 : String := "urn:a-c:toy:object:a"

def str7 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:object:a\",\"owner\":\"urn:a-c:toy:author\",\"scope\":[\"urn:a-c:toy:scope\"],\"sort\":\"urn:a-c:toy:sort:statement\",\"value\":{\"arguments\":[\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:b\"],\"text\":\"A requires B. A may be restated; its unresolved reading stays visible.\"}}"

def record1 : Record := { key := 1, family := .objects, identity := str6, context := str1, owner := str2, scope := str3, basis := str4, payload := str7 }

def str8 : String := "urn:a-c:toy:object:b"

def str9 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:object:b\",\"owner\":\"urn:a-c:toy:author\",\"scope\":[\"urn:a-c:toy:scope\"],\"sort\":\"urn:a-c:toy:sort:statement\",\"value\":{\"arguments\":[],\"text\":\"B also requires A, creating a finite cycle.\"}}"

def record2 : Record := { key := 2, family := .objects, identity := str8, context := str1, owner := str2, scope := str3, basis := str4, payload := str9 }

def str10 : String := "urn:a-c:toy:relation:parallel:one"

def str11 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:relation:parallel:one\",\"kind\":\"urn:a-c:toy:relation-kind:requires\",\"owner\":\"urn:a-c:toy:author\",\"qualifiers\":{\"arguments\":[\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:a\"],\"role\":\"required\"},\"scope\":[\"urn:a-c:toy:scope\"],\"source\":\"urn:a-c:toy:object:a\",\"target\":\"urn:a-c:toy:object:b\"}"

def record3 : Record := { key := 3, family := .relations, identity := str10, context := str1, owner := str2, scope := str3, basis := str4, payload := str11 }

def str12 : String := "urn:a-c:toy:relation:parallel:two"

def str13 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:relation:parallel:two\",\"kind\":\"urn:a-c:toy:relation-kind:requires\",\"owner\":\"urn:a-c:toy:author\",\"qualifiers\":{\"arguments\":[\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:a\"],\"role\":\"required\"},\"scope\":[\"urn:a-c:toy:scope\"],\"source\":\"urn:a-c:toy:object:a\",\"target\":\"urn:a-c:toy:object:b\"}"

def record4 : Record := { key := 4, family := .relations, identity := str12, context := str1, owner := str2, scope := str3, basis := str4, payload := str13 }

def str14 : String := "urn:a-c:toy:relation:reverse"

def str15 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:relation:reverse\",\"kind\":\"urn:a-c:toy:relation-kind:requires\",\"owner\":\"urn:a-c:toy:author\",\"qualifiers\":{\"arguments\":[\"urn:a-c:toy:object:b\",\"urn:a-c:toy:object:b\"],\"role\":\"required\"},\"scope\":[\"urn:a-c:toy:scope\"],\"source\":\"urn:a-c:toy:object:b\",\"target\":\"urn:a-c:toy:object:a\"}"

def record5 : Record := { key := 5, family := .relations, identity := str14, context := str1, owner := str2, scope := str3, basis := str4, payload := str15 }

def str16 : String := "urn:a-c:toy:relation:self"

def str17 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:relation:self\",\"kind\":\"urn:a-c:toy:relation-kind:requires\",\"owner\":\"urn:a-c:toy:author\",\"qualifiers\":{\"arguments\":[\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:a\"],\"role\":\"required\"},\"scope\":[\"urn:a-c:toy:scope\"],\"source\":\"urn:a-c:toy:object:a\",\"target\":\"urn:a-c:toy:object:a\"}"

def record6 : Record := { key := 6, family := .relations, identity := str16, context := str1, owner := str2, scope := str3, basis := str4, payload := str17 }

def str18 : String := "urn:a-c:toy:relation:discovery"

def str19 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:relation:discovery\",\"kind\":\"urn:a-c:toy:relation-kind:discovery\",\"owner\":\"urn:a-c:toy:author\",\"qualifiers\":{\"arguments\":[\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:a\"],\"role\":\"discovery\"},\"scope\":[\"urn:a-c:toy:scope\"],\"source\":\"urn:a-c:toy:object:a\",\"target\":\"urn:a-c:toy:object:c\"}"

def record7 : Record := { key := 7, family := .relations, identity := str18, context := str1, owner := str2, scope := str3, basis := str4, payload := str19 }

def str20 : String := "urn:a-c:toy:constraint:review"

def str21 : String := "{\"applies_to\":[\"urn:a-c:toy:object:a\"],\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:constraint:review\",\"judgment_kind\":\"urn:a-c:toy:judgment-kind:review\",\"kind\":\"urn:a-c:toy:constraint-kind:review\",\"latitude_ref\":[\"urn:a-c:toy:latitude:wording\"],\"owner\":\"urn:a-c:toy:author\",\"predicate\":{\"arguments\":[\"urn:a-c:toy:object:a\"],\"operator\":\"requires-external-review\"},\"refusal\":\"urn:a-c:toy:stop:refusal\",\"scope\":[\"urn:a-c:toy:scope\"]}"

def record8 : Record := { key := 8, family := .constraints, identity := str20, context := str1, owner := str2, scope := str3, basis := str4, payload := str21 }

def str22 : String := "urn:a-c:toy:latitude:wording"

def str23 : String := "{\"allowed_variation\":[\"Restate words while preserving the declared dependency.\"],\"applies_to\":[\"urn:a-c:toy:object:a\"],\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"forbidden_variation\":[\"Remove the dependency or unresolved reading.\"],\"id\":\"urn:a-c:toy:latitude:wording\",\"invalidation\":\"urn:a-c:toy:invalidation\",\"owner\":\"urn:a-c:toy:author\",\"scope\":[\"urn:a-c:toy:scope\"]}"

def record9 : Record := { key := 9, family := .latitude, identity := str22, context := str1, owner := str2, scope := str3, basis := str4, payload := str23 }

def str24 : String := "urn:a-c:toy:residual:reading"

def str25 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"consequence\":\"Semantic acceptance remains open.\",\"context\":\"urn:a-c:toy:context\",\"id\":\"urn:a-c:toy:residual:reading\",\"invalidation\":\"urn:a-c:toy:invalidation\",\"kind\":\"urn:a-c:toy:residual-kind:uncertainty\",\"owner\":\"urn:a-c:toy:author\",\"re_entry\":[\"urn:a-c:toy:traversal:review\"],\"scope\":[\"urn:a-c:toy:scope\"],\"subject\":\"urn:a-c:toy:object:a\",\"uncertainty\":\"Whether A's wording preserves every material reading is unassessed.\"}"

def record10 : Record := { key := 10, family := .residuals, identity := str24, context := str1, owner := str2, scope := str3, basis := str4, payload := str25 }

def str26 : String := "urn:a-c:toy:traversal:review"

def str27 : String := "{\"authority\":\"urn:a-c:toy:authority\",\"basis\":\"urn:a-c:toy:basis\",\"codomain\":\"urn:a-c:toy:domain:judgment\",\"context\":\"urn:a-c:toy:context\",\"domain\":\"urn:a-c:toy:domain:proposal\",\"evidence\":[\"urn:a-c:toy:object:c\"],\"id\":\"urn:a-c:toy:traversal:review\",\"owner\":\"urn:a-c:toy:author\",\"postconditions\":[],\"preconditions\":[\"urn:a-c:toy:constraint:review\"],\"provenance\":[\"urn:a-c:toy:object:c\"],\"scope\":[\"urn:a-c:toy:scope\"],\"stop_states\":[\"urn:a-c:toy:stop:refusal\"]}"

def record11 : Record := { key := 11, family := .traversals, identity := str26, context := str1, owner := str2, scope := str3, basis := str4, payload := str27 }

def str28 : String := "urn:a-c:toy:transformation:inert"

def str29 : String := "{\"basis\":\"urn:a-c:toy:basis\",\"codomain_model\":\"urn:a-c:toy:model:external-after\",\"context\":\"urn:a-c:toy:context\",\"domain_model\":\"urn:a-c:toy:model:external-before\",\"evidence\":[],\"external_introduced\":[],\"external_preserved\":[],\"external_removed\":[],\"external_resolution_witnesses\":[],\"id\":\"urn:a-c:toy:transformation:inert\",\"introduced\":[],\"invalidation\":\"urn:a-c:toy:invalidation\",\"operation_authority\":\"urn:a-c:toy:authority\",\"owner\":\"urn:a-c:toy:author\",\"preconditions\":[],\"preservation_relation\":\"urn:a-c:toy:preservation-law\",\"preserved\":[\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:b\",\"urn:a-c:toy:object:c\"],\"provenance\":[],\"re_entry\":[\"urn:a-c:toy:traversal:review\"],\"removed\":[],\"residuals\":[\"urn:a-c:toy:residual:reading\"],\"scope\":[\"urn:a-c:toy:scope\"],\"stop_states\":[\"urn:a-c:toy:stop:refusal\"],\"traversal\":\"urn:a-c:toy:traversal:review\"}"

def record12 : Record := { key := 12, family := .transformations, identity := str28, context := str1, owner := str2, scope := str3, basis := str4, payload := str29 }

def str30 : String := "urn:a-c:toy:judgment:unassessed"

def str31 : String := "{\"authority\":\"urn:a-c:toy:authority\",\"basis\":\"urn:a-c:toy:basis\",\"context\":\"urn:a-c:toy:context\",\"decided_at\":\"2026-10-15T00:00:00Z\",\"decision\":\"indeterminate\",\"evaluator\":\"urn:a-c:toy:author\",\"evidence\":[\"urn:a-c:toy:evidence:authored-fixture\"],\"id\":\"urn:a-c:toy:judgment:unassessed\",\"kind\":\"urn:a-c:toy:judgment-kind:review\",\"owner\":\"urn:a-c:toy:author\",\"provenance\":[\"urn:a-c:toy:evidence:authored-fixture\"],\"scope\":[\"urn:a-c:toy:scope\"],\"subject\":\"urn:a-c:toy:object:a\",\"subject_digest\":\"4ca55007b54e1b60d33aa0f01695eae35be44fcb7022630d3533e8536066b6fc\"}"

def record13 : Record := { key := 13, family := .judgments, identity := str30, context := str1, owner := str2, scope := str3, basis := str4, payload := str31 }

def records0 : List Record := [
record0,
record1,
record2,
record3,
record4,
record5,
record6,
record7,
record8,
record9,
record10,
record11,
record12,
record13
]

def records : List Record := [records0].flatten

def nameTable : Array String := #[str0, str6, str8, str10, str12, str14, str16, str18, str20, str22, str24, str26, str28, str30]

def lookupName (i : Nat) : String := nameTable[i]?.getD ""

def nameOrder : List Nat := [8, 13, 9, 1, 2, 0, 7, 3, 4, 5, 6, 10, 12, 11]

def str32 : String := "applies_to"

def str33 : String := "urn:a-c:toy:reference-domain:declared"

def str34 : String := "basis"

def str35 : String := "context"

def str36 : String := "judgment_kind"

def str37 : String := "urn:a-c:toy:judgment-kind:review"

def str38 : String := "kind"

def str39 : String := "urn:a-c:toy:constraint-kind:review"

def str40 : String := "latitude_ref"

def str41 : String := "owner"

def str42 : String := "predicate"

def str43 : String := "arguments"

def str44 : String := "refusal"

def str45 : String := "urn:a-c:toy:stop:refusal"

def str46 : String := "scope"

def str47 : String := "urn:a-c:toy:scope"

def str48 : String := "authority"

def str49 : String := "urn:a-c:toy:authority"

def str50 : String := "evaluator"

def str51 : String := "evidence"

def str52 : String := "urn:a-c:toy:evidence:authored-fixture"

def str53 : String := "provenance"

def str54 : String := "subject"

def str55 : String := "invalidation"

def str56 : String := "urn:a-c:toy:invalidation"

def str57 : String := "sort"

def str58 : String := "urn:a-c:toy:sort:statement"

def str59 : String := "value"

def str60 : String := "urn:a-c:toy:relation-kind:discovery"

def str61 : String := "qualifiers"

def str62 : String := "source"

def str63 : String := "target"

def str64 : String := "urn:a-c:toy:relation-kind:requires"

def str65 : String := "urn:a-c:toy:residual-kind:uncertainty"

def str66 : String := "re_entry"

def str67 : String := "codomain_model"

def str68 : String := "urn:a-c:toy:model:external-after"

def str69 : String := "domain_model"

def str70 : String := "urn:a-c:toy:model:external-before"

def str71 : String := "operation_authority"

def str72 : String := "preservation_relation"

def str73 : String := "urn:a-c:toy:preservation-law"

def str74 : String := "preserved"

def str75 : String := "residuals"

def str76 : String := "stop_states"

def str77 : String := "traversal"

def str78 : String := "codomain"

def str79 : String := "urn:a-c:toy:domain:judgment"

def str80 : String := "domain"

def str81 : String := "urn:a-c:toy:domain:proposal"

def str82 : String := "preconditions"

def references0 : List Reference := [
{ owner := 8, path := [.field str32, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 8, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 8, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 8, path := [.field str36], target := .external str37, governing := false, domain := str33 },
{ owner := 8, path := [.field str38], target := .external str39, governing := false, domain := str33 },
{ owner := 8, path := [.field str40, .index 0], target := .localRecord 9, governing := true, domain := str33 },
{ owner := 8, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 8, path := [.field str42, .field str43, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 8, path := [.field str44], target := .external str45, governing := false, domain := str33 },
{ owner := 8, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 13, path := [.field str48], target := .external str49, governing := false, domain := str33 },
{ owner := 13, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 13, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 13, path := [.field str50], target := .external str2, governing := false, domain := str33 },
{ owner := 13, path := [.field str51, .index 0], target := .external str52, governing := false, domain := str33 },
{ owner := 13, path := [.field str38], target := .external str37, governing := false, domain := str33 },
{ owner := 13, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 13, path := [.field str53, .index 0], target := .external str52, governing := false, domain := str33 },
{ owner := 13, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 13, path := [.field str54], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 9, path := [.field str32, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 9, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 9, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 9, path := [.field str55], target := .external str56, governing := false, domain := str33 },
{ owner := 9, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 9, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 1, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 1, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 1, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 1, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 1, path := [.field str57], target := .external str58, governing := false, domain := str33 },
{ owner := 1, path := [.field str59, .field str43, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 1, path := [.field str59, .field str43, .index 1], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 1, path := [.field str59, .field str43, .index 2], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 2, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 2, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 2, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 2, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 2, path := [.field str57], target := .external str58, governing := false, domain := str33 },
{ owner := 0, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 0, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 0, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 0, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 0, path := [.field str57], target := .external str58, governing := false, domain := str33 },
{ owner := 7, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 7, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 7, path := [.field str38], target := .external str60, governing := false, domain := str33 },
{ owner := 7, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 7, path := [.field str61, .field str43, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 7, path := [.field str61, .field str43, .index 1], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 7, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 7, path := [.field str62], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 7, path := [.field str63], target := .localRecord 0, governing := true, domain := str33 },
{ owner := 3, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 3, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 3, path := [.field str38], target := .external str64, governing := false, domain := str33 },
{ owner := 3, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 3, path := [.field str61, .field str43, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 3, path := [.field str61, .field str43, .index 1], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 3, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 3, path := [.field str62], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 3, path := [.field str63], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 4, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 4, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 4, path := [.field str38], target := .external str64, governing := false, domain := str33 },
{ owner := 4, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 4, path := [.field str61, .field str43, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 4, path := [.field str61, .field str43, .index 1], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 4, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 4, path := [.field str62], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 4, path := [.field str63], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 5, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 5, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 5, path := [.field str38], target := .external str64, governing := false, domain := str33 },
{ owner := 5, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 5, path := [.field str61, .field str43, .index 0], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 5, path := [.field str61, .field str43, .index 1], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 5, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 5, path := [.field str62], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 5, path := [.field str63], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 6, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 6, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 6, path := [.field str38], target := .external str64, governing := false, domain := str33 },
{ owner := 6, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 6, path := [.field str61, .field str43, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 6, path := [.field str61, .field str43, .index 1], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 6, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 6, path := [.field str62], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 6, path := [.field str63], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 10, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 10, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 10, path := [.field str55], target := .external str56, governing := false, domain := str33 },
{ owner := 10, path := [.field str38], target := .external str65, governing := false, domain := str33 },
{ owner := 10, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 10, path := [.field str66, .index 0], target := .localRecord 11, governing := false, domain := str33 },
{ owner := 10, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 10, path := [.field str54], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 12, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 12, path := [.field str67], target := .external str68, governing := false, domain := str33 },
{ owner := 12, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 12, path := [.field str69], target := .external str70, governing := false, domain := str33 },
{ owner := 12, path := [.field str55], target := .external str56, governing := false, domain := str33 },
{ owner := 12, path := [.field str71], target := .external str49, governing := false, domain := str33 },
{ owner := 12, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 12, path := [.field str72], target := .external str73, governing := false, domain := str33 },
{ owner := 12, path := [.field str74, .index 0], target := .localRecord 1, governing := true, domain := str33 },
{ owner := 12, path := [.field str74, .index 1], target := .localRecord 2, governing := true, domain := str33 },
{ owner := 12, path := [.field str74, .index 2], target := .localRecord 0, governing := true, domain := str33 },
{ owner := 12, path := [.field str66, .index 0], target := .localRecord 11, governing := false, domain := str33 },
{ owner := 12, path := [.field str75, .index 0], target := .localRecord 10, governing := true, domain := str33 },
{ owner := 12, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 12, path := [.field str76, .index 0], target := .external str45, governing := false, domain := str33 },
{ owner := 12, path := [.field str77], target := .localRecord 11, governing := true, domain := str33 },
{ owner := 11, path := [.field str48], target := .external str49, governing := false, domain := str33 },
{ owner := 11, path := [.field str34], target := .external str4, governing := false, domain := str33 },
{ owner := 11, path := [.field str78], target := .external str79, governing := false, domain := str33 },
{ owner := 11, path := [.field str35], target := .external str1, governing := false, domain := str33 },
{ owner := 11, path := [.field str80], target := .external str81, governing := false, domain := str33 },
{ owner := 11, path := [.field str51, .index 0], target := .localRecord 0, governing := false, domain := str33 },
{ owner := 11, path := [.field str41], target := .external str2, governing := false, domain := str33 },
{ owner := 11, path := [.field str82, .index 0], target := .localRecord 8, governing := true, domain := str33 },
{ owner := 11, path := [.field str53, .index 0], target := .localRecord 0, governing := false, domain := str33 },
{ owner := 11, path := [.field str46, .index 0], target := .external str47, governing := false, domain := str33 },
{ owner := 11, path := [.field str76, .index 0], target := .external str45, governing := false, domain := str33 }
]

def references : List Reference := [references0].flatten

def str83 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:author\",\"external_target_kind\":\"urn:a-c:toy:external-kind:actor\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:author\"}"

def str84 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:authority\",\"external_target_kind\":\"urn:a-c:toy:external-kind:authority\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:authority\"}"

def str85 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:basis\",\"external_target_kind\":\"urn:a-c:toy:external-kind:basis\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:basis\"}"

def str86 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:constraint-kind:review\",\"external_target_kind\":\"urn:a-c:toy:external-kind:constraint-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:constraint-kind:review\"}"

def str87 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:context\",\"external_target_kind\":\"urn:a-c:toy:external-kind:context\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:context\"}"

def str88 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:domain:judgment\",\"external_target_kind\":\"urn:a-c:toy:external-kind:domain\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:domain:judgment\"}"

def str89 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:domain:proposal\",\"external_target_kind\":\"urn:a-c:toy:external-kind:domain\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:domain:proposal\"}"

def str90 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:evidence:authored-fixture\",\"external_target_kind\":\"urn:a-c:toy:external-kind:evidence\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:evidence:authored-fixture\"}"

def str91 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:invalidation\",\"external_target_kind\":\"urn:a-c:toy:external-kind:invalidation\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:invalidation\"}"

def str92 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:judgment-kind:review\",\"external_target_kind\":\"urn:a-c:toy:external-kind:judgment-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:judgment-kind:review\"}"

def str93 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:model:external-after\",\"external_target_kind\":\"urn:a-c:toy:external-kind:model\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:model:external-after\"}"

def str94 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:model:external-before\",\"external_target_kind\":\"urn:a-c:toy:external-kind:model\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:model:external-before\"}"

def str95 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:preservation-law\",\"external_target_kind\":\"urn:a-c:toy:external-kind:preservation-law\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:preservation-law\"}"

def str96 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:relation-kind:discovery\",\"external_target_kind\":\"urn:a-c:toy:external-kind:relation-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:relation-kind:discovery\"}"

def str97 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:relation-kind:requires\",\"external_target_kind\":\"urn:a-c:toy:external-kind:relation-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:relation-kind:requires\"}"

def str98 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:residual-kind:uncertainty\",\"external_target_kind\":\"urn:a-c:toy:external-kind:residual-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:residual-kind:uncertainty\"}"

def str99 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:scope\",\"external_target_kind\":\"urn:a-c:toy:external-kind:scope\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:scope\"}"

def str100 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:sort:statement\",\"external_target_kind\":\"urn:a-c:toy:external-kind:sort\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:sort:statement\"}"

def str101 : String := "{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:stop:refusal\",\"external_target_kind\":\"urn:a-c:toy:external-kind:stop\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:stop:refusal\"}"

def externals0 : List External := [
{ identity := str2, payload := str83 },
{ identity := str49, payload := str84 },
{ identity := str4, payload := str85 },
{ identity := str39, payload := str86 },
{ identity := str1, payload := str87 },
{ identity := str79, payload := str88 },
{ identity := str81, payload := str89 },
{ identity := str52, payload := str90 },
{ identity := str56, payload := str91 },
{ identity := str37, payload := str92 },
{ identity := str68, payload := str93 },
{ identity := str70, payload := str94 },
{ identity := str73, payload := str95 },
{ identity := str60, payload := str96 },
{ identity := str64, payload := str97 },
{ identity := str65, payload := str98 },
{ identity := str47, payload := str99 },
{ identity := str58, payload := str100 },
{ identity := str45, payload := str101 }
]

def externals : List External := [externals0].flatten

def edges0 : List (Nat × Nat) := [
(1,1),
(1,2),
(1,3),
(1,4),
(1,6),
(1,8),
(1,9),
(1,10),
(2,5),
(3,1),
(3,2),
(4,1),
(4,2),
(5,1),
(5,2),
(6,1),
(7,0),
(7,1),
(8,1),
(8,9),
(9,1),
(10,1),
(11,8),
(12,0),
(12,1),
(12,2),
(12,10),
(12,11),
(13,1)
]

def edges : List (Nat × Nat) := [edges0].flatten

def str102 : String := "urn:a-c:toy:model:proposal"

def str103 : String := "a72d423a222ecd84a429e28796c93ba07ac8b79d40caf3b74af02c36029f3b0b"

def str104 : String := "d275eb906b8ac2871e6fd7415065c1dabf915242e8583fe3e202bc723a18dec3"

def str105 : String := "{\"basis\":{\"calculus\":{\"sha256\":\"cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d\",\"uri\":\"stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md\"},\"id\":\"urn:a-c:toy:basis\",\"subject\":{\"id\":\"urn:a-c:toy:subject\",\"inventory\":[{\"id\":\"urn:a-c:toy:source:subject.md\",\"sha256\":\"2adc1caa28b8da863cc23314a4138564fe0cce847d9f0eb8afcf5b938f6282b6\"}],\"sha256\":\"2adc1caa28b8da863cc23314a4138564fe0cce847d9f0eb8afcf5b938f6282b6\"}},\"coordinates\":{\"context\":\"urn:a-c:toy:context\",\"owner\":\"urn:a-c:toy:author\",\"scope\":[\"urn:a-c:toy:scope\"]},\"dependency_contract\":{\"attachment_families\":[\"constraints\",\"latitude\",\"residuals\"],\"id\":\"urn:a-c:toy:dependency-contract\",\"required_relation_kinds\":[\"urn:a-c:toy:relation-kind:requires\"]},\"external_resolutions\":[{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:author\",\"external_target_kind\":\"urn:a-c:toy:external-kind:actor\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:author\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:authority\",\"external_target_kind\":\"urn:a-c:toy:external-kind:authority\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:authority\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:basis\",\"external_target_kind\":\"urn:a-c:toy:external-kind:basis\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:basis\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:constraint-kind:review\",\"external_target_kind\":\"urn:a-c:toy:external-kind:constraint-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:constraint-kind:review\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:context\",\"external_target_kind\":\"urn:a-c:toy:external-kind:context\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:context\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:domain:judgment\",\"external_target_kind\":\"urn:a-c:toy:external-kind:domain\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:domain:judgment\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:domain:proposal\",\"external_target_kind\":\"urn:a-c:toy:external-kind:domain\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:domain:proposal\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:evidence:authored-fixture\",\"external_target_kind\":\"urn:a-c:toy:external-kind:evidence\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:evidence:authored-fixture\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:invalidation\",\"external_target_kind\":\"urn:a-c:toy:external-kind:invalidation\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:invalidation\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:judgment-kind:review\",\"external_target_kind\":\"urn:a-c:toy:external-kind:judgment-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:judgment-kind:review\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:model:external-after\",\"external_target_kind\":\"urn:a-c:toy:external-kind:model\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:model:external-after\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:model:external-before\",\"external_target_kind\":\"urn:a-c:toy:external-kind:model\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:model:external-before\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:preservation-law\",\"external_target_kind\":\"urn:a-c:toy:external-kind:preservation-law\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:preservation-law\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:relation-kind:discovery\",\"external_target_kind\":\"urn:a-c:toy:external-kind:relation-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:relation-kind:discovery\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:relation-kind:requires\",\"external_target_kind\":\"urn:a-c:toy:external-kind:relation-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:relation-kind:requires\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:residual-kind:uncertainty\",\"external_target_kind\":\"urn:a-c:toy:external-kind:residual-kind\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:residual-kind:uncertainty\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:scope\",\"external_target_kind\":\"urn:a-c:toy:external-kind:scope\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:scope\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:sort:statement\",\"external_target_kind\":\"urn:a-c:toy:external-kind:sort\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:sort:statement\"},{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"evidence_identity\":\"urn:a-c:toy:evidence:external-coordinates\",\"external_identity\":\"urn:a-c:toy:stop:refusal\",\"external_target_kind\":\"urn:a-c:toy:external-kind:stop\",\"reference_domain\":\"urn:a-c:toy:reference-domain:declared\",\"resolution_basis\":\"urn:a-c:toy:basis\",\"resolved_target_identity\":\"urn:a-c:toy:resolved:stop:refusal\"}],\"functor_bindings\":{\"urn:a-c:toy:traversal:review\":\"urn:stdo:concept:axiomatic-calculus:f-p\"},\"id\":\"urn:a-c:toy:model:proposal\",\"identity_universe\":[\"urn:a-c:toy:author\",\"urn:a-c:toy:authority\",\"urn:a-c:toy:basis\",\"urn:a-c:toy:constraint-kind:review\",\"urn:a-c:toy:constraint:review\",\"urn:a-c:toy:context\",\"urn:a-c:toy:domain:judgment\",\"urn:a-c:toy:domain:proposal\",\"urn:a-c:toy:evidence:authored-fixture\",\"urn:a-c:toy:invalidation\",\"urn:a-c:toy:judgment-kind:review\",\"urn:a-c:toy:judgment:unassessed\",\"urn:a-c:toy:latitude:wording\",\"urn:a-c:toy:model:external-after\",\"urn:a-c:toy:model:external-before\",\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:b\",\"urn:a-c:toy:object:c\",\"urn:a-c:toy:preservation-law\",\"urn:a-c:toy:relation-kind:discovery\",\"urn:a-c:toy:relation-kind:requires\",\"urn:a-c:toy:relation:discovery\",\"urn:a-c:toy:relation:parallel:one\",\"urn:a-c:toy:relation:parallel:two\",\"urn:a-c:toy:relation:reverse\",\"urn:a-c:toy:relation:self\",\"urn:a-c:toy:residual-kind:uncertainty\",\"urn:a-c:toy:residual:reading\",\"urn:a-c:toy:scope\",\"urn:a-c:toy:sort:statement\",\"urn:a-c:toy:stop:refusal\",\"urn:a-c:toy:transformation:inert\",\"urn:a-c:toy:traversal:review\"],\"interpretation\":{\"authority\":{\"id\":\"urn:a-c:toy:authority\",\"sha256\":\"92284f331e8580e48a01dffd98f290cd006fad6d61d7a3b59f6ef09fb083ee7d\"},\"contract\":{\"id\":\"urn:a-c:toy:interpretation-contract\",\"sha256\":\"a65ebf2875b7ef9da14af347274db89445a3d49c5382d419e55a4de084b6ff80\"},\"dispositions\":[{\"authority\":\"urn:a-c:toy:authority\",\"basis\":\"urn:a-c:toy:basis\",\"decision\":\"retained\",\"reason\":\"Explicit demonstration interpretation; all inert families are retained for carrier testing, without claiming semantic validity.\",\"records\":[\"urn:a-c:toy:object:c\",\"urn:a-c:toy:object:a\",\"urn:a-c:toy:object:b\",\"urn:a-c:toy:relation:parallel:one\",\"urn:a-c:toy:relation:parallel:two\",\"urn:a-c:toy:relation:reverse\",\"urn:a-c:toy:relation:self\",\"urn:a-c:toy:relation:discovery\",\"urn:a-c:toy:constraint:review\",\"urn:a-c:toy:latitude:wording\",\"urn:a-c:toy:residual:reading\",\"urn:a-c:toy:traversal:review\",\"urn:a-c:toy:transformation:inert\",\"urn:a-c:toy:judgment:unassessed\"],\"source\":\"urn:a-c:toy:source:subject.md\"}],\"interpreter\":{\"id\":\"urn:a-c:toy:interpreter\",\"sha256\":\"09a50bae0a7aabeb6bdc391861f1aec11842dbe2f37cc567909f19e274a95216\"},\"invalidation\":{\"id\":\"urn:a-c:toy:invalidation\",\"sha256\":\"876c8eda1c567df60b0678c9a521afd928174e87c9599729bc517106c5e08e32\"},\"provenance\":[{\"id\":\"urn:a-c:toy:evidence:authoring\",\"sha256\":\"2d0881787438d5c2587436de7b0867ae338eb531df3c9e12b354c5d4465a5dca\"}],\"selection_ledger\":{\"id\":\"urn:a-c:toy:selection-ledger\",\"sha256\":\"08cf724646fa3c3970aa7fa57900d45336531c7fa35d7d9ee11a253429a0c27c\"},\"source_reentry\":{\"id\":\"urn:a-c:toy:source-reentry\",\"sha256\":\"7526ca3439184c0c84b7726053fef82cb6b8e1dd863c83894fcb440e8a64befa\"}},\"profile\":\"a_c.graphify.model/1\",\"signature\":{\"definition\":{\"constraint_kinds\":{\"urn:a-c:toy:constraint-kind:review\":{\"applies_to\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"predicate\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"operator\":{\"type\":\"enum\",\"values\":[\"requires-external-review\"]}},\"type\":\"object\"}}},\"fields\":{\"constraints\":{\"applies_to\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"id\":{\"type\":\"identity\"},\"judgment_kind\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:judgment-kind\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"kind\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:constraint-kind\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"latitude_ref\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"latitude\"],\"local_sorts\":[],\"type\":\"ref\"},\"max_items\":1,\"min_items\":0,\"type\":\"array\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"predicate\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"operator\":{\"type\":\"enum\",\"values\":[\"requires-external-review\"]}},\"type\":\"object\"},\"refusal\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:stop\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"}},\"judgments\":{\"authority\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:authority\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"decided_at\":{\"min_length\":1,\"type\":\"string\"},\"decision\":{\"type\":\"enum\",\"values\":[\"indeterminate\",\"refused\",\"accepted\"]},\"evaluator\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"evidence\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"id\":{\"type\":\"identity\"},\"kind\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:judgment-kind\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"provenance\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"subject\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"subject_digest\":{\"min_length\":1,\"type\":\"string\"}},\"latitude\":{\"allowed_variation\":{\"items\":{\"min_length\":1,\"type\":\"string\"},\"min_items\":1,\"type\":\"array\"},\"applies_to\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"forbidden_variation\":{\"items\":{\"min_length\":1,\"type\":\"string\"},\"min_items\":1,\"type\":\"array\"},\"id\":{\"type\":\"identity\"},\"invalidation\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:invalidation\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"}},\"objects\":{\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"id\":{\"type\":\"identity\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"sort\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:sort\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"value\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"text\":{\"min_length\":1,\"type\":\"string\"}},\"type\":\"object\"}},\"relations\":{\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"id\":{\"type\":\"identity\"},\"kind\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:relation-kind\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"qualifiers\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"role\":{\"type\":\"enum\",\"values\":[\"required\",\"discovery\"]}},\"type\":\"object\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"source\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"target\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"}},\"residuals\":{\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"consequence\":{\"min_length\":1,\"type\":\"string\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"id\":{\"type\":\"identity\"},\"invalidation\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:invalidation\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"kind\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:residual-kind\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"re_entry\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":false,\"local_families\":[\"traversals\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"subject\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\",\"relations\",\"constraints\"],\"local_sorts\":[],\"type\":\"ref\"},\"uncertainty\":{\"min_length\":1,\"type\":\"string\"}},\"transformations\":{\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"codomain_model\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:model\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"domain_model\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:model\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"evidence\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"external_introduced\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:external-resolution\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"external_preserved\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:external-resolution\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"external_removed\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:external-resolution\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"external_resolution_witnesses\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:witness\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"id\":{\"type\":\"identity\"},\"introduced\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:future-record\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"invalidation\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:invalidation\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"operation_authority\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:authority\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"preconditions\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"constraints\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"preservation_relation\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:preservation-law\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"preserved\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"provenance\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"re_entry\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":false,\"local_families\":[\"traversals\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"removed\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"residuals\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"residuals\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"stop_states\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:stop\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"traversal\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"traversals\"],\"local_sorts\":[],\"type\":\"ref\"}},\"traversals\":{\"authority\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:authority\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"basis\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:basis\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"codomain\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:domain\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"context\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:context\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"domain\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:domain\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"evidence\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"id\":{\"type\":\"identity\"},\"owner\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:actor\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"postconditions\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"constraints\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"preconditions\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"constraints\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"provenance\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"scope\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:scope\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"stop_states\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:stop\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"}}},\"functor_kinds\":[\"urn:stdo:concept:axiomatic-calculus:f-d\",\"urn:stdo:concept:axiomatic-calculus:f-p\",\"urn:stdo:concept:axiomatic-calculus:f-h\"],\"judgment_kinds\":{\"urn:a-c:toy:judgment-kind:review\":{\"decision\":{\"type\":\"enum\",\"values\":[\"indeterminate\",\"refused\",\"accepted\"]},\"evidence\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:evidence\"],\"governing\":false,\"local_families\":[\"objects\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":1,\"type\":\"array\"},\"subject\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"}}},\"relation_kinds\":{\"urn:a-c:toy:relation-kind:discovery\":{\"qualifiers\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"role\":{\"type\":\"enum\",\"values\":[\"required\",\"discovery\"]}},\"type\":\"object\"},\"source\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"target\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"}},\"urn:a-c:toy:relation-kind:requires\":{\"qualifiers\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"role\":{\"type\":\"enum\",\"values\":[\"required\",\"discovery\"]}},\"type\":\"object\"},\"source\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"target\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"}}},\"required_families\":[\"objects\",\"relations\",\"constraints\",\"latitude\",\"residuals\",\"traversals\",\"transformations\",\"judgments\"],\"residual_kinds\":{\"urn:a-c:toy:residual-kind:uncertainty\":{\"consequence\":{\"min_length\":1,\"type\":\"string\"},\"invalidation\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[\"urn:a-c:toy:external-kind:invalidation\"],\"governing\":false,\"local_families\":[],\"local_sorts\":[],\"type\":\"ref\"},\"re_entry\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":false,\"local_families\":[\"traversals\"],\"local_sorts\":[],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"subject\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\",\"relations\",\"constraints\"],\"local_sorts\":[],\"type\":\"ref\"},\"uncertainty\":{\"min_length\":1,\"type\":\"string\"}}},\"sorts\":{\"urn:a-c:toy:sort:statement\":{\"value\":{\"fields\":{\"arguments\":{\"items\":{\"basis_relation\":\"urn:a-c:toy:basis-relation:exact\",\"domain\":\"urn:a-c:toy:reference-domain:declared\",\"external_kinds\":[],\"governing\":true,\"local_families\":[\"objects\"],\"local_sorts\":[\"urn:a-c:toy:sort:statement\"],\"type\":\"ref\"},\"min_items\":0,\"type\":\"array\"},\"text\":{\"min_length\":1,\"type\":\"string\"}},\"type\":\"object\"}}},\"stop_kinds\":[\"urn:a-c:toy:stop:refusal\"]},\"id\":\"urn:a-c:toy:signature\",\"sha256\":\"2b5fe15584eba0e75c0c033b6f9ee5aac4fe45a41fad919e14fd544fa871419c\"}}"

def str106 : String := "{\"id\":\"urn:a-c:toy:invalidation\",\"sha256\":\"876c8eda1c567df60b0678c9a521afd928174e87c9599729bc517106c5e08e32\"}"

def model : Model := {
  identity := str102
  rawSha256 := str103
  canonicalSha256 := str104
  envelope := str105
  invalidation := str106
  records := records
  references := references
  externalResolutions := externals
  edges := edges
}

end AC.GateData
