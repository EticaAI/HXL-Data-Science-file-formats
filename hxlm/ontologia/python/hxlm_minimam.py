"""hxlm_minimam.lang
License: Public Domain"""

# pj --output hxlm/ontologia/javascript hxlm/ontologia/python/

# from hxlm.ontologia.python.commune import (
#     Factum
# )

# def factum_to_sexpr(factum: Factum) -> str:
def factum_to_sexpr(factum):
    """Convert Factum object to S-expression string

    Args:
        factum ([Factum]): An Factum object

    Returns:
        [str]: An S-expression string
    """
    if 'linguam' in factum:
        desc = '(' + factum.linguam + ' "' + factum.descriptionem + '")'
    else:
        desc = '"' + factum.descriptionem + '"'

    resultatum = "(vkg.attr.factum "
    resultatum += '(vkg.attr.descriptionem ' + desc + ')'

    if 'fontem' in factum:
        resultatum += '(vkg.attr.fontem "' + str(factum.fontem) + '")'

    if 'datum' in factum:
        resultatum += '(vkg.attr.datum "' + str(factum.datum) + '")'

    resultatum += ")"

    return resultatum
