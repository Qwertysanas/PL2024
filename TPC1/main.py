import math

NOME = 3
SOBRENOME = 4
IDADE = 5
MODALIDADE = 8
RESULTADO = -1

f = open("emd.csv")
next(f)

mds = set()
apt = 0
inapt = 0
escs = {2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : [], 10 : []}

for line in f:
    it = line.split(',')
    
    k = math.floor(int(it[IDADE]) / 5)
    escs[k].append(it[NOME] + ' ' + it[SOBRENOME])
    
    mds.add(it[MODALIDADE])
    
    if it[RESULTADO] == "true\n":
        apt += 1
    else:
        inapt += 1
    
aptp = round(apt/(apt + inapt) * 100, 2)
inaptp = 100 - aptp

print("modalidades:", sorted(mds))
print("aptos:", aptp, "%")
print("inaptos:", inaptp, "%")
print("escaloes:")
for k in escs:
    esc = f"[{(k * 5)}-{k * 5 + 4}]"
    print(esc, '-', sorted(escs[k]))
    
