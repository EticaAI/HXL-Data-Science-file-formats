"""hxlm.core.hdp.exception

See:
  - https://docs.python.org/3/tutorial/errors.html
  - https://docs.python.org/3/library/exceptions.html

https://en.wiktionary.org/wiki/exceptio#Latin

>>> raise HDPExceptionem('Exemplum')
Traceback (most recent call last):
...
core.hdp.exception.HDPExceptionem: [vkg.attr.descriptionem: Exemplum]

##> raise HDPExceptionem('Exemplum', 'hxlm.core.hdp.hazmat.policy', {'a': 'b'})

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# TODO: Consider implementing VKG (localized messages) even for exceptions.
#       The _get_l10n_term have a rudimentar draft for this.
#       (Emerson Rocha, 2021-03-21 10:13 UTC)


def _get_l10n_term(term: str) -> str:
    """TODO: get_l10n_term"""
    return term


class HDPExceptionem(Exception):
    """Base class for other HDPExceptionem"""

    def __init__(self, descriptionem, fontem=None, datum=None):
        # Exception.__init__(self, message)
        # super(HDPException, self).__init__(message)
        super().__init__()
        self.descriptionem = descriptionem
        self.fontem = fontem
        self.datum = datum

    def __str__(self):
        result = '[' + _get_l10n_term('vkg.attr.descriptionem') + \
            ': ' + self.descriptionem + ']'
        # result = str(self.descriptionem)
        if self.fontem is not None:
            result = result + '[' + _get_l10n_term('vkg.attr.fontem') + \
                ': ' + str(self.fontem) + ']'

        if self.datum is not None:
            result = result + '[' + _get_l10n_term('vkg.attr.datum') + \
                ': ' + str(self.datum) + ']'

        return result


# # hcompliance is not an good Latin reference term. Eventually will be changed
# class HcomplianceHDPExceptionem(HDPExceptionem):
#     """Okay Exception ('not okay') related to L10N (localization)"""


# class L10nOkayHDPExceptionem(HDPExceptionem):
#     """Okay Exception ('not okay') related to L10N (localization)"""
