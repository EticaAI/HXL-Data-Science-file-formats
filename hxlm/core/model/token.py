"""hxlm.core.model.token is an internal colletion of helpers to assist
hdpcli command line helper.

NOTE: this class may be moved outsite the core library later.


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""
import os
import configparser


class HSToken:
    """HSToken is (TODO: document)
    """

    raw_ini = None

    file_suffix: str = ".key.ini"

    env_prefix: str = 'HK_'

    env_prefix_active: str = ''

    def __init__(self, workspace: str = None):
        """
        Constructs all the necessary attributes for the HDPCLI object.
        """
        # print('workspace', workspace)

        self._load_from_enviroment()

        if workspace:
            self.raw_ini = self._load_from_path(workspace)

    def _load_from_path(self, workspace: str, strict: bool = False):

        for file in os.listdir(workspace):
            if file.endswith(self.file_suffix):
                config = configparser.ConfigParser()
                config.read(os.path.join(workspace, file))
                config.sections()
                print('config', config)
                print('config type', type(config))
                print('config sections', config.sections())
                # print(os.path.join(workspace, file))
                return config
        if strict:
            raise RuntimeError('HKeystore file detection failed ', workspace)
        return None

    def _load_from_keyring(self, workspace: str):
        print('TODO _load_from_keyring', workspace)

    def _load_from_enviroment(self):
        print('os.environ', os.environ)

        print('TODO _load_from_enviroment')
