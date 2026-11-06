#!/usr/bin/env python3
"""Observe the pinned installed Graphify roundtrip for an exact selected model."""
from pathlib import Path
import argparse
import hashlib
import importlib
import importlib.metadata
import json
import os
import sys
import subprocess

import ac_graph
import ac_generate as gen


def read(path):
    path = Path(path).absolute()
    gen.require(not any(p.is_symlink() for p in (path, *path.parents)) and path.is_file(), 'Input must be a regular non-redirected file: '+str(path))
    return path.read_bytes()


def digest(raw): return hashlib.sha256(raw).hexdigest()


def run(model_path, carrier_path, selections_path, upstream, runtime_path, output):
    output = Path(output).absolute(); upstream = Path(upstream).absolute()
    gen.require(not output.exists() and not any(p.is_symlink() for p in (output,*output.parents)), 'Output must be a fresh non-redirected directory')
    inputs = {name: read(path) for name,path in [('model',model_path),('carrier',carrier_path),('selections',selections_path),('runtime',runtime_path)]}
    resolved_output = output.resolve()
    for path in (model_path,carrier_path,selections_path,runtime_path,upstream):
        resolved_input = Path(path).resolve()
        gen.require(not resolved_input.is_relative_to(resolved_output)
                    and not resolved_output.is_relative_to(resolved_input), 'Output overlaps an input')
    runtime = gen._decode(inputs['runtime'])
    gen.require(runtime.get('version')=='3.0.5' and runtime.get('status')=='installed', 'Unsupported installed runtime')
    invocation = Path(sys.executable).absolute()
    gen.require(runtime.get('python')==str(invocation) and sys.prefix!=sys.base_prefix, 'Invoke the selected private runtime Python, preserving its virtualenv path')
    gen.require(Path(runtime.get('upstream','')).resolve()==upstream.resolve() and runtime.get('upstream_commit')==gen.UPSTREAM_COMMIT, 'Runtime selects a different upstream')
    root = Path(__file__).resolve().parents[3]
    gen.require(runtime.get('bootstrap_sha256')==digest(read(root/'scripts/bootstrap.py')), 'Runtime bootstrap source changed')
    for name, expected in runtime.get('requirements',{}).items():
        gen.safe_relative(name)
        gen.require(digest(read(Path(__file__).resolve().parents[1]/name))==expected, 'Runtime requirement source changed')
    gen.require(set(runtime.get('requirements',{}))=={'test_env/requirements-qualification.txt','code/generation/requirements.txt','code/code-requirements.txt'}, 'Runtime requirement population differs')
    packages = {}
    for name in runtime['requirements']:
        for line in read(Path(__file__).resolve().parents[1]/name).decode().splitlines():
            line = line.strip()
            if not line or line.startswith('#'): continue
            package, version = line.split('==')
            gen.require(importlib.metadata.version(package)==version, 'Installed dependency differs from exact pin: '+package)
            packages[package] = version
    package_probe = [str(invocation), '-m', 'pip', 'freeze', '--all']
    package_bytes = subprocess.check_output(package_probe)
    gen.require(digest(package_bytes)==runtime.get('packages_sha256'), 'Private installed package population changed after bootstrap')
    model = ac_graph.validate(gen._decode(inputs['model']))
    carrier = ac_graph.GraphCarrier(gen._decode(inputs['carrier']))
    gen.require(ac_graph.decode(carrier).document==model.document, 'Selected carrier differs from selected model')
    selections = gen._decode(inputs['selections'])
    gen.require(isinstance(selections,list) and bool(selections), 'Select a nonempty ordered projection list')
    for selection in selections:
        gen.require(isinstance(selection,dict) and set(selection)=={'seeds','budget_records'}, 'Malformed projection selection')
    views = ac_graph.project_many(model,[(selection['seeds'],selection['budget_records']) for selection in selections])
    modules = gen.upstream_modules(upstream)
    loader = importlib.import_module('graphify.paths')
    gen.require(Path(loader.__file__).resolve().is_relative_to(upstream.resolve()), 'Graph loader imported from a different installation')
    output.mkdir(parents=True)
    for name, raw in inputs.items(): (output/(name+'.json')).write_bytes(raw)
    graph = modules['build'].build_from_json(ac_graph.extraction(carrier),dedup=False)
    gen.require(modules['export'].to_json(graph,{},str(output/'graph.json'),force=True,built_at_commit=gen.UPSTREAM_COMMIT),'Actual upstream export refused')
    loaded = loader.load_node_link_graph(output/'graph.json')
    recovered = ac_graph.decode(ac_graph.GraphCarrier(gen.load(output/'graph.json')))
    gen.require(recovered.document==model.document,'Actual upstream roundtrip changed selected model')
    expected_ids = {node['id'] for node in carrier.document['nodes']}
    gen.require(set(graph.nodes)==expected_ids and set(loaded.nodes)==expected_ids, 'Actual upstream node population changed')
    gen.require(graph.number_of_edges()==loaded.number_of_edges()==len(carrier.document['links']), 'Actual upstream occurrence edge population changed')
    gen.require(ac_graph.project_many(recovered,[(s['seeds'],s['budget_records']) for s in selections])==views,'Recovered projection changed')
    gen.save(output/'views.json',views)
    source_pins = {name:digest(read(Path(__file__).with_name(name))) for name in ('ac_upstream.py','ac_generate.py','ac_graph.py')}
    loaded_modules = {}
    for name,module in sorted(sys.modules.items()):
        path = getattr(module,'__file__',None)
        if not path: continue
        path = Path(path).resolve()
        if path.is_file() and (path.is_relative_to(upstream.resolve()) or path.is_relative_to(Path(sys.prefix).resolve()) or path.is_relative_to(Path(__file__).parent.resolve())):
            loaded_modules[name] = {'path':str(path),'sha256':digest(path.read_bytes())}
    gen.verify_upstream(upstream)
    result = {'schema':'a_c.graphify.current-roundtrip/1','status':'verified','version':'3.0.5',
              'model':{'id':model.document['id'],'raw_sha256':digest(inputs['model']),'canonical_sha256':model.sha256},
              'carrier_raw_sha256':digest(inputs['carrier']),'selections':selections,'views_sha256':digest(read(output/'views.json')),
              'upstream_trial':{'commit':gen.UPSTREAM_COMMIT,'nodes':loaded.number_of_nodes(),'edges':loaded.number_of_edges(),'decoded_model_sha256':recovered.sha256},
              'runtime':{'receipt_path':str(Path(runtime_path).absolute()),'receipt_sha256':digest(inputs['runtime']),
                         'python_invocation':str(invocation),'python_physical':str(invocation.resolve()),'python_sha256':digest(invocation.resolve().read_bytes()),
                         'prefix':sys.prefix,'base_prefix':sys.base_prefix,'source_pins':source_pins,'loaded_modules':loaded_modules,
                         'required_packages':packages,'package_probe':{'argv':package_probe,'returncode':0,'stdout_sha256':digest(package_bytes)}},
              'artifacts':{p.name:digest(p.read_bytes()) for p in output.iterdir() if p.is_file()},
              'claim':'Actual pinned build/export/path-load/decode preserves this declared model and its selected views; no source-prose fidelity or acceptance claim.'}
    gen.save(output/'result.json',result)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('model','carrier','selections','upstream','runtime','output'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    try:
        result=run(a.model,a.carrier,a.selections,a.upstream,a.runtime,a.output)
        print(json.dumps(result,sort_keys=True));return 0
    except (OSError,ValueError,KeyError,TypeError,ImportError,subprocess.SubprocessError) as error:
        print(json.dumps({'schema':'a_c.graphify.current-roundtrip/1','status':'refused_or_incomplete','reason':str(error),'recovery':'Retain partial output; no overwrite or blind retry.'}));return 2

if __name__=='__main__': raise SystemExit(main())
