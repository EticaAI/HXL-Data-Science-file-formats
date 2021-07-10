"""hxlm.core.internal.formatter is an pygments wrapper
"""

import sys

from pygments import highlight
# import pygments.formatters.TerminalFormatter
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
# from pygments.formatters import TerminalFormatter
# from pygments.lexers.data import (
#     JsonLexer
# )

__all__ = ['beautify']


# def format_json_as_terminal(json_string):
#     if sys.stdout.isatty():
#         # json_string = '{}'
#         lexer = get_lexer_by_name("json", stripall=True)
#         formatter = get_formatter_by_name('terminal')
#         return highlight(json_string, lexer, formatter)

#     return json_string


def beautify(input_string: str,
             lexer_alias: str,
             formatter_alias: str = 'terminal16m',
             #    lexer_options = None,
             #    formatter_options = None,
             ) -> str:
    """Beautify (format) an string input to an console terminal, PNG image, etc

    Args:
        input_string (str): An string to format. Often YAML or JSON
        lexer_alias (str): An Pygments lexer alias.
                        See https://pygments.org/docs/lexers/.
        formatter_alias (str, optional): An Pygments formatter alias.
                        See https://pygments.org/docs/lexers/.
                        Defaults to 'terminal16m'.

    Returns:
        str: An formatted output
    """
    if formatter_alias in ['terminal', 'console', 'terminal16m', 'console16m']:
        # Default is print to terminal. But may not be a terminal, so...
        if sys.stdout.isatty():
            # lexer = get_lexer_by_name(lexer_alias, **lexer_options)
            # formatter = get_formatter_by_name(formatter_alias,
            #                                     **formatter_options)
            lexer = get_lexer_by_name(lexer_alias)
            formatter = get_formatter_by_name(formatter_alias)
            return highlight(input_string, lexer, formatter)
        return input_string

    # lexer = get_lexer_by_name(lexer_alias, **lexer_options)
    # formatter = get_formatter_by_name(formatter_alias, **formatter_options)
    lexer = get_lexer_by_name(lexer_alias)
    formatter = get_formatter_by_name(formatter_alias)
    return highlight(input_string, lexer, formatter)
