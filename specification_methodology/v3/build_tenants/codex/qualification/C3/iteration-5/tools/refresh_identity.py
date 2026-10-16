"""Rebuild packaged historical verification material after source changes."""
import argparse
import build_interpretation as build
from pathlib import Path
from context import HERE, PACKAGE, INPUTS, library, sha, write


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-commit',required=True)
    parser.add_argument('--theory-root',type=Path,required=True)
    args=parser.parse_args()
    build.documentary_inventory(args.source_commit)
    build.verify_dependencies(args.theory_root)
    helper=library('synthesis/derivation_material.py')
    before=sha((PACKAGE/helper.RESOURCE).read_bytes())
    material=helper.build(PACKAGE,args.theory_root)
    report=helper.test(PACKAGE)
    if not report['valid']:
        raise ValueError('Reconstructed historical basis failed')
    write(HERE/'IDENTITY_BUILD.json',{
        'documentary_preimage':args.source_commit,
        'generator_sha256':INPUTS['libraries']['synthesis/derivation_material.py'],
        'historical_manifest_sha256':build.MANIFEST_SHA,
        'resource':helper.RESOURCE,'before_sha256':before,
        'sha256':sha((PACKAGE/helper.RESOURCE).read_bytes()),
        'bytes':(PACKAGE/helper.RESOURCE).stat().st_size,
        'principle_refs':len(material['principle_refs']),
        'verified_historical_members':len(material['members']),
        'cold_check':report,
        'limits':['Reconstruction and fixture verification only, not independent derivation or release acceptance.']})
    print({'valid':report['valid'],'negative_controls':len(report['negative_controls']),
           'historical_members':len(material['members'])})


if __name__=='__main__':
    main()
