"""hxlm.core.hdp.util.debug

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# Vocabularies:
# - "explanare":
#   - explano: https://en.wiktionary.org/wiki/explano#Latin
#   - explanare: https://en.wiktionary.org/wiki/explanare#Latin
# - "optionem":
#   - https://en.wiktionary.org/wiki/optio#Latin

from typing import (
    Any
)


def explanare(thing: Any) -> str:
    """Generic converter for things to str. Not as useful.

    Args:
        thing (Any): Anything that can be converted to str

    Returns:
        str: String
    """
    return str(thing)


def explanare_optionem(thing: Any) -> str:
    """Output debug information from data structures used on HDP containers

    Args:
        thing (Any): Anything that can be converted to str

    Returns:
        str: String
    """
    return str(thing)
