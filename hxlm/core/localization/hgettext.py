"""hxlm.core.localization.hgettext is an draft

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


def _h(key: str, mkg=None):
    """An gettext (...)

    Args:
        key ([str]): Key term. If MKG is none, will return this
        mkg ([dict], optional): An dict to search by falues. Defaults to None.

    Returns:
        [str]: The result
    """
    if mkg:
        if key in mkg:
            return mkg[key]
    return key
