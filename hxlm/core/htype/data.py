"""DataHXLtype is (TODO: document)"""
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d
#      /1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=717813523

# ## libhxl-python Datatypes (we must be fully compatible/extend these)
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/datatypes.py
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/model.py
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/validation.py
#  - https://docs.google.com/spreadsheets/d
#    /1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=1881622062
# ## numpy
#  - https://numpy.org/devdocs/user/basics.types.html
#  - https://numpy.org/devdocs/reference/arrays.dtypes.html#arrays-dtypes
#  - https://numpy.org/devdocs/reference/typing.html#module-numpy.typing
# ## pandas
#  - https://github.com/pandas-dev/pandas/tree/master/pandas/core/dtypes
#  - https://github.com/pandas-dev/pandas/blob/master/pandas/core
#    /dtypes/dtypes.py  # noqa
# ##
# - attrs
#   - https://www.attrs.org/en/stable/

# Temp references
# - https://docs.python.org/3/library/typing.html
# - https://docs.python.org/3/library/typing.html
# - https://docs.python.org/3/library/dataclasses.html
# - https://stackoverflow.com/questions/47955263
#   /what-are-data-classes-and-how-are-they-different-from-common-classes
# - https://www.programiz.com/python-programming/multiple-inheritance

from dataclasses import dataclass

# https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes/dtypes.py
from typing import (
    Any,
    Type
)

from hxlm.core.model.base import HXLBaseInformation
# from hxlm.core.htype.encryption import EncryptionHtype
from hxlm.core.htype.level import LevelHtype
# from hxlm.core.htype.sensitive import SensitiveHtype
from hxlm.core.htype.storage import StorageHtype
from hxlm.core.htype.usage import UsageHtype
from hxlm.core.htype.weight import WeightHtype


HXL_HTYPE_DATA_TEXT_UID = "textDataHtype"
HXL_HTYPE_DATA_NUMBER_UID = "numberDataHtype"
HXL_HTYPE_DATA_URL_UID = "urlDataHtype"
HXL_HTYPE_DATA_EMAIL_UID = "emailDataHtype"
HXL_HTYPE_DATA_PHONE_UID = "phoneDataHtype"
HXL_HTYPE_DATA_DATE_UID = "dateDataHtype"


@dataclass(init=True, repr=True, eq=True)
class DataHtype(HXLBaseInformation):
    name: str = None
    # dataType: str = None
    # encryptionType: Type[EncryptionHtype] = None  # HXLBaseInformation
    level: Type[LevelHtype] = None
    # sensitiveType: Type[SensitiveHtype] = None  # HXLBaseInformation
    storage: Type[StorageHtype] = None
    usage: Type[UsageHtype] = None
    weight: Type[WeightHtype] = None
    value: Any = None


class textDataHtype(DataHtype):
    def __post_init__(self):
        self.dataType = HXL_HTYPE_DATA_TEXT_UID


class numberDataHtype(DataHtype):
    def __post_init__(self):
        self.dataType = HXL_HTYPE_DATA_NUMBER_UID


class urlDataHtype(DataHtype):
    def __post_init__(self):
        self.dataType = HXL_HTYPE_DATA_URL_UID


class emailDataHtype(DataHtype):
    def __post_init__(self):
        self.dataType = HXL_HTYPE_DATA_EMAIL_UID


class phoneDataHtype(DataHtype):
    def __post_init__(self):
        self.dataType = HXL_HTYPE_DATA_PHONE_UID


class dateDataHtype(DataHtype):
    def __post_init__(self):
        self.dataType = HXL_HTYPE_DATA_DATE_UID
