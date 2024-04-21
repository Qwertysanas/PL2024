import sys
from lexer import Lexer
from maq import MaquinaV
from datetime import datetime

def printm(msg):
    print("maq: " + msg)
    return

def main(inp):
    # Inicialização da máquina
    maq = MaquinaV("stock.json")

    # Correr a máquina
    maq.start()
    return

if __name__ == "__main__":
    main(sys.argv)