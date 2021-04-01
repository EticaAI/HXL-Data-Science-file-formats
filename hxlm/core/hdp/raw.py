"""hxlm.core.hdp.raw deal with RAW HDP instructures before transpose with VKG

Rationale
----------

While most use ideal use of HDP will implicitly convert on-the-fly for the user
using the Vocabulary Knowledge Graph (VKG), the hxlm.core.hdp.raw contains
functions to deal with objects that have bare minimum valid HDP syntax. Two
expected examples:

- An HDP file written in an unknown vocabulary for the current user
- An know vocabulary, but misspelled terms

Valid cases for RAW HDP files
------------------------------

The most common expected (to no say, desirable) use case for at least this
module offer minimal usability is when an HDP file is written in an entire new
language. To make it viable, the underlining tools need to offer some minimum
support.

Note that while this obvioulsy should happen with complete new languages, most
of so called macrolanguages (ARA https://iso639-3.sil.org/code/ara and
https://iso639-3.sil.org/code/zho, just to cite a few) do have more variants
that are very different. And is complicated to people agree with each other
even when they want it. That's why, when new languages appear, it may take
time to eventually people come to a consensus and in the middle of the process
the pivot languages may be something not even in the same writing system, like
Spanish or French.

>>> import hxlm.core as HXLm
>>> resource1 = HXLm.io.util.get_entrypoint(
...    HXLm.HDATUM_UDHR + 'udhr.lat.hdp.yml')
>>> hdpraw = convert_resource_to_hdpraw(resource1)
>>> hdpraw
<class 'hxlm.ontologia.python.hdp.radix.HDPRaw'>
>>> hdpraw.failed
False
>>> type(hdpraw.hsilos)
<class 'list'>
>>> resource1hmeta = get_raw_hmeta(hdpraw.hsilos[0])
>>> resource1hmeta.keys()
dict_keys(['([Lingua Latina])'])
>>> resource1hcor = get_raw_hcor(hdpraw.hsilos[0])
>>> resource1hcor.keys()
dict_keys(['hsilo', 'hdatum'])

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os

from hxlm.ontologia.python.hdp.radix import HDPRaw
from hxlm.ontologia.python.systema import ResourceWrapper

# os.environ["HDP_DEBUG"] = "1"
_IS_DEBUG = bool(os.getenv('HDP_DEBUG', ''))


def convert_resource_to_hdpraw(resource: ResourceWrapper) -> HDPRaw:
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

    # hdpraw.log.append('ResourceWrapper.failed ⇒ ∀(HDPRaw.failed)')

    if resource.failed:
        hdpraw.failed = True
        hdpraw.log.append('ResourceWrapper.failed ⇒ ∀(HDPRaw.failed)')
        if _IS_DEBUG:
            print('∃(ResourceWrapper.failed) ⇔ ∀(HDPRaw.failed)')
        return hdpraw

    if isinstance(resource.content, str):
        hdpraw.failed = True
        hdpraw.log.append(
            '(ResourceWrapper.content ⇒ "str") ⇒ ∀(HDPRaw.failed)')

    if isinstance(resource.content, list):
        content_ = resource.content
    else:
        # dict and any garbage, like str, another list, etc
        content_ = [resource.content]

    error_count = 0
    for idx, maybe_silo in enumerate(content_):
        if not isinstance(maybe_silo, dict):
            error_count += 1
            hdpraw.log.append('ResourceWrapper.content(' +
                              str(idx) + ') ¬ dict')
            continue
        if is_raw_hdp_item_syntax(maybe_silo):
            hdpraw.hsilos.append(maybe_silo)
        else:
            error_count += 1
            hdpraw.log.append('ResourceWrapper.content(' +
                              str(idx) + ') ¬ is_raw_hdp_item_syntax')

    if error_count > 0:
        hdpraw.failed = True

    if len(hdpraw.log) > 0:
        if _IS_DEBUG:
            print('ResourceWrapper2HDPRaw', error_count, hdpraw.log)

    return hdpraw


def get_raw_hcor(thing: dict) -> dict:
    """For an RAW hsilo-like dict, get only the non hmeta part.

    This function requires at leat one key that seems an hmeta, but if more
    than one exists, will also return None.

    Args:
        thing (dict): An HSilo-like dictionary

    Returns:
        dict: An dict with only the hmeta part (no transposition)
    """

    if thing is None or not isinstance(thing, dict):
        return None

    if len(thing.keys()) == 0:
        return None

    dict_with_only_hcor = {}

    for _, key in enumerate(thing):
        if is_raw_hmeta_key(key):
            continue
        dict_with_only_hcor[key] = thing[key]

    return dict_with_only_hcor


def get_raw_hmeta(thing: dict) -> dict:
    """For an RAW hsilo-like dict, get only the hmeta part (no vocab search)

    This function requires at leat one key that seems an hmeta, but if more
    than one exists, will also return None.

    Note that this will not check if do exist any hcor (the body part). The
    is_raw_hdp_item_syntax is responsible for this high level.

    Args:
        thing (dict): An HSilo-like dictionary

    Returns:
        dict: An dict with only the hmeta part (no transposition)
    """

    hmeta_count = 0
    dict_with_only_hmeta = {}

    if thing is None or not isinstance(thing, dict):
        return None

    for _, key in enumerate(thing):
        if not is_raw_hmeta_key(key):
            continue

        dict_with_only_hmeta[key] = thing[key]
        hmeta_count += 1

    # TODO: not check for body, let the is_raw_hdp_item_syntax do it
    if not hmeta_count == 1:
        return None

    return dict_with_only_hmeta


def is_raw_hdp_item_syntax(thing: dict) -> bool:
    """Check if an dict object is bare-minimum like an HSilo (no vocab check)

    Only one, and exact one, dict key could be somewhat equivalent to an
    hmeta key header. Also an HSilo needs at least some key in addition to the
    hmeta key header

    Args:
        thing (dict): An dictionary to check if is like an HSilo

    Returns:
        bool: True if HSilo like

    >>> hdummy = {'([ZZZ])': ['test'], 'hdatum': []}
    >>> is_raw_hdp_item_syntax(hdummy)
    True
    >>> is_raw_hdp_item_syntax([hdummy])
    False
    >>> hdummy_err = {'([ZZZ])': ['test'], '([YYY])': []}
    >>> is_raw_hdp_item_syntax(hdummy_err)
    False
    >>> is_raw_hdp_item_syntax({})
    False
    >>> is_raw_hdp_item_syntax(None)
    False
    """

    hcor = get_raw_hcor(thing)
    hmeta = get_raw_hmeta(thing)

    return (hmeta is not None) and (hcor is not None)


def is_raw_hmeta_key(term: str) -> bool:
    """For a given string term, return if MAY be an HMeta key (no vocab search)

    Args:
        term (str): The term to search

    Returns:
        bool: True if MAY be an hmeta key
    """

    # The minimal viable term is '([ZZZ])', We do some quick checks
    if term is None or len(term) < 7:
        return False

    if not term.startswith('(') or not term.endswith(')') or \
            term.index('[') == -1 or term.index(']') == -1:
        return False

    # TODO: the has_hsilo_syntax is doing a very basic check. Some
    #       responsability will be passed for check later, like actually
    #       compare to an know language. But we could at least check
    #       here for wrong number of open and closed () [].

    return True
