"""hxlm.core.internal.signature contains hash-like functions

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from typing import (
    Union
)


def get_normalized_string(thing: Union[str, dict, list]) -> str:
    if isinstance(thing, str):
        return thing