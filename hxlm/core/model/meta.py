"""hxlm.core.model.meta contans HMeta


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


class HMeta:
    """HMeta is the main entry point to glue collections of HConteiner and etc
    In practice, is mostly used to, with help with external utils, abstract
    hmeta.yml from disk
    """

    def __init__(self, schemas_raw=None):
        self.kind: str = 'HMeta'
        self._schemas_raw = schemas_raw

    def export_schemas(self):
        return self._schemas_raw

    def load_schemas(self, schemas_raw):
        """load_schemas load object and convert to HMeta

        How the object is saved on disk (or received from external sources)
        is out of scope of this class.

        Args:
            schemas (Object): Load generic object to HMeta
        """
        self._schemas_raw = schemas_raw
        # print(schemas)

