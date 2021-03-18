#!/usr/bin/env python3

# To output even more verbose results
#     ./tests/test_shell_basic.py
#
# To test directly
#     pytest -vv ./tests/test_shell_basic.py

# NOTE: this file require testinfra, https://testinfra.readthedocs.io/en/latest/
#     pip3 install pytest-testinfra

# TODO: https://testinfra.readthedocs.io/en/latest/examples.html
#       Implement things via parameters


# @see https://github.com/amoffat/sh
# @see https://amoffat.github.io/sh/
# @see https://blog.esciencecenter.nl/testing-shell-commands-from-python-2a2ec87ebf71
# @see https://github.com/NLeSC/python-template/blob/master/tests/test_project.py

import pytest
import os

# import pytest.testinfra

# import yaml


def test_libhxl_help(host):
    cmd = host.run("hxlspec --help")

    assert cmd.succeeded


def test_hdpcli_help(host):
    cmd = host.run("hdpcli --help")

    assert cmd.succeeded


def test_urnresolver_help(host):
    cmd = host.run("urnresolver --help")

    assert cmd.succeeded

# # Returns empty:
# hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --non-grupum salve-mundi


def test_hdpcli_errors(host):
    cmd = host.run(
        "hdpcli tests/hrecipe/FILE_THAT_DO_NOT_EXIST.mul.hdp.yml --non-grupum salve-mundi")

    # assert not cmd.succeeded
    assert cmd.stderr != ''
    assert cmd.rc != 0


def test_hdpcli_empty(host):
    cmd = host.run(
        "hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --non-grupum salve-mundi")

    assert cmd.succeeded
    assert cmd.stderr == ''
    assert cmd.rc == 0

# TODO: more specific tests need to be done with actuall results of hdpcli.
#       It may be easy to do it with the final cli than only with internal
#       library