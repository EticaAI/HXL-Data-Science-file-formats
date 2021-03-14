"""hxlm.core.internal.formatter is an pygments wrapper
"""

from pygments import highlight
# import pygments.formatters.TerminalFormatter
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
# from pygments.formatters import TerminalFormatter
# from pygments.lexers.data import (
#     JsonLexer
# )

__all__ = ['format_pygments_generic', 'format_json_as_terminal']

def format_pygments_generic(generic_know, pygments_formatter, pygments_lexer, outfile=None):
    return highlight(generic_know, pygments_formatter, pygments_lexer, outfile)

def format_json_as_terminal(json_string):
    # json_string = '{}'
    lexer = get_lexer_by_name("json", stripall=True)
    formatter = get_formatter_by_name('terminal')
    return format_pygments_generic(json_string, lexer, formatter)
