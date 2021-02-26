#!/usr/bin/env python3

import hxlm.core.base
from hxlm.core.htype.encryption import EncryptionHtype
from hxlm.core.htype.sensitive import SensitiveHtype

mdataset = hxlm.core.base.MDataset()



print(mdataset)
# mdataset.encryption = "abc"
mdataset.sensitive = "erf"
print(mdataset.describe())