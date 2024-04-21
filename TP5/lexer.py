from ply import lex as lex

# Classe do lexer
class Lexer:

    # Lista de tokens
    tokens = (
        "LISTARC",
        "LISTAR",
        "TMOEDA",
        "MOEDA",
        "SELECIONAR",
        "SALDO",
        "SAIR",
        "ADICIONAR",
        "ID",
        "NEWLINE")

    # Literais
    literals = [',', '.']

    # Inicialização do lexer
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Expressões regulares para os tokens
    def t_LISTARC(self, t):
        r"LISTARC"
        return t

    def t_LISTAR(self, t):
        r"LISTAR"
        return t

    def t_TMOEDA(self, t):
        r"([12]e)|([125]0c)|(5c)"
        return t

    def t_MOEDA(self, t):
        r"MOEDA"
        return t
    
    def t_SELECIONAR(self, t):
        r"SELECIONAR"
        t.value = t.value[10:]
        return t

    def t_SALDO(self, t):
        r"SALDO"
        return t

    def t_SAIR(self, t):
        r"SAIR"
        return t

    def t_ADICIONAR(self, t):
        r"ADICIONAR"
        return t

    def t_ID(self, t):
        r"[A-Z][A-Z0-9]+"
        return t

    def t_NEWLINE(self, t):
        r'\n'
        t.lexer.lineno += 1
        return t
    
    # Ignorar whitespaces e newlines e Error handling
    t_ignore = " \t"
    def t_error(self, t):
        raise Exception("[ERRO] Carácter inválido: " + t.value[0])
        t.lexer.skip(1)