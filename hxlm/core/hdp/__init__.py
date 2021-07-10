"""hxlm.core.hdp

This module provide some aliases for HDP functionality

Examples (pytest -vv hxlm/ --doctest-modules)

>>> import hxlm.core as HXLm
>>> file_path = HXLm.HDATUM_UDHR + '/udhr.lat.hdp.yml'
>>> hsilo_example = HXLm.HDP.load(file_path)
>>> hsilo_example[0]['hsilo']['tag']
['udhr']

Now, without explicitly label the file:
>>> import hxlm.core as HXLm
>>> dir_path = HXLm.HDATUM_UDHR
>>> hsilo_example2 = HXLm.HDP.load(file_path)
>>> hsilo_example2[0]['hsilo']['tag']
['udhr']


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

__all__ = [
    'get_language_identifiers',
    'get_metadata',
    'transpose'
]

import hxlm.core.hdp.exception  # noqa

from hxlm.core.hdp.project import (  # noqa
    project
)

from hxlm.core.hdp.util.common import (  # noqa
    get_language_identifiers,
    get_metadata,
    hashable,
    load,
    transpose
)

from hxlm.core.util import (  # noqa
    to_yaml
)
