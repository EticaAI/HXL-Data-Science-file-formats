"""hxlm.core.hdp.util.debug

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# Vocabularies:
# - "explanare":
#   - explano: https://en.wiktionary.org/wiki/explano#Latin
#   - explanare: https://en.wiktionary.org/wiki/explanare#Latin
# - "optionem":
#   - https://en.wiktionary.org/wiki/optio#Latin

from typing import (
    Any,
    List,
    Union
)

# from hxlm.ontologia.python.hdp.abst import (
#     AbstAux,
#     AbstRadix
# )

HXLM_MKG = {
    'ENG': {
        'vkg.attr.factum': 'Fact',
        'vkg.attr.descriptionem': 'Description',
        'vkg.attr.fontem': 'Source',
        'vkg.attr.datum': 'Data'
    },
    'LAT': {
        'vkg.attr.factum': 'Factum',
        'vkg.attr.descriptionem': 'Descriptionem',
        'vkg.attr.fontem': 'Fontem',
        'vkg.attr.datum': 'Datum'
    },
}
"""Minimal Knowledge Graph.
TODO: This should be get from JSON or something
"""


def _s(key, mkg=None):
    """An poor human gettext, by key

    Args:
        key ([str]): Key term. If MKG is none, will return this
        mkg ([dict], optional): An dict to search by falues. Defaults to None.

    Returns:
        [str]: The result
    """
    if mkg:
        if key in mkg:
            return mkg[key]
    return key


def hxlm_factum_to_sexpr(factum, **kwargs) -> str:
    """Convert Factum object to S-expression string

    Args:
        factum ([Factum]): An Factum object

    Returns:
        [str]: An S-expression string

>>> f1_simple = {'descriptionem': 'Exemplum'}
>>> f1_lang = {'descriptionem': 'Example', 'linguam': 'ENG', 'datum': [1, 2]}
>>> hxlm_factum_to_sexpr(f1_simple)
'(vkg.attr.factum (vkg.attr.descriptionem "Exemplum"))'
>>> hxlm_factum_to_sexpr(f1_lang, MKG=HXLM_MKG['ENG'])      # With Python
'(Fact (Description (ENG "Example"))(Data "[1, 2]"))'
>>> # hxlm_factum_to_sexpr(f1_lang, {MKG: HXLM_MKG['ENG']}) # With JavaScript
    """
    _MKG = None
    if 'MKG' in kwargs:
        _MKG = kwargs['MKG']

    resultatum = '(' + _s('vkg.attr.factum', _MKG) + ' '

    if 'linguam' in factum and 'descriptionem' in factum:
        resultatum += '(' + _s('vkg.attr.descriptionem', _MKG) + ' (' + \
            factum['linguam'] + ' "' + factum['descriptionem'] + '"))'
    elif 'descriptionem' in factum:
        # resultatum += '(vkg.attr.descriptionem "' + \
        resultatum += '(' + _s('vkg.attr.descriptionem', _MKG) + ' "' + \
            factum['descriptionem'] + '")'

    if 'fontem' in factum:
        resultatum += '(' + _s('vkg.attr.fontem', _MKG) + \
            ' "' + str(factum['fontem']) + '")'

    if 'datum' in factum:
        resultatum += '(' + _s('vkg.attr.datum', _MKG) + \
            ' "' + str(factum['datum']) + '")'

    resultatum += ")"

    return resultatum


def explanare_errorem(res: Any) -> Union[List[str], bool]:
    """Explain an error of a thing (if there is one). True means no error.

    Trivia:
    - errōrem: https://en.wiktionary.org/wiki/error#Latin

    Args:
        thing (Any): Anything that can be converted to str

    Returns:
        Union[List[str], bool]: Returns False not very specific type of object.
                    True If this object does not seems to have information
                    about errors, and a list of strings or Factum objects
                    if do exist errors
    """

    if res is None or res == '' or len(res) == 0:
        return False

    # if 'okay' not in res or 'librum' not in res:
    if 'okay' not in res or 'librum' not in res:
        # print('Unknow object type')
        return False

    # if not isinstance(thing, dict) and \
    #     not isinstance(thing, AbstAux) and \
    #         not isinstance(thing, AbstRadix):
    #     return str(thing)

    if res.okay is True:
        # thing not marked with error.
        return True

    if 'librum' not in res or len(res['librum']) == 0:
        return ['Unknow error']
    return str(res)


def explanare_optionem(thing: Any) -> str:
    """Output debug information from data structures used on HDP containers

    Args:
        thing (Any): Anything that can be converted to str

    Returns:
        str: String
    """
    return str(thing)
