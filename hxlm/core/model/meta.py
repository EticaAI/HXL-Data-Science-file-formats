"""hxlm.core.model.meta contains HMeta


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
from hxlm.core.model.file import HFile
from hxlm.core.model.recipe import HRecipe


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
        self._hfiles = []
        self._hrecipes = []
        self._htasks = []
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
                    self._parse_schemas_raw_hdatasets(item)
                if 'hfiles' in item:
                    self._parse_schemas_raw_hfile(item)
                if 'hrecipes' in item:
                    self._parse_schemas_raw_hrecipe(item)
                if 'htasks' in item:
                    self._parse_schemas_raw_htask(item)
            else:
                raise HXLmException(
                    'No hmeta found on this item of this file. Error?')

    def _parse_schemas_raw_hdatasets(self, hdatasets):
        dataset_ = []
        for dataset in hdatasets:
            dataset_ = HDataset().load_schema_dataset(dataset)
        self._hdatasets.append(dataset_)

    def _parse_schemas_raw_hfile(self, hfile):
        hfile = HFile().load_schema_file(hfile)
        self._hfiles.append(hfile)

    def _parse_schemas_raw_hrecipe(self, hrecipe):
        hrecipe = HRecipe().load_schema_recipe(hrecipe)
        self._hrecipes.append(hrecipe)

    def _parse_schemas_raw_htask(self, htask):
        """HTask is an draft
        """
        self._htasks.append(htask)
        # htask = HTask().load_schema_recipe(htask)
        # self._hrecipes.append(htask)

    def export_schemas(self):
        # as input would be this:
        #return self._schemas_raw
        schemas = []

        print('testtest _hdatasets', self._hdatasets)

        if len(self._hdatasets) > 0:
            hdatasets_ = []
            for dataset in self._hdatasets:
                hdatasets_.append(dataset.export_schema_dataset())

            schemas.append({'hdatasets': hdatasets_})
        
        return schemas

    def export_schemas_raw(self):
        # as input would be this:
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
