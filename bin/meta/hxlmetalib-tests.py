#!/usr/bin/env python3
# This is just a quick test. Can be ignored (fititnt, 2021-02-22 02:19 UTC)

import sys

import hxltype.base
import hxltype.data
import hxltype.level
import hxltype.storage
import hxltype.usage
import hxltype.weight

example_text = hxltype.data.emailDataHtype(value="Lorem ipsum")
print('example_text', example_text.value)
print('sys.getsizeof', sys.getsizeof(example_text))

example_number = hxltype.data.numberDataHtype(value=3.14)
print('example_number', example_number.value)
print('sys.getsizeof', sys.getsizeof(example_number))

example_url = hxltype.data.urlDataHtype(value="https://example.org")
print('example_url', example_url.value)
print('sys.getsizeof', sys.getsizeof(example_url))

example_email = hxltype.data.emailDataHtype(value="https://example.org")
print('example_email', example_email.value)
print('sys.getsizeof', sys.getsizeof(example_email))

example_phone = hxltype.data.phoneDataHtype(value="+55 51 99999-9999")
print('example_phone', example_phone.value)
print('sys.getsizeof', sys.getsizeof(example_phone))
print('sys.getsizeof', sys.getsizeof(example_email))

example_date = hxltype.data.dateDataHtype(value="25/01/1986")
print('example_date', example_date.value)
print('sys.getsizeof', sys.getsizeof(example_date))

#hxltype.base.test()

# v1 = hxltype.data.DataHXLt(1, 1, 1)
# v2 = hxltype.data.DataHXLt2(1, 1, 1)
# v22 = hxltype.data.DataHXLt22(name=1, lat=1, lon=1)

# print('sys.getsizeof', sys.getsizeof(v1))
# print('sys.getsizeof2', sys.getsizeof(v2))
# print('sys.getsizeof22', sys.getsizeof(v22))

# var1 = hxltype.data.DataHXLt(1, 1, 1)
# print('sys.getsizeofvar1', sys.getsizeof(var1))
# print(var1)