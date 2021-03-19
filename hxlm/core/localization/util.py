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


import locale


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
    info['preferredencoding2'] = locale.getpreferredencoding()
    info['LC_CTYPE'] = locale.LC_CTYPE
    info['LC_COLLATE'] = locale.LC_COLLATE
    info['LC_TIME'] = locale.LC_TIME
    info['LC_MONETARY'] = locale.LC_MONETARY
    info['LC_MESSAGES'] = locale.LC_MESSAGES
    info['LC_NUMERIC'] = locale.LC_NUMERIC
    info['LC_ALL'] = locale.LC_ALL
    info['CHAR_MAX'] = locale.CHAR_MAX
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

# @see https://code.visualstudio.com/docs/python/jupyter-support
# @see https://ipython.org/ipython-doc/3/config/extensions/autoreload.html

# import importlib
# import hxlm.core.localization as l10n
# importlib.reload(hxlm.core.localization)

# import importlib
# import hxlm.core.localization as l10n
# l10n.debug_localization()
# importlib.reload(l10n.util)
