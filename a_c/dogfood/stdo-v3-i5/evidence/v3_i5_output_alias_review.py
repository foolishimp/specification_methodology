import importlib.util, os, sys, tempfile
from pathlib import Path
path=Path('/Users/jim/src/apps/specification_methodology/a_c/dogfood/v3_graphify_upstream.py')
spec=importlib.util.spec_from_file_location('v3upstreamreview',path); mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod)
with tempfile.TemporaryDirectory(prefix='v3-output-review-') as temp:
 root=Path(temp); protected=root/'subject.json'; protected.write_text('{"tenant":"review"}')
 alias=root/'report.json'; os.link(protected,alias)
 mod.source_paths=lambda consumer:{'subject':protected}
 mod.qualification=lambda args:{'status':'passed'}
 sys.argv=['review','--tenant','claude','--upstream',str(root),'--out',str(alias)]
 rc=mod.main()
 print({'return_code':rc,'protected_source_overwritten':protected.read_text()!='{"tenant":"review"}','same_file':protected.samefile(alias)})
