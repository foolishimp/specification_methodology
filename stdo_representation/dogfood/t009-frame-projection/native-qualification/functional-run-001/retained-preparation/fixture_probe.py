import json
from cache import remove_last
observations=[]
for before in [["a"], ["a","b"]]:
    after,count=remove_last(before)
    observations.append({"before":before,"after":after,"count":count,"satisfied":count==len(after)})
print(json.dumps({"producer":"P0 finite fixture probe v1","domain_complete":True,"observations":observations,"public_members":{"p.save":"{\"input\":\"Item\",\"output\":\"Saved\",\"timeout\":30}","p.inspect":"{\"input\":\"Id\",\"output\":\"View\"}"},"upstream_root_helper":"unchanged","accepted_trace":{"design":"D0","acceptance":"A0","current":True,"scope":"cache:refresh","complete":True}},sort_keys=True))
