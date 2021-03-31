"""hxlm.core.hdp.exception

See:
  - https://docs.python.org/3/tutorial/errors.html
  - https://docs.python.org/3/library/exceptions.html

https://en.wiktionary.org/wiki/exceptio#Latin

>>> raise HDPExceptionem('Exemplum')
Traceback (most recent call last):
...
core.hdp.exception.HDPExceptionem: [vkg.attr.descriptionem: Exemplum]

>>> l10n_descriptionem('Exemplum')
'[vkg.attr.descriptionem: Exemplum]'
>>> l10n_descriptionem('Exemplum', 'examplum.fontem')
'[vkg.attr.descriptionem: Exemplum][vkg.attr.fontem: examplum.fontem]'
>>> l10n_descriptionem('Exemplum', datum=[1, 2, 3])
'[vkg.attr.descriptionem: Exemplum][vkg.attr.datum: [1, 2, 3]]'

##> raise HDPExceptionem('Exemplum', 'hxlm.core.hdp.hazmat.policy', {'a': 'b'})

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

__all__ = ['HDPExceptionem']

# TODO: Consider implementing VKG (localized messages) even for exceptions.
#       The _get_l10n_term have a rudimentar draft for this.
#       (Emerson Rocha, 2021-03-21 10:13 UTC)


def _get_l10n_term(term: str) -> str:
    """get localized term when possible from an predictable string input


    Args:
        term (str): the term, example: vkg.attr.descriptionem

    Returns:
        str: if possible, the term on user language. It will fallback to
                    the term itself
    """

    # TODO: implement the most base capability of load the core VKG. But since
    #       even core VKG could be tottally broken, still return something
    #       (Emerson Rocha, 2021-03-31 11:04 UTC)

    # TODO: in addition to load the core VKG, try to guess user localization.
    #       if the localization is not possible (or is 'too generic', like
    #       English with no vkg.attr.adm0), we still fallback as if was Latin.
    #       (Emerson Rocha, 2021-03-31 11:08 UTC)

    return term


def l10n_descriptionem(descriptionem: str, fontem=None, datum=None) -> str:
    """Localized description from a source, with extra arguments

    Args:
        descriptionem ([type]): The textual description
        fontem ([Any], optional): The source. Defaults to None.
        datum ([Any], optional): Extra information. Defaults to None.

    Returns:
        [str]: An localized description
    """
    l10n_ = '[' + _get_l10n_term('vkg.attr.descriptionem') + \
        ': ' + descriptionem + ']'
    if fontem is not None:
        l10n_ = l10n_ + '[' + _get_l10n_term('vkg.attr.fontem') + \
            ': ' + str(fontem) + ']'

    if datum is not None:
        l10n_ = l10n_ + '[' + _get_l10n_term('vkg.attr.datum') + \
            ': ' + str(datum) + ']'
    return l10n_


class HDPExceptionem(Exception):
    """HDP Exception with L10N features (e.g. try to load user language)

    If want to prepare an message like this, but without raise exception, see
    l10n_descriptionem()
    """

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
