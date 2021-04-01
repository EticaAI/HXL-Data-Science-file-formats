"""hxlm.core.hdp.util.common

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os
from copy import deepcopy
from typing import Union
from pathlib import Path

# from binascii import crc32

import hxlm.core.constant as C
import hxlm.core.util as Cutil
from hxlm.core.localization.util import (
    get_language_user_know,
    get_localization_lids
)

from hxlm.core.internal.integrity import (
    get_checksum_crc32,
    get_hashable
)

from hxlm.core.io.util import (
    strip_file_protocol
)

from hxlm.core.util import load_file as generic_load_file

# TODO: move vocabulary conversions from hxlm.core.schema.vocab to here
#       (Emerson Rocha, 2021-03-20 03:01 UTC)

__all__ = [
    'build_new_vocabulary_knowledge_graph',  # Maybe make it short?
    'checksum',
    'get_hdp_term_cleaned',  # Maybe this could be _private?
    'get_metadata',
    'get_language_identifiers',
    'get_language_from_hdp_raw',  # Deprecated
    'hashable',
    'transpose',
    'transpose_hsilo'
]

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

# HDP_VKG = Cutil.load_file(C.HXLM_ROOT + '/core/schema/core_vocab.yml')
# HDP_VKG = Cutil.load_file(C.HXLM_ROOT + '/ontology/core.vkg.yml')
HDP_VKG = Cutil.load_file(C.HXLM_ROOT + '/ontologia/core.vkg.yml')
"""Vocabulary knowledge graph, aka ontologia/core.vkg.yml"""

HDP_VKG_FULL: dict = {}
"""Dictionary with transposition from other languages back to Latin"""


CORE_LKG = Cutil.load_file(C.HXLM_ROOT + '/ontologia/core.lkg.yml')
"""Localization knowledge graph, aka ontologia/core.lkg.yml"""


def _clean_metakeys(thing: Union[dict, list],
                    level: int = 0,
                    prefix: str = None,
                    suffix: str = None) -> Union[dict, list]:
    """Remove internal meta keys like (<<! preffix & !>> suffix) from an thing

    Args:
        thing (Union[dict, list]): An list/dict HDP like object
        level (int, optional): Level of nesting, used to mitigate infinite
                    loops. Defaults to 0.
        prefix (str, optional): Prefix. Defaults to
                    ontologia/core.lkg.yml -> itkn.internal_l1.start
        suffix (str, optional): Prefix. Defaults to
                    ontologia/core.lkg.yml -> itkn.internal_l1.end

    Returns:
        Union[dict, list]: Same thing, but without metakeys (if any)
    """

    level += 1

    if prefix is None:
        prefix = CORE_LKG['itkn']['internal_l1']['start']
    if suffix is None:
        suffix = CORE_LKG['itkn']['internal_l1']['end']

    if level >= 10:
        # Likely to be some error.
        return thing

    if isinstance(thing, dict):

        # We do a deep copy to not change in place (raise would raise errors)
        thing_new = deepcopy(thing)
        for key, _ in thing.items():
            if key.startswith(prefix) and key.endswith(suffix):
                if _IS_DEBUG:
                    print('_clean_comments cleared', key)
                # print('_clean_comments cleared', key)
                del thing_new[key]
            else:
                thing_new[key] = _clean_metakeys(thing[key], level)

        return thing_new
    if isinstance(thing, list):
        # Lists do not have named keys, so we just iterate over
        for key, _ in enumerate(thing):
            thing[key] = _clean_metakeys(thing[key], level)

    # Neiter list or dict; Likely to be an end value (or set/tuple). Return it
    return thing


def _get_hsilo_body(hsilo_item: dict) -> dict:
    """Get an individual HSilo body

    Args:
        hsilo_item (dict): An individual HSilo item

    Returns:
        hsilo_item (dict): The same HSilo item without meta header field
    """

    hsilo_item_new = {}

    for key in hsilo_item.keys():
        lang_ = get_lid_from_keyterm(key)
        if lang_ is None:
            hsilo_item_new[key] = hsilo_item[key]

    return hsilo_item_new


def _get_hsilo_body_language_identifier(hsilo_item: dict) -> dict:
    """Generic test to try all possibilities to detect lid of only hsilo body

    Args:
        hsilo_item (dict): An individual HSilo item

    Returns:
        hsilo_item (dict): The same HSilo item without meta header field
    """

    # TODO do _get_hsilo_body_language_identifier or remove

    lid = {
        'TODO': hsilo_item
    }

    # hsilo_item_new = {}

    # for key in hsilo_item.keys():
    #     lang_ = get_lid_from_keyterm(key)
    #     if lang_ is None:
    #         hsilo_item_new[key] = hsilo_item[key]

    return lid


def _get_checksum(hashable_str: str, chktag: str = 'α') -> list:
    """Generic CRC32 checksum for strings

    Args:
        hashable_str (str): an alterady ready to hash (like Latin) input

    Returns:
        list: List of S-expression checksum values
    """

    # TODO: maybe move this entire function out of here? it's somewhat
    #       redundant with checksum()
    #       (Emerson Rocha, 2021-03-26 08:37 UTC)

    return '(CRC32 \'' + chktag + ' "' + \
        str(get_checksum_crc32(hashable_str)) + '")'


def _get_checksum_keyterm(keyterm: str) -> dict:
    """Both check an keyterm seems to be an checksum, and, if is, explain it

    Args:
        keyterm (keyterm): keyterm to search

    Returns:
        dict: an dict with: 'algorithm', 'chktag', 'value' & (if any) 'salt'

    Examples:
    >>> _get_checksum_keyterm('invalid')
    >>> _get_checksum_keyterm('(invalid invalid invalid invalid)')
    >>> _get_checksum_keyterm('CRC32 \\'α "invalid"')
    >>> _get_checksum_keyterm('(CRC32 \\'α "3839021470")')
    {'algorithm': 'CRC32', 'chktag': "'α", 'value': '3839021470'}
    >>> _get_checksum_keyterm("(CRC32 'α '3839021470')")
    {'algorithm': 'CRC32', 'chktag': "'α", 'value': '3839021470'}
    >>> _get_checksum_keyterm("(CRC32 'α 3839021470)")
    {'algorithm': 'CRC32', 'chktag': "'α", 'value': '3839021470'}
    """

    # print('_get_checksum_keyterm', keyterm)
    # We do some very quick checks. An CRC checkcksum is similar to
    #    (CRC32 'α "3839021470")
    if len(keyterm) < 20 or \
            not keyterm.startswith('(') or not keyterm.endswith(')'):
        return None

    # Even if someone implement an SHA-3 512, the hash would have
    # like 128 characters.
    #    (SHA3-512 'term123 "looooooooooooooooooooooooooooooooooooooooo.....")
    # We will just add 128 + 64 to limit at something, but this could would
    # need to be updated to support other hashes
    if len(keyterm) > 192:
        return None

    # At this moment, only CRC32 is supported. And we do not internationalized
    # another terms
    if not keyterm.startswith('(CRC32 '):
        return None

    result = {
        'algorithm': None,
        'chktag': None,  # TODO: I18N this thing if is know, see VKG.numerum
        'value': None
        # 'salt': None  # Not implemented, but maybe will be
    }

    t_1 = keyterm.replace('(', '', 1)
    t_2 = t_1.replace(')', '', len(t_1))

    # Know issue: at the moment, we still not support Lisp/Racket like
    # symbols with spaces in it. like (CRC32 '|my custom tag| "3839021470")
    t_parts = t_2.split(' ')

    if len(t_parts) < 3:
        raise ValueError('Checksum parts too small, [' + keyterm + ']')

    if len(t_parts) > 4:
        raise ValueError('Checksum parts too big, [' + keyterm + ']')

    result['algorithm'] = t_parts[0]
    result['chktag'] = t_parts[1]
    v_1 = t_parts[2]
    v_2 = v_1.replace('"', '', 1)
    # result['value'] = v_2.replace('"', '', len(v_2))
    v_3 = v_2.replace('"', '', len(v_2))
    v_4 = v_3.replace('\'', '', 1)
    result['value'] = v_4.replace('\'', '', len(v_4))
    # result['value'] = v_3
    # if result['value'][0] == "'" and \
    #     result['value'][len(result['value'])] == "'":

    if len(t_parts) >= 4:
        result['salt'] = t_parts[3]

    return result


def _get_file_preferred_suffix() -> tuple:
    """Based on ontologia/core.lkg.yml + env variable LANGUAGE, build preferred
    user language

    Returns:
        tuple: the result of file sufisex
    """
    userpref_suffix = []

    core_suffix = CORE_LKG['fs']['hdp']['base']

    userlangs_upper = get_language_user_know()
    if len(userlangs_upper) > 0:
        userlangs = map(lambda x: x.lower(), userlangs_upper)
        for lang_ in userlangs:
            userpref_suffix.append(lang_ + '.hdp.json')
            userpref_suffix.append(lang_ + '.hdp.yml')

    combined_suffixes = userpref_suffix + core_suffix

    return tuple(combined_suffixes)


def _get_ideal_header_key(generic_lang_term: str) -> str:
    """Return the most ideal header key for an input term

    This method is mostly used when transposing

    >>> _get_ideal_header_key('POR')
    '([Língua portuguesa])'
    >>> _get_ideal_header_key('ENG-Latn')
    '([English language])'
    >>> _get_ideal_header_key('Idioma español')
    '([Idioma español])'

    Args:
        generic_lang_term (str): The generic term (language code, text, etc)

    Returns:
        str: [description]
    """
    check1_lid = get_lid_from_keyterm(generic_lang_term)
    if check1_lid is not None:
        return '([' + check1_lid['klid'] + '])'

    # It's somewhat lazy to reuse the get_lid_from_keyterm when often this
    # function would already know the language input. But this could
    # be more restricted later
    check2_lid = get_lid_from_keyterm('([' + generic_lang_term + '])')
    if check2_lid is not None:
        return '([' + check2_lid['klid'] + '])'

    return None


def _get_hsilo_meta_header(hsilo_item: dict) -> dict:
    """Get an individual HSilo meta header

    Args:
        hsilo (list): An HSilo (list of individual HSilo items)

    Returns:
        dict: Only each HSilo header field
    """
    hsilo_item_new = {}

    for key in hsilo_item.keys():
        lang_ = get_lid_from_keyterm(key)
        if lang_ is not None:
            hsilo_item_new[key] = hsilo_item[key]
            return hsilo_item_new

    # return hsilo_item_new


def _get_language_hsilo_header(hdp_robj: dict) -> dict:
    """For an RAW HDP object, return the natural language

    This will search for tokens like '([Lingua Latina])', ([Русский язык]),
    '(['اللغة العربية الفصحى الحديثة'])', etc and return the language.

    Args:
        hdp_robj (dict): An raw HDP file (as if loaded direct from disk)

    Returns:
        dict: An HDP LKG dict

    """

    raise DeprecationWarning('Use _get_language_hsilo_header')
    # for key in hdp_robj.keys():
    #     lang_ = get_lid_from_keyterm(key)
    #     if lang_ is not None:
    #         return lang_
    # return None


# def _is_hsilo_lid(hsilo_item: dict, lid: str = 'LAT'):
#     print('TODO:')


def load(path: str) -> Union[dict, list]:
    """Syntatic sugar to load file from local disk (YAML, JSON, CSV)

    Note that this method does not do advanced processing. As long as the
    file have some valid syntax, it will work.

    Args:
        path (str): Directory path or exact file

    Returns:
        Union[dict, list]: An list or dict from the loaded file (or, if
                directory, try some default filenames)
    """

    path = strip_file_protocol(path)

    file_prefered_suffix = _get_file_preferred_suffix()

    if os.path.isfile(path):
        return generic_load_file(path)
    if os.path.isdir(path):
        pitr = Path(path).glob('*')
        for file_ in pitr:
            if str(file_.name).startswith('~'):
                continue
            if str(file_.name).endswith(file_prefered_suffix):
                return generic_load_file(path + '/' + file_.name)
        raise SyntaxError('Path is used, but no default file found')

    raise SyntaxError('Cannot load this path [' + str(path) + ']')


def build_new_vocabulary_knowledge_graph(
    key_vid: str = 'LAT',
    vkg_name: str = None,
    source_vkg: dict = None,
    keep_source_vkg: bool = True,
    full_vkgs: dict = None,
) -> dict:
    """Transpose core.vkg.yml to point from LAT-Latn from a new language

    Args:
        key_vid (str): The Vocabulary id on the HDP_VKG on the source_vkg to
                        point from new references
        vkg_name (str, optional): The name of the new VID. Defaults to use
                        key_vid
        source_vkg (str, optional): The source of the source_vkg to transpose.
                        Defaults to use core_vocab (LAT-Latn), HDP_VKG
        keep_source_vkg (dict, optional): If you want to, instead of create an
                        strict new vocab, still allow old keys on the new
                        VKG. In practice, this means that implicitly, if your
                        new vocabulay already does not define terms a new
                        meaning from the source vocabulary had (like att
                        LAT exemplum), even if define the same term (like
                        attr POR exemplo), when transposing both 'examplum'
                        and 'exemplo' would be undestood. Defaults to True
        full_vkgs (dict, optional): The source full_vkgs. Defaults to
                        HDP_VKG_FULL.

    Returns:
        dict: Return the result. Use as reference input of full_vkgs

    Examples:
        >>> vkg_1 = build_new_vocabulary_knowledge_graph()
        >>> vkg_1['LAT']['root']['hfilum']['SPA']['id']
        'archivo'
    """
    # TODO: maybe we should review this need here
    global HDP_VKG_FULL  # pylint: disable=W0603

    if vkg_name is None:
        vkg_name = key_vid

    if source_vkg is None:
        source_vkg = HDP_VKG

    if full_vkgs is None:
        full_vkgs = HDP_VKG_FULL

    # This already is a know vocabulary. We don't need to re-create it.
    if vkg_name in full_vkgs:
        if _IS_DEBUG:
            print('build_new_vocabulary_knowledge_graph was cached', vkg_name)
        return full_vkgs

    vkg_new = {
        'root': {},
        'attr': {}
    }

    # if keep_source_vkg, we copy them first; they can be replaced later
    if keep_source_vkg:
        for r_key in source_vkg['root']:
            vkg_new['root'][r_key] = source_vkg['root'][r_key]
        for a_key in source_vkg['attr']:
            vkg_new['attr'][a_key] = source_vkg['attr'][a_key]

    # First the id_alts
    # TODO: implement id_alts

    # Then the IDs
    for r_key in source_vkg['root']:
        r_key_new = source_vkg['root'][r_key][key_vid]['id']
        vkg_new['root'][r_key_new] = source_vkg['root'][r_key]

    for a_key in source_vkg['attr']:
        a_key_new = source_vkg['attr'][a_key][key_vid]['id']
        vkg_new['attr'][a_key_new] = source_vkg['attr'][a_key]

    # for r_key in source_vkg['root']:
    #     source_vkg['root'][r_key] =

    full_vkgs[vkg_name] = vkg_new
    return full_vkgs


def check_authenticity():
    """Check authenticity of the resource

    Raises:
        NotImplementedError: HDP, without external help, can not grant
                             authenticity. check_integrity can be used for
                             non-intentional data corruption.
    """
    raise NotImplementedError(
        "HDP, without external help, can not grant authenticity. " +
        "check_integrity can be used for non-intentional data corruption."
    )


def check_integrity(hdpgroup: list,
                    verbose: bool = False,
                    enforce: bool = False) -> Union[list, bool]:
    """Check integrity (comprare checksums) non-proposital data corruption

    Args:
        hdpgroup (list): [description]
        verbose (bool, optional): [description]. Defaults to False.
        enforce (bool, optional): [description]. Defaults to False.

    Raises:
        SyntaxError: [description]

    Returns:
        Union[list, bool]: [description]

    >>> import hxlm.core as HXLm
    >>> UDUR_LAT = HXLm.util.load_file(HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml')
    >>> check_integrity(UDUR_LAT)
    True
    >>> check_integrity(UDUR_LAT, verbose=True)
    [True, []]
    >>> HXL_ENG = HXLm.util.load_file(HXLm.HDATUM_HXL + '/hxl.eng.hdp.yml')
    >>> check_integrity(HXL_ENG)
    True
    """
    any_invalid = False
    result = []
    verbose_msgs = []

    for hsilo in hdpgroup:

        mheader = _get_hsilo_meta_header(hsilo)

        if mheader is None:
            # This item does not even have mheader. It's beyond invalid
            any_invalid = True
            verbose_msgs.append('check_integrity not even mheader')
            continue

        crcs_list = []
        # loop = 0

        hheadervals = mheader.values()
        # print('hheadervals', hheadervals)

        # has_any_crc = False

        # for hitem in hheadervals:
        for _, hitem0 in enumerate(hheadervals):
            for hitem1 in hitem0:
                # print('loop', hitem1, _)
                # continue
                crc_resp = _get_checksum_keyterm(hitem1)

                if crc_resp is not None:
                    # has_any_crc = True
                    crcs_list.append(crc_resp)

        # print('oooi', crcs_list)
        if len(crcs_list) == 0:
            # Enforce enabled; We will require an CRC
            if enforce:
                any_invalid = True

            verbose_msgs.append('check_integrity no CRCs for ' + str(mheader))
            result.append(None)
            continue

        # print('crcs_list now', crcs_list)

        for crc_now in crcs_list:

            hsilo_hash_string = checksum([hsilo],
                                         algorithm=crc_now['algorithm'],
                                         chktag=crc_now['chktag'])[0]

            # hsilo_hash_string2 = hsilo_hash_string.replace("\'\'", "'")
            hsilo_hash = _get_checksum_keyterm(hsilo_hash_string)

            if crc_now['value'] != hsilo_hash['value']:

                # TODO: deal with more than one CRC on some files; it should
                #       tolerate by default such cases, but now we're
                #       considering total from multiple hsilos
                result.append(False)
                any_invalid = True
                verbose_msgs.append('check_integrity FAILED ' +
                                    '[' + str(crc_now) + '][' +
                                    str(hsilo_hash))
            else:
                result.append(True)

    if any_invalid and enforce:
        raise SyntaxError('check_integrity failed')

    if verbose:
        return [not any_invalid, verbose_msgs]

    return not any_invalid


def checksum(hdpgroup: list,
             algorithm: str = 'CRC32',
             chktag: str = '\'α') -> list:
    """List of checksums-like for detection of Non-intentional data corruption

    See https://en.wikipedia.org/wiki/Cksum
    See https://en.wikipedia.org/wiki/Checksum

    Args:
        hdpgroup (list): list of HDP-like objects
        type (str): The type of checker
        htag (str): select only by special tags (for complex documents) mixing
                several hashings. See hashable()

    Returns:
        list: List of strings optimized to be used as input for hashing

    >>> import hxlm.core as HXLm
    >>> UDUR_LAT = HXLm.util.load_file(HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml')
    >>> checksum(UDUR_LAT)
    ['(CRC32 \\'\\'α "3839021470")']
    >>> UDUR_RUS = HXLm.util.load_file(HXLm.HDATUM_UDHR + '/udhr.rus.hdp.yml')
    >>> checksum(UDUR_RUS)
    ['(CRC32 \\'\\'α "3839021470")']
    """

    if algorithm != 'CRC32':
        raise NotImplementedError('algorithm [' +
                                  str(algorithm) + '] not implemented')

    # Escape ' is not an walk in the park. Just to simplify, we will replace
    # double '' with '
    if chktag.find("''") > -1:
        chktag = chktag.replace("''", "'")

    result = []
    for hsilo in hdpgroup:

        hashable_str = hashable([hsilo])[0]
        hashable_code = _get_checksum(hashable_str, chktag=chktag)
        result.append(hashable_code)

    return result


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
        >>> get_lid_from_keyterm('([LAT])')['lid']
        'LAT-Latn'
        >>> get_lid_from_keyterm('([RUS-Cyrl])')['q']
        'Q7737'
        >>> get_lid_from_keyterm('[LAT]')
        >>> # This should return None
        >>> get_lid_from_keyterm('(LAT)')
        >>> # This should return None
        >>> get_lid_from_keyterm('([Língua portuguesa])')['iso3693']
        'POR'
        >>> get_lid_from_keyterm('([Português])')['iso3693']
        'POR'
        >>> get_lid_from_keyterm('([Língua tupi]POR)')
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


def get_language_identifiers(hdp_item: dict) -> dict:
    """For an RAW HDP object, return the natural language

    This will search for tokens like '([Lingua Latina])', ([Русский язык]),
    '(['اللغة العربية الفصحى الحديثة'])', etc and return the language.

    Args:
        hdp_robj (dict): An raw HDP file (as if loaded direct from disk)

    Returns:
        dict: An HDP LKG dict

    Examples
    >>> import hxlm.core as HXLm
    >>> urhd_lat = HXLm.util.load_file(HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml')
    >>> result1 = get_language_identifiers(urhd_lat[0])
    >>> result1['header']['lid']
    'LAT-Latn'
    """

    result = {
        'header': None,
        'header_key': None,
        'body': None
    }

    for key in hdp_item.keys():
        lid_header = get_lid_from_keyterm(key)
        if lid_header is not None:
            result['header'] = lid_header
            result['header_key'] = key
            break

    # TODO: implement result['header'] body
    return result


def get_language_from_hdp_raw(hdp_robj: dict) -> dict:
    """Deprecated. Use get_language_identifiers"""
    # raise DeprecationWarning('Use _get_language_hsilo_header')
    return get_language_identifiers(hdp_robj)['header']  # noqa


def get_metadata(hdpgroup: list) -> list:
    """Get Metadata from an HDP group (e.g. an 'HDP file with 1+ hsilos)

    Args:
        hdpgroup (list): an HDP Grouping (a list with one or more hsilo)

    Returns:
        list: list of dicts with metadata information
    """

    result = []

    for hsilo in hdpgroup:
        meta = {
            # Checksum consider only the body
            'checksum': None,
            'header_lid': None,
            'body_lid': None,
            'header': _get_hsilo_meta_header(hsilo),
            'body': None,
            'body_canonical': None,
            'checksum_source': hashable([hsilo])[0]
        }

        lids = get_language_identifiers(hsilo)

        # print('lids', lids)

        if lids['header'] is not None and 'lid' in lids['header']:  # noqa pylint: disable=E1135
            meta['header_lid'] = lids['header']['lid']  # pylint: disable=E1136

        if lids['body'] is not None and 'lid' in lids['body']:  # noqa pylint: disable=E1135
            meta['body_lid'] = lids['body']['lid']  # pylint: disable=E1136

        meta['body'] = _get_hsilo_body(hsilo)
        # meta['body_lat'] = 'TODO'

        # TODO: this should only be used when already is Latin
        meta['body_canonical'] = _get_hsilo_body(hsilo)
        meta['checksum_source'] = get_hashable(meta['body_canonical'])
        meta['checksum'] = _get_checksum(meta['checksum_source'])

        result.append(meta)

    return result


def hashable(hdpgroup: list, chktag: str = 'α') -> list:
    """Get list of hashable strings from hdpgroups

    Args:
        hdpgroup (list): list of HDP-like objects
        chktag (str): select only by special tags (for complex documents)
                mixing several hashings

    Returns:
        list: List of strings optimized to be used as input for hashing

    >>> import hxlm.core as HXLm
    >>> UDUR_LAT = HXLm.util.load_file(HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml')
    >>> hashable(UDUR_LAT)[0].startswith('{"hdatum": [{"descriptionem": {')
    True
    >>> hashable(UDUR_LAT)[0].endswith('["UN"], "tag": ["udhr"]}}')
    True
    """
    result = []

    if chktag != 'α':
        raise NotImplementedError('chktag still work in progress')

    for hsilo in hdpgroup:

        # transpose requires array, but we're calling directly
        hsilo_lat = transpose([hsilo], 'LAT')[0]
        hsilo_lat_body = _get_hsilo_body(hsilo_lat)
        hsilo_lat_body_clean = _clean_metakeys(
            hsilo_lat_body, prefix='<<', suffix='>>')

        hsilo_lat_body_clean_str = get_hashable(
            hsilo_lat_body_clean)
        result.append(hsilo_lat_body_clean_str)

    return result


def transpose(hsilo: list,
              target_lid: str,
              verbose: bool = False) -> list:
    """Transpose ('translate') and HSilo betwen languages

    Args:
        hsilo (list): [description]
        target_lid (str): An Localization ID, like RUS-Cyrl
        verbose (bool, optional): If output metakeys. Defaults to False.

    Returns:
        list: An transposed hdggroup
    """

    transposed = transpose_hsilo(hsilo, target_lid=target_lid)
    if not verbose:
        transposed = _clean_metakeys(transposed)
        # print('oioioi', verbose, transposed)

    return transposed


def transpose_hsilo(hsilo: Union[list, dict],
                    target_lid: str,
                    source_lid: str = None) -> Union[list, dict]:
    """Transpose ('translate') and HSilo from Latin to another language

    If the object already is not in Latin, you should first prepare in Latin
    before use this function

    Args:
        hsilo (dict): An HSilo object
        target_lid (str): An Localization ID, like RUS-Cyrl
        source_lid (str): An Localization ID, like RUS-Cyrl. If not given, will
                be implicitly detected

    Returns:
        dict: An transposed HSilo

    Examples:

    >>> import hxlm.core as HXLm
    >>> urhd_lat = HXLm.util.load_file(HXLm.HDATUM_UDHR + 'udhr.lat.hdp.yml')
    >>> result1 = get_language_from_hdp_raw(urhd_lat[0])
    >>> result1['lid']
    'LAT-Latn'
    >>> urhd_rus = HXLm.util.load_file(HXLm.HDATUM_UDHR + 'udhr.rus.hdp.yml')
    >>> result1 = get_language_from_hdp_raw(urhd_rus[0])
    >>> result1['lid']
    'RUS-Cyrl'
    """

    # TODO: maybe we should review this need here
    global HDP_VKG_FULL  # pylint: disable=W0603

    # print('target_lid', target_lid)

    result = []

    for idx, _ in enumerate(hsilo):
        if source_lid is None:
            # print('hsilo', hsilo)
            # raise Exception('hsilo' + str(hsilo))
            # result1 = _get_language_hsilo_header(hsilo[idx])
            result1 = get_language_identifiers(hsilo[idx])
            source_lid_ = result1['header']['lid']   # pylint: disable=E1136
        else:
            source_lid_ = source_lid

        if len(target_lid) == 8:
            # We still using 3 letter (like RUS) instead of 8 (like RUS-Cyrl)
            target_lid = target_lid[0:3]

        if len(source_lid_) == 8:
            # We still using 3 letter (like RUS) instead of 8 (like RUS-Cyrl)
            source_lid_ = source_lid_[0:3]

        # HDP_VKG_FULL = build_new_vocabulary_knowledge_graph(
        #     key_vid=target_lid)
        HDP_VKG_FULL = build_new_vocabulary_knowledge_graph(
            key_vid=source_lid_)

        # active_vkg = HDP_VKG
        active_vkg = HDP_VKG_FULL[source_lid_]

        # print('active_vkg', source_lid_, hsilo[idx])
        # print('active_vkg', source_lid_, target_lid, active_vkg)
        # if HPD_VKG is None:
        #     HPD_VKG = Cutil.load_file(C.HXLM_ROOT + '/schema/core_vocab.yml')

        hsilo_ = _transpose_root(hsilo,
                                 objectivum_linguam=target_lid,
                                 fontem_linguam=source_lid_,
                                 active_vkg=active_vkg
                                 )
        # TODO: this selection of first item of list should be changed when
        #       _transpose_root receive an refactoring. See notes there.
        #       (Emerson Rocha, 2021-03-26 06:39)

        # print('aaa', type(hsilo_[0]), hsilo_[0])
        # print('aaa', type(hsilo_[0]), hsilo_[0]['<<!transpose!>>'])

        # if hsilo_[0]['<<!transpose!>>']:
        #     print ('oi', hsilo_[0]['<<!transpose!>>'])

        if hsilo_[0]['<<!transpose!>>']['needs_header_change']:

            tmeta = hsilo_[0]['<<!transpose!>>']

            h_new = tmeta['header_key_target']
            h_old = tmeta['header_key_now']

            hsilo_[0][h_new] = [
                tmeta['checksum'],
                {
                    h_old: hsilo_[0][h_old]
                }
            ]

            # hsilo_[0][h_new] = []
            # hsilo_[0][h_new].append(tmeta['checksum'])
            # hsilo_[h_new].append(
            #     {
            #         h_old: hsilo_[0][h_old]
            #     }
            # )
            # Delete old header
            # print('oi2', hsilo_[0].keys())
            # print('oooi', hsilo_[0][h_old])
            hsilo_[0].pop(h_old)
            # delattr(hsilo_[0], h_old)
            # delattr(hsilo_[0], h_old)
            # del hsilo_[0][h_old]
        result.extend(hsilo_)

    # print('result >>>>', result)
    return result

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

    # TODO: maybe this should be converted to change only one dict while
    #       transpose_hsilo keep track of the lists. For now lists will
    #       stay as it is, but this is something to do on potential refactoring
    #       (Emerson Rocha, 2021-03-26 06:39)

    # print('oi1', hdp_current)

    if _IS_DEBUG:
        print('HDP._transpose_root', fontem_linguam,
        objectivum_linguam, hdp_current)  # noqa
        # print('HDP._transpose_root', HDP_VKG)

    if len(hdp_current) == 0:
        return hdp_current

    hdp_result = deepcopy(hdp_current)

    # if len(objectivum_linguam) != 3 or not objectivum_linguam.isalpha():
    #     raise SyntaxError('No 3 letter or 3 ASCII letter? ' +
    #                       'linguam must be an ISO 639-3 (3 letter) ' +
    #                       'code, like "ARA" or "RUS" ' +
    #                       '[' + objectivum_linguam + ']')
    # if not objectivum_linguam.isupper():
    #     raise SyntaxError('No UPPERCASE? ' +
    #                       'linguam must be an ISO 639-3 (3 letter) ' +
    #                       'code, like "ARA" or "ARA" ' +
    #                       '[' + objectivum_linguam + ']')

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
                hdp_result[hdpns][newterm] = _transpose_recursive(
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
                    hdp_result[hdpns][key_l1] = _transpose_recursive(
                        hdp_current[hdpns][key_l1],
                        objectivum_linguam=objectivum_linguam,
                        fontem_linguam=fontem_linguam,
                        context=key_l1,
                        active_vkg=active_vkg)

        # print(type(hdp_current[hdpns]))

        lidsnow_ = get_language_identifiers(hdp_result[hdpns])
        hdp_result[hdpns]['<<!transpose!>>'] = {
            'checksum': '(CRC (TODO))',
            'checksum_changed': False,  # TODO: this need to be tested later
            'source_lid': fontem_linguam,
            'target_lid': objectivum_linguam,
            'header_key_now': lidsnow_['header_key'],
            'header_key_target': _get_ideal_header_key(objectivum_linguam),
            'needs_header_change': True
        }

        # meta['body_canonical'] = _get_hsilo_body(hsilo)
        # meta['checksum_source'] = get_hashable(meta['body_canonical'])
        # meta['checksum'] = _get_checksum(meta['checksum_source'])

        if _IS_DEBUG:
            hdp_result[hdpns]['<<!!transpose!!>>'] = {
                'body_canonical': None,
                'checksum_source': None
            }

        # print('lidsnow_', lidsnow_)

        # if fontem_linguam != objectivum_linguam:

        #     hheader = _get_hsilo_meta_header(hdp_current[hdpns])
        #     mheaderkey = list(hheader.keys())[0]
        #     hheaderkey_new = '([' + objectivum_linguam + '])'

        #     print(hdp_current[hdpns])
        #     hdp_current[hdpns][mheaderkey] = 'old'
        #     # delattr(hdp_current[hdpns], mheaderkey)

        #     hdp_current[hdpns][hheaderkey_new] = hheader

        #     print('TODO: add header', hheader, mheaderkey)

    # TODO: the transpose root should create a new header with the new
    #       language. At the moment it's not doing this, so the language
    #       detection may vail

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
