"""hxlm.core.hdp.project


>>> import hxlm.core as HXLm
>>> # Loading single file
>>> hp =HXLm.HDP.project(HXLm.HDATUM_UDHR)

# >>> hp.info()
# >>> hp.info('entry_point')

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

# from dataclasses import asdict

from typing import (
    List
)

from hxlm.core.types import (
    L10NContext
)
from hxlm.core.util import (
    get_value_if_key_exists
)

from hxlm.core.hdp.datamodel import (
    HSiloWrapper,
    HDPRaw
)

from hxlm.core.localization.util import (
    l10n
)

__all__ = ['project']

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


class HDPProject:
    """Abstraction to an HDP Declarative Programming  project

    While is possible to load individual YAML/JSON file to work with single
    resouce, the HDPProject is an way to deal with colletions of HDP files.

    It's an partial refactoring of the hxlm/core/model/hdp.py
    """

    _entry_point: str

    _l10n: L10NContext
    """Current active user context."""

    hdpraw: List[HDPRaw]
    """HDPRaw is, informally speaking it is a crude representation of
    information in a disk file that MAY be an single hsilo or not.
    """

    hsilos: List[HSiloWrapper]
    """List of individual HSilo (one physical file could have multiple)"""

    def __init__(self, entry_point: str, user_l10n: L10NContext):
        self._entry_point = entry_point
        self._l10n = user_l10n

    def _init_project(self, entry_point: str):
        pass

    def info(self, dotted_key: str = None) -> str:
        """Quick sumamary about current HDP project
        """
        info = {
            'entry_point': self._entry_point,
            'l10n': self._l10n
            # 'l10n_user': asdict(self._l10n_user)
        }

        # raise SyntaxError(info)
        if dotted_key is not None:
            return get_value_if_key_exists(info, dotted_key)

        return info


def project(entry_point: str) -> HDPProject:
    user_l10n = l10n()
    # raise SyntaxError(l10n_user.know_languages)
    # raise SyntaxError(l10n_user.about())
    result = HDPProject(entry_point, user_l10n=user_l10n)
    return result
