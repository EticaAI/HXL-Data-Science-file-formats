"""
hxl.core.base is (...)
TODO: document like
        - google.github.io/styleguide/pyguide.html
        - sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
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

from hxlm.core.htype.encryption import EncryptionHtype
from hxlm.core.htype.sensitive import SensitiveHtype


class HConteiner:
    """HConteiner is, informally speaking, a conteiner of one or more HDatasets

    It is an analogy for a compressed folder of CSVs, Excel Workbook, HDF5
    file, NetCDF file or an CKan Dataset.

    While most of the time data manipulation is done using HDataset the
    HConteiner can play a hole when have to load group of datasets or save
    then in same file format.

    TODO: is 'HConteiner' an resonable naming? The idea was something that
          could
    """

    def __init__(self, encryption: Type[EncryptionHtype] = None,
                 sensitive: Type[SensitiveHtype] = None):
        self._encryption = encryption
        self._sensitive = sensitive


class HDataset:
    """HDataset is, informally speaking, a dataset 

    It is an analogy for a single CSV file, Excel worksheet, or an Pandas
    NDframe (actually, more similar to xarray).

    @see NDFrame https://github.com/pandas-dev/pandas/blob/master/pandas
                 /core/generic.py#L191

    TODO: both Excel, CKan and formats like HDF5 work with MULDIPLE datasets.
          so, which structure use for this? (E.Rocha, 2021-02-26 08:10 UTC)
    """

    def __init__(self, encryption: Type[EncryptionHtype] = None,
                 sensitive: Type[SensitiveHtype] = None):
        self._encryption = encryption
        self._sensitive = sensitive

    def describe(self):
        mdataset_description = {
            'kind': "MDataset",
            'encryption': self._encryption,
            'sensitive': self._sensitive,
        }
        return mdataset_description

    @property
    def encryption(self):
        return self._encryption

    @encryption.setter
    def encryption(self, value):
        if isinstance(value, EncryptionHtype):
            self._encryption = value
        else:
            self._encryption = EncryptionHtype(code=value)

    # @encryption.deleter
    # def encryption(self):
    #     del self._encryption

    @property
    def sensitive(self):
        return self._sensitive

    @sensitive.setter
    def sensitive(self, value):
        if isinstance(value, SensitiveHtype):
            self._sensitive = value
        else:
            self._sensitive = SensitiveHtype(code=value)


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
