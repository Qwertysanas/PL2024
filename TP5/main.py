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
    
    printm(datetime.now().strftime("%d-%m-%y") + ", Stock carregado, Estado atualizado.")
    printm("Bom dia. Estou disponível para atender o seu pedido.")

    
    return

if __name__ == "__main__":
    main(sys.argv)