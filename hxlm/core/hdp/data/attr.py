"""hxlm.core.hdp.data.attr

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# https://en.wiktionary.org/wiki/attributus#Latin

from dataclasses import dataclass


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
