"""GenericSpecializationHtype
"""
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# TODO: create an entry on the spreadsheet

from dataclasses import dataclass

# from typing import (
#     Any
# )


@dataclass(init=True, repr=True, eq=True)
class GenericSpecializationHtype:
    """
    Note: HXL data points does not need to enforce any specialization. This
    Class can be used to 'reset' other specializations.
    """
    specialization: str = None

# TODO: create an somewhat generic class for something that represents
#       an place (#loc, #country, #adm1-#adm5, +lat, +lon, etc)
#       @see https://www.humanitarianresponse.info/en/applications/tools
#            /toolbox-item/implementing-p-codes
#       @see https://www.humanitarianresponse.info/en/operations/stima
#            /document/pcode-matching-tool-excel-add
#       (fititnt, 2021-02-22 18:35 UTC)
