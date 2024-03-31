# TPC4
## Gabriel Pereira a100891

## Enunciado

Este trabalho consiste em desenvolver em **[Python](https://www.python.org/)** um **analisador léxico** para uma linguagem de query, na qual se podem escrever frases do género:

    Select id, nome, salario From empregados Where salario >= 820

## Resolução

Para atingir o objetivo do enunciado foi usada a ferramenta **Lex.py**, analisador léxico do módulo **[Ply](https://www.dabeaz.com/ply/ply.html)**.

## Testagem

Eis algumas linhas que foram usadas na testagem do programa:

    Select id, nome, salario From empregados Where salario >= 820
    Select * From empregados Where id >= 100 And id < 200 #comentário
    Select * From empregados Where balance == -1000 ### comentários começam com múltiplas ocorrências do char '#'
    Select id, nome From empregados Where salario < 2000
    Select nome, apelido, idade From empregados Where id == 200 Or salario > 1000 Or morada == "Rua Mouzinho Silveira"
    Select * From encomendas Where peso > 50

## Execução

A execução deste TP pode ser realizada através do seguinte comando:
    
    $ sed -n 18,23p README.md | python3 main.py > README.tks