"""Finite deterministic support for source-bound F_P development actors.

The source-owned method remains external. This module acquires exact inputs,
computes the declared finite relations and prepares immutable effect plans.
It never persists evidence or launches an actor/executor. The only subprocess
primitive is fixed read-only Git plumbing for immutable source acquisition.
"""
from __future__ import annotations

import base64
import copy
from dataclasses import dataclass, replace
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import time
from typing import Callable, TypeAlias, cast

import ac_graph

JSON: TypeAlias = ac_graph.JSON
Object: TypeAlias = dict[str, JSON]
CoreOutcome: TypeAlias = Object
EffectPlan: TypeAlias = Object
Resolver: TypeAlias = Callable[[Object], bytes]
History: TypeAlias = Callable[[str, Object], Object]

REQUEST = "a_c.fd-support.request/1"
ARTIFACT = "a_c.fd-support.artifact/1"
PROFILE_ID = "urn:a-c:fd-support:method:claude-rc9:executive:1"
PROFILE_SHA256 = "bdb937545c13d2cea8eaa93507102cff7c2ea41ca0fc169a8ec84c81003dc7d1"
METHOD_SOURCE = "c2cfa9b908d1722ae3f26c32fa4ece691083bdc3"
BUILDER_SHA256 = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
CORE_VALUES = ("satisfied", "falsified", "indeterminate", "out_of_frame", "invalid_basis")
KINDS = ("observation", "context", "preflight", "attempt", "return", "expectation", "acquisition", "operation", "resource", "raw", "qualification")
PREFIX = "Use the activated frame and declared return contract below.\n"

# Tenant-owned serialization copied at construction from the selected HOW.
# No runtime read/import of mutable method/design source occurs.
CONTENT_SCHEMAS: Object = cast(Object, json.loads(r'''
{"$defs":{"Accounting":{"additionalProperties":false,"properties":{"authority_source":{"$ref":"#/$defs/SourceRef"},"counter_rules":{"items":{"$ref":"#/$defs/CounterRule"},"type":"array"},"elapsed":{"$ref":"#/$defs/Elapsed"},"id":{"$ref":"#/$defs/Id"},"limit_predicates":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"pricing":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/Pricing"}]},"records":{"items":{"$ref":"#/$defs/ArtifactRef"},"type":"array"},"schema":{"const":"a_c.fd-support.accounting/1"}},"required":["schema","id","authority_source","records","counter_rules","elapsed","pricing","limit_predicates"],"type":"object"},"AcquiredRef":{"oneOf":[{"$ref":"#/$defs/SourceRef"},{"$ref":"#/$defs/ArtifactRef"}]},"Applicability":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/ProofCondition"}]},"ArtifactRef":{"additionalProperties":false,"properties":{"id":{"pattern":"^sha256:[0-9a-f]{64}$","type":"string"},"sha256":{"$ref":"#/$defs/Sha256"}},"required":["id","sha256"],"type":"object"},"Assessment":{"additionalProperties":false,"properties":{"applicability":{"$ref":"#/$defs/Applicability"},"basis":{"$ref":"#/$defs/Basis"},"coverage":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"id":{"$ref":"#/$defs/Id"},"key":{"$ref":"#/$defs/AssessmentKey"},"mandatory":{"type":"boolean"},"predicate":{"$ref":"#/$defs/SourceRef"},"subject":{"$ref":"#/$defs/Identity"}},"required":["id","key","predicate","subject","basis","mandatory","coverage","applicability"],"type":"object"},"AssessmentKey":{"additionalProperties":false,"properties":{"activation":{"$ref":"#/$defs/Identity"},"attempt":{"$ref":"#/$defs/ArtifactRef"},"evaluation_id":{"$ref":"#/$defs/Id"},"producer":{"$ref":"#/$defs/Id"}},"required":["producer","activation","attempt","evaluation_id"],"type":"object"},"Basis":{"additionalProperties":false,"properties":{"method_profile":{"$ref":"#/$defs/Identity"},"observations":{"items":{"$ref":"#/$defs/ArtifactRef"},"type":"array"}},"required":["method_profile","observations"],"type":"object"},"BasisChange":{"additionalProperties":false,"properties":{"current":{"$ref":"#/$defs/Basis"},"evidence":{"items":{"$ref":"#/$defs/ArtifactRef"},"type":"array"},"id":{"$ref":"#/$defs/Id"},"kind":{"const":"changed_basis"},"nodes":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"previous":{"$ref":"#/$defs/Basis"}},"required":["id","kind","nodes","previous","current","evidence"],"type":"object"},"Composite":{"additionalProperties":false,"properties":{"basis":{"$ref":"#/$defs/Basis"},"predicate":{"$ref":"#/$defs/SourceRef"},"subject":{"$ref":"#/$defs/Identity"}},"required":["predicate","subject","basis"],"type":"object"},"ConjunctionPlan":{"additionalProperties":false,"properties":{"assessments":{"items":{"$ref":"#/$defs/Assessment"},"minItems":1,"type":"array"},"authority_source":{"$ref":"#/$defs/SourceRef"},"basis_relation":{"const":"exact_equal_to_composite"},"composite":{"$ref":"#/$defs/Composite"},"decision_authority":{"$ref":"#/$defs/SourceRef"},"id":{"$ref":"#/$defs/Id"},"inherited":{"items":{"$ref":"#/$defs/ArtifactRef"},"type":"array"},"operator_id":{"const":"claude-rc9.conjunction/1"},"required_constraints":{"items":{"$ref":"#/$defs/RequiredConstraint"},"type":"array"},"required_obligations":{"items":{"$ref":"#/$defs/Obligation"},"minItems":1,"type":"array"},"rule":{"const":"first_non_satisfied_in_plan_order"},"schema":{"const":"a_c.fd-support.conjunction-plan/1"}},"required":["schema","id","authority_source","operator_id","composite","decision_authority","rule","basis_relation","required_obligations","required_constraints","assessments","inherited"],"type":"object"},"ContractSupersession":{"additionalProperties":false,"properties":{"authority_source":{"$ref":"#/$defs/SourceRef"},"contract_sha256":{"$ref":"#/$defs/Sha256"},"evidence":{"items":{"$ref":"#/$defs/AcquiredRef"},"type":"array"},"reason":{"$ref":"#/$defs/Id"},"schema":{"const":"a_c.fd-support.contract-supersession/1"},"successor_contract_sha256":{"$ref":"#/$defs/Sha256"}},"required":["schema","contract_sha256","successor_contract_sha256","authority_source","reason","evidence"],"type":"object"},"CounterOwner":{"additionalProperties":false,"properties":{"kind":{"enum":["attempt","operation"]},"record":{"$ref":"#/$defs/ArtifactRef"}},"required":["kind","record"],"type":"object"},"CounterRule":{"additionalProperties":false,"properties":{"counter_id":{"$ref":"#/$defs/Id"},"mode":{"enum":["delta","cumulative"]},"provider":{"$ref":"#/$defs/Id"},"scope":{"$ref":"#/$defs/Id"},"source":{"$ref":"#/$defs/SourceRef"},"subset_of":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/Id"}]},"unit":{"$ref":"#/$defs/Id"}},"required":["provider","counter_id","unit","scope","source","mode","subset_of"],"type":"object"},"CounterSample":{"additionalProperties":false,"properties":{"counter_id":{"$ref":"#/$defs/Id"},"interval":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/Interval"}]},"owner":{"$ref":"#/$defs/CounterOwner"},"provider":{"$ref":"#/$defs/Id"},"raw_source":{"$ref":"#/$defs/AcquiredRef"},"sample_id":{"$ref":"#/$defs/Id"},"scope":{"$ref":"#/$defs/Id"},"sequence":{"minimum":0,"type":"integer"},"unit":{"$ref":"#/$defs/Id"},"value":{"oneOf":[{"type":"null"},{"minimum":0,"type":"integer"}]}},"required":["owner","provider","counter_id","unit","scope","sample_id","sequence","value","raw_source","interval"],"type":"object"},"Coverage":{"additionalProperties":false,"properties":{"dependency_complete":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/ProofCondition"}]},"impact_complete":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/ProofCondition"}]},"population_source":{"$ref":"#/$defs/SourceRef"}},"required":["population_source","dependency_complete","impact_complete"],"type":"object"},"Dependency":{"additionalProperties":false,"properties":{"dependency":{"$ref":"#/$defs/Id"},"dependent":{"$ref":"#/$defs/Id"},"source":{"$ref":"#/$defs/SourceRef"}},"required":["dependent","dependency","source"],"type":"object"},"Elapsed":{"additionalProperties":false,"properties":{"mode":{"enum":["interval_union","enclosing_interval"]},"window":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/Interval"}]}},"required":["mode","window"],"type":"object"},"ExecutiveProof":{"additionalProperties":false,"properties":{"conjunction":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/ArtifactRef"}]},"consumed_results":{"items":{"$ref":"#/$defs/ArtifactRef"},"type":"array"},"disposition_authority":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/SourceRef"}]},"mandate":{"$ref":"#/$defs/SourceRef"},"predicate_ids":{"items":{"$ref":"#/$defs/Id"},"type":"array"}},"required":["mandate","consumed_results","conjunction","disposition_authority","predicate_ids"],"type":"object"},"Id":{"minLength":1,"type":"string"},"Identity":{"additionalProperties":false,"properties":{"id":{"$ref":"#/$defs/Id"},"sha256":{"$ref":"#/$defs/Sha256"}},"required":["id","sha256"],"type":"object"},"Interval":{"additionalProperties":false,"properties":{"clock":{"const":"unix_ns"},"ended_ns":{"minimum":0,"type":"integer"},"started_ns":{"minimum":0,"type":"integer"}},"required":["clock","started_ns","ended_ns"],"type":"object"},"Invalidator":{"oneOf":[{"$ref":"#/$defs/MaterialChange"},{"$ref":"#/$defs/BasisChange"},{"$ref":"#/$defs/RevisingObservation"}]},"Invalidators":{"additionalProperties":false,"properties":{"declarations_sha256":{"$ref":"#/$defs/Sha256"},"events":{"items":{"$ref":"#/$defs/Invalidator"},"type":"array"},"id":{"$ref":"#/$defs/Id"},"schema":{"const":"a_c.fd-support.invalidators/1"}},"required":["schema","id","declarations_sha256","events"],"type":"object"},"Json":{"oneOf":[{"type":"null"},{"type":"boolean"},{"type":"integer"},{"type":"string"},{"items":{"$ref":"#/$defs/Json"},"type":"array"},{"additionalProperties":{"$ref":"#/$defs/Json"},"type":"object"}]},"JsonPointer":{"pattern":"^(?:/(?:[^~]|~[01])*)*$","type":"string"},"JudgmentRef":{"additionalProperties":false,"properties":{"pointer":{"$ref":"#/$defs/JsonPointer"},"record":{"$ref":"#/$defs/ArtifactRef"}},"required":["record","pointer"],"type":"object"},"MaterialChange":{"additionalProperties":false,"properties":{"current":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/SourceRef"}]},"evidence":{"items":{"$ref":"#/$defs/ArtifactRef"},"type":"array"},"id":{"$ref":"#/$defs/Id"},"kind":{"const":"material_input_change"},"nodes":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"previous":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/SourceRef"}]}},"required":["id","kind","nodes","previous","current","evidence"],"type":"object"},"ModelRef":{"additionalProperties":false,"properties":{"format":{"enum":["model","carrier"]},"model_id":{"$ref":"#/$defs/Id"},"model_sha256":{"$ref":"#/$defs/Sha256"},"source":{"$ref":"#/$defs/SourceRef"}},"required":["source","format","model_id","model_sha256"],"type":"object"},"Node":{"additionalProperties":false,"properties":{"id":{"$ref":"#/$defs/Id"},"source":{"$ref":"#/$defs/SourceRef"}},"required":["id","source"],"type":"object"},"Obligation":{"additionalProperties":false,"properties":{"applicability":{"$ref":"#/$defs/Applicability"},"id":{"$ref":"#/$defs/Id"},"source":{"$ref":"#/$defs/SourceRef"}},"required":["id","source","applicability"],"type":"object"},"Pricing":{"additionalProperties":false,"properties":{"currency":{"$ref":"#/$defs/Id"},"minor_unit_scale":{"minimum":0,"type":"integer"},"rates":{"items":{"$ref":"#/$defs/Rate"},"type":"array"},"source":{"$ref":"#/$defs/SourceRef"}},"required":["source","currency","minor_unit_scale","rates"],"type":"object"},"ProofCondition":{"additionalProperties":false,"properties":{"evaluation":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/JudgmentRef"}]},"predicate":{"$ref":"#/$defs/SourceRef"}},"required":["predicate","evaluation"],"type":"object"},"Rate":{"additionalProperties":false,"properties":{"counter_id":{"$ref":"#/$defs/Id"},"denominator":{"minimum":1,"type":"integer"},"numerator":{"minimum":0,"type":"integer"},"provider":{"$ref":"#/$defs/Id"},"scope":{"$ref":"#/$defs/Id"},"unit":{"$ref":"#/$defs/Id"}},"required":["provider","counter_id","unit","scope","numerator","denominator"],"type":"object"},"RefreshCheck":{"additionalProperties":false,"properties":{"id":{"$ref":"#/$defs/Id"},"node":{"$ref":"#/$defs/Id"},"obligations":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"result":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/JudgmentRef"}]}},"required":["id","node","result","obligations"],"type":"object"},"RefreshDeclarations":{"additionalProperties":false,"properties":{"authority_source":{"$ref":"#/$defs/SourceRef"},"checks":{"items":{"$ref":"#/$defs/RefreshCheck"},"type":"array"},"coverage":{"$ref":"#/$defs/Coverage"},"dependencies":{"items":{"$ref":"#/$defs/Dependency"},"type":"array"},"id":{"$ref":"#/$defs/Id"},"impact_cover":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"mandatory_gates":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"new_basis":{"$ref":"#/$defs/Basis"},"new_obligations":{"items":{"$ref":"#/$defs/Obligation"},"type":"array"},"new_subject":{"$ref":"#/$defs/Identity"},"nodes":{"items":{"$ref":"#/$defs/Node"},"type":"array"},"old_basis":{"$ref":"#/$defs/Basis"},"old_subject":{"$ref":"#/$defs/Identity"},"retention":{"items":{"$ref":"#/$defs/Retention"},"type":"array"},"schema":{"const":"a_c.fd-support.refresh-declarations/1"}},"required":["schema","id","authority_source","old_subject","new_subject","old_basis","new_basis","nodes","dependencies","checks","coverage","impact_cover","new_obligations","mandatory_gates","retention"],"type":"object"},"RelationApplicability":{"additionalProperties":false,"properties":{"condition":{"$ref":"#/$defs/Applicability"},"target":{"$ref":"#/$defs/RelationTarget"}},"required":["target","condition"],"type":"object"},"RelationApplicabilityFact":{"additionalProperties":false,"properties":{"condition":{"$ref":"#/$defs/Applicability"},"core_value":{"oneOf":[{"type":"null"},{"enum":["satisfied","falsified","indeterminate","out_of_frame","invalid_basis"]}]},"declaration_present":{"type":"boolean"},"excluded":{"type":"boolean"},"expected_subject":{"$ref":"#/$defs/Identity"},"gaps":{"items":{"$ref":"#/$defs/Json"},"type":"array"},"judgment":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/JudgmentRef"}]},"target":{"$ref":"#/$defs/RelationTarget"},"unresolved":{"type":"boolean"}},"required":["target","declaration_present","condition","expected_subject","core_value","judgment","excluded","unresolved","gaps"],"type":"object"},"RelationBoundary":{"additionalProperties":false,"properties":{"candidate_closure":{"type":"boolean"},"excluded_relations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"limits":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"missing_mappings":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"non_governing_relations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"out_of_scope_obligations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"unknown_obligations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"unresolved_traversal_relations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true}},"required":["candidate_closure","unresolved_traversal_relations","excluded_relations","non_governing_relations","unknown_obligations","missing_mappings","out_of_scope_obligations","limits"],"type":"object"},"RelationCoverage":{"additionalProperties":false,"properties":{"explicit_unknowns":{"items":{"$ref":"#/$defs/RelationUnknown"},"type":"array"},"mapped_support":{"items":{"$ref":"#/$defs/SupportMapping"},"type":"array"},"obligations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true}},"required":["obligations","mapped_support","explicit_unknowns"],"type":"object"},"RelationCoverageFacts":{"additionalProperties":false,"properties":{"declared_support_present":{"items":{"$ref":"#/$defs/SupportMapping"},"type":"array"},"empty_declared_support":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"explicit_unknowns":{"items":{"$ref":"#/$defs/RelationUnknown"},"type":"array"},"mapping_absent":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"missing_declared_support":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"required_missing":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"scoped_population":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true}},"required":["scoped_population","declared_support_present","missing_declared_support","mapping_absent","empty_declared_support","explicit_unknowns","required_missing"],"type":"object"},"RelationDeclarations":{"additionalProperties":false,"properties":{"applicability":{"items":{"$ref":"#/$defs/RelationApplicability"},"type":"array"},"basis":{"$ref":"#/$defs/Basis"},"coverage":{"$ref":"#/$defs/RelationCoverage"},"governing_kinds":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"id":{"$ref":"#/$defs/Id"},"model":{"$ref":"#/$defs/ModelRef"},"model_basis":{"$ref":"#/$defs/Identity"},"relations":{"items":{"$ref":"#/$defs/RelationEdge"},"type":"array"},"schema":{"const":"a_c.fd-support.relation-declarations/1"},"subject":{"$ref":"#/$defs/Identity"}},"required":["schema","id","model","model_basis","subject","basis","relations","governing_kinds","coverage","applicability"],"type":"object"},"RelationEdge":{"additionalProperties":false,"properties":{"id":{"$ref":"#/$defs/Id"},"kind":{"$ref":"#/$defs/Id"},"source":{"$ref":"#/$defs/Id"},"target":{"$ref":"#/$defs/Id"}},"required":["id","source","target","kind"],"type":"object"},"RelationPath":{"additionalProperties":false,"properties":{"records":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"relations":{"items":{"$ref":"#/$defs/Id"},"type":"array"}},"required":["records","relations"],"type":"object"},"RelationQueryResult":{"additionalProperties":false,"properties":{"applicability":{"items":{"$ref":"#/$defs/RelationApplicabilityFact"},"type":"array"},"basis":{"$ref":"#/$defs/Basis"},"boundary":{"$ref":"#/$defs/RelationBoundary"},"coverage":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/RelationCoverageFacts"}]},"declarations":{"$ref":"#/$defs/SourceRef"},"model":{"$ref":"#/$defs/ModelRef"},"model_basis":{"$ref":"#/$defs/Identity"},"path":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/RelationPath"}]},"query":{"enum":["dependencies","path","impact","coverage"]},"records":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true},"relations":{"items":{"$ref":"#/$defs/RelationEdge"},"type":"array"},"schema":{"const":"a_c.fd-support.relation-query-result/1"},"seeds":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"subject":{"$ref":"#/$defs/Identity"},"traversed_relations":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true}},"required":["schema","query","declarations","model","model_basis","subject","basis","seeds","records","relations","traversed_relations","path","coverage","applicability","boundary"],"type":"object"},"RelationTarget":{"additionalProperties":false,"properties":{"id":{"$ref":"#/$defs/Id"},"kind":{"enum":["relation","obligation"]}},"required":["kind","id"],"type":"object"},"RelationUnknown":{"additionalProperties":false,"properties":{"obligation_id":{"$ref":"#/$defs/Id"},"reason":{"$ref":"#/$defs/Id"}},"required":["obligation_id","reason"],"type":"object"},"RequiredConstraint":{"additionalProperties":false,"properties":{"obligation_id":{"$ref":"#/$defs/Id"},"predicate":{"$ref":"#/$defs/SourceRef"}},"required":["obligation_id","predicate"],"type":"object"},"RequiredEvaluation":{"additionalProperties":false,"properties":{"id":{"$ref":"#/$defs/Id"},"predicate":{"$ref":"#/$defs/SourceRef"}},"required":["id","predicate"],"type":"object"},"Resource":{"additionalProperties":false,"properties":{"gaps":{"items":{"$ref":"#/$defs/Json"},"type":"array"},"interval":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/Interval"}]},"owner":{"$ref":"#/$defs/CounterOwner"},"samples":{"items":{"$ref":"#/$defs/CounterSample"},"type":"array"},"schema":{"const":"a_c.fd-support.resource/1"}},"required":["schema","owner","samples","interval","gaps"],"type":"object"},"Retention":{"additionalProperties":false,"properties":{"assertion_basis":{"$ref":"#/$defs/ProofCondition"},"claim_scope":{"$ref":"#/$defs/ProofCondition"},"dependencies":{"$ref":"#/$defs/ProofCondition"},"observation_basis":{"$ref":"#/$defs/ProofCondition"},"result":{"$ref":"#/$defs/JudgmentRef"}},"required":["result","claim_scope","assertion_basis","observation_basis","dependencies"],"type":"object"},"ReturnContract":{"oneOf":[{"additionalProperties":false,"properties":{"authority_source":{"$ref":"#/$defs/SourceRef"},"carrier":{"const":"a_c.fd-support.closed-return/1"},"id":{"$ref":"#/$defs/Id"},"output_slot":{"const":"final_stdout_object"},"proof":{"$ref":"#/$defs/WorkerProof"},"required_evaluations":{"items":{"$ref":"#/$defs/RequiredEvaluation"},"type":"array"},"role":{"const":"Worker"},"schema":{"const":"a_c.fd-support.return-contract/1"}},"required":["schema","id","authority_source","carrier","output_slot","required_evaluations","role","proof"],"type":"object"},{"additionalProperties":false,"properties":{"authority_source":{"$ref":"#/$defs/SourceRef"},"carrier":{"const":"a_c.fd-support.closed-return/1"},"id":{"$ref":"#/$defs/Id"},"output_slot":{"const":"final_stdout_object"},"proof":{"$ref":"#/$defs/ReviewerProof"},"required_evaluations":{"items":{"$ref":"#/$defs/RequiredEvaluation"},"type":"array"},"role":{"const":"Reviewer"},"schema":{"const":"a_c.fd-support.return-contract/1"}},"required":["schema","id","authority_source","carrier","output_slot","required_evaluations","role","proof"],"type":"object"},{"additionalProperties":false,"properties":{"authority_source":{"$ref":"#/$defs/SourceRef"},"carrier":{"const":"a_c.fd-support.closed-return/1"},"id":{"$ref":"#/$defs/Id"},"output_slot":{"const":"final_stdout_object"},"proof":{"$ref":"#/$defs/ExecutiveProof"},"required_evaluations":{"items":{"$ref":"#/$defs/RequiredEvaluation"},"type":"array"},"role":{"const":"Executive"},"schema":{"const":"a_c.fd-support.return-contract/1"}},"required":["schema","id","authority_source","carrier","output_slot","required_evaluations","role","proof"],"type":"object"}]},"ReviewerProof":{"additionalProperties":false,"properties":{"claim":{"$ref":"#/$defs/SourceRef"},"comparison":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/SourceRef"}]},"expectations":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/ArtifactRef"}]},"independence_policy":{"oneOf":[{"type":"null"},{"$ref":"#/$defs/SourceRef"}]},"predicate_ids":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"proof_sources":{"items":{"$ref":"#/$defs/SourceRef"},"type":"array"}},"required":["claim","expectations","proof_sources","comparison","independence_policy","predicate_ids"],"type":"object"},"RevisingObservation":{"additionalProperties":false,"properties":{"declaration":{"$ref":"#/$defs/SourceRef"},"id":{"$ref":"#/$defs/Id"},"kind":{"const":"declared_revising_observation"},"nodes":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"observation":{"$ref":"#/$defs/ArtifactRef"}},"required":["id","kind","nodes","declaration","observation"],"type":"object"},"Sha256":{"pattern":"^[0-9a-f]{64}$","type":"string"},"SourceRef":{"additionalProperties":false,"properties":{"engine":{"enum":["workspace-regular-file","immutable-git-blob","retained-evidence"]},"object":{"oneOf":[{"type":"null"},{"pattern":"^(?:[0-9a-f]{40}|[0-9a-f]{64})$","type":"string"}]},"path":{"$ref":"#/$defs/Id"},"root":{"$ref":"#/$defs/Id"},"selector":{"oneOf":[{"type":"null"},{"additionalProperties":false,"properties":{"lines":{"items":false,"maxItems":2,"minItems":2,"prefixItems":[{"minimum":1,"type":"integer"},{"minimum":1,"type":"integer"}],"type":"array"}},"required":["lines"],"type":"object"},{"additionalProperties":false,"properties":{"json_pointer":{"$ref":"#/$defs/JsonPointer"}},"required":["json_pointer"],"type":"object"}]},"sha256":{"$ref":"#/$defs/Sha256"}},"required":["engine","root","path","object","sha256","selector"],"type":"object"},"SupportMapping":{"additionalProperties":false,"properties":{"obligation_id":{"$ref":"#/$defs/Id"},"support_ids":{"items":{"$ref":"#/$defs/Id"},"type":"array","uniqueItems":true}},"required":["obligation_id","support_ids"],"type":"object"},"WorkerProof":{"additionalProperties":false,"properties":{"predicate_ids":{"items":{"$ref":"#/$defs/Id"},"type":"array"},"transition_sources":{"items":{"$ref":"#/$defs/SourceRef"},"type":"array"}},"required":["transition_sources","predicate_ids"],"type":"object"}},"$id":"urn:a-c:fd-support:content-schemas:1","$schema":"https://json-schema.org/draft/2020-12/schema","oneOf":[{"$ref":"#/$defs/ConjunctionPlan"},{"$ref":"#/$defs/RefreshDeclarations"},{"$ref":"#/$defs/Invalidators"},{"$ref":"#/$defs/Accounting"},{"$ref":"#/$defs/Resource"},{"$ref":"#/$defs/ReturnContract"},{"$ref":"#/$defs/ContractSupersession"},{"$ref":"#/$defs/RelationDeclarations"}]}
'''))

# Executive-selected realization refinement retained before implementation in
# core/REVIEW_CLAIM.clarification.txt; previous 57 definitions are unchanged.
_cdefs = cast(Object, CONTENT_SCHEMAS["$defs"])
_cdefs["ReviewClaim"] = {"type": "object", "properties": {"id": {"$ref": "#/$defs/Id"}, "candidate_sources": {"type": "array", "items": {"$ref": "#/$defs/SourceRef"}, "uniqueItems": True}}, "required": ["id", "candidate_sources"], "additionalProperties": False}
cast(list[JSON], CONTENT_SCHEMAS["oneOf"]).append({"$ref": "#/$defs/ReviewClaim"})

CODES: dict[str, str | None] = {
    **{k: None for k in ("malformed_request", "unknown_operation", "invalid_initialize", "unsupported_protocol_method")},
    **{k: "refused(capability)" for k in ("unsupported_contract", "unsupported_measurement", "unsupported_translation", "unsupported_executor", "unsupported_check")},
    **{k: "refused(authority)" for k in ("authority_missing", "acquisition_denied", "result_surface_denied", "role_effect_denied", "transition_record_missing")},
    **{k: "refused(basis)" for k in ("basis_missing", "basis_ambiguous", "basis_stale", "source_missing", "digest_mismatch", "dependency_changed", "history_incomplete", "unqualified_operator", "domain_invalid")},
    **{k: "refused(constraint)" for k in ("path_refused", "budget_exceeded", "request_identity_conflict", "target_conflict", "contract_violation")},
    **{k: "held(observation)" for k in ("observation_unavailable", "evidence_publication_failed", "internal_failure")},
    **{k: "held(effect)" for k in ("effect_unreconciled", "effect_completion_unknown")},
}


class SupportError(ValueError):
    def __init__(self, code: str, reason: str, gaps: list[JSON] | None = None,
                 source_refs: list[JSON] | None = None) -> None:
        if code not in CODES:
            raise ValueError("unknown support error code: " + code)
        super().__init__(reason)
        self.code = code
        self.reason = reason
        self.gaps = gaps if gaps is not None else []
        self.source_refs = source_refs if source_refs is not None else []

    def document(self) -> Object:
        return document({"code": self.code, "reason": self.reason,
                "gaps": self.gaps, "source_refs": self.source_refs})


def fail(code: str, reason: str, gaps: list[JSON] | None = None,
         source_refs: list[JSON] | None = None) -> None:
    raise SupportError(code, reason, gaps, source_refs)


def as_object(value: JSON, label: str = "object") -> Object:
    if not isinstance(value, dict):
        raise SupportError("contract_violation", label + " must be an object")
    return value


def as_list(value: JSON, label: str = "array") -> list[JSON]:
    if not isinstance(value, list):
        raise SupportError("contract_violation", label + " must be an array")
    return value


def text(value: JSON, label: str = "string") -> str:
    if not isinstance(value, str) or not value:
        raise SupportError("contract_violation", label + " must be a nonempty string")
    return value


def integer(value: JSON, label: str = "integer", minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise SupportError("contract_violation", label + " must be an integer >= " + str(minimum))
    return value


def exact_keys(value: Object, required: list[str] | tuple[str, ...],
               optional: tuple[str, ...] = (), label: str = "object") -> None:
    if set(value) - set(required) - set(optional) or set(required) - set(value):
        raise SupportError("contract_violation", label + " has missing or unknown fields", [
            document({"missing": sorted(set(required) - set(value)),
             "unknown": sorted(set(value) - set(required) - set(optional))})])


def _json(value: object, depth: int = 0) -> JSON:
    if depth > 128:
        raise SupportError("budget_exceeded", "JSON nesting exceeds the published 128-level parser bound")
    if value is None or type(value) in (bool, int, str):
        return cast(JSON, value)
    if isinstance(value, list):
        return [_json(v, depth + 1) for v in value]
    if isinstance(value, dict) and all(isinstance(k, str) for k in value):
        return {str(k): _json(v, depth + 1) for k, v in value.items()}
    raise SupportError("malformed_request", "Only integer-only finite JSON values are supported")


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise SupportError("malformed_request", "Duplicate JSON key: " + key)
        out[key] = value
    return out


def _noninteger(token: str) -> object:
    raise SupportError("malformed_request", "Noninteger JSON token: " + token)


def parse_json(raw: bytes) -> JSON:
    try:
        value: object = json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs,
                                   parse_float=_noninteger, parse_constant=_noninteger)
        return _json(value)
    except SupportError:
        raise
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise SupportError("malformed_request", "Invalid UTF-8 JSON: " + str(exc)) from exc


def document(value: object) -> Object:
    return as_object(_json(value))


def canonical(value: JSON) -> bytes:
    _json(value)
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value: JSON) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _equal(a: JSON, b: JSON) -> bool:
    return canonical(a) == canonical(b)


def pointer(value: JSON, path: str) -> JSON:
    if path == "":
        return value
    if not re.fullmatch(r"(?:/(?:[^~]|~[01])*)*", path):
        raise SupportError("contract_violation", "Invalid JSON pointer: " + path)
    current = value
    for raw in path.split("/")[1:]:
        part = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and re.fullmatch(r"0|[1-9][0-9]*", part) and int(part) < len(current):
            current = current[int(part)]
        else:
            raise SupportError("basis_missing", "JSON pointer is absent: " + path)
    return current


def validate_schema(value: JSON, schema: Object, definitions: Object | None = None,
                    location: str = "$") -> None:
    """Interpret only the finite schema keywords published by this tenant."""
    defs = as_object(CONTENT_SCHEMAS["$defs"]) if definitions is None else definitions
    if "$ref" in schema:
        ref = text(schema["$ref"])
        if not ref.startswith("#/$defs/") or ref[8:] not in defs:
            raise SupportError("unsupported_contract", "Unsupported schema reference: " + ref)
        validate_schema(value, as_object(defs[ref[8:]]), defs, location)
        return
    if "oneOf" in schema:
        hits = 0
        for candidate in as_list(schema["oneOf"]):
            try:
                validate_schema(value, as_object(candidate), defs, location)
                hits += 1
            except SupportError:
                pass
        if hits != 1:
            raise SupportError("contract_violation", location + " must match exactly one declared shape")
        return
    if "const" in schema and not _equal(value, schema["const"]):
        raise SupportError("unsupported_contract", location + " has unsupported constant")
    if "enum" in schema and not any(_equal(value, x) for x in as_list(schema["enum"])):
        raise SupportError("unsupported_contract", location + " has unsupported enum")
    kind = schema.get("type")
    checks = {"null": value is None, "boolean": type(value) is bool,
              "integer": type(value) is int, "string": isinstance(value, str),
              "array": isinstance(value, list), "object": isinstance(value, dict)}
    if isinstance(kind, str) and not checks.get(kind, False):
        raise SupportError("contract_violation", location + " has wrong declared type " + kind)
    if isinstance(value, str):
        if "minLength" in schema and len(value) < integer(schema["minLength"]):
            raise SupportError("contract_violation", location + " is empty")
        if "pattern" in schema and re.search(text(schema["pattern"]), value) is None:
            raise SupportError("contract_violation", location + " has invalid lexical form")
    if type(value) is int:
        if "minimum" in schema and value < integer(schema["minimum"]):
            raise SupportError("contract_violation", location + " is below minimum")
        if "maximum" in schema and value > integer(schema["maximum"]):
            raise SupportError("contract_violation", location + " is above maximum")
    if isinstance(value, list):
        if "minItems" in schema and len(value) < integer(schema["minItems"]):
            raise SupportError("contract_violation", location + " has too few items")
        if "maxItems" in schema and len(value) > integer(schema["maxItems"]):
            raise SupportError("contract_violation", location + " has too many items")
        if schema.get("uniqueItems") is True and len({canonical(x) for x in value}) != len(value):
            raise SupportError("contract_violation", location + " has duplicate items")
        prefix = as_list(schema.get("prefixItems", []))
        for index, member in enumerate(value):
            item = prefix[index] if index < len(prefix) else schema.get("items", {})
            if item is False:
                raise SupportError("contract_violation", location + " has extra positional items")
            if isinstance(item, dict):
                validate_schema(member, item, defs, location + "/" + str(index))
    if isinstance(value, dict):
        props = as_object(schema.get("properties", {}))
        required = as_list(schema.get("required", []))
        if any(text(k) not in value for k in required):
            raise SupportError("contract_violation", location + " is missing required fields")
        for key, member in value.items():
            if key in props:
                validate_schema(member, as_object(props[key]), defs, location + "/" + key)
            elif schema.get("additionalProperties") is False:
                raise SupportError("contract_violation", location + " has unknown field " + key)
            elif isinstance(schema.get("additionalProperties"), dict):
                validate_schema(member, as_object(schema["additionalProperties"]), defs, location + "/" + key)


def validate_content(value: JSON, kind: str) -> Object:
    defs = as_object(CONTENT_SCHEMAS["$defs"])
    if kind not in defs:
        raise SupportError("unsupported_contract", "Unknown content contract: " + kind)
    validate_schema(value, as_object(defs[kind]))
    return as_object(value)


def _ref(name: str) -> Object:
    return document({"$ref": "#/$defs/" + name})


def _array(item: Object) -> Object:
    return document({"type": "array", "items": item})


def _object(properties: Object, optional: tuple[str, ...] = ()) -> Object:
    return document({"type": "object", "properties": properties,
            "required": [k for k in properties if k not in optional], "additionalProperties": False})


def _nullable(schema: Object) -> Object:
    return document({"oneOf": [{"type": "null"}, schema]})


_SCOPE = _object({"root": _ref("Id"), "path": _ref("Id"), "kind": {"enum": ["file", "directory"]}})
_SELECTION = _object({"seeds": _array(_ref("Id")), "budget_records": _nullable({"type": "integer", "minimum": 0})}, ("budget_records",))
_ARGUMENTS: dict[str, Object] = {
    "tools.describe": _object({"operation": _ref("Id"), "method_profile": _ref("Identity")}, ("operation", "method_profile")),
    "workspace.observe": _object({"scope": _array(_SCOPE), "previous": _ref("ArtifactRef")}, ("previous",)),
    "source.read": _object({"source": _ref("SourceRef"), "encoding": {"enum": ["utf8", "base64"]}, "max_content_bytes": {"type": "integer", "minimum": 0}}, ("max_content_bytes",)),
    "records.find": _object({"model": _ref("ModelRef"), "text": {"type": "string"}}),
    "records.read": _object({"model": _ref("ModelRef"), "ids": _array(_ref("Id"))}),
    "graph.project": _object({"model": _ref("ModelRef"), "selections": _array(_SELECTION)}),
    "relations.query": _object({"model": _ref("ModelRef"), "declarations": _ref("SourceRef"), "query": {"enum": ["dependencies", "path", "impact", "coverage"]}, "seeds": _array(_ref("Id"))}),
    "context.assemble": _object({"packet": {"type": "object"}, "models": _array(_object({"model": _ref("ModelRef"), "selections": _array(_SELECTION)})), "sources": _array(_ref("SourceRef")), "late_acquisition": _array(_ref("SourceRef")), "envelope": _object({"capacity_bytes": _nullable({"type": "integer", "minimum": 0}), "boundary": {"const": "executor-stdin-utf8"}, "host_context": _object({"state": {"enum": ["known", "bounded", "unknown"]}, "bytes": _nullable({"type": "integer", "minimum": 0}), "evidence": _nullable(_ref("SourceRef"))})})}),
    "contract.preflight": _object({"context": _ref("ArtifactRef"), "grant_id": _ref("Id"), "executor_id": _ref("Id"), "result_key": _ref("Id"), "observations": _array(_ref("ArtifactRef")), "admission_record": _ref("AcquiredRef")}, ("admission_record",)),
    "dispatch.start": _object({"preflight": _ref("ArtifactRef"), "retry_of": _ref("ArtifactRef"), "reconciliation": _ref("ArtifactRef")}, ("retry_of", "reconciliation")),
    "dispatch.observe": _object({"attempt": _ref("ArtifactRef"), "after_event": {"type": "integer", "minimum": 0}}),
    "dispatch.cancel": _object({"attempt": _ref("ArtifactRef"), "reason": _ref("Id")}),
    "events.wait": _object({"attempt": _ref("ArtifactRef"), "after_event": {"type": "integer", "minimum": 0}, "timeout_ms": {"type": "integer", "minimum": 0}, "cadence_ms": {"type": "integer", "minimum": 1}, "purpose": _ref("Id"), "stop_condition": _ref("Id")}),
    "return.capture": _object({"attempt": _ref("ArtifactRef"), "payload": _ref("ArtifactRef"), "return_contract": _ref("SourceRef")}),
    "return.check": _object({"return": _ref("ArtifactRef"), "context": _ref("ArtifactRef"), "consumer": _ref("Id"), "observations": _array(_ref("ArtifactRef")), "predicates": _array(_ref("Id"))}),
    "review.prepare": _object({"phase": {"enum": ["expectation", "candidate"]}, "claim": _ref("SourceRef"), "sources": _array(_ref("SourceRef")), "candidate": _nullable(_ref("SourceRef")), "proof": _array(_ref("SourceRef")), "comparison": _nullable(_ref("SourceRef")), "expectations": _nullable(_ref("ArtifactRef")), "expectation_body": _nullable(_object({"text": {"type": "string"}, "source_inputs": _array(_ref("ArtifactRef"))}))}),
    "checks.evaluate": _object({"predicate_id": _ref("Id"), "inputs": {"type": "object", "additionalProperties": _ref("AcquiredRef")}, "subject": _ref("Identity"), "basis": _ref("Basis")}),
    "results.conjoin": _object({"operator_id": _ref("Id"), "plan": _ref("SourceRef"), "returns": _array(_ref("ArtifactRef")), "current_observations": _array(_ref("ArtifactRef"))}),
    "work.project": _object({"carrier": _ref("SourceRef"), "selection": _array(_ref("Id"))}),
    "work.write": _object({"grant_id": _ref("Id"), "target": {"type": "object"}, "mode": {"enum": ["append", "replace"]}, "record": _object({"text": {"type": "string"}, "provenance": _ref("SourceRef")}), "interpretation": _nullable(_object({"text": {"type": "string"}, "author": _ref("SourceRef")})), "observations": _array(_ref("ArtifactRef"))}),
    "refresh.prepare": _object({"previous": _ref("ArtifactRef"), "current": _ref("ArtifactRef"), "declarations": _ref("SourceRef"), "results": _array(_ref("ArtifactRef")), "invalidators": _ref("SourceRef")}),
    "resources.aggregate": _object({"attempts": _array(_ref("ArtifactRef")), "accounting": _ref("SourceRef")}),
    "evidence.read": _object({"artifact": _ref("ArtifactRef"), "max_content_bytes": {"type": "integer", "minimum": 0}}, ("max_content_bytes",)),
}
EFFECT_OPERATIONS = frozenset({"contract.preflight", "dispatch.start", "dispatch.observe", "dispatch.cancel", "events.wait", "work.write"})


def request_schema(operation: str | None = None) -> Object:
    if operation is not None and operation not in _ARGUMENTS:
        raise SupportError("unknown_operation", "Unknown operation: " + operation)
    if operation is None:
        return document({"$schema": "https://json-schema.org/draft/2020-12/schema",
                "$defs": _definition_closure({"oneOf": [_request_body(name) for name in sorted(_ARGUMENTS)]}),
                "oneOf": [_request_body(name) for name in sorted(_ARGUMENTS)]})
    result = _object({"schema": {"const": REQUEST}, "id": _ref("Id"),
                      "operation": {"const": operation}, "arguments": copy.deepcopy(_ARGUMENTS[operation])})
    result["$defs"] = _definition_closure(result)
    return result


def inventory(operation: str | None = None) -> Object:
    if operation is not None and operation not in _ARGUMENTS:
        raise SupportError("unknown_operation", "Unknown operation: " + operation)
    names = [operation] if operation is not None else sorted(_ARGUMENTS)
    return document({"schema": "a_c.fd-support.inventory/1", "method_profile": {"id": PROFILE_ID, "sha256": PROFILE_SHA256},
            "builder": {"uri": "stdo://releases/v2.5.1-rc.2/", "manifest_sha256": BUILDER_SHA256},
            "operations": [{"name": name, "input_schema": request_schema(name),
                            "effect": name in EFFECT_OPERATIONS,
                            "output_schema": response_schema(),
                            "prerequisites": ["trusted exact policy", "fixed principal operation grant", "exact acquired input basis"],
                            "checked_fragment": "selected finite declared contract only"} for name in names],
            "content_schemas": copy.deepcopy(CONTENT_SCHEMAS), "refusal_codes": cast(Object, dict(CODES)),
            "qualification": "provisional construction; independent integrated qualification and owner acceptance pending",
            "unsupported": ["other method cuts", "semantic sufficiency certification", "inferred semantic edges", "arbitrary executable predicates", "OS sandboxing", "external producer authentication", "MCP server/discover", "benefit or acceptance claims"]})


def validate_request(request: JSON) -> Object:
    obj = as_object(request, "request")
    if set(obj) != {"schema", "id", "operation", "arguments"} or obj.get("schema") != REQUEST:
        raise SupportError("malformed_request", "Request must use the exact versioned envelope")
    name = obj.get("operation")
    if not isinstance(name, str) or name not in _ARGUMENTS:
        raise SupportError("unknown_operation", "Unknown operation")
    validate_schema(obj, request_schema(name))
    return obj


def parse_request(raw_bytes: bytes) -> Object:
    return validate_request(parse_json(raw_bytes))


def operation_outcome(operation: str, value: str = "returned", code: str | None = None,
                      evidence: list[JSON] | None = None, limits: list[JSON] | None = None) -> Object:
    if code is not None:
        mapped = CODES[code]
        if mapped is None:
            raise SupportError("contract_violation", "An unbound guard has no operation outcome")
        value = mapped
    parents = {"returned": "satisfied", "held(observation)": "indeterminate", "held(effect)": "indeterminate",
               "refused(constraint)": "falsified", "refused(basis)": "invalid_basis",
               "refused(authority)": "out_of_frame", "refused(capability)": "out_of_frame"}
    if value not in parents:
        raise SupportError("contract_violation", "Unsupported operation outcome")
    return document({"predicate": "B(" + operation + "): declared exact output/effect-evidence payload availability on the requested basis",
            "value": value, "cause": code if code is not None else "declared output available",
            "core_value": parents[value],
            "source_parent": {"member": "FOUNDATIONS.md", "sha256": "fd2d895f90eb39bda0950c1c7ff02057ef5d8ae73fcbc5b3203f7e99081d6e3f", "clause": "results"},
            "evidence": evidence if evidence is not None else [],
            "limits": limits if limits is not None else ["output availability only; no semantic acceptance"]})


def refusal_outcome(runtime: Runtime, request: Object, error: SupportError) -> CoreOutcome:
    del runtime
    op = request.get("operation")
    bound = isinstance(op, str) and op in _ARGUMENTS and CODES[error.code] is not None
    return document({"result": None, "artifacts": [], "operation_outcome": operation_outcome(cast(str, op), code=error.code) if bound else None,
            "refusal": error.document(), "acquisitions": []})

@dataclass(frozen=True)
class Runtime:
    policy_path: Path
    policy_sha256: str
    principal_id: str
    _policy: Object
    _principal: Object
    evidence_root: Path
    resolve_artifact: Resolver | None = None
    query_artifacts: History | None = None

    @property
    def policy(self) -> Object:
        return copy.deepcopy(self._policy)

    @property
    def principal(self) -> Object:
        return copy.deepcopy(self._principal)

    @classmethod
    def from_policy(cls, path: str | Path, expected_sha256: str, principal: str,
                    *, resolve_artifact: Resolver | None = None,
                    query_artifacts: History | None = None) -> Runtime:
        policy_path = Path(path).absolute()
        raw = _regular_bytes(policy_path)
        if _sha(raw) != expected_sha256:
            raise SupportError("digest_mismatch", "Policy bytes do not match trusted startup digest")
        policy = as_object(parse_json(raw), "policy")
        exact_keys(policy, ("schema", "id", "product", "method_profile", "sources", "principals", "grants", "predicates", "operators", "executors", "event_sinks", "independence_policy", "evidence_root", "limits", "authority_sources"), label="policy")
        if policy["schema"] != "a_c.fd-support.policy/1":
            raise SupportError("unsupported_contract", "Unsupported policy schema")
        text(policy["id"])
        roots = as_object(policy["sources"])
        for root_id, value in roots.items():
            text(root_id)
            root = as_object(value)
            exact_keys(root, ("path", "read_scope", "kind", "writable"), label="source root")
            if root["kind"] not in ("workspace", "git") or type(root["writable"]) is not bool:
                raise SupportError("unsupported_contract", "Unsupported source root configuration")
            if not Path(text(root["path"])).is_absolute():
                raise SupportError("path_refused", "Trusted source root must be absolute")
            for scope in as_list(root["read_scope"]):
                item = as_object(scope)
                exact_keys(item, ("path", "kind"))
                _relative(text(item["path"]))
                if item["kind"] not in ("file", "directory"):
                    raise SupportError("unsupported_contract", "Unknown read-scope kind")
        principals = as_object(policy["principals"])
        if principal not in principals:
            raise SupportError("authority_missing", "Startup principal is not registered")
        for principal_value in principals.values():
            p = as_object(principal_value)
            exact_keys(p, ("actor_id", "role", "family", "authorship", "operations", "role_binding", "role_transition"), label="principal")
            if p["role"] not in ("Executive", "Worker", "Reviewer"):
                raise SupportError("unsupported_contract", "Unknown registered method role")
            for field in ("actor_id", "family", "authorship"):
                text(p[field])
            _strings(p["operations"])
            validate_content(p["role_binding"], "SourceRef")
            if p["role_transition"] is not None:
                validate_content(p["role_transition"], "SourceRef")
        profile = as_object(policy["method_profile"])
        exact_keys(profile, ("id", "sha256", "source"))
        if profile["id"] != PROFILE_ID or profile["sha256"] != PROFILE_SHA256:
            raise SupportError("unsupported_contract", "Only the exact Claude RC9 binding is supported")
        validate_content(profile["source"], "SourceRef")
        product = as_object(policy["product"])
        exact_keys(product, ("definition_id", "definition", "authority_binding"))
        text(product["definition_id"])
        validate_content(product["definition"], "SourceRef")
        authority = as_object(product["authority_binding"])
        exact_keys(authority, ("definition_locator", "owner_record", "mechanism", "result_surface", "scope"))
        text(authority["definition_locator"])
        validate_content(authority["owner_record"], "SourceRef")
        mechanism = as_object(authority["mechanism"])
        exact_keys(mechanism, ("id", "source", "implementation_sha256"))
        surface = as_object(authority["result_surface"])
        exact_keys(surface, ("root", "namespace", "consumer"))
        _relative(text(surface["namespace"]))
        evidence_root = Path(text(policy["evidence_root"])).absolute()
        if evidence_root.is_symlink():
            raise SupportError("path_refused", "Protected evidence root cannot be a symlink")
        if Path(text(surface["root"])).absolute() != evidence_root:
            raise SupportError("result_surface_denied", "Product-selected evidence root differs from policy")
        for name in ("max_message_bytes", "max_files", "max_bytes", "max_history_records", "max_wait_ms"):
            integer(as_object(policy["limits"])[name], "limits." + name, 1)
        for name in ("grants", "predicates", "operators", "executors", "event_sinks"):
            as_object(policy[name])
        for grant_id, value in as_object(policy["grants"]).items():
            grant = as_object(value)
            exact_keys(grant, ("id", "authority_sources", "outcome", "principals", "targets", "operations", "tools", "executors", "territory", "preconditions", "admission", "notification_sink"), label="grant")
            if grant["id"] != grant_id:
                raise SupportError("contract_violation", "Grant key/id mismatch")
            _admission_selection(grant["admission"])
            for t in as_list(grant["territory"]):
                territory = as_object(t)
                validate_schema(territory, _SCOPE)
                root = as_object(roots[text(territory["root"])])
                base = Path(text(root["path"])).resolve()
                candidate = base / _relative(text(territory["path"]))
                if _overlaps(candidate, evidence_root) or _overlaps(candidate, policy_path):
                    raise SupportError("role_effect_denied", "Writer territory aliases protected policy/evidence")
                for other in roots.values():
                    configured = as_object(other)
                    if configured["writable"] is False and _overlaps(candidate, Path(text(configured["path"])).resolve()):
                        raise SupportError("role_effect_denied", "Writer territory aliases protected source root")
            sink = grant["notification_sink"]
            if "dispatch.start" in _strings(grant["operations"]) and sink is None:
                raise SupportError("contract_violation", "Dispatch grant requires explicit notification sink")
            if sink is not None and text(sink) not in as_object(policy["event_sinks"]):
                raise SupportError("contract_violation", "Unknown Grant-selected notification sink")
        runtime = cls(policy_path, expected_sha256, principal, policy,
                      as_object(principals[principal]), evidence_root,
                      resolve_artifact, query_artifacts)
        actual_profile = read_source(runtime, as_object(profile["source"]))
        if actual_profile["parent_sha256"] != PROFILE_SHA256:
            raise SupportError("unsupported_contract", "Profile content is not the supported exact binding")
        read_source(runtime, as_object(product["definition"]))
        read_source(runtime, as_object(runtime.principal["role_binding"]))
        return runtime

    def with_callbacks(self, resolve_artifact: Resolver, query_artifacts: History) -> Runtime:
        return replace(self, resolve_artifact=resolve_artifact, query_artifacts=query_artifacts)


def _strings(value: JSON) -> list[str]:
    return [text(x) for x in as_list(value)]


def _admission_selection(value: JSON) -> Object:
    admission = as_object(value)
    exact_keys(admission, ("mechanism_id", "mechanism_source", "authority_source",
                          "required_predicates", "allowed_override_sources"),
               ("required_reconciliation_predicates",), label="admission selection")
    _strings(admission["required_predicates"])
    if "required_reconciliation_predicates" in admission:
        _strings(admission["required_reconciliation_predicates"])
    return admission


def _unique(values: list[str], label: str) -> None:
    if len(values) != len(set(values)):
        raise SupportError("contract_violation", "Duplicate " + label)


def _relative(value: str) -> Path:
    if not value or "\x00" in value or "\\" in value or value.startswith("/"):
        raise SupportError("path_refused", "Only unambiguous relative paths are supported")
    parts = value.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise SupportError("path_refused", "Ambiguous or escaped relative path")
    return Path(*parts)


def _overlaps(a: Path, b: Path) -> bool:
    return a == b or a in b.parents or b in a.parents


def _regular_bytes(path: Path) -> bytes:
    try:
        info = path.lstat()
        if not stat.S_ISREG(info.st_mode):
            raise SupportError("path_refused", "Expected a regular non-symlink file: " + str(path))
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            raw = stream.read()
            after = os.fstat(stream.fileno())
        if (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise SupportError("dependency_changed", "File changed during acquisition: " + str(path))
        return raw
    except SupportError:
        raise
    except FileNotFoundError as exc:
        raise SupportError("source_missing", "Missing source: " + str(path)) from exc
    except OSError as exc:
        raise SupportError("observation_unavailable", "Cannot acquire source: " + str(exc)) from exc


def _root(runtime: Runtime, root_id: str) -> Object:
    roots = as_object(runtime.policy["sources"])
    if root_id not in roots:
        raise SupportError("acquisition_denied", "Unregistered source root")
    return as_object(roots[root_id])


def _allowed(root: Object, relative: str) -> bool:
    for value in as_list(root["read_scope"]):
        scope = as_object(value)
        prefix = text(scope["path"])
        if relative == prefix or (scope["kind"] == "directory" and relative.startswith(prefix + "/")):
            return True
    return False


def source_path(runtime: Runtime, ref: Object, *, write: bool = False,
                allow_absent: bool = False) -> Path:
    if ref.get("engine") != "workspace-regular-file":
        raise SupportError("unsupported_contract", "Local path requires a workspace regular-file source")
    root = _root(runtime, text(ref.get("root")))
    relative = text(ref.get("path"))
    member = _relative(relative)
    if not _allowed(root, relative):
        raise SupportError("acquisition_denied", "Source path is outside the configured read scope")
    if write and root["writable"] is not True:
        raise SupportError("role_effect_denied", "Source root is not a configured Writer root")
    base = Path(text(root["path"])).resolve(strict=True)
    current = base
    for index, part in enumerate(member.parts):
        current = current / part
        try:
            info = current.lstat()
        except FileNotFoundError:
            if allow_absent and index == len(member.parts) - 1:
                return current
            raise SupportError("source_missing", "Missing path component: " + str(current)) from None
        if stat.S_ISLNK(info.st_mode):
            raise SupportError("path_refused", "Symlink path components are refused")
        if index < len(member.parts) - 1 and not stat.S_ISDIR(info.st_mode):
            raise SupportError("path_refused", "Intermediate path is not a directory")
    if write and (_overlaps(current, runtime.evidence_root) or _overlaps(current, runtime.policy_path)):
        raise SupportError("role_effect_denied", "Writer target aliases protected policy/evidence")
    return current


def read_source(runtime: Runtime, ref: Object) -> Object:
    validate_content(ref, "SourceRef")
    engine = text(ref["engine"])
    raw: bytes
    acquisition: Object = document({})
    if engine == "workspace-regular-file":
        if ref["object"] is not None:
            raise SupportError("contract_violation", "Workspace source has no Git object")
        raw = _regular_bytes(source_path(runtime, ref))
    elif engine == "immutable-git-blob":
        root = _root(runtime, text(ref["root"]))
        relative = text(ref["path"])
        _relative(relative)
        if root["kind"] != "git" or not _allowed(root, relative):
            raise SupportError("acquisition_denied", "Git source is outside registered immutable scope")
        obj = text(ref["object"])
        if re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", obj) is None:
            raise SupportError("contract_violation", "Git source requires a full exact object id")
        executable = Path("/usr/bin/git")
        executable_raw = _regular_bytes(executable)
        environment = {"PATH": "/usr/bin:/bin", "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                       "GIT_OPTIONAL_LOCKS": "0", "GIT_TERMINAL_PROMPT": "0", "GIT_NO_REPLACE_OBJECTS": "1", "GIT_NO_LAZY_FETCH": "1"}
        common = [str(executable), "--no-optional-locks", "-c", "core.hooksPath=" + os.devnull,
                  "-c", "core.fsmonitor=false", "-c", "core.useReplaceRefs=false", "-C", text(root["path"])]
        try:
            listing = subprocess.run(common + ["ls-tree", "-z", obj, "--", relative], env=environment, capture_output=True, timeout=30, check=False)
            if listing.returncode != 0:
                raise SupportError("source_missing", "Exact Git tree/member acquisition failed")
            rows = listing.stdout.split(b"\0")
            matched = [row for row in rows if row and row.split(b"\t", 1)[-1] == relative.encode()]
            if len(matched) != 1:
                raise SupportError("source_missing", "Exact Git member is absent/ambiguous")
            metadata = matched[0].split(b"\t", 1)[0].split()
            if metadata[0] not in (b"100644", b"100755") or metadata[1] != b"blob":
                raise SupportError("path_refused", "Git source is not a regular blob")
            blob = metadata[2].decode("ascii")
            result = subprocess.run(common + ["cat-file", "blob", blob], env=environment, capture_output=True, timeout=30, check=False)
            if result.returncode != 0:
                raise SupportError("source_missing", "Exact Git blob unavailable; lazy fetching is disabled")
            raw = result.stdout
            acquisition = {"git_executable": {"path": str(executable), "sha256": _sha(executable_raw)}, "object": obj,
                           "blob": blob, "mode": metadata[0].decode(), "configuration_scope": "registered repository plus explicit isolated environment/read-only overrides; no hooks/filters/checkout/lazy fetch"}
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise SupportError("observation_unavailable", "Git acquisition unavailable: " + str(exc)) from exc
    elif engine == "retained-evidence":
        if ref["object"] is not None or runtime.resolve_artifact is None:
            raise SupportError("basis_missing", "Retained source requires the protected artifact resolver")
        if text(ref["root"]) != "evidence":
            raise SupportError("acquisition_denied", "Retained source must use the protected evidence alias")
        ident = text(ref["path"])
        raw = runtime.resolve_artifact({"id": ident, "sha256": ref["sha256"]})
    else:
        raise SupportError("unsupported_contract", "Unsupported source engine")
    if _sha(raw) != ref["sha256"]:
        raise SupportError("digest_mismatch", "Acquired whole source differs from pinned bytes", source_refs=[ref])
    selected = raw
    coordinates: JSON = None
    selector = ref["selector"]
    if selector is not None:
        selection = as_object(selector)
        if "lines" in selection:
            first, last = [integer(v, "line", 1) for v in as_list(selection["lines"])]
            try:
                lines = raw.decode("utf-8").splitlines(keepends=True)
            except UnicodeError as exc:
                raise SupportError("domain_invalid", "Line selection requires UTF-8") from exc
            if first > last or last > len(lines):
                raise SupportError("basis_missing", "Selected original line coordinates do not exist")
            selected = "".join(lines[first - 1:last]).encode()
            coordinates = {"lines": [first, last]}
        else:
            selected = canonical(pointer(parse_json(raw), cast(str, selection["json_pointer"])))
            coordinates = selection
    return document({"source": ref, "parent_sha256": _sha(raw), "selected_sha256": _sha(selected),
            "size_bytes": len(selected), "content_base64": base64.b64encode(selected).decode("ascii"),
            "coordinates": coordinates, "acquisition": acquisition})


def _source_bytes(runtime: Runtime, ref: Object) -> bytes:
    return base64.b64decode(text(read_source(runtime, ref)["content_base64"]))


def _source_json(runtime: Runtime, ref: Object, kind: str | None = None) -> Object:
    value = parse_json(_source_bytes(runtime, ref))
    return validate_content(value, kind) if kind is not None else as_object(value)


def load_artifact(runtime: Runtime, ref: Object, expected_kind: str | None = None) -> Object:
    validate_content(ref, "ArtifactRef")
    if ref["id"] != "sha256:" + text(ref["sha256"]):
        raise SupportError("contract_violation", "Artifact id and digest must agree")
    if runtime.resolve_artifact is None:
        raise SupportError("basis_missing", "Protected artifact resolver is not configured")
    raw = runtime.resolve_artifact(ref)
    if _sha(raw) != ref["sha256"]:
        raise SupportError("digest_mismatch", "Retained envelope digest differs")
    value = as_object(parse_json(raw))
    exact_keys(value, ("schema", "kind", "provenance", "payload"), label="artifact")
    if value["schema"] != ARTIFACT or value["kind"] not in KINDS or canonical(value) != raw:
        raise SupportError("contract_violation", "Retained envelope has unsupported/noncanonical shape")
    if expected_kind is not None and value["kind"] != expected_kind:
        raise SupportError("basis_missing", "Artifact has wrong kind for this input")
    return value


def provenance(runtime: Runtime, request: Object, started_ns: int, ended_ns: int,
               target: str | None = None, attempt: Object | None = None) -> Object:
    product = as_object(runtime.policy["product"])
    return document({"request_id": request["id"], "request_sha256": digest(request),
            "requester_principal": runtime.principal_id, "target_principal": target,
            "product_id": product["definition_id"], "definition_sha256": as_object(product["definition"])["sha256"],
            "method_profile_sha256": PROFILE_SHA256, "policy_sha256": runtime.policy_sha256,
            "actor": copy.deepcopy(runtime.principal), "attempt": attempt,
            "observed_interval": document({"clock": "unix_ns", "started_ns": started_ns, "ended_ns": ended_ns})})


def make_artifact(kind: str, payload: JSON, provenance: Object) -> tuple[Object, Object]:
    if kind not in KINDS:
        raise SupportError("unsupported_contract", "Unknown retained artifact kind")
    exact_keys(provenance, ("request_id", "request_sha256", "requester_principal", "target_principal", "product_id", "definition_sha256", "method_profile_sha256", "policy_sha256", "actor", "attempt", "observed_interval"), label="provenance")
    envelope: Object = document({"schema": ARTIFACT, "kind": kind, "provenance": copy.deepcopy(provenance), "payload": copy.deepcopy(payload)})
    sha = digest(envelope)
    return envelope, {"id": "sha256:" + sha, "sha256": sha}


def require_operation(runtime: Runtime, operation: str) -> None:
    if _sha(_regular_bytes(runtime.policy_path)) != runtime.policy_sha256:
        raise SupportError("basis_stale", "Trusted policy changed; no hot reload or stale authority use")
    if operation not in _strings(runtime.principal["operations"]):
        raise SupportError("authority_missing", "Startup principal has no selected operation capability")


def _binding(runtime: Runtime) -> Object:
    product = as_object(runtime.policy["product"])
    return document({"policy_sha256": runtime.policy_sha256, "product_definition": product["definition"],
            "method_profile": as_object(runtime.policy["method_profile"])["source"]})


def observe(runtime: Runtime, scope: list[JSON]) -> Object:
    started = time.time_ns()
    entries: dict[tuple[str, str], Object] = {}
    max_files = integer(as_object(runtime.policy["limits"])["max_files"], minimum=1)
    max_bytes = integer(as_object(runtime.policy["limits"])["max_bytes"], minimum=1)
    total = 0
    for raw in scope:
        item = as_object(raw)
        validate_schema(item, _SCOPE)
        root_id = text(item["root"]); relative = text(item["path"])
        fake: Object = document({"engine": "workspace-regular-file", "root": root_id, "path": relative})
        path = source_path(runtime, fake, allow_absent=True)
        candidates: list[tuple[str, Path]] = [(relative, path)]
        if path.exists() and item["kind"] == "directory":
            if not path.is_dir():
                raise SupportError("domain_invalid", "Declared observation directory is not a directory")
            for folder, directories, files in os.walk(path, followlinks=False):
                for member in sorted(directories + files):
                    child = Path(folder) / member
                    rel = relative + "/" + child.relative_to(path).as_posix()
                    source_path(runtime, {"engine": "workspace-regular-file", "root": root_id, "path": rel})
                    candidates.append((rel, child))
        for rel, member_path in candidates:
            if (root_id, rel) in entries:
                continue
            exists = member_path.exists()
            mode = member_path.lstat().st_mode if exists else 0
            if exists and not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
                raise SupportError("path_refused", "Observation encountered nonregular/symlink content")
            data = _regular_bytes(member_path) if stat.S_ISREG(mode) else b""
            total += len(data)
            if len(entries) >= max_files or total > max_bytes:
                raise SupportError("budget_exceeded", "Observation population/byte bound exceeded; no complete snapshot returned")
            entries[(root_id, rel)] = {"root": root_id, "path": rel, "exists": exists,
                                       "type": "file" if stat.S_ISREG(mode) else "directory" if exists else "absent",
                                       "size": len(data) if stat.S_ISREG(mode) else None,
                                       "sha256": _sha(data) if stat.S_ISREG(mode) else None}
    return document({"schema": "a_c.fd-support.observation/1", "scope": scope,
            "observed_interval": {"clock": "unix_ns", "started_ns": started, "ended_ns": time.time_ns()},
            "entries": [entries[key] for key in sorted(entries)], "bindings": _binding(runtime),
            "git": None, "diff": [], "gaps": []})


def observation_diff(previous: Object, current: Object) -> list[JSON]:
    before = {(text(as_object(x)["root"]), text(as_object(x)["path"])): x for x in as_list(previous["entries"])}
    after = {(text(as_object(x)["root"]), text(as_object(x)["path"])): x for x in as_list(current["entries"])}
    return [{"root": key[0], "path": key[1], "previous": before.get(key), "current": after.get(key)}
            for key in sorted(set(before) | set(after)) if not _equal(before.get(key), after.get(key))]


def check_preconditions(runtime: Runtime, recheck_set: Object) -> Object:
    exact_keys(recheck_set, ("schema", "policy_sha256", "product_definition", "method_profile", "sources", "observations", "executor_dependencies"))
    if recheck_set["schema"] != "a_c.fd-support.recheck/1":
        raise SupportError("unsupported_contract", "Unknown recheck contract")
    changes: list[JSON] = []; gaps: list[JSON] = []; observations: list[JSON] = []
    try:
        if _sha(_regular_bytes(runtime.policy_path)) != runtime.policy_sha256 or recheck_set["policy_sha256"] != runtime.policy_sha256:
            changes.append({"kind": "policy_changed"})
    except SupportError as exc:
        gaps.append(exc.document())
    refs = [recheck_set["product_definition"], recheck_set["method_profile"]] + as_list(recheck_set["sources"]) + as_list(recheck_set["executor_dependencies"])
    for value in refs:
        try:
            read_source(runtime, as_object(value))
        except SupportError as exc:
            gaps.append(exc.document())
    for value in as_list(recheck_set["observations"]):
        try:
            old = as_object(load_artifact(runtime, as_object(value), "observation")["payload"])
            fresh = observe(runtime, as_list(old["scope"]))
            diff = observation_diff(old, fresh)
            fresh["diff"] = diff
            observations.append(fresh)
            changes.extend(diff)
        except SupportError as exc:
            gaps.append(exc.document())
    return document({"observations": observations, "changes": changes, "gaps": gaps})


def _history(runtime: Runtime, kind: str, matches: Object) -> tuple[list[Object], Object]:
    if runtime.query_artifacts is None:
        raise SupportError("history_incomplete", "Protected cross-process history is unavailable")
    query = runtime.query_artifacts(kind, matches)
    exact_keys(query, ("refs", "complete", "gaps", "scope", "observed_at_ns"))
    records: list[Object] = []
    for value in as_list(query["refs"]):
        record = load_artifact(runtime, as_object(value), kind)
        if as_object(record["provenance"])["product_id"] != as_object(runtime.policy["product"])["definition_id"]:
            raise SupportError("history_incomplete", "History escaped its exact selected Product scope")
        for field, expected in matches.items():
            try:
                actual = pointer(record, "/" + field.replace(".", "/"))
            except SupportError as exc:
                raise SupportError("history_incomplete", "History returned an unmatching record") from exc
            if not _equal(actual, expected):
                raise SupportError("history_incomplete", "History returned an unmatching record")
        records.append(record)
    return records, query


def _profile_basis(runtime: Runtime, basis: Object, observations: bool = True) -> None:
    validate_content(basis, "Basis")
    identity = as_object(basis["method_profile"])
    if identity != {"id": PROFILE_ID, "sha256": PROFILE_SHA256}:
        raise SupportError("basis_stale", "Execution basis is not this exact selected method/profile")
    if observations:
        for ref in as_list(basis["observations"]):
            load_artifact(runtime, as_object(ref), "observation")


def _model(runtime: Runtime, model_ref: Object) -> ac_graph.Model:
    validate_content(model_ref, "ModelRef")
    raw = _source_bytes(runtime, as_object(model_ref["source"]))
    try:
        document = as_object(parse_json(raw))
        model = ac_graph.validate(document) if model_ref["format"] == "model" else ac_graph.decode(ac_graph.GraphCarrier(document))
    except ac_graph.Refusal as exc:
        raise SupportError("domain_invalid", "Model input cannot establish the declared structural basis: " + str(exc)) from exc
    if model.identity != model_ref["model_id"] or model.sha256 != model_ref["model_sha256"]:
        raise SupportError("digest_mismatch", "Decoded native model identity/digest mismatch")
    return model


def _record(model: ac_graph.Model, record_id: str) -> Object:
    try:
        return ac_graph.inspect(model, record_id)
    except ac_graph.Refusal as exc:
        raise SupportError("domain_invalid", "Unknown same-model record: " + record_id) from exc


def _selections(value: JSON) -> list[tuple[list[str], int | None]]:
    selections: list[tuple[list[str], int | None]] = []
    for raw in as_list(value):
        selection = as_object(raw)
        validate_schema(selection, _SELECTION)
        seeds = _strings(selection["seeds"])
        _unique(seeds, "selection seeds")
        budget = selection.get("budget_records")
        selections.append((seeds, None if budget is None else integer(budget)))
    return selections


def _project(model: ac_graph.Model, selections: JSON) -> list[JSON]:
    try:
        return cast(list[JSON], ac_graph.project_many(model, _selections(selections)))
    except ac_graph.Refusal as exc:
        raise SupportError("contract_violation", "Declared projection constraint cannot be satisfied: " + str(exc)) from exc


def _all_source_refs(value: JSON) -> list[Object]:
    refs: list[Object] = []
    if isinstance(value, dict):
        if set(value) == {"engine", "root", "path", "object", "sha256", "selector"}:
            validate_content(value, "SourceRef")
            refs.append(value)
        else:
            for item in value.values():
                refs.extend(_all_source_refs(item))
    elif isinstance(value, list):
        for item in value:
            refs.extend(_all_source_refs(item))
    return refs


def _target(runtime: Runtime, actor: Object) -> tuple[str, Object]:
    principals = as_object(runtime.policy["principals"])
    choices = [(name, as_object(value)) for name, value in principals.items()
               if as_object(value)["actor_id"] == actor.get("actor_id") and as_object(value)["role"] == actor.get("role")]
    if len(choices) != 1:
        raise SupportError("basis_ambiguous", "Packet actor/role does not bind exactly one registered target")
    return choices[0]


def _validate_packet(runtime: Runtime, packet: Object) -> tuple[str, Object]:
    groups: dict[str, tuple[str, ...]] = {
        "activation": ("id", "revision", "configuration"),
        "frame": ("id", "revision", "declaration", "evaluation", "result_algebra"),
        "subject_basis": ("subject", "method_profile", "product", "observations", "dependencies", "time_basis"),
        "attention": ("material_relations", "invariants", "semantic_sources", "exclusions", "prohibited_assumptions"),
        "actor_authority": ("actor_id", "role", "capability", "semantic", "evaluation", "operation", "decision", "acceptance", "publication", "territory", "tools"),
        "evidence_relations": ("admissible_evidence", "acquisition", "dependencies", "conjunction", "translation", "consumer", "return_contract"),
        "stop_change": ("invalidators", "stop_conditions", "residuals", "re_entry", "reconfiguration"),
        "profile_additions": (),
    }
    exact_keys(packet, tuple(groups), label="packet")
    for name, required in groups.items():
        if name != "profile_additions":
            exact_keys(as_object(packet[name]), required, label="packet." + name)
    for name in ("activation", "frame"):
        value = as_object(packet[name]); text(value["id"]); text(value["revision"])
    basis = as_object(packet["subject_basis"])
    validate_content(basis["subject"], "Identity")
    _profile_basis(runtime, {"method_profile": basis["method_profile"], "observations": basis["observations"]})
    product = as_object(basis["product"]); exact_keys(product, ("id", "definition"))
    registered = as_object(runtime.policy["product"])
    if product["id"] != registered["definition_id"] or not _equal(product["definition"], registered["definition"]):
        raise SupportError("basis_stale", "Packet Product definition differs from the selected exact Product")
    text(basis["time_basis"])
    actor = as_object(packet["actor_authority"])
    target_id, principal = _target(runtime, actor)
    for key in ("semantic", "evaluation", "operation", "decision", "acceptance", "publication"):
        if actor[key] is not None:
            validate_content(actor[key], "SourceRef")
    for territory_value in as_list(actor["territory"]):
        validate_schema(territory_value, _SCOPE)
    _strings(actor["tools"])
    for stop_value in as_object(packet["stop_change"]).values():
        as_list(stop_value)
    evidence = as_object(packet["evidence_relations"])
    text(evidence["consumer"])
    if evidence["translation"] is not None:
        raise SupportError("unsupported_translation", "Composite method translations are outside this fragment")
    additions = as_object(packet["profile_additions"])
    role = text(principal["role"]).lower()
    exact_keys(additions, (role,), label="profile additions")
    fields = {"worker": ("operation_grant_id", "mutation_subject", "territory"),
              "reviewer": ("claim", "composition", "population", "oracle", "ordinary_module_path", "falsification_condition", "independence", "assurance", "severity_scale"),
              "executive": ("product_role_map", "mandate", "frontier", "result_triage_ledger", "priority_policy", "conjunction", "disposition_grant")}
    extra = as_object(additions[role]); exact_keys(extra, fields[role], label=role + " additions")
    if role == "worker":
        text(extra["operation_grant_id"])
        validate_content(extra["mutation_subject"], "Identity")
        if not _equal(extra["territory"], actor["territory"]):
            raise SupportError("contract_violation", "Worker profile and operation territories disagree")
    for source in _all_source_refs(packet):
        validate_content(source, "SourceRef")
    return target_id, principal


def _acquisition(runtime: Runtime, request: Object, source: JSON, content: JSON,
                 started: int, ended: int, model: JSON = None,
                 selection: JSON = None, recipient: str | None = None,
                 derived_sources: list[JSON] | None = None) -> tuple[Object, Object]:
    payload: Object = document({"schema": "a_c.fd-support.acquisition/1",
                       "recipient": recipient if recipient is not None else runtime.principal["actor_id"],
                       "source": source, "model": model, "selection": selection,
                       "operation": request["operation"], "content_sha256": digest(content),
                       "channel": "actor-context" if recipient is not None else "public-response",
                       "delivery": document({"state": "prepared", "interval": document({"clock": "unix_ns", "started_ns": started, "ended_ns": ended})})})
    if derived_sources is not None:
        payload["derived_sources"] = derived_sources
    return make_artifact("acquisition", payload, provenance(runtime, request, started, ended))


def _assemble(runtime: Runtime, request: Object, args: Object, started: int) -> CoreOutcome:
    packet = as_object(args["packet"])
    target_id, target = _validate_packet(runtime, packet)
    late = [as_object(x) for x in as_list(args["late_acquisition"])]
    late_ids = {canonical(x) for x in late}
    refs: dict[bytes, Object] = {canonical(x): x for x in _all_source_refs(packet)}
    for raw in as_list(args["sources"]):
        ref = as_object(raw); refs[canonical(ref)] = ref
    sources: list[JSON] = []; artifacts: list[JSON] = []; acquisitions: list[JSON] = []
    for key, ref in sorted(refs.items()):
        if key in late_ids:
            # The route is checked; its bytes are not misreported as delivered.
            if ref["engine"] == "workspace-regular-file":
                source_path(runtime, ref)
            continue
        acquired = read_source(runtime, ref)
        sources.append(acquired)
        item, item_ref = _acquisition(runtime, request, ref, acquired, started, time.time_ns(), recipient=text(target["actor_id"]))
        artifacts.append(item); acquisitions.append(item_ref)
    projections: list[JSON] = []
    for raw in as_list(args["models"]):
        selected = as_object(raw); model_ref = as_object(selected["model"])
        projection = document({"model": model_ref, "views": _project(_model(runtime, model_ref), selected["selections"])})
        projections.append(projection)
        acquired_projection, projection_ref = _acquisition(runtime, request, model_ref["source"], projection, started, time.time_ns(), model_ref, selected["selections"], text(target["actor_id"]))
        artifacts.append(acquired_projection); acquisitions.append(projection_ref)
    boundaries: Object = document({"late_acquisition": cast(list[JSON], late), "semantic_sufficiency": "not assessed",
                          "projection_limits": "declared selected governing closure only", "acquired_sources": len(sources), "activation_identity": activation_identity(packet)})
    body: Object = document({"schema": "a_c.fd-support.actor-context/1", "packet": packet,
                    "projections": projections, "sources": sources,
                    "late_acquisition": cast(list[JSON], late), "boundaries": boundaries})
    rendered = PREFIX + canonical(body).decode("utf-8")
    measured = len(rendered.encode("utf-8"))
    envelope = as_object(args["envelope"]); host = as_object(envelope["host_context"])
    capacity = envelope["capacity_bytes"]
    fit_judgment: JSON = None; gaps: list[JSON] = []
    known_host: int | None = None
    if host["state"] in ("known", "bounded"):
        if host["bytes"] is None or host["evidence"] is None:
            gaps.append("Host contribution lacks exact bound evidence")
        else:
            read_source(runtime, as_object(host["evidence"]))
            known_host = integer(host["bytes"])
    else:
        gaps.append("Unmeasured host context")
    # Exact late bytes are counted without claiming delivery. No unknown read
    # is silently treated as a zero-byte allowance.
    late_total = 0; late_complete = True
    for ref in late:
        try:
            late_total += integer(read_source(runtime, ref)["size_bytes"])
        except SupportError as exc:
            late_complete = False; gaps.append(exc.document())
    if late and capacity is not None:
        late_complete = False
        gaps.append("Late acquisition tool/protocol framing is not a qualified full-active upper bound")
    if capacity is not None:
        cap = integer(capacity)
        lower = measured + late_total
        if lower > cap:
            core = "falsified"
        elif known_host is None or not late_complete:
            core = "indeterminate"
        else:
            core = "satisfied" if lower + known_host <= cap else "falsified"
        fit_judgment = {"predicate": "selected full-active-input utf8_bytes fit", "domain_outcome": {"stdin_bytes": measured, "late_bytes": late_total, "host_bytes": known_host, "capacity_bytes": cap},
                        "core_value": core, "subject": as_object(packet["subject_basis"])["subject"],
                        "basis": {"method_profile": as_object(packet["subject_basis"])["method_profile"], "observations": as_object(packet["subject_basis"])["observations"]},
                        "evidence": [], "limits": ["byte boundary only; no semantic sufficiency"], "gaps": gaps}
    fit: Object = document({"selected": capacity is not None, "stdin_bytes": measured, "capacity_bytes": capacity,
                   "late_bytes": late_total, "host_context": host, "judgment": fit_judgment, "gaps": gaps})
    payload: Object = document({"schema": "a_c.fd-support.context/1", "packet": packet, "projections": projections,
                       "sources": sources, "late_acquisition": cast(list[JSON], late), "boundaries": boundaries,
                       "rendered_utf8": rendered, "rendered_sha256": _sha(rendered.encode()),
                       "fit": fit, "observations": as_object(packet["subject_basis"])["observations"]})
    artifact, ref = make_artifact("context", payload, provenance(runtime, request, started, time.time_ns(), target_id))
    artifacts.append(artifact)
    return document({"result": {"artifact": ref, "value": {"fit": fit, "activation_identity": activation_identity(packet), "manifest": {"acquired": [{k: v for k, v in as_object(s).items() if k != "content_base64"} for s in sources], "late_acquisition": cast(list[JSON], late)}, "rendered_sha256": payload["rendered_sha256"], "boundaries": boundaries}},
            "artifacts": artifacts, "operation_outcome": operation_outcome("context.assemble"), "refusal": None, "acquisitions": acquisitions})


@dataclass(frozen=True)
class _Truth:
    value: JSON
    missing: tuple[str, ...] = ()
    invalid: tuple[str, ...] = ()


def _expression(expression: JSON, inputs: Object, depth: int = 0) -> _Truth:
    if depth > 64:
        raise SupportError("unsupported_check", "Predicate exceeds finite expression depth")
    expr = as_object(expression)
    if set(expr) == {"literal"}:
        return _Truth(expr["literal"])
    if set(expr) == {"input", "pointer"}:
        name = text(expr["input"])
        if name not in inputs:
            return _Truth(None, (name,))
        try:
            return _Truth(pointer(inputs[name], cast(str, expr["pointer"])))
        except SupportError:
            return _Truth(None, (name + ":" + cast(str, expr["pointer"]),))
    exact_keys(expr, ("op", "args"), label="predicate expression")
    op = text(expr["op"]); args = as_list(expr["args"])
    arity = {"equals": 2, "member": 2, "contains_all": 2, "not": 1}
    if op not in ("equals", "member", "contains_all", "all", "any", "not"):
        raise SupportError("unsupported_check", "Unsupported predicate primitive")
    if (op in arity and len(args) != arity[op]) or (op in ("all", "any") and not args):
        raise SupportError("unsupported_check", "Predicate primitive has wrong arity")
    values = [_expression(arg, inputs, depth + 1) for arg in args]
    missing = tuple(m for result in values for m in result.missing)
    invalid = tuple(m for result in values for m in result.invalid)
    if invalid:
        return _Truth(None, missing, invalid)
    if op in ("all", "any", "not"):
        bad = ["Boolean operand required" for result in values if not result.missing and type(result.value) is not bool]
        if bad:
            return _Truth(None, missing, tuple(bad))
        known = [result.value for result in values if not result.missing]
        if op == "all" and False in known:
            return _Truth(False, missing)
        if op == "any" and True in known:
            return _Truth(True, missing)
        if missing:
            return _Truth(None, missing)
        return _Truth(all(known) if op == "all" else any(known) if op == "any" else not known[0])
    if missing:
        return _Truth(None, missing)
    a, b = values[0].value, values[1].value
    if op == "equals":
        return _Truth(_equal(a, b))
    if not isinstance(b, list) or (op == "contains_all" and not isinstance(a, list)):
        return _Truth(None, (), ("finite array set operands required",))
    if op == "member":
        return _Truth(any(_equal(a, member) for member in b))
    # contains_all(set, required)
    if not isinstance(a, list):
        return _Truth(None, (), ("finite array set operand required",))
    return _Truth(all(any(_equal(required, member) for member in a) for required in b))


def evaluate_predicate(runtime: Runtime, predicate_id: str, inputs: Object,
                       subject: Object, basis: Object) -> Object:
    definitions = as_object(runtime.policy["predicates"])
    if predicate_id not in definitions:
        raise SupportError("unsupported_check", "Predicate is not registered")
    definition = as_object(definitions[predicate_id])
    exact_keys(definition, ("id", "source", "subject", "basis", "input_names", "expression", "limits"))
    if definition["id"] != predicate_id:
        raise SupportError("contract_violation", "Predicate registry id mismatch")
    read_source(runtime, as_object(definition["source"]))
    _validate_expression(definition["expression"])
    _profile_basis(runtime, basis)
    validate_content(subject, "Identity")
    if not _equal(subject, definition["subject"]) or not _equal(basis, definition["basis"]):
        return document({"predicate": definition["source"], "domain_outcome": None, "core_value": "invalid_basis", "subject": subject, "basis": basis,
                "evidence": [], "gaps": ["registered predicate subject/basis mismatch"], "limits": definition["limits"]})
    allowed = _strings(definition["input_names"])
    if set(inputs) - set(allowed):
        raise SupportError("contract_violation", "Undeclared predicate input binding")
    outcome = _expression(definition["expression"], inputs)
    if outcome.invalid:
        core = "invalid_basis"
    elif type(outcome.value) is bool:
        core = "satisfied" if outcome.value else "falsified"
    elif outcome.missing:
        core = "indeterminate"
    else:
        core = "invalid_basis"
    return document({"predicate": definition["source"], "domain_outcome": outcome.value,
            "core_value": core, "subject": subject, "basis": basis, "evidence": [],
            "gaps": list(outcome.missing), "domain_errors": list(outcome.invalid),
            "limits": definition["limits"]})


def _judgment(runtime: Runtime, ref: Object) -> Object:
    validate_content(ref, "JudgmentRef")
    envelope = load_artifact(runtime, as_object(ref["record"]))
    kind = envelope["kind"]
    payload = as_object(envelope["payload"])
    path = cast(str, ref["pointer"])
    if kind == "return":
        producer = as_object(payload["producer"])
        if producer.get("authenticated") is not True or not path.startswith("/payload/original/evaluations/"):
            raise SupportError("basis_missing", "Judgment is not an authenticated original performed evaluation")
        original = as_object(payload["original"])
        result = copy.deepcopy(as_object(pointer(envelope, path)))
        if set(result) != {"id", "predicate", "domain_outcome", "core_value", "evidence", "residuals", "invalidators"}:
            raise SupportError("basis_missing", "Judgment pointer must identify one performed evaluation")
        result["subject"] = original["subject"]; result["basis"] = original["basis"]
    elif kind == "operation":
        request = as_object(payload["request"])
        if request["operation"] not in ("checks.evaluate", "results.conjoin") or path != "/payload/response_without_evidence/result/value/judgment":
            raise SupportError("basis_missing", "Pointer is not an actually executed tool judgment")
        response = as_object(payload["response_without_evidence"])
        if response["status"] != "ok":
            raise SupportError("basis_missing", "Tool judgment was not returned")
        result = as_object(pointer(envelope, path))
    else:
        raise SupportError("basis_missing", "Imported/asserted JSON is not retained judgment provenance")
    if result.get("core_value") not in CORE_VALUES:
        raise SupportError("basis_missing", "Retained judgment has no actual core result")
    return result


def _condition(runtime: Runtime, condition: JSON, expected_subject: Object,
               basis: Object) -> tuple[str | None, list[JSON]]:
    if condition is None:
        return None, []
    proof = as_object(condition)
    if proof.get("evaluation") is None:
        return None, ["Missing actual condition judgment"]
    try:
        read_source(runtime, as_object(proof["predicate"]))
        result = _judgment(runtime, as_object(proof["evaluation"]))
        if not _equal(result["predicate"], proof["predicate"]) or not _equal(result["subject"], expected_subject) or not _equal(result["basis"], basis):
            return None, ["Condition predicate/target subject/basis mismatch"]
        _profile_basis(runtime, basis)
        return text(result["core_value"]), []
    except SupportError as exc:
        return None, [exc.document()]


def relation_query(runtime: Runtime, args: Object) -> Object:
    model_ref = as_object(args["model"]); model = _model(runtime, model_ref)
    source = as_object(args["declarations"])
    declarations = _source_json(runtime, source, "RelationDeclarations")
    if not _equal(declarations["model"], model_ref):
        raise SupportError("basis_stale", "Relation declaration ModelRef differs from the exact request")
    native = as_object(model.document["basis"])
    native_basis: Object = document({"id": native["id"], "sha256": digest(native)})
    native_subject = as_object(native["subject"])
    subject: Object = document({"id": native_subject["id"], "sha256": native_subject["sha256"]})
    if not _equal(declarations["model_basis"], native_basis) or not _equal(declarations["subject"], subject):
        raise SupportError("basis_stale", "Relation declaration native basis/represented subject mismatch")
    basis = as_object(declarations["basis"]); _profile_basis(runtime, basis)
    seeds = _strings(args["seeds"]); query = text(args["query"])
    if query == "path":
        if len(seeds) != 2:
            raise SupportError("contract_violation", "Path requires exactly two ordered seeds")
    else:
        _unique(seeds, "relation seeds")
    for record_id in seeds:
        _record(model, record_id)
    relations = [as_object(raw) for raw in as_list(declarations["relations"])]
    by_id = {text(edge["id"]): edge for edge in relations}
    if len(by_id) != len(relations):
        raise SupportError("contract_violation", "Duplicate relation identity")
    for edge in relations:
        _record(model, text(edge["source"])); _record(model, text(edge["target"]))
    governing = _strings(declarations["governing_kinds"]); _unique(governing, "governing kind")
    coverage = as_object(declarations["coverage"])
    obligations = _strings(coverage["obligations"]); _unique(obligations, "coverage obligation")
    for identity in obligations:
        _record(model, identity)
    mappings = [as_object(raw) for raw in as_list(coverage["mapped_support"])]
    _unique([text(row["obligation_id"]) for row in mappings], "support mapping")
    mapped: dict[str, list[str]] = {}
    for row in mappings:
        obligation = text(row["obligation_id"])
        if obligation not in obligations:
            raise SupportError("contract_violation", "Mapping obligation is undeclared")
        supports = _strings(row["support_ids"]); _unique(supports, "support record")
        for identity in supports:
            _record(model, identity)
        mapped[obligation] = supports
    unknowns = [as_object(raw) for raw in as_list(coverage["explicit_unknowns"])]
    _unique([text(row["obligation_id"]) for row in unknowns], "unknown obligation")
    if any(row["obligation_id"] not in obligations for row in unknowns):
        raise SupportError("contract_violation", "Unknown row names undeclared obligation")
    conditions: dict[tuple[str, str], JSON] = {}
    for raw in as_list(declarations["applicability"]):
        row = as_object(raw); target = as_object(row["target"])
        key = (text(target["kind"]), text(target["id"]))
        if key in conditions or (key[0] == "relation" and key[1] not in by_id) or (key[0] == "obligation" and key[1] not in obligations):
            raise SupportError("contract_violation", "Duplicate/dangling applicability target")
        conditions[key] = row["condition"]
    facts: dict[tuple[str, str], Object] = {}
    all_targets = [("relation", ident) for ident in by_id] + [("obligation", ident) for ident in obligations]
    for kind, ident in all_targets:
        target_coord: Object = document({"kind": kind, "id": ident})
        native_record = by_id[ident] if kind == "relation" else as_object(_record(model, ident)["record"])
        binding: Object = document({"model": {"id": model.identity, "sha256": model.sha256}, "model_basis": native_basis,
                           "subject": subject, "basis": basis, "target": target_coord, "target_sha256": digest(native_record)})
        expected: Object = document({"id": ident, "sha256": digest(binding)})
        present = (kind, ident) in conditions
        condition = conditions.get((kind, ident))
        core, gaps = _condition(runtime, condition, expected, basis) if present else (None, ["Applicability declaration absent"])
        condition_unresolved = not present or (condition is not None and core not in ("satisfied", "falsified"))
        facts[(kind, ident)] = {"target": target_coord, "declaration_present": present, "condition": condition,
                                "expected_subject": expected, "core_value": core,
                                "judgment": as_object(condition)["evaluation"] if condition is not None else None,
                                "excluded": core == "falsified", "unresolved": condition_unresolved, "gaps": gaps}
    retained = [edge for edge in relations if edge["kind"] in governing and facts[("relation", text(edge["id"]))]["excluded"] is not True]

    def closure(starts: list[str], reverse: bool = False) -> tuple[list[str], list[str]]:
        seen = set(starts); pending = sorted(starts); traversed: set[str] = set()
        while pending:
            current = pending.pop(0)
            for edge in sorted(retained, key=lambda item: text(item["id"])):
                before = text(edge["target"] if reverse else edge["source"])
                after = text(edge["source"] if reverse else edge["target"])
                if before == current:
                    traversed.add(text(edge["id"]))
                    if after not in seen:
                        seen.add(after); pending.append(after); pending.sort()
        return sorted(seen), sorted(traversed)

    records, traversed = closure(seeds[:1] if query == "path" else seeds, query == "impact")
    path: JSON = None
    if query == "path":
        import heapq
        pending_paths: list[tuple[int, tuple[str, ...], tuple[str, ...]]] = [(0, (seeds[0],), ())]
        best: dict[str, int] = {}
        while pending_paths:
            length, nodes, edges = heapq.heappop(pending_paths)
            current = nodes[-1]
            if current == seeds[1]:
                path = {"records": list(nodes), "relations": list(edges)}
                break
            if current in best and best[current] < length:
                continue
            best[current] = length
            for edge in retained:
                after = text(edge["target"])
                if edge["source"] == current and after not in nodes:
                    heapq.heappush(pending_paths, (length + 1, nodes + (after,), edges + (text(edge["id"]),)))
    unresolved: list[str] = []
    can_reach = closure([seeds[1]], True)[0] if query == "path" else []
    for edge in retained:
        relevant = (edge["target"] in records if query == "impact" else edge["source"] in records)
        if query == "path":
            relevant = relevant and edge["target"] in can_reach
        if relevant and facts[("relation", text(edge["id"]))]["unresolved"] is True:
            unresolved.append(text(edge["id"]))
    scoped = sorted(set(obligations) & set(records)) if query == "coverage" else []
    missing = sorted(ident for ident in scoped if not mapped.get(ident))
    coverage_result: JSON = None
    if query == "coverage":
        coverage_result = document({"scoped_population": scoped,
                           "declared_support_present": [{"obligation_id": ident, "support_ids": mapped[ident]} for ident in scoped if mapped.get(ident)],
                           "missing_declared_support": missing, "mapping_absent": [ident for ident in missing if ident not in mapped],
                           "empty_declared_support": [ident for ident in missing if ident in mapped],
                           "explicit_unknowns": sorted([row for row in unknowns if row["obligation_id"] in scoped], key=lambda row: text(row["obligation_id"])),
                           "required_missing": [ident for ident in missing if facts[("obligation", ident)]["excluded"] is not True]})
    result: Object = document({"schema": "a_c.fd-support.relation-query-result/1", "query": query, "declarations": source,
                      "model": model_ref, "model_basis": native_basis, "subject": subject, "basis": basis, "seeds": seeds,
                      "records": records, "relations": sorted(relations, key=lambda edge: text(edge["id"])),
                      "traversed_relations": traversed, "path": path, "coverage": coverage_result,
                      "applicability": [facts[key] for key in sorted(facts)],
                      "boundary": {"candidate_closure": bool(unresolved), "unresolved_traversal_relations": sorted(unresolved),
                                   "excluded_relations": sorted(ident for kind, ident in facts if kind == "relation" and facts[(kind, ident)]["excluded"] is True),
                                   "non_governing_relations": sorted(text(edge["id"]) for edge in relations if edge["kind"] not in governing),
                                   "unknown_obligations": sorted(ident for ident in scoped if facts[("obligation", ident)]["unresolved"] is True),
                                   "missing_mappings": sorted(ident for ident in scoped if ident not in mapped),
                                   "out_of_scope_obligations": sorted(set(obligations) - set(scoped)),
                                   "limits": ["authored same-model graph only", "no semantic dependency completeness", "mapping presence is not satisfaction", "no frontier or acceptance selection"]}})
    validate_content(result, "RelationQueryResult")
    return result


def _acquired(runtime: Runtime, reference: Object) -> JSON:
    if set(reference) == {"id", "sha256"}:
        return load_artifact(runtime, reference)
    raw = _source_bytes(runtime, reference)
    try:
        return parse_json(raw)
    except SupportError as exc:
        if exc.code != "malformed_request":
            raise
        return document({"source": reference, "raw_base64": base64.b64encode(raw).decode(), "format": "non-JSON acquired bytes"})


def _qualified_operator(runtime: Runtime, operator_id: str, plan_ref: Object) -> Object:
    operators = as_object(runtime.policy["operators"])
    if operator_id != "claude-rc9.conjunction/1" or operator_id not in operators:
        raise SupportError("unsupported_check", "Only the registered RC9 conjunction operator is supported")
    operator = as_object(operators[operator_id])
    exact_keys(operator, ("id", "source", "decision_authority", "rule", "plan_source", "qualification"))
    if operator["id"] != operator_id or operator["rule"] != "first_non_satisfied_in_plan_order" or not _equal(operator["plan_source"], plan_ref):
        raise SupportError("unqualified_operator", "Registered operator/rule/plan does not match")
    read_source(runtime, as_object(operator["source"])); read_source(runtime, as_object(operator["decision_authority"]))
    try:
        qualification = as_object(_acquired(runtime, as_object(operator["qualification"])))
        if qualification.get("schema") == ARTIFACT:
            qualification = as_object(qualification["payload"])
        required = ("schema", "operator_id", "definition_sha256", "rule", "method_profile", "implementation_sha256", "dependencies", "fragment", "proof_sources")
        exact_keys(qualification, required, label="external operator qualification")
        body: Object = {key: value for key, value in operator.items() if key != "qualification"}
        if qualification["schema"] != "a_c.fd-support.operator-qualification/1" or qualification["operator_id"] != operator_id or qualification["rule"] != operator["rule"] or qualification["definition_sha256"] != digest(body):
            raise SupportError("unqualified_operator", "External qualification binds a different operator definition/rule")
        if qualification["method_profile"] != {"id": PROFILE_ID, "sha256": PROFILE_SHA256} or qualification["implementation_sha256"] != _sha(_regular_bytes(Path(__file__))):
            raise SupportError("unqualified_operator", "External qualification is stale for actual implementation/profile")
        for dependency in as_list(qualification["dependencies"]):
            read_source(runtime, as_object(dependency))
        if not as_list(qualification["proof_sources"]) or not as_list(qualification["fragment"]):
            raise SupportError("unqualified_operator", "External qualification has no actual fragment/proof")
        for proof in as_list(qualification["proof_sources"]):
            _acquired(runtime, as_object(proof))
    except SupportError as exc:
        if exc.code == "unqualified_operator":
            raise
        raise SupportError("unqualified_operator", "External operator qualification could not bind", [exc.document()]) from exc
    return operator


def _evaluation_key(original: Object, attempt: JSON, evaluation: Object) -> Object:
    return document({"producer": as_object(original["actor"])["id"], "activation": original["activation"],
            "attempt": attempt, "evaluation_id": evaluation["id"]})


def _conjunction_returns(runtime: Runtime, references: list[JSON]) -> tuple[dict[str, list[Object]], list[JSON], list[JSON]]:
    candidates: dict[str, list[Object]] = {}; originals: list[JSON] = []; failures: list[JSON] = []
    seen: set[str] = set()
    for raw in references:
        ref = as_object(raw)
        if text(ref["id"]) in seen:
            continue
        seen.add(text(ref["id"]))
        payload = as_object(load_artifact(runtime, ref, "return")["payload"])
        originals.append({"record": ref, "original": payload["original"], "producer": payload["producer"]})
        if payload["original"] is None or as_object(payload["producer"]).get("authenticated") is not True or any(isinstance(gap, dict) and "binding" in gap for gap in as_list(as_object(payload["binding_checks"])["gaps"])):
            continue
        original = as_object(payload["original"])
        for raw_evaluation in as_list(original["evaluations"]):
            evaluation = as_object(raw_evaluation)
            key = _evaluation_key(original, payload["attempt"], evaluation)
            entry = document({"key": key, "evaluation": evaluation, "subject": original["subject"], "basis": original["basis"], "return": ref})
            candidates.setdefault(digest(key), []).append(entry)
            if evaluation["core_value"] == "falsified":
                failures.append(entry)
    return candidates, originals, failures


def _evaluation_identity(entry: Object) -> str:
    return digest({name: entry[name] for name in ("key", "evaluation", "subject", "basis")})


def _inherited_counterexamples(runtime: Runtime, references: list[JSON], current_returns: list[JSON],
                              subject: Object, basis: Object) -> tuple[set[str], list[JSON]]:
    """Revalidate typed original evidence; never import old mandatory order."""
    pending = list(references); visited: set[str] = set()
    plans: list[tuple[Object, Object, Object]] = []; returns = list(current_returns)
    eligible: set[str] = set(); gaps: list[JSON] = []
    maximum = integer(as_object(runtime.policy["limits"])["max_history_records"], minimum=1)
    while pending:
        ref = as_object(pending.pop())
        if text(ref["id"]) in visited:
            continue
        if len(visited) >= maximum:
            gaps.append({"cause": "inherited_history_exceeds_selected_limit", "limit": maximum}); break
        visited.add(text(ref["id"]))
        try:
            old = as_object(load_artifact(runtime, ref, "operation")["payload"])
            request = validate_request(old["request"])
            if request["operation"] != "results.conjoin":
                raise SupportError("basis_missing", "Inherited record is not a conjunction operation")
            args = as_object(request["arguments"])
            prior = as_object(as_object(as_object(old["response_without_evidence"])["result"])["value"])
            if not _equal(prior["plan"], args["plan"]):
                raise SupportError("basis_stale", "Inherited plan differs from its owning request")
            plan = _source_json(runtime, as_object(args["plan"]), "ConjunctionPlan")
            composite = as_object(plan["composite"]); judgment = as_object(prior["judgment"])
            if any(not _equal(item["subject"], subject) or not _equal(item["basis"], basis) for item in (composite, judgment)) or not _equal(args["current_observations"], basis["observations"]):
                raise SupportError("basis_stale", "Inherited counterexample is not on this exact subject/basis")
            read_source(runtime, as_object(plan["authority_source"]))
            read_source(runtime, as_object(composite["predicate"]))
            plans.append((ref, plan, args))
            returns.extend(as_list(args["returns"]))
            pending.extend(as_list(plan["inherited"]))
        except SupportError as error:
            gaps.append({"inherited": ref, "cause": error.document()})
    try:
        population, _, _ = _conjunction_returns(runtime, returns)
        for ref, plan, args in plans:
            candidates, _, _ = _conjunction_returns(runtime, as_list(args["returns"]))
            for raw in as_list(plan["assessments"]):
                assessment = as_object(raw)
                read_source(runtime, as_object(assessment["predicate"]))
                if not _equal(assessment["subject"], subject) or not _equal(assessment["basis"], basis):
                    raise SupportError("basis_stale", "Inherited assessment has another exact subject/basis")
                condition, condition_gaps = _condition(runtime, assessment["applicability"], subject, basis)
                if condition == "falsified":
                    continue
                if assessment["applicability"] is not None and condition != "satisfied":
                    gaps.append({"inherited": ref, "assessment": assessment["id"], "cause": "unresolved_applicability", "gaps": condition_gaps}); continue
                key = digest(assessment["key"])
                local = {_evaluation_identity(row): row for row in candidates.get(key, [])}
                complete = {_evaluation_identity(row): row for row in population.get(key, [])}
                if len(local) != 1 or len(complete) != 1:
                    gaps.append({"inherited": ref, "assessment": assessment["id"], "cause": "cardinality_conflict" if local else "not_performed_or_missing"}); continue
                entry = next(iter(local.values())); evaluation = as_object(entry["evaluation"])
                if not _equal(entry["subject"], subject) or not _equal(entry["basis"], basis) or not _equal(evaluation["predicate"], assessment["predicate"]):
                    gaps.append({"inherited": ref, "assessment": assessment["id"], "cause": "stale_wrong_subject_basis_or_predicate"}); continue
                if evaluation["core_value"] == "falsified":
                    eligible.add(_evaluation_identity(entry))
    except SupportError as error:
        gaps.append({"cause": error.document()})
    return eligible, gaps


def conjoin(runtime: Runtime, args: Object) -> Object:
    plan_ref = as_object(args["plan"])
    operator = _qualified_operator(runtime, text(args["operator_id"]), plan_ref)
    plan = _source_json(runtime, plan_ref, "ConjunctionPlan")
    if plan["operator_id"] != operator["id"] or plan["rule"] != operator["rule"] or not _equal(plan["decision_authority"], operator["decision_authority"]):
        raise SupportError("unqualified_operator", "Plan is not the exact externally qualified operator binding")
    read_source(runtime, as_object(plan["authority_source"]))
    composite = as_object(plan["composite"]); subject = as_object(composite["subject"]); basis = as_object(composite["basis"])
    read_source(runtime, as_object(composite["predicate"]))
    _profile_basis(runtime, basis)
    if not _equal(basis["observations"], args["current_observations"]):
        raise SupportError("basis_stale", "Conjunction current observations differ from selected composite")
    obligations = [as_object(raw) for raw in as_list(plan["required_obligations"])]
    assessments = [as_object(raw) for raw in as_list(plan["assessments"])]
    _unique([text(row["id"]) for row in obligations], "obligation")
    _unique([text(row["id"]) for row in assessments], "assessment")
    obligation_ids = {text(row["id"]) for row in obligations}
    required: set[str] = set(); applicability_gaps: list[JSON] = []
    for obligation in obligations:
        read_source(runtime, as_object(obligation["source"]))
        core, gaps = _condition(runtime, obligation["applicability"], subject, basis)
        if core != "falsified":
            required.add(text(obligation["id"]))
        if obligation["applicability"] is not None and core not in ("satisfied", "falsified"):
            applicability_gaps.append({"obligation": obligation["id"], "gaps": gaps})
    constraints = [as_object(raw) for raw in as_list(plan["required_constraints"])]
    for constraint in constraints:
        read_source(runtime, as_object(constraint["predicate"]))
    if any(row["obligation_id"] not in obligation_ids for row in constraints):
        raise SupportError("contract_violation", "Required constraint names undeclared obligation")
    candidates, originals, failures = _conjunction_returns(runtime, as_list(args["returns"]))
    inherited_gaps: list[JSON] = []
    planned_gaps: list[JSON] = []; coverage: set[str] = set(); applicable: list[Object] = []; conflicts: list[JSON] = []
    excluded: list[JSON] = []
    basis_disagreement = False
    for assessment in assessments:
        aid = text(assessment["id"])
        read_source(runtime, as_object(assessment["predicate"]))
        declared_coverage = _strings(assessment["coverage"])
        if set(declared_coverage) - obligation_ids:
            raise SupportError("contract_violation", "Assessment coverage names undeclared obligation")
        if not _equal(assessment["subject"], subject) or not _equal(assessment["basis"], basis):
            raise SupportError("unsupported_translation", "Only equal exact composite subject/bases are supported")
        core, gaps = _condition(runtime, assessment["applicability"], subject, basis)
        if core == "falsified":
            excluded.append(aid); continue
        coverage.update(declared_coverage)
        if assessment["applicability"] is not None and core != "satisfied":
            planned_gaps.append({"assessment": aid, "cause": "unresolved_applicability", "gaps": gaps}); continue
        options = candidates.get(digest(assessment["key"]), [])
        # Equal answer bytes from different return records with one actual key
        # are replay only when the original actual payloads are equal.
        distinct: dict[str, Object] = {}
        for option in options:
            distinct[digest({"evaluation": option["evaluation"], "subject": option["subject"], "basis": option["basis"]})] = option
        if len(distinct) != 1:
            cause = "cardinality_conflict" if distinct else "not_performed_or_missing"
            planned_gaps.append({"assessment": aid, "cause": cause})
            if distinct:
                conflicts.append({"assessment": aid, "results": list(distinct.values())})
            continue
        option = next(iter(distinct.values())); evaluation = as_object(option["evaluation"])
        if not _equal(option["subject"], subject) or not _equal(option["basis"], basis) or not _equal(evaluation["predicate"], assessment["predicate"]):
            planned_gaps.append({"assessment": aid, "cause": "stale_wrong_subject_basis_or_predicate", "historical": option}); continue
        applicable.append({"assessment": assessment, "result": option})
    inherited_required: set[str] = set(); inherited_coverage: set[str] = set()
    inherited_constraint_failures: list[JSON] = []
    obligation_records = {text(item["id"]): item for item in obligations if text(item["id"]) in required}
    for raw in as_list(plan["inherited"]):
        ref = as_object(raw)
        try:
            envelope = load_artifact(runtime, ref, "operation"); old = as_object(envelope["payload"])
            if as_object(old["request"])["operation"] != "results.conjoin":
                raise SupportError("basis_missing", "Inherited record is not a conjunction operation")
            response = as_object(old["response_without_evidence"])
            prior = as_object(as_object(response["result"])["value"])
            old_plan_ref = as_object(prior["plan"])
            old_plan = _source_json(runtime, old_plan_ref, "ConjunctionPlan")
            if not _equal(as_object(prior["judgment"])["subject"], subject) or not _equal(as_object(prior["judgment"])["basis"], basis):
                raise SupportError("basis_stale", "Inherited conjunction is not applicable here")
            failures.extend(as_list(prior["failures"])); inherited_gaps.extend(as_list(prior["planned_gaps"]))
            inherited_required.update(_strings(prior["required_obligations"])); inherited_coverage.update(_strings(prior["planned_coverage"]))
            inherited_constraint_failures.extend(as_list(prior["constraint_failures"]))
            for raw_obligation in as_list(old_plan["required_obligations"]):
                old_obligation = as_object(raw_obligation); old_id = text(old_obligation["id"])
                if old_id in _strings(prior["required_obligations"]):
                    if old_id in obligation_records and not _equal(as_object(obligation_records[old_id])["source"], old_obligation["source"]):
                        raise SupportError("contract_violation", "Inherited obligation identity collides on a different source")
                    obligation_records[old_id] = old_obligation
        except SupportError as exc:
            inherited_gaps.append({"inherited": ref, "cause": exc.document()})
    inherited_eligible, fresh_inherited_gaps = _inherited_counterexamples(runtime, as_list(plan["inherited"]), as_list(args["returns"]), subject, basis)
    inherited_gaps.extend(fresh_inherited_gaps)
    required.update(inherited_required); coverage.update(inherited_coverage)
    uncovered = sorted(required - coverage); planned_gaps.extend(inherited_gaps)
    planned_gaps.extend(applicability_gaps)
    core_value = "satisfied"
    for entry in applicable:
        assessment = as_object(entry["assessment"]); evaluation = as_object(as_object(entry["result"])["evaluation"])
        if assessment["mandatory"] is True and evaluation["core_value"] != "satisfied":
            core_value = text(evaluation["core_value"]); break
    constraint_failures: list[JSON] = list(inherited_constraint_failures)
    for failure in failures:
        f = as_object(failure); evaluation = as_object(f["evaluation"])
        for constraint in constraints:
            if constraint["obligation_id"] in required and _equal(evaluation["predicate"], constraint["predicate"]):
                admitted = [entry for entry in applicable if _evaluation_identity(as_object(entry["result"])) == _evaluation_identity(f)]
                if admitted or _evaluation_identity(f) in inherited_eligible:
                    constraint_failures.append({"failure": f, "required_constraint": constraint, "obligation": obligation_records[text(constraint["obligation_id"])]})
    if core_value == "satisfied":
        if basis_disagreement:
            core_value = "invalid_basis"
        elif planned_gaps or uncovered:
            core_value = "indeterminate"
        elif constraint_failures:
            core_value = "falsified"
    claim_values: dict[str, set[str]] = {}
    for entry in applicable:
        if as_object(entry["assessment"])["mandatory"] is True:
            result = as_object(as_object(entry["result"])["evaluation"])
            claim_values.setdefault(digest(result["predicate"]), set()).add(text(result["core_value"]))
    contradictory = any({"satisfied", "falsified"} <= values for values in claim_values.values())
    domain = "decision(holds)" if core_value == "satisfied" else "conflict" if core_value == "falsified" and contradictory else "decision(fails)" if core_value == "falsified" else core_value
    judgment: Object = document({"predicate": composite["predicate"], "domain_outcome": domain, "core_value": core_value,
                        "subject": subject, "basis": basis, "evidence": args["returns"],
                        "limits": ["exact externally qualified declared conjunction only; no authority transfer"]})
    return document({"judgment": judgment, "plan": plan_ref, "originals": originals, "applicable": applicable,
            "excluded": excluded, "failures": failures, "constraint_failures": constraint_failures,
            "planned_gaps": planned_gaps, "uncovered": uncovered, "conflicts": conflicts,
            "required_obligations": sorted(required), "planned_coverage": sorted(coverage), "obligation_records": list(obligation_records.values())})


def _grant(runtime: Runtime, grant_id: str, operation: str) -> Object:
    grants = as_object(runtime.policy["grants"])
    if grant_id not in grants:
        raise SupportError("authority_missing", "No existing registered grant")
    grant = as_object(grants[grant_id])
    if runtime.principal_id not in _strings(grant["principals"]) or operation not in _strings(grant["operations"]):
        raise SupportError("authority_missing", "Grant does not authorize this requester/operation")
    for raw in as_list(grant["authority_sources"]):
        read_source(runtime, as_object(raw))
    outcome = as_object(grant["outcome"]); exact_keys(outcome, ("id", "source"))
    text(outcome["id"]); read_source(runtime, as_object(outcome["source"]))
    return grant


def _admission_authority(runtime: Runtime) -> Object:
    product = as_object(runtime.policy["product"])
    definition_ref = as_object(product["definition"])
    definition = _source_json(runtime, definition_ref)
    binding = as_object(product["authority_binding"])
    selected = pointer(definition, text(binding["definition_locator"]))
    owner_ref = as_object(binding["owner_record"])
    matched = _equal(selected, owner_ref)
    if isinstance(selected, str) and definition_ref["engine"] == "workspace-regular-file" and owner_ref["engine"] == "workspace-regular-file":
        definition_path = source_path(runtime, definition_ref)
        owner_path = source_path(runtime, owner_ref)
        locator_path = selected.split("#", 1)[0]
        matched = bool(locator_path) and (definition_path.parent / locator_path).resolve() == owner_path.resolve()
    if not matched:
        raise SupportError("authority_missing", "Product-definition locator does not resolve the selected owner record")
    owner = _source_json(runtime, owner_ref)
    for field in ("mechanism", "result_surface", "scope"):
        if field not in owner or not _equal(owner[field], binding[field]):
            raise SupportError("authority_missing", "Actual Product-located owner record does not select mechanism/surface/scope")
    mechanism = as_object(binding["mechanism"])
    if mechanism["id"] != "product-policy-preflight/1":
        raise SupportError("unsupported_contract", "No alternative runtime admission mechanism is implemented")
    read_source(runtime, as_object(mechanism["source"]))
    if mechanism["implementation_sha256"] != _sha(_regular_bytes(Path(__file__))):
        raise SupportError("unqualified_operator", "Product-selected admission implementation digest is stale")
    surface = as_object(binding["result_surface"])
    if Path(text(surface["root"])).absolute() != runtime.evidence_root:
        raise SupportError("result_surface_denied", "Selected durable result surface differs")
    return binding


def _within(scope: Object, allowed: Object) -> bool:
    path = text(scope["path"]); parent = text(allowed["path"])
    return scope["root"] == allowed["root"] and (path == parent and (scope["kind"] == allowed["kind"] or allowed["kind"] == "directory") or allowed["kind"] == "directory" and path.startswith(parent + "/"))


def _role_transition(runtime: Runtime, operation: str, grant_id: str, subject: JSON,
                     territory: JSON) -> None:
    same_actor_executive = any(as_object(raw)["actor_id"] == runtime.principal["actor_id"] and as_object(raw)["role"] == "Executive" for raw in as_object(runtime.policy["principals"]).values())
    if runtime.principal["role"] == "Worker" and same_actor_executive:
        ref = runtime.principal["role_transition"]
        if ref is None:
            raise SupportError("transition_record_missing", "Same-actor Executive to Writer transition requires an existing record")
        record = _source_json(runtime, as_object(ref))
        required = ("actor_id", "old_activation", "new_activation", "old_frame", "new_frame", "operation", "grant_id", "subject", "territory", "authority_source")
        exact_keys(record, required)
        if record["actor_id"] != runtime.principal["actor_id"] or record["operation"] != operation or record["grant_id"] != grant_id or not _equal(record["subject"], subject) or not _equal(record["territory"], territory):
            raise SupportError("transition_record_missing", "Existing transition does not bind the actual Writer operation")
        read_source(runtime, as_object(record["authority_source"]))
        for key in ("old_activation", "new_activation", "old_frame", "new_frame"):
            text(record[key])


def _recheck(runtime: Runtime, sources: list[JSON], observations: list[JSON],
             executor_dependencies: list[JSON] | None = None) -> Object:
    product = as_object(runtime.policy["product"])
    return document({"schema": "a_c.fd-support.recheck/1", "policy_sha256": runtime.policy_sha256,
            "product_definition": product["definition"],
            "method_profile": as_object(runtime.policy["method_profile"])["source"],
            "sources": sources, "observations": observations,
            "executor_dependencies": executor_dependencies if executor_dependencies is not None else []})


def _effect_plan(runtime: Runtime, request: Object, target: str | None,
                 recheck: Object, payload: Object) -> EffectPlan:
    return document({"schema": "a_c.fd-support.effect-plan/1", "operation": request["operation"],
            "request_id": request["id"], "request_sha256": digest(request),
            "requester_principal": runtime.principal_id, "target_principal": target,
            "policy_sha256": runtime.policy_sha256, "recheck": recheck, "payload": payload})


def _context_material_sources(context: Object) -> list[JSON]:
    """Only declared acquired input positions, never their opaque contents."""
    sources: list[JSON] = []
    for acquired in as_list(context["sources"]):
        source = as_object(acquired)["source"]
        validate_content(source, "SourceRef")
        sources.append(source)
    for projection in as_list(context["projections"]):
        model = as_object(as_object(projection)["model"])
        validate_content(model, "ModelRef")
        # The complete model identity remains in the immutable Context. Its
        # exact source bytes are rechecked; new bytes never replace that model.
        sources.append(model["source"])
    fit = as_object(context["fit"])
    if fit["selected"] is True:
        host = as_object(fit["host_context"])
        if host["state"] in ("known", "bounded"):
            source = host["evidence"]
            if source is not None:
                validate_content(source, "SourceRef")
                sources.append(source)
            # Missing evidence already prevents the required fit guard from
            # succeeding; do not replace its existing gap with assumed bytes.
    return list({canonical(source): source for source in sources}.values())


def build_preflight(runtime: Runtime, request: Object) -> EffectPlan:
    validate_request(request); require_operation(runtime, "contract.preflight")
    if request["operation"] != "contract.preflight":
        raise SupportError("contract_violation", "Preflight receives only its whole named request")
    args = as_object(request["arguments"])
    authority = _admission_authority(runtime)
    context_ref = as_object(args["context"])
    context = as_object(load_artifact(runtime, context_ref, "context")["payload"])
    packet = as_object(context["packet"]); target_id, target = _validate_packet(runtime, packet)
    grant_id = text(args["grant_id"])
    grant = _grant(runtime, grant_id, "contract.preflight")
    executor_id = text(args["executor_id"])
    executors = as_object(runtime.policy["executors"])
    if executor_id not in executors:
        raise SupportError("unsupported_executor", "No registered exact executor")
    executor = as_object(executors[executor_id])
    exact_keys(executor, ("id", "executable", "argv", "dependencies", "cwd", "environment", "actor_id", "settings", "tools", "effect_scope", "stdin_mode", "stdout_decoder", "observers"))
    actor = as_object(packet["actor_authority"])
    evidence = as_object(packet["evidence_relations"])
    checks: list[JSON] = []; gaps: list[JSON] = []

    def guard(predicate: str, holds: bool, code: str) -> None:
        checks.append({"predicate": predicate, "domain_outcome": holds,
                       "core_value": "satisfied" if holds else "out_of_frame" if CODES[code] == "refused(authority)" else "invalid_basis",
                       "source_code": None if holds else code})
        if not holds:
            gaps.append({"code": code, "predicate": predicate})

    guard("registered requester-to-target authority", target_id in _strings(grant["targets"]), "authority_missing")
    guard("registered executor permission", executor_id in _strings(grant["executors"]), "authority_missing")
    guard("executor actor matches activated target", executor["actor_id"] == target["actor_id"], "basis_stale")
    guard("packet tools granted", set(_strings(actor["tools"])) <= set(_strings(grant["tools"])) and set(_strings(actor["tools"])) <= set(_strings(executor["tools"])), "authority_missing")
    permitted = [as_object(x) for x in as_list(grant["territory"])]
    guard("packet territory granted", all(any(_within(as_object(scope), parent) for parent in permitted) for scope in as_list(actor["territory"])), "authority_missing")
    if target["role"] in ("Executive", "Reviewer"):
        guard("nonmutating activated role", not as_list(actor["territory"]), "role_effect_denied")
    if target["role"] == "Worker":
        worker = as_object(as_object(packet["profile_additions"])["worker"])
        guard("Worker operation grant binding", worker["operation_grant_id"] == grant_id, "authority_missing")
        guard("Worker mutation subject", _equal(worker["mutation_subject"], as_object(packet["subject_basis"])["subject"]), "basis_stale")
    sink_id = grant["notification_sink"]
    sink: Object | None = None
    if "dispatch.start" in _strings(grant["operations"]):
        if sink_id is None or text(sink_id) not in as_object(runtime.policy["event_sinks"]):
            raise SupportError("contract_violation", "Dispatch grant requires exact registered notification binding")
        sink = as_object(as_object(runtime.policy["event_sinks"])[text(sink_id)])
        exact_keys(sink, ("kind", "directory", "consumer", "authority_source", "retention"))
        if sink["kind"] != "durable-file-events" or sink["retention"] != "indefinite":
            raise SupportError("unsupported_contract", "Unsupported sink kind/retention")
        _relative(text(sink["directory"]))
        if sink["consumer"] != evidence["consumer"]:
            raise SupportError("contract_violation", "Grant-selected sink consumer differs from activated packet")
        read_source(runtime, as_object(sink["authority_source"]))
    guard("Product result consumer", as_object(authority["result_surface"])["consumer"] == evidence["consumer"], "result_surface_denied")
    if executor["stdin_mode"] != "context-utf8":
        raise SupportError("unsupported_executor", "Unsupported executor stdin contract")
    executable = as_object(executor["executable"]); exact_keys(executable, ("path", "sha256"))
    if _sha(_regular_bytes(Path(text(executable["path"])))) != executable["sha256"]:
        raise SupportError("dependency_changed", "Executor executable preimage changed")
    argv = _strings(executor["argv"])
    if not argv or argv[0] != executable["path"] or not Path(text(executor["cwd"])).is_absolute():
        raise SupportError("unsupported_executor", "Fixed executor argv/cwd not bound to executable")
    if any(not isinstance(value, str) for value in as_object(executor["environment"]).values()):
        raise SupportError("unsupported_executor", "Executor environment must be an explicit string map")
    admission = _admission_selection(grant["admission"])
    if admission["mechanism_id"] != "product-policy-preflight/1":
        raise SupportError("unsupported_contract", "Unsupported selected admission mechanism")
    read_source(runtime, as_object(admission["mechanism_source"])); read_source(runtime, as_object(admission["authority_source"]))
    contract: Object = document({"context": context_ref, "grant_id": grant_id, "executor_id": executor_id,
                        "result_key": args["result_key"], "requester": runtime.principal_id,
                        "target": target_id, "policy_sha256": runtime.policy_sha256})
    contract_sha = digest(contract)
    observations = as_list(args["observations"])
    if not _equal(context["observations"], observations):
        guard("context observation currentness", False, "basis_stale")
    fit = as_object(context["fit"])
    fit_judgment = fit.get("judgment")
    if fit.get("selected") is True:
        guard("selected required full-active-input fit", isinstance(fit_judgment, dict) and fit_judgment.get("core_value") == "satisfied", "basis_missing")
    sources: list[JSON] = list(_all_source_refs(packet)) + _context_material_sources(context) + as_list(grant["authority_sources"]) + [as_object(grant["outcome"])["source"], admission["mechanism_source"], admission["authority_source"], as_object(as_object(runtime.policy["product"])["authority_binding"])["owner_record"]]
    if sink is not None:
        sources.append(sink["authority_source"])
    source_preconditions: list[JSON] = []
    for raw in as_list(grant["preconditions"]):
        ref = as_object(raw)
        if set(ref) == {"id", "sha256"}:
            observations = observations + [ref]
        else:
            source_preconditions.append(ref)
    sources.extend(source_preconditions)
    recheck = _recheck(runtime, sources, observations, as_list(executor["dependencies"]))
    fresh = check_preconditions(runtime, recheck)
    guard("fresh material sources and observation population", not as_list(fresh["changes"]) and not as_list(fresh["gaps"]), "dependency_changed")
    packet_basis = as_object(packet["subject_basis"])
    basis: Object = document({"method_profile": packet_basis["method_profile"], "observations": packet_basis["observations"]})
    for predicate_id in _strings(admission["required_predicates"]):
        evaluation = evaluate_predicate(runtime, predicate_id, _predicate_inputs(runtime, predicate_id, {"context": context, "grant": grant, "executor": executor, "observations": fresh}), as_object(packet_basis["subject"]), basis)
        checks.append(evaluation)
        if evaluation["core_value"] != "satisfied":
            gaps.append({"predicate_id": predicate_id, "core_value": evaluation["core_value"]})
    if "admission_record" in args:
        override = as_object(args["admission_record"])
        if not any(_equal(override, ref) for ref in as_list(admission["allowed_override_sources"])):
            raise SupportError("authority_missing", "Caller admission/override is not separately registered")
        actual = as_object(_acquired(runtime, override))
        if actual.get("contract_sha256") != contract_sha:
            raise SupportError("basis_stale", "Registered override binds another exact contract")
        # Its authorization is a separate fact; it never turns fit into satisfied.
        checks.append({"predicate": "registered exact override", "domain_outcome": actual, "core_value": "satisfied"})
    payload: Object = document({"schema": "a_c.fd-support.preflight/1", "context": context_ref,
                       "contract_sha256": contract_sha, "grant_id": grant_id, "executor_id": executor_id,
                       "result_key": args["result_key"], "requester": runtime.principal_id, "target": target_id,
                       "contract_state": "drafted", "decision": None, "state_evidence": [],
                       "mechanism": authority["mechanism"], "authority": authority,
                       "evaluations": checks, "recheck": recheck, "gaps": gaps})
    return _effect_plan(runtime, request, target_id, recheck, payload)


def check_writer_authority(runtime: Runtime, request: Object) -> None:
    """Current authority for this exact request, without target-byte planning."""
    validate_request(request); require_operation(runtime, "work.write")
    if request["operation"] != "work.write":
        raise SupportError("contract_violation", "Writer receives only its named whole request")
    if runtime.principal["role"] != "Worker":
        raise SupportError("role_effect_denied", "Executive/Reviewer cannot mutate an authoritative carrier")
    read_source(runtime, as_object(runtime.principal["role_binding"]))
    read_source(runtime, as_object(as_object(runtime.policy["method_profile"])["source"]))
    _admission_authority(runtime)
    for source in as_list(runtime.policy["authority_sources"]):
        read_source(runtime, as_object(source))
    args = as_object(request["arguments"]); grant_id = text(args["grant_id"])
    grant = _grant(runtime, grant_id, "work.write")
    admission = _admission_selection(grant["admission"])
    read_source(runtime, as_object(admission["mechanism_source"]))
    read_source(runtime, as_object(admission["authority_source"]))
    target = as_object(args["target"])
    exact_keys(target, ("engine", "root", "path", "object", "sha256", "selector"))
    if target["engine"] != "workspace-regular-file" or target["object"] is not None or target["selector"] is not None:
        raise SupportError("unsupported_contract", "Writer supports whole regular workspace files only")
    validate_schema(target["sha256"], _nullable(_ref("Sha256")))
    path = source_path(runtime, target, write=True, allow_absent=True)
    scope: Object = document({"root": target["root"], "path": target["path"], "kind": "file"})
    if not any(_within(scope, as_object(raw)) for raw in as_list(grant["territory"])):
        raise SupportError("role_effect_denied", "Target is outside the exact registered Writer territory")
    _role_transition(runtime, "work.write", grant_id, {"id": str(path), "sha256": target["sha256"]}, grant["territory"])


def prepare_write(runtime: Runtime, request: Object) -> EffectPlan:
    check_writer_authority(runtime, request)
    args = as_object(request["arguments"]); grant_id = text(args["grant_id"])
    grant = _grant(runtime, grant_id, "work.write")
    target = as_object(args["target"])
    path = source_path(runtime, target, write=True, allow_absent=target["sha256"] is None)
    exists = path.exists()
    if target["sha256"] is None:
        if exists:
            raise SupportError("target_conflict", "Writer requires an absent target preimage")
        before = b""
    else:
        before = _regular_bytes(path)
        if _sha(before) != target["sha256"]:
            raise SupportError("target_conflict", "Writer target preimage differs")
    record = as_object(args["record"])
    read_source(runtime, as_object(record["provenance"]))
    if args["interpretation"] is not None:
        read_source(runtime, as_object(as_object(args["interpretation"])["author"]))
    content = cast(str, record["text"]).encode("utf-8")
    intended = before + content if args["mode"] == "append" else content
    refs: list[JSON] = [ref for ref in _all_source_refs(grant)]
    refs.append(record["provenance"])
    if target["sha256"] is not None:
        refs.append(target)
    observations = as_list(args["observations"])
    for raw in as_list(grant["preconditions"]):
        ref = as_object(raw)
        if set(ref) == {"id", "sha256"}:
            observations = observations + [ref]
        else:
            refs.append(ref)
    recheck = _recheck(runtime, refs, observations)
    fresh = check_preconditions(runtime, recheck)
    if as_list(fresh["changes"]) or as_list(fresh["gaps"]):
        raise SupportError("dependency_changed", "Writer material preconditions advanced", [fresh])
    payload: Object = document({"target": target, "path": str(path), "mode": args["mode"], "record": record,
                       "interpretation": args["interpretation"], "intended_base64": base64.b64encode(intended).decode(),
                       "intended_sha256": _sha(intended), "grant_id": grant_id,
                       "requester": runtime.principal_id, "target_preimage": target["sha256"]})
    return _effect_plan(runtime, request, None, recheck, payload)


def _closed_format(original: Object) -> None:
    exact_keys(original, ("schema", "id", "frame", "activation", "subject", "basis", "actor", "consumer", "evaluations", "not_performed", "work_result", "residuals", "invalidators"))
    if original["schema"] != "a_c.fd-support.closed-return/1":
        raise SupportError("unsupported_contract", "Unsupported closed-return carrier")
    text(original["id"]); text(original["consumer"])
    frame = as_object(original["frame"]); exact_keys(frame, ("id", "revision")); text(frame["id"]); text(frame["revision"])
    validate_content(original["activation"], "Identity"); validate_content(original["subject"], "Identity")
    validate_content(original["basis"], "Basis")
    actor = as_object(original["actor"]); exact_keys(actor, ("id", "family", "authorship"))
    for value in actor.values():
        text(value)
    ids: list[str] = []
    for raw in as_list(original["evaluations"]):
        evaluation = as_object(raw)
        exact_keys(evaluation, ("id", "predicate", "domain_outcome", "core_value", "evidence", "residuals", "invalidators"))
        ids.append(text(evaluation["id"]))
        if evaluation["core_value"] not in CORE_VALUES:
            raise SupportError("contract_violation", "Closed evaluation has unsupported core value")
        validate_content(evaluation["predicate"], "SourceRef")
        for key in ("evidence", "residuals", "invalidators"):
            as_list(evaluation[key])
    _unique(ids, "performed evaluation")
    absent = _strings(original["not_performed"]); _unique(absent, "unperformed evaluation")
    if set(ids) & set(absent):
        raise SupportError("contract_violation", "An evaluation cannot be performed and not_performed")
    as_list(original["residuals"]); as_list(original["invalidators"])
    work = original["work_result"]
    if work is not None:
        result = as_object(work)
        exact_keys(result, ("value", "cause", "candidate", "evidence", "residuals"))
        if result["value"] not in ("candidate_ready", "refused", "incomplete", "re_entry_requested"):
            raise SupportError("unsupported_contract", "Unknown construction-availability refinement")
        text(result["cause"]); as_list(result["evidence"]); as_list(result["residuals"])
        if result["value"] == "candidate_ready" and result["candidate"] is None:
            raise SupportError("contract_violation", "candidate_ready has no exact candidate")


def _decode_output(raw: bytes, decoder: Object) -> Object:
    exact_keys(decoder, ("format", "pointer", "decode_json_string"))
    if decoder["format"] == "json":
        value = parse_json(raw)
        if decoder["pointer"] is not None:
            value = pointer(value, cast(str, decoder["pointer"]))
        if decoder["decode_json_string"] is True:
            if not isinstance(value, str):
                raise SupportError("domain_invalid", "Decoder selected a nonstring answer")
            value = parse_json(value.encode())
    elif decoder["format"] == "utf8":
        value = parse_json(raw)
    else:
        raise SupportError("unsupported_contract", "Unknown fixed stdout decoder")
    return as_object(value)


def _capture_return(runtime: Runtime, request: Object, args: Object, started: int) -> CoreOutcome:
    attempt_ref = as_object(args["attempt"])
    attempt = as_object(load_artifact(runtime, attempt_ref, "attempt")["payload"])
    raw_ref = as_object(args["payload"])
    raw_envelope = load_artifact(runtime, raw_ref, "raw"); raw_payload = as_object(raw_envelope["payload"])
    gaps: list[JSON] = []; authenticated = False
    raw_bytes = b""; original: JSON = None
    if raw_payload.get("schema") == "a_c.fd-support.process-output/1" and isinstance(raw_payload.get("bytes_base64"), str):
        try:
            raw_bytes = base64.b64decode(cast(str, raw_payload["bytes_base64"]), validate=True)
        except ValueError:
            gaps.append("Invalid retained raw output encoding")
        events, history = _history(runtime, "raw", {"payload.schema": "a_c.fd-support.attempt-event/1", "payload.attempt.id": attempt_ref["id"], "payload.kind": "output_finalized"})
        if history["complete"] is not True:
            gaps.append({"history": history})
        final_refs = {canonical(as_object(as_object(event["payload"])["data"]).get("stdout")) for event in events}
        final = [event for event in events if _equal(as_object(as_object(event["payload"])["data"]).get("stdout"), raw_ref)]
        producer = as_object(raw_payload.get("producer", {}))
        target_id = text(attempt["target"])
        principals = as_object(runtime.policy["principals"])
        expected = as_object(principals[target_id])
        selected_executor = attempt["executor"]
        executor_id = text(selected_executor) if isinstance(selected_executor, str) else text(as_object(selected_executor)["id"])
        registered_executor = as_object(as_object(runtime.policy["executors"])[executor_id])
        actual_invocation = as_object(attempt["invocation"])
        expected_executable = actual_invocation.get("executable", registered_executor["executable"])
        authenticated = bool(final) and len(final_refs) == 1 and producer.get("executor_id") == executor_id and _equal(producer.get("executable"), expected_executable) and _equal(raw_payload.get("decoder"), registered_executor["stdout_decoder"]) and raw_payload.get("complete") is True and raw_payload.get("stream") == "stdout" and raw_payload.get("slot") == "final_stdout_object" and _equal(raw_payload.get("attempt"), attempt_ref) and producer.get("principal_id") == target_id and _equal(producer.get("actor"), expected)
        if not authenticated:
            gaps.append("Unauthenticated final output: Attempt argument or equal bytes alone is insufficient")
        try:
            decoder = as_object(raw_payload["decoder"])
            original = _decode_output(raw_bytes, decoder)
            _closed_format(as_object(original))
        except SupportError as exc:
            gaps.append(exc.document()); original = None
    else:
        # Preserve imports exactly, but do not grant producer identity.
        raw_bytes = canonical(raw_payload)
        gaps.append("External/imported raw material is not authenticated in this increment")
        try:
            candidate = as_object(parse_json(raw_bytes)); _closed_format(candidate); original = candidate
        except SupportError as exc:
            gaps.append(exc.document())
    return_contract = _source_json(runtime, as_object(args["return_contract"]), "ReturnContract")
    context = as_object(load_artifact(runtime, as_object(attempt["context"]), "context")["payload"])
    packet = as_object(context["packet"]); _, target = _validate_packet(runtime, packet)
    if not _equal(as_object(packet["evidence_relations"])["return_contract"], args["return_contract"]) or return_contract["role"] != target["role"]:
        gaps.append("Return contract differs from the original activation role/source")
    if original is not None:
        returned_original = as_object(original)
        expected_coordinates: Object = document({"frame": {key: as_object(packet["frame"])[key] for key in ("id", "revision")}, "activation": activation_identity(packet), "subject": as_object(packet["subject_basis"])["subject"], "basis": {"method_profile": as_object(packet["subject_basis"])["method_profile"], "observations": as_object(packet["subject_basis"])["observations"]}, "actor": {"id": target["actor_id"], "family": target["family"], "authorship": target["authorship"]}, "consumer": as_object(packet["evidence_relations"])["consumer"]})
        for coordinate, expected_coordinate in expected_coordinates.items():
            if not _equal(returned_original[coordinate], expected_coordinate):
                gaps.append({"binding": coordinate, "historical": returned_original[coordinate], "expected": expected_coordinate})
    payload: Object = document({"schema": "a_c.fd-support.return/1", "attempt": attempt_ref,
                       "raw_payload": raw_ref, "return_contract": args["return_contract"], "original": original,
                       "producer": {"authenticated": authenticated, "actor": target, "principal_id": attempt["target"], "attempt": attempt_ref},
                       "transport": {"raw_sha256": _sha(raw_bytes), "complete": raw_payload.get("complete"), "slot": raw_payload.get("slot")},
                       "binding_checks": {"gaps": gaps, "format_valid": original is not None}})
    envelope, ref = make_artifact("return", payload, provenance(runtime, request, started, time.time_ns(), text(attempt["target"]), attempt_ref))
    return document({"result": {"artifact": ref, "value": payload}, "artifacts": [envelope], "operation_outcome": operation_outcome("return.capture"), "refusal": None, "acquisitions": []})


def activation_identity(packet: Object) -> Object:
    return document({"id": as_object(packet["activation"])["id"], "sha256": digest(packet)})


def _check_return(runtime: Runtime, args: Object) -> Object:
    envelope = load_artifact(runtime, as_object(args["return"]), "return"); payload = as_object(envelope["payload"])
    context = as_object(load_artifact(runtime, as_object(args["context"]), "context")["payload"])
    packet = as_object(context["packet"]); _, target = _validate_packet(runtime, packet)
    gaps = list(as_list(as_object(payload["binding_checks"])["gaps"]))
    original = payload["original"]
    if original is None:
        return document({"original": None, "checks": [], "gaps": gaps, "consumable": False, "duplicates": [], "conflicts": []})
    result = as_object(original); _closed_format(result)
    expected_frame = {key: as_object(packet["frame"])[key] for key in ("id", "revision")}
    expected_basis: Object = document({"method_profile": as_object(packet["subject_basis"])["method_profile"], "observations": args["observations"]})
    coordinates: Object = document({"frame": expected_frame, "activation": activation_identity(packet),
                           "subject": as_object(packet["subject_basis"])["subject"], "basis": expected_basis,
                           "consumer": args["consumer"],
                           "actor": {"id": target["actor_id"], "family": target["family"], "authorship": target["authorship"]}})
    checks: list[JSON] = []
    for name, expected in coordinates.items():
        holds = _equal(result[name], expected)
        checks.append({"predicate": "exact return " + name, "domain_outcome": holds, "core_value": "satisfied" if holds else "invalid_basis", "historical": result[name], "expected": expected})
        if not holds:
            gaps.append({"binding": name, "historical": result[name], "expected": expected})
    fresh = check_preconditions(runtime, _recheck(runtime, [], as_list(args["observations"])))
    if as_list(fresh["changes"]) or as_list(fresh["gaps"]):
        gaps.append({"currentness": fresh})
    contract = _source_json(runtime, as_object(payload["return_contract"]), "ReturnContract")
    performed = {text(as_object(raw)["id"]): as_object(raw) for raw in as_list(result["evaluations"])}
    absent = set(_strings(result["not_performed"]))
    required = [as_object(raw) for raw in as_list(contract["required_evaluations"])]
    _unique([text(raw["id"]) for raw in required], "required return evaluation")
    for expected in required:
        identity = text(expected["id"])
        if identity not in performed:
            gaps.append({"not_performed" if identity in absent else "missing_evaluation": identity})
        elif not _equal(performed[identity]["predicate"], expected["predicate"]):
            gaps.append({"wrong_predicate": identity})
        for route in as_list(performed.get(identity, {}).get("evidence", [])):
            try:
                _acquired(runtime, as_object(route))
            except SupportError as exc:
                gaps.append(exc.document())
    role = text(contract["role"]); proof = as_object(contract["proof"])
    if role in ("Executive", "Reviewer") and result["work_result"] is not None:
        gaps.append("Assessment/coordination return cannot assert Worker construction availability")
    if role == "Worker" and result["work_result"] is not None:
        work = as_object(result["work_result"])
        if work["value"] == "candidate_ready":
            if not as_list(work["evidence"]):
                gaps.append("candidate_ready has no acquired transition evidence")
            for source in as_list(proof["transition_sources"]):
                try:
                    read_source(runtime, as_object(source))
                except SupportError as exc:
                    gaps.append(exc.document())
            if isinstance(work["candidate"], dict) and "engine" in work["candidate"]:
                try:
                    read_source(runtime, work["candidate"])
                except SupportError as exc:
                    gaps.append(exc.document())
            else:
                gaps.append("Candidate identity lacks a directly acquired exact route")
    if role == "Reviewer":
        reviewer = as_object(as_object(packet["profile_additions"])["reviewer"])
        if not _equal(proof["claim"], reviewer["claim"]) or not _equal(proof["independence_policy"], runtime.policy["independence_policy"]):
            gaps.append("Reviewer proof claim/independence contract differs from selected activation")
        if proof["expectations"] is None:
            gaps.append("Required Reviewer source-derived expectation is missing")
        else:
            expectation = load_artifact(runtime, as_object(proof["expectations"]), "expectation")
            ep = as_object(expectation["payload"])
            if as_object(ep["producer"])["actor_id"] != target["actor_id"] or not _equal(ep["claim"], proof["claim"]) or as_object(ep["exposure_check"]).get("source_first_observed") is not True:
                gaps.append("Reviewer expectation/source-first producer relation is not established")
        for source in as_list(proof["proof_sources"]):
            try:
                read_source(runtime, as_object(source))
            except SupportError as exc:
                gaps.append(exc.document())
        if proof["comparison"] is not None:
            read_source(runtime, as_object(proof["comparison"]))
        if target["authorship"] == as_object(result["actor"])["authorship"]:
            # Equality here binds actual Reviewer producer. Nonauthorship of the
            # candidate remains a separately supplied policy/claim premise.
            checks.append({"predicate": "Reviewer producer binding", "domain_outcome": True, "core_value": "satisfied"})
    elif role == "Executive":
        executive = as_object(as_object(packet["profile_additions"])["executive"])
        if not _equal(proof["mandate"], executive["mandate"]) or not _equal(proof["disposition_authority"], executive["disposition_grant"]):
            gaps.append("Executive proof mandate/disposition binding differs")
        for consumed in as_list(proof["consumed_results"]):
            load_artifact(runtime, as_object(consumed))
        if proof["conjunction"] is not None:
            joined = as_object(load_artifact(runtime, as_object(proof["conjunction"]), "operation")["payload"])
            if as_object(joined["request"])["operation"] != "results.conjoin":
                gaps.append("Executive conjunction route is not an actual conjunction record")
    predicate_ids = _strings(args["predicates"])
    if set(predicate_ids) - set(_strings(proof["predicate_ids"])):
        raise SupportError("unsupported_check", "Return check predicate is not selected by the role contract")
    basis = as_object(result["basis"])
    history_records, query = _history(runtime, "return", {"payload.attempt.id": as_object(payload["attempt"])["id"]})
    duplicates: list[JSON] = []; conflicts: list[JSON] = []
    for other in history_records:
        other_payload = as_object(other["payload"])
        if _equal(other, envelope):
            duplicates.append({"id": "sha256:" + digest(other), "sha256": digest(other)})
        elif other_payload["original"] is not None:
            other_original = as_object(other_payload["original"])
            for raw in as_list(other_original["evaluations"]):
                evaluation = as_object(raw)
                key = text(evaluation["id"])
                if key in performed and not _equal(evaluation, performed[key]):
                    conflicts.append({"evaluation_id": key, "original": evaluation, "other": performed[key]})
    if query["complete"] is not True:
        gaps.append({"history": query})
    if conflicts:
        gaps.append("Conflicting final evaluation provenance requires authority disposition")
    for predicate_id in predicate_ids:
        checked = evaluate_predicate(runtime, predicate_id, _predicate_inputs(runtime, predicate_id, {"original": result, "context": context, "proof": proof, "history": query}), as_object(result["subject"]), basis)
        checks.append(checked)
        if checked["core_value"] != "satisfied":
            gaps.append({"selected_return_check": predicate_id, "core_value": checked["core_value"]})
    if as_object(payload["producer"])["authenticated"] is not True:
        gaps.append("Producer is unauthenticated")
    return document({"original": result, "checks": checks, "gaps": gaps, "consumable": not gaps,
            "duplicates": duplicates, "conflicts": conflicts, "not_performed": result["not_performed"]})


def transport_observation(runtime: Runtime, request: Object, response: Object,
                          interval: Object, bytes_sha256: str, byte_count: int) -> Object:
    operation_ref = as_object(response["evidence"])
    operation = as_object(load_artifact(runtime, operation_ref, "operation")["payload"])
    expected_response = copy.deepcopy(response); expected_response["evidence"] = None
    if not _equal(operation["request"], request) or not _equal(operation["response_without_evidence"], expected_response):
        raise SupportError("basis_stale", "Transport evidence does not bind the actual response/request")
    validate_content(interval, "Interval")
    if integer(interval["ended_ns"]) < integer(interval["started_ns"]):
        raise SupportError("domain_invalid", "Transport interval is reversed")
    acquisitions: list[JSON] = []
    for value in as_list(operation["acquisitions"]):
        ref = as_object(value); acquisition_payload = as_object(load_artifact(runtime, ref, "acquisition")["payload"])
        if acquisition_payload.get("channel") == "public-response" and acquisition_payload.get("recipient") == runtime.principal["actor_id"]:
            acquisitions.append(ref)
    payload: Object = document({"schema": "a_c.fd-support.transport-observation/1", "operation": operation_ref,
                       "response_sha256": digest(response), "request_sha256": digest(request),
                       "recipient": runtime.principal["actor_id"], "acquisitions": acquisitions,
                       "delivery": {"state": "write_flushed", "interval": interval},
                       "wire": {"sha256": bytes_sha256, "bytes": byte_count}})
    envelope, _ = make_artifact("acquisition", payload, provenance(runtime, request, integer(interval["started_ns"]), integer(interval["ended_ns"])))
    return envelope


def _source_overlap(a: Object, b: Object) -> bool:
    if any(not _equal(a.get(key), b.get(key)) for key in ("engine", "root", "path", "object", "sha256")):
        return False
    first = a["selector"]; second = b["selector"]
    if first is None or second is None:
        return True
    left = as_object(first); right = as_object(second)
    if "lines" in left and "lines" in right:
        l = as_list(left["lines"]); r = as_list(right["lines"])
        return integer(l[0]) <= integer(r[1]) and integer(r[0]) <= integer(l[1])
    if "json_pointer" in left and "json_pointer" in right:
        p = cast(str, left["json_pointer"]); q = cast(str, right["json_pointer"])
        return p == q or p.startswith(q + "/") or q.startswith(p + "/") or not p or not q
    return True  # mixed selectors cannot establish non-overlap mechanically


def _delivery_records(runtime: Runtime, acquisition_ref: Object, actor_id: str,
                      before_ns: int) -> tuple[bool, list[JSON]]:
    records, query = _history(runtime, "acquisition", {"payload.schema": "a_c.fd-support.transport-observation/1", "payload.recipient": actor_id})
    delivered = False; gaps: list[JSON] = []
    for record in records:
        payload = as_object(record["payload"])
        delivery = as_object(payload["delivery"]); interval = as_object(delivery["interval"])
        if any(_equal(acquisition_ref, ref) for ref in as_list(payload["acquisitions"])) and delivery["state"] == "write_flushed":
            operation = load_artifact(runtime, as_object(payload["operation"]), "operation")
            operation_provenance = as_object(operation["provenance"])
            if as_object(operation_provenance["actor"])["actor_id"] != actor_id:
                gaps.append("Transport record actual producer differs from recipient")
            elif integer(interval["ended_ns"]) < before_ns:
                delivered = True
            else:
                gaps.append("Source delivery ordering is overlapping or late")
    if query["complete"] is not True:
        gaps.append({"history": query})
    context_delivered, context_gaps = _context_delivery(runtime, acquisition_ref, actor_id, before_ns)
    delivered = delivered or context_delivered
    if not delivered:
        gaps.extend(context_gaps)
        gaps.append("No actual prior scoped source transport write is established")
    return delivered and not gaps, gaps


def _review(runtime: Runtime, request: Object, args: Object, started: int) -> CoreOutcome:
    phase = text(args["phase"]); claim_ref = as_object(args["claim"])
    claim = read_source(runtime, claim_ref)
    candidate_ref = args["candidate"]
    candidate = as_object(candidate_ref) if candidate_ref is not None else None
    candidate_population, population_complete, population_gaps = _review_claim_population(runtime, claim, candidate)
    sources: list[JSON] = []; artifacts: list[JSON] = []; acquisition_refs: list[JSON] = []
    # Claim bytes are authority acquired now, never an inferred semantic source map.
    requested = [claim_ref] + [as_object(raw) for raw in as_list(args["sources"])] + [as_object(raw) for raw in as_list(args["proof"])]
    if phase == "candidate":
        if candidate is None:
            raise SupportError("basis_missing", "Candidate phase needs exact candidate source")
        requested += candidate_population
        if args["comparison"] is not None:
            requested.append(as_object(args["comparison"]))
    elif args["expectations"] is not None:
        raise SupportError("contract_violation", "Expectation recording does not accept a candidate-phase expectation reference")
    unique_requested = {canonical(source): source for source in requested}
    for source in unique_requested.values():
        if phase == "expectation" and any(_source_overlap(source, member) for member in candidate_population):
            raise SupportError("contract_violation", "Expectation acquisition intersects exact candidate material")
        acquired = claim if _equal(source, claim_ref) else read_source(runtime, source)
        sources.append(acquired)
        envelope, ref = _acquisition(runtime, request, source, acquired, started, time.time_ns())
        artifacts.append(envelope); acquisition_refs.append(ref)
    history, query = _history(runtime, "acquisition", {"payload.schema": "a_c.fd-support.acquisition/1", "payload.recipient": runtime.principal["actor_id"]})
    exposure: list[JSON] = []; gaps: list[JSON] = list(population_gaps)
    if candidate_population:
        for record in history:
            payload = as_object(record["payload"])
            supplied_source = payload.get("source")
            delivered_sources = ([supplied_source] if isinstance(supplied_source, dict) else []) + [as_object(member) for member in as_list(payload.get("derived_sources", []))]
            if any(_source_overlap(delivered_source, member) for delivered_source in delivered_sources for member in candidate_population):
                interval = as_object(as_object(payload["delivery"])["interval"])
                if integer(interval["started_ns"]) <= started:
                    exposure.append(document({"acquisition": {"id": "sha256:" + digest(record), "sha256": digest(record)}, "scope": delivered_sources, "state": as_object(payload["delivery"])["state"], "interval": interval}))
    if query["complete"] is not True:
        gaps.append({"history": query})
    expectation_ref: JSON = None
    if phase == "expectation" and args["expectation_body"] is not None:
        if runtime.principal["role"] != "Reviewer":
            raise SupportError("role_effect_denied", "Only the fixed Reviewer can record its F_P expectation text")
        body = as_object(args["expectation_body"])
        for raw in as_list(body["source_inputs"]):
            ref = as_object(raw); source_input = load_artifact(runtime, ref, "acquisition")
            source_payload = as_object(source_input["payload"])
            if source_payload.get("recipient") != runtime.principal["actor_id"] or source_payload.get("schema") != "a_c.fd-support.acquisition/1":
                gaps.append("Expectation source input has wrong actual actor/type")
            else:
                supplied = source_payload.get("source")
                if isinstance(supplied, dict) and any(_source_overlap(supplied, member) for member in candidate_population):
                    gaps.append("Expectation input includes candidate exposure")
                _, delivery_gaps = _delivery_records(runtime, ref, text(runtime.principal["actor_id"]), started)
                gaps.extend(delivery_gaps)
        if not as_list(body["source_inputs"]):
            gaps.append("No actual prior source input for the supplied expectation")
        if exposure:
            gaps.append("Prior candidate material exposure is observed/potential")
        expectation_payload: Object = document({"schema": "a_c.fd-support.expectation/1", "claim": claim_ref,
                           "subject": candidate_ref, "producer": runtime.principal,
                           "text": body["text"], "source_inputs": body["source_inputs"],
                           "exposure_check": {"prior": exposure, "history": query, "gaps": gaps, "candidate_population": candidate_population, "population_complete": population_complete, "claim_parent_sha256": claim["parent_sha256"], "source_first_observed": not gaps and population_complete},
                           "external_exposure": "unknown"})
        envelope, expectation_ref = make_artifact("expectation", expectation_payload, provenance(runtime, request, started, time.time_ns()))
        artifacts.append(envelope)
    if phase == "candidate":
        if args["expectations"] is None:
            gaps.append("No prior recorded source-derived expectations")
        else:
            previous = load_artifact(runtime, as_object(args["expectations"]), "expectation")
            expect_payload = as_object(previous["payload"])
            if not _equal(expect_payload["claim"], claim_ref) or as_object(expect_payload["producer"])["actor_id"] != runtime.principal["actor_id"]:
                gaps.append("Expectation claim/producer differs from current Reviewer")
            if as_object(previous["provenance"])["observed_interval"] is not None:
                prior_interval = as_object(as_object(previous["provenance"])["observed_interval"])
                if integer(prior_interval["ended_ns"]) >= started:
                    gaps.append("Expectation/candidate acquisition order is not established")
            previous_scope = as_object(expect_payload["exposure_check"])
            if not _equal(previous_scope.get("candidate_population"), document({"population": candidate_population})["population"]) or previous_scope.get("claim_parent_sha256") != claim["parent_sha256"]:
                gaps.append("Candidate phase differs from expectation exact claim/population parent")
            gaps.extend(as_list(previous_scope["gaps"]))
            expectation_ref = args["expectations"]
    comparison: JSON = None
    if phase == "candidate" and candidate is not None and args["comparison"] is not None:
        candidate_bytes = _source_bytes(runtime, candidate); other_bytes = _source_bytes(runtime, as_object(args["comparison"]))
        comparison = {"byte_equal": candidate_bytes == other_bytes, "candidate_sha256": _sha(candidate_bytes), "comparison_sha256": _sha(other_bytes),
                      "meaning": "exact byte comparison only"}
    policy = runtime.policy["independence_policy"]
    independence: Object = document({"selected_policy": policy, "semantic_independence": "not certified", "external_exposure": "unknown"})
    if policy is not None:
        selected = _source_json(runtime, as_object(policy))
        exact_keys(selected, ("id", "authority_source", "claim_scope", "require_non_author", "allowed_family_pairs", "source_first", "mechanical_sharing", "predicates"))
        if selected["require_non_author"] is not True or selected["source_first"] is not True:
            raise SupportError("contract_violation", "Independence binding cannot weaken source nonauthorship/source-first conditions")
        read_source(runtime, as_object(selected["authority_source"]))
        independence["governing_conditions"] = selected
    value: Object = document({"phase": phase, "claim": claim_ref, "candidate_population": candidate_population, "population_complete": population_complete, "acquired": sources, "expectations": expectation_ref,
                     "exposure": exposure, "comparison": comparison, "independence": independence,
                     "gaps": gaps, "limits": ["acquisition/diff/exposure facts only; no severity, disposition or mental-independence certificate"]})
    return document({"result": {"artifact": expectation_ref, "value": value}, "artifacts": artifacts,
            "operation_outcome": operation_outcome("review.prepare"), "refusal": None, "acquisitions": acquisition_refs})


# Public pure verifier for the effect membrane; no new predicate/authority.
judgment = _judgment


def refresh(runtime: Runtime, args: Object) -> Object:
    previous_ref = as_object(args["previous"]); current_ref = as_object(args["current"])
    previous = as_object(load_artifact(runtime, previous_ref, "observation")["payload"])
    current = as_object(load_artifact(runtime, current_ref, "observation")["payload"])
    declarations_ref = as_object(args["declarations"])
    declarations = _source_json(runtime, declarations_ref, "RefreshDeclarations")
    invalidators = _source_json(runtime, as_object(args["invalidators"]), "Invalidators")
    read_source(runtime, as_object(declarations["authority_source"]))
    if invalidators["declarations_sha256"] != declarations_ref["sha256"]:
        raise SupportError("digest_mismatch", "Invalidators bind a different declarations source")
    old_basis = as_object(declarations["old_basis"]); new_basis = as_object(declarations["new_basis"])
    _profile_basis(runtime, old_basis); _profile_basis(runtime, new_basis)
    if not any(_equal(previous_ref, ref) for ref in as_list(old_basis["observations"])) or not any(_equal(current_ref, ref) for ref in as_list(new_basis["observations"])):
        raise SupportError("basis_stale", "Declared refresh bases do not bind actual previous/current observations")
    if not _equal(previous["scope"], current["scope"]):
        raise SupportError("basis_ambiguous", "Refresh observations have different scoped populations")
    nodes = [as_object(raw) for raw in as_list(declarations["nodes"])]
    checks = [as_object(raw) for raw in as_list(declarations["checks"])]
    _unique([text(node["id"]) for node in nodes], "dependency node")
    _unique([text(check["id"]) for check in checks], "refresh check")
    ids = {text(node["id"]) for node in nodes}
    source_by_id = {text(node["id"]): as_object(node["source"]) for node in nodes}
    for source in source_by_id.values():
        read_source(runtime, source)
    adjacency: dict[str, set[str]] = {identity: set() for identity in ids}
    for raw in as_list(declarations["dependencies"]):
        edge = as_object(raw); dependent = text(edge["dependent"]); dependency = text(edge["dependency"])
        if dependent not in ids or dependency not in ids:
            raise SupportError("contract_violation", "Dangling refresh dependency")
        read_source(runtime, as_object(edge["source"]))
        adjacency[dependent].add(dependency)
    for check in checks:
        if check["node"] not in ids:
            raise SupportError("contract_violation", "Check names missing dependency node")
    cover = set(_strings(declarations["impact_cover"]))
    if cover - ids:
        raise SupportError("contract_violation", "Conservative impact cover contains undeclared node")
    changes = observation_diff(previous, current)
    gaps: list[JSON] = []; event_nodes: set[str] = set(); matched_changes: set[tuple[str, str]] = set()
    event_ids: list[str] = []
    for raw in as_list(invalidators["events"]):
        event = as_object(raw); event_ids.append(text(event["id"]))
        selected = set(_strings(event["nodes"]))
        if selected - ids:
            raise SupportError("contract_violation", "Invalidator names undeclared node")
        valid = True
        if event["kind"] == "material_input_change":
            before = event["previous"]; after = event["current"]
            if before is None and after is None or _equal(before, after):
                valid = False
            for value in (before, after):
                if value is not None:
                    source = as_object(value)
                    matching = [as_object(change) for change in changes if as_object(change)["root"] == source["root"] and as_object(change)["path"] == source["path"]]
                    if not matching:
                        valid = False
                    else:
                        expected_entry = as_object(matching[0]["previous" if value is before else "current"]) if matching[0]["previous" if value is before else "current"] is not None else {}
                        if expected_entry.get("sha256") != source["sha256"]:
                            valid = False
                        matched_changes.add((text(source["root"]), text(source["path"])))
            for evidence in as_list(event["evidence"]):
                load_artifact(runtime, as_object(evidence))
            if not as_list(event["evidence"]):
                valid = False
        elif event["kind"] == "changed_basis":
            valid = _equal(event["previous"], old_basis) and _equal(event["current"], new_basis) and not _equal(old_basis, new_basis) and bool(as_list(event["evidence"]))
            for evidence in as_list(event["evidence"]):
                load_artifact(runtime, as_object(evidence))
        else:
            read_source(runtime, as_object(event["declaration"]))
            observation = load_artifact(runtime, as_object(event["observation"]))
            triggers = [ref for raw_result in as_list(args["results"]) for ref in _all_source_refs(load_artifact(runtime, as_object(raw_result)))]
            valid = any(_equal(event["declaration"], trigger) for trigger in triggers) and bool(observation)
        if valid:
            event_nodes.update(selected)
        else:
            gaps.append({"invalidator": event["id"], "cause": "change/trigger proof is missing or contradictory"})
    _unique(event_ids, "invalidator event")
    for raw in changes:
        change = as_object(raw)
        if (text(change["root"]), text(change["path"])) not in matched_changes:
            gaps.append({"unmodeled_observed_change": change})
    coverage = as_object(declarations["coverage"])
    read_source(runtime, as_object(coverage["population_source"]))
    subject = as_object(declarations["new_subject"])
    complete = True
    for field in ("dependency_complete", "impact_complete"):
        proof = coverage[field]
        if proof is None:
            complete = False; gaps.append({"coverage": field, "cause": "no supplied proof"})
        else:
            value, failures = _condition(runtime, proof, subject, new_basis)
            if value != "satisfied":
                complete = False; gaps.append({"coverage": field, "gaps": failures, "core_value": value})
    affected: list[JSON] = []; survivors: list[JSON] = []; result_ids = {text(as_object(ref)["id"]) for ref in as_list(args["results"])}
    for check in checks:
        seen = {text(check["node"])}; frontier = list(seen)
        while frontier:
            current_node = frontier.pop()
            for dependency in adjacency[current_node] - seen:
                seen.add(dependency); frontier.append(dependency)
        intersection = sorted(seen & cover)
        is_candidate = bool(intersection) or not complete or bool(gaps)
        if check["result"] is not None:
            if text(as_object(as_object(check["result"])["record"])["id"]) not in result_ids:
                raise SupportError("contract_violation", "Refresh Check.result is outside acquired results population")
            original_check = _judgment(runtime, as_object(check["result"]))
            if not _equal(original_check["subject"], declarations["old_subject"]) or not _equal(original_check["basis"], old_basis):
                raise SupportError("basis_stale", "Refresh original check does not bind declared old subject/basis")
        fact: Object = document({"check": check["id"], "dependencies": sorted(seen), "impact_intersection": intersection, "original": check["result"], "candidate": is_candidate})
        (affected if is_candidate else survivors).append(fact)
    retention: list[JSON] = []
    for raw in as_list(declarations["retention"]):
        item = as_object(raw); original = _judgment(runtime, as_object(item["result"]))
        supported = True; support: list[JSON] = []
        for field in ("claim_scope", "assertion_basis", "observation_basis", "dependencies"):
            core, missing = _condition(runtime, item[field], subject, new_basis)
            support.append({"condition": field, "core_value": core, "gaps": missing})
            if core != "satisfied":
                supported = False
        retention.append({"original": item["result"], "historical_subject": original["subject"], "historical_core_value": original["core_value"], "new_subject": subject,
                          "new_basis": new_basis, "supported_applicability": supported, "proof": support})
    new_obligations = [as_object(raw) for raw in as_list(declarations["new_obligations"])]
    allowed_gates = {text(check["id"]) for check in checks} | {text(obligation["id"]) for obligation in new_obligations}
    if set(_strings(declarations["mandatory_gates"])) - allowed_gates:
        raise SupportError("contract_violation", "Mandatory refresh gate is dangling")
    return document({"differences": changes, "affected_candidates": affected, "unchanged_candidates": survivors,
            "retention": retention, "new_obligations": new_obligations, "mandatory_gates": declarations["mandatory_gates"], "gaps": gaps,
            "handoff": {"previous": previous_ref, "current": current_ref, "declarations": declarations_ref,
                        "original_results": args["results"], "retention": retention, "residuals": gaps,
                        "unreconciled_effects": "Retained Attempt histories must be separately acquired before dependent retry"},
            "limits": ["computed affected/support candidates, never semantic non-influence or automatic execution"]})


def aggregate_resources(runtime: Runtime, args: Object) -> Object:
    accounting = _source_json(runtime, as_object(args["accounting"]), "Accounting")
    refs = [as_object(raw) for raw in as_list(args["attempts"])]
    unique: dict[str, Object] = {}
    for ref in refs:
        identity = text(ref["id"])
        if identity in unique and not _equal(unique[identity], ref):
            raise SupportError("request_identity_conflict", "Conflicting retained resource root identity")
        unique[identity] = ref
    if {canonical(ref) for ref in unique.values()} != {canonical(ref) for ref in as_list(accounting["records"])}:
        raise SupportError("contract_violation", "Accounting.records must equal the explicit unique selected roots")
    read_source(runtime, as_object(accounting["authority_source"]))
    gaps: list[JSON] = []; samples: dict[str, Object] = {}; conflicts: set[str] = set()
    intervals: list[tuple[int, int, str]] = []; actor_intervals: list[tuple[int, int, str]] = []; resources: list[JSON] = []
    rules: dict[tuple[str, str, str, str], Object] = {}
    for raw in as_list(accounting["counter_rules"]):
        rule = as_object(raw); key = tuple(text(rule[field]) for field in ("provider", "counter_id", "unit", "scope"))
        if key in rules:
            raise SupportError("contract_violation", "Duplicate accounting counter rule")
        read_source(runtime, as_object(rule["source"]))
        rules[cast(tuple[str, str, str, str], key)] = rule
    for key, rule in rules.items():
        visited: set[str] = set(); parent = rule["subset_of"]
        while parent is not None:
            identity = text(parent)
            if identity in visited:
                raise SupportError("contract_violation", "Counter subset cycle")
            visited.add(identity)
            target = (key[0], identity, key[2], key[3])
            if target not in rules:
                raise SupportError("contract_violation", "Counter subset names missing same-domain rule")
            parent = rules[target]["subset_of"]
    for owner_id, owner_ref in unique.items():
        record = load_artifact(runtime, owner_ref)
        if record["kind"] not in ("attempt", "operation"):
            raise SupportError("basis_missing", "Resource accounting roots must be actual Attempt/OperationEvidence")
        owner: Object = document({"kind": record["kind"], "record": owner_ref})
        found, query = _history(runtime, "resource", {"payload.owner.record.id": owner_id})
        if query["complete"] is not True:
            gaps.append({"owner": owner, "history": query})
        if not found:
            gaps.append({"owner": owner, "cause": "no actual resource observation; usage and interval unknown"})
        for envelope in found:
            resource = validate_content(envelope["payload"], "Resource")
            if not _equal(resource["owner"], owner):
                raise SupportError("contract_violation", "Resource owner differs from actual retained record")
            resources.append(resource); gaps.extend(as_list(resource["gaps"]))
            interval = resource["interval"]
            if interval is not None:
                measured = as_object(interval); start = integer(measured["started_ns"]); end = integer(measured["ended_ns"])
                if end < start:
                    raise SupportError("domain_invalid", "Resource interval reversed")
                triple = (start, end, owner_id)
                if triple not in intervals:
                    intervals.append(triple)
                if owner["kind"] == "attempt" and triple not in actor_intervals:
                    actor_intervals.append(triple)
            else:
                gaps.append({"owner": owner, "cause": "interval unknown"})
            for raw_sample in as_list(resource["samples"]):
                sample = as_object(raw_sample)
                if not _equal(sample["owner"], owner):
                    raise SupportError("contract_violation", "Counter sample owner mismatch")
                try:
                    _acquired(runtime, as_object(sample["raw_source"]))
                except SupportError as exc:
                    gaps.append(exc.document())
                identity = digest({key: sample[key] for key in ("owner", "provider", "counter_id", "unit", "scope", "sample_id")})
                if identity in samples and not _equal(samples[identity], sample):
                    conflicts.add(identity)
                else:
                    samples[identity] = sample
    if conflicts:
        raise SupportError("request_identity_conflict", "Actual resource samples conflict under one full identity", [{"sample": identity} for identity in sorted(conflicts)])
    grouped: dict[tuple[str, str, str, str, str], list[Object]] = {}
    for sample in samples.values():
        domain = tuple(text(sample[field]) for field in ("provider", "counter_id", "unit", "scope"))
        key = cast(tuple[str, str, str, str], domain)
        if key not in rules:
            gaps.append({"counter": list(key), "cause": "undocumented counter scope/unit"}); continue
        sample_owner_id = text(as_object(as_object(sample["owner"])["record"])["id"])
        grouped.setdefault((sample_owner_id,) + key, []).append(sample)
    totals: dict[tuple[str, str, str, str], int] = {}; unknown: list[JSON] = []; displayed: list[JSON] = []
    for group_key, members in grouped.items():
        key = group_key[1:]; rule = rules[key]
        selected = members
        if rule["mode"] == "cumulative":
            greatest = max(integer(sample["sequence"]) for sample in members)
            selected = [sample for sample in members if sample["sequence"] == greatest]
            if len({canonical(sample["value"]) for sample in selected}) != 1:
                unknown.append({"owner": group_key[0], "counter": list(key), "cause": "conflicting maximum cumulative sequence"}); continue
            selected = selected[:1]
        if any(sample["value"] is None for sample in selected):
            unknown.append({"owner": group_key[0], "counter": list(key), "cause": "actual usage unknown"})
        known = sum(integer(sample["value"]) for sample in selected if sample["value"] is not None)
        displayed.append(document({"owner": group_key[0], "counter": list(key), "known_subtotal": known, "subset_of": rule["subset_of"], "samples": members}))
        if rule["subset_of"] is None:
            totals[key] = totals.get(key, 0) + known
    elapsed = as_object(accounting["elapsed"]); window = elapsed["window"]
    clipped: list[tuple[int, int, str]] = []
    for start, end, interval_owner in intervals:
        if window is not None:
            selected_window = as_object(window)
            start = max(start, integer(selected_window["started_ns"])); end = min(end, integer(selected_window["ended_ns"]))
        if end >= start:
            clipped.append((start, end, interval_owner))
    merged: list[tuple[int, int]] = []
    for start, end, _ in sorted(clipped):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    elapsed_ns = sum(end - start for start, end in merged) if elapsed["mode"] == "interval_union" else max((end for _, end, _ in clipped), default=0) - min((start for start, _, _ in clipped), default=0)
    overlaps: list[JSON] = []
    for index, (start, end, actor_owner_id) in enumerate(actor_intervals):
        for other_start, other_end, other_owner in actor_intervals[index + 1:]:
            if min(end, other_end) > max(start, other_start):
                overlaps.append({"owners": [actor_owner_id, other_owner], "nanoseconds": min(end, other_end) - max(start, other_start)})
    priced: JSON = None
    pricing = accounting["pricing"]
    if pricing is not None:
        from fractions import Fraction
        price = as_object(pricing); read_source(runtime, as_object(price["source"]))
        subtotal = Fraction(0); unpriced: list[JSON] = []
        rate_by_key: dict[tuple[str, str, str, str], Object] = {}
        for raw in as_list(price["rates"]):
            rate = as_object(raw); key = cast(tuple[str, str, str, str], tuple(text(rate[field]) for field in ("provider", "counter_id", "unit", "scope")))
            if key in rate_by_key:
                raise SupportError("contract_violation", "Duplicate source-bound rate")
            rate_by_key[key] = rate
        for key, value in totals.items():
            if key in rate_by_key:
                rate = rate_by_key[key]; subtotal += Fraction(value * integer(rate["numerator"]), integer(rate["denominator"], minimum=1))
            else:
                unpriced.append(list(key))
        priced = {"currency": price["currency"], "minor_unit_scale": price["minor_unit_scale"], "numerator": subtotal.numerator, "denominator": subtotal.denominator, "unpriced": unpriced, "unknown": unknown}
    total_rows: list[JSON] = [{"provider": key[0], "counter_id": key[1], "unit": key[2], "scope": key[3], "known_subtotal": value} for key, value in sorted(totals.items())]
    result: Object = document({"roots": list(unique.values()), "resources": resources, "counters": displayed,
                      "totals": total_rows, "unknowns": unknown, "gaps": gaps,
                      "elapsed": {"mode": elapsed["mode"], "nanoseconds": elapsed_ns, "known_intervals": [[start, end] for start, end in merged]},
                      "actor_duration": {"nanoseconds": sum(end - start for start, end, _ in actor_intervals), "overlaps": overlaps},
                      "price": priced, "limit_judgments": [], "limits": ["selected actual observation population only; no accepted-result benefit"]})
    judgments: list[JSON] = []
    for predicate_id in _strings(accounting["limit_predicates"]):
        definition = as_object(as_object(runtime.policy["predicates"])[predicate_id])
        judgments.append(evaluate_predicate(runtime, predicate_id, _predicate_inputs(runtime, predicate_id, document({"totals": total_rows, "unknowns": unknown, "elapsed": result["elapsed"], "actor_duration": result["actor_duration"]})), as_object(definition["subject"]), as_object(definition["basis"])))
    result["limit_judgments"] = judgments
    return result


def response_schema() -> Object:
    diagnostic = _object({"code": document({"enum": sorted(CODES)}), "reason": document({"type": "string"}), "gaps": _array(_ref("Json")), "source_refs": _array(_ref("Json"))})
    boundary = _object({"predicate": _ref("Json"), "value": {"enum": ["returned", "held(observation)", "held(effect)", "refused(constraint)", "refused(basis)", "refused(authority)", "refused(capability)"]},
                        "cause": _ref("Id"), "core_value": {"enum": list(CORE_VALUES)},
                        "source_parent": _object({"member": _ref("Id"), "sha256": _ref("Sha256"), "clause": _ref("Id")}),
                        "evidence": _array(_ref("Json")), "limits": _array(_ref("Json"))})
    result = _object({"schema": {"const": "a_c.fd-support.response/1"}, "id": _nullable(_ref("Id")),
                      "operation": _nullable(_ref("Id")), "status": {"enum": ["ok", "refused", "error"]},
                      "result": _nullable(_object({"artifact": _nullable(_ref("ArtifactRef")), "value": _ref("Json")})),
                      "refusal": _nullable(diagnostic), "operation_outcome": _nullable(boundary), "evidence": _nullable(_ref("ArtifactRef"))})
    result["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    result["$defs"] = _definition_closure(result)
    return result


def _work_projection(runtime: Runtime, args: Object) -> Object:
    source = as_object(args["carrier"]); raw = _source_bytes(runtime, source)
    selected: list[JSON] = []
    for selection in _strings(args["selection"]):
        if selection.startswith("/"):
            selected.append({"selection": selection, "original": pointer(parse_json(raw), selection)})
        else:
            try:
                lines = raw.decode("utf-8").splitlines(keepends=True)
            except UnicodeError as exc:
                raise SupportError("domain_invalid", "Markdown projection requires UTF-8") from exc
            matches = [i for i, line in enumerate(lines) if re.fullmatch(r"#{1,6} +" + re.escape(selection) + r"\s*", line.rstrip("\r\n"))]
            if len(matches) != 1:
                raise SupportError("basis_ambiguous" if matches else "basis_missing", "Selected Markdown heading absent/ambiguous")
            first = matches[0]; level = len(lines[first]) - len(lines[first].lstrip("#")); last = len(lines)
            for index in range(first + 1, len(lines)):
                found = re.match(r"^(#{1,6}) +", lines[index])
                if found is not None and len(found.group(1)) <= level:
                    last = index; break
            selected.append({"selection": selection, "lines": [first + 1, last], "original": "".join(lines[first:last])})
    return document({"source": source, "parent_sha256": _sha(raw), "selected": selected,
            "limits": ["original wording only; no inferred state, ruling, closure or release"]})


def verify_reconciliation(runtime: Runtime, evidence_ref: Object, predecessor_ref: Object,
                          grant: Object, basis: Object) -> Object:
    predecessor = load_artifact(runtime, predecessor_ref, "attempt")
    _profile_basis(runtime, basis)
    admission = _admission_selection(grant["admission"])
    selected = _strings(admission.get("required_reconciliation_predicates", []))
    subject: Object = document({"id": predecessor_ref["id"], "sha256": predecessor_ref["sha256"]})
    definitions = as_object(runtime.policy["predicates"])
    if not selected:
        raise SupportError("effect_unreconciled", "Grant has no selected predecessor-bound reconciliation contract")
    for identity in selected:
        if identity not in definitions:
            raise SupportError("effect_unreconciled", "Selected reconciliation predicate is not registered", [{"predicate_id": identity}])
        definition = as_object(definitions[identity])
        if not _equal(definition["subject"], subject) or not _equal(definition["basis"], basis):
            raise SupportError("effect_unreconciled", "Selected reconciliation predicate does not bind this predecessor/current basis", [{"predicate_id": identity}])
    supplied = load_artifact(runtime, evidence_ref, "operation")
    records, query = _history(runtime, "operation", {"payload.request.operation": "checks.evaluate"})
    records.append(supplied)
    if query["complete"] is not True:
        raise SupportError("history_incomplete", "Reconciliation evidence history is incomplete", [query])
    actual: list[JSON] = []
    for identity in selected:
        matches: list[Object] = []
        for record in records:
            payload = as_object(record["payload"]); request = as_object(payload["request"])
            if request["operation"] != "checks.evaluate" or as_object(request["arguments"])["predicate_id"] != identity:
                continue
            ref: Object = document({"id": "sha256:" + digest(record), "sha256": digest(record)})
            value = _judgment(runtime, {"record": ref, "pointer": "/payload/response_without_evidence/result/value/judgment"})
            if _equal(value["subject"], subject) and _equal(value["basis"], basis) and value["core_value"] == "satisfied":
                # Reacquire exact declared input references; historical pass alone
                # is not a current reconciliation premise.
                for reference in as_object(as_object(request["arguments"])["inputs"]).values():
                    _acquired(runtime, as_object(reference))
                matches.append(value)
        if not matches:
            raise SupportError("effect_unreconciled", "A selected actual reconciliation predicate is missing/not satisfied", [{"predicate_id": identity}])
        actual.append(document({"predicate_id": identity, "results": matches}))
    return document({"predecessor": predecessor_ref, "subject": subject, "basis": basis,
            "selected": actual, "grant": grant["id"], "history": query,
            "original_attempt": predecessor["payload"], "limits": ["current supplied reconciliation conditions only; prior unknown effects unchanged; no retry grant created"]})


def execute_read(runtime: Runtime, request: Object) -> CoreOutcome:
    validate_request(request)
    operation = text(request["operation"])
    started = time.time_ns()
    try:
        require_operation(runtime, operation)
        args = as_object(request["arguments"])
        if operation in EFFECT_OPERATIONS:
            raise SupportError("unsupported_contract", "Named effect must pass the effect membrane")
        if operation == "context.assemble":
            return _assemble(runtime, request, args, started)
        if operation == "return.capture":
            return _capture_return(runtime, request, args, started)
        if operation == "review.prepare":
            return _review(runtime, request, args, started)
        artifacts: list[JSON] = []; acquisitions: list[JSON] = []; primary: JSON = None
        value: JSON
        if operation == "tools.describe":
            if "method_profile" in args and not _equal(args["method_profile"], {"id": PROFILE_ID, "sha256": PROFILE_SHA256}):
                raise SupportError("unsupported_contract", "Requested exact method/profile is unsupported")
            value = inventory(cast(str | None, args.get("operation")))
        elif operation == "workspace.observe":
            payload = observe(runtime, as_list(args["scope"]))
            if "previous" in args:
                old = as_object(load_artifact(runtime, as_object(args["previous"]), "observation")["payload"])
                if not _equal(old["scope"], args["scope"]):
                    raise SupportError("basis_ambiguous", "Observation scopes differ")
                payload["diff"] = observation_diff(old, payload)
            artifact, primary = make_artifact("observation", payload, provenance(runtime, request, started, time.time_ns()))
            artifacts.append(artifact); value = payload
        elif operation == "source.read":
            source = as_object(args["source"]); acquired = read_source(runtime, source)
            raw = base64.b64decode(cast(str, acquired["content_base64"]))
            if "max_content_bytes" in args and len(raw) > integer(args["max_content_bytes"]):
                raise SupportError("budget_exceeded", "Source content exceeds selected output byte bound")
            try:
                content = raw.decode("utf-8") if args["encoding"] == "utf8" else base64.b64encode(raw).decode()
            except UnicodeError as exc:
                raise SupportError("domain_invalid", "Source is not UTF-8; explicit base64 acquisition is available") from exc
            value = {key: item for key, item in acquired.items() if key != "content_base64"}
            value["encoding"] = args["encoding"]; value["content"] = content
            artifact, ref = _acquisition(runtime, request, source, value, started, time.time_ns())
            artifacts.append(artifact); acquisitions.append(ref)
        elif operation in ("records.find", "records.read", "graph.project"):
            model_ref = as_object(args["model"]); model = _model(runtime, model_ref)
            if operation == "records.find":
                if not args["text"]:
                    raise SupportError("contract_violation", "Empty literal search is unsupported")
                value = ac_graph.find(model, cast(str, args["text"]))
            elif operation == "records.read":
                ids = _strings(args["ids"]); _unique(ids, "record request")
                value = {"parent": ac_graph.model_identity(model), "records": [_record(model, identity) for identity in ids], "basis": model.document["basis"], "coverage": model.document.get("interpretation"), "limits": ["selected authored model only"]}
            else:
                for seeds, _ in _selections(args["selections"]):
                    for identity in seeds:
                        _record(model, identity)
                value = {"parent": ac_graph.model_identity(model), "views": _project(model, args["selections"]), "limits": ["exact authored governing closure; no semantic sufficiency"]}
            artifact, ref = _acquisition(runtime, request, as_object(model_ref["source"]), value, started, time.time_ns(), model_ref, args.get("ids", args.get("selections", {"search": args.get("text")})))
            artifacts.append(artifact); acquisitions.append(ref)
        elif operation == "relations.query":
            value = relation_query(runtime, args)
        elif operation == "checks.evaluate":
            inputs: Object = document({})
            for name, raw_input in as_object(args["inputs"]).items():
                reference = as_object(raw_input)
                if "engine" in reference:
                    inputs[name] = parse_json(_source_bytes(runtime, reference))
                else:
                    inputs[name] = load_artifact(runtime, reference)
            value = {"judgment": evaluate_predicate(runtime, text(args["predicate_id"]), inputs, as_object(args["subject"]), as_object(args["basis"]))}
        elif operation == "results.conjoin":
            value = conjoin(runtime, args)
        elif operation == "work.project":
            value = _work_projection(runtime, args)
            artifact, ref = _acquisition(runtime, request, args["carrier"], value, started, time.time_ns(), selection=args["selection"])
            artifacts.append(artifact); acquisitions.append(ref)
        elif operation == "return.check":
            value = _check_return(runtime, args)
        elif operation == "refresh.prepare":
            value = refresh(runtime, args)
        elif operation == "resources.aggregate":
            value = aggregate_resources(runtime, args)
        elif operation == "evidence.read":
            ref = as_object(args["artifact"]); envelope = load_artifact(runtime, ref)
            raw = canonical(envelope)
            if "max_content_bytes" in args and len(raw) > integer(args["max_content_bytes"]):
                raise SupportError("budget_exceeded", "Retained evidence exceeds selected acquisition byte bound")
            value = {"artifact": ref, "envelope": envelope, "parent_sha256": _sha(raw), "size_bytes": len(raw)}
            artifact, acquisition_ref = _acquisition(runtime, request, {"engine": "retained-evidence", "root": "evidence", "path": ref["id"], "object": None, "sha256": ref["sha256"], "selector": None}, value, started, time.time_ns(), derived_sources=_delivered_evidence_sources(envelope))
            artifacts.append(artifact); acquisitions.append(acquisition_ref)
        else:
            raise SupportError("unknown_operation", "Operation is not implemented by the finite core")
        boundary = operation_outcome(operation)
        boundary["predicate"] = "B(" + operation + ")[request_sha256=" + digest(request) + "]: declared output availability"
        return document({"result": {"artifact": primary, "value": value}, "artifacts": artifacts,
                "operation_outcome": boundary, "refusal": None, "acquisitions": acquisitions})
    except SupportError as exc:
        return refusal_outcome(runtime, request, exc)
    except ac_graph.Refusal as exc:
        return refusal_outcome(runtime, request, SupportError("domain_invalid", "Exact codec operation refused: " + str(exc)))


def _packet_schema() -> Object:
    refs = _array(_ref("SourceRef")); strings = _array({"type": "string"}); nullable_ref = _nullable(_ref("SourceRef"))
    authority: Object = {key: nullable_ref for key in ("semantic", "evaluation", "operation", "decision", "acceptance", "publication")}
    authority.update({"actor_id": _ref("Id"), "role": {"enum": ["Executive", "Worker", "Reviewer"]}, "capability": _ref("SourceRef"), "territory": _array(_SCOPE), "tools": _array(_ref("Id"))})
    reviewer = _object({key: _ref("SourceRef") for key in ("claim", "composition", "population", "oracle", "ordinary_module_path", "falsification_condition", "independence", "assurance")})
    as_object(reviewer["properties"])["severity_scale"] = nullable_ref
    reviewer["required"] = list(as_object(reviewer["properties"]))
    executive = _object({key: nullable_ref if key in ("conjunction", "disposition_grant") else _ref("SourceRef") for key in ("product_role_map", "mandate", "frontier", "result_triage_ledger", "priority_policy", "conjunction", "disposition_grant")})
    return _object({
        "activation": _object({"id": _ref("Id"), "revision": _ref("Id"), "configuration": _ref("SourceRef")}),
        "frame": _object({"id": _ref("Id"), "revision": _ref("Id"), "declaration": _ref("SourceRef"), "evaluation": _ref("SourceRef"), "result_algebra": _ref("SourceRef")}),
        "subject_basis": _object({"subject": _ref("Identity"), "method_profile": _ref("Identity"), "product": _object({"id": _ref("Id"), "definition": _ref("SourceRef")}), "observations": _array(_ref("ArtifactRef")), "dependencies": refs, "time_basis": _ref("Id")}),
        "attention": _object({"material_relations": refs, "invariants": refs, "semantic_sources": refs, "exclusions": strings, "prohibited_assumptions": strings}),
        "actor_authority": _object(authority),
        "evidence_relations": _object({"admissible_evidence": refs, "acquisition": refs, "dependencies": refs, "conjunction": nullable_ref, "translation": {"type": "null"}, "consumer": _ref("Id"), "return_contract": _ref("SourceRef")}),
        "stop_change": _object({key: _array(_ref("Json")) for key in ("invalidators", "stop_conditions", "residuals", "re_entry", "reconfiguration")}),
        "profile_additions": {"oneOf": [_object({"worker": _object({"operation_grant_id": _ref("Id"), "mutation_subject": _ref("Identity"), "territory": _array(_SCOPE)})}), _object({"reviewer": reviewer}), _object({"executive": executive})]},
    })


as_object(_ARGUMENTS["context.assemble"]["properties"])["packet"] = _packet_schema()
_target_schema = copy.deepcopy(as_object(as_object(CONTENT_SCHEMAS["$defs"])["SourceRef"]))
as_object(_target_schema["properties"])["sha256"] = _nullable(_ref("Sha256"))
as_object(_ARGUMENTS["work.write"]["properties"])["target"] = _target_schema


def _context_delivery(runtime: Runtime, acquisition_ref: Object, actor_id: str,
                      before_ns: int) -> tuple[bool, list[JSON]]:
    acquisition = as_object(load_artifact(runtime, acquisition_ref, "acquisition")["payload"])
    if acquisition.get("channel") != "actor-context" or acquisition.get("recipient") != actor_id:
        return False, []
    events, history = _history(runtime, "raw", {"payload.schema": "a_c.fd-support.attempt-event/1", "payload.kind": "context_delivery"})
    gaps: list[JSON] = []
    if history["complete"] is not True:
        gaps.append({"context_delivery_history": history})
    for envelope in events:
        event = as_object(envelope["payload"]); data = as_object(event["data"])
        attempt = as_object(load_artifact(runtime, as_object(event["attempt"]), "attempt")["payload"])
        target_id = text(attempt["target"])
        target = as_object(as_object(runtime.policy["principals"])[target_id])
        context_ref = as_object(attempt["context"])
        context = as_object(load_artifact(runtime, context_ref, "context")["payload"])
        if target["actor_id"] != actor_id or data.get("recipient") != target_id or data.get("complete") is not True or not _equal(data.get("context"), context_ref):
            continue
        rendered = text(context["rendered_utf8"]).encode()
        if data.get("rendered_sha256") != _sha(rendered) or data.get("bytes") != len(rendered):
            continue
        delivery_end = integer(as_object(data["interval"])["ended_ns"]) if isinstance(data.get("interval"), dict) else integer(event["observed_at_ns"])
        if delivery_end >= before_ns:
            gaps.append("Context delivery order overlaps expectation")
            continue
        parents, parent_history = _history(runtime, "operation", {"payload.request.operation": "context.assemble", "payload.response_without_evidence.result.artifact.id": context_ref["id"]})
        if parent_history["complete"] is not True:
            gaps.append({"context_parent_history": parent_history}); continue
        if any(any(_equal(ref, acquisition_ref) for ref in as_list(as_object(parent["payload"])["acquisitions"])) for parent in parents):
            return True, gaps
    return False, gaps


def _request_body(operation: str) -> Object:
    return _object({"schema": {"const": REQUEST}, "id": _ref("Id"), "operation": {"const": operation}, "arguments": copy.deepcopy(_ARGUMENTS[operation])})


def _definition_closure(schema: Object) -> Object:
    definitions = as_object(CONTENT_SCHEMAS["$defs"])
    selected: set[str] = set()
    def visit(value: JSON) -> None:
        if isinstance(value, dict):
            if isinstance(value.get("$ref"), str):
                reference = text(value["$ref"])
                if reference.startswith("#/$defs/") and reference[8:] not in selected:
                    name = reference[8:]
                    if name not in definitions:
                        raise SupportError("unsupported_contract", "Missing published referenced definition")
                    selected.add(name); visit(definitions[name])
            for key, member in value.items():
                if key != "$defs":
                    visit(member)
        elif isinstance(value, list):
            for member in value:
                visit(member)
    visit(schema)
    return {name: copy.deepcopy(definitions[name]) for name in sorted(selected)}


def _predicate_inputs(runtime: Runtime, predicate_id: str, available: Object) -> Object:
    definitions = as_object(runtime.policy["predicates"])
    if predicate_id not in definitions:
        raise SupportError("unsupported_check", "Predicate is not registered")
    names = _strings(as_object(definitions[predicate_id])["input_names"])
    return {name: value for name, value in available.items() if name in names}


def _validate_expression(expression: JSON, depth: int = 0) -> None:
    if depth > 64:
        raise SupportError("unsupported_check", "Predicate exceeds finite expression depth")
    node = as_object(expression)
    if set(node) == {"literal"}:
        _json(node["literal"]); return
    if set(node) == {"input", "pointer"}:
        text(node["input"]); validate_schema(node["pointer"], _ref("JsonPointer")); return
    if set(node) != {"op", "args"}:
        raise SupportError("unsupported_check", "Unsupported predicate AST")
    op = text(node["op"]); args = as_list(node["args"])
    arity = {"equals": 2, "member": 2, "contains_all": 2, "not": 1}
    if op not in ("equals", "member", "contains_all", "all", "any", "not") or op in arity and len(args) != arity[op] or op in ("all", "any") and not args:
        raise SupportError("unsupported_check", "Unsupported predicate operator/arity")
    for argument in args:
        _validate_expression(argument, depth + 1)


def _review_claim_population(runtime: Runtime, claim: Object,
                             candidate: Object | None) -> tuple[list[Object], bool, list[JSON]]:
    raw = base64.b64decode(text(claim["content_base64"]))
    declared: list[Object] = []; complete = False; gaps: list[JSON] = []
    try:
        body = parse_json(raw)
    except SupportError as exc:
        if exc.code != "malformed_request":
            raise
        body = None
    if isinstance(body, dict) and ("candidate_sources" in body or "id" in body):
        structured = validate_content(body, "ReviewClaim")
        declared = [as_object(ref) for ref in as_list(structured["candidate_sources"])]
        complete = True
    else:
        gaps.append("Opaque/missing ReviewClaim candidate population remains unknown; no inferred prose mapping")
    if candidate is not None:
        declared.append(candidate)
    unique: dict[bytes, Object] = {}; parents: dict[tuple[str, str, str, str], JSON] = {}
    for ref in declared:
        validate_content(ref, "SourceRef")
        if ref["engine"] == "workspace-regular-file":
            source_path(runtime, ref)  # identity/access only; no candidate bytes
        elif ref["engine"] == "immutable-git-blob":
            root = _root(runtime, text(ref["root"]))
            _relative(text(ref["path"]))
            if root["kind"] != "git" or not _allowed(root, text(ref["path"])):
                raise SupportError("acquisition_denied", "Declared candidate Git identity is outside selected scope")
        elif text(ref["root"]) != "evidence" or text(ref["path"]) != "sha256:" + text(ref["sha256"]):
            raise SupportError("contract_violation", "Declared retained candidate parent identity is inconsistent")
        key = (text(ref["engine"]), text(ref["root"]), text(ref["path"]), str(ref["object"]))
        if key in parents and parents[key] != ref["sha256"]:
            raise SupportError("basis_ambiguous", "Candidate population assigns competing whole-parent hashes")
        parents[key] = ref["sha256"]
        unique[canonical(ref)] = ref
    return list(unique.values()), complete, gaps


def _delivered_evidence_sources(envelope: Object) -> list[JSON]:
    """Known inline content carriers only; following a locator is not delivery."""
    payload = as_object(envelope["payload"]); sources: list[JSON] = []
    if envelope["kind"] == "context":
        for value in as_list(payload["sources"]):
            acquired = as_object(value)
            if isinstance(acquired.get("content_base64"), str):
                sources.append(acquired["source"])
        for value in as_list(payload["projections"]):
            projection = as_object(value)
            if as_list(projection["views"]):
                sources.append(as_object(projection["model"])["source"])
    elif envelope["kind"] == "operation":
        request = as_object(payload["request"]); response = as_object(payload["response_without_evidence"])
        if response["result"] is not None:
            result_value = as_object(response["result"])["value"]
            if isinstance(result_value, dict):
                if request["operation"] == "source.read" and "content" in result_value:
                    sources.append(result_value["source"])
                elif request["operation"] == "work.project" and as_list(result_value["selected"]):
                    sources.append(result_value["source"])
                elif request["operation"] in ("records.read", "records.find", "graph.project"):
                    sources.append(as_object(as_object(request["arguments"])["model"])["source"])
    unique = {canonical(source): source for source in sources}
    return [unique[key] for key in sorted(unique)]
