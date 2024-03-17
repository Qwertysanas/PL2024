import sys
import re

trex = {
    "SKIP": r"[ \t\n]+",
    "COMMENT": r"\#.*",
    "KEYWORD": r"Select|From|Where",
    "ID": r"[a-zA-Z_][a-zA-Z_0-9]*",
    "OPERATOR": r"[<>=]?=|<|>",
    "BOOLOP": r"And|Or",
    "NUMBER": r"[+\-]?\d+",
    "WILDCARD": r"\*",
    "COMMA": r','
}

def tok(l):
    toks = {}
    for t, rex in trex.items():        
        if re.findall(rex, l):
            toks[t] = re.findall(rex, l)
    # retirar palavras reservadas dos identificadores
    if "ID" in toks.keys():
        toks["ID"] = [id for id in filter(lambda x: not re.match(trex["KEYWORD"] + r'|' + trex["BOOLOP"], x), toks["ID"])]
    return toks

def eval(toks):
    for k, v in toks.items():
        print(k, v)

def main(inp):
    if (len(inp) == 1):
        for l in sys.stdin:
            toks = tok(l)
            eval(toks)
        return
    else:
        file = open(inp[1])
        for l in file:
            toks = tok(l)
            eval(toks)
    return

if __name__ == "__main__":
    main(sys.argv)