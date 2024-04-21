import sys
import re
from ply import lex as lex

tokens = (
    "COMMENT",
    "KEYWORD",
    "BOOLOP",
    "ID",
    "STRING",
    "OPERATOR",
    "NUMBER",
    "WILDCARD",
    "COMMA",
    "NEWLINE"
)

def t_COMMENT(t):
    r"\#.*"
    t.value = re.sub(pattern = r"\#{1,}(.*)", repl = r'\1', string = t.value)
    return t

def t_KEYWORD(t):
    r"Select|From|Where"
    return t

def t_BOOLOP(t):
    r"And|Or"
    return t

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    return t
    
def t_STRING(t):
    r'"[^"]*"'
    return t

def t_OPERATOR(t):
    r"[=<>]?=|<|>"
    return t

def t_NUMBER(t):
    r"[+\-]?\d+"
    return t

def t_WILDCARD(t):
    r'\*'
    return t    

def t_COMMA(t):
    r','
    return t    

def t_NEWLINE(t):
    r'\n'
    return t

t_ignore = r"[\t ]+"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def main(inp):
    lexer = lex.lex()
    i = 1
    if (len(inp) == 1):
        for l in sys.stdin:
            lexer.input(l)
            print("linha", i)
            for tok in lexer:
                print(tok)
            i += 1
        return
    else:
        file = open(inp[1])
        for l in file:
            lexer.input(l)
            print("linha", i)
            for tok in lexer:
                print(tok)
            i += 1
        file.close()
    return

if __name__ == "__main__":
    main(sys.argv)