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
    List,
    Union
)

import pathlib

import json
import csv
import yaml

from hxlm.core.io.util import (
    strip_file_protocol
)

__all__ = ['is_local', 'is_local_dir', 'is_local_file', 'load_file']


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


def is_local_file(file_path: str) -> bool:
    """Check if an path exist on local computer

    Args:
        path (str): Path to directory

    Returns:
        bool: True if exists on local disk (either file or path)
    """

    file_path = strip_file_protocol(file_path, strict=False)
    path_ = pathlib.Path(file_path)

    # print('is_local_file?? ', path)
    return path_.is_file() and os.access(path_, os.R_OK)

# NOTE: while the initial reason for load_file is load some small files
#       (like the configuration files for HDP) for huge files (the real
#       datasets) this would be less efficient. We should abstract this
#       for the user


def load_any_file(file_paths: List[str],
                  delimiter: str = ',') -> Union[dict, list]:
    """Generic simple file loader (YAML, JSON, CSV) for first available file

    See also function load_file()

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

    for filepath in file_paths:
        if is_local_file(filepath):
            return load_file(filepath, delimiter=delimiter)

    raise IOError(
        'No files available from this list [' + str(file_paths) + ']'
    )


@lru_cache(maxsize=128)
def load_file(file_path: str, delimiter: str = ',') -> Union[dict, list]:
    """Generic simple file loader (YAML, JSON, CSV) with cache.

    Note: this function is not HXL-aware. The CSV parser is primitive and
          is not intented for general use.

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
    norm_path = os.path.normpath(file_path)

    with open(norm_path, 'r') as stream:
        if norm_path.endswith('.json'):
            return json.load(stream)
        if norm_path.endswith('.yml'):
            return yaml.safe_load(stream)
        if norm_path.endswith('.csv'):
            reader = csv.reader(stream, delimiter=delimiter)
            result = []
            for row in reader:
                result.append(row)
            return result

    raise IOError('Unknow input [' + str(file_path) + ']')
