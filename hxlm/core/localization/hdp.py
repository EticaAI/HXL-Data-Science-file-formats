"""hxlm.core.localization.hdp is an draft

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os
from copy import deepcopy
from typing import Union

import hxlm.core.constant as C
import hxlm.core.util as Cutil
from hxlm.core.localization.util import (
    get_localization_lids
)


# TODO: move vocabulary conversions from hxlm.core.schema.vocab to here
#       (Emerson Rocha, 2021-03-20 03:01 UTC)

__all__ = ['get_hdp_term_cleaned', 'get_language_from_hdp_raw',
           'transpose_hsilo']

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))

# _HDP_RECURSION_LEAF = None

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


# TODO: the VOCAB_RECURSION_LEAF could be on the core_vocab.yml itself, no?

# TODO: solve circular imports and then remove duplicated code.
#       this part on from hxlm.core.schema.vocab
#       (Emerson Rocha, 2021-03-22 08:37 UTC)
# from hxlm.core.schema.vocab import (
#     VOCAB_RECURSION_LEAF
# )
VOCAB_RECURSION_LEAF = (
    'hsilo.adm0',
    'hsilo.grupum',
    # 'hsilo.tag',
    '.tag',
    # 'htransformare.exemplum.fontem.datum',
    'fontem.datum',
)

HDP_VKG = Cutil.load_file(C.HXLM_ROOT + '/core/schema/core_vocab.yml')
"""Vocabulary knowledge graph, aka core_vocab.yml"""

HDP_VKG_FROM: dict = None
"""Dictionary with transposition from other languages back to Latin"""


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
        dict: An HDP LKG dict

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


def get_language_from_hdp_raw(hdp_robj: dict) -> dict:
    """For an RAW HDP individual object, return the natural language

    This will search for tokens like '([Lingua Latina])', ([Русский язык]),
    '(['اللغة العربية الفصحى الحديثة'])', etc and return the language.

    Args:
        hdp_robj (dict): An raw HDP file (as if loaded direct from disk)

    Returns:
        dict: An HDP LKG dict

    Examples
    >>> from hxlm.core.constant import HXLM_TESTS_ROOT
    >>> from hxlm.core.util import load_file
    >>> from hxlm.core.localization.hdp import get_language_from_hdp_raw
    >>> file_path1 = HXLM_TESTS_ROOT + '/htransformare/salve-mundi.lat.hdp.yml'
    >>> hsilo_example1 = load_file(file_path1)
    >>> result1 = get_language_from_hdp_raw(hsilo_example1[0])
    >>> result1['lid']
    'LAT-Latn'
    >>> file_path2 = HXLM_TESTS_ROOT + '/htransformare/salve-mundi.por.hdp.yml'
    >>> hsilo_example2 = load_file(file_path2)
    >>> result2 = get_language_from_hdp_raw(hsilo_example2[0])
    >>> result2['lid']
    'POR-Latn'
    """

    for key in hdp_robj.keys():
        lang_ = get_lid_from_keyterm(key)
        if lang_ is not None:
            return lang_
    return None


def transpose_hsilo(hsilo: dict,
                    target_lid: str, source_lid: str = 'LAT') -> dict:
    """Transpose ('translate') and HSilo from Latin to another language

    If the object already is not in Latin, you should first prepare in Latin
    before use this function

    Args:
        hdp_hsilo (dict): An HSilo object
        target_lid (str): An Localization ID, like RUS-Cyrl

    Returns:
        dict: An transposed HSilo
    """

    # print('target_lid', target_lid)

    if len(target_lid) == 8:
        # We still using 3 letter (like RUS) instead of 8 (like RUS-Cyrl)
        target_lid = target_lid[0:3]
    # print('target_lid', target_lid)

    source_lid = 'LAT'
    active_vkg = HDP_VKG
    # if HPD_VKG is None:
    #     HPD_VKG = Cutil.load_file(C.HXLM_ROOT + '/schema/core_vocab.yml')

    return _transpose_root(hsilo,
                           objectivum_linguam=target_lid,
                           fontem_linguam=source_lid,
                           active_vkg=active_vkg
                           )

    # return hsilo


def _transpose_root(hdp_current: dict,
                    objectivum_linguam: str,
                    fontem_linguam: str = None,
                    active_vkg: dict = HDP_VKG) -> dict:
    """For an hdp_current (already with internal format) get translation

    Args:
        hdp_current (dict): an hdp meta object. Must already have keys in
                            the linguam:HDP
        objectivum_linguam (str): ISO 639-3 code to convert
        fontem_linguam (str): ISO 639-3 code to import. Defaults to none

    Raises:
        SyntaxError: when using ISO 639-3 invalid codes

    Returns:
        dict: And HDP object already translated to target linguam
    """

    # print('oi1', hdp_current)

    if _IS_DEBUG:
        print('HDP._transpose_root', fontem_linguam,
        objectivum_linguam, hdp_current)  # noqa
        # print('HDP._transpose_root', HDP_VKG)

    if len(hdp_current) == 0:
        return hdp_current

    hdp_result = deepcopy(hdp_current)

    if len(objectivum_linguam) != 3 or not objectivum_linguam.isalpha():
        raise SyntaxError('No 3 letter or 3 ASCII letter? ' +
                          'linguam must be an ISO 639-3 (3 letter) ' +
                          'code, like "ARA" or "RUS" ' +
                          '[' + objectivum_linguam + ']')
    if not objectivum_linguam.isupper():
        raise SyntaxError('No UPPERCASE? ' +
                          'linguam must be an ISO 639-3 (3 letter) ' +
                          'code, like "ARA" or "ARA" ' +
                          '[' + objectivum_linguam + ']')

    # for hdpns in hdp_current:
    for hdpns, _ in enumerate(hdp_current):

        # print('hdpns', hdpns)

        # First level
        for key_l1 in hdp_current[hdpns]:
            # for key_l1, _ in enumerate(hdp_current[hdpns]):

            # print('oooi', hdpns, key_l1)
            if ((key_l1 in active_vkg['root']) and
            (objectivum_linguam in active_vkg['root'][key_l1])):  # noqa
                newterm = active_vkg['root'][key_l1][objectivum_linguam]['id']  # noqa
                # print('key_l1 in active_vkg.root', key_l1)
                # print('key_l1 in active_vkg.root', newterm)  # noqa
                hdp_result[hdpns][newterm] = hdp_result[hdpns].pop(key_l1)
                hdp_result[hdpns][newterm] = \
                    _transpose_recursive(
                        hdp_result[hdpns][newterm],
                        objectivum_linguam=objectivum_linguam,
                        fontem_linguam=fontem_linguam,
                        context=key_l1,
                        active_vkg=active_vkg)
            else:

                # print('hdp_current', hdp_current[hdpns])
                # print('hdp_current', 'aaaaaaaaa')

                # TODO: bruteforce here the thing
                # if _IS_DEBUG:
                #     res = self.quid_est_hoc(key_l1)
                #     print('    HDP.quid_est_hoc ', key_l1, res)

                if not str(key_l1).startswith('_'):
                    hdp_result[hdpns][key_l1] = \
                        _transpose_recursive(
                        hdp_current[hdpns][key_l1],
                        objectivum_linguam=objectivum_linguam,
                        fontem_linguam=fontem_linguam,
                        context=key_l1,
                        active_vkg=active_vkg)

    return hdp_result


def _transpose_recursive(hdp_current: Union[dict, list],
                         objectivum_linguam: str,
                         fontem_linguam: str = None,
                         context: str = None,
                         level: int = 1,
                         active_vkg: dict = HDP_VKG) -> Union[dict, bool]:
    """Recursively translate an item.

    Args:
        hdp_current (dict, list): The hdp internal object/list
        objectivum_linguam (str): ISO 639-3 code
        context (str, optional): Context (key on upper level key).
                                    Defaults to None.
        level (int, optional): How deep we are on this recursion?
        active_vkg (dict, optional): Active vocabulary knowledge graph.
                                  Defaults to vocab_core.yml (Latin)

    Returns:
        Union[dict, bool]: And HDP object already translated to target
                            linguam or bool if no translation is need
    """

    if level > 10:
        raise RecursionError('Level too high. ' +
                             'Programming or HDP file error? ' +
                             '[ ' + str(level) + ' ] ' +
                             '[ ' + str(context) + ' ] ' +
                             '[ ' + str(objectivum_linguam) + ' ] ' +
                             '[ ' + str(fontem_linguam) + ' ] ' +
                             '[ ' + str(hdp_current) + ' ] ')

    if _IS_DEBUG:
        print('_transpose_recursive: start', level, context,
                objectivum_linguam, fontem_linguam)  # noqa

    if context.endswith(VOCAB_RECURSION_LEAF):
        if _IS_DEBUG:
            print('_transpose_recursive: leaf. nop')
        return hdp_current

    if isinstance(hdp_current, list):
        if _IS_DEBUG:
            print('_transpose_recursive: list')  # noqa

        hdp_new = []

        # for idx, item in enumerate(hdp_current):
        for idx, _ in enumerate(hdp_current):
            # print('    pepa', type(idx))
            # print('    pepa', type(item))

            hdp_new.append(
                _transpose_recursive(
                    hdp_current[idx],
                    objectivum_linguam=objectivum_linguam,
                    fontem_linguam=fontem_linguam,
                    context=context,
                    level=(level+1),
                    active_vkg=active_vkg)
            )
        return hdp_new

    if isinstance(hdp_current, dict):
        if _IS_DEBUG:
            print('_transpose_recursive: dict', hdp_current)  # noqa

        hdp_new = {}

        for idx, (k, v) in enumerate(hdp_current.items()):

            # key attribute start with k. Don't translate this or leafs
            if str(k).startswith('_'):
                hdp_new[k] = hdp_current[k]
                continue

            # Let's find if current attribute is translatabe
            # - attr exists?
            # - objectivum_linguam exists for this attr?
            # - id exists for this attr+objectivum_linguam?
            if ((k in active_vkg['attr']) and
                    (active_vkg['attr'][k][objectivum_linguam]['id']) and
                    (active_vkg['attr'][k][objectivum_linguam]['id'])):

                k_new = active_vkg['attr'][k][objectivum_linguam]['id']
            else:
                if _IS_DEBUG:
                    print('_transpose_recursive: nop k', k)

                # Ok. Deeper search

                k_new = k

            if isinstance(hdp_current, (dict, list)):
                context_new = context + '.' + k
                hdp_new[k_new] = _transpose_recursive(
                    hdp_current[k],
                    objectivum_linguam=objectivum_linguam,
                    fontem_linguam=fontem_linguam,
                    context=context_new,
                    level=(level+1),
                    active_vkg=active_vkg
                )
                continue

            if isinstance(v, str):
                # If value already is an string, perfect match
                hdp_new[k_new] = hdp_current[k]
                continue

            # Did exist some conditiono not checked?
            if _IS_DEBUG:
                print('_transpose_recursive: dict (?)', k, v)
            hdp_new[k_new] = hdp_current[k]

        return hdp_new

    if _IS_DEBUG:
        print('_transpose_recursive: not dict/list')  # noqa

    return hdp_current
