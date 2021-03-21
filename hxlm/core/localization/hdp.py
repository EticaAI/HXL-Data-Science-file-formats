"""hxlm.core.localization.hdp is an draft

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

# from hxlm.core.localization.util import (
#     # HXLM_CORE_LOCALIZATION_CORE_LOC
#     get_localization_knowledge_graph
# )

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
    """[summary]

    Examples:
        >>> import hxlm.core.localization.hdp as hdploc
        >>> hdploc.get_lid_from_keyterm('([LAT])')
        'LAT'
        >>> hdploc.get_lid_from_keyterm('[LAT]')
        >>> hdploc.get_lid_from_keyterm('(LAT)')
        >>> # This should return None

    Args:
        keyterm (str): [description]

    Returns:
        dict: [description]
    """
    # The minimal viable term is '([ZZZ])', We do some quick checks
    if keyterm is None or len(keyterm) < 7 or not keyterm.startswith('(['):
        return None

    result = {
        'todo': keyterm
    }
    return result


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
