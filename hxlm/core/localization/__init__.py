"""hxlm.core.localization contain localization (L10N) modules

TODO: check these references
  - https://github.com/unicode-org/cldr


Examples:
-----------------

>>> import hxlm.core as HXLm
>>> urhd_lat = HXLm.util.load_file(HXLm.HDATUM_UDUR + '/udhr.lat.hdp.yml')
>>> HXLm.L10N.get_language_from_hdp_raw(urhd_lat[0])['iso3693']
'LAT'
"""

from hxlm.core.localization.util import *  # noqa
from hxlm.core.localization.hdp import *  # noqa

# import hxlm.core as HXLm
