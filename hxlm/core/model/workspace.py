"""hxlm.core.model.workspace abstraction to workspace.yml (...)


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


class HWorkspace:
    """HWorkspace is an abstraction to workspace.yml (...)
    """

    def __init__(self):
        self.kind: str = 'HWorkspace'
