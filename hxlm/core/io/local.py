"""hxlm.core.io.local

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from functools import reduce, lru_cache
from functools import lru_cache

from typing import (
    # Any,
    Union
)

import json
import csv
import yaml


def is_local():
    """TODO: is_local is an draft"""


def is_local_dir():
    """TODO: is_local_dir is an draft"""


def is_local_file():
    """TODO: is_local_file is an draft"""


@lru_cache(maxsize=128)
def load_file(file_path: str, delimiter: str = ',') -> Union[dict, list]:
    """Generic simple file loader (YAML, JSON, CSV) with cache.

    Args:
        file_path (str): Path or bytes for the file
        delimiter (str): Delimiter. Only applicable if is an CSV/TSV like item

    Returns:
        Union[dict, list]: The loaded file result

    >>> import hxlm.core as HXLm
    >>> file_path = HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml'
    >>> hsilo_example = load_file(file_path)
    >>> hsilo_example[0]['hsilo']['tag']
    ['udhr']
    """

    with open(file_path, 'r') as stream:
        if file_path.endswith('.json'):
            return json.load(stream)
        if file_path.endswith('.yml'):
            return yaml.safe_load(stream)
        if file_path.endswith('.csv'):
            reader = csv.reader(stream, delimiter=delimiter)
            result = []
            for row in reader:
                result.append(row)
            return result

    raise SystemError('Unknow input [' + str(file_path) + ']')
