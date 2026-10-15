"""Check current artifacts and cold identity without rewriting old receipts."""
import argparse
import time
from context import HERE, PACKAGE, INPUTS, library, members, read, sha, write


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package-commit', required=True)
    args = parser.parse_args()
    from context import git_bytes, REPO
    inventory = members()
    for member in inventory:
        if sha(git_bytes(args.package_commit, (PACKAGE/member['path']).relative_to(REPO))) != member['sha256']:
            raise ValueError('Package differs from frozen commit: ' + member['path'])
    check = library('synthesis/check_artifacts.py').Check()
    check.links_and_surface()
    check.compressions()
    check.ownership_signals()
    render = library('iteration-3/refresh_current.py')
    changes, index = render.render_views(PACKAGE, HERE, INPUTS['common_input'])
    if any(path.read_text() != value for path, value in changes.items()) or index != read(HERE/'FRAME_INPUTS.json'):
        raise ValueError('Frame/source reproduction differs')
    # The standalone verifier audits only its supplied temporary fixture.
    # It neither issues a release nor reads the historical builder as subject.
    started = time.monotonic()
    identity = library('synthesis/derivation_material.py').test(PACKAGE)
    identity.update(package_commit=args.package_commit,
                    verifier_sha256=INPUTS['libraries']['synthesis/derivation_material.py'],
                    elapsed_seconds=time.monotonic()-started)
    write(HERE/'IDENTITY_CHECK.json', identity)
    result = {'package_commit':args.package_commit, 'members':inventory,
              'common_input':INPUTS['common_input'],
              'checks':check.counts, 'failures':check.failures,
              'frames':len(index['frames']),
              'cold_identity_valid':identity['valid'],
              'negative_identity_controls':len(identity['negative_controls']),
              'limits':['Artifact/reference checks and hypothetical publication fixture only.',
                        'No native installed-v3 admission, actual-use, semantic acceptance or release claim.']}
    write(HERE/'ARTIFACT_CHECK.json', result)
    if check.failures or not identity['valid']:
        raise ValueError('Package checks failed: '+str(check.failures))
    print({k:result[k] for k in ('package_commit','frames','cold_identity_valid','negative_identity_controls')})


if __name__ == '__main__':
    main()
