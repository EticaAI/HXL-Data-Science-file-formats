"""hxlm.core.io.converter

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from functools import reduce, lru_cache
from typing import (
    Any,
    # Union
)

import json
# import csv
import yaml


def to_json(thing: Any, indent=4, sort_keys=True, ensure_ascii=False) -> str:
    """Generic JSON exporter

    Args:
        thing (Any): Object to convert to JSON string
        indent (int, optional): JSON string ident. Defaults to 4.
        sort_keys (bool, optional): If keys are shorted. Defaults to True.

    Returns:
        str: Returns an JSON formated string
    """

    return json.dumps(thing, indent=indent, sort_keys=sort_keys,
                      ensure_ascii=ensure_ascii)


def to_yaml(thing: Any) -> str:
    """Generic YAML exporter

    Returns:
        str: Returns an YAML formated string
    """

    return yaml.dump(thing, Dumper=Dumper,
                     encoding='utf-8', allow_unicode=True)


class Dumper(yaml.Dumper):
    """Force identation on pylint, https://github.com/yaml/pyyaml/issues/234
    TODO: check on future if this still need
          (Emerson Rocha, 2021-02-28 10:56 UTC)
    """

    def increase_indent(self, flow=False, *args, **kwargs):  # noqa
        return super().increase_indent(flow=flow, indentless=False)
