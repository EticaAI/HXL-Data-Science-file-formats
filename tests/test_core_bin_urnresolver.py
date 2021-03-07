#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_core_bin_urnresolver.py
#
# To test directly
#     pytest -vv ./tests/test_core_bin_urnresolver.py

from hxlm.core.schema.urn.util import (
    get_urn_resolver_from_csv,
    get_urn_resolver_from_json,
    get_urn_resolver_from_yml,
    # get_urn_resolver_local,
)
import os
import pathlib
TESTDIR = str(pathlib.Path(__file__).parent.absolute()) + '/urnresolver'
TEST_SIG_A = 'urn:data:xz:hxl:standard:core:hashtag'


def test_core_bin_urnresolver_json():
    result = get_urn_resolver_from_json(TESTDIR + '/json/urn.json')
    print('result', result)
    print('result urnnnn', result[0]['urn'])
    assert result[0]['urn'] == TEST_SIG_A
    assert result[0]['urnref'] == "urn.json"


def test_core_bin_urnresolver_csv():
    result = get_urn_resolver_from_csv(TESTDIR + '/csv/urn.csv')
    # print('result', result)
    assert result[0]['urn'] == TEST_SIG_A
    assert result[0]['urnref'] == "urn.csv"


def test_core_bin_urnresolver_yml():
    result = get_urn_resolver_from_yml(TESTDIR + '/yml/urn.yml')
    # print('result', result)
    assert result[0]['urn'] == TEST_SIG_A
    assert result[0]['urnref'] == "urn.yml"


test_core_bin_urnresolver_json()
test_core_bin_urnresolver_yml()
