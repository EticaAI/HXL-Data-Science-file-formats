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
    # List,
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


def is_remote_file(iri: str):
    """TODO: is_remote_file is an draft (HTTP HEAD request) """
    # req = requests.head(iri)
    # print('is_remote_filereq', req)

    return True


# @lru_cache(maxsize=128)
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
