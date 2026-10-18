"""Assemble I5 task routes using the existing pure frame renderer."""
import argparse
import copy
from context import HERE, PRIOR, PACKAGE, INPUTS, library, read, sha, write


def route(member, anchor):
    return {'owner': 'standards/' + member + '.md', 'anchor': anchor}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--reconciliation', required=True,
                        help='Authored current body/source comparison; hashes alone are insufficient')
    parser.add_argument('--routes', required=True, help='Authored I5 frame additions and scopes on this common basis')
    args = parser.parse_args()
    render = library('iteration-3/refresh_current.py')
    comparison = read(args.reconciliation)
    if comparison['common_input'] != INPUTS['common_input']:
        raise ValueError('Wrong common input')
    index = copy.deepcopy(read(PRIOR / 'FRAME_INPUTS.json'))
    for path in sorted((PACKAGE / 'standards/authority_compressions').glob('*.md')):
        pair = render.compression_body(path)
        if pair is None:
            continue
        name = str(path.relative_to(PACKAGE))
        item = comparison['rows'][name]
        if (item['body_sha256'] != sha(pair[1].encode())
                or item['owner_pins'] != render.compression_owners(path, PACKAGE)
                or not item['comparison'] or not item['affected_source_sections']):
            raise ValueError('Unreconciled compression: ' + name)
        index['compression_body_reviews'][name] = item
    by_name = {f['path']:f for f in index['frames']}
    additions = {
        'standards/frames/DOMAIN_BINDING.md': [route('SPEC_METHOD','what-how-and-work-carriers')],
        'standards/frames/RELEASE_ADOPTION.md': [route('FOUNDATIONS','judgment-and-authority')],
    }
    for name, routes in additions.items():
        existing = {(r['owner'],r['anchor']) for r in by_name[name]['routes']}
        by_name[name]['routes'] += [r for r in routes if (r['owner'],r['anchor']) not in existing]
    name = 'standards/frames/MEMBER_CONSTRUCTION_ASSESSMENT.md'
    frame = {'path': name,
        'scope': 'Construct or assess one member against its selected Product requirements and actual grant, preserving domain optionality and separate construction, assessment and acceptance predicates.',
        'routes': [route('FOUNDATIONS','bounded-construction'),route('FOUNDATIONS','result-algebra'),
                   route('FOUNDATIONS','result-conjunction'),route('FOUNDATIONS','judgment-and-authority'),
                   route('TRANSFORMATION_LIBRARY','contract-application'),
                   route('SPEC_METHOD','what-how-and-work-carriers'),
                   route('SPEC_METHOD','construction-assessment-and-delegation'),
                   route('REFERENCE_FRAME_METHOD','minimal-frame-activation-binding')],
        'argument_routes': [route('FOUNDATIONS','core-contract-derivations'),route('SPEC_METHOD','method-families')],
        'route_selection_standing': 'Author-selected rule assembly; the actual task supplies requirements, subject, authority and evidence. Sufficiency requires actual use.'}
    if name not in by_name:
        index['frames'].append(frame)
    authored = read(args.routes)
    if authored.get('common_input') != INPUTS['common_input']:
        raise ValueError('Frame additions name another common basis')
    targets = {f['path']: f for f in index['frames']}
    for addition in authored['frames']:
        target = targets.get(addition['path'])
        if target is None:
            raise ValueError('New frame needs explicit packaging design: ' + addition['path'])
        for field in ('routes', 'argument_routes'):
            for selected in addition.get(field, []):
                if selected not in target.setdefault(field, []):
                    target[field].append(selected)
        if 'scope' in addition:
            target['scope'] = addition['scope']
    for item in index['frames']:
        for selected in item['routes'] + item.get('argument_routes', []):
            render.PARSE.section((PACKAGE / selected['owner']).read_text(), selected['anchor'])
    path = PACKAGE / name
    header = ('# Member Construction And Assessment\n\n'
              'This view supplies method rules for one member task. The activation\n'
              'binds the actual Product requirements, member subject, permitted effects,\n'
              'assessment obligations and decision authority. Domain profiles apply only\n'
              'through their selected adoption conditions. The view supplies no grant or\n'
              'universal sufficiency claim.\n')
    path.write_text(header)
    index['input_commit'] = INPUTS['common_input']
    write(HERE / 'FRAME_INPUTS.json', index)
    changes, final = render.render_views(PACKAGE, HERE, INPUTS['common_input'])
    for target, value in changes.items():
        target.write_text(value)
    write(HERE / 'FRAME_INPUTS.json', final)
    print({'frames': len(final['frames']), 'rendered_members': len(changes)})


if __name__ == '__main__':
    main()
