"""hxlm.core.model.recipe contains SStorage (...)

- https://unix.stackexchange.com/questions/162900
  /what-is-this-folder-run-user-1000
- https://superuser.com/questions/45342
  /when-should-i-use-dev-shm-and-when-should-i-use-tmp

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


class SStorage:
    """SStorage is an abstraction to both 'permanent' and temporary files.

    NOTE: this may actually be implemented at external libraries
    """

    def __init__(self):
        self.kind: str = 'SStorage'
