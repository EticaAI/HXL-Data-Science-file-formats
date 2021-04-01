"""hxlm.lisp.bootstrapper.hdplisp

>>> ex_add = "(add 1 2)"
>>> ex_nest_a = "(add 3 (add 1 2))"
>>> ex_nest_b = "(add 3 [add 1 2])"
>>> ex_nest_c = "(add 3 {add 1 2})"

>>> parser(ex_add)
>(add 1 2)
>>> parser(ex_nest_a)
>(add 3 (add 1 2))


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

# TODO: use as reference the Racket reference (have more options than averange
#       lisp-like implementations found on most places), see
#       https://docs.racket-lang.org/reference/reader.html
#       (Emerson Rocha, 2021-03-31 18:59 UTC)

from dataclasses import InitVar, dataclass

from typing import (
    Union
)


@dataclass(repr=False)
class HDPlisp:
    """An HDP-like Lisp abstraction class"""

    sexpr: str
    """The raw initial S-expression"""

    steps: InitVar[list] = []
    """An somewat Abstract Syntax Tree (needs testing)"""

    token_delimiters = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    """Non-escaped tokens (, [, { match non-escaped ), ], }

    While '(' and ')' are more common, the HDPlisp users decide others chars
    to help with organization
    """

    def __repr__(self):
        return self.sexpr


def explain(thing: Union[str, HDPlisp], level: int = 1):
    """(debug) Just print current pointer

    Args:
        thing (str): the information
    """
    print((">" * level) + str(thing))


def parser(sexpression: str):
    """Parse an S-expression

    Args:
        sexpression (str): The input term
    """
    hdplisp = HDPlisp(sexpression)
    return tokenizer(hdplisp)


def reader(token: HDPlisp):
    """reader..."""

    explain(token)


def tokenizer(hdpsexpr: HDPlisp):
    """tokenizer..."""
    # print(type(hdpsexpr))
    return reader(hdpsexpr)
