#!/usr/bin/env python3

import hxlm.core.util
import hxlm.core
import hxlm.routing
import hxlm.core.schema as schema

# hxlm.routing.routing_info()

# print(hxlm.core.schema)

# hxlm.schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hmeta.yml')

# print(hxlm.core.debug())
# print(hxlm.schema)

example = schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline/hmeta.yml')

# print('get_schema (source file)')
# print(example)
# get_schema (source file)
# {'$schema': 'https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/hxlm/core/schema/hxlm.schema.json', 'title': 'hxml.core.data.baseline', 'hdatasets': [{'key': 'place', 'comments': 'HXL-CPLP-FOD_countries-territories.csv', 'source': 'https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0', 'tags': ['ISO 3166', 'ISO 3166-2', 'ISO 3166-3']}, {'key': 'lang', 'comments': 'HXL-CPLP-FOD_languages', 'source': 'https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0', 'tags': ['ISO 639-3', 'ISO 3692-2', 'ISO 3692-3']}], 'hfiles': [{'key': 'TODO.txt'}]}

print('export_schema_yaml (string to export)')
print(schema.export_schema_yaml(example))
# export_schema_yaml (string to export)
# $schema: https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/hxlm/core/schema/hxlm.schema.json
# hdatasets:
# - comments: HXL-CPLP-FOD_countries-territories.csv
#   key: place
#   source: https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0
#   tags:
#   - ISO 3166
#   - ISO 3166-2
#   - ISO 3166-3
# - comments: HXL-CPLP-FOD_languages
#   key: lang
#   source: https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0
#   tags:
#   - ISO 639-3
#   - ISO 3692-2
#   - ISO 3692-3
# hfiles:
# - key: TODO.txt
# title: hxml.core.data.baseline

# print('export_schema_json (string to export)')
# print(schema.export_schema_json(example))
# export_schema_json (string to export)
# {"$schema": "https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/hxlm/core/schema/hxlm.schema.json", "title": "hxml.core.data.baseline", "hdatasets": [{"key": "place", "comments": "HXL-CPLP-FOD_countries-territories.csv", "source": "https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0", "tags": ["ISO 3166", "ISO 3166-2", "ISO 3166-3"]}, {"key": "lang", "comments": "HXL-CPLP-FOD_languages", "source": "https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0", "tags": ["ISO 639-3", "ISO 3692-2", "ISO 3692-3"]}], "hfiles": [{"key": "TODO.txt"}]}



schema_baseline = schema.get_schema('/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/core/schema/baseline.yml')
print('export_schema_yaml schema_baseline')
print(schema.export_schema_yaml(schema_baseline))