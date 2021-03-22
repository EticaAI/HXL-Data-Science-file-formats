"""hxlm.core.internal.integrity contains hash-like functions

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from typing import (
    Union
)

import json

__all__ = ['get_hashable_result']


def get_hashable(thing: Union[str, dict, list]) -> str:
    """Get an normalized string ready to be normalized

    Args:
        thing (Union[str, dict, list]): Input source

    Returns:
        str: String ready to be hashed

    Examples:
        >>> import hxlm.core.internal.integrity as HDP_i
        >>> HDP_i.get_hashable('test string')
        'test string'
        >>> HDP_i.get_hashable(12345)
        '12345'
    """
    if isinstance(thing, str):
        jsonlike = is_json_string(thing)
        if not jsonlike:
            return thing
        else:
            return get_hashable_json(jsonlike)
        return thing
    if isinstance(thing, int):
        return str(thing)


def get_hashable_json(thing: Union[dict, list]) -> str:
    """[summary]

    Args:
        thing (Union[dict, list]): [description]

    Returns:
        str: An JSON string ideal for hashing
    Examples:
        >>> import hxlm.core.internal.integrity as HDP_i
        >>> HDP_i.get_hashable_json(['test'])
        '["test"]'
    """
    # json_object = json.load(thing)
    return json.dumps(thing, indent=None, sort_keys=True)


def is_json_string(thing: str) -> Union[bool, str]:
    try:
        json_object = json.loads(thing)
        return json_object
    # except ValueError as err:
    except ValueError:
        return False
    return None
