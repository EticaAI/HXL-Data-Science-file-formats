"""hxlm.core.hdp.hazmat.policy

While is impossible to deal with all potential specific needs on how
rules/ontologies (that per HDP conventions should themselves not be strict
confidential, because HDP is focused on auditability and make as hard as
possible to end users leak passwords or something on typical HDP file) at
least when using HDP to load data sets is predicatable that users who already
have some level of trust may by mistake try to process data that requires
higher level (like, for example, air gapped network) or that the data set
request that no local caching (or local backup) should be made.

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

from hxlm.core.hdp.datamodel import (
    HDPPolicyLoad,
    # HDPLoadRecursion
)
# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


def get_policy_HDSL1() -> HDPPolicyLoad:
    """Generate an HDPPolicyLoad for the internal constant 'HDSL1'

    See:
      - hxlm/core/constant.py
        - HDSL1: Low Sensitivity

    Returns:
        [HDPPolicyLoad]: HDPPolicyLoad
    """
    # pylint: disable=invalid-name

    policy = HDPPolicyLoad
    return policy


def get_policy_HDSL4() -> HDPPolicyLoad:
    """Generate an HDPPolicyLoad for the internal constant 'HDSL4'

    See:
      - hxlm/core/constant.py
        - HDSL4: Severe Sensitivity

    Returns:
        [HDPPolicyLoad]: HDPPolicyLoad
    """
    # pylint: disable=invalid-name

    policy = HDPPolicyLoad
    return policy
