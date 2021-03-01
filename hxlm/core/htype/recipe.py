"""hxlm.core.htype.recipe

TODO: this actually is more complicated than averagen HType, and is not just
      an dataclass. We should rework on something else
      (Emerson Rocha, 2021-03-01 02:20 UTC)

See 
- https://github.com/HXLStandard/hxl-proxy/wiki/JSON-recipes
- https://github.com/OCHA-DAP/hxl-recipes


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


from dataclasses import dataclass

from typing import (
    Any
)


@dataclass(init=True, eq=True)
class RecipeHtype:
    kind: str = 'RecipeHtype'


class HXLProxyRecipeHtype(RecipeHtype):
    """Abstraction ton an HXL-Proxy recipe

    See https://github.com/HXLStandard/hxl-proxy/wiki/JSON-recipes

    Args:
        RecipeHtype ([type]): [description]
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
