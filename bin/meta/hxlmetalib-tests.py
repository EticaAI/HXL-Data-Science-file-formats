#!/usr/bin/env python3
# This is just a quick test. Can be ignored (fititnt, 2021-02-22 02:19 UTC)

import sys

import hxltype.base
import hxltype.data
import hxltype.level
import hxltype.storage
import hxltype.usage
import hxltype.weight

hxltype.base.test()

v1 = hxltype.data.DataHXLt(1, 1, 1)
v2 = hxltype.data.DataHXLt2(1, 1, 1)

print('sys.getsizeof', sys.getsizeof(v1))
print('sys.getsizeof2', sys.getsizeof(v2))

var1 = hxltype.data.DataHXLt(1, 1, 1)
print('sys.getsizeofvar1', sys.getsizeof(var1))
print(var1)