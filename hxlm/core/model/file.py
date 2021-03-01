"""hxlm.core.model.meta contains HFile (...)


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

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

        return self._file_raw

    def load_schema_file(self, file_raw):
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