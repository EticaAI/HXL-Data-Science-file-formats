"""hxlm.core.hdp.project

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

__all__ = ['HDPProject']

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


class HDPProject:

    _entry_point: str

    def __init__(self, entry_point: str):
        self._entry_point = entry_point

    def _init_project(self, entry_point: str):
        pass
