import json
import re
from ply import lex as lex

# Utils:

# Conversão de float para euros (str)
def float2euros(cost : float) -> str:
    cents = str(cost * 100).split('.')[0] + 'c'
    if cost < 1:
        return cents
    return re.sub(r"(\d+)\.\d+", r"\1e" + cents[-3:], str(cost))

# Conversão de int (cêntimos) para euros (str)
def int2euros(cost : int) -> str:
    cents = str(cost)[-2:] + 'c'
    if cost < 100:
        return cents
    euros = str(cost)[:-2] + 'e'
    return euros + cents

# Classe de uma máquina de vending
class MaquinaV:

    # Inicialização da máquina
    def __init__(self, stock_path : str) -> None:
        self.balance = 0
        self.stock_path = stock_path
        stock_file = open(stock_path, 'r')
        stock_struct = json.loads(stock_file.read())
        self.stock = stock_struct
        stock_file.close()

    # Guardar o stock
    def save(self) -> None:
        stock_file = open(self.stock_path, 'w')
        stock_file.write(json.dumps(self.stock))
        stock_file.close()
    
    # Devolução do printable do saldo
    def printable_balance(self) -> str:
        return "Saldo = " + int2euros(self.balance)
    
    # Adição de saldo, devolve o saldo sob a forma de printable
    def add_balance(self, amount : int) -> str:
        self.balance += amount
        return self.printable_balance()
    
    # Remoção de saldo (aquando de uma compra), devolve o saldo sob a forma de printable
    def take_balance(self, amount : int) -> str:
        self.balance -= amount
        return self.printable_balance
    
    # Seleção de um item pelo código, devolve um dicionário
    def select_item(self, code : str) -> dict:
        for item in self.stock:
            if item["cod"] == code:
                return item
        return None

    # Lista de items disponíveis
    def printable_stock(self) -> str:
        res = "\ncod | nome               | quant | preco\n"
        for item in self.stock:
            res += (item["cod"] + " | "
                + item["nome"] + (19 - len(item["nome"])) * ' ' + "| "
                + str(item["quant"]) + (6 - len(str(item["quant"]))) * ' ' + "| "
                + int2euros(item["preco"]) + '\n')
        return res

    # Lista de items disponíveis, cor de erro -> indisponível, cor de aviso -> sem saldo suficiente
    def pcolours_stock(self) -> str:
        res = "\ncod | nome               | quant | preco\n"
        for item in self.stock:
            if item["quant"] == 0:
                res += '\033[91m'
            elif item["preco"] > self.balance:
                res += '\033[93m'
            res += (item["cod"] + " | "
                + item["nome"] + (19 - len(item["nome"])) * ' ' + "| "
                + str(item["quant"]) + (6 - len(str(item["quant"]))) * ' ' + "| "
                + int2euros(item["preco"]) + "\033[0m" + '\n')
        return res

    # Compra de um item, devolve uma lista de strings com informações sobre a compra
    def buy(self, code : str) -> str:
        item = self.select_item(code)
        if not item:
            return "[ERRO] Código inválido"
        if item['quant'] == 0:
            return "Produto esgotado"
        if self.balance < item['preco']:
            return ("Saldo insuficiente para satisfazer o seu pedido\n" 
                    + self.printable_balance() + "; " + "Pedido = " + int2euros(item['preco']))
        self.take_balance(item['preco'])
        item['quant'] -= 1
        return ('Pode retirar o produto dispensado "' + item["nome"] + '"\n'
                + self.printable_balance())
        

m = MaquinaV("stock.json")
print(m.printable_stock())
print(m.add_balance(340))
print(m.buy("A23"))
print(m.buy("B25"))
print(m.buy("B25"))
print(m.buy("A23"))
print(m.buy("A23"))
print(m.buy("C30"))
