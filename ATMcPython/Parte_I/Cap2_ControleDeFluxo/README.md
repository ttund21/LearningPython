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

#### Condicionais

+ Instrução **if**:
  + O bloco após o if só será executado se a condição for True;
  + "Se(if) esta condição for verdadeira, execute o código que está no bloco.";
  + Em Python uma instrução if é construída das seguintes partes:
    1. Palavra-chave(if);
    2. Uma condição(True ou False);
    3. Dois-pontos(:);
    4. Um bloco de código indentado.
  + Exemplo:
    ```instrucaoif
    if name == 'Alice':
      print('Hi, Alice.')
    ```

+ Instrução **else**:
  + O **if** pode ser seguido pela uma instrnção **else**;
  + O **else** vai ser executado quando toda estrutura condicional for False;
  + "Se(if) esta condição for verdadeira execute este código; senão(else) execute aquele código.";
  + Usado para encerrar uma estrutura condicional;
  + Uma instrução **else** vai ser constituida de:
    + Palavra-Chave(else)
    + Dois-pontos(:)
    + Um bloco de código indentado.
    + Exemplo:
      ```instrucaoelse
      if name == 'Alice':
        print('Hi, Alice.')
      else:
        print('Hello, stranger.')
      ```

+ Instrução **elif**:
  + Usado quando quer executar mais de uma clausula(condição);
  + O **elif(else if)** vem sempre após um if ou outro elif;
  + Só será executado se a clausula anterior for False;
  + "Se a primeira condição for verdadeira, faça isso; Se segunda for verdadeira faça aquilo. Do contrário faça algo diferente."
  + Uma instrução **elif** será constituida de:
    + Palavra-chave(elif);
    + Uma condição;
    + Dois-pontos(:);
    + Um bloco de código indentado.
  + Exemplo:
      ```instrucaoelif
      if name == 'Alice':
    	  print('Hi, Alice')
      elif age < 12:
     	  print('You are not Alice, kiddo.')
      ```
 
  + A ordem das instruções **elif** é muito importante, um exemplo:
      ```ordemelif
      if name == 'Alice':
      	  print('Hi, Alice.')
      elif age < 12:
    	  print('You are not Alice, kiddo.')
      elif age > 100:
    	  print('You are not Alice, grannie.')
      elif age > 2000: # Esse bloco NUNCA será executado, pois o bloco acima sempre vai ser True, ouseja, qualquer numero acima é maior que 100, então 'age > 100' será sempre True.
    	  print('Unlike you, Alice is not an undead, immortal vampire.')
      ```

#### Repetição

+ Instrução de loop **while**:
  + Usado apra repetir um código repetidamente;
  + O código na cláusula **while** ficará executando sempre que a instrução **while** for True, após se tornar False parará de executar;
  + Uma instrução **while** será constituida de:
    + Palavra-chave(while);
    + Uma condição;
    + Dois-pontos(:);
    + Um bloco de linha identado.
  + Exemplo:
    ```instrucaoloopwhile
    username = ''

    while username != 'Alice':      
        print('\nUsername:')
        username = input()
        if username != 'Alice':
            print('\nWrong Username')
    print('\nAccess Granted!')

    # Enquanto a variavel 'username' for diferente de 'Alice' a instrução while será avaliada como True e executará seu bloco repetidamente;
    # Até que 'username' seja igual a 'Alice' ai a expressão 'Alice != Alice' será False, finalizando o loop e executando o proximo bloco. 
    ```

+ Instrução **break**:
  + Um atalho para finalizar previamente um loop;
  + Se a instrução **break** for executada o loop será finalizado imediatamente;
  + A instrução é apenas constituida da palavra-chave **break**;
  + Exemplo:
    ```intrucaobreak
    count = ''
    i = 0
    print("Let's count.")

    while True:
        i = i +1
        print(i)
        print('Do u want stop it? y, n')
        count = input()
        if count == 'y':
            break
    print('Thank you')

    # Aqui foi criado uma loop infinito definindo que o while vai ser sempre True;
    # Depois foi instruido que se o count for igual a y, use a instrução break;
    # Então após o break for executado o loop é quebrado e o proximo bloco é executado.
    ```

+ Instrução **continue**:
  + São usadas dentro loop;
  + Usada para retornar o loop para o inicio;
  + Constituida apenas da palavra-chave **continue**;
  + Exemplo:
    ```instrucaocontinue
    name = ''
    password = ''

    while True:
        print('Who are u?')
        name = input()
        if name != 'Joe':
            continue
        print('Hey, Joe. What is the password?')
        password = input()
        if password == 'swordfish':
            break
    print('Access Granted')

    # Aqui foi add um loop infinito;
    # Foi definido que enquando a variavel 'name' for diferente de 'Joe' será executado a instrução 'continue' e o loop voltará pro inicio;
    # O código so será finalizado se e somente se name == Joe e password == swordfish.
    ```

+ Loop **for**:
  + Sua grande diferença para o **while** é que ele não vai uma condição booleana;
  + É um loop que é executado através de uma sequêcia,ou seja, uma lista, um tupla, dicionario e etc;
  + Praticamente ele vai fazer um contagem de 'itens' e gerar uma repetição, exemplo:
    ```forexample
    print('Banana has 6 letters!')

    for i in 'banana':
    	print(f'{i} I like apple!')
    # Saída:

    # Banana has 6 letters!
    # b I like apple!
    # a I like apple!
    # n I like apple!
    # a I like apple!
    # n I like apple!
    # a I like apple!

    # Veja que o for vai fazer a contagem de 'itens';
    # Que nesse caso já que 'banana' não é uma lista, ou algo do tipo, ele vai contar por letras.
    ```
  + Mesma coisa acontece com o range(), quando o o gera ele vai gerar uma "lista" e o for vai contar esses itens, exemplo:
    ```forexample2
    print('This is the range output:')
    print(list(range(6)), '\n')

    for i in range(6):
    	print(f'{i} I like apple!')
    ```

+ Equivalencia nas instruções loops:
  + Será mostrado dois códigos que irá fazer uma somatória de 0 a 100;
  + **for in range()**:
    ```equifor
    total = 0

    for i in range(101):
    	total = total + i

    print('Soma de 0 a 100 é igual a: ' + str(total))
    ```
  + **while**:
    ```equiwhile
    i = 0
    total = 0

    while i < 100:
    	i = i + 1
    	total = total + i
    
    print(total)
    ```
 
+ Função **range()**:
  + Basicamente quando chamado ele gerará uma "lista" com o respectivos argumentos passados;
  + Algumas funções podem ser chamadas com argumento seperado por virgula;
  + Apenas deve ser passado numeros inteiros no argumento;
  + Exemplo:
    ```exrange2
    for i in range(0, 10):
    	print(i)

    # Saida: 0 1 2 3 4 5 6 7 8 9
    # O primeiro argumento, 0, será o inicio;
    # O segundo argumento, 10, será o fim.
    ```
  + Também pode ser passada com 3 argumentos.
  + Exemplos:
    ```exrange3
    for in range(0, 10, 2):
    	print(i)

    # Saida: 0 2 4 6 8   
    # O primeiro argumento, 0, será o inicio;
    # O segundo argumento, 10, será o fim;
    # O terceiro argumento, 2, será a quantidade somada por loop. 
    ```
    ```exrange3_2
    for i in range(10, -1, -1):
    	print(i)
    
    # Saida: 10 9 8 7 6 5 4 3 2 1 0
    ```

### Importando Módulos

+ Instrução **import**:
  + No python existe um conjunto de módulos(programas) chamados de biblioteca-padrão;
  + Esses módulos podem ser chamados em seu código usando a instração **import**;
  + Pode ser encontrado uma lista de módulos nas [Docs do Python](https://docs.python.org/3/py-modindex.html)
  + É constituída por:
    + Palavra-chave **import**;
    + Nome do módulo;
    + Opcional, mais nomes de módulos desde que sejam separados por vírgula.
  + Um exemplo usando o módulo [random](https://docs.python.org/3/library/random.html#module-random):
    ```instrucaoimport
    import random
   
    for i in range(10):
    	print(random.randint(1,100))
    ```
  + Um exemplo usando 2 módulos:
    ```instrucaoimport2
    import random, math
   
    number = random.randint(10, 100)
    print('Random number: ' + str(number))
    resp = math.sqrt(number)
    print('Square root of the random number: ' + str(resp))
    ```

+ Instrução **from import**:
  + Usado para deixar mais "enxuto" o código importando apenas partes de um módulo;
  + Composta por:
    + Palavra-chave **from** seguida por nome do módulo;
    + Palavra-chave **import** seguida por uma função do módulo.
  + Exemplo de uso:
  ```instrucaofromimport
  from random import randint
   
  print(randint(1, 100))
  ```
  + Uma adendo, renomeando recursos importados usando o **as**;
  + Exemplo:
  ```instrucaofromimportas
  from random import randint as d
   
  print(d(1, 100))
  ```
  

