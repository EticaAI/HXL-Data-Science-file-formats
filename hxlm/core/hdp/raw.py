"""hxlm.core.hdp.raw

- '∀' ∀(x)
  - "given any" or "for all"
  - https://en.wikipedia.org/wiki/Universal_quantification
- '∃' ∃(x)
  - "there exists", "there is at least one"
  - https://en.wikipedia.org/wiki/Existential_quantification

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hxlm.core.hdp.datamodel import HDPRaw
from hxlm.core.types import ResourceWrapper


def ResourceWrapper2HDPRaw(resource: ResourceWrapper) -> HDPRaw:
    """Convert an ResourceWrapper to an HDPRaw

    This function will not do any deeper check (like if is an know vocabulary)
    but since the bare minimum specification requires that an HDP with HSilos
    should be a list with objects and one object that contains the natural
    language the HDP is written should contain one (and ONLY one) key starting
    with "([" (or "(.*[" and ending with "])" or "])", we require this here.

    Args:
        resource (ResourceWrapper): [description]

    Returns:
        HDPRaw: [description]
    """
    # pylint: disable=invalid-name

    hdpraw = HDPRaw
    hdpraw.resource = resource
    if resource.failed:
        hdpraw.failed = True
        # hdpraw.log.extend(resource.log)
        hdpraw.log.append('ResourceWrapper.failed ⇒ ∀(HDPRaw.failed)')
        return hdpraw

    return hdpraw
