#!/usr/bin/env python3
"""Losslessly expose a declared source-semantic a_c model through Axiom Indexer."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import quote
import ac

VOCAB = 'urn:axiom-indexer:model-conversion:v1:'
FAMILIES = ('objects', 'relations', 'constraints', 'latitude', 'residuals', 'transformations', 'traversals', 'judgments')
CONFIG_KEYS = {'program_uri', 'source_basis', 'calculus_ref', 'metadata_source_ref', 'source_mappings', 'frame_indexes'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canon(value):
    return ac.canonical_bytes(value).decode('utf-8')


def digest(value):
    return hashlib.sha256(ac.canonical_bytes(value)).hexdigest()


def local_refs(value, identities, path=''):
    result = []
    if isinstance(value, dict):
        for key in sorted(value):
            if key == 'id' and not path:
                continue
            result.extend(local_refs(value[key], identities, path + '/' + key.replace('~', '~0').replace('/', '~1')))
    elif isinstance(value, list):
        for n, item in enumerate(value):
            result.extend(local_refs(item, identities, path + '/' + str(n)))
    elif isinstance(value, str) and value in identities:
        result.append({'role': VOCAB + 'pointer:' + quote(path, safe=''), 'ref': value})
    return result


def record_content(family, row):
    return row[{'objects': 'value', 'relations': 'qualifiers', 'constraints': 'predicate', 'latitude': 'allowed_variation', 'residuals': 'uncertainty'}[family]]


def grounds(family, row):
    if family == 'latitude':
        return row['allowed_variation']['grounding'] + row['forbidden_variation']['grounding']
    return record_content(family, row)['grounding']


def statement(family, row):
    content = record_content(family, row)
    if family == 'objects':
        return content['label'] + ': ' + content['definition']
    if family == 'relations':
        return content['meaning']
    if family == 'constraints':
        return content['statement']
    if family == 'latitude':
        return canon({'allowed': row['allowed_variation']['statements'], 'forbidden': row['forbidden_variation']['statements']})
    return content['statement']


def source_refs(family, row, config):
    refs = []
    for ground in grounds(family, row):
        path = ground['path']
        require(isinstance(path, str) and not Path(path).is_absolute() and '..' not in Path(path).parts, 'invalid grounding path')
        matches = [m for m in config['source_mappings'] if path.startswith(m['path_prefix'])]
        require(bool(matches), 'missing source mapping: ' + path)
        matches.sort(key=lambda m: len(m['path_prefix']), reverse=True)
        require(len(matches) == 1 or len(matches[0]['path_prefix']) != len(matches[1]['path_prefix']), 'ambiguous source mapping')
        mapping = matches[0]
        refs.append(mapping['uri_prefix'] + quote(path[len(mapping['path_prefix']):], safe='/'))
    require(bool(refs), 'empty record grounding')
    return sorted(set(refs))


def convert(model, config):
    require(isinstance(config, dict) and set(config) == CONFIG_KEYS, 'invalid conversion configuration')
    for key in ('program_uri', 'source_basis', 'calculus_ref', 'metadata_source_ref'):
        require(ac.is_uri(config[key]), 'invalid configuration URI: ' + key)
    require(isinstance(config['source_mappings'], list) and bool(config['source_mappings']), 'missing source mappings')
    for mapping in config['source_mappings']:
        require(set(mapping) == {'path_prefix', 'uri_prefix'} and isinstance(mapping['path_prefix'], str) and ac.is_uri(mapping['uri_prefix']), 'invalid source mapping')
    populations = model['populations']
    require(set(populations) == set(FAMILIES), 'unsupported model population family')
    require(all(isinstance(populations[f], list) for f in FAMILIES), 'invalid populations')
    require(all(not populations[f] for f in FAMILIES[5:]), 'operational populations require an explicit future conversion contract')
    rows = [(f, row) for f in FAMILIES for row in populations[f]]
    identifiers = [row['id'] for _, row in rows]
    require(len(identifiers) == len(set(identifiers)) and all(ac.is_uri(x) for x in identifiers), 'duplicate or invalid record identity')
    ids = set(identifiers)
    metadata_id = config['program_uri'] + ':model-metadata'
    require(metadata_id not in ids and config['program_uri'] not in ids, 'conversion identity collision')
    vocab = {VOCAB + 'model-metadata', VOCAB + 'payload', VOCAB + 'conversion-metadata'}
    metadata = {'profile': 'axiom-indexer.ac-model-conversion/1', 'config': copy.deepcopy(config), 'model': {k:copy.deepcopy(v) for k,v in model.items() if k != 'populations'}, 'family_order': {f:[row['id'] for row in populations[f]] for f in FAMILIES}}
    clauses = [{'uri': metadata_id, 'clause_type': 'relation', 'operator': VOCAB + 'model-metadata', 'arguments': [{'role': VOCAB + 'conversion-metadata', 'literal': canon(metadata)}], 'statement': 'Exact model metadata and explicit conversion configuration; no semantic verdict.', 'source_refs': [config['metadata_source_ref']]}]
    residuals = []
    for family, row in rows:
        refs = source_refs(family, row, config)
        if family == 'residuals':
            require(row['subject'] in ids and row['subject'] != row['id'], 'dangling residual subject')
            residuals.append({'uri':row['id'], 'kind':'unresolved', 'subject_refs':[row['subject']], 'detail':canon({'family':family,'record':row}), 'source_refs':refs, 're_entry_refs':refs})
        else:
            operator = VOCAB + 'family:' + family
            args = local_refs(row, ids) + [{'role':VOCAB + 'payload', 'literal':canon({'family':family,'record':row})}]
            vocab.add(operator)
            vocab.update(arg['role'] for arg in args)
            clauses.append({'uri':row['id'], 'clause_type':'constraint' if family in ('constraints','latitude') else 'relation','operator':operator,'arguments':args,'statement':statement(family,row),'source_refs':refs})
    # Model attachment laws are checked here as well as by the upstream provider.
    concepts = {r['id'] for r in populations['objects']}
    for row in populations['relations']:
        require(row['source'] in concepts and row['target'] in concepts, 'dangling relation endpoint')
    for family in ('constraints','latitude'):
        for row in populations[family]:
            require(bool(row['applies_to']) and set(row['applies_to']) <= concepts, 'dangling attachment')
    indexes = copy.deepcopy(config['frame_indexes'])
    require(isinstance(indexes,list), 'invalid frame indexes')
    clause_ids = {r['uri'] for r in clauses}
    residual_ids = {r['uri'] for r in residuals}
    for index in indexes:
        require(set(index) == ac.FRAME_INDEX_KEYS, 'invalid frame index shape')
        require(set(index['clause_refs']) <= clause_ids and set(index['residual_refs']) <= residual_ids, 'dangling frame root')
        require(bool(index['clause_refs'] or index['residual_refs']), 'empty frame index')
    return {'kind':'axiom-indexer.axiomatic-program','schema_version':1,'uri':config['program_uri'],'calculus_ref':config['calculus_ref'],'source_basis':config['source_basis'],'frame_refs':sorted({x['frame_ref'] for x in indexes}),'vocabulary_refs':sorted(vocab),'symbols':[],'clauses':sorted(clauses,key=lambda r:r['uri']),'residuals':sorted(residuals,key=lambda r:r['uri']),'frame_indexes':sorted(indexes,key=lambda r:r['uri'])}


def restore(program):
    metadata_rows = [r for r in program['clauses'] if r['operator'] == VOCAB + 'model-metadata']
    require(len(metadata_rows) == 1, 'missing or duplicate conversion metadata')
    args = metadata_rows[0]['arguments']
    require(len(args) == 1 and args[0]['role'] == VOCAB + 'conversion-metadata', 'invalid conversion metadata')
    metadata = json.loads(args[0]['literal'])
    require(metadata['profile'] == 'axiom-indexer.ac-model-conversion/1', 'unsupported conversion profile')
    retained = {}
    for row in program['clauses']:
        if row is metadata_rows[0]: continue
        payloads = [a['literal'] for a in row['arguments'] if a['role'] == VOCAB + 'payload' and 'literal' in a]
        require(len(payloads) == 1, 'missing or duplicate record payload')
        payload = json.loads(payloads[0]); require(payload['record']['id'] == row['uri'] and row['uri'] not in retained, 'payload identity mismatch')
        retained[row['uri']] = payload
    for row in program['residuals']:
        payload = json.loads(row['detail']);require(payload['record']['id'] == row['uri'] and row['uri'] not in retained, 'payload identity mismatch')
        retained[row['uri']] = payload
    model = copy.deepcopy(metadata['model']); model['populations'] = {}
    order = metadata['family_order'];require(set(order)==set(FAMILIES),'family inventory mismatch')
    expected = [ident for family in FAMILIES for ident in order[family]]
    require(len(expected)==len(set(expected)) and set(expected)==set(retained),'record inventory mismatch')
    for family in FAMILIES:
        require(all(retained[ident]['family']==family for ident in order[family]),'record family mismatch')
        model['populations'][family] = [retained[ident]['record'] for ident in order[family]]
    require(convert(model, metadata['config']) == program, 'program differs from exact model derivation')
    return model


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__); sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('convert');p.add_argument('--model',required=True);p.add_argument('--config',required=True);p.add_argument('--output',required=True);p.add_argument('--receipt',required=True)
    p=sub.add_parser('restore');p.add_argument('--program',required=True);p.add_argument('--output',required=True)
    args=parser.parse_args(argv)
    try:
        inputs=[Path(getattr(args,k)).resolve() for k in ('model','config') if hasattr(args,k)] or [Path(args.program).resolve()]
        outputs=[Path(args.output).absolute()]+([Path(args.receipt).absolute()] if hasattr(args,'receipt') else [])
        require(len({p.resolve() for p in outputs})==len(outputs),'colliding outputs')
        require(all(not p.exists() and not p.is_symlink() and p.resolve() not in inputs for p in outputs),'output exists or aliases input')
        if args.command=='convert':
            model=ac.load_json(inputs[0]);config=ac.load_json(inputs[1]);result=convert(model,config);back=restore(result);require(back==model,'model preservation failed')
            receipt={'kind':'axiom-indexer.model-conversion-receipt','schema_version':1,'model_sha256':digest(model),'configuration_sha256':digest(config),'program_sha256':digest(result),'restored_model_sha256':digest(back),'preserved':True,'claim':'Exact declared model value preserved; source fidelity and semantic acceptance unassessed.'}
        else:result=restore(ac.load_json(inputs[0]))
        outputs[0].parent.mkdir(parents=True,exist_ok=True)
        with outputs[0].open('x',encoding='utf-8') as handle:handle.write(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
        if args.command=='convert':
            outputs[1].parent.mkdir(parents=True,exist_ok=True)
            with outputs[1].open('x',encoding='utf-8') as handle:handle.write(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
        print(json.dumps({'status':'converted' if args.command=='convert' else 'restored','output':str(outputs[0]),'sha256':digest(result)}))
        return 0
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print(json.dumps({'status':'refused','diagnostic':str(exc)}));return 1

if __name__=='__main__':
    sys.exit(main())
