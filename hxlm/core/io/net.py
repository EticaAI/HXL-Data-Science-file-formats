"""hxlm.core.io.net

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from functools import reduce, lru_cache
# from functools import lru_cache

# import os

from typing import (
    # Any,
    List,
    Union
)
import json
import csv

import yaml
import requests

# TODO: like libhxl-python, also implement
#       https://pypi.org/project/requests-cache/
#       https://github.com/reclosedev/requests-cache/tree/master/examples
#       https://requests-cache.readthedocs.io/en/latest/


__all__ = [
    'is_remote_file',
    'load_remote_file'
]


def is_remote_file(iri: str, verify: bool = True) -> bool:
    """Check if a remote file exists without fully downloaded it

    This method will do an HEAD request, so as long as you are not trying to
    check a resouce that is created on demand (like an HXL-proxy without
    cache) this strategy is acceptable cheap

    Args:
        iri (str): An single HTT
        verify (bool, optional): [description]. Defaults to True.

    Returns:
        [bool]: True if ok
    """

    # TODO: is_remote_file is likely to require more testing (like how to deal
    #       with redirects)

    resp = requests.head(iri, verify=verify)
    return resp.ok


def load_huge_remote_file():
    """(not implemented yet)
    """
    raise NotImplementedError(
        'hxlm.core.io.net is not optimized at this ' +
        'moment for huge files, like for streams. You can use ' +
        'load_remote_file or HXL directly')

# @lru_cache(maxsize=128)


def load_any_remote_file(iris: List[str],
                         delimiter: str = ',',
                         verify: bool = True) -> Union[dict, list]:
    """Generic remote file loader (YAML, JSON, CSV) for first available resource

    See also function load_remote_file()

    Args:
        file_paths (List[str]): List of one or more absolute file paths
        delimiter (str, optional): If any file do have CSV extension, this
                    could be used to parse an not fully HXLated dataset. Not
                    as powerful as HXL parser, so use as last resort.
                    Defaults to ','.

    Raises:
        IOError: If none of the file_paths is available this will raise error

    Returns:
        Union[dict, list]: Return parsed result of the file
    """

    for iri in iris:
        if is_remote_file(iri):
            return load_remote_file(iri, delimiter=delimiter, verify=verify)

    raise IOError(
        'No remote files available from this list [' + str(iris) + ']'
    )


def load_remote_file(iri: str, delimiter: str = ',',
                     verify: bool = True) -> Union[dict, list]:
    """Generic simple remote file loader (YAML, JSON, CSV)

    Note: this function is not HXL-aware. The CSV parser is primitive and
          is not intented for general use.

    Args:
        iri (str): Path to an exact file (not directory)
        delimiter (str): Delimiter. Only applicable if is an CSV/TSV like item
        verify (bool): If using HTTPS, when true will enforce valid certificate

    Returns:
        Union[dict, list]: The loaded file result
    """

    resp = requests.get(iri, verify=verify)

    if resp.ok:
        if iri.endswith('.json'):
            return json.load(resp.text)
        if iri.endswith('.yml'):
            return yaml.safe_load(resp.text)

        # Note: not actually tested with remote CSV resources at the moment
        #       But still here just as syntatic sugar with
        #       hxlm.core.io.local.load_file()
        if iri.endswith('.csv'):
            reader = csv.reader(resp.text, delimiter=delimiter)
            result = []
            for row in reader:
                result.append(row)
            return result

        raise IOError('Unknow input extension [' + str(iri) + ']')

    raise IOError('Request not OK [' + str(iri) + '][' + str(resp) + ']')
