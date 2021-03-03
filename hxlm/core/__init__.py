"""hxlm.core is (TODO: document)
"""

import os

import hxlm.core.constant  # noqa: F401
import hxlm.core.exception  # noqa: F401
import hxlm.core.model  # noqa: F401

# Users need to explicitly call this
# import hxlm.core.compliance

__version__ = "0.7.3"
HXLM_CORE_BASE = os.path.dirname(os.path.realpath(__file__))
