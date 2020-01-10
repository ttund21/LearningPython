# Função de “lista para dicionário” para o inventário de jogo de fantasia

+ Suponha que os despojos de um dragão vencido seja representado como uma lista de strings como esta:
  ```lista
  dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
  ```
+ Crie uma função chamada addToInventory(inventory, addedItems), em que o parâmetro inventory seja um dicionário representando o inventário do jogador (como no projeto anterior) e o parâmetro addedItems seja uma lista como dragonLoot. A função addToInventory() deve retornar um dicionário que represente o inventário atualizado. Observe que a lista addedItems pode conter vários itens iguais. Seu código poderá ser semelhante a:
  ```addToInventory
  def addToInventory(inventory, addedItems):
  	# seu código deve ser inserido aqui
  inv = {'gold coin': 42, 'rope': 1}
  dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
  inv = addToInventory(inv, dragonLoot)
  displayInventory(inv)
  ```
+ O programa anterior (com sua função displayInventory() do projeto anterior) apresentará a saída a seguir:
  ```exit
  Inventory:
  45 gold coin
  1 rope
  1 ruby
  1 dagger
  Total number of items: 48
  ```
