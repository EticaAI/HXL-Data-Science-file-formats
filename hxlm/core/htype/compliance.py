# LicenseHtype & CopyrightLicenseHtype
# @see https://spdx.org/licenses/
# @see https://en.wikipedia.org/wiki/Humanitarian_use_licenses

from dataclasses import dataclass


# import hxlm.core.constant
from hxlm.core.constant import (
    HDSL3
)

from typing import (
    # Any,
    List,
    Type
)

# TODO: implement some functionality around SPDX,
#       see https://spdx.org/licenses/ (fititnt, 2031-02-26 10:48 UTC)
# TODO: also implement ways to define MORE than one license (both AND and OR)
#       since SPDX actually allow this  (fititnt, 2031-02-26 10:50 UTC)


@dataclass(init=True, eq=True)
class BaseComplianceHtype:
    """Most Generic ComplianceHtype. Mostly for compabitility.

    TODO: maybe define this as abstract or something, so do not allow be used
          directly.
    """
    todo: str = None


@dataclass(init=True, eq=True)
class BaseRuleComplianceHtype:
    """Most Generic individual rule for ComplianceHtype.
    """
    todo: str = None


class RuleComplianceHtype(BaseRuleComplianceHtype):
    """An individual rule to test compliance
    """
    todo: str = None


class ComplianceHtype(BaseComplianceHtype):
    """Group of rules to test against an HConteiner.
    The general idea is for each kind of abstraction an hxlm information have
    implementors could apply some rules.

    How they are enforced or tested is out of scope of the core library.
    """
    #: computation_stage is (...)
    computation_stage: int = -1

    # While define as global default High Sensitivity HDSL3 (on an scale
    # from 1 to 4) may be too optionated, something have to be defined.
    allowed_sensitive_max: str = HDSL3
    # allowed_sensitive_min =  # Do not seems necessary.
    allowed_sensitive_unknow: str = True

    rules: List[Type[RuleComplianceHtype]]
    # rules: List[Type[BaseRuleComplianceHtype]]
