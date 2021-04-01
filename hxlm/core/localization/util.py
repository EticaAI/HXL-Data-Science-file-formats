"""hxlm.core.localization.util contain localization (L10N) utilities

See:
- https://www.w3.org/International/questions/qa-i18n


Terms:
> From https://blog.mozilla.org/l10n/2011/12/14/i18n-vs-l10n-whats-the-diff/:

- Internationalization (i18n).
- Localization (l10n).
- Globalization (g11n).
- Localizability (l12y).
  - @see https://docs.microsoft.com/en-us/globalization/localizability
         /localizability
  - @see https://docs.microsoft.com/en-us/globalization/localizability
         /mirroring-awareness

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from functools import lru_cache
import locale
import os

# from typing import (
#     Any
# )

import yaml

from hxlm.ontologia.python.commune import (
    Factum
)

from hxlm.ontologia.python.systema import (
    # Factum,
    L10NContext
)


__all__ = ['debug_localization',
           'get_ISO_369_3_from_string',
           'get_language_preferred',
           'get_language_user_know',
           'get_localization_knowledge_graph',
           'get_localization_lids',
           'l10n'  # This is the user-friendly call
           ]


# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))

# HXLM_CORE_LOCALIZATION_CORE_LOC = \
#     os.path.dirname(os.path.realpath(__file__)) + '/core_loc.yml'
HXLM_CORE_LOCALIZATION_CORE_LOC = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__)))) + '/ontologia/core.lkg.yml'
"""ontologia/core.lkg.yml is the default reference of knowledge base
for localization
"""


@lru_cache(maxsize=1)
def _get_langs_strict_default():
    """List of keys from the 'HDP localization knowledge graph'

    Returns:
        [list]: the default keys with core HDP.
    """
    hdp_lkg = get_localization_knowledge_graph(HXLM_CORE_LOCALIZATION_CORE_LOC)
    if hdp_lkg and 'linguam23' in hdp_lkg:
        return list(hdp_lkg['linguam23'].values())
    return []


def debug_localization() -> dict:
    """Show information about current locale

    See:
        - https://docs.python.org/3/library/locale.html

    Returns:
        dict: Dictionary with general information about current host
    """
    info = {}
    info['locale'] = locale.getlocale()
    info['defaultlocale'] = locale.getdefaultlocale()
    info['preferredencoding'] = locale.getpreferredencoding(),
    info['environment'] = {
        'LANG': os.getenv('LANG'),
        'LANGUAGE': os.getenv('LANGUAGE'),
        'LC_ALL': os.getenv('LC_ALL'),
        'LC_ADDRESS': os.getenv('LC_ADDRESS'),
        'LC_COLLATE': os.getenv('LC_COLLATE'),
        'LC_CTYPE': os.getenv('LC_CTYPE'),
        'LC_IDENTIFICATION': os.getenv('LC_IDENTIFICATION'),
        'LC_MEASUREMENT': os.getenv('LC_MEASUREMENT'),
        'LC_MESSAGES': os.getenv('LC_MESSAGES'),
        'LC_MONETARY': os.getenv('LC_MONETARY'),
        'LC_NAME': os.getenv('LC_NAME'),
        'LC_NUMERIC': os.getenv('LC_NUMERIC'),
        'LC_PAPER': os.getenv('LC_PAPER'),
        'LC_TELEPHONE': os.getenv('LC_TELEPHONE'),
        'LC_TIME': os.getenv('LC_TIME')
    }
    info['pylocale'] = {
        'LC_CTYPE': locale.LC_CTYPE,
        'LC_COLLATE': locale.LC_COLLATE,
        'LC_TIME': locale.LC_TIME,
        'LC_MONETARY': locale.LC_MONETARY,
        'LC_MESSAGES': locale.LC_MESSAGES,
        'LC_NUMERIC': locale.LC_NUMERIC,
        'LC_ALL': locale.LC_ALL,
        'CHAR_MAX': locale.CHAR_MAX
    }

    info['nl_langinfo'] = {
        'CODESET': locale.nl_langinfo(locale.CODESET),
        'D_T_FMT': locale.nl_langinfo(locale.D_T_FMT),
        'D_FMT': locale.nl_langinfo(locale.D_FMT),
        'T_FMT': locale.nl_langinfo(locale.T_FMT),
        'T_FMT_AMPM': locale.nl_langinfo(locale.T_FMT_AMPM),
        'DAY_1': locale.nl_langinfo(locale.DAY_1),
        'DAY_2': locale.nl_langinfo(locale.DAY_2),
        'DAY_3': locale.nl_langinfo(locale.DAY_3),
        'DAY_4': locale.nl_langinfo(locale.DAY_4),
        'DAY_5': locale.nl_langinfo(locale.DAY_5),
        'DAY_6': locale.nl_langinfo(locale.DAY_6),
        'DAY_7': locale.nl_langinfo(locale.DAY_7),
        'ABDAY_1': locale.nl_langinfo(locale.ABDAY_1),
        'ABDAY_2': locale.nl_langinfo(locale.ABDAY_2),
        'ABDAY_3': locale.nl_langinfo(locale.ABDAY_3),
        'ABDAY_4': locale.nl_langinfo(locale.ABDAY_4),
        'ABDAY_5': locale.nl_langinfo(locale.ABDAY_5),
        'ABDAY_6': locale.nl_langinfo(locale.ABDAY_6),
        'ABDAY_7': locale.nl_langinfo(locale.ABDAY_7),
        'MON_1': locale.nl_langinfo(locale.MON_1),
        'MON_2': locale.nl_langinfo(locale.MON_2),
        'MON_3': locale.nl_langinfo(locale.MON_3),
        'MON_4': locale.nl_langinfo(locale.MON_4),
        'MON_5': locale.nl_langinfo(locale.MON_5),
        'MON_6': locale.nl_langinfo(locale.MON_6),
        'MON_7': locale.nl_langinfo(locale.MON_7),
        'ABMON_1': locale.nl_langinfo(locale.ABMON_1),
        'ABMON_2': locale.nl_langinfo(locale.ABMON_2),
        'ABMON_3': locale.nl_langinfo(locale.ABMON_3),
        'ABMON_4': locale.nl_langinfo(locale.ABMON_4),
        'ABMON_5': locale.nl_langinfo(locale.ABMON_5),
        'ABMON_6': locale.nl_langinfo(locale.ABMON_6),
        'ABMON_7': locale.nl_langinfo(locale.ABMON_7),
        'RADIXCHAR': locale.nl_langinfo(locale.RADIXCHAR),
        'THOUSEP': locale.nl_langinfo(locale.THOUSEP),
        'YESEXPR': locale.nl_langinfo(locale.YESEXPR),
        'NOEXPR': locale.nl_langinfo(locale.NOEXPR),
        'CRNCYSTR': locale.nl_langinfo(locale.CRNCYSTR),
        'ERA': locale.nl_langinfo(locale.ERA),
        'ERA_D_T_FMT': locale.nl_langinfo(locale.ERA_D_T_FMT),
        'ERA_D_FMT': locale.nl_langinfo(locale.ERA_D_FMT),
        'ERA_T_FMT': locale.nl_langinfo(locale.ERA_T_FMT),
        'ALT_DIGITS': locale.nl_langinfo(locale.ALT_DIGITS)
    }

    return info


def get_ISO_369_3_from_string(term: str,
                              default: str = None,
                              strict: bool = False,
                              hdp_lkg: dict = None) -> str:
    """Convert an individual item to a ISO 369-3 language code, UPPERCASE

    Args:
        term (str): The input term to search
        default (str, optional): Default no match found. Defaults to None.
        strict (bool, optional): If require exact match on hdp_lkg.
        hdp_lkg (dict, optional): HDP localization knowledge graph dictionary.
                    Default to use internal HDP localization knowledge graph.

    Returns:
        str: An ISO 369-3 language code, UPPERCASE

    Examples:
        >>> import hxlm.core.localization as l10n
        >>> l10n.get_ISO_369_3_from_string(term='pt')
        'POR'
        >>> l10n.get_ISO_369_3_from_string(term='en')
        'ENG'
        >>> l10n.get_ISO_369_3_from_string(term='ZZZ', strict=False)
        'ZZZ'
        >>> l10n.get_ISO_369_3_from_string(term='pt_BR')
        >>> # inputs like 'pt_BR' still not implemented... yet
        >>> # But when using system languages, like 'pt_BR:pt:en',
        >>> # often the next term would be PT anyway
    """

    if _IS_DEBUG:
        print('get_ISO_369_3_from_string')
        print('  term', term)
        print('  term.upper', term.upper())
        print('  default', default)
        print('  strict', strict)
        # print('  hdp_lkg', hdp_lkg)

    result = default
    if hdp_lkg is None:
        hdp_lkg = get_localization_knowledge_graph()

    # Since the HDP localization knowledge may not contain the full ISO 639-3
    # language codes, without strict = True, if the input already is 3 letter
    # uppercase ASCII letters, we will fallback to this
    if not strict and (len(term) == 3 and term.isalpha() and term.isupper()):
        result = term

    if hdp_lkg is None or 'linguam23' not in hdp_lkg:
        return result

    if term.upper() in hdp_lkg['linguam23']:
        return hdp_lkg['linguam23'][term.upper()]

    if len(term) >= 5 and len(term) >= 12:
        if _IS_DEBUG:
            print('  TODO: implement some type of search by language name')

    return result


# import hxlm.core.localization as l10n
# os.environ["HDP_DEBUG"] = "1"
# l10n.get_language_preferred()


def get_language_preferred(
        hint_preferred: str = None,
        langs_original: list = None,
        langs_strict: list = None,
        langs_extra: list = None,
        hdp_lkg: dict = None) -> str:
    """Get user preferred language to see an resource

    - langs_original, if defined, will take priority over langs_strict (the
      ones HDP would be able to convert on the fly)
      - In other words, except if user force traslate, it will always try
        to use at least some language know by the user.
    - hint_preferred, if defined, will be used over try to guess the language
      user wants (read environment variables)

    See https://superuser.com/questions/392439
        /lang-and-language-environment-variable-in-debian-based-systems
    for the syntax of hint_preferred.

    Args:
        hint_preferred (str, optional): An string with language preferences.
                    Defaults to search local user environment variable.
        langs_original (list, optional): If the resource already have one or
                    more languages availible as original (e.g, without any
                    automated strict or extra conversion) we will recommend
                    the original
        langs_strict (list, optional): List of strict, equally valid,
                    conversions that can be done for this resource. Default
                    to use internal HDP localization knowledge graph.
                    PROTIP: set this as false or as empty list to avoid
                    loading the _get_langs_strict_default()
        langs_extra (list, optional): if do exist some way that, while not as
                    perfect as langs_strict, still be able to do automated
                    conversion, use the langs_extra. Defaults to not be used.
        hdp_lkg (dict, optional): HDP localization knowledge graph dictionary.
                    Default to use internal HDP localization knowledge graph.

    Returns:
        dict: an object with one exact language and the type of how it was
              discovered

    Examples:
        >>> import hxlm.core.localization as l10n
        >>> l10n.get_language_preferred('pt_BR:pt:en')
        {'lang': 'POR', 'type': 'strict'}
        >>> l10n.get_language_preferred('pt_BR:pt:en', langs_original=['ARA'])
        {'lang': 'POR', 'type': 'strict'}
        >>> l10n.get_language_preferred('pt_BR:pt:en', langs_original=['ENG'])
        {'lang': 'ENG', 'type': 'original'}
    """

    result = {
        'lang': None,
        'type': None
    }

    # if linguam23 is None:

    if hdp_lkg is None:
        hdp_lkg = get_localization_knowledge_graph()

    user_languages = get_language_user_know(hint_preferred, hdp_lkg=hdp_lkg)

    if _IS_DEBUG:
        print('get_language_preferred')
        print('  hint_preferred', hint_preferred)
        print('  user_languages', user_languages)
        print('  langs_original', langs_original)
        print('  langs_strict', langs_strict)
        print('  langs_extra', langs_extra)

    if langs_strict is None:
        langs_strict = _get_langs_strict_default()

    # print('langs_strict', langs_strict)

    for lang_ in user_languages:
        if langs_original is not None:
            if lang_ in langs_original:
                result['lang'] = lang_
                result['type'] = 'original'
                return result

    for lang_ in user_languages:
        if langs_strict is not None:
            if lang_ in langs_strict:
                result['lang'] = lang_
                result['type'] = 'strict'
                return result

    for lang_ in user_languages:
        if langs_extra is not None:
            if lang_ in langs_extra:
                result['lang'] = lang_
                result['type'] = 'extra'
                return result
    return result


def get_language_user_know(hint_preferred: str = None,
                           hdp_lkg: dict = None) -> list:
    """List of user know languages that we're may able to provide extra help

    Args:
        hint_preferred (str, optional): An string with language preferences.
                    Defaults to search local user environment variable.
        hdp_lkg (dict, optional): HDP localization knowledge graph dictionary.
                    Default to use internal HDP localization knowledge graph.
    Returns:
        list: List of ISO 639-3 language codes. First one is preferred
    """

    if hint_preferred is None:
        # We will default to... Latin! Often system already defaults to en
        hint_preferred = os.getenv('LANGUAGE', 'la')

    system_langs_list = hint_preferred.split(':')
    result = []
    for lang_ in system_langs_list:
        parsed = get_ISO_369_3_from_string(lang_, hdp_lkg=hdp_lkg)
        if parsed:
            result.append(parsed)
    return result


@lru_cache(maxsize=8)
def get_localization_knowledge_graph(
        path: str = HXLM_CORE_LOCALIZATION_CORE_LOC) -> dict:
    """Get an HDP localization knowledge graph

    Args:
        path (str, optional): Path for an file compatible with the
                    'HDP localization knowledge graph.
                    Defaults to HXLM_CORE_LOCALIZATION_CORE_LOC.

    Returns:
        dict: an HDP localization knowledge graph dict
    """

    with open(path, 'r') as openfile:
        data = yaml.safe_load(openfile)
        return data


@lru_cache(maxsize=1)
def get_localization_lids() -> dict:
    """Get ontologia/core.lkg.yml contents

    # TODO: Allow return just LIDs or ISO codes as option

    Returns:
        dict: ontologia/core.lkg.yml contents
    """
    hdp_lkg = get_localization_knowledge_graph()

    if _IS_DEBUG:
        print('get_localization_lids')
        print('  hdp_lkg', hdp_lkg)

    return hdp_lkg['lid']


def i10n_factum(factum: Factum) -> str:
    """Get an translated version of Factum as S-expression string

    Args:
        factum (Factum): an Factum entry

    Returns:
        str: An S-expression string

>>> i10n_factum(Factum("Testing"))
'(vkg.attr.factum (vkg.attr.descriptionem "Testing"))'
>>> i10n_factum(Factum("Testing", linguam="ENG"))
'(vkg.attr.factum (vkg.attr.descriptionem (ENG "Testing")))'
>>> i10n_factum(Factum("Testing", datum=[1, 2]))
'(vkg.attr.factum (vkg.attr.descriptionem "Testing")(vkg.attr.datum "[1, 2]"))'
    """

    # TODO: implement, _de facto_ the localization. This is just a dummy.
    return str(factum)


def l10n() -> L10NContext:
    """Get an summarized localization current context

    Note: This function is the that is recommended for end users

    Returns:
        L10NContext: The user current context
    """

    lids_all = get_localization_lids()
    available = []

    for _, key in enumerate(lids_all):
        available.append(lids_all[key]['lid'])

    result = L10NContext(
        available=available,
        user=get_language_user_know()
    )

    # print('result', result)
    # raise SyntaxError(str(get_language_user_know()))
    # raise SyntaxError(str(result.__dict__))

    return result

# def search_by_value(search: dict, dotted_key: str,
#                     default: Any = None) -> Any:
#     """Get value by dot notation key

#     Examples:
#         >>> from hxlm.core.schema.vocab import HVocabHelper
#         >>> HVocabHelper().get_value('datum.POR.id')
#         >>> HVocabHelper().get_value('attr.datum.POR.id')
#         'dados'

#     Args:
#         search (dict): Dictionary to search
#         dotted_key (str): Dotted key notation
#         default ([Any], optional): Value if not found. Defaults to None.

#     Returns:
#         [Any]: Return the result. Defaults to default
#     """
#     keys = dotted_key.split('.')
#     return reduce(
#         lambda d, key: d.get(
#             key) if d else default, keys, search
#     )

    # print(hdp_lkg)

    # pass

    # @see https://code.visualstudio.com/docs/python/jupyter-support
    # @see https://ipython.org/ipython-doc/3/config/extensions/autoreload.html

    # import importlib
    # import hxlm.core.localization as l10n
    # importlib.reload(hxlm.core.localization)

    # import importlib
    # import hxlm.core.localization as l10n
    # l10n.debug_localization()
    # importlib.reload(l10n.util)
