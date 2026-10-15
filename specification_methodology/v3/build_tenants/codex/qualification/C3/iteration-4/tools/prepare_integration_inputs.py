"""Pin returned patches and their exact scoped field preimages."""
import json
from context import HERE, REPO, encoded, git_bytes, read, sha, write
from reconcile_account import get_path, owned_family, scoped_operations

RECEIVING_COMMIT='989ee2278d4a5d9bcfbfc80570570450ee811b24'
RECEIVING_SHA='b8c43489311b387045de129db459ef1bf29c1334724fcccc36474ea9565fedcd'
SELECTED=[('delivery-selector','source_repair'),('dmm-governance','source_repair'),
          ('core-routing','account_routing'),('profile-routing','account_routing'),
          ('delivery-routing','account_routing')]


def main():
    raw=git_bytes(RECEIVING_COMMIT,(HERE/'DETERMINATIONS.json').relative_to(REPO))
    if sha(raw)!=RECEIVING_SHA:
        raise ValueError('Receiving account preimage differs')
    rows={r['id']:r for r in json.loads(raw)['determinations']}
    selected=[]
    for name,stage in SELECTED:
        path=HERE/'source'/name/'ACCOUNT_PATCH.json'
        part=read(path)
        record={'path':str(path.relative_to(HERE)),'sha256':sha(path.read_bytes()),'stage':stage}
        if stage=='account_routing':
            record['before_fields']={}
            if name=='profile-routing':
                record['excluded_items']={
                    'DESIGN_MODULE_METHOD.11a-governancestrategy-separation-rule':
                    {'reason':'The known local law now has a direct source argument; its prior unresolved table-binding proposal is superseded.',
                     'replacement':'source/dmm-governance/ACCOUNT_PATCH.json'}}
            for item in part['patches']:
                expected={}
                for key in set(item.get('set',{})) | set(item.get('semantic_fields',{})):
                    value=get_path(rows[item['id']],key)
                    scope=scoped_operations(item).get(key)
                    if scope:
                        value=[x for x in (value or []) if owned_family(x,scope)]
                    expected[key]=sha(encoded(value))
                record['before_fields'][item['id']]=expected
        selected.append(record)
    write(HERE/'INTEGRATION_INPUTS.json',{
        'receiving_account':{'commit':RECEIVING_COMMIT,'sha256':RECEIVING_SHA,
                            'standing':'intermediate authored account; not a qualified package'},
        'patches':selected,
        'application':'Original three source patches and delivery dependencies first; source repairs enter at their owners. Scoped routing preserves other owners. Field preimages refuse unexpected overlap.'})
    print({'selected_returns':len(selected)})


if __name__=='__main__':
    main()
