"""hxlm.core.io.local

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# from functools import reduce, lru_cache
from functools import lru_cache

import os

from typing import (
    # Any,
    Union
)

import pathlib

import json
import csv
import yaml

from hxlm.core.io.util import (
    strip_file_protocol
)


def is_local(path: str) -> bool:
    """Check if what seems to be an path is valid on local computer

    Args:
        path (str): Path to file or directory

    Returns:
        bool: True if exists on local disk (either file or path)
    """

    path = strip_file_protocol(path, strict=False)
    path = pathlib.Path(path)
    return path.exists() and os.access(path, os.R_OK)


def is_local_dir(path: str) -> bool:
    """Check if an path exist on local computer

    Args:
        path (str): Path to directory

    Returns:
        bool: True if exists on local disk (either file or path)
    """

    path = strip_file_protocol(path, strict=False)
    path = pathlib.Path(path)
    return path.is_dir() and os.access(path, os.R_OK)


def is_local_file(path: str) -> bool:
    """Check if an path exist on local computer

    Args:
        path (str): Path to directory

    Returns:
        bool: True if exists on local disk (either file or path)
    """

    path = strip_file_protocol(path, strict=False)
    path = pathlib.Path(path)
    return path.is_file() and os.access(path, os.R_OK)

# NOTE: while the initial reason for load_file is load some small files
#       (like the configuration files for HDP) for huge files (the real
#       datasets) this would be less efficient. We should abstract this
#       for the user


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

    file_path = strip_file_protocol(file_path)

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
