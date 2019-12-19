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
