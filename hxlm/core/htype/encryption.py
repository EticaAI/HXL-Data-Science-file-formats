"""hxlm.core.htype.encryption
- @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
TODO: create an entry on the spreadsheet
"""


from dataclasses import dataclass

# from typing import (
#     Any
# )


@dataclass(init=True, repr=True, eq=True)
class EncryptionHtype:
    """EncryptionHtype is the generic class for encryption of an data point.
    """
    code: str = None
