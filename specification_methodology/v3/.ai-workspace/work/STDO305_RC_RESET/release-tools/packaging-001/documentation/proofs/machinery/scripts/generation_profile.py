"""Tenant-owned parameterized ordinary-generation signature contract (version 1)."""
from __future__ import annotations
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from urllib.parse import quote, unquote

PROFILE_PATH = Path(__file__).resolve().parents[1] / 'profiles/generation-signature-v1.json'
PROFILE = 'a_c.lean.generation-signature/1'

class ProfileError(ValueError):
    def __init__(self, message, *, unsupported=False):
        super().__init__(message); self.unsupported = unsupported

def validate_generation_profile(model: dict) -> dict:
    try:
        subject = model['basis']['subject']['id']
        if type(subject) is not str:
            raise ProfileError('generation subject identity must be a string')
        prefix = 'urn:a-c:generation:' + hashlib.sha256(subject.encode()).hexdigest()[:24] + ':'
        signature = model['signature']
        if type(signature) is not dict:
            raise ProfileError('generation signature must be an object')
        if signature.get('id') != prefix + 'signature:compact-source-proposal-v1':
            raise ProfileError('unsupported signature/profile identity', unsupported=True)
        template = json.loads(PROFILE_PATH.read_text())
        if template['profile'] != PROFILE:
            raise ProfileError('selected generation profile is not version 1')
        expected = json.loads(json.dumps(template['definition'], ensure_ascii=False).replace('$NS:', prefix))
        actual_kinds = signature['definition']['relation_kinds']
        if type(actual_kinds) is not dict:
            raise ProfileError('generation relation catalog must be an object')
        governing = []
        for identity, definition in actual_kinds.items():
            stem = prefix + 'relation-kind:'
            if type(identity) is not str or not identity.startswith(stem):
                raise ProfileError('relation-kind namespace is not the exact subject namespace')
            suffix = identity[len(stem):]
            category, separator, label = suffix.partition(':')
            if category not in ('governing', 'discovery') or not separator or not label or quote(unquote(label),safe=':/') != label:
                raise ProfileError('unsupported generation relation-kind parameter')
            is_governing = category == 'governing'
            endpoint = deepcopy(expected['fields']['relations']['source'])
            endpoint['governing'] = is_governing
            expected['relation_kinds'][identity] = {
                'source':endpoint, 'target':deepcopy(endpoint),
                'qualifiers':deepcopy(expected['fields']['relations']['qualifiers'])}
            if is_governing: governing.append(identity)
        if signature['definition'] != expected:
            raise ProfileError('signature changes fixed generation fields/domains/cardinality/governing semantics')
        encoded = json.dumps({'id':signature['id'],'definition':expected},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
        if signature['sha256'] != hashlib.sha256(encoded).hexdigest():
            raise ProfileError('stale generation signature digest')
        if model['dependency_contract']['required_relation_kinds'] != sorted(governing):
            raise ProfileError('generation required relation kinds differ from exact governing catalog')
        if model['dependency_contract']['id'] != prefix+'dependency-contract:authored-governing-relations':
            raise ProfileError('generation dependency contract identity mismatch')
        if any(model['populations'][f] for f in ('traversals','transformations','judgments')) or model['functor_bindings'] != {}:
            raise ProfileError('ordinary generation v1 has explicitly empty traversal/transformation/judgment populations')
        return {'profile':PROFILE,'namespace':prefix,'signature_sha256':signature['sha256'],
                'relation_kinds':len(actual_kinds),'governing_relation_kinds':governing}
    except ProfileError:
        raise
    except (KeyError,TypeError,UnicodeError) as exc:
        raise ProfileError('malformed ordinary-generation profile: '+str(exc)) from exc
