"""hxlm.core.schema allow load schemas from YAML without coding
# @see https://pyyaml.org/wiki/PyYAMLDocumentation
"""

from typing import (
    Union
)

import json
import yaml

from hxlm.core.model.meta import (
    HMeta
)
from hxlm.core.schema.vocab import (
    ItemHVocab
)

__all__ = ['export_schema_yaml', 'export_schema_json', 'get_schema',
           'get_schema_as_hmeta', 'get_schema_vocab']


def export_schema_yaml(schema: HMeta) -> str:
    """Export an schema as YAML format

    Args:
        schema (HMeta): An HMeta instance

    Returns:
        str: result schema in valid YAML format
    """
    # return yaml.dump(schema, indent=4)
    # @see https://github.com/yaml/pyyaml/issues/234

    return yaml.dump(schema, Dumper=Dumper)


def export_schema_json(schema: HMeta) -> str:
    """Export an schema as YAML format

    Args:
        schema (HMeta): An HMeta instance

    Returns:
        str: Result schema in valid JSON format
    """
    return json.dumps(schema)


def get_schema(file):
    """Get an HMeta schema from file (raw object, without Model)

    Args:
        file (String): Object containing the schema on local disk

    Returns:
        Object: Raw object from YAML file
    """
    # Funciona Ok, exceto com a Noruega https://noyaml.com/

    with open(file) as f:

        data = yaml.safe_load(f)
        # data = yaml.safe_load_all(f)
        # print(data)
        return data


def get_schema_as_hmeta(file):
    """Get an HMeta schema from file (raw object, without Model)

    Args:
        file (String): Object containing the schema on local disk

    Returns:
        Object: Raw object from YAML file
    """
    # Funciona Ok, exceto com a Noruega https://noyaml.com/

    with open(file) as f:

        data = yaml.safe_load(f)
        hmeta = HMeta()
        hmeta.load_schemas(schemas_raw=data)
        # hmeta.export_schemas(schemas=data)
        # data = yaml.safe_load_all(f)
        # print(data)
        # return data
        # return hmeta.export_schemas()

        # For debug, use this (will just export the input)
        return {'as_meta': hmeta.export_schemas(),
                'raw': hmeta.export_schemas_raw()}


def get_schema_vocab(vocab: Union[str, dict] = None,
                     allow_local: bool = False):
    if vocab is not None:
        vocab = ItemHVocab(vocab=vocab, allow_local=allow_local)
    else:
        vocab = ItemHVocab()
    return vocab


class Dumper(yaml.Dumper):
    """Force identation on pylint, https://github.com/yaml/pyyaml/issues/234
    TODO: check on future if this still need
          (Emerson Rocha, 2021-02-28 10:56 UTC)
    """

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
