# TPC1
## Gabriel Pereira a100891

## Enunciado

Este tpc tem como objetivo processar um ficheiro csv com a ausência do módulo **csv** em **[Python](https://www.python.org/)**.

## Resolução

Para ignorar a primeira linha do ficheiro usa-se a função *next* e para separar os campos em elementos de uma lista usa-se o método *split*.
Para gerar a lista de modalidades foi usado um *set* e um sort no fim para ordenar alfabeticamente. Para guardar em memória a lista dos indivíduos por escalão foi usado um *dicionário*.

## Execução

A execução deste TP pode ser realizada através do seguinte comando:
    
    $ python3 main.py README.md > emd.out