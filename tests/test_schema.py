#!/usr/bin/env python3

import hxlm.core.util
import hxlm.core
import hxlm.routing
import hxlm.core.schema


# hxlm.routing.routing_info()

# print(hxlm.core.schema)

# hxlm.schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hmeta.yml')



# print(hxlm.core.debug())
# print(hxlm.schema)

baseline_meta = hxlm.core.schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hmeta.yml')

print(baseline_meta)
