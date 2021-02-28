"""hxlm.core.schema allow load schemas from YAML without coding
# @see https://pyyaml.org/wiki/PyYAMLDocumentation
"""

import yaml
import json


def export_schema_yaml(schema):
    return yaml.dump(schema)
    # print('todo')


def export_schema_json(schema):
    return json.dumps(schema)


def get_schema(file):
    # Funciona Ok, exceto com a Noruega https://noyaml.com/

    with open(file) as f:

        data = yaml.safe_load(f)
        return data
