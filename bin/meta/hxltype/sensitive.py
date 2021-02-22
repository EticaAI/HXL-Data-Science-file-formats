# SensitiveHXLtype
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
# TODO: create an entry on the spreadsheet

#### HXL Standard & other discussions related to sensitiveHType
# - About the '+sensitive'
#   - https://groups.google.com/g/hxlproject/c/N-606LwRz80/m/Q7dq88YzBAAJ

#### Links (need organization)
# - https://humanitarian.atlassian.net/wiki/spaces/HDXKB/pages/2132148234/Data+Loss+Prevention+on+HDX
# - https://cloud.google.com/dlp/docs/infotypes-reference

from dataclasses import dataclass

from typing import (
    Any
)

@dataclass(init=True, repr=True, eq=True)
class SensitiveHXLtype:
    code: str = None
