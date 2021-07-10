"""hxlm.core.htype.storage
"""

# StorageHtype
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d
#      /1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=211012023


# - https://numpy.org/doc/stable/user/basics.types.html
# - https://numpy.org/doc/stable/reference/generated
#   /numpy.dtype.html#numpy.dtype

from dataclasses import dataclass

# https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes
# /dtypes.py
# from typing import (
#     Any
# )


@dataclass(init=True, repr=True, eq=True)
class StorageHtype:
    code: str = None
