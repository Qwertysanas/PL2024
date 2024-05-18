from ply import yacc as yacc
from lexer import Lexer, tokens

class Parser:

    tokens = tokens

    def __init__(self, lexer):
        self.lexer = lexer
        self.parser = yacc.yacc(module=self)

    def p_Start(self, p):   "Z : code"

    def p_code1(self, p):   "code : op codeop"
    def p_code2(self, p):   "code : "

    def p_codeop1(self, p): "codeop : NL code"
    def p_codeop0(self, p): "codeop : "

    def p_op1(self, p):    "op : '!' expr"
    def p_op2(self, p):    "op : '?' ID"
    def p_op3(self, p):    "op : ID '=' expr"

    def p_expr1(self, p):  "expr : term '*' expr"
    def p_expr2(self, p):  "expr : term '/' expr"
    def p_expr3(self, p):  "expr : term"

    def p_term1(self, p):  "term : factor '+' term"
    def p_term2(self, p):  "term : factor '-' term"
    def p_term3(self, p):  "term : factor"

    def p_factor1(self, p): "factor : NUMBER"
    def p_factor2(self, p): "factor : ID"
    def p_factor3(self, p): "factor : '(' expr ')'"

    def p_error(self, p):
        print(f"Syntax error at {p.value}, column {p.lexpos}, line {p.lineno}")

    def parse(self, s):
        self.parser.parse(s)
