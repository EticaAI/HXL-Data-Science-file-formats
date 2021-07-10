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
from urllib.parse import urlparse

from typing import (
    Union
)

from hxlm.core.io.util import (
    get_entrypoint_type
)

from hxlm.ontologia.python.systema import (
    EntryPointType,
    # ResourceWrapper
)

from hxlm.ontologia.python.hdp.aux import (
    AuxLoadPolicy,
    # HDPLoadRecursion
)

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))

__all__ = ['get_policy_HDSL1', 'get_policy_HDSL4',
           'is_not_acceptable_load_this']


def _get_bunker() -> AuxLoadPolicy:
    """bunker"""
    policy = AuxLoadPolicy()

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


def _get_debug() -> AuxLoadPolicy:
    """debug"""
    policy = _get_user_know_what_is_doing()
    policy.debug_no_restrictions = True
    return policy


def _get_user_know_what_is_doing() -> AuxLoadPolicy:
    """get_user_know_what_is_doing template policy

    Returns:
        AuxLoadPolicy: The policy
    """
    policy = AuxLoadPolicy()

    # Note: in general the default generic AuxLoadPolicy somewhat already
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


def get_policy_HDSL1() -> AuxLoadPolicy:
    """Syntatic sugar to generate an generic optionated policy for 'HDSL1'

    Very important notes:
      - Implementers very likely would want to create AuxLoadPolicy directly
        that would align with the specific needs

    See:
      - hxlm/core/constant.py
        - HDSL1: Low Sensitivity

    Returns:
        [AuxLoadPolicy]: AuxLoadPolicy
    """
    # pylint: disable=invalid-name

    return _get_user_know_what_is_doing()


def get_policy_HDSL4() -> AuxLoadPolicy:
    """Generate an AuxLoadPolicy for the internal constant 'HDSL4'

    Very important notes:
      - Implementers very likely would want to create AuxLoadPolicy directly
        that would align with the specific needs

    See:
      - hxlm/core/constant.py
        - HDSL4: Severe Sensitivity

    Returns:
        [AuxLoadPolicy]: AuxLoadPolicy
    """
    # pylint: disable=invalid-name
    return _get_bunker()


def is_not_acceptable_load_this(
        entrypoint_str: str,
        policy: AuxLoadPolicy) -> Union[bool, str]:
    """Checj if an entrypoint string is not acceptable by an policy

    Args:
        entrypoint_str (str): An full entrypoint string (not an object)
        policy (AuxLoadPolicy): the reference policy

    Returns:
        Union[bool, str]: False if ok. String with explanation if not.

    >>> url_INT = 'https://example.int/data/data.lat.urn.yml'
    >>> url_com = 'git://example.com/data/data.lat.urn.yml'
    >>> url_SSH = 'ssh://example.int/home/user/data/data.lat.urn.yml'
    >>> pHDSL1 = get_policy_HDSL1()
    >>> pHDSL4 = get_policy_HDSL4()
    >>> is_not_acceptable_load_this(url_INT, pHDSL1)
    False
    >>> is_not_acceptable_load_this(url_com, pHDSL1)
    '∉ policy.allowed_entrypoint_type'
    >>> is_not_acceptable_load_this(url_SSH, pHDSL1)
    False
    >>> is_not_acceptable_load_this(url_SSH, pHDSL4)
    '¬ policy.allowed_entrypoint_type'
    """

    if policy.debug_no_restrictions:
        return False

    if entrypoint_str.find('://') == -1:
        return '∄ (RFC3986 protocol)'

    etype = get_entrypoint_type(entrypoint_str)

    # print(entrypoint_str, etype, policy.allowed_entrypoint_type)
    if etype not in policy.allowed_entrypoint_type:
        # print(entrypoint_str, etype, policy.allowed_entrypoint_type)
        return '¬ policy.allowed_entrypoint_type'

    if etype in [EntryPointType.HTTP, EntryPointType.FTP,
                 EntryPointType.GIT, EntryPointType.SSH]:
        result = urlparse(entrypoint_str).netloc
        # print('result', result)
        if policy.custom_allowed_domains is None or \
                len(policy.custom_allowed_domains) == 0:
            return '∅ policy.custom_allowed_domains'
            # return False
        for domain_suffix in policy.custom_allowed_domains:
            if result.endswith(domain_suffix):
                return False
        return '∉ policy.allowed_entrypoint_type'
        # return False

    return False
