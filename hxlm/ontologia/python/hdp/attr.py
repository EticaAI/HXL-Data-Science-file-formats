"""hxlm.ontologia.python.hdp.attr is an draft. Not implemented yet

- attr (Latin: Attributus):
  - This file contains classes related to HDP attributes'.
    Most of the time this is an syntatic sugar for who create code with HXLm
    do not work with plain objects (it helps with code autocomplete)
  - This module DOES represents direct implementation of some parts of VKG/LKGs

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
