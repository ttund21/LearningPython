# Básico Sobre o Python

## Anotações:

+ Tipos de operadores em Python:

| Operador |     Operação     | Exemplo  |  Resposta |
|    ---   |        ---       |    ---   |    ---    |
|    **    |    Exponencial   |  2 ** 3  |     8     |
|     %    |       Resto      |  22 % 8  |     6     |
|    //    |  Divisão Inteira |  22 // 8 |     2     |
|    /     |      Divisão     |  22 / 8  |    2.75   |
|    *     |   Multiplicação  |   3 * 5  |     15    |
|    -     |     Subtração    |   5 - 2  |     3     |
|    +     |      Adição      |   2 + 2  |     4     |

+ Tipos de Dados:

| Tipo de dado  |      Exemplo      |
|     ---       |        ---        |
|  Integer(int) |     -1, 0, 1      |
|  Float        |   -1.0, 0.0, 1.0  |
|  Strings(str) |  'Hello', 'World' |

+ Concatenação e repetiçaõ de strings:

|     Exemplo     |  Resposta  |
|       ---       |     ---    |
| 'Alice' + 'Bob' |  AliceBob  |
| 'Alice' * 2     | AliceAlice |

+ Declarando uma variavel:

```declvariavel
>>> nome_variavel = 2
>>> print(nome_variavel)
2
```

+ Nomes validos e invalidos para variaveis:
  1. O nome pode ser constituído somente de uma palavra.
  2. Somente letras, números e o caractere underscore (_) podem ser usados.
  3. O nome não pode começar com um número.

|  Nomes válidos de variaveis  |               Nomes inválidos de variáveis                   |
|             ---              |                            ---                               |
|           balance            |  current-balance (hifens não são permitidos)                 |
|        currentBalance        |  current balance (espaços não são permitidos)                |
|        current_balance       |  4account (não pode começar com um número)                   |
|           _spam              |  42 (não pode começar com um número)                         |
|           SPAM               |  total_$um (caracteres especiais como $ não são permitidos)  |
|         account4             |  'hello' (caracteres especiais como ' não são permitidos)    |

+ firstprogram.py

```firstprogram.py
# Este programa diz hello e pergunta o meu nome.
print('Hello world!')# usado para exibir uma informação na tela.
print()
print('What is your name?') # pergunta o nome.
myName = input() # o input() vai receber uma string.
print('It is good to meet you, ' + myName)
print()
print('The length of your name is:' + ' ' + str(len(myName))) # a função 'len()' conta o número de caracteres de uma string, ela é considerada um valor inteiro.
print()
print('What is your age?') # pergunta a idade.
myAge = input()
print()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # str(int(myAge) + 1), vai pegar a variavel 'myAge' vai transformar em inteiro para somar com o 1 e depois vai voltar para string para concatenar com as outras strings.

# str(): transformara o valor recebido em string
# float(): transformara o valor recebido em float
# int(): transformara o valor recebido em inteiro, sempre que for usado em um valor do tipo float, irá arredonda-lo para baixo.
```

