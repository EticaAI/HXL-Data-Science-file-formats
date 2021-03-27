"""hxlm.core.model.recipe contains HRecipe (...)

Quick links:
- TEST ONLINE!
  - https://proxy.hxlstandard.org/api/from-spec.html
- JSON specs:
  - https://github.com/HXLStandard/hxl-proxy/wiki/JSON-processing-specs
- Filter parameters:
  - https://github.com/HXLStandard/hxl-proxy/wiki/JSON-recipes
- API endpoint:
  - https://github.com/HXLStandard/hxl-proxy/wiki/Process-JSON-spec
- JSON processing specs for HXL data, by David Megginson, 2021-03-11
  - https://docs.google.com/presentation/d
    /17vXOnq2atIDnrODGLs36P1EaUvT-vXPjsc2I1q1Qc50/edit#slide=id.p

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import json
import urllib

from dataclasses import dataclass


# TODO: allow user change the proxy URL (e.g. if using Docker or other service)
HXLPROXY_URL = "https://proxy.hxlstandard.org"


class HRecipe:
    """HMeta is the main entry point to glue collections of HConteiner and etc
    In practice, is mostly used to, with help with external utils, abstract
    hmeta.yml from disk
    """

    _valid_options = ['add_columns', 'aggregators', 'append_source',
                      'before', 'blacklist', 'date', 'date_format',
                      'is_regex', 'latlon', 'lower', 'map_source',
                      'number', 'number_format', 'original', 'pattern',
                      'patterns', 'purge', 'queries', 'replacement',
                      'reverse', 'skip_untagged', 'source_list_url',
                      'specs', 'upper', 'whitelist', 'whitespace']

    # Both are required
    input: str = None
    filter: str = None
    """The filter: add_columns, append, append_external_list, cache, ..."""

    add_columns: str = None
    aggregators: str = None
    append_source: str = None
    before: str = None
    # TODO: maybe propose an alias for blacklist/whitelist, see
    # - https://www.adexchanger.com/data-driven-thinking
    #   /no-more-inflammatory-jargon-change-blacklist-to-blocklist/
    # - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6148600/
    # - https://insights.dice.com/2020/07/17
    #   /whitelist-blacklist-the-new-debate-over-security-terminology/
    # - https://english.stackexchange.com/questions/51088
    #   /alternative-terms-to-blacklist-and-whitelist
    # Maybe allowlist / blocklist ? (Emerson Rocha, 2021-03-01 02:52 UTC)
    blacklist: str = None
    date: str = None
    date_format: str = None
    is_regex: str = None
    latlon: str = None
    lower: str = None
    map_source: str = None
    number: str = None
    number_format: str = None
    original: str = None
    pattern: str = None
    patterns: str = None
    purge: str = None
    queries: str = None
    replacement: str = None
    reverse: str = None
    skip_untagged: str = None
    source_list_url: str = None
    specs: str = None
    upper: str = None
    whitelist: str = None
    whitespace: str = None

    def __init__(self, recipe_raw=None):
        self.kind: str = 'HRecipe'
        self._recipe_raw = recipe_raw
        # if self._recipe_raw:
        #     self._recipe = recipe_raw

    def export_schema(self):
        # TODO: improve this. Still just outputing the input
        return self._recipe_raw
        # return vars(self)

    def get_hxlproxy_url(self):
        """For the current HRecipe instance return an HXLProxy URL

        TODO: check better if is selecting if the filter is selecting the
              rigth spreadsheet instead of default to the first one when using
              recipes. Do recipes need to specify the exact spreadsheet?
              (Emerson Rocha, 2021-03-01 10:21 UTC)
        """

        # @see https://github.com/HXLStandard/hxl-proxy/wiki
        #      /JSON-processing-specs

        # hxlspec = {}
        source = ''
        if self._recipe_raw['src']:
            # hxlspec['input'] = self._recipe_raw['src']
            source = self._recipe_raw['src']
        elif self._recipe_raw['srcs'] and self._recipe_raw['srcs'][0]:
            # hxlspec['input'] = self._recipe_raw['src'][0]
            source = self._recipe_raw['src'][0]

        spec_string = urllib.parse.quote(
            json.dumps(self._recipe_raw['filters']))

        return HXLPROXY_URL + '/data.csv?url=' + source + '&recipe=' \
            + spec_string

    def load_schema(self, recipe_raw):
        """load_schema load object and convert to HRecipe

        How the object is saved on disk (or received from external sources)
        is out of scope of this class.

        Args:
            recipe_raw (Object): Load generic object to HRecipe
        """

        self._recipe_raw = recipe_raw
        return self
        # self._parse_schemas_raw()
        # print(schemas)


# from typing import (
#     Any
# )


@dataclass(init=True, eq=True)
class RecipeHtype:
    kind: str = 'RecipeHtype'


class HXLProxyRecipeHtype(RecipeHtype):
    """Abstraction ton an HXL-Proxy recipe

    See https://github.com/HXLStandard/hxl-proxy/wiki/JSON-recipes

    Args:
        RecipeHtype ([type]): Base Class for data processing recipes
    """
    kind: str = 'HXLProxyRecipeHtype'


class ItemHXLProxyRecipeHtype(RecipeHtype):
    """Abstraction ton an HXL-Proxy recipe (individual item)

    See https://github.com/HXLStandard/hxl-proxy/wiki/JSON-recipes

    Args:
        RecipeHtype ([type]): [description]
    """

    kind: str = 'ItemHXLProxyRecipeHtype'

    # This is somewhat required
    filter: str = None
    """The filter: add_columns, append, append_external_list, cache, ..."""

    add_columns: str = None
    aggregators: str = None
    append_source: str = None
    before: str = None
    # TODO: maybe propose an alias for blacklist/whitelist, see
    # - https://www.adexchanger.com/data-driven-thinking
    #   /no-more-inflammatory-jargon-change-blacklist-to-blocklist/
    # - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6148600/
    # - https://insights.dice.com/2020/07/17
    #   /whitelist-blacklist-the-new-debate-over-security-terminology/
    # - https://english.stackexchange.com/questions/51088
    #   /alternative-terms-to-blacklist-and-whitelist
    # Maybe allowlist / blocklist ? (Emerson Rocha, 2021-03-01 02:52 UTC)
    blacklist: str = None
    date: str = None
    date_format: str = None
    is_regex: str = None
    latlon: str = None
    lower: str = None
    map_source: str = None
    number: str = None
    number_format: str = None
    original: str = None
    pattern: str = None
    patterns: str = None
    purge: str = None
    queries: str = None
    queries: str = None
    replacement: str = None
    reverse: str = None
    skip_untagged: str = None
    source_list_url: str = None
    specs: str = None
    upper: str = None
    whitelist: str = None
    whitespace: str = None
