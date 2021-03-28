"""hxlm.core.io.hxl is an syntatic sugar for the fantastic libhxl-python

This file at the moment is an draft. But is on IO submodule because libhxl
package from the HXLStandard already is able to work to manipulate files from
remote sources. It _only_ does not write on remote sources alone.

See:
- https://github.com/HXLStandard/libhxl-python

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


# NOTE: the is_hxl_file, in special if is remote files, is likely to reeealy
#       need some work around the hxlm.core.io.cache before we make it too
#       easy for users. Also the is_hxl_file itself should be somewhat
#       equivalent to an HTTP HEAD request (aka we do not load too much
#       data)
def is_hxl_file():
    """TODO: is_hxl_file is an draft. """
