# TPC3
## Gabriel Pereira a100891

## Enunciado

Este trabalho consiste em desenvolver em **[Python](https://www.python.org/)** um *somador ON/OFF*. Eis as regras do texto de input:

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

## Resolução

Há várias maneiras de atacar este problema. No programa `main.py` resolveu-se usar a combinação de *grupos de captura* e o operador '*|*' com a função `re.findall`, que irá devolver uma lista de tuplos, cada um deles com apenas o campo ordenado do match preenchido. Concatenando as listas basta apenas avaliar uma só no final do programa, ou no final de cada linha caso corra sem ficheiro de input.
Uma alternativa de resolução poderia ser o uso da ferramenta *lexer*, mas como foi dito nas aulas teóricas, seria como matar uma formiga com um canhão (ou algo semelhante).

## Testagem

A testagem deste programa foi feita através deste documento *Markdown*. Até agora, a aparição do símbolo '*=*' deverá devolver imprimir o resultado 100904 (3 + 100891 + 1 + 2 + 3 + 4 = 100904). Segue-se um capítulo de teste sob a forma de um link de imagem.

### Imagem

Aqui está uma imagem de uma calculadora

**![Calculador](https://i5.walmartimages.com/asr/f019d3ef-40c5-4dfd-a3c1-74f52b10690e_1.6eed2f21ec6dcb5f5b956731b5ee6439.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff)**

### Resultado
    100904
    100904
    302712
    1377497
    1378497
    1379497
    

## Execução

A execução deste TP pode ser realizada através do seguinte comando:
    
    `$>python3 main.py README.md > README_sum`