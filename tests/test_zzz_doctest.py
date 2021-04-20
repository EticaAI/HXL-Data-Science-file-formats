#!/usr/bin/env python3

# WARNING: the test_zzz_doctest.py MAY return false positives (e.g. test
#          testdoc code even outside the hxlm module). Consider temporary
#          disable this test file and run
#              pytest -vv hxlm/ --doctest-modules
#          manually.

# To output even more verbose results
#     ./tests/test_zzz_doctest.py
#
# To test directly
#     pytest -vv ./tests/test_zzz_doctest.py

# NOTE: In theory, tox + pylint does not support both generic pylint and
#       docttest, see
#       - https://stackoverflow.com/questions/49254777
#         /how-to-let-pytest-discover-and-run-doctests-in-installed-modules
#       - https://github.com/EticaAI/HXL-Data-Science-file-formats/issues
#         /12#issuecomment-802464166
#       So this means that this file is somewhat an POR:gambirra
#       (Emerson Rocha, 2021-03-25 01:55 UTC)


# NOTE: this file require testinfra, https://testinfra.readthedocs.io/en/latest/
#     pip3 install pytest-testinfra

# TODO: https://testinfra.readthedocs.io/en/latest/examples.html
#       Implement things via parameters


# @see https://github.com/amoffat/sh
# @see https://amoffat.github.io/sh/
# @see https://blog.esciencecenter.nl/testing-shell-commands-from-python-2a2ec87ebf71
# @see https://github.com/NLeSC/python-template/blob/master/tests/test_project.py

import os
import sys
import pytest


def test_pytest_doctest_modules_all_may_have_false_positives(host):
    """Run pytest -vv hxlm/ --doctest-modules
    WARNING: the test_zzz_doctest.py MAY return false positives (e.g. test
    testdoc code even outside the hxlm module). Consider temporary disable this
    test file and run
        pytest -vv hxlm/ --doctest-modules
    Manually.
    """

    # hxlquickmeta have dependencies issues Orange3 (Qt) on python 3.7
    if sys.version_info <= (3, 8):
        return True

    cmd = host.run("pytest -vv hxlm/ --doctest-modules")
    # cmd = host.run("pytest --doctest-modules")

    print('cmd.stdout')
    print(cmd.stdout)

    print('cmd.stderr')
    print(cmd.stderr)

    assert cmd.succeeded

# test_libhxl_pytest_doctest_modules_all()
