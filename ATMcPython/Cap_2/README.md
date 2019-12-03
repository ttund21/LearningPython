# Controle De Fluxo

## Anotações:

+ Valores booleanos:

  + É um tipo de dados que diferente da string, integer e float, possui apenas dois valores que é o True e False. Serve para mostrar se dada expressão é verdadeira ou falsa.

+ Operadores de Comparação:

|  Operador  |    Significado     |     Valores       |
|     ---    |        ---         |       ---         |
|     ==     |  Igual a           |  str, int, float  |
|     !=     |  Diferente de      |  str, int, float  |
|     <      |  Menor que         |  int, float       |
|     >      |  Maior que         |  int, float       |
|     <=     |  Menor ou Igual a  |  int, float       |
|     >=     |  Maior ou Igual a  |  int, float       |

### Operadores Booleanos
**And, or e not**

+ **Operadores Booleanos Binários(and e or):**

  + Operadores binários sempre vai receber apenas dois valores booleanos, ou seja, ele sempre vai fazer um comparativo entre valores.

+ And:

|     Expressão     |  Avaliada como  |
|        ---        |       ---       |
|  True and True    |      True       |
|  True and False   |      False      |
|  False and True   |      False      |
|  False and False  |      False      |

**Obs: No 'and' os dois valores tem que ser verdadeiros para gerar o valor True.**

+ Or:

|     Expressão     |  Avaliada como  |
|        ---        |       ---       |
|  True or True     |      True       |
|  True or False    |      True       |
|  False or True    |      True       |
|  False or False   |      False      |

**Obs: No 'or' apenas um dos valores precisa ser verdadeiro para gerar o valor True.**

+ **Operador Not:**

  + Simplesmente gera o valor oposto do booleano avaliado.

|     Expressão     |  Avaliada como  |
|        ---        |       ---       |
|      not True     |      False      |
|      not False    |      True       |
|  not not True     |      True       |

### Misturando operadores booleanos e de comparação

+ Exemplos:

  + (5 != 5) and (6 == 6.0) // False
  + (5 != 5) or (6 == 6.0) //  True
  + not (2 + 3 == 5.0) and not not (2.5 + 2.5 != 5) // False

### Elementos do controle de fluxo

+ Condição
  + São sempre avaliadas em True ou False;
  + Estão sempre determinando uma condição. Ex: (5 != 5) and (6 == 6.0);
  + Ex: Está chovendo? False.

+ Blocos de código
  + Linhas de código Python podem ser agrupadas em blocos;
  + Pode-se reconhecer aonde começa e termina um bloco de código apenas pela identação;
  + Há três regras para blocos:
    1. Os blocos começam no local em que a identação aumenta;
    2. Os blocos podem conter outros blocos; 
    3. Os blocos terminam no local em que a indentação se reduz a zero ou na indentação do bloco que o contém.
  + Exemplo:
    ```blocodecodigo
     if name == 'Mary':
       print('Hello Mary')  # Primeiro Bloco
     if password == 'swordfish':
       print('Access granted.') # Segundo Bloco
     else:
       print('Wrong password.') # Terceiro Bloco 
    ```

### Instrução de controle de fluxo

+ Instrução **if**:
  + O bloco após o if só será executado se a condição for True;
  + "Se(if) esta condição for verdadeira, execute o código que está no bloco.";
  + Em Python uma instrução if é construída das seguintes partes:
    1. Palavra-chave(if);
    2. Uma condição(True ou False);
    3. Dois pontos(:);
    4. Um bloco de código indentado.
  + Exemplo:
    ```instrucaoif
    if name == 'Alice':
      print('Hi, Alice.')
    ```

+ Instrução **else**:
