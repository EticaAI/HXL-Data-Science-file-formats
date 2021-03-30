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

from hxlm.core.types import (
    EntryPointType,
    # ResourceWrapper
)

from hxlm.core.hdp.datamodel import (
    HDPPolicyLoad,
    # HDPLoadRecursion
)
# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


def _get_bunker() -> HDPPolicyLoad:
    """bunker"""
    policy = HDPPolicyLoad

    policy.enforce_startup_generic_tests = True

    policy.allowed_entrypoint_type = (
        EntryPointType.LOCAL_DIR,  # air-gapped compliant
        EntryPointType.LOCAL_FILE,  # air-gapped compliant
        EntryPointType.NETWORK_DIR,  # air-gapped compliant
        EntryPointType.NETWORK_FILE,  # air-gapped compliant
        EntryPointType.PYDICT,  # air-gapped compliant
        EntryPointType.PYLIST,  # air-gapped compliant
        EntryPointType.STRING,  # air-gapped compliant
        EntryPointType.URN  # air-gapped compliant (it's an resolver)
    )
    policy.safer_zones_hosts = None
    policy.safer_zone_list = None

    return policy


def _get_debug() -> HDPPolicyLoad:
    """debug"""
    policy = _get_user_know_what_is_doing()
    policy.debug_no_restrictions = True
    return policy


def _get_user_know_what_is_doing() -> HDPPolicyLoad:
    """get_user_know_what_is_doing template policy

    Returns:
        HDPPolicyLoad: The policy
    """
    policy = HDPPolicyLoad

    # Note: in general the default generic HDPPolicyLoad somewhat already
    #       is flexible (with exception that does not have hardcoded names
    #       for network domains). This means that we will add some domains.
    #       Most of then are either for organizations accredited at
    #       international level or are places that averange software developer
    #       would release open source material.
    policy.custom_allowed_domains = (
        # >>> very specific global level domains
        '.int',  # intergovernmental organisations
        # TODO: add suffix of user country (if we manage to detect)
        # >>> Humanitarian-focused
        'data.humdata.org',
        'hxlstandard.org',  # Includes proxy.hxlstandard.org
        # >>> Common sites to share code and data
        'gitee.com',  # Very popular on China.
        'github.com',
        'githubusercontent.com',
        'gitlab.com',

    )
    return policy


def get_policy_HDSL1() -> HDPPolicyLoad:
    """Syntatic sugar to generate an generic optionated policy for 'HDSL1'

    Very important notes:
      - Implementers very likely would want to create HDPPolicyLoad directly
        that would align with the specific needs

    See:
      - hxlm/core/constant.py
        - HDSL1: Low Sensitivity

    Returns:
        [HDPPolicyLoad]: HDPPolicyLoad
    """
    # pylint: disable=invalid-name

    return _get_user_know_what_is_doing()


def get_policy_HDSL4() -> HDPPolicyLoad:
    """Generate an HDPPolicyLoad for the internal constant 'HDSL4'

    Very important notes:
      - Implementers very likely would want to create HDPPolicyLoad directly
        that would align with the specific needs

    See:
      - hxlm/core/constant.py
        - HDSL4: Severe Sensitivity

    Returns:
        [HDPPolicyLoad]: HDPPolicyLoad
    """
    # pylint: disable=invalid-name
    return _get_bunker()
