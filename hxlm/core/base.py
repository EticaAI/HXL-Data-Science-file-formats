"""
hxl.core.base is (...)
"""

# TODO: use Numpy conventions about documentation
#       https://numpydoc.readthedocs.io/en/latest/format.html

# *HXLtype
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d
#      /1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1066910203

from dataclasses import dataclass

# https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes/dtypes.py
from typing import (
    Any,
    Type
)

from .htype.encryption import EncryptionHtype
from .htype.sensitive import SensitiveHtype

# ### True, False, Missing, Unknow, Encrypted, START _________________________
# Even without controlled vocabularies (like +v_un_bool with 6 official UN
# languages, and +v_eu_bool with 23+ working languages of EU, we still need
# some way that would allow have both internal representations and exchange
# data with de facto industry tools (like ISOs, database systems terms for
# true/false, etc)
HXL_COREHTYPE_TRUE_PYTHON = True      # 'HT1' ?
HXL_COREHTYPE_FALSE_PYTHON = False    # 'HT0' ?
# NOTE: while most database systems treat missing and unknow as Null, it's
# actually very important the distinction for data mining and data analysis
HXL_COREHTYPE_MISSING_PYTHON = ""     # 'HT ' ?
HXL_COREHTYPE_UNKNOW_PYTHON = "?"     # 'HT?' ?

# NOTE: Encryption is likely to be a very, VERY common case on HXLated datasets
#       both at column and row level (Think Encryption At Rest) ant this
#       actually must be well done, since just encrypt/protect the full dataset
#       limit valid cases. The difference betwen this and MISSING/UNKNOW
#       is user tools actually have partial information to decrypt.
# NOTE: One original data point that is decrypted by the user is converted
#       to whatever was the original value instead of this. This can be used
#       on much more than just boolean.
HXL_COREHTYPE_ENCRYPTED_PYTHON = "E"  # 'HTE' ?

# TODO: this is draft
HXL_COREHTYPE_TRUE_STRING = ""
HXL_COREHTYPE_TRUE_STRING_LIST = []
HXL_COREHTYPE_FALSE_STRING = ""
HXL_COREHTYPE_FALSE_STRING_LIST = []
# ### True, False, Missing, Unknow, Encrypted, START _________________________

@dataclass(init=True)
class HXLBaseInformation:
    """
    HXLBaseInformation (temporary name; temporary file) is base class for
    almost anything that could have some information. From very specific cell
    value to the entire dataset.

    Since is too generic, only Sensitive and Encryption (because is possible
    to encrypt entire file) are here. Also both values override the entire
    dataset.

    See also hxltype.data.DataHtype

    TODO: HXLBaseInformation is both temporary name and file. Solve this.
    """
    encryption: Type[EncryptionHtype] = None
    sensitive: Type[SensitiveHtype] = None


@dataclass(init=True, repr=True, eq=True)
class HXLRow(HXLBaseInformation):
    """
    'Article 7: All are equal before the law and are entitled without any
    discrimination to equal protection of the law. All are entitled to equal
    protection against any discrimination in violation of this Declaration and
    against any incitement to such discrimination.' -- Universal Declaration
    of Human Rights.

    HXLRow can be used to manipulate what HXL may call a 'row' or 'line', and
    statistical programs may call 'observation' or 'record'. In practice
    to reflect real world usage it means that while an entire HXL dataset
    may have one level of sentivity and encryption state, and columns (or
    variables, like as a person with a disease) may have more strict
    requeriments, there are cases where what this class represents needs to
    be treated in an even more special way. And this often varies across
    countries/territories.

    Being more specific, HXLRow could represent, for example, an individual
    like an unknown person (who could be targeted because of private
    information) to you or even a chief of state. Different from average
    database systems where row-level encryption is unworkable and
    data science files formats, HXL could treat different also at HXLRow.
    If the software you need to use the data does not support HXL, you can
    simply export the data without including (or converting these data)
    and still be able to comply with local laws

    """
    kind: str = "HXLRow"

# ### Ignore after here ______________________________________________________

# Projects to test
#  - https://github.com/pydata/xarray
#  - https://github.com/man-group/dtale


# Quick links to see (delete later)
#
# xarrays/dask
#  - http://xarray.pydata.org/en/stable/faq.html#approach-to-metadata
#  - http://xarray.pydata.org/en/stable/related-projects.html#related-projects
#  - http://xarray.pydata.org/en/stable/data-structures.html
#  - http://xarray.pydata.org/en/stable/generated/xarray.DataArray.astype.html
#  - https://docs.python.org/3/library/dataclasses.html
#  - https://github.com/astropenguin/xarray-dataclasses/blob/master
#    /xarray_dataclasses/methods.py
#  - http://xarray.pydata.org/en/stable/io.html#io
#  - https://xarray-extras.readthedocs.io/en/latest/api/csv.html
#  - https://distributed.dask.org/en/latest/
#  - https://distributed.dask.org/en/latest/quickstart.html
