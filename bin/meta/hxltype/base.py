# *HXLtype
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# @see https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1066910203    # noqa

from dataclasses import dataclass

# https://github.com/pandas-dev/pandas/blob/master/pandas/core/dtypes/dtypes.py
from typing import (
    Any,
    Type
)

from hxltype.encryption import EncryptionHtype
from hxltype.sensitive import SensitiveHtype


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
    encryptionType: Type[EncryptionHtype] = None
    sensitiveType: Type[SensitiveHtype] = None

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
#  - https://github.com/astropenguin/xarray-dataclasses/blob/master/xarray_dataclasses/methods.py    # noqa
#  - http://xarray.pydata.org/en/stable/io.html#io
#  - https://xarray-extras.readthedocs.io/en/latest/api/csv.html
#  - https://distributed.dask.org/en/latest/
#  - https://distributed.dask.org/en/latest/quickstart.html
