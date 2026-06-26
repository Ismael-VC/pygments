"""
    pygments.styles.monotal_light
    ~~~~~~~~~~~~~~~~~~~~~~~

    Minimal Monokai inspired style optimized for Uxntal.

    :copyright: Copyright 2006-present by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import (
    Token, Whitespace, Comment, Keyword,
    Name, String, Number, Operator, Literal
)


__all__ = ['Monotal_LightStyle']


class Monotal_LightStyle(Style):
    """
    Monokai inspired style tuned for Uxntal.
    """
    name = 'monotal_light'

    background_color = "#f8efe7"
    highlight_color = "#f0e7e0"

    # Color palette:
    #  Color  | Color Hex |    Lexer Scope   |    Uxntal Token
    #---------+-----------+------------------+-------------------
    # Pink    |  #ce4770  |  Keyword         |  Opcodes
    # Orange  |  #d4572b  |  Name.Decorator  |  Macro, include
    # Yellow  |  #b16803  |  String          |  Padding
    # Green   |  #218871  |  Number          |  Lit num, raw str
    # Cyan    |  #2473b6  |  Operator        |  Labels, sublabels
    # Purple  |  #6851a2  |  Literal         |  Addressing modes
    # Gray    |  #a59c9c  |  Comment         |  Ignored
    # Black   |  #2c232e  |  Default         |  Fallback

    styles = {
        Token:          "#2c232e",
        Whitespace:     "",
        Comment:        "italic #a59c9c",
        Keyword:        "#ce4770",
        Operator:       "italic #2473b6",
        Name.Decorator: "italic #d4572b",
        Literal:        "#6851a2",
        Number:         "#218871",
        String:         "#b16803",
    }
