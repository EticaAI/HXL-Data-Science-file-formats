"""WeightHXLtype is (...)"""
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d
#      /1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1507056660

from dataclasses import dataclass

# from typing import (
#     Any
# )


@dataclass(init=True, repr=True, eq=True)
class WeightHtype:
    """WeightHtype is (undocumented)
    """
    code: str = None
