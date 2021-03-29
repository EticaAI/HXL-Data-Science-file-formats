"""hxlm.core.hdp.index


An HDP index file have syntax similar to this:

    # .hdp.yml
    #### Vocabulary Knowledge Graph
    # Notation: ∫, ∬, ∭
    ∫:
      - hxlm/data/core.vkg.yml

    #### Localization Knowledge Graph
    # Notation: ∮, ∯, ∰
    ∮:
      - hxlm/data/core.lkg.yml

    #### HDP Declarative Programming entry points
    # Notation: ∂
    ∂:
      - hxlm/data/hxl/hxl.eng.hdp.yml
      - hxlm/data/udhr/udhr.lat.hdp.yml


>>> import hxlm.core as HXLm
>>> exemplum = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_EXEMPLUM, indexes=['.hdp.yml'])
>>> exemplum.content.keys()
dict_keys(['∫', '∮', '∂'])
>>> is_index_hdp(exemplum.content)
True
>>> non_index = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_UDHR + 'udhr.lat.hdp.yml')
>>> is_index_hdp(non_index)
False

# >>> exemplum = HXLm.io.util.get_entrypoint(
# ...    HXLm.HDATUM_EXEMPLUM, indexes=['.hdp.yml'])
# >>> exemplum



Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# TODO: move this to ontology
HDP_INDEX_ALLOWED = (
    '∫',  # ∫, ∬, ∭
    '∮',  # ∮, ∯, ∰
    '∂'
)


def is_index_hdp(thing: dict) -> bool:
    """Check if a file is an valid HDP index of files

    Args:
        thing (dict): An HDP Index object

    Returns:
        bool: True if valid HDP-like index
    """
    if thing is None or not isinstance(thing, dict):
        return False

    valid_with_content = 0
    for key in thing:
        if key not in HDP_INDEX_ALLOWED:
            return False
        if not isinstance(thing[key], list):
            return False
        if len(thing[key]) > 0:
            valid_with_content += 1

    return valid_with_content > 0
