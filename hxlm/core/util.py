"""hxlm.core.util provive quick utilitaries for common tasks
"""
# from functools import reduce, lru_cache
from functools import reduce
from typing import (
    Any,
    # Union
)

# import json
# import csv
# import yaml


import hxl

from hxlm.core.constant import (
    # HTYPE_TRUE
    # HTYPE_FALSE
    HTYPE_UNKNOW
)

from hxlm.core.constant import (
    HDSLU,
    HDSL_DEFAULT
)


from hxlm.core.internal.util import _get_submodules
from hxlm.core.compliance import verbose_event

from hxlm.core.io.local import (  # noqa
    load_file
)

from hxlm.core.io.converter import (  # noqa
    to_json,
    to_yaml
)

__all__ = [
    'cmp_sensitive_level',
    'debug',
    'get_value_if_key_exists',
    'hxl_info',
    'load_file',  # hxlm.core.io.local
    'to_json',    # hxlm.core.io.converter
    'to_yaml'     # hxlm.core.io.converter
]


def cmp_sensitive_level(level, reference_level=None):
    """Compare a Information sensitivity level with an reference level.

    HXLm + plugins infer the level based on the data itself (not the
    infrastrucure or the human agent.)

    less or equal to zero: Good
    greater than zero: this is more sensitive, Bad
    ?: your level or the reference_level is HTYPE_UNKNOW

    Examples:
        cmp_sensitive_level('HDSL1', 'HDSLU') -> ?
        cmp_sensitive_level('HDSL1', 'HDSL1') -> 0
        cmp_sensitive_level('HDSL4', 'HDSL1') -> 3
        cmp_sensitive_level('HDSL1', 'HDSL4')) -> -3

    Args:
        level ([type]): Current sensitive level to compare
        reference_level ([type], optional): reference. Defaults to None.

    Returns:
        Union[int, float]: Numeric result
    """

    # We tolerate both HDSLU (exact string) or generic HTYPE_UNKNOW (?)
    if (level == HDSLU or reference_level == HDSLU) or \
            (level == HTYPE_UNKNOW or reference_level == HTYPE_UNKNOW):
        return HTYPE_UNKNOW
    if reference_level is None:
        reference_level = HDSL_DEFAULT

    return int(level[-1]) - int(reference_level[-1])


def debug():
    """Debug things"""
    verbose_event()
    _get_submodules()


def get_value_if_key_exists(source: dict,
                            dotted_key: str,
                            default: Any = None) -> Any:
    """Get value of an nesteb object by dotted notation key (if key exist)

    Examples:
        >>> import hxlm.core.util as Cutil
        >>> import hxlm.core.localization.util as Lutil
        >>> hdp_lkg = Lutil.get_localization_knowledge_graph()
        >>> Cutil.get_value_if_key_exists(hdp_lkg, 'linguam23.AR')
        'ARA'

    Args:
        source (dict): An nested object to search
        dotted_key (str): Dotted key notation
        default ([Any], optional): Value if not found. Defaults to None.

    Returns:
        [Any]: Return the result. Defaults to default
    """
    keys = dotted_key.split('.')
    return reduce(
        lambda d, key: d.get(
            key) if d else default, keys, source
    )


def get_object_if_value_eq_on_key(source: list,
                                  key: str,
                                  value: Any) -> dict:
    """For a list of objects, return an dict that match an key value

    Args:
        source (list): a list of objects to search
        key (str): the key to compare an exact value
        value (Any): The value to be compared

    Returns:
        dict: Return the entire dictionary if an key match

    Examples:

    >>> import hxlm.core.util as Cutil
    >>> import hxlm.core.localization.util as Lutil
    >>> hdp_lkg = Lutil.get_localization_knowledge_graph()
    >>> v = Cutil.get_object_if_value_eq_on_key(hdp_lkg['lid'], 'q', 'Q397')
    >>> print(v['iso6391'])
    LA
    >>> print(v['iso3693'])
    LAT
    >>> print(v['macro'])
    False
    """

    for item in source:
        if source[item][key] == value:
            return source[item]

    return None


def get_object_by_value_in_key(source: dict,
                               key: str,
                               value: Any) -> dict:
    """For a list of objects, return an dict that the key have the value on it

    Args:
        source (list): a list of objects to search
        key (str): the key to compare an exact value
        value (Any): The value that need to be inside of an list

    Returns:
        dict: Return the entire dictionary if an value is found on key

    Examples:

    >>> import hxlm.core.util as Cutil
    >>> import hxlm.core.localization.util as Lutil
    >>> hdp_lkg = Lutil.get_localization_knowledge_graph()
    >>> v = Cutil.get_object_by_value_in_key(hdp_lkg['lid'], \
                                             'klid_alts', 'English')
    >>> print(v['klid_alts'])
    ['English']
    >>> print(v['klid'])
    English language
    >>> print(v['iso3693'])
    ENG
    """

    for item in source:
        if source[item][key] is not None and \
                value in source[item][key]:
            return source[item]

    return None


def hxl_info(data):
    """The df.info, but for HXLated object

    TODO: maybe remove this and just document
    TODO: implement compliance.verbose_event() or move logic to
          HContainer/HDataset (Emerson Rocha, 2021-02-02 23:48 UTC)

    @see pandas.pydata.org/pandas-docs/stable/reference/api
         /pandas.DataFrame.info.html
    """
    result = {}
    # result.data = []
    if isinstance(data, hxl.io.HXLReader):
        rows_ = []
        count = -1
        for row in data:
            # rows_.append(row.get_all())
            # print(row)
            # print(row.values)
            # rows_.append(row.dictionary())
            count += 1
            if (count < 10):
                # TODO: idealy, we should get the last itens of table too.
                rows_.append(row.values)

        result['columns'] = data.columns
        result['values_total'] = count
        result['values'] = rows_
        return result

    # Is not hxl.io.HXLReader? Lets just return the data
    print('hxl_info needs undestand what is this. Fix me later.')
    return data


def is_secure():
    raise NotImplementedError("is_secure depends on extra code")


def is_encrypted():
    """(draft) Is the thing encrypted?

    For now we will hardcoded False, since there is no publised code that
    helps to encrypt HXlated datasets... yet (fititnt, 2021-02-24 00:42)

    Returns:
        Bool: If is encrypted
    """
    return False


def is_technically_right():
    raise NotImplementedError("is_technically_right depends on extra code")


def is_morally_right():
    """Is this thing morally right? (please use more specific library)

    hxlm.core.util.is_morally_right is a placeholder funcion. Eventually
    it may work as an alias to an more specific library used.

    Returns:
        HType: True, False, ?
    """
    return HTYPE_UNKNOW


def is_legally_right():
    """Is this thing legally right? (please use more specific library)

    hxlm.core.util.is_legally_right is a placeholder funcion. Eventually
    it may work as an alias to an more specific library used.

    Returns:
        HType: True, False, ?
    """
    return HTYPE_UNKNOW
