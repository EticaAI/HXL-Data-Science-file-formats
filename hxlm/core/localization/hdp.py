"""hxlm.core.localization.hdp is an draft

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os


import hxlm.core.util as Cutil

from hxlm.core.localization.util import (
    # HXLM_CORE_LOCALIZATION_CORE_LOC
    get_localization_lids
)

# TODO: move vocabulary conversions from hxlm.core.schema.vocab to here
#       (Emerson Rocha, 2021-03-20 03:01 UTC)

__all__ = ['get_hdp_term_cleaned']

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))

HDP_TOKEN_CHARS = (
    '[',
    # '[[',
    '(',
    # '((',
    '{',
    # '{{',
    '<',
    # '<<',
    ']',
    # ']]',
    ')',
    # ')',
    '}'
    # '}}'
    '>'
    # '>>'
)


def get_hdp_term_cleaned(term: str) -> str:
    """get_hdp_term_cleaned is (TODO: document)"""
    for tkc in HDP_TOKEN_CHARS:
        term = term.replace(tkc, '')
    return term


def get_lid_from_keyterm(keyterm: str) -> dict:
    """From an full keyterm, return an object from core_loc

    Args:
        keyterm (str): keyterm to search

    Returns:
        dict: An HDP Location ID object

    Examples:
        >>> import hxlm.core.localization.hdp as hdploc
        >>> hdploc.get_lid_from_keyterm('([LAT])')['lid']
        'LAT-Latn'
        >>> hdploc.get_lid_from_keyterm('([RUS-Cyrl])')['q']
        'Q7737'
        >>> hdploc.get_lid_from_keyterm('[LAT]')
        >>> # This should return None
        >>> hdploc.get_lid_from_keyterm('(LAT)')
        >>> # This should return None
        >>> hdploc.get_lid_from_keyterm('([Língua portuguesa])')['iso3693']
        'POR'
        >>> hdploc.get_lid_from_keyterm('([Português])')['iso3693']
        'POR'
        >>> hdploc.get_lid_from_keyterm('([Língua tupi]POR)')
    """
    # The minimal viable term is '([ZZZ])', We do some quick checks
    if len(keyterm) < 7 or \
            not keyterm.startswith('(') or not keyterm.endswith(')') or \
            keyterm.index('[') == -1 or keyterm.index(']') == -1:
        return None

    hpd_lkb = get_localization_lids()
    kt_norm1 = get_hdp_term_cleaned(keyterm)

    # print(hpd_lkb)

    # Both '([ZZZ])' and '([ZZZ-Xxxx])', like ([RUS-Cyrl]), are very specific
    if len(keyterm) == 7 and len(kt_norm1) == 3:
        return Cutil.get_object_if_value_eq_on_key(hpd_lkb,
                                                   'iso3693', kt_norm1)
    if len(keyterm) == 12 and len(kt_norm1) == 8 and keyterm.index('-') != -1:
        return Cutil.get_object_if_value_eq_on_key(hpd_lkb,
                                                   'lid', kt_norm1)

    # Now we do an typical search
    test1 = Cutil.get_object_if_value_eq_on_key(hpd_lkb, 'klid', kt_norm1)
    if test1:
        return test1

    test2 = Cutil.get_object_by_value_in_key(hpd_lkb, 'klid_alts', kt_norm1)

    if test2:
        return test2

    # TODO: support syntax like '([Língua tupi]POR)', see
    #       https://pt.wikipedia.org/wiki/L%C3%ADngua_tupi

    return None


def get_hdp_raw_object_language(hdp_robj: dict) -> dict:
    """For an RAW HDP individual object, return the natural language

    This will search for tokens like '([Lingua Latina])', ([Русский язык]),
    '(['اللغة العربية الفصحى الحديثة'])', etc and return the language.

    Args:
        hdp_robj (dict): [description]

    Returns:
        dict: [description]
    """
    # TODO: draft get_hdp_silo_language
    result = {
        'todo': hdp_robj
    }
    return result
