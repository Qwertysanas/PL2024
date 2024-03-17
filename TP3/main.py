import sys
import re

res = 0
toks = []
on = True

rex = r"([\-+]?[0-9]+)|(on)|(off)|(=)"

def tok(l):
    toks.extend(re.findall(rex, l))

def eval():
    global res, on
    while toks:
        n, o, f, e = toks.pop(0)
        if n and on:
            res += int(n)
        elif o:
            on = True
        elif f:
            on = False
        elif e:
            print(res)

def main(inp):
    if (len(inp) == 1):
        for l in sys.stdin:
            tok(l)
            eval()
    else:
        file = open(inp[1])
        for l in file:
            tok(l)
        eval()
    return

if __name__ == "__main__":
    main(sys.argv)