"""hxlm.ontologia.python.hdp.radix

- radix (Latin: rādīcem; English: root)
  -  This module contains classes related either to root objects on HDP file
     (like hdatum, hsilo, htransformare...) or pseudo objets that are not
     documented to the end user, but act as somewhat wrapper.
  - Part (not all) of module DOES represents direct implementation of VKG/LKGs

See also:
  - hxlm/core/types.py
  - hxlm/core/htype/

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# TODO: maybe use analogy to 'medicus' to tasks related to recover from errors
#       see https://en.wiktionary.org/wiki/medic
# TODO: resultatum = result, temp varis to return values, etc
#       see resultātum https://en.wiktionary.org/wiki/resultatum#Latin

# >>> Lingua Latina on this document
# "basim":
#  > (linguam->LAT 'basim)
#    > (ENG 'base)
#      - https://en.wiktionary.org/wiki/basis#Latin
# "optionem":
#   > (linguam->LAT 'optionem)
#     - https://en.wiktionary.org/wiki/option#English
#     > (ENG 'option)
#

# >>>> Internal comments about latin usage, ignore this, START
# >? ENG: 'HDP Declarative programming' ?
#    maybe LAT 'HDP declarativa programmandi' ??
#
# >>> TODO: "Program"
#   - ENG https://en.wiktionary.org/wiki/program
#   - LAT https://en.wiktionary.org/wiki/programma#Latin
#   - https://en.wiktionary.org/wiki/program#Ladin
#   - Late Latin 'programma'
# >>> TODO: "Declarative"
#  - ENG https://en.wiktionary.org/wiki/declarative
#    - FRA: https://en.wiktionary.org/wiki/d%C3%A9claratif#Middle_French
#  - "Declare"
#    - FRA https://en.wiktionary.org/wiki/declare
# >>> TODO: etc...
# - Debug messages, convert messages, etc "explain" / "explanare"
#   - https://en.wiktionary.org/wiki/explain
# >>>> Internal comments about latin usage, ignore this, END

# from dataclasses import dataclass, field, InitVar
from dataclasses import dataclass, InitVar

from typing import (
    # Any,
    List,
    # Tuple,
    # Type,
    Union
)

# from hxlm.core.types import (
#     L10NContext
# )

from hxlm.ontologia.python.systema import (
    # EntryPointType,
    ResourceWrapper
)

from hxlm.core.constant import (
    HONTOLOGIA_LKG,
    HONTOLOGIA_VKG
)

from hxlm.ontologia.python.hdp.attr import (
    # AttrAdm0,
    AttrDescriptionem
)

# @dataclass
# class BasimHDPOptionemBasim:
#     """

#     Trivia:
#       - "Optionem" <= ENG option
#         - https://en.wiktionary.org/wiki/option#English
#       - "Basim" <= ENG base
#         - https://en.wiktionary.org/wiki/option#English

#     Raises:
#         NotImplementedError: [description]

#     Returns:
#         [type]: [description]
#     """


__all__ = [
    'HSiloWrapper', 'HDPRaw'
]


@dataclass(init=True, eq=True)
class HDPIndex:
    """An HDP Index object

    Different from most HDP files (that most of the time can reference
    data sets, files, data transformation tasks, etc), HDP index files are
    mostly to be used by people 'building' colletion of HDP files that may be
    in several different places.

    They have a very minimalistic syntax.

    An HDP index file have syntax similar to this:

        # .hdp.yml
        #### Vocabulary Knowledge Graph
        # Notation: ∫, ∬, ∭
        ∫:
          - hxlm/data/core.vkg.yml

        #### Localization Knowledge Graph
        # Notation: ∮, ∯, ∰
        ∮:
          - hxlm/data/core.lkg.yml

        #### HDP Declarative Programming entry points
        # Notation: ∂
        ∂:
          - hxlm/data/hxl/hxl.eng.hdp.yml
          - hxlm/data/udhr/udhr.lat.hdp.yml
    """
    # pylint: disable=invalid-name,non-ascii-name

    resource: ResourceWrapper
    """The ResourceWrapper from this item"""

    hsilos: List['HSiloWrapper']

    # ∂
    hdp: InitVar[list] = []
    """List of HDP indexes files"""

    # ∫
    vkg: InitVar[list] = [
        'file://' + HONTOLOGIA_VKG
    ]
    """List of Vocabulary Knowledge Graph"""

    # ∮, ∯, ∰
    lkg: InitVar[list] = [
        'file://' + HONTOLOGIA_LKG
    ]
    """List of Localization Knowledge Graph"""

    log: InitVar[list] = []
    """Log of messages. Can be used when failed = True or for verbose output"""

    failed: bool = False
    """If something failed"""


@dataclass(init=True, eq=True)
class HDPRaw:
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.

    """

    resource: ResourceWrapper
    """The ResourceWrapper from this item"""

    # hsilos: List[dict]
    hsilos: InitVar[List[dict]] = []
    """The list of hsilos"""

    log: InitVar[list] = []
    """Log of messages. Can be used when failed = True or for verbose output"""

    failed: bool = False
    """If something failed"""

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
