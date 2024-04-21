# TPC2
## Gabriel Pereira a100891

## Enunciado

Este trabalho consiste em desenvolver em **[Python](https://www.python.org/)** um pequeno conversor de MarkDown para *HTML* para os elementos descritos na *Basic Syntax* apresentada na *Cheat Sheet* do **[Markdown Guide](https://www.markdownguide.org/cheat-sheet/)**.

## Resolução

O método usado na resolução deste trabalho foi o uso de **grupos de captura** nas expressões regulares e **funções lambda** de modo a substituir os segmentos pretendidos por formatação *HTML*. Uma alternativa às funções anónimas é selecionar os grupo de captura com **números escapados por barra**.

## Testagem

A testagem deste programa foi feita através deste documento *Markdown*. Seguem-se capítulos que especificam certas regras do formato.

### Listas

Segundo o guia de sintaxe básica uma lista **começa com o número 1**.

1. Primeiro item
2. Segundo item com **bold**
3. Terceiro item com *itálico*

Outro exemplo:

1. Isto também
3. é
100. uma
1. lista

### Imagens

Aqui apresenta-se a prática de uso de **regular expressions** com a ferramenta **[Regex101](https://regex101.com/)**

![Exemplo1](https://d2h1bfu6zrdxog.cloudfront.net/wp-content/uploads/2022/04/img_625491e9ce092.png)

## Execução

A execução deste TP pode ser realizada através do seguinte comando:

    $ python3 main.py README.md > README.html
