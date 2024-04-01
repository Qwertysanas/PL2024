from ply import lex as lex

# Lista de tokens
tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SALDO",
    "SAIR",
    "ADICIONAR")

# Literais
literals = ["2e", "1e", "50c", "20c", "10c", "5c"]

# Expressões regulares para os tokens
def t_LISTAR(t):
    r"listar"
    return t

def t_MOEDA(t):
    r"MOEDA"
    return t

def t_SELECIONAR(t):
    r"SELECIONAR"
    return t

def t_SALDO(t):
    r"SALDO"
    return t

def t_SAIR(t):
    r"SAIR"
    return t

def t_ADICIONAR(t):
    r"ADICIONAR"
    return t

# Ignorar whitespaces e newlines e Error handling
t_ignore = " \t\n"
def t_error(t):
    print("Carácter ilegal: ", t.value[0])
    t.lexer.skip(1)

