from ply.lex import lex as lex

tokens = (
    "NUMBER",
    "ID",
    "NL",
)

class Lexer:
    tokens = tokens

    def __init__(self):
        self.lexer = lex(module=self)
        self.lexer.begin('INITIAL')

    literals = ['+', '-', '*', '/', '(', ')', '=', '!', '?']

    t_ignore = ' \t'

    def t_NUMBER(self, t):
        r"[+\-]?\d+"
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r"[a-zA-Z_][a-zA-Z0-9_]*"
        return t

    def t_NL(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)
        return t

    def t_error(self, t):
        print(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)
