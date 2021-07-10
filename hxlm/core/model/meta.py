"""hxlm.core.model.meta contains HMeta


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hxlm.core.exception import (
    HXLmException
)
# from hxlm.core.model import (
#     HDataset
# )
from hxlm.core.model.base import (
    HDataset
)
from hxlm.core.model.file import HFile
from hxlm.core.model.recipe import HRecipe
# from hxlm.core.schema import ConversorHSchema

# TODO: as 2021-03-23 the HMeta is outdated. Some terms, like hdatasets
#       (hdatum) changed. (Emerson Rocha, 2021-03-23 05:29 UTC)


class HMeta:
    """HMeta is the main entry point to glue collections of HConteiner and etc
    In practice, is mostly used to, with help with external utils, abstract
    hmeta.yml from disk
    """

    def __init__(self, schemas_raw=None, vocab_base=None):
        self.kind: str = 'HMeta'
        self._schemas_raw = schemas_raw
        self._schemas_internal = None
        self._schemas = []
        self._hdatasets = []
        self._hfiles = []
        self._hrecipes = []
        self._htasks = []

        if vocab_base:
            self._vocab_base = vocab_base
        else:
            self._vocab_base = None  # TODO

        if self._schemas_raw:
            self._parse_schemas_raw()

    def _parse_schemas_raw(self):
        # print('self._schemas_raw', self._schemas_raw)
        # print('self._schemas', self._schemas)
        # self._schemas_internal =
        #      ConversorHSchema(vocab_base=self._vocab_base)

        for item in self._schemas_raw:
            # print('_parse_schemas_raw item', item)
            # print('_parse_schemas_raw item type', type(item))
            # print('_parse_schemas_raw item type hmeta', type(item['hmeta']))
            # if 'hmeta' in item:
            if 'urn' in item:
                # print('_parse_schemas_raw item item.hmeta yes')
                if 'hdatasets' in item:
                    # print('oooooi', item['hdatasets'])
                    self._parse_schemas_raw_hdatasets(item['hdatasets'])
                if 'hfiles' in item:
                    self._parse_schemas_raw_hfiles(item['hfiles'])
                if 'hrecipes' in item:
                    self._parse_schemas_raw_hrecipe(item['hrecipes'])
                # htasks is deprecated
                # if 'htasks' in item:
                #     self._parse_schemas_raw_htask(item['htasks'])
            else:
                raise HXLmException(
                    'No hmeta found on this item of this file. Error?')

    def _parse_schemas_raw_hdatasets(self, hdatasets):
        dataset_ = []
        for dataset in hdatasets:
            dataset_ = HDataset().load_schema_dataset(dataset)
        self._hdatasets.append(dataset_)

    def _parse_schemas_raw_hfiles(self, hfiles):
        # hfile_ = []
        for hfile in hfiles:
            hfile_ = HFile().load_schema(hfile)

            # print('is_available_locally', hfile_.is_available_locally())
            # print('is_available_sources', hfile_.is_available_sources())
            # print('reload_from_souces', hfile_.reload_from_souces())
            self._hfiles.append(hfile_)

    def _parse_schemas_raw_hrecipe(self, hrecipes):
        hrecipe_ = []
        for recipe in hrecipes:

            # print('oioioi', recipe)
            hrecipe_ = HRecipe().load_schema(recipe)
        self._hrecipes.append(hrecipe_)

        # hrecipe = HRecipe().load_schema(hrecipe)
        # self._hrecipes.append(hrecipe)

    # htasks is deprecated
    # def _parse_schemas_raw_htask(self, htask):
    #     """HTask is an draft
    #     """
    #     self._htasks.append(htask)
    #     # htask = HTask().load_schema_recipe(htask)
    #     # self._hrecipes.append(htask)

    def export_schemas(self):
        """Export HMeta schema (not data) after being processed by each class

        Note that the result may not expose raw results. like compliance
        computed rules or (if any) encryption keys.

        Compared to debug methods, this class is the recommended way to tell
        users to inspect implementations

        Returns:
            [Array]: Array of schemas
        """
        schemas = []

        if len(self._hdatasets) > 0:
            hdatasets_ = []
            for dataset in self._hdatasets:
                hdatasets_.append(dataset.export_schema())
            schemas.append({'hdatasets': hdatasets_})

        if len(self._hfiles) > 0:
            hfiles_ = []
            for file in self._hfiles:
                hfiles_.append(file.export_schema())
            schemas.append({'hfiles': hfiles_})

        if len(self._hrecipes) > 0:
            recipes_ = []
            for recipe in self._hrecipes:
                # print('recipe.get_hxlproxy_url', recipe.get_hxlproxy_url())
                # print(vars(recipe))
                recipes_.append(recipe.export_schema())
            schemas.append({'hrecipe': recipes_})

        # TODO: implement htasks

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
