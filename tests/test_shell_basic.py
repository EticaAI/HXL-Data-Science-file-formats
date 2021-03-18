#!/usr/bin/env python3


# To output even more verbose results
#     ./tests/test_shell_basic.py
#
# To test directly
#     pytest -vv ./tests/test_shell_basic.py

# NOTE: this file require testinfra, https://testinfra.readthedocs.io/en/latest/
#     pip3 install pytest-testinfra


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

# def test_passwd_file(host):
#     passwd = host.file("/etc/passwd")
#     assert passwd.contains("root")

# test_libhxl_help('localhost')

# import sh
# print(sh)
# sh.python(['hxlspec', 'install'])
# # print(sh("hxlspec --version"))

# def load_yaml(filename):
#     """Return object in yaml file."""
#     with open(filename) as myfile:
#         content = myfile.read()
#         return yaml.safe_load(content)

# def test_project(cookies):



#     project = cookies.bake()

#     assert project.exit_code == 0
#     assert project.exception is None
#     assert project.project.basename == 'my_python_project'
#     assert project.project.isdir()


# def test_install(cookies):
#     # generate a temporary project using the cookiecutter
#     # cookies fixture
#     project = cookies.bake()
#     # remember the directory where tests should be run from
#     cwd = os.getcwd()
#     # change directories to the generated project directory
#     # (the installation command must be run from here)
#     os.chdir(str(project.project))
#     try:
#         # run the shell command
#         sh.python(['setup.py', 'install'])
#     except sh.ErrorReturnCode as e:
#         # print the error, so we know what went wrong
#         print(e)
#         # make sure the test fails
#         pytest.fail(e)
#     finally:
#         # always change directories to the test directory
#         os.chdir(cwd)
