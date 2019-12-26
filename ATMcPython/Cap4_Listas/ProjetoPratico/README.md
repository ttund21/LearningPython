# Projetos práticos
Para exercitar, escreva programas que executem as tarefas a seguir.

## Código para vírgulas

+ Suponha que você tenha um valor de lista como:
  ```codvirg
  spam = ['apples', 'bananas', 'tofu', 'cats']
  ```
+ Crie uma função que aceite um valor de lista como argumento e retorne uma string com todos os itens separados por uma vírgula e um espaço, com and inserido antes do último item. Por exemplo, se passarmos a lista spam anterior à função, 'apples, bananas, tofu, and cats' será retornado. Porém sua função deverá ser capaz de trabalhar com qualquer valor de lista que ela receber.


## Grade para imagem composta de caracteres

+ Suponha que você tenha uma lista de listas em que cada valor das listas internas seja uma string de um caractere como:
  ```imagem
  grid = [['.', '.', '.', '.', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['.', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.']]
  ```
+ Podemos pensar em grid[x][y] como sendo o caractere nas coordenadas x e y de uma “imagem” desenhada com caracteres textuais. A origem (0, 0) estará no canto superior esquerdo, as coordenadas x aumentam para a direita e as coordenadas y aumentam para baixo.
+ Copie o valor da grade anterior e crie um código que a utilize para exibir a imagem:
  ```imagem2
  ..OO.OO..
  .OOOOOOO.
  .OOOOOOO.
  ..OOOOO..
  ...OOO...
  ....O....
  ```
+ Dica: você deverá usar um loop em um loop para exibir grid[0][0], em seguida grid[1][0], grid[2][0] e assim por diante, até grid[8][0]. Com isso, a primeira linha estará concluída, portanto exiba uma quebra de linha. Em seguida, seu programa deverá exibir grid[0][1], depois grid[1][1], grid[2][1] e assim por diante. O último item que seu programa exibirá é grid[8][5].
+ Além disso, lembre-se de passar o argumento nomeado end para print() se não quiser que uma quebra de linha seja exibida automaticamente após cada chamada a print().
