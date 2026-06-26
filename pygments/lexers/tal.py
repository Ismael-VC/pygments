"""
    pygments.lexers.monotal
    ~~~~~~~~~~~~~~~~~~~

    Lexer for Uxntal (Monotal)

    :copyright: Copyright 2006-present by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Keyword, Name, String, Number, \
    Whitespace, Literal, Operator, Token

__all__ = ['TalLexer']


class TalLexer(RegexLexer):
    """
    For Uxntal source code.
    """

    name = 'Tal'
    aliases = ['tal', 'uxntal']
    filenames = ['*.tal']
    mimetypes = ['text/x-uxntal']
    url = 'https://wiki.xxiivv.com/site/uxntal.html'
    version_added = '2.12'

    instructions = [
        'BRK', 'LIT', 'INC', 'POP', 'DUP', 'NIP', 'SWP', 'OVR', 'ROT',
        'EQU', 'NEQ', 'GTH', 'LTH', 'JMP', 'JCN', 'JSR', 'STH',
        'LDZ', 'STZ', 'LDR', 'STR', 'LDA', 'STA', 'DEI', 'DEO',
        'ADD', 'SUB', 'MUL', 'DIV', 'AND', 'ORA', 'EOR', 'SFT'
    ]

    tokens = {
        'comment': [
            (r'(?<!\S)\((?!\S)', Comment, '#push'),
            (r'(?<!\S)\)(?!\S)', Comment, '#pop'),
            (r'[^()]+', Comment),
            (r'[()]+', Comment),
        ],

        'root': [
            (r'\s+', Whitespace),

            # Crey
            (r'(?<!\S)\((?!\S)', Comment, 'comment'),
            (r'[\[\]](?!\S)', Comment),

            # Pink
            (words(instructions, prefix=r'(?<!\S)', suffix=r'2?k?r?(?!\S)'),
             Keyword),

            # Green
            (r'#([0-9a-f]{2}){1,2}(?!\S)', Number),
            (r'([0-9a-f]{2}){1,2}(?!\S)', Token),
            (r'"\S+', Number),

            # Yellow
            (r'[\|$]\S+', String),
            (r'[|$](?!\S)', String),

            # Orange
            (r'[%\\~:]\S+', Name.Decorator),

            # Cyan
            (r'[@&]\S+', Operator),

            # Purple
            (r'[\.,;=_-]\S+', Literal),

            # White or Black depending on theme
            (r'[/!?]\S+', Token),
            (r'\S+', Token),
        ]
    }

    def analyse_text(text):
        return '|0100' in text[:500]
