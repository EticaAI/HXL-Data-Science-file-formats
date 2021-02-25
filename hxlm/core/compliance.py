"""Core facade to policy, standard or law compliance-like methods

TL;DR: check if user is authorized to do something based on context and then
       take an decision (from just remove the sensitive content to raise
       warnings)

While most automated tools that do compliance checks tend to be about
technical standards or conventions on files ("does this file have this
attribute?" "Does this field is the right date type?")" the main goal of
this module is focused on more police/law for common tasks related to
process the data.

Please note that do exist limitations on automated checks:
- The quality of the checks are based on how the input data was HXLated
- The number of false positives is likely to be high even if you use rules
  from one domain (like education) for people who work on healthcare.
- Consider implement additional features, like require user credentials, or
  maybe allow reduce severity based on infrastruture (like if be aware that
  someone granted that the data would be deleted).

Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


def check_compliance_init(Tolerance, **kwargs):
    """Check compliance with policy/law/standard at initialization 

    Args:
        Tolerance ([Number]): [description]

    Returns:
        [Bool]: When tolerance level accepts, return True/False instead of
                trow exception.
    """

    # TODO: implement plugin-like feature, while use this as facade
    return True



