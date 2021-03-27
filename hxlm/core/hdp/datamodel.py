"""hxlm.core.hdp.datamodel is focused on data model strictly related to HDP

See also:
  - hxlm/core/types.py
  - hxlm/core/htype/

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from dataclasses import InitVar, dataclass
from dataclasses import dataclass

from typing import (
    List,
    Union
)


@dataclass
class HDPRaw:
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.

    """

    raw: str
    """The RAW string value"""

    hsilos: List[dict]
    """The list of hsilos"""

    # def about(self, key: str = None):
    #     """Export values"""
    #     about = {
    #         'raw': self.raw,
    #         'hsilos': self.hsilos,
    #     }
    #     if key:
    #         if key in about:
    #             return about[key]
    #         return None
    #     return about


@dataclass
class AttrAdm0:
    """Country/territory"""
    value: str


@dataclass
class AttrDescriptionem:
    """Description with localized key, examples
      descriptionem:
        ARA: "الإعلان العالمي لحقوق الإنسان"
        ENG: Universal Declaration of Human Rights
        FRA: Déclaration universelle des droits de l’homme
    """
    values: dict


@dataclass
class HDatumItem:
    """A Data set group"""
    _id: str
    descriptionem: AttrDescriptionem
    tag: List[str]


@dataclass
class HFilumItem:
    """A File"""
    _id: str
    descriptionem: AttrDescriptionem
    tag: List[str]


@dataclass
class HTransformareItem:
    """Data transformation"""
    _id: str
    descriptionem: AttrDescriptionem
    tag: List[str]
    grupum:  List[str]


@dataclass
class HMetaItem:
    """An individual item in an metadata header reference.
    Like the 'salve mundi!' in the:

    - ([Lingua Latina]):
      - salve mundi!
      - (CRC32 'α "3839021470")
    """

    _type: str  # CRC, raw string, etc

    value_raw: str
    """The raw value"""


@dataclass
class HMetaWrapper:
    """The metadata header reference.

    Like the entire group:

    - ([Lingua Latina]):
      - salve mundi!
      - (CRC32 'α "3839021470")

    Note: the last item of an HMetaWrapper can be another HMetaWrapper!
    """

    values: List[Union[HMetaItem, 'HMetaWrapper']]
    """Ordered list of values"""


@dataclass
class HSiloItem:
    """Individual HSilo (one physical file could have multiple"""


@dataclass
class HSiloWrapper:
    """Individual HSilo (one physical file could have multiple)"""

    hdatum: List[HDatumItem]
    """A list of HDatum (data sets)"""

    hfilum: List[HFilumItem]
    """A list of Hfilum (files)"""

    hsilo: HSiloItem
    """The HSilo representation"""

    htransformare: List[HTransformareItem]
    """Data transformation"""

    source_raw: dict
    """The original source, without any changes"""
