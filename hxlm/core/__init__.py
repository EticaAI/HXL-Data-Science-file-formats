"""hxlm.core is (TODO: decide what hxlm.core is)


Notes: if you are reading the source code, when you find these '>>>' this is
Python doctest (https://docs.python.org/3/library/doctest.html) and are tested
when the code is deployed (so are somewhat granted that are valid). If
downloading from the GitHub, this is the command to run all the tests:
    pytest -vv hxlm/ --doctest-modules

Examples:

    >>> import hxlm.core as HXLm
    >>> UDUR_LAT = HXLm.util.load_file(HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml')
    >>> HXLm.HDP.util.common.get_language_from_hdp_raw(UDUR_LAT[0])['iso3693']
    'LAT'
    >>> UDUR_LAT2RUS = HXLm.HDP.util.common.transpose_hsilo(
    ...    UDUR_LAT, 'RUS-Cyrl')
    >>> UDUR_LAT2RUS[0]['силосная']['тег']
    ['udhr']
    >>> UDUR_LAT2RUS2POR = HXLm.HDP.util.common.transpose_hsilo(
    ...    UDUR_LAT2RUS, 'POR', 'RUS'
    ... )
    >>> UDUR_LAT2RUS2POR[0]['silo']['etiqueta']
    ['udhr']
"""

# import os

import hxlm.core.constant as C  # noqa: F401
import hxlm.core.exception  # noqa: F401
import hxlm.core.model  # noqa: F401

# Users need to explicitly call this
# import hxlm.core.compliance

__version__ = "v0.8.7.3"

# To simplify documentation, we're always load this constant when end users do
#    import hxlm as HXLm
from hxlm.core.constant import (  # noqa: F401
    HDATUM_EXEMPLUM,
    HDATUM_HXL,
    HDATUM_UDHR
)

import hxlm.core.localization as L10N  # noqa: F401
import hxlm.core.util as util  # noqa: F401

import hxlm.ontologia.python as Ontologia  # noqa: F401

import hxlm.core.hdp as HDP  # noqa: F401
import hxlm.core._dt as _DT  # noqa: F401
