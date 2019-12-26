# LISTAS

## Anotações:

### Tipo de dado lista

+ Basicamente lista é um **valor** que contém diversos valores em uma sequência ordenada;
+ A *lista* é referida como valor, pois ela pode ser armazenada em uma variável ou passado para uma função, como qualquer outro valor;
+ A lista é constituída de um colchete de abertura( [ ), seus itens, vírgula para separar cada ítem e colchete fechamento( ] );
+ Um valor dentro de um lista é chamda de **item**;
+ Como as strings é possivel passar uma lista vazia, string vazia ' ', lista vazia [ ];
+ Um exemplo:
  ```exemplolista
  firstList = ['Hello', 'World', '2019']
  print(firstList)
  ```

### Obtendo valores individuais de uma lista por meio de índices

+ Após a criação de uma lista é possivel, chamar um item dela individualmente;
+ Um exemplo:
  ```itemlista
  firstList = ['Hello', 'World', '2019']
  print(firstList[0])
  ```
+ Simplesmente só é preciso chamar a variável a qual ela foi armazenada e entre colchetes armazenar o índice do item, ou seja, a posição do item;
+ Lembrando que a lista começa contando do zero;
+ Mais um exemplo de lista/indice:
  ```itemlista2
  helo = ['Snipe Elite', 'Resident Evil', 'Fallout', 'Mass Effect']
  print('U have:', len(helo), 'itens on your list!')
  print('First Item:', helo[0] )
  print('Second Item:', helo[1])
  print('Third Item:', helo[2] )
  print('Fourth Item:', helo[3])
  print('Fifth Item:', helo[4])

  # Observe que o len() conta o número de itens em uma lista;
  # Veja que a também uma mistura de valores string e intenger;
  # E também observer que a contagem começa do 0.
  ```
+ Listas também podem conter outros valores de lista, exemplo:
  ```itemlista3
  myList = [['Tomato', 'Potato', 'Lettuce'], ['Pork', 'Beef', 'Fish', 'Chicken']]
  print('This is your list', myList)
  print('U have:', len(myList), 'lists.')
  print('In the first list, u have:', len(myList[0]), 'itens.')
  print('In the second list, u have:', len(myList[1]), 'itens.')
  print('This is your first item on your first list:', myList[0][0])
  print('This is your first item on your second list:', myList[1][0])
  
  # Note que myList[Posição da lista][Posição do item na lista];
  ```

### Índices negativos

+ Embora os índices comecem com zero, podemos usar números negativos para começar a lista de formar invertida;
+ Exemplo:
  ```indiceinvertido
  myList = ['Tomato', 'Potato', 'Lettuce']
  print(myList[-1])
  print(myList[-2])
  
  # A saída vai ser:
  # Lettuce
  # Potato
  ```

### Obtendo sublistas com slices

+ O **slice** serve para nos dar acesso apenas a uma parte da lista;
+ Ele é representado por dois pontos, myList[0:2], o primeiro inteiro se refere ao ínicio e o segundo ao fim;
+ Exemplo:
  ```slice
  myList = [0,1,2,3,4,5,6,7,8,9,10]
  print(myList[0:6])

  # Saída:
  # [0, 1, 2, 3, 4, 5]
  ```
+ Como um atalho podemos deixar de especificar um dos inteiros:
  + Deixar de espicificar o primeiro inteiro ele será considerado um 0;
    ```sliceatalho
    myList = [0,1,2,3,4,5,6,7,8,9,10]
    print(myList[:6])

    # Saída:
    # [0, 1, 2, 3, 4, 5]
    ```
  + Deixar de especificar o segundo item da lista é o mesmo que usar toda a lista, ele terminará no final da lista;
    ```sliceatalho2
    myList = [0,1,2,3,4,5,6,7,8,9,10]
    print(myList[2:])

    # Saída:
    # [2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

### Alterando valores de uma lista usando índices

+ Do mesmo jeito que uma variável podemos alterar os valores do itens em uma lista;
+ Só que agora colocamos o indice ao lado da variável, exemplo:
  ```altValList
   myList = ['Tomato', 'Potato', 'Lettuce']
   print(myList)
   myList[1] = 'Mango'
   print(myList)
  
  # Saída:
  # ['Tomato', 'Potato', 'Lettuce']
  # ['Tomato', 'Mango', 'Lettuce']
  ```

### Concatenação e repetição de listas

+ Como os outros valores, string, integer e float, podemos concatenar listas usando usando operadores;
+ Os operados suportados são + e *;
+ Exemplos:
  ```concaList
  [1,2,3,4] + ['A', 'B', 'C']

  # Saída:
  # [1, 2, 3, 4, 'A', 'B', 'C']
  ```

  ```concaList2
  ['A', 'B', 'C'] * 2

  # Saída:
  # ['A', 'B', 'C', 'A', 'B', 'C']
  ```

### Removendo valores de listas usando instrução del

+ A instrução **del** simplesmente vai apagar um item da sua lista, todos os outros itens serão realocados para outro índice;
+ Exemplo:
  ```delList
  myList = ['Tomato', 'Potato', 'Lettuce']
  print(myList)
  del myList[1]
  print(myList)
  print(myList[1])

  # Saída:
  # ['Tomato', 'Potato', 'Lettuce']
  # ['Tomato', 'Lettuce']
  # Lettuce
  ```
+ O **del** pode ser usado em uma variável normal também, ele simplesmente vai deletar a variável;

## Trabalhando com listas

### Utilizando loops for com listas

+ Tecnicamente o loop for repete o bloco de código uma vez para cada valor de uma lista ou de um valor semelhante a uma lista;
+ Por exemplo:
  ```loopforlist
  print('Esse é o valor de range(4):')
  print(list(range(4)),'\n')

  print('Essa é a saida dele no for:')
  for i in range(4):
  	print(i)

  # Saída:
  #
  # Esse é o valor de range(4):
  # [0, 1, 2, 3] 
  #
  # Essa é a saida dele no for:
  # 0
  # 1
  # 2
  # 3
  ```
+ O que o for faz é executar sua variável "i" em todos os índices de uma lista;
+ Uma boa tecnica é usar o **range(len(nomeDaLista))**, pois além de executar todos os itens da lista, você ainda vai ter um índice para anexar ao seu código, exemplo:
  ```loopforlisttecnica
  names = ['Anna', 'Marie', 'Jezabel']

  for i in range(len(names)):
  	print(f'{i + 1}º: {names[i]}')

  # Saída:
  #
  # 1º: Anna
  # 2º: Marie
  # 3º: Jezabel
  ```

### Operadores in e not in

+ Podemos usa-los para determinar se um determinado valor está em uma lista;
+ Eles são usados em expressões e faz a associção de dois valores, o primeiro vai ser o valor a ser procurado e o segundo a lista que ele deve procurar;
+ As expressões irão retornar um valor booleano;
+ Exemplo:
  ```inNotInExample
  myList = ['Welcome', 'Hi', 'Hello']

  print('Hi' in myList)
  print('Hi' not in myList)

  # Saída:
  # True
  # False
  ```

### Truque da atribuição múltipla

+ Atribuição múltipla é um truque para atribuir uma variável única para um item em uma lista;
+ Exemplo:
  ```atribMult
  myList = ['Water', 'Apple', 'Pencil']

  fruit = myList[1]
  print(fruit)

  # Saída:
  # Apple
  ```
+ Exemplo 2:
  ```atribMult2
  myList = ['Marie', 'Apple', 'Pencil']

  human,fruit,objecT = myList

  print(human)
  print(fruit)
  print(objecT)

  # Saída:
  # Marie
  # Apple
  # Pencil
  ```
+ A quantidade de variáveis tem que ser **exatamente** iguais ao número total de itens na lista, *nem maior nem menor*.

## Operadores de atribuição expandidos

+ Com frequencia usamos variáveis para armazenar um valor e usarmos ela para alguma expressão;
+ Um exemplo de uso de variável é:
  ```opeExpand
  myVar = 10
  myVar = myVar + 1
  print(myVar)

  # Saída:
  # 11
  ```
+ Podemos simplicar essa expressão 'myVar = myVar + 1' usando os operadores de atribuição expandidos. Exemplo:
  ```opeExpand
  myVar = 10
  myVar += 1
  print(myVar)

  # Saída:
  # 11
  ```
+ Tipos de Operadores de atribuição expandidos:

  |Instrução de atribuição expandida|Instrução de atribuição equivalente|
  |                ---              |                 ---               |
  |          spam += 1              |        spam = spam + 1            |
  |          spam -= 1              |        spam = spam - 1            |
  |          spam *= 1              |        spam = spam * 1            |
  |          spam /= 1              |        spam = spam / 1            |
  |          spam %= 1              |        spam = spam % 1            |

+ O operador += pode fazer concatenação de strings e lista, exemplos:
  ```opeExpandStrings+=
  myVar = 'Hello'
  myVar += ' World'
  print(myVar)
  
  # Saída:
  # Hello World
  ```

  ```opeExpandList+=
  myVar = ['Hello', 'World', 'OK']
  myVar += ['Test']
  print(myVar)

  # Saída:
  # ['Hello', 'World', 'OK', 'Test']
  ```

+ O operador *= pode fazer a repetição de listas e strings, exemplos:
  ```opeExpandList*=
  myVar = ['Hello', 'World', 'OK']
  myVar *= 2
  print(myVar)

  # Saída:
  # ['Hello', 'World', 'OK', 'Hello', 'World', 'OK']
  ```

  ```opeExpandStrings*=
  myVar = 'Hello'
  myVar *= 2
  print(myVar)

  # Saída:
  # HelloHello
  ```

## Métodos

+ O método é parecido com a função exceto que ele chamado sobre um valor;
+ Um exemplo de método é o lista.index('item'), que é um método que vai trazer a posição de um item em uma lista;
+ Cada tipo de dado tem seu próprio conjunto de método.

### Encontrando um valor em uma lista com o método index()

+ Os valores de lista tem um método chamado **index()**, onde ele retorna o valor referente a posição do item na lista, exemplo:
  ```mtdIndex
  names = ['Anna', 'Marie', 'Jezabel']

  print(names.index('Marie'))
 
  # Saída:
  # 1
  ```
+ Caso o argumento passado no index não exista na lista, o python gerará uma exceção "ValueError: 'teste' is not in list";
+ E caso haja um item duplicado na lista ele retornará o valor do primeiro, exemplo:
  ```mtdIndex2
  names = ['Anna', 'Marie', 'Jezabel']

  print(names.index('Marie'))
 
  # Saída:
  # 1
  ```

### Adicionando valores a listas com os métodos append() e insert()

+ Podemos adicionar um item **no final de uma lista** usando o método append(), exemplo:
  ```mtdAppend
  names = ['mom', 'dad', 'sister']

  names.append('brother')
  print(names)

  # Saída:
  # ['mom', 'dad', 'sister', 'brother']
  ```
+ E também podemos adicionar um item **em qualquer índice de uma lista** usando insert(), exemplo:
  ```mtdInsert
  names = ['mom', 'dad', 'sister']

  names.insert(1,'brother')
  print(names)

  # Saída:
  # ['mom', 'brother', 'dad', 'sister']
  ```
+ Tenha em mente que o código **não é "lista = lista.append('string')"** e **sim "lista.append('string')"**, não é necessário chamar uma variável e armezenar o valor de retorno nela, pois o valor de retorno desses métodos é None. Exemplo:
  ```mtdInsertNone
  names = ['mom', 'dad', 'sister']

  names = names.insert(1,'brother')
  print(names)

  # Saída:
  # None
  ```
+ Métodos pertecem a um único tipo de dado. O append() e insert() são exclusivos dos valores do tipo lista;

### Removendo valores de lista remove()

+ O método remove() é usado para apagar um item na lista, exemplo:
  ```mtdRemove
  names = ['mom', 'dad', 'sister']

  names.remove('dad')
  print(names)

  # Saída:
  # ['mom', 'sister']
  ```
+ Se você tentar apagar um item que não existe, irá gerar um exceção "ValueError: list.remove(x): x not in list";
+ Se houver valores duplicados na lista apenas o primeiro vai ser apagado, exemplo:
  ```mtdRemove2
  names = ['mom', 'dad', 'sister', 'dad']

  names.remove('dad')
  print(names)

  # Saída:
  # ['mom', 'sister', 'dad']
  ```

### Ordenando os valores de uma lista com o método sort()

+ Usado para ordenar listas númericas e strings, exemplo:
  ```mtdSort
  names = ['d', 'b', 'c', 'a']
  numbers = [4, 2, 3 ,1]

  names.sort()
  numbers.sort()
  print(names)
  print(numbers)

  # Saída:
  # ['a', 'b', 'c', 'd']
  # [1, 2, 3, 4]
  ```
+ Podemos passar o argumento **reverse** para ordenar de forma inversa, exemplo:
  ```mtdSortReverse
  names = ['d', 'b', 'c', 'a']

  names.sort(reverse=True)
  print(names)

  # Saída:
  # ['d', 'c', 'b', 'a']
  ```
+ Listas que possuem diferentes tipos de dados como númericos(float e int) e string, gerará um exceção "TypeError: '<' not supported between instances of 'str' and 'int'";
+ O sort() usa a "ordem ASCII" e não a alfabética, então quando ele for ordenar letras maiúsculas serão postas na frente das letras minúsculas, exemplo:
  ```mtdSortASCII
  names = ['anne', 'Anne', 'Ying', '1']

  names.sort()
  print(names)
  
  # Saída:
  # ['1', 'Anne', 'Ying', 'anne']
  ```
+ Caso haja a necessidade de ordenar em ordem alfabética use o argumento "key=str.lower", exemplo:
  ```mtdSortAlfabetico
  names = ['anne', 'Anne', 'Ying', '1']

  names.sort(key=str.lower)
  print(names)

  # Saída:
  # ['1', 'anne', 'Anne', 'Ying']
  ```

## Tipos semelhantes a listas: strings e tuplas

+ Lista não são o único valor que representa uma sequencia ordenada de valores;
+ String é considerado também uma sequencia ordenada de caracteres;
+ Por exemplo na string podemos usar o 'in ou not in', loops com o for, indexação , etc;
+ Exemplo:
  ```stringlista
  name = 'banana'

  print(name[-2])
  print(name[0:4])
  print('a' in name)

  for i in name:
  	print(i)

  # Saída:
  # n
  # bana
  # True
  # b
  # a
  # n
  # a
  # n
  # a
  ```

### Tipos de dados mutáveis e imutáveis

+ Uma grande diferença entre string e lista, é que lista é um valor mutável e string imutável;
+ Mutável: ele pode ter valor adicionado, removido ou alterados;
+ Imutável: não pode ser alterado;
+ Se tentamos adicionar um valor à string dará um erro:
  ```stringerror
  name = 'pydhon'

  name[2] = 't'

  print(name)

  # Erro:
  # TypeError: 'str' object does not support item assignment
  ```
+ O "único jeito" de mutar uma string é criando uma nova variável e referenciando a antiga com o slice, exemplo:
  ```mutarstring
  name = 'pydhon'

  newName = name[0:2] + 't' + name[3:6]

  print(newName)

  # Saída:
  # python
  ```
+ Lembrando alterar a lista é diferente de renovar a variável, exemplo:
  ```renoVar
  name = ['pydhon', 'python', 'testing']

  name = ['C', 'C++', 'C#']

  print(name)

  # Saída:
  # ['C', 'C++', 'C#']
  ```
+ O código acima não está mutando a lista, e sim sobrepondo a variável 'name';
+ Um exemplo de mutação de variável:
  ```birlHoraDoShowPorra
  num = [0, 1, 2]

  for i in range(len(num) -1, -1, -1):
  	del num[i]

  for i in range(3, 6): 
  	num.append(i)

  print(num)

  # Saída:
  # [3, 4, 5]
  ```
+ Agora sim a lista foi modificada em vez de sobrescrita, foi apagada com o 'del' todos os itens e adicionado com o append() os outros itens.

### Tipo de dado tupla

+ Tupla é praticamente uma lista imutável;
+ Tuplas são declaradas quase do mesmo jeito das lista só que em vez de usar os colchetes, [], usamos parênteses, (), exemplo:
  ```tupla
  tupla = (0, 1, 2)

  print(tupla)
  del tupla[0]

  # Saída:
  # (0, 1, 2)
  # TypeError: 'tuple' object doesn't support item deletion
  ```
+ Caso queira adicionar apenas um valor na tupla, adicione uma vírgula após o item exemplo:
  ```tuplaumitem
  print(type((1)))
  print(type((1,)))

  # Saída:
  # <class 'int'>
  # <class 'tuple'>
  ```
+ Resumindo usaremos uma tupla quando a intenção é por um valor imutável no código.

### Convertendo tipos com as funções list() e tuple()

+ Assim como int(), str() e float() retornam um valor que condiz com seu tipo de dado, list() e tuple() são a mesma coisa, exemplo:
  ```convertlisttuple
  lisT = ['Water', 'Apple', 'Mango']
  print(lisT)
  print(type(lisT))

  lisT = tuple(lisT)
  print(lisT)
  print(type(lisT))

  # Saída:
  # ['Water', 'Apple', 'Mango']
  # <class 'list'>
  # ('Water', 'Apple', 'Mango')
  # <class 'tuple'>
  ```

## Referências

+ Como já visto é possivel armazenar valores em uma variável, exemplo:
  ```referenciaex
  spam = [0,1,2]
  che = spam
  spam = [3,4,5]
  print(spam)
  print(che)
  
  # Saída:
  # [3, 4, 5]
  # [0, 1, 2]
  ```
+ No código acima criamos a variavel *spam* com o valor [0,1,2] e atribuimos o valor de *spam* para *che* (che = spam), logo após na linha abaixo (spam = [3,4,5]) houve uma quebra de referência, pois como já dito que alterar uma lista é diferente renovar uma variável, então o valor inicial foi destruído perdendo assim a referência da lista inicial, e finalizando mostrando valores distintos.
+ Um exemplo de referência:
  ```referenciaex2
  spam = [0,1,2]
  che = spam
  spam.append(3)
  spam.append(4)
  spam.append(5)
  print(spam)
  print(che)

  # Saída:
  # [0, 1, 2, 3, 4, 5]
  # [0, 1, 2, 3, 4, 5]
  ```
+ Listas tem um comportamento diferente com relação à variável, pois não se atribui uma lista à uma variável e sim uma **referência** da lista, então basicamente no código acima acontece isso atribuimos uma *referência à lista* para a variável 'spam' e logo após passamos a mesma referência para a variável 'che';
+ *Referência é um valor que aponta para uma porção de dados*;

### Passando referências

+ Quando uma função é chamada, os valores dos argumentos são copiados para as variáveis referentes aos parâmetros,no caso da lista e do dicionário é feita uma copia da referência que será usada no parâmetro da função;
+ Exemplo:
  ```refefunc
  def test(a):
  	a.append('Hello')
    
  op = [1,2,3]
  test(op)
  print(op)

  # Saída:
  # [1, 2, 3, 'Hello']
  ```
+ Observe que uma **variável global** foi alterada através de um escopo local, isso acontece pois apesar de 'test()' e 'op' estarem em escopos diferentes eles conseguem fazer referência a mesma lista;
+ Um exemplo com um número inteiro aonde não referência:
  ```refefuncerro
  def test(a):
  	op = 4
    
  op = 1
  test(op)
  print(op)

  # Saída:
  # 1
  ```

### Funções copy() e deepcopy() do módulo copy

+ Essas funções são um bom jeito para "burlar" a referência de uma lista e impedir que o valor seja alterado, um exemplo usando a função *copy()* que é usada para criar copiar um valor:
  ```copy
  import copy

  list1 = [1, 2, 3]
  list2 = copy.copy(list1)
  list2[1] = 8
  print(list1)
  print(list2)

  # Saída:
  # [1, 2, 3]
  # [1, 8, 3]
  ```
+ Veja que não houve uma cópia da referência, o *copy()* apenas copiou o valor da 'list1', basicamente agora foi criada duas listas diferentes;
+ O *deepcopy()* copiará recursivamente a lista;




