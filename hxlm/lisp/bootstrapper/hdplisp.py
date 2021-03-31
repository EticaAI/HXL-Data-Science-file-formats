"""hxlm.lisp.bootstrapper.hdplisp

>>> ex_add = "(add 1 2)"
>>> ex_nest_a = "(add 3 (add 1 2))"
>>> ex_nest_b = "(add 3 [add 1 2])"
>>> ex_nest_c = "(add 3 {add 1 2})"

>>> parser(ex_add)
>(add 1 2)


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


def explain(thing: str, level: int = 1):
    """(debug) Just print current pointer

    Args:
        thing (str): the information
    """
    print((">" * level) + thing)


def parser(sexpression: str):
    """Parse an S-expression

    Args:
        sexpression (str): The inputterm
    """
    return tokenizer(sexpression)


def reader(token: str):
    """reader..."""
    explain(token)


def tokenizer(sexpression: str):
    """tokenizer..."""
    return reader(sexpression)
