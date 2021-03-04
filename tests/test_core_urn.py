#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_core_urn.py
#
# To test directly
#     pytest -vv ./tests/test_core_urn.py

import os

from hxlm.core.constant import (
    HXLM_ROOT
)


# from hxlm.core.schema.urn import (
#     HURN
# )
from hxlm.core.htype.urn import (
    is_urn,
    URNHtype
)


# def test_core_schema_urn_example_valid():
#     example1 = 'urn:x-hurn:xz:eticaai:HXL-Data-Science-file-formats'

#     resul1 = HURN().is_valid(example1)

#     assert resul1 is True


# def test_core_schema_urn_example_invalid():
#     example1 = 'urn:hurn:xz:eticaai:HXL-Data-Science-file-formats'

#     resul1 = HURN().is_valid(example1)

#     assert resul1 is False


def test_core_htype_urn_is_urn_valid():
    example1='urn:x-hurn:xz:eticaai:HXL-Data-Science-file-formats'
    example2=URNHtype(value = example1)

    resul1=is_urn(example1, 'urn:x-hurn:')
    resul2=is_urn(example2)

    assert resul1 is True
    assert resul2 is True


def test_core_htype_urn_is_urn_invalid():
    example1='urn:hurn:xz:eticaai:HXL-Data-Science-file-formats'
    example2=URNHtype(value = example1)

    print('oooi', example2, example2.is_valid())

    resul1=is_urn(example1, 'urn:x-hurn:')
    resul2=is_urn(example2)

    assert resul1 is False
    assert resul2 is False


test_core_htype_urn_is_urn_invalid()
# test_core_schema_urn_test1()
