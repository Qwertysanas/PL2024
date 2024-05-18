#!/usr/bin/env python

import sys
from lexer import Lexer
from parser import Parser

def main(inp):

    lexer = Lexer()
    parser = Parser(lexer)
    
    if (len(inp) == 1):
        for l in sys.stdin:
            parser.parse(l)
    else:
        file = open(inp[1])
        f = ""
        for l in file:
            f += l
        parser.parse(f)
        file.close()

if __name__ == "__main__":
    main(sys.argv)