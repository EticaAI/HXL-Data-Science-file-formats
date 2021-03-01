"""hxlm.core.model.meta contans HMeta


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hxlm.core.exception import (
    HXLmException
)
from hxlm.core.model import (
    HDataset
)


class HMeta:
    """HMeta is the main entry point to glue collections of HConteiner and etc
    In practice, is mostly used to, with help with external utils, abstract
    hmeta.yml from disk
    """

    def __init__(self, schemas_raw=None):
        self.kind: str = 'HMeta'
        self._schemas_raw = schemas_raw
        self._schemas = []
        self._hdatasets = []
        if self._schemas_raw:
            self._parse_schemas_raw()

    def _parse_schemas_raw(self):
        # print('self._schemas_raw', self._schemas_raw)
        # print('self._schemas', self._schemas)
        for item in self._schemas_raw:
            # print('_parse_schemas_raw item', item)
            # print('_parse_schemas_raw item type', type(item))
            # print('_parse_schemas_raw item type hmeta', type(item['hmeta']))
            if 'hmeta' in item:
                # print('_parse_schemas_raw item item.hmeta yes')
                if 'hdatasets' in item:
                    self._parse_schemas_raw_hdataset(item)
            else:
                raise HXLmException(
                    'No hmeta found on this item of this file. Error?')

    def _parse_schemas_raw_hdataset(self, hdataset):
        hdataset = HDataset().load_schema_dataset(hdataset)
        self._hdatasets.append(hdataset)
        # print('todo', hdataset)

    def export_schemas(self):
        return self._schemas_raw

    def load_schemas(self, schemas_raw):
        """load_schemas load object and convert to HMeta

        How the object is saved on disk (or received from external sources)
        is out of scope of this class.

        Args:
            schemas (Object): Load generic object to HMeta
        """

        # TODO: HMeta should allow load even HMetas from DIFFERENT files
        #       and then parse the fila result. For now it is able
        #       to work with one file at time but users may want to divide
        #       on several files (Emerson Rocha, 2021-03-01 05:10 UTC)
        self._schemas_raw = schemas_raw
        self._parse_schemas_raw()
        # print(schemas)
