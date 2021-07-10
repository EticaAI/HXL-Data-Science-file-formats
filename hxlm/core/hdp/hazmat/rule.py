"""hxlm.core.hdp.hazmat.rule contains routines to load rules/ontologies

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

from hxlm.ontologia.python.hdp.aux import (
    AuxLoadRecursion
)

from hxlm.ontologia.python.hdp.aux import (
    AuxLoadPolicy,
    # HDPLoadRecursion
)

from hxlm.core.hdp.index import (
    # convert_resource_to_hdpindex,
    is_index_hdp
)

from hxlm.core.hdp.raw import (
    # convert_resource_to_hdpraw,
    is_raw_hdp_item_syntax,
    ResourceWrapper
)

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


def hdprecursion_resource(
        resource: ResourceWrapper,
        policy: AuxLoadPolicy) -> AuxLoadRecursion:
    """HDP recursion of resource

    Args:
        resource (ResourceWrapper): [description]

    Returns:
        HDPRecursion: [description]
    """
    if resource.failed:
        if _IS_DEBUG:
            print('resource.failed: [' + str(resource) + ']' +
                  '[' + str(policy) + ']')
    elif is_index_hdp(resource.content):
        print('TODO: is_index_hdp')

    elif is_raw_hdp_item_syntax(resource.content):
        print('TODO: is_index_hdp')
    else:
        print(
            'resource ¬ (is_index_hdp | is_raw_hdp_item_syntax) ['
            + str(resource) + ']')
