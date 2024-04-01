import json
import re

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

# Conversão de float (em euros) para int (centimos)
def float2cents(cost : float) -> int:
    return int(cost * 100)

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
    
    # Mudança da quantidade de um item no stock
    def add_item(self, code : str, quantity : int) -> str:
        item = self.select_item(code)
        if not item:
            return "[ERRO] Código inválido"
        item['quant'] += quantity
        return str(item["quant"]) + "x unidades de " + item["nome"] + " adicionadas ao stock"
    
    # Adição de um item ao stock
    def new_item(self, code : str, name : str, quantity : int, price : float) -> str:
        self.stock.append({
            "cod": code,
            "nome": name,
            "quant": quantity,
            "preco": price
        })
        return "Item " + name + " adicionado ao stock, código: " + code

    # Lista de items disponíveis
    def printable_stock(self) -> str:
        res = "cod | nome               | quant | preco"
        for item in self.stock:
            res += '\n' + (item["cod"] + " | "
                + item["nome"] + (19 - len(item["nome"])) * ' ' + "| "
                + str(item["quant"]) + (6 - len(str(item["quant"]))) * ' ' + "| "
                + int2euros(float2cents(item["preco"])))
        return res

    # Lista de items disponíveis, cor de erro -> indisponível, cor de aviso -> sem saldo suficiente
    def pcolours_stock(self) -> str:
        res = "cod | nome               | quant | preco"
        for item in self.stock:
            if item["quant"] == 0:
                res += '\033[91m'
            elif item["preco"] > self.balance:
                res += '\033[93m'
            res += '\n' + (item["cod"] + " | "
                + item["nome"] + (19 - len(item["nome"])) * ' ' + "| "
                + str(item["quant"]) + (6 - len(str(item["quant"]))) * ' ' + "| "
                + int2euros(float2cents(item["preco"])) + "\033[0m")
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
        self.take_balance(float2cents(item["preco"]))
        item['quant'] -= 1
        return ('Pode retirar o produto dispensado "' + item["nome"] + '"\n'
                + self.printable_balance())

    def __str__(self) -> str:
        return (self.printable_stock()
                + '\n' + self.printable_balance())