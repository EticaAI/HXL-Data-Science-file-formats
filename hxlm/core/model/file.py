"""hxlm.core.model.meta contains HFile (...)


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import sys
import os.path
import requests

# from typing import (
#     Type
# )

# TODO: this obvously should not be hardcoded. Update
#       (Emerson Rocha, 2021-03-01 10:47 UTC)
# HMETA_BASE = HXLM_CORE_BASE + "/data/baseline"
HMETA_BASE = "/workspace/git/EticaAI/HXL-Data-Science-file-formats" + \
"/hxlm/data/baseline"  # noqa
HMETA_HFILE_BASE = HMETA_BASE+"/hfile"
HMETA_HFILE_BASE_ALT = "/tmp"
HMETA_HFILE_BASE_NEW = HMETA_HFILE_BASE  # Base path for new requests


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
        path_default = HMETA_HFILE_BASE + '/' + self._file_raw['id']
        path_alt = HMETA_HFILE_BASE_ALT + '/' + self._file_raw['id']

        # return expected_path

        if os.path.isfile(path_default):
            return path_default
        elif os.path.isfile(path_alt):
            return path_alt
        else:
            return False

    def is_available_sources(self):
        """Get first source URL/Path that seems available and False if none

        Returns:
            [Union[str, False]]: Reference to a resource that have the HFile
        """

        available_urls = []

        if 'source' in self._file_raw:
            if type(self._file_raw['source']) is str:
                available_urls.append(self._file_raw['source'])
            elif 'url' in self._file_raw['source']:
                available_urls.append(self._file_raw['source']['url'])

        if 'sources' in self._file_raw:
            for s in self._file_raw['sources']:
                if type(s) is str:
                    available_urls.append(s)
                elif 'url' in s:
                    available_urls.append(s['url'])

        # At this moment, only URL requests are implemented, but we should
        # implement both copy file from OTHER hfile and also from other
        # hmeta playbooks ;D
        for url in available_urls:
            r = requests.head(url)
            if r.status_code == 200 or r.status_code == 304:
                return url
            else:
                sys.stderr.write(
                    'WARNING: HFile()->is_available_sources HTTP code [' +
                    r.status_code + '] for' + url)

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

    def reload_from_souces(self, reload=False):
        """If HFile is not on local disk, download from first source available

        Args:
            reload (bool, optional): Force reload. Defaults to False.

        Returns:
            bool: Result of operation
        """

        path_new = HMETA_HFILE_BASE_NEW + '/' + self._file_raw['id']

        if os.path.isfile(path_new):
            if reload:
                print('HFile().download_from_sources: TODO, implement rm -f')
        else:
            source = self.is_available_sources()
            if source:
                r = requests.get(source, allow_redirects=True)
                print('yupi')
                return open(path_new, 'wb').write(r.content)

        return True


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
