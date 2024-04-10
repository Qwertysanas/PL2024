import json
import re
import sys
from datetime import datetime
from lexer import Lexer

# Utils:

# Dicionário de moedas
cdict = {1 : 200, 2 : 100, 3 : 50, 4 : 20, 5 : 10, 6 : 5}

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
        self.lexer = Lexer()
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
    
    # Leitura de uma moeda
    def add_coin(self, coin : str) -> str:
        coin = re.sub(r"(\d+)e", lambda x: str(int(x[1]) * 100), coin)
        coin = re.sub(r"(\d+)c", lambda x: x[1], coin)
        self.add_balance(int(coin))
        return self.printable_balance()
    
    # Leitura de uma lista de moedas
    def add_coins(self, coins : list) -> str:
        for coin in coins:
            self.add_coin(coin)
        return self.printable_balance()

    # Devolução do saldo
    def get_coins(self) -> str:
        if self.balance == 0:
            return "Não tem saldo a devolver."
        global cdict
        rdict = {}
        for k in cdict:
            rdict[k] = 0
            
        for k in cdict:
            while self.balance >= cdict[k]:
                self.balance -= cdict[k]
                rdict[k] += 1
        
        res = "Pode retirar o troco: "
        for k in rdict:
            if rdict[k]:
                res += str(rdict[k]) + "x " + int2euros(cdict[k]) + ", "
        
        self.balance = 0
        return res[:-2] + '.'

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
            elif item["preco"] * 100 > self.balance:
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
            return "[ERRO] Produto esgotado"
        if self.balance < item['preco']:
            return ("[ERRO] Saldo insuficiente para satisfazer o seu pedido\n" 
                    + self.printable_balance() + "; " + "Pedido = " + int2euros(item['preco']))
        self.take_balance(float2cents(item["preco"]))
        item['quant'] -= 1
        return ('Pode retirar o produto dispensado "' + item["nome"] + '"\n'
                + self.printable_balance())
    
    # Sair
    def exit(self) -> str:
        self.save()
        return self.get_coins()

    def __str__(self) -> str:
        return (self.printable_stock()
                + '\n' + self.printable_balance())

    def start(self) -> None:
        print(datetime.now().strftime("%d-%m-%y") + ", Stock carregado, Estado atualizado.")
        print("Bom dia. Estou disponível para atender o seu pedido.")
        for line in sys.stdin:
            try:
                self.lexer.lexer.input(line)
                for tok in self.lexer.lexer:
                    if tok.type == "LISTARC":
                        print(self.pcolours_stock())
                        pass
                    elif tok.type == "LISTAR":
                        print(self.printable_stock())
                        pass
                    elif tok.type == "MOEDA":
                        coins = []
                        try:
                            while (tok.type != '.'):
                                tok = self.lexer.lexer.token()
                                if tok != None and tok.type == "TMOEDA":
                                    coins.append(tok.value)
                            print(self.add_coins(coins))
                        except Exception:
                            print("[ERRO] Sequência inválida")
                            print("[SUGESTAO] talvez falte um '.'")
                            break
                        pass
                    elif tok.type == "SELECIONAR":
                        try:
                            tok = self.lexer.lexer.token()
                            if tok.type == "ID":
                                print(self.buy(tok.value))
                            else:
                                print("[ERRO] Código não encontrado")
                        except Exception as e:
                            print(e)
                            print("[SUGESTAO] Formato de ID: [A-Z][A-Z0-9]+")
                            break
                        pass
                    elif tok.type == "SALDO":
                        print(self.printable_balance())
                        pass
                    elif tok.type == "SAIR":
                        print(self.exit())
                        return
                        pass
                    elif tok.type == "ADICIONAR":
                        # Extra por fazer
                        pass
            except Exception as e:
                print(e)
                print("HELP: LISTARC|LISTAR|MOEDA|SELECIONAR|SALDO|SAIR")
        return