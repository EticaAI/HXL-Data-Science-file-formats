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

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from functools import lru_cache
import locale
import os

import yaml

__all__ = ['debug_localization', 'get_language_preferred',
           'get_ISO_369_3_from_string',
           'get_localization_knowledge_graph']


# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))

HXLM_CORE_LOCALIZATION_CORE_LOC = \
    os.path.dirname(os.path.realpath(__file__)) + '/core_loc.yml'
"""localization/core_loc.yml is the default reference of knowledge base
for localization
"""


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
                              hdp_lkg: dict = None) -> str:
    return term


# import hxlm.core.localization as l10n
# os.environ["HDP_DEBUG"] = "1"
# l10n.get_language_preferred()


def get_language_preferred(
        hint_preferred: str = None,
        langs_original: list = None,
        langs_strict: list = None,
        langs_extra: list = None,
        hdp_lkg: dict = None) -> str:
    """[summary]

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
        langs_extra (list, optional): if do exist some way that, while not as
                    perfect as langs_strict, still be able to do automated
                    conversion, use the langs_extra. Defaults to not be used.
        hdp_lkg (dict, optional): HDP localization knowledge graph dictionary.
                    Default to use internal HDP localization knowledge graph.

    Returns:
        str: [description]
    """

    result = {
        'lang': None,
        'type': None
    }

    # if linguam23 is None:

    if hint_preferred is None:
        # We will default to... Latin
        hint_preferred = os.getenv('LANGUAGE', 'la')

    if hdp_lkg is None:
        hdp_lkg = get_localization_knowledge_graph()

    if not isinstance(hint_preferred, list):
        hint_preferred = hint_preferred.split(':')

    if _IS_DEBUG:
        print('get_language_preferred')
        print('  hint_preferred', hint_preferred)
        print('  langs_original', langs_original)
        print('  langs_strict', langs_strict)
        print('  langs_extra', langs_extra)
    for lang_ in hint_preferred:
        lnorm = get_ISO_369_3_from_string(lang_, hdp_lkg=hdp_lkg)
        if langs_original is not None:
            if lnorm in langs_original:
                result['lang'] = lnorm
                result['type'] = 'original'
                return result
        if langs_strict is not None:
            if lnorm in langs_strict:
                result['lang'] = lnorm
                result['type'] = 'strict'
                return result
        if langs_extra is not None:
            if lnorm in langs_extra:
                result['lang'] = lnorm
                result['type'] = 'extra'
                return result
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

    # @see https://code.visualstudio.com/docs/python/jupyter-support
    # @see https://ipython.org/ipython-doc/3/config/extensions/autoreload.html

    # import importlib
    # import hxlm.core.localization as l10n
    # importlib.reload(hxlm.core.localization)

    # import importlib
    # import hxlm.core.localization as l10n
    # l10n.debug_localization()
    # importlib.reload(l10n.util)
