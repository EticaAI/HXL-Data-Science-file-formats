#!/usr/bin/env python3

# ./tests/hxlm-manual-tests.py

import hxlm.core
import hxlm.core.util
# from hxlm.core.htype.encryption import EncryptionHtype
# from hxlm.core.htype.sensitive import SensitiveHtype

hdata = hxlm.core.base.HConteiner()

print(hdata)
# mdataset.encryption = "abc"
hdata.sensitive = hxlm.core.constant.HDSL1
print(hdata.describe())

hxlm.core.util.debug()