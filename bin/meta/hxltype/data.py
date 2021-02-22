# DataHXLtype
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=717813523

### libhxl-python Datatypes (we must be fully compatible/extend these)
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/datatypes.py
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/model.py
#  - github.com/HXLStandard/libhxl-python/blob/master/hxl/validation.py
### numpy
#  - https://numpy.org/devdocs/user/basics.types.html
#  - https://numpy.org/devdocs/reference/arrays.dtypes.html#arrays-dtypes
#  - https://numpy.org/devdocs/reference/typing.html#module-numpy.typing
### pandas
#  - https://github.com/pandas-dev/pandas/tree/master/pandas/core/dtypes
#  - https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes/dtypes.py
###
# - attrs
#   - https://www.attrs.org/en/stable/

# Temp references
# - https://docs.python.org/3/library/typing.html
# - https://docs.python.org/3/library/typing.html
# - https://docs.python.org/3/library/dataclasses.html
# - https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes
# - https://www.programiz.com/python-programming/multiple-inheritance
# - https://medium.com/@jacktator/dataclass-vs-namedtuple-vs-object-for-performance-optimization-in-python-691e234253b9

from dataclasses import dataclass


@dataclass()
class DataHXLt:
    name: str
    lon: float
    lat: float

@dataclass()
class DataHXLt2:
    name: str
    lon: float
    lat: float
