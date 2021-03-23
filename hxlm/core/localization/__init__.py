"""hxlm.core.localization contain localization (L10N) modules

TODO: check these references
  - https://github.com/unicode-org/cldr

Example of usage:
---------------

>>> # Note: this usage is a bit too low level, but is used as part of
>>> # testing with command
>>> #    pytest -vv hxlm/ --doctest-modules
>>> #
>>> import hxlm
>>> import hxlm.core.localization as HL10n
>>> from hxlm.core.constant import HDATUM_UDUR
>>> urhd_lat = hxlm.core.util.load_file(HDATUM_UDUR + '/udhr.lat.hdp.yml')
>>> HL10n.get_language_from_hdp_raw(urhd_lat[0])['iso3693']
'LAT'
>>> # urhd_lat_rus = HL10n.transpose_hsilo(urhd_lat, 'RUS-Cyrl')
>>> # This is one way to dump an YAML string
>>> #   hxlm.core.util.to_yaml(urhd_lat)
"""

from hxlm.core.localization.util import *  # noqa
from hxlm.core.localization.hdp import *  # noqa
