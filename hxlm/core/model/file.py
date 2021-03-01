"""hxlm.core.model.meta contains HFile (...)


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os.path

from typing import (
    Type
)

# TODO: this obvously should not be hardcoded. Update (Emerson Rocha, 2021-03-01 10:47 UTC)
HMETA_LOCAL_BASE="/workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/data/baseline"
HMETA_LOCAL_HFILE_BASE=HMETA_LOCAL_BASE+"/hfile"

class HFile:
    """HMeta is the main entry point to glue collections of HConteiner and etc
    In practice, is mostly used to, with help with external utils, abstract
    hmeta.yml from disk
    """

    def __init__(self, file_raw=None):
        self.kind: str = 'HFile'
        self._file_raw = file_raw

    def export_schema(self):
        # TODO: improve this. Still just outputing the input

        # print('HFile export_schema', self._file_raw)

        return self._file_raw

    def is_available_locally(self):
        """Returns file path if available locally, and False if not

        Returns:
            [Union[str, False]]: Path to local file or false
        """

        # TODO: parse to not need use _file_raw
        expected_path = HMETA_LOCAL_HFILE_BASE + '/' + self._file_raw['id']

        #return expected_path

        if os.path.isfile(expected_path):
            return expected_path
        else:
            return False

    def load_schema(self, file_raw):
        """load_schema_file load object and convert to HFile

        How the object is saved on disk (or received from external sources)
        is out of scope of this class.

        Args:
            dataset_raw (Object): Load generic object to HFile
        """

        self._file_raw = file_raw
        return self
        # self._parse_schemas_raw()
        # print(schemas)


def action_cache_hfile(hfile: Type[HFile]):
    print('todo')


# class HFile:
#     """HFile is an reference for an file on an HConteiner

#     Differentes from HFile to HDataset
#         - HFile is more generic than HDataset
#         - HFile does not have attribute sensitive (but can have encryption)

#     TODO: both Excel, CKan and formats like HDF5 work with MULDIPLE datasets.
#           so, which structure use for this? (E.Rocha, 2021-02-26 08:10 UTC)
#     """

#     def __init__(self, encryption: Type[EncryptionHtype] = None,
#                  sensitive: Type[SensitiveHtype] = None):
#         self._encryption = encryption
#         self._sensitive = sensitive

#     def describe(self):
#         mdataset_description = {
#             'kind': "HFile",
#             'encryption': self._encryption
#         }
#         verbose_event()
#         return mdataset_description

#     @property
#     def encryption(self):
#         return self._encryption

#     @encryption.setter
#     def encryption(self, value):
#         if isinstance(value, EncryptionHtype):
#             self._encryption = value
#         else:
#             self._encryption = EncryptionHtype(code=value)