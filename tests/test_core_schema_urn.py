#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_core_schema_urn.py
#
# To test directly
#     pytest -vv ./tests/test_core_schema_urn.py

import os

from hxlm.core.constant import (
    HXLM_ROOT
)


from hxlm.core.schema.urn import (
    HURN
)


def test_core_schema_urn_example_valid():
    example1 = 'urn:x-hurn:xz:eticaai:HXL-Data-Science-file-formats'

    resul1 = HURN().is_valid(example1)

    assert resul1 is True


def test_core_schema_urn_example_invalid():
    example1 = 'urn:hurn:xz:eticaai:HXL-Data-Science-file-formats'

    resul1 = HURN().is_valid(example1)

    assert resul1 is False

# test_core_schema_urn_test1()
