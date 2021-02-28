"""hxlm.core.schema allow load schemas from YAML without coding
# @see https://pyyaml.org/wiki/PyYAMLDocumentation
"""

# TODO: consider use JSON instead of YAML (so even less external libraries)
import yaml

def get_schema(file):
    # Funciona Ok, exceto com a Noruega https://noyaml.com/

    with open(file) as f:
    
        data = yaml.safe_load(f)
        return data

