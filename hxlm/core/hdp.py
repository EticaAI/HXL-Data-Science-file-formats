"""hxlm.core.hdp

This module provide some aliases for HDP functionality

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

__all__ = [
    'get_language_identifiers',
    'get_metadata',
    'transpose'
]

from hxlm.core.localization.hdp import (  # noqa
    get_language_identifiers,
    get_metadata,
    transpose
)
