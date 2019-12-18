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


