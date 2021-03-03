"""hxlm is (TODO: document)
"""

__version__="0.7.3"

import os

HXLM_CORE_BASE = os.path.dirname(os.path.realpath(__file__))

import hxlm.core.constant
import hxlm.core.exception
import hxlm.core.model

# Users need to explicitly call this
import hxlm.core.compliance
