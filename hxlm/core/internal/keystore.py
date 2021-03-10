"""hxlm.core.internal.keystore is an internal colletion of helpers to assist
hdpcli command line helper.

NOTE: this class may be moved outsite the core library later.


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


class HKeystore:
    """Keystore is (TODO: document)
    """

    def __init__(self, workspace: str = None):
        """
        Constructs all the necessary attributes for the HDPCLI object.
        """

    def _load_from_path(self, workspace: str):
        print('TODO _load_from_path', workspace)

    def _load_from_keyring(self, workspace: str):
        print('TODO _load_from_path', workspace)

    def _load_from_enviroment(self, workspace: str):
        print('TODO _load_from_enviroment', workspace)
