import json

stock = [
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.6},
    {"cod": "A27", "nome": "sumo 0.33L", "quant": 4, "preco": 1.2},
    {"cod": "A29", "nome": "iogurte líquido", "quant": 7, "preco": 0.6},
    {"cod": "A30", "nome": "café", "quant": 9, "preco": 0.5},
    {"cod": "A31", "nome": "leite chocolatado", "quant": 10, "preco": 0.6},
    {"cod": "B24", "nome": "kitkat", "quant": 5, "preco": 0.7},
    {"cod": "B25", "nome": "lanche misto", "quant": 2, "preco": 1.0},
    {"cod": "B26", "nome": "bolacha maria", "quant": 3, "preco": 0.5},
    {"cod": "B28", "nome": "batatas fritas", "quant": 6, "preco": 0.8},
    {"cod": "B32", "nome": "pastilha elástica", "quant": 1, "preco": 0.3}
]

file = open("stock.json", 'w')
file.write(json.dumps(stock))
file.close()