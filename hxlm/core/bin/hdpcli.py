#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hdpcli
#
#         USAGE:  Load all *.hdp.yml/*hdp.json on current directory:
#                   hdpcli .
#                 Specific file, local:
#                   hdpcli path/to/my.hdp.yml
#                 Specific file, remote:
#                   hdpcli http://example.org/path/my.hdp.yml
#
#   DESCRIPTION:  HDP Declarative Programming Command Line Interface
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (@see https://pypi.org/project/libhxl/)
#                     - hxlm (github.com/EticaAI/HXL-Data-Science-file-formats)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  Etica.AI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v0.7.43
#       CREATED:  2021-03-09 15:40 UTC v0.7.4 started (based on hxl2example)
#      REVISION:  ---
# ==============================================================================


# @see https://github.com/sobolevn/awesome-cryptography
# @see https://github.com/pFarb/awesome-crypto-papers
# @see https://github.com/mozilla/sops
# @see More about RSA:
#      https://blog.trailofbits.com/2019/07/08/fuck-rsa/
#      https://www.youtube.com/watch?v=lElHzac8DDI
#      About Tink and focus on usability. Definely worth read
#      https://www.youtube.com/watch?v=pqev9r3rUJs&t=9665s
#      https://github.com/google/tink/blob/master/docs
#      /Tink-a_cryptographic_library--RealWorldCrypto2019.pdf
# @see About user experience
#      "Designing Crypto and Security APIs That Busy Engineers
#      and Sysadmins Can Use Securely":
#      https://www.usenix.org/sites/default/files/conference
#      /protected-files/hotsec15_slides_green.pdf

# TODO:
#   https://stackoverflow.com/questions/25638905/coloring-json-output-in-python

# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter
# from pygments.formatters import ImageFormatter
# from pygments.formatters import TerminalTrueColorFormatter
# from pygments.formatters import NullFormatter

# code = 'print "Hello World"'
# # print(highlight(code, PythonLexer(), TerminalTrueColorFormatter()))
# print(highlight(code, PythonLexer(), NullFormatter()))
# # print(highlight(code, PythonLexer(), HtmlFormatter()))
# # print(highlight(code, PythonLexer(), ImageFormatter(), 'img.png'))

import sys
import os
import logging
import argparse
# import tempfile
from pathlib import Path
from distutils.util import strtobool
# import base64
import secrets

import gettext

from cryptography.fernet import Fernet

# import nacl
# from nacl.public import PrivateKey, PublicKey
# from cryptography.hazmat.primitives import hashes
# import hashlib
# from cryptography.hazmat.primitives import hashes, hmac

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io

from hxlm.core.model.hdp import (
    HDP
)

from hxlm.core.internal.keystore import (
    HKeystore
)

from hxlm.core.internal.formatter import (
    beautify
)

# @see https://github.com/hugapi/hug
#     pip3 install hug --upgrade
# import hug

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


_HOME = str(Path.home())
# TODO: clean up redundancy from hxlm/core/schema/urn/util.py
HXLM_CONFIG_BASE = os.getenv(
    'HXLM_CONFIG_BASE', _HOME + '/.config/hxlm/')

HXLM_DATA_POLICY_BASE = os.getenv(
    'HXLM_DATA_POLICY_BASE', _HOME + '/.config/hxlm/policy/')

HXLM_DATA_VAULT_BASE = os.getenv(
    'HXLM_DATA_VAULT_BASE', _HOME + '/.local/var/hxlm/data/')

HXLM_DATA_VAULT_BASE_ALT = os.getenv('HXLM_DATA_VAULT_BASE_ALT')
HXLM_DATA_VAULT_BASE_ACTIVE = os.getenv(
    'HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE)

HXLM_DATA_POLICY_BASE = os.getenv(
    'HXLM_DATA_POLICY_BASE', _HOME + '/.config/hxlm/policy/')

# Directory/File permissions for NEW content create by hdpcli
HXLM_CONFIG_PERM_MODE = os.getenv(
    'HXLM_CONFIG_PERM_MODE', "0700")

HXLM_DATA_VAULT_PERM_MODE = os.getenv(
    'HXLM_DATA_VAULT_PERM_MODE', "0700")

HXLM_LOCALE = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__)))) + '/locale'

gettext.bindtextdomain('hdp', HXLM_LOCALE)
gettext.textdomain('hdp')
_ = gettext.gettext


def prompt_confirmation(message: str) -> bool:
    """Simple wrapper to ask user yes/no with a message without ValueError

    Args:
        message (str): Message to ask user input

    Returns:
        bool: True if agree, False if did not agree
    """
    val = input(message + " [yes/no]\n")
    try:
        sys.stdout.write("'yes' or 'no'? \n")
        yesorno = strtobool(val)
    except ValueError:
        return prompt_confirmation(message)
    return yesorno


class HDPCLI:
    """
    HDP Declarative Programming Command Line Interface
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the HDPCLI object.
        """
        self.hxlhelper = None
        self.args = None

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def _exec_export_to_hxl_json_processing_specs(self,
                                                  hdp_entry_point: str,
                                                  debug: bool = False) -> str:

        # TODO: while the default of HDP (and later also from the hdpcli) is
        #       not allow online initialization, at this moment, for testing,
        #       we're allowing here. (Emerson Rocha, 2021-03-13 01:48 UTC)
        hdp = HDP(hdp_entry_point=hdp_entry_point,
                  online_unrestricted_init=True,
                  debug=debug)

        # if debug:
        #     print('hdpcli ... hdp', hdp)
        #     print('hdpcli ... hdp', hdp.export_yml())

        # string_result = hdp.export_yml()
        string_result = hdp.export_json_processing_specs()

        return string_result

        # return self.EXIT_OK

    def _exec_hdp_init(self, config_base: str = None,
                       data_base: str = None,
                       please: bool = None) -> int:
        """Initialize HDP enviroment

        Args:
            config_base (str, optional): Configuration path. Defaults to None.
            data_base (str, optional): Data path. Defaults to None.
            please (bool, optional): If already confirm changes upfront
                                     Defaults to None.

        Returns:
            int: EXIT_OK or EXIT_ERROR
        """
        step1 = self._exec_hdp_init_home(
            config_base=config_base, please=please)
        step2 = self._exec_hdp_init_data(data_base=data_base, please=please)

        if (step1 + step2) == self.EXIT_OK:
            return self.EXIT_OK

        return self.EXIT_ERROR

    def _exec_hdp_init_data(self, data_base: str = None, please: bool = None):
        """Initialize HDP enviroment, data base only

        Args:
            data_base (str, optional): Data path. Defaults to None.
            please (bool, optional): If already confirm changes upfront
                                     Defaults to None.

        Returns:
            int: EXIT_OK or EXIT_ERROR
        """
        if data_base is None:
            data_base = HXLM_DATA_VAULT_BASE_ACTIVE

        data_base = os.path.normpath(data_base)

        if os.path.exists(data_base):
            print('OK: data_base [' + data_base + '] exists')
            return self.EXIT_OK

        allowed = please or prompt_confirmation(
            'Create [' + data_base + '] with permissions [' +
            str(HXLM_DATA_VAULT_PERM_MODE) + ']?')

        if allowed:
            os.makedirs(data_base, mode=int(HXLM_DATA_VAULT_PERM_MODE, 8))
            print('data_base [' + data_base + '] created.')
            return self.EXIT_OK
        else:
            print('INFO: data_base creation not allowed.')

        return self.EXIT_ERROR

    def _exec_hdp_init_home(self, config_base: str = None,
                            please: bool = None):
        """Initialize HDP enviroment, configuration base only

        Args:
            config_base (str, optional): Configuration path. Defaults to None.
            please (bool, optional): If already confirm changes upfront
                                     Defaults to None.

        Returns:
            int: EXIT_OK or EXIT_ERROR
        """
        if config_base is None:
            config_base = HXLM_CONFIG_BASE

        config_base = os.path.normpath(config_base)

        # print('_debug_entropy', self._entropy_pseudotest(self._get_salt))
        # # print('_exec_hdp_init_home _get_salt', self._get_salt())
        # print('_debug_entropy', self._entropy_pseudotest(self._get_fernet))
        # print('_exec_hdp_init_home get_fernet',  self._get_fernet())
        # print('_debug_entropy', self._entropy_pseudotest(self._get_keypar))
        # print('_exec_hdp_init_home _get_keypar',  self._get_keypar())

        # Path creation
        if os.path.exists(config_base):
            print('OK: config_base [' + config_base + '] exists')
            return self.EXIT_OK

        allowed = please or prompt_confirmation(
            'Create [' + config_base + '] with permissions [' +
            str(HXLM_CONFIG_PERM_MODE) + ']?')

        if allowed:
            os.makedirs(config_base, mode=int(HXLM_CONFIG_PERM_MODE, 8))
            print('config_base [' + config_base + '] created.')
            return self.EXIT_OK
        else:
            print('INFO: config_base creation not allowed.')

        print('TODO: create salt or something')
        return self.EXIT_ERROR

    def _entropy_pseudotest(self, method) -> None:
        """Run a few turns any function supposed to return randon values

        Note that while is actually hard to test entropy, this pseudotest
        can at least give some hint if of very obvious errors, like an
        salt or crypto key generated with same seeds values.

        Args:
            method (Function): A method/function to run
        """
        debug_output = 10

        print('Testing entropy of method ' + method.__name__ + '\n')
        while debug_output > 0:
            print('  [' + str(debug_output).zfill(3) + '] ' + str(method()))
            debug_output -= 1

        print('\n If the lines above seems repetitive. Something is ' +
              'wrong with this code or machine.\n\n')

    def _get_fernet(self):
        """Get a new Fernet key

        @see https://github.com/fernet/spec
        @see https://cryptography.io/en/latest/fernet.html
        @see https://docs.openstack.org/keystone/pike/admin
             /identity-fernet-token-faq.html

        Returns:
            [type]: [description]
        """
        # https://cryptography.io/en/latest/fernet.html
        return Fernet.generate_key()

    def _get_keypar(self):
        """_get_keypar is an draft. The entire way to store the keys should
           be at least a bit hardened

        Returns:
            [type]: [description]
        """

        # TODO: these imports from nacl, since are temporary test, are not
        #       installed as dependency, so we removed from top file import
        #       and move here to at least allow test-infra tests don't fail.
        #       This also means that last releases likely do not installed
        #       correctly on other peoples machines
        #       (Emerson Rocha, 2021-03-18 22:58)
        import nacl  # noqa
        from nacl.public import PrivateKey, PublicKey  # noqa

        # @see https://github.com/pyca/pynacl/issues/192
        # @see https://pynacl.readthedocs.io/en/latest/encoding/
        # @see https://stackoverflow.com/questions/54093558
        #      /how-to-load-signingkey-from-its-value-in-pynacl
        key = PrivateKey.generate()
        encoded_public_key = key.public_key.encode(
            encoder=nacl.encoding.Base64Encoder)
        loaded_public_key = PublicKey(
            encoded_public_key, encoder=nacl.encoding.Base64Encoder)

        # print('oooi', key._private_key)
        # print('oooi', key._private_key)

        # print(bytes(key).hex())
        # print(bytes(key).decode('utf-8'))

        # base64.urlsafe_b64encode(bytes(key))
        # print('ooi2', base64.urlsafe_b64encode(bytes(key).decode('utf-8')))
        assert loaded_public_key.encode() == key.public_key.encode()
        return {
            'public_key': encoded_public_key,
            'private_key': bytes(key).hex()
        }

    def _get_password(self):
        # @see https://docs.python.org/pt-br/3/library/getpass.html
        # @see https://gist.github.com/noqqe/cd9f8dc6477c7929f8b3
        # @see https://github.com/pyca/pynacl/issues/192
        print('TODO _get_password')

    def _get_salt(self, size: int = 64) -> str:
        """Get a new salt

        Args:
            size (int, optional): Byte size of the salt. Defaults to 64.

        Returns:
            str: an salt
        """

        return secrets.token_urlsafe(size)
        # return 'test'

    def make_args_hdpcli(self):
        """Prepare parse args

        Returns:
            [dict]: args
        """

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=(
                # This is an test comment for translators
                _("HDP Declarative Programming Command Line Interface."))
        )

        parser.add_argument(
            '--debug',
            help='instead of return the result, do full debug',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--export-to-hxl-json-processing-specs',
            help='Export JSON processing specs for HXL data. Use with ' +
            '"hxlspec myspec.json > data.hxl.csv" or HXL-proxy.' +
            '(https://proxy.hxlstandard.org/api/from-spec.html)',
            action='store',
            # const=True,
            default=None,
            # nargs='?'
            # # default=HXLM_CONFIG_BASE,
            # default=HXLM_CONFIG_BASE,
            # # default=False,
            # nargs='?'
        )

        parser.add_argument(
            '--fontem-linguam',
            help='(draft) Source language (use if not autodetected)' +
            'Must be an ISO 639-3 code',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--hdp-init',
            help='Initialize local to work with hxlm.core cli tools. ' +
            'This will use defaults that would work with most single ' +
            'workspace users. ' +
            'HXLM_CONFIG_BASE [' + HXLM_CONFIG_BASE + '], ' +
            'HXLM_DATA_VAULT_BASE_ACTIVE [' +
            HXLM_DATA_VAULT_BASE_ACTIVE + ']',
            action='store_const',
            const=True,
            default=False,
            # nargs='?'
            # # default=HXLM_CONFIG_BASE,
            # default=HXLM_CONFIG_BASE,
            # # default=False,
            # nargs='?'
        )

        parser.add_argument(
            '--hdp-init-data',
            help='Initialize local with non-default data base. ' +
            'Intented for users planning to work with multiple workspaces ' +
            'or that want to store on specific path ' +
            '(like an huge external HDD or SSD)',
            action='store',
            # const=True,
            default=False,
            nargs='?'
            # # default=HXLM_CONFIG_BASE,
            # default=HXLM_CONFIG_BASE,
            # # default=False,
            # nargs='?'
        )

        parser.add_argument(
            '--hdp-init-home',
            help='Initialize local with non-default configuration home. ' +
            'Intented for users planning to work with multiple workspaces ' +
            'or that want to store on specific path ' +
            '(like an USB stick). ',
            action='store',
            # const=True,
            default=None,
            # nargs='?'
            # # default=HXLM_CONFIG_BASE,
            # default=HXLM_CONFIG_BASE,
            # # default=False,
            # nargs='?'
        )

        parser.add_argument(
            '--hdp-init-keystore',
            help='(draft, may be removed) Initialize an keystore',
            action='store',
            # const=True,
            default=False,
            nargs='?'
            # # default=HXLM_CONFIG_BASE,
            # default=HXLM_CONFIG_BASE,
            # # default=False,
            # nargs='?'
        )

        parser.add_argument(
            '--non-adm0',
            help='(draft) Filter by except adm0 (country/territory). ' +
            'Must be an ISO 3166-1 alpha-2 code',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--non-grupum',
            help='Filter by except grupum (group). ' +
            'Use values based on strings defined on each hsilo.grupum',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--non-nomen',
            help='(draft) Filter by except nomen pattern' +
            'Use values based on strings defined on HDP file.',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--non-tag',
            help='(draft) Filter by except tag. ' +
            'Use values based on strings defined on HDP file.',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--non-urn',
            help='Filter by except URN pattern. ' +
            'Use values based on strings defined on HDP file.',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--objectivum-linguam',
            help='(draft) Objective language / target language to export. ' +
            'Must be an ISO 639-3 code (UPPERCASE)',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--please',
            help='For commants that ask for user change, already agree',
            # action='store',
            # action=argparse.BooleanOptionalAction,
            metavar='please',
            const=True,
            default=False,
            # nargs='?'
            # # default=HXLM_CONFIG_BASE,
            # default=HXLM_CONFIG_BASE,
            # # default=False,
            nargs='?'
        )

        # TODO: add unitary tests for --urn-index-local
        parser.add_argument(
            '--urn-index-local',
            help='Load URN index from local file/folder ' +
            '(accept multiple options)',
            metavar='urn_index_local',
            type=str,
            action='append'
            # action='store_const',
            # const=True,
            # default=False
        )

        # TODO: add unitary tests for --urn-index-remote
        parser.add_argument(
            '--urn-index-remote',
            help='Load URN index from exact URL (accept multiple options)',
            metavar='urn_index_remote',
            type=str,
            action='append'
            # action='store_const',
            # const=True,
            # default=False
        )

        parser.add_argument(
            '--no-urn-user-defaults',
            help='Disable load urnresolver URN indexes from ' +
            '~/.config/hxlm/urn/.',
            metavar='no_urn_user',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--no-urn-vendor-defaults',
            help='Disable load urnresolver urnresolver-default.urn.yml',
            metavar='no_urn_vendor_defaults',
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            '--verum-adm0',
            help='(draft) Filter by adm0 (country/territory). ' +
            'Must be an ISO 3166-1 alpha-2 code',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--verum-grupum',
            help='Filter by grupum (group). ' +
            'Use values based on strings defined on each hsilo.grupum',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--verum-tag',
            help='(draft) Filter by tag. ' +
            'Use values based on strings defined on HDP file.',
            action='store',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--verum-urn',
            help='Filter by URN pattern.' +
            'Use values based on strings defined on HDP file.',
            action='store',
            default=None,
            nargs='?'
        )

        self.args = parser.parse_args()
        return self.args

    def execute_cli(self, args,
                    stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        """
        The execute_cli is the main entrypoint of HDPCLI. When
        called will try to convert the URN to an valid IRI.
        """

        is_debug = False

        # Test commands:
        # urnresolver --debug urn:data:xz:hxl:standard:core:hashtag
        # urnresolver urn:data:xz:hxl:standard:core:hashtag
        #                --urn-file tests/urnresolver/all-in-same-dir/
        # hxlquickimport $(urnresolver urn:data:xz:hxl:standard:core:hashtag
        #                      --urn-file tests/urnresolver/all-in-same-dir/)
        #

        if 'debug' in args and args.debug:
            print('DEBUG: CLI args [[', args, ']]')
            is_debug = True

        if args.export_to_hxl_json_processing_specs:
            hdp_result = self._exec_export_to_hxl_json_processing_specs(
                hdp_entry_point=args.export_to_hxl_json_processing_specs,
                debug=is_debug
            )
            # print('export_to_hxl_json_processing_specs', hdp)
            # return str(hdp)
            # print(hdp_result)
            # print(format_json_as_terminal(hdp_result))
            print(beautify(hdp_result, 'json'))
            return self.EXIT_OK

        # TODO: 'Is AI just a bunch of if and else statements?'
        if (args.hdp_init and (args.hdp_init_home or args.hdp_init_data)) or \
                (args.hdp_init_home and (args.hdp_init
                                         or args.hdp_init_data)) or \
                (args.hdp_init_data and (args.hdp_init or args.hdp_init_home)):
            print('ERROR: only one of the options can run at same time: \n' +
                  ' --hdp-init \n --hdp-init-home \n --hdp-init-home')
            return self.EXIT_ERROR

        if args.hdp_init_keystore:
            hks = HKeystore(args.hdp_init_keystore)
            print('hks', hks)
            return self.EXIT_OK

        if args.hdp_init_data:
            return self._exec_hdp_init_data(args.hdp_init_data,
                                            please=args.please)
        if args.hdp_init_home:
            return self._exec_hdp_init_home(args.hdp_init_home,
                                            please=args.please)
        if args.hdp_init:
            return self._exec_hdp_init(please=args.please)

        # TODO: and what if infile actually is some command piping to hdpcli?
        #       We should either test better this or disable
        #       (Emerson Rocha, 2021-03-14 00:52 UTC)

        # TODO: while the default of HDP (and later also from the hdpcli) is
        #       not allow online initialization, at this moment, for testing,
        #       we're allowing here. (Emerson Rocha, 2021-03-13 01:48 UTC)
        if 'infile' in args and (os.path.isfile(args.infile) or
                                 os.path.isdir(args.infile) or
                                 args.infile.startswith(('http://',
                                                         'https://',
                                                         'urn:'))):
            hdp = HDP(hdp_entry_point=args.infile,
                      online_unrestricted_init=True,
                      debug=is_debug)

            hdp_filters = hdp.get_prepared_filter(args)

            # print('hdp_filters', hdp_filters)
            # print('hdp', hdp)
            hdp_rules = hdp.export_yml(hdp_filters, args.objectivum_linguam)

            # if 'objectivum_linguam' in args:

            print(beautify(hdp_rules, 'yaml'))
            # print(hdp.export_yml())
            # print('hdp _hdp', hdp._hdp)
            return self.EXIT_OK

        print('ERROR: what to do? try:', file=stderr)
        print('    hdpcli --help', file=stderr)
        print('    hdpcli --debug <your instructions>', file=stderr)
        # print(self.EXIT_ERROR)
        return sys.exit(self.EXIT_ERROR)


class HXLUtils:
    """
    HXLUtils contains functions from the Console scripts of libhxl-python
    (HXLStandard/libhxl-python/blob/master/hxl/scripts.py) with few changes
    to be used as class (and have one single place to change).
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, description, hxl_output=True):
        """Set up parser with default arguments.
        @param description: usage description to show
        @param hxl_output: if True (default), include options for HXL output.
        @returns: an argument parser, partly set up.
        """
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            'infile',
            help='HXL file to read (if omitted, use standard input).',
            nargs='?'
        )
        if hxl_output:
            parser.add_argument(
                'outfile',
                help='HXL file to write (if omitted, use standard output).',
                nargs='?'
            )
        parser.add_argument(
            '--sheet',
            help='Select sheet from a workbook (1 is first sheet)',
            metavar='number',
            type=int,
            nargs='?'
        )
        parser.add_argument(
            '--selector',
            help='JSONPath expression for starting point in JSON input',
            metavar='path',
            nargs='?'
        )
        parser.add_argument(
            '--http-header',
            help='Custom HTTP header to send with request',
            metavar='header',
            action='append'
        )
        if hxl_output:
            parser.add_argument(
                '--remove-headers',
                help='Strip text headers from the CSV output',
                action='store_const',
                const=True,
                default=False
            )
            parser.add_argument(
                '--strip-tags',
                help='Strip HXL tags from the CSV output',
                action='store_const',
                const=True,
                default=False
            )
        parser.add_argument(
            "--ignore-certs",
            help="Don't verify SSL connections (useful for self-signed)",
            action='store_const',
            const=True,
            default=False
        )
        parser.add_argument(
            '--log',
            help='Set minimum logging level',
            metavar='debug|info|warning|error|critical|none',
            choices=['debug', 'info', 'warning', 'error', 'critical'],
            default='error'
        )
        return parser

    def add_queries_arg(
        self,
        parser,
        help='Apply only to rows matching at least one query.'
    ):
        parser.add_argument(
            '-q',
            '--query',
            help=help,
            metavar='<tagspec><op><value>',
            action='append'
        )
        return parser

    def do_common_args(self, args):
        """Process standard args"""
        logging.basicConfig(
            format='%(levelname)s (%(name)s): %(message)s',
            level=args.log.upper())

    def make_source(self, args, stdin=STDIN):
        """Create a HXL input source."""

        # construct the input object
        input = self.make_input(args, stdin)
        return hxl.io.data(input)

    def make_input(self, args, stdin=sys.stdin, url_or_filename=None):
        """Create an input object"""

        if url_or_filename is None:
            url_or_filename = args.infile

        # sheet index
        sheet_index = args.sheet
        if sheet_index is not None:
            sheet_index -= 1

        # JSONPath selector
        selector = args.selector

        http_headers = self.make_headers(args)

        return hxl.io.make_input(
            url_or_filename or stdin,
            sheet_index=sheet_index,
            selector=selector,
            allow_local=True,  # TODO: consider change this for execute_web
            http_headers=http_headers,
            verify_ssl=(not args.ignore_certs)
        )

    def make_output(self, args, stdout=sys.stdout):
        """Create an output stream."""
        if args.outfile:
            return FileOutput(args.outfile)
        else:
            return StreamOutput(stdout)

    def make_headers(self, args):
        # get custom headers
        header_strings = []
        header = os.environ.get("HXL_HTTP_HEADER")
        if header is not None:
            header_strings.append(header)
        if args.http_header is not None:
            header_strings += args.http_header
        http_headers = {}
        for header in header_strings:
            parts = header.partition(':')
            http_headers[parts[0].strip()] = parts[2].strip()
        return http_headers


class FileOutput(object):
    """
    FileOutput contains is based on libhxl-python with no changes..
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self, filename):
        self.output = open(filename, 'w')

    def __enter__(self):
        return self

    def __exit__(self, value, type, traceback):
        self.output.close()


class StreamOutput(object):
    """
    StreamOutput contains is based on libhxl-python with no changes..
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self, output):
        self.output = output

    def __enter__(self):
        return self

    def __exit__(self, value, type, traceback):
        pass

    def write(self, s):
        self.output.write(s)


if __name__ == "__main__":

    hdpcli = HDPCLI()
    args_ = hdpcli.make_args_hdpcli()

    hdpcli.execute_cli(args_)


def exec_from_console_scripts():
    hdpcli = HDPCLI()
    args_ = hdpcli.make_args_hdpcli()

    hdpcli.execute_cli(args_)
