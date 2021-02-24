"""hxlm.core.utils provive quick utilitaries for common tasks
"""

from hxlm.core.constant import HTYPE_TRUE, HTYPE_FALSE, HTYPE_UNKNOW
from hxlm.core.constant import (
    HSLVU,
    HSLV_DEFAULT
)
from hxlm.core.internal.util import _get_plugins

import hxl


def cmp_sensitive_level(level, reference_level=None):
    """Compare a sensitive level with an reference.
    less or equal to zero: Good
    greater than zero: this is more sensitive, Bad
    ?: your level or the reference_level is HTYPE_UNKNOW

    Examples:
        cmp_sensitive_level('HSLV1', 'HSLVU') -> ?
        cmp_sensitive_level('HSLV1', 'HSLV1') -> 0
        cmp_sensitive_level('HSLV4', 'HSLV1') -> 3
        cmp_sensitive_level('HSLV1', 'HSLV4')) -> -3

    Args:
        level ([type]): Current sensitive level to compare
        reference_level ([type], optional): reference. Defaults to None.

    Returns:
        Union[int, float]: Numeric result
    """
    if level == HSLVU or reference_level == HSLVU:
        return HTYPE_UNKNOW
    if reference_level is None:
        reference_level = HSLV_DEFAULT

    return int(level[-1]) - int(reference_level[-1])


def debug():
    _get_plugins()


def hxl_info(data):
    """The df.info, but for HXLated object

    TODO: maybe remove this and just document

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
