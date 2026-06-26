"""
    pygments.styles.monotal_dark
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Minimal Monokai inspired style optimized for Uxntal.

    :copyright: Copyright 2006-present by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import (
    Token, Whitespace, Comment, Keyword,
    Name, String, Number, Operator, Literal
)


__all__ = ['Monotal_DarkStyle']


class Monotal_DarkStyle(Style):
    """
    Monokai inspired style tuned for Uxntal.
    """
    name = 'monotal_dark'

    background_color = "#2c2525"
    highlight_color = "#342d2d"

    # Color palette:
    #  Color  | Color Hex |    Lexer Scope   |    Uxntal Token
    #---------+-----------+------------------+-------------------
    # Pink    |  #ff6188  |  Keyword         |  Opcodes
    # Orange  |  #fc9867  |  Name.Decorator  |  Macro, include
    # Yellow  |  #ffd866  |  String          |  Padding
    # Green   |  #a9dc76  |  Number          |  Lit num, raw str
    # Cyan    |  #78dce8  |  Operator        |  Labels, sublabels
    # Purple  |  #ab9df2  |  Literal         |  Addressing modes
    # Gray    |  #72696a  |  Comment         |  Ignored
    # White   |  #fff1f3  |  Default         |  Fallback

    styles = {
        Token:          "#fff1f3",
        Whitespace:     "",
        Comment:        "italic #72696a",
        Keyword:        "#ff6188",
        Operator:       "italic #78dce8",
        Name.Decorator: "italic #fc9867",
        Literal:        "#ab9df2",
        Number:         "#a9dc76",
        String:         "#ffd866",
    }
