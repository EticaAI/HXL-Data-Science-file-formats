# LicenseHtype & CopyrightLicenseHtype
# @see https://spdx.org/licenses/
# @see https://en.wikipedia.org/wiki/Humanitarian_use_licenses

from dataclasses import dataclass

from typing import (
    Any
)

# TODO: implement some functionality around SPDX,
#       see https://spdx.org/licenses/ (fititnt, 2031-02-26 10:48 UTC)
# TODO: also implement ways to define MORE than one license (both AND and OR)
#       since SPDX actually allow this  (fititnt, 2031-02-26 10:50 UTC)

@dataclass(init=True, repr=True, eq=True)
class LicenseHtype:
    comment: str = None
    # Note: ideally we should implement some abstraction, so even if user
    # does not use exactly what we want, we could still try to make inference
    spdx_identifier: str = None
    is_humanitarian_use: bool = True


@dataclass(init=True, repr=True, eq=True)
class CopyrightHtype:
    comment: str = None
    author: str = None  # And if is an list?
    # Copyright actually would need more than this