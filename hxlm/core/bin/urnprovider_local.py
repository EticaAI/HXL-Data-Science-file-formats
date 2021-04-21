#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  urnprovider_local.py
#
#         USAGE:  urnprovider-local (...)
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  Etica.AI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.1
#       CREATED:  2021-04-21 04:21 UTC v0.1 draft
# ==============================================================================

import argparse

# from hxlm.core.schema.urn.util import (
#     get_urn_resolver_local,
#     # get_urn_resolver_remote,
#     # HXLM_CONFIG_BASE
# )


class URNProviderLocal:

    def __init__(self):
        """
        Constructs all the necessary attributes for the URNProviderLocal
        object.
        """
        self.hxlhelper = None
        self.args = None

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args_urnprovider_local(self):
        parser = argparse.ArgumentParser(description="TODO")
        return parser

    def execute_cli(self, args):
        print("{}")
        # /home/fititnt/.local/share/urn/
        # get_urn_resolver_local("/home/fititnt/.config/hxlm/urn/data/")
        # pass


if __name__ == "__main__":

    urnprovider_local = URNProviderLocal()
    args = urnprovider_local.make_args_urnprovider_local()

    urnprovider_local.execute_cli(args)


def exec_from_console_scripts():
    urnprovider_local_ = URNProviderLocal()
    args = urnprovider_local_.make_args_urnprovider_local()

    urnprovider_local_.execute_cli(args)
