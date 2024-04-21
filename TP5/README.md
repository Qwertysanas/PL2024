# TPC5
## Gabriel Pereira a100891

## Enunciado

Este trabalho consiste em desenvolver em **[Python](https://www.python.org/)** uma *máquina de venda*. Em anexo nesta pasta está o documento **[Enunciado](./enunciado.pdf)** que contém as regras deste TPC.

## Resolução

Foi criado um objeto *Lexer* em `lexer.py` cujo propósito é realizar a análise léxica a ser usada neste contexto. A máquina *MaquinaV* localizada em `maq.py` contém a lógica de funcionamento de uma máquina de vending mais funções auxiliares à resolução do problema. No programa `main.py` é ligada a máquina ao *standard input* onde o cliente irá interagir e executar as operações pretendidas.

## Execução

Para começar o programa principal:

    $ python3 main.py

Podem ser usados vários comandos como:

    MOEDA 50c 20c
    LISTAR
    SELECIONAR A23
    MOEDA 50c, 20c.
    LISTARC
    SELECIONAR A13
    SELECIONAR A23
    SALDO
    SAIR

Nem todos os comandos fornecidos acima são válidos de modo a mostrar o tratamento de erros da aplicação. Para regenerar a base de dados que a máquina de venda usa basta executar `stock.py`:

    $ python3 stock.py
