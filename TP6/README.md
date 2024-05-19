# TPC6
## Gabriel Pereira a100891

## Enunciado

Este trabalho consiste em desenvolver uma gramática para um *parser recursivo descendente* da seguinte linguagem:

        ? a                     # Ler var a
        ! a * 2 + 7             # imprimir
        b = (a + 3) * 4 - 5     # guardar na var b
        ! a + b
        
## Resolução

Apesar de a resolução consistir apenas na escrita de uma gramática, foi implementada fisicamente em python para testar.

Aqui está a gramática escrita com os LA's calculados:

        T = {'+', '-', '*', '/', '(', ')', '=', '!', '?', ID, NUMBER, NL}

        N = {Z, code, codeop, op, expr, infix6, term, infix7, factor}

        Z       -> code             LA = {'!', '?', ID}

        code    -> op codeop        LA = {'!', '?', ID} U {$}
                | ε

        codeop  -> NL code          LA = NL U {$}
                | ε
        
        op      -> '!' expr         LA = {'!'}
                | '?' ID            LA = {'?'}
                | ID '=' expr       LA = {'ID'}

        expr    -> term infix6      LA = {NUMBER, ID, '('}
        
        infix6  -> '+' expr         LA = {'+'}
                | '-' expr          LA = {'-'}
                | ε                 LA = {$, NL, ')'}

        term    -> factor infix7    LA = {NUMBER, ID, '('}
        
        infix7  -> '*' term         LA = {'*'}
                | '/' term          LA = {'/'}
                | ε                 LA = {'+', '-', $, NL, ')'}
        
        factor  -> NUMBER           LA = {NUMBER}
                | ID                LA = {ID}
                | '(' expr ')'      LA = {'('}

## Execução

Para verificar que a gramática funcionava foi escrito em **[Python](https://www.python.org/)** um script que analisa sintaticamente frases desta linguagem. A execução deste TP pode ser realizada através do seguinte comandos:
    
    $ ./main.py                 # para interpretar linha a linha
    $ ./main.py exemplo.txt     # para ler um ficheiro:
    $ cat parser.out            # para ver o output
