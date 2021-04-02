"""hxlm_minimam.lang

This file, originally written in python (and in a simplified way, to help code
transpilers) contains some very simple functions of internal parts of HXLm,
especially HXLm.HDP. _Maybe_, if eventually useful, some subset using
HXLm.Lisp could be ported, so even end users browsers could manipulate data.

>> hxlm_minimam.py

See https://github.com/EticaAI/HXL-Data-Science-file-formats
    /blob/main/hxlm/ontologia/python/hxlm_minimam.py

>> hxlm_minimam.js

The JavaScript output, using https://github.com/metapensiero/metapensiero.pj:

    pj --output hxlm/ontologia/javascript hxlm/ontologia/python/

Note: metapensiero.pj actually have _more_ features than what is used.

License: Public Domain
"""

# pylint disable=W

# def factum_to_sexpr(factum: Factum) -> str:

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


def _sv(key, mkg=None):
    """An poor human gettext, get the key if value match

    Args:
        key ([str]): Key term. If MKG is none, will return this
        mkg ([dict], optional): An dict to search by falues. Defaults to None.

    Returns:
        [str]: The result
    """

    # TODO: implement by value
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


def hxlm_factum_to_object(factum) -> dict:
    """Factum to an object"""
    # return dict(factum) # this does not transpile well...
    return factum


def hxlm_sespr_to_object(sexpr: str, **kwargs) -> dict:
    """S-expression to object

    TODO: this function _actually_ requires build an minimal lisp parser. So
          this for now is just an draft (Emerson Rocha, 2021-04-01 23:32 UTC)

    Args:
        sexpr (str): The S-expression

    Returns:
        dict: The AST-like object

>>> s1 = '(vkg.attr.factum (vkg.attr.descriptionem "Exemplum"))'
>>> hxlm_sespr_to_object(s1)
['(vkg.attr.factum', '(vkg.attr.descriptionem', '"Exemplum"))']
    """
    _MKG = None
    if 'MKG' in kwargs:
        _MKG = kwargs['MKG']

    # This is a draft
    resultatum = sexpr.split(' ')
    return resultatum
