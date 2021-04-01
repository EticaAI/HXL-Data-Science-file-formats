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

>>> non_index = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_UDHR + 'udhr.lat.hdp.yml')
>>> is_index_hdp(non_index)
False

>>> exemplum = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_EXEMPLUM, indexes=['.hdp.yml'])
>>> exemplum.content.keys()
dict_keys(['∫', '∮', '∂'])
>>> is_index_hdp(exemplum.content)
True

# >>> ex_index = convert_resource_to_hdpindex(exemplum)
# >>> ex_index.lkg
# >>> ex_index.resource.entrypoint
# >>> exemplum = HXLm.io.util.get_entrypoint(
# ...    HXLm.HDATUM_EXEMPLUM, indexes=['.hdp.yml'])
# >>> exemplum



Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

from hxlm.ontologia.python.systema import (
    ResourceWrapper
)


from hxlm.ontologia.python.hdp.radix import (
    HDPIndex
)

__all__ = ['convert_resource_to_hdpindex', 'is_index_hdp']

# TODO: move this to ontologia
HDP_INDEX_ALLOWED = (
    '∫',     # ∫, ∬, ∭
    # 'vkg',   # alias for ∫
    '∮',     # ∮, ∯, ∰
    # 'lkg'    # alias for ∮
    '∂',     # ∂
    # 'hdp'    # alias for ∂
)


# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


def convert_resource_to_hdpindex(resource: ResourceWrapper) -> HDPIndex:
    """Convert an ResourceWrapper to an HDPIndex

    Args:
        resource (ResourceWrapper): The resource with the value

    Returns:
        HDPIndex: The HDPIndex object
    """

    hdpindex = HDPIndex
    hdpindex.resource = resource

    # hdpraw.log.append('ResourceWrapper.failed ⇒ ∀(HDPRaw.failed)')

    if resource.failed:
        hdpindex.failed = True
        hdpindex.log.append('ResourceWrapper.failed ⇒ ∀(HDPIndex.failed)')
        return hdpindex

    if not is_index_hdp(resource.content):
        hdpindex.failed = True
        hdpindex.log.append('ResourceWrapper.content ¬ is_index_hdp')
        return hdpindex

    if 'hdp' in resource.content:
        hdpindex.hdp.extend(resource.content['hdp'])
    if '∂' in resource.content:
        hdpindex.hdp.extend(resource.content['∂'])

    if 'vkg' in resource.content:
        hdpindex.vkg.extend(resource.content['vkg'])
    if '∫' in resource.content:
        hdpindex.vkg.extend(resource.content['∫'])

    if 'lkg' in resource.content:
        hdpindex.lkg.extend(resource.content['lkg'])
    if '∮' in resource.content:
        hdpindex.lkg.extend(resource.content['∮'])

    # TODO: since files often have relative paths, test if is relative
    #       (do not start with protocol, like file:/// or urn://) and
    #       then prepend whatever was the entrypoint, like
    #          hdpindex.hdp[0] = resource.entrypoint + hdpindex.hdp[0]

    # TODO: break this method in smaller ones

    if len(hdpindex.hdp) > 0:
        for idx, item in enumerate(hdpindex.hdp):
            # print(idx, item, item.find('://'), item.find('://') == -1)
            if item.find('://') == -1:
                hdpindex.hdp[idx] = resource.entrypoint['entrypoint'] + \
                    hdpindex.hdp[idx]

    if len(hdpindex.vkg) > 0:
        for idx, item in enumerate(hdpindex.vkg):
            # print(idx, item, item.find('://'), item.find('://') == -1)
            if item.find('://') == -1:
                hdpindex.vkg[idx] = resource.entrypoint['entrypoint'] + \
                    hdpindex.vkg[idx]

    if len(hdpindex.lkg) > 0:
        for idx, item in enumerate(hdpindex.lkg):
            # print(idx, item, item.find('://'), item.find('://') == -1)
            if item.find('://') == -1:
                hdpindex.lkg[idx] = resource.entrypoint['entrypoint'] + \
                    hdpindex.lkg[idx]

    return hdpindex


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
    valid_even_if_empty = 0
    for key in thing:
        # print('key', key, key not in HDP_INDEX_ALLOWED, len(thing[key]) > 0)
        if key not in HDP_INDEX_ALLOWED:
            return False
        if thing[key] is None:
            valid_even_if_empty += 1
            continue
        if not isinstance(thing[key], list):
            return False
        if len(thing[key]) > 0:
            valid_with_content += 1
            valid_even_if_empty += 1
            # raise SyntaxError('DEBUG: valid_with_content')

    # print('valid',  valid_even_if_empty > 0)
    # return valid_with_content > 0
    return valid_even_if_empty > 0
