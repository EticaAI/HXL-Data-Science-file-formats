"""hxlm.core.types contain envelope to internal types that are not Htypes

- https://stackoverflow.com/questions/53409117
  /what-are-the-main-differences-of-namedtuple-and-typeddict-in-python-mypy
  /63218574#63218574

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from dataclasses import dataclass
# from typing import NamedTuple, TypedDict
from enum import Enum


class EntryPointType(Enum):
    """Typehints for entry points to resources (the 'pointer', not content)"""

    RAW_STRING = "RAW_STRING"
    """Generic raw string"""

    UNKNOW = "?"
    """Unknow entrypoint"""

    URN = "URN"
    """Uniform Resource Name, see https://tools.ietf.org/html/rfc8141"""


class URNType(Enum):
    """Uniform Resource Name, see https://tools.ietf.org/html/rfc8141

    See also hxlm/core/htype/urn.py (not fully implemented yet with this)
    """

    DATA = "urn:data"
    """URN Data
    See:
      - https://github.com/EticaAI/HXL-Data-Science-file-formats/tree/main
        /urn-data-specification
    """

    HDP = "urn:hdp"
    """HDP Declarative Programming URN"""

    IETF = "urn:ietf"
    """IETF URN, see https://tools.ietf.org/html/rfc2648"""

    ISO = "urn:ietf"
    """..., see https://tools.ietf.org/html/rfc5141"""

    UNKNOW = "?"
    """Unknow URN type"""
