# DataHXLtype
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=717813523  # noqa

# ## libhxl-python Datatypes (we must be fully compatible/extend these)
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/datatypes.py
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/model.py
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/validation.py
#  - https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=1881622062  # noqa
# ## numpy
#  - https://numpy.org/devdocs/user/basics.types.html
#  - https://numpy.org/devdocs/reference/arrays.dtypes.html#arrays-dtypes
#  - https://numpy.org/devdocs/reference/typing.html#module-numpy.typing
# ## pandas
#  - https://github.com/pandas-dev/pandas/tree/master/pandas/core/dtypes
#  - https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes/dtypes.py  # noqa
# ##
# - attrs
#   - https://www.attrs.org/en/stable/

# Temp references
# - https://docs.python.org/3/library/typing.html
# - https://docs.python.org/3/library/typing.html
# - https://docs.python.org/3/library/dataclasses.html
# - https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes  # noqa
# - https://www.programiz.com/python-programming/multiple-inheritance
# - https://medium.com/@jacktator/dataclass-vs-namedtuple-vs-object-for-performance-optimization-in-python-691e234253b9  # noqa
# - https://stackoverflow.com/questions/50180735/how-can-dataclasses-be-made-to-work-better-with-slots  # noqa

from dataclasses import dataclass

from hxlm.core.base import HXLBaseInformation
from hxltype.encryption import EncryptionHtype
from hxltype.level import LevelHtype
from hxltype.sensitive import SensitiveHtype
from hxltype.storage import StorageHtype
from hxltype.usage import UsageHtype
from hxltype.weight import WeightHtype

# https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes/dtypes.py
from typing import (
    Any,
    Type
)

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
    levelType: Type[LevelHtype] = None
    # sensitiveType: Type[SensitiveHtype] = None  # HXLBaseInformation
    storageType: Type[StorageHtype] = None
    usageType: Type[UsageHtype] = None
    weightType: Type[WeightHtype] = None
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
