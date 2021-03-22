"""hxlm.core.internal.integrity contains hash-like functions

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hashlib import md5, sha256

from typing import (
    Union
)

import json

__all__ = ['get_hashable', 'get_hashable_json', 'is_json_string']


def _get_hash_md5(thing) -> str:
    """MD5 hash (inly for data integrity / detect unintentional corruption)
    From https://en.wikipedia.org/wiki/MD5:
        "The MD5 message-digest algorithm is a widely used hash function
        producing a 128-bit hash value. Although MD5 was initially designed
        to be used as a cryptographic hash function, it has been found
        to suffer from extensive vulnerabilities.

        It can still be used as a checksum to verify data integrity,
        but only against unintentional corruption"

    See also:
    - https://eprint.iacr.org/2013/170.pdf
    """
    return md5(str(thing).encode('utf-8')).hexdigest()


def _get_hash_sha2_256(thing) -> str:
    """MD5 hash (inly for data integrity / detect unintentional corruption)
    From https://en.wikipedia.org/wiki/SHA-2:
        "SHA-2 (Secure Hash Algorithm 2) is a set of cryptographic hash
        functions designed by the United States National Security Agency
        (NSA) and first published in 2001.

         It can still be used as a checksum to verify data integrity,
         but only against unintentional corruption"
    """

    return sha256(str(thing).encode('utf-8')).hexdigest()


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

    return get_hashable_json(jsonlike)


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
    """Check if is an JSON-like string and return as JSON object if yes

    Args:
        thing (str): The input

    Returns:
        Union[bool, str]: Either False (not JSON-like input) or the result
    """
    try:
        json_object = json.loads(thing)
        return json_object
    # except ValueError as err:
    except ValueError:
        return False
    return None
