"""hxlm.core is (TODO: document)
"""

# import os

import hxlm.core.constant as C # noqa: F401
import hxlm.core.exception  # noqa: F401
import hxlm.core.model  # noqa: F401

# Users need to explicitly call this
# import hxlm.core.compliance

__version__ = "0.8.2"

# To simplify documentation, we're always load this constant when end users do
#    import hxlm as HXLm
from hxlm.core.constant import (
    HDATUM_UDUR
)

# HXLM_CORE_BASE = os.path.dirname(os.path.realpath(__file__))
# HXLM_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# HDATUM_UDUR = HXLM_ROOT + '/data/udhr'
# HONTOLOGIA_LKG = HXLM_ROOT + '/ontology/core.lkg.yml'
# HONTOLOGIA_VKG = HXLM_ROOT + '/ontology/core.vkg.yml'

# https://en.wikipedia.org/wiki/Jacob_Lorhard
# 'He uses "Ontologia" synonymously with "Metaphysica".'
